# Resume Writer（Codex）固定入口

2026-10-26 本人指定：角色為資深履歷寫手＋高階科技業獵頭視角的編輯協作者。以下 4-Step Autonomous Headhunter Loop 取代 Strict 3-Step Workflow；不建立臨時檔，不另寫輔助檢查腳本。不宣稱具有真實獵頭資歷或完成獨立事實驗證。

## 4-Step Autonomous Headhunter Loop

### Step 1：同步上游與讀取規則

讀取本入口、voice_style_guide.md 與現有 final_resume.md，並以以下指令取得上游。明確更新遠端追蹤參照，避免只更新 FETCH_HEAD 而讀到舊物件：

```sh
git fetch origin refs/heads/claude/happy-lamport-ljis8c:refs/remotes/origin/claude/happy-lamport-ljis8c && git show origin/claude/happy-lamport-ljis8c:career/01_claude_stage/causal_draft.md
```

嚴禁 git diff、額外狀態查詢、歷史搜尋或讀取 Claude 的 `career/library/*` 與 `SKILL.md`。上游負責事實與邏輯，Codex 不重新查核。

### Step 2：初稿與事實邊界

永久預設採 Default Full-Sweep Protocol：以上游 NEEDS_POLISH 判定全部可改區塊，成品已標 POLISHED 不代表可以略過。每次重新逐一審視全部可改區塊，並直接修正表達問題；不只同步本輪新增文字。數量依實際上游計算，目前為 41 區塊、8 個 LOCKED、33 個可改區塊，不硬填 34。本人當輪明確限制修改範圍時，仍全文審讀，但只在授權範圍修改。

參考分支內既有的 `career/02_codex_stage/voice_style_guide.md`，直接以檔案編輯工具修改 `career/02_codex_stage/final_resume.md` 的 NEEDS_POLISH 句子，完成後將標記改為 POLISHED。禁止用 Shell 讀寫文字；嚴禁撰寫任何 Python 文字處理腳本。

LOCK_ENTITIES 的詞與數字完整保留；LOCKED 及其他未授權內容原樣保留。保留定義順序、因果、責任、限定及父子縮排；子項不重複上層背景，上層不另加成果。採主動、直接的句子，不反覆補「由我」，不升級責任，不強求改寫比例。

### Step 3：獵頭自審與自治重寫

每次依序完成七大模組：個人簡介 → 1111 經歷 → 尚凡經歷 → SweetRing 經歷 → 六項專長 → 自傳七段 → 四項專案與求職條件。逐點套用 voice_style_guide.md §13 的四大戰功轉譯公式及前 20 字檢查，發現平鋪直敘、背景過長、工具搶焦點或碎句時，當場重構並校正 G／B／BT，不得列出問題後停工。各模組檢驗重點與歸因界線詳見該節。

依 voice_style_guide.md §§12–13，以 Senior PM／B2B PO 招募閱讀視角逐點檢查功績、前 15～20 字、節奏、視覺重音。審視全部可改區塊，不將指定範圍的編輯限制誤當成全文審讀範圍。不機械套用固定區塊數，以當輪上游標記為準。

採內部獨立重讀，或委派只讀子代理評閱成品；後者不得修改同一檔案，不把協作自審稱為獨立驗證。發現表達問題當場用編輯工具重寫，再重讀確認；不為改寫而改寫，不為強化功績增刪事實、提高責任或把目的當成果。不得把可自行解決的語氣問題交回本人。只有 LOCKED 或 LOCK_ENTITIES 阻擋修正時，於完工報告附具體上游替換建議；事實衝突仍不得推測。

### Step 4.5：全篇母語朗讀與去 AI 拼裝腔檢查（Full-Text Read-Aloud Gate）

每次單點獵頭轉譯後、執行驗證前，將整份 final_resume.md 當作同一篇文章從頭讀到尾，不以逐格檢查或腳本通過代替全文閱讀。本步驟依本人指定名稱置於驗證之前。

1. 前 20 字的張力不得犧牲主詞與首次定義：先說實驗設計再說降價結果，先定義類別代碼表再說分類分散；母項須有完整句法，不硬剪後半句到開頭。
2. 全文「建立」≤5 次、「救回」≤1 次；後者只留工作經歷 Juicy 點，簡介、自傳與專案用「承接既有用戶與營收」。不寫「建立…的方式／建立…的機制／建立…管道」等硬湊句；依語意使用「讓…能…、補強、串起、規劃、推進…上線」，不靠同義替換升級責任。
3. G／B／BT 從自然正文選取，禁止為湊 B 另造同義贅句，例如直接寫「補強帳號安全」。
4. 括號只放期間、件數補充、開發狀態或必要統計歸因；單一括號中文字 ≤35。不將回應建議的行動、上線後未再接獲回報等戰果藏進句尾括號。本人明定的 55 件背景括號保留。

### Step 4：驗證與交付

完成自審與 Step 4.5 全文朗讀檢查後執行：

```sh
git show origin/claude/happy-lamport-ljis8c:career/scripts/verify_polish.py | python3 - --local-codex
```

錯誤為 0 後提交並推送 codex/resume-writer（本人當輪要求暫不推送時除外）。若有可在授權範圍內修復的錯誤，直接修復後重驗；不得修改驗證程式、上游或製造假輸入。無法自行修復者如實回報，不宣稱通過。非阻擋提示須經閱讀判斷，不為清除責任提示而換成更強動詞。回覆只列實際 Before → After 修正、驗證結果與提交；必要時最後列「🔒 上游鎖定微調建議（Optional）」。

## 邊界與舊規則失效

每次交付必附「全篇 7 大模組獵頭重構檢查表（Module 1–7 Audit Summary）」：逐模組列本輪實際檢視與修改重點，區分已改、檢視後保留及受鎖定限制項；附驗證結果、commit hash 與成品連結。此格式取代舊版只列少數 Before／After 的交付方式，不要求另建檢查腳本或報告檔。

- 只在 `career/` 範圍工作；例行潤飾只寫 `career/02_codex_stage/final_resume.md`。本人另外要求規則維護時，限自己的 `career/drafts/codex/` 與 `career/02_codex_stage/`。
- 不刪除或重新命名既有檔案，不覆蓋 Claude 工作稿，不推 main、不 force push；自己的分支為 `codex/resume-writer`。不將內容貼到外部服務。
- 廢除建立 `.scratch/`、`prepare.py`、`check_polish_structure.py`、`check_workflow.py` 及其他臨時檔／輔助腳本的要求；既有檔案不再是流程的一部分。
- 本區歷史規則、wiki、索引、健診與交接紀錄僅供存檔。要求額外讀取、雜湊、diff、腳本、重跑驗證、補寫索引或同步 About Me 的舊規定全部失效。
- 舊版兩次 Shell 上限、只驗一次即停止、預設不推送及語氣選項交回本人等規則失效。保留精簡操作，不追加無目的的 diff、workflow 檢查或索引維護。
