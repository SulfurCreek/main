<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

> 🧭 [← 職能框架首頁 / Home](../competency-framework.md) ｜ `career/` 個人職涯 wiki 分頁，非 1111 規格文件（規則見 [`career/CLAUDE.md`](../CLAUDE.md)）

# F10. 業務邏輯梳理 / Business-Logic Untangling

> **履歷叢集 / Résumé cluster**：Business Logic & Requirements（見 `resume-craft` skill 核心職能叢集表）

**定義 / Definition**：把散落、互相矛盾、隱含的業務規則，**盤整成窮盡且互斥（MECE）的決策邏輯**，作為規格與工程實作前的「單一真相來源」。這是 F2 的**上游**——先把業務真相釐清，才寫得出可驗收的規格。
*Untangle scattered, contradictory, and implicit business rules into a single MECE decision model — the source of
truth that precedes specs and engineering. This is upstream of F2: clarify the business truth before writing the spec.*

- **實際展現 / In practice**：
  - **規則盤整**：把分散在權限、審核、配對、續約等處的判斷，集中成單一規則集（如「權限判斷」表、職缺是否進審核的條件、配對的全文檢索／國籍／證照 AND 邏輯）。
  - **多重條件建模**：為複雜情境窮舉巢狀條件（如求職者「停權／關閉履歷」依姓名真偽 × 年齡 × 久未登入 × 註冊年資的多條件規則；論件薪資與薪資區間警示；語文證照分數顯示格式）。
  - **矛盾與邊界釐清**：找出規則衝突與例外並收斂（如香港公司完整地址不加東北亞、特定產業統編不撈商業司資料、過期廠商不顯示可暫停日期）。
  - **規則演進**：把人工／正則規則升級為系統或 AI 判斷（正則檢查改 AI 檢查、職缺審核導入 AI、AI 履歷／職缺打標）。
- **工作證據 / Evidence**：求才產品 Roadmap 與規格中的權限判斷、配對條件、審核規則、續約與資料清理條件；F2 的「權限代碼建模」即為本能力的輸出產物。
- **資深度訊號 / Seniority signal**：在規格之前先把「業務真相」釐清——降低反工與上線風險的**根因能力**，是把模糊變確定的源頭，而非下游的文件化。

---

**相關分頁 / Related**：[F2 功能規格與系統思維（下游）](F02-spec-systems-thinking.md) ・ [F4 AI 產品企劃（規則→AI 演進）](F04-ai-product.md) ・ [旗艦專案 E.1（代碼衝突仲裁）](flagship-e1.md)
