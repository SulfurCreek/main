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

## 去識別化實作（e320-unread 實測）

網址公開，且 HTML 為自包含（圖片 base64 內嵌），**原圖像素會跟著檔案公開**，所以：

1. **改像素，不是疊遮罩**：用 Pillow 開原圖（轉灰階），把要去識別的區塊塗成底色，再畫通用文字；HTML 裡只留改寫後的圖。CJK 字型用 `/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc`。
2. **通用文字對照**：求職者姓名→「求職者」、公司名→「○○股份有限公司」、學校／科系→「○○大學｜○○系」、廠商或活動標籤→「標籤」（底色取同排標籤的像素值，圓角矩形蓋掉）。
3. **座標做法**：先把圖裁出來用 Read 看過，照 1:1 像素座標塗；塗完再裁一次確認沒有殘字。
4. **頁面文字也要清**：便利貼、標題、表格裡不得出現廠商名（例：「巨匠／資展／聯成／赫綵／天地人」改寫成「合作單位或活動標籤」）。
5. **自動檢查**（推送前跑，結果列給使用者）：把 base64 換成 `IMG` 後 grep 廠商名、人名、公司名、內部欄位名、`http`（不得有外部連結）。
6. **外部依賴一律拿掉**：Google Fonts、Tailwind CDN 都不載，改用系統字體 fallback；用到的少量 utility class 直接寫進 `<style>`。頁面 `<head>` 加 `noindex, nofollow`。
7. **功能名稱、通用篩選字樣**（例：配對條件、履歷狀態選項、多筆操作）不算識別資訊，但要在回報裡列給使用者確認。
8. **使用者說「不用去識別化」時**：照使用者決定，但若已有現成的去識別化版本，直接用它（不損失閱讀），並在回報裡說明；不要為了還原原圖而額外製造風險。
9. **範圍**：一頁只放使用者核可的需求；另案畫面（例：重複履歷標籤）要使用者另外說加進來。

## Cloudflare 推送實測備忘

- **工作區保持乾淨**：未核可的頁面放暫存目錄（scratchpad），**不要放進 repo**，否則 stop hook 會一直要求 commit／push 未追蹤檔，而一推就等於上線。核可後才複製進 `wireframe-site/<slug>/`。
- **核可 ≠ 免檢查**：使用者說「這頁可以上線」才推；先把去識別化檢查結果列給使用者（上一節 5）。
- **推送指令被 auto mode 擋下時**（`git push origin HEAD:main` 可能被分類器拒絕）：不要換方式繞過，回報使用者；使用者明確下達該指令（或加 Bash 允許規則）後再重跑。
- **只 `git add wireframe-site`**；`git pull --rebase origin main` 後再 `git push origin HEAD:main`；不 force push。
- **在已上線頁面追加畫面**：從 `main` 上現有檔出發（`git pull --rebase` 後），只把新增的 JS／CSS 區塊接進去，不要拿 handoff 版覆蓋；追加內容同樣要使用者核可。
- **PAGES 區一列格式**：`<li><a href="./<slug>/">頁面標題</a>（YYYY-MM-DD）</li>`，放在 `PAGES:START`～`PAGES:END` 之間。
- **推完驗證**：等 1–2 分鐘；用 `curl -s -o /dev/null -w '%{http_code}' "https://spec-site-hosting.calvinasqw.workers.dev/<slug>/?v=$RANDOM"` 驗證首頁與該頁都回 200（`-I | head -1` 在 proxy 環境第一行是 `200 Connection Established`，不可信；加隨機參數避開快取）。
- **這個 session 對 main 的權限只限 `wireframe-site/`**：skill、CLAUDE.md、wiki 的修改一律推在自己的分支（`claude/lofi-wireframer-skill-0u25rk`），請 Repo Steward 對照吸收。

