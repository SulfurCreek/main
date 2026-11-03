# 給 Codex：檢查器契約調整（T1，2026-11-03，本人已同意）

問題：`career/drafts/codex/scripts/check_polish_structure.py` 第 59 行要求成品不含 `[STATUS:` 等控制標記；Claude 端 `verify_polish.py` 要求 `final_resume.md` 保留標記。同一份檔案不可能兩者都過。

新契約：
1. `career/02_codex_stage/final_resume.md`＝**帶標記的編輯來源**（保留 `<!-- [STATUS: POLISHED|LOCKED] … -->`），由 Claude `verify_polish.py` 驗。
2. 由 Claude 分支的 `career/scripts/strip_markers.py` 產生 `career/02_codex_stage/final_resume.clean.md`＝**去標記成品**：
   `python3 career/scripts/strip_markers.py career/02_codex_stage/final_resume.md career/02_codex_stage/final_resume.clean.md`
3. `check_polish_structure.py` 改為驗 clean 檔：`check_polish_structure.py <causal_draft.md> <final_resume.clean.md>`。
4. 交件前必跑對帳：`python3 career/scripts/strip_markers.py --check career/02_codex_stage/final_resume.md career/02_codex_stage/final_resume.clean.md`，Exit 0。
5. **禁止**手動刪標記或在 clean 檔另行改字湊通過。

回報：check_polish_structure.py 的修改 commit SHA 與上述三個指令的結果。
