# 樣式與符號慣例

> 屬 `spec-doc-1111` skill 的參考檔。**查特定樣式寫法時才讀**（紅字、反引號、圖片、摺疊區塊、錨點連結、版控調整說明格式）。

### 紅字：新需求／本版變更

新增或修改的需求，整段用紅字包起來，版控紀錄的「調整說明」要寫明異動區段：

```markdown
* <font style="color:red">**1-2-2 下期合約可暫停天數** `useDeadline`-`deadline_open`</font>
```

標題也可整行標紅：`##### <font style="color:red">2-1-1 預計開權時間`（紅字 `<font>` 可跨多個條列，於段落結尾再 `</font>`）。

### 欄位、旗標、狀態值：反引號

所有程式可辨識的值都用反引號，避免與說明文字混淆：

- 旗標位元運算：`organs.confirmed&131072`、`organs.showfield&4096`、`organsMore:setKind&16`
- 狀態值：`oStatus:1`、`oStatus:3`、`iskeepemployeesstatus:true`
- 權限代碼：`代碼9`、`權限代碼26`、`權限代碼27`、`（46）`
- 廠商狀態集合：`status = 0,2,4,5,6`
- 計算式：`合約結束日`-`今日日期`、`useDeadline-今天`

### 版控紀錄調整說明格式

每次發布必須在版控表新增一列，**調整說明格式**：`[異動區段] 說明內容`

- ✗ 不可只寫：「更新文件」
- ✓ 應寫：「[進入畫面權限判斷] 新增 `confirmed&131072` 外網限制，整合為權限判斷表格」
- ✓ 應寫：「[1-1-2 可暫停天數] 補充 2077/7/7 無限期顯示邏輯」

### 圖片

- 圖片來源兩種皆可：HackMD `_uploads`（手動拖入）或 GitHub raw URL（repo `.claude/assets/` 下，URL 帶 commit SHA）
- 全寬示意圖：`![image](https://hackmd.io/_uploads/xxxx.png)`
- 限寬內嵌圖兩種寫法：
  - `<div style="max-width:375px">![image](...)</div>`（markdown 圖包 div）
  - `<img style="max-width:600px" src="..." alt="{章節編號＋元件說明}">`（GitHub raw 圖用 img tag，**必加 alt** 描述對應章節）
- 常見寬度：選單 `200px`、手機版 `375px`、空狀態／lightbox `500px`、聊天室全景 `600px`、列表 `800px`、tooltip `300px`

### 截圖標注／覆蓋（從 Figma 產生規格截圖）

> ⚠️ 一般紅框／編號標註優先用 `.claude/skills/photo/SKILL.md`（HTML 覆蓋，不燒像素）。以下 Pillow 流程僅在需要**覆蓋改寫截圖裡既有文字**、或維護既有「截圖標號＝章節編號」舊格式文件時使用（完整規則見 `.claude/skills/png/SKILL.md`）。

當設計稿與規格需求有落差，或要在畫面上補規格章節標號時，用 Pillow 在截圖上疊加，**不要求設計稿與規格完全一致**——目的是示意落差與對應章節。流程：

1. **抓圖**：`mcp__Figma__get_screenshot`（傳 `nodeId`＋`fileKey`，`maxDimension` 視需要放大，預設回傳短效 URL），用 `curl` 下載 PNG。需要定位元件座標時再呼叫 `get_design_context`（輸出大時用 `excludeScreenshot:true`、再從存檔檔案 grep `data-node-id`）。
2. **定位**：用 Pillow 逐列掃描像素（無 numpy 時用 `img.getpixel`）找出區塊邊界（底色、border、文字色），決定覆蓋與標號座標。
3. **覆蓋改字**：在目標區先畫白底矩形蓋掉舊內容，再用 `ImageDraw.text` 重寫。中文字型用 `/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc`（系統無 Noto TC 時的後備）。
4. **章節標號徽章**：紅底 `#FF5F57`、`border-radius:10px`、`padding:4px 10px`（單字元約 `34×33px`）＋白字（字型 `Inter`、`font-weight:700`、`font-size:20px`、`line-height:24px`、`#FFFFFF`）；`N` 放區塊左上、`N.M` 貼元件左上（完整標號慣例見 `.claude/skills/png/SKILL.md`）。
5. **落差標注**（選用）：黃框（`outline=(255,200,0)`）圈出與設計稿不同處，旁邊以文字注明「規格：XX／現況：OO」。用 `Image.alpha_composite` 疊半透明層。
6. **裁切成小圖**：`img.crop((x0,y0,x1,y1))` 只留相關區塊，避免整頁大圖。
7. **入庫**：上傳到 Cloudflare R2 圖床（見 `.claude/skills/photo/SKILL.md` 規則一的 boto3 流程與環境變數），用回傳的 `public_url` 引用；不 commit 進 `.claude/assets/`／組 `raw.githubusercontent.com` 網址（舊法已棄用，僅 R2 環境變數不可用時當備案）。
8. **置入文件**：限寬內嵌（手機版 `<div style="max-width:375px">…</div>`），緊貼對應 `### N.M` heading 下方。

> 圖片層級只能「蓋白重寫」，無法智慧抹除原字再換字；若要乾淨替換 UI 內文字，改用 Figma MCP 編輯設計稿文字節點再重新截圖。

> **多狀態元件**（如按鈕依條件呈現不同樣式／文案）：優先用**單張代表性截圖**＋表格文字描述各狀態差異，不要把多個狀態的局部截圖裁切後堆疊拼接成一張合成圖；狀態邏輯本身寫進對應表格欄位（見下方「欄位／列定義表」）。

**固定 UI 區塊（sticky/pinned）的裁切原則**：
針對聊天室頂部固定橫欄（如面試行程確認區塊 §1.3.6）等 sticky 元件，截圖時只裁切該元件本身，**不含周圍聊天背景或其他訊息泡泡**。裁切步驟：(1) 用 `img.getpixel` 逐列掃描找橘色（`R>235,G>185,B<220`）及白底展開區邊界；(2) 上下各留 3px padding；(3) badge **不壓畫面**——用 `Image.new` 在元件上緣擴增一條純白邊（高度剛好容納 badge，約 33px＋上下各約 4px），原圖貼白邊下方，badge 畫在留白內（x=4）；badge 文字可帶「類型·視角」（如 `詢問意願·廠商發出`）。兩種情境各一張截圖：**展開狀態**（摘要列＋展開資訊＋操作按鈕）＋**下拉選單**（摘要列＋選單項）。

### 摺疊區塊

- 大段補充（如判斷邏輯、流程圖）：`:::spoiler {標題}` ... `:::`
- 行內小補充：`<details><summary>{摘要}</summary>{內容}</details>`
- 需要縮排的 spoiler 可包在 `<div style="padding-left:50px">` 內

### 跨文件／錨點連結

- 連到同文件章節：`[1.1 篩選 Tab](#1.1-篩選-Tab)`（錨點為編號＋標題去空白）
- 連到另一份 HackMD 規格：`[信件列表](/uoldEfXhT9KrbGxQJwg4ew)`（**相對 note 路徑**，不用完整 URL）
