---
name: job-classification-kb
description: >
  1111 人力銀行「職類校正 / 不合理清單」專案的工作知識庫入口。
  當任務涉及判斷職缺的正解職務小類、處理「不合理清單」、修改 plan() 語意規則、
  操作 sync_md.py 的 export/diff/apply、產出「現有 vs 建議」對照 Excel、
  查詢 tCode 代碼表（tCodeDutyNM / DutyPT / Certify / CompSkill / WorkAbility 等）、
  或讀寫本專案的 Google Sheet 時，使用本 skill。
  關鍵字：職類校正、正解、中類、葉、不合理清單、plan()、keep/replace/add、tCode、北三區。
---

# 職類校正知識庫（job-classification-kb）

1111 人力銀行「不合理清單職類校正」專案的完整工作知識庫。任務目標：對職缺判斷**單一最佳職務小類（正解）**，產出「現有 vs 建議」對照 Excel。執行者定位是**專業資料處理員**：精確、可追溯、改動前先審查、寫入前先 diff。

## 知識庫位置

知識庫在 repo 內：`job-classification-kb/`。本 skill 是它的觸發入口；實際內容、邏輯、資料都在該目錄。

## 開工前必讀（依序）

1. `job-classification-kb/CLAUDE.md` — 專案進入點（任務、鐵則、工作流程）
2. `job-classification-kb/README.md` — 知識庫地圖
3. `job-classification-kb/wiki/00-index.md` — 關鍵字總索引（找任何主題從這裡）
4. `job-classification-kb/logic/02-verified-logic.md` — ✅ 已驗證規則 + 校準案例（**改 plan() 前必讀**）
5. `job-classification-kb/logic/03-pitfalls.md` — ⚠️ 9 個踩過的雷（**改 plan() 前必讀**）

## 索引機制

- `job-classification-kb/INDEX.json` — 所有 MD 的機器可讀索引（file / title / headings）。要做主題定位或全文檢索，先讀這個再開對應檔。
- `job-classification-kb/wiki/00-index.md` — 人讀的關鍵字 → 文件對照表。

## 核心工作流程

```bash
cd job-classification-kb
python3 scripts/sync_md.py export          # Excel/CSV → MD 資料層
python3 scripts/sync_md.py diff            # 預覽差異（寫入前必跑）
python3 scripts/sync_md.py apply --confirm # 寫入對照版 Excel
python3 scripts/tcode_to_md.py tCodeDutyNM # tCode 表 → MD
```

> 移轉注意：`scripts/sync_md.py`、`scripts/tcode_to_md.py` 頂部的路徑常數需對應實際目錄；duty 資料若檔案系統重置，從 `TCode_Export_*.xlsx` 重載（見 `tcode/01-schema.md`）。

## 鐵則（違反會出錯）

1. **資料層是 MD**（`不合理清單_職類校正.md`）＝正解的唯一真實來源。個案修正改「正解」欄。
2. **規則層是 plan()**（`scripts/sync_md.py`）。規則性錯誤改這裡，不做一次性 hack。
3. **改 plan() → 跑全校準案例回歸**（`logic/02` 表格），全過才放行。
4. **寫 Excel 前先 diff，寫完讀回抽查**（防 P1：mode 分支不齊→判斷對卻沒寫入）。
5. **看 mode 不夠，要看 5 格實際輸出**（哪格槓、哪格建議）。
6. **擦邊保留**是核心價值：寧可多留相關項，只槓明確錯的。
7. 重大規則變動 → **三輪自我審查**再回報（流程見 `logic/02` 末節）。
8. apply 後**重建北三區 sheet**（主表 + 北三區兩個分頁）。

## 主題定位速查

| 你想找… | 開這份 |
|---|---|
| plan() 怎麼決定槓哪格、補哪格 | `logic/01-plan-algorithm.md` |
| 哪些判斷已確認是對的（回歸基準） | `logic/02-verified-logic.md` |
| 以前犯過什麼錯、別再犯 | `logic/03-pitfalls.md` |
| 某個 eNo 為什麼這樣判 | `logic/04-case-decisions.md` |
| 規則怎麼從 v1 演進到 v8 | `CHANGELOG.md` |
| tCode 有哪些表、各做什麼 | `tcode/00-tcode-index.md` |
| tCode 欄位、CodeType 階層 | `tcode/01-schema.md` |
| 把某張表轉成 MD 的食譜 | `tcode/02-analysis-recipes.md` |
| 職務表 NM/HL/PT/ST/TU 差異 | `tcode/03-duty-tables.md` |
| 現成代碼資料 MD | `tcode/data_*.md` |
| 讀寫 Google Sheet（憑證/gspread/配色/配額） | `skills/google-sheets-skill.md` |
| sync_md.py 用法細節 | `skills/sync-md-skill.md` |

## tCode 速查

15 張代碼表，職類校正主用 `tCodeDutyNM`（614 葉 / 58 中類 / 20 大類）。表用途見 `tcode/00-tcode-index.md`，現成資料 MD 在 `tcode/data_*.md`。
