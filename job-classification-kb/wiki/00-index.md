# 00 — 總索引 (Master Index)

> 用關鍵字快速定位文件。Ctrl+F 你要找的詞。

## 關鍵字 → 文件對照

| 你想找… | 看這份 |
|---|---|
| 整個專案在幹嘛 | [01-project-overview](01-project-overview.md) |
| 怎麼跑、改完怎麼套用 | [02-workflow](02-workflow.md) |
| 「正解」「中類」「葉」是什麼 | [03-glossary](03-glossary.md) |
| plan() 怎麼決定槓哪格、補哪格 | [../logic/01-plan-algorithm](../logic/01-plan-algorithm.md) |
| 哪些判斷已經確認是對的 | [../logic/02-verified-logic](../logic/02-verified-logic.md) |
| 以前犯過什麼錯、不要再犯 | [../logic/03-pitfalls](../logic/03-pitfalls.md) |
| 某個 eNo 為什麼這樣判 | [../logic/04-case-decisions](../logic/04-case-decisions.md) |
| tCode 有哪些表、各做什麼用 | [../tcode/00-tcode-index](../tcode/00-tcode-index.md) |
| tCode 欄位、CodeType 階層 | [../tcode/01-schema](../tcode/01-schema.md) |
| 怎麼把某張表變成 MD | [../tcode/02-analysis-recipes](../tcode/02-analysis-recipes.md) |
| 職務表 NM/HL/PT 差在哪 | [../tcode/03-duty-tables](../tcode/03-duty-tables.md) |
| 讀寫 Google Sheet | [../skills/google-sheets-skill](../skills/google-sheets-skill.md) |

## 概念關鍵字（語意規則）

| 規則關鍵字 | 說明 | 詳見 |
|---|---|---|
| `keep` | 正解已在現有、無錯誤項 → 不動 | [logic/01](../logic/01-plan-algorithm.md) |
| `keep_strike` | 正解已在、但要槓掉旁邊錯誤項 | [logic/01](../logic/01-plan-algorithm.md) |
| `replace` | 槓一格錯的、放正解 | [logic/01](../logic/01-plan-algorithm.md) |
| `replace_multi` | 槓主錯項+不相關雜項，正解放主格 | [logic/01](../logic/01-plan-algorithm.md) |
| `replace_all` | 現有全錯 → 全槓、正解放第一格 | [logic/01](../logic/01-plan-algorithm.md) |
| `add` | 有空格 → 直接補正解 | [logic/01](../logic/01-plan-algorithm.md) |
| 辦公室類 (OFFICE_MID) | 正解屬此類 → 一般行政可寬鬆保留 | [logic/01](../logic/01-plan-algorithm.md) |
| function tail | 職稱末段職務詞優先於前段 context | [logic/02](../logic/02-verified-logic.md) |
| agency 公司 | 派遣/人力/顧問公司 → 行業≠職缺 | [logic/02](../logic/02-verified-logic.md) |
| 語言保護/主動補 | 職稱有語言 → 翻譯職類保護或補上 | [logic/02](../logic/02-verified-logic.md) |
| 管理詞保護 | 職稱有幹部/組長 → 管理職類受保護 | [logic/02](../logic/02-verified-logic.md) |
| 機構行政共存 | 長照/醫療/學校 → 行政項目可共存 | [logic/02](../logic/02-verified-logic.md) |
| 職稱拆解 | 居服組長 = 居服 + 組長，各自保護 | [logic/02](../logic/02-verified-logic.md) |

## tCode 表關鍵字

> ⚠️ **查 tCode 內容先讀 MD，不要直接讀 Excel。** 下表「現成 MD」欄有檔的直接讀；標 ⬜ 的先 `python3 scripts/tcode_to_md.py <表名>` 匯出再讀。完整對照見 [tcode/00-tcode-index §資料層 MD 對照](../tcode/00-tcode-index.md#資料層-md-對照先讀-md不要直接讀-excel)。

| 表名 | 一句話用途 | 葉數 | 現成 MD |
|---|---|---|---|
| tCodeDutyNM | **職務小類（全職）** — 本專案主用 | 614 | ✅ [data](../tcode/data_tCodeDutyNM.md) |
| tCodeDutyPT | 職務（兼職 part-time） | 525 | ✅ [data](../tcode/data_tCodeDutyPT.md) |
| tCodeCompSkill | 電腦/工作技能 | 765 | ✅ [data](../tcode/data_tCodeCompSkill.md) |
| tCodeBenefit | 福利（B 公司>福利制度） | 85 | ✅ [data](../tcode/data_tCodeBenefit.md) |
| tCodeCertify | 證照 | 2,451 | ◑ [摘要](../tcode/data_tCodeCertify_summary.md) |
| tCodeWorkAbility | 工作能力／職能 | 1,093 | ◑ [摘要](../tcode/data_tCodeWorkAbility_summary.md) |
| tCodeDutyHL | 職務（精簡/高階版） | 77 | ⬜ 需 export |
| tCodeDutyST | 職務（學生/短期？） | 219 | ⬜ 需 export |
| tCodeDutyTU | 職務（家教 tutor） | 199 | ⬜ 需 export |
| tCodeCity | 縣市鄉鎮 | 999 | ⬜ 需 export |
| tCodeCollege | 學校 | 213 | ⬜ 需 export |
| tCodeMajor | 科系 | 183 | ⬜ 需 export |
| tCodeMRT | 捷運站 | 275 | ⬜ 需 export |
| tCodeNation | 國家 | 196 | ⬜ 需 export |
| tCodeTrade | 行業別 | 289 | ⬜ 需 export |

詳見 [tcode/00-tcode-index](../tcode/00-tcode-index.md)。
