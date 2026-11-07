# v12.20 FINAL LOCKED（2026-11-03）

來源：Codex 549f3a1（自跑 verify_polish 0 錯誤＋獨立盲審一輪，報告 `drafts/codex/v12.20-polish-report.md` 在 Codex 分支）。
Claude Stage 4：`verify_polish.py` GATEKEEPER PASSED（41 區塊）；`gen_104_md.py` 產 `career/drafts/v12.20/104-v12.20.md`，`--verify-104` 通過。
收斂停機 4 項客觀檢查：①事實／限定詞：11-03 九句關鍵語（陳舊、向量演算法、新開發者、溝通窗口＋向上級說明、15 張、技術單位、完稿規格、可重複使用、導入）皆在，743／840、88%、52→79%、24→80%、開發中、提案滿 30 天口徑皆在 ②同段重複：無 ③概念偷跑：verify 通過 ④首句被動／單一動詞超標：主導 5（皆授權區塊）、推進 2。
不跑第 3 輪盲測。已知小項：視覺重音 15 金／15 藍（v12.19 為 18／17），1111「職位範疇」區塊未標重音；不影響驗收。

## 重潤版（Codex 7ed877d，基準上游 6ee7a2d）FINAL LOCKED
Claude Stage 4：`verify_polish.py` GATEKEEPER PASSED（40 區塊）；`gen_104_md.py` 產 `104-v12.20.md`，`--verify-104` 通過（含新增子項縮排斷言：4 個縮排子項皆為 `<li style="margin-left: 1em;">`，「以下兩項方案：」後兩點已縮排）。雙語版 `gen_104_bilingual.py`＋`verify_104_bilingual.py` Exit 0（專長 3.3 取完整兩句、3.4 取使用流程句、5.3 晴藍標名詞）。七點優化皆已落地。已知：KOOL 仍保留子項（上游結構）。

Codex 18a8b9f：移除 Scrum 後重產一般版與雙語版，verify_polish／--verify-104／verify_104_bilingual 皆通過，全檔 Scrum 0 次。
