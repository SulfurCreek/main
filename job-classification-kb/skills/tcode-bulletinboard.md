# Skill：tCode 異動清單／公告產出（tcode-bulletinboard）

> 引用來源：`tcode/01-schema.md`、`tcode/02-analysis-recipes.md` 早就提到「比對兩版 export、產生異動清單、發系統公告的流程，使用 `tcode-bulletinboard` skill」，但這個 skill 檔案一直沒被建立——本檔補上，格式依使用者提供的既有公告範例（Certify／WorkAbility／DutyPT 公告）逆推而來。

## 時機

使用者要「公告」「異動清單」「新增/改名項目整理」時用本 skill，不要自由發揮格式。

## 鐵則

1. **輸出目的地＝聊天訊息本身**。不產生 `.md`／`.html` 檔案、不用 Artifact 渲染、不 commit 進 repo，除非使用者另外明確要求「存檔」「寫進repo」「做成頁面」。
2. **按表分節，不跨表合併**：每張 tCode 表（Certify／WorkAbility／DutyNM／DutyPT／DutyST／DutyHL…）各自一個大節，用中文數字（一、二、三…）編號，標題「{編號}、{中文表名}（{英文表名}）」。
3. **節內再依異動類型分小節**：`🆕 新增分類`、`🆕 新增項目`；若該表本次也有改名，比照新增的結構用 `✏️ 改名項目`（見下方「改名項目擴充」）。**不要用 ADD/EDIT 這種代碼字樣**，公告面向的是人看的中文標籤。
4. **新增項目一律按「類別」分組**，同一類別底下的新增項目用「、」串成一行，不要每個新增項目各佔一列。
5. 每個小節標題括號內註明筆數，如「🆕 新增項目（143 項）」——筆數＝該小節列出的**項目總數**，不是分組數。
6. 若某張表在這批異動裡完全沒有新增分類（只有新增項目，沒新的中類/大類），就省略「🆕 新增分類」小節，直接接「🆕 新增項目」。

## Duty 系列表名對照（公告一律用中文人話名，不用代碼）

| 代碼 | 公告用名 |
|---|---|
| tCodeDutyNM | 全職 |
| tCodeDutyPT | 兼職 |
| tCodeDutyST | 工讀 |
| tCodeDutyHL | 中高階 |

四表**各自獨立成一節**（一、全職　二、兼職　三、工讀　四、中高階），不可合併成一節帶括號列代碼。

## 標準格式範本

```
一、{表中文名}（{表英文名}）

🆕 新增分類（{N} 個）

| 新增分類 |
|---|
| {新分類A}、{新分類B}、{新分類C}… |

🆕 新增項目（{M} 項）

| 類別 | 新增項目 |
|---|---|
| {類別1} | {項目a}、{項目b}、{項目c}… |
| {類別2} | {項目d}、{項目e}… |
```

若該表本次也有改名，在新增項目之後加一節（改名項目擴充）：

```
✏️ 改名項目（{K} 項）

| 類別 | 項目（原名稱→新名稱） |
|---|---|
| {類別1} | {原名A}→{新名A}、{原名B}→{新名B} |
```

> 中類/大類本身被改名（不是葉節點改名）時，該列項目直接寫「{原中類名}→{新中類名}」，類別欄位可留該中類所屬的上一層（大類），或註明「（中類層級）」。

## 範例（使用者提供的既有公告，逐字保留作為對照基準）

```
一、證照（Certify）

🆕 新增分類（4 個）

新增分類
TIPCI 臺灣國際專業認證學會、ICDL Foundation／財團法人電腦技能基金會（CSF）、HashiCorp、CNCF

🆕 新增項目（143 項）

類別	新增項目
MICROSOFT	Microsoft Certified: Power Platform Fundamentals、Security, Compliance, and Identity Fundamentals、Azure Data Scientist Associate
...

二、工作技能（WorkAbility）

🆕 新增分類（1 個）

新增分類
金融行政業務

🆕 新增項目（75 項）

類別	新增項目
專案管理	溫室氣體盤查、產品碳足跡盤查
...

三、兼職職務（DutyPT）
🆕 新增項目（5 項）

類別	新增項目
教育師資	英語教師、日語教師、韓語教師、其他語系教師、華語教師
```

（DutyPT 這節示範了「該表沒有新增分類」的情況：直接省略 `🆕 新增分類`，只留 `🆕 新增項目`。）

## 資料來源鐵則：ChangeType 只是「指標」，不是「證據」

**慘痛教訓**（實例：ChangeType 為 edit/add 的項目公告，第一版做錯了）：只憑「修改需求文件」（使用者持續在編輯的 Google Sheet）自己的 `ChangeType` 欄位＋自己當下的 `CodeNameA`/`CodeNameB`，或是拿專案裡任何一份舊 baseline（如 `TCode_Export.xlsx`、之前手動整理的異動清單）去跟它比對，**都不足以判定真的改了什麼**。原因：

1. `ChangeType` 常常「掛著沒清」——一筆之前為了別的原因（例如補 `CodeAlike` 相似詞）被標成 `edit`，但 `CodeNameA`／`CodeNameB` 其實從未變動；直接拿 ChangeType=edit 的清單去發公告，會生出一堆「原名稱→新名稱」兩邊寫得一模一樣的假異動。
2. 用來對照的 baseline 版本不對，也會生出反方向或無關的假異動（例如把「這次要新增的代碼」誤判成「原本不存在」）。

**正確做法**：使用者會提供三份**各自獨立**的檔案／連結，缺一不可：

| 檔案 | 角色 | 怎麼用 |
|---|---|---|
| 修改需求文件 | 這一輪異動的「索引」，`ChangeType` 欄位標記哪些 CodeNo 這輪有動 | 只拿它篩「候選列」（`ChangeType` in `edit`/`add`），**不要**信它自己的 CodeNameA/CodeNameB |
| 修改前檔案 | 真正的「舊」內容 | 依候選列的 CodeNo 查這份檔案的 CodeNameA/CodeNameB/CodeNameC，當作「原本」 |
| 修改後檔案 | 真正的「新」內容 | 依候選列的 CodeNo 查這份檔案的 CodeNameA/CodeNameB/CodeNameC，當作「改成」 |

流程：① 用需求文件篩出 `ChangeType` 為 `edit`/`add` 的 CodeNo；② 對每個 CodeNo 分別去「修改前」「修改後」兩份檔案各查一次 CodeNameA/CodeNameB/CodeNameC；③ **逐欄比較前後兩份檔案的值**（不是需求文件本身的值）——完全相同的直接排除（噪音標記，不進公告），只有 A/B/C 任一欄真的不同才算數；④ 前後皆有但 A 不同＝改名，B/C 不同但 A 相同＝中類／大類調整，前面查不到（`None`）但後面有＝真新增。

**技術細節**：xlsx 讀出來的 CodeNo 常是 `float`（如 `1006.0`），需求文件的 CSV 是字串（`"1006"`）——比對前先正規化成同一型別（如 `str(int(float(x)))`），不然會全部對不上、誤判成「查無此代碼」。

## 與其他文件的關係

- 各表現況資料：`tcode/data_*.md`
- 逐表 ChangeType 清單（本 skill 的資料來源）：`tcode/data_tCodeDuty_changetype_sync.md`、`tcode/data_tCodeDutyNM_changes.md`
- 全表結構/欄位定義：`tcode/01-schema.md`
