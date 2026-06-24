<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

# 信件訊息頁（ResumePoolNoticeMail）前端視覺調整需求

> 代號：`待補`（求才系統 B 端，頁面 `ResumePoolNoticeMail.aspx`）

* User Story: `身為一個求才廠商，我想要在「信件訊息」頁看到符合新版設計系統的列表與篩選介面，以便更清楚地檢視與操作與求職者的聯繫訊息`
* Use Case:
  * `廠商進入信件訊息頁 → 系統依新版視覺（底線式頁籤、合併便當、列表樣式）渲染畫面`
  * `本文件僅描述前端視覺/樣式調整，不變更後端資料來源與既有互動邏輯`

:::spoiler Document info

文件版本：v0.1.0
最後更新：2026/06/23
文件作者：UIUX
文件狀態： <span style="color:blue">草稿</span></h6>
功能位置：
<https://recruit.1111.com.tw/.../ResumePoolNoticeMail.aspx>

## 版控紀錄

| 版本 | 日期 | 作者 | 調整說明（異動區段 + 內容摘要） |
| :---: | :--- | :--- | :--- |
| 0.1.0 | 2026-06-23 | UIUX | 初版：彙整信件訊息頁前端視覺調整需求，逐一列出每個 HTML 標籤的更動與對應 CSS 檔名/行數 |

[TOC]

:::

## 示意圖

* 對應 Figma：頁籤 `信件簡訊範本 node 3235-13620`、設計系統 `Horizontal/Tab node 566-1943`。
* 預覽：隨本文件附上之自包含預覽檔 `preview-tab-underline.html`（單檔可直接於瀏覽器開啟）。
* 完整截圖：`待補`

## 初始化

> 本文件為**純前端視覺/樣式調整**，不涉及進入權限、資料來源或路由變更。

### 進入路徑

* 沿用現行頁面進入路徑（求才後台 → 信件訊息），不變更。

### 權限判斷

* 無新增/變更權限條件，沿用原頁面。

### 資料載入

* 資料來源、API、分頁邏輯**皆不變**，僅調整呈現樣式。

---

## 閱讀方式（給工程師）

1. 下列章節**逐一對應一個 HTML 標籤／區塊**；該標籤若有 CSS 調整，CSS 需求寫在同一章節內，並標明**修改的 CSS 檔名與行數**。
2. CSS 檔名統一為 **`resumePoolNoticeMail.css`**；所附行號為**隨附 mock 檔**的行號（共 1706 行版本），正式 codebase 行號請依 selector 對應。
3. 值一律以反引號標出（如 `#1a66ff`、`16px`）。涉及 HTML 結構/屬性的更動另以 🚧 標明，並提醒**以正式環境結構為準**（背景見 `01_HTML結構調整對照.md` §2.5）。
4. 標 <font style="color:red">紅字</font> 者為需特別注意之結構前提或與正式環境不一致處。
5. <font style="color:red">**字體一律使用微軟正黑體**</font>（`"Microsoft JhengHei","微軟正黑體","新微軟正黑體",sans-serif`）。設計稿雖標 `Noto Sans TC`，**實作不採用**；全頁文字統一微軟正黑體。`Font Awesome`（圖示字型）為功能性字型，維持不動。

---

## 1 標題列 `<h2 class="Title">`（「信件訊息」）

| 項目 | 內容 |
| :--- | :--- |
| HTML 更動 | 無（僅改樣式） |
| 需求 | 套用設計系統 `Chinese/Title/28-Medium`：字體 **微軟正黑體**（`"Microsoft JhengHei","微軟正黑體","新微軟正黑體",sans-serif`）、字重 `500`、字級 `28px`、行高 `150%`(≈42px)、字色 `#212529` |
| CSS 檔／行 | `resumePoolNoticeMail.css` L1686–1693（新增 `.headingBar .Title` override）｜原值在 L556–560：`color:#4e4e4e; font-size:20px` |
| 視覺目的 | 標題放大、改用設計系統標題級距與中性主色 |

---

## 2 頁籤 `<ul class="tabs"> / <li class="tab">`（底線式 Tab）

HTML **不變**（底線以 `li.active::after` 偽元素達成，無新增節點）。依設計系統把「膠囊/方塊式」改為「底線式 Tab」。

