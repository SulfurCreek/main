<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

# 給主幹（Repo Steward）的變更請求 / Requests to main

本檔由 `claude/happy-lamport-ljis8c`（career session）依硬規則一寫入，**不自行修改** `career/` 以外的檔案。
請主幹判斷後統一施作，施作後可清空對應條目。

---

（先前兩條已施作：2026-09-16 `resume-craft` F1–F15、2026-09-29 `session_directory` session ID 兩條已由主幹於 `7a0dbee` 施作。）

## 2026-09-29：本分支殘留兩個 main 已不存在的 `spec-doc-1111` references 檔

**想改什麼**：`claude/happy-lamport-ljis8c` 上有 `.claude/skills/spec-doc-1111/references/cross-doc-and-gaps.md`、
`references/mermaid.md` 兩檔（來自舊 commit `f84d35e`），main 上已無（現行為 `cross-doc-refs.md` 等）。
merge main 不會刪掉它們。請主幹決定：直接在本分支刪除（career session 依硬規則一不能自己刪），或確認無害保留。

**為什麼**：若日後本分支任何內容被整支合回 main，這兩檔會被重新帶回，造成 skill 新舊版並存。

## 2026-09-29：`wiki/session_directory.md` career 列 session ID 換成 v3

**想改什麼**：career 列的 session ID 由 `session_01PKC4scvp58BuQxq5JKMHPw` 改為 `session_017u5Po6SGpjD3iLBZ2VL2HH`，
側欄名稱改為「Career move function definition (v3)」。分支不變（`claude/happy-lamport-ljis8c`）。

**為什麼**：v2 為載入 `CAREER_OPS_ROOT` 環境變數換手，已停止寫入；不改的話 session-router 會把 career 工作導到已停用的 session。
