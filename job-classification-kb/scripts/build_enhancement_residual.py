import pandas as pd, csv, json

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
    return (fhr, recs)  # fhr: 1-based hit rank or None

old=parse_md(OLD_MD); new=pd.read_excel(NEW_XLSX, sheet_name="Sheet1", dtype=str)
n=min(len(old),len(new))

FILLER_STRONG = {'調酒師／吧台人員','冷熱飲調製人員','侍酒師','飯店／旅館服務人員','西式廚師'}

tree = json.load(open('/home/user/main/job-classification-kb/scripts/_dutynm_tree.json', encoding='utf-8'))
leaf2cat = {leaf:(M,mid) for M,mids in tree.items() for mid,ls in mids.items() for leaf in ls}

rows_out = []
status_count = {'already_top5':0, 'still_enhancement':0, 'still_worst_dedup_skip':0}

for i in range(n):
    o = old[i]
    du = [o.get(c,'') for c in DUTY]
    fhr_old, old_recs = classify(du, [o.get(c,'') for c in REC]) or (None, [])
    if fhr_old is None or fhr_old <= 5: continue  # 只看舊模型 enhancement(6-10) 案例
    top5_old = set(old_recs[:5])
    if not (top5_old & FILLER_STRONG): continue  # 只看被強填充項擠壓的

    rn_row = new.iloc[i]
    new_recs = [rn_row[c] for c in REC if pd.notna(rn_row[c])]
    dutyset = set(d for d in du if d and str(d) != 'nan')
    fhr_new = next((idx+1 for idx,r in enumerate(new_recs) if r in dutyset), None)

    if fhr_new is not None and fhr_new <= 5:
        status_count['already_top5'] += 1
        continue  # 已解決，不需要處理

    # 找正解：舊模型在第6~10名命中的那個職類
    correct_duty = old_recs[fhr_old-1]

    if fhr_new is not None and fhr_new > 5:
        status_count['still_enhancement'] += 1
        tag = '萬用填充項擠壓-新模型仍未解決(排序6-10)'
        current_recs = new_recs
    else:
        # 完全沒中＝與 4_worst_case_rescue_plan.csv 的退步定義完全重複（同一筆職缺、同一個正解），
        # 已改由該檔單獨涵蓋，這裡不重複產生訓練標籤，避免同一筆資料出現在兩份回饋檔。
        status_count['still_worst_dedup_skip'] += 1
        continue

    ideal = [correct_duty] + [r for r in current_recs if r != correct_duty]
    ideal = ideal[:10]
    while len(ideal) < 10: ideal.append('')
    current_padded = (current_recs + ['']*10)[:10]

    rows_out.append({
        '排序問題樣態': tag,
        '職缺名稱': o.get('職缺名稱',''),
        **{f'duty{j}': du[j] for j in range(5)},
        **{f'現有版本_推薦{j+1}': current_padded[j] for j in range(10)},
        **{f'理想推薦_{j+1}': ideal[j] for j in range(10)},
    })

print("殘餘案例分布:", status_count)
print("待新增列數:", len(rows_out))

# append to CSV
CSV_PATH = "/home/user/main/job-classification-kb/training_feedback/5_enhancement_reorder_plan.csv"
cols = ['排序問題樣態','職缺名稱','duty0','duty1','duty2','duty3','duty4'] + \
       [f'現有版本_推薦{j}' for j in range(1,11)] + [f'理想推薦_{j}' for j in range(1,11)]

with open(CSV_PATH, 'a', encoding='utf-8-sig', newline='') as f:
    w = csv.DictWriter(f, fieldnames=cols)
    for r in rows_out:
        w.writerow(r)

print("已附加至", CSV_PATH)
