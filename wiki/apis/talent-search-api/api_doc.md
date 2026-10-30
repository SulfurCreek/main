# TalentSearch API — 分析文件（api_doc）

## 1. 概觀

| 項目 | 內容 |
| :--- | :--- |
| 用途 | 將文字分析為 1111 UI 範本，再以確定性方式編譯成用於人才搜尋的完整範本 |
| Spec 版本 | OpenAPI 3.1.0 / API `v2.0.0` |
| Spec 檔 | `spec/talent-search-api_v2.0.0.yaml` |
| 與 Talent Sourcing Gateway API（v1.0.1）的關係 | **不同服務**（title 不同：`TalentSearch API` vs `Talent Sourcing Gateway API`），非同一 API 的新版本，需獨立建 `wiki/apis/` 資料夾、獨立憑證 |
| 分析日期 | 2026-07-20 |

**⚠️ spec 未定義 `servers` 區塊** — 沒有 base URL／`apiId` 變數可用，實測前必須另外取得部署後的 API Gateway URL。

## 2. Auth

- `ApiKeyAuth`：header `x-api-key`，「使用一組共用 API Gateway 金鑰。`client_id` 是稽核上下文，不是授權選擇器」（spec 原文）。
- `GET /health` 無此 security 要求，但改用「來源 IP 允許清單」做存取控制（見 403 說明），與 v1 的「無 auth」不同。
- **憑證未知**：不確定是否與 v1（`TSG_API_KEY`／`TSG_API_ID`）共用同一把 key／同一個 API Gateway，需向使用者確認。

## 3. 端點表

| Method | Path | operationId | 摘要 | Auth |
| :--- | :--- | :--- | :--- | :--- |
| GET | `/health` | `health` | 健康狀態 | 無 security scheme，但限制來源 IP（403） |
| POST | `/v2/analyze` | `analyze_v2` | 將文字／職缺網址分析為完整搜尋範本 | ✅ `x-api-key` |
| POST | `/v2/search` | `search_v2` | 使用完整 UI 範本進行搜尋 | ✅ `x-api-key` |

## 4. 關鍵架構差異（v1 沒有的設計，測試前必讀）

### 4.1 `/v2/search` 不能只丟一個 URL 或文字——它要「完整 101 欄位範本」

`SearchRequest.search_template` 是 `SearchTemplate`：**101 個欄位的巨大結構**（工作地點、學歷、年齡、經歷×6組、語言、證照、駕照、身障條件……），而且 spec 明文規定：

> 「即使值為 `null` 或空 list，每個欄位仍須存在於 JSON 中。此設計刻意將 API 完整性與前端表單的必填規則分開。」

也就是說 **101 個欄位全部必填**（`required` 清單涵蓋幾乎所有欄位），只是允許值為 `null`／`[]`。**不能只送一個 `ai_query` 就當作合法 request**——除非自己手刻把其餘 100 個欄位都補上 `null`/`[]`。

### 4.2 正確測試流程是「先 analyze 再 search」

`/v2/analyze` 的職責就是把文字或職缺網址（跟 v1 `/v1/recommend` 的 `query` 同樣支援純文字／104／1111 網址／網址+文字）轉成**完整合法的 `search_template`**：

```
POST /v2/analyze  {"query": "<文字或104/1111網址>", "client_id": "..."}
  → 200 { "search_template": {...101欄位...}, "metadata": {...} }

POST /v2/search  {"client_id": "...", "search_template": <上一步整包塞回去>}
  → 200 { "recommendations": [...最多5筆...], "metadata": {...} }
```

**要測試「search 這隻的功能」用一個 104 職缺網址，必須先呼叫 `/v2/analyze` 取得 `search_template`，再把它原封不動放進 `/v2/search`。直接對 `/v2/search` 塞網址字串是不合法的請求（少了 100 個必填欄位）。**

### 4.3 與 v1 的其他關鍵差異

| 項目 | v1 `/v1/recommend` | v2 `/v2/search` |
| :--- | :--- | :--- |
| 推薦筆數上限 | 無上限（實測常見 50~250+ 筆） | **`maxItems: 5`**（最多只回 5 筆） |
| 推薦項目欄位 | talentNo／resumeGuid／final_score／rank | talentNo／resumeGuid／**rank**／**recommendation_reason**（可讀理由，可為 null）——**沒有 `final_score`** |
| metadata 的 source | 有 `source`（type/url/job_id） | **`SearchMetadata` 沒有 source 欄位**（來源資訊只在 `/v2/analyze` 的 `AnalyzeMetadata` 裡） |
| 排序診斷 | 無 | `ranking: {strategy, fallback_used}`（新增） |
| 自然語言解析診斷 | 無 | `/v2/analyze` 回傳 `nlq: {status: parsed/partial/fallback, applied_filters, ignored_filters, missing_information}`（新增） |
| 錯誤碼 | `ErrorDetail.code` 為固定 10 值 enum | `ErrorDetail.code` **只是 string，spec 未列舉列舉值**——需靠實測歸納 |

## 5. 參數與約束表

### 5.1 `/v2/analyze` Request — `AnalyzeRequest`

| 欄位 | 型別 | 必填 | 約束 |
| :--- | :--- | :--- | :--- |
| `query` | string | ✅ | 1–20000 字元；文字／支援的職缺網址／網址+補充文字 |
| `client_id` | string | ✅ | 1–64、pattern `^[A-Za-z0-9._-]+$` |

### 5.2 `/v2/analyze` Response — `AnalyzeResponse`

