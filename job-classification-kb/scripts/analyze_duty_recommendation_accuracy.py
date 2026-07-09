#!/usr/bin/env python3
"""驗證職類推薦(職類推薦1~10) vs 現有掛載職類(duty0~4)精準度。
讀 MD 資料層(不回讀 Excel)，依 tCodeDutyNM 階層樹(_dutynm_tree.json)分大類/中類統計。
輸出：報告 md 由呼叫端另外組裝，本腳本只印最終彙整結果(JSON 存檔 + 少量 stdout 摘要)。
"""
import json
import re
from collections import defaultdict, Counter

ROOT = '/home/user/main/job-classification-kb'
DATA_MD = f'{ROOT}/tcode/data_職缺名稱_dutyMapping.md'
TREE_JSON = f'{ROOT}/scripts/_dutynm_tree.json'
OUT_JSON = f'{ROOT}/scripts/_duty_accuracy_stats.json'

tree = json.load(open(TREE_JSON, encoding='utf-8'))
leaf2cat = {}
for major, mids in tree.items():
    for mid, leaves in mids.items():
        for leaf in leaves:
            leaf2cat[leaf] = (major, mid)


def parse_rows(path):
    with open(path, encoding='utf-8') as f:
        lines = f.readlines()
    header = None
    data_start = None
    for i, l in enumerate(lines):
        if l.startswith('| 職缺名稱'):
            header = [c.strip() for c in l.strip().strip('|').split('|')]
            data_start = i + 2
            break
    for l in lines[data_start:]:
        l = l.rstrip('\n')
        if not l.startswith('|'):
            continue
        cells = [c.strip() for c in l.strip('|').split('|')]
        if len(cells) != len(header):
            continue
        yield dict(zip(header, cells))


# ---- feature flags for qualitative failure analysis ----
DECO_RE = re.compile(r'[◎★☆【】()（）※□▲△○]')
SLASH_RE = re.compile(r'[／/]')
DIGIT_RE = re.compile(r'\d')
ASCII_RE = re.compile(r'[A-Za-z]')
FUNCTION_TAIL_SUFFIXES = ('助理', '專員', '主管', '人員', '工程師', '經理', '代表', '師', '員')


def features(title):
    f = {}
    f['deco'] = bool(DECO_RE.search(title))
    f['slash_multi'] = bool(SLASH_RE.search(title))
    f['digit'] = bool(DIGIT_RE.search(title))
    f['ascii'] = bool(ASCII_RE.search(title))
    f['short_le3'] = len(title) <= 3
    f['long_ge10'] = len(title) >= 10
    f['generic_tail'] = title.endswith(FUNCTION_TAIL_SUFFIXES)
    return f


# ---- main pass ----
cat_stats = defaultdict(lambda: Counter())          # (major, mid) -> level counter
unmapped_leaves = Counter()                          # duty0 leaf not found in tree
level_counter = Counter()                            # global
feature_miss = defaultdict(lambda: {'miss': 0, 'total': 0})
mismatch_examples = defaultdict(list)                # feature -> [(title, duty0, top3_recs)]
seen_titles_for_examples = set()
recoverable_examples = []                            # 正解卡在推薦6~10名(前5名看不到)的案例
seen_recoverable = set()

n_rows = 0
n_no_duty0 = 0

