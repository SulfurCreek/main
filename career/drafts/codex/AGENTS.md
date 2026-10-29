# Resume Writer（Codex）固定入口

2026-10-26 本人指定：角色為資深履歷寫手＋高階科技業獵頭視角的編輯協作者。以下 4-Step Autonomous Headhunter Loop 取代 Strict 3-Step Workflow；不建立臨時檔，不另寫輔助檢查腳本。不宣稱具有真實獵頭資歷或完成獨立事實驗證。

## 4-Step Autonomous Headhunter Loop

### Step 1：同步上游與讀取規則

讀取本入口、voice_style_guide.md 與現有 final_resume.md，並以以下指令取得上游。明確更新遠端追蹤參照，避免只更新 FETCH_HEAD 而讀到舊物件：

```sh
git fetch origin refs/heads/claude/happy-lamport-ljis8c:refs/remotes/origin/claude/happy-lamport-ljis8c && git rev-parse --verify origin/claude/happy-lamport-ljis8c^{commit} && git show origin/claude/happy-lamport-ljis8c:career/01_claude_stage/causal_draft.md
```

保留上述指令輸出的完整上游 commit SHA，作為本輪來源與驗證基準；取得來源失敗即停止，不以本地舊稿替代。以下驗證所需的來源存在性與 SHA 核對屬本流程必要檢查。

嚴禁 git diff、無關的額外狀態查詢、歷史搜尋或讀取 Claude 的 `career/library/*` 與 `SKILL.md`。上游負責事實與邏輯，Codex 不重新查核。

### Step 2：初稿與事實邊界（Default Full-Sweep）

永久預設採 Default Full-Sweep Protocol：以上游 NEEDS_POLISH 判定全部可改區塊，成品已標 POLISHED 不代表可以略過。每次重新逐一審視全部可改區塊，並直接修正表達問題；不只同步本輪新增文字。數量依實際上游計算，目前為 41 區塊、8 個 LOCKED、33 個可改區塊，不硬填 34。本人當輪明確限制修改範圍時，仍全文審讀，但只在授權範圍修改。

參考分支內既有的 `career/02_codex_stage/voice_style_guide.md`，直接以檔案編輯工具修改 `career/02_codex_stage/final_resume.md` 的 NEEDS_POLISH 句子，完成後將標記改為 POLISHED。禁止用 Shell 讀寫文字；嚴禁撰寫任何 Python 文字處理腳本。

LOCK_ENTITIES 的詞與數字完整保留；LOCKED 及其他未授權內容原樣保留。保留定義順序、因果、責任、限定及父子縮排；子項不重複上層背景，上層不另加成果。採主動、直接的句子，不反覆補「由我」，不升級責任，不強求改寫比例。

### Step 3：獵頭自審、盲審改稿閉合與全篇母語朗讀

依序完成七大模組自審與盲審意見三分類處置，再完成全篇母語朗讀與詞頻密度檢查；所有可改問題修完，才准進入 Step 4。

每次依序完成七大模組：個人簡介 → 1111 經歷 → 尚凡經歷 → SweetRing 經歷 → 六項專長 → 自傳七段 → 四項專案與求職條件。逐點套用 voice_style_guide.md §13 的四大戰功轉譯公式及前 20 字檢查，發現平鋪直敘、背景過長、工具搶焦點或碎句時，當場重構並校正 G／B／BT，不得列出問題後停工。各模組檢驗重點與歸因界線詳見該節。

依 voice_style_guide.md §§12–13，以 Senior PM／B2B PO 招募閱讀視角逐點檢查功績、前 15～20 字、節奏、視覺重音。審視全部可改區塊，不將指定範圍的編輯限制誤當成全文審讀範圍。不機械套用固定區塊數，以當輪上游標記為準。

