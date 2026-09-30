# user-journey / html

`../recruiter_journey_map.md`（素材，只有文件助手能改內容）→ 自包含 HTML（成品輸出到上一層 `user-journey/`）。

| 檔案 | 作用 |
| :--- | :--- |
| `step1_parse_journey.py` | 解析素材（user-journey-map skill 三段式＋附錄）→ `report_data.json`；只搬運，不改寫、不補齊；〈路由〉是 AI 索引，不進 HTML |
| `report_template.html` | Journey map 看板版型（`__DATA__` 佔位符；不含 html/head/body 外框，可直接發布成 artifact；無外部資源） |
| `step2_build_report.py` | 注入資料 → `../recruiter_journey_report.html`（加外框與 UTF-8 charset）；`--fragment <路徑>` 另出無外框版給 artifact |
| `../recruiter_journey_report.html` | 成品（離線可開，深淺雙主題，手機可讀） |

重跑：`python3 step1_parse_journey.py && python3 step2_build_report.py`

規則：`US`／`US*`／`〔推論〕`／`NULL` 照原標記；素材格式若再改（見 skill〈下游〉），step1 要跟著改。圖片與標註不在本資料夾範圍（見 `../README.md`）。
