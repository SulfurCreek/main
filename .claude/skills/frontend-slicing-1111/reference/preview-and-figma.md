<!--markdownlint-disable MD013-->

# 自包含預覽 + Figma token 擷取 + 環境限制

## 自包含預覽（每次動畫面都要做）

規則來自專案 `CLAUDE.md`「UI/UX 工作慣例」：**只要動到 HTML/CSS，完成後一律重生一份自包含預覽並交付**，不用使用者另外要求。

做法：讀目標 HTML 與其 CSS，把 `<link rel="stylesheet">` 換成內嵌 `<style>…完整 CSS…</style>`，輸出單檔。

```python
html=open('ResumePoolNoticeMail.html',encoding='utf-8').read()
css =open('_files/resumePoolNoticeMail.css',encoding='utf-8').read()
link='<link rel="stylesheet" href="./_files/resumePoolNoticeMail.css">'
assert link in html
open('preview-tab-underline.html','w',encoding='utf-8').write(html.replace(link,'<style>\n'+css+'\n</style>'))
```

- 用 `SendUserFile` 交付預覽檔；預覽檔也納版控、隨改動 commit/push。
- 無頭瀏覽器通常不可用（playwright 下載被擋）→ **不要因為截不了圖就略過預覽**，直接交付自包含 HTML 讓使用者自己開。

## Figma token 擷取

1. 從 URL 取 `fileKey` 與 `nodeId`（`?node-id=1-2` → nodeId `1:2`）。
2. `mcp__Figma__get_design_context`：拿到參考 code（Tailwind/React）＋截圖＋用到的字體樣式。把 Tailwind 變數對回實際值。
3. `mcp__Figma__get_variable_defs`：拿**精確 token**（hex、間距、字級、radius）。例如底線頁籤：`Text/Primary/Primary #1a66ff`、`Surface/Primary/Primary #1a66ff`、`Radius/Full 80`、`Space/800 32`；灰 Tag：`Surface/Neutral/Tertiary #e9ecef`、`Text/Neutral/Secondary #495057`、`Body/14`、`XS 999`。
4. 元件常只給部分狀態（如 Default/Actived），缺的（hover）要追問或找對應變體節點；別自己亂編，用 `get_design_context` 指定那個變體節點再抓。
5. 設計稿字體（常是 Noto Sans TC）**換成微軟正黑體**再落地。

## 環境限制速查

| 限制 | 症狀 | 對策 |
| :-- | :-- | :-- |
| 無頭瀏覽器 | 無法截圖 | 交付自包含預覽 HTML |
| HackMD egress 擋 | `hackmd.io`/`api.hackmd.io` 403 或連線失敗 | 請使用者貼/上傳內容；或開放 egress |
| 無 `HACKMD_TOKEN` | 無法用 HackMD API 建/改 note | 設 token 環境變數＋重開 session（執行中容器不會吃到新變數） |
| Figma MCP | 通常可用 | 直接用 |

## 雜項

- commit/push 時注意：若 `cwd` 已在子目錄，`git add handoff` 會失敗 → 回 repo 根目錄再 `git add`。
- 每個 commit 對應一個需求；commit message 寫清楚異動。
