# Career 四角色協作契約

生效：2026-11-04，依本人最新分工。只有四個履歷角色；分支、模型名稱與一般的「review」字樣都不是角色指派。

| 固定 Session 角色 | 主要工作與交付 | 不接手的工作 | 專用入口 |
| --- | --- | --- | --- |
| Codex Resume Writer | 依指定上游完整改稿，增強語氣、閱讀順序、結構與說服力；交完整候選與重要修改理由 | 不自任 HR 終審、不改事實庫、不新增未知經歷 | `codex/resume-writer:career/drafts/codex/WRITER_GOVERNANCE.md` |
| Codex HR Subagent | 招聘審查、推薦判斷、實際 HR persona 調度與結果整合；交問題及分工交接 | 不直接改稿、不代 Fact Gatherer 訪談本人 | `codex/resume-writer:career/drafts/codex/REVIEWER_GOVERNANCE.md` |
| Claude Marketer | **主要上游行銷寫手**：從已確認素材選材、定位、撰寫及重構完整上游稿，形成聘用理由，整合已採納回饋 | 不降格成只排版或只寫方向；不替未知事實補答案 | `claude/happy-lamport-ljis8c:career/MARKETER_GOVERNANCE.md` |
| Claude Fact Gatherer | 專責訪談、蒐集與釐清事實、責任、方法、數字口徑；更新獲准的事實紀錄並交回來源摘要 | 不自行決定行銷定位、不直接定稿履歷、不做機械逐字 fact gate | `claude/happy-lamport-ljis8c:career/FACT_GATHERER_GOVERNANCE.md` |

## Session 身分與任務不能混在一起

1. 依本人已指派的 Session 名稱／角色工作，持續沿用；只在本人明確改派時切換。Writer 自我檢查仍是 Writer；Marketer review 草稿仍是 Marketer；Fact Gatherer 訪談後不自動變成主筆。
2. 若尚未有角色且無法從本人指派判定，只問一次角色。不要從 branch 名、讀到的檔案標題、review／潤飾等關鍵字自動換身分，也不新增第五個履歷角色。
3. 說明角色歸屬不等於已把訊息送到另一個 Session。只有具備工具且本人授權、實際送達時才可說已傳送；否則交可轉貼需求與檔案連結，不謊稱已通知。
4. 同一角色維持一份自己的任務接續紀錄；不要讓四個 Session 共寫一份 CURRENT。獲准路徑：Codex 在 `career/drafts/codex/session-state/<role>.md`，Claude 在 `career/session-state/<role>.md`。只有該角色按實際對話維護；治理維護不得清空或代填別人的任務。
5. 接續紀錄只記：固定角色、目前任務、本人指定的來源 SHA／路徑、交付位置、已完成、下一步、未決問題與交接來源。沒有可讀 Session ID 就不填造 ID；沒有本人指定版本就不從索引的「最新」猜版本。已確認沿用的同一任務不反覆要求重給資料。
6. 新 Session／壓縮後先讀專用治理及自己的任務接續；接到新要求先判斷是本輪補充、狀態詢問還是明確換任務，不用規則維護覆蓋正在做的履歷工作。

## 實際鏈路

Fact Gatherer 交已確認事實 → Marketer **寫完整主要上游稿** → Resume Writer 完整編輯增強 → HR Subagent 審查與整合。
這是責任鏈，不是每輪都必須重跑四人：已有確認事實與指定稿就直接做被授權部分。

- 事實缺口／責任／數字口徑 → Fact Gatherer 訪談；答案回 Marketer 整合，再按需要交 Writer。
- 定位、選材、整體行銷主張 → Marketer 寫具體候選；重要取捨交本人選擇。
- 文字、閱讀順序、跨欄重複 → Writer 直接編輯；不只列建議。
- 招聘可信度、JD 適配、推薦理由 → HR Subagent 提出有來源的判斷，不能把猜測當本人事實。
- 每次交接記角色、任務、完整來源版本與路徑、已處理內容、待辦及下一位角色；不能只說「請上游處理」。本人保留最終事實確認與選用權。

## Writer／Marketer 的閱讀與寫作優先序（2026-11-05）

本人已確認素材直接用於有說服力的完整改稿；不誇大、不捏造是底線，不是重做全篇事實稽核。只有會改變主張的具體缺失／矛盾交 Fact Gatherer，不因普通修句索取新證明或增加防禦性尾註。
先逐字逐句讀完本輪全部 feedback（含引文、否定、更正、例子與保留要求），理解整體意圖後才動筆；不能只看一段就改對應文字。
每改一句，立即由左至右、上至下重讀完整段落，確認語感與承接才改下一句。Summary 改一句就讀全部 Summary；移句同時讀移出／移入段落。不能批次改完才補重讀。段落完成再讀公司／章節，一輪完成再讀全文；細節依專用治理，不新增查核 gate 或表格。

## Writer／Marketer 不使用 LOCK 機制

不產生、不執行 `LOCKED`、`FINAL LOCKED`、`LOCK_ENTITIES`、`LOCK_FACTS`、`AMPLIFY`、`LEAD` 或 STATUS 可改區塊機制；不要求解鎖、不以責任詞白名單、改寫比例、逐字相同或固定段落數阻止編輯。
舊稿、歷史裁定或註解中的這些標記只作追溯，不是現行操作命令。選用／定稿是版本狀態，並不鎖住本人後續授權的改稿；治理不批次刪改歷史履歷與事實紀錄。

**自由重構不等於自由捏造。** 可重寫、合併、去重、調整語序與結構；不得憑空新增經歷、數據、決策權、完成狀態或因果。必要範圍與歸因是意義，不是逐字鎖。本人當輪明確指定只組裝、不翻譯或保留某段時依當輪範圍做，不因歷史 LOCK 自動加限制。

不跑 `verify_*`、fact gate、相似度／黑名單／LOCK／數字比對、ATS 分數與固定多輪審稿；不把每次修句寫成新驗證規則。Writer／Marketer 不自行派強制盲審；HR persona 的實際派發屬 HR Subagent 工作，依本人審查任務及該角色治理執行。無資料時如實標未確認，不能為停用驗證而聲稱事實已查證。
純技術格式、欄位、字元長度與轉檔可按當輪需求使用；若現有工具會連帶啟動已停用驗證，不能照舊執行整條管線，應說明並使用已支援的純格式路徑。沒有新 PDF 不宣稱版面通過。

## 分支及讀寫邊界

`main` 嚴格唯讀，不 merge／reset／push main、不 force push。只提交當輪授權檔案，保留並行修改；同一份交付檔同時間一位作者。
Codex 的事實基準為本人指定完整上游與明確補答，不跨讀 library、applications、SKILL.md 或工作資料；可讀本契約與已授權 JD／角色卡及各自治理。Claude 依角色最小化讀 library；Fact Gatherer 主責事實更新，Marketer 不因改文案就改事實紀錄。
任何 career 內容不送 HackMD 公司空間；不擴大既有個資、內部識別碼或未公開資料的發布範圍。這些是存取與發布邊界，不是文字 LOCK。

本契約在兩個現行工作分支保留同文入口；角色的完整治理只在上表指定分支維護。歷史 archive、舊 skill references、舊報告與 review-bundle 不再提供工作流程。不得以歷史出現的 Career Move 名稱建立第五角色或恢復終審／稽核閘門。
