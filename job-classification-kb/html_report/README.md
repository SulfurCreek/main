# HTML 報告產出流程

把 `職類推薦精準度` 分析結果轉成可離線開啟的自包含 HTML 報告。

## 檔案

- `../scripts/analyze_duty_recommendation_accuracy.py` — 上游分析腳本，讀 MD 資料層、輸出 `../scripts/_duty_accuracy_stats.json`
- `report_data.json` — 從 `_duty_accuracy_stats.json` 篩選出報告要用的聚合數字（TL;DR、Top/Bottom 10 中類、可回收排行、文字特徵表、抽樣案例）
- `report_template.html` — 版面 + 圖表邏輯，內含 `__DATA__` 佔位符
- `build_report.py` — 把 `report_data.json` 注入 `report_template.html`，輸出 `../analysis_推薦精準度_報告.html`
- `shot.js` — Playwright 截圖腳本（深/淺色雙模驗證用，非必要不進版控）

## 重跑

```bash
# 1. 若上游資料變動，先重跑分析腳本
python3 ../scripts/analyze_duty_recommendation_accuracy.py

# 2. 重新產生 report_data.json（見腳本內聚合邏輯，或手動更新）

# 3. 注入模板出圖
python3 build_report.py

# 4.（選用）深/淺色截圖驗證
NODE_PATH=/opt/node22/lib/node_modules node shot.js
```

改樣式/圖表版面 → 改 `report_template.html`，不用重跑分析。
改分析邏輯/口徑 → 改上游 `analyze_duty_recommendation_accuracy.py`，重跑後同步更新 `report_data.json`。

## 已知限制

- 15,113 筆完全重複列未去重；10 筆 duty0 值本身填錯已排除於分類統計外。
- 圖表為純 SVG/CSS + vanilla JS，無外部 CDN 依賴，符合 CSP 自包含要求。
- 色盲安全驗證：`node <dataviz skill>/scripts/validate_palette.js "#2a78d6,#eda100,#e34948" --mode light` 與 `--mode dark` 皆通過（light 模式 yellow 對比度 WARN，已用直接數字標籤緩解）。
