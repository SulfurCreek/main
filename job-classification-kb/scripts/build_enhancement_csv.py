import csv, json
from collections import Counter

ROOT = "/home/user/main/job-classification-kb"
tree = json.load(open(f"{ROOT}/scripts/_dutynm_tree.json", encoding='utf-8'))
leaf2cat = {leaf:(M,mid) for M,mids in tree.items() for mid,ls in mids.items() for leaf in ls}

rows = list(csv.DictReader((l for l in open(f"{ROOT}/training_feedback/2_enhancement.csv", encoding='utf-8-sig') if not l.startswith('#'))))
REC = [f"職類推薦{i}" for i in range(1,11)]
DUTY = [f"duty{i}" for i in range(5)]

FILLER = {'調酒師／吧台人員','冷熱飲調製人員','侍酒師','飯店／旅館服務人員','洗碗人員','西式廚師','餐廚助手'}

rows_out = []
tag_count = Counter()
for r in rows:
    recs = [r[c] for c in REC if r[c]]
    hit_rank = int(r['命中名次'])
    correct_duty = recs[hit_rank-1]
    top5 = set(recs[:5])
    is_filler_case = bool(top5 & FILLER)
    cat = leaf2cat.get(r['duty0'])
    is_crossdomain = is_filler_case and cat and cat[1] not in ('餐飲烘焙','觀光旅遊','美容美髮')

    tag = ''
    if is_crossdomain:
        tag = '萬用填充項擠壓-跨領域(高信心)'
    elif is_filler_case:
        tag = '萬用填充項擠壓-同領域'
    tag_count[tag or '(其他排序問題)'] += 1

    # 理想重排：正解移到第1名，其餘保留原順序，移除正解在原位置的重複
    ideal = [correct_duty] + [x for x in recs if x != correct_duty]
    ideal = ideal[:10]
    while len(ideal) < 10: ideal.append('')
    cur10 = (recs + ['']*10)[:10]

    row = {'排序問題樣態': tag, '職缺名稱': r['職缺名稱']}
    for c in DUTY: row[c] = r[c]
    for k in range(10): row[f'現有版本_推薦{k+1}'] = cur10[k]
    for k in range(10): row[f'理想推薦_{k+1}'] = ideal[k]
    rows_out.append(row)

print("總筆數:", len(rows_out))
print("樣態分布:", dict(tag_count))

cols = ['排序問題樣態','職缺名稱'] + DUTY + [f'現有版本_推薦{k+1}' for k in range(10)] + [f'理想推薦_{k+1}' for k in range(10)]
OUT = f"{ROOT}/training_feedback/5_enhancement_reorder_plan.csv"
with open(OUT, 'w', encoding='utf-8-sig', newline='') as f:
    f.write(f"# 排序待優化案例（enhancement）：全部 {len(rows_out)} 筆，AI有推到正解但排在第6~10名、前端看不到，逐筆理想重排（正解移至第1名）。訓練回饋用，非全域規則。\n")
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    w.writerows(rows_out)
print("saved ->", OUT)