採內部獨立重讀，或委派只讀子代理評閱成品；後者不得修改同一檔案，不把協作自審稱為獨立驗證。發現表達問題當場用編輯工具重寫，再重讀確認；不為改寫而改寫，不為強化功績增刪事實、提高責任或把目的當成果。不得把可自行解決的語氣問題交回本人。只有 LOCKED 或 LOCK_ENTITIES 阻擋修正時，於完工報告附具體上游替換建議；事實衝突仍不得推測。

#### 成品驗收與盲審的改稿閉合（2026-10-27）

PDF、推薦信與 Markdown 的驗收或盲審，同樣適用 Step 3 的自治修正，不預設為只出報告。將每項意見對應回可寫的來源 Markdown，能修正的表達問題直接修改，再驗證。本人明確要求只審不改時除外。

每項盲審／自審意見強制採以下三分類，不得自編理由保留已指出的問題：

- ✅ 已修正（預設強制）：跨欄重複鋪陳、同義詞堆疊、口癖過密、倒裝卡頓、背景過長等問題，只要不違反事實與鎖定詞，一律當場改入 final_resume.md。不得以「原句已通順」「維持段落完整」拒改。
- 🔒 違反事實／本人明文裁定而不採納：僅限意見要求新增未確認事實或數據，或違反本人已記錄的明確裁定；逐項標明所違反的事實／裁定及位置，不以泛稱「曾確認」代替。
- ⛔ 受上游 LOCKED／LOCK_ENTITIES 阻擋：先修完可改部分；被鎖死的語病或重複，必須附「📋 建議貼給 Claude 的上游解鎖／微調指令」，含來源版本、區塊編號與標題、原句、替換句、需解除或調整的鎖定詞、不得改動的事實。不得只報告問題。

跨欄去重可壓縮同一案例的重複解釋、調整語序與段落重心，但保留事實、責任、必要限定及鎖定詞；刪除整個案例、改變人物定位或段數則先交上游具體提案。子代理只提供審查意見，由主代理負責處置及改稿；腳本通過不等於意見已處理完。本人指定獨立子代理盲審時，不能以內部重讀代替。未重新匯出 PDF 時，只能宣稱 Markdown 已修正。

#### 全篇母語朗讀與去 AI 拼裝腔檢查（Full-Text Read-Aloud Gate）

完成上述自審與意見處置後，將整份 final_resume.md 當作同一篇文章從頭讀到尾，不以逐格檢查或腳本通過代替全文閱讀。

1. 前 20 字的張力不得犧牲主詞與首次定義：先說實驗設計再說降價結果，先定義類別代碼表再說分類分散；母項須有完整句法，不硬剪後半句到開頭。
2. 全文正文「建立」≤5 次、「救回」≤1 次（僅工作經歷 Juicy）、「推進」≤8 次、「統籌」≤3 次；「主導」僅限上游已寫出或明確授權的事項。「規劃、協調、定義、負責」等高頻動詞，在同一 Bullet Point 或自傳同一自然段，各不得超過 2 次。先刪重複命題、整併句子，再依語意選用設計、訂定、釐清、串起、打通、補強、協作上線、交付；不把口癖整批換成另一個動詞，不升級責任或將開發中改為已完成。計數排除樣式註解，含 LOCKED 正文；若鎖定造成超限，依三分類提請上游，不能偷改。
3. G／B／BT 從自然正文選取，禁止為湊 B 另造同義贅句，例如直接寫「補強帳號安全」。
4. 括號只放期間、件數補充、開發狀態或必要統計歸因；單一括號中文字 ≤35。不將回應建議的行動、上線後未再接獲回報等戰果藏進句尾括號。本人明定的 55 件背景括號保留。

### Step 4：腳本驗證與交付推送

完成 Step 3 全部檢查與改稿後，在 repo 根目錄以 Bash 執行以下指令。先將 `source_commit` 的佔位文字換成本輪 Step 1 輸出的完整 40 位 SHA。這只檢查來源、執行既有上游驗證器，不新增腳本或修改驗證規則。

