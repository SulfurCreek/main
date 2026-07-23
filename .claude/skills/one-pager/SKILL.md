---
name: one-pager
description: >
  把一個決策、比較、成效摘要或檢查清單，濃縮成「單張、橫式、高密度、5分鐘讀完並驅動一個行動」的
  視覺化 one-pager，**最終輸出 PNG 圖檔**（非 HTML）。只要使用者要「一頁式」「one pager」「單張圖」
  「決策海報」「懶人包」「一張圖看懂」「給主管/會議用的單張摘要」「把這份東西變成一張圖」，或要把
  報告/選項/方案/KPI 濃縮成一張可貼進簡報或群組的圖，就用本 skill。
  鐵則：出圖前一定先把「純文字大綱」列給使用者確認，核可後才產圖；產物是 PNG。
  關鍵字：one-pager、一頁式、單張圖、決策海報、懶人包、一張圖看懂、資訊圖、simple、摘要圖、PNG。
---

# One-Pager 產生器（單張 PNG 決策/摘要海報）

把資訊濃縮成**一張橫式圖**：讀者 5 分鐘看完、當場能做一個決策或行動。核心是「精煉」——
砍到只剩最關鍵的、排成一眼可掃的結構，最後輸出 **PNG 圖檔**。

> 與 `report-generator` 分工：report-generator 產「多段、可捲動、可搜尋」的 MD/HTML 報告；
> one-pager 產「單畫布、固定尺寸、給人看一眼、輸出 PNG」的海報。兩者共用「結論先行、精煉、
> 語意配色」的 DNA。圖表配色規範仍以官方 `dataviz` skill 為準。

## 🚦 兩道硬規則（絕對不可跳過）

1. **GATE①：出圖前先給純文字大綱等使用者確認。** 把整張圖的所有文字（kicker、大標、每欄名、
   每一列/每一格、解說卡、頁尾）用 markdown 列出來貼給使用者，**明確問「這樣的文字內容可以嗎？」**
   使用者核可（或改完再核可）後，才進到填模板、出圖。不要一次做到底。
2. **GATE②：最終交付是 PNG，不是 HTML。** HTML 只是中間鷹架，用完可丟；交付一定是 `.png`，
   用 `SendUserFile`（`display: render`）送出。

## 版型 DNA（五個由上而下的帶狀區塊）

所有 one-pager 共用同一套骨架，只有中間 **body** 換版型：

1. **kicker 情境列**：小字＋accent 直條。含情境定位＋「閱讀時間」（例：`… · 5 分鐘`）。
2. **大標**：巨大粗體，內含一段換色強調（`<em>…</em>`）。**標題講「要做的決策/結論」，不是主題**
   （✅`請勾：該不該上` ❌`負回饋選項說明`）。
3. **body（主角）**：四選一版型，見下。
4. **解說卡列（0~3 張）**：回答讀者「但為什麼／X 是什麼」的預期問題。**抽出來當卡片，不要塞進主表**。
5. **頁尾**：主要行動（按鈕樣）＋進度／圖例／頁碼。把「讀完要做什麼」講明。

視覺語言：深色、單一 accent（藍）、語意狀態色（綠=正向/通過、紅=排除/警示、琥珀=關鍵數值/期限）、
高密度但**每格短（中文 ≤ ~15 字）**、格內只粗體關鍵字、emoji 當列識別。

## 精煉方法（把資訊砍到只剩一張圖）

- **一列一決策單位**：每列自足，讀者能只看一列就行動。
- **欄位平行**：每一欄跨所有列回答**同一個問題**（例：這欄都在講「系統做什麼」）。
- **標題是結論不是主題**；頁尾把行動講明。
- **預期問題外掛成解說卡**，不污染主表。
- 砍字原則：能用詞就不用句、能用數字就不用形容詞、重複的字提到欄名去。

## 四種 body 版型與內容 JSON

內容用一份 JSON 描述，`layout` 決定 body 版型。四種：

