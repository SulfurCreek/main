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

def test_rule(name, predicate):
    matched = [r for r in all_rows if predicate(r)]
    regs = [r for r in matched if r['old_sc']=='hit' and r['new_sc']=='worst']
    rescues = [r for r in matched if r['old_sc']=='worst' and r['new_sc']=='hit']
    other = [r for r in matched if not (r in regs or r in rescues)]
    print(f"\n===== 規則：{name} =====")
    print(f"命中規則總筆數: {len(matched)}")
    print(f"  可修(舊命中→新退步): {len(regs)}")
    print(f"  會誤傷(舊沒命中→新救回，若壓抑此規則會讓這些案例回到沒命中): {len(rescues)}")
    print(f"  其他(不受影響): {len(other)}")
    if rescues:
        print(f"  ⚠️ 有救回案例會被誤傷，列出前5筆檢查是否合理被壓抑：")
        for r in rescues[:5]:
            print(f"    `{r['title']}` duty0={r['duty0']} → {r['new_recs'][:3]}")
    else:
        print("  ✅ 零誤傷：可安全修正")
    return regs, rescues

# ===== 桶2：駐校代表 =====
print("########## 桶2：駐校代表 ##########")
test_rule(
    "標題含「理貨」→ 新推薦1=駐校代表",
    lambda r: '理貨' in r['title'] and r['new_top1']=='駐校代表'
)
test_rule(
    "標題含「駐點」→ 新推薦1=駐校代表",
    lambda r: '駐點' in r['title'] and r['new_top1']=='駐校代表'
)
# 合併規則：理貨 或 駐點 → 駐校代表（整桶幾乎全覆蓋）
test_rule(
    "標題含「理貨」或「駐點」→ 新推薦1=駐校代表（合併規則，涵蓋整桶）",
    lambda r: ('理貨' in r['title'] or '駐點' in r['title']) and r['new_top1']=='駐校代表'
)

# ===== 桶3：電話行銷人員 =====
print("\n\n########## 桶3：電話行銷人員 ##########")
ECOM_RE = re.compile(r'電商|理貨|倉儲|物流')
COMP_RE = re.compile(r'時薪|日領|週領|供餐|排休|臨時工|報班')
test_rule(
    "標題含電商/理貨/倉儲/物流字樣 + 薪資班表描述詞 → 新推薦1=電話行銷人員",
    lambda r: ECOM_RE.search(r['title']) and COMP_RE.search(r['title']) and r['new_top1']=='電話行銷人員'
)
# 只看 duty0 屬於運輸物流/採購物流品質檢測 大類 的情況（廠商原本就標為物流類）
test_rule(
    "廠商送出主選屬「運輸物流」中類 → 新推薦1=電話行銷人員",
    lambda r: leaf2cat.get(r['duty0'],(None,None))[1]=='運輸物流' and r['new_top1']=='電話行銷人員'
)
