# CSS 樣式調整對照表（ResumePoolNoticeMail 信件訊息頁）

> 本文件逐條列出「相對於原始 CSS」的所有樣式變更，供後續 AI agent 轉成人類前端工程師可執行的修改需求。
> 每條包含：**作用 selector｜原始值｜新值｜所屬原始檔｜變更性質｜原因**。
>
> 變更分兩種性質：
> - **【改值】**：原規則已存在該屬性，僅調整數值 → 工程師直接在原 CSS 檔改該行。
> - **【補值/覆蓋】**：原規則無該屬性，或需以新規則覆蓋 → 工程師在對應 CSS 檔該 selector 補上屬性，或新增 override。
>
> 原始 CSS 檔來源：`resumePoolNoticeMail.css`（主）、`pageBox.css`（分頁）、`all.min.css`（FontAwesome）、`normalize.css`、`intro_popModal.css`（操作指引鈕）。

---

## A. 直接改原始規則的值（建議直接改原 CSS 檔對應行）

### A1. 表頭列（header row）配色 — 依設計圖
| selector | 屬性 | 原值 | 新值 | 原始檔 | 性質 |
|---|---|---|---|---|---|
| `.msgTable .thead .tr` | `background` | `#e5eaf3` | `#E3ECFD` | resumePoolNoticeMail.css | 【改值】 |
| `.msgTable .thead .tr` | `color` | （無，繼承深色） | `#0D2760` | resumePoolNoticeMail.css | 【補值】 |

> 表頭文字配合既有 `font-weight:bold`（來自各 `.th` 的 inline style）。底色與文字色取樣自使用者提供的設計圖（淺藍底＋深藍字）。
> ⚠️ 表頭底色在本 mock 中同時存在三處需一致：(1) 上述原始規則、(2) 像素取樣覆蓋規則、(3) `.thead` 的 inline `style`。正式環境**以原始規則為準即可**，移除多餘來源。

### A2. 資料列儲存格 padding
| selector | 屬性 | 原值 | 新值 | 原始檔 | 性質 |
|---|---|---|---|---|---|
| `.msgTable .tr .td` | `padding` | `10px 15px`（原始） | `10px 15px`（維持） | resumePoolNoticeMail.css | 【改值/最終回復原值】 |

> 過程中曾改 `8px 15px` 縮列高，後依 DevTools 指示**回復為原始 `10px 15px`**。最終 = 原值，工程師無需變更此項。

#### A2-bis. 表頭列（第一個 `.tr`）儲存格上下 padding
| selector | 屬性 | 原值 | 新值 | 原始檔 | 性質 |
|---|---|---|---|---|---|
| `.msgTable .thead .tr .th` | `padding-top` / `padding-bottom` | `10px`（繼承 `.tr .th` 的 `10px 15px`） | `12px`（左右仍 `15px`） | resumePoolNoticeMail.css | 【改值】 |

> 需求：第一個 `div.tr`（＝表頭列，含全選 checkbox 那列）上下 padding 由 10px 改 12px，列高略增。僅影響表頭列；資料列 `.td` 維持 10px。

### A3. list 卡片（便當）padding
| selector | 屬性 | 原值 | 新值 | 原始檔 | 性質 |
|---|---|---|---|---|---|
| `.whiteBg.list` | `padding` | `20px 24px 20px 24px` | `0 0 20px 0` | resumePoolNoticeMail.css | 【改值】 |

> 需求：表格上方與左右**貼齊卡片邊**（移除上/左/右 padding），**僅保留下方 20px**（沿用原始 bottom 值）讓分頁不貼底。

### A4. 卡片（便當）下外距
| selector | 屬性 | 原值 | 新值 | 原始檔 | 性質 |
|---|---|---|---|---|---|
| `.whiteBg` | `margin-bottom` | `20px` | `0` | resumePoolNoticeMail.css | 【改值】 |

---

## B. 覆蓋規則（override，目前以獨立區塊 + `!important` 實作；工程師可整併進原檔）

