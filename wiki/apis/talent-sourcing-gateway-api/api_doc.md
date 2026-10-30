# Talent Sourcing Gateway API — 分析文件（api_doc）

## 1. 概觀

| 項目 | 內容 |
| :--- | :--- |
| 用途 | 將純文字、104 職缺網址、1111 職缺網址，或「職缺網址＋補充文字」轉成 TalentRecommendation 查詢，回傳精簡的人才推薦結果 |
| Spec 版本 | OpenAPI 3.0.3 / API `v1.0.1` |
| Spec 檔 | `spec/talent-sourcing-ateway-api_v1.0.1@20260717.yaml`（原檔名 "ateway" 為上游拼字，保留） |
| 分析日期 | 2026-07-20 |

## 2. Servers 與 Auth

- Base URL：`https://{apiId}.execute-api.ap-northeast-1.amazonaws.com/dev`（AWS API Gateway dev stage；`apiId` 由 CloudFormation output 取得，走環境變數 `TSG_API_ID`）
- Auth：`ApiKeyAuth` — header `x-api-key`（走環境變數 `TSG_API_KEY`）
- 例外：`GET /health` 明示 `security: []`（**無 auth**）

## 3. 端點表

| Method | Path | operationId | 摘要 | Auth |
| :--- | :--- | :--- | :--- | :--- |
| POST | `/v1/recommend` | `recommendTalents` | 依職缺需求推薦人才 | ✅ `x-api-key` |
| GET | `/health` | `healthCheck` | Lambda 存活檢查（不檢查/揭露下游與 Secret） | ❌ 無 |

`/v1/recommend` 業務規則（spec description 明載）：
- `query` 三種輸入模式：①純文字 ②單一 104／1111 職缺網址 ③單一職缺網址＋補充文字。
- **一次只能包含一個網址**。
- 零筆推薦回 **200＋空陣列**，並在 `metadata.suggestion` 給下一輪建議；**不會自動改寫後重查**。

## 4. 參數與約束表

### 4.1 Request — `RecommendRequest`（`additionalProperties: false`，required: `query`, `client_id`）

| 欄位 | 型別 | 必填 | 約束 | 說明 |
| :--- | :--- | :--- | :--- | :--- |
| `query` | string | ✅ | minLength 1、maxLength **20000** | 純文字／單一 104 或 1111 職缺網址／網址＋補充文字 |
| `client_id` | string | ✅ | minLength 1、maxLength **64**、pattern `^[A-Za-z0-9._-]+$` | 呼叫端識別碼（audit/追蹤/預留 rate-limit）；非認證資訊，v1 不實作 per-client rate limit |

### 4.2 Response 200 — `RecommendResponse`（`additionalProperties: false`，required: `recommendations`, `metadata`）

| 欄位 | 型別 | 必填 | 約束 | 說明 |
| :--- | :--- | :--- | :--- | :--- |
| `recommendations` | array\<`RecommendationItem`> | ✅ | — | 依 `rank` **升冪**；零結果為空陣列 |
| `metadata` | `RecommendMetadata` | ✅ | — | 見 4.4 |

### 4.3 `RecommendationItem`（`additionalProperties: false`，required 全欄位）

| 欄位 | 型別 | 約束 | 說明 |
| :--- | :--- | :--- | :--- |
| `talentNo` | string | minLength 1 | 人才編號 |
| `resumeGuid` | string | minLength 1 | 履歷唯一識別碼 |
| `final_score` | number (double) | — | TalentRecommendation 最終分數 |
| `rank` | integer (int32) | minimum 1 | 排序名次，越小越優先 |

### 4.4 `RecommendMetadata`（`additionalProperties: false`，required 全 8 欄）

| 欄位 | 型別 | 約束 | 說明 |
| :--- | :--- | :--- | :--- |
| `request_id` | string | minLength 1 | API Gateway request ID；本地執行由應用程式產生 |
| `client_id` | string | — | 原請求 client_id |
| `input_mode` | string enum | `text` / `url` / `url_text` | 本次辨識出的輸入模式 |
| `source` | `SourceMetadata` | — | 見 4.5 |
| `query_used` | string | — | 實際送至 TalentRecommendation 的完整查詢文字 |
| `query_truncated` | boolean | — | `query_used` 是否因長度上限被截斷 |
| `result_count` | integer | minimum 0 | `recommendations` 筆數 |
| `suggestion` | `QuerySuggestion` | — | 見 4.6 |

### 4.5 `SourceMetadata`（`additionalProperties: false`，required 全 3 欄）

| 欄位 | 型別 | 約束 | 說明 |
| :--- | :--- | :--- | :--- |
| `type` | string enum | `direct` / `104` / `1111` | 來源類型 |
| `url` | string (uri), nullable | — | 來源職缺網址；純文字模式為 null |
| `job_id` | string, nullable | — | 104 job ID 或 1111 employee number；純文字模式為 null |

### 4.6 `QuerySuggestion`（`additionalProperties: false`，required 全 4 欄）

