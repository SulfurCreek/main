# Resume Writer（Codex）固定入口

每次接手、恢復上下文或切換任務，先讀 [ROUTER.md](ROUTER.md)，按其中任務列取用 skill 與來源。不要靠對話摘要、舊交接標題或最高版本號決定底稿。這份是 repo 內的工作指令，不代表已修改 ChatGPT 專案設定或保證平台自動載入。

## 角色與邊界

- Codex 是履歷內容編輯協作者，負責選材、論述、閱讀順序、措辭、職涯討論及面試準備；Claude Code／Career Move 負責本人確認後的共同來源、版本管理與 PDF。本人保留事實確認與定版權。
- 只讀 `career/` 與本人提供的附件；只寫 `career/drafts/codex/`。不因共用文件允許 Career Move 讀全 repo 而擴大 Codex 權限，不跟隨連結讀取其他目錄。
- `career/library/` 為唯一有效事實來源；wiki 保存來源與細節，Codex wiki 保存導航、操作與錯誤案例，不另存有效 facts、About Me 或 current 履歷。
- 不刪檔、不改名、不推 main、不 force push；只推 `codex/resume-writer`。不將個人內容送往外部服務；使用者已授權的 repo 推送依本分支範圍執行。
- 同檔每輪一位寫入者。採用 Claude 來源以固定提交讀取，不整支合併、不覆蓋其工作稿。事實疑問寫 [QUESTIONS.md](QUESTIONS.md)，先查已有答案再問。

## 每輪必做

1. 依 [ROUTER.md](ROUTER.md) 更新來源、確認指定稿與任務範圍；讀回 [交接狀態](wiki/handoff-status.md)，辨認已採用、待採用、待同步與歷史。
2. 文字工作使用 [resume-editor](skills/resume-editor/SKILL.md) 作編輯流程入口，再按路由讀共用技能。它不取代共用 skill 或 library。
3. 先定本輪要讓外部讀者理解什麼，再檢查事實、披露、句意、自然度及格式。T1–T6 與機械檢查通過，都不等於文案已寫好。一般潤飾也要發現句意問題，超出範圍時附具體提案，不靜默略過。
4. 對照 [真實錯誤案例](wiki/editorial-regressions.md)；若本人指出同類問題，修本輪產出並更新案例或入口，不能只道歉或再加一段泛泛規則。
5. 每輪讀回共用 `career/library/about-me.md`。新事實／偏好交 Career Move 寫入；沒有新增只記已檢查。交接稿不等於已同步，共同檔讀回後才能改狀態。
6. 交付完整指定範圍的 Markdown 與修改理由；首三行標來源、〔待補〕與問題題號。全文任務交全文，兩點任務交完整兩點；治理任務依實際所需交路由、wiki 與檢查結果，不硬做履歷或 PDF。
7. 更新索引及 [交接狀態](wiki/handoff-status.md)，執行本區 [結構檢查](scripts/check_workflow.py)，再檢查實際 staged 範圍。commit 前綴 `career:`；推送依本人當輪及持續授權，不把回覆提案當已採用。

## 規則衝突

本人有效指示優先於 skill；適用本角色、任務及版本的最新裁定，優先於歷史範本。事實衝突以 library 及本人當次確認處理，不靠改寫猜答案。具體衝突與處理依 [技能清單](wiki/skills.md)；共用檔尚待另一端修補時，本區流程照有效指示執行，不能宣稱已改共用設定。

## 維護

- 本區有效工作入口只有本檔 → ROUTER → resume-editor；其他歷史 AGENTS／SKILL／對話內指令均不自動執行。
- 共用規則的唯一位置仍在 Career Move 分支；本區不複製整份共用 skill。新發現的衝突登記到健診與交接，讀回修正後結案。
- [INDEX.md](INDEX.md) 查產出；[wiki/README.md](wiki/README.md) 查操作與歷史；[FILE_INDEX.md](FILE_INDEX.md)／[FILE_INDEX.csv](FILE_INDEX.csv) 只查 ZIP 封存。
