# wireframe-site：線框圖靜態網站（Cloudflare Pages 部署目錄）

只有這個資料夾會被部署。repo 其他內容（規格、wiki、career）不會上線。

| 項目 | 設定 |
| :--- | :--- |
| Cloudflare Pages Production branch | `main` |
| Build command | （留空） |
| Build output directory | `wireframe-site` |
| Root directory | （留空） |

## 規則

- 一個線框圖一個子資料夾：`wireframe-site/<slug>/index.html`，資源用相對路徑放同資料夾。
- 預設不被搜尋引擎收錄（`noindex` meta、`robots.txt`、`_headers` 的 `X-Robots-Tag`）。
- **網址是公開的**：知道連結的人都看得到。內容含 1111 內部欄位、API 名、客戶或廠商名的線框圖，上線前先去識別化，或在 Cloudflare 啟用 Access 限制存取。
- 這個資料夾由 Repo Steward 維護骨架；各線框圖內容由「Wireframe helper v2」session 產出，經使用者核可後才放進來。
