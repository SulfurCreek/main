<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

> 🧭 [← 職能框架首頁 / Home](../competency-framework.md)

# F2. 功能規格與系統思維 / Functional Spec & Systems Thinking

> **履歷叢集 / Résumé cluster**：Technical Fluency ＋ Business Logic & Requirements（見 `resume-craft` skill 核心職能叢集表）

**定義 / Definition**：以「狀態 → 行為」與「條件 → 結果」的方式描述規格，涵蓋邊界與例外，讓 RD/QA 可無歧義實作與驗收。
*Specify in state→behavior and condition→result terms, covering edge cases so engineers and QA can build and
verify without ambiguity.*

- **實際展現 / In practice**：
  - **MECE 四狀態**：所有非同步資料區塊一律覆蓋 `載入中／有資料／無資料／錯誤`（loading / data / empty / error）。
  - **權限代碼建模**：將散落的權限判斷集中為單一「權限判斷」表格，欄位以代碼建模（`oStatus:1`、`confirmed&4096`、`代碼54`）。
  - **條件邏輯**：巢狀條列描述「判斷 → 顯示／行為」，搭配狀態術語（default／disabled／Error／hover／toast）。
  - **流程與系統建模 / Diagramming**：以 **循序圖（sequence）／活動圖（activity）／使用案例圖（use case）／BPMN** 表達系統互動、操作流程與角色行為，對齊 RD／QA 與利害關係人；循序圖、活動圖以 Mermaid 等 AI 工具加速產出，使用案例圖與 BPMN 手繪建模。
  - **對外 API 契約與安全架構設計（2026/09 起，進行中）**：主責一支**跨業合作夥伴查詢型 API** 的規格與合約議定——定義端點、請求／回應 JSON schema，並窮舉 **MECE 狀態面**（成功／格式錯誤／未授權或簽章逾時／超量限流四種情境各自的 HTTP 狀態碼與錯誤結構）；業務判斷邏輯依既有客戶狀態碼與名單規則收斂為單一「保護／可開發」二元判斷（延續 F10 的規則盤整方法論）。同時定義**傳輸與驗證安全性**：敏感識別碼一律置於 request body（不落 URL，避免留存於伺服器日誌／快取）、以 API 金鑰對 timestamp＋body 產出 **HMAC-SHA256 簽章**、**5 分鐘重放窗口**防禦、**RPS 限流**防禦。
- **工作證據 / Evidence**：skill 核心原則（狀態驅動、欄位即真相、MECE）；`初始化` 三段式（進入路徑／權限判斷／資料載入）；
  `[REF] 求才系統權限代碼表`；跨業合作夥伴 API 規格與合約議定文件（本人撰寫，進行中）。
- **資深度訊號 / Seniority signal**：把模糊需求轉成**可驗收的系統規格**，降低反工與上線風險；對外 API 合約議定更把規格能力延伸到**跨組織邊界**——需同時滿足己方業務保護邏輯、對方整合需求、與雙方都能驗收的安全承諾，是內部規格的自然升級。

> ⚠️ **對外引用務必抽象化**：可述「設計跨業合作夥伴查詢型 API，含簽章驗證、重放防禦、限流」，但**勿外露**內部端點名稱、欄位語意、廠商狀態碼定義與合作對象名稱（1111 機密／商業條款）。

---

**相關分頁 / Related**：[F10 業務邏輯梳理（上游）](F10-business-logic.md) ・ [F1 產品定義全鏈路](F01-product-definition.md) ・ [F5 交付流程與品質](F05-delivery-quality.md) ・ [旗艦專案 E.1](flagship-e1.md)