> 以下為 mock 中的 override 區塊。每條標注「邏輯上應整併進哪個原始 selector / 檔」。
> 多數使用 `!important` 是因 mock 採「原 CSS bundle + 後綴覆蓋」策略；正式環境整併後可移除 `!important`。

### B1. 全域 / 容器
| selector | 屬性=值 | 性質 | 原因 |
|---|---|---|---|
| `body` | `background:#f0f0f0` | 補值 | 頁面底灰（取樣值），原站由外層 layout 提供 |
| `.msgTable .tr .td.w50 / .th.w50` | `flex:1; min-width:0` | 補值 | 訊息欄原 CSS 無 `w50` 寬度定義 → 需 flex 撐滿剩餘寬 |
| 欄寬 `.w2/.w5/.w8/.w10/.w12/.w13/.w100` | `width:2/5/8/10/12/13/100%` | 補值 | 原站欄寬定義在未打包的 boxPage.css，需補回 |

### B2. 頁籤 tabs（底線式 Tab，依共用設計系統 `Horizontal` 元件）

> **改版說明（取代舊膠囊/方塊頁籤）**：依 Figma 共用設計系統（`TXqUqUVQWVfMmOPnTPGOKc`，`Horizontal` / `Tab`，含 Default/Hover/Actived 三態 = node `566-1943`；情境圖 node `3235-13620`）把頁籤由「膠囊/方塊式」改為「底線式 Tab」。
> 三態：**Default** 灰字 `#212529`/weight 400；**Hover** 藍字 `#1a66ff`/weight 400/無底線；**Selected(active)** 藍字 `#1a66ff`/weight 500 + 4px 藍底線 `#1a66ff`（上緣圓角 80px）。
> 底線以 `li.active::after` 偽元素達成（**DOM 零改動**）。此段一併覆蓋舊像素取樣值（原 B2 膠囊樣式）。

| selector | 屬性=值（新） | 原值 | 性質 | 原因／token |
|---|---|---|---|---|
| `#bookmark.titleBar` | `background:#fff` | （無底色） | 補值 | 頁籤襯白、接合下方白卡 |
| `.tabs` | `display:flex; justify-content:flex-start; align-items:stretch; gap:32px; list-style:none; margin:0; padding:16px 32px 0 32px; border-bottom:1px solid #e9ecef` | 原 `justify-content:center; align-items:flex-end; border-bottom:#4f6b90 1px`（且舊覆蓋為 `#DCE3EB` 底線） | 改值 | 左對齊、頁籤間距 32px(Space/800)、上 16px(Space/400)、左右 32px(Space/800)、底部分隔線 `#e9ecef`(Border/Neutral/Tertiary) |
| `.tabs .tab`（default） | `position:relative; margin:0; padding:8px 0 16px 0; background:none; border:none; border-radius:0; color:#212529; font-size:16px; font-weight:400; line-height:1.55; cursor:pointer` | 舊膠囊：`background:#DCE3EB; color:#3f3f3f; padding:9px 28px; border-radius:8px 8px 0 0; margin:0 4px` | 改值 | 去膠囊底色/圓角，純文字；灰字 `#212529`(Text/Neutral/Primary)、16px、pt 8px(Size/100)/pb 16px(Size/200)/px 0 |
| `.tabs .tab:hover` | `color:#1a66ff` | （無 hover 樣式） | 補值 | hover 轉品牌藍 `#1a66ff`(Text/Primary/Primary)、不變字重/無底線 |
| `.tabs .tab.active, .tabs .active`（selected） | `color:#1a66ff; font-weight:500; background:none; border:none` | 舊：`background:#fff; color:#000; margin:0 4px -3px 4px; padding:10px 28px 11px 28px` | 改值 | 選中藍字 `#1a66ff` + weight 500（Chinese/Body/16-Medium） |
| `.tabs .tab.active::after, .tabs .active::after` | `content:""; position:absolute; left:0; right:0; bottom:0; height:4px; background:#1a66ff; border-radius:80px 80px 0 0` | — | 補值 | 選中底線：4px、`#1a66ff`(Surface/Primary/Primary)、上緣圓角 80px(Radius/Full) |