| 欄位 | 型別 | 約束 | 說明 |
| :--- | :--- | :--- | :--- |
| `status` | string enum | `not_needed` / `generated` / `unavailable` | 見 §5.1 |
| `suggested_query` | string, nullable | — | 建議下一次自行送出的查詢；Gateway 不自動重查 |
| `reason` | string, nullable | — | 產生建議的原因 |
| `missing_information` | array\<string> | — | 建議補充的資訊 |

### 4.7 `ErrorResponse` / `ErrorDetail`（皆 `additionalProperties: false`）

`ErrorResponse` required: `error`；`ErrorDetail` required: `code`, `message`, `request_id`。

| 欄位 | 型別 | 約束 | 說明 |
| :--- | :--- | :--- | :--- |
| `error.code` | string enum | 10 碼，見 §5.3 | 錯誤代碼 |
| `error.message` | string | — | **不含**下游原始 body、查詢全文或 Secret 的安全錯誤訊息 |
| `error.request_id` | string | minLength 1 | 請求追蹤 ID |

### 4.8 `HealthResponse`（`additionalProperties: false`，required: `status`）

| 欄位 | 型別 | 約束 |
| :--- | :--- | :--- |
| `status` | string enum | 僅 `ok` |

## 5. 狀態面

### 5.1 Enum 全值展開

| Enum | 值 | 語意 |
| :--- | :--- | :--- |
| `input_mode` | `text` | 純文字查詢 |
| | `url` | 單一 104／1111 職缺網址 |
| | `url_text` | 網址＋補充文字 |
| `source.type` | `direct` | 純文字模式（url/job_id 為 null） |
| | `104` | 104 職缺來源 |
| | `1111` | 1111 職缺來源 |
| `suggestion.status` | `not_needed` | 已有結果，無需建議 |
| | `generated` | 零結果，已產生下一輪建議 |
| | `unavailable` | 建議服務失敗，但推薦回應仍成功（200） |
| `health.status` | `ok` | 服務存活 |
| `error.code` | 10 碼 | 見 §5.3 |

### 5.2 欄位連動規則（contract 驗證重點）

1. `input_mode = text` ⇔ `source.type = direct` 且 `source.url`、`source.job_id` 皆 null。
2. `input_mode = url / url_text` ⇒ `source.type ∈ {104, 1111}` 且 `url`、`job_id` 非 null。
3. `suggestion.status = not_needed` ⇒ `suggested_query`、`reason` 為 null、`missing_information` 為空陣列（依 spec example；schema 未強制 → 列觀察項）。
4. `suggestion.status = generated` ⇒ `suggested_query` 非 null。
5. `result_count` ＝ `recommendations` 長度；零結果仍回 200。
6. `recommendations` 依 `rank` 升冪，`rank` ≥ 1。
7. `unavailable` 是「建議服務壞掉但主流程成功」→ 仍是 200，不是 5xx。

### 5.3 HTTP status ↔ 錯誤碼對應

| HTTP | 回應定義 | error.code | 觸發條件 |
| :--- | :--- | :--- | :--- |
| 400 | BadRequest | `INVALID_JSON` | request body 非合法 JSON |
| 400 | BadRequest | `INVALID_QUERY` | 欄位不合法（缺欄位／長度／pattern／多餘欄位） |
| 400 | BadRequest | `MULTIPLE_URLS` | query 內含兩個以上網址 |
| 400 | BadRequest | `UNSUPPORTED_URL` | 網址非 104／1111 來源 |
| 403 | Forbidden | `INVALID_API_KEY` | 缺少或無效 `x-api-key` |
| 404 | NotFound | `JOB_NOT_FOUND` | 來源職缺不存在或已下架 |
| 502 | BadGateway | `JD_SOURCE_ERROR` | JD 來源回應異常 |
| 502 | BadGateway | `RECOMMENDATION_ERROR` | TalentRecommendation 回應異常 |
| 504 | GatewayTimeout | `JD_SOURCE_TIMEOUT` | JD 來源呼叫逾時 |
| 504 | GatewayTimeout | `RECOMMENDATION_TIMEOUT` | TalentRecommendation 呼叫逾時 |

> ⚠️ spec 未明載 400 系四碼與觸發條件的一對一強制關係（例如缺欄位是否一定回 `INVALID_QUERY`）——矩陣中 400 案例驗「status=400＋code ∈ 400 系」為主，實際 code 記錄於報告。

## 6. 測試矩陣（TSG-*）

> 欄位：ID｜分類｜前置/輸入｜預期結果｜可外部觸發?

### A 正常案例

