<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

# career/ — 個人職涯資料 / Personal career material

這裡是**使用者的個人職涯資料**（職能盤點、履歷素材、作品集），與本 repo 的 1111 規格文件工作**刻意分開**。
當成一般 Markdown 文件處理即可。

## 📚 開工第一步：讀 `library/`（2026-10-08 起）

**使用者提供、確認、更正過的所有事實與決定收在 [`library/`](library/README.md)**，衝突時優先於 `wiki/` 與任何產出檔。
動筆前至少讀 [`library/decisions.md`](library/decisions.md)＋對應的 `facts-*.md`；審稿時對照 [`library/superseded.md`](library/superseded.md)；
遇到〔待補〕先查 [`library/open-questions.md`](library/open-questions.md)，已答過的不要再問。

**使用者在對話中提供任何新事實、更正或決定 → 當下先寫進 library（附日期與來源），再改下游檔案。** 被推翻的舊說法移到 `superseded.md`，不刪。
這條是為了解決「之前提供的資訊被忘記」：wiki 是逐次疊加的證據層，讀到舊段落就會寫回已更正的內容。

*The user's personal career material — competency inventory, résumé source, portfolio. Deliberately kept apart
from this repo's 1111 spec-documentation work. Treat as plain Markdown.*

## 🚫 硬規則一：全部可讀，只有 `career/` 與自有 skill 可寫 / Read everything, write only `career/` and owned skills

這條 session（分支 `claude/happy-lamport-ljis8c`，側欄「Career Move」，`session_017u5Po6SGpjD3iLBZ2VL2HH`）的工作是
**讀既有產出 → 萃取成職能與履歷素材**。它對 repo 內其他所有東西是**唯讀**的。

| 動作 | 可以嗎 |
| :--- | :--- |
| Read／Grep／Glob 任何檔案（規格書、`notes/`、`.claude/skills/`、`wiki/`、分析產出、其他分支） | ✅ 不受限制——這些是職能證據的來源 |
| 寫 `career/` 底下的檔案（職能 wiki、portfolio、履歷素材） | ✅ 這是它唯一的主場。**例外：`career/site/` 歸「作品集網站助手」session 寫，Career Move 不動** |
| 改個人線自有 skill：`.claude/skills/resume-craft/`、`resume-review-panel/`、`portfolio-site/` | ✅ **2026-10-08 起由你自己改、自己推**（使用者裁示：這些 skill 跟 1111 主線無關）。commit 前綴 `career(skill):`；推到本分支即可，Repo Steward 會單向同步到 main |
| 改其他 `.claude/skills/`、根目錄 `CLAUDE.md`、`wiki/`、`scripts/`、`.claude_index.md` | ❌ 一律禁止 |
| 改 `notes/`、`handoff/`、`job-classification-kb/` 等任何專案產出 | ❌ 一律禁止 |
| push 到 `claude/happy-lamport-ljis8c` 以外的分支 | ❌ 一律禁止 |
| 在 HackMD 上建立或修改任何 note | ❌ 一律禁止（另見下方硬規則二）|

**需要改以上範圍以外的東西時**（例如發現某份規格書寫錯、想改 `spec-doc-1111`）：
不要自己動手，把需求寫進 **`career/_requests-to-main.md`**（自己開檔即可，格式：一段標題＋想改什麼＋為什麼），
由主幹管理 session（Repo Steward）判斷後統一施作。

**為什麼**：證據來源與證據解讀必須分開。這條分支若同時能改產出又能引用產出當證據，履歷素材就失去可查證性；
實務上也已經發生過越界（刪掉主幹刻意保留的 `hackmd-api` 空殼、改根目錄 `CLAUDE.md`），
造成跟主幹的合併衝突。護欄：`scripts/guard_career_scope.sh`（PreToolUse hook，只在本分支生效，
放行 `career/` 與三個自有 skill，其餘寫入擋下，讀取完全不擋）。
改自有 skill 時：main 不會直接改這三個目錄，所以 merge main 時不會撞；但**不要**順手改其他 skill 或共用檔。

*This session reads the repo's existing output and distils it into competency and résumé material.
Everything outside `career/` and its three owned skills (resume-craft, resume-review-panel, portfolio-site) is **read-only** for it. To change anything outside `career/`, write the request
into `career/_requests-to-main.md` instead of editing — the trunk-managing session decides and applies it.
Enforced by `scripts/guard_career_scope.sh` (PreToolUse hook, this branch only; reads are never blocked).*

## 🤝 協作：作品集網站助手（2026-10-05 起）

同一分支另有 **作品集網站助手** session（`session_01X5B4jtorqQNpioe46ePnFs`），只負責把作品集渲染成靜態網站。完整規則：**`wiki/personal_line_collab.md`**（先讀，需先 merge 最新 main）。重點：

