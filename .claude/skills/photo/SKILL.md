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
   - **⚠️ 整頁渲染看不出小元件的框準不準——小框一定要另外放大檢查**：文件裡的圖通常縮到 400–520px 寬顯示，一顆 40px 的按鈕在那個尺度下只有幾個 pixel，框歪了、框太大框到隔壁欄位，在整頁截圖上完全看不出來（看起來都「差不多對」）。所以除了整頁渲染，**對每個小元件（按鈕、icon、單一欄位這類短邊 < 60px 的目標）另外做一次原生解析度的裁切放大檢查**：用 Pillow 依算好的百分比座標在原圖上畫框 → `crop` 出該元件周邊一小塊 → 放大 2–4 倍 → Read 出來確認。這步只是唯讀核對、不落地存檔，跟規則一「不產生新圖檔」不衝突。這次「分析按鈕紅框不精準」就是只看了整頁渲染就 push 才被打回。
   - **小元件不要用肉眼讀網格圖猜座標**：本節第 1 點的顏色遮罩掃描對小元件一樣適用而且更該用。畫網格圖只適合「大致定位在畫面哪一區」，最終 bounding box 一律以遮罩掃描的數值為準。
5. 圈選整個元件（如按鈕）用邊框style而非填色 badge：

```html
<div style="position:absolute; top:83.3%; left:50.2%; width:47%; height:6.3%; border:3px solid #FF5F57; border-radius:8px;"></div>
```

- 純「框住某元件」：用上面這種透明背景＋色框的 `<div>`，不填色、不擋住畫面。
- 純「編號說明」：用規則二開頭那種實心圓角 badge。
- 兩者可疊加使用（框住元件＋角落標號）。

### 單張截圖＋多個標註區域 → 說明文字放「側邊」，不是放下面

**先判斷是哪一種版型再動手**，這兩種很容易搞混、用錯會被打回：

| 情境 | 版型 | 說明文字位置 |
| :--- | :--- | :--- |
| **多張截圖**串成流程（A 圖點按鈕 → B 圖） | flex 橫向並排多張圖 | 各自**緊貼自己那張圖下方**（見下一節） |
| **單張截圖**、圖上有多個標註區域要逐一解釋 | 圖固定寬度靠左，說明用絕對定位排在**圖的右側** | **側邊**，每則對齊自己那個紅框的高度 |

單張截圖多標註時，**絕對不要把說明寫成圖片下方的編號清單**——那樣讀者得在「圖上的框」和「圖下的文字」之間來回跳，對不起來。正確做法是讓每則說明水平擺在它所標註的那個區域旁邊，視線直接平移過去：

```html
<div style="background:#fff; padding:16px 360px 16px 16px; border-radius:8px;">
<div style="position:relative; display:inline-block; width:400px;">
<img src="<圖網址>" style="display:block; width:100%;">
<div style="position:absolute; top:5.27%; left:17.34%; width:74.87%; height:4.6%; border:3px solid #FF5F57; border-radius:6px;"></div>
<div style="position:absolute; top:4.1%; left:14.5%; background:#FF5F57; color:#fff; font-family:Inter,Helvetica,Arial,sans-serif; font-size:15px; font-weight:700; width:26px; height:26px; line-height:26px; text-align:center; border-radius:50%; box-shadow:0 1px 3px rgba(0,0,0,0.4);">1</div>
<div style="position:absolute; top:2.5%; left:104%; width:310px; font-size:15px; color:#222; line-height:1.65;"><span style="color:#FF5F57; font-weight:700;">→</span> <b>①</b> 這個區域的說明文字</div>
</div>
</div>
```

技術要點（缺一不可）：

- **圖上一定要有編號 badge，不能只有側邊文字**：紅框只表示「這一塊」，讀者無從得知它對應右邊哪一則說明。每個紅框都要在**框的左上角外側**放一顆圓形數字 badge（`border-radius:50%`、`width/height:26px`、`line-height:26px` 讓數字垂直置中），側邊 callout 開頭再用同一個數字（`①②③`）呼應。**漏掉 badge 是實際被打回過的錯誤**。
- **外層容器右側預留空間**：用不對稱 padding（`padding:16px 360px 16px 16px`）把右邊空出來給 callout，否則 callout 會溢出白底容器、在 HackMD 上被裁掉。預留寬度 ≈ callout `width` ＋ 50px 餘裕。
- **圖片容器給固定寬度**（`width:400px`，不要用 `max-width:100%`）：callout 用 `left:104%` 定位是相對於這個容器寬度，容器寬度浮動的話 callout 位置會跟著飄。
- **callout 用 `left:104%`** 貼在圖的右緣外側；`top` 設成**與它對應的紅框大致相同的百分比**（可微調 ±3% 讓多則之間不互相擠壓）。
- **字級不要吝嗇**：callout `font-size` 用 **15px**（不要 12–13px）、`color:#222`（不要 `#333` 以下的淺灰）、`line-height:1.65`。截圖本身通常被縮到 400px 寬、裡面的 UI 文字已經很小，旁邊的說明文字若也小就整張圖都難讀。**「文字太小、清晰度不足」是實際被打回過的錯誤**。
- **箭頭寫在 callout 文字裡**（`<span style="color:#FF5F57; font-weight:700;">→</span>` 開頭），不要另外做一個獨立的箭頭元素——獨立箭頭在絕對定位下很難跟文字對齊。
- 若某個步驟是**純概念說明、畫面上沒有對應區域**（例如「後端分析並轉成 JSON」），一樣放一則 callout、但不畫紅框也不放 badge，`top` 放在流程順序的相應位置即可。

