# v10.2 三模型統整（2026-10-17）

> 單版本對 15 份 A 級職缺；不做版本比較。Gemini＝gemini-4-argon；ChatGPT 報告 model_id 為 unknown（依檔名格式判定）；Opus＝本 repo 子代理。

## 決定與 Level

| 職缺 | ChatGPT | Gemini | Opus |
| :-- | :-- | :-- | :-- |
| jd03 | interview 8 | interview 8 | interview 7 |
| jd09 | interview 8 | interview 8 | interview 8 |
| jd11 | interview 8 | interview 8 | interview 7 |
| jd14 | interview 7 | interview 7 | interview 7 |
| jd20 | interview 7 | **clarify 7** | interview 7 |
| jd26 | interview 8 | interview 7 | interview 7 |
| jd30 | interview 8 | interview 8 | interview 8 |
| jd31 | interview 8 | **clarify 7** | interview 8 |
| jd32 | interview 8 | interview 8 | interview 7 |
| jd34 | interview 8 | interview 8 | interview 7 |
| jd36 | interview 8 | interview 7 | interview 7 |
| jd40 | interview 8 | **clarify 7** | interview 7 |
| jd43 | interview 8 | **clarify 7** | interview 7 |
| jd44 | interview 8 | interview 7 | interview 7 |
| jd47 | interview 8 | interview 8 | interview 8 |

- 41/45 interview；4 份 clarify_first 全來自 Gemini（jd20、31、40、43）。
- 沒有任何一家給 Level 9。三家一致給 8 的：jd09、jd30、jd47；一致給 7 的：jd14。
- 三家共同的「最難」：jd20（B2B 年資、SQL、英文）；另 jd14（成長主責）、jd31／jd40（直接客戶、KA／NRE）。

## 共同缺口（≥2 家）

| 缺口 | ChatGPT | Gemini | Opus | 處理建議 |
| :-- | :-: | :-: | :-: | :-- |
| 1111 新版／群組／AI 上線後成效指標 | — | 12 份 | 8 份 | 有就補一個數字；沒有就面試說明，不硬加 |
| API／JSON／SQL 實作深度 | 5 份 | 7 份 | 6 份 | 可把已有的「外部合作 API 規格」（簽章、防重放、錯誤碼）寫成一句 |
| Jira／Confluence／指定工具 | 6 份 | 5 份 | 4 份 | 沒用過就不寫；面試說明內部工單流程 |
| 處理週期 100.4→30.9 天口徑 | 11 份 | — | （measurement） | 準備兩季件數、起訖、結案範圍 |
| 直接對外客戶／售前／KA | — | 5 份 | jd31、jd40 | 事實面待使用者確認有無 |
| 領域不符（支付法遵、零售、音樂） | 有 | 有 | 有 | 投遞取捨，不是改稿問題 |

## 單一模型提出、需留意
- Gemini 將冒用事件讀成「至 10 月零復發」——原句「依目前掌握的情況…未再出現同類冒用」仍可能被讀成零事件；可考慮改成「至 2026/10 未再接獲廠商回報同類冒用」（library 既定口徑）。
- ChatGPT：Peach 占比≠營收增加；Juicy DAU≠留存。屬面試口徑。

## ATS
- ChatGPT 實測雙欄 PDF：讀序仍有風險（職稱與日期被切開、「求職條件」跨頁）。投遞用單欄。
