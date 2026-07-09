---
name: photo
description: >
  處理任何「截圖存檔＋標註」任務時使用：Figma MCP 截圖（get_screenshot／get_design_context）、
  使用者上傳的圖片、或其他來源的畫面圖，只要需要（1）存進 repo 供 HackMD／文件引用，或（2）在圖片上
  疊加 badge／紅框／編號說明，都套用本 skill。取代舊版 `wiki/figma_rules.md`（該檔已改為指向本檔）。
  觸發時機包含但不限於：「截圖」「badge」「標註」「框起來」「打編號」「Figma 截一張圖」「存到 repo」
  「畫流程圖／點擊流程」「這個按鈕框紅框」。
  核心規則：**標註一律用 HTML 絕對定位覆蓋（absolute positioning），不燒進圖片像素**——與
  `CLAUDE.md`／`wiki/master_prompt.md` 既有的「HTML 絕對定位覆蓋」規範一致（不使用 Pillow 把 badge
  畫進 PNG 的舊做法）。
---

# 截圖存檔與標註（photo）

任何截圖任務分兩件獨立的事，本 skill 各自訂規則：

1. **存檔**：截圖從哪裡來（Figma fetch／使用者上傳）都要進 repo，才能在 HackMD 用穩定網址引用。
2. **標註**：badge／紅框／編號一律用 **HTML 絕對定位覆蓋**疊在 `<img>` 上，不修改圖片本身像素。

---

## 規則一：截圖存檔（不分來源）

無論截圖是 Figma MCP 截的，還是使用者直接貼圖/上傳，一律走同一套存檔流程：

1. **取得原始圖檔**
   - Figma 來源：呼叫 `get_screenshot`（或 `get_design_context` 取 asset URL）→ 立即 `curl -L -o` 下載到本地（scratchpad 或 `/tmp`），因為 Figma 回傳的網址是短效連結。
   - 使用者上傳／貼圖來源：若對話環境能讓工具直接讀到檔案路徑就直接用；**若拿不到原始檔案位元（純聊天貼圖、沒有落地路徑）**，明確告知使用者「無法讀取貼圖原始檔」，請對方提供檔案路徑、上傳連結，或 Figma node-id 讓我改用 Figma fetch——不可用其他截圖偽造替代，也不要用外部 AI 圖像生成模型「重畫」一張假設相似的圖。
2. **不裁切、不疊字，維持原始像素**：下載下來的圖是最終素材，後續標註一律用 HTML overlay，不用 Pillow/PIL 二次繪製或壓字進圖檔。
   - 例外：若需要知道某個 UI 元件（如按鈕）在圖片中的**像素座標**以利定位 badge，可以用 Pillow/PIL **唯讀分析**像素（如掃描邊框顏色算 bounding box），但不能用 PIL 產生新圖檔或覆寫原圖。
3. **檔名慣例**：`{章節代碼}_{語意}_{視角}.png`，例如 `E1_change_vendor.png`、`E1_offer_seeker_tag.png`。沿用既有專案慣例，勿加時間戳或亂數。
4. **落地路徑固定為 `.claude/assets/`**：
   ```
   cp <下載的圖> /home/user/main/.claude/assets/<檔名>.png
   git add .claude/assets/<檔名>.png
   git commit -m "..."
   git push -u origin <目前工作分支>
   ```
5. **取得 commit SHA 後組網址**：
   ```
   https://raw.githubusercontent.com/sulfurcreek/main/<commit_sha>/.claude/assets/<檔名>.png
   ```
   HackMD／規格書內一律引用這個網址，不要引用 HackMD 自己的 `_uploads` 暫存網址（除非該圖本來就是別人已經傳到 HackMD 的既有素材）。
6. **PATCH 前確認資產已可達**：`curl -sI <raw url>` 確認 200 再寫進文件，避免文件裡出現 404 圖。

---

## 規則二：標註樣式 —— HTML 絕對定位覆蓋

### 基本結構

外層 `position:relative` 容器包住 `<img>`，badge 用 `position:absolute` 疊在對應座標：

```html
<div style="position:relative; display:inline-block; max-width:400px;">
  <img src="https://raw.githubusercontent.com/sulfurcreek/main/<sha>/.claude/assets/E1_change_vendor.png" style="display:block; width:100%;">
  <div style="position:absolute; top:83%; left:50%; background:#FF5F57; color:#fff; font-family:Inter,Helvetica,Arial,sans-serif; font-size:13px; font-weight:700; padding:3px 9px; border-radius:10px; box-shadow:0 1px 3px rgba(0,0,0,0.3);">1</div>
</div>
```

