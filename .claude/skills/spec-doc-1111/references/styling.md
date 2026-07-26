# 樣式與符號慣例

> 屬 `spec-doc-1111` skill 的參考檔。**查特定樣式寫法時才讀**（紅字、反引號、圖片、摺疊區塊、錨點連結、版控調整說明格式）。

### 紅字：新需求／本版變更

新增或修改的需求，整段用紅字包起來，版控紀錄的「調整說明」要寫明異動區段：

```markdown
* <font style="color:red">**1-2-2 下期合約可暫停天數** `useDeadline`-`deadline_open`</font>
```

標題也可整行標紅：`##### <font style="color:red">2-1-1 預計開權時間`（紅字 `<font>` 可跨多個條列，於段落結尾再 `</font>`）。

### 欄位、旗標、狀態值：反引號

所有程式可辨識的值都用反引號，避免與說明文字混淆：

- 旗標位元運算：`organs.confirmed&131072`、`organs.showfield&4096`、`organsMore:setKind&16`
- 狀態值：`oStatus:1`、`oStatus:3`、`iskeepemployeesstatus:true`
- 權限代碼：`代碼9`、`權限代碼26`、`權限代碼27`、`（46）`
- 廠商狀態集合：`status = 0,2,4,5,6`
- 計算式：`合約結束日`-`今日日期`、`useDeadline-今天`

### 版控紀錄調整說明格式

每次發布必須在版控表新增一列，**調整說明格式**：`[異動區段] 說明內容`

- ✗ 不可只寫：「更新文件」
- ✓ 應寫：「[進入畫面權限判斷] 新增 `confirmed&131072` 外網限制，整合為權限判斷表格」
- ✓ 應寫：「[1-1-2 可暫停天數] 補充 2077/7/7 無限期顯示邏輯」

### 圖片

- 圖片來源兩種皆可：HackMD `_uploads`（手動拖入）或 GitHub raw URL（repo `.claude/assets/` 下，URL 帶 commit SHA）
- 全寬示意圖：`![image](https://hackmd.io/_uploads/xxxx.png)`
- 限寬內嵌圖兩種寫法：
  - `<div style="max-width:375px">![image](...)</div>`（markdown 圖包 div）
  - `<img style="max-width:600px" src="..." alt="{章節編號＋元件說明}">`（GitHub raw 圖用 img tag，**必加 alt** 描述對應章節）
- 常見寬度：選單 `200px`、手機版 `375px`、空狀態／lightbox `500px`、聊天室全景 `600px`、列表 `800px`、tooltip `300px`

### 摺疊區塊

- 大段補充（如判斷邏輯、流程圖）：`:::spoiler {標題}` ... `:::`
- 行內小補充：`<details><summary>{摘要}</summary>{內容}</details>`
- 需要縮排的 spoiler 可包在 `<div style="padding-left:50px">` 內

### 跨文件／錨點連結

- 連到同文件章節：`[1.1 篩選 Tab](#1.1-篩選-Tab)`（錨點為編號＋標題去空白）
- 連到另一份 HackMD 規格：`[信件列表](/uoldEfXhT9KrbGxQJwg4ew)`（**相對 note 路徑**，不用完整 URL）
