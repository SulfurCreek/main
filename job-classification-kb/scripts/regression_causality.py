import pandas as pd, json
from collections import Counter, defaultdict

OLD_MD = "/home/user/main/job-classification-kb/tcode/data_職缺名稱_dutyMapping.md"
NEW_XLSX = "/root/.claude/uploads/6d643d58-f39d-53f8-a740-df69060d043b/a61c2155-________20260720.xlsx"
DUTY = [f"duty{i}" for i in range(5)]; REC = [f"職類推薦{i}" for i in range(1,11)]
tree = json.load(open('/home/user/main/job-classification-kb/scripts/_dutynm_tree.json',encoding='utf-8'))
leaf2cat = {leaf:(M,mid) for M,mids in tree.items() for mid,ls in mids.items() for leaf in ls}

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
    return ('worst' if fhr is None else ('hit'), recs)

old=parse_md(OLD_MD); new=pd.read_excel(NEW_XLSX,sheet_name="Sheet1",dtype=str)
n=min(len(old),len(new))

# per-mid: fed_worst(old worst 數) / rescued(old worst→new hit) / regressed(old hit→new worst)
per=defaultdict(lambda: Counter())
reg_newtop1=Counter(); rescued_newtop1=Counter()
for i in range(n):
    o=old[i]; du=[o.get(c,'') for c in DUTY]
    ro=classify(du,[o.get(c,'') for c in REC])
    rn_row=new.iloc[i]; new_recs=[rn_row[c] if pd.notna(rn_row[c]) else '' for c in REC]
    rn=classify(du,new_recs)
    if ro is None or rn is None: continue
    mid=leaf2cat.get(du[0],(None,None))[1]
    if mid is None: continue
    old_sc=ro[0]; new_sc=rn[0]
    if old_sc=='worst': per[mid]['fed_worst']+=1
    if old_sc=='worst' and new_sc=='hit':
        per[mid]['rescued']+=1
        rescued_newtop1[[r for r in new_recs if r][0]] += 1
    if old_sc=='hit' and new_sc=='worst':
        per[mid]['regressed']+=1
        reg_newtop1[[r for r in new_recs if r][0]] += 1

rows=[]
for mid,c in per.items():
    rows.append((mid,c['fed_worst'],c['rescued'],c['regressed']))
# sort by regressed desc
rows.sort(key=lambda x:-x[3])
print(f"{'中類':16s} {'餵進要修(舊worst)':>14s} {'救回':>8s} {'退步':>8s} {'退步/救回':>10s}")
tot_fed=tot_res=tot_reg=0
for mid,fed,res,reg in rows[:15]:
    ratio = f"{reg/res:.2f}" if res else "-"
    print(f"{mid:16s} {fed:>14d} {res:>8d} {reg:>8d} {ratio:>10s}")
for mid,fed,res,reg in rows:
    tot_fed+=fed; tot_res+=res; tot_reg+=reg
print(f"\n全體: 餵進要修={tot_fed}, 救回={tot_res}, 退步={tot_reg}")

# correlation: do categories with more fed_worst also have more regressions?
import statistics
fed=[r[1] for r in rows]; reg=[r[3] for r in rows]
# pearson
mf=statistics.mean(fed); mr=statistics.mean(reg)
cov=sum((a-mf)*(b-mr) for a,b in zip(fed,reg))
sf=(sum((a-mf)**2 for a in fed))**.5; sr=(sum((b-mr)**2 for b in reg))**.5
print(f"\n各中類「餵進要修的量」vs「退步量」相關係數 r = {cov/(sf*sr):.3f}")

print("\n=== 退步案例 被推去哪(new top1) top10 ===")
for k,v in reg_newtop1.most_common(10): print(f"  {k}: {v}")
print("\n=== 被救回的worst案例 推去哪(new top1) top10 ===")
for k,v in rescued_newtop1.most_common(10): print(f"  {k}: {v}")

print("\n\n=== 決定性檢驗:同一目標桶,救回 vs 退步 都落在這 ===")
# 交集:同時是救回去處與退步去處的 new_top1 類別
both = set(reg_newtop1) & set(rescued_newtop1)
rows2 = [(t, rescued_newtop1[t], reg_newtop1[t]) for t in both]
rows2.sort(key=lambda x:-(x[1]+x[2]))
print(f"{'新推薦目標類別':20s} {'救回進來':>8s} {'退步進來':>8s} {'汙染率(退步/總)':>14s}")
for t,res,reg in rows2[:12]:
    poll = reg/(res+reg)
    print(f"{t:20s} {res:>8d} {reg:>8d} {poll*100:>12.1f}%")