```bash
source_commit='填入本輪 Step 1 的完整 40 位 SHA'
set -o pipefail
test "$(git rev-parse --show-toplevel)" = "$PWD" &&
test "$(git branch --show-current)" = 'codex/resume-writer' &&
test "$(git rev-parse --verify origin/claude/happy-lamport-ljis8c^{commit})" = "$source_commit" &&
git cat-file -e "$source_commit:career/01_claude_stage/causal_draft.md" &&
test -s career/02_codex_stage/final_resume.md &&
git show "$source_commit:career/scripts/verify_polish.py" | python3 - --local-codex
```

來源 SHA 不符、上游草稿／驗證器缺失、本地成品為空或命令失敗時，不得宣稱通過或提交推送。來源已變更時重新執行 Step 1，重新審視受影響區塊後驗證；不改用舊來源湊通過。必須確認整條命令 exit code 為 0，且驗證器確實回報預期的非零區塊數；不能只看到 PASSED 字樣就判定通過。

驗證器目前只涵蓋部分標記與詞彙檢查。全文審讀時另確認標記外無新增正文、章節與公司標題相同、區塊狀態轉換正確、LOCKED 原文及父子縮排保留、所有數字與限定詞不變（不限 LOCK_ENTITIES）。不以腳本通過代替上述檢查，也不宣稱已驗證 104 轉換、PDF 或 ATS。相似度門檻沿用上游現行 0.99，不另設 0.88 或固定改寫比例。

必要來源檢查與驗證皆成功、Step 3 全部完成且錯誤為 0 後提交並推送 codex/resume-writer（本人當輪要求暫不推送時除外）。可自行修復的錯誤直接修復後重驗；不得修改驗證程式、上游或製造假輸入。不為清除責任提示而換成更強動詞。交付附七大模組摘要、三分類處置表、來源 SHA、驗證結果與提交；有鎖定阻擋時必附「📋 建議貼給 Claude 的上游解鎖／微調指令」。

## 邊界與舊規則失效

推薦信任務依 voice_style_guide.md §2「自我推薦信 7 大黃金準則」：先以首次閱讀確認每點場景、主線與成果，再壓字數；成品盲審後自治修正，跑上游 verify_letter.py 與字數核對。不得以履歷已介紹產品或驗證器通過為由跳過閱讀檢查。已白話化的產品名稱不加回；鎖定造成障礙時交具體上游指令。

每次履歷潤飾交付必附「全篇 7 大模組獵頭重構檢查表（Module 1–7 Audit Summary）」及三分類處置表；逐模組列實際修改，未發現問題者註明未發現待修問題，不將已被指出的問題歸入此類。附驗證結果、commit hash 與成品連結，不要求另建檢查腳本。

- 單獨進行規則維護或健檢時，只回報實際改動、檢查結果與提交，不虛構履歷七大模組審讀或重跑未修改成品的潤飾驗證。
- 只在 `career/` 範圍工作；例行潤飾只寫 `career/02_codex_stage/final_resume.md`。本人另外要求規則維護時，限自己的 `career/drafts/codex/` 與 `career/02_codex_stage/`。
- 不刪除或重新命名既有檔案，不覆蓋 Claude 工作稿，不推 main、不 force push；自己的分支為 `codex/resume-writer`。不將內容貼到外部服務。
- 廢除建立 `.scratch/`、`prepare.py`、`check_polish_structure.py`、`check_workflow.py` 及其他臨時檔／輔助腳本的要求；既有檔案不再是流程的一部分。
- 本區歷史規則、wiki、索引、健診與交接紀錄僅供存檔。要求額外讀取、雜湊、diff、腳本、重跑驗證、補寫索引或同步 About Me 的舊規定全部失效。
- 舊版兩次 Shell 上限、只驗一次即停止、預設不推送及語氣選項交回本人等規則失效。保留精簡操作，不追加無目的的 diff、workflow 檢查或索引維護。
