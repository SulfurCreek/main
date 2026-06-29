# 1111 職類校正知識庫 (Job Classification Knowledge Base)

> 移轉至 Claude Code 的完整工作知識庫。本庫記錄「不合理清單職類校正」專案累積的全部分析經驗、已驗證邏輯、待避免錯誤，以及 tCode 代碼表的結構與快速分析法。

## 這個庫是什麼

1111人力銀行的職缺「職務小類」常被亂掛（一個職缺掛 5 個不相關職類）。本專案針對「管理幕僚／人資／行政」不合理清單（1,072 筆），用語意規則自動判斷每個職缺的**正解職類**，並產出「現有 vs 建議」的對照 Excel。本庫是這套規則與工作流程的完整文件。

## 角色設定

執行者是**專業資料處理員**：精確、可追溯、改動有審查。核心紀律：
- 改 plan() 規則前先看 `logic/02-verified-logic.md` 的校準案例，改完一定回歸測試。
- 寫入 Excel 前一定先 diff。
- 個案修正同時更新「資料層 (MD)」與「規則層 (plan)」，不做一次性 hack。

## 索引 (Index)

### 🧭 Wiki — 概念與導覽
- [wiki/00-index.md](wiki/00-index.md) — **總索引、關鍵字對照表**（從這裡找任何主題）
- [wiki/01-project-overview.md](wiki/01-project-overview.md) — 專案背景、輸入輸出、檔案地圖
- [wiki/02-workflow.md](wiki/02-workflow.md) — MD↔Excel 同步工作流程
- [wiki/03-glossary.md](wiki/03-glossary.md) — 術語表（正解／現有／中類／葉…）

### 🧠 Logic — 分析邏輯（最重要）
- [logic/01-plan-algorithm.md](logic/01-plan-algorithm.md) — plan() 演算法完整規格（模式、保護、取代）
- [logic/02-verified-logic.md](logic/02-verified-logic.md) — ✅ **已驗證 OK 的邏輯**（含校準案例，回歸測試基準）
- [logic/03-pitfalls.md](logic/03-pitfalls.md) — ⚠️ **要避免的錯誤邏輯**（歷次踩過的雷）
- [logic/04-case-decisions.md](logic/04-case-decisions.md) — 逐案判定紀錄（eNo → 為何這樣判）

### 📊 tCode — 代碼表知識
- [tcode/00-tcode-index.md](tcode/00-tcode-index.md) — **15 張表總覽 + 用途對照**
- [tcode/01-schema.md](tcode/01-schema.md) — 共通 schema（欄位、CodeType 階層、ChangeType）
- [tcode/02-analysis-recipes.md](tcode/02-analysis-recipes.md) — 各表「如何快速分析產生 MD」食譜
- [tcode/03-duty-tables.md](tcode/03-duty-tables.md) — 職務表深入（NM/HL/PT/ST/TU 差異、中類清單）

### 🛠 Skills — Claude Code 技能
- [skills/google-sheets-skill.md](skills/google-sheets-skill.md) — **讀寫 Google Sheet 技能**（憑證、API、讀寫範式）
- [skills/sync-md-skill.md](skills/sync-md-skill.md) — MD↔Excel 同步工具使用說明

### 💾 Scripts — 可執行程式
- [scripts/sync_md.py](scripts/sync_md.py) — 主同步工具（export/diff/apply）
- [scripts/tcode_to_md.py](scripts/tcode_to_md.py) — tCode 表 → MD 產生器

## 快速上手 (Claude Code)

```bash
# 1. 重建 MD 資料層（從 Excel/CSV）
python3 scripts/sync_md.py export

# 2. 看會改什麼（不寫入）
python3 scripts/sync_md.py diff

# 3. 確認後寫入對照版 Excel
python3 scripts/sync_md.py apply --confirm

# 4. 把任一 tCode 表轉成可讀 MD
python3 scripts/tcode_to_md.py tCodeDutyNM
```

## 維護原則

- **資料層**＝MD 檔（`不合理清單_職類校正.md`），是正解的唯一真實來源 (single source of truth)。
- **規則層**＝`sync_md.py` 的 `plan()`，所有語意判斷集中於此。
- 個案微調 → 同時改 MD 正解 + plan 規則 → 回歸測試校準案例 → diff → apply。
- 重大規則變動要做「三輪自我審查」（見 [logic/02](logic/02-verified-logic.md) 末節）。
