# 履歷管線驗證與產生

從 repo 根目錄執行。上游草稿由 Claude 維護，Codex 的 `02_codex_stage/`、`drafts/codex/` 不由本流程修改。

```bash
python3 -m unittest discover -s career/scripts/tests -v
python3 career/scripts/verify_polish.py
python3 career/scripts/verify_polish.py --verify-104 career/drafts/<版本>/104-<版本>.md
```

`verify_polish.py` 預設讀本地 Claude 草稿與指定遠端 Codex 成品；`--local-codex` 則讀指定遠端 Claude 草稿與本地 Codex 成品。指定的本地或 Git 來源不存在、讀取失敗、為空時直接失敗，不尋找其他分支或退回舊稿。執行前明確更新所需的遠端追蹤參照：

```bash
git fetch origin refs/heads/codex/resume-writer:refs/remotes/origin/codex/resume-writer
```

檢查包含非零區塊、合法狀態轉換、標記外正文、章節與公司標題、列點數量及父子關係、逐區塊數字與出現次數，以及 LOCKED 原文與內部空行。可改區塊的 2／4 格子項縮排若保留相同父子關係，視為等價；LOCKED 不允許這種格式改動。數字檢查不證明語意歸因，仍須人工閱讀。

104 驗證按 directive 的欄位、順序及 index 比對：每欄 code block 類型、完整可見文字、段落順序與重複次數皆須相同；名稱、標籤、鎖定欄位與圖片操作必須符合來源與已核可 metadata。拒絕多餘 code block、重複 JSON key 及未知 HTML 標籤。這不取代瀏覽器、PDF 或 ATS 驗收。

## 產生一般版與公開版

先將指定遠端成品唯讀匯出到自己的暫存位置，不 checkout 到 Codex 目錄。以原始未去識別成品為輸入：

```bash
python3 career/scripts/gen_104_md.py <成品快照.md> <104輸出.md> <版本> <來源說明>
python3 career/scripts/gen_104_md.py <成品快照.md> <104公開輸出.md> <版本> <來源說明> --public
```

預設以本地 `career/01_claude_stage/causal_draft.md` 驗證；需要固定快照時可用 `--draft <草稿快照.md>` 明確指定，不以成品自己當草稿。一般版先完整驗證草稿與成品，公開版亦先驗證原始定稿，再套用現有去識別規則。既有「先 public_redact 再傳入 --public」用法只在輸入與指定遠端定稿去識別結果完全一致時接受。

輸出先寫同目錄暫存候選檔，完整驗證與 104 欄位檢查成功後才加入「可填表／驗證通過」並原子替換目的檔。失敗不發布新成品，清理本輪暫存檔；若目的地已有上次成功的檔案，保留原檔不冒充本輪輸出。

公開版驗證：

```bash
python3 career/scripts/verify_polish.py --verify-104 <104公開輸出.md> --public
```

## 標籤與事實依據

已核可的 104 metadata 集中於 `verify_polish.py`，產生器引用同一份政策，驗證器獨立從來源章節重建預期欄位，不以重新呼叫產生器作為驗證。

- Scrum：保留 facts-1111 §§13–15 的 2022–2023 歷史能力，現行流程仍為 Kanban＋瀑布。另依 styling-directive-guide 的內文佐證要求，該專長卡沒提 Scrum 時不自動填 Scrum 標籤。目前定稿未提及，因此新產出不帶該標籤。
- UML：facts-1111 §4 有建模事實，定稿系統分析段有循序圖方法，保留。
- 其他現有標籤沿用核可映射，不因官方分類清單有該名稱就新增個人能力；Jira、SQL 等已否決工具仍攔截。

此次同步 main 後已確認 `resume-craft`、`resume-review-panel` 的所有 blob 與個人線一致；後續以個人線為準，由 Repo Steward 同步 main，不在本流程推 main。

## 語言分流（2026-11-02）

| 語言 | 工具 |
| :-- | :-- |
| 中文（104 履歷、自傳） | `verify_polish.py`、`gen_104_md.py`、`verify_letter.py`（中文推薦信）、`public_redact.py` |
| 英文（LINE Resume／通用版） | `verify_line_profile.py`、`verify_line_pdf.py`、`build_line_pdf.py`、`gen_line_pack.py`、`gen_line_pdf.py` |

兩邊工具互不呼叫、規則不共用；共用的只有 `library/` 事實與 `CAREER_START_HERE.md` 的 Gatekeeper／盲審流程。

## 104 推薦信批次：產生與驗收契約（2026-11-02 P0／P1）

