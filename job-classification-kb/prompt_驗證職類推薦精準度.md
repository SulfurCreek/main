# 分析任務 Prompt — 驗證「職類推薦 vs 現有 duty」精準度

> 本檔是給執行分析的模型讀的完整任務說明書。所有需要的資料、規則、既有知識都在本 repo（分支 `claude/extract-job-duty-markdown-4avmd6`），路徑以 repo 根目錄起算。**先讀完本檔再動手。**

---

## 一、任務目標

針對 183,713 筆「職缺名稱 × tCodeDuty 對照」巨量資料，**驗證系統產出的職類推薦（職類推薦1~10）相對於現有掛載職類（duty0~4）的精準度**。

產出方向（由你規劃細節，但至少涵蓋）：
1. 推薦命中率：職類推薦1~N 是否涵蓋 duty0~4（依名次分層：top1 / top3 / top5 / top10）。
2. 推薦與現有的偏差樣態：完全不重疊、部分重疊、順位錯置等分布。
3. 以職缺名稱語意判斷「現有 vs 推薦誰比較準」的抽樣質性分析（用既有語意規則，見下方資源）。
4. 統計結果一律輸出為 **最終 Markdown 表格或 Mermaid 圖**，不 dump 明細。

---

## 二、主資料檔

`job-classification-kb/tcode/data_職缺名稱_dutyMapping.md`（約 55MB，183,719 行）

- 格式：單一 Markdown 表格，前 2 行為標題與來源說明，第 4 行是表頭，第 5 行是分隔線，之後每行一筆。
- 欄位（16 欄）：

| 欄 | 意義 | 非空筆數 |
|---|---|---|
| 職缺名稱 | 職缺標題原文 | 183,712（1 筆空） |
| duty0 | 現有掛載職類（主） | 183,713 |
| duty1~duty4 | 現有掛載職類（次，遞減稀疏） | 125,620 / 64,301 / 8,814 / 7,007 |
| 職類推薦1~職類推薦5 | 系統推薦（幾乎全滿） | 各 183,712 |
| 職類推薦6~職類推薦10 | 系統推薦（尾端漸稀） | 183,425 → 180,780 |

- 資料特性（已偵察）：
  - 整檔有 **15,113 筆完全重複列**（未去重，分析時自行決定要不要去重並註明）。
  - 原始儲存格內的 `|` 已在匯出時替換為 `／`（共 620 格受影響），比對職類名稱時注意全形斜線。
  - 職類值是**中文職類名稱字串**（非代碼），對應 tCodeDutyNM 的葉名稱。

### ⛔ 讀檔鐵則（token 控制，違反會爆 context）

- **嚴禁**用 Read/cat 整檔載入對話。一律寫 Python 腳本處理（pandas 讀 MD 表格：跳過前 5 行 meta，用 `sep='|'` 解析，或逐行 split）。
- 對話中只印 `df.info()` / `head(3)` 級別的偵察輸出與**最終彙整結果**。
- 中間運算（value_counts 全量、逐列迴圈結果、中繼 df）都留在腳本內。
- 對應 repo skill：`.claude/skills/tabular-token-min/`（必讀必遵守）。

---

## 三、必用的 repo skills（.claude/skills/）

| Skill | 何時套用 |
|---|---|
| `tabular-token-min` | 全程。任何表格讀取/運算的 token 鐵則 |
| `md-datalayer` | 全程。MD 是唯一真實來源，不回讀 Excel；只有使用者明說要 Excel 才產出 |
| `job-classification-kb` | 專案知識庫入口，涉及正解判斷、tCode 查詢時 |
| `safe-excel-editor` | 僅在最後被要求輸出 Excel 時 |

---

## 四、比對基準：tCodeDutyNM 代碼表（已有現成 MD，不要重新匯出）

