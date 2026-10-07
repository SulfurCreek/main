---
name: lofi-wireframer
description: >
  Balsamiq 風格的低保真（lo-fi）線框圖產生器。將輸入（截圖、需求描述、既有頁面）轉成純結構性的
  手繪風 HTML wireframe，並在右側 300px 側欄附上編號對照的技術規格／流程邏輯註記（sticky notes）。
  當任務涉及「wireframe」「線框圖」「lo-fi」「mockup」「手繪風草圖」「UI flow 草圖」時使用，
  即使使用者只說「畫個草圖」「先出個簡單版面」沒有明講以上關鍵字。
  本 skill 只負責「結構草圖＋流程/資料庫邏輯註記」，不處理視覺高保真設計（那屬於 `design` skill）、
  另含「反向工程模式」：把既有真實畫面截圖＋規格書，推回有異動區塊的灰階線框圖（見 §4）。
  不處理 Figma 截圖標註（那屬於 `photo` skill）、也不涉及 1111 規格書章節格式（那屬於 `spec-doc-1111`）。
---

# Balsamiq 風格 Lo-Fi Wireframer

把輸入（截圖、需求描述、既有頁面結構）轉成極簡的手繪風 HTML wireframe，聚焦「結構、使用者流程、系統邏輯」，
不呈現任何視覺設計細節。

## 核心輸出限制

- 輸出**單一自包含的 `index.html`**（Tailwind CSS 走 CDN 引入）。
- **只輸出程式碼**，不要輸出 markdown 說明文字。

## 1. Balsamiq 手繪風美學

- **字體**：全域套用 Google Fonts 的 `Caveat`，模擬手寫感。
- **色彩**：只准黑、白、淺灰三色，去除所有品牌色。
- **邊框**：所有容器與輸入框一律 `border-2 border-black`。
- **圖片**：一律用以下佔位方塊取代真實圖片：
  ```html
  <div class="bg-gray-200 border-2 border-black flex items-center justify-center text-gray-500 font-bold text-2xl">X</div>
  ```
- **文字**：長段落一律用結構性方括號取代，例如 `[ 系統狀態說明放這裡 ]`。

## 2. 註記與流程系統

- **版面**：強制 2 欄式版面。左側放主線框圖，右側固定保留 300px 側欄作為「Technical Specs & Flow Logic」。
- **編號徽章**：在線框圖中互動元件上疊加醒目的小型編號徽章。
- **側邊便利貼**：右側側欄對應每個編號建立便利貼樣式的說明區塊：
  ```html
  <div class="bg-yellow-100 border border-yellow-400 p-3 mb-4 text-sm">…</div>
  ```
- **便利貼內容**：用來說明資料庫邏輯、使用者狀態、技術限制，例如「外部使用者連續 3 次登入失敗後觸發安全冷卻狀態」。

## 3. 執行方式

1. 分析輸入內容的核心版面結構。
2. 依上述美學規則轉成 lo-fi 版本。
3. 把任何功能性邏輯（狀態機、資料庫欄位、觸發條件等）抽取到右側註記側欄，並用編號徽章對應連結。

## 4. 反向工程模式（真實畫面截圖＋規格書 → 異動區塊線框圖）

當輸入是**已存在的真實 UI 截圖**加規格書（例：E3.2.0「未讀」篩選，產出在 `handoff/wireframes/E320_unread/`），
改用本節規則；與 §1 衝突時**以本節為準**（不用 Caveat、不用 X 佔位方塊，保持真實版面）。

### 4.1 版面與灰階
- 以真實畫面寬度為基準（例：1182px = 截圖 2364px @2x），`.stage` 加 `filter: grayscale(1)`，**整張灰階**；標註徽章（黑底白字）用 `filter:none`。
- **未異動區塊用真實截圖裁切**（`background:url(...) / <實寬>px`），**只重畫有異動的區塊**；不要整頁重畫。
- 裁切圖前先轉灰階存檔（Pillow `convert('L')`），透明區先合成到畫面底色 `#F0F0F0`。
- 要蓋掉截圖內的舊元件（如 tag 列）時，用同位置白底 cover 疊上重畫版，位置以渲染後截圖比對校正（偏差 ≤2px）。

### 4.2 圖片來源（踩過的坑）
- **相對路徑 `assets/…` 會在使用者端失效**（檔案單獨開啟／預覽窗找不到資料夾 → 區塊變白底）。
- **最終交付的 `index.html` 必須自包含**：圖片以 base64 data URI 內嵌（單張 <200KB 可行）。外部 R2 網址也可能被預覽環境擋，不當唯一來源。
- 圖片仍依 `photo` skill 規則上傳 R2（key 前綴 `photo-skill/`，憑證只讀環境變數）供 HackMD 嵌圖；R2 用途是「各狀態輸出 PNG」，不是 HTML 的載圖來源。
- 使用者給的新截圖（R2 網址）先 `curl` 下載到 scratchpad、確認尺寸與內容再裁切。

### 4.3 空畫面／空白區處理
- 規格定義為「不顯示」的區塊（例：空畫面 b 不顯示卡片），**不可真的畫出來**；若版面出現大片空白，用**現有真實圖片淡化（opacity≈.38）＋虛線框＋標籤**補齊，標籤寫明「示意：…（實際不顯示）」。
- 規格未定義的間距／是否顯示，**不自行決定**：用虛線框＋「[ 待確認 ]」標出，並列入側欄「文件待確認」便利貼（黃底虛線）。
- 並排對照（a／b）時各欄寬度不同，示意圖用 `width:100%` 縮放，不寫死像素。

### 4.4 輸出 PNG 與交接
- 單一狀態截圖模式：`index.html#sN` 只顯示該 frame（`body.single`，隱藏側欄與標題），Playwright `device_scale_factor=2`，`locator('.frame.cur .stage').screenshot()`；載圖後 `wait_for_function("document.fonts.status=='loaded'")` 再等 1.5s。
- 檔名 `E320_unread_s1.png`～`sN.png`，上傳 R2 時帶 `CacheControl: no-cache`，驗證用 `curl -s -o /dev/null -w '%{http_code}'`（**不要用 `curl -sI | head -1`**：proxy 環境第一行是 `200 Connection Established`，不是真實狀態）。
- 重新產圖後**回報實際尺寸**，與交接文件預期尺寸不同時要明講（補示意卡片會讓高度變大）。
- 交付前把 `index.html` 複製到**空資料夾**單獨渲染驗證，確認沒有外部依賴；改完 commit＋push 指定分支。
