<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

# HackMD API — Folder API

> 回 [`../SKILL.md`](../SKILL.md)。權威來源：`https://api.hackmd.io/v1/docs`。

管理 note 分類用的資料夾 API。資料夾可巢狀（透過 `parentFolderId`）。每組端點都有
**個人工作區**（`/folders`）與**團隊工作區**（`/teams/:teamPath/folders`）兩種形式，行為相同。
資料夾 id 可從 `https://hackmd.io/?nav=overview` 的資料夾網址找到。

> **為什麼重要**：`GET /notes`、`GET /teams/:teamPath/notes` 回傳的 per-note folder 資訊被 API 攤平成
> top-level，**無法**從 notes 端點重建真正的巢狀結構。Folder API 的 `parentFolderId` 才是資料夾樹的
> 權威來源——重建階層（例如產生 `tree.md`）一律走這裡。

## `ApiFolder` 物件

| Field | Type | Notes |
|-------|------|-------|
| `id` | string | 資料夾 ID — 路徑中的 `:folderId` |
| `name` | string | 資料夾名稱 |
| `description` | string/null | |
| `icon` | string/null | |
| `color` | string/null | |
| `parentFolderId` | string/null | 父資料夾 ID；`null` 代表 top-level。**階層的真實來源** |
| `createdAt` | number | Unix epoch ms |
| `updatedAt` | number | Unix epoch ms |

`ApiFolderOrder`：一個物件，把「父資料夾 id（或字面值 `root`）」映射到「子資料夾 id 的有序陣列」。

## 端點

**列出** → `ApiFolder` 陣列：

```
GET /folders
GET /teams/:teamPath/folders
```

**建立**（body 全部可選）：

```
POST /folders
POST /teams/:teamPath/folders
```

```json
{
  "name": "New folder",
  "description": "…",
  "icon": "…",
  "color": "…",
  "parentFolderId": "PARENT_FOLDER_ID"
}
```

省略 `parentFolderId` 會建在工作區根層；給值則巢狀在該父資料夾下。

**單筆讀取** → 一個 `ApiFolder`：

```
GET /folders/:folderId
GET /teams/:teamPath/folders/:folderId
```

**更新**（欄位全部可選；nullable 欄位可傳 `null` 清除）：`name`、`description`、`icon`、`color`、`parentFolderId`。
改 `parentFolderId` 即為「搬移資料夾到新的父層」。

```
PATCH /folders/:folderId
PATCH /teams/:teamPath/folders/:folderId
```

**刪除** → `204`，無 body：

```
DELETE /folders/:folderId
DELETE /teams/:teamPath/folders/:folderId
```

## 資料夾排序 / folder-order

```
GET /folders/folder-order
PUT /folders/folder-order
GET /teams/:teamPath/folders/folder-order
PUT /teams/:teamPath/folders/folder-order
```

`GET` 回傳 `ApiFolderOrder`。`PUT` **整包取代**個人排序——⚠️ 一定要先 `GET` 現有排序、合併後再 `PUT` 回去，
否則會覆蓋掉未列出的部分。排序是**個人設定**，不影響其他團隊成員。

```json
{ "order": { "root": ["folderIdA", "folderIdB"], "folderIdA": ["childId1", "childId2"] } }
```
