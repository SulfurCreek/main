import pandas as pd, json
from collections import Counter, defaultdict

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

old=parse_md(OLD_MD); new=pd.read_excel(NEW_XLSX,sheet_name="Sheet1",dtype=str)
n=min(len(old),len(new))

# 蒐集:每個「退步落入的目標桶」→ 該桶的退步(誤傷)案例 (title, old duty0, old top3 rec, new top3 rec)
bucket_examples = defaultdict(list)
bucket_stats = Counter()  # (target, 'res'/'reg') -> count

for i in range(n):
    o=old[i]; du=[o.get(c,'') for c in DUTY]
    ro=classify(du,[o.get(c,'') for c in REC])
    rn_row=new.iloc[i]; new_recs_raw=[rn_row[c] if pd.notna(rn_row[c]) else '' for c in REC]
    rn=classify(du,new_recs_raw)
    if ro is None or rn is None: continue
    new_recs=[r for r in new_recs_raw if r]
    target = new_recs[0] if new_recs else None
    if target is None: continue
    if ro[0]=='worst' and rn[0]=='hit': bucket_stats[(target,'res')]+=1
    if ro[0]=='hit' and rn[0]=='worst':
        bucket_stats[(target,'reg')]+=1
        if len(bucket_examples[target]) < 3:
            old_recs=[r for r in ro[1] if r]
            bucket_examples[target].append({
                'title': o.get('職缺名稱',''),
                'duty0': du[0],
                'old_top3': old_recs[:3],
                'new_top3': new_recs[:3],
            })

json.dump({'examples': bucket_examples, 'stats': {f"{k[0]}|{k[1]}":v for k,v in bucket_stats.items()}},
          open('bucket_examples.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
print("saved bucket_examples.json")
print("total target buckets with regression examples:", len(bucket_examples))
