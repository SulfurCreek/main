# CLAUDE.md

1111 人力銀行**求才／求職系統規格文件**的工作 repo。內容不是應用程式原始碼，而是文件與產出文件的工具：
規格書撰寫慣例（skill）、HackMD `1111-jobdocs` 團隊工作區的文件樹（`tree.md`，307 份），
以及 `career/`（使用者個人職涯資料，與規格工作完全分離）。

## 路由 / Where things live

| 任務 | 用什麼 |
| :--- | :--- |
| 寫／改規格書、需求文件、Use Case | `spec-doc-1111` skill（含求才／求職兩套範本）|
| 打 HackMD API（讀寫 note、資料夾、重建 `tree.md`）| `hackmd-api` skill |
| 履歷／作品集／職能盤點 | `resume-craft` skill ＋ `career/`（見 `career/CLAUDE.md`）|
| 查團隊現有文件位置 | `tree.md` |

團隊工作區：**`1111-jobdocs`**——所有 team 端點的 `:teamPath` 用它。

---

## 陷阱 / Gotchas

踩過才知道、Swagger 上看不出來的東西。動手前先看這段。

### HackMD API

- **`parentFolderId` 要用內部 UUID，不是網址上的短 `clientId`。** 把 note 移進資料夾時
  （`PATCH /teams/:teamPath/notes/:noteId`，body `{"parentFolderId": "<UUID>"}`），傳短 id 或 `folderId`
  會回 **`202` 但靜默不生效**。UUID 來自 note 的 `folderPaths[].id` 或 Folder API 的 `id`。
  改完務必**重抓 note 檢查 `folderPaths`** 確認真的生效。
- **資料夾階層只存在於 Folder API。** notes 列表端點回傳的 folder 資訊被攤平成 top-level，
  無法用來重建巢狀結構——要建資料夾樹一律讀 `GET /teams/:teamPath/folders` 的 `parentFolderId`。
- **`folder-order` 的 `PUT` 是整包覆蓋**，且屬個人設定。先 `GET` 現況、合併、再 `PUT` 回去，否則會清掉沒列到的部分。
- **`content` 只有單筆 GET 和建立回應才有**，列表端點一律沒有——要內文就得逐筆 `GET /notes/:noteId`。
- **權限必須成對給**（`readPermission` ＋ `writePermission`），且 `writePermission` 不得寬於 `readPermission`。
- **`teamPath` 是團隊的 `path` 欄位，不是 `id`。**
- **時間格式不一致**：note 的時間戳是 Unix epoch **毫秒**，team 的 `createdAt` 卻是 **ISO 8601**。
- **Token 只顯示一次**，遺失只能到 Settings → API 撤銷重發。存 `HACKMD_TOKEN` 環境變數，勿寫死。
- 沒有 token 但 note 已公開發布時，`https://hackmd.io/<noteId>/download` 可直接取得 Markdown 原文
  （連 `{%hackmd %}` 嵌入的子文件也能照樣逐份抓）。
- 有疑義時，**live Swagger `https://api.hackmd.io/v1/docs` 為準**。

### 規格書引用語法（HackMD 平台特性）

寫進 note `content` 時可直接使用，API 不會轉義：

- **相對 note 連結**：`[標題](/noteId)`——同一 team workspace 下可直接導航。規格書互連**一律用這種形式**，
  不要用完整 URL。例：`[求才系統代碼表](/B1j3sN-bzx)`。
- **全文嵌入**：`{%hackmd <noteId> %}`——就地嵌入渲染另一份 note。慣例是包在 `:::spoiler {名稱}` 內、
  外層再套 `<div style="padding-left:50px">`，讓讀者展開讀引用文件而不離開本文。
- 其餘撰寫慣例（三層引用、🚧 待補規則區塊、階段拆分、版控表）見 `spec-doc-1111` skill。

### career/ 防火牆

`career/` 是使用者的**個人職涯資料**，與 1111 規格工作刻意分離。**絕不**把 `career/` 的內容推送或建立到
HackMD `1111-jobdocs`（或任何 HackMD note）——那是不可逆的資料外洩。細節見 `career/CLAUDE.md`。