- **你寫內容，它寫 `career/site/`**：目錄不重疊，彼此唯讀。
- **網站只用對外版**：你從內部版 `portfolio/*.md` 產出 `career/portfolio/public/<slug>.md`（front matter `publish: draft|ready`、`highlights`），依 `resume-craft/references/portfolio.md` 去識別化；使用者在你的對話明確核可該頁文字後才設 `ready`。
- **它的問題在 `career/site/QUESTIONS.md`**；你的回覆寫 `career/portfolio/public/STATUS.md`（Q 編號、答覆、日期；另有「使用者決定」表），不要改 QUESTIONS.md。
- 推送前 `git pull --rebase origin claude/happy-lamport-ljis8c`，禁止 force push，commit 前綴 `career:`。
- 雲端 session 之間傳不了訊息：交接完成後在回報最後一行寫「請到作品集網站助手說：請看 `career/portfolio/public/STATUS.md`」，由使用者轉達。

## 🧭 履歷平台路由：104 與 Cake 不要混用

| 任務 | 讀這裡 | 備註 |
| :--- | :--- | :--- |
| 產生、填寫、驗證 **104 履歷** | `104/README.md` →（`104/fields-spec.md` 欄位規格、`104/ui-notes.md` 介面紀錄、`104/resume-104.md` 逐欄內容、`104/chrome-playbook.md` Chrome 操作手冊、`104/resume-104-v6.1.txt` 現行版） | 必填欄位、字數上限、個資與機密規則一律以 `fields-spec.md` 為準 |
| 產生 **Cake Resume** | 尚未建立 `cake/`；要做時先開 `cake/` 目錄、先取得 Cake 編輯頁欄位規格再寫 | **不得套用 104 的欄位規格與字數上限**；內容事實與數字仍共用 `wiki/` |
| 英文 ATS 履歷、自傳、求職信 | `resume-craft` skill、`letters/` | 與平台表單無關 |

事實與數字的來源：先 `library/`（現行事實），細節再查 `wiki/`；各平台檔案只是格式不同的呈現。**中文語氣一律依 `style/resume-voice-zh.md`**（104、Cake 共用，第 3 節護欄優先於語氣）。

## 🚫 硬規則二：不外流 / Hard rule: never publish

**絕不**把 `career/` 的任何內容推送、同步或建立到 HackMD `1111-jobdocs` 團隊工作區（或任何 HackMD note）。
那是公司共用空間，一旦寫入即為不可逆的個人資料外洩。

*Never push, sync, or create `career/` content in the HackMD `1111-jobdocs` team workspace (or any HackMD note) —
it is a shared company space and the leak would be irreversible.*

同理，`career/` 的量化數字若來自 1111 內部資料（工單、客戶名冊、Roadmap），**對外版本必須抽象化**：
可寫「跨系統即時訊息」「1,279 家付費帳號」，但**不外露**內部 API 名、欄位名、權限代碼、廠商編號與名稱。

## 結構 / Structure

| 路徑 | 內容 |
| :--- | :--- |
| `library/` | **使用者提供資料庫**：現行事實、裁定、已推翻說法、待確認問題（衝突時最優先） |
| `HANDOFF.md` | **新 session 開工先讀**：角色邊界、慣例、完整檔案清單、未完成事項 |
| `competency-framework.md` | **wiki 入口**：定位、Profile Snapshot、路由表、F1–F15 總覽 |
| `wiki/` | 職能分頁（`F01`–`F15`）、旗艦專案、履歷摘要、學歷證照、證據頁、PM 語彙對照、缺口盤點 |
| `drafts/` | 履歷工作流程中間產物（職能清單、證據表、essay、去 AI 感、審查），每版一個資料夾 |
| `104/` | 104 履歷工作區；現行版見 `104/README.md` 標示，舊版在 `104/archive/` |
| `style/` | 中文語氣（`resume-voice-zh.md`）、去 AI 感＋ATS（`anti-ai-ats.md`）、PM 履歷最佳實務 |
| `letters/` | 求職信、素材庫（`story-bank.md`）、投遞紀錄 |
| `review-panel/` | `resume-review-panel` skill 的審查者與同儕素材 |
| `portfolio/` | 作品集 case study（內部完整版）；`portfolio/public/` 為對外版與 `STATUS.md` |
| `site/` | **作品集網站助手的暫存區**（網站原始碼、`QUESTIONS.md`），Career Move 唯讀 |
| `career-ops/` | [career-ops](https://github.com/career-ops-hq/career-ops) 求職工具的個人資料層（`cv.md`、`config/profile.yml`）與產出（`reports/`、`output/`、`data/`），經 `CAREER_OPS_ROOT` 直接讀寫；`cv.md` 由 `wiki/` 單向同步 |

**依任務只載入需要的分頁**（入口的路由表會指路），不要整包讀進來。更新職能內容時改對應的 `wiki/` 分頁，
入口只維護索引與快照。

## 工具分工 / Tooling

- 履歷／CV／LinkedIn／作品集／職能盤點 → **`resume-craft`** skill
- 1111 規格書 → **`spec-doc-1111`** skill（**不要**套用到 `career/`，這裡不是規格書：
  沒有 User Story／Use Case 區塊、初始化、權限代碼表、版控表那一套）
- 這兩者與根目錄 `CLAUDE.md`（HackMD API）是三條獨立的線，刻意不混用。

> 做一般 SA／PM 規格產出、打 HackMD API、看 Figma、跑資料分析時，不需要載入 `career/` 或 `resume-craft`——
> 保持日常工作流的 context 乾淨。
