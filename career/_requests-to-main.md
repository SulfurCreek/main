<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

# 給主幹（Repo Steward）的變更請求 / Requests to main

本檔由 `claude/happy-lamport-ljis8c`（career session）依硬規則一寫入，**不自行修改** `career/` 以外的檔案。
請主幹判斷後統一施作，施作後可清空對應條目。

---

## 2026-10-19｜移除誤傳到 `claude/claude-md-docs-BmaVo` 的 `career/companies.md`、`career/jobs.md`

- 使用者在 GitHub 網頁上傳時落在 `claude/claude-md-docs-BmaVo`（commit `17ca5ab`），不是個人線分支。
- 個人線已收進 `career/targets/jobs.md`、`career/targets/companies.md`（內容相同，修正一處表格跳脫）。
- 請主幹在 BmaVo 刪除這兩個檔，避免 `career/` 在兩條線各有一份。個人線不推其他分支。

---

（其餘無待處理請求。已施作：resume-craft F1–F15、作品集雙軌、求職信、`portfolio-site`、個人線協作規則、104 履歷路由與 `tw-voice.md`、`resume-review-panel`、去 AI 感＋ATS 規範（主幹 `80bf591`）、V4 防禦型規則（主幹 `95e4223`）、resume-review-panel 審查清單 v2（主幹 `a6997eb`）。）

## 2026-10-20 納管兩個個人線 skill：104coverletter、104resume

- 想要：把 `career/skills/104coverletter/`、`career/skills/104resume/` 註冊為可用 skill（例如在 `.claude/skills/` 建同名目錄，或加入個人線自有 skill 清單讓本分支自行維護）。
- 為什麼：本人要求獨立成 skill；本 session 依硬規則一不能新建 `.claude/skills/` 目錄。內容與 1111 主線無關，建議比照 resume-craft 歸個人線擁有。

## 2026-10-22 註冊 skill：resume-causal-logic-compiler（比照 104resume 流程）

- 想要：把 `career/skills/resume-causal-logic-compiler/` 註冊為可用 skill（例如在 `.claude/skills/` 建同名目錄，或納入個人線自有 skill 清單由本分支維護）。
- 為什麼：本人要求；本 session 依硬規則一不能新建 `.claude/skills/` 目錄。內容與 1111 主線無關，建議比照 `resume-craft` 歸個人線擁有。檔案已依本人指定內容寫入，並附 Career Move 增補附註（事實界線、披露規則）。