```bash
# 產生（寫檔前先驗證；同名檔預設跳過；>350 字只警告）
python3 career/scripts/gen_cover_drafts.py <jobs.json> <companies.json> <codes.txt> --outdir <DIR> [--overwrite]
# 真實資料整合測試（固定 automation/104-data 快照 SHA）
python3 career/scripts/gen_cover_drafts.py --self-test [--snapshot <SHA>]
# 單封驗收（未給 --job／--company 時讀草稿檔頭；缺上下文會標「未完成對位驗證」）
python3 career/scripts/verify_letter.py <檔> --job "<對外職稱>" --company "<公司>"
# 全掃（逐檔帶上下文；略過已投遞／不投遞／已面試；驗證 0 封時 Exit 1）
python3 career/scripts/verify_letter.py --all
# 離線回歸測試（合成資料，只寫暫存目錄）
python3 -m unittest discover -s career/scripts/tests -p "test_*.py"
```

| 契約 | 內容 |
| :-- | :-- |
| 正文 | 共用 `extract_bodies()`：缺 fence、未閉合、空正文、只有稱謂／署名一律失敗 |
| 長度 | 中文信 ```text 區塊去空白字元數；<250 失敗、>350 警告（交 Codex 壓縮）；英文信不套中文長度與結尾規則 |
| 結構 | 中文信 3 個條列 |
| 禁詞 | 英文詞不分大小寫、加字母邊界；中文照字面 |
| 職稱 | 檔頭同時記職缺原名、job_id 與對外職稱；`--job` 用對外職稱 |
| 寫檔 | 硬性失敗不寫；同名檔不覆蓋（`--overwrite` 才覆蓋）；逐封回報成功／略過／失敗 |

已知限制：程式只能比對數字、限定詞與字面規則，不能證明語意歸因與選材適配；這兩項仍由主代理人工查核與盲審判斷。`--all` 會同時掃草稿與成品，報告分別列出檔名。

## 履歷工具鏈契約（2026-11-02 修訂）

### 英文 LINE：支援格式與路由

| 格式 | 判定方式 | verify | pack（fill／resume JSON） | pdf |
| :-- | :-- | :-- | :-- | :-- |
| resume | 有「Professional Summary」二級標題（不限編號）＋ directive | ✅ | ✅ | ✅ |
| profile | 沒有 Summary，只有 directive＋列點（例：Codex `line-profile-polished.md`） | ✅ | ❌ 前置拒絕 | ❌ 前置拒絕 |

```bash
python3 career/scripts/verify_line_profile.py <md> [--for verify|pack|pdf] [--upstream <上游 md>]
python3 career/scripts/gen_line_pack.py <resume 格式 md>
python3 career/scripts/build_line_pdf.py <md> <out.pdf> [--upstream <上游 md>]
python3 career/scripts/verify_line_pdf.py <pdf> --json <resume.json> [--html <html>]
```

- 解析共用 `line_md.py`：必要欄位非空、directive 型別、允許 action（basic＝replace_all，其餘＝replace_row）、重複鍵、區塊數量、index 連號。
- 語氣與錨點只看對外正文（HTML 註解剔除）。
- 來源串接：md →（source_sha256）→ resume.json（payload_sha256）→ HTML `<meta>` → PDF。renderer 重算兩個雜湊，不符即拒絕。
- PDF 內容對帳：Summary、Skills、職稱、公司、列點、學歷逐項出現、順序一致、次數相同，圓點數＝來源數。沒給 `--json` 時 Exit 1。
- 發布：HTML／PDF 先寫暫存，驗收通過才替換；JSON 原子寫入，驗收失敗不寫。自動縮字只控頁數，閱讀品質需人工視覺驗收。

### 事實保存（中英共用 `fact_lock.py`）

| 程式拒絕 | 人工查核（只回報） |
| :-- | :-- |
| 數字＋單位 multiset 改變（88% → 88 件） | 責任歸屬與因果是否改寫 |
| 上游 `[LOCK_FACTS: 對象=數值; …]` 對象與數值不在同句或被對調 | 比較組語意 |
| 開發中／規劃中被刪或改成已上線 | 限定詞換位置後的語意 |
| 限定詞（約、近、逾、至少、以上、團隊完成、協助、參與、限定口徑；about、nearly、more than…）次數減少 | |

- 中文：`verify_polish.py` 逐區塊比對；上游用 `[LOCK_FACTS: …]` 編譯必要對象與數值。
- 英文：`verify_line_profile.py --upstream`；沒給上游時明確標「未核對」。
- `NEEDS_POLISH`：取消 0.99 相似度一刀切。只有「逐字照抄且未標 `[KEEP: 保留理由]`」才算漏處理；標了 KEEP 即視為審讀後保留，列入主代理確認。

### 四種狀態不得混稱

格式通過（verify）≠ 事實保存（`--upstream`／`verify_polish`）≠ 語氣審查（盲審）≠ PDF 視覺驗收（人工看版面）。
