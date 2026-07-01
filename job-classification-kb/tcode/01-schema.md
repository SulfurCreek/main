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

### CodeNo 位數規則（三層表，如 tCodeDutyNM）

`CodeNo` 本身就能看出層級，不必只靠 `CodeType` 欄：

| CodeType | 層級 | CodeNo 特徵 | 範例 |
|---|---|---|---|
| 1 | 大類 | 末四碼 `0000` | `160000` |
| 2 | 中類 | 末兩碼 `00` | `160100` |
| 3 | 葉／小類 | 末兩碼非 `00` | `160101` |

判斷一筆「新增／改名」該掛在中類還是小類層級：若來源資料只有大類／中類名稱、小類代碼與名稱是空的，代表這筆是**中類層級**的異動，對應代碼末兩碼必為 `00`；反之才是小類層級的新增/改名。

### 階層與 CodeNameA/B/C 的對應

對**葉節點**而言：
- `CodeNameA` = 葉名（如「經營管理主管」）
- `CodeNameB` = 中類（如「管理幕僚」）
- `CodeNameC` = 大類（如「管理幕僚／人資／行政」）

範例（tCodeDutyNM 葉）：
```
CodeNameA=經營管理主管 | CodeNameB=管理幕僚 | CodeNameC=管理幕僚／人資／行政 | CodeType=3
```

## I~T：職務內容描述欄（tCodeDutyNM／DutyPT／DutyHL 等 Duty 系表適用）

葉節點才會填這些欄；中類/大類列多半是空的。

| 欄 | 欄名 | 內容 | 與其他表的關聯 |
|---|---|---|---|
| I | CodeDescript | 工作內容條列（`<br>` 分隔） | — |
| J | CodeCore | 核心職能關鍵字 | — |
| K | CodeAlike | 相似／同義職稱（搜尋同義詞用） | — |
| L | CodeCert | 建議相關證照 | **強關聯 `tCodeCertify`**：值與該表葉節點 `CodeNameA` 逐字對應（抽樣 3 筆 100% 命中），可用字串比對自動關聯 |
| M | CodeFuture | 職涯發展／晉升方向（未來職稱） | — |
| N | CodeMajor | 建議學歷／科系 | **弱關聯 `tCodeMajor`**：僅文字概念呼應（如「工業管理類」對 tCodeMajor 的「工業管理學類」），非嚴格對照，不可字串比對 |
| O | CodeDefinition | 一句話定義 | — |
| P | chsNameA | **大陸對應職稱**（非簡繁轉換，是整套另外引用的大陸職業分類資料，用語/定義常與 CodeNameA 不同，如「經營管理主管」對應「首席執行官」） | — |
| Q | chsDescription | 大陸用語版職務說明（`φ` 開頭條列，明顯外部來源格式） | — |
| R | chsJobContent | 大陸用語版工作內容（同上格式） | — |
| S | chsJobSkills | 大陸用語版所需技能（同上格式） | — |
| T | chsAlike | 大陸用語版相似職稱（同上格式） | — |

> P~T 這組跟 D~O 是**兩套獨立內容**，不是彼此的翻譯——P~T 抄自另一套大陸職業分類資料源，用詞、定義、技能都改寫過。

## Z~AQ：多語系名稱欄（葉/中類/大類三層皆有值；Descript_* 系列抽樣多為空）

| 欄 | 欄名 | 內容 |
|---|---|---|
| Z | CodeNameEN | 葉節點英文名（與 AB 重複） |
| AA | CodeNameCHS | 葉節點**簡體中文**名（純繁轉簡，如「經營管理主管」→「经营管理主管」，跟 P 欄的「大陸對應職稱」不同） |
| AB/AC/AD | CodeNameA/B/C_EN | 葉／中類／大類 英文名 |
| AE | CodeDescript_EN | 英文版描述（抽樣多為空） |
| AF/AG/AH | CodeNameA/B/C_VI | 葉／中類／大類 **越南文**名 |
| AI | CodeDescript_VI | 越南文描述（多為空） |
| AJ/AK/AL | CodeNameA/B/C_TH | 葉／中類／大類 **泰文**名 |
| AM | CodeDescript_TH | 泰文描述（多為空） |
| AN/AO/AP | CodeNameA/B/C_ID | 葉／中類／大類 **印尼文**名 |
| AQ | CodeDescript_ID | 印尼文描述（多為空） |

> VI／TH／ID 對應 **`tCodeNation`** 的移工主要來源國，服務外籍移工／外語求職者介面的職稱在地化顯示。
> 實務技巧：同一中類下所有葉節點的 `CodeNameB/C_*`（EN/VI/TH/ID）**值完全相同**（因為是中類/大類層級翻譯，逐葉複製而來）——新增葉節點時，B/C 系列翻譯可直接**沿用同中類下任一既有葉節點的值**，只需新寫 A 系列（葉名本身）與 chs 系列。

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
wb = openpyxl.load_workbook('TCode_Export.xlsx', read_only=True)
ws = wb['tCodeDutyNM']
rows = list(ws.iter_rows(min_row=1, values_only=True))
hdr = [str(c) if c else '' for c in rows[0]]
idx = {h:i for i,h in enumerate(hdr)}
leaves = [r for r in rows[1:] if str(r[idx['CodeType']]) == '3']
# 葉名→中類 對照（plan() 用的 MID）
MID = {r[idx['CodeNameA']]: r[idx['CodeNameB']] for r in leaves}
wb.close()
```
