<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

> 🧭 [← 職能框架首頁 / Home](../competency-framework.md) ｜ `career/` 個人職涯 wiki 分頁，非 1111 規格文件（規則見 [`career/CLAUDE.md`](../CLAUDE.md)）

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
- **工作證據 / Evidence**：skill 核心原則（狀態驅動、欄位即真相、MECE）；`初始化` 三段式（進入路徑／權限判斷／資料載入）；
  `[REF] 求才系統權限代碼表`。
- **資深度訊號 / Seniority signal**：把模糊需求轉成**可驗收的系統規格**，降低反工與上線風險。

---

**相關分頁 / Related**：[F10 業務邏輯梳理（上游）](F10-business-logic.md) ・ [F1 產品定義全鏈路](F01-product-definition.md) ・ [F5 交付流程與品質](F05-delivery-quality.md) ・ [旗艦專案 E.1](flagship-e1.md)
