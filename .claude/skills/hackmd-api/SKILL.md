---
name: hackmd-api
description: >
  呼叫 HackMD API 時使用——讀取／建立／更新／刪除 note、列出 team notes、操作資料夾（folder）與資料夾排序、
  重建文件樹（如 `tree.md`）、把規格書同步到 HackMD `1111-jobdocs` 團隊工作區。
  只要任務涉及「打 HackMD API」「抓 note 內容」「建立／更新 note」「列出團隊文件」「folder / parentFolderId /
  folder-order」「重建 tree.md」「HACKMD_TOKEN」，就載入本 skill 取得端點與欄位細節。
  本 skill 只管 API 呼叫；規格書「怎麼寫」屬 `spec-doc-1111`，個人職涯資料屬 `resume-craft`。
---

<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

# hackmd-api — HackMD API 呼叫指南

本專案團隊工作區：**`1111-jobdocs`**（`https://hackmd.io/team/1111-jobdocs?nav=overview`）——所有 team 端點的 `:teamPath` 都用它。

> 陷阱（gotchas）寫在 repo 根目錄 `CLAUDE.md`，動手前先看那份。
> 權威來源是 live Swagger：`https://api.hackmd.io/v1/docs`——本檔與它衝突時以 Swagger 為準。

## 認證 / Auth

```
Base URL:  https://api.hackmd.io/v1
Header:    Authorization: Bearer $HACKMD_TOKEN
```

Token 於 **HackMD → Settings → API → Create API token** 建立，**只顯示一次**。存成環境變數（`HACKMD_TOKEN`），
勿寫死在程式碼；`.env` 要進 `.gitignore`；GitHub Actions 存成 repo secret。成功回應都帶 `X-HackMD-API-Version: 1.0.0`。

驗證 token 是否有效：

```bash
curl "https://api.hackmd.io/v1/me" -H "Authorization: Bearer $HACKMD_TOKEN"
```

## 端點總表 / Endpoint summary

| Method | Path | 用途 |
|--------|------|------|
| GET | `/me` | 目前登入使用者 |
| GET | `/notes` ・ `/teams/:teamPath/notes` | 列出 note（**不含 `content`**）|
| GET | `/notes/:noteId` | 取單筆 note（**含 `content`**）|
| POST | `/notes` ・ `/teams/:teamPath/notes` | 建立 note（`201`，回傳含 `content`）|
| PATCH | `/notes/:noteId` ・ `/teams/:teamPath/notes/:noteId` | 更新 note（`202`，body 為 `Accepted`）|
| DELETE | `/notes/:noteId` ・ `/teams/:teamPath/notes/:noteId` | 刪除 note（`204`）|
| GET | `/history` | 近期讀取紀錄 |
| GET | `/teams` | 可存取的團隊（`path` 欄位才是 `:teamPath`）|
| POST | `/notes/:noteId/upload` | 上傳附件（experimental，用前先對 Swagger）|
| GET·POST | `/folders` ・ `/teams/:teamPath/folders` | 列出／建立資料夾 |
| GET·PATCH·DELETE | `/folders/:folderId` ・ `/teams/:teamPath/folders/:folderId` | 單一資料夾讀／改／刪 |
| GET·PUT | `/folders/folder-order` ・ `/teams/:teamPath/folders/folder-order` | 個人資料夾排序（PUT **整包覆蓋**）|

狀態碼：`200` OK ｜ `201` 建立 ｜ `202` 已接受（PATCH）｜ `204` 無內容（DELETE）｜
`401` token 無效 ｜ `403` 權限不足 ｜ `404` 找不到 ｜ `429` 觸發限流。

## 關鍵欄位語意 / Field semantics

**權限**：`readPermission`／`writePermission` 取值 `owner`｜`signed_in`｜`guest`；
`commentPermission` 取值 `disabled`｜`forbidden`｜`owners`｜`signed_in_users`｜`everyone`。
設定時**兩個 permission 必須成對給**，且 `writePermission` 不得寬於 `readPermission`（嚴格度 `owner` > `signed_in` > `guest`）。

**標題**推導優先序：content 的 H1 → YAML front matter 的 `title` → request 的 `title` 欄位 → `Untitled`。

**時間格式不一致**：note 的 `createdAt`／`lastChangedAt`／`publishedAt` 是 **Unix epoch 毫秒**；
team 的 `createdAt` 是 **ISO 8601**。

**資料夾層級**只存在於 Folder API 的 `parentFolderId`（`null` 表示 top-level）——
notes 端點回傳的 folder 資訊是扁平的，**無法**用來重建巢狀結構。

## 詳細參考 / Detailed references

需要完整欄位表、request/response 範例時再讀：

- [`references/endpoints.md`](references/endpoints.md) — 每支 note／team 端點的 body、回傳、完整欄位對照表
- [`references/folders.md`](references/folders.md) — Folder API 全貌、`ApiFolder`／`ApiFolderOrder` 結構、重建資料夾樹的做法
- [`references/snippets.md`](references/snippets.md) — Node.js／Python／cURL 可直接套用的呼叫樣板
