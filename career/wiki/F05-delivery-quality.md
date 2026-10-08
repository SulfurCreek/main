<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

> 🧭 [← 職能框架首頁 / Home](../competency-framework.md)

# F5. 交付流程與品質 / Delivery Process & Quality

> **履歷叢集 / Résumé cluster**：Execution & Delivery（見 `resume-craft` skill 核心職能叢集表）

**定義 / Definition**：以可控、可追溯、可驗收的流程交付規格，管理變更與缺口；並由規格推導測試案例、與 QA 協作驗收。
*Deliver specs through a controlled, traceable, verifiable process; manage change and gaps; derive test cases from specs and run acceptance with QA.*

- **實際展現 / In practice**：
  - **版本控管**：每次發布更新版控表，調整說明採 `[異動區段] 內容摘要`，可 diff、可回溯。
  - **缺口管理**：規格缺口以 🚧 `:::warning` 區塊記錄（現況／缺口／待確認 checkbox／來源），而非孤立的「待補」。
  - **分階段交付**：第二階段內容拆為獨立文件並記錄出處，第一階段保留入口連結。
  - **變更標紅**：本版調整一律紅字，方便 RD/QA 一眼辨識差異。
  - **測試案例設計（2026/09 起）**：由規格直接推導**驗收測試案例**，每條案例回連到規格章節；範圍依規格狀態取捨
    （排除「暫緩」「下一階段」「待補」內容）。實例：跨系統即時訊息第二階段 **11 條 happy path 案例**
    （篩選、封鎖、未讀提示、取消面試、收回訊息、發送邀約、範本、夾帶檔案、摘要列、履歷頁快速聊天）。
    並把寫法**沉澱為可重複使用的流程**（`qa-happy-path-cases` skill：範圍鐵律、案例來源、輸出格式、規格章節連結算法）。
  - **與 QA 協作**：與 QA 共同產出測試案例；測試執行期間**溝通範圍與方案異動**，必要時介入協調。
    實例（工單 T11669，公司形象圖片無法更換）：根因為含角括號的內容被防火牆（WAF）擋下；前端／QA／後端討論後，
    編碼範圍由「所有 API 轉碼、排除例外」收斂為「僅檔案上傳類請求轉碼」，工程列出建議驗證頁面，QA 據以產出簡易測試清單，
    並於 **QA 與 Staging 兩個環境**各自驗證，**通過率 100%、風險評估低**後結案。
    *Co-authored test cases with QA and managed scope/solution changes during test execution, stepping in when needed —
    e.g. an image-upload failure traced to WAF blocking angle brackets, where the fix scope was narrowed and verified
    across two environments at a 100% pass rate.*
- **工作證據 / Evidence**：skill「修改既有規格時」「版控紀錄」「階段拆分」「待補規則區塊」章節；交付前檢查清單；
  `qa-happy-path-cases` skill（2026-09-23 建立、09-24 兩次實測修訂）與其產出的 11 條測試案例；工單 T11669 留言板測試紀錄。
- **待補 / TODO**：**測試計畫（Test Plan）**層級的產出（範圍／策略／時程／進出場條件）〔待補數據〕；
  本人**親自執行**測試的範圍（App／Web／工具）〔待使用者確認〕。
- **資深度訊號 / Seniority signal**：把「寫規格」提升為**可治理的交付流程**，是帶人／帶專案的基礎。

---

**相關分頁 / Related**：[F8 專案管理／路線圖交付](F08-roadmap-delivery.md) ・ [F2 功能規格與系統思維](F02-spec-systems-thinking.md) ・ [F7 流程標準化與工具化](F07-process-tooling.md)
