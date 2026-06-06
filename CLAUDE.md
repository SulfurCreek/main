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
- When in doubt, the **live Swagger docs at `https://api.hackmd.io/v1/docs`** are canonical.
