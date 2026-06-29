# Skill — 讀寫 Google Sheet (Google Sheets Access)

> 在 Claude Code 環境讀取/寫入 Google Sheet。本專案的來源清單與交付對照表可改放 Google Sheet，取代本機 CSV/Excel。

## 適用時機

- 來源「不合理清單」改由 Google Sheet 維護（多人協作）。
- 交付「對照版」要寫回 Google Sheet 給客服/企劃看。
- 任何需要程式化讀寫試算表的任務。

## 前置：憑證設定

兩種方式，擇一：

### A. Service Account（推薦，無互動）
1. Google Cloud Console 建立專案 → 啟用 **Google Sheets API**。
2. 建立 Service Account → 產生 JSON 金鑰，存為 `credentials/service_account.json`（**勿進版控**）。
3. 把目標 Sheet **分享給** service account 的 email（`xxx@xxx.iam.gserviceaccount.com`），給編輯權限。

### B. OAuth User（個人帳號互動授權）
1. 建立 OAuth Client ID（Desktop）→ 下載 `credentials.json`。
2. 首次執行會開瀏覽器授權，產生 `token.json` 供後續重用。

## 安裝套件

```bash
pip install gspread google-auth google-auth-oauthlib google-api-python-client --break-system-packages
```

## 讀取（gspread，最簡）

```python
import gspread
gc = gspread.service_account(filename='credentials/service_account.json')
sh = gc.open_by_key('SPREADSHEET_ID')          # 從 URL /d/<ID>/ 取得
ws = sh.worksheet('不合理清單')                  # 或 sh.sheet1
rows = ws.get_all_records()                      # list[dict]，第一列當 header
# 或：values = ws.get_all_values()               # list[list]，純文字
```

## 寫入

```python
# 整批覆寫（含 header）
header = ['eNo','職缺名稱','正解']
data = [[r['eNo'], r['職缺名稱'], r['正解']] for r in records]
ws.update('A1', [header] + data, value_input_option='USER_ENTERED')

# 單格 / 範圍
ws.update_acell('C2', '產品經理')
ws.update('A2:C2', [['132520270','專案經理','專案經理']])

# 追加列
ws.append_row(['新eNo','新職稱','新正解'], value_input_option='USER_ENTERED')
```

## 格式化（刪除線、底色）— 需 Sheets API batchUpdate

gspread 的 `format()` 處理底色/字體；刪除線需 textFormat。

```python
# 底色（建議格=橘）
ws.format('B2', {'backgroundColor': {'red':1,'green':0.65,'blue':0}})
# 刪除線（被槓現有格）
ws.format('A2', {'textFormat': {'strikethrough': True},
                 'backgroundColor': {'red':1,'green':0.78,'blue':0.81}})
```

> 對照版的配色對應（與 Excel 一致）：
> - 現有被槓：刪除線 + 淺紅 `FFFFC7CE` → `{red:1, green:0.78, blue:0.81}`
> - 建議：橘 `FFFFA500` → `{red:1, green:0.65, blue:0}`

## 與本專案整合的建議

1. **來源**：`sync_md.py export` 改成可從 Google Sheet 讀「不合理清單」(get_all_records) → 寫 MD。
2. **交付**：`apply` 後，除了寫本機 Excel，另提供 `push_to_gsheet()` 把對照版兩個分頁（不合理清單、北三區）寫回 Google Sheet 並套色。
3. **ID 管理**：把 SPREADSHEET_ID 放 `.env` 或 config，不要寫死在程式。

## 常見錯誤

| 錯誤 | 原因 / 解法 |
|---|---|
| `PermissionError 403` | Sheet 沒分享給 service account email |
| `SpreadsheetNotFound` | ID 錯，或用了整個 URL 而非 /d/<ID>/ 的 ID |
| `APIError 429` | 配額超限；批次 `update` 一次寫多格，別逐格 |
| 中文變亂碼 | 確保讀寫都 UTF-8；gspread 預設 OK |
| 數字被轉成科學記號 | `value_input_option='USER_ENTERED'` 或先轉字串 |

## 配額注意

Sheets API 預設每分鐘每使用者 60 次讀 + 60 次寫。大量寫入要用 `batch_update` / 單次 `update` 多格，避免逐格呼叫觸發 429。
