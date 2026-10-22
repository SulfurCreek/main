---
name: resume-causal-logic-compiler
description: 專治履歷「概念偷跑（未定義先引用）」與「因果斷裂」問題。透過建立實體字典、強制單向依賴規則與邏輯審查閘門，確保每個 Bullet Point 具備獨立可讀性與嚴格的線性因果邏輯。
---
# Resume Causal Logic Compiler

## Core Compiler Rules (嚴格編譯規則)
1. **禁止前向引用 (No Forward Referencing)**：撰寫第 N 個 Bullet Point 時，絕對禁止直接使用第 N+1 個（或更後面）才會首次定義的系統名稱、專案代號或業務背景。
2. **首次提及必定義 (Define on First Use)**：任何內部專有名詞或系統在「第一次出現」時，必須附帶完整的上下文錨點（是什麼系統、服務什麼量級的受眾、解決什麼痛點）。
3. **單點獨立性測試 (Standalone Readability Test)**：假設把其他所有點遮住，只單獨讀當前這一點，外部 HR 也必須 100% 理解前因、動作與量化影響。
4. **句內因果結構**：以「量化成果 (Result) ｜ 核心行動與首次定義背景 (Action & Defined Context) ＋ 克服的限制與最終影響 (Constraint & Impact)」呈現。

## Execution Workflow
每次修改 `career/01_claude_stage/causal_draft.md` 時，必須先在內部完成：
1. **Phase 1 (Entity Dictionary)**：盤點本次涉及的專有名詞、外部白話定義與首次解鎖位置。
2. **Phase 2 (Topological Sort)**：檢查依賴順序，若前面的點依賴了後面才定義的系統，強制重排順序或將定義前移。
3. **Phase 3 (Verification Gate)**：確認無未知黑話、無 `**粗體開頭：**`、且已正確標註 `<!-- [STATUS: NEEDS_POLISH] [LOCK_ENTITIES: ...] -->` 或 `<!-- [STATUS: LOCKED] -->`。

---

## 附註（Career Move 增補，不影響上方原文；本人 2026-10-21／22 已裁定仍有效）

- **事實界線**：無 library 數字的點不估、不編，標〔待補數據〕交本人；本人是規劃／協作／驗收者，工程實作不歸本人，動詞不升級。
- **披露與跨欄位**：不寫投票名次、被延後項目、預計上線日期；進行中專案可寫狀態（本人 2026-10-22 允許信件與即時通寫「開發中」）；目標、提示文案、預期值不當成效；經歷移除的內容，專案／專長／自傳／簡介也不得殘留。
- **草稿結構**：`causal_draft.md` 的實體字典、拓撲大綱、檢查三節只供編輯，不屬於列點；成品（final_resume.md）不含這三節。
- 前版全文與本人原始版：在個人線分支 `claude/happy-lamport-ljis8c` 的 `career/skills/resume-causal-logic-compiler/references/`（main 的副本不含歷史版本）。