| 狀態 | 樣式需求 | token |
| :--- | :--- | :--- |
| 容器 `.tabs` | `display:flex; justify-content:flex-start; gap:32px; border-bottom:1px solid #e9ecef; padding:16px 32px 0`；移除 `list-style`/`margin` | Space/800、Border/Neutral/Tertiary |
| Default `.tabs .tab` | 透明底、無框；字色 `#212529`、字重 `400`、`16px`、行高 `1.55`；`padding:8px 0 16px`；`cursor:pointer` | Text/Neutral/Primary |
| Hover `.tabs .tab:hover` | 字色轉 `#1a66ff`、無底線、字重不變 | Text/Primary/Primary |
| Selected `.tabs .tab.active` | 字色 `#1a66ff`、字重 `500`；底線 `::after` 4px、`#1a66ff`、上緣圓角 `80px` | Surface/Primary/Primary、Radius/Full |

* CSS 檔／行：`resumePoolNoticeMail.css` L1634–1678（容器 L1652、default L1661、hover L1669、selected L1670、底線 `::after` L1674）。
* 取代來源：原膠囊規則 L1067–1106 及像素取樣覆蓋（L1362、L1364、L1402–1416、L1504、L1529）；正式整併時可刪除舊規則與本區塊 `!important`。
* <font style="color:red">註：頁籤順序與「全部/未讀/已讀/已加星號/有意願」在正式環境的排序，請以正式環境為準（mock 末兩項順序與正式不同，屬 mock 偏離，非本需求）。</font>

---

## 3 頁籤容器 `#bookmark.titleBar` ＋ 篩選卡 `.whiteBg.filter`（合併為同一便當）

| 項目 | 內容 |
| :--- | :--- |
| 需求 | 將頁籤列與下方篩選列**視覺上合併為同一張圓角白卡**：上方圓角＝便當原圓角 `10px`、整體一圈陰影、中間以 `#e9ecef` 細線分隔；左右 padding 對齊便當 `32px` |
| `#bookmark.titleBar`（便當上半） | `background:#fff; border-radius:10px 10px 0 0; box-shadow:0 3px 6px rgba(0,0,0,.15); z-index:1` |
| `.whiteBg.filter`（便當下半） | `border-radius:0 0 10px 10px; margin-top:0; z-index:2`（不透明白底蓋住接縫陰影） |
| CSS 檔／行 | `resumePoolNoticeMail.css` L1640–1645（titleBar）、L1647–1650（filter） |
| 視覺目的 | 頁籤與篩選成為單一卡片，去除兩塊分離感 |

> 🚧 <font style="color:red">**結構前提（務必確認）**：本合併假設 `#bookmark.titleBar` 與 `.whiteBg.filter` 為**相鄰 sibling**。但**正式環境** `#bookmark.titleBar` 位於 `.whiteBg.list > .msgList` 內，與 `.whiteBg.filter` 並不相鄰（mock 是前一手把頁籤搬到最上層才相鄰）。</font>
>
> 工程師需先確認正式環境要採哪種版面：
> * [ ] 若維持正式環境 DOM（頁籤在 list 內）：本「合併便當」需求需改以正式結構重新定義，或調整 DOM 使兩者相鄰。
> * [ ] 若採 mock 版面（頁籤移至篩選卡上方）：需確認此 DOM 位移是否為正式需求。
> * 來源：`01_HTML結構調整對照.md` §2.5 C。

---

## 4 訊息筆數 `<span class="msgRecord">`（「共 N 筆」）

| 項目 | 內容 |
| :--- | :--- |
| HTML 更動 | 無 |
| 需求 | 套用 `Chinese/Body/16-Regular`：字體 **微軟正黑體**（`"Microsoft JhengHei","微軟正黑體","新微軟正黑體",sans-serif`）、字重 `400`、`16px`、行高 `155%`(≈25px)、字色 `#495057`、`display:inline-flex; align-items:center` |
| CSS 檔／行 | `resumePoolNoticeMail.css` L1696–1705（新增 `.actionBtn .msgRecord` override）｜原為 `14px`（L1554 群組） |
| 視覺目的 | 筆數文字級距/顏色與設計系統一致 |

---

## 5 批次按鈕 `.deleteBtn > a` / `.starBtn > a` / `.readBtn > a`

| 子項 | HTML | CSS | 說明 |
| :--- | :--- | :--- | :--- |
| 5.1 移除 icon | 🚧 移除 `.deleteBtn a` 內 `<i class="far fa-trash-alt">`、`.starBtn a` 內 `<i class="far fa-star">`（`.readBtn` 原本就無 icon） | — | 需求來源：按鈕只留文字 |
| 5.2 尺寸/置中 | 無 | L1619、L1508–1517：`width:auto; padding:0 14px; display:inline-flex; align-items:center; justify-content:center; height:25px` | 固定寬改自然寬、文字＋hover 置中 |
| 5.3 條件顯示 | 無 | L1628（預設 `display:none`）、L1631（`.actionBtn.has-checked …{display:inline-flex}`） | **勾選任一列 checkbox 才顯示三顆按鈕**（行為見 §13） |
| 5.4 配色（維持原值） | — | 刪除 `#e25656`(hover `#FFEAEB`)、星號/已讀 `#199ed8`(hover `#e9f8ff`) | 不變更 |

