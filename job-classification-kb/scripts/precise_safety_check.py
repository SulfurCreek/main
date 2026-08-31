import pandas as pd

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

# 精確驗證：這個桶本身(target)有沒有真的被廠商標記過(=在 duty0~4 裡出現)
for target in ['駐校代表','電話行銷人員']:
    true_hits = 0
    total_appear_top1 = 0
    for i in range(n):
        o=old[i]; du=[o.get(c,'') for c in DUTY]
        ro=classify(du,[o.get(c,'') for c in REC])
        rn_row=new.iloc[i]; new_recs_raw=[rn_row[c] if pd.notna(rn_row[c]) else '' for c in REC]
        rn=classify(du,new_recs_raw)
        if ro is None or rn is None: continue
        new_recs=[r for r in new_recs_raw if r]
        if not new_recs or new_recs[0]!=target: continue
        total_appear_top1 += 1
        if ro[0]=='worst' and rn[0]=='hit':
            # 檢查：救回的關鍵是不是「target」這個字本身
            if target in du:
                true_hits += 1
    print(f"目標桶「{target}」排名第1的所有案例：{total_appear_top1} 筆")
    print(f"  其中「舊worst→新hit」且救回關鍵真的是「{target}」本身(廠商也標記過這個類別)：{true_hits} 筆")
    print(f"  → 若把「{target}」從推薦中抑制/降權，會真正損失的救回數 = {true_hits} 筆\n")