| ID | 輸入 | 預期 | 可觸發? |
| :--- | :--- | :--- | :--- |
| TSG-A1 | 純文字 query（如「熟悉 Python、AWS 與 REST API 的後端工程師」） | 200；`input_mode=text`、`source.type=direct`、`url`/`job_id`=null；通過 RecommendResponse schema | ✅ |
| TSG-A2 | 單一 104 職缺網址 | 200；`input_mode=url`、`source.type=104`、`job_id` 非 null | ✅（需有效職缺網址） |
| TSG-A3 | 單一 1111 職缺網址 | 200；`input_mode=url`、`source.type=1111` | ✅（需有效職缺網址） |
| TSG-A4 | 網址＋補充文字 | 200；`input_mode=url_text`；`query_used` 含補充需求與來源 JD 兩段 | ✅（需有效職缺網址） |
| TSG-A5 | 冷僻條件文字查詢（預期零結果） | 200；`recommendations=[]`、`result_count=0`、`suggestion.status ∈ {generated, unavailable}`；不自動重查 | ✅（結果筆數不保證，零結果時驗） |
| TSG-A6 | `GET /health`（不帶任何 header） | 200；body 恰為 `{"status":"ok"}` | ✅ |

### B 邊界值

| ID | 輸入 | 預期 | 可觸發? |
| :--- | :--- | :--- | :--- |
| TSG-B1 | `query` 長度 1（min 界內） | 200 | ✅ |
| TSG-B2 | `query` 長度 20000（max 界內） | 200；觀察 `query_truncated` | ✅ |
| TSG-B3 | `query` 空字串（min 出界） | 400；code ∈ 400 系（預期 `INVALID_QUERY`） | ✅ |
| TSG-B4 | `query` 長度 20001（max 出界） | 400 | ✅ |
| TSG-B5 | `client_id` 長度 1 與 64（界內，pattern 合法） | 200 | ✅ |
| TSG-B6 | `client_id` 長度 65（出界） | 400 | ✅ |
| TSG-B7 | `client_id` 含 pattern 外字元（空白/中文/`@`） | 400 | ✅ |

### C Auth

| ID | 輸入 | 預期 | 可觸發? |
| :--- | :--- | :--- | :--- |
| TSG-C1 | `/v1/recommend` 不帶 `x-api-key` | 403；`code=INVALID_API_KEY`；通過 ErrorResponse schema | ✅ |
| TSG-C2 | `/v1/recommend` 帶無效 `x-api-key` | 403；`code=INVALID_API_KEY` | ✅ |
| TSG-C3 | `/health` 不帶 key | 200（無 auth 端點） | ✅（與 A6 合併執行） |

### D 錯誤碼

| ID | 輸入 | 預期 | 可觸發? |
| :--- | :--- | :--- | :--- |
| TSG-D1 | body 非合法 JSON（如 `{"query": `） | 400；`code=INVALID_JSON` | ✅ |
| TSG-D2 | 缺 `query`／缺 `client_id`／多餘欄位（`additionalProperties: false`） | 400；`code=INVALID_QUERY`（實際 code 記錄於報告） | ✅ |
| TSG-D3 | query 含兩個網址 | 400；`code=MULTIPLE_URLS` | ✅ |
| TSG-D4 | 非 104/1111 網址（如 linkedin.com） | 400；`code=UNSUPPORTED_URL` | ✅ |
| TSG-D5 | 不存在或已下架的職缺網址 | 404；`code=JOB_NOT_FOUND` | ✅（需準備已下架網址） |
| TSG-D6 | JD 來源回應異常 | 502；`code=JD_SOURCE_ERROR` | ❌ 需 mock 下游 |
| TSG-D7 | TalentRecommendation 回應異常 | 502；`code=RECOMMENDATION_ERROR` | ❌ 需 mock 下游 |
| TSG-D8 | JD 來源逾時 | 504；`code=JD_SOURCE_TIMEOUT` | ❌ 需 mock 下游 |
| TSG-D9 | TalentRecommendation 逾時 | 504；`code=RECOMMENDATION_TIMEOUT` | ❌ 需 mock 下游 |

### E Contract 一致性（offline 可先驗 spec 內 examples；live 時對真實回應再驗）

| ID | 驗證 | 預期 | 可觸發? |
| :--- | :--- | :--- | :--- |
| TSG-E1 | spec 內 200 examples（success / noResult）對 RecommendResponse schema | 全數通過（required、`additionalProperties`、型別、enum） | ✅ offline |
| TSG-E2 | spec 內 4xx/5xx examples 對 ErrorResponse schema；message 不含下游 body/查詢全文/secret | 全數通過 | ✅ offline |
| TSG-E3 | live 200 回應：`recommendations` 依 `rank` 升冪、`result_count` 與長度一致 | 通過 | ✅ live |
| TSG-E4 | suggestion 三態連動（§5.2 規則 3–4） | 通過（schema 未強制者列觀察項） | ✅ live |
| TSG-E5 | spec 完整性自檢：10 個 error code、3 組業務 enum、400/403/404/502/504 responses 皆存在於 spec | 通過 | ✅ offline |

**統計**：矩陣共 **30 案**（A6＋B7＋C3＋D9＋E5）；可外部觸發 26 案（其中 offline 可先跑 3 案：E1/E2/E5）、需 mock 4 案（D6–D9）。

## 7. 版控表

| 日期 | Spec 版本 | 異動摘要 |
| :--- | :--- | :--- |
| 2026-07-20 | v1.0.1@20260717 | 初版分析：2 端點、10 錯誤碼、4 組 enum、30 案測試矩陣 |
