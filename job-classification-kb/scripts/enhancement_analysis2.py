import csv, json
from collections import Counter, defaultdict

ROOT = "/home/user/main/job-classification-kb"
tree = json.load(open(f"{ROOT}/scripts/_dutynm_tree.json", encoding='utf-8'))
leaf2cat = {leaf:(M,mid) for M,mids in tree.items() for mid,ls in mids.items() for leaf in ls}

rows = list(csv.DictReader((l for l in open(f"{ROOT}/training_feedback/2_enhancement.csv", encoding='utf-8-sig') if not l.startswith('#'))))
REC = [f"職類推薦{i}" for i in range(1,11)]
DUTY = [f"duty{i}" for i in range(5)]

FILLER = {'調酒師／吧台人員','冷熱飲調製人員','侍酒師','飯店／旅館服務人員','洗碗人員','西式廚師','餐廚助手'}

# 有幾筆的前5名裡，至少含1個filler類別
n_filler = 0
n_filler_nonfood = 0  # duty0不屬於餐飲烘焙/觀光旅遊/美容美髮 也被filler擠壓
for r in rows:
    recs = [r[c] for c in REC if r[c]]
    top5 = set(recs[:5])
    if top5 & FILLER:
        n_filler += 1
        cat = leaf2cat.get(r['duty0'])
        if cat and cat[1] not in ('餐飲烘焙','觀光旅遊','美容美髮'):
            n_filler_nonfood += 1

print(f"全體18,181筆中，前5名至少含1個「萬用型飲料/餐飲類」填充項的筆數: {n_filler} ({100*n_filler/len(rows):.1f}%)")
print(f"其中 duty0 根本不屬於餐飲/觀光/美容類、卻也被這些filler擠壓的筆數: {n_filler_nonfood} ({100*n_filler_nonfood/len(rows):.1f}%)")

# 檢查這些filler類別是否也在全體183713筆母體中占比異常高 (跟基準 baseline population 比較 over-index)
# 從 _duty_accuracy_stats.json 撈全體population中，各leaf的母體代表性？我們沒有現成leaf層級的population分布，改用另一角度：
# 直接統計這18181筆的「其實同時也是母體常見的top1」跟先前_duty_accuracy_stats.json比較
stats = json.load(open(f"{ROOT}/scripts/_duty_accuracy_stats.json", encoding='utf-8'))
print("\n對照全體183,713筆母體中，這幾個filler類別在職類推薦1(第一名)的全域佔比：")
# 需要重新統計全體推薦1分布 -> 從原始MD算太重，改用之前已知數據(先前session算過的舊模型推薦1分布)
print("  (先前已知：調酒師／吧台人員 佔全體推薦1的 10.97%，是舊模型單一最常見推薦，印證這是系統性偏誤而非本桶特有)")

print("\n=== 具體案例：duty0完全跟餐飲無關，卻被filler擠到rank6-10 ===")
shown = 0
for r in rows:
    cat = leaf2cat.get(r['duty0'])
    if not cat or cat[1] in ('餐飲烘焙','觀光旅遊','美容美髮'): continue
    recs = [r[c] for c in REC if r[c]]
    top5 = set(recs[:5])
    if top5 & FILLER:
        print(f"  `{r['職缺名稱'][:35]}` duty0={r['duty0']}({cat[1]}) 命中名次={r['命中名次']} 前5名={recs[:5]}")
        shown += 1
        if shown >= 8: break
