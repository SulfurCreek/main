#!/usr/bin/env python3
"""深入分析「退步案例」（舊模型有命中/沾邊、新模型完全沒命中）的根因，
並輸出：①完整退步清單 MD（追蹤用）②依中類的 over-index 統計。
讀 MD 資料層（舊）+ 廠商提供的模型輸出 xlsx（新），逐列配對。
"""
import json
import re
from collections import Counter
from pathlib import Path

import pandas as pd

ROOT = Path("/home/user/main/job-classification-kb")
OLD_MD = ROOT / "tcode" / "data_職缺名稱_dutyMapping.md"
NEW_XLSX = "/root/.claude/uploads/6d643d58-f39d-53f8-a740-df69060d043b/a61c2155-________20260720.xlsx"
TREE_JSON = ROOT / "scripts" / "_dutynm_tree.json"
POP_STATS = ROOT / "scripts" / "_duty_accuracy_stats.json"
OUT_TRACKING_MD = ROOT / "tracking_退步案例_20260720.md"

DUTY = [f"duty{i}" for i in range(5)]
REC = [f"職類推薦{i}" for i in range(1, 11)]

tree = json.load(open(TREE_JSON, encoding="utf-8"))
leaf2cat = {}
for major, mids in tree.items():
    for mid, leaves in mids.items():
        for leaf in leaves:
            leaf2cat[leaf] = (major, mid)

pop_stats = json.load(open(POP_STATS, encoding="utf-8"))
pop_n = {(r["major"], r["mid"]): r["n"] for r in pop_stats["category_table"]}
total_pop = sum(pop_n.values())


def parse_md(path):
    lines = open(path, encoding="utf-8").read().splitlines()
    start, header = None, None
    for i, l in enumerate(lines):
        if l.startswith("| 職缺名稱"):
            header = [c.strip() for c in l.strip().strip("|").split("|")]
            start = i + 2
            break
    rows = []
    for l in lines[start:]:
        if not l.startswith("|"):
            continue
        cells = [c.strip() for c in l.strip("|").split("|")]
        if len(cells) != len(header):
            continue
        rows.append(dict(zip(header, cells)))
    return rows


def classify(duties_raw, recs_raw):
    duties = list(dict.fromkeys([d for d in duties_raw if d and str(d) != "nan"]))
    recs = [r for r in recs_raw if r and str(r) != "nan"]
    if not duties or not recs:
        return None
    sel = set(duties)
    n_sel = len(duties)
    fhr = None
    for i, r in enumerate(recs):
        if r in sel:
            fhr = i + 1
            break
    cov5 = len(sel & set(recs[:5]))
    if recs[0] in sel and cov5 == n_sel:
        sc = "best"
    elif fhr is not None and fhr > 5:
        sc = "enhance"
    elif fhr is None:
        sc = "worst"
    else:
        sc = "other_top5hit"
    return dict(sc=sc, recs=recs, duties=duties, fhr=fhr)


old_rows = parse_md(OLD_MD)
new_df = pd.read_excel(NEW_XLSX, sheet_name="Sheet1", dtype=str)
n = min(len(old_rows), len(new_df))

regressions = []
for i in range(n):
    o = old_rows[i]
    du = [o.get(c, "") for c in DUTY]
    ro = classify(du, [o.get(c, "") for c in REC])
    rn_row = new_df.iloc[i]
    rn = classify(du, [rn_row[c] if pd.notna(rn_row[c]) else "" for c in REC])
    if ro is None or rn is None:
        continue
    if ro["sc"] != "worst" and rn["sc"] == "worst":
        cat = leaf2cat.get(ro["duties"][0])
        new_cat = leaf2cat.get(rn["recs"][0])
        regressions.append({
            "title": o.get("職缺名稱", ""),
            "employeeNo": rn_row.get("employeeNo", ""),
            "old_scenario": ro["sc"],
            "duties": ro["duties"],
            "old_recs": ro["recs"],
            "new_recs": rn["recs"],
            "major": cat[0] if cat else "",
            "mid": cat[1] if cat else "",
            "new_top1_major": new_cat[0] if new_cat else "",
            "same_major": bool(cat and new_cat and cat[0] == new_cat[0]),
        })