| layout | 何時用 | body |
|---|---|---|
| `decision_matrix`（主，對齊範例） | 多選項各要一個 yes/no 決策 | 表頭＋N列，末欄勾選 chip |
| `comparison` | 2~4 方案並排比優劣 | 欄=方案、列=維度，格內語意色 |
| `kpi` | 一組成效數字一眼看完 | 大數字卡片列 |
| `checklist` | 上線前/交付前逐項確認 | 分組核取項＋狀態燈 |

共用欄位：`kicker`（字串）、`headline`（字串，可含 `<em>`）、`cards`（`[{title, body}]`，0~3 張）、
`footer`（`{action, progress, legend, page, note}`）。各版型專屬欄位：

```jsonc
// decision_matrix
"matrix": { "columns": ["…5欄名…"], "rows": [
  { "emoji":"💼", "option":"…", "action":"…（可含 <b>）", "ttl":"90/30 天",
    "learn":"…", "learn_status":"good|bad", "verdict":"check" } ] }
// comparison
"comparison": { "options":["方案A","方案B"], "rows":[
  { "dim":"成本", "cells":[ {"text":"低","status":"good"}, {"text":"高","status":"bad"} ] } ] }
// kpi
"kpi": { "tiles":[ {"label":"命中率","value":"79.7%","tone":"good|bad|accent","delta":"+17.9pp"} ] }
// checklist
"checklist": { "groups":[ {"title":"資料","items":[ {"text":"去重完成","state":"done|todo|warn"} ]} ] }
```

完整可跑範例：[`assets/example_decision_matrix.json`](assets/example_decision_matrix.json)（重現使用者提供的 7 選項海報）。

## 標準流程

1. **釐清目標**：這張圖要驅動什麼決策/傳達什麼摘要、誰讀、讀完的唯一行動是什麼；選 `layout`。
2. **精煉成純文字大綱**：把 kicker、大標、每欄名、每列每格、解說卡、頁尾全部寫成 markdown。
3. **🚦 GATE①：貼大綱給使用者，問「這樣可以嗎？」等核可**（改完再核可）。
4. 把核可內容寫成 `content.json`。
5. 產圖（在 skill 的 `assets/` 目錄跑，或把 assets 複製到工作區）：
   ```bash
   python3 assets/build.py content.json out.html
   NODE_PATH=/opt/node22/lib/node_modules node assets/render_png.js out.html out.png
   ```
6. **看 PNG**（用 Read 開圖）：檢查中文有無缺字（豆腐字）、欄位有無溢出/重疊、密度是否過擠。
   有問題就改 `content.json`（砍字）或微調 `template.html`，重跑步驟 5。
7. **🚦 GATE②：`SendUserFile`（`display: render`）交付 `.png`**。HTML 為暫存鷹架，不是交付物。

## 已定案的技術參數（不要隨意改）

- **畫布**：16:9 橫式 **2000×1125**；`render_png.js` 用 `deviceScaleFactor:2` → **4000×2250** 高解析 PNG。
- **字型**：系統 **文泉驛正黑（WenQuanYi Zen Hei）**——本環境唯一可靠的中文字型。粗體是瀏覽器合成，
  所以**靠字級大小拉出層次，不要依賴細字重**。不要嵌外部字型、不要連 CDN（維持自包含）。
- **render 路徑**：Chromium `/opt/pw-browsers/chromium`（勿 `playwright install`）；
  Playwright 在 `/opt/node22/lib/node_modules`（故 `NODE_PATH=/opt/node22/lib/node_modules`）。
- `render_png.js` 會攔截 pageerror／console error，有 JS 錯誤會 exit 非 0——**別忽略**。

## 反例對照

| ❌ 不要 | ✅ 要 |
|---|---|
| 直接做圖給使用者看 | 先列純文字大綱等核可（GATE①） |
| 交付 HTML 或截圖連結 | 交付 PNG 檔（GATE②） |
| 標題寫主題（「選項說明」） | 標題寫決策（「請勾：該不該上」） |
| 一格塞一整句話 | 一格 ≤ ~15 字，只粗體關鍵字 |
| 把「為什麼」解釋塞進主表 | 抽成底部解說卡 |
| 塞到 12+ 列硬擠一頁 | 超過負荷就拆兩張或改版型；一頁只講一件事 |
| 依賴細字重做層次 | 用字級大小＋語意色做層次（字型無細字重） |
