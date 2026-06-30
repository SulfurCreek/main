---
name: md-datalayer
description: >
  以 Markdown 作為表格資料的工作資料層（唯一真實來源）的工作流程鐵則。
  當任務在分析或修改 Excel/CSV 內容（尤其職類校正、不合理清單等已建立 MD 資料層的資料）時，
  一律讀寫 MD、不回讀 Excel；只有使用者明確要求「輸出／給我 Excel」時才由 MD 產生 Excel。
  關鍵字：資料層、MD、Markdown、唯一真實來源、Excel 輸出、md_sync、不回讀 Excel。
---

# Markdown 資料層工作流程（md-datalayer）

表格資料（Excel/CSV）一旦建立 MD 資料層，**MD 就是唯一真實來源**。

## 鐵則

1. **分析讀 MD，不讀 Excel**
   - 任何查詢、統計、判斷、比對 → 讀 `.md` 資料層。**不要**回去 `load_workbook` 讀 Excel 取值。

2. **修改改 MD，不改 Excel**
   - 個案修正、加建議、改值 → 直接編輯 MD 表格（或用腳本重寫 MD）。Excel 不是編輯對象。

3. **Excel 只在「要輸出時」才產生**
   - 使用者明確說「輸出／給我 Excel／產生檔案」時，才由 MD → Excel。
   - 平時對話、分析、改資料**都不產生 Excel**。

4. **產生 Excel 時套 safe-excel-editor**
   - 由 MD 寫 Excel 仍遵守槓必補、配色、最小回報等規則（見 `safe-excel-editor` skill）。

## 本專案實作（職類校正）

- 資料層：`job-classification-kb/不合理清單_職類校正.md`
  - 每分頁一個 `##` 區段，欄位：
    `eNo | 廠商編號 | 廠商名稱 | 廠商狀態 | 分區 | 客服人員 | 職缺名稱 | 現有1 | 建議1 | 現有2 | 現有3 | 現有4 | 現有5`
  - **「建議1」有值 ⟺ 現有1 判定有誤**（輸出時：現有1 刪除線+淺紅、建議1 橘底）。
  - 欄內 `|` 一律以 `／` 取代。

- 同步腳本：`scripts/md_sync.py`
  ```bash
  python3 scripts/md_sync.py to-md   [來源.xlsx]   # Excel → MD（重建資料層；通常只做一次）
  python3 scripts/md_sync.py to-xlsx [輸出.xlsx]   # MD → Excel（使用者要輸出時才跑）
  ```
  - round-trip 已驗證：MD↔Excel 筆數與標記數一致。

## 流程

```
建立資料層（一次）         分析 / 修改（多次）            輸出（要求時）
Excel ──to-md──▶ MD  ─────▶  讀 MD、改 MD（不碰 Excel） ─────▶ MD ──to-xlsx──▶ Excel
```

> 與 `tabular-token-min`、`safe-excel-editor` 搭配：讀 MD 仍只取需要的子集、運算在腳本內；輸出 Excel 時套安全編輯鐵則。
