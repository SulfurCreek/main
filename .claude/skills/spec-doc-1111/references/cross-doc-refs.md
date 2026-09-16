# 跨文件引用與嵌入（三層方式）

> 屬 `spec-doc-1111` skill 的參考檔。**需要連結或嵌入其他 note 時才讀**。

引用既有文件時依「讀者需要看多深」選擇：

### 1️⃣ 行內連結 — 讀者只需要知道去哪看

相對 note 路徑連結，用在權限表、入口頁、其他功能文件：

```markdown
| 權限條件 | 代碼 [求才系統代碼表](/B1j3sN-bzx) | 不符合時的處理 |
* [信件列表](/uoldEfXhT9KrbGxQJwg4ew) 訊息列表點擊任一對話
* 點擊外開分頁前往[封鎖名單](/I3yns2xqQiuwVIEfEHAxhw)
```

### 2️⃣ iframe 開啟現版功能 — 沿用現版 lightbox 時

說明點擊行為 + **iframe 尺寸** + **帶入參數**，並連結該 lightbox 的規格文件：

```markdown
* **訊息來往紀錄**：
  * 點擊後，以iframe方式開啟現版 [紀錄管理Lightbox](https://hackmd.io/@1111-jobdocs/Sk4AvcZ-We)
    * iframe尺寸：800x680
    * 帶`求職者姓名`、`tNO`、`oNo`
    * landing在`信件紀錄管理`
```

### 3️⃣ 全文嵌入 — 讓讀者不離開本文即可展開閱讀引用文件

`{%hackmd <noteId> %}` 嵌入語法，包在 `:::spoiler` 內、外層 `<div style="padding-left:50px">` 縮排。
**緊跟在 2️⃣ 的 iframe 說明之後**，作為該 lightbox 規格的就地參照：

```markdown
<div style="padding-left:50px">

:::spoiler 紀錄管理Lightbox

{%hackmd Sk4AvcZ-We %}

:::

</div>
```

> 引用舊版規格的特定章節時，連結文字註明版本與章節：`（舊版 [4.1 v1.0.1／§4.3](/r1ghrPxP-x)）`。
