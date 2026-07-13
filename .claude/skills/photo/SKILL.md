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

**Step 0：先判斷這張圖是不是已經有穩定的 HackMD 網址了**——如果圖片本來就已經存在於某份 HackMD 文件裡（例如既有內容裡已經寫著 `![image](https://hackmd.io/_uploads/xxx.png)`，或使用者直接貼給你的就是一個 `hackmd.io/_uploads/...png` 連結），代表這張圖**已經有 HackMD 自己的圖床網址、本來就穩定可引用**，直接沿用這個既有網址即可：
- **不要**下載、**不要** `cp` 進 `.claude/assets/`、**不要** commit、**不要** push。
- 直接把這個 `hackmd.io/_uploads/...` 網址當成 `<img src="...">` 的來源，套用規則二的 HTML 標註／排版即可。
- 只有在**需要用 Pillow 唯讀分析像素座標**（例如量測按鈕 bounding box 來定位紅框）時，才需要暫時 `curl` 下載一份到本地 `/tmp` 做分析用——這份本地暫存檔只是分析用途，分析完不用存進 repo，因為最終引用的還是原本的 HackMD 網址。
- 這條規則的判斷依據很簡單：**這張圖現在能不能直接在瀏覽器打開一個 HackMD 網域的網址看到它？能，就沿用；不能（純聊天貼圖、Figma fetch 出來的短效網址、使用者本地檔案），才進下面完整存檔流程。**

若圖片**沒有**既有的 HackMD 網址（Figma MCP 剛截的圖、使用者上傳的本地檔案等），才走以下完整存檔流程：

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
   HackMD／規格書內一律引用這個網址。（若該圖其實已有既有 HackMD 網址，見上方 Step 0——那種情況根本不會走到這一步）
6. **PATCH 前確認資產已可達**：`curl -sI <raw url>` 確認 200 再寫進文件，避免文件裡出現 404 圖。

---

## 規則二：標註樣式 —— HTML 絕對定位覆蓋

### 基本結構

**最外層一律加白色背景容器**（`background:#fff`），再放 `position:relative` 包住 `<img>`，badge 用 `position:absolute` 疊在對應座標：

```html
<div style="background:#fff; padding:14px; border-radius:8px;">
  <div style="position:relative; display:inline-block; max-width:400px;">
    <img src="https://raw.githubusercontent.com/sulfurcreek/main/<sha>/.claude/assets/E1_change_vendor.png" style="display:block; width:100%;">
    <div style="position:absolute; top:83%; left:50%; background:#FF5F57; color:#fff; font-family:Inter,Helvetica,Arial,sans-serif; font-size:13px; font-weight:700; padding:3px 9px; border-radius:10px; box-shadow:0 1px 3px rgba(0,0,0,0.3);">1</div>
  </div>
</div>
```

> ⚠️ **一定要包白底**：HackMD 深色模式（dark mode）下，頁面背景會變深色，但截圖裡的黑字說明文字／深色 UI 文字不會跟著反轉，導致深色模式下文字看不清楚甚至完全消失。外層 `background:#fff`（加 `padding` 讓白底有呼吸空間）確保截圖無論在淺色／深色模式下都維持原始可讀對比度。**這條規則不可省略**，是本 skill 所有 HTML 標註區塊的必要外層。

| 項目 | 值 | 說明 |
| :--- | :--- | :--- |
| badge 底色 | `#FF5F57` | 沿用既有紅色慣例（與舊 Pillow badge 同色，僅改實作方式） |
| badge 文字色 | `#fff` | 白字 |
| 字型 | `Inter, Helvetica, Arial, sans-serif` | 與 mermaid 圖表字型一致 |
| `border-radius` | `10px` | 圓角 |
| `padding` | `3px 9px`（單純數字編號）／`4px 10px`（較長文字） | 依內容長度微調 |
| 定位 | `top`/`left` 用 **百分比**，不用絕對 px | 圖片在不同裝置寬度縮放時 badge 仍對齊；px 只在你已固定 `<img>` 顯示寬度時才用 |

### 座標怎麼抓

