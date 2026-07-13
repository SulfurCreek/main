#!/usr/bin/env python3
"""從 ../scripts/_duty_accuracy_stats.json 篩出報告要用的聚合數字，輸出 report_data.json。
術語：推薦=AI語意推薦；實際選擇=廠商送出的職類。上游改分析邏輯後重跑本檔。
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
STATS = json.loads((HERE.parent / "scripts" / "_duty_accuracy_stats.json").read_text(encoding="utf-8"))

g = STATS["global_levels"]
n = sum(g.values())
top1 = g["top1"]; top5 = top1 + g["top3"] + g["top5"]
only6_10 = g["top10"]; top10 = top5 + only6_10
overall = {
    "n_total": n,
    "top1": top1, "top1_pct": round(100 * top1 / n, 1),
    "top5": top5, "top5_pct": round(100 * top5 / n, 1),
    "gap6_10": only6_10, "gap6_10_pct": round(100 * only6_10 / n, 1),
    "top10": top10, "top10_pct": round(100 * top10 / n, 1),
    "miss_mid": g["沾邊_中類"], "miss_mid_pct": round(100 * g["沾邊_中類"] / n, 1),
    "miss_major": g["沾邊_大類"], "miss_major_pct": round(100 * g["沾邊_大類"] / n, 1),
    "miss_far": g["無關"], "miss_far_pct": round(100 * g["無關"] / n, 1),
}
overall["miss_total_pct"] = round(overall["miss_mid_pct"] + overall["miss_major_pct"] + overall["miss_far_pct"], 1)

mh = STATS["multi_hit"]
hd = mh["hits_in_top5_dist"]
# 命中職缺中，覆蓋幾個廠商選擇的分佈（排除0）
hit_total = sum(int(v) for k, v in hd.items() if k != "0")
multi_hit = {
    "avg_selected": mh["avg_selected"],
    "n_selected_dist": mh["n_selected_dist"],
    "top1_hit_total": mh["top1_hit_total"],
    "top1_matched_primary": mh["top1_matched_position"]["0"],
    "top1_matched_primary_pct": mh["top1_matched_primary_pct"],
    "top1_matched_secondary_pct": round(100 - mh["top1_matched_primary_pct"], 1),
    "hit_total": hit_total,
    "cover1": int(hd.get("1", 0)), "cover1_pct": round(100 * int(hd.get("1", 0)) / hit_total, 1),
    "cover2": int(hd.get("2", 0)), "cover2_pct": round(100 * int(hd.get("2", 0)) / hit_total, 1),
    "cover3plus": sum(int(hd.get(k, 0)) for k in ("3", "4", "5")),
    "cover3plus_pct": round(100 * sum(int(hd.get(k, 0)) for k in ("3", "4", "5")) / hit_total, 1),
    "avg_recall_top5_pct": round(mh["avg_recall_top5"] * 100, 1),
    "multi_select_jobs": mh["multi_select_jobs"],
    "multi_select_2plus_covered_pct": mh["multi_select_2plus_covered_pct"],
}

cat = [r for r in STATS["category_table"] if r["n"] >= 300]
worst = sorted(cat, key=lambda x: x["top5_cum_pct"])[:10]
best = sorted(cat, key=lambda x: -x["top5_cum_pct"])[:5]
reorder = sorted(cat, key=lambda x: -x["recoverable_6_10_pct"])[:10]

def slim(r):
    return {"major": r["major"], "mid": r["mid"], "n": r["n"],
            "top5": r["top5_cum_pct"], "gap": r["recoverable_6_10_pct"],
            "top10": r["top10_cum_pct"], "miss_far": r["irrelevant_pct"]}

feat = [{"feature": f["feature"], "n": f["n"], "miss_rate": f["miss_rate_pct"], "lift": f["lift_vs_baseline"]}
        for f in sorted(STATS["feature_table"], key=lambda r: -(r["lift_vs_baseline"] or -999))]

# 每個指標的定義 + 一句舉例（廠商送出 vs AI推薦 的情境）
level_examples = [
    {"level": "AI 第1筆就命中", "desc": "AI 推薦的第1個，就是廠商送出的職類之一",
     "example": "廠商送出「業務助理」，AI 推薦第1個就是「業務助理」"},
    {"level": "前5名內命中（真命中率，主指標）", "desc": "廠商送出的職類出現在 AI 推薦前5名以內——前端只顯示5筆",
     "example": "廠商送出「業務助理」，AI 前5個裡有「業務助理」（不論排第幾）"},
    {"level": "命中但看不到（第6~10名）", "desc": "AI 有推到廠商送的職類，但排到第6~10名、前端不顯示",
     "example": "廠商送「牙醫助理」，AI 排到第6名，畫面只顯示前5個，看不到"},
    {"level": "前10名內命中（僅驗證方向）", "desc": "出現在 AI 全部10個推薦裡任一個，只用來確認方向對不對",
     "example": "把上面兩項加起來"},
    {"level": "沒命中·近同中類", "desc": "前10名都沒廠商送的職類，AI 只推到同中類的別的職類——仍是沒命中",
     "example": "廠商送「餐飲服務人員」，AI 只推同屬餐飲的「調酒師／吧台人員」"},
    {"level": "沒命中·近同大類", "desc": "前10名都沒中，AI 只推到同大類的別的職類——仍是沒命中",
     "example": "廠商送「業務助理」，AI 只推同屬業務的「客服人員」"},
    {"level": "沒命中·完全不同領域", "desc": "AI 推薦與廠商送的連大方向都搭不上",
     "example": "廠商送「保全人員／警衛」，AI 推「電機技師／工程師」"},
]

examples = {
    "literal_hit_pushed_down": [
        {"title": "牙醫助理", "answer": "牙醫助理", "rank": 6,
         "top5": ["牙醫師", "牙體技術人員", "其他醫療從業人員", "護理師", "醫事檢驗師"]},
        {"title": "美編設計人員【連鎖加盟總部 擴大徵才】", "answer": "美編人員", "rank": 8,
         "top5": ["平面設計", "設計主管", "建築繪圖／設計", "軟體專案主管", "CAD／CAM工程師"]},
    ],
    "noise_pushed_down": [
        {"title": "🎵 卡比音樂工作室｜儲備幹部招募（士林）", "answer": "儲備幹部", "rank": 7,
         "top5": ["調酒師／吧台人員", "店長／門市管理人員", "品管／品保主管", "餐飲主管", "侍酒師"]},
        {"title": "(找合作)國際進口產品專業人員", "answer": "國貿人員", "rank": 6,
         "top5": ["神秘客", "客服工程師", "國外業務人員", "工業設計", "資材人員"]},
    ],
    "full_ad_text_miss": [
        {"title": "W【日班安全室組長】中壢工業區：工廠，薪62,000元/月上班24天(288H)，有供餐及特休",
         "selected": "保全人員／警衛", "top3": ["智慧製程工程師", "電機技師／工程師", "電機設備裝配員"]},
        {"title": "產線儲備幹部(冷氣廠房.供餐)", "selected": "機械操作人員",
         "top3": ["智慧製程工程師", "生管主管", "電機技師／工程師"]},
    ],
    "new_title_not_in_codebook": [
        {"title": "社區經理-北區(鄰近科博館)", "selected": "總幹事",
         "top3": ["社群經營人員", "金融營業人員", "資材主管"]},
    ],
}

out = {"overall": overall, "multi_hit": multi_hit, "level_examples": level_examples,
       "worst": [slim(r) for r in worst], "best": [slim(r) for r in best],
       "reorder": [slim(r) for r in reorder], "features": feat, "examples": examples,
       "baseline_miss_rate": STATS["baseline_miss_rate_pct"]}
(HERE / "report_data.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print("wrote report_data.json")
print("multi_hit:", json.dumps(multi_hit, ensure_ascii=False))
