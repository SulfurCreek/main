import csv, json
from collections import Counter, defaultdict

ROOT = "/home/user/main/job-classification-kb"
tree = json.load(open(f"{ROOT}/scripts/_dutynm_tree.json", encoding='utf-8'))
leaf2cat = {leaf:(M,mid) for M,mids in tree.items() for mid,ls in mids.items() for leaf in ls}

rows = list(csv.DictReader((l for l in open(f"{ROOT}/training_feedback/2_enhancement.csv", encoding='utf-8-sig') if not l.startswith('#'))))
print("總筆數:", len(rows))

REC = [f"職類推薦{i}" for i in range(1,11)]
DUTY = [f"duty{i}" for i in range(5)]

# 1. 依 duty0 中類分布(排序問題集中在哪些中類)
mid_counter = Counter()
for r in rows:
    cat = leaf2cat.get(r['duty0'])
    if cat: mid_counter[cat] += 1
print("\n=== 排序問題最集中的中類 top15 ===")
for k,v in mid_counter.most_common(15):
    print(f"  {k}: {v}")

# 2. 找出「擠掉正解、佔據前5名」最常見的類別
crowd_counter = Counter()
for r in rows:
    correct = r['duty0']  # 主要看 duty0 是否為命中的那個? 需要重新判斷是哪個duty命中
    duties = [r[c] for c in DUTY if r[c]]
    recs = [r[c] for c in REC if r[c]]
    hit_rank = int(r['命中名次'])
    top5 = recs[:5]
    for t in top5:
        crowd_counter[t] += 1

print("\n=== 佔據前5名格位最常見的類別 top20(整體樣本，非僅退步案例) ===")
for k,v in crowd_counter.most_common(20):
    print(f"  {k}: {v} ({100*v/len(rows):.1f}%)")

print("\n\n=== 深入：這些擠佔前5名的類別，是不是全面性的(不分duty0類別都出現)，還是集中在特定duty0類別？ ===")
crowd_by_duty0cat = defaultdict(Counter)
for r in rows:
    cat = leaf2cat.get(r['duty0'])
    if not cat: continue
    recs = [r[c] for c in REC if r[c]]
    top5 = recs[:5]
    for t in top5:
        crowd_by_duty0cat[cat][t] += 1

# 看調酒師/吧台人員 這個最強勢的擠壓者，出現在哪些 duty0 中類底下(是不是跨很多不相關類別)
target = '調酒師／吧台人員'
print(f"\n「{target}」出現在前5名格位時，對應的 duty0 中類分布(看是否跨很多不相關類別)：")
cross_cats = Counter()
for r in rows:
    recs = [r[c] for c in REC if r[c]]
    if target in recs[:5]:
        cat = leaf2cat.get(r['duty0'])
        if cat: cross_cats[cat] += 1
for k,v in cross_cats.most_common(15):
    print(f"  {k}: {v}")
