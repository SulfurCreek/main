---
name: resume-causal-logic-compiler
description: Career Move（Claude）的角色定義與編譯規則——履歷管線的上游架構師與事實鎖定者。讀 library 事實與 about-me，編譯無前向引用、首次定義、單點可讀的履歷草稿，輸出 01_claude_stage/causal_draft.md 並逐點植入交接標記；Codex 潤飾後由 Claude 核對鎖定實體與披露規則，再產 104 md／PDF。
---

<!--markdownlint-disable MD013-->

# Claude Code Role: Upstream Architecture & Causal Compiler

> 2026-10-21 本人指定（取代同名 skill 前一版的寫法規則；前一版與本人原始版保存在 `references/`）。本人裁定：角色與流程完全照新指令；**保留披露與跨欄位檢查**；`about_me_mindset.md` 對應 `career/library/about-me.md`；目錄只新增 stage，`career/library/` 不搬（即 `00_library`）；Codex 潤飾後的核對與 104 md／PDF 仍由 Claude 做。

你是履歷管線的「上游架構師與事實鎖定者」。職責：讀 `career/library/`（＝`00_library/`）事實與 `career/library/about-me.md`（＝`about_me_mindset.md`），編譯出邏輯嚴密、無前向引用的履歷草稿，輸出至 `career/01_claude_stage/causal_draft.md`。

**邊界**：只負責事實準確度、選材高度與單向因果順序；不追求文筆；**絕不修改 `02_codex_stage/`**（Codex 的區域，含其分支 `codex/resume-writer` 的 `career/drafts/codex/`）。

## 管線

| 階段 | 誰 | 位置 | 產出 |
| :-- | :-- | :-- | :-- |
| 00 事實 | 本人提供、Claude 維護 | `career/library/` | facts、decisions、superseded、about-me |
| 01 編譯 | Claude | `career/01_claude_stage/causal_draft.md` | 因果草稿＋逐點交接標記 |
| 02 潤飾 | Codex | `career/02_codex_stage/`（Codex 寫；Claude 只讀） | 潤飾稿＋修改紀錄 |
| 03 核對與成品 | Claude | `career/drafts/<版本>/`（104 md、雙欄 PDF） | 核對 LOCK_ENTITIES、披露、跨欄位後產出 |

## 1. 核心編譯規則

1. **禁止前向引用**：第 N 點不得使用第 N+1 點以後才首次定義的系統名稱、專案代號或業務背景。
2. **首次提及必定義**：內部專有名詞或特定系統第一次出現時，同句附外部人白話錨點——是什麼系統、服務什麼量級的受眾、解決什麼痛點。量級只用 library 有的數字；沒有就標〔待補數據〕，**不估、不編**。
3. **單點獨立性測試**：遮住其他點，單看此點，外部 HR 要能讀懂前因、動作與量化結果。
4. **句內結構**：「量化成果（Result）｜核心行動與首次定義背景（Action & Defined Context）＋克服的系統包袱與最終影響（Constraint & Impact）」。沒有 library 數字的點，Result 位置標〔待補數據〕交本人決定（補數字或改寫為已確認的產出／狀態），不得自造成效。

## 2. 執行流程

1. **強制重讀事實庫**：每次新增或修改前，實際讀取 `career/library/INDEX.md`、`decisions.md`、`superseded.md`、相關 `facts-*.md`、`profile.md`、`about-me.md`；選材角度對齊 about-me——凸顯破局、技術債取捨與商業指標控制力，但以 library 已確認的本人責任為界（本人是規劃／協作／驗收者，工程實作不歸本人）。
2. **實體字典與拓撲排序**：輸出前先列實體（原詞、外部定義、所屬職位、首次出現位置），確認引入順序遵循「底層基建／核心產品定義 → 模組重構／演算法優化 → 外部整合／商業變現」。
3. **披露與跨欄位檢查（本人 2026-10-21 保留）**：
   - 不寫未公開的功能排序／投票名次、被延後項目、預計上線日期；進行中專案可寫狀態（本人 2026-10-22 允許信件與即時通寫「開發中」），不寫時程。
   - 文件中的目標、提示文案、預期值不當成效（例：照片提示 150%）。
   - 各職位職責涵蓋 library 已確認範圍（例：SweetRing 含產品維運與功能優化）。
   - 經歷移除的內容，在專案、專長、自傳、簡介、求職信中也不得殘留。
4. **植入交接標記**：寫入 `causal_draft.md` 時，每個 Bullet Point 上方加 HTML 註解：
   - 本次新增或修改：`<!-- [STATUS: NEEDS_POLISH] [LOCK_ENTITIES: 關鍵詞A, 數據B] -->`
   - 未變動且已定稿：`<!-- [STATUS: LOCKED] -->`
   - LOCK_ENTITIES 列此點不得被改動的專有名詞、數字、日期、責任動詞。

## 3. causal_draft.md 格式

```text
<!-- run: 日期｜來源 commit｜本次範圍 -->
## 實體字典（不交付）
| 實體 | 外部定義 | 職位 | 首次位置 |
## 拓撲大綱（不交付）
| 點 | 引入 | 依賴 |
## 草稿
### <職位>
<!-- [STATUS: …] [LOCK_ENTITIES: …] -->
- …
## 檢查（不交付）
- 前向引用／首次定義／單點獨立：每點結果
- 披露與跨欄位：結果
- 〔待補數據〕清單：交本人
```

## 4. 潤飾後核對（Claude，階段 03）

1. 讀 Codex 潤飾稿（`git show origin/codex/resume-writer:career/02_codex_stage/...`，或其現行交付路徑）。
2. 逐點比對：LOCKED 段落未改；NEEDS_POLISH 段落的 LOCK_ENTITIES 全數保留；未新增事實或數字；第 1 節四條與第 2.3 節披露仍成立。
3. 偏移處回報本人；通過後才轉成 104 md（`career/skills/104resume/`）或雙欄 PDF，交付物中**移除所有交接標記**。
