# -*- coding: utf-8 -*-
"""Step 2：補算回鍋率/慢性占比 → 產出 report_data.json → 注入 report_template.html 產出最終 HTML 報告。

用法：python3 step2_build_report.py <資料目錄>
<資料目錄> 需含 尾數{0-9}.csv、寄送廠商數.csv 與 step1 產出的 summary.json。
輸出：<資料目錄>/report_data.json 與 ../提醒信成效分析報告.html
"""
import json
import sys
from pathlib import Path

import pandas as pd

DATA_DIR = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
HERE = Path(__file__).parent
res = json.load(open(DATA_DIR / "summary.json", encoding="utf-8"))

# ---------- 補算：消失後回鍋率 ----------
bounce = []
for digit in range(10):
    df = pd.read_csv(DATA_DIR / f"尾數{digit}.csv", dtype={"廠商編號": str})
    df["日期"] = df["日期"].astype(str).str.strip().str.replace("　", "")
    dates = sorted(df["日期"].unique(), key=lambda s: (int(s.split("/")[0]), int(s.split("/")[1])))
    sets = [set(df[df["日期"] == d]["廠商編號"]) for d in dates]
    for i in range(len(sets) - 2):
        gone = sets[i] - sets[i + 1]
        later = set().union(*sets[i + 2:])
        back = gone & later
        bounce.append({"digit": digit, "transition": i + 1, "gone": len(gone), "came_back": len(back)})
res["bounceback"] = bounce

# ---------- 補算：慢性族群未讀占比（各批最後一輪） ----------
tot_last_unread = 0
chronic_last_unread = 0
for digit in range(10):
    df = pd.read_csv(DATA_DIR / f"尾數{digit}.csv", dtype={"廠商編號": str})
    df["日期"] = df["日期"].astype(str).str.strip().str.replace("　", "")
    dates = sorted(df["日期"].unique(), key=lambda s: (int(s.split("/")[0]), int(s.split("/")[1])))
    appear = df.groupby("廠商編號")["日期"].nunique()
    ch = set(appear[appear == len(dates)].index)
    last = df[df["日期"] == dates[-1]]
    tot_last_unread += last["未讀履歷數"].sum()
    chronic_last_unread += last[last["廠商編號"].isin(ch)]["未讀履歷數"].sum()
res["chronic_unread_share"] = {"chronic_unread": int(chronic_last_unread), "total_unread": int(tot_last_unread)}

# ---------- 彙總成圖表用 report_data.json ----------
out = {}
rt = pd.DataFrame(res["retention"])
bb = pd.DataFrame(res["bounceback"])
out["kpi"] = {
    "avg_gone_rate": round(rt["gone_rate"].mean(), 4),
    "total_transitions_n": int(rt["n"].sum()),
    "unique_vendors": sum(b["unique_vendors"] for b in res["batches"].values()),
    "chronic": sum(c["n_chronic"] for c in res["chronic"]),
    "chronic_unread": res["chronic_unread_share"]["chronic_unread"],
    "total_unread_last": res["chronic_unread_share"]["total_unread"],
    "back_rate": round(bb["came_back"].sum() / bb["gone"].sum(), 4),
}

g = rt.groupby("transition")["gone_rate"].agg(["mean", "min", "max", "count"])
out["retention_by_transition"] = [
    {"transition": int(t), "mean": round(v["mean"], 4), "min": round(v["min"], 4),
     "max": round(v["max"], 4), "batches": int(v["count"])}
    for t, v in g.iterrows()]

flow = []
for t in [1, 2]:
    r = rt[rt["transition"] == t]
    b = bb[bb["transition"] == t]
    n, stay, gone = int(r["n"].sum()), int(r["stay"].sum()), int(r["gone"].sum())
    back = int(b["came_back"].sum())
    flow.append({"transition": t, "n": n, "stay": stay, "gone_back": back, "gone_clean": gone - back})
out["flow"] = flow

im = pd.DataFrame(res["improvement"])
s = im.sum(numeric_only=True)
out["improvement"] = {
    "n_stay": int(s["n_stay"]),
    "unread": {"down": int(s["unread_down"]), "flat": int(s["unread_flat"]), "up": int(s["unread_up"])},
    "jobs": {"down": int(s["jobs_down"]), "flat": int(s["jobs_flat"]), "up": int(s["jobs_up"])},
}

p4 = {}
for d in map(str, range(9)):
    for k, v in res["batches"][d]["persistence"].items():
        p4[int(k)] = p4.get(int(k), 0) + v
out["persistence_4cycle"] = [{"times": k, "vendors": p4[k]} for k in sorted(p4)]
out["persistence_digit9"] = [{"times": int(k), "vendors": v}
                             for k, v in sorted(res["batches"]["9"]["persistence"].items(), key=lambda x: int(x[0]))]

bins = {}
for c in res["chronic"]:
    for k, v in c["dist"].items():
        bins[k] = bins.get(k, 0) + v
order = ["1-5", "6-10", "11-20", "21-50", "51-100", "100+"]
out["chronic_unread_bins"] = [{"bin": k, "vendors": bins[k]} for k in order]

out["overview"] = res["overview"]
out["first_last"] = [{"digit": int(d), "first": b["cycle_vendors"][0], "last": b["cycle_vendors"][-1],
                      "first_date": b["dates"][0], "last_date": b["dates"][-1], "n_cycles": b["n_cycles"]}
                     for d, b in res["batches"].items()]

json.dump(out, open(DATA_DIR / "report_data.json", "w", encoding="utf-8"), ensure_ascii=False)

# ---------- 注入模板 ----------
tpl = open(HERE / "report_template.html", encoding="utf-8").read()
html = tpl.replace("__DATA__", json.dumps(out, ensure_ascii=False))
target = HERE.parent / "提醒信成效分析報告.html"
open(target, "w", encoding="utf-8").write(html)
print(f"wrote {target} ({len(html.encode())} bytes)")
