# HTML 結構調整對照表（ResumePoolNoticeMail 信件訊息頁）

> 本文件供後續 AI agent / 前端工程師理解「相對於原始頁面 HTML」做了哪些**結構與標籤層級**的調整。
> 原則：**DOM 結構與既有 class / tag 名稱完全沿用原檔，不新增、不改名、不刪除既有節點。** 僅有的差異是「資料替換為 mock」「補回原本就存在但渲染不出的節點」與「新增行為用 JS」。

---

## 0. 對照基準

| 項目 | 說明 |
|---|---|
| 原始頁面 | 1111 recruit 企業端 `ResumePoolNoticeMail.aspx`（信件訊息列表） |
| 對照檔 | `ResumePoolNoticeMail.html`（本次產出） |
| DOM 層級 | `.content > .cont > [.headingBar, #bookmark.titleBar, .whiteBg.filter, .actionBtn, .headingBar(空), .whiteBg.list]` |
| 結論 | **結構零改動**；僅資料 mock 化、補 inline SVG 圖示替身、加入互動 JS |

---

## 1. 結構層級：完全沿用，未改動

下列節點的標籤名稱、class、巢狀關係與原檔**逐一相同**，工程師端**不需要任何 HTML 變更**：

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

## 2. 差異點（共 3 類，皆非結構破壞性）

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

> **工程師需注意**：求職者回覆欄（`.td-status`）有三種狀態文字結構，皆沿用原檔：
> - 已回覆：`<p class="reply-content isReply" title="已回覆">已回覆</p>`
> - 未讀：`<p class="reply-content isNotReply" title="未回覆">求職者未讀</p>`
> - 已讀未回覆：`<p class="reply-content isNotReply" title="未回覆">未回覆<br>求職者已讀</p>`
>
> 信件類別（`.td-mail > p.mail-type`）有意願/無意願時，沿用原檔 **inline style 上色**：
> - 有意願：`<p class="mail-type lastMailTypeName" title="面試邀約" style="color:#1D880D;font-weight:bold;">面試邀約 有意願</p>`
> - 無意願：`... style="color:#BF1212;font-weight:bold;">面試邀約 無意願</p>`

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

---

## 3. 給後續 Agent 的判讀提示

1. **本檔 HTML 不應被當成「要套用的新結構」**——它就是原結構。真正要交付給工程師的是「**樣式值變更**」（見 `02_CSS樣式調整對照.md`）與本檔列出的 3 個結構差異。
2. 產出人類可讀需求時，HTML 面向只需描述三件事：
   - (a) 刪除 / 移除星號按鈕**拿掉 icon**；
   - (b) 表頭 checkbox **全選**、列 checkbox **任一勾選才顯示三顆批次按鈕**（互動規格）；
   - (c) 其餘 HTML **維持原樣**。
3. 不要要求工程師改動 class 名稱或 DOM 階層——所有視覺調整都能、且應該、只透過 CSS 值達成。
