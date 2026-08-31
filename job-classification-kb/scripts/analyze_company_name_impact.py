"""量化「職缺名稱含公司/品牌資訊」對推薦準確度的影響。

比較含公司資訊 vs 不含者，在 best/enhancement/worst 三情境的分布差異；
並找出「品牌行業聯想 ≠ 實際職務」的高風險案例（如 DHL × 招募專員）。
"""
import json, csv, re, collections

BASE = '/home/user/main/job-classification-kb/'
tok = json.load(open(BASE + 'scripts/_company_tokens.json', encoding='utf-8'))
labels = json.load(open(BASE + 'scripts/_company_brand_labels.json', encoding='utf-8'))

# 直接沿用已清理過的清單（build_company_token_csv.py 的第6類），避免地區/產業誤入
brands = set()
with open(BASE + 'analysis_職缺名稱公司資訊清單.csv', encoding='utf-8-sig') as fh:
    for r in csv.reader(fh):
        if r and r[0] == '6_公司品牌名稱':
            brands.add(r[1])
brand_rx = re.compile('|'.join(sorted((re.escape(b) for b in brands), key=len, reverse=True)))

ATTR_RX = re.compile('|'.join(
    re.escape(w) for k in tok['attr'] for w in tok['attr'][k]))

scen = {}
for f, s in [('1_best_practice.csv', 'best'),
             ('2_enhancement.csv', 'enhancement'),
             ('3_worst_practice.csv', 'worst')]:
    with open(BASE + 'training_feedback/' + f, encoding='utf-8-sig') as fh:
        next(fh)
        for row in csv.DictReader(fh):
            scen.setdefault(row['職缺名稱'], (s, row))

grp = collections.defaultdict(collections.Counter)
for n, (s, _) in scen.items():
    has_b = bool(brand_rx.search(n))
    has_a = bool(ATTR_RX.search(n))
    key = '含公司品牌名' if has_b else ('僅含公司屬性' if has_a else '不含公司資訊')
    grp[key][s] += 1

print(f"{'族群':<14}{'樣本':>9}{'best':>9}{'enh':>9}{'worst':>9}{'worst占比':>10}")
for k in ['不含公司資訊', '僅含公司屬性', '含公司品牌名']:
    c = grp[k]; t = sum(c.values())
    print(f"{k:<14}{t:>9,}{c['best']:>9,}{c['enhancement']:>9,}{c['worst']:>9,}{c['worst']/t:>10.1%}")

# 高風險案例：含品牌名且落在 worst
risk = []
for n, (s, row) in scen.items():
    if s != 'worst':
        continue
    m = brand_rx.search(n)
    if not m:
        continue
    duty = [row.get(f'duty{i}', '') for i in range(5)]
    recs = [row.get(f'職類推薦{i}', '') for i in range(1, 6)]
    risk.append((m.group(0), n, [d for d in duty if d], recs))

print(f"\n含品牌名且完全沒命中(worst)：{len(risk):,} 筆")
top = collections.Counter(r[0] for r in risk)
print("最常出現的品牌（worst 筆數）：", top.most_common(20))

out = BASE + 'analysis_公司品牌名誤導案例.csv'
with open(out, 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f)
    w.writerow(['品牌名', '職缺名稱'] + [f'廠商duty{i}' for i in range(5)]
               + [f'AI推薦{i}' for i in range(1, 6)])
    for b, n, d, r in sorted(risk):
        w.writerow([b, n] + d + [''] * (5 - len(d)) + r)
print(f"→ {out}")
