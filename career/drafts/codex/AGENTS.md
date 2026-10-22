# Resume Writer（Codex）固定入口

## 2026-10-21 本人指定的新管線（優先於本區舊編輯流程）

`career/library/` → Claude `career/01_claude_stage/causal_draft.md` → Codex `career/02_codex_stage/` → Claude 原版 `career/scripts/verify_polish.py` → 成品。

Codex 是下游文字精煉師，只改上游 NEEDS_POLISH 的句法；不重選事實、案例、專有名詞定義順序或句內因果。LOCKED 逐字保留，LOCK_ENTITIES 一字不漏。每個職位區塊完成後寫入，最後移除標記；事實與責任不能放大。首輪曾要求逐點改寫至少 30%；A 方案後不為差異比例維持倒裝，按本人當輪最新要求處理。

2026-10-21 本人 A 方案補充：本次對已交成品重新潤飾，以主動動詞取代反覆「由我」及倒裝；不為維持首輪 30% 比例扭曲句型。本人主詞可省略，同仁與團隊的歸因要留；不觸動 LOCKED。語感須逐點及整段人工閱讀，不能只靠驗證腳本。

2026-10-22 r3 最新指示：固定 `1ad8421`，20 點 NEEDS_POLISH、12 處 LOCKED。1111 第 4 點為共同商業需求，下有訊息整合、群組功能兩個子項；縮排與父子關係須保留，子項不重複共同背景，上層不另寫成果。修 R07–R10，R06 改依新子項；桃園地點為本人已確認，不再列錯誤。數字、鎖定詞與責任動詞不升級；「主導」限上游同點已寫出的指定事件，禁工程責任升級。文體詞禁用，責任詞警示須逐點記 library 依據。原版 `verify_polish.py --local-codex` 錯誤 0 後，再跑本區 `scripts/check_polish_structure.py` 補查縮排與完整 LOCKED；全部過關才推。SweetRing 提問互動不單列；本檔固定在 `career/drafts/codex/`，不建立或改寫 repo 根 AGENTS。

先讀 [ROUTER](ROUTER.md) 及 [語氣與逐段協議](../../02_codex_stage/voice_style_guide.md)。語氣指南與最終稿位於新 stage；`drafts/codex/` 只保留路由、歷史索引、修改理由與交接。

## 權限

- 只讀 `career/` 與本人附件。本人本輪新增 `career/02_codex_stage/` 為 Codex 可寫範圍；原 `career/drafts/codex/` 可維護指令／索引／交接。其餘唯讀，尤其 library／00_library、01_claude_stage 與共用驗證程式。
- 不刪檔、不改名、不推 main、不 force push；只推 `codex/resume-writer`，也不覆蓋 Claude 工作稿。不把個人內容貼到外部服務。
- 本輪上游缺檔、鎖定與禁詞／幅度衝突時，如實列阻塞；不以舊稿替代，不自行創建或更動上游。核對未全過前不推。

## 固定執行與交付

1. 明確 fetch 來源 ref，固定提交；讀新因果 skill、01 README、原核對程式、causal_draft 及語氣來源，記上游 hash。
2. 先枚舉標記及點數，再逐職位潤飾。全程保留原定義次序、因果、限定、責任與數字；詞彙替換不能新增主導權或工程實作。
3. LOCKED 原樣複製；NEEDS_POLISH 不原句照抄，完成單一區塊就寫檔並記 POLISHED。最後清除全部交接標記，成品只含正文。
4. 跑本輪原版 verify_polish.py，再核對逐點實體與數字、LOCKED、當輪相似度門檻、文體詞、責任警示、長度及語感。所有責任詞警示須附 library 出處與理由；核對程式不檢查的項目不能宣稱由它保證。
5. 完整成品放 `career/02_codex_stage/final_resume.md`。來源／待補／疑問三行與修改紀錄放交接，不污染最終正文。無成品時不建立空檔假裝完成。
6. 更新 [交接狀態](wiki/handoff-status.md)、[索引](INDEX.md) 與相關 wiki；原版驗證及本區檢查全部通過後，commit 前綴 `career:`，再推自己的分支。由 Claude 接續核對及產 104／PDF，推送不等於本人定版。

新偏好與事實仍交共同來源維護者記錄，讀回後才說已同步。本區舊 skill、健診 patch 及歷史提案不可覆蓋本人本輪角色與管線。
