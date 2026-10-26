# Resume Gen｜Codex 接手封存包

整理時間：2026-10-20T15:03:48+08:00。用途：把此端可取得的 Resume Gen 專案檔案交給 Codex，供與 Claude Code 的既有專案整合。

本包是原檔封存與交接索引。尚未連接或修改接收端的儲存庫，也沒有替本人選定 SSOT 工作底稿、定版履歷或重做驗證。

## 接手閱讀順序

1. 讀 `AGENTS.md` 及 `handoff/01_project_instructions.md`，理解事實與驗證邊界。
2. 讀 `handoff/02_current_state.md`，辨認最後處理的草稿、已找到的 PDF 與未同步事項。
3. 讀 `reference/context/about-me-resume-gen.md`，理解人物脈絡；不要從它擅自補履歷數字。
4. 讀 `handoff/03_ssot_workflow.md`，與接收端既有檔案核對後再導入共同維護方式。
5. 按任務查看指定原稿。完整檔案清單見 `handoff/FILE_INVENTORY.csv`；PDF 清單見 `handoff/PDF_INVENTORY.md`。

## 重要檔案

| 內容 | 路徑／狀態 |
| --- | --- |
| 最後處理的文字稿 | `archive/workspace/resume-v10.10-draft.md`；v10.10，仍為 draft，並非自動指定的工作底稿 |
| 前一份文字稿 | `archive/workspace/resume-v10.9-draft.md`；v10.9 |
| 目前找到版本號最高的 PDF | `pdf/resume-v10.9-twocol.pdf`；不能代表 v10.10 的排版 |
| 人物參考 | `reference/context/about-me-resume-gen.md`；原檔第四版，2026/10/19 15:33，未改寫 |
| Claude Code 既有交接 | `reference/context/claude-code-about-me-instructions.md`；歷史原文，內含當時的整合指令 |
| 專案狀態 | `project_state.json`；active_resume 為 null，表示尚未在接收端指定 |
| 給 Codex 的接收指令 | `handoff/04_codex_import_prompt.md`；包含 Codex／Claude Code 分工 |
| 既有分工的依據與延續 | `handoff/08_collaboration_roles.md` |
| 完整對話的放置位置 | `conversations/`；使用者尚未提供本次全量匯出 |

## 封存內容

- 全部已找到的 19 份履歷專案 PDF，保留原檔名與不同上傳版本。
- 可取得的各版 Markdown、完整交接備註、自傳提案、人物參考、研究資料與工作中間產物。
- 原有編輯腳本、版面檢查圖片、文字擷取結果；作歷史資料保留，未宣稱它們能重新產生所有 PDF。
- 兩份專案自訂技能的原文快照與其附屬檔案。快照未安裝、未更新，也未改成接收端技能。
- 歷史驗證報告、規準與合成資料放在 `archive/historical_validation/`，僅作追溯；不要預設載入或把它交給獨立驗證者。
- 來源對照、逐檔 SHA-256、PDF 清單與打包檢查結果。

## 使用限制

此次範圍是本對話工作區及目前可取得的相關專案檔案。使用者另一端的 Claude Code 專案、PDF 排版原始碼與完整對話匯出尚未交付。詳見 `handoff/06_scope_and_gaps.md`。

同名且位元組完全一致的多處副本只保存一份內容，來源全部記在 `handoff/SOURCE_MAP.json`；不同檔名的 PDF 即使內容相同仍逐份保留。原始履歷及備註均未改寫。