#### ⚠️ 分辨「給我的指示」與「要顯示的說明文字」

使用者描述步驟時，同一句話裡常常混著兩種東西，**只有後者可以出現在成品上**：

| 類型 | 性質 | 處理方式 |
| :--- | :--- | :--- |
| **定位指示** | 告訴我「框要畫在哪」 | 我讀完拿去算座標，**不可寫進 callout 文字** |
| **說明文案** | 要給讀者看的內容 | 原文照登進 callout |

實例（使用者原話）：

> 第四步：箭頭回到下方條件選擇區域（**工作經歷的或右方區域&與學歷限制以下的所有區塊**）

粗體那段是在指我「紅框要涵蓋哪些區塊」，屬於定位指示；成品 callout 只該寫「分析結果自動帶入下方條件選擇區域」。**曾經把括號裡的定位指示原封不動印在圖上被打回**——紅框本身已經表達了範圍，再用文字複述一次既冗長又像是漏編輯的草稿。

判斷訣竅：如果那段文字**拿掉之後、讀者看著紅框仍然知道在講哪裡**，它就是定位指示，該拿掉。反之若是講「這一步會發生什麼事／打哪支 API／帶入什麼資料」，才是說明文案。

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

### ⚠️ 寫進 HackMD 前：整段 HTML 每一行都不能縮排 4 個空白以上

**這是本 skill 最容易踩的雷、也是實際發生過的事故**：巢狀 `<div>` 一層一層用 2 格縮排寫，疊到第三、四層時單行縮排就會累積到 4 格以上——Markdown 規範裡「行首 4 個空白＝縮排程式碼區塊」，HackMD 的解析器會把那幾行當成 code block 逐字印出來，而不是繼續當 HTML 解析，使用者看到的會是一整串裸露的 HTML 原始碼而不是渲染結果。

**修法：組 HTML 字串時，每一行一律頂格寫（縮排 0 格），不管巢狀幾層。** 本文件裡上面所有範例的多行 `<div>` 寫法只是方便閱讀，**實際寫進 HackMD 前必須攤平成每行都從第 0 欄開始**（可以用程式接字串時直接不加 `\n  ` 縮排、只加 `\n`）。本地 `file://` 渲染驗證那步（見規則二「座標怎麼抓」第 4 點）也要用攤平後的最終版本去測，不要只測縮排版；縮排版在瀏覽器 `file://` 渲染時看不出問題（瀏覽器本來就忽略 HTML 縮排），只有實際 PATCH 進 HackMD 用 Markdown 解析器跑過一次才會現形，所以光靠本地渲染驗證這關不夠，寫入前務必自我檢查「這段字串裡有沒有任何一行開頭是 4 個以上空白」。

---

## 交付預覽 PNG 給使用者

使用者要「看成品」時一律給 PNG（原因見 Gotcha：`hackmd.io/_uploads` 的圖需登入憑證，交付 `.html` 只會破圖）。產這張 PNG 時：

- **緊貼內容裁切，不要留大片空白**：不要用 `page.screenshot({fullPage:true})` 直接拍整個 body——版面右側／下方預留給 callout 的空間會變成一大塊灰白邊，使用者得自己再裁一次。改成**對最外層白底容器那個元素截圖**，或先量出它的 bounding box 再用 `clip` 參數：

```js
const el = await page.$('body > div');           // 最外層白底容器
await el.screenshot({ path: 'preview.png' });    // 自動緊貼元素邊界
```

- **`deviceScaleFactor: 3`**（不是 2）：截圖裡的原始 UI 文字本來就小，再經過縮放與二次截圖會糊掉；拉到 3 倍才看得清楚。搭配上一節的 15px callout 字級一起做，兩者缺一都還是會被嫌「看不清楚」。
- 產完 Read 出來自己先看一遍，確認**文字讀得清楚、四周沒有多餘空白**，再交付。

## PATCH 進 HackMD 前的自檢清單

這幾項每一條都對應過至少一次「push 完被打回重做」。動手 PATCH 前逐條確認：

