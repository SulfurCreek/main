<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

# 樣式與符號慣例 ・ 表格 ・ 條件邏輯

> 回 [`../SKILL.md`](../SKILL.md)。

## 紅字：新需求／本版變更

新增或修改的需求整段用紅字包起來，版控紀錄的「調整說明」要寫明異動區段：

```markdown
* <font style="color:red">**1-2-2 下期合約可暫停天數** `useDeadline`-`deadline_open`</font>
```

標題也可整行標紅：`##### <font style="color:red">2-1-1 預計開權時間`
（紅字 `<font>` 可跨多個條列，於段落結尾再 `</font>`）。

## 欄位、旗標、狀態值：反引號

所有程式可辨識的值都用反引號，避免與說明文字混淆：

- 旗標位元運算：`organs.confirmed&131072`、`organs.showfield&4096`、`organsMore:setKind&16`
- 狀態值：`oStatus:1`、`oStatus:3`、`iskeepemployeesstatus:true`
- 權限代碼：`代碼9`、`權限代碼26`、`權限代碼27`、`（46）`
- 廠商狀態集合：`status = 0,2,4,5,6`
- 計算式：`合約結束日`-`今日日期`、`useDeadline-今天`

## 版控紀錄調整說明格式

每次發布必須在版控表新增一列，格式：`[異動區段] 說明內容`

- ✗ 不可只寫：「更新文件」
- ✓ 應寫：「[進入畫面權限判斷] 新增 `confirmed&131072` 外網限制，整合為權限判斷表格」
- ✓ 應寫：「[1-1-2 可暫停天數] 補充 2077/7/7 無限期顯示邏輯」

## 圖片

- 來源兩種皆可：HackMD `_uploads`（手動拖入）或 GitHub raw URL（repo `.claude/assets/` 下，URL 帶 commit SHA）
- 全寬示意圖：`![image](https://hackmd.io/_uploads/xxxx.png)`
- 限寬內嵌圖兩種寫法：
  - `<div style="max-width:375px">![image](...)</div>`（markdown 圖包 div）
  - `<img style="max-width:600px" src="..." alt="{章節編號＋元件說明}">`（GitHub raw 圖用 img tag，**必加 alt**）
- 常見寬度：選單 `200px`、手機版 `375px`、空狀態／lightbox `500px`、聊天室全景 `600px`、列表 `800px`、tooltip `300px`

## 摺疊區塊

- 大段補充（判斷邏輯、流程圖）：`:::spoiler {標題}` … `:::`
- 行內小補充：`<details><summary>{摘要}</summary>{內容}</details>`
- 需要縮排的 spoiler 可包在 `<div style="padding-left:50px">` 內

## 跨文件／錨點連結

- 連到同文件章節：`[1.1 篩選 Tab](#1.1-篩選-Tab)`（錨點為編號＋標題去空白）
- 連到另一份 HackMD 規格：`[信件列表](/uoldEfXhT9KrbGxQJwg4ew)`（**相對 note 路徑**，不用完整 URL）

---

## 表格慣例：欄位／列定義表

描述列表每一列要顯示什麼，用兩欄表格，左欄欄位名、右欄行為；多條件用儲存格內 `<ul><li>`：

```markdown
|每筆排程顯示為一個row|滑鼠進入時，顯示為hover樣式|
|---|--|
|操作時間|操作時寫入log的文字|
|操作人員|操作的帳號姓名（若為內網操作，則顯示為`客服人員`）|
|狀態|判斷機制為：`排程時間 - 當下時間`<br><ul><li>尚未執行的排程顯示`待執行`</li><li>已執行的排程顯示：`已執行`</li></ul>|
```

儲存格內換行用 `<br>`，多層判斷用 `<ul><li>…<ul><li>…</li></ul></li></ul>` 巢狀。
狀態相關欄位若受廠商狀態影響，**把廠商狀態判斷寫在最前**（優先於時間／其他判斷），
例如「`status = 0,2,4,5,6` 時固定 disabled，其餘狀態才往下判斷」。

---

## 條件邏輯的寫法

用巢狀條列描述「判斷 → 結果」。**每層縮排必須用兩個空格**（不是一個空格或 Tab）：

```markdown
* 判斷登入帳號權限：
  * 有線上續約權限（46）時：
    * 顯示加入VIP按鈕
    * 點擊後前往`vipContractOther.aspx`
  * 無權限時：
    * 固定顯示文字
    * 不顯示按鈕
```

慣用句型：`判斷{對象}{狀態}時`、`當{條件}時，顯示為{default／disabled／Error}樣式`、`點擊後{行為}`、
`寫入操作紀錄：{log 文字}`。

樣式術語固定用：`default 樣式（黑色）`、`Error 樣式（紅色）`、`disabled 樣式`、`hover 樣式`、
`selected 狀態`、`toast`、`alert modal`、`tooltip`。
