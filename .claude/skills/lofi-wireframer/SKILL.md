---
name: lofi-wireframer
description: >
  Balsamiq 風格的低保真（lo-fi）線框圖產生器。將輸入（截圖、需求描述、既有頁面）轉成純結構性的
  手繪風 HTML wireframe，並在右側 300px 側欄附上編號對照的技術規格／流程邏輯註記（sticky notes）。
  當任務涉及「wireframe」「線框圖」「lo-fi」「mockup」「手繪風草圖」「UI flow 草圖」時使用，
  即使使用者只說「畫個草圖」「先出個簡單版面」沒有明講以上關鍵字。
  本 skill 只負責「結構草圖＋流程/資料庫邏輯註記」，不處理視覺高保真設計（那屬於 `design` skill）、
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