> 備註：`gap` 取代原 margin，第一顆「全部」自然貼齊容器左 padding（32px，與下方篩選卡內容對齊）；`align-items:stretch` 讓各 `li` 等高、底緣對齊分隔線，底線即落在線上。
> 此區塊覆蓋的既有膠囊樣式來源（正式整併時可刪）：原始 `.tabs`/`.tabs .tab`/`.tabs .active`、像素取樣覆蓋、接合覆蓋（active `-3px`）、`.tabs .tab:first-child` 對齊、字級覆蓋。

### B2-bis. 頁籤併入篩選便當（頁籤＋篩選＝同一張白色圓角卡）

> 需求：把頁籤列 `#bookmark.titleBar` 與下方篩選列 `.whiteBg.filter` 做成**同一個便當**。上方圓角與左右 padding 沿用原篩選便當（`.whiteBg` 的 `border-radius:10px`、左右 `32px`）。**CSS-only，DOM 不變**（兩者本就是 `.cont` 內相鄰 sibling）。

| selector | 屬性=值（新） | 原值 | 性質 | 原因 |
|---|---|---|---|---|
| `#bookmark.titleBar` | `background:#fff; border-radius:10px 10px 0 0; box-shadow:0 3px 6px 0 rgba(0,0,0,.15); position:relative; z-index:1` | 原 `padding:0; z-index:3`、無圓角/陰影 | 改值/補值 | 便當**上半**：上方圓角 10px（＝`.whiteBg`）、與便當同陰影使側邊連續 |
| `.whiteBg.filter` | `border-radius:0 0 10px 10px; margin-top:0; position:relative; z-index:2` | 原 `.whiteBg` 四角 `10px`、`z-index:1` | 改值 | 便當**下半**：僅留下方圓角與頁籤接合；`z-index:2`＋不透明白底蓋掉頁籤往下投射的接縫陰影 |

> 原理：兩相鄰 sibling 各帶相同便當陰影 → 上/下/左右陰影連續；下半 `z-index` 較高且與上半齊貼（`margin-top:0`），其白底蓋住接縫處的下投陰影 → 視覺成為單一卡片。頁籤底部 `#e9ecef` 細線（B2 的 `.tabs` border-bottom）落在接縫上方，恰為頁籤/篩選分隔線。左右 padding 已是 `32px`（與便當一致），「全部」與「篩選訊息」左緣對齊。

### B3. 操作列 actionBtn（截圖為靠左群組）
| selector | 屬性=值 | 原值 | 性質 | 原因 |
|---|---|---|---|---|
| `.actionBtn` | `justify-content:flex-start` | `space-between` | 改值 | 截圖操作項目靠左群組，非兩端撐開 |
| `.actionBtn .msgRecord` | `margin:7px 12px 7px 0` | inline `7px 10px` | 改值 | 「共127筆」與後續按鈕間距 |
| `.actionBtn #rPoolMail` | `margin-left:8px` | — | 補值 | 下拉群組與按鈕群組間距 |
| `.actionBtn .LMType` | `margin:0 8px 0 0` | — | 補值 | 下拉間距 |

