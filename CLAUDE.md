# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

# HackMD API Reference

Complete reference for authenticating and calling every HackMD API endpoint. Live interactive spec: `https://api.hackmd.io/v1/docs`.

## Base URL

```
https://api.hackmd.io/v1
```

## Authentication

Bearer token in every request:

```
Authorization: Bearer <token>
```

Token is created in **HackMD → Settings → API → Create API token** and shown only once — copy it immediately. Store it as an environment variable, never hard-coded:

```
HACKMD_TOKEN=<your token>
```

Read via `process.env.HACKMD_TOKEN` (Node) or `os.environ["HACKMD_TOKEN"]` (Python). Keep `.env` in `.gitignore`. For GitHub Actions, store as repo secret `HACKMD_TOKEN`.

Quick auth test:
```bash
curl "https://api.hackmd.io/v1/me" -H "Authorization: Bearer $HACKMD_TOKEN"
```

Every successful response includes `X-HackMD-API-Version: 1.0.0`.

## This Project's Team

Team path: `1111-jobdocs`  
Team URL: `https://hackmd.io/team/1111-jobdocs?nav=overview`

Use `1111-jobdocs` as `:teamPath` in all team note endpoints.

---

## Endpoint Summary

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/me` | Get current authenticated user |
| GET | `/notes` | List notes in the user's workspace |
| GET | `/notes/:noteId` | Get a single note (incl. content) |
| POST | `/notes` | Create a note in the user's workspace |
| PATCH | `/notes/:noteId` | Update a note |
| DELETE | `/notes/:noteId` | Delete a note |
| GET | `/history` | Get history of read notes |
| GET | `/teams` | List teams the user can access |
| GET | `/teams/:teamPath/notes` | List notes in a team workspace |
| POST | `/teams/:teamPath/notes` | Create a note in a team workspace |
| PATCH | `/teams/:teamPath/notes/:noteId` | Update a team note |
| DELETE | `/teams/:teamPath/notes/:noteId` | Delete a team note |
| POST | `/notes/:noteId/upload` | Upload attachment (experimental) |
| GET | `/folders` | List folders in the user's workspace |
| POST | `/folders` | Create a folder in the user's workspace |
| GET | `/folders/folder-order` | Get personal folder ordering (user workspace) |
| PUT | `/folders/folder-order` | Replace personal folder ordering (user workspace) |
| GET | `/folders/:folderId` | Get a single user folder |
| PATCH | `/folders/:folderId` | Update a user folder |
| DELETE | `/folders/:folderId` | Delete a user folder |
| GET | `/teams/:teamPath/folders` | List folders in a team workspace |
| POST | `/teams/:teamPath/folders` | Create a folder in a team workspace |
| GET | `/teams/:teamPath/folders/folder-order` | Get personal folder ordering (team workspace) |
| PUT | `/teams/:teamPath/folders/folder-order` | Replace personal folder ordering (team workspace) |
| GET | `/teams/:teamPath/folders/:folderId` | Get a single team folder |
| PATCH | `/teams/:teamPath/folders/:folderId` | Update a team folder |
| DELETE | `/teams/:teamPath/folders/:folderId` | Delete a team folder |

---

## Field Reference

### Permissions

| Field | Type | Allowed values |
|-------|------|----------------|
| `readPermission` | string | `owner`, `signed_in`, `guest` |
| `writePermission` | string | `owner`, `signed_in`, `guest` |
| `commentPermission` | string | `disabled`, `forbidden`, `owners`, `signed_in_users`, `everyone` |

**Rules:**
- Both `readPermission` and `writePermission` must be provided together when setting permissions.
- `writePermission` must be at least as strict as `readPermission`. Strictness order: `owner` > `signed_in` > `guest`.

### Title derivation (priority order)

1. H1 heading in `content` (`# Heading`)
2. `title` in YAML front matter
3. `title` request field
4. `Untitled`

### Note object fields (in responses)

