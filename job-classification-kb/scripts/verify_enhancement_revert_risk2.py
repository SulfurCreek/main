import pandas as pd, csv
from collections import Counter

OLD_MD = "/home/user/main/job-classification-kb/tcode/data_職缺名稱_dutyMapping.md"
NEW_XLSX = "/root/.claude/uploads/6d643d58-f39d-53f8-a740-df69060d043b/a61c2155-________20260720.xlsx"
DUTY = [f"duty{i}" for i in range(5)]; REC = [f"職類推薦{i}" for i in range(1,11)]

def parse_md(path):
    lines=open(path,encoding='utf-8').read().splitlines(); start=header=None
    for i,l in enumerate(lines):
        if l.startswith("| 職缺名稱"): header=[c.strip() for c in l.strip().strip("|").split("|")]; start=i+2; break
    out=[]
    for l in lines[start:]:
        if not l.startswith("|"): continue
        c=[x.strip() for x in l.strip("|").split("|")]
        if len(c)==len(header): out.append(dict(zip(header,c)))
    return out

def classify(duties_raw, recs_raw):
    duties=list(dict.fromkeys([d for d in duties_raw if d and str(d)!='nan']))
    recs=[r for r in recs_raw if r and str(r)!='nan']
    if not duties or not recs: return None
    sel=set(duties); fhr=next((i+1 for i,r in enumerate(recs) if r in sel),None)
    return ('worst' if fhr is None else 'hit', recs)

old=parse_md(OLD_MD); new=pd.read_excel(NEW_XLSX, sheet_name="Sheet1", dtype=str)
n=min(len(old),len(new))

# 找出 舊模型是 enhancement(前5沒中、6-10命中) 的所有列，看新模型現在的狀態
FILLER_STRONG = {'調酒師／吧台人員','冷熱飲調製人員','侍酒師','飯店／旅館服務人員','西式廚師'}  # 排除洗碗人員(混合)、餐廚助手(合法)

new_status = Counter()
crossdomain_new_status = Counter()
examples_still_bad = []
examples_now_fixed = []

import json
tree = json.load(open('/home/user/main/job-classification-kb/scripts/_dutynm_tree.json', encoding='utf-8'))
leaf2cat = {leaf:(M,mid) for M,mids in tree.items() for mid,ls in mids.items() for leaf in ls}

count_checked = 0
for i in range(n):
    o = old[i]
    du = [o.get(c,'') for c in DUTY]
    ro = classify(du, [o.get(c,'') for c in REC])
    if ro is None or ro[0] != 'hit': continue
    old_recs = ro[1]
    top5_old = set(old_recs[:5])
    fhr = next((idx+1 for idx,r in enumerate(old_recs) if r in du), None)
    if fhr is None or fhr <= 5: continue  # 只看 enhancement(6-10)案例
    if not (top5_old & FILLER_STRONG): continue  # 只看被強填充項擠壓的
    count_checked += 1

    rn_row = new.iloc[i]
    new_recs = [rn_row[c] for c in REC if pd.notna(rn_row[c])]
    rn = classify(du, new_recs)
    new_status[rn[0] if rn else 'N/A'] += 1

    cat = leaf2cat.get(du[0])
    is_crossdomain = cat and cat[1] not in ('餐飲烘焙','觀光旅遊','美容美髮')
    if is_crossdomain:
        crossdomain_new_status[rn[0] if rn else 'N/A'] += 1
        if rn and rn[0] == 'worst' and len(examples_still_bad) < 5:
            examples_still_bad.append({'title':o.get('職缺名稱',''),'duty0':du[0],'new_recs':new_recs[:5]})
        if rn and rn[0] == 'hit' and len(examples_now_fixed) < 5:
            examples_now_fixed.append({'title':o.get('職缺名稱',''),'duty0':du[0],'new_recs':new_recs[:5]})

print(f"舊模型「被強填充項擠壓的enhancement案例」共 {count_checked} 筆")
print(f"這些案例在新模型(20260720)現在的狀態分布: {dict(new_status)}")
print(f"\n其中跨領域(duty0與餐飲/觀光/美容無關)的案例，新模型狀態分布: {dict(crossdomain_new_status)}")

print("\n=== 跨領域案例，新模型仍然沒中的範例(代表這是新舊模型共同的老問題，不是revert風險，是待修) ===")
for e in examples_still_bad:
    print(f"  `{e['title'][:35]}` duty0={e['duty0']} → 新推薦前5={e['new_recs']}")

print("\n=== 跨領域案例，新模型已經修好的範例(側面驗證新模型有進步) ===")
for e in examples_now_fixed:
    print(f"  `{e['title'][:35]}` duty0={e['duty0']} → 新推薦前5={e['new_recs']}")