- [ ] **版型選對了嗎**：單張圖多標註 → 說明在**側邊**；多張圖串流程 → 說明在**各自圖下方**。（最常見的打回原因）
- [ ] **每個紅框都配了編號 badge 嗎**，且側邊 callout 用同一組數字呼應。
- [ ] **callout 裡沒有混進「定位指示」**（那種描述「框要畫在哪些區塊」的話），只留給讀者看的說明文案。
- [ ] **字級 15px、`color:#222`**，不是 12–13px 的淺灰小字。
- [ ] **小元件的框放大檢查過了嗎**：短邊 < 60px 的目標，整頁渲染看不出準不準，要另外裁切放大核對。
- [ ] **框線在元件外圍留白處**，沒有壓在按鈕本體／圓角上；框上緣在元件最上緣**之上**。
- [ ] **整段 HTML 每行縮排 0 格**（沒有任何一行開頭 ≥4 個空白）。
- [ ] **最外層有 `background:#fff`**（深色模式防呆）。
- [ ] **絕對定位的 callout 沒有溢出白底容器**（外層有預留右側 padding）。
- [ ] **圖片網址對**：已有 HackMD 網址的沿用原網址、沒有多存一份進 repo；新圖則已 commit＋push 且 `curl -sI` 回 200。
- [ ] **若是「重新繪製」**：整個區段換掉，舊 HTML 與使用者新貼的裸圖都已清乾淨。
- [ ] **暫時 `.html` 驗證檔已刪除**，沒有留在 repo 或工作區。

## Gotcha

- **HackMD 對外層 `<div style="...">` 的支援**：HackMD 的 markdown 渲染器允許內嵌 HTML block，但每次寫完務必 PATCH 後 GET 回來確認渲染正常（尤其巢狀 `position:absolute` 在部分 markdown 解析器可能被過濾掉 style 屬性）——若發現 style 被吃掉，改用行內 `<img>` + 相鄰文字編號對照表當退場方案（`CLAUDE.md`「Markdown 標號對照表」選項）。
- **深色模式（dark mode）務必包白底**：HackMD 有淺色／深色模式切換，深色模式下頁面背景變深，但截圖與說明文字顏色不會自動反轉——沒包白底的話深色模式下文字/淺色 UI 會看不清楚甚至消失。任何 HTML 標註區塊最外層一律加 `background:#fff`（見規則二範本），這是必要步驟不是可選項。
- **「重畫一次」時要換掉整個區段，不是只換自己上次那段 HTML**：使用者說「重新繪製」時，往往同時**自己在文件裡貼了新截圖**（變成一行裸的 `![image](...)`）。若只用「上次那段 HTML 字串」當 anchor 去替換，結果會是「新貼的裸圖」＋「新版流程圖」兩份並存。正確做法：重新 GET 最新內容 → 找出目標 heading 到**下一個 heading 之間的整個區段** → 整段換成新的 HTML（順手把裸圖、舊 HTML 一起清掉）→ 驗證時明確檢查「舊圖網址已不存在於文件中」。
- **不要交付引用 `hackmd.io/_uploads` 的獨立 `.html` 檔給使用者**：私人／團隊限閱筆記的圖片網址需要登入憑證才讀得到，瀏覽器的 `<img>` 沒辦法帶 token，使用者打開那個 HTML 只會看到一片破圖。使用者要「看成品」時**一律交付渲染好的 PNG**，且要照〈[交付預覽 PNG 給使用者](#交付預覽-png-給使用者)〉的規格產（緊貼內容裁切、`deviceScaleFactor:3`），不是把驗證用的 fullPage 截圖直接丟過去；只有在對方明確要 HTML 原始碼時才給，並附註圖片需登入才顯示。
- **禁止事項**（沿用 `CLAUDE.md`／`master_prompt.md` 既有規則）：不使用或提及任何外部 AI 圖像生成模型重繪畫面；不得用 Pillow 把 badge 燒進像素後才存檔——那是舊流程，本 skill 生效後棄用。
- **舊資產保留**：先前用 Pillow 燒進像素的既有素材（`.claude/assets/` 內已存在的 badge 版本，如 `E1_offer_seeker_tag.png`）不用回頭重做，只有「之後新增」的標註任務才套用本 skill；若之後有人要求重繪舊圖才改。

## 適用範圍

- 任何 Figma MCP 截圖／使用者上傳圖需要進 repo 給 HackMD 引用時。
- 任何需要在截圖上標紅框、編號、點擊流程箭頭時。
- 不適用於 Mermaid 圖表樣式（見 `.claude/skills/mermaid-sequence-diagram/SKILL.md` 與 `wiki/mermaid_styling_rules.md`）、不適用於規格書章節格式（見 `.claude/skills/spec-doc-1111/SKILL.md`）。
