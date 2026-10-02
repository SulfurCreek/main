---
name: safe-excel-editor
description: >
  修改、更新或寫入既有 Excel 檔案時的安全編輯鐵則（局部、原子化、保留格式）。
  只要任務涉及對既有 .xlsx 做欄位/儲存格修改、標記刪除線或底色、更新特定 ID 的值、
  回寫分析結果（如職類校正對照、不合理清單標記）時，務必套用本 skill。
  關鍵字：openpyxl、load_workbook、儲存格修改、刪除線、底色、備份、原子化編輯、Excel 寫入。
---

# Excel 局部編輯與安全修改（safe-excel-editor）

收到修改／更新／寫入既有 Excel 的指令時，**嚴格**執行以下腳本操作。

## 鐵則

1. **格式與公式保留（Openpyxl 優先）**
   - **嚴禁**用 `pandas` 覆寫檔案（會遺失既有 UI 格式、背景色、公式、欄寬、凍結窗格）。
   - 必須用 `openpyxl` 的 `load_workbook()` 載入，針對特定 Cell 精準修改。

2. **強制備份機制（Auto-Backup）**
   - 執行任何修改腳本**前**，先用 `shutil` 把原檔複製為 `[原檔名]_backup_YYYYMMDD.xlsx`。

3. **原子化靜默操作（Silent Atomic Edits）**
   - 用程式碼定位目標列/欄（找並取代特定狀態、更新特定 ID 的欄位），完成後 `workbook.save()`。
   - **嚴禁**在對話框印出修改前後的大量資料比對。

4. **極簡確認回報（Minimal ACK）**
   - 腳本跑完，只輸出：「✅ 已備份並成功更新 N 筆儲存格」，並隨機抽 1 筆修改後的 Row 作驗證。

5. **槓必補、放旁邊（Strike ⇒ mandatory adjacent suggestion）**
   - 只要對某格做刪除線／槓除（移除原推薦或原值），**就一定要在它旁邊的欄位補上建議，不可留空**——不論是職類 1/2/3/4/5 哪一格。
   - 建議欄緊鄰被槓欄右側（如：`現有1 | 建議1 | 現有2 | 建議2 | …`），被槓格用刪除線＋淺紅，建議格用橘底。
   - 反向亦然：**沒有可補的建議就不要槓**（擦邊保留）。存檔前防呆驗證「被槓格數 == 同列建議格有值數」，殘留空建議要當錯誤擋下。

6. **不污染未處理欄（No cross-column contamination）**
   - 只標記本次要處理的欄；其餘欄位**不得殘留**上一版的刪除線／底色。
   - 若來源檔可能帶舊格式（人工標記殘留），改格式前先確認；必要時**從純值重建**（`values_only` 讀出再寫回）以清掉繼承樣式，避免「莫名其妙的刪除線」。

## 標準起手式

```python
import shutil, openpyxl
from datetime import datetime           # 注意：取日期請用傳入值，勿依賴沙箱被禁的 API
from openpyxl.styles import Font, PatternFill

SRC = "檔案.xlsx"
bak = SRC.replace(".xlsx", f"_backup_{YYYYMMDD}.xlsx")   # YYYYMMDD 由外部給定
shutil.copyfile(SRC, bak)                                # ① 先備份

wb = openpyxl.load_workbook(SRC)                          # ② 載入（保留格式）
ws = wb["工作表"]
n = 0
for row in ws.iter_rows(min_row=2):
    # 定位 → 精準改 cell（值 / 字體 / 底色）
    ...
    n += 1
wb.save(SRC)                                              # ③ 原子化存回
print(f"✅ 已備份並成功更新 {n} 筆儲存格")                 # ④ 極簡 ACK + 抽 1 列驗證
```

## 本專案配色慣例（職類校正對照）

| 標記 | 樣式 | openpyxl |
|---|---|---|
| 現有項被槓（錯誤） | 刪除線 + 淺紅 `FFFFC7CE` | `Font(strike=True)` + `PatternFill('solid', fgColor='FFC7CE')` |
| 建議項（正解） | 橘 `FFFFA500` | `PatternFill('solid', fgColor='FFA500')` |

> 與 `tabular-token-min` skill 搭配：分析/運算在腳本內完成，只回報最終結果與 1 列抽驗，不 dump 全表。
