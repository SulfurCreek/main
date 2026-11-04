---
name: resume-review-panel
description: 將招聘審查交固定 Codex HR Subagent，不替 Claude 寫手恢復盲審或 FINAL LOCKED。
---

# Resume Review Panel：轉交固定 HR Subagent

招聘審查、推薦判斷與實際 persona 調度由 Codex HR Subagent Session 負責；治理為 codex/resume-writer:career/drafts/codex/REVIEWER_GOVERNANCE.md、hr-personas/PROTOCOL.md。
Claude Marketer 是主要上游行銷寫手，不因載入本 skill 變成主審；Fact Gatherer 仍只負責訪談與來源。角色契約在 career/ROLE_CONTRACT.md。
舊 rubric、kit、scripts、分數、二十 persona／同儕評比、HR→ATS→主管九步、多輪盲審、Claude Final Arbiter、FINAL LOCKED 與解鎖規則不再啟用。不要跑 build_run、f_scan、verify 或用平均分決定改稿。
HR 依本人的新審查任務實際派 persona，未派發就如實標記，不把 Writer／Marketer 自審當獨立結果。回饋依事實／行銷／表達分別交 Fact Gatherer／Marketer／Writer。