| 項目 | 值 | 說明 |
| :--- | :--- | :--- |
| badge 底色 | `#FF5F57` | 沿用既有紅色慣例（與舊 Pillow badge 同色，僅改實作方式） |
| badge 文字色 | `#fff` | 白字 |
| 字型 | `Inter, Helvetica, Arial, sans-serif` | 與 mermaid 圖表字型一致 |
| `border-radius` | `10px` | 圓角 |
| `padding` | `3px 9px`（單純數字編號）／`4px 10px`（較長文字） | 依內容長度微調 |
| 定位 | `top`/`left` 用 **百分比**，不用絕對 px | 圖片在不同裝置寬度縮放時 badge 仍對齊；px 只在你已固定 `<img>` 顯示寬度時才用 |

### 座標怎麼抓

1. 用 Read 工具開圖確認視覺位置，用 Pillow 唯讀掃描算出目標元件的 pixel bounding box（沿用規則一的唯讀分析）。
2. 換算成百分比：`top% = box_y / image_height * 100`、`left% = box_x / image_width * 100`。
3. 圈選整個元件（如按鈕）用邊框style而非填色 badge：

```html
<div style="position:absolute; top:83.3%; left:50.2%; width:47%; height:6.3%; border:3px solid #FF5F57; border-radius:8px;"></div>
```

- 純「框住某元件」：用上面這種透明背景＋色框的 `<div>`，不填色、不擋住畫面。
- 純「編號說明」：用規則二開頭那種實心圓角 badge。
- 兩者可疊加使用（框住元件＋角落標號）。

### 多圖流程／點擊跳轉（取代舊的 Pillow 合成拼圖）

兩張以上截圖要表達「點擊 A 圖某按鈕 → 跳到 B 圖」時，不再用 Pillow 把兩張圖拼成一張新 PNG，改用 HTML flex 容器並排＋純 HTML 箭頭：

```html
<div style="display:flex; align-items:center; gap:16px; flex-wrap:wrap;">
  <div style="position:relative; display:inline-block; max-width:360px;">
    <img src="<圖A網址>" style="display:block; width:100%;">
    <div style="position:absolute; top:83%; left:52%; width:44%; height:6%; border:3px solid #FF5F57; border-radius:8px;"></div>
  </div>
  <div style="font-size:28px; color:#FF5F57; font-weight:700;">→</div>
  <div style="max-width:360px;">
    <img src="<圖B網址>" style="display:block; width:100%;">
  </div>
</div>
<div style="display:flex; gap:16px; margin-top:4px; flex-wrap:wrap;">
  <div style="max-width:360px; font-size:13px; color:#333; text-align:center;">圖 A 說明文字</div>
  <div style="width:44px;"></div>
  <div style="max-width:360px; font-size:13px; color:#333; text-align:center;">圖 B 說明文字</div>
</div>
```

- 兩張圖各自獨立存檔（規則一），HTML 只是排版容器，不產生新圖檔、不 commit 額外的拼接 PNG。
- 箭頭用純文字 `→` 或簡單 CSS 三角形，不用圖片箭頭素材。

---

## Gotcha

- **HackMD 對外層 `<div style="...">` 的支援**：HackMD 的 markdown 渲染器允許內嵌 HTML block，但每次寫完務必 PATCH 後 GET 回來確認渲染正常（尤其巢狀 `position:absolute` 在部分 markdown 解析器可能被過濾掉 style 屬性）——若發現 style 被吃掉，改用行內 `<img>` + 相鄰文字編號對照表當退場方案（`CLAUDE.md`「Markdown 標號對照表」選項）。
- **禁止事項**（沿用 `CLAUDE.md`／`master_prompt.md` 既有規則）：不使用或提及任何外部 AI 圖像生成模型重繪畫面；不得用 Pillow 把 badge 燒進像素後才存檔——那是舊流程，本 skill 生效後棄用。
- **舊資產保留**：先前用 Pillow 燒進像素的既有素材（`.claude/assets/` 內已存在的 badge 版本，如 `E1_offer_seeker_tag.png`）不用回頭重做，只有「之後新增」的標註任務才套用本 skill；若之後有人要求重繪舊圖才改。

## 適用範圍

- 任何 Figma MCP 截圖／使用者上傳圖需要進 repo 給 HackMD 引用時。
- 任何需要在截圖上標紅框、編號、點擊流程箭頭時。
- 不適用於 Mermaid 圖表樣式（見 `.claude/skills/mermaid-sequence-diagram/SKILL.md` 與 `wiki/mermaid_styling_rules.md`）、不適用於規格書章節格式（見 `.claude/skills/spec-doc-1111/SKILL.md`）。