| Field | Type | Notes |
|-------|------|-------|
| `id` | string | Long note ID (used in API paths) |
| `shortId` | string | Short note ID |
| `title` | string | Derived from content |
| `tags` | array/null | Note tags |
| `content` | string | Markdown body — **only in single-note GET and create response** |
| `createdAt` | number | Unix epoch ms |
| `lastChangedAt` | number | Unix epoch ms |
| `lastChangeUser` | object/null | `{ name, photo, biography, userPath }` |
| `publishType` | string | e.g. `view` |
| `publishedAt` | number/null | Unix epoch ms |
| `permalink` | string/null | Custom permalink |
| `publishLink` | string | Public publish URL |
| `userPath` | string/null | Owner user path |
| `teamPath` | string/null | Team path if a team note |
| `readPermission` | string | See above |
| `writePermission` | string | See above |

### Folder object fields (in responses)

`ApiFolder` (returned by folder list / get endpoints):

| Field | Type | Notes |
|-------|------|-------|
| `id` | string | Folder ID — used as `:folderId` in paths |
| `name` | string | Folder name |
| `description` | string/null | |
| `icon` | string/null | |
| `color` | string/null | |
| `parentFolderId` | string/null | Parent folder ID, or `null` if top-level. **This is the real hierarchy source** — the notes list endpoints do **not** expose folder nesting |
| `createdAt` | number | Unix epoch ms |
| `updatedAt` | number | Unix epoch ms |

`ApiFolderOrder`: an object mapping a parent folder id (or the literal `root`) → ordered array of child folder ids. Used by the `folder-order` endpoints.

---

## Endpoints — Full Detail

### Get current user
```
GET /me
```
Returns authenticated user's profile.

### List user notes
```
GET /notes
```
Returns array of note objects. No `content` field — call `GET /notes/:noteId` to fetch body.

### Get a note
```
GET /notes/:noteId
```
Returns single note object **including** `content`.

### Create a note
```
POST /notes
```
Body (all optional):
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
Returns `201` with created note object.

### Update a note
```
PATCH /notes/:noteId
```
Body (all optional):
```json
{
  "content": "# Updated",
  "readPermission": "signed_in",
  "writePermission": "owner",
  "permalink": "new-slug"
}
```
Returns `202` with body `Accepted`.

### Delete a note
```
DELETE /notes/:noteId
```
Returns `204` (no body).

### Get read history
```
GET /history
```
Returns array of recently read note objects.

### List teams
```
GET /teams
```
Returns array of team objects:

| Field | Type | Notes |
|-------|------|-------|
| `id` | string (uuid) | |
| `ownerId` | string (uuid) | |
| `path` | string | Use as `:teamPath` in team endpoints |
| `name` | string | |
| `logo` | string | Data URI |
| `description` | string | |
| `visibility` | string | e.g. `public` |
| `createdAt` | string | ISO 8601 (unlike note timestamps which are epoch ms) |

### List team notes
```
GET /teams/:teamPath/notes
```
Returns array of note objects (no `content`).

### Create a team note
```
POST /teams/:teamPath/notes
```
Same body as Create a note. Returns `201` with created note (includes `teamPath`).

### Update a team note
```
PATCH /teams/:teamPath/notes/:noteId
```
Same body as Update a note. Returns `202`.

### Delete a team note
```
DELETE /teams/:teamPath/notes/:noteId
```
Returns `204`.

### Upload attachment (experimental)
```
POST /notes/:noteId/upload
```
Multipart form field: `file`. Verify against live Swagger docs before relying on this endpoint.

---

## Folder API

Management API for organising notes into folders. Folders can be nested (a folder may have a `parentFolderId`). Find a folder's id via the folder's URL in `https://hackmd.io/?nav=overview`. Each set of endpoints exists for both the user workspace (`/folders`) and a team workspace (`/teams/:teamPath/folders`); the team variants take `:teamPath` (e.g. `1111-jobdocs`) and otherwise behave identically.

> **Why this matters here:** the notes list endpoints (`GET /notes`, `GET /teams/:teamPath/notes`) return a per-note `folderPaths`/parent that the API reports flat (top-level), so true nesting can't be reconstructed from notes alone. The Folder API's `parentFolderId` is the authoritative source for the folder tree — use it when building a hierarchy (e.g. `tree.md`).

