# 00 — tCode 代碼表總覽 (Index & Purpose)

> `TCode_Export_20260622.xlsx`，15 張工作表。所有表共用同一套 schema（見 [01-schema](01-schema.md)）。本頁是用途對照與選表指南。

## 15 張表一覽

| 表名 | 用途（一句話） | 列數 | 葉數 | 葉 CodeType | 中類數 |
|---|---|---|---|---|---|
| **tCodeDutyNM** | **職務小類（全職 Normal）— 本專案主用** | 691 | 614 | 3 | 58 |
| tCodeDutyHL | 職務（精簡/高階 HL，77 葉精選） | 135 | 77 | 3 | 41 |
| tCodeDutyPT | 職務（兼職 Part-Time） | 602 | 525 | 3 | 59 |
| tCodeDutyST | 職務（ST，219 葉） | 286 | 219 | 3 | 48 |
| tCodeDutyTU | 職務（家教 TUtor） | 214 | 199 | 3 | 18 |
| tCodeCertify | 證照／認證 | 2,621 | 2,451 | 3 | 149 |
| tCodeCompSkill | 電腦／工作技能（Word, Excel…） | 790 | 765 | 2 | 26 |
| tCodeWorkAbility | 工作能力／職能（談判、營運分析…） | 1,208 | 1,093 | 3 | 94 |
| tCodeCity | 縣市／鄉鎮區 | 1,077 | 999 | 3 | 67 |
| tCodeCollege | 學校／大專院校 | 235 | 213 | 3 | 21 |
| tCodeMajor | 科系／學門 | 216 | 183 | 3 | 25 |
| tCodeMRT | 捷運站 | 292 | 275 | 3 | 13 |
| tCodeNation | 國家／地區 | 224 | 196 | 3 | 23 |
| tCodeTrade | 行業別 | 372 | 289 | 3 | 67 |
| tCodeBenefit | 福利項目 | 95 | 85 | 2 | 10 |

## 資料層 MD 對照（先讀 MD，不要直接讀 Excel）

> **鐵則**：要查某張 tCode 表的內容，**先看下表有沒有現成 `data_*.md`**；有就讀 MD。
> 只有「尚未產出」的表才需先跑 `python3 scripts/tcode_to_md.py <表名>` 由 `TCode_Export.xlsx` 匯出，匯出後一樣讀 MD。**不要為了查值直接 `load_workbook` 讀 Excel。**

| 表名 | 現成 MD | 狀態 |
|---|---|---|
| tCodeDutyNM | [`data_tCodeDutyNM.md`](data_tCodeDutyNM.md) | ✅ 完整（20260701 已依 Google Sheet 即時匯出更新，617葉，含已套用 add/edit） |
| tCodeDutyPT | [`data_tCodeDutyPT.md`](data_tCodeDutyPT.md) | ✅ 完整（20260701 已依 Google Sheet 即時匯出更新，528葉） |
| tCodeDutyHL | [`data_tCodeDutyHL.md`](data_tCodeDutyHL.md) | ✅ 完整（20260701 新產出，Google Sheet 即時匯出，79葉） |
| tCodeDutyST | [`data_tCodeDutyST.md`](data_tCodeDutyST.md) | ✅ 完整（20260701 新產出，Google Sheet 即時匯出，219葉） |
| tCodeCompSkill | [`data_tCodeCompSkill.md`](data_tCodeCompSkill.md) | ✅ 完整 |
| tCodeBenefit | [`data_tCodeBenefit.md`](data_tCodeBenefit.md) | ✅ 完整（含 CodeNo/CodeNoNew，供 B 公司>福利制度） |
| tCodeCertify | [`data_tCodeCertify_summary.md`](data_tCodeCertify_summary.md) | ◑ 中類摘要（大表，葉太多） |
| tCodeWorkAbility | [`data_tCodeWorkAbility_summary.md`](data_tCodeWorkAbility_summary.md) | ◑ 中類摘要 |
| tCodeDutyTU | — | ⬜ 未產出，需先 export |
| tCodeCity | — | ⬜ 未產出，需先 export |
| tCodeCollege | — | ⬜ 未產出，需先 export |
| tCodeMajor | — | ⬜ 未產出，需先 export |
| tCodeMRT | — | ⬜ 未產出，需先 export |
| tCodeNation | — | ⬜ 未產出，需先 export |
| tCodeTrade | — | ⬜ 未產出，需先 export |

> **待議新增／改名建議**（尚未寫入正式代碼表）：[`data_tCodeDutyNM_changes.md`](data_tCodeDutyNM_changes.md) — 20260420 討論表整理的 5 筆新增、30 筆改名（含 3 筆中類層級改名）。
> **四表 ChangeType 同步檢查**（20260701）：[`data_tCodeDuty_changetype_sync.md`](data_tCodeDuty_changetype_sync.md) — 比對 Google Sheet 即時匯出中 NM/PT/ST/HL 四表已套用的 add/edit，找出跨表沒同步的項目（如 250510~250514 語言老師搬遷只有 PT 標記、NM 沒套用）。

## 選表指南

| 你要處理… | 用哪張表 |
|---|---|
| 職缺的「職務小類」（全職） | **tCodeDutyNM** |
| 兼職職缺職務 | tCodeDutyPT |
| 家教科目 | tCodeDutyTU |
| 求職者證照 | tCodeCertify |
| 求職者會的軟體/技能 | tCodeCompSkill |
| 求職者職能/能力標籤 | tCodeWorkAbility |
| 工作地點 | tCodeCity（行政區）/ tCodeMRT（捷運） |
| 學歷（學校/科系） | tCodeCollege / tCodeMajor |
| 公司行業分類 | tCodeTrade |
| 公司福利 | tCodeBenefit |
| 外語/國籍 | tCodeNation |

## DutyNM 大類 → 中類 結構（職務表核心）

職務表三層：大類(CodeNameC) > 中類(CodeNameB) > 葉(CodeNameA)。21 個大類、58 個中類、614 葉。完整清單見 [03-duty-tables](03-duty-tables.md)。**OFFICE_MID（辦公室類白名單）對應的中類**散落在「管理幕僚／人資／行政」「行銷／企劃／專案管理」「業務／貿易／客服／門市」「金融保險／財會／稽核」「法務專利／顧問諮詢」「影視傳媒／出版翻譯」等大類下。

## 注意

- 各表 ChangeType 在 20260622 版全為 `UnChange`（無待處理異動）。若拿到含 新增/改名/合併 的版本，見 [tcode-excel-ops skill](../skills/) 與 [01-schema](01-schema.md) 的 ChangeType 說明。
- DutyNM / HL / PT / ST / TU 是**同一套職類的不同子集/版本**，中類名稱大致共用，葉的收錄範圍不同。比對差異見 [03-duty-tables](03-duty-tables.md)。
