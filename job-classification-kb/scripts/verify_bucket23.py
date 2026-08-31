import pandas as pd, json, re
from collections import Counter

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
    return ('worst' if fhr is None else 'hit', recs)

old=parse_md(OLD_MD); new=pd.read_excel(NEW_XLSX,sheet_name="Sheet1",dtype=str)
n=min(len(old),len(new))

all_rows=[]
for i in range(n):
    o=old[i]; du=[o.get(c,'') for c in DUTY]
    ro=classify(du,[o.get(c,'') for c in REC])
    rn_row=new.iloc[i]; new_recs_raw=[rn_row[c] if pd.notna(rn_row[c]) else '' for c in REC]
    rn=classify(du,new_recs_raw)
    if ro is None or rn is None: continue
    new_recs=[r for r in new_recs_raw if r]
    all_rows.append({'title':o.get('職缺名稱',''),'duty0':du[0],'old_sc':ro[0],'new_sc':rn[0],
                      'new_top1': new_recs[0] if new_recs else None, 'new_recs':new_recs})

print("========== 桶2：駐校代表 — 驗證「理貨+班別」 vs 「日班/夜班單獨」 ==========\n")
zhu_regs = [r for r in all_rows if r['old_sc']=='hit' and r['new_sc']=='worst' and r['new_top1']=='駐校代表']
print(f"駐校代表 退步案例總數: {len(zhu_regs)}")
lihuo_re = re.compile(r'理貨')
n_lihuo = sum(1 for r in zhu_regs if lihuo_re.search(r['title']))
print(f"標題含「理貨」: {n_lihuo} ({100*n_lihuo/len(zhu_regs):.1f}%)")
# baseline理貨 rate across ALL regressions
all_regs = [r for r in all_rows if r['old_sc']=='hit' and r['new_sc']=='worst']
base_lihuo = sum(1 for r in all_regs if lihuo_re.search(r['title']))
print(f"全體退步案例含「理貨」基準比例: {100*base_lihuo/len(all_regs):.1f}%  (over-index: {(n_lihuo/len(zhu_regs))/(base_lihuo/len(all_regs)):.1f}x)\n")

# 驗證：理貨+班別 vs 理貨(不論班別) vs 班別(不論理貨) 三種切法哪個對駐校代表最集中
lihuo_only = [r for r in zhu_regs if lihuo_re.search(r['title'])]
print(f"含「理貨」的{len(lihuo_only)}筆中，同時也含班別關鍵字的比例：")
shift_re = re.compile(r'日班|夜班|早班|中班|大夜|晚班')
n_both = sum(1 for r in lihuo_only if shift_re.search(r['title']))
print(f"  {n_both}/{len(lihuo_only)} = {100*n_both/len(lihuo_only) if lihuo_only else 0:.1f}%")

print("\n所有含「理貨」的駐校代表退步案例（全列）：")
for r in zhu_regs:
    if lihuo_re.search(r['title']):
        print(f"  `{r['title']}` duty0={r['duty0']} → {r['new_recs'][:3]}")

print("\n不含「理貨」的駐校代表退步案例（全列，看看還有沒有別的樣態）：")
for r in zhu_regs:
    if not lihuo_re.search(r['title']):
        print(f"  `{r['title']}` duty0={r['duty0']} → {r['new_recs'][:3]}")

print("\n\n========== 桶3：電話行銷人員 — 不含電信字的42筆，是不是同一種撐大機制 ==========\n")
tel_re = re.compile(r'電信|遠傳|中華電信|台哥大|台灣大哥大|Myfone|亞太電信')
phone_bucket_all = [r for r in all_rows if r['new_top1']=='電話行銷人員']
phone_regs = [r for r in phone_bucket_all if r['old_sc']=='hit' and r['new_sc']=='worst']
phone_rescues = [r for r in phone_bucket_all if r['old_sc']=='worst' and r['new_sc']=='hit']
print(f"電話行銷人員 桶：救回{len(phone_rescues)}筆／退步{len(phone_regs)}筆／污染率{100*len(phone_regs)/(len(phone_regs)+len(phone_rescues)):.1f}%")

no_tel_regs = [r for r in phone_regs if not tel_re.search(r['title'])]
no_tel_rescues = [r for r in phone_rescues if not tel_re.search(r['title'])]
print(f"\n不含電信字：退步{len(no_tel_regs)}筆／救回{len(no_tel_rescues)}筆")
if no_tel_regs or no_tel_rescues:
    pol = 100*len(no_tel_regs)/(len(no_tel_regs)+len(no_tel_rescues)) if (len(no_tel_regs)+len(no_tel_rescues)) else 0
    print(f"不含電信字這一群的污染率：{pol:.1f}%  <- 若接近/高於整體污染率，代表這就是同一種撐大機制的副作用")

print("\n不含電信字、但被救回(hit)的案例(代表這個子群本身也有救回貢獻，非純誤傷)：")
for r in no_tel_rescues[:5]:
    print(f"  `{r['title']}` duty0={r['duty0']} → {r['new_recs'][:3]}")

print("\n不含電信字的退步(誤傷)全列：")
for r in no_tel_regs:
    print(f"  `{r['title']}` duty0={r['duty0']} → {r['new_recs'][:3]}")