### List folders
```
GET /folders
GET /teams/:teamPath/folders
```
Returns an array of `ApiFolder` objects.

### Create a folder
```
POST /folders
POST /teams/:teamPath/folders
```
Body (all optional):
```json
{
  "name": "New folder",
  "description": "…",
  "icon": "…",
  "color": "…",
  "parentFolderId": "PARENT_FOLDER_ID"
}
```
Omit `parentFolderId` (or pass top-level) to create at workspace root; set it to nest inside another folder.

### Get a single folder
```
GET /folders/:folderId
GET /teams/:teamPath/folders/:folderId
```
Returns one `ApiFolder` object.

### Update a folder
```
PATCH /folders/:folderId
PATCH /teams/:teamPath/folders/:folderId
```
Body (all optional; nullable fields can be set to `null` to clear): `name`, `description`, `icon`, `color`, `parentFolderId`. Set `parentFolderId` to move the folder under a new parent.

### Delete a folder
```
DELETE /folders/:folderId
DELETE /teams/:teamPath/folders/:folderId
```
Returns `204` (no body).

### Get / set folder ordering
```
GET /folders/folder-order
PUT /folders/folder-order
GET /teams/:teamPath/folders/folder-order
PUT /teams/:teamPath/folders/folder-order
```
`GET` returns an `ApiFolderOrder` (parent folder id or `root` → ordered array of child folder ids). `PUT` **replaces** the personal ordering; body:
```json
{ "order": { "root": ["folderIdA", "folderIdB"], "folderIdA": ["childId1", "childId2"] } }
```

---

## Code Snippets

### Node.js (fetch)

```javascript
const BASE = "https://api.hackmd.io/v1";
const TOKEN = process.env.HACKMD_TOKEN;

async function hackmd(path, options = {}) {
  const res = await fetch(`${BASE}${path}`, {
    ...options,
    headers: {
      Authorization: `Bearer ${TOKEN}`,
      "Content-Type": "application/json",
      ...(options.headers || {}),
    },
  });
  if (!res.ok) throw new Error(`${res.status} ${await res.text()}`);
  return res.status === 204 ? null : res.json();
}

// Usage
await hackmd("/me");
await hackmd("/notes");
await hackmd("/notes/NOTE_ID");
await hackmd("/teams/1111-jobdocs/notes");
await hackmd("/notes", { method: "POST", body: JSON.stringify({ content: "# Hello" }) });
await hackmd("/notes/NOTE_ID", {
  method: "PATCH",
  body: JSON.stringify({ content: "# Updated", readPermission: "owner", writePermission: "owner" }),
});
await hackmd("/notes/NOTE_ID", { method: "DELETE" });
// Folders
await hackmd("/teams/1111-jobdocs/folders");
await hackmd("/teams/1111-jobdocs/folders", { method: "POST", body: JSON.stringify({ name: "規格文件", parentFolderId: "PARENT_ID" }) });
await hackmd("/teams/1111-jobdocs/folders/FOLDER_ID", { method: "PATCH", body: JSON.stringify({ parentFolderId: "NEW_PARENT_ID" }) });
```

### Python (requests)

```python
import os, requests

BASE = "https://api.hackmd.io/v1"
HEADERS = {"Authorization": f"Bearer {os.environ['HACKMD_TOKEN']}"}

def get(path): r = requests.get(BASE + path, headers=HEADERS); r.raise_for_status(); return r.json()
def post(path, data): r = requests.post(BASE + path, headers=HEADERS, json=data); r.raise_for_status(); return r.json()
def patch(path, data): r = requests.patch(BASE + path, headers=HEADERS, json=data); r.raise_for_status(); return r.status_code
def delete(path): r = requests.delete(BASE + path, headers=HEADERS); r.raise_for_status(); return r.status_code

# Usage
get("/me")
get("/notes")
get("/notes/NOTE_ID")
get("/teams/1111-jobdocs/notes")
post("/notes", {"content": "# Hello"})
patch("/notes/NOTE_ID", {"content": "# Updated", "readPermission": "owner", "writePermission": "owner"})
delete("/notes/NOTE_ID")
# Folders
get("/teams/1111-jobdocs/folders")
post("/teams/1111-jobdocs/folders", {"name": "規格文件", "parentFolderId": "PARENT_ID"})
patch("/teams/1111-jobdocs/folders/FOLDER_ID", {"parentFolderId": "NEW_PARENT_ID"})
```