### B4. 三顆批次按鈕（刪除 / 移除星號 / 已讀勾選訊息）
| selector | 屬性=值 | 原值 | 性質 | 原因 |
|---|---|---|---|---|
| `.actionBtn .deleteBtn` | `margin-left:0` | （原無） | 改值 | 間距一致：deleteBtn 不留左距 |
| `.actionBtn .starBtn` | `margin-left:5px` | `margin:0 0 0 5px`（原值） | 維持原值 | 三顆間距一致＝原始 5px |
| `.actionBtn .readBtn` | `margin-left:5px` | `5px`（原值） | 維持原值 | 同上 |
| `.actionBtn .deleteBtn a / .starBtn a / .readBtn a` | `width:auto; padding:0 14px; display:inline-flex; align-items:center; justify-content:center; height:25px; line-height:1` | 原 `width:80px/110px; display:inline-block; line-height:25px; text-align:center` | 改值 | 固定寬改自然寬、文字+hover 置中 |
| `.actionBtn .deleteBtn / .starBtn / .readBtn` | `display:none`（預設） | — | 補值 | **預設隱藏** |
| `.actionBtn.has-checked .deleteBtn / .starBtn / .readBtn` | `display:inline-flex; align-items:center` | — | 補值 | **勾選任一 checkbox（JS 加 `.has-checked`）才顯示** |

> 顏色維持原值：刪除 `#e25656`（hover `#FFEAEB`）、星號/已讀 `#199ed8`（hover `#e9f8ff`）。

### B5. 六個輸入元件 邊框 / 行為統一
作用對象：`#EmpInput.jobList`(職缺)、`.LMDateSet`(日期外框)、`.searchName`(關鍵字)、`.otherAcc`(查看其他帳號)、`.LMType select`(信件類別)、`.seekerWillStatus select`(求職者回覆)

| 狀態 | 屬性=值 | 原值 | 性質 | 原因 |
|---|---|---|---|---|
| 預設 | `border:1px solid #ccc; border-radius:4px; box-shadow:none; transition:border-color .15s` | 各元件邊框/圓角不一 | 改值 | 統一 |
| `.searchName` | `border-right:none; border-top-right-radius:0; border-bottom-right-radius:0` | — | 補值 | 與搜尋鈕相接 |
| `.btnSch` | 左角 0、右角 4px | — | 補值 | 與關鍵字框相接 |
| `.LMDateSet .start/.end` | `border:none` | — | 補值 | 日期外框統一、內部 input 無框 |
| `:hover` | `border-color:#9aa7b2` | — | 補值 | 一致 hover |
| `:focus` / `:focus-within` | `outline:none; border-color:#4f6b92` | — | 補值 | 一致 focus |

### B6. 訊息類別段落間距（面試邀約上下過大）
| selector | 屬性=值 | 原值 | 性質 | 原因 |
|---|---|---|---|---|
| `.msgTable p` | `margin:0` | `<p>` 預設 `16px 0`（UA） | 改值 | 移除類別/狀態/職缺 `<p>` 的預設 16px 上下 margin |
| `.msgTable .td-mail bdi` | `padding:2px 0 0 0` | 原 `3px 0 0 0` | 改值 | 類別與內容間距收斂 |

### B7. 未讀紅點放大
| selector | 屬性=值 | 原值 | 性質 | 原因 |
|---|---|---|---|---|
| `.msgTable .td-mail .badge` | `width:10px; height:10px` | `6px; 6px` | 改值 | 放大為 10×10 |
| `.msgTable .td-mail:has(.badge) .mail-type, bdi` | `max-width:calc(100% - 12px - 18px - 10px)` | `...- 6px` | 改值 | 配合紅點變大保留寬度 |

### B8. 一般內容文字 16px（排除中間操作項目）
**放大為 16px**：`.tabs .tab`、`.headingBar .LMInstruct`、`.filterBox .LMVacancies`、`.filterBox input/.jobList/.searchName/.start/.end/.btnSch`、`.msgTable .thead .tr`、`.msgTable .tName`、`.td-status .reply-content`、`.mail-type`、`.td-mail bdi`、`.job-content`、`.td.w8`(日期)、`.pageBox.DataPager` 及其 a/.Currect/.dataPagerText/select/input。

**維持 14px（明確排除）**：`.actionBtn` 與其 `.msgRecord`、三顆批次按鈕 a、`.otherAcc`、`.LMType select`、`.seekerWillStatus select`。

**次要層級**：`.td-status .sub-read`（求職者已讀）`14px`。