for row in parse_rows(DATA_MD):
    n_rows += 1
    title = row['職缺名稱']
    duties = [row.get(f'duty{i}', '') for i in range(5)]
    duties = [d for d in duties if d]
    recs = [row.get(f'職類推薦{i}', '') for i in range(1, 11)]
    recs = [r for r in recs if r]

    if not duties:
        n_no_duty0 += 1
        continue
    primary = duties[0]  # duty0，僅用來決定該列歸屬哪個大類/中類(分組用)

    # 命中判定：duty0~duty4(現有全部 5 格) 任一格 命中 職類推薦1~10 任一項即算，
    # 不要求順序/名次對齊，只看最先出現的名次落在哪個桶(top1/top3/top5/top10)。
    rank = None
    for idx, r in enumerate(recs):
        if r in duties:
            rank = idx + 1
            break

    cat = leaf2cat.get(primary)
    if cat is None:
        unmapped_leaves[primary] += 1

    if rank is not None:
        if rank <= 1:
            lvl = 'top1'
        elif rank <= 3:
            lvl = 'top3'
        elif rank <= 5:
            lvl = 'top5'
        else:
            lvl = 'top10'
        is_miss = False
    else:
        rec_cats = [leaf2cat.get(r) for r in recs]
        if cat and any(rc and rc[1] == cat[1] for rc in rec_cats):
            lvl = '沾邊_中類'
        elif cat and any(rc and rc[0] == cat[0] for rc in rec_cats):
            lvl = '沾邊_大類'
        else:
            lvl = '無關'
        is_miss = True

    level_counter[lvl] += 1
    if cat:
        cat_stats[cat][lvl] += 1

    # 收集「正解卡在推薦6~10名」的案例：命中(rank)但落在前5名之外，
    # 前端只顯示前5筆 → 這格答案使用者實際看不到，是順序優化的回收標的。
    if rank is not None and rank > 5 and title and title not in seen_recoverable and len(seen_recoverable) < 3000:
        hit_leaf = recs[rank - 1]
        recoverable_examples.append({
            'title': title,
            'hit_leaf': hit_leaf,          # 命中的正解(卡在第 rank 名)
            'hit_rank': rank,
            'top5_recs': recs[:5],         # 前端實際會顯示的前5筆(把正解擠掉的內容)
        })
        seen_recoverable.add(title)

    if not title:
        continue

    feats = features(title)
    for fname, fval in feats.items():
        if fval:
            feature_miss[fname]['total'] += 1
            if is_miss:
                feature_miss[fname]['miss'] += 1
    feature_miss['__all__']['total'] += 1
    if is_miss:
        feature_miss['__all__']['miss'] += 1

    if is_miss and title not in seen_titles_for_examples and len(seen_titles_for_examples) < 4000:
        for fname, fval in feats.items():
            if fval and len(mismatch_examples[fname]) < 8:
                mismatch_examples[fname].append({
                    'title': title,
                    'duty0': primary,
                    'top3_recs': recs[:3],
                    'level': lvl,
                })
        if lvl == '無關' and len(mismatch_examples['無關_all']) < 15:
            mismatch_examples['無關_all'].append({
                'title': title,
                'duty0': primary,
                'top3_recs': recs[:3],
            })
        seen_titles_for_examples.add(title)

# ---- assemble output ----
def pct(n, d):
    return round(100 * n / d, 2) if d else None


cat_table = []
for (major, mid), counter in cat_stats.items():
    n = sum(counter.values())
    top1 = counter['top1']
    top3_cum = top1 + counter['top3']
    top5_cum = top3_cum + counter['top5']
    only_6_10 = counter['top10']          # 正解只出現在推薦6~10名(前5名看不到)
    top10_cum = top5_cum + only_6_10
    zb_mid = counter['沾邊_中類']
    zb_major = counter['沾邊_大類']
    irrelevant = counter['無關']
    cat_table.append({
        'major': major, 'mid': mid, 'n': n,
        'top1_pct': pct(top1, n), 'top3_cum_pct': pct(top3_cum, n),
        'top5_cum_pct': pct(top5_cum, n), 'top10_cum_pct': pct(top10_cum, n),
        'recoverable_6_10_pct': pct(only_6_10, n),   # 順序優化可回收比例
        'zhanbian_mid_pct': pct(zb_mid, n), 'zhanbian_major_pct': pct(zb_major, n),
        'irrelevant_pct': pct(irrelevant, n),
    })
cat_table.sort(key=lambda r: -r['n'])

feature_table = []
baseline_miss = feature_miss['__all__']['miss']
baseline_total = feature_miss['__all__']['total']
baseline_rate = pct(baseline_miss, baseline_total)
for fname, d in feature_miss.items():
    if fname == '__all__':
        continue
    feature_table.append({
        'feature': fname, 'n': d['total'], 'miss_n': d['miss'],
        'miss_rate_pct': pct(d['miss'], d['total']),
        'lift_vs_baseline': round(pct(d['miss'], d['total']) - baseline_rate, 2) if d['total'] else None,
    })
feature_table.sort(key=lambda r: -(r['lift_vs_baseline'] or -999))

out = {
    'n_rows': n_rows,
    'n_no_duty0': n_no_duty0,
    'baseline_miss_rate_pct': baseline_rate,
    'global_levels': dict(level_counter),
    'unmapped_leaves_top20': unmapped_leaves.most_common(20),
    'category_table': cat_table,
    'feature_table': feature_table,
    'examples': mismatch_examples,
    'recoverable_examples': recoverable_examples[:200],
}
json.dump(out, open(OUT_JSON, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print('rows:', n_rows, 'no_duty0:', n_no_duty0)
print('global levels:', dict(level_counter))
print('baseline miss rate %:', baseline_rate)
print('unmapped leaf top10:', unmapped_leaves.most_common(10))
print('saved ->', OUT_JSON)
