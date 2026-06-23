# HTML 結構調整對照表（ResumePoolNoticeMail 信件訊息頁）

> 本文件供後續 AI agent / 前端工程師理解「相對於原始頁面 HTML」做了哪些**結構與標籤層級**的調整。
>
> ⚠️ **2026-06 更正**：本文件原宣稱「DOM 結構與 class/tag 完全沿用原檔、零改動」。經取得正式環境 `ResumePoolNoticeMail.aspx` HTML 後逐行比對，確認**此宣稱不成立**——前一手在產出 mock 時對結構有多處偏離。**class/tag 名稱本身沒有被改名或拼錯**（mock 未出現任何正式環境不存在的 class），偏離屬於「**節點刪除／屬性（`data-*`、`onclick`）移除／位置搬移／意願呈現方式改寫／新增節點**」。完整清單見 **§2.5 與正式環境結構偏離清單**。下方 §0 結論、§1「完全沿用」、§3 之敘述均以 §2.5 為準理解。本輪僅更正紀錄文件，**未更動 HTML**。

---

## 0. 對照基準

| 項目 | 說明 |
|---|---|
| 原始頁面 | 1111 recruit 企業端 `ResumePoolNoticeMail.aspx`（信件訊息列表） |
| 對照檔 | `ResumePoolNoticeMail.html`（本次產出） |
| DOM 層級 | `.content > .cont > [.headingBar, #bookmark.titleBar, .whiteBg.filter, .actionBtn, .headingBar(空), .whiteBg.list]` |
| 結論 | ⚠️ 原記「**結構零改動**」**不正確**（見 §2.5）。實際有結構偏離：刪節點、移除 `data-*`/`onclick`、位置搬移、意願呈現改寫、新增節點。惟 **class/tag 名稱均無改名/拼錯**。 |

---

## 1. 結構層級（mock 現況樹）

> ⚠️ 下圖是**本 mock 目前的 DOM 樹**，並非「與正式環境逐一相同」。標題列、頁籤位置、空 `.headingBar` 間隔等已與正式環境不同（例如 `#bookmark.titleBar` 在正式環境是位於 `.whiteBg.list > .msgList` 內，mock 搬到了 `.cont` 最上層；且正式環境 titleBar 內含 `h1.titleFont` 與 `span.msgRecord`，mock 已刪/搬走）。差異全列於 §2.5。
>
> 以下節點的**標籤名稱與 class 確實與原檔相同（無改名）**，差異在於位置與是否保留：

```
.content
└─ .cont
   ├─ .headingBar              （標題列：h2.Title + button#btnGuidedTour.btn-guidedTour + .LMInstruct）
   ├─ #bookmark.titleBar
   │  └─ #UpdatePanel3.Areabox
   │     └─ ul.tabs > li.tab[data-target][data-type] ×5
   ├─ .whiteBg.w100.filter
   │  └─ .filterBox
   │     ├─ .LMVacancies > .SearchPanelMainDiv（#EmpInput.jobList.w95 + i.SearchPanelClear）
   │     ├─ .LMDateSet（#StartDate.datepicker.start / #EndDate.datepicker.end）
   │     └─ .LMSch > #UpdatePanel1.Areabox（#txtSearchKeyWord.searchName + #btnSearch.btnSch）
   ├─ .actionBtn
   │  ├─ span.msgRecord
   │  ├─ .col（.deleteBtn / .starBtn / .readBtn / #ucSelectAccountListPanel.accoutSelect>.otherAcc）
   │  └─ #rPoolMail.Areabox > .col（.LMType>select#ddlMailType / .seekerWillStatus>select#ddlReaded）
   ├─ .headingBar（空節點，原檔即存在，作間隔用）
   └─ .whiteBg.w100.list
      └─ .msgList > #UpdatePanel2.Areabox > #divMailList.tabContent > #all.panel.active
         └─ .msgTable
            ├─ .thead > .tr（.th.w5>label.checkAll>input#checkALL + .th.w2 + .th.w10/w12/w50/w13/w8）
            ├─ .tr > .mDetailA[.read]（×5 資料列）
            │   └─ .td.w5>label.cbox>input[name=mainNo] + .td.w2>i + .td.w10.tName + .td.w12.td-status
            │      + .td.w50.td-mail（p.mail-type + bdi + span.badge?） + .td.w13.td-job + .td.w8
            └─ #...PagerDiv.pageBox.DataPager（.DataPagerObj + select.FC）
```

