#!/usr/bin/env python3
"""從 MD 資料層抽出三種情境的原始資料，輸出 CSV 供推薦模型訓練回饋。
鐵則：只讀 MD 資料層（data_職缺名稱_dutyMapping.md），不碰 CSV/Excel。

情境（互斥）：
  1 best_practice ：職類推薦1 就命中，且廠商送出的所有職類 100% 都在前5名內（完美命中且全可見）
  2 enhancement   ：前5名完全沒命中，但廠商選擇出現在第6~10名（有推到，只是排序沒進 top5 → 該優化排序）
  3 worst_practice：推薦1~10 完全沒命中廠商任一選擇（不管同中類/大類，都算沒命中）
術語：推薦=AI語意推薦；duty0~4=廠商實際送出的職類。
"""
import csv
from pathlib import Path

ROOT = Path("/home/user/main/job-classification-kb")
DATA_MD = ROOT / "tcode" / "data_職缺名稱_dutyMapping.md"
OUT_DIR = ROOT / "training_feedback"
OUT_DIR.mkdir(exist_ok=True)

DUTY_COLS = [f"duty{i}" for i in range(5)]
REC_COLS = [f"職類推薦{i}" for i in range(1, 11)]


def parse_rows(path):
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    header, data_start = None, None
    for i, l in enumerate(lines):
        if l.startswith("| 職缺名稱"):
            header = [c.strip() for c in l.strip().strip("|").split("|")]
            data_start = i + 2
            break
    for l in lines[data_start:]:
        l = l.rstrip("\n")
        if not l.startswith("|"):
            continue
        cells = [c.strip() for c in l.strip("|").split("|")]
        if len(cells) != len(header):
            continue
        yield dict(zip(header, cells))


SCENARIOS = {
    "best_practice": "第一筆(職類推薦1)就命中，且廠商送出的所有職類100%都出現在前5名內（完美命中且全部可見）",
    "enhancement": "前5名完全沒命中，但廠商送出的職類出現在第6~10名（AI有推到、只是排序沒進top5，應優化排序把它調進前5）",
    "worst_practice": "AI推薦1~10完全沒命中廠商送出的任一職類（不管同中類、同大類，都算沒命中）",
}
OUT_COLS = ["情境", "職缺名稱"] + DUTY_COLS + REC_COLS + ["命中名次", "前5名覆蓋數", "廠商送出數"]

buckets = {k: [] for k in SCENARIOS}
seen = {k: set() for k in SCENARIOS}   # 去重（完全相同的整列不重複餵給訓練）
dup_removed = {k: 0 for k in SCENARIOS}
n_rows = 0

for row in parse_rows(DATA_MD):
    n_rows += 1
    title = row.get("職缺名稱", "")
    duties_raw = [row.get(c, "") for c in DUTY_COLS]
    duties = list(dict.fromkeys([d for d in duties_raw if d]))   # 去重保序
    recs = [row.get(c, "") for c in REC_COLS]
    recs_nonempty = [r for r in recs if r]
    if not duties or not recs_nonempty:
        continue
    sel_set = set(duties)
    n_sel = len(duties)

    first_hit_rank = None
    for idx, r in enumerate(recs_nonempty):
        if r in sel_set:
            first_hit_rank = idx + 1
            break
    covered_top5 = len(sel_set & set(recs_nonempty[:5]))

    scenario = None
    if recs_nonempty[0] in sel_set and covered_top5 == n_sel:
        scenario = "best_practice"
    elif first_hit_rank is not None and first_hit_rank > 5:
        scenario = "enhancement"
    elif first_hit_rank is None:
        scenario = "worst_practice"
    if scenario is None:
        continue

    key = (title, tuple(duties_raw), tuple(recs))
    if key in seen[scenario]:
        dup_removed[scenario] += 1
        continue
    seen[scenario].add(key)

    out = {
        "情境": scenario, "職缺名稱": title,
        **{c: row.get(c, "") for c in DUTY_COLS},
        **{c: row.get(c, "") for c in REC_COLS},
        "命中名次": first_hit_rank if first_hit_rank is not None else "",
        "前5名覆蓋數": covered_top5, "廠商送出數": n_sel,
    }
    buckets[scenario].append(out)

for scenario, rows in buckets.items():
    fname = {"best_practice": "1_best_practice.csv",
             "enhancement": "2_enhancement.csv",
             "worst_practice": "3_worst_practice.csv"}[scenario]
    with open(OUT_DIR / fname, "w", encoding="utf-8-sig", newline="") as f:
        f.write(f"# 情境：{scenario}｜說明：{SCENARIOS[scenario]}\n")
        w = csv.DictWriter(f, fieldnames=OUT_COLS)
        w.writeheader()
        w.writerows(rows)
    print(f"{fname}: {len(rows)} 列（去重移除 {dup_removed[scenario]}）")

print("total rows scanned:", n_rows)
