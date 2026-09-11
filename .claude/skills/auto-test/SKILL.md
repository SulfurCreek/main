---
name: auto-test
description: >
  自動化產生與執行 API 測試腳本時使用：讀 `wiki/apis/<api名稱>/api_doc.md` 的測試矩陣，
  產生 Python pytest 腳本到 `tests/`、執行後依模板出報告到 `reports/`。
  只要任務涉及「產生/更新測試腳本」「跑 API 測試」「執行測試矩陣」「出測試報告」「驗證這支 API」，
  即使使用者沒明講 skill 名稱，務必使用本 skill。
  前置條件：該 API 必須已有 `api_doc.md`（由 skill `api` 產出）；沒有就先跑 `api`。
---

# 自動化測試腳本產生與執行（auto-test）

方法論統整自 api-test-automation（測試分類與 CRUD/auth/邊界案例生成）與 Schemathesis（schema conformance 檢查：
status code / content-type / response schema 一致性、negative testing）。資料夾與報告模板以 `wiki/api_testing_rules.md` 為準。

## 鐵律

1. **矩陣是唯一真相來源**：只依 `api_doc.md` 的測試矩陣產案例，不重新解析 spec、不自行加減案例；矩陣有缺就先回頭改 `api_doc.md`。
2. **每列矩陣 ↔ 一個 test case**，test ID 與矩陣 ID 一致（如 `TSG-B4` → `test_tsg_b4_*`），報告才能對得回去。
3. **結果不得偽造**：沒執行＝⏭ skip＋原因；缺憑證整批標「pending credentials」，不得填想像中的結果。
4. **機密**：憑證只從環境變數讀（命名見 `wiki/api_testing_rules.md` §4）；腳本、報告、log 一律遮罩 key。

## 流程

### 步驟 1：產生腳本（寫到 `wiki/apis/<api名稱>/tests/`）
- 技術棧固定 **Python pytest + requests**（repo 慣例，參考 `scripts/hackmd_safe_patch.py` 的風格）。
- 檔案切分：
  - `conftest.py`：env 讀取（缺憑證 → 對 live 案例統一 skip）、base_url fixture、spec 載入、遮罩 helper。
  - `test_offline_*.py`：**離線案例**——用 spec 內 examples 對 schema 做本地驗證（jsonschema）、約束完整性檢查；無憑證也能跑。
  - `test_live_*.py`：**線上案例**——實際打 API 的 A/B/C/D 分類案例；每案驗 status code、content-type、回應 schema（Schemathesis 三件套思路）。
- 矩陣標「需 mock」的案例：產出 `@pytest.mark.skip(reason="需 mock 下游")` 的佔位案例，保留 ID 對應。
- 可選補洞：在報告附一條 property-based 指令
  `schemathesis run <spec路徑> --url <base_url> -H "x-api-key: $<API縮寫>_API_KEY"`（不強制執行）。

### 步驟 2：執行
```bash
python3 -m pytest wiki/apis/<api名稱>/tests/ -v --tb=short
```
- 缺憑證時只會跑 offline 部分，live 全 skip——照實記錄。
- 需要真打 dev/prod 時，先向使用者確認環境與憑證來源，憑證放 `.env` 後 `source` 進環境變數。

### 步驟 3：出報告（寫到 `reports/YYYYMMDD-HHMM_<範圍>.md`）
- 依 `wiki/api_testing_rules.md` §3 模板：測試資訊 → Pass/Fail 總表（對矩陣 ID）→ 失敗案例摘要（遮罩）→ 覆蓋率 → 待辦。
- `<範圍>` 命名：`offline`、`dev-full`、`dev-smoke`、`regression-<主題>` 等，一看即知本次跑了什麼。
- 更新 `.claude_index.md`（若是該 API 首份報告，補一列指向 `reports/`）。

## 回報格式
任務完成只回：報告路徑＋Pass/Fail/Skip 三個數字＋是否有缺陷待辦。不重貼報告全文。
