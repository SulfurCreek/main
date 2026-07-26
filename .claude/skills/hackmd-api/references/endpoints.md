<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

# HackMD API — Note 與 Team 端點細節

> 回 [`../SKILL.md`](../SKILL.md)。權威來源：`https://api.hackmd.io/v1/docs`。

## Note 物件欄位（回應中）

| Field | Type | Notes |
|-------|------|-------|
| `id` | string | 長 note ID（API 路徑用這個）|
| `shortId` | string | 短 note ID |
| `title` | string | 由 content 推導 |
| `tags` | array/null | Note tags |
| `content` | string | Markdown 內文 — **只在單筆 GET 與建立回應中出現** |
| `createdAt` | number | Unix epoch ms |
| `lastChangedAt` | number | Unix epoch ms |
| `lastChangeUser` | object/null | `{ name, photo, biography, userPath }` |
| `publishType` | string | 例：`view` |
| `publishedAt` | number/null | Unix epoch ms |
| `permalink` | string/null | 自訂 permalink |
| `publishLink` | string | 公開發布網址 |
| `userPath` | string/null | 擁有者 user path |
| `teamPath` | string/null | team note 才有 |
| `readPermission` / `writePermission` | string | 見 SKILL.md 權限段 |

## 使用者與歷史

```
GET /me         回傳目前登入使用者 profile
GET /history    回傳近期讀取過的 note 陣列
```

## Notes

```
GET /notes              列出，無 content
GET /notes/:noteId      單筆，含 content
```

**建立** `POST /notes` → `201` + 建立好的 note 物件。Body 全部可選：

```json
{
  "title": "New note",
  "content": "# Heading",
  "readPermission": "owner",
  "writePermission": "owner",
  "commentPermission": "everyone",
  "permalink": "custom-slug"
}
```

**更新** `PATCH /notes/:noteId` → `202`，body 就是字串 `Accepted`。欄位全部可選：

```json
{
  "content": "# Updated",
  "readPermission": "signed_in",
  "writePermission": "owner",
  "permalink": "new-slug"
}
```

**刪除** `DELETE /notes/:noteId` → `204`，無 body。

## Teams

`GET /teams` 回傳團隊陣列：

| Field | Type | Notes |
|-------|------|-------|
| `id` | string (uuid) | |
| `ownerId` | string (uuid) | |
| `path` | string | **這個才是 `:teamPath`**（不是 `id`）|
| `name` | string | |
| `logo` | string | Data URI |
| `description` | string | |
| `visibility` | string | 例：`public` |
| `createdAt` | string | **ISO 8601**（note 時間戳卻是 epoch ms）|

Team note 端點與個人版行為完全相同，只是多帶 `:teamPath`（本專案為 `1111-jobdocs`），
且建立回應會包含 `teamPath`：

```
GET    /teams/:teamPath/notes            列出（無 content）
POST   /teams/:teamPath/notes            建立 → 201
PATCH  /teams/:teamPath/notes/:noteId    更新 → 202
DELETE /teams/:teamPath/notes/:noteId    刪除 → 204
```

## 把 note 移進資料夾

```
PATCH /teams/:teamPath/notes/:noteId
{"parentFolderId": "<資料夾的內部 UUID>"}
```

⚠️ 必須是**內部 UUID**（來自 note 的 `folderPaths[].id` 或 Folder API 的 `id`），
**不是**資料夾網址上看到的短 `clientId`——傳錯會回 `202` 但靜默不生效。改完務必重抓 note 檢查 `folderPaths`。

## 上傳附件（experimental）

```
POST /notes/:noteId/upload
```

Multipart form 欄位名 `file`。此端點仍為實驗性質，依賴前先對照 live Swagger 確認。
