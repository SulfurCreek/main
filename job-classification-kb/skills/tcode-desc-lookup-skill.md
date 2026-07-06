# Skill：tCode Description 反查（tcode-desc-lookup）

> **時機**：判斷某職缺名稱的正解葉、或懷疑現有葉判錯時，**必須先反查候選葉的職務說明**再裁決，
> 不可只憑葉名字面相似度。本 skill 定義反查的合法資料路徑與快取維護程序。

## 鐵則

1. **禁止直接讀 Excel 查值**：不可為了看某葉的 Description 而 `load_workbook('TCode_Export.xlsx')` 逐格翻看。
2. **先查快取 MD**：[`tcode/data_tCodeDutyNM_descript_cache.md`](../tcode/data_tCodeDutyNM_descript_cache.md) 已收錄用過的葉。有就直接讀。
3. **快取沒有 → 用腳本抽取補進快取，再讀快取**（腳本一次性抽取＝合法；人工翻 Excel＝違規）。
4. **逐案累積，不做全表 dump**：614 葉全文 ~1.9MB，違反 tabular-token-min。只補本案需要的葉。
5. 反查後的裁決寫進快取 MD 文末「快取使用案例」表，並同步 `logic/04-case-decisions.md`。

## 反查判斷法

拿職缺名稱的**功能關鍵字**（R7 拆解後的字段）逐一對照候選葉的三個欄位：

| 欄位 | 用途 |
|---|---|
| `CodeDefinition` | 一句話定義——先看這個，快速排除 |
| `CodeDescript` | 工作內容條列——關鍵字職能是否被明確涵蓋（如「文件控管」「維護公司網路和資料」） |
| `CodeAlike` | 相似職稱——職缺名稱若直接命中此欄，強烈支持該葉 |

裁決原則：**說明涵蓋 > 葉名字面**。例：「文件管制課-助理工程師」字面像「檔案資料管理人員」，
但工程助理的 Descript 明載「文件控管」，且檔案資料管理人員的說明是純檔案室職能 → 正解為工程助理。

## 補快取程序（快取缺葉時）

資料來源優先序：
1. session 暫存的 Google Sheet 匯出 CSV（若本 session 已抓過，通常在 scratchpad）
2. 重抓 Google Sheet 發布連結的 CSV（見 `skills/google-sheets-skill.md`）
3. 都不可行時，才由 `TCode_Export.xlsx` **以腳本一次性抽取**（非人工翻閱）

```python
# 由來源抽取指定葉，貼進 data_tCodeDutyNM_descript_cache.md「已快取葉節點」段
import pandas as pd
nm = pd.read_csv('gs_tCodeDutyNM.csv', dtype={'CodeNo': str})   # 或改用 openpyxl 對 xlsx 做同樣一次性抽取
for t in ['要補的葉名']:
    r = nm[nm['CodeNameA'] == t].iloc[0]
    print(f"### {r['CodeNo']} {t}（{r['CodeNameB']}／{r['CodeNameC']}）\n")
    print(f"- **CodeDefinition**：{r['CodeDefinition']}")
    print(f"- **CodeDescript**：{str(r['CodeDescript'])}")
    print(f"- **CodeAlike（相似職稱）**：{str(r['CodeAlike'])}\n")
```

## 與其他文件的關係

- 欄位定義（I~T 欄怎麼讀）：[`tcode/01-schema.md`](../tcode/01-schema.md)
- 職缺名稱拆解規則 R7：`logic/01-plan-algorithm.md`
- 案例裁決記錄：`logic/04-case-decisions.md`
