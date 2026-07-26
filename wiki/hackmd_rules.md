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

## 🚀 Token 節省與本地快取規範（Local Caching Policy）

撈取既有 HackMD note 內容做後續編輯（尤其是規格書這種數千字的長文）時，**禁止把整份 Response 直接印進對話/終端輸出**，否則每一輪修改都會把全文重新攤進 context，token 線性膨脹。改用「落地快取 → 本地編輯 → 一次性回寫」流程：

* **規則 A — 落地快取，不印全文**：呼叫 `GET /notes/:noteId`／`GET /teams/:teamPath/notes/:noteId` 時，把 `content` 寫進本次 session 的**暫存目錄**（即系統指定的 scratchpad 路徑，不是 repo 工作目錄），不要讓整份內容出現在工具回傳的可見輸出裡。
  * 範例（Python，搭配既有的 `os.environ['HACKMD_TOKEN']` 慣例）：
    ```python
    import os, requests, json
    r = requests.get(f"{BASE}/notes/{note_id}", headers=HEADERS)
    with open(f"{SCRATCHPAD}/{note_id}.md", "w") as f:
        f.write(r.json()["content"])
    ```
  * 絕對不要寫到 repo 路徑（如 `tmp/`）下 —— 該路徑未列入 `.gitignore`，有被誤 commit 的風險。一律用 scratchpad 暫存目錄，工作結束後可捨棄。
* **規則 B — 在本地檔案上迭代，不在對話裡整篇覆寫**：對落地的快取檔案用 `Read`／`Edit` 工具做局部修改（精準字串替換、可控的小範圍 diff），不要在回覆裡貼出整份重寫後的 Markdown。
* **規則 C — 確認無誤後才一次性回寫**：所有修改（章節調整、Mermaid 圖、欄位表）都在本地快取檔案改完，並經使用者確認後，才執行一次 `PATCH /teams/:teamPath/notes/:noteId`（或 `PATCH /notes/:noteId`）把本地檔案內容整份送回 HackMD —— 避免多次小步 PATCH，也避免漏改。

> 新建（`POST`）或只改幾行的小幅修補不必硬套這套流程；本規範主要針對「讀取既有長文 → 大幅編輯 → 寫回」這種會讓全文重複出現在 context 裡的情境。

* **規則 D — 安全回寫契約（防覆蓋 / anti-clobber）**：規則 A 落地 baseline 到規則 C 一次性 PATCH 之間，遠端可能已被別人（如小聶手改）改動；直接 `PATCH` 會把對方的編輯**盲蓋掉**。回寫前務必先「重抓 → 比對 → 才寫」：
  1. **baseline**：規則 A 落地當下那份就是 baseline，別動它。
  2. **recheck**：PATCH 前再 `GET` 一次遠端 `content`。
  3. **diff**：`diff(baseline, recheck)`——
     * **無差異** → 遠端沒被動過，安全 `PATCH` working 內容。
     * **有差異** → 遠端在你編輯期間被改過，**中止、不要 PATCH**；重新 fetch 最新內容、把本地修改重套上去後再跑一次。
  4. 用現成腳本一次做完 recheck+diff+PATCH（衝突時 exit 1、不寫入）：
     ```bash
     python3 scripts/hackmd_safe_patch.py \
       --note-id <內部 noteId> \
       --baseline "$SCRATCHPAD/<noteId>.md" \
       --working  "$SCRATCHPAD/<noteId>.working.md" \
       --team-path 1111-jobdocs
     ```
     Exit code：`0` 已更新／`1` 衝突（遠端已變，未寫入）／`2` 參數或 API 錯誤。這正是本 repo 每次改 E.1／uS9 前「重抓確認小聶有沒有手動編輯」那步的自動化版本。
  > 移植自官方 `hackmd-skills/shared/scripts/safe-sync.sh`（原版用 `hackmd-cli`），改用本 repo 的 REST API＋`HACKMD_TOKEN` 慣例。

### short id／team URL → 內部 note id

`PATCH`／`export`／API 路徑一律要**內部長 id**（如 `uS9yE837SYedY9hQFneb6Q`），不是網址上的 short slug。拿到 `https://hackmd.io/@1111-jobdocs/<shortId>` 這種 team 短連結時，用 team notes 清單反查：

```bash
curl -s "https://api.hackmd.io/v1/teams/1111-jobdocs/notes" \
  -H "Authorization: Bearer $HACKMD_TOKEN" \
  | jq -r --arg s "<shortId>" '[.[] | select(.shortId==$s or .id==$s)][0].id'
```

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

## Endpoints 完整規格／Folder API／程式碼範例

各端點的 request body、response 欄位、Folder API 全套操作，以及 Node.js／Python／cURL 範例——**需要時才讀** → `wiki/references/hackmd-api-endpoints.md`

> 日常回寫走 `scripts/hackmd_safe_patch.py`（見上方規則 D），不必展開本節。

---

## 規格書引用語法（HackMD 平台特性）

寫入 note `content` 時可直接使用以下 HackMD 原生語法（API 不會轉義）：

- **相對 note 連結**：`[標題](/noteId)` — 在同一 team workspace 下點擊可直接導航，規格書間互連一律用此形式，不用完整 URL。例：`[求才系統代碼表](/B1j3sN-bzx)`。
- **全文嵌入**：`{%hackmd <noteId> %}` — 將另一份 note 的內容就地嵌入渲染。慣例是包在 `:::spoiler {名稱}` 內、外層 `<div style="padding-left:50px">`，讓讀者展開閱讀引用文件（如 lightbox 規格）而不離開本文。
- 詳細的文件撰寫慣例（三層引用方式、🚧 待補規則區塊、階段拆分）見 `spec-doc-1111` skill。

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
- **Moving a note into a folder**: `PATCH /teams/:teamPath/notes/:noteId` with body `{"parentFolderId": "<folder UUID>"}`. The UUID must be the folder's **internal UUID** (from the note's `folderPaths[].id` or the Folder API `id`), **not** the short `clientId` seen in folder URLs — passing `folderId` or the short id returns `202` but silently does nothing. Verify by re-fetching the note and checking `folderPaths`.
- **內嵌 HTML 區塊遇空行會斷掉。** HackMD 走 markdown-it（CommonMark），Type 6 HTML 區塊（`<div>` 等）**在遇到空行時就結束**——之後的內容會被當成一般 markdown 或 code block 而跑版。寫「HTML 絕對定位覆蓋」標註或整段 `<div>` 版面時：body 內不要留空行、行首不要 4 格縮排、避免 `<main>`（改用 `<div>`）。`<style>` 要生效還需在該 note 開啟 Custom CSS 預覽（工具列油漆刷 → Custom CSS）。（來源：官方 `hackmd-skills/visualize-hmd`。）
- When in doubt, the **live Swagger docs at `https://api.hackmd.io/v1/docs`** are canonical.