### cURL

```bash
# List team notes
curl "https://api.hackmd.io/v1/teams/1111-jobdocs/notes" \
  -H "Authorization: Bearer $HACKMD_TOKEN"

# Create a team note
curl -X POST "https://api.hackmd.io/v1/teams/1111-jobdocs/notes" \
  -H "Authorization: Bearer $HACKMD_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"content":"# Hello from API"}'

# List team folders (real hierarchy via parentFolderId)
curl "https://api.hackmd.io/v1/teams/1111-jobdocs/folders" \
  -H "Authorization: Bearer $HACKMD_TOKEN"
```

---

## Status Codes

| Code | Meaning |
|------|---------|
| `200` | OK (GET success) |
| `201` | Created (POST success; returns the note) |
| `202` | Accepted (PATCH success; body literally `Accepted`) |
| `204` | No Content (DELETE success; empty body) |
| `401` | Bad/missing token |
| `403` | Token lacks permission for resource |
| `404` | Note/team not found |
| `429` | Rate limited |

---

## Gotchas

- **Token shown once.** Lost token = revoke + reissue via Settings → API.
- **`content` only returned by single-note GET and create**, not list endpoints.
- **Permissions come in pairs** — always provide both `readPermission` and `writePermission` together.
- **`writePermission` must be at least as strict as `readPermission`.**
- **`teamPath`** is the team's `path` field, not its `id`.
- **Team `createdAt` is ISO 8601**; note timestamps (`createdAt`, `lastChangedAt`, `publishedAt`) are Unix epoch milliseconds.
- **Folder hierarchy lives in the Folder API, not the notes endpoints.** To reconstruct a folder tree, read `parentFolderId` from `GET /folders` or `GET /teams/:teamPath/folders` — the notes list does not expose nesting.
- **`folder-order` is personal and `PUT` replaces it wholesale** — fetch current order first, merge, then put back.
- When in doubt, the **live Swagger docs at `https://api.hackmd.io/v1/docs`** are canonical.

---

# 規格書 UI 截圖標號慣例（求才系統）

