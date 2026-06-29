# Skill — sync_md.py 同步工具使用

> MD↔Excel 雙向同步工具。完整原始碼見 [../scripts/sync_md.py](../scripts/sync_md.py)。

## 指令

```bash
python3 sync_md.py export          # Excel/CSV → MD（重建資料層）
python3 sync_md.py diff            # 顯示差異，不寫
python3 sync_md.py apply           # 顯示前30筆差異，不寫
python3 sync_md.py apply --confirm # 確認寫入對照版 Excel
```

## 頂部常數（移轉時要改路徑）

```python
MD_PATH  = '.../不合理清單_職類校正.md'           # 資料層
XLSX_SRC = '.../不合理清單_職類校正.xlsx'         # 主檔（前/後段欄位、T欄正解來源）
CSV_SRC  = '.../管理幕僚_人資_行政_-_不合理清單.csv'  # 現有職類來源
OUT_PATH = '.../不合理清單_職類校正_對照版.xlsx'   # 交付
PKL_PATH = '.../duty_all.pkl'                     # tCodeDutyNM 快取（可改成直讀 xlsx）
```

## 內部結構

| 函式 | 作用 |
|---|---|
| `load_duty()` | 載入葉名→中類 MID 對照（從 pkl 或 TCode xlsx） |
| `plan(vals, correct, ctx, title, MID)` | **核心判斷**，見 [logic/01](../logic/01-plan-algorithm.md) |
| `domain_ok(e, ctx, title)` | 領域保護判斷 |
| `lang_extra(title)` | 語言主動補：回傳該補的翻譯職類 |
| `cmd_export()` | 讀 Excel/CSV → 寫 MD |
| `parse_md()` | 讀 MD → list[dict] |
| `build_excel(rows, MID, do_write)` | 套 plan + 寫對照版（含配色、diff 收集） |
| `cmd_diff()` / `cmd_apply()` | 包裝 build_excel |

## MD 格式

```
| eNo | 職缺名稱 | 廠商名稱 | 現有1 | 現有2 | 現有3 | 現有4 | 現有5 | 正解 | S |
```
- 編輯時**只改「正解」欄**（個案修正）。
- 欄內若含 `|` 用 `／` 取代避免破壞表格。

## 修改 plan() 的安全流程

1. 改 `plan()` 或常數。
2. 跑 [logic/02](../logic/02-verified-logic.md) 全校準案例回歸。
3. `diff` 確認影響範圍。
4. `apply --confirm`。
5. 重建北三區 sheet（`split_region`，見 scripts）。
6. 重大變動做三輪自我審查。

## build_excel mode 分支檢查清單（防 P1 雷）

確認這六種 mode 都有寫入邏輯：
- [ ] `keep` — 不動
- [ ] `keep_strike` — 槓 list 中各格
- [ ] `replace` — 槓 idx、建議 idx=正解
- [ ] `replace_multi` — 槓 list 各格、list[0] 建議=正解
- [ ] `replace_all` — 槓所有非空、建議1=正解
- [ ] `add` — 建議 idx=正解、現有不動
- [ ] 語言主動補：`lang_extra` 補到空格
