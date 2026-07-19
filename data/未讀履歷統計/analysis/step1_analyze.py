# -*- coding: utf-8 -*-
"""提醒信成效分析：從尾數 0-9 明細 CSV 產出彙總 JSON（僅聚合統計，不輸出 raw data）。"""
import json
import pandas as pd

import sys
SCRATCH = sys.argv[1] if len(sys.argv) > 1 else "."  # 放置 尾數{0-9}.csv 與 寄送廠商數.csv 的目錄；summary.json 也輸出到這裡

# ---------- 總覽 ----------
overview = pd.read_csv(f"{SCRATCH}/寄送廠商數.csv")
overview.columns = [c.strip() for c in overview.columns]
overview["寄送廠商數"] = overview["寄送廠商數"].astype(str).str.strip().str.replace("　", "").astype(int)
overview["日期"] = overview["日期"].astype(str).str.strip().str.replace("　", "")

result = {
    "overview": overview.rename(columns={"日期": "date", "尾數": "digit", "寄送廠商數": "sent"}).to_dict("records"),
    "batches": {},
}

# 各尾數在總覽中的日期序（cycle 順序）
overview_dates = {d: g["日期"].tolist() for d, g in overview.groupby("尾數")}

validation = []
retention_rows = []       # 逐批逐 transition 的回流統計
persistence_total = {}    # 出現次數分佈（僅計 4-cycle 批次，另計 3-cycle）
improve_rows = []         # 連續出現者的改善度
chronic_unread_dist = []  # 慢性族群的未讀量級
composition_rows = []     # 各 cycle 新進 vs 重複

for digit in range(10):
    df = pd.read_csv(f"{SCRATCH}/尾數{digit}.csv", dtype={"廠商編號": str})
    df["日期"] = df["日期"].astype(str).str.strip().str.replace("　", "")
    dates = sorted(df["日期"].unique(), key=lambda s: (int(s.split("/")[0]), int(s.split("/")[1])))
    n_cycles = len(dates)

    # 驗證：明細 cycle 日期應與總覽該尾數日期一致、每 cycle 廠商數 = 總覽寄送數
    ov_dates = overview_dates.get(digit, [])
    for d in dates:
        n_detail = df[df["日期"] == d]["廠商編號"].nunique()
        n_rows = len(df[df["日期"] == d])
        ov_row = overview[(overview["尾數"] == digit) & (overview["日期"] == d)]
        n_ov = int(ov_row["寄送廠商數"].iloc[0]) if len(ov_row) else None
        validation.append({
            "digit": digit, "date": d, "detail_vendors": n_detail,
            "detail_rows": n_rows, "overview_sent": n_ov,
            "match": n_detail == n_ov,
        })

    # 每 cycle 廠商集合與個體彙總
    cyc = {}
    for i, d in enumerate(dates):
        g = df[df["日期"] == d].groupby("廠商編號").agg(
            jobs=("職缺數", "sum"), unread=("未讀履歷數", "sum")).reset_index()
        cyc[i] = g.set_index("廠商編號")

    batch = {"dates": dates, "n_cycles": n_cycles,
             "cycle_vendors": [len(cyc[i]) for i in range(n_cycles)],
             "cycle_unread_total": [int(cyc[i]["unread"].sum()) for i in range(n_cycles)],
             "cycle_jobs_total": [int(cyc[i]["jobs"].sum()) for i in range(n_cycles)]}

    # 回流率：cycle i -> i+1
    for i in range(n_cycles - 1):
        cur, nxt = set(cyc[i].index), set(cyc[i + 1].index)
        stay = cur & nxt
        gone = cur - nxt
        retention_rows.append({
            "digit": digit, "from_date": dates[i], "to_date": dates[i + 1],
            "transition": i + 1,  # 第幾次提醒之後
            "n": len(cur), "gone": len(gone), "stay": len(stay),
            "gone_rate": round(len(gone) / len(cur), 4),
        })
        # 組成：cycle i+1 中新進 vs 重複
        new = nxt - cur
        composition_rows.append({
            "digit": digit, "date": dates[i + 1], "cycle": i + 2,
            "total": len(nxt), "returning": len(stay), "new": len(new),
        })
        # 連續出現者改善度
        a = cyc[i].loc[list(stay)]
        b = cyc[i + 1].loc[list(stay)]
        d_unread = b["unread"] - a["unread"]
        d_jobs = b["jobs"] - a["jobs"]
        improve_rows.append({
            "digit": digit, "transition": i + 1, "n_stay": len(stay),
            "unread_down": int((d_unread < 0).sum()),
            "unread_flat": int((d_unread == 0).sum()),
            "unread_up": int((d_unread > 0).sum()),
            "jobs_down": int((d_jobs < 0).sum()),
            "jobs_flat": int((d_jobs == 0).sum()),
            "jobs_up": int((d_jobs > 0).sum()),
        })

    # 持續性：每廠商出現 cycle 數
    appear = df.groupby("廠商編號")["日期"].nunique()
    dist = appear.value_counts().sort_index().to_dict()
    batch["persistence"] = {int(k): int(v) for k, v in dist.items()}
    batch["unique_vendors"] = int(appear.shape[0])

    # 慢性族群（每個 cycle 都出現）的最後一個 cycle 未讀量級
    chronic_ids = set(appear[appear == n_cycles].index)
    if chronic_ids:
        last = cyc[n_cycles - 1]
        ch = last.loc[last.index.isin(chronic_ids), "unread"]
        bins = [0, 5, 10, 20, 50, 100, float("inf")]
        labels = ["1-5", "6-10", "11-20", "21-50", "51-100", "100+"]
        cut = pd.cut(ch, bins=bins, labels=labels).value_counts().reindex(labels)
        chronic_unread_dist.append({"digit": digit, "n_chronic": len(chronic_ids),
                                    "dist": {k: int(v) for k, v in cut.items()}})
    result["batches"][str(digit)] = batch

result["validation"] = validation
result["retention"] = retention_rows
result["composition"] = composition_rows
result["improvement"] = improve_rows
result["chronic"] = chronic_unread_dist

with open(f"{SCRATCH}/summary.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=1)

# ---- console 摘要（僅聚合數字） ----
mismatch = [v for v in validation if not v["match"]]
print(f"validation mismatches: {len(mismatch)}")
for m in mismatch[:15]:
    print("  ", m)

rt = pd.DataFrame(retention_rows)
print("\n回流率（gone_rate）by transition:")
print(rt.groupby("transition")["gone_rate"].agg(["mean", "min", "max", "count"]).round(3))
print("\n全體平均 gone_rate:", round(rt["gone_rate"].mean(), 4))

im = pd.DataFrame(improve_rows)
tot = im[["n_stay", "unread_down", "unread_flat", "unread_up"]].sum()
print("\n連續出現者未讀變化：", dict(tot))

pers = {}
for b in result["batches"].values():
    for k, v in b["persistence"].items():
        pers[k] = pers.get(k, 0) + v
print("\n出現次數分佈（全批合計）:", dict(sorted(pers.items())))
print("chronic per batch:", [(c['digit'], c['n_chronic']) for c in chronic_unread_dist])
