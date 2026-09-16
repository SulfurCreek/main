<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

# 信件訊息（ResumePoolNoticeMail）前端修改工程單

版本 v1.0｜2026-07-03｜格式：前端修改工程單（`frontend-change-ticket-1111`）
對應規格：《[4.1 信件訊息列表規格文件](/rJkyKgeGWl)》區塊 1／2.1／2.2／2.3／3（與下圖 badge 一致）
以下「正式環境」＝線上 `ResumePoolNoticeMail.aspx` 現況（P）；「改成」＝目標畫面（A）。CSS 行號皆為隨附 mock 檔 `resumePoolNoticeMail.css`（1706 行版）行號，正式 codebase 請依 selector 對應；找不到既有行號的規則會註明「行號未附，依 selector 對應」。

<img style="max-width:800px" src="https://raw.githubusercontent.com/SulfurCreek/main/0d21e2de5fd4969f479c8efe3884ed09d1f689f2/.claude/assets/resumePoolNoticeMail-before-blocks.png" alt="信件訊息頁 調整前 區塊標號：1 Heading與篩選區、2.1 Tab、2.2 操作列、2.3 下拉篩選選單、3 信件對話">

badge 對照：`1` Heading與篩選區｜`2.1` Tab｜`2.2` 操作列｜`2.3` 下拉篩選選單｜`3` 信件對話。

---

## 1 Heading與篩選區

<img style="max-width:800px" src="https://raw.githubusercontent.com/SulfurCreek/main/ba1076c5937a4ebbcbf812a155b951bdf1d03127/.claude/assets/resumePoolNoticeMail-block-1.png" alt="信件訊息頁 調整前 區塊1 Heading與篩選區：標題＋篩選列">

**HTML 改動**

* 正式環境 `#bookmark.titleBar`（頁籤區塊，內含 `ul.tabs`）現在包在 `.whiteBg.list > .msgList` 裡面，跟 `.whiteBg.filter` 不相鄰。把它整塊搬出來，移到 `.cont` 最上層、緊接在 `.whiteBg.filter` 正上方，讓兩者變成相鄰 sibling（下面的圓角/陰影 CSS 才能合併成同一張卡）。
* 其餘 HTML 不動。

**CSS 改動**

* `.headingBar .Title`（「信件訊息」標題）：新增 `font-family:"Microsoft JhengHei","微軟正黑體","新微軟正黑體",sans-serif; font-weight:500; font-size:28px; line-height:150%; color:#212529`（原 `color:#4e4e4e; font-size:20px`，無指定字重/行高）。改哪：第 1686–1693 行。
* `#bookmark.titleBar`（搬移後的便當上半）：新增 `background:#fff; border-radius:10px 10px 0 0; box-shadow:0 3px 6px rgba(0,0,0,.15); z-index:1`（原無圓角/陰影）。改哪：第 1640–1645 行。
* `.whiteBg.filter`（便當下半）：改 `border-radius:0 0 10px 10px; margin-top:0; z-index:2`（原四角 `10px`）。改哪：第 1647–1650 行。
* 篩選欄位邊框統一：`#EmpInput.jobList`（職缺）、`.LMDateSet .start`/`.end`（日期）、`#txtSearchKeyWord.searchName`（關鍵字）、`#btnSearch.btnSch`（搜尋鈕）套用同一組規則——預設 `border:1px solid #ccc; border-radius:4px; box-shadow:none; transition:border-color .15s`，hover `border-color:#9aa7b2`，focus `outline:none; border-color:#4f6b92`。改哪：預設第 1442 行起、hover 第 1467 行、focus 第 1477 行；`.searchName` 右側去邊框圓角另改第 1448 行；`.btnSch` 左直角右 `4px` 另改第 1452 行；`.LMDateSet` 內部兩個 `input` 改 `border:none` 另改第 1457 行。
* 文字放大為 `16px`（原 13/14/15px 不等）：`.headingBar .LMInstruct`、`.filterBox .LMVacancies`、`.filterBox input`/`.jobList`/`.searchName`/`.start`/`.end`/`.btnSch`。改哪：第 1529 行起。