---

## 2. 差異點

> 註：原本只記了 §2.1~2.3 三類並稱「皆非結構破壞性」，實際尚有與正式環境的結構偏離，見 **§2.5**。

### 2.1 資料列內容：替換為 mock data（**結構不變、僅文字值替換**）

- 原檔資料列為真實求職者資料（姓名、履歷編號、訊息全文、職缺名）。
- 本檔將**姓名 / 訊息內容 / 職缺名稱**替換為假資料，**但每一列的 tag、class、層級完全沿用原檔列模板**。
- 列數由原本一頁多筆**精簡為 5 筆**（流程審查需要；正式環境由後端綁定資料來源，不受影響）。
- 每列模板（與原檔相同）：

```html
<div class="tr">
  <div class="mDetailA read">
    <div class="td w5"><label class="cbox"><input name="mainNo" type="checkbox" autocomplete="off"></label></div>
    <div class="td w2  "><i class="far fa-star "></i></div>
    <div class="td w10  tdDetail tName" title="{姓名}">{姓名}</div>
    <div class="td w12  tdDetail td-status ">{狀態 p}</div>
    <div class="td w50 lastMailContent tdDetail td-mail">{類別 p} <bdi>{內容}</bdi>{紅點 span.badge?}</div>
    <div class="td w13 tdDetail td-job " title="{職缺}"><p class="job-content">{職缺}</p></div>
    <div class="td w8 tdDetail">{日期}</div>
  </div>
</div>
```

> ⚠️ **更正（原此處敘述有誤）**：原文宣稱回覆狀態與意願「皆沿用原檔」，**與正式環境不符**。實情如下（詳見 §2.5 D）：
>
> **回覆狀態欄 `.td-status`**
> - 回覆本身沿用原 class：`<p class="reply-content isReply">已回覆</p>` / `<p class="reply-content isNotReply">未回覆</p>`（class 無改名）。
> - 但 mock 的狀態**文字是自填**，非原檔字：mock 寫「求職者未讀」「未回覆\<br\>求職者已讀」，正式環境只有「未回覆」「已回覆」。
> - **意願在正式環境是放在同一欄、用獨立節點** `p.wish-content.isWish` / `p.wish-content.isNoWish`（以 `&nbsp;•&nbsp;` 分隔），例：`已回覆 • 無意願`。**mock 把這組 `wish-content/isWish/isNoWish` 節點刪掉了**。
>
> **意願改用 `.mail-type` inline 上色＝mock 自行改寫，非原檔做法**
> - mock：`<p class="mail-type lastMailTypeName" title="面試邀約" style="color:#1D880D;font-weight:bold;">面試邀約 有意願</p>` / 無意願 `style="color:#FF5D15;…">面試邀約 無意願</p>`（無意願色依需求由 `#BF1212`→`#FF5D15`）。
> - 正式環境的 `.mail-type` **只放類別文字**（例「面試邀約」），**不含**「有意願/無意願」、**也沒有** inline color；意願是上面的 `wish-content` 節點。
> - 先前依需求改「無意願」色時，已同步更新 CSS `.td-status .isNoWish`（正式環境真正使用的 class）為 `#FF5D15`，方向正確；但 mock 畫面上實際變色的是 `.mail-type` 那段 inline 文字（偏離）。

### 2.2 「移除星號」「刪除」按鈕：移除左側 `<i>` icon（**刪節點**）

