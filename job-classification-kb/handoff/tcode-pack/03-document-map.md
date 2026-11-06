# 03 — 文件地圖（要做什麼 → 看哪份）

> 每一行都是本次打包時用 `[ -f path ]` 逐檔核對過的結果（2026-11-06）。路徑相對於 repo 根目錄 `/home/user/main`。不存在的檔案標「❌ 已不存在」，不要照抄進新文件裡當作現有資源。

## 查某張表現況

| 要查哪張表 | 看哪份 | 存在狀態 |
|---|---|---|
| tCodeDutyNM | `job-classification-kb/tcode/data_tCodeDutyNM.md` | ✅ 存在 |
| tCodeDutyPT | `job-classification-kb/tcode/data_tCodeDutyPT.md` | ✅ 存在 |
| tCodeDutyST | `job-classification-kb/tcode/data_tCodeDutyST.md` | ✅ 存在 |
| tCodeDutyHL | `job-classification-kb/tcode/data_tCodeDutyHL.md` | ✅ 存在 |
| tCodeBenefit | `job-classification-kb/tcode/data_tCodeBenefit.md` | ✅ 存在 |
| tCodeCompSkill | `job-classification-kb/tcode/data_tCodeCompSkill.md` | ✅ 存在 |
| tCodeCertify | `job-classification-kb/tcode/data_tCodeCertify_summary.md`（中類摘要，非完整表；**內容落後，見 `04-known-facts.md`**） | ✅ 存在但內容落後 |
| tCodeWorkAbility | `job-classification-kb/tcode/data_tCodeWorkAbility_summary.md`（中類摘要，非完整表；**內容落後，見 `04-known-facts.md`**） | ✅ 存在但內容落後 |
| tCodeDutyTU／City／College／Major／MRT／Nation／Trade | 無現成 MD，需先 `python3 scripts/tcode_to_md.py <表名>` 從 `TCode_Export.xlsx` 匯出 | ⬜ 未產出 |
| 總表／選表指南／15 表一覽 | `job-classification-kb/tcode/00-tcode-index.md` | ✅ 存在 |

**鐵則（原文抄自 `00-tcode-index.md`）**：先看有沒有現成 `data_*.md`；有就讀 MD，不要直接 `load_workbook` 讀 Excel。只有「尚未產出」的表才需先跑 `scripts/tcode_to_md.py` 匯出。

## 產公告／異動清單

| 要做什麼 | 看哪份 | 存在狀態 |
|---|---|---|
| 發公告（公司內部異動公告格式） | `.claude/skills/tcode-excel-ops`（slash: `/tcode-bulletinboard`），規則本體 `.claude/skills/tcode-excel-ops/references/bulletinboard-rules.md` | ✅ 存在（已完整複製於本包 `05-skills-bundle/tcode-excel-ops/`） |
| 比對兩版匯出檔、產異動清單 xlsx、驗證 ChangeType | 同上 skill，另見 `references/compare.py`、`references/export-schema.md`、`references/changetype-rules.md`、`references/markdown-output.md` | ✅ 存在 |

## 某一輪異動的逐表明細、工程交辦紀錄

| 批次 | 看哪份 | 存在狀態 |
|---|---|---|
| tCodeDuty 系列（NM/PT/ST/HL）工程需求追蹤，含 20260707／20261102 複查結果 | `job-classification-kb/tcode/change_request_tCodeDuty_engineering.md` | ✅ 存在 |
| tCodeDuty 20260821 驗收檔（大量 move/move_edit 明細） | `job-classification-kb/tcode/20260821_change_summary.md` | ✅ 存在 |
| tCodeDuty / Certify ChangeType 跨表同步檢查 | `job-classification-kb/tcode/data_tCodeDuty_changetype_sync.md` | ✅ 存在 |
| tCodeDutyNM 校正討論表（待議新增／改名／合併建議） | `job-classification-kb/tcode/data_tCodeDutyNM_changes.md` | ✅ 存在 |
| tCodeBenefit 異動對照 | `job-classification-kb/tcode/tCodeBenefit_change_comparison.md` | ✅ 存在 |
| tCodeBenefit 顯示排序對照 | `job-classification-kb/tcode/tCodeBenefit_排序對照表.md` | ✅ 存在 |
| **tCodeCertify AI 證照新增／改名需求表** | `job-classification-kb/tcode/change_request_tCodeCertify_AI_certs.md` | ❌ **已不存在**（曾建立於 commit `d275a54`，使用者指示「刪掉這個檔案這個output不需要在repo」後於 `ef77f0a` 刪除；內容只存在於該次對話紀錄中，repo 裡查不到） |
| 2026-11-06 批（Certify AI 證照 12 筆 + DutyHL 1 筆整併 + WorkAbility 310000 大類 14 筆新增）合併需求表 | **只存在於出產該批次那個 session 的 scratchpad**（`tcode_change_request_20261106.md`），**不在 repo 內**，本 KB 分支找不到對應檔案 | ❌ 不在 repo（見 `07-open-questions.md`） |

## 全表欄位結構、分析手法、SOP

| 要查什麼 | 看哪份 | 存在狀態 |
|---|---|---|
| 全表欄位結構定義（schema） | `job-classification-kb/tcode/01-schema.md` | ✅ 存在 |
| 常用分析手法（recipes） | `job-classification-kb/tcode/02-analysis-recipes.md` | ✅ 存在 |
| DutyNM/HL/PT/ST/TU 子集差異對照 | `job-classification-kb/tcode/03-duty-tables.md` | ✅ 存在 |
| 公司內部協作 SOP／流程圖 | `job-classification-kb/tcode/04-change-workflow-sop.md` | ✅ 存在 |

## 原始 Excel 與舊版 skill 指標

| 項目 | 路徑 | 存在狀態 |
|---|---|---|
| 官方匯出原始檔 | `job-classification-kb/TCode_Export.xlsx`（15 張工作表） | ✅ 存在 |
| 舊版分支內 skill 指標（已併入 `.claude/skills/tcode-excel-ops`） | `job-classification-kb/skills/tcode-bulletinboard.md`（一行指標，不含內容） | ✅ 存在（僅一行指標） |
| 舊版分支本地 skill 檔（已刪除） | `.claude/skills/tcode-bulletinboard/SKILL.md` | ❌ 已不存在（main 把內容併入 `tcode-excel-ops` 後，此分支已刪除對應的本地 pointer skill） |

## 這份文件地圖本身的侷限

- 只核對了「檔案存不存在」，**沒有**核對每份文件「內容是否最新」——內容新鮮度請看 `04-known-facts.md`。
- 原始 `04-change-workflow-sop.md`〈三、相關文件地圖〉是本檔的精簡版本，兩者同步維護；本檔是打包給 Handoff 助手的完整版，多列了已刪除／已搬移的路徑及其狀態。
