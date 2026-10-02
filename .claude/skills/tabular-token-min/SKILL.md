---
name: tabular-token-min
description: >
  處理 Excel／CSV／試算表等表格檔案時，強制最小化 token 消耗、控制 context window 的鐵則。
  只要任務涉及讀取、清洗、樞紐分析、運算或彙整 .xlsx / .xls / .csv / .tsv 等表格資料
  （例如 TCode_Export.xlsx、不合理清單、廠商身分 sheet、任何 dataframe 操作），務必套用本 skill。
  關鍵字：Excel、CSV、試算表、pandas、df.info、df.head、樞紐、資料清洗、token 最小化。
---

# Excel/CSV Token 消耗最小化（tabular-token-min）

處理表格檔案時，**強制**執行以下操作以控制 Context Window。違反會把整張表灌進對話、爆掉 context。

## 鐵則

1. **禁止純文字讀取**：嚴禁將檔案內容轉為純文字載入對話上下文（不可 `cat`／`Read` 整個 CSV、不可貼整張表、不可 dump 全部 rows）。

2. **強制 Python 採樣**：必須呼叫 Python（如 `pandas`）讀取檔案；初次確認時**僅允許**印出：
   - `df.info()` — 結構（欄位、型別、筆數）
   - `df.head(3)` — 前三筆預覽

3. **背景運算限制**：所有資料清洗、樞紐分析與運算皆須於 Python 腳本內完成；**嚴禁**於對話中列印中間運算數據（不印逐列迴圈結果、不印完整 value_counts、不印中繼 dataframe）。

4. **極簡輸出**：僅允許輸出
   - 運算後的**最終 Markdown 表格**，或
   - 高維度資料的 **Mermaid 統計圖表語法**。

## 標準起手式

```python
import pandas as pd
df = pd.read_excel("檔案.xlsx", sheet_name="工作表")   # CSV 用 pd.read_csv(...)
df.info()        # 結構
df.head(3)       # 前三筆
```

確認結構後，後續清洗／樞紐／聚合一律寫進腳本，只把**最終結果**轉成 Markdown 表格或 Mermaid 圖回報。

## 套用提醒

- 大表（數千列以上，如 `TCode_Export.xlsx`、`tCodeCertify`、`tCodeWorkAbility`）尤其要遵守：先 `df.info()`／`head(3)` 偵察，再以腳本聚合，**不 dump 全表**（與 `job-classification-kb` 的 tCode 分析食譜一致）。
- 需要中類／群組統計時，於腳本內 `groupby().size()` 後，只輸出彙整後的表或圖，不印明細列。
- 若使用者要看「某幾列原始資料」，只取該子集（`df.loc[...]`）並限制欄位，仍避免整表輸出。