| 位置 | 原檔 | 本檔 | 性質 |
|---|---|---|---|
| `.deleteBtn > a` | `<a ...><i class="far fa-trash-alt"></i>刪除</a>` | `<a ...>刪除</a>` | 移除 `<i>` 子節點 |
| `.starBtn > a` | `<a ...><i class="far fa-star"></i>移除星號</a>` | `<a ...>移除星號</a>` | 移除 `<i>` 子節點 |

> 需求來源：使用者要求移除這兩顆按鈕左側 icon，按鈕只留文字。
> `.readBtn`（已讀勾選訊息）原本就無 icon，不動。

### 2.3 互動行為：新增 `<script>`（**新增行為，未動既有結構**）

於 `</body>` 前新增一段 vanilla JS，**不依賴原檔任何 framework**，操作對象皆為原檔既有節點：

| 功能 | 觸發 | 操作對象（皆原檔既有節點） |
|---|---|---|
| 表頭全選 / 全不選 | `#checkALL` change | 所有 `input[name="mainNo"]` |
| 半選狀態同步 | 列 checkbox change | `#checkALL.indeterminate` |
| 批次按鈕條件顯示 | 任一 `input[name="mainNo"]` 被勾 | 在 `.actionBtn` 加/移除 class `has-checked` |

> **工程師需注意**：正式環境若已有對應 ASP.NET / jQuery 行為，此段 JS 僅作行為**規格示意**，實作方式由工程師決定。`has-checked` 為新增的 state class（見 CSS 對照 2.7）。

### 2.4 頁籤（tabs）改底線式 Tab：**CSS-only，DOM 零改動**

- 依共用設計系統把頁籤由「膠囊/方塊式」改為「底線式 Tab」（未選灰字、hover 藍字、選中藍字＋4px 藍底線）。
- `ul.tabs > li.tab[.active] ×5` 的標籤、class、巢狀關係**完全沿用原檔**；底線以 `li.active::after` 偽元素達成，**未新增任何節點**。
- 雖約束允許「可搬移 DOM 到別的 div」，本次**未搬移**——純靠 CSS 即可完成。
- 對應樣式見 `02_CSS樣式調整對照.md` B2「頁籤 tabs（底線式 Tab）」。
- **頁籤與篩選「同一便當」亦為純 CSS 視覺合併**：DOM 仍是 `.cont` 內兩個相鄰 sibling（`#bookmark.titleBar` 與 `.whiteBg.filter`），未搬移、未包新節點；合併靠圓角/陰影/z-index 達成（見 02 文件 B2-bis）。
- 表頭列（第一個 `.tr`）上下 padding 調整見 02 文件 A2-bis，亦為純樣式值變更。

### 2.5 與正式環境結構偏離清單（前一手 mock 化時動到，非本輪所為）

> 經與正式環境 `ResumePoolNoticeMail.aspx` HTML 逐行比對得出。**class/tag 名稱無改名/拼錯**（mock 未出現任何正式環境不存在的 class）；以下屬「節點刪除／屬性移除／位置搬移／呈現改寫／新增節點」。本輪僅更正紀錄，**未動 HTML**。

**A. 刪除的節點（連同其 class）**
| 正式環境 | mock | 說明 |
|---|---|---|
| `#UpdatePanel3.Areabox > h1.titleFont`「訊息列表」 | 無 | 整個刪除（唯一被刪的 `h1`）|
| `.td-status` 內 `p.wish-content.isWish` / `.isNoWish`（有意願/無意願） | 無 | 刪除；意願改到 `.mail-type` inline 上色（見 D）|
| `.deleteBtn a > i.far.fa-trash-alt`、`.starBtn a > i.far.fa-star` | 無 | 已記於 §2.2（使用者要求拿掉 icon）|
| 操作指引浮層 `#guidedTour`（`guidedTour-step`/`box-*`/`step-1~4`/`close-step`/`next-step`/`icon-x-mark`…） | 無 | 未納入 mock |
| 分頁「最後頁」`a.leaf.LastBtn`、GoPage 相關節點 | 無/簡化 | 未納入 |
| 多個 `input[type=hidden]`（`HideEmpNo/Name/Role`、`hiducSelectAccount*`、`hidDDLVal`、`hfChooseReadType`）與頁面 `<script>` | 無 | 未納入 mock |