---

## 2.1 Tab

<img style="max-width:800px" src="https://raw.githubusercontent.com/SulfurCreek/main/ba1076c5937a4ebbcbf812a155b951bdf1d03127/.claude/assets/resumePoolNoticeMail-block-2_1.png" alt="信件訊息頁 調整前 區塊2.1 Tab：訊息列表頁籤（全部/未讀/已讀/已加星號/有意願）">

**HTML 改動**

* 正式環境 `#bookmark.titleBar > #UpdatePanel3.Areabox` 內有 `h1.titleFont`「訊息列表」子標題：建議刪除，跟 1 區的頁面主標「信件訊息」重複，設計稿未再顯示這行字。
* `span.msgRecord`「共 N 筆」目前也在這個 `Areabox` 內：搬到 `.actionBtn` 操作列（見 [2.2](#22-操作列)），放最前面。
* `ul.tabs > li.tab` ×5 標籤與巢狀關係不變；底線用 `li.active::after` 偽元素做，不新增節點。
* 頁籤順序維持正式環境規格順序（全部／未讀／已讀／已加星號／有意願），不要照 mock 把最後兩項對調。

**CSS 改動**

* `.tabs`：改 `display:flex; justify-content:flex-start; align-items:stretch; gap:32px; list-style:none; margin:0; padding:16px 32px 0; border-bottom:1px solid #e9ecef`（原 `justify-content:center; align-items:flex-end` 的膠囊式頁籤）。改哪：第 1634–1678 行（容器第 1652 行）。
* `.tabs .tab`（預設）：`position:relative; margin:0; padding:8px 0 16px 0; background:none; border:none; border-radius:0; color:#212529; font-size:16px; font-weight:400; line-height:1.55; cursor:pointer`。改哪：第 1661 行。
* `.tabs .tab:hover`：`color:#1a66ff`（無底線、字重不變）。改哪：第 1669 行。
* `.tabs .tab.active`：`color:#1a66ff; font-weight:500; background:none; border:none`。改哪：第 1670 行。
* `.tabs .tab.active::after`：新增 `content:""; position:absolute; left:0; right:0; bottom:0; height:4px; background:#1a66ff; border-radius:80px 80px 0 0`。改哪：第 1674 行。
* 舊膠囊規則（第 1067–1106 行）與像素取樣覆蓋（第 1362、1364、1402–1416、1504、1529 行）、本次覆蓋用的 `!important`，正式整併時可一併刪除。

---

## 2.2 操作列

<img style="max-width:520px" src="https://raw.githubusercontent.com/SulfurCreek/main/ba1076c5937a4ebbcbf812a155b951bdf1d03127/.claude/assets/resumePoolNoticeMail-block-2_2.png" alt="信件訊息頁 調整前 區塊2.2 操作列：刪除/移除星號/已讀勾選訊息/查看其他帳號">

**HTML 改動**

* 正式環境 `.actionBtn` 目前包在 `.msgList` 裡面：搬出來，移到 `.whiteBg.filter` 跟 `.whiteBg.list` 中間，變成獨立一列。
* `span.msgRecord`「共 N 筆」從頁籤區塊（見 [2.1](#21-tab)）搬進來，放在 `.actionBtn` 最前面。
* `.deleteBtn > a` 內的 `<i class="far fa-trash-alt">` 拿掉，按鈕只留文字「刪除」。
* `.starBtn > a` 內的 `<i class="far fa-star">` 拿掉，按鈕只留文字「移除星號」。
* `.readBtn > a` 本來就沒有 icon，不用動。
* 新增互動行為（vanilla JS 或既有 ASP.NET/jQuery 機制皆可，這裡只規定行為）：表頭 `#checkALL` 變動時，同步所有 `input[name="mainNo"]` 全選/全不選；任一列 `input[name="mainNo"]` 變動時，同步 `#checkALL` 的半選狀態（`indeterminate`）；只要有任一列被勾選，就在 `.actionBtn` 加上 class `has-checked`（沒有勾選則移除），控制下面三顆按鈕顯示/隱藏。

**CSS 改動**

* 三顆按鈕 `.deleteBtn a`/`.starBtn a`/`.readBtn a`：改 `width:auto; padding:0 14px; display:inline-flex; align-items:center; justify-content:center; height:25px; line-height:1`（原固定寬 `80px`/`110px`、用 `line-height:25px` 置中）。改哪：第 1508–1517、1619 行。
* 三顆按鈕預設 `display:none`；`.actionBtn.has-checked` 底下改 `display:inline-flex; align-items:center`（勾選任一列才顯示）。改哪：第 1628 行（預設隱藏）、第 1631 行（勾選顯示）。
* 三顆按鈕顏色維持原值不變：刪除 `#e25656`（hover `#FFEAEB`）、星號/已讀 `#199ed8`（hover `#e9f8ff`）。
* `span.msgRecord`：新增 `font-family:"Microsoft JhengHei","微軟正黑體","新微軟正黑體",sans-serif; font-weight:400; font-size:16px; line-height:155%; color:#495057; display:inline-flex; align-items:center`（原 `14px`、色繼承）。改哪：第 1696–1705 行。
* `.actionBtn`：`justify-content:flex-start`（原 `space-between`）。改哪：行號未附，依 selector 對應（來源：02 對照表 B3）。
* `.actionBtn .msgRecord` margin：`7px 12px 7px 0`（原 inline `7px 10px`）；`.actionBtn #rPoolMail` 新增 `margin-left:8px`；`.actionBtn .LMType` 新增 `margin:0 8px 0 0`。改哪：行號未附，依 selector 對應（來源：02 對照表 B3）。
* `#txtChooseUNOs.otherAcc`（查看其他帳號）套用 1 區同款輸入框邊框：預設/hover/focus 同第 1442/1467/1477 行。
* `.actionBtn` 本身、三顆按鈕 `a`、`.otherAcc`、`.LMType select`、`.seekerWillStatus select` 維持原字級 `14px`，**不要**跟著 [3](#3-信件對話-by-職缺求職者) 的文字放大一起改成 `16px`（`msgRecord` 例外，已在上面改 `16px`）。

---

## 2.3 下拉篩選選單

<img style="max-width:380px" src="https://raw.githubusercontent.com/SulfurCreek/main/ba1076c5937a4ebbcbf812a155b951bdf1d03127/.claude/assets/resumePoolNoticeMail-block-2_3.png" alt="信件訊息頁 調整前 區塊2.3 下拉篩選選單：信件類別/求職者回覆">

**HTML 改動**

* 不用動。

**CSS 改動**

* `#ddlMailType`（信件類別下拉）、`#ddlReaded`（求職者回覆下拉）套用跟 1 區同款輸入框邊框：預設 `border:1px solid #ccc; border-radius:4px; box-shadow:none; transition:border-color .15s`，hover `border-color:#9aa7b2`，focus `outline:none; border-color:#4f6b92`。改哪：第 1442/1467/1477 行（跟 1 區共用同一組規則）。
* 兩個下拉維持原字級 `14px`，不放大。
* 下拉本身的篩選邏輯與選項值（信件類別 value、面試類別、求職者回覆 value）不在本次視覺需求範圍，沿用規格 2.3.1～2.3.3。

---

## 3 信件對話 by 職缺&求職者

<img style="max-width:800px" src="https://raw.githubusercontent.com/SulfurCreek/main/ba1076c5937a4ebbcbf812a155b951bdf1d03127/.claude/assets/resumePoolNoticeMail-block-3.png" alt="信件訊息頁 調整前 區塊3 信件對話：表頭與資料列">

**HTML 改動**

* `.whiteBg.list` 這張卡片，把原本包住的 `#bookmark.titleBar`（見 2.1）跟 `.actionBtn`（見 2.2）都搬走後，現在只剩 `.msgTable`，結構不變。
* 意願呈現沿用正式環境既有結構，**不要改**：`.td-status` 內是 `p.reply-content.isReply`/`.isNotReply`（回覆）＋ `p.wish-content.isWish`/`.isNoWish`（意願），中間用 `&nbsp;•&nbsp;` 分隔（例：`已回覆 • 無意願`）；`p.mail-type` 只放類別文字（如「面試邀約」），不要把意願文字或顏色塞進 `.mail-type` 的 inline style。
* 星號 icon（`.td.w2 > i.far.fa-star`）本次無視覺調整，維持原樣。
* 其餘資料列標籤/class/`data-*` 屬性維持正式環境原樣，不用比照任何精簡版 mock 拿掉。

**CSS 改動**

* `.whiteBg.list` padding：`0 0 20px 0`（原 `20px 24px 20px 24px`）——上面跟左右貼齊卡片邊，只留下方 `20px`。改哪：第 1428 行。
* `.whiteBg` margin-bottom：`0`（原 `20px`）。改哪：第 1565 行。
* `.msgTable .thead .tr`：底色 `#E3ECFD`（原 `#e5eaf3`）、新增文字色 `#0D2760`（配合各 `.th` 既有 `font-weight:bold`）。改哪：第 1388 行。
* `.msgTable .thead .tr .th` 上下 padding：`12px`（原 `10px`，左右維持 `15px`）。改哪：第 1682–1683 行。
* `.msgTable .thead .tr` 頂角：新增 `border-radius:10px 10px 0 0`（配合卡片圓角，銜接上面的 padding 調整）。改哪：第 1429 行。
* `.msgTable .tr .mDetailA:hover`：改 `box-shadow:none; background:#FFF7F7; cursor:pointer`（原左右內陰影＋外陰影邊框＋`z-index:2`）。改哪：第 921–927 行（直接改原始 `:hover` 規則）。
* `.msgTable .td-status .isNoWish`（無意願）：`color:#FF5D15`（原 `#BF1212`，依規格 3.3 調整）；`.isWish`（有意願）維持 `#1D880D`。改哪：第 983 行／第 980 行。未讀紅點 `--State-warning #BF1212`（badge）語意不同，不更動。
* `.msgTable .td-mail bdi` padding：`2px 0 0 0`（原 `3px 0 0 0`）。改哪：第 1386 行。
* `.msgTable .td-mail .badge`（未讀紅點）：`10px × 10px`（原 `6px × 6px`）。改哪：第 1496 行。
* `.td-mail:has(.badge) .mail-type, bdi` 內文寬：`max-width:calc(100% - 12px - 18px - 10px)`（原扣 `6px`，配合紅點變大保留寬度）。改哪：第 1497 行。
* `.msgTable p`（`.mail-type`／`.wish-content`／`.reply-content`／`.job-content` 共用）：`margin:0`（清掉瀏覽器預設 `16px 0`）。改哪：第 1596 行。
* 文字放大為 `16px`（原 13/14/15px 不等）：`.msgTable .thead .tr`、`.tName`、`.td-status .reply-content`、`.mail-type`、`.td-mail bdi`、`.job-content`、`.td.w8`（日期）、`.pageBox.DataPager` 及其 `a`/`.Currect`/`.dataPagerText`/`select`/`input`。改哪：第 1529 行起。`.td-status .sub-read`（求職者已讀）維持次要層級 `14px`，不隨上面放大。

---

## 不需處理（mock 精簡產物，正式環境不用比照）

* `body{background:#f0f0f0}`、欄寬 `.w2`/`.w5`/…／`.w50{flex:1}`：mock 補值（正式環境由外層 layout／`boxPage.css` 已提供）。
* FontAwesome CDN `@font-face`、三顆按鈕/星號/清除/箭頭等 inline SVG、`.icon-bulb` SVG：離線預覽替身，正式環境用站台原資產。
* `data-*`/`onclick` 屬性、隱藏欄位（`input[type=hidden]`）、操作指引浮層 `#guidedTour`：mock 為離線預覽精簡掉，正式環境維持原樣即可。
