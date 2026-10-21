---
name: polish-104
description: 潤飾 Career Move 產出的 104 特化版草稿（drafts/<版本>/104-<版本>.md）的文字，產出可交給填表 agent 的潤飾稿。只改文字，不改事實、數字、欄位路徑與 HTML 樣式。觸發：「潤飾 104」「104 特化版」「104-v11」。
---

<!--markdownlint-disable MD013-->

# polish-104：104 特化版草稿潤飾

> 維護者：Career Move（Claude）。使用者：Resume Writer（Codex）。本檔放在 `career/` 內是因為 Codex 只讀 `career/`。

## 1. 輸入與輸出

| 項目 | 位置 |
| :-- | :-- |
| 草稿（唯讀） | `origin/claude/happy-lamport-ljis8c` 的 `career/drafts/<版本>/104-<版本>.md`；開頭會標「草稿，待 Resume Writer（Codex）潤飾」與**未潤飾段落清單** |
| 事實來源（唯讀） | `career/library/`：先讀 `INDEX.md`、`decisions.md`（§1–§4、§20）、`superseded.md`；疑問查 `fact-snapshot-2026-10-13.md`、`facts-1111.md`、`facts-prior.md` |
| 格式規格（唯讀） | `career/104/content-spec-quill.md`（**範例文字只取格式，不取事實**）、`career/104/fields-spec.md`（字數上限） |
| 語氣 | `career/style/resume-voice-zh.md`、`career/library/about-me.md`（編輯參考，不給驗證者） |
| 輸出 | `career/drafts/codex/104-<版本>-polished.md`（**整份**，結構與草稿相同）＋同檔末尾〈修改紀錄〉 |
| 事實疑問 | `career/drafts/codex/QUESTIONS.md` |

讀草稿：`git fetch origin claude/happy-lamport-ljis8c && git show origin/claude/happy-lamport-ljis8c:career/drafts/v11/104-v11.md`

## 2. 可以改／不能改

| 可以 | 不能 |
| :-- | :-- |
| 語序、斷句、用字、連接詞，讓陌生讀者左到右、上到下讀得懂 | 新增或刪除事實、數字、日期、人數、功能名、產品名 |
| 把同一句拆成兩句或合併 | 改 `▼ 欄位路徑`、欄位順序、〔待補〕、管理責任欄 |
| 調整小標文字（`<strong>…</strong>` 內） | 改 HTML 標籤與樣式（`blockquote`、`ql-size-large`、`#00afb8`、`#fbf3db`、`ql-divider`、`small`） |
| 螢光標記移到更準確的數字上 | 加螢光到非數字的形容詞；新增螢光數字 |
| 精簡贅字 | 為了變短刪掉動機、轉折、限定詞（例如「上線與導流期間」「依公司公開資料」「非個人單獨成果」） |

**兩種任務，先判斷是哪一種**：
- **一般潤飾**：只修用字、語序與斷句，不新增或刪除事實；未潤飾段落優先，已沿用投遞正文的段落只修明顯不順處。
- **本人明確要求重新整理／重寫指定欄位**：可在該欄位重新選材與安排結構，交代刪留理由與限定；其他欄位維持一般潤飾範圍。不授權改寫 library 事實。
- 個人簡介與頂部個人特色依 `career/104/content-spec-quill.md` §5。
- 選稿標準是閱讀清楚、事實完整、定位合適；**不用模型分數或 Level 選稿**（舊二十版本評分流程不再執行）。

## 3. 禁止事項（防倒退）

- 不寫：Spearheaded／主導開發／架構、#1／第一大（只能「依公司公開資料…暢銷榜第一」）、3 週上線、千萬營收、承接率、效率提升 %、申訴率 %、每兩週 Sprint、Jira、Confluence、SQL 能力。
- 「商家」不寫「案主／業主」；外籍實習生是協作對象，不是下屬；1111 是「2 名直屬產品企劃」。
- 金流：Peach／JustDating 台灣＝智冠；JustDating 含 Juicy 台灣以外＝CodaPay；思維特 CodaPay＝印尼、泰國等。
- 不出現同事姓名、內部系統名、API／欄位名。
- 有疑問不要猜：寫進 `QUESTIONS.md`，正文維持草稿原句。

## 4. 字數上限（純文字，去 HTML 計）

自述 ≤300｜經歷每段 ≤1500｜專長名 ≤15、desc 100–200｜專案名 ≤30、說明 ≤2000｜中文自傳 ≤4000。

## 5. 交付前自檢

1. 用 `diff` 比對草稿與潤飾稿：每處差異只動文字，沒有動到數字、日期、欄位路徑、標籤。
2. 第 3 節禁止詞全文搜尋為 0。
3. 字數全在第 4 節範圍內。
4. 檔末〈修改紀錄〉：逐段一行「改了什麼、為什麼」，以及寫進 QUESTIONS.md 的題號。
5. commit 前綴 `career:`，推 `codex/resume-writer`。完成後告訴使用者檔名，由使用者轉給 Career Move 核對。
