<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

# career/ — 個人職涯資料 / Personal career material

這裡是**使用者的個人職涯資料**（職能盤點、履歷素材、作品集），與本 repo 的 1111 規格文件工作**刻意分開**。
當成一般 Markdown 文件處理即可。

*The user's personal career material — competency inventory, résumé source, portfolio. Deliberately kept apart
from this repo's 1111 spec-documentation work. Treat as plain Markdown.*

## 🚫 硬規則一：全部可讀，只有 `career/` 可寫 / Read everything, write only `career/`

這條 session（分支 `claude/happy-lamport-ljis8c`，側欄「Career move function definition」）的工作是
**讀既有產出 → 萃取成職能與履歷素材**。它對 repo 內其他所有東西是**唯讀**的。

| 動作 | 可以嗎 |
| :--- | :--- |
| Read／Grep／Glob 任何檔案（規格書、`notes/`、`.claude/skills/`、`wiki/`、分析產出、其他分支） | ✅ 不受限制——這些是職能證據的來源 |
| 寫 `career/` 底下的檔案（職能 wiki、portfolio、履歷素材） | ✅ 這是它唯一的主場 |
| 改 `CLAUDE.md`／`.claude/skills/`（含 `resume-craft`）／`wiki/`／`scripts/`／`.claude_index.md` | ❌ 一律禁止 |
| 改 `notes/`、`handoff/`、`job-classification-kb/` 等任何專案產出 | ❌ 一律禁止 |
| push 到 `claude/happy-lamport-ljis8c` 以外的分支 | ❌ 一律禁止 |
| 在 HackMD 上建立或修改任何 note | ❌ 一律禁止（另見下方硬規則二） |

**需要改 `career/` 以外的東西時**（例如覺得 `resume-craft` skill 該補一段、或發現某份規格書寫錯）：
不要自己動手，把需求寫進 **`career/_requests-to-main.md`**（自己開檔即可，格式：一段標題＋想改什麼＋為什麼），
由主幹管理 session（Repo Steward）判斷後統一施作。

**為什麼**：證據來源與證據解讀必須分開。這條分支若同時能改產出又能引用產出當證據，履歷素材就失去可查證性；
實務上也已經發生過越界（刪掉主幹刻意保留的 `hackmd-api` 空殼、反覆改 `resume-craft` 與 `CLAUDE.md`），
造成跟主幹的合併衝突。護欄：`scripts/guard_career_scope.sh`（PreToolUse hook，只在本分支生效，
擋 `career/` 以外的寫入，讀取完全不擋）。

*This session reads the repo's existing output and distils it into competency and résumé material.
Everything outside `career/` is **read-only** for it. To change anything outside `career/`, write the request
into `career/_requests-to-main.md` instead of editing — the trunk-managing session decides and applies it.
Enforced by `scripts/guard_career_scope.sh` (PreToolUse hook, this branch only; reads are never blocked).*

## 🚫 硬規則二：不外流 / Hard rule: never publish

**絕不**把 `career/` 的任何內容推送、同步或建立到 HackMD `1111-jobdocs` 團隊工作區（或任何 HackMD note）。
那是公司共用空間，一旦寫入即為不可逆的個人資料外洩。

*Never push, sync, or create `career/` content in the HackMD `1111-jobdocs` team workspace (or any HackMD note) —
it is a shared company space and the leak would be irreversible.*

同理，`career/` 的量化數字若來自 1111 內部資料（工單、客戶名冊、Roadmap），**對外版本必須抽象化**：
可寫「跨系統即時訊息」「1,109 家付費帳號」，但**不外露**內部 API 名、欄位名、權限代碼、廠商編號與名稱。

## 結構 / Structure

| 路徑 | 內容 |
| :--- | :--- |
| `competency-framework.md` | **wiki 入口**：定位、Profile Snapshot、路由表、F1–F11 總覽 |
| `wiki/` | 職能分頁（`F01`–`F11`）、旗艦專案、履歷摘要、學歷證照、證據頁、缺口盤點 |
| `portfolio/` | 作品集 case study（完整敘事＋圖表）|

**依任務只載入需要的分頁**（入口的路由表會指路），不要整包讀進來。更新職能內容時改對應的 `wiki/` 分頁，
入口只維護索引與快照。

## 工具分工 / Tooling

- 履歷／CV／LinkedIn／作品集／職能盤點 → **`resume-craft`** skill
- 1111 規格書 → **`spec-doc-1111`** skill（**不要**套用到 `career/`，這裡不是規格書：
  沒有 User Story／Use Case 區塊、初始化、權限代碼表、版控表那一套）
- 這兩者與根目錄 `CLAUDE.md`（HackMD API）是三條獨立的線，刻意不混用。

> 做一般 SA／PM 規格產出、打 HackMD API、看 Figma、跑資料分析時，不需要載入 `career/` 或 `resume-craft`——
> 保持日常工作流的 context 乾淨。