1. 用 Read 工具開圖確認視覺位置，用 Pillow 唯讀掃描算出目標元件的 pixel bounding box（沿用規則一的唯讀分析）。掃描時**用元件實際邊框顏色做遮罩**（例如按鈕邊框藍色 `r<130,g<180,b>190` 這類寬鬆但排他的顏色條件），對每一列/每一行加總遮罩像素數（`colsum`/`rowsum`），取非零區間頭尾當成 bounding box——比憑肉眼目測或憑經驗猜座標準確。
2. **框線必須完全落在元件外圍留白處，不可壓在按鈕/元件本身上**：這是最常被打槍的點。算出元件 bounding box 後，四邊各往外擴 padding 再轉百分比，讓 3px 紅框線清楚坐落在元件邊緣**之外**的空白區，跟元件之間看得到一圈間隙——不是把框「貼齊」元件邊界（那樣紅線會壓在按鈕圓角/陰影上，看起來像框破了）。具體：
   - **上下**：往外擴較多（各約 10–14px），因為按鈕上下通常有留白，擴大高度最能製造「框包住整顆按鈕」的視覺；使用者反覆要求的多半是「高度不夠、把框高度再擴大」。
   - **「不壓到」的定義＝框上緣要在按鈕的「最上緣」之上**（落在按鈕上方那條留白間隙裡），不是「在按鈕內文字之上」就好——框頂只到按鈕框內、還壓在按鈕本體上是不合格的。實務數值參考：480×819 的手機截圖、按鈕列在底部時，`top` 抓到約 `83%`（框頂進入按鈕上方留白）、`height` 約 `7.7%` 才能讓上下框線都在按鈕外。
   - **外側**（元件與畫面邊緣、或空白較大那側）：多擴（約 8–10px）。
   - **內側**（兩個相鄰框中間那側）：少擴（約 3px），避免兩框重疊。
   - 目標是框線看起來完整包住整個按鈕（含圓角、陰影）並外留一圈空隙，而不是剛好卡在文字或元件邊框上。
3. 換算成百分比：`top% = box_y / image_height * 100`、`left% = box_x / image_width * 100`；寬高同理用 `(box_x1 - box_x0) / image_width * 100`。
4. **下 PATCH 前必做「真實 HTML 渲染」驗證（不是只用 Pillow 疊框近似）**：Pillow 疊框只能大致核對座標，真正決定成品的是瀏覽器怎麼渲染那段 HTML。流程：
   - 把要寫進 HackMD 的整段 HTML（含 `position:absolute` 紅框）**存成一個暫時 `.html` 檔**放在 scratchpad（`/tmp/...`，**絕不放進 repo、絕不 commit**）。
   - 圖片 `src` 暫時改成**本地檔案 `file://` 絕對路徑**（指向 `.claude/assets/` 內的圖）——因為沙箱瀏覽器載不到 `raw.githubusercontent.com`（會顯示破圖、框就浮掉）；用本地路徑才能真實渲染。
   - 用 Playwright＋Chromium（`executablePath: '/opt/pw-browsers/chromium'`、`deviceScaleFactor:2`）開這個 `file://` 檔、`fullPage` 截圖，Read 出來目視確認紅框完整包住按鈕、上下都在按鈕外、兩張圖垂直置中、文字緊貼圖片。
   - **確認 OK 後把暫時 `.html` 檔刪掉**（`rm`），不要留在 repo 或工作區；渲染出來的驗證截圖 `.png` 留在 scratchpad 無妨（本來就不在 repo）。
   - 唯有渲染驗證通過，才把 HTML（`src` 換回 `raw.githubusercontent.com` 正式網址）PATCH 進 HackMD。曾經發生過多次問題都是省略或只做 Pillow 近似驗證：框偏移、框太貼邊不夠大、框壓在按鈕上、兩圖沒垂直置中——全都是跳過真實渲染驗證才發生。
5. 圈選整個元件（如按鈕）用邊框style而非填色 badge：

```html
<div style="position:absolute; top:83.3%; left:50.2%; width:47%; height:6.3%; border:3px solid #FF5F57; border-radius:8px;"></div>
```

- 純「框住某元件」：用上面這種透明背景＋色框的 `<div>`，不填色、不擋住畫面。
- 純「編號說明」：用規則二開頭那種實心圓角 badge。
- 兩者可疊加使用（框住元件＋角落標號）。

### 多圖流程／點擊跳轉（取代舊的 Pillow 合成拼圖）

兩張以上截圖要表達「點擊 A 圖某按鈕 → 跳到 B 圖」時，不再用 Pillow 把兩張圖拼成一張新 PNG，改用 HTML flex 容器並排＋純 HTML 箭頭；**同樣要包在白色背景容器內**（理由同上，深色模式防呆）。

