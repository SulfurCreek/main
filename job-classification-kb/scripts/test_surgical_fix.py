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

# 定義「連鎖超商+班別」樣態：標題含超商連鎖品牌 + 班別關鍵字
CHAIN_RE = re.compile(r'全家|7-11|7-ELEVEN|統一超商|萊爾富|OK超商|美廉社')
SHIFT_RE = re.compile(r'早班|中班|晚班|大夜|日班|夜班')
TARGET_BUCKETS = {'儲備幹部','餐飲服務人員','公家機關相關人員','日式廚師','中式廚師','中／港式點心廚師','洗碗人員'}

matched_regressions = []   # 符合樣態、且被誤判成 worst 的案例（可修）
matched_rescues = []       # 符合樣態、且被救回成 hit 的案例（修了會不會誤傷）
matched_other = []         # 符合樣態、但本來就 hit->hit 或 worst->worst（不受影響）

for i in range(n):
    o=old[i]; du=[o.get(c,'') for c in DUTY]
    title = o.get('職缺名稱','')
    is_pattern = bool(CHAIN_RE.search(title) and SHIFT_RE.search(title))
    if not is_pattern: continue
    mid = leaf2cat.get(du[0], (None,None))[1]
    if mid != '門市銷售': continue  # 限定廠商送出主選確實是門市銷售類

    ro=classify(du,[o.get(c,'') for c in REC])
    rn_row=new.iloc[i]; new_recs_raw=[rn_row[c] if pd.notna(rn_row[c]) else '' for c in REC]
    rn=classify(du,new_recs_raw)
    if ro is None or rn is None: continue
    new_recs=[r for r in new_recs_raw if r]
    new_top1 = new_recs[0] if new_recs else None
    if new_top1 not in TARGET_BUCKETS: continue  # 只看落入這幾個可疑桶的

    rec = {'title':title,'duty0':du[0],'old_sc':ro[0],'new_sc':rn[0],'new_top1':new_top1,'new_top3':new_recs[:3]}
    if ro[0]=='hit' and rn[0]=='worst':
        matched_regressions.append(rec)
    elif ro[0]=='worst' and rn[0]=='hit':
        matched_rescues.append(rec)
    else:
        matched_other.append(rec)

print(f"符合「連鎖超商+班別」樣態、廠商送出為門市銷售類、新推薦落入可疑桶的職缺：")
print(f"  舊命中→新退步(可修的誤傷)：{len(matched_regressions)} 筆")
print(f"  舊沒命中→新救回(修了會不會誤傷這些)：{len(matched_rescues)} 筆")
print(f"  其他(不受影響)：{len(matched_other)} 筆")

print("\n=== 可修的誤傷案例(舊命中→新退步) 全部列出 ===")
for r in matched_regressions:
    print(f"  `{r['title']}` duty0={r['duty0']} → {r['new_top3']}")

print("\n=== 若做規則修正，會不會誤傷「本來就靠這個樣態被救回」的案例 ===")
if matched_rescues:
    for r in matched_rescues:
        print(f"  `{r['title']}` duty0={r['duty0']} → {r['new_top3']}")
else:
    print("  無——這個樣態下，沒有任何案例是靠新推薦=可疑桶而被救回的。")