| 欄位 | 說明 |
| :--- | :--- |
| `search_template` | 完整 `SearchTemplate`（見 §5.4），可原樣放入 `/v2/search` |
| `metadata` | `AnalyzeMetadata`：`request_id`／`client_id`／`input_mode`(text/url/url_text)／`query_used`／`nlq`(NLQDiagnostics) |

### 5.3 `/v2/search` Request — `SearchRequest`

| 欄位 | 型別 | 必填 | 說明 |
| :--- | :--- | :--- | :--- |
| `client_id` | string | ✅ | 同上規則 |
| `search_template` | `SearchTemplate` | ✅ | 完整 101 欄位，通常直接沿用 `/v2/analyze` 的回傳 |

### 5.4 `SearchTemplate`（101 欄位，節錄關鍵幾類；完整清單見 spec）

| 欄位群 | 代表欄位 | 型別/約束 |
| :--- | :--- | :--- |
| AI 檢索原文 | `ai_query` | string，≤20000 字元，可空字串 |
| 全文檢索 | `corp_organ` | string，≤500 字元 |
| 地點 | `cityVal`／`liveVal` | tCodeCity 代碼陣列，≤10 項，**非 nullable，以 `[]` 表示未選**（跟其他多數陣列欄位不同！） |
| 職務類別 | `dutyVal` | tCodeDutyNM 代碼陣列，≤10 項，同樣非 nullable |
| 科系 | `majorVal` | tCodeMajor 代碼陣列，≤10 項，非 nullable |
| 學歷 | `grade`／`designateGrade` | enum 字串，**非 nullable**（其餘大多數欄位是 nullable） |
| 年齡 | `age0`／`age1` | string 數字，16–80 歲區間，`age1=99` 表不拘 |
| 年資 | `experience`／`experienceRestrict` | 代碼字串＋up/down/res |
| 工作經歷（6 組） | `expduty1~6`／`expyear1~6`／`expRestrict1~6` | 每組 4 欄位配對 |
| 技能／證照 | `skill`／`certify` | 代碼陣列 + `skillItem`/`certifyItem`(And/Or) |
| 語言 | `lang0` + `lang_des01~04` | 語言代碼 + 聽說讀寫程度 |
| 身障 | `disabledType0~2`／`disabledLevel0~2`／`disabledAids` | 3 組類別+等級配對 |
| 性別／婚姻／國籍 | `sex`／`marriage`／`nationality` | 皆 nullable enum |

**⚠️ 注意 nullable 不一致**：`dutyVal`／`cityVal`／`liveVal`／`majorVal`／`grade`／`designateGrade`／`age0`／`age1` 是**非 nullable**（schema 沒有 `anyOf null`），必須給實際值（陣列給 `[]`、字串給有效 enum 值）；其餘大多數欄位允許 `null`。手動組 `search_template` 時容易在這裡出錯。

### 5.5 `/v2/search` Response — `SearchResponse`

| 欄位 | 說明 |
| :--- | :--- |
| `recommendations` | 最多 **5 筆**，`RecommendationItem`：talentNo／resumeGuid／rank／recommendation_reason(nullable) |
| `metadata` | `SearchMetadata`：request_id／client_id／`suggestion`(QuerySuggestion，同 v1 三態)／`ranking`(strategy, fallback_used) |

## 6. 狀態面

| Enum | 值 | 出現於 |
| :--- | :--- | :--- |
| `input_mode` | text / url / url_text | AnalyzeMetadata |
| `nlq.status` | parsed / partial / fallback | AnalyzeMetadata.nlq |
| `suggestion.status` | not_needed / generated / unavailable | SearchMetadata.suggestion（與 v1 相同三態） |
| `skillItem`/`certifyItem`/`lan0Rule`/`lan1Rule`/`carLisenceRule` | And / Or | SearchTemplate |

HTTP status：`/v2/analyze` 與 `/v2/search` 皆定義 400／403／404／502／504；`error.code` **未列舉具體值**（不像 v1 有固定 10 碼），需實測歸納。

## 7. 測試矩陣（初版，待 analyze/search 串接驗證後補充案例編號）

| 分類 | 案例 | 預期 |
| :--- | :--- | :--- |
| A1 | `/health` | 200，`{"status":"ok"}`（若來源 IP 在允許清單內；否則 403） |
| A2 | `/v2/analyze` 純文字 query | 200，`input_mode=text`，`search_template.ai_query` 有值，`nlq.status` 有值 |
| A3 | `/v2/analyze` 104 URL query | 200，`input_mode=url`，`search_template` 含解析出的地點/職務等欄位 |
| B1 | 用 A3 的 `search_template` 呼叫 `/v2/search` | 200，`recommendations` ≤5 筆，含 `recommendation_reason` |
| B2 | `/v2/search` 直接塞裸字串（不先 analyze） | 預期 **400**（缺 101 必填欄位）——驗證「不能跳過 analyze」的假設 |
| C1 | `search_template` 中非 nullable 欄位（如 `dutyVal`）傳 `null` | 預期 400（違反 schema） |
| D1 | 缺 `x-api-key` 呼叫 analyze/search | 403 |

## 8. 版控表

| 日期 | Spec 版本 | 異動摘要 |
| :--- | :--- | :--- |
| 2026-07-20 | v2.0.0 | 初版分析：3 端點，識別出「search 需先 analyze 取得完整 101 欄位範本」的關鍵架構限制；servers 未定義，憑證待確認 |