* CSS 檔：`resumePoolNoticeMail.css`。

---

## 6 篩選輸入元件群（邊框/hover/focus 統一）

作用標籤：`#EmpInput.jobList`(職缺)、`.LMDateSet`(日期外框)、`#txtSearchKeyWord.searchName`(關鍵字)、`#btnSearch.btnSch`(搜尋鈕)、`#txtChooseUNOs.otherAcc`(查看其他帳號)、`#ddlMailType`(信件類別)、`#ddlReaded`(求職者回覆)。

| 狀態 | 樣式 | CSS 檔／行 |
| :--- | :--- | :--- |
| 預設 | `border:1px solid #ccc; border-radius:4px; box-shadow:none; transition:border-color .15s` | L1442 起 |
| `.searchName` 接搜尋鈕 | 右側不圓角、不重複右框 | L1448 |
| `.btnSch` | 左角 `0`、右角 `4px` | L1452 |
| `.LMDateSet .start/.end` | `border:none`（外框統一、內部 input 無框） | L1457 |
| hover | `border-color:#9aa7b2` | L1467 |
| focus / focus-within | `outline:none; border-color:#4f6b92` | L1477 |

---

## 7 卡片容器 `.whiteBg` / `.whiteBg.list`

| 項目 | 原值 | 新值 | CSS 檔／行 | 視覺目的 |
| :--- | :--- | :--- | :--- | :--- |
| `.whiteBg.list` padding | `20px 24px 20px 24px` | `0 0 20px 0` | L1428 | 表格上/左/右貼齊卡片邊，僅留下方 `20px` |
| `.whiteBg` margin-bottom | `20px` | `0` | L1565 | 卡片移除下外距 |
| `.whiteBg.list .thead .tr` 頂角 | — | `border-radius:10px 10px 0 0` | L1429 | 表頭頂角隨卡片圓角 |

---

## 8 表頭列 `.msgTable .thead .tr`（含 `.th`）

| 項目 | 原值 | 新值 | CSS 檔／行 | 視覺目的 |
| :--- | :--- | :--- | :--- | :--- |
| 底色 | `#e5eaf3` | `#E3ECFD` | L1388 | 依設計圖淺藍底 |
| 文字色 | （繼承深色） | `#0D2760` | L1388 | 深藍字（配合各 `.th` 既有 `font-weight:bold`） |
| 儲存格上下 padding | `10px` | `12px`（左右維持 `15px`） | L1682–1683（`.msgTable .thead .tr .th`） | 表頭列略加高 |

---

## 9 資料列 `.msgTable .tr .mDetailA`（hover）

| 項目 | 原值 | 新值 | CSS 檔／行 | 視覺目的 |
| :--- | :--- | :--- | :--- | :--- |
| hover 效果 | 左右內陰影＋外陰影邊框（`box-shadow … inset …`）＋`z-index:2` | **移除邊框/陰影**，改 `box-shadow:none; background:#FFF7F7; cursor:pointer` | L921–927（直接改原始 `:hover` 規則） | hover 僅以淡紅底色提示，無邊框 |

---

## 10 訊息內容欄 `.td-mail`（`p.mail-type` / `bdi` / `span.badge`）

| 項目 | 原值 | 新值 | CSS 檔／行 | 視覺目的 |
| :--- | :--- | :--- | :--- | :--- |
| `<p>` 預設上下 margin | UA `16px 0` | `0`（`.msgTable p`） | L1596 | 移除類別/狀態/職缺 `<p>` 預設間距 |
| `bdi` 上 padding | `3px 0 0 0` | `2px 0 0 0` | L1386 | 類別與內容間距收斂 |
| 未讀紅點 `.badge` | `6px×6px` | `10px×10px` | L1496 | 紅點放大 |
| `.td-mail:has(.badge)` 內文寬 | `…- 6px` | `max-width:calc(100% - 12px - 18px - 10px)` | L1497 | 配合紅點變大保留寬度 |

---

## 11 回覆狀態欄 `.td-status`（含意願）

| 項目 | 內容 |
| :--- | :--- |
| 需求 | 「無意願」文字色由 `#BF1212` 改為 `#FF5D15`；「有意願」維持 `#1D880D` |
| CSS 檔／行 | `resumePoolNoticeMail.css` L983（`.msgTable .td-status .isNoWish{color:#FF5D15}`）；有意願 L980（`.isWish #1D880D`） |

