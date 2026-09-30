# user-journey / html

`../recruiter_journey_map.md`（素材，只有 HackMD 文件 session 能改內容）→ 自包含 HTML（成品輸出到上一層 `user-journey/`）。

| 檔案 | 作用 |
| :--- | :--- |
| `step1_parse_journey.py` | 解析素材 MD → `report_data.json`（只搬運，不改寫、不補齊；並輸出「§3 引用但 §4 未列」自檢） |
| `report_template.html` | 版面模板（`__DATA__` 佔位符；內含五層面視覺規格註解；無外部 CDN／字型） |
| `step2_build_report.py` | 注入資料 → `recruiter_journey_report.html` |
| `../recruiter_journey_report.html` | 成品（放在 user-journey/ 底下；離線可開，深淺雙主題，手機可讀） |

重跑：`python3 step1_parse_journey.py && python3 step2_build_report.py`

規則：`US`／`US*`／`NULL` 照原標記；素材缺口與自檢發現只回報，不在此修正；圖片與標註不在本資料夾範圍（見 `../README.md`）。
