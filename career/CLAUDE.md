<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

# career/ — 個人職涯資料 / Personal career material

這裡是**使用者的個人職涯資料**（職能盤點、履歷素材、作品集），與本 repo 的 1111 規格文件工作**刻意分開**。
當成一般 Markdown 文件處理即可。

*The user's personal career material — competency inventory, résumé source, portfolio. Deliberately kept apart
from this repo's 1111 spec-documentation work. Treat as plain Markdown.*

## 🚫 硬規則：不外流 / Hard rule: never publish

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
