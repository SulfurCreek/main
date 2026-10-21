# Resume Writer 協作與檔案入口

## 新管線交付（2026-10-21 本人指定，優先）

- [個人語氣指南](../../02_codex_stage/voice_style_guide.md)：新 stage 的語氣參數、禁詞對照、逐區塊協議與檢查規則。
- [A 方案主動句修整](2026-10-21-stage-active-voice-handoff.md)：在原交稿基礎修正反覆「由我」及倒裝；附完整逐點前後文、驗證結果與 Claude 接續指令。
- [下游潤飾全文](../../02_codex_stage/final_resume.md)：來自上游 `7839fd4`，20 點已潤飾，12 處 LOCKED 及六處〔待補數據〕原樣保留；原版 verify_polish.py 已通過，修改理由與逐點檢查見本輪交接。
- [本輪狀態與依賴](2026-10-21-stage-pipeline-handoff.md)。以下為歷史產出與治理入口，不另立 current 工作稿。


**開工先讀 [ROUTER.md](ROUTER.md)** → [本區流程 skill](skills/resume-editor/SKILL.md)；[交接狀態](wiki/handoff-status.md) 辨認採用／同步／PDF。以下日期型產出與交接僅為索引，不自動指定現行稿。

- [技能健診與共用修補](2026-10-21-skills-healthcheck-and-claude-handoff.md)、[技能清單](wiki/skills.md)、[真實錯誤檢查](wiki/editorial-regressions.md)。

- [本區工作指令](AGENTS.md)：讀寫邊界、共用來源及歷史資料使用方式。
- [分類 wiki](wiki/README.md)：有效操作導航、技能狀態、錯誤案例，以及歷史來源追溯。
- [逐檔索引](FILE_INDEX.md)、[CSV／SHA-256](FILE_INDEX.csv)。
- [ZIP 匯入說明](archive/2026-10-20-resumegen/README.md)、[匯入核對報告](archive/2026-10-20-resumegen/IMPORT_REPORT.json)。
- [共用路由增補稿](ROUTER-INTEGRATION.md)：交由 Career Move 加入共用 ROUTER.md。
- [接手紀錄](2026-10-20-resumegen-handoff.md)、[對話與共用來源核對](2026-10-20-conversation-reconciliation.md)、[疑問與處理狀態](QUESTIONS.md)。

現行資料讀取順序以共用 career/ROUTER.md 及 library/ 的最新裁定為準。本區歷史來源與索引不替代 SSOT。共用來源位於同一儲存庫的 Career Move 分支，不要求每個聊天各自維護副本。

## 對外選材與因果邏輯（2026-10-21 歷史交接）

- [四階段分析、SweetRing 已上線案例與 Claude 更新指令](2026-10-21-resume-causal-logic-and-sweetring-handoff.md)：本人新 skill 的適用調整、動筆前必過門檻、避免公開 roadmap 的跨欄位檢查、1111／SweetRing 完整片段及共同來源更新。SweetRing 三份規劃均由本人確認主責且已上線；原始 Keynote 與畫面未提交 repo。此輪為分析與送核稿，不自動改版或重產 PDF。

## 已交接的編輯素材（同步狀態見 wiki/handoff-status.md）

- [2026-10-20 管理案例：指導同仁完成類別對照](2026-10-20-management-case-handoff.md)

## 104 內容潤飾稿

- [104 v11.2 帶人案例與客戶回饋兩點修訂](2026-10-21-104-management-feedback-rewrite.md)：依本人指出的語意問題重新安排主線，附完整替換文字、原格式 HTML、理由與給 Career Move 的逐點整合指令；屬提案，未覆蓋共同稿。
- [104 v11.2 完整潤飾稿與修改紀錄](104-v11.2-polished.md)：依 Career Move `403c8ea` 做一般潤飾與去前綴後的語感檢查，附逐處理由、T1–T6 重跑結果及各欄實算字數；個人簡介、五個特色與格式鎖定不動，待本人檢視，PDF 未更新。
- [104 v11 完整潤飾稿與修改紀錄](104-v11-polished.md)：依 polish-104 skill 處理，待 Career Move 核對，未自動取代現行稿。

## 104 個人簡介與頂部 chip（2026-10-21）

- [104 下載 PDF 逐頁閱讀檢視](2026-10-21-104-downloaded-pdf-reading-review.md)：按七頁實際版面檢查語句、首次背景、分頁及欄位矛盾；附可替換全文、Q006–Q009 與給 Career Move 的處理順序，尚未改動 104 或 PDF。
- [本輪完整 Claude Code 交接](2026-10-21-104-summary-chips-claude-handoff.md)：243 字簡介、五個短句 chip（含本人指定 Client／Business）、About Me 同步片段及規格／skill 調整；本輪整合入口，PDF 不需更新。
- [歷版與指令檢視](2026-10-21-summary-review-and-rewrite.md)：47 種摘要文字與來源、規則衝突及取捨，供追溯；較早的六個 chip 已由本輪交接取代。
- [chip 短句初稿](2026-10-21-104-chips-punchline-proposal.md)：保留本輪措辭演變，整合請採上述完整交接的最新第二句。

## 每輪 About Me 同步

- [About Me 同步增補與給 Career Move 的指令](2026-10-20-about-me-sync.md)：管理案例、來源落差及常態同步授權；共用 About Me 實際寫入狀態見交接稿。

## v11.1 完整文字草稿

- [v11.1 潤飾稿、七段自傳與修改交接](resume-v11.1-polished.md)：依本人本次附件編輯，包含已確認的管理案例，待本人確認；PDF 與 104 尚待同步。

## 104 自我推薦信

- [沛思坦網路｜【北士科】Product Manager：A／B 完整潤飾稿](letters/8o3s3-%E6%B2%9B%E6%80%9D%E5%9D%A6%E7%B6%B2%E8%B7%AF-polished.md)：中英混合與全中文備選，附修改紀錄、字數及 Career Move 核對指令。

- [沛思坦網路推薦信：依語氣回饋重寫 A／B](letters/8o3s3-%E6%B2%9B%E6%80%9D%E5%9D%A6%E7%B6%B2%E8%B7%AF-rewritten.md)：取消能力小標、英文安排說明與敬上；附 skill／About Me 同步指令，前輪稿保留供追溯。

- [沛思坦網路方案 A：公司鉤子與共用英文規範版](letters/8o3s3-%E6%B2%9B%E6%80%9D%E5%9D%A6%E7%B6%B2%E8%B7%AF-company-hook-polished.md)：依新附件與 voice-en，保留角色、事實及公司服務對象，附修改紀錄與字數。

- [沛思坦推薦信收尾修訂與 pending-edits 核對](2026-10-21-pacston-letter-and-pending-review.md)：完整中英混合提案，英文 120 words；保留公司事實、修掉本人先前質疑的舊收尾，另指出待改清單第 9 項摘要字數應更新為 248。雙欄正文與 PDF 維持待用，尚未投遞或定稿。
