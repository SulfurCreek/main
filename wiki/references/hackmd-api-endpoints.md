# HackMD API — 端點完整規格與程式碼範例

> 屬 `wiki/hackmd_rules.md` 的參考檔。**需要查特定端點的 request/response 細節、Folder API、或要現寫 Node/Python/cURL 呼叫時才讀**。
> 日常「讀取既有 note → 本地編輯 → 回寫」不需要本檔——走 `scripts/hackmd_safe_patch.py` 即可（見 `wiki/hackmd_rules.md` 規則 A–D）。
> 端點一覽（method + path + 用途）已在 `wiki/hackmd_rules.md` 的 Endpoint Summary 表，本檔只放展開細節。

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

### 無 token 時的替代讀法

沒有 `HACKMD_TOKEN`（或想避免消耗 rate limit）時，可直接用內部 note id 抓 Markdown 原文，**不需要 Authorization header**（已對本專案 team note 實測 200）：

```bash
curl -sL "https://hackmd.io/<noteId>/download"
```

這條路徑也能取得 note 內嵌的 `{%hackmd <id> %}` 子文件——把子文件 id 再抓一次即可。仍是唯讀捷徑，**改寫一律走正規 `PATCH` API＋`scripts/hackmd_safe_patch.py`**，不要用這個端點做寫入判斷的依據。

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
