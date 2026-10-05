<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

# 給主幹（Repo Steward）的變更請求 / Requests to main

本檔由 `claude/happy-lamport-ljis8c`（career session）依硬規則一寫入，**不自行修改** `career/` 以外的檔案。
請主幹判斷後統一施作，施作後可清空對應條目。

---

（目前沒有待處理請求。已施作：resume-craft F1–F15、作品集雙軌、求職信（`references/cover-letters.md`）、`portfolio-site` skill（主幹 `2947203`）。）

## 2026-10-05：路由表加上「104 履歷」，並與 Cake 履歷分開

**想改什麼**：根目錄 `CLAUDE.md` 路由表與 `resume-craft/SKILL.md` 任務路由各加一列：
「產生／填寫／驗證 104 履歷 → 先讀 `career/104/README.md`（欄位規格 `fields-spec.md`、內容 `resume-104.md`、匯入用 `resume-104-import.txt`）；
Cake Resume 另案，不得套用 104 的欄位規格與字數上限」。

**為什麼**：使用者之後還要產生 Cake Resume，兩個平台的欄位、必填項與字數限制不同，混用會填錯。career 內部路由已寫在 `career/CLAUDE.md`〈履歷平台路由〉。
