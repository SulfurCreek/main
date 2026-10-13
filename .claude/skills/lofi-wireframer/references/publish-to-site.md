# 線框圖上線：推到 wireframe-site/（Cloudflare 自動部署）

> 回 [`../SKILL.md`](../SKILL.md)。適用 session：**Wireframe helper v2**（`session_01WDKHLDHNQtrz6oez35c7ma`）。
> 部署方式：repo 根目錄 `wrangler.jsonc` 只部署 `wireframe-site/`；推到 `main` 後 Cloudflare 約 1–2 分鐘自動上線，網址 `https://spec-site-hosting.calvinasqw.workers.dev/<slug>/`。

## 你被授權寫的範圍（main 上唯一例外）

| 路徑 | 權限 |
| :--- | :--- |
| `wireframe-site/<slug>/**`（你自己的線框圖頁面與資源） | ✅ 可建、可改 |
| `wireframe-site/index.html` 的 `PAGES:START`～`PAGES:END` 之間 | ✅ 只能在這區加／改自己那一列 |
| `wireframe-site/` 其他檔案（`_headers`、`robots.txt`、README、區塊以外的 index） | ❌ 不動，要改請回報 Repo Steward |
| main 上其他一切（`CLAUDE.md`、`.claude/`、`wiki/`、`scripts/`、`career/`…） | ❌ 唯讀 |

## 上線前閘門（缺一不可）

1. **使用者明確說這一頁可以上線**。沒說就只做在 `handoff/` 或暫存，不推 `wireframe-site/`。
2. **網址是公開的，內容要先去識別化**：不得出現內部 API 名、欄位名、資料表名、權限代碼、客戶與廠商名稱、員工姓名。未確定能否公開的字眼，一律先用通用說法，或在回報裡列給使用者確認。
3. **自包含**：資源（CSS、JS、圖）放在同一個 `<slug>/` 資料夾用相對路徑，或用 R2 絕對網址；不引用 repo 其他路徑，不載外部追蹤碼。
4. 頁面 `<head>` 要有 `<meta name="robots" content="noindex, nofollow">`（站台層級已有，頁面也加）。
5. `<slug>` 用小寫英數與連字號，例如 `e320-unread`；一頁一個資料夾，入口檔一律叫 `index.html`。

## 推送流程

```bash
git fetch origin main && git checkout main && git pull --rebase origin main
# 建立或更新 wireframe-site/<slug>/index.html（與資源）
# 在 wireframe-site/index.html 的 PAGES 區加一列：
#   <li><a href="./<slug>/">頁面標題</a>（YYYY-MM-DD）</li>
git add wireframe-site
git commit -m "wireframe: 發布 <slug>"
git pull --rebase origin main && git push origin HEAD:main
```

- 只 `git add wireframe-site`，不要 `git add -A`。
- 推送前一律 `git pull --rebase`，**禁止 force push**。
- 推完等 1–2 分鐘，打開 `https://spec-site-hosting.calvinasqw.workers.dev/<slug>/` 確認；在回報最後一行貼網址。
- 撤下一頁：刪掉 `wireframe-site/<slug>/` 與 index 那一列，commit 推送；需要使用者要求才做。

## 若推到 main 被拒（403）

這個 session 的輸出分支如果不是 `main`，平台可能擋推。這時不要換別的分支硬推，回報使用者：請他在該 session 設定把輸出分支改成 `main`，或另開一個輸出分支為 `main` 的新 session。
