# API 測試資料結構與流程規範（api_testing_rules）

> 本檔是 API 測試 VM 分支（`claude/vm-api-testing-setup-wpf6y8`）的規則本體。
> `CLAUDE.md` 只保留路由指向本檔，**不存任何 API 本身的資料**；所有 API 實體資料一律放 `wiki/apis/<api名稱>/`。

---

## 1. 資料夾規範

每支 API 一個資料夾，名稱用 **kebab-case 的 API 名稱**（如 `talent-sourcing-gateway-api`），固定四件套：

```
wiki/apis/<api名稱>/
  spec/        ← 原始 API 文件（OpenAPI YAML/JSON、Word 轉出的 md 等）；保留原檔名不改名，以利追溯
  api_doc.md   ← 用 skill `api` 產出的分析文件（唯一真相來源，見 §2）
  tests/       ← 用 skill `auto-test` 產出的測試腳本
  reports/     ← 每次測試一份報告：YYYYMMDD-HHMM_<範圍>.md（見 §3）
```

- spec 出新版時：新檔進 `spec/`（不覆蓋舊版），重跑 `api` skill 更新 `api_doc.md`，並在 `api_doc.md` 版控表記錄差異。
- 新增/搬移檔案後順手更新根目錄 `.claude_index.md`。

## 2. `api_doc.md` 模板（章節固定）

1. **概觀**：API 用途一句話、spec 版本、spec 檔路徑、分析日期。
2. **Servers 與 Auth**：base URL（含變數）、認證機制（header 名稱、無 auth 端點另註明）；**不得寫入任何真實 key**。
3. **端點表**：method / path / operationId / 摘要 / auth 要求。
4. **參數與約束表**：逐欄位列 型別｜必填｜min/max｜pattern｜enum｜nullable｜`additionalProperties`。request 與 response 分開列。
5. **狀態面**：所有 enum 全值展開、HTTP status ↔ 錯誤碼對應表、狀態轉移敘述（如 suggestion 三態的觸發條件）。
6. **測試矩陣**（MECE）：每列一個案例，欄位＝`ID｜分類｜前置/輸入｜預期結果｜可外部觸發?`。ID 規則：`<API縮寫>-<分類字母><流水號>`（如 `TSG-A1`）。分類固定：
   - **A 正常案例**（每種輸入模式/成功路徑各一）
   - **B 邊界值**（min/max/pattern 內外各一）
   - **C Auth**（有/無/錯誤憑證）
   - **D 錯誤碼**（每個錯誤碼一列；無法由外部穩定觸發者標「需 mock」）
   - **E Contract 一致性**（回應 schema、排序、欄位連動規則）
7. **版控表**：日期｜spec 版本｜異動摘要。

## 3. 測試報告模板（`reports/YYYYMMDD-HHMM_<範圍>.md`）

1. **測試資訊**：日期時間、執行環境（offline / dev / …）、spec 版本、腳本 commit。
2. **Pass/Fail 總表**：矩陣 ID｜結果（✅/❌/⏭ skip）｜備註。
3. **逐案摘要**：失敗與異常案例的 request/response 摘要（**header 中的 key 一律遮罩為 `x-api-key: ****`**）。
4. **覆蓋率**：已執行案例數 / 矩陣總數，未覆蓋原因（pending credentials、需 mock…）。
5. **待辦與缺陷**：發現的問題、下次要補的案例。

規範：結果**不得偽造**——沒跑到就標 ⏭ 並寫原因；缺憑證整批標「pending credentials」。

## 4. 機密規範

- API 憑證一律走環境變數，存 `.env`（已在 `.gitignore`）。命名慣例：`<API縮寫>_API_KEY`、`<API縮寫>_API_ID`（本分支現行：`TSG_API_KEY`、`TSG_API_ID`）。
- **絕不**把 key/token 寫進任何 md、腳本、報告、commit；報告內 header 一律遮罩。
- 提交前自查：`git grep -in "api.key\|x-api-key"` 結果中不得出現真實 key 值。

## 5. 新增一支 API 的 SOP

1. 建 `wiki/apis/<api名稱>/` 四件套，spec 原檔放入 `spec/`。
2. 用 Skill 工具載入 **`api`** → 產出/更新 `api_doc.md`（含測試矩陣）。
3. 用 Skill 工具載入 **`auto-test`** → 依矩陣產生 `tests/` 腳本。
4. 執行測試（缺憑證先跑 offline 部分）→ 依 §3 模板寫報告到 `reports/`。
5. 更新 `.claude_index.md`，commit（訊息含 API 名稱與 spec 版本）。
