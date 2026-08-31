import pandas as pd, json
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

old=parse_md(OLD_MD)
FILLER = ['調酒師／吧台人員','冷熱飲調製人員','侍酒師','飯店／旅館服務人員','洗碗人員','西式廚師','餐廚助手']

print("========== 第一步：這些填充類別，在舊模型基準(183,713筆)裡，本身是不是「有效類別」？ ==========\n")
print(f"{'類別':16s} {'排第1名總筆數':>12s} {'其中真的是廠商送出(合法)':>18s} {'合法率':>8s}")
for target in FILLER:
    total_top1 = 0
    true_hits = 0
    for row in old:
        du = [row.get(c,'') for c in DUTY]
        recs = [row.get(c,'') for c in REC if row.get(c,'')]
        if not recs or recs[0] != target: continue
        total_top1 += 1
        if target in du:
            true_hits += 1
    rate = 100*true_hits/total_top1 if total_top1 else 0
    print(f"{target:16s} {total_top1:>12d} {true_hits:>18d} {rate:>7.1f}%")
