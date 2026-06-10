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
| POST | `/notes/:noteId/images` | Upload an image to a note |
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
| `folderPaths` | array | Folder ancestor chain `[{ id, name, parentId, ... }]` (root → leaf). Returned by the single-note GET; reflects where `parentFolderId` filed the note |

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
  "permalink": "custom-slug",
  "tags": ["求才系統web"],
  "description": "短描述",
  "parentFolderId": "FOLDER_ID"
}
```
- `parentFolderId` — file the note directly into a folder **at creation** (no separate "move" call needed). Omit to create at workspace root.
- `tags` — array of tag strings.
- `description` — short note description.

Returns `201` with created note object (includes `folderPaths` — the folder ancestor chain).

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
  "permalink": "new-slug",
  "parentFolderId": "FOLDER_ID"
}
```
- `parentFolderId` — **move** the note into a different folder. Same field as create; this is how you re-file an existing note via API.

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

### Upload an image
```
POST /notes/:noteId/images
```
Multipart upload of an image; returns a hosted image URL you can embed in note content as `![image](<returned-url>)`. Useful for adding `## 示意圖` screenshots programmatically. Confirm the exact multipart field name against the live Swagger (`https://api.hackmd.io/v1/docs`) before relying on it.

---

## Folder API

Management API for organising notes into folders. Folders can be nested (a folder may have a `parentFolderId`). Find a folder's id via the folder's URL in `https://hackmd.io/?nav=overview`. Each set of endpoints exists for both the user workspace (`/folders`) and a team workspace (`/teams/:teamPath/folders`); the team variants take `:teamPath` (e.g. `1111-jobdocs`) and otherwise behave identically.

> **Note placement vs. folder tree — two different things:**
> - **To create / move a note into a folder**, set `parentFolderId` in the note's POST or PATCH body (see Create/Update a note). No separate "move" endpoint is needed.
> - **To read a note's folder location**, use the single-note `GET /teams/:teamPath/notes/:noteId`, which returns a `folderPaths` array — the full ancestor chain (e.g. `求才系統 > A. 首頁 > A.1 Topbar`).
> - **Only the *list* endpoints** (`GET /notes`, `GET /teams/:teamPath/notes`) don't guarantee full nesting; the Folder API's `parentFolderId` is the authoritative source when reconstructing the whole tree (e.g. `tree.md`).

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
- **A note's folder is set via `parentFolderId` on note POST/PATCH, and read via `folderPaths` on the single-note GET.** Don't assume notes can't be filed via API — they can, at creation or later. The Folder API (`GET /folders`) remains the authoritative source for reconstructing the *whole* tree, since the note *list* endpoints don't guarantee full nesting.
- **Image upload endpoint is `/notes/:noteId/images`** (not `/upload`). Upload returns a hosted URL to embed as `![image](...)`.
- **`folder-order` is personal and `PUT` replaces it wholesale** — fetch current order first, merge, then put back.
- When in doubt, the **live Swagger docs at `https://api.hackmd.io/v1/docs`** are canonical.