| selector | 屬性=值 | 原值 | 性質 |
|---|---|---|---|
| 上列「放大」群 | `font-size:16px` | 原 13/14/15px 不等 | 改值 |
| `.actionBtn` 群 | `font-size:14px`（維持） | `14px` | 維持/明確排除 |

### B9. 標題與訊息筆數文字（依設計 Figma typography token）
| selector | 屬性=值（新） | 原值 | 性質 | 原因／token |
|---|---|---|---|---|
| `.headingBar .Title`（「信件訊息」標題） | `font-family:'Noto Sans TC'; font-weight:500; font-size:28px; line-height:150%; color:#212529` | `color:#4e4e4e; font-size:20px`（無指定 family/weight） | 改值 | Chinese/Title/28-Medium（行高 150%=42px、文字色 #212529 Text/Neutral/Primary） |
| `.actionBtn .msgRecord`（「共127筆」） | `font-family:'Noto Sans TC'; font-weight:400; font-size:16px; line-height:155%; color:#495057; display:inline-flex; align-items:center` | `font-size:14px`（B8 原列為「維持 14px」）、色繼承深色 | 改值 | Chinese/Body/16-Regular（行高 155%=25px、色 #495057）。**注意：此項覆蓋 B8「`.msgRecord` 維持 14px」之排除，改為 16px #495057** |

---

## C. 離線預覽替身（**正式環境不需要，務必排除**）

> 以下純為「打包檔缺資產」而做的替身，正式站台資產齊全，**工程師端不要套用**。

| 項目 | mock 做法 | 正式環境 |
|---|---|---|
| FontAwesome 字型 | `@font-face` 指向 CDN woff2 | 用站台原字型路徑 |
| 三顆按鈕 trash/star icon、行星號、清除叉叉、搜尋/日期/下拉/分頁箭頭 | 以 inline SVG `data-uri` 取代（原站走 `../../images`、`/images` 未打包） | 用站台原圖示資產 |
| 操作指引 `.icon-bulb` | inline SVG 替身（原 `/images/ICON/icon-bulb.svg` 未打包） | 用站台原 svg |

---

## D. 給後續 Agent 的轉譯指引

1. **交付工程師時，C 區全部略過**（僅離線替身）。
2. **A 區**＝直接改 `resumePoolNoticeMail.css` 既有行的值，最單純，優先描述。
3. **B 區**＝可整併進 `resumePoolNoticeMail.css` 對應 selector（移除 `!important`），或保留為一段 page-scoped override。轉譯時請逐條對應「selector → 原值 → 新值 → 視覺目的」。
4. 顏色值務必原樣保留：**標題「信件訊息」字 `#212529`（28px/500）**、**「共127筆」字 `#495057`（16px/400）**；**底線式頁籤** default 字 `#212529`、hover/selected 字＋底線 `#1a66ff`、分隔線 `#e9ecef`；表頭 `#E3ECFD`/`#0D2760`、有意願 `#1D880D`、**無意願 `#FF5D15`（原 `#BF1212`，依需求更新）**、刪除 `#e25656`、星號/已讀 `#199ed8`、搜尋鈕 `#4f6b92`、focus `#4f6b92`、hover `#9aa7b2`。（tab 未選舊值 `#DCE3EB` 已隨頁籤改版淘汰。）

> **無意願文字色更新**：`面試邀約 無意願` 文字由 `#BF1212` → `#FF5D15`。本 mock 該列以 inline `style="color:#FF5D15"` 呈現；對應的語意 CSS 類別 `.msgTable .td-status .isNoWish` 亦同步改為 `#FF5D15`（正式環境若以此 class 上色，值已一致）。註：未讀紅點 `--State-warning #BF1212`（badge）為不同語意，未更動。
5. 互動規格（全選 / 半選 / 批次按鈕條件顯示）請以「行為描述」交付，實作方式（jQuery / 原生）由工程師決定；CSS 端對應 `.actionBtn.has-checked` state class。
