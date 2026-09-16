---
name: api
description: >
  分析 API 文件（OpenAPI/Swagger YAML/JSON 或自由格式文件）內的所有狀態與參數時使用：
  萃取端點、request/response 全欄位約束、enum 狀態面、錯誤碼與 HTTP status 對應，並產出 MECE 測試矩陣，
  寫入 `wiki/apis/<api名稱>/api_doc.md`。只要任務涉及「分析這份 API」「整理 API 參數/狀態」「新增一支 API 到 wiki/apis」
  「讀 spec 產文件」「API 文件轉測試矩陣」，即使使用者沒明講 skill 名稱，務必使用本 skill。
  本 skill 只負責「文件 → 分析 → 測試矩陣」；產生與執行測試腳本、出報告由 skill `auto-test` 接手。
---

# API 文件分析（api）

本 skill 統整自公開 API 測試 skill 的方法論——api-test-automation（spec 解析與測試分類）、api-contract-testing
（Pact/contract 驗證觀念：驗結構不驗值、錯誤路徑必測、版本相容）、Schemathesis（property-based：由 schema 約束自動推邊界案例）——
濃縮為適用本 repo 的固定流程。資料夾結構與模板規範以 `wiki/api_testing_rules.md` 為準，本 skill 不重複。

## 流程（依序執行）

### 步驟 1：讀 spec
- 讀 `wiki/apis/<api名稱>/spec/` 下的原始文件。OpenAPI 優先照 schema 走；自由格式文件則逐段萃取，**缺漏欄位標 `NULL` 不推測**。
- 確認 spec 版本號與檔名，寫進 `api_doc.md` 概觀與版控表。

### 步驟 2：萃取結構（解析 checklist）
逐項核對，漏一即不完整：
- [ ] servers（base URL、URL 變數）與每端點的 auth 要求（含「無 auth」端點）
- [ ] 每個端點：method / path / operationId / 摘要
- [ ] request schema 全欄位：型別、必填、minLength/maxLength、minimum/maximum、pattern、enum、nullable、`additionalProperties`
- [ ] response schema 全欄位（含巢狀 `$ref` 展開）、required 清單
- [ ] spec 內附的 examples（後續 offline 驗證要用）

### 步驟 3：列狀態面
- 所有 enum **全值展開**（一個都不能少），並附每值的語意。
- HTTP status ↔ 錯誤碼對應表：每個錯誤碼標「觸發條件」與「所屬 status」。
- 狀態轉移敘述：欄位間的連動規則（例：某狀態值時哪些欄位必為 null / 必非 null）、排序保證、旗標語意。

### 步驟 4：產出測試矩陣（MECE）
依 `wiki/api_testing_rules.md` §2.6 的 A–E 五分類與 ID 規則產矩陣。設計原則（統整自上述來源）：
- **邊界值成對**：每個 min/max 都要「剛好在界內」＋「剛好出界」兩案例；pattern 要「合法」＋「非法字元」兩案例（Schemathesis 的 negative testing 思路）。
- **錯誤碼逐一觸發**：每個錯誤碼至少一列；無法由外部穩定觸發的（如下游故障/逾時類）標「需 mock」，不假裝可測。
- **Auth 三態**：有效／缺失／無效憑證各一列；無 auth 端點驗證「不帶憑證也能通」。
- **Contract 驗結構不驗值**：200 與錯誤回應都要驗 schema（required、`additionalProperties`、型別），對動態值只驗格式不寫死。
- **錯誤路徑必測**：錯誤回應本身也要驗 ErrorResponse schema，並確認 message 不洩漏下游內容或機密。

### 步驟 5：寫檔與收尾
- 依模板寫入 `wiki/apis/<api名稱>/api_doc.md`；更新 `.claude_index.md`。
- 回報時只列「產出檔案＋矩陣案例數＋需 mock 案例數」，不重貼全文。

## 禁忌
- 不在 `api_doc.md` 或任何輸出寫入真實 key/token。
- 不憑記憶補 spec 沒寫的行為；不確定就標 `NULL` 或 🚧 待確認。
- 不在本 skill 內產生測試腳本——那是 `auto-test` 的職責。