兩條排版規則缺一不可：

1. **文字跟著圖片走，不單獨分列**：說明文字必須放在同一個直向欄位內、緊貼圖片下方（`margin-top:6px` 左右）——每張圖與其說明文字包在同一個 `<div>` 直向欄位裡，欄位之間才用 flex 並排。不要把所有圖片排一列、說明文字另外分一列放在下方，那樣圖片與對應文字會離很遠。
2. **兩張圖高矮不一時，欄位要垂直置中對齊**：外層 flex 容器用 `align-items:center`（不要用 `flex-start`）。來源圖（如直式手機畫面）通常比結果圖（如橫式表單截圖）高很多，`flex-start` 會讓矮的那張圖被推去跟高圖的頂部切齊、視覺上偏移不自然；`align-items:center` 讓兩欄以中線對齊，箭頭也用 `align-self:center` 確保垂直居中，不受任一欄圖片高度影響：

```html
<div style="background:#fff; padding:14px; border-radius:8px;">
  <div style="display:flex; align-items:center; gap:14px; flex-wrap:wrap;">
    <div style="max-width:260px;">
      <div style="position:relative; display:inline-block; width:100%;">
        <img src="<圖A網址>" style="display:block; width:100%;">
        <div style="position:absolute; top:85.71%; left:1.46%; width:47.08%; height:6.23%; border:3px solid #FF5F57; border-radius:8px;"></div>
      </div>
      <div style="font-size:13px; color:#333; text-align:center; margin-top:6px;">圖 A 說明文字</div>
    </div>
    <div style="font-size:26px; color:#FF5F57; font-weight:700; align-self:center;">→</div>
    <div style="max-width:300px;">
      <img src="<圖B網址>" style="display:block; width:100%;">
      <div style="font-size:13px; color:#333; text-align:center; margin-top:6px;">圖 B 說明文字</div>
    </div>
  </div>
</div>
```

- 兩張圖各自獨立存檔（規則一），HTML 只是排版容器，不產生新圖檔、不 commit 額外的拼接 PNG。
- 箭頭用純文字 `→` 或簡單 CSS 三角形，不用圖片箭頭素材；`align-self:center` 讓箭頭在圖片直欄之間垂直置中，不受圖片高矮影響。
- 多組流程（如同一來源圖分岔出兩個結果）分別各自包一層白底容器，不要共用同一層外框，保持每組流程獨立可讀。

---

## Gotcha

- **HackMD 對外層 `<div style="...">` 的支援**：HackMD 的 markdown 渲染器允許內嵌 HTML block，但每次寫完務必 PATCH 後 GET 回來確認渲染正常（尤其巢狀 `position:absolute` 在部分 markdown 解析器可能被過濾掉 style 屬性）——若發現 style 被吃掉，改用行內 `<img>` + 相鄰文字編號對照表當退場方案（`CLAUDE.md`「Markdown 標號對照表」選項）。
- **深色模式（dark mode）務必包白底**：HackMD 有淺色／深色模式切換，深色模式下頁面背景變深，但截圖與說明文字顏色不會自動反轉——沒包白底的話深色模式下文字/淺色 UI 會看不清楚甚至消失。任何 HTML 標註區塊最外層一律加 `background:#fff`（見規則二範本），這是必要步驟不是可選項。
- **禁止事項**（沿用 `CLAUDE.md`／`master_prompt.md` 既有規則）：不使用或提及任何外部 AI 圖像生成模型重繪畫面；不得用 Pillow 把 badge 燒進像素後才存檔——那是舊流程，本 skill 生效後棄用。
- **舊資產保留**：先前用 Pillow 燒進像素的既有素材（`.claude/assets/` 內已存在的 badge 版本，如 `E1_offer_seeker_tag.png`）不用回頭重做，只有「之後新增」的標註任務才套用本 skill；若之後有人要求重繪舊圖才改。

## 適用範圍

- 任何 Figma MCP 截圖／使用者上傳圖需要進 repo 給 HackMD 引用時。
- 任何需要在截圖上標紅框、編號、點擊流程箭頭時。
- 不適用於 Mermaid 圖表樣式（見 `.claude/skills/mermaid-sequence-diagram/SKILL.md` 與 `wiki/mermaid_styling_rules.md`）、不適用於規格書章節格式（見 `.claude/skills/spec-doc-1111/SKILL.md`）。
