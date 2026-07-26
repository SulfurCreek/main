<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

# HackMD API — 呼叫樣板

> 回 [`../SKILL.md`](../SKILL.md)。團隊路徑：`1111-jobdocs`。

## Node.js (fetch)

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

## Python (requests)

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

## cURL

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

## 無 token 時的替代讀法

沒有 `HACKMD_TOKEN`、但 note 是公開發布時，可直接抓 Markdown 原文：

```bash
curl -sL "https://hackmd.io/<noteId>/download"
```

這條路徑也能取得 note 內嵌的 `{%hackmd <id> %}` 子文件——把子文件 id 再抓一次即可。
