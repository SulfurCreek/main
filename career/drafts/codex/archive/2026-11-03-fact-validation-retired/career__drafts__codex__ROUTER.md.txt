# Codex Resume Writer 路由

現行操作唯一入口為 [AGENTS.md](AGENTS.md) 的 4-Step Autonomous Headhunter Loop，順序依 AGENTS「正式入口對齊」節：全文自審、驗證 Exit 0、隔離盲審、改稿後重驗及全文閱讀。舊 Strict 3-Step、兩次 Shell 上限、只驗一次即停及完工後等待語氣選擇均已失效。

| 用途 | 路徑與規則 |
| --- | --- |
| 正式入口（唯讀例外） | `origin/claude/happy-lamport-ljis8c:career/CAREER_START_HERE.md`；只開放本檔，不開放受限來源 |
| 上游輸入 | `origin/claude/happy-lamport-ljis8c:career/01_claude_stage/causal_draft.md`；依 AGENTS Step 1 同步並記錄完整來源 SHA |
| 本地語氣參考 | [voice_style_guide.md](../../02_codex_stage/voice_style_guide.md)，配合 AGENTS 的現行規則 |
| 例行唯一潤飾產出 | [final_resume.md](../../02_codex_stage/final_resume.md) |
| 驗證 | 依 AGENTS Step 4 的來源檢查與 Bash 指令執行既有上游 verifier；必要修復後可重驗 |
| 規則維護 | 本人授權時限 `career/drafts/codex/` 與 `career/02_codex_stage/` |
| Claude／共用資產 | `career/library/`、`career/01_claude_stage/`、`career/scripts/`、main 及 repo 共用檔案不由本流程修改 |

每輪重新審視上游全部 NEEDS_POLISH；成品已標 POLISHED 仍需審讀，適切文字可保留。修改範圍依本人當輪授權，LOCKED、事實、數字、限定與父子縮排保留。視覺參數依語氣指南 §11，獵頭自審與全文朗讀依 §§12–14 及 AGENTS。

來源或驗證失敗不能以舊稿替代，也不能宣稱通過。既有 verifier 通過只代表已執行的檢查通過，不代表獨立事實驗證、104 轉換、PDF 或 ATS 通過；其漏檢項依 AGENTS Step 4 納入全文審讀。

履歷潤飾交付依 AGENTS 的七大模組摘要，附來源 SHA、實際驗證結果、commit 與成品連結。規則維護只回報本輪實際改動與檢查。

不讀 Claude library、applications 或 SKILL.md，不執行無關 diff，不新增臨時檔或輔助檢查腳本。歷史索引、wiki、技能與退役腳本僅供存檔，不構成現行流程要求。