**B. 被移除的屬性（非 class）**
| 元素 | 正式環境屬性 | mock |
|---|---|---|
| 列星號 `.td.w2 > i.far.fa-star` | `data-starno="0"` | 移除 |
| 資料列 `.mDetailA` | `data-mailno/tno/empno/tname/rno/rguid` | 移除 |
| 列 checkbox `input[name=mainNo]` | `value`、`data-tname`、`data-empname`、`data-starno` | 移除 |
| 三顆按鈕 `<a>` | `onclick="delSel()/removeStarSel()/saveReadMail()"` | 移除 |
| `.td-mail` | `data-mailno` | 移除 |

**C. 位置搬移（class/tag 不變，僅位置）**
- `#bookmark.titleBar`（頁籤＋`h1.titleFont`＋`span.msgRecord`）：正式環境在 `.whiteBg.list > .msgList` **內**；mock 搬到 `.cont` **最上層**。
- `.actionBtn`：正式環境在 `.msgList` 內；mock 搬到 `.cont`（filter 與 list 之間）。
- `span.msgRecord`「共N筆」：正式環境在 `#UpdatePanel3.Areabox`（titleBar）內；mock 搬進 `.actionBtn`。
- 頁籤順序：正式 `全部／未讀／已讀／已加星號／有意願`；mock 末兩項對調為 `…／有意願／已加星號`。
- `<li>` class 由 `active tab` 寫成 `tab active`（同樣兩 class、純順序、無影響）。

**D. 呈現方式改寫（意願）**
- 正式環境：`.td-status` 內＝`p.reply-content.isReply/.isNotReply`（回覆）＋ `p.wish-content.isWish/.isNoWish`（意願，`&nbsp;•&nbsp;` 分隔）；`.mail-type` 只放類別。
- mock：`.td-status` 只留 `reply-content`；意願移到 `.td-mail > p.mail-type` 用 inline `style="color:…"` 寫「面試邀約 有意願/無意願」。
- 影響：CSS 已改 `.td-status .isNoWish`＝`#FF5D15`（對到正式 class，正確）；但 mock 畫面實際變色處是 `.mail-type` inline 文字（偏離正式結構）。

**E. mock 新增**
- `.cont` 內多一個空 `.headingBar` 間隔 div（正式環境無）。
- 整份為 standalone 文件（多 `html/head/body/meta/link/title`），供單檔預覽。

---

## 3. 給後續 Agent 的判讀提示

1. ⚠️ **本檔 HTML ≠ 正式環境原結構**（原此處宣稱「它就是原結構」，已更正）。本檔是 mock，與正式環境有 §2.5 所列偏離。要交付工程師的視覺需求＝「**樣式值變更**」（見 `02_CSS樣式調整對照.md`），但**結構面請以正式環境為準**，不要直接照搬本 mock 的 DOM。
2. 產出人類可讀需求時，HTML 面向需描述：
   - (a) 刪除 / 移除星號按鈕**拿掉 icon**；
   - (b) 表頭 checkbox **全選**、列 checkbox **任一勾選才顯示三顆批次按鈕**（互動規格）；
   - (c) **意願**仍應沿用正式環境的 `.td-status > p.wish-content.isWish/.isNoWish`（mock 改成 `.mail-type` inline 上色是偏離，勿沿用）；
   - (d) 其餘結構**維持正式環境原樣**。
3. **class/tag 名稱本來就沒被改名**；正式環境上線時請依 §2.5 還原被刪節點/屬性，不要把 mock 的偏離帶進正式環境。所有視覺調整都應只透過 CSS 值達成。
