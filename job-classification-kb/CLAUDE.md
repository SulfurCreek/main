# CLAUDE.md — 專案進入點

> Claude Code 讀我。這是「1111 職類校正」專案的工作說明書。你是一名**專業資料處理員**：精確、可追溯、改動前先審查、寫入前先 diff。

## 你的任務

對 1111人力銀行「不合理清單」職缺，判斷每個職缺的單一最佳職務小類（正解），產出「現有 vs 建議」對照 Excel。

## 先讀這些（依序）

1. `README.md` — 知識庫地圖
2. `wiki/00-index.md` — 關鍵字總索引（找任何主題從這裡）
3. `logic/02-verified-logic.md` — 已驗證 OK 的規則 + 校準案例（**改 code 前必讀**）
4. `logic/03-pitfalls.md` — 要避免的錯誤（**改 code 前必讀**）

## 索引機制

- `INDEX.json` — 所有 MD 的機器可讀索引（file/title/headings）。要做全文檢索或定位主題，先讀這個。
- 每份 wiki 文件互相以相對連結串接。

## 核心工作流程

```bash
python3 scripts/sync_md.py export          # Excel/CSV → MD 資料層
python3 scripts/sync_md.py diff            # 預覽差異
python3 scripts/sync_md.py apply --confirm # 寫入對照版 Excel
python3 scripts/tcode_to_md.py tCodeDutyNM # tCode 表 → MD
```

## 鐵則（違反會出錯）

1. **資料層是 MD**（`不合理清單_職類校正.md`），正解的唯一真實來源。個案修正改這裡的「正解」欄。
2. **規則層是 plan()**（`scripts/sync_md.py`）。規則性錯誤改這裡，不做一次性 hack。
3. **改 plan() → 跑全校準案例回歸**（logic/02 表格），全過才放行。
4. **寫 Excel 前先 diff，寫完讀回抽查**（防 P1：mode 分支不齊導致判斷對卻沒寫入）。
5. **看 mode 不夠，要看 5 格實際輸出**（哪格槓、哪格建議）。
6. **擦邊保留**是核心價值：寧可多留相關項，只槓明確錯的。
7. 重大規則變動 → **三輪自我審查**再回報（流程見 logic/02 末節）。
8. apply 後**重建北三區 sheet**（主表+北三區兩個分頁）。

## 環境注意

- 路徑：`scripts/sync_md.py` 與 `tcode_to_md.py` 頂部常數需對應你的目錄。
- 檔案系統可能重置 → duty 資料從 `TCode_Export_*.xlsx` 重載（見 tcode/01-schema 載入程式）。
- 來源/交付可改用 Google Sheet → 見 `skills/google-sheets-skill.md`。

## tCode 速查

15 張代碼表，職類校正用 `tCodeDutyNM`（614 葉 / 58 中類 / 20 大類）。表用途見 `tcode/00-tcode-index.md`，現成資料 MD 在 `tcode/data_*.md`。