print("total regressions:", len(regressions))

# ---- root-cause check 1: keyword hypothesis ----
kw_hit = sum(1 for r in regressions if "儲備" in r["title"])
print(f"含'儲備'關鍵字比例: {100*kw_hit/len(regressions):.1f}%（用來檢驗是否為關鍵字誤判驅動）")

DECO_RE = re.compile(r"[◎★☆【】()（）※□▲△○🔥📣👉🎵📞💰]")
deco_hit = sum(1 for r in regressions if DECO_RE.search(r["title"]))
print(f"含裝飾符號/emoji比例: {100*deco_hit/len(regressions):.1f}%")

# ---- root-cause check 2: over-index by mid category ----
mid_c = Counter((r["major"], r["mid"]) for r in regressions if r["mid"])
total_classified = sum(mid_c.values())
overindex_rows = []
for cat, n_reg in mid_c.items():
    if cat not in pop_n or pop_n[cat] < 200:
        continue
    reg_pct = 100 * n_reg / total_classified
    pop_pct = 100 * pop_n[cat] / total_pop
    idx = reg_pct / pop_pct
    overindex_rows.append((cat, n_reg, pop_n[cat], reg_pct, pop_pct, idx))
overindex_rows.sort(key=lambda x: -x[5])

print("\n=== over-index top10（n_pop>=200）===")
for cat, n_reg, n_pop, reg_pct, pop_pct, idx in overindex_rows[:10]:
    print(f"{cat}: 退步佔比{reg_pct:.1f}% / 母體佔比{pop_pct:.1f}% = {idx:.2f}x  ({n_reg}/{n_pop})")

# ---- same-major rate for the top-3 over-indexed categories ----
for target_cat, *_ in overindex_rows[:3]:
    sub = [r for r in regressions if (r["major"], r["mid"]) == target_cat]
    same_major_rate = 100 * sum(1 for r in sub if r["same_major"]) / len(sub)
    print(f"{target_cat}: 新推薦1 仍在同大類比例 = {same_major_rate:.1f}%（越低代表跳到越不相關領域）")

json.dump(regressions, open(ROOT / "scripts" / "_regressions_full.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print(f"\nsaved -> {ROOT / 'scripts' / '_regressions_full.json'}")

# ---- write full tracking MD ----
def esc(v):
    return str(v).replace("|", "／").replace("\n", " ").strip()

with open(OUT_TRACKING_MD, "w", encoding="utf-8") as f:
    f.write("# 退步案例追蹤清單（20260720 模型更新）\n\n")
    f.write(f"> 舊模型有命中/沾邊、新模型完全沒命中的職缺，共 {len(regressions)} 筆。")
    f.write("原始資料：舊=`tcode/data_職缺名稱_dutyMapping.md`，新=廠商提供 `a61c2155-…20260720.xlsx`。\n")
    f.write("> 分析與根因見 [`analysis_退步案例根因分析_20260720.md`](analysis_退步案例根因分析_20260720.md)；")
    f.write("給模型團隊的精簡清單見 [`feedback_模型退步問題清單_20260720.md`](feedback_模型退步問題清單_20260720.md)。\n\n")
    f.write("| 職缺名稱 | 廠商送出 | 舊情境 | 舊推薦(前3) | 新推薦(前3) | 大類 | 中類 | 新推薦1同大類 |\n")
    f.write("|---|---|---|---|---|---|---|---|\n")
    for r in regressions:
        f.write(
            f"| {esc(r['title'])} | {esc('、'.join(r['duties']))} | {r['old_scenario']} | "
            f"{esc('、'.join(r['old_recs'][:3]))} | {esc('、'.join(r['new_recs'][:3]))} | "
            f"{esc(r['major'])} | {esc(r['mid'])} | {'是' if r['same_major'] else '否'} |\n"
        )
print(f"saved -> {OUT_TRACKING_MD}")
