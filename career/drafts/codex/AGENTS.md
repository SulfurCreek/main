# Resume Writer（Codex）固定入口

2026-10-22 本人指定：以下 Strict 3-Step Workflow 取代本區所有舊操作規則。每次履歷潤飾最多執行 2 次 Shell 指令，不建立臨時檔，不另寫或執行輔助檢查腳本。

## Strict 3-Step Workflow

### Step 1：唯一一次讀取指令

只准執行以下一行，不追加其他命令：

```sh
git fetch origin claude/happy-lamport-ljis8c && git show origin/claude/happy-lamport-ljis8c:career/01_claude_stage/causal_draft.md
```

嚴禁 git diff、額外狀態查詢、歷史搜尋或讀取 Claude 的 `career/library/*` 與 `SKILL.md`。上游負責事實與邏輯，Codex 不重新查核。

### Step 2：直接改字

參考分支內既有的 `career/02_codex_stage/voice_style_guide.md`，直接以檔案編輯工具修改 `career/02_codex_stage/final_resume.md` 的 NEEDS_POLISH 句子，完成後將標記改為 POLISHED。禁止用 Shell 讀寫文字；嚴禁撰寫任何 Python 文字處理腳本。

LOCK_ENTITIES 的詞與數字完整保留；LOCKED 及其他未授權內容原樣保留。保留定義順序、因果、責任、限定及父子縮排；子項不重複上層背景，上層不另加成果。採主動、直接的句子，不反覆補「由我」，不升級責任，不強求改寫比例。

### Step 3：唯一一次驗證指令

只執行一次：

```sh
python3 career/scripts/verify_polish.py --local-codex
```

通過即回覆結果並結束任務。不得再執行額外檢查或 git 指令，也不修改 INDEX.md、ROUTER.md、voice_style_guide.md 等設定與交接檔。驗證失敗或程式缺失時如實回報，不追加 Shell、不建立暫存副本、不自改驗證程式或上游。

## 邊界與舊規則失效

- 只在 `career/` 範圍工作；例行潤飾只寫 `career/02_codex_stage/final_resume.md`。本人另外要求規則維護時，限自己的 `career/drafts/codex/` 與 `career/02_codex_stage/`。
- 不刪除或重新命名既有檔案，不覆蓋 Claude 工作稿，不推 main、不 force push；自己的分支為 `codex/resume-writer`。不將內容貼到外部服務。
- 廢除建立 `.scratch/`、`prepare.py`、`check_polish_structure.py`、`check_workflow.py` 及其他臨時檔／輔助腳本的要求；既有檔案不再是流程的一部分。
- 本區歷史規則、wiki、索引、健診與交接紀錄僅供存檔。要求額外讀取、雜湊、diff、腳本、重跑驗證、補寫索引或同步 About Me 的舊規定全部失效。
- 例行潤飾驗證通過即結束，不自動 commit／push，不把 git 交付偷加到驗證指令；版本交付依本人另外指定的任務處理。
