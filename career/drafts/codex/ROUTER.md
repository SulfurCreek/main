# Codex Resume Writer 路由

2026-10-22 本人指定：操作只依 [AGENTS.md](AGENTS.md) 的 Strict 3-Step Workflow。每次履歷潤飾最多 2 次 Shell 指令，不增加前置讀取或收尾步驟。

| 用途 | 唯一路徑 |
| --- | --- |
| 上游輸入 | `career/01_claude_stage/causal_draft.md`，以 AGENTS 的唯一讀取指令取得 |
| 本地語氣參考 | `career/02_codex_stage/voice_style_guide.md` |
| 唯一潤飾產出 | `career/02_codex_stage/final_resume.md` |
| 唯一驗證 | `python3 career/scripts/verify_polish.py --local-codex`，一次 |

直接用檔案編輯工具改 NEEDS_POLISH，保留鎖定內容與父子層級，改完標記為 POLISHED。驗證通過即結束，不更新路由、索引、語氣指南、wiki 或交接檔。

不讀 library 或 SKILL.md，不執行 git diff，不建立臨時檔或文字處理腳本，不執行額外 workflow／結構檢查。歷史索引、wiki、腳本與舊交接紀錄均不再提供例行操作要求。
