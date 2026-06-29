# 01 — tCode 共通 Schema

所有 tCode 表共用這套欄位（順序固定）：

| 欄 | 欄名 | 說明 |
|---|---|---|
| A | ChangeType | 異動類型：UnChange / 新增(add) / 改名(rename/edit) / 合併(merge)。決定該列要不要套用變更 |
| B | Old_CodeNo | 舊代碼（改名/合併時的來源） |
| C | New_CodeNo | 新代碼（改名/合併後的目標） |
| D | CodeNo | 現行代碼（程式用的鍵值） |
| E | CodeNameA | 名稱第一層 = **葉節點名稱**（最細，可選的實際選項） |
| F | CodeNameB | 名稱第二層 = **中類** |
| G | CodeNameC | 名稱第三層 = **大類**（部分表如 Benefit/CompSkill 無此欄） |
| (H/G) | CodeType | 階層層級：見下 |
| … | CodeDescript | 部分表（Benefit/CompSkill）有描述欄取代 CodeNameC |

## CodeType 階層

CodeType 標示該列在樹的哪一層。**葉 = CodeType 的最大值**：

| 表類型 | 階層 | 葉 CodeType |
|---|---|---|
| 三層表（多數：Duty*, Certify, City, College, Major, MRT, Nation, Trade, WorkAbility） | 大類(1) > 中類(2) > 葉(3) | **3** |
| 兩層表（Benefit, CompSkill） | 中類(1) > 葉(2) | **2** |

> 判讀：`CodeType == 葉值` 的列才是可選的實際選項；其餘是分類節點。

### 階層與 CodeNameA/B/C 的對應

對**葉節點**而言：
- `CodeNameA` = 葉名（如「經營管理主管」）
- `CodeNameB` = 中類（如「管理幕僚」）
- `CodeNameC` = 大類（如「管理幕僚／人資／行政」）

範例（tCodeDutyNM 葉）：
```
CodeNameA=經營管理主管 | CodeNameB=管理幕僚 | CodeNameC=管理幕僚／人資／行政 | CodeType=3
```

## ChangeType 處理（拿到含異動的版本時）

| ChangeType | 意義 | 動作 |
|---|---|---|
| UnChange | 無異動 | 略過 |
| 新增 / add | 全新代碼 | 在系統新增 CodeNo + 名稱 |
| 改名 / edit / rename | 名稱變更 | 依 Old_CodeNo→New_CodeNo 更新名稱 |
| 合併 / merge | 多碼併一碼 | 舊碼資料轉掛到 New_CodeNo，停用舊碼 |

> 比對兩版 export、產生異動清單、發系統公告的流程，使用 `tcode-excel-ops` skill（見 skills 目錄）。

## 載入程式（Python / openpyxl）

```python
import openpyxl
wb = openpyxl.load_workbook('TCode_Export_20260622.xlsx', read_only=True)
ws = wb['tCodeDutyNM']
rows = list(ws.iter_rows(min_row=1, values_only=True))
hdr = [str(c) if c else '' for c in rows[0]]
idx = {h:i for i,h in enumerate(hdr)}
leaves = [r for r in rows[1:] if str(r[idx['CodeType']]) == '3']
# 葉名→中類 對照（plan() 用的 MID）
MID = {r[idx['CodeNameA']]: r[idx['CodeNameB']] for r in leaves}
wb.close()
```
