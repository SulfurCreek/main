# Skill：職類1（現有1）個案修正工作流程（cat1-correction-workflow）

> **時機**：使用者點名一或多個 eNo，說「現有1 判錯了」，要你找正解寫進「建議1」。
> 這是**完整、可直接照做**的操作程序（原始版本是寫給 mid-tier 模型的 prompt，現收錄為正式 skill）。

## 角色與工作目錄

你是 1111 職類校正專案的資料處理員，工作目錄：`job-classification-kb/`。

## 任務

使用者會給你若干職缺編號（eNo），這些職缺的「現有1」職類被判定不合理。
你要為每筆找出更符合職缺名稱的正解葉，寫進 MD 資料層的「建議1」欄。

## 嚴格流程（不可跳步）

1. 讀 [`skills/tcode-desc-lookup-skill.md`](tcode-desc-lookup-skill.md) 與 [`skills/sync-md-skill.md`](sync-md-skill.md)，照做。
2. 在 `不合理清單_職類校正.md` 用 eNo 找到該筆（**注意**：同一 eNo 會出現在「不合理清單」和「北三區」兩個 `##` 區段——北三區是不合理清單的子集，非獨立資料——**兩處都要改**）。
3. 對職缺名稱做關鍵字拆解（R7，見 [`logic/01-plan-algorithm.md`](../logic/01-plan-algorithm.md)）：取功能尾詞優先（工程師／主管／助理／專員…前面的功能詞）。
4. **Step 0 優先**（見 `tcode-desc-lookup-skill.md`）：先看現有2~5 是否已有合理正解——有就是 `keep_strike`，直接把該值填進建議1，不必查 Description。
5. Step 0 無解時才反查候選葉的職務說明：
   - 只准讀 [`tcode/data_tCodeDutyNM_descript_cache.md`](../tcode/data_tCodeDutyNM_descript_cache.md) 的快取；
   - 快取缺葉 → 依 `tcode-desc-lookup-skill.md` 內的腳本一次性抽取補進快取後再讀；
   - **絕對禁止**直接 `load_workbook` 翻 `TCode_Export.xlsx` 查值。
6. 裁決原則：`CodeDescript`／`CodeDefinition`／`CodeAlike` 的「說明涵蓋」勝過葉名字面相似。資歷層級要對齊（主管≠專員，見 [`logic/03-pitfalls.md`](../logic/03-pitfalls.md) 的 P10）。
7. 只把正解寫進該筆的「建議1」欄（第 9 欄），其他欄位一律不動；**建議1 不可留空**（槓必補）。
8. 把裁決記錄追加到 `data_tCodeDutyNM_descript_cache.md` 的「快取使用案例」表，與 [`logic/04-case-decisions.md`](../logic/04-case-decisions.md)。
9. **預設**只處理使用者點名的 eNo，禁止回頭掃描或改動其他資料列——**除非使用者明確要求「review 整份／整批／whole spreadsheet」**，此時才擴大到全表（見下方「全表審查模式」）。
10. 不產生 Excel。使用者明確說「給我 Excel」時才跑 `python3 scripts/md_sync.py to-xlsx`。
11. 回報格式：表格（eNo｜職缺名稱｜原現有1｜新建議1｜反查依據引用的說明關鍵句），然後停止（除非在全表審查模式，見下）。

## 全表審查模式（使用者明確要求時才啟動）

逐筆對 614 葉做 Description 反查不可行（太貴）。改用**分層篩選**：

1. 先看「建議1」目前是否已有值（已處理過的不重查，除非使用者要求複查既有建議）。
2. 對「建議1」空白的列，用**擴充版 R7 關鍵字掃描**（比 `scripts/suggest_cat1.py` 的 `KWMAP` 更廣）找出「職缺名稱含明確功能詞，但現有1 是籠統／不對應類別」的候選列。
3. 候選列先跑 Step 0（現有2~5 是否已有解）。
4. 剩下的才對候選（不是全表）做 Description 反查確認。
5. 只有 Description 明確支持才寫入建議1；證據不足 → 依「擦邊保留」原則不動，列入報告的「檢視但不改」清單，附理由。
6. 收工後：把新掃出的關鍵字規律回饋進 `scripts/suggest_cat1.py` 的 `KWMAP`（如本次新增「文件管制／系統維護／商務」等 pattern），避免下次全表審查要再重找一次。

## 與其他文件的關係

- 反查程序細節：[`tcode-desc-lookup-skill.md`](tcode-desc-lookup-skill.md)
- MD⇆Excel 同步：[`sync-md-skill.md`](sync-md-skill.md)
- R7 拆解與 keep_strike 規則：[`logic/01-plan-algorithm.md`](../logic/01-plan-algorithm.md)
- 已驗證規則、校準案例：[`logic/02-verified-logic.md`](../logic/02-verified-logic.md)
- 常見錯誤：[`logic/03-pitfalls.md`](../logic/03-pitfalls.md)
- 個案裁決記錄：[`logic/04-case-decisions.md`](../logic/04-case-decisions.md)