> 🚧 <font style="color:red">**結構說明（重要）**：正式環境的「有意願/無意願」是放在 `.td-status` 內、以獨立節點 `p.wish-content.isWish` / `p.wish-content.isNoWish` 呈現（與 `p.reply-content` 以 `•` 分隔，例：`已回覆 • 無意願`）。本需求的 `#FF5D15` 即套在 `.isNoWish`，**正式環境請以此為準**。</font>
>
> mock 畫面上的「無意願」其實是前一手改寫到 `.td-mail > p.mail-type` 的 inline 上色（偏離正式結構），**正式環境請勿沿用** mock 的 inline 寫法。來源：`01_HTML結構調整對照.md` §2.5 D。
> 另：未讀紅點 `--State-warning #BF1212`（badge）為不同語意，**不更動**。

---

## 12 一般內容文字放大 `16px`（排除中間操作項目）

| 項目 | 內容 |
| :--- | :--- |
| 放大為 `16px` | `.tabs .tab`、`.headingBar .LMInstruct`、`.filterBox .LMVacancies`、`.filterBox input/.jobList/.searchName/.start/.end/.btnSch`、`.msgTable .thead .tr`、`.tName`、`.td-status .reply-content`、`.mail-type`、`.td-mail bdi`、`.job-content`、`.td.w8`(日期)、`.pageBox.DataPager` 及其 `a/.Currect/.dataPagerText/select/input` |
| 維持 `14px`（明確排除） | `.actionBtn` 與其 `.msgRecord`(見 §4 已另調 16px)、三顆批次按鈕 `a`、`.otherAcc`、`.LMType select`、`.seekerWillStatus select` |
| 次要層級 | `.td-status .sub-read`（求職者已讀）`14px` |
| CSS 檔／行 | `resumePoolNoticeMail.css` L1529 起（16px 群組） |

---

## 13 表頭/列 Checkbox 互動 `#checkALL` / `input[name="mainNo"]`（行為規格）

> 行為規格，實作方式（jQuery／原生）由工程師決定；CSS 端對應 `.actionBtn.has-checked` state class（§5.3）。

| 功能 | 觸發 | 操作對象 |
| :--- | :--- | :--- |
| 表頭全選/全不選 | `#checkALL` change | 所有 `input[name="mainNo"]` |
| 半選狀態同步 | 列 checkbox change | `#checkALL.indeterminate` |
| 批次按鈕條件顯示 | 任一 `input[name="mainNo"]` 被勾 | 在 `.actionBtn` 加/移除 class `has-checked` → 顯示/隱藏三顆批次按鈕 |

---

## 14 不需處理 / 排除項目

| 項目 | 說明 |
| :--- | :--- |
| `body{background:#f0f0f0}`（L1316）、欄寬 `.w2/.w5/...` 與 `.w50 flex:1`（L1320） | **mock 補值**（原站定義在未打包的 `boxPage.css`、外層 layout 提供）；正式環境已具備，**無需處理** |
| FontAwesome CDN `@font-face`、三顆按鈕/星號/清除/箭頭等 inline SVG `data-uri`、`.icon-bulb` SVG 替身 | **離線預覽替身**（打包缺資產用），正式環境用站台原字型/圖示資產，**務必排除** |

---

## 附錄：CSS 行號對照（隨附 mock 檔 `resumePoolNoticeMail.css`，1706 行版）

| 區段 | selector | 行號 |
| :--- | :--- | :--- |
| 標題 | `.headingBar .Title` | 1686–1693 |
| 底線式 Tab | `.tabs` / `.tab` / `:hover` / `.active` / `::after` | 1652 / 1661 / 1669 / 1670 / 1674 |
| 便當合併 | `#bookmark.titleBar` / `.whiteBg.filter` | 1640 / 1647 |
| 筆數 | `.actionBtn .msgRecord` | 1696–1705 |
| 批次按鈕 | 自然寬/置中、隱藏、has-checked | 1619、1508–1517 / 1628 / 1631 |
| 輸入元件 | border / hover / focus | 1442 / 1467 / 1477 |
| 卡片 | `.whiteBg.list` padding / `.whiteBg` margin | 1428 / 1565 |
| 表頭 | 配色 / `.th` padding | 1388 / 1682–1683 |
| 資料列 hover | `.mDetailA:hover` | 921–927 |
| 訊息欄 | `.msgTable p` / `bdi` / `.badge` | 1596 / 1386 / 1496 |
| 意願 | `.isNoWish` / `.isWish` | 983 / 980 |
| 16px 群 | 多 selector | 1529 起 |
