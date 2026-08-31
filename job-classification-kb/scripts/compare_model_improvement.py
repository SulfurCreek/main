"""比較推薦模型調整前後三情境（best/enhancement/worst）改善。
新舊用同一套情境定義分類，只比佔比（樣本數不同）。
用法：python3 compare_model_improvement.py <新資料.xlsx>（省略則需自行改 NEW_XLSX）
"""
import sys
import pandas as pd
from pathlib import Path
from collections import Counter

OLD_MD = Path("/home/user/main/job-classification-kb/tcode/data_職缺名稱_dutyMapping.md")
NEW_XLSX = sys.argv[1] if len(sys.argv) > 1 else "調整後資料.xlsx"
DUTY = [f"duty{i}" for i in range(5)]
REC = [f"職類推薦{i}" for i in range(1, 11)]

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
    # multi-hit extras
    top1_primary = (fhr == 1 and recs[0] == duties[0])
    return dict(sc=sc, fhr=fhr, cov5=cov5, n_sel=n_sel,
               top5hit=(fhr is not None and fhr <= 5), top1hit=(fhr == 1),
               top1_primary=top1_primary)

def parse_md(path):
    lines = open(path, encoding="utf-8").read().splitlines()
    start = None; header = None
    for i, l in enumerate(lines):
        if l.startswith("| 職缺名稱"):
            header = [c.strip() for c in l.strip().strip("|").split("|")]; start = i + 2; break
    for l in lines[start:]:
        if not l.startswith("|"): continue
        cells = [c.strip() for c in l.strip("|").split("|")]
        if len(cells) != len(header): continue
        row = dict(zip(header, cells))
        yield [row.get(c, "") for c in DUTY], [row.get(c, "") for c in REC]

def summarize(rows):
    c = Counter(); tot = 0; top5 = 0; top1 = 0; top1p = 0; top1hit = 0
    cov_sum = 0.0; recall_sum = 0.0
    for du, re in rows:
        r = classify(du, re)
        if r is None: continue
        tot += 1
        c[r["sc"]] += 1
        if r["top5hit"]: top5 += 1
        if r["top1hit"]:
            top1 += 1
            if r["top1_primary"]: top1p += 1
        recall_sum += r["cov5"] / r["n_sel"]
    return dict(tot=tot, best=c["best"], enhance=c["enhance"], worst=c["worst"],
               other=c["other_top5hit"], top5=top5, top1=top1, top1p=top1p,
               recall=recall_sum)

old = summarize(parse_md(OLD_MD))
ndf = pd.read_excel(NEW_XLSX, sheet_name="Sheet1", dtype=str)
new_rows = [([ndf.at[i, c] for c in DUTY], [ndf.at[i, c] for c in REC]) for i in ndf.index]
new = summarize(new_rows)

def pc(n, d): return round(100 * n / d, 1)
for name, s in [("OLD(全量)", old), ("NEW(新樣本)", new)]:
    t = s["tot"]
    print(f"=== {name} n={t} ===")
    print(f"  命中率(前5名內)       : {pc(s['top5'],t)}%")
    print(f"  第1名就命中           : {pc(s['top1'],t)}%")
    print(f"  best_practice         : {pc(s['best'],t)}%  ({s['best']})")
    print(f"  enhancement(6-10)     : {pc(s['enhance'],t)}%  ({s['enhance']})")
    print(f"  worst_practice(沒命中): {pc(s['worst'],t)}%  ({s['worst']})")
    print(f"  other(前5中但非完美)  : {pc(s['other'],t)}%")
    print(f"  第1名命中打中主選比例 : {pc(s['top1p'],s['top1'])}%")
    print(f"  前5名平均覆蓋率       : {round(100*s['recall']/t,1)}%")
