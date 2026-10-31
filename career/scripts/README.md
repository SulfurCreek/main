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
