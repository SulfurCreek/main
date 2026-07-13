---
name: report-generator
description: >
  把 CSV/Excel 等原始數據轉成一份可離線開啟、自包含（self-contained）的靜態 HTML 分析報告。
  當任務是「產生報告」「做一個 HTML 頁面呈現數據／分析結果」「視覺化成效分析」，且不是規格書
  （`spec-doc-1111`）也不是單純數據分析結論（`pm-toolkit` 模組 C）時使用——本 skill 收錄的是
  「數據 → 聚合統計 → 圖表 → 可重跑 pipeline」這條產出鏈的實作經驗，圖表視覺規則一律以官方
  `dataviz` skill 為準，本檔不重複、只收流程與本 repo 特有的踩坑教訓。
  觸發詞：「產出 HTML 報告」「視覺化」「dashboard」「成效分析報告」「圖表報告」。
---

# 靜態 HTML 報告產生器（report-generator）

來源：實作「未讀履歷提醒信成效分析報告」時的經驗（`data/未讀履歷統計/提醒信成效分析報告.html`
與其 `analysis/` pipeline 為參考範例，可直接抄結構）。

## 標準流程

1. **原始資料留在磁碟，不進 context**：依 `wiki/master_prompt.md` 的「Excel/CSV 漸進式分析」
   規範，用 pandas 讀取、聚合，只把**聚合後的統計數字**（不是逐列 raw data）寫成一份中繼
   `summary.json` / `report_data.json`。所有中間運算（分組、比率、分佈）都在 Python 裡做完。
2. **先讀 `dataviz` skill 再寫任何圖表**：形式選擇（`choosing-a-form.md`）、色彩指定
   （`color-formula.md`）、色盲安全驗證（`node scripts/validate_palette.js "<hex,...>" --mode light/dark`
   ——兩個 mode 都要跑）、mark 規格與間距（`marks-and-anatomy.md`）、hover/tooltip
   （`interaction.md`）、上線前對照 `anti-patterns.md` 逐條檢查。不要跳過驗證腳本用肉眼判斷。
3. **模板 + 資料注入分離**：寫一份 `report_template.html`，內含 `__DATA__` 佔位符；一支
   build script 讀聚合 JSON、`json.dumps` 後字串替換注入，輸出最終 HTML。好處：改樣式不用重跑
   分析，改分析邏輯不用碰版面。
4. **深淺色雙模一定要用 Playwright 截圖驗證，不能只憑 CSS 邏輯推測**：
   ```js
   const p = await browser.newPage({ colorScheme: 'dark' }); // 'light' 另開一次
   await p.goto('file://' + path); await p.screenshot({ path: 'shot-dark.png', fullPage: true });
   ```
   本專案已有 Chromium：`executablePath: '/opt/pw-browsers/chromium'`（見系統環境設定，不要
   `playwright install`）。**必看兩張截圖**，逐張檢查有無：
   - 文字被圖形元素（誤差線、gridline）穿過或重疊（實際踩過的坑：長條圖上方數值標籤被
     min-max 誤差線的鬚穿過，改成貼齊誤差線頂端才修好）
   - label/tooltip 溢出容器、深色模式下對比度不足
   - `page.on('pageerror'/'console')` 監聽有沒有 JS 錯誤
5. **自包含（self-contained）鐵律**：CSP 情境下無法載外部 CDN/字型/圖片。CSS 用
   `<style>` 內嵌、圖表用純 SVG＋vanilla JS（不依賴 D3/Chart.js 等外部庫）、`prefers-color-scheme`
   做預設＋`:root[data-theme]` 做手動切換覆蓋（雙向都要贏）。
6. **Pipeline 要能重跑，不是一次性產物**：拆成 `stepN_xxx.py`（分析）與
   `stepM_build_report.py`（注入模板出圖），加一份 `README.md` 寫清楚輸入資料目錄結構、
   執行指令、已知資料落差／清洗規則。驗證方式：重跑一次比對輸出是否 byte-identical。
7. **交付**：檔案存進 repo 對應資料夾＋更新 `.claude_index.md`；同時用 `SendUserFile`
   （`display: render`）把 HTML 送給使用者當場預覽，不要只給檔案路徑。

## 報告內容準則（非圖表視覺，是敘事結構）

- 開頭一律先給 **TL;DR 結論句**（含關鍵數字），再展開方法論與圖表——不要讓讀者滑到最後才知道結論
- 若分析基於代理指標（proxy，例如「消失＝已讀」這種無法直接觀測的推論），**必須有獨立一節
  列出限制聲明**，且每個關鍵數字附近要能回頭對照這些限制，不能只在開頭寫一次就假裝結論是鐵板
- 結尾一定要有「建議的產品行動方案」（依 `pm-toolkit` 模組 C 的行動導向原則），不能停在數字覆述
- 全文繁體中文（台灣），沿用 `pm-toolkit`〈通用輸出原則〉

## 與既有 skill 的分工

| 面向 | 權威來源 |
| :--- | :--- |
| 圖表形式/配色/mark/互動規範 | 官方 `dataviz` skill（本檔不重複） |
| 數據分析的敘事準則（指標結構化、行動導向結論） | `pm-toolkit` 模組 C |
| CSV/Excel 漸進式分析、raw data 不進 context | `wiki/master_prompt.md` |
| 規格書格式（若報告其實是規格書） | `spec-doc-1111`（本 skill 不適用） |