| 檔案 | 內容 |
|---|---|
| `job-classification-kb/tcode/data_tCodeDutyNM.md` | **主基準表**：617 葉 / 58 中類 / 20 大類完整清單（大類→中類→葉 名稱）。推薦與現有值都應能對到這裡的葉名稱；比對「中類/大類層級是否相近」也靠這張的階層 |
| `job-classification-kb/tcode/data_tCodeDutyNM_descript_cache.md` | 已反查過的葉節點職務說明快取（質性判斷時查語意） |
| `job-classification-kb/tcode/00-tcode-index.md` | 15 張 tCode 表總覽、選表指南 |
| `job-classification-kb/tcode/03-duty-tables.md` | NM/HL/PT/ST/TU 五表差異 + DutyNM 完整大類/中類結構表 |
| `job-classification-kb/tcode/01-schema.md` | tCode 欄位與 CodeType 階層定義 |
| `job-classification-kb/tcode/data_tCodeDutyNM_changes.md` | 待議新增/改名清單（若有職類名對不上葉，先查這裡是否改名中） |
| `job-classification-kb/scripts/_dutynm_tree.json` | DutyNM 階層樹的機器可讀版（腳本比對中類/大類時直接載這個，免解析 MD） |

> ⚠️ 名稱正規化提醒：職類名稱含全形斜線 `／`（如「廣告／行銷企劃主管」），主資料檔與代碼表兩邊一致；但仍建議比對前 strip 空白並統一全半形。

---

## 五、語意判斷資源（質性抽樣時用）

本專案已累積一套「職缺名稱 → 正解職類」的驗證過規則，抽樣判斷「現有 vs 推薦誰較準」時**必須沿用，不要自創**：

| 檔案 | 內容 |
|---|---|
| `job-classification-kb/logic/02-verified-logic.md` | **已驗證 OK 的語意規則 + 校準案例**（function tail、agency 公司、語言保護、管理詞保護、機構行政共存、職稱拆解…） |
| `job-classification-kb/logic/03-pitfalls.md` | 以前犯過的錯，不要再犯 |
| `job-classification-kb/logic/01-plan-algorithm.md` | plan() 的 keep/replace/add 決策邏輯（概念可借用於「推薦是否合理」的分級） |
| `job-classification-kb/wiki/03-glossary.md` | 術語表：正解、中類、葉、OFFICE_MID、SUPPORT、loosely_related 等定義 |
| `job-classification-kb/wiki/00-index.md` | 關鍵字總索引，找任何主題從這裡 |
| `job-classification-kb/skills/tcode-desc-lookup-skill.md` | 反查葉節點職務說明（Description）的方法 |
| `job-classification-kb/INDEX.json` | 全 KB 的機器可讀索引（file/title/headings） |

關鍵語意規則速記（詳見 logic/02）：
- **function tail**：職稱末段職務詞優先於前段 context（「連鎖門市**人資專員**」→ 人資）。
- **agency 公司**：派遣/人力/顧問公司的行業 ≠ 職缺本身職類。
- **擦邊保留**：寧可多留相關項，只判「明確錯的」為錯 —— 評推薦精準度時同理，「沾邊」不應計為全錯，建議設計 命中/沾邊(同中類或同大類)/無關 三級。

---

## 六、建議產出物

1. `job-classification-kb/analysis_推薦精準度_報告.md` — 最終報告（統計表 + Mermaid 圖 + 質性抽樣結論）。
2. 分析腳本放 `job-classification-kb/scripts/`（可重跑、參數化）。
3. 若需中繼彙整資料（如「職缺名稱去重後的 unique 對照」），存成新的 `data_*.md` 於 `tcode/` 或 scratchpad，並在報告註明。
4. **不要**產出 Excel，除非使用者明確要求。

## 七、範圍限制

- 只做「推薦 vs 現有」精準度驗證與樣態分析；**不要**回寫/修改主資料檔或代碼表。
- 不要動 `不合理清單_職類校正.md`（那是另一條工作流的資料層）。
- 改動前先讀 `job-classification-kb/CLAUDE.md` 的鐵則。
