import pandas as pd
from collections import Counter

OLD_MD = "/home/user/main/job-classification-kb/tcode/data_職缺名稱_dutyMapping.md"
NEW_XLSX = "/root/.claude/uploads/6d643d58-f39d-53f8-a740-df69060d043b/a61c2155-________20260720.xlsx"
DUTY = [f"duty{i}" for i in range(5)]
REC = [f"職類推薦{i}" for i in range(1, 11)]

def parse_md(path):
    lines = open(path, encoding="utf-8").read().splitlines()
    start=None; header=None
    for i,l in enumerate(lines):
        if l.startswith("| 職缺名稱"):
            header=[c.strip() for c in l.strip().strip("|").split("|")]; start=i+2; break
    rows=[]
    for l in lines[start:]:
        if not l.startswith("|"): continue
        cells=[c.strip() for c in l.strip("|").split("|")]
        if len(cells)!=len(header): continue
        rows.append(dict(zip(header,cells)))
    return rows

def classify(duties_raw, recs_raw):
    duties = list(dict.fromkeys([d for d in duties_raw if d and str(d) != 'nan']))
    recs = [r for r in recs_raw if r and str(r) != 'nan']
    if not duties or not recs:
        return None
    sel = set(duties); n_sel = len(duties)
    fhr = None
    for i, r in enumerate(recs):
        if r in sel:
            fhr = i + 1; break
    cov5 = len(sel & set(recs[:5]))
    if recs[0] in sel and cov5 == n_sel:
        sc = "best"
    elif fhr is not None and fhr > 5:
        sc = "enhance"
    elif fhr is None:
        sc = "worst"
    else:
        sc = "other_top5hit"
    top5hit = fhr is not None and fhr <= 5
    return dict(sc=sc, fhr=fhr, cov5=cov5, n_sel=n_sel, top5hit=top5hit,
               top1hit=(fhr==1), top1_primary=(fhr==1 and recs[0]==duties[0]))

old_rows = parse_md(OLD_MD)
new_df = pd.read_excel(NEW_XLSX, sheet_name="Sheet1", dtype=str)

n = min(len(old_rows), len(new_df))
transition = Counter()
old_summary = Counter(); new_summary = Counter()
old_top5=old_top1=old_top1p=0; new_top5=new_top1=new_top1p=0
old_recall=0.0; new_recall=0.0
classified = 0

for i in range(n):
    o = old_rows[i]
    du = [o.get(c,'') for c in DUTY]
    ro = classify(du, [o.get(c,'') for c in REC])
    rn_row = new_df.iloc[i]
    rn = classify(du, [rn_row[c] if pd.notna(rn_row[c]) else '' for c in REC])
    if ro is None or rn is None:
        continue
    classified += 1
    transition[(ro['sc'], rn['sc'])] += 1
    old_summary[ro['sc']] += 1; new_summary[rn['sc']] += 1
    if ro['top5hit']: old_top5 += 1
    if rn['top5hit']: new_top5 += 1
    if ro['top1hit']:
        old_top1 += 1
        if ro['top1_primary']: old_top1p += 1
    if rn['top1hit']:
        new_top1 += 1
        if rn['top1_primary']: new_top1p += 1
    old_recall += ro['cov5']/ro['n_sel']
    new_recall += rn['cov5']/rn['n_sel']

def pc(x,d): return round(100*x/d,1)
print("paired rows classified:", classified)
print()
print("=== OLD vs NEW (同一批職缺，逐列配對) ===")
print(f"{'指標':30s} {'舊':>8s} {'新':>8s} {'差':>8s}")
def line(label, o, n_):
    print(f"{label:30s} {pc(o,classified):>7.1f}% {pc(n_,classified):>7.1f}% {pc(n_,classified)-pc(o,classified):>+7.1f}pp")
line("命中率(前5名內)", old_top5, new_top5)
line("第1名就命中", old_top1, new_top1)
line("best_practice", old_summary['best'], new_summary['best'])
line("enhancement(6-10)", old_summary['enhance'], new_summary['enhance'])
line("worst_practice(沒命中)", old_summary['worst'], new_summary['worst'])
print(f"{'第1名命中打中主選比例':30s} {pc(old_top1p,old_top1):>7.1f}% {pc(new_top1p,new_top1):>7.1f}%")
print(f"{'前5名平均覆蓋率':30s} {round(100*old_recall/classified,1):>7.1f}% {round(100*new_recall/classified,1):>7.1f}%")

print()
print("=== 逐列轉移矩陣（舊情境 -> 新情境，筆數）===")
labels = ['best','enhance','worst','other_top5hit']
print(f"{'舊->新':15s}", *[f"{l:>15s}" for l in labels])
for lo in labels:
    row = [transition.get((lo,ln),0) for ln in labels]
    print(f"{lo:15s}", *[f"{v:>15d}" for v in row])

print()
print("worst -> best/enhance/other(救回)：", sum(transition.get(('worst',x),0) for x in ['best','enhance','other_top5hit']))
print("worst -> worst(仍沒命中)：", transition.get(('worst','worst'),0))
print("best -> worst(退步)：", transition.get(('best','worst'),0))
print("enhance -> worst(退步)：", transition.get(('enhance','worst'),0))
print("other -> worst(退步)：", transition.get(('other_top5hit','worst'),0))
