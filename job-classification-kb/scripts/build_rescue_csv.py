import pandas as pd, json, re, csv
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

# 三個規則的判定函式
CHAIN_RE = re.compile(r'全家|7-11|7-ELEVEN|統一超商|萊爾富|OK超商|美廉社')
SHIFT_RE = re.compile(r'早班|中班|晚班|大夜|日班|夜班')
STORE_BUCKETS = {'儲備幹部','餐飲服務人員','公家機關相關人員','日式廚師','中式廚師','中／港式點心廚師','洗碗人員'}

LIHUO_RE = re.compile(r'理貨|駐點')

ECOM_RE = re.compile(r'電商|理貨|倉儲|物流')
COMP_RE = re.compile(r'時薪|日領|週領|供餐|排休|臨時工|報班')

def rule_bucket1(title, duty0, new_top1):
    return bool(CHAIN_RE.search(title) and SHIFT_RE.search(title)
                and leaf2cat.get(duty0,(None,None))[1]=='門市銷售'
                and new_top1 in STORE_BUCKETS)

def rule_bucket2(title, duty0, new_top1):
    return bool(LIHUO_RE.search(title) and new_top1=='駐校代表')

def rule_bucket3(title, duty0, new_top1):
    cond_a = bool(ECOM_RE.search(title) and COMP_RE.search(title) and new_top1=='電話行銷人員')
    cond_b = bool(leaf2cat.get(duty0,(None,None))[1]=='運輸物流' and new_top1=='電話行銷人員')
    return cond_a or cond_b

rows_out = []
counts = Counter()

for i in range(n):
    o=old[i]; du=[o.get(c,'') for c in DUTY]
    title = o.get('職缺名稱','')
    ro=classify(du,[o.get(c,'') for c in REC])
    rn_row=new.iloc[i]; new_recs_raw=[rn_row[c] if pd.notna(rn_row[c]) else '' for c in REC]
    rn=classify(du,new_recs_raw)
    if ro is None or rn is None: continue
    if not (ro[0]=='hit' and rn[0]=='worst'): continue  # 只處理「舊命中→新退步」的退步案例
    new_recs=[r for r in new_recs_raw if r]
    new_top1 = new_recs[0] if new_recs else None
    duty0 = du[0]

    bucket_name = None
    if rule_bucket1(title, duty0, new_top1): bucket_name = '儲備幹部類(連鎖超商+班別)'
    elif rule_bucket2(title, duty0, new_top1): bucket_name = '駐校代表(理貨/駐點誤判)'
    elif rule_bucket3(title, duty0, new_top1): bucket_name = '電話行銷人員(電商倉儲時薪供餐)'
    if bucket_name is None: continue

    counts[bucket_name] += 1

    # 找出「正解」：廠商送出(duty0~4)裡，哪一個出現在舊推薦中(=舊模型判斷正確的那一個)
    duties_ordered = list(dict.fromkeys([d for d in du if d]))
    old_recs = ro[1]
    correct_duty = next((d for d in duties_ordered if d in old_recs), duties_ordered[0])

    # 判定要從「現有版本」剔除哪些桶
    if bucket_name.startswith('儲備幹部'):
        bad_buckets = STORE_BUCKETS
    elif bucket_name.startswith('駐校代表'):
        bad_buckets = {'駐校代表'}
    else:
        bad_buckets = {'電話行銷人員'}

    # 建構「理想推薦top10」：正解放第1名，移除誤判桶與正解自身的重複，其餘保留原順序遞補
    ideal = [correct_duty]
    for r in new_recs:
        if r in bad_buckets: continue
        if r == correct_duty: continue
        ideal.append(r)
    ideal = ideal[:10]
    while len(ideal) < 10:
        ideal.append('')

    cur10 = (new_recs + ['']*10)[:10]

    row = {
        '問題桶': bucket_name,
        '職缺名稱': title,
        'duty0': du[0], 'duty1': du[1], 'duty2': du[2], 'duty3': du[3], 'duty4': du[4],
    }
    for k in range(10):
        row[f'現有版本_推薦{k+1}'] = cur10[k]
    for k in range(10):
        row[f'理想推薦_{k+1}'] = ideal[k]
    rows_out.append(row)

print("各桶筆數：", dict(counts))
print("總筆數：", len(rows_out))

cols = ['問題桶','職缺名稱'] + DUTY + [f'現有版本_推薦{k+1}' for k in range(10)] + [f'理想推薦_{k+1}' for k in range(10)]
OUT = "/home/user/main/job-classification-kb/training_feedback/4_worst_case_rescue_plan.csv"
with open(OUT, 'w', encoding='utf-8-sig', newline='') as f:
    fh = f
    fh.write("# worst case 拯救方案：已驗證安全的手術式修正（儲備幹部/駐校代表/電話行銷人員 三桶，共" + str(len(rows_out)) + "筆，零誤傷本次已救回案例）\n")
    w = csv.DictWriter(fh, fieldnames=cols)
    w.writeheader()
    w.writerows(rows_out)
print("saved ->", OUT)
