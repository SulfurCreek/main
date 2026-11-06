# 05 — Skill 打包清單

以下 6 個 skill 逐個原文複製（`SKILL.md` 與 `references/`／`scripts/` 全部子檔），未摘要、未改寫。每個 skill 下面補一行：觸發條件、依賴的檔案或環境、目前已知問題。

## tcode-excel-ops（`tcode-excel-ops/`）

- **觸發條件**：使用者操作 `TCode_Export` 檔案或提到 代碼表／職務代碼／證照／工作技能／職能 相關試算表，想要檢查、比對、套用新增/改名/合併需求、驗證 ChangeType、找 CodeNo 衝突、產異動清單 xlsx、寫 Markdown 異動表、或草擬系統公告。即使使用者只說「更新 export」「列出異動項目」「發公告」「整理這次的改動」「比對舊新檔」「分析這個代碼表」也要觸發。
- **依賴的檔案或環境**：`TCode_Export.xlsx`（或其新/舊兩版），本 skill 的 `scripts/compare.py`／`scripts/build_report.py`／`scripts/tcode.py`，以及 `references/` 下 4 份規則文件（`bulletinboard-rules.md`〈資料來源鐵則〉、`changetype-rules.md`、`export-schema.md`、`announcement-template.md`、`markdown-output.md`）。
- **已知問題**：`references/bulletinboard-rules.md` 的鐵則本身強調「不信任 ChangeType 欄位」——這代表上游資料（企劃填的表）本身品質不穩定，不是 skill 的 bug，但使用這個 skill 產出的任何結論都要連帶附上「比對了哪兩份檔案」的交代，否則結論不可信。

## md-datalayer（`md-datalayer/`）

- **觸發條件**：分析或修改 Excel/CSV 內容（尤其職類校正、不合理清單等已建立 MD 資料層的資料）時，一律讀寫 MD、不回讀 Excel；只有使用者明確要求「輸出／給我 Excel」時才由 MD 產生 Excel。
- **依賴的檔案或環境**：已存在的 `data_*.md` 資料層檔案；原始 Excel/CSV 僅作首次匯出來源。
- **已知問題**：本次打包發現 `data_tCodeCertify_summary.md`／`data_tCodeWorkAbility_summary.md` 這兩份「唯一真實來源」MD 實際上落後於已確認套用的異動（見 `04-known-facts.md`〈資料層副本落後現況〉）——這違反了這個 skill「MD 是唯一真實來源」的前提，使用前要先確認 MD 本身有沒有過期。

## safe-excel-editor（`safe-excel-editor/`）

- **觸發條件**：對既有 `.xlsx` 做欄位/儲存格修改、標記刪除線或底色、更新特定 ID 的值、回寫分析結果（如職類校正對照、不合理清單標記）時。
- **依賴的檔案或環境**：`openpyxl`；修改目標是既有 Excel 檔（非新建）。
- **已知問題**：無已知問題記錄。

## tabular-token-min（`tabular-token-min/`）

- **觸發條件**：讀取、清洗、樞紐分析、運算或彙整 `.xlsx`／`.xls`／`.csv`／`.tsv` 等表格資料時（例如 `TCode_Export.xlsx`、不合理清單、廠商身分 sheet、任何 dataframe 操作），強制套用以控制 context window。
- **依賴的檔案或環境**：pandas；大型表格檔案。
- **已知問題**：無已知問題記錄。

## gsheet-vendor-identity（`gsheet-vendor-identity/`）

- **觸發條件**：查詢「廠商身分」Google Sheet 資料表中特定功能項目（頁面區塊）的完整廠商身分狀態資料，例如查某個功能編號（如 A.1.7）或功能名稱對應的各廠商身分文案或行為。
- **依賴的檔案或環境**：特定 Google Sheet（試算表 ID `1cLqoBpmjkMkWa_ZJ9pDQNektQsnPlcehNcnA1wwuSmY`，工作表名稱「廠商身分」），需要 Google Sheets WebFetch 權限（本分支 `.claude/settings.json` 已含對應 allowlist）。
- **已知問題**：此 skill 與 tCode 代碼表流程無直接關聯，是同一分支下的獨立工具，收錄進本包是因為原始需求清單裡要求一併打包，實際與 tCode handoff 主題關聯度低。

## job-classification-kb（`job-classification-kb/`）

- **觸發條件**：判斷職缺的正解職務小類、處理「不合理清單」、修改 `plan()` 語意規則、操作 `sync_md.py` 的 export/diff/apply、產出「現有 vs 建議」對照 Excel、查詢 tCode 代碼表、或讀寫本專案的 Google Sheet 時。
- **依賴的檔案或環境**：`job-classification-kb/` 整個目錄（`README.md`、`wiki/00-index.md`、`logic/02-verified-logic.md`、`logic/03-pitfalls.md`、`INDEX.json`、`scripts/sync_md.py`、`scripts/tcode_to_md.py`）。這是整個職類校正專案的知識庫入口 skill，比前 5 個範圍更大，tCode 只是其中一部分。
- **已知問題**：此 skill 的範圍涵蓋「不合理清單職類校正」主線（挑正解職務小類），跟本次打包聚焦的「tCode 代碼表異動協作流程」是相鄰但不同的任務——Handoff 助手產文件時要分清楚哪些事實屬於職類校正主線、哪些屬於 tCode 異動協作，不要混為一談。本打包的 `01`～`04` 檔只涵蓋後者。
