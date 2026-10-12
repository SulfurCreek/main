# Session 任務簡介（給 Project 協調者派工用）

> 用途：Project 的協調者要把工作派給 worker 執行緒（sub agent）時，用本檔判斷「這件事該給誰」以及「交辦時要帶什麼」。
> 完整職責對照與 session_id 快照見 [`session_directory.md`](session_directory.md)；本檔只講這兩個常駐 session。
> 維護：只有 Repo Steward 改本檔。分支與規則是穩定的，側欄名稱與 session_id 會變，**以分支為準**。

## 一眼判斷

| 需求長什麼樣 | 派給 |
| :--- | :--- |
| 寫／改 HackMD 規格書文字、章節、狀態表、紅字、版控表；E.1 信件即時通整併；把圖「放進」文件 | **文件助手** |
| 在截圖上畫紅框／badge／編號；把多張圖組成流程圖／點擊流程圖；做規格書示意圖版面 | **規格文件 HTML 示意圖助手** |
| 一件事同時要「示意圖」和「放進文件」 | 先示意圖助手出圖 → 再文件助手搬 R2＋嵌入。**順序固定，兩邊不互相代做** |

不確定時不要硬套，回頭問使用者；也可載入 `session-router` skill 查 `session_directory.md`。

---

## 1. 文件助手

| 項目 | 內容 |
| :--- | :--- |
| 職責 | 1111 求才／求職系統 HackMD 規格書的內容撰寫與修改：章節結構、MECE 狀態表、Use Case、紅字需求、版控表、`🚧 待補` 區塊；E.1 聯絡人才／信件即時通整併；履歷文件編修之外的 HackMD 文件維護 |
| 分支 | `main`（歷史上 outcome 寫 `claude/claude-md-docs-BmaVo`，該分支仍可能被它使用，**不要刪**） |
| 專屬資料 | HackMD 團隊 `1111-jobdocs`；本機快取 `notes/`、API 契約 `notes/api/`；素材與 inference 規則見 `wiki/recruitment_system_rules.md` §3、§6 |
| 必讀 | `spec-doc-1111` skill（格式細則）、`wiki/hackmd_rules.md`（API）、`wiki/recruitment_system_rules.md`（業務代碼、求才 vs 求職先確認）、`wiki/glossary.md`（縮寫） |
| 寫入方式 | 改既有 HackMD note 一律走 `scripts/hackmd_safe_patch.py`（baseline → 本地改 → 回寫；遠端被改過會 exit 1 中止，不盲蓋）。Token 在環境變數 `HACKMD_TOKEN`，不寫進任何檔案 |
| 圖片 | **只做「搬到 R2＋限寬嵌入」**。收到繪製需求不動手，轉給示意圖助手 |
| 做什麼之前先確認 | 文件屬於求才還是求職專案（範本不同）；引用後端欄位時只用 `notes/api/` 的契約，缺資料標 `NULL`，不推測 |
| 絕對不碰 | `career/` 內容（絕不寫進 HackMD）；`.claude/skills/`、`wiki/`、`CLAUDE.md` 等共用資產（歸 Repo Steward）；圖片繪製 |
| 與 skill 衝突時 | 以 HackMD 上的規格為準，回頭請 Repo Steward 修 skill |

**交辦時要帶**：目標文件（HackMD note 連結或內部 noteId）、要改的章節、需求原文或截圖、是求才還是求職、是否已有 baseline。
**回報格式**：改了哪個 note／章節、版號變化、回寫結果（exit code）、仍待補項目。

---

## 2. 規格文件 HTML 示意圖助手

| 項目 | 內容 |
| :--- | :--- |
| 職責 | 規格書用的示意圖**繪製**：Figma MCP 截圖存檔、截圖上的紅框／badge／編號標註、組合流程圖／點擊流程圖、示意圖版面 |
| 分支 | `claude/gifted-meitner-6eSoK`。**開工前必須先 `git fetch origin main && git merge origin/main`**，在最新 main 之上作業 |
| 必讀 | `photo` skill（主規則）；`png` skill 僅在需要「覆蓋改寫截圖裡既有文字」或維護舊版「截圖標號＝章節編號」規格書時才用；`wiki/mermaid_styling_rules.md`（有 Mermaid 時） |
| 核心鐵則 | 標註一律用 **HTML 絕對定位覆蓋**，不把 badge 燒進圖片像素；**禁止使用任何外部 AI 圖像生成模型**渲染畫面；成品圖一律存 **R2**（不再沿用 `hackmd.io/_uploads` 或 GitHub raw） |
| 輸出 | 成品圖的 R2 網址＋預覽網址／對照表，交給文件助手嵌入 |
| 絕對不碰 | HackMD 文件文字內容；共用資產；用分支自己的舊版 skill（一律用 main 上的 `photo`／`png`） |

**交辦時要帶**：Figma 連結或截圖、要標註的位置與編號對應、輸出用途（哪份文件哪個章節）、版面寬度限制。
**回報格式**：成品 R2 網址、標號對照表、哪些位置不確定。

---

## 派工原則（給協調者）

1. **一個執行緒一個主題**，不要把「畫圖」和「改文件」塞進同一個執行緒。
2. **兩個執行緒不要同時改同一份 HackMD note**；同一份文件的修改排隊處理。
3. 兩個助手都**不能改共用資產**（`CLAUDE.md`／`.claude/skills/`／`wiki/`／`scripts/`／`.claude_index.md`／`.claude/settings.json`）。需要改時回報，轉給 Repo Steward。
4. 協調者自己不要替它們動手寫規格或畫圖，只負責派、收、串接順序。
5. 派出前確認基準：執行緒要從**最新 `main`** 開始（示意圖助手還要先 merge main）。
6. 回報收到後，把結果寫進專案記憶時只記「決定與產出位置」，不要複製規格內文，以免與 HackMD 上的版本分岔。
