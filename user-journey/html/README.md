# user-journey / html

`../recruiter_journey_map.md`（素材，只有文件助手能改內容）→ 自包含 HTML（成品輸出到上一層 `user-journey/`）。

| 檔案 | 作用 |
| :--- | :--- |
| `step0_fetch_sitemap.py` | 讀 HackMD [求才系統] Sitemap（需 `HACKMD_TOKEN`），輸出 `sitemap_docs.json`：各 Sitemap 模組掛的文件名稱＋shortId（不含頁面 URL、不存原文）；並依 journey map〈流程圖索引〉抓文件內 `## 流程圖` 的 mermaid，存 `flows/*.mmd` 並用 mermaid-cli 渲染成 `flows/*.svg`。離線重跑時可略過 |
| `step1_parse_journey.py` | 解析素材（user-journey-map skill 三段式＋附錄）→ `report_data.json`；只搬運，不改寫、不補齊；〈路由〉是 AI 索引，不進 HTML |
| `report_template.html` | Journey map 看板版型（`__DATA__` 佔位符；不含 html/head/body 外框，可直接發布成 artifact；無外部資源） |
| `step2_build_report.py` | 注入資料 → `../recruiter_journey_report.html`（加外框與 UTF-8 charset）；`--fragment <路徑>` 另出無外框版給 artifact |
| `../recruiter_journey_report.html` | 成品（離線可開，深淺雙主題，手機可讀） |

重跑：`python3 step0_fetch_sitemap.py`（Sitemap 有異動時）→ `python3 step1_parse_journey.py && python3 step2_build_report.py`

目前呈現規則（使用者指示）：痛點相關資訊（Pain Points 列、Persona 核心痛點、含「痛點」的缺口）與 Key Takeaways 段先不呈現，素材本身不改；獨立的「流程圖」區塊（在矩陣下方、跟隨階段篩選）依〈流程圖索引〉呈現已有的流程圖（目前只有 C 職缺的新增職缺流程），其餘階段留白。

規則：`US`／`US*`／`〔推論〕`／`NULL` 照原標記；素材格式若再改（見 skill〈下游〉），step1 要跟著改。圖片與標註不在本資料夾範圍（見 `../README.md`）。

## Sitemap 區塊（Journey 與流程圖之間）
- `step0_fetch_sitemap.py` 另解析 Sitemap 各節樹狀頁面名稱（`modules[].tree`，只留名稱與層級、不留 URL）。
- 預設全部模組顯示；選階段後對應模組亮起、其餘變淡。Touchpoints 列改為 Sitemap 頁面名稱，選階段後每個名稱為錨點，點擊捲到 Sitemap 節點。
- PC（≥1024px）左 Sitemap、右文件關係；流程圖進頁為空狀態，選階段後才載入。

## 2026-10-01 改版（路線圖版型）
- Hero 改成「招募路線圖」：站點＝階段篩選；捲動後頂部出現迷你路線列。改動與理由見 `MERIT.md`。
- 字體用 Google Fonts（Noto Sans TC／Archivo／IBM Plex Mono），都有系統字體 fallback，離線可讀。

## 2026-10-05 Persona 區塊重建
- md 的「1. Persona」整併了 Context 與術語表：step1 解析總覽矩陣、P1~P7、受限廠商類型、名詞；step0 另把附錄〈文件關係〉表讀進 `sitemap_docs.json`（`relations`）。
- 版面規則以 md 開頭的 `[SYSTEM: UI/UX RENDERING INSTRUCTIONS…]` 註解為準。persona 選定後，旅程看板依「可走的旅程」反灰；受限廠商卡可疊加。
- 「可走的旅程」文字由 `stage_states()` 轉成狀態（可走／部分／依權限／不可／NULL），只依文字照搬。