來源：分析求才系統格式最完整的規格書 **[4.1 信件訊息對話規格文件](https://hackmd.io/@1111-jobdocs/r1ghrPxP-x)**（次選 [2.0 職缺內頁＞職缺內容](https://hackmd.io/@1111-jobdocs/BJ7Yob8W-g)）。新規格書（含 `E.1 聯繫人才`）的截圖標號與章節編號**一律依此慣例**。

## 核心原則：截圖標號 == 章節編號（1:1 對應）

截圖上標示的每個編號，**必對應一個同號的 Markdown heading**；反之每個編號 heading 應能在截圖上找到對應標號。標號是「畫面區塊 ↔ 規格章節」的唯一橋樑，RD/QA 靠它對照畫面與文字。

## 編號階層與章節對應

| 編號 | 標的 | Markdown | 截圖呈現 |
| :--- | :--- | :--- | :--- |
| `N`（整數） | 一個主要 UI 區塊（畫面分區） | `## N {區塊名}`（如 `## 2 對話區塊`） | 區塊**總覽截圖**緊接在 `## N` heading 下方；該截圖左上緣放一個**大號**標號 `N` |
| `N.M` | 區塊內的元件／子區域 | `### N.M {元件名}`（如 `### 2.4 廠商訊息`） | 在同一張區塊總覽截圖上，於該元件左上角放**小號**標號 `N.M` |
| `N.M.K` | 元件內的細項 | `#### N.M.K {細項名}`（如 `#### 2.4.1 信件類型`） | 視需要在更細的截圖或同張圖上標 `N.M.K` |

* 每個 `## N` 區塊**自帶一張總覽截圖**（區塊內所有 `N.M` 標號集中標在這張圖上），緊接在 heading 之後。
* 編號**連續**且**對應畫面標號**；`初始化` 不編號、固定放最前（見 spec-doc-1111 skill）。
* 特殊變體用小寫字母後綴（如 `#### 2.2a 勾選兼職`、`2.2b`），對應同一元件的不同情境。

## 標號徽章樣式（畫在截圖上）

* **顏色**：紅／珊瑚紅底 `#FF5F57`、**白色粗體**數字。
* **字型**：`Inter`、`font-weight:700`、`font-size:20px`、`line-height:24px`、置中、白色 `#FFFFFF`。
* **形狀／尺寸**：圓角矩形 `border-radius:10px`、`padding:4px 10px`（單字元徽章約 `34×33px`）；整數區塊號 `N` 用較大、近正圓的徽章，子號 `N.M` 用較小的圓角矩形。
* **位置**：
  * 區塊號 `N`：放在該區塊總覽截圖的**左上緣／左外側**。
  * 子號 `N.M`：放在所對應元件的**左上角**，緊貼元件。
* **閱讀順序**：由上而下、由左至右，編號隨之遞增。

## 套用步驟（從 Figma 畫面產生標號截圖）

1. 從 Figma 對應 node 抓取目標區塊的乾淨截圖（design token / 畫面切圖）。
2. 依「由上而下、由左至右」決定區塊與元件的編號。
3. 在截圖上以上述徽章樣式（紅底白字圓角）標上 `N` / `N.M`。
4. 規格文件以**編號為單位**建立／更新對應的 `## N` / `### N.M` 章節，使截圖標號與 heading 完全同步。
5. 圖片寬度沿用既有慣例（手機版 `375px`、區塊總覽 `500`～`800px`）。

## 以 Pillow 在截圖上標注／覆蓋文字

設計稿與規格有落差時，可在 Figma 截圖上疊加標號、覆蓋改字、標注落差（不要求設計稿與規格一致，目的是示意）。完整步驟見 `spec-doc-1111` skill「截圖標注／覆蓋」一節，重點：

* **抓圖**：`mcp__Figma__get_screenshot`（`nodeId`＋`fileKey`，回傳短效 URL→`curl` 下載）；定位座標再用 `get_design_context`。
* **改字**：先畫白底矩形蓋舊內容，再 `ImageDraw.text` 重寫；中文字型用 `/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc`（無 Noto TC 時後備）。
* **標號徽章**：紅底白字圓角，底色 `#FF5F57`、`border-radius:10px`、`padding:4px 10px`、字型 `Inter` 700 / `20px` / `line-height:24px`，`N` / `N.M` 依慣例放置。
* **落差標注**：黃框（`(255,200,0)`）圈出差異處，旁注「規格：XX／現況：OO」。
* **入庫**：HackMD `upload` 端點不可用→圖 commit 到 `.claude/assets/`、push 後用 `raw.githubusercontent.com/sulfurcreek/main/{commit}/.claude/assets/{file}.png` 引用。
* **限制**：只能蓋白重寫，無法智慧抹除；要乾淨換字改用 Figma MCP 編輯設計稿文字節點再重截。

---

# 版控表慣例（所有規格書共通）

每份規格書 `## 版控紀錄` 表格的版本列**一律時間升冪排列**：最舊的版本在最上面、**最新版永遠 append 在表格最末列**。

* 每次發布只在表格**最下方**新增一列，**不可插在中間、也不可倒序**（最新版放最上面是錯的）。
* 調整說明格式：`[異動區段] 內容摘要`；版號採 `主.次.修` 三段。
* 此規則與 `spec-doc-1111` skill 一致；用 HackMD API PATCH 既有文件時，若發現舊列亂序，順手重排為升冪。

---

# 規格書格式偏好（依作者人工調整 E.1 歸納，所有規格書共通）

來源：比對 E.1 v0.7.0 機器版與作者手動調整版（2026/06/10）。撰寫／修改規格書時一律套用：

1. **User Story / Use Case 整句包反引號**：`` User Story: `身為…` ``。
2. **未知資訊直接寫 `TBD`／`待補`**：功能位置沒有確定 URL 就寫 `TBD`，不要放推測網址再加待補註解；`## 示意圖` 沒有合適整頁圖就只寫 `待補`，不要拿入口圖或局部截圖充數。
3. **同一個待補只標一次**：表格儲存格已寫 `待補`，不得在表格下方再加紅字段落重述。
4. **跨文件連結文字＝文件名稱**，不加 `[REF]` 前綴。
5. **進入路徑直接條列各入口**（不加「路徑 A／B／C」標籤），入口截圖緊貼該 bullet 下方。
6. **現版 iframe lightbox 集中為單一章**（如 `### 3 現版Lightbox`），各 lightbox 為 `#### 3-1`、`#### 3-2`… dash 編號子節，子節之間不加 `---`（`---` 只放在大章之間）。
7. **階段拆分文件的大架構順序**：`## 初始化` → `## 第一階段內容` → `## 第二階段內容` → `## 跨系統流程與後端邏輯`（跨系統章為獨立 H2、不屬於任何階段，子節 H3 點號編號如 `### 6.1`）。延後實作的功能整節（含截圖）搬到第二階段，並以 `> 來源：原 §x.x` 註明出處。

---

# 求才系統帳號權限模型（帳號權限 ≠ 廠商權限）

來源：帳號權限 Google Sheet（2026/06/10 擷取）。完整代碼定義一律以 HackMD [求才系統權限代碼表](https://hackmd.io/@1111-jobdocs/B1j3sN-bzx) 為準；規格書凡提及帳號權限，務必附上該文件連結，代碼名稱以表中「新版 Label」為準。

* **帳號權限 ≠ 廠商權限，絕對不可混淆**：
  * **帳號權限**＝登入帳號層級的整數權限代碼。每個廠商名下有一個**主帳號**（權限最大、全開放、不可被限制）與多個**副帳號**（權限可於帳號設定逐項勾選）。
  * **廠商權限／狀態**＝公司層級欄位（`oStatus`、`organs.confirmed`、`organs.showfield`、`organsMore`），與帳號無關。規格書權限判斷表中兩者分開列。
* 權限代碼對應求才系統各功能的 **C/R/U/D** 操作；R 型代碼控制帳號可讀取的資料範圍（哪些職缺、聯絡人、範本、簡訊、人才庫、帳號）。
* 組合寫法 `主代碼+範圍代碼`（主代碼單獨不提供勾選）：帳號 `7+22`（自己）/`7+23`（全部）、聯絡人 `8+24`/`8+25`、職缺 `10+26`/`10+27`、範本 `14+28`/`14+29`、人才庫 `16+30`/`16+31`、簡訊 `43+32`/`43+33`。注意 `10`（管理職缺）無值時帳號**可看到全部職缺**。
* 常用獨立代碼：`6` 編輯公司資料、`9` 暫停/開啟公司刊登、`65` 群組管理、`53` 新增/修改職缺、`50` 刪除職缺、`54` 開關職缺、`12` 職缺排序、`41` 職缺同步、`44` 職缺移轉、`51` 管理履歷與人才搜尋（E.1 即時通訊／E.2 邀約名單入口）、`52` 刪除備註、`13` 封鎖求職者、`49` 人才庫可取消儲存、`15` 面試行事曆、`45` 刪除範本、`38` 修改密碼、`66` 修改通知設定、`48` 刪除聯絡人、`19` 徵才報表、`55` 帳號邀約紀錄、`46` 線上續約、`21` 購買廣告、`47` 職缺廣告、`20` 紅利兌換。
* 無代碼時共通行為：不顯示功能入口；URL 直進顯示不可修改 Alert、點擊後返回上一頁；內網（客服後台）仍可見入口但進入亦顯示 Alert。
* `56`–`64` 為部門權限預留代碼（pending）；`36`/`37` 為停用舊代碼；大類代碼 `1`–`5` 與 `42`（帳號維護）新版不提供勾選（`42`：不勾選也可看到並修改自己帳號）。
* 用字統一為「權限」（禁用異體「権限」）。
