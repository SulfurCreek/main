# 履歷驗證報告：單份履歷 × 15 職缺｜2026-10-17｜model_id: gemini-4-argon｜human_calibration: not_run

## 1. 結論（≤6 行，先講答案）
- 招聘決定分布（interview／clarify_first／not_matched／insufficient_info 各幾份職缺）：`interview` 11 份（`jd03, jd09, jd11, jd14, jd26, jd30, jd32, jd34, jd36, jd44, jd47`）／`clarify_first` 4 份（`jd20, jd31, jd40, jd43`）／`not_matched` 0 份／`insufficient_info` 0 份。
- Level 分布（列出每個 Level 的職缺數；不算平均）：**Level 8 共 7 份**（`jd03, jd09, jd11, jd30, jd32, jd34, jd47`）；**Level 7 共 8 份**（`jd14, jd20, jd26, jd31, jd36, jd40, jd43, jd44`）；嚴格執行硬性規則 2，進行中未上線案例（如內部封測中之信件與即時通整合、搜尋改版）與未附成效數字之交付項目不撐起 Level 9。
- 最適合投遞的 5 份職缺代號與一句理由：**`jd32`**（現任同業招募系統 PO，負責前後端分離改版、資料欄位對照與跨 10 單位需求收斂，且將處理週期由 100.4 天降至 30.9 天）、**`jd11`**（近 10 年 PM 且直接具備 HR 招募系統群組權限、Scrum/Kanban 與 3 項 AI 生成推薦功能上線經驗）、**`jd30`**（具備 KOOL 網紅媒合平台 0 到 1 規劃與 Claude Code 協作流程轉譯工程條件實務）、**`jd34`**（具備逾 6 萬家企業平台 PO、大客戶分店群組權限、Scrum 及訂閱點數與 CodaPay 金流經驗）、**`jd03`**（具備 Peach 內購轉網頁付款占營收升至 80%+、CodaPay 跨國串接與帳號防冒用驗證實績）。
- 最可能被卡的 3 份職缺代號與卡在哪個條件：**`jd20`**（必備條件要求「5-8年以上B2B/B2G經驗」與「自行使用SQL/BI查詢解讀數據」，目前純 B2B 約 4 年且須與 DBA 協作取數）、**`jd40`**（核心職責要求參與「KA 客戶與 NRE 客製化專案交付管理」，履歷未呈現外部客戶合約範疇與 NRE 需求變更控管證據）、**`jd31`**（核心職責第 1、2 項要求「直接與客戶進行需求訪談」與「業務售前產品展示 Pre-sales」，履歷需求多由內部 10 個單位轉交）。

## 2. 職缺矩陣（每列一份職缺，不加總）
| 職缺 | 決定／Level | 六維度（簡寫：強/足/待/未） | 決定性條件（≤20 字） | 約談理由第一名（≤20 字） |
| :-- | :-: | :-: | :-- | :-- |
| [jd03 產品經理 (Pi錢包)｜拍付國際](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F91sgi) | interview／Level 8 | 足/強/強/強/強/強 | 2年PM＋PRD與金流API串接 | 內購轉網頁付款占營收升至80%以上 |
| [jd09 產品經理 Product Manager｜微拓科技 (beBit TECH)](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F82slf) | interview／Level 8 | 強/強/強/足/強/強 | 3年軟體PM＋B2B SaaS經驗 | 主責服務逾6萬家付費廠商之企業系統 |
| [jd11 【北士科】Product Manager｜沛思坦 (Pacston)](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F8o3s3) | interview／Level 8 | 強/強/強/足/強/強 | 5年PM與HR/AI產品經驗 | 規劃企業招募系統群組權限與AI推薦 |
| [jd14 D441 MyVideo影音產品Growth PM｜台灣大哥大](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F94le0) | interview／Level 7 | 足/足/強/強/強/強 | 3年Growth PM與轉換留存實驗 | iOS定價實驗使相對營收多28% |
| [jd20 Senior Product Manager (Anti-Scam BU/2B)｜Gogolook](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F950oe) | clarify_first／Level 7 | 足/待/強/足/強/強 | 5-8年B2B經驗與獨立SQL查詢 | 處理廠商帳號冒用危機至10月零復發 |
| [jd26 全支付- Product Manager (專案執行)](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F7996v) | interview／Level 7 | 足/足/足/強/強/強 | Axure規劃與跨部門/法遵交付 | 具Axure且主責50項大功能上線 |
| [jd30 資深產品經理｜Senior Product Manager｜USPACE](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F8bymx) | interview／Level 8 | 足/強/強/強/強/強 | 0到1完整週期與Claude協作 | 0到1規劃KOOL且具AI協作流程 |
| [jd31 資深產品經理【擴編】｜人易科技 (NUEIP)](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F92io8) | clarify_first／Level 7 | 強/足/強/足/強/強 | 直接客戶訪談、售前支援與多系統串接 | 規劃企業端群組權限解決大客戶痛點 |
| [jd32 產品專案經理(內部系統)｜104人力銀行](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F94n8b) | interview／Level 8 | 強/強/強/強/強/強 | 網站開發/SA經驗與運用AI工具分析 | 現任招募系統PO主導改版與迭代 |
| [jd34 SaaS 產品經理 / Product Owner｜91APP](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F8dbp3) | interview／Level 8 | 強/強/強/強/強/強 | 2年PM及金流/會員/促購功能開發 | 經手6萬廠商系統與訂閱點數金流機制 |
| [jd36 全支付- Product Manager (內部系統、串接)](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F8ocje) | interview／Level 7 | 強/足/強/強/強/強 | 3年經驗、內部作業優化與API串接 | 重構新舊系統並行架構並串接海外金流 |
| [jd40 【PMC】軟體產品經理 (PM / TPM)｜QuickClick快一點](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F94fod) | clarify_first／Level 7 | 足/足/強/足/強/強 | 5年技術產品經驗與KA/NRE交付管理 | 具備前後端分離改版與第三方金流串接 |
| [jd43 Product Manager (Messenger \& OA)｜LINE Taiwan](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F95jyg) | clarify_first／Level 7 | 足/足/強/強/強/強 | 5年科技PM、帳號安全防詐與跨國合作 | 協調處理招募帳號遭冒用與登入驗證 |
| [jd44 \[Music\] Senior Product Planner｜KKBOX (KKCompany)](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F93qa8) | interview／Level 7 | 足/足/強/強/強/強 | 3年網路PM、0到1經驗與AI功能上線 | 具訂閱制App定價實驗與AI功能上線 |
| [jd47 產品經理｜Product Manager｜USPACE](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F95mvt) | interview／Level 8 | 足/強/強/強/強/強 | 0到1與成熟產品迭代、內部教育訓練 | 兼顧0到1產品與6萬廠商成熟系統迭代 |

## 3. 職缺分群（依職缺內容自行分，最多 5 群）
| 群組 | 職缺代號 | 共同優勢 | 共同卡關 |
| :-- | :-- | :-- | :-- |
| **A. B2B SaaS／企業級系統與 HR Tech** | `jd09, jd11, jd31, jd32, jd34` | 現任 1111 企業端招募系統專案負責人（服務逾 6 萬家活躍付費廠商），主導前後端分離新架構改版、針對大型客戶部門／分店分工規劃「群組功能」於 2025/09 上線、上線 3 項 AI 生成與推薦功能，且具備每週一 Sprint 之 Scrum 與 Kanban 經驗。 | 1111 上線之新版第一階段、群組功能與 AI 推薦未列出上線後的客戶採用率或留存數據；缺乏第一線跟隨業務拜訪外部企業客戶（Pre-sales/BD）與實體零售 OMO 物流庫存描寫。 |
| **B. 支付金流／內部系統與第三方串接** | `jd03, jd26, jd36, jd40` | 具備 Peach 內購轉網頁付款（占營收由 24% 升至 80% 以上）、CodaPay 東南亞電信帳單與超商付款串接、抽成稅費實收試算、新舊系統並行資料欄位對照，以及透過互動原型與 FAQ 向客服業務說明功能之實績。 | 專案管理工具列「內部工單與看板系統、Notion、Trello」，未直接點名 `Jira、Confluence`；金流偏商戶端聚合支付串接，缺乏銀行專線、電子支付機構內部清算與 KA/NRE 合約管理證據。 |
| **C. 0-1 創新／AI 工具賦能與營運成長** | `jd30, jd47` | 同時具備 KOOL 網紅媒合平台從 0 到 1 規劃（案主與網紅雙邊需求釐清、VIP 訂閱與點數付費牆）與 1111 成熟系統 50 項大功能迭代；以 Claude Code 建立協作流程與共用 skill，將業務規則轉為可與工程討論的條件描述。 | 必備條件要求「理解 API、JSON 與基本 SQL」，履歷雖證明懂資料表與欄位結構，但取數為與 DBA 協作撈取且未明寫 `JSON` 字樣；KOOL 未在本版列出上線後用戶與報名規模數字。 |
| **D. 訂閱制消費平台／Growth 與內容娛樂** | `jd14, jd44` | 具備約 6 年交友與訂閱制內容 App 經驗、馬來西亞 iOS 降價三階段對照實驗（各期 21 天，iOS +5% vs Android -18%，相對多 28%）、Juicy 6 週內男性 DAU 由 3,200 增至 1.25 萬、網頁付款轉換提升等實證。 | 成長與定價實驗集中於 2018–2022 年；缺乏 `Firebase` 操作紀錄，且近 4 年在 1111 較少呈現 A/B Test 與漏斗轉換率數據。 |
| **E. 跨國防詐資安／大型通訊與 2B 解決方案** | `jd20, jd43` | 具備 2026/04 廠商招募帳號遭冒用之危機處理與登入驗證調整閉環（至 2026/10 未再出現同類冒用）、信件與即時通整合（已進入公司內部封測）、TOEIC 980、赴美交換與 7 國市場在地化協作經驗。 | 純 B2B 產品經驗約 4 年（未滿 `jd20` 5-8 年 B2B 門檻）、跨國團隊協作停留於 2016–2021 年、信件與即時通整合尚在封測中（預計 2026/11 底上線），且未明列 Confluence、Jira。 |

## 4. 跨職缺重複出現的缺口（≥3 份職缺出現才列；≤6 項）
| 缺口 | 出現職缺數 | 影響哪類職缺 | 履歷原句（≤40 字） | 需要候選人補什麼事實 |
| :-- | :-: | :-- | :-- | :-- |
| **1. 1111 企業端功能與 KOOL 缺乏上線後採用／業務成效指標** | 12 份（`jd03, 09, 11, 14, 20, 30, 31, 34, 40, 43, 44, 47`） | 重視數據驅動、產品效益評估與商業成長之職缺 | `整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線。` | 補充 1111「群組功能」、「新版第一階段」、「AI 推薦人才」以及尚凡「KOOL 平台」上線後的實際客戶採用家數、網紅與報名規模、使用率或推薦轉換數據。 |
| **2. 缺乏 SQL 獨立查詢與 JSON/API 格式實務細節** | 7 份（`jd03, 20, 30, 31, 36, 40, 47`） | 要求自行撈取數據或強調技術架構深度之 PM 職缺 | `擬定資料表與欄位需求，與 DBA 協作取數` | 補充本人是否能撰寫基礎 SQL（如 `SELECT / JOIN`）查詢資料庫，以及在 API 串接規劃中是否實際定義或檢視過 JSON 欄位結構、狀態碼與錯誤處理邏輯。 |
| **3. 專案管理工具未明列 Jira 與 Confluence** | 5 份（`jd11, 20, 26, 36, 43`） | 明文將 Jira、Confluence 列為必備條件之團隊 | `Figma、Axure RP、Notion、Trello、內部工單與看板系統` | 若曾使用過 Jira 或 Confluence 請直接補入技能欄；若僅使用內部工單與看板系統，可於面試說明其權限、狀態流轉與看板管理邏輯如何對應 Jira。 |
| **4. 缺乏第一線對接外部企業客戶（BD/Pre-sales/KA）描寫** | 5 份（`jd09, 20, 26, 31, 40`） | B2B SaaS、KA/NRE 專案、業務售前支援之職缺 | `對接工程、行銷、業務與客服等 10 個需求單位。` | 補充在規劃大型客戶「群組功能」或處理重大需求時，是否曾親自參與外部企業客戶訪談、協同業務進行售前展示（Pre-sales），或管理外部客戶需求變更。 |
| **5. 近期（2022–2026）缺乏 A/B Test 與成長漏斗實驗案例** | 4 份（`jd14, 30, 43, 44`） | Growth PM 與強調持續實驗驗證假設之消費級產品職缺 | `設計馬來西亞 iOS 定價實驗，以售價不變的 Android 作對照（2021/05–08）` | 補充在 1111 任職期間（如搜尋結果頁優化、職缺生成、登入改版）是否有透過 GA4、分流測試（Bucket/A/B test）或漏斗轉換率來驗證改版成效。 |
| **6. 進行中專案（即時通整合、搜尋改版）尚未產出最終上線結果** | 4 份（`jd09, 11, 32, 43`） | 重視即時通、搜尋體驗與近期大型交付成果之職缺 | `兩案均在開發中，信件與即時通整合已進入公司內部封測，預計 2026/11 底上線。` | 依硬性規則 2，開發中案例僅支持決策取捨（`decision`）而不計入已實現成果（`outcome`）；請準備內部封測目前已收集到的量化測試指標與舊版工單基準線供面試驗證。 |

## 5. 評語（合併後）

### 5.1 做得好（3 點；每點至少 2 份職缺支持，附原句與職缺代號）
1. **位置**：工作經歷 - 尚凡國際創新科技（第 3、4 點）
   - **原句**：`設計馬來西亞 iOS 定價實驗，以售價不變的 Android 作對照，依序測試原價、降價與還原原價（2021/05–08，各期 21 天）。降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%，相對變化約多 28%`；`2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上。`
   - **支持職缺**：`jd03, jd09, jd14, jd30, jd34, jd43, jd44, jd47`
   - **為什麼有用**：清楚交代實驗設計（對照組排除季節性干擾）、時間跨度（各期 21 天）、比較基準與最終商業決策（團隊依結果決定採用低價），並搭配內購轉網頁付款占比提升至 80%+ 的變現成果，完整展示數據驅動與商業推論能力。
2. **位置**：工作經歷 - 1111 全球華人（導言與第 1、2 點）
   - **原句**：`推動系統改版至前後端分離的新架構，採新舊並行、分階段上線`；`接手重啟的求才系統改版，保留既有設計理念，重新制定業務流程、對照資料欄位並重構規格，處理新舊系統並行的相容性需求`；`針對大型客戶依部門或分店分工的需求，規劃群組功能...整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線。`
   - **支持職缺**：`jd03, jd09, jd11, jd26, jd31, jd32, jd34, jd36, jd40`
   - **為什麼有用**：具體展現資深 PM 處理「遺留系統重構」、「前後端分離改版」、「資料欄位對照與轉換規則」及「B2B 大型客戶部門／分店群組權限架構」的硬實力，對企業級 SaaS 與內部系統翻新職缺極具說服力。
3. **位置**：工作經歷 - 1111 全球華人（第 3、5、7 點）
   - **原句**：`透過互動原型與 FAQ 向客服、業務說明功能`；`廠商招募帳號遭冒用，帶來求職者個資外洩風險。我協調工程與客服，釐清受影響範圍、確認帳號驗證與解鎖流程，於 2026/04 完成登入驗證調整...調整後至 2026/10 未再出現同類冒用`；`2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天。`
   - **支持職缺**：`jd03, jd11, jd20, jd26, jd32, jd36, jd43, jd47`
   - **為什麼有用**：同時呈現清晰的資安防冒用危機應變閉環、PO 治理 10 個需求單位將平均處理時間縮短近 70% 的排程成效，以及運用互動原型與 FAQ 賦能業務與客服的落地交付力。

### 5.2 可改進（≤6 點；欄位依 §6.2；只列 ≥2 份職缺重複或 blocking 的項目）
1. **1111 上線功能與 KOOL 平台缺乏採用與業務成效數據**
   - 位置：工作經歷 - 1111 全球華人（第 1、2、6 點）與尚凡國際（第 1 點）
   - 原句：`整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線。`
   - 問題類型：`measurement`
   - 嚴重度：`interview_follow_up`
   - 影響：在 12 份職缺中，用人主管只能確認「交付完成（`output`）」，無法從本版履歷看到新版系統、群組功能、AI 推薦人才及 KOOL 平台對用戶與業務產生的「實際影響規模（`outcome`）」，也使可追溯量測受限而停在 Level 7–8。
   - 建議方向：在不違反保密原則下，補回真實可核的成效或規模數據（例如：KOOL 網紅檔案數與累計報名次數、1111 群組功能開通廠商數或留存表現、AI 推薦規則調整前後的採用率差異）。
2. **數據查詢與 API 規格的技術深度邊界未明**
   - 位置：專業技能 - 研究與數據／跨部門與系統整合
   - 原句：`擬定資料表與欄位需求，與 DBA 協作取數。`
   - 問題類型：`requirement`
   - 嚴重度：`interview_follow_up`（對 `jd20` 為關鍵釐清項）
   - 影響：`jd20, jd30, jd31, jd40, jd47` 皆要求 SQL、JSON 或深度 API 規格理解；「與 DBA 協作取數」會讓主管追問候選人是否具備基礎 SQL 閱讀與查詢能力。
   - 建議方向：若具備基礎 SQL 語法閱讀或撰寫能力（如 `SELECT / WHERE / JOIN`），建議明寫；並於 API 串接處補充實際負責的規格層級（如定義 Request/Response JSON 欄位或錯誤碼對照）。
3. **B2B 外部企業客戶直接對接與售前／KA 角色不清**
   - 位置：工作經歷 - 1111 全球華人（導言與第 2 點）
   - 原句：`對接工程、行銷、業務與客服等 10 個需求單位。`
   - 問題類型：`ownership`
   - 嚴重度：`interview_follow_up`（對 `jd20, jd31, jd40` 為關鍵釐清項）
   - 影響：B2B 職缺（`jd09, jd20, jd31, jd40`）重視 PM 能否直接面對外部企業客戶進行需求訪談、售前展示（Pre-sales）與 KA 客製化範疇管理；目前寫法看似僅透過內部 10 個單位間接接收需求。
   - 建議方向：補充在規劃大型客戶群組功能或處理重大客訴時，是否曾直接參與企業客戶訪談、問卷調查，或協同業務向客戶確認規格與範疇。
4. **約 50 項大項功能欠缺分類與代表性規模錨點**
   - 位置：工作經歷 - 1111 全球華人（第 3 點）
   - 原句：`約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃。`
   - 問題類型：`readability`
   - 嚴重度：`interview_follow_up`
   - 影響：約 28 個月內上線 50 項「大項功能」（平均每月近 2 項）在企業級系統中頻率極高，用人主管易追問「大項功能」的定義標準與規模分布。
   - 建議方向：簡要說明這 50 項的構成類型（例如：包含幾項核心模組改版、幾項跨系統整合、幾項營運與權限優化）或總處理工單量，讓交付規模更具說服力。
5. **專案管理工具名稱與主流 JD 關鍵字落差**
   - 位置：專業技能 - 工具與技術素養
   - 原句：`Figma、Axure RP、Notion、Trello、內部工單與看板系統`
   - 問題類型：`requirement`
   - 嚴重度：`editorial`
   - 影響：`jd11, jd20, jd26, jd36, jd43` 皆明文點名 `Jira` 與 `Confluence`；若僅寫內部工單與看板系統，在字面條件對照時會被列為 `partial`。
   - 建議方向：若過往曾用過 Jira / Confluence 請直接補上；若無，則保留現有誠實表述並於面試說明內部工單與看板系統之 ticket 狀態流轉與權限管理邏輯。

### 5.3 面試最可能被追問的 5 題（附建議準備的事實，不代答）
1. **【成效衡量】你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際數據表現如何？**
   - **建議準備的事實**：準備各功能的北極星指標與觀測數據（例如：群組功能上線後開通的企業家數、占目標大型客群比例或留存表現；AI 推薦規則依客服測試回饋調整了哪些條件、調整前後的通過率或廠商採用率；新舊系統並行期間的切換率與客訴工單變化）。
2. **【優先級與高層利害關係人管理】面對工程、行銷、業務、客服等 10 個需求單位，以及參與一級主管日會向總經理、副總匯報時，當高層指令與使用者旅程痛點衝突，你如何決定優先級？**
   - **建議準備的事實**：以「2026 Q1 至 Q2 平均處理時間由 100.4 天降至 30.9 天」及「信件與即時通整合排在其他新功能之前、搜尋結果頁痛點排在職缺健檢之前」為例，準備當時評估工單量、影響廠商數、開發人天成本的具體排序依據，以及如何在一級主管日會與各單位間取得共識。
3. **【技術協作與系統架構】在 1111 前後端分離改版與新舊系統並行，以及過去串接 CodaPay 時，你實際處理了哪些資料結構、API 規格或相容性難題？**
   - **建議準備的事實**：準備「舊帳號 E-mail 非唯一值」的驗證流程圖與新舊資料庫欄位對照表；說明新舊系統並行時（2025/10 登入與首頁上線、2026/01 公司資料上線，但其他功能仍在舊版），帳號權限、職缺關聯與資料轉換規則是如何與工程師敲定並完成 UAT 驗收的；同時準備與 DBA 協作取數時的資料表與欄位規格實例。
4. **【B2B 客戶洞察與 0 到 1 需求探索】在企業端產品（如大型客戶群組功能）與 0 到 1 產品（如 KOOL 網紅媒合平台）中，你是如何直接挖掘用戶需求的？有沒有因為訪談或測試回饋而調整原本設計的案例？**
   - **建議準備的事實**：梳理群組功能規劃前，從業務、客服或直接訪談大型企業客戶收集到的「部門／分店分工」真實使用情境（為何原本「全公司／個人」兩種範圍不夠用、權限邊界如何設定）；以及 KOOL 在沒有直接競品可對照下，如何拆解案主與網紅雙邊需求、設計刊案／報名／邀約流程與 VIP／點數付費牆，並準備好 KOOL 上線後的網紅檔案數與報名規模數據。
5. **【AI 協作工作流與資安危機應變】請具體說明你如何「以 Claude Code 建立協作流程與共用 skill，將業務規則轉為可與工程討論的條件描述」？另外 2026/04 廠商帳號遭冒用時，登入驗證調整了什麼？**
   - **建議準備的事實**：準備 1 個使用 Claude Code 與共用 skill 撰寫規格、整理資料並將複雜或衝突業務規則轉化為工程條件的真實案例（輸入什麼、產出什麼、節省多少時間或減少多少漏判）；以及 2026/04 帳號遭冒用事件的受影響範圍盤點、登入驗證與解鎖流程的具體調整內容，以及客服回饋後修正了哪一步操作流程。

## 6. ATS 準備檢查（五塊，不加總）

> **說明**：已針對本次新上傳之實體 PDF 檔案 **`resume-v10.2-twocol.pdf`**（`793,878 bytes`，2 頁，Producer: `Skia/PDF m141` / `HeadlessChrome/141.0.0.0`，建立時間：`2026-10-17 08:34:08 UTC`，SHA-256：`71f037d52ada7e651e5308aff09829dac1c82cde3973b00cb99a173070451a80`）執行本機擷取實測（`pypdf`、`pdfplumber`、`pdftotext`、`pdftotext -layout`；`test_level: local_extraction_only`、`actual_ats_import_performed: false`）。依 **ATS02** 與 **硬性規則 1**，ATS 檢查獨立成段、不併入內容評分，亦不合成「ATS 分數」。
> **重大改善確認**：前次舊版 PDF 出現的**粗體字雙重疊字問題（`聶崑淮聶崑淮`／`kkuunnhhuuaaiinniiee`）在 `resume-v10.2-twocol.pdf` 中已 100% 修復消失**！姓名、職稱、Email（`kunhuainie@gmail.com`）、電話（`0978802871`）與各段落標題在所有解析器中皆能單次乾淨還原。惟本機實測仍檢出 **2 項排版與字型編碼層級的解析風險（標為 `risk`）**：

| 檢查區塊 | 狀態 | 檢查依據與 `resume-v10.2-twocol.pdf` 本機實測結果（ATS01–ATS14） |
| :-- | :-: | :-- |
| 1. 檔案接受 (File Acceptance) | `pass`（本機檔案）／`not_tested`（真實平台） | **ATS01/02/13**：本機檢查 `resume-v10.2-twocol.pdf` 為標準未加密 PDF（`is_encrypted: False`，檔案大小約 775 KB，共 2 頁），完全符合常見 ATS 上傳格式與大小限制；未執行真實平台投遞匯入（`actual_ats_import_performed: false`）。 |
| 2. 欄位解析 (Field Parsing) | **`risk`**（粗體疊字已修復 `pass`；雙欄跨頁斷句與讀序穿插為 `risk`） | **ATS03/04/12**：<br>① **聯絡資訊與標題擷取（`pass`）**：姓名 `聶崑淮`、職稱 `資深產品經理｜Senior Product Manager`、Email `kunhuainie@gmail.com`、電話 `0978802871` 均 100% 正確單次擷取，無任何疊字。<br>② **第 1 頁底部左、右兩欄同時發生「跨頁斷句」與「讀序穿插」（`risk`）**：<br>- **左欄底部斷句**：第 1 頁左欄底部在 `尚凡國際創新科技｜2018/01 - 2022/03` 的導言結尾停在半句話 `...與工程、設計、行銷及海外金流團隊協作完成`，下半句 `上線，正式職稱為 APP 專案管理師。` 與 4 條核心 bullet 則落到第 2 頁頂部。在 `pypdf` 與 `pdftotext` 預設讀序中，左欄讀到 `協作完成` 後，**中間會被插入整欄第 1 頁右欄（專業技能 → 學歷 → 求職條件）**，到了第 2 頁才接回 `上線，正式職稱為 APP 專案管理師。`，導致尚凡經歷的標題與 4 條成果被右欄攔腰截斷。<br>- **右欄底部「求職條件」跨頁孤字**：第 1 頁右欄底部 `求職條件` 寫到 `...｜錄取後三週可` 即滿頁，最後兩個字 **`上班`** 溢流到第 2 頁右上角！在 `pdfplumber` 與 `pdftotext -layout` 中，第 2 頁第 1 行被拼成 `上線，正式職稱為 APP 專案管理師。 上班`；在 `pdftotext` 預設模式中，`上班` 則孤立出現在第 2 頁尚凡國際第 4 條 bullet（Peach 網頁付款）與 `Associate PM｜思維特網路資訊` 之間。<br>- **雙欄橫向同行合併**：在 `pdfplumber` 與 `pdftotext -layout` 中，第 1 頁左欄與右欄同高度的文字仍會被橫向合併為同一行（如 `近 10 年 PM 經驗...網紅媒合平台與 產品文件與設計`）。 |
| 3. 搜尋可見性 (Search Visibility) | **`risk`**（英文關鍵字與 `pdftotext` 為 `pass`；`pypdf`/`pdfminer` 有康熙部首字元風險） | **ATS05/06**：<br>① **英文技術與職能關鍵字（`pass`）**：英文採 `/Type0` `LiberationSans` 字型嵌入，包含 `Product Owner`、`Product Manager`、`PRD`、`User Journey Map`、`User Story`、`Use Case`、`Wireframe`、`Prototype`、`UAT`、`Scrum`、`Sprint`、`Kanban`、`GA4`、`API`、`Figma`、`Axure RP`、`Notion`、`Trello`、`HTML`、`CSS`、`Claude Code`、`AI Agent`、`TOEIC 980`、`AWS` 在所有工具中皆 100% 精準命中。<br>② **中文字型 `/Type3` 康熙部首編碼（`risk`）**：Linux Chromium 將部分中文字型轉為 `/Type3` 子集（第 1 頁 170 個字型物件、第 2 頁 114 個），其中 **35 個常用漢字（全文共出現 174 次）** 的 `ToUnicode` 映射為 **康熙部首區段（Unicode `U+2F00..U+2FD5`，如 `⼯` U+2F2F、`⽤` U+2F64、`⼈` U+2F08、`⼒` U+2F12、`⾏` U+2F8F、`⾴` U+2FB4、`⼾` U+2F3E、`⾨` U+2FA8、`⾦` U+2FA6、`⽂` U+2F42）** 而非一般 CJK 統一表意文字（`U+4E00..U+9FFF`）。在自動做 NFKC 正規化的解析器（如 `pdftotext`）中可 100% 正常檢索；但在未做 Unicode NFKC 正規化的解析器（如 `pypdf`、`pdfplumber`/`pdfminer`）中，直接搜尋一般 UTF-8 字串 `工程`、`使用者`、`人力銀行`、`網頁`、`客戶`、`部門`、`金流` 會因字碼不同（`⼯程` vs `工程`）而無法精確匹配。 |
| 4. 資格與流程條件 (Qualifications & Workflow) | `unknown` | **ATS07/08/10/11**：無外部平台申請表問答欄位與平台中繼資料（標 `unknown`）；履歷內載明之求職條件（雙北、可接受遠端或混合辦公、錄取後三週可上班）與 15 份職缺均無已知衝突。 |
| 5. 匹配功能與未知設定 (Matching & Unknown Config) | `unknown` | **ATS09/14**：雇主後台是否啟用 AI 排序與權重設定未知（標 `unknown`），不合成通用 ATS 分數；若雇主使用未正規化 Unicode 之舊型解析器或單流段落剖析器，第 2、3 塊之跨頁斷句與康熙部首字碼可能影響自動欄位歸類與中文關鍵字完全匹配。 |

## 7. 方法限制、V 階段（截斷文字可見性壓力測試）與 PDF 微調建議
- `model_id`、是否每次都是新 context、實際跑了幾次：
  - `model_id`: `gemini-4-argon`（Gemini 4 Argon）。
  - 實際執行次數：針對最新上傳之 **`resume-v10.2-twocol.pdf`** 完整執行 **單份審查 A 共 15 次**（15 份職缺各 1 次，100% 依據 `resume-v10.2-twocol.pdf` 內文重新取證判讀，不引用舊版履歷已刪除之句子或任何其他對話之分數）＋ **本機多工具 PDF 抽字與 Unicode 字碼檢查 1 次**＋ **V 階段截斷可見性壓力測試 1 次**＋ **跨職缺彙整報告 1 次**。
  - 是否每次都是新 context（限制誠實揭露）：受限於單一代理執行環境，無法開啟 15 個物理隔離的全新對話視窗；本報告於同一執行環境中透過程式化結構隔離逐一針對每份職缺的明文條件獨立取證判讀（嚴格遵守硬性規則 1、2、4、5，不拿 A 職缺條件扣 B 職缺分），並依 §0 規定誠實揭露「非 15 個獨立對話視窗執行」。
- **V 階段（對應套件 §4.4 截斷文字可見性壓力測試與本機抽字測試）**：
  1. **套件 §4.4 遮罩截斷測試（「前 3 行全句＋經歷抬頭前 24 字寬＋其他行只剩開頭 10 字寬，約 1,400 字截斷」）**：
     - **可見項目**：姓名（`聶崑淮`）、目標職稱（`資深產品經理｜Senior Product Manager`）、聯絡資訊（`kunhuainie@gmail.com 0978802871`）、現職抬頭（`Product Owner／PM｜1111 全球華人｜2022/08 - 迄今`）與前段經歷抬頭（`Product Manager｜尚凡國際創新科技｜2018/01 - 2022/03`）均清楚可見；1111 各條開頭（`人力銀行企業端招募系`、`接手重啟的求才系統改`、`針對大型客戶依部門或`、`約 50 項大項功能於`、`依使用者旅程與工單問`、`廠商招募帳號遭冒用，`、`與資料科學團隊合作，`、`統整各單位提出的功能`）能看出改版、大客戶、50 項功能、防冒用與資料科學合作輪廓。
     - **被遮罩／截斷而變 `unknown` 之關鍵證據**：由於每行僅保留開頭 10 字寬且在約 1,400 字處截斷，所有位於句中／句尾的量化結果與具體技術名詞（如 `2025/10 上線`、`2025/09 完成上線`、`100.4 天降至 30.9 天`、`2026/04 完成登入驗證調整`、`公司簡介生成／AI 推薦人才`）以及第 2 頁的 `KOOL 網紅媒合平台`、`馬來西亞 iOS 定價實驗（+5% vs -18%）`、`CodaPay 新加坡串接`、`SweetRing 7 國在地化` 均會落入 `unknown`。
  2. **第 1 頁單頁可見性（`V-1page`）**：
     - 由於採用雙欄排版（左欄放摘要與 1111 經歷，右欄放專業技能、學歷、求職條件），第 1 頁已能同時呈現「1111 完整 7 點經歷」與「完整專業技能（含 Scrum、GA4、DBA 取數、CodaPay、Axure、Claude Code、TOEIC 980、AWS 證照）」，第一頁資訊覆蓋度優於傳統單欄！但「尚凡國際 4 條核心實績（KOOL 0 到 1、Juicy DAU、馬來西亞定價實驗、Peach 網頁付款串接）」與「思維特 7 國在地化」則完全位於第 2 頁。
- **給候選人的 PDF 版面微調建議（僅需微調 CSS 行高或邊距即可消除第 1 頁底部的兩處跨頁斷句）**：
  1. **收回右欄底部溢出的「上班」二字**：目前第 1 頁右欄最底部的 `求職條件` 僅差 2 個字（`上班`）就能完全收進第 1 頁右欄。只要將右欄 `.sidebar` 的段落間距（`margin-bottom`）或行高微調縮減 `1px–2px`，即可讓 `錄取後三週可上班` 完整留在第 1 頁右欄底部，徹底消除第 2 頁右上角的孤字 `上班`。
  2. **避免左欄底部「尚凡國際創新科技」導言跨頁斷句**：目前第 1 頁左欄底部放了 `Product Manager｜尚凡國際創新科技｜2018/01 - 2022/03` 標題與導言前半句（`...與工程、設計、行銷及海外金流團隊協作完成`），下半句（`上線，正式職稱為 APP 專案管理師。`）卻被切到第 2 頁。建議在「尚凡國際創新科技」整個區塊加上 `break-inside: avoid;`（或直接將尚凡國際標題移至第 2 頁頂部），或微調左欄行距讓導言整句在第 1 頁收尾，即可避免句子與經歷被跨頁及右欄切斷。
- 未做：真實 ATS 匯入、真人校準：
  - 真實 ATS 匯入：`not_run`（`actual_ats_import_performed: false`）。
  - 真人校準：`not_run`（`human_calibration: not_run`）。
- 技術失敗或格式修補（保留原始輸出，不改判定）：
  - 無審查 `technical_failure`；15 份單行 JSON 全數通過欄位完整性、`human_calibrated=false`、`ai_authorship.probability=null` 與字數上限（`evidence <= 40`、`application_note <= 30`、`決定性條件 <= 20`、`約談理由第一名 <= 20`）程式檢核。

# 附錄 A：15 份單份審查完整輸出（單行 JSON ＋ §6.2 評語格式）

## 單份審查｜履歷 Resume_v10.2_twocol（jd03 產品經理 (Pi錢包)｜拍付國際）｜第 1 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.2_twocol","job_id":"jd03","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd03-01","human_calibrated":false,"requirements":[{"id":"R01","text":"2年以上獨立PM經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"獨立負責多款B2C與B2B產品規劃與交付"},{"id":"R02","text":"能撰寫PRD/User Story/Wireframe","type":"required","status":"supported","evidence":["設計流程與畫面、撰寫 PRD 與製作 Prototype"],"blocks_interview":false,"reason":"完整具備User Story、Wireframe與PRD實績"},{"id":"R03","text":"理解API串接與系統運作邏輯","type":"required","status":"supported","evidence":["與 CodaPay 新加坡技術團隊協調串接"],"blocks_interview":false,"reason":"具跨國第三方金流API串接與系統分析經驗"},{"id":"R04","text":"金融科技/支付/點數/電子票證/電商經驗","type":"preferred","status":"supported","evidence":["另規劃並上線 VIP 訂閱、點數付費牆與精選曝光"],"blocks_interview":false,"reason":"具網頁付款、點數牆與超商電信帳單支付經驗"},{"id":"R05","text":"政府機關或銀行產品串接經驗","type":"preferred","status":"unknown","evidence":["未呈現銀行或政府機關直接串接紀錄"],"blocks_interview":false,"reason":"僅列第三方聚合支付CodaPay串接"},{"id":"R06","text":"會員經營/用戶留存與數據觀測分析經驗","type":"preferred","status":"supported","evidence":["降價期 iOS 非續訂營收較基準期增 5%"],"blocks_interview":false,"reason":"具訂閱會員定價實驗與世代分析經驗"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["系統服務逾 6 萬家活躍付費廠商（2026 Q3）"],"missing":["近4年主責B2B招募系統，非高頻錢包支付核心"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"強","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"missing":["未呈現銀行或政府機關系統直接串接紀錄"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["廠商反映的溝通中斷問題，使我優先推進信件與即時通整合"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"missing":["1111改版與群組功能未列上線後採用率數字"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"於 2026/04 完成登入驗證調整...至 2026/10 未再出現同類冒用","kinds":["output","outcome"]},{"quote":"兩案均在開發中，信件與即時通整合已進入公司內部封測","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"對位 jd03 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 Product Owner，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["擬定資料表與欄位需求，與 DBA 協作取數"],"application_note":"清楚界定個人規劃與DBA/工程/DS分工"},{"rule_id":"HR04","status":"partial","resume_evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"application_note":"具處理週期與定價實驗數據，缺1111功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與E-mail登入驗證取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端成長型產品演進至B2B大型平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["透過互動原型與 FAQ 向客服、業務說明功能"],"application_note":"Scrum、原型、FAQ教學、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"application_note":"段落清楚，重點指標與背景脈絡易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["產品上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"主動標註行銷導流期間表現與開發中狀態"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd03 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"application_note":"證據鏈完整支持安排 jd03 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["針對大型客戶依部門或分店分工的需求，規劃群組功能"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線的新版第一階段、群組功能與 AI 推薦人才，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["將業務規則轉為可與工程討論的條件描述"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"過去串接 CodaPay 與規劃 Peach 網頁付款時，如何處理交易異常、掉單重試與對帳流程？若改對接銀行端或政府機關，你預期技術與法遵流程有哪些差異？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd03 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定條件或技術工具細節待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"未呈現銀行或政府機關產品直接串接經驗（過往金流為第三方聚合支付 CodaPay 與網頁付款）","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"1111上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 全球華人經歷第 1、2、4、6 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線","reason":"1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗，經手 6 款產品","約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd03","具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗","已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環"],"key_gaps":["未呈現銀行或政府機關產品直接串接經驗（過往金流為第三方聚合支付 CodaPay 與網頁付款）","1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據","資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節"],"strengths":["1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd03 證明遺留系統重構與B2B組織權限設計力","尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd03 展現嚴謹對照實驗與商業變現能力","1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd03 展現資安危機閉環與10單位治理效率"],"interview_questions":["過去串接 CodaPay 與規劃 Peach 網頁付款時，如何處理交易異常、掉單重試與對帳流程？若改對接銀行端或政府機關，你預期技術與法遵流程有哪些差異？","你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？","在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd03 具備多個已實現案例、清楚取捨與跨部門治理實證（惟1111功能缺上線後採用率outcome數據且開發中案例不撐起Level 9，故評為Level 8）"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「網頁付款占營收由 24% 升至 80% 以上」且具 CodaPay 串接經驗，支持約談。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 系統服務逾 6 萬家活躍付費廠商（2026 Q3） | 近4年主責B2B招募系統，非高頻錢包支付核心 |
| role_evidence | 強 | 近 10 年 PM 經驗，經手 6 款產品 | 未呈現銀行或政府機關系統直接串接紀錄 |
| decision_depth | 強 | 廠商反映的溝通中斷問題，使我優先推進信件與即時通整合 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 1111改版與群組功能未列上線後採用率數字 |
| ownership | 強 | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 2年以上獨立PM經驗 | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 獨立負責多款B2C與B2B產品規劃與交付 |
| R02 能撰寫PRD/User Story/Wireframe | 必要 | supported | 設計流程與畫面、撰寫 PRD 與製作 Prototype | 完整具備User Story、Wireframe與PRD實績 |
| R03 理解API串接與系統運作邏輯 | 必要 | supported | 與 CodaPay 新加坡技術團隊協調串接 | 具跨國第三方金流API串接與系統分析經驗 |
| R04 金融科技/支付/點數/電子票證/電商經驗 | 加分 | supported | 另規劃並上線 VIP 訂閱、點數付費牆與精選曝光 | 具網頁付款、點數牆與超商電信帳單支付經驗 |
| R05 政府機關或銀行產品串接經驗 | 加分 | unknown | 未呈現銀行或政府機關直接串接紀錄 | 僅列第三方聚合支付CodaPay串接 |
| R06 會員經營/用戶留存與數據觀測分析經驗 | 加分 | supported | 降價期 iOS 非續訂營收較基準期增 5% | 具訂閱會員定價實驗與世代分析經驗 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 對位 jd03 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 Product Owner，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 擬定資料表與欄位需求，與 DBA 協作取數 | 清楚界定個人規劃與DBA/工程/DS分工 |
| HR04 | partial | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 具處理週期與定價實驗數據，缺1111功能採用率 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現功能優先序與E-mail登入驗證取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端成長型產品演進至B2B大型平台主任 |
| HR07 | supported | 透過互動原型與 FAQ 向客服、業務說明功能 | Scrum、原型、FAQ教學、AI與英文協作皆有實例 |
| HR08 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 段落清楚，重點指標與背景脈絡易讀 |
| HR09 | supported | 產品上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 主動標註行銷導流期間表現與開發中狀態 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd03 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 證據鏈完整支持安排 jd03 面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 針對大型客戶依部門或分店分工的需求，規劃群組功能 | 能針對大客戶部門/分店分工痛點設計群組權限 |
| HM03 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與E-mail登入取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數付費牆與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18% | 定價實驗與處理週期基準清晰，缺1111功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整 | 具新舊系統並行相容、重複信箱驗證與防冒用閉環 |
| HM08 | supported | 將業務規則轉為可與工程討論的條件描述 | 能將業務規則轉為工程條件，惟取數與DBA協作 |
| HM09 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程 | 依客服回饋修正登入操作流程與AI推薦規則 |
| HM12 | supported | 具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd03 明文條件獨立取證判讀 | 僅依 jd03 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd03 |
| 2 | 具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗 |
| 3 | 已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 未呈現銀行或政府機關產品直接串接經驗（過往金流為第三方聚合支付 CodaPay 與網頁付款） | 過去串接 CodaPay 與規劃 Peach 網頁付款時，如何處理交易異常、掉單重試與對帳流程？若改對接銀行端或政府機關，你預期技術與法遵流程有哪些差異？ |
| 2 | 1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據 | 你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？ |
| 3 | 資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節 | 在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd03 證明遺留系統重構與B2B組織權限設計力
- 尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd03 展現嚴謹對照實驗與商業變現能力
- 1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd03 展現資安危機閉環與10單位治理效率

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：未呈現銀行或政府機關產品直接串接經驗（過往金流為第三方聚合支付 CodaPay 與網頁付款）
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落
- 位置：1111 全球華人經歷第 1、2、4、6 點
  - 原句：整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：強

### 8. 未測試聲明
PDF 抽字：risk（本機實測 `resume-v10.2-twocol.pdf` 粗體疊字已完全修復，惟仍有雙欄跨頁斷句與 Type3 康熙部首字元風險） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 Resume_v10.2_twocol（jd09 產品經理 Product Manager｜微拓科技 (beBit TECH)）｜第 2 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.2_twocol","job_id":"jd09","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd09-02","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上軟體產品或專案管理經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"年資與軟體產品交付量充足"},{"id":"R02","text":"B2B SaaS經驗尤佳","type":"preferred","status":"supported","evidence":["系統服務逾 6 萬家活躍付費廠商（2026 Q3）"],"blocks_interview":false,"reason":"近4年主責大型B2B企業端招募系統"},{"id":"R03","text":"熟悉UI/UX概念方法論","type":"required","status":"supported","evidence":["User Journey Map、User Story、Use Case"],"blocks_interview":false,"reason":"具使用者旅程地圖、Wireframe與原型設計經驗"},{"id":"R04","text":"批判性思維與問題拆解","type":"required","status":"supported","evidence":["針對大型客戶依部門或分店分工的需求，規劃群組功能"],"blocks_interview":false,"reason":"拆解大客戶權限痛點與重複信箱驗證限制"},{"id":"R05","text":"數據驅動思維","type":"required","status":"supported","evidence":["使用者訪談與問卷、競品實測、GA4、世代分析"],"blocks_interview":false,"reason":"具三階段定價對照實驗與處理週期追蹤"},{"id":"R06","text":"獨立作業善跨部門溝通","type":"required","status":"supported","evidence":["對接工程、行銷、業務與客服等 10 個需求單位"],"blocks_interview":false,"reason":"獨立統籌50大項功能並跨10單位協作"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["系統服務逾 6 萬家活躍付費廠商（2026 Q3）"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"強","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"missing":["未直接經手 MarTech（CDP+MA+BI）行銷自動化領域產品"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["廠商反映的溝通中斷問題，使我優先推進信件與即時通整合"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"足夠","evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"missing":["1111新系統與群組功能未列上線後廠商採用率或留存數據"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"於 2026/04 完成登入驗證調整...至 2026/10 未再出現同類冒用","kinds":["output","outcome"]},{"quote":"兩案均在開發中，信件與即時通整合已進入公司內部封測","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"對位 jd09 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 Product Owner，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["擬定資料表與欄位需求，與 DBA 協作取數"],"application_note":"清楚界定個人規劃與DBA/工程/DS分工"},{"rule_id":"HR04","status":"partial","resume_evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"application_note":"具處理週期與定價實驗數據，缺1111功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與E-mail登入驗證取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端成長型產品演進至B2B大型平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["透過互動原型與 FAQ 向客服、業務說明功能"],"application_note":"Scrum、原型、FAQ教學、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"application_note":"段落清楚，重點指標與背景脈絡易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["產品上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"主動標註行銷導流期間表現與開發中狀態"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd09 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"application_note":"證據鏈完整支持安排 jd09 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["針對大型客戶依部門或分店分工的需求，規劃群組功能"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線的新版第一階段、群組功能與 AI 推薦人才，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["將業務規則轉為可與工程討論的條件描述"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"你在 1111 規劃企業端「群組功能」與「AI 推薦人才」上線後，實際有多少大型企業開通使用？這套分群與推薦邏輯如何遷移至 CDP+MA 行銷自動化場景？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd09 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定條件或技術工具細節待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"1111 企業端功能（新版第一階段、群組功能、AI 推薦人才）僅記載完成上線，未呈現上線後的廠商採用率或留存成效指標","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"1111上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 全球華人經歷第 1、2、4、6 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線","reason":"1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗，經手 6 款產品","約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd09","具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗","已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環"],"key_gaps":["1111 企業端功能（新版第一階段、群組功能、AI 推薦人才）僅記載完成上線，未呈現上線後的廠商採用率或留存成效指標","1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據","資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節"],"strengths":["1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd09 證明遺留系統重構與B2B組織權限設計力","尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd09 展現嚴謹對照實驗與商業變現能力","1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd09 展現資安危機閉環與10單位治理效率"],"interview_questions":["你在 1111 規劃企業端「群組功能」與「AI 推薦人才」上線後，實際有多少大型企業開通使用？這套分群與推薦邏輯如何遷移至 CDP+MA 行銷自動化場景？","你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？","在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd09 具備多個已實現案例、清楚取捨與跨部門治理實證（惟1111功能缺上線後採用率outcome數據且開發中案例不撐起Level 9，故評為Level 8）"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「系統服務逾 6 萬家活躍付費廠商」且具跨部門排程與群組權限規劃實績，支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 系統服務逾 6 萬家活躍付費廠商（2026 Q3） | 無關鍵缺口，可於面試深化 |
| role_evidence | 強 | 近 10 年 PM 經驗，經手 6 款產品 | 未直接經手 MarTech（CDP+MA+BI）行銷自動化領域產品 |
| decision_depth | 強 | 廠商反映的溝通中斷問題，使我優先推進信件與即時通整合 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 足夠 | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 1111新系統與群組功能未列上線後廠商採用率或留存數據 |
| ownership | 強 | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 3年以上軟體產品或專案管理經驗 | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 年資與軟體產品交付量充足 |
| R02 B2B SaaS經驗尤佳 | 加分 | supported | 系統服務逾 6 萬家活躍付費廠商（2026 Q3） | 近4年主責大型B2B企業端招募系統 |
| R03 熟悉UI/UX概念方法論 | 必要 | supported | User Journey Map、User Story、Use Case | 具使用者旅程地圖、Wireframe與原型設計經驗 |
| R04 批判性思維與問題拆解 | 必要 | supported | 針對大型客戶依部門或分店分工的需求，規劃群組功能 | 拆解大客戶權限痛點與重複信箱驗證限制 |
| R05 數據驅動思維 | 必要 | supported | 使用者訪談與問卷、競品實測、GA4、世代分析 | 具三階段定價對照實驗與處理週期追蹤 |
| R06 獨立作業善跨部門溝通 | 必要 | supported | 對接工程、行銷、業務與客服等 10 個需求單位 | 獨立統籌50大項功能並跨10單位協作 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 對位 jd09 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 Product Owner，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 擬定資料表與欄位需求，與 DBA 協作取數 | 清楚界定個人規劃與DBA/工程/DS分工 |
| HR04 | partial | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 具處理週期與定價實驗數據，缺1111功能採用率 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現功能優先序與E-mail登入驗證取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端成長型產品演進至B2B大型平台主任 |
| HR07 | supported | 透過互動原型與 FAQ 向客服、業務說明功能 | Scrum、原型、FAQ教學、AI與英文協作皆有實例 |
| HR08 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 段落清楚，重點指標與背景脈絡易讀 |
| HR09 | supported | 產品上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 主動標註行銷導流期間表現與開發中狀態 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd09 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 證據鏈完整支持安排 jd09 面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 針對大型客戶依部門或分店分工的需求，規劃群組功能 | 能針對大客戶部門/分店分工痛點設計群組權限 |
| HM03 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與E-mail登入取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數付費牆與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18% | 定價實驗與處理週期基準清晰，缺1111功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整 | 具新舊系統並行相容、重複信箱驗證與防冒用閉環 |
| HM08 | supported | 將業務規則轉為可與工程討論的條件描述 | 能將業務規則轉為工程條件，惟取數與DBA協作 |
| HM09 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程 | 依客服回饋修正登入操作流程與AI推薦規則 |
| HM12 | supported | 具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd09 明文條件獨立取證判讀 | 僅依 jd09 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd09 |
| 2 | 具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗 |
| 3 | 已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 1111 企業端功能（新版第一階段、群組功能、AI 推薦人才）僅記載完成上線，未呈現上線後的廠商採用率或留存成效指標 | 你在 1111 規劃企業端「群組功能」與「AI 推薦人才」上線後，實際有多少大型企業開通使用？這套分群與推薦邏輯如何遷移至 CDP+MA 行銷自動化場景？ |
| 2 | 1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據 | 你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？ |
| 3 | 資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節 | 在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd09 證明遺留系統重構與B2B組織權限設計力
- 尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd09 展現嚴謹對照實驗與商業變現能力
- 1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd09 展現資安危機閉環與10單位治理效率

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：1111 企業端功能（新版第一階段、群組功能、AI 推薦人才）僅記載完成上線，未呈現上線後的廠商採用率或留存成效指標
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落
- 位置：1111 全球華人經歷第 1、2、4、6 點
  - 原句：整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：強

### 8. 未測試聲明
PDF 抽字：risk（本機實測 `resume-v10.2-twocol.pdf` 粗體疊字已完全修復，惟仍有雙欄跨頁斷句與 Type3 康熙部首字元風險） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 Resume_v10.2_twocol（jd11 【北士科】Product Manager｜沛思坦 (Pacston)）｜第 3 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.2_twocol","job_id":"jd11","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd11-03","human_calibrated":false,"requirements":[{"id":"R01","text":"5年以上PM經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"年資近10年且涵蓋B2B與B2C"},{"id":"R02","text":"熟悉敏捷開發與跨部門專案管理","type":"required","status":"supported","evidence":["曾參與每週一個 Sprint 的 Scrum，現行以 Kanban"],"blocks_interview":false,"reason":"兼具Scrum與Kanban跨10單位專案管理"},{"id":"R03","text":"優秀邏輯與溝通能力","type":"required","status":"supported","evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"blocks_interview":false,"reason":"跨部門排程並將業務規則轉為工程條件描述"},{"id":"R04","text":"熟悉Jira、Notion等工具","type":"required","status":"partial","evidence":["Figma、Axure RP、Notion、Trello、內部工單與看板系統"],"blocks_interview":false,"reason":"具Notion與內部工單看板系統，未點名Jira"},{"id":"R05","text":"中英文文件撰寫能力","type":"required","status":"partial","evidence":["英文 TOEIC 980、TOEFL iBT 93，曾赴美交換"],"blocks_interview":false,"reason":"具高分英檢與英文跨國協作，缺英文PRD樣本"},{"id":"R06","text":"HR Tech/LegalTech/生成式AI產品經驗","type":"preferred","status":"supported","evidence":["上線公司簡介生成、職缺工作說明生成及 AI 推薦人才"],"blocks_interview":false,"reason":"直接具備HR招募系統與3項GenAI上線實績"},{"id":"R07","text":"LLM prompt設計或自動化內容編排經驗","type":"preferred","status":"supported","evidence":["以 Claude Code 建立協作流程與共用 skill"],"blocks_interview":false,"reason":"建立Claude Code協作流程與AI Agent應用"},{"id":"R08","text":"資料導向思維、AB測試與技術背景","type":"preferred","status":"supported","evidence":["設計馬來西亞 iOS 定價實驗，以售價不變的 Android 作對照"],"blocks_interview":false,"reason":"具對照實驗、基本HTML/CSS、DB知識與AWS證照"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["系統服務逾 6 萬家活躍付費廠商（2026 Q3）"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"強","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"missing":["使用內部工單與看板系統及 Notion，未直接寫出 Jira 字樣"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["廠商反映的溝通中斷問題，使我優先推進信件與即時通整合"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"足夠","evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"missing":["1111 企業端群組功能與 3 項 AI 功能未列上線後採用或轉換成效數字（依硬性規則 2 評為 Level 8）"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"於 2026/04 完成登入驗證調整...至 2026/10 未再出現同類冒用","kinds":["output","outcome"]},{"quote":"兩案均在開發中，信件與即時通整合已進入公司內部封測","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"對位 jd11 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 Product Owner，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["擬定資料表與欄位需求，與 DBA 協作取數"],"application_note":"清楚界定個人規劃與DBA/工程/DS分工"},{"rule_id":"HR04","status":"partial","resume_evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"application_note":"具處理週期與定價實驗數據，缺1111功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與E-mail登入驗證取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端成長型產品演進至B2B大型平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["透過互動原型與 FAQ 向客服、業務說明功能"],"application_note":"Scrum、原型、FAQ教學、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"application_note":"段落清楚，重點指標與背景脈絡易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["產品上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"主動標註行銷導流期間表現與開發中狀態"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd11 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"application_note":"證據鏈完整支持安排 jd11 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["針對大型客戶依部門或分店分工的需求，規劃群組功能"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線的新版第一階段、群組功能與 AI 推薦人才，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["將業務規則轉為可與工程討論的條件描述"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"在 1111 與資料科學團隊合作上線「公司簡介生成、職缺工作說明生成及 AI 推薦人才」3 項 AI 功能時，你如何定義驗收標準？上線後的採用率與推薦準確度表現如何？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd11 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定條件或技術工具細節待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"1111 企業端「群組功能」與「公司簡介生成、職缺說明生成及 AI 推薦人才」未列出上線後的採用率或推薦轉換指標","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"1111上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 全球華人經歷第 1、2、4、6 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線","reason":"1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗，經手 6 款產品","約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd11","具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗","已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環"],"key_gaps":["1111 企業端「群組功能」與「公司簡介生成、職缺說明生成及 AI 推薦人才」未列出上線後的採用率或推薦轉換指標","1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據","資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節"],"strengths":["1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd11 證明遺留系統重構與B2B組織權限設計力","尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd11 展現嚴謹對照實驗與商業變現能力","1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd11 展現資安危機閉環與10單位治理效率"],"interview_questions":["在 1111 與資料科學團隊合作上線「公司簡介生成、職缺工作說明生成及 AI 推薦人才」3 項 AI 功能時，你如何定義驗收標準？上線後的採用率與推薦準確度表現如何？","你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？","在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd11 具備多個已實現案例、清楚取捨與跨部門治理實證（惟1111功能缺上線後採用率outcome數據且開發中案例不撐起Level 9，故評為Level 8）"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「人力銀行企業端招募系統專案負責人」且「上線公司簡介生成、職缺工作說明生成及 AI 推薦人才」，高度對口。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 系統服務逾 6 萬家活躍付費廠商（2026 Q3） | 無關鍵缺口，可於面試深化 |
| role_evidence | 強 | 近 10 年 PM 經驗，經手 6 款產品 | 使用內部工單與看板系統及 Notion，未直接寫出 Jira 字樣 |
| decision_depth | 強 | 廠商反映的溝通中斷問題，使我優先推進信件與即時通整合 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 足夠 | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 1111 企業端群組功能與 3 項 AI 功能未列上線後採用或轉換成效數字（依硬性規則 2 評為 Level 8） |
| ownership | 強 | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 5年以上PM經驗 | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 年資近10年且涵蓋B2B與B2C |
| R02 熟悉敏捷開發與跨部門專案管理 | 必要 | supported | 曾參與每週一個 Sprint 的 Scrum，現行以 Kanban | 兼具Scrum與Kanban跨10單位專案管理 |
| R03 優秀邏輯與溝通能力 | 必要 | supported | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 跨部門排程並將業務規則轉為工程條件描述 |
| R04 熟悉Jira、Notion等工具 | 必要 | partial | Figma、Axure RP、Notion、Trello、內部工單與看板系統 | 具Notion與內部工單看板系統，未點名Jira |
| R05 中英文文件撰寫能力 | 必要 | partial | 英文 TOEIC 980、TOEFL iBT 93，曾赴美交換 | 具高分英檢與英文跨國協作，缺英文PRD樣本 |
| R06 HR Tech/LegalTech/生成式AI產品經驗 | 加分 | supported | 上線公司簡介生成、職缺工作說明生成及 AI 推薦人才 | 直接具備HR招募系統與3項GenAI上線實績 |
| R07 LLM prompt設計或自動化內容編排經驗 | 加分 | supported | 以 Claude Code 建立協作流程與共用 skill | 建立Claude Code協作流程與AI Agent應用 |
| R08 資料導向思維、AB測試與技術背景 | 加分 | supported | 設計馬來西亞 iOS 定價實驗，以售價不變的 Android 作對照 | 具對照實驗、基本HTML/CSS、DB知識與AWS證照 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 對位 jd11 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 Product Owner，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 擬定資料表與欄位需求，與 DBA 協作取數 | 清楚界定個人規劃與DBA/工程/DS分工 |
| HR04 | partial | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 具處理週期與定價實驗數據，缺1111功能採用率 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現功能優先序與E-mail登入驗證取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端成長型產品演進至B2B大型平台主任 |
| HR07 | supported | 透過互動原型與 FAQ 向客服、業務說明功能 | Scrum、原型、FAQ教學、AI與英文協作皆有實例 |
| HR08 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 段落清楚，重點指標與背景脈絡易讀 |
| HR09 | supported | 產品上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 主動標註行銷導流期間表現與開發中狀態 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd11 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 證據鏈完整支持安排 jd11 面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 針對大型客戶依部門或分店分工的需求，規劃群組功能 | 能針對大客戶部門/分店分工痛點設計群組權限 |
| HM03 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與E-mail登入取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數付費牆與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18% | 定價實驗與處理週期基準清晰，缺1111功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整 | 具新舊系統並行相容、重複信箱驗證與防冒用閉環 |
| HM08 | supported | 將業務規則轉為可與工程討論的條件描述 | 能將業務規則轉為工程條件，惟取數與DBA協作 |
| HM09 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程 | 依客服回饋修正登入操作流程與AI推薦規則 |
| HM12 | supported | 具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd11 明文條件獨立取證判讀 | 僅依 jd11 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd11 |
| 2 | 具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗 |
| 3 | 已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 1111 企業端「群組功能」與「公司簡介生成、職缺說明生成及 AI 推薦人才」未列出上線後的採用率或推薦轉換指標 | 在 1111 與資料科學團隊合作上線「公司簡介生成、職缺工作說明生成及 AI 推薦人才」3 項 AI 功能時，你如何定義驗收標準？上線後的採用率與推薦準確度表現如何？ |
| 2 | 1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據 | 你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？ |
| 3 | 資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節 | 在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd11 證明遺留系統重構與B2B組織權限設計力
- 尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd11 展現嚴謹對照實驗與商業變現能力
- 1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd11 展現資安危機閉環與10單位治理效率

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：1111 企業端「群組功能」與「公司簡介生成、職缺說明生成及 AI 推薦人才」未列出上線後的採用率或推薦轉換指標
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落
- 位置：1111 全球華人經歷第 1、2、4、6 點
  - 原句：整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：強

### 8. 未測試聲明
PDF 抽字：risk（本機實測 `resume-v10.2-twocol.pdf` 粗體疊字已完全修復，惟仍有雙欄跨頁斷句與 Type3 康熙部首字元風險） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 Resume_v10.2_twocol（jd14 D441 MyVideo影音產品Growth PM｜台灣大哥大）｜第 4 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.2_twocol","job_id":"jd14","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd14-04","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上Growth PM經驗（全生命週期漏斗）","type":"required","status":"supported","evidence":["推進定價實驗及付款渠道調整；男性 DAU 增至 1.25 萬"],"blocks_interview":false,"reason":"具約4年訂閱制App獲取、付費轉換與定價實驗經驗"},{"id":"R02","text":"能獨立撰寫PRD/User Flow/Wireframe","type":"required","status":"supported","evidence":["設計流程與畫面、撰寫 PRD 與製作 Prototype"],"blocks_interview":false,"reason":"完整具備流程圖、Wireframe與PRD實績"},{"id":"R03","text":"熟悉GA4、Firebase","type":"required","status":"partial","evidence":["使用者訪談與問卷、競品實測、GA4、世代分析與對照組實驗"],"blocks_interview":false,"reason":"明列GA4與世代分析，未呈現Firebase"},{"id":"R04","text":"訂閱與會員轉換優化、A/B Test產品實驗","type":"required","status":"supported","evidence":["網頁付款占營收由 24% 升至 80% 以上"],"blocks_interview":false,"reason":"具VIP訂閱、點數牆、網頁金流與三階段定價實驗"},{"id":"R05","text":"跨部門溝通能力","type":"required","status":"supported","evidence":["對接工程、行銷、業務與客服等 10 個需求單位"],"blocks_interview":false,"reason":"跨工程、設計、行銷與金流團隊推進交付"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["系統服務逾 6 萬家活躍付費廠商（2026 Q3）"],"missing":["近4年重心為B2B企業招募系統，C端訂閱成長實驗集中於2018–2022年"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"足夠","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"missing":["未呈現 Firebase 操作經驗，且 KOOL 未列雙邊媒合規模或轉換漏斗數字"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["廠商反映的溝通中斷問題，使我優先推進信件與即時通整合"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"missing":["KOOL 網紅媒合平台與 1111 近期改版未列漏斗轉換率與留存數據"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"於 2026/04 完成登入驗證調整...至 2026/10 未再出現同類冒用","kinds":["output","outcome"]},{"quote":"兩案均在開發中，信件與即時通整合已進入公司內部封測","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["推進定價實驗及付款渠道調整；男性 DAU 增至 1.25 萬"],"application_note":"對位 jd14 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 Product Owner，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["擬定資料表與欄位需求，與 DBA 協作取數"],"application_note":"清楚界定個人規劃與DBA/工程/DS分工"},{"rule_id":"HR04","status":"partial","resume_evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"application_note":"具處理週期與定價實驗數據，缺1111功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與E-mail登入驗證取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端成長型產品演進至B2B大型平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["透過互動原型與 FAQ 向客服、業務說明功能"],"application_note":"Scrum、原型、FAQ教學、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"application_note":"段落清楚，重點指標與背景脈絡易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["產品上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"主動標註行銷導流期間表現與開發中狀態"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd14 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"application_note":"證據鏈完整支持安排 jd14 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["針對大型客戶依部門或分店分工的需求，規劃群組功能"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線的新版第一階段、群組功能與 AI 推薦人才，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["將業務規則轉為可與工程討論的條件描述"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"在規劃 KOOL 網紅媒合平台與 VIP 訂閱／點數付費牆時，Acquisition 到 Activation 的漏斗轉換表現如何？過去是否有使用 Firebase Events 追蹤 App 行為的經驗？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd14 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定條件或技術工具細節待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"必備條件點名之 Firebase 未呈現；且成長與定價實驗集中於 2018–2022 年，近 4 年在 1111 較少呈現 A/B Test 與轉換漏斗數據","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"1111上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 全球華人經歷第 1、2、4、6 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線","reason":"1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["推進定價實驗及付款渠道調整；男性 DAU 增至 1.25 萬","約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd14","具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗","已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環"],"key_gaps":["必備條件點名之 Firebase 未呈現；且成長與定價實驗集中於 2018–2022 年，近 4 年在 1111 較少呈現 A/B Test 與轉換漏斗數據","1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據","資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節"],"strengths":["1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd14 證明遺留系統重構與B2B組織權限設計力","尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd14 展現嚴謹對照實驗與商業變現能力","1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd14 展現資安危機閉環與10單位治理效率"],"interview_questions":["在規劃 KOOL 網紅媒合平台與 VIP 訂閱／點數付費牆時，Acquisition 到 Activation 的漏斗轉換表現如何？過去是否有使用 Firebase Events 追蹤 App 行為的經驗？","你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？","在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":7,"uncertainty_levels":1,"basis":"針對 jd14 具備多個已實現案例、清楚取捨與跨部門治理實證（惟1111功能缺上線後採用率outcome數據且開發中案例不撐起Level 9，故評為Level 7）"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：7（±1）
- 一句話理由：「設計馬來西亞 iOS 定價實驗...相對變化約多 28%」與網頁金流轉換具實證，支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 系統服務逾 6 萬家活躍付費廠商（2026 Q3） | 近4年重心為B2B企業招募系統，C端訂閱成長實驗集中於2018–2022年 |
| role_evidence | 足夠 | 近 10 年 PM 經驗，經手 6 款產品 | 未呈現 Firebase 操作經驗，且 KOOL 未列雙邊媒合規模或轉換漏斗數字 |
| decision_depth | 強 | 廠商反映的溝通中斷問題，使我優先推進信件與即時通整合 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | KOOL 網紅媒合平台與 1111 近期改版未列漏斗轉換率與留存數據 |
| ownership | 強 | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 3年以上Growth PM經驗（全生命週期漏斗） | 必要 | supported | 推進定價實驗及付款渠道調整；男性 DAU 增至 1.25 萬 | 具約4年訂閱制App獲取、付費轉換與定價實驗經驗 |
| R02 能獨立撰寫PRD/User Flow/Wireframe | 必要 | supported | 設計流程與畫面、撰寫 PRD 與製作 Prototype | 完整具備流程圖、Wireframe與PRD實績 |
| R03 熟悉GA4、Firebase | 必要 | partial | 使用者訪談與問卷、競品實測、GA4、世代分析與對照組實驗 | 明列GA4與世代分析，未呈現Firebase |
| R04 訂閱與會員轉換優化、A/B Test產品實驗 | 必要 | supported | 網頁付款占營收由 24% 升至 80% 以上 | 具VIP訂閱、點數牆、網頁金流與三階段定價實驗 |
| R05 跨部門溝通能力 | 必要 | supported | 對接工程、行銷、業務與客服等 10 個需求單位 | 跨工程、設計、行銷與金流團隊推進交付 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 推進定價實驗及付款渠道調整；男性 DAU 增至 1.25 萬 | 對位 jd14 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 Product Owner，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 擬定資料表與欄位需求，與 DBA 協作取數 | 清楚界定個人規劃與DBA/工程/DS分工 |
| HR04 | partial | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 具處理週期與定價實驗數據，缺1111功能採用率 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現功能優先序與E-mail登入驗證取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端成長型產品演進至B2B大型平台主任 |
| HR07 | supported | 透過互動原型與 FAQ 向客服、業務說明功能 | Scrum、原型、FAQ教學、AI與英文協作皆有實例 |
| HR08 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 段落清楚，重點指標與背景脈絡易讀 |
| HR09 | supported | 產品上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 主動標註行銷導流期間表現與開發中狀態 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd14 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 證據鏈完整支持安排 jd14 面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 針對大型客戶依部門或分店分工的需求，規劃群組功能 | 能針對大客戶部門/分店分工痛點設計群組權限 |
| HM03 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與E-mail登入取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數付費牆與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18% | 定價實驗與處理週期基準清晰，缺1111功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整 | 具新舊系統並行相容、重複信箱驗證與防冒用閉環 |
| HM08 | supported | 將業務規則轉為可與工程討論的條件描述 | 能將業務規則轉為工程條件，惟取數與DBA協作 |
| HM09 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程 | 依客服回饋修正登入操作流程與AI推薦規則 |
| HM12 | supported | 具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd14 明文條件獨立取證判讀 | 僅依 jd14 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd14 |
| 2 | 具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗 |
| 3 | 已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 必備條件點名之 Firebase 未呈現；且成長與定價實驗集中於 2018–2022 年，近 4 年在 1111 較少呈現 A/B Test 與轉換漏斗數據 | 在規劃 KOOL 網紅媒合平台與 VIP 訂閱／點數付費牆時，Acquisition 到 Activation 的漏斗轉換表現如何？過去是否有使用 Firebase Events 追蹤 App 行為的經驗？ |
| 2 | 1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據 | 你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？ |
| 3 | 資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節 | 在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd14 證明遺留系統重構與B2B組織權限設計力
- 尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd14 展現嚴謹對照實驗與商業變現能力
- 1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd14 展現資安危機閉環與10單位治理效率

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：必備條件點名之 Firebase 未呈現；且成長與定價實驗集中於 2018–2022 年，近 4 年在 1111 較少呈現 A/B Test 與轉換漏斗數據
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落
- 位置：1111 全球華人經歷第 1、2、4、6 點
  - 原句：整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：risk（本機實測 `resume-v10.2-twocol.pdf` 粗體疊字已完全修復，惟仍有雙欄跨頁斷句與 Type3 康熙部首字元風險） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 Resume_v10.2_twocol（jd20 Senior Product Manager (Anti-Scam BU/2B)｜Gogolook）｜第 5 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.2_twocol","job_id":"jd20","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd20-05","human_calibrated":false,"requirements":[{"id":"R01","text":"5-8年以上B2B/B2G產品或專案管理經驗","type":"required","status":"partial","evidence":["1111 全球華人｜2022/08 - 迄今（服務逾 6 萬家廠商）"],"blocks_interview":false,"reason":"總PM近10年，惟純B2B經驗約4年略低於5-8年門檻"},{"id":"R02","text":"接近母語等級英語口說與書寫","type":"required","status":"partial","evidence":["英文 TOEIC 980、TOEFL iBT 93，曾赴美交換"],"blocks_interview":false,"reason":"高分英檢與英文跨國協作，母語級B2B商務簡報待驗"},{"id":"R03","text":"優異溝通與關係人管理能力","type":"required","status":"supported","evidence":["參與公司一級主管日會，向總經理、副總等主管匯報"],"blocks_interview":false,"reason":"跨10個部門協調需求並向總經理、副總匯報"},{"id":"R04","text":"扎實PM基礎（PRD/路線圖/待辦清單/時程風險）","type":"required","status":"supported","evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"blocks_interview":false,"reason":"主責50大項功能並將處理週期由100.4天降至30.9天"},{"id":"R05","text":"強烈數據敏感度（能獨立使用SQL/BI/試算表）","type":"required","status":"partial","evidence":["擬定資料表與欄位需求，與 DBA 協作取數"],"blocks_interview":false,"reason":"懂資料表欄位並精熟Sheet/Excel，惟非獨立自寫SQL查詢"},{"id":"R06","text":"熟悉AI工具（如Claude）與Jira/Confluence串接","type":"required","status":"partial","evidence":["以 Claude Code 建立協作流程與共用 skill"],"blocks_interview":false,"reason":"Claude Code應用深入，惟未列Jira/Confluence串接"},{"id":"R07","text":"對防詐與風險偵測有熱情及相關產品經驗","type":"required","status":"supported","evidence":["廠商招募帳號遭冒用...於 2026/04 完成登入驗證調整"],"blocks_interview":false,"reason":"親歷B2B帳號遭冒用個資外洩風險控管並完成登入驗證調整"},{"id":"R08","text":"曾服務海外企業客戶或政府機關","type":"preferred","status":"partial","evidence":["推進 SweetRing 在美國、墨西哥...7 個市場的在地化"],"blocks_interview":false,"reason":"具7國B2C在地化與台灣B2B，缺海外B2B/B2G企業客戶"},{"id":"R09","text":"具Agile/Scrum與產品定價成本利潤分析經驗","type":"preferred","status":"supported","evidence":["曾參與每週一個 Sprint 的 Scrum；完成實收試算"],"blocks_interview":false,"reason":"具Scrum經歷、定價實驗與跨國金流抽成稅費實收試算"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["系統服務逾 6 萬家活躍付費廠商（2026 Q3）"],"missing":["純B2B經驗約4年（未滿5-8年門檻），且未直接面對海外B2B/B2G客戶與BD收集需求"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"待補","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"missing":["資料庫取數需與 DBA 協作而非獨立寫 SQL/BI 查詢；未明列 Jira/Confluence"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["廠商反映的溝通中斷問題，使我優先推進信件與即時通整合"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"足夠","evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"missing":["1111企業端功能未列上線後採用或營收留存指標"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"於 2026/04 完成登入驗證調整...至 2026/10 未再出現同類冒用","kinds":["output","outcome"]},{"quote":"兩案均在開發中，信件與即時通整合已進入公司內部封測","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"partial","resume_evidence":["1111 全球華人｜2022/08 - 迄今（服務逾 6 萬家廠商）"],"application_note":"對位 jd20 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 Product Owner，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["擬定資料表與欄位需求，與 DBA 協作取數"],"application_note":"清楚界定個人規劃與DBA/工程/DS分工"},{"rule_id":"HR04","status":"partial","resume_evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"application_note":"具處理週期與定價實驗數據，缺1111功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與E-mail登入驗證取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端成長型產品演進至B2B大型平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["透過互動原型與 FAQ 向客服、業務說明功能"],"application_note":"Scrum、原型、FAQ教學、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"application_note":"段落清楚，重點指標與背景脈絡易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["產品上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"主動標註行銷導流期間表現與開發中狀態"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd20 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"partial","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"application_note":"建議先釐清 jd20 關鍵條件再安排面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["針對大型客戶依部門或分店分工的需求，規劃群組功能"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線的新版第一階段、群組功能與 AI 推薦人才，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"partial","resume_evidence":["將業務規則轉為可與工程討論的條件描述"],"evidence_type":"output","source_ids":[],"interview_question":"請說明如何將業務規則轉為工程條件描述，以及是否具基礎 SQL/JSON 實作經驗？"},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"請以英文簡述 2026/04 1111 廠商帳號遭冒用事件中，你如何釐清受影響範圍、設計登入驗證與解鎖流程？另外你本人能否獨立撰寫 SQL 查詢資料庫？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd20 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定條件或技術工具細節待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"必備條件要求「5-8年以上B2B/B2G經驗」與「自行查詢解讀產品數據（獨立使用SQL/BI）」，目前純 B2B 年資約 4 年且須與 DBA 協作取數","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"1111上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 全球華人經歷第 1、2、4、6 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線","reason":"1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證"}],"decision":{"recommendation":"clarify_first","evidence":["1111 全球華人｜2022/08 - 迄今（服務逾 6 萬家廠商）","約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"blocking_unknowns":["必備條件要求「5-8年以上B2B/B2G經驗」與「自行查詢解讀產品數據（獨立使用SQL/BI）」，目前純 B2B 年資約 4 年且須與 DBA 協作取數"]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd20","具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗","已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環"],"key_gaps":["必備條件要求「5-8年以上B2B/B2G經驗」與「自行查詢解讀產品數據（獨立使用SQL/BI）」，目前純 B2B 年資約 4 年且須與 DBA 協作取數","1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據","資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節"],"strengths":["1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd20 證明遺留系統重構與B2B組織權限設計力","尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd20 展現嚴謹對照實驗與商業變現能力","1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd20 展現資安危機閉環與10單位治理效率"],"interview_questions":["請以英文簡述 2026/04 1111 廠商帳號遭冒用事件中，你如何釐清受影響範圍、設計登入驗證與解鎖流程？另外你本人能否獨立撰寫 SQL 查詢資料庫？","你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？","在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":7,"uncertainty_levels":1,"basis":"針對 jd20 具備多個已實現案例、清楚取捨與跨部門治理實證（惟1111功能缺上線後採用率outcome數據且開發中案例不撐起Level 9，故評為Level 7）"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：clarify_first
- Level：7（±1）
- 一句話理由：具「2026/04 完成登入驗證調整」防冒用經驗，惟純 B2B 年資約 4 年且取數須與 DBA 協作，建議先釐清。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 系統服務逾 6 萬家活躍付費廠商（2026 Q3） | 純B2B經驗約4年（未滿5-8年門檻），且未直接面對海外B2B/B2G客戶與BD收集需求 |
| role_evidence | 待補 | 近 10 年 PM 經驗，經手 6 款產品 | 資料庫取數需與 DBA 協作而非獨立寫 SQL/BI 查詢；未明列 Jira/Confluence |
| decision_depth | 強 | 廠商反映的溝通中斷問題，使我優先推進信件與即時通整合 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 足夠 | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 1111企業端功能未列上線後採用或營收留存指標 |
| ownership | 強 | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 5-8年以上B2B/B2G產品或專案管理經驗 | 必要 | partial | 1111 全球華人｜2022/08 - 迄今（服務逾 6 萬家廠商） | 總PM近10年，惟純B2B經驗約4年略低於5-8年門檻 |
| R02 接近母語等級英語口說與書寫 | 必要 | partial | 英文 TOEIC 980、TOEFL iBT 93，曾赴美交換 | 高分英檢與英文跨國協作，母語級B2B商務簡報待驗 |
| R03 優異溝通與關係人管理能力 | 必要 | supported | 參與公司一級主管日會，向總經理、副總等主管匯報 | 跨10個部門協調需求並向總經理、副總匯報 |
| R04 扎實PM基礎（PRD/路線圖/待辦清單/時程風險） | 必要 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 主責50大項功能並將處理週期由100.4天降至30.9天 |
| R05 強烈數據敏感度（能獨立使用SQL/BI/試算表） | 必要 | partial | 擬定資料表與欄位需求，與 DBA 協作取數 | 懂資料表欄位並精熟Sheet/Excel，惟非獨立自寫SQL查詢 |
| R06 熟悉AI工具（如Claude）與Jira/Confluence串接 | 必要 | partial | 以 Claude Code 建立協作流程與共用 skill | Claude Code應用深入，惟未列Jira/Confluence串接 |
| R07 對防詐與風險偵測有熱情及相關產品經驗 | 必要 | supported | 廠商招募帳號遭冒用...於 2026/04 完成登入驗證調整 | 親歷B2B帳號遭冒用個資外洩風險控管並完成登入驗證調整 |
| R08 曾服務海外企業客戶或政府機關 | 加分 | partial | 推進 SweetRing 在美國、墨西哥...7 個市場的在地化 | 具7國B2C在地化與台灣B2B，缺海外B2B/B2G企業客戶 |
| R09 具Agile/Scrum與產品定價成本利潤分析經驗 | 加分 | supported | 曾參與每週一個 Sprint 的 Scrum；完成實收試算 | 具Scrum經歷、定價實驗與跨國金流抽成稅費實收試算 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | partial | 1111 全球華人｜2022/08 - 迄今（服務逾 6 萬家廠商） | 對位 jd20 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 Product Owner，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 擬定資料表與欄位需求，與 DBA 協作取數 | 清楚界定個人規劃與DBA/工程/DS分工 |
| HR04 | partial | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 具處理週期與定價實驗數據，缺1111功能採用率 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現功能優先序與E-mail登入驗證取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端成長型產品演進至B2B大型平台主任 |
| HR07 | supported | 透過互動原型與 FAQ 向客服、業務說明功能 | Scrum、原型、FAQ教學、AI與英文協作皆有實例 |
| HR08 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 段落清楚，重點指標與背景脈絡易讀 |
| HR09 | supported | 產品上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 主動標註行銷導流期間表現與開發中狀態 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd20 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | partial | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 建議先釐清 jd20 關鍵條件再安排面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 針對大型客戶依部門或分店分工的需求，規劃群組功能 | 能針對大客戶部門/分店分工痛點設計群組權限 |
| HM03 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與E-mail登入取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數付費牆與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18% | 定價實驗與處理週期基準清晰，缺1111功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整 | 具新舊系統並行相容、重複信箱驗證與防冒用閉環 |
| HM08 | partial | 將業務規則轉為可與工程討論的條件描述 | 能將業務規則轉為工程條件，惟取數與DBA協作 |
| HM09 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程 | 依客服回饋修正登入操作流程與AI推薦規則 |
| HM12 | supported | 具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd20 明文條件獨立取證判讀 | 僅依 jd20 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd20 |
| 2 | 具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗 |
| 3 | 已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 必備條件要求「5-8年以上B2B/B2G經驗」與「自行查詢解讀產品數據（獨立使用SQL/BI）」，目前純 B2B 年資約 4 年且須與 DBA 協作取數 | 請以英文簡述 2026/04 1111 廠商帳號遭冒用事件中，你如何釐清受影響範圍、設計登入驗證與解鎖流程？另外你本人能否獨立撰寫 SQL 查詢資料庫？ |
| 2 | 1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據 | 你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？ |
| 3 | 資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節 | 在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd20 證明遺留系統重構與B2B組織權限設計力
- 尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd20 展現嚴謹對照實驗與商業變現能力
- 1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd20 展現資安危機閉環與10單位治理效率

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：必備條件要求「5-8年以上B2B/B2G經驗」與「自行查詢解讀產品數據（獨立使用SQL/BI）」，目前純 B2B 年資約 4 年且須與 DBA 協作取數
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落
- 位置：1111 全球華人經歷第 1、2、4、6 點
  - 原句：整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：risk（本機實測 `resume-v10.2-twocol.pdf` 粗體疊字已完全修復，惟仍有雙欄跨頁斷句與 Type3 康熙部首字元風險） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 Resume_v10.2_twocol（jd26 全支付- Product Manager (專案執行)）｜第 6 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.2_twocol","job_id":"jd26","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd26-06","human_calibrated":false,"requirements":[{"id":"R01","text":"2年以上相關工作經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"年資與專案推進經驗豐富"},{"id":"R02","text":"能運用Axure撰寫規劃，透過Jira/Confluence管理","type":"required","status":"partial","evidence":["Figma、Axure RP、Notion、Trello、內部工單與看板系統"],"blocks_interview":false,"reason":"具Axure RP與內部工單看板系統，未直接寫出Jira/Confluence"},{"id":"R03","text":"同步考慮技術可行性及系統架構關連影響","type":"required","status":"supported","evidence":["重新制定業務流程、對照資料欄位並重構規格，處理新舊系統並行"],"blocks_interview":false,"reason":"兼顧前後端分離改版、資料欄位對照與新舊系統並行相容性"},{"id":"R04","text":"與合作方確認需求並與法遵確認適法性","type":"required","status":"supported","evidence":["工程、設計、QA、資料科學、客服、業務、法務與稽核協作"],"blocks_interview":false,"reason":"明列法務與稽核協作及海外金流團隊對接"},{"id":"R05","text":"執行專案測試、驗收、上線協調與教育訓練","type":"required","status":"supported","evidence":["透過互動原型與 FAQ 向客服、業務說明功能"],"blocks_interview":false,"reason":"具UAT制定、上線計畫與透過互動原型/FAQ進行內部教育訓練"},{"id":"R06","text":"喜愛或熟悉數位金融、支付產品","type":"required","status":"supported","evidence":["導入 CodaPay，讓印尼、泰國用戶可用電信帳單與超商付款"],"blocks_interview":false,"reason":"具網頁付款、App內購與跨國替代支付串接經驗"},{"id":"R07","text":"熟悉代理收付、電子支付領域知識；精通英文","type":"preferred","status":"partial","evidence":["整理抽成、稅、手續費與撥款週期，完成實收試算"],"blocks_interview":false,"reason":"具金流撥款實收試算與高分英文，無專營電支機構內部帳務經驗"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["系統服務逾 6 萬家活躍付費廠商（2026 Q3）"],"missing":["金流經驗偏向商戶端串接，無台灣本地專營電子支付機構與銀行合作專案經驗"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"足夠","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"missing":["專案追蹤使用內部工單與看板系統及 Notion/Trello，未直接寫出 Jira/Confluence"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"足夠","evidence":["廠商反映的溝通中斷問題，使我優先推進信件與即時通整合"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"於 2026/04 完成登入驗證調整...至 2026/10 未再出現同類冒用","kinds":["output","outcome"]},{"quote":"兩案均在開發中，信件與即時通整合已進入公司內部封測","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"對位 jd26 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 Product Owner，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["擬定資料表與欄位需求，與 DBA 協作取數"],"application_note":"清楚界定個人規劃與DBA/工程/DS分工"},{"rule_id":"HR04","status":"partial","resume_evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"application_note":"具處理週期與定價實驗數據，缺1111功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與E-mail登入驗證取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端成長型產品演進至B2B大型平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["透過互動原型與 FAQ 向客服、業務說明功能"],"application_note":"Scrum、原型、FAQ教學、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"application_note":"段落清楚，重點指標與背景脈絡易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["產品上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"主動標註行銷導流期間表現與開發中狀態"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd26 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"application_note":"證據鏈完整支持安排 jd26 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["針對大型客戶依部門或分店分工的需求，規劃群組功能"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線的新版第一階段、群組功能與 AI 推薦人才，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["將業務規則轉為可與工程討論的條件描述"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"在 1111 招募系統改版與過往 CodaPay 金流串接中，你如何與法務稽核確認適法性，並透過互動原型與 FAQ 完成客服與業務的教育訓練？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd26 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定條件或技術工具細節待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"專案管理使用「內部工單與看板系統、Notion、Trello」，未明列必備條件點名之 Jira、Confluence；且缺乏專營電子支付機構代理收付領域經驗","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"1111上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 全球華人經歷第 1、2、4、6 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線","reason":"1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗，經手 6 款產品","約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd26","具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗","已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環"],"key_gaps":["專案管理使用「內部工單與看板系統、Notion、Trello」，未明列必備條件點名之 Jira、Confluence；且缺乏專營電子支付機構代理收付領域經驗","1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據","資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節"],"strengths":["1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd26 證明遺留系統重構與B2B組織權限設計力","尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd26 展現嚴謹對照實驗與商業變現能力","1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd26 展現資安危機閉環與10單位治理效率"],"interview_questions":["在 1111 招募系統改版與過往 CodaPay 金流串接中，你如何與法務稽核確認適法性，並透過互動原型與 FAQ 完成客服與業務的教育訓練？","你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？","在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":7,"uncertainty_levels":1,"basis":"針對 jd26 具備多個已實現案例、清楚取捨與跨部門治理實證（惟1111功能缺上線後採用率outcome數據且開發中案例不撐起Level 9，故評為Level 7）"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：7（±1）
- 一句話理由：具「Axure RP」與「約 50 項大項功能於 2023/12–2026/03 上線」及法務稽核協作經驗，支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 系統服務逾 6 萬家活躍付費廠商（2026 Q3） | 金流經驗偏向商戶端串接，無台灣本地專營電子支付機構與銀行合作專案經驗 |
| role_evidence | 足夠 | 近 10 年 PM 經驗，經手 6 款產品 | 專案追蹤使用內部工單與看板系統及 Notion/Trello，未直接寫出 Jira/Confluence |
| decision_depth | 足夠 | 廠商反映的溝通中斷問題，使我優先推進信件與即時通整合 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 2年以上相關工作經驗 | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 年資與專案推進經驗豐富 |
| R02 能運用Axure撰寫規劃，透過Jira/Confluence管理 | 必要 | partial | Figma、Axure RP、Notion、Trello、內部工單與看板系統 | 具Axure RP與內部工單看板系統，未直接寫出Jira/Confluence |
| R03 同步考慮技術可行性及系統架構關連影響 | 必要 | supported | 重新制定業務流程、對照資料欄位並重構規格，處理新舊系統並行 | 兼顧前後端分離改版、資料欄位對照與新舊系統並行相容性 |
| R04 與合作方確認需求並與法遵確認適法性 | 必要 | supported | 工程、設計、QA、資料科學、客服、業務、法務與稽核協作 | 明列法務與稽核協作及海外金流團隊對接 |
| R05 執行專案測試、驗收、上線協調與教育訓練 | 必要 | supported | 透過互動原型與 FAQ 向客服、業務說明功能 | 具UAT制定、上線計畫與透過互動原型/FAQ進行內部教育訓練 |
| R06 喜愛或熟悉數位金融、支付產品 | 必要 | supported | 導入 CodaPay，讓印尼、泰國用戶可用電信帳單與超商付款 | 具網頁付款、App內購與跨國替代支付串接經驗 |
| R07 熟悉代理收付、電子支付領域知識；精通英文 | 加分 | partial | 整理抽成、稅、手續費與撥款週期，完成實收試算 | 具金流撥款實收試算與高分英文，無專營電支機構內部帳務經驗 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 對位 jd26 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 Product Owner，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 擬定資料表與欄位需求，與 DBA 協作取數 | 清楚界定個人規劃與DBA/工程/DS分工 |
| HR04 | partial | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 具處理週期與定價實驗數據，缺1111功能採用率 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現功能優先序與E-mail登入驗證取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端成長型產品演進至B2B大型平台主任 |
| HR07 | supported | 透過互動原型與 FAQ 向客服、業務說明功能 | Scrum、原型、FAQ教學、AI與英文協作皆有實例 |
| HR08 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 段落清楚，重點指標與背景脈絡易讀 |
| HR09 | supported | 產品上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 主動標註行銷導流期間表現與開發中狀態 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd26 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 證據鏈完整支持安排 jd26 面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 針對大型客戶依部門或分店分工的需求，規劃群組功能 | 能針對大客戶部門/分店分工痛點設計群組權限 |
| HM03 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與E-mail登入取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數付費牆與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18% | 定價實驗與處理週期基準清晰，缺1111功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整 | 具新舊系統並行相容、重複信箱驗證與防冒用閉環 |
| HM08 | supported | 將業務規則轉為可與工程討論的條件描述 | 能將業務規則轉為工程條件，惟取數與DBA協作 |
| HM09 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程 | 依客服回饋修正登入操作流程與AI推薦規則 |
| HM12 | supported | 具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd26 明文條件獨立取證判讀 | 僅依 jd26 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd26 |
| 2 | 具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗 |
| 3 | 已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 專案管理使用「內部工單與看板系統、Notion、Trello」，未明列必備條件點名之 Jira、Confluence；且缺乏專營電子支付機構代理收付領域經驗 | 在 1111 招募系統改版與過往 CodaPay 金流串接中，你如何與法務稽核確認適法性，並透過互動原型與 FAQ 完成客服與業務的教育訓練？ |
| 2 | 1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據 | 你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？ |
| 3 | 資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節 | 在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd26 證明遺留系統重構與B2B組織權限設計力
- 尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd26 展現嚴謹對照實驗與商業變現能力
- 1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd26 展現資安危機閉環與10單位治理效率

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：專案管理使用「內部工單與看板系統、Notion、Trello」，未明列必備條件點名之 Jira、Confluence；且缺乏專營電子支付機構代理收付領域經驗
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落
- 位置：1111 全球華人經歷第 1、2、4、6 點
  - 原句：整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：risk（本機實測 `resume-v10.2-twocol.pdf` 粗體疊字已完全修復，惟仍有雙欄跨頁斷句與 Type3 康熙部首字元風險） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 Resume_v10.2_twocol（jd30 資深產品經理｜Senior Product Manager｜USPACE）｜第 7 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.2_twocol","job_id":"jd30","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd30-07","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上Software PM且至少一次完整0到1直接負責經歷","type":"required","status":"supported","evidence":["規劃 KOOL 網紅媒合平台，從案主與網紅兩種角色釐清需求"],"blocks_interview":false,"reason":"主導KOOL從0到1需求釐清、媒合流程設計與VIP/點數上線"},{"id":"R02","text":"能寫清楚的規格文件（PRD、流程圖、資料結構）","type":"required","status":"supported","evidence":["流程圖／循序圖、Wireframe、Prototype、PRD"],"blocks_interview":false,"reason":"具PRD、循序圖、資料欄位對照與擬定資料表及欄位能力"},{"id":"R03","text":"理解API、JSON與基本SQL","type":"required","status":"partial","evidence":["API 串接規劃；擬定資料表與欄位需求，與 DBA 協作取數"],"blocks_interview":false,"reason":"具API與資料表欄位規劃，未明列JSON與自行撰寫SQL"},{"id":"R04","text":"習慣用AI工具（Claude Code等）把工作流程化","type":"preferred","status":"supported","evidence":["以 Claude Code 建立協作流程與共用 skill"],"blocks_interview":false,"reason":"直接命中Claude Code協作流程與轉譯工程討論條件"},{"id":"R05","text":"支付或FinTech經驗、Growth或數據分析經驗","type":"preferred","status":"supported","evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"blocks_interview":false,"reason":"具網頁金流、CodaPay串接與三階段定價實驗"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["系統服務逾 6 萬家活躍付費廠商（2026 Q3）"],"missing":["過往為純軟體平台與App，尚未接觸智慧停車或MaaS車聯網硬體場域"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"強","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"missing":["必備條件中之 JSON 未明文呈現，且資料庫查詢為與 DBA 協作取數而非自寫 SQL"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["廠商反映的溝通中斷問題，使我優先推進信件與即時通整合"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"於 2026/04 完成登入驗證調整...至 2026/10 未再出現同類冒用","kinds":["output","outcome"]},{"quote":"兩案均在開發中，信件與即時通整合已進入公司內部封測","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台，從案主與網紅兩種角色釐清需求"],"application_note":"對位 jd30 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 Product Owner，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["擬定資料表與欄位需求，與 DBA 協作取數"],"application_note":"清楚界定個人規劃與DBA/工程/DS分工"},{"rule_id":"HR04","status":"partial","resume_evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"application_note":"具處理週期與定價實驗數據，缺1111功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與E-mail登入驗證取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端成長型產品演進至B2B大型平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["透過互動原型與 FAQ 向客服、業務說明功能"],"application_note":"Scrum、原型、FAQ教學、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"application_note":"段落清楚，重點指標與背景脈絡易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["產品上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"主動標註行銷導流期間表現與開發中狀態"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd30 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"application_note":"證據鏈完整支持安排 jd30 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["針對大型客戶依部門或分店分工的需求，規劃群組功能"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線的新版第一階段、群組功能與 AI 推薦人才，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"partial","resume_evidence":["將業務規則轉為可與工程討論的條件描述"],"evidence_type":"output","source_ids":[],"interview_question":"請說明如何將業務規則轉為工程條件描述，以及是否具基礎 SQL/JSON 實作經驗？"},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"請分享你如何「以 Claude Code 建立協作流程與共用 skill，並將業務規則轉為可與工程討論的條件描述」？另外能否說明 KOOL 上線後的規模與轉換數據？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd30 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定條件或技術工具細節待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"必備條件要求「理解 API、JSON 與基本 SQL」，履歷雖載明 API 串接規劃與擬定資料表欄位與 DBA 協作取數，但未明文呈現 JSON 與自行撰寫 SQL","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"1111上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 全球華人經歷第 1、2、4、6 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線","reason":"1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["規劃 KOOL 網紅媒合平台，從案主與網紅兩種角色釐清需求","約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd30","具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗","已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環"],"key_gaps":["必備條件要求「理解 API、JSON 與基本 SQL」，履歷雖載明 API 串接規劃與擬定資料表欄位與 DBA 協作取數，但未明文呈現 JSON 與自行撰寫 SQL","1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據","資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節"],"strengths":["1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd30 證明遺留系統重構與B2B組織權限設計力","尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd30 展現嚴謹對照實驗與商業變現能力","1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd30 展現資安危機閉環與10單位治理效率"],"interview_questions":["請分享你如何「以 Claude Code 建立協作流程與共用 skill，並將業務規則轉為可與工程討論的條件描述」？另外能否說明 KOOL 上線後的規模與轉換數據？","你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？","在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd30 具備多個已實現案例、清楚取捨與跨部門治理實證（惟1111功能缺上線後採用率outcome數據且開發中案例不撐起Level 9，故評為Level 8）"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：具「規劃 KOOL 網紅媒合平台」0 到 1 經驗與「以 Claude Code 建立協作流程」，高度契合。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 系統服務逾 6 萬家活躍付費廠商（2026 Q3） | 過往為純軟體平台與App，尚未接觸智慧停車或MaaS車聯網硬體場域 |
| role_evidence | 強 | 近 10 年 PM 經驗，經手 6 款產品 | 必備條件中之 JSON 未明文呈現，且資料庫查詢為與 DBA 協作取數而非自寫 SQL |
| decision_depth | 強 | 廠商反映的溝通中斷問題，使我優先推進信件與即時通整合 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 3年以上Software PM且至少一次完整0到1直接負責經歷 | 必要 | supported | 規劃 KOOL 網紅媒合平台，從案主與網紅兩種角色釐清需求 | 主導KOOL從0到1需求釐清、媒合流程設計與VIP/點數上線 |
| R02 能寫清楚的規格文件（PRD、流程圖、資料結構） | 必要 | supported | 流程圖／循序圖、Wireframe、Prototype、PRD | 具PRD、循序圖、資料欄位對照與擬定資料表及欄位能力 |
| R03 理解API、JSON與基本SQL | 必要 | partial | API 串接規劃；擬定資料表與欄位需求，與 DBA 協作取數 | 具API與資料表欄位規劃，未明列JSON與自行撰寫SQL |
| R04 習慣用AI工具（Claude Code等）把工作流程化 | 加分 | supported | 以 Claude Code 建立協作流程與共用 skill | 直接命中Claude Code協作流程與轉譯工程討論條件 |
| R05 支付或FinTech經驗、Growth或數據分析經驗 | 加分 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具網頁金流、CodaPay串接與三階段定價實驗 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 規劃 KOOL 網紅媒合平台，從案主與網紅兩種角色釐清需求 | 對位 jd30 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 Product Owner，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 擬定資料表與欄位需求，與 DBA 協作取數 | 清楚界定個人規劃與DBA/工程/DS分工 |
| HR04 | partial | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 具處理週期與定價實驗數據，缺1111功能採用率 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現功能優先序與E-mail登入驗證取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端成長型產品演進至B2B大型平台主任 |
| HR07 | supported | 透過互動原型與 FAQ 向客服、業務說明功能 | Scrum、原型、FAQ教學、AI與英文協作皆有實例 |
| HR08 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 段落清楚，重點指標與背景脈絡易讀 |
| HR09 | supported | 產品上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 主動標註行銷導流期間表現與開發中狀態 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd30 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 證據鏈完整支持安排 jd30 面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 針對大型客戶依部門或分店分工的需求，規劃群組功能 | 能針對大客戶部門/分店分工痛點設計群組權限 |
| HM03 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與E-mail登入取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數付費牆與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18% | 定價實驗與處理週期基準清晰，缺1111功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整 | 具新舊系統並行相容、重複信箱驗證與防冒用閉環 |
| HM08 | partial | 將業務規則轉為可與工程討論的條件描述 | 能將業務規則轉為工程條件，惟取數與DBA協作 |
| HM09 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程 | 依客服回饋修正登入操作流程與AI推薦規則 |
| HM12 | supported | 具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd30 明文條件獨立取證判讀 | 僅依 jd30 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd30 |
| 2 | 具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗 |
| 3 | 已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 必備條件要求「理解 API、JSON 與基本 SQL」，履歷雖載明 API 串接規劃與擬定資料表欄位與 DBA 協作取數，但未明文呈現 JSON 與自行撰寫 SQL | 請分享你如何「以 Claude Code 建立協作流程與共用 skill，並將業務規則轉為可與工程討論的條件描述」？另外能否說明 KOOL 上線後的規模與轉換數據？ |
| 2 | 1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據 | 你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？ |
| 3 | 資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節 | 在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd30 證明遺留系統重構與B2B組織權限設計力
- 尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd30 展現嚴謹對照實驗與商業變現能力
- 1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd30 展現資安危機閉環與10單位治理效率

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：必備條件要求「理解 API、JSON 與基本 SQL」，履歷雖載明 API 串接規劃與擬定資料表欄位與 DBA 協作取數，但未明文呈現 JSON 與自行撰寫 SQL
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落
- 位置：1111 全球華人經歷第 1、2、4、6 點
  - 原句：整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：強

### 8. 未測試聲明
PDF 抽字：risk（本機實測 `resume-v10.2-twocol.pdf` 粗體疊字已完全修復，惟仍有雙欄跨頁斷句與 Type3 康熙部首字元風險） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 Resume_v10.2_twocol（jd31 資深產品經理【擴編】｜人易科技 (NUEIP)）｜第 8 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.2_twocol","job_id":"jd31","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd31-08","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上產品規劃與需求訪談、熟悉0到1或迭代流程","type":"required","status":"partial","evidence":["對接 10 個需求單位；使用者訪談與問卷"],"blocks_interview":false,"reason":"具0到1與迭代經驗，惟B2B需求多由內部10單位轉交，缺直接拜訪客戶與售前支援描寫"},{"id":"R02","text":"具備專案管理與風險管理經驗","type":"required","status":"supported","evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"blocks_interview":false,"reason":"具50大項功能時程控管、新舊系統並行與帳號防冒用風控"},{"id":"R03","text":"有多系統整合或API串接經驗","type":"required","status":"supported","evidence":["API 串接規劃、舊系統資料盤點與新舊流程銜接"],"blocks_interview":false,"reason":"具前後端分離改版、新舊系統並行銜接與跨國金流串接"},{"id":"R04","text":"熟悉PRD、功能規格與流程圖設計","type":"required","status":"supported","evidence":["系統分析、流程圖／循序圖、Wireframe、Prototype、PRD"],"blocks_interview":false,"reason":"產品規格與流程圖產出體系完整"},{"id":"R05","text":"熟悉敏捷開發流程（Scrum）","type":"required","status":"supported","evidence":["曾參與每週一個 Sprint 的 Scrum，現行以 Kanban"],"blocks_interview":false,"reason":"明確具備每週一Sprint之Scrum與Kanban雙重實務"},{"id":"R06","text":"曾主導企業級系統（ERP/HRM/SaaS/平台）規劃","type":"preferred","status":"supported","evidence":["人力銀行企業端招募系統專案負責人，服務逾 6 萬家廠商"],"blocks_interview":false,"reason":"直接主導企業招募平台與部門/分店群組權限，與HRM高度同源"},{"id":"R07","text":"具備資料分析能力（SQL/BI工具）與技術背景","type":"preferred","status":"partial","evidence":["擬定資料表與欄位需求，與 DBA 協作取數"],"blocks_interview":false,"reason":"懂資料庫欄位、API與系統分析，惟非自寫SQL/BI"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["系統服務逾 6 萬家活躍付費廠商（2026 Q3）"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"足夠","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"missing":["核心職責要求「直接與客戶進行需求訪談」與「業務支援與售前規劃（參與客戶會議、產品展示）」，履歷目前僅寫對接內部業務與客服等 10 單位"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["廠商反映的溝通中斷問題，使我優先推進信件與即時通整合"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"足夠","evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"missing":["群組功能與新版求才系統未列上線後客戶採用率數據"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"於 2026/04 完成登入驗證調整...至 2026/10 未再出現同類冒用","kinds":["output","outcome"]},{"quote":"兩案均在開發中，信件與即時通整合已進入公司內部封測","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"partial","resume_evidence":["對接 10 個需求單位；使用者訪談與問卷"],"application_note":"對位 jd31 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 Product Owner，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["擬定資料表與欄位需求，與 DBA 協作取數"],"application_note":"清楚界定個人規劃與DBA/工程/DS分工"},{"rule_id":"HR04","status":"partial","resume_evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"application_note":"具處理週期與定價實驗數據，缺1111功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與E-mail登入驗證取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端成長型產品演進至B2B大型平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["透過互動原型與 FAQ 向客服、業務說明功能"],"application_note":"Scrum、原型、FAQ教學、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"application_note":"段落清楚，重點指標與背景脈絡易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["產品上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"主動標註行銷導流期間表現與開發中狀態"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd31 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"partial","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"application_note":"建議先釐清 jd31 關鍵條件再安排面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["針對大型客戶依部門或分店分工的需求，規劃群組功能"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線的新版第一階段、群組功能與 AI 推薦人才，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"partial","resume_evidence":["將業務規則轉為可與工程討論的條件描述"],"evidence_type":"output","source_ids":[],"interview_question":"請說明如何將業務規則轉為工程條件描述，以及是否具基礎 SQL/JSON 實作經驗？"},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"在 1111 規劃「大型客戶依部門或分店分工的群組功能」時，你是否曾親自與業務一同拜訪企業客戶進行需求訪談或產品展示（Pre-sales）？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd31 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定條件或技術工具細節待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"職缺第 1、2 項核心職責要求「直接與客戶進行需求訪談」與「共同參與客戶會議、產品展示（Pre-sales）」，履歷目前描寫偏向透過內部業務與客服等 10 個單位收斂需求","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"1111上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 全球華人經歷第 1、2、4、6 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線","reason":"1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證"}],"decision":{"recommendation":"clarify_first","evidence":["對接 10 個需求單位；使用者訪談與問卷","約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"blocking_unknowns":["職缺第 1、2 項核心職責要求「直接與客戶進行需求訪談」與「共同參與客戶會議、產品展示（Pre-sales）」，履歷目前描寫偏向透過內部業務與客服等 10 個單位收斂需求"]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd31","具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗","已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環"],"key_gaps":["職缺第 1、2 項核心職責要求「直接與客戶進行需求訪談」與「共同參與客戶會議、產品展示（Pre-sales）」，履歷目前描寫偏向透過內部業務與客服等 10 個單位收斂需求","1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據","資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節"],"strengths":["1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd31 證明遺留系統重構與B2B組織權限設計力","尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd31 展現嚴謹對照實驗與商業變現能力","1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd31 展現資安危機閉環與10單位治理效率"],"interview_questions":["在 1111 規劃「大型客戶依部門或分店分工的群組功能」時，你是否曾親自與業務一同拜訪企業客戶進行需求訪談或產品展示（Pre-sales）？","你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？","在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":7,"uncertainty_levels":1,"basis":"針對 jd31 具備多個已實現案例、清楚取捨與跨部門治理實證（惟1111功能缺上線後採用率outcome數據且開發中案例不撐起Level 9，故評為Level 7）"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：clarify_first
- Level：7（±1）
- 一句話理由：「針對大型客戶依部門或分店分工的需求，規劃群組功能」高度相關，惟缺直接拜訪客戶與售前展示描寫，建議先釐清。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 系統服務逾 6 萬家活躍付費廠商（2026 Q3） | 無關鍵缺口，可於面試深化 |
| role_evidence | 足夠 | 近 10 年 PM 經驗，經手 6 款產品 | 核心職責要求「直接與客戶進行需求訪談」與「業務支援與售前規劃（參與客戶會議、產品展示）」，履歷目前僅寫對接內部業務與客服等 10 單位 |
| decision_depth | 強 | 廠商反映的溝通中斷問題，使我優先推進信件與即時通整合 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 足夠 | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 群組功能與新版求才系統未列上線後客戶採用率數據 |
| ownership | 強 | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 3年以上產品規劃與需求訪談、熟悉0到1或迭代流程 | 必要 | partial | 對接 10 個需求單位；使用者訪談與問卷 | 具0到1與迭代經驗，惟B2B需求多由內部10單位轉交，缺直接拜訪客戶與售前支援描寫 |
| R02 具備專案管理與風險管理經驗 | 必要 | supported | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 具50大項功能時程控管、新舊系統並行與帳號防冒用風控 |
| R03 有多系統整合或API串接經驗 | 必要 | supported | API 串接規劃、舊系統資料盤點與新舊流程銜接 | 具前後端分離改版、新舊系統並行銜接與跨國金流串接 |
| R04 熟悉PRD、功能規格與流程圖設計 | 必要 | supported | 系統分析、流程圖／循序圖、Wireframe、Prototype、PRD | 產品規格與流程圖產出體系完整 |
| R05 熟悉敏捷開發流程（Scrum） | 必要 | supported | 曾參與每週一個 Sprint 的 Scrum，現行以 Kanban | 明確具備每週一Sprint之Scrum與Kanban雙重實務 |
| R06 曾主導企業級系統（ERP/HRM/SaaS/平台）規劃 | 加分 | supported | 人力銀行企業端招募系統專案負責人，服務逾 6 萬家廠商 | 直接主導企業招募平台與部門/分店群組權限，與HRM高度同源 |
| R07 具備資料分析能力（SQL/BI工具）與技術背景 | 加分 | partial | 擬定資料表與欄位需求，與 DBA 協作取數 | 懂資料庫欄位、API與系統分析，惟非自寫SQL/BI |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | partial | 對接 10 個需求單位；使用者訪談與問卷 | 對位 jd31 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 Product Owner，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 擬定資料表與欄位需求，與 DBA 協作取數 | 清楚界定個人規劃與DBA/工程/DS分工 |
| HR04 | partial | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 具處理週期與定價實驗數據，缺1111功能採用率 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現功能優先序與E-mail登入驗證取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端成長型產品演進至B2B大型平台主任 |
| HR07 | supported | 透過互動原型與 FAQ 向客服、業務說明功能 | Scrum、原型、FAQ教學、AI與英文協作皆有實例 |
| HR08 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 段落清楚，重點指標與背景脈絡易讀 |
| HR09 | supported | 產品上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 主動標註行銷導流期間表現與開發中狀態 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd31 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | partial | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 建議先釐清 jd31 關鍵條件再安排面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 針對大型客戶依部門或分店分工的需求，規劃群組功能 | 能針對大客戶部門/分店分工痛點設計群組權限 |
| HM03 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與E-mail登入取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數付費牆與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18% | 定價實驗與處理週期基準清晰，缺1111功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整 | 具新舊系統並行相容、重複信箱驗證與防冒用閉環 |
| HM08 | partial | 將業務規則轉為可與工程討論的條件描述 | 能將業務規則轉為工程條件，惟取數與DBA協作 |
| HM09 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程 | 依客服回饋修正登入操作流程與AI推薦規則 |
| HM12 | supported | 具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd31 明文條件獨立取證判讀 | 僅依 jd31 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd31 |
| 2 | 具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗 |
| 3 | 已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 職缺第 1、2 項核心職責要求「直接與客戶進行需求訪談」與「共同參與客戶會議、產品展示（Pre-sales）」，履歷目前描寫偏向透過內部業務與客服等 10 個單位收斂需求 | 在 1111 規劃「大型客戶依部門或分店分工的群組功能」時，你是否曾親自與業務一同拜訪企業客戶進行需求訪談或產品展示（Pre-sales）？ |
| 2 | 1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據 | 你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？ |
| 3 | 資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節 | 在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd31 證明遺留系統重構與B2B組織權限設計力
- 尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd31 展現嚴謹對照實驗與商業變現能力
- 1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd31 展現資安危機閉環與10單位治理效率

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：職缺第 1、2 項核心職責要求「直接與客戶進行需求訪談」與「共同參與客戶會議、產品展示（Pre-sales）」，履歷目前描寫偏向透過內部業務與客服等 10 個單位收斂需求
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落
- 位置：1111 全球華人經歷第 1、2、4、6 點
  - 原句：整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：risk（本機實測 `resume-v10.2-twocol.pdf` 粗體疊字已完全修復，惟仍有雙欄跨頁斷句與 Type3 康熙部首字元風險） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 Resume_v10.2_twocol（jd32 產品專案經理(內部系統)｜104人力銀行）｜第 9 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.2_twocol","job_id":"jd32","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd32-09","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上經驗且具網站開發或SA系統分析經驗","type":"required","status":"supported","evidence":["釐清需求並完成系統分析後，設計流程與畫面、撰寫 PRD"],"blocks_interview":false,"reason":"現任同業招募系統PO且親自執行系統分析、資料欄位對照與重構"},{"id":"R02","text":"接手內部使用者與外部客戶議題並安排優化或修正","type":"required","status":"supported","evidence":["統整各單位提出的功能需求與使用問題，追蹤處理進度並每週回報"],"blocks_interview":false,"reason":"統整10個需求單位之功能需求與使用問題，處理週期降至30.9天"},{"id":"R03","text":"運用AI工具進行營運分析或提案","type":"required","status":"supported","evidence":["以 Claude Code 建立協作流程與共用 skill"],"blocks_interview":false,"reason":"深入運用Claude Code與AI Agent整理分析資料與轉譯業務規則"},{"id":"R04","text":"熟悉規格撰寫、跨單位溝通與評估時程可行性","type":"required","status":"supported","evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"blocks_interview":false,"reason":"規格完整且將跨單位案件平均處理時間縮短近70%"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["系統服務逾 6 萬家活躍付費廠商（2026 Q3）"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"強","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"missing":[],"issue_ids":[]},{"id":"decision_depth","rating":"強","evidence":["廠商反映的溝通中斷問題，使我優先推進信件與即時通整合"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"於 2026/04 完成登入驗證調整...至 2026/10 未再出現同類冒用","kinds":["output","outcome"]},{"quote":"兩案均在開發中，信件與即時通整合已進入公司內部封測","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["釐清需求並完成系統分析後，設計流程與畫面、撰寫 PRD"],"application_note":"對位 jd32 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 Product Owner，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["擬定資料表與欄位需求，與 DBA 協作取數"],"application_note":"清楚界定個人規劃與DBA/工程/DS分工"},{"rule_id":"HR04","status":"partial","resume_evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"application_note":"具處理週期與定價實驗數據，缺1111功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與E-mail登入驗證取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端成長型產品演進至B2B大型平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["透過互動原型與 FAQ 向客服、業務說明功能"],"application_note":"Scrum、原型、FAQ教學、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"application_note":"段落清楚，重點指標與背景脈絡易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["產品上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"主動標註行銷導流期間表現與開發中狀態"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd32 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"application_note":"證據鏈完整支持安排 jd32 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["針對大型客戶依部門或分店分工的需求，規劃群組功能"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線的新版第一階段、群組功能與 AI 推薦人才，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["將業務規則轉為可與工程討論的條件描述"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"你在 1111 將各單位需求與問題單的平均處理時間由 100.4 天降至 30.9 天的具體排程與分流機制為何？如何運用 Claude Code 與 AI Agent 協助需求分析與規格撰寫？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd32 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定條件或技術工具細節待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"自傳提到「希望把更多心力放回產品策略」，而本職缺聚焦於「內部營運用網站的功能設計與議題修正」，需於面試對齊職涯期待；另兩案（信件與即時通整合、搜尋改版）尚在開發中","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"1111上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 全球華人經歷第 1、2、4、6 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線","reason":"1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["釐清需求並完成系統分析後，設計流程與畫面、撰寫 PRD","約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd32","具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗","已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環"],"key_gaps":["自傳提到「希望把更多心力放回產品策略」，而本職缺聚焦於「內部營運用網站的功能設計與議題修正」，需於面試對齊職涯期待；另兩案（信件與即時通整合、搜尋改版）尚在開發中","1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據","資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節"],"strengths":["1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd32 證明遺留系統重構與B2B組織權限設計力","尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd32 展現嚴謹對照實驗與商業變現能力","1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd32 展現資安危機閉環與10單位治理效率"],"interview_questions":["你在 1111 將各單位需求與問題單的平均處理時間由 100.4 天降至 30.9 天的具體排程與分流機制為何？如何運用 Claude Code 與 AI Agent 協助需求分析與規格撰寫？","你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？","在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd32 具備多個已實現案例、清楚取捨與跨部門治理實證（惟1111功能缺上線後採用率outcome數據且開發中案例不撐起Level 9，故評為Level 8）"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：現任同業招募系統 PO，「重新制定業務流程、對照資料欄位並重構規格」且將處理時間由 100.4 天降至 30.9 天，完全對口。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 系統服務逾 6 萬家活躍付費廠商（2026 Q3） | 無關鍵缺口，可於面試深化 |
| role_evidence | 強 | 近 10 年 PM 經驗，經手 6 款產品 | 無關鍵缺口，可於面試深化 |
| decision_depth | 強 | 廠商反映的溝通中斷問題，使我優先推進信件與即時通整合 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 3年以上經驗且具網站開發或SA系統分析經驗 | 必要 | supported | 釐清需求並完成系統分析後，設計流程與畫面、撰寫 PRD | 現任同業招募系統PO且親自執行系統分析、資料欄位對照與重構 |
| R02 接手內部使用者與外部客戶議題並安排優化或修正 | 必要 | supported | 統整各單位提出的功能需求與使用問題，追蹤處理進度並每週回報 | 統整10個需求單位之功能需求與使用問題，處理週期降至30.9天 |
| R03 運用AI工具進行營運分析或提案 | 必要 | supported | 以 Claude Code 建立協作流程與共用 skill | 深入運用Claude Code與AI Agent整理分析資料與轉譯業務規則 |
| R04 熟悉規格撰寫、跨單位溝通與評估時程可行性 | 必要 | supported | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 規格完整且將跨單位案件平均處理時間縮短近70% |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 釐清需求並完成系統分析後，設計流程與畫面、撰寫 PRD | 對位 jd32 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 Product Owner，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 擬定資料表與欄位需求，與 DBA 協作取數 | 清楚界定個人規劃與DBA/工程/DS分工 |
| HR04 | partial | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 具處理週期與定價實驗數據，缺1111功能採用率 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現功能優先序與E-mail登入驗證取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端成長型產品演進至B2B大型平台主任 |
| HR07 | supported | 透過互動原型與 FAQ 向客服、業務說明功能 | Scrum、原型、FAQ教學、AI與英文協作皆有實例 |
| HR08 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 段落清楚，重點指標與背景脈絡易讀 |
| HR09 | supported | 產品上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 主動標註行銷導流期間表現與開發中狀態 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd32 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 證據鏈完整支持安排 jd32 面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 針對大型客戶依部門或分店分工的需求，規劃群組功能 | 能針對大客戶部門/分店分工痛點設計群組權限 |
| HM03 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與E-mail登入取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數付費牆與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18% | 定價實驗與處理週期基準清晰，缺1111功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整 | 具新舊系統並行相容、重複信箱驗證與防冒用閉環 |
| HM08 | supported | 將業務規則轉為可與工程討論的條件描述 | 能將業務規則轉為工程條件，惟取數與DBA協作 |
| HM09 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程 | 依客服回饋修正登入操作流程與AI推薦規則 |
| HM12 | supported | 具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd32 明文條件獨立取證判讀 | 僅依 jd32 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd32 |
| 2 | 具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗 |
| 3 | 已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 自傳提到「希望把更多心力放回產品策略」，而本職缺聚焦於「內部營運用網站的功能設計與議題修正」，需於面試對齊職涯期待；另兩案（信件與即時通整合、搜尋改版）尚在開發中 | 你在 1111 將各單位需求與問題單的平均處理時間由 100.4 天降至 30.9 天的具體排程與分流機制為何？如何運用 Claude Code 與 AI Agent 協助需求分析與規格撰寫？ |
| 2 | 1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據 | 你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？ |
| 3 | 資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節 | 在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd32 證明遺留系統重構與B2B組織權限設計力
- 尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd32 展現嚴謹對照實驗與商業變現能力
- 1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd32 展現資安危機閉環與10單位治理效率

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：自傳提到「希望把更多心力放回產品策略」，而本職缺聚焦於「內部營運用網站的功能設計與議題修正」，需於面試對齊職涯期待；另兩案（信件與即時通整合、搜尋改版）尚在開發中
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落
- 位置：1111 全球華人經歷第 1、2、4、6 點
  - 原句：整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：強

### 8. 未測試聲明
PDF 抽字：risk（本機實測 `resume-v10.2-twocol.pdf` 粗體疊字已完全修復，惟仍有雙欄跨頁斷句與 Type3 康熙部首字元風險） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 Resume_v10.2_twocol（jd34 SaaS 產品經理 / Product Owner｜91APP）｜第 10 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.2_twocol","job_id":"jd34","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd34-10","human_calibrated":false,"requirements":[{"id":"R01","text":"5年以上經驗（含2年以上產品管理經驗）","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"資深PM與B2B平台PO年資充足"},{"id":"R02","text":"金流、物流、會員、促購、優惠券、購買流程、訂單經驗","type":"required","status":"partial","evidence":["另規劃並上線 VIP 訂閱、點數付費牆；7／30／90 天訂閱方案與加贈"],"blocks_interview":false,"reason":"具金流、會員帳號權限、訂閱點數與加贈方案，缺電商實體物流與OMO庫存訂單"},{"id":"R03","text":"產品管理和設計並與UX/RD/QA密切協作、製作介面","type":"required","status":"supported","evidence":["設計流程與畫面、撰寫 PRD 與製作 Prototype"],"blocks_interview":false,"reason":"完整主導開發循環與UX/RD/QA協作"},{"id":"R04","text":"參與和運作Scrum團隊；定義目標並用數據分析效益","type":"required","status":"supported","evidence":["曾參與每週一個 Sprint 的 Scrum；降價期 iOS 非續訂營收增 5%"],"blocks_interview":false,"reason":"具Scrum經驗與定價實驗效益分析"},{"id":"R05","text":"從0到1開發經驗、支付生態、運用Gen AI加入產品案例","type":"preferred","status":"supported","evidence":["規劃 KOOL 媒合平台；上線 3 項 AI 生成與推薦功能"],"blocks_interview":false,"reason":"同時具備KOOL 0到1媒合平台、CodaPay金流與3項GenAI上線案例"},{"id":"R06","text":"簡報募資提案經驗；200人以上軟體團隊2年以上經驗","type":"preferred","status":"unknown","evidence":["參與公司一級主管日會，向總經理、副總等主管匯報"],"blocks_interview":false,"reason":"具高層匯報經驗，未載明軟體團隊是否逾200人及外部募資簡報"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["系統服務逾 6 萬家活躍付費廠商（2026 Q3）"],"missing":["過往為人力銀行與社交媒合平台，未直接經手零售電商 OMO 虛實融合場景"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"強","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"missing":["缺乏零售電商之實體物流、門市庫存與實體商品訂單管理模組直接經驗"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["廠商反映的溝通中斷問題，使我優先推進信件與即時通整合"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"於 2026/04 完成登入驗證調整...至 2026/10 未再出現同類冒用","kinds":["output","outcome"]},{"quote":"兩案均在開發中，信件與即時通整合已進入公司內部封測","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"對位 jd34 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 Product Owner，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["擬定資料表與欄位需求，與 DBA 協作取數"],"application_note":"清楚界定個人規劃與DBA/工程/DS分工"},{"rule_id":"HR04","status":"partial","resume_evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"application_note":"具處理週期與定價實驗數據，缺1111功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與E-mail登入驗證取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端成長型產品演進至B2B大型平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["透過互動原型與 FAQ 向客服、業務說明功能"],"application_note":"Scrum、原型、FAQ教學、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"application_note":"段落清楚，重點指標與背景脈絡易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["產品上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"主動標註行銷導流期間表現與開發中狀態"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd34 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"application_note":"證據鏈完整支持安排 jd34 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["針對大型客戶依部門或分店分工的需求，規劃群組功能"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線的新版第一階段、群組功能與 AI 推薦人才，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["將業務規則轉為可與工程討論的條件描述"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"你在 1111 規劃「大型客戶部門／分店群組權限」與在 KOOL 設計雙邊媒合付費機制的經驗，如何遷移至 91APP 複雜的「連鎖品牌門市 OMO 權限、優惠券與購物車訂單」場景？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd34 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定條件或技術工具細節待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"具備金流、會員權限、訂閱點數與雙邊媒合經驗，但缺乏零售電商之「實體物流串接、優惠券折抵與門市 OMO 訂單管理」直接經驗，且 1111 功能未附採用率數據","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"1111上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 全球華人經歷第 1、2、4、6 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線","reason":"1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗，經手 6 款產品","約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd34","具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗","已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環"],"key_gaps":["具備金流、會員權限、訂閱點數與雙邊媒合經驗，但缺乏零售電商之「實體物流串接、優惠券折抵與門市 OMO 訂單管理」直接經驗，且 1111 功能未附採用率數據","1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據","資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節"],"strengths":["1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd34 證明遺留系統重構與B2B組織權限設計力","尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd34 展現嚴謹對照實驗與商業變現能力","1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd34 展現資安危機閉環與10單位治理效率"],"interview_questions":["你在 1111 規劃「大型客戶部門／分店群組權限」與在 KOOL 設計雙邊媒合付費機制的經驗，如何遷移至 91APP 複雜的「連鎖品牌門市 OMO 權限、優惠券與購物車訂單」場景？","你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？","在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd34 具備多個已實現案例、清楚取捨與跨部門治理實證（惟1111功能缺上線後採用率outcome數據且開發中案例不撐起Level 9，故評為Level 8）"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：具「服務逾 6 萬家活躍付費廠商」B2B 平台、Scrum、訂閱點數金流與 3 項 GenAI 上線實績，支持約談。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 系統服務逾 6 萬家活躍付費廠商（2026 Q3） | 過往為人力銀行與社交媒合平台，未直接經手零售電商 OMO 虛實融合場景 |
| role_evidence | 強 | 近 10 年 PM 經驗，經手 6 款產品 | 缺乏零售電商之實體物流、門市庫存與實體商品訂單管理模組直接經驗 |
| decision_depth | 強 | 廠商反映的溝通中斷問題，使我優先推進信件與即時通整合 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 5年以上經驗（含2年以上產品管理經驗） | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 資深PM與B2B平台PO年資充足 |
| R02 金流、物流、會員、促購、優惠券、購買流程、訂單經驗 | 必要 | partial | 另規劃並上線 VIP 訂閱、點數付費牆；7／30／90 天訂閱方案與加贈 | 具金流、會員帳號權限、訂閱點數與加贈方案，缺電商實體物流與OMO庫存訂單 |
| R03 產品管理和設計並與UX/RD/QA密切協作、製作介面 | 必要 | supported | 設計流程與畫面、撰寫 PRD 與製作 Prototype | 完整主導開發循環與UX/RD/QA協作 |
| R04 參與和運作Scrum團隊；定義目標並用數據分析效益 | 必要 | supported | 曾參與每週一個 Sprint 的 Scrum；降價期 iOS 非續訂營收增 5% | 具Scrum經驗與定價實驗效益分析 |
| R05 從0到1開發經驗、支付生態、運用Gen AI加入產品案例 | 加分 | supported | 規劃 KOOL 媒合平台；上線 3 項 AI 生成與推薦功能 | 同時具備KOOL 0到1媒合平台、CodaPay金流與3項GenAI上線案例 |
| R06 簡報募資提案經驗；200人以上軟體團隊2年以上經驗 | 加分 | unknown | 參與公司一級主管日會，向總經理、副總等主管匯報 | 具高層匯報經驗，未載明軟體團隊是否逾200人及外部募資簡報 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 對位 jd34 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 Product Owner，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 擬定資料表與欄位需求，與 DBA 協作取數 | 清楚界定個人規劃與DBA/工程/DS分工 |
| HR04 | partial | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 具處理週期與定價實驗數據，缺1111功能採用率 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現功能優先序與E-mail登入驗證取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端成長型產品演進至B2B大型平台主任 |
| HR07 | supported | 透過互動原型與 FAQ 向客服、業務說明功能 | Scrum、原型、FAQ教學、AI與英文協作皆有實例 |
| HR08 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 段落清楚，重點指標與背景脈絡易讀 |
| HR09 | supported | 產品上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 主動標註行銷導流期間表現與開發中狀態 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd34 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 證據鏈完整支持安排 jd34 面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 針對大型客戶依部門或分店分工的需求，規劃群組功能 | 能針對大客戶部門/分店分工痛點設計群組權限 |
| HM03 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與E-mail登入取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數付費牆與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18% | 定價實驗與處理週期基準清晰，缺1111功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整 | 具新舊系統並行相容、重複信箱驗證與防冒用閉環 |
| HM08 | supported | 將業務規則轉為可與工程討論的條件描述 | 能將業務規則轉為工程條件，惟取數與DBA協作 |
| HM09 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程 | 依客服回饋修正登入操作流程與AI推薦規則 |
| HM12 | supported | 具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd34 明文條件獨立取證判讀 | 僅依 jd34 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd34 |
| 2 | 具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗 |
| 3 | 已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 具備金流、會員權限、訂閱點數與雙邊媒合經驗，但缺乏零售電商之「實體物流串接、優惠券折抵與門市 OMO 訂單管理」直接經驗，且 1111 功能未附採用率數據 | 你在 1111 規劃「大型客戶部門／分店群組權限」與在 KOOL 設計雙邊媒合付費機制的經驗，如何遷移至 91APP 複雜的「連鎖品牌門市 OMO 權限、優惠券與購物車訂單」場景？ |
| 2 | 1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據 | 你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？ |
| 3 | 資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節 | 在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd34 證明遺留系統重構與B2B組織權限設計力
- 尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd34 展現嚴謹對照實驗與商業變現能力
- 1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd34 展現資安危機閉環與10單位治理效率

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：具備金流、會員權限、訂閱點數與雙邊媒合經驗，但缺乏零售電商之「實體物流串接、優惠券折抵與門市 OMO 訂單管理」直接經驗，且 1111 功能未附採用率數據
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落
- 位置：1111 全球華人經歷第 1、2、4、6 點
  - 原句：整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：強

### 8. 未測試聲明
PDF 抽字：risk（本機實測 `resume-v10.2-twocol.pdf` 粗體疊字已完全修復，惟仍有雙欄跨頁斷句與 Type3 康熙部首字元風險） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 Resume_v10.2_twocol（jd36 全支付- Product Manager (內部系統、串接)）｜第 11 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.2_twocol","job_id":"jd36","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd36-11","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上相關工作經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"年資近10年且具豐富後台與系統改版經驗"},{"id":"R02","text":"能運用Axure撰寫規劃，透過Jira/Confluence管理","type":"required","status":"partial","evidence":["Figma、Axure RP、Notion、Trello、內部工單與看板系統"],"blocks_interview":false,"reason":"Axure原型與PRD經驗豐富，惟使用內部工單看板系統非Jira"},{"id":"R03","text":"同步考慮技術可行性及系統架構關連影響","type":"required","status":"supported","evidence":["重新制定業務流程、對照資料欄位並重構規格，處理新舊系統並行"],"blocks_interview":false,"reason":"親做系統分析、資料欄位對照與新舊系統並行分階段交付"},{"id":"R04","text":"熟悉API規格；與合作方確認需求並與法遵確認適法性","type":"required","status":"supported","evidence":["API 串接規劃；法務與稽核協作；與 CodaPay 新加坡技術團隊協調串接"],"blocks_interview":false,"reason":"具API串接規劃、外部技術團隊對接與法務稽核協作"},{"id":"R05","text":"執行測試驗收、上線協調與內部教育訓練","type":"required","status":"supported","evidence":["透過互動原型與 FAQ 向客服、業務說明功能"],"blocks_interview":false,"reason":"具UAT制定、上線計畫與透過互動原型/FAQ向客服業務進行內部教育訓練"},{"id":"R06","text":"熟悉代理收付、電子支付領域知識；資管或資工畢或相關經驗","type":"preferred","status":"partial","evidence":["整理抽成、稅、手續費與撥款週期，完成實收試算"],"blocks_interview":false,"reason":"具金流撥款試算與10年軟體PM經驗，無銀行專線或電支清算後台"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["系統服務逾 6 萬家活躍付費廠商（2026 Q3）"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"足夠","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"missing":["未直接經手銀行端串接或專營電子支付機構內部清算後台；專案工具為內部工單與看板系統而非 Jira"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["廠商反映的溝通中斷問題，使我優先推進信件與即時通整合"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"於 2026/04 完成登入驗證調整...至 2026/10 未再出現同類冒用","kinds":["output","outcome"]},{"quote":"兩案均在開發中，信件與即時通整合已進入公司內部封測","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"對位 jd36 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 Product Owner，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["擬定資料表與欄位需求，與 DBA 協作取數"],"application_note":"清楚界定個人規劃與DBA/工程/DS分工"},{"rule_id":"HR04","status":"partial","resume_evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"application_note":"具處理週期與定價實驗數據，缺1111功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與E-mail登入驗證取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端成長型產品演進至B2B大型平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["透過互動原型與 FAQ 向客服、業務說明功能"],"application_note":"Scrum、原型、FAQ教學、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"application_note":"段落清楚，重點指標與背景脈絡易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["產品上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"主動標註行銷導流期間表現與開發中狀態"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd36 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"application_note":"證據鏈完整支持安排 jd36 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["針對大型客戶依部門或分店分工的需求，規劃群組功能"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線的新版第一階段、群組功能與 AI 推薦人才，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["將業務規則轉為可與工程討論的條件描述"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"過去在進行 CodaPay 跨國金流 API 串接與 1111 新舊系統並行改版時，你如何定義 API 欄位對照、錯誤處理與帳務或資料同步異常排查流程？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd36 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定條件或技術工具細節待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"具備第三方金流 CodaPay 串接與撥款實收試算經驗，但未直接經手銀行端專線串接或電子支付機構內部代理收付清算系統；工具未直接點名 Jira/Confluence","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"1111上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 全球華人經歷第 1、2、4、6 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線","reason":"1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗，經手 6 款產品","約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd36","具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗","已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環"],"key_gaps":["具備第三方金流 CodaPay 串接與撥款實收試算經驗，但未直接經手銀行端專線串接或電子支付機構內部代理收付清算系統；工具未直接點名 Jira/Confluence","1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據","資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節"],"strengths":["1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd36 證明遺留系統重構與B2B組織權限設計力","尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd36 展現嚴謹對照實驗與商業變現能力","1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd36 展現資安危機閉環與10單位治理效率"],"interview_questions":["過去在進行 CodaPay 跨國金流 API 串接與 1111 新舊系統並行改版時，你如何定義 API 欄位對照、錯誤處理與帳務或資料同步異常排查流程？","你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？","在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":7,"uncertainty_levels":1,"basis":"針對 jd36 具備多個已實現案例、清楚取捨與跨部門治理實證（惟1111功能缺上線後採用率outcome數據且開發中案例不撐起Level 9，故評為Level 7）"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：7（±1）
- 一句話理由：「重新制定業務流程、對照資料欄位並重構規格，處理新舊系統並行的相容性需求」且具 Axure 與金流串接經驗，支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 系統服務逾 6 萬家活躍付費廠商（2026 Q3） | 無關鍵缺口，可於面試深化 |
| role_evidence | 足夠 | 近 10 年 PM 經驗，經手 6 款產品 | 未直接經手銀行端串接或專營電子支付機構內部清算後台；專案工具為內部工單與看板系統而非 Jira |
| decision_depth | 強 | 廠商反映的溝通中斷問題，使我優先推進信件與即時通整合 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 3年以上相關工作經驗 | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 年資近10年且具豐富後台與系統改版經驗 |
| R02 能運用Axure撰寫規劃，透過Jira/Confluence管理 | 必要 | partial | Figma、Axure RP、Notion、Trello、內部工單與看板系統 | Axure原型與PRD經驗豐富，惟使用內部工單看板系統非Jira |
| R03 同步考慮技術可行性及系統架構關連影響 | 必要 | supported | 重新制定業務流程、對照資料欄位並重構規格，處理新舊系統並行 | 親做系統分析、資料欄位對照與新舊系統並行分階段交付 |
| R04 熟悉API規格；與合作方確認需求並與法遵確認適法性 | 必要 | supported | API 串接規劃；法務與稽核協作；與 CodaPay 新加坡技術團隊協調串接 | 具API串接規劃、外部技術團隊對接與法務稽核協作 |
| R05 執行測試驗收、上線協調與內部教育訓練 | 必要 | supported | 透過互動原型與 FAQ 向客服、業務說明功能 | 具UAT制定、上線計畫與透過互動原型/FAQ向客服業務進行內部教育訓練 |
| R06 熟悉代理收付、電子支付領域知識；資管或資工畢或相關經驗 | 加分 | partial | 整理抽成、稅、手續費與撥款週期，完成實收試算 | 具金流撥款試算與10年軟體PM經驗，無銀行專線或電支清算後台 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 對位 jd36 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 Product Owner，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 擬定資料表與欄位需求，與 DBA 協作取數 | 清楚界定個人規劃與DBA/工程/DS分工 |
| HR04 | partial | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 具處理週期與定價實驗數據，缺1111功能採用率 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現功能優先序與E-mail登入驗證取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端成長型產品演進至B2B大型平台主任 |
| HR07 | supported | 透過互動原型與 FAQ 向客服、業務說明功能 | Scrum、原型、FAQ教學、AI與英文協作皆有實例 |
| HR08 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 段落清楚，重點指標與背景脈絡易讀 |
| HR09 | supported | 產品上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 主動標註行銷導流期間表現與開發中狀態 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd36 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 證據鏈完整支持安排 jd36 面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 針對大型客戶依部門或分店分工的需求，規劃群組功能 | 能針對大客戶部門/分店分工痛點設計群組權限 |
| HM03 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與E-mail登入取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數付費牆與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18% | 定價實驗與處理週期基準清晰，缺1111功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整 | 具新舊系統並行相容、重複信箱驗證與防冒用閉環 |
| HM08 | supported | 將業務規則轉為可與工程討論的條件描述 | 能將業務規則轉為工程條件，惟取數與DBA協作 |
| HM09 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程 | 依客服回饋修正登入操作流程與AI推薦規則 |
| HM12 | supported | 具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd36 明文條件獨立取證判讀 | 僅依 jd36 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd36 |
| 2 | 具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗 |
| 3 | 已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 具備第三方金流 CodaPay 串接與撥款實收試算經驗，但未直接經手銀行端專線串接或電子支付機構內部代理收付清算系統；工具未直接點名 Jira/Confluence | 過去在進行 CodaPay 跨國金流 API 串接與 1111 新舊系統並行改版時，你如何定義 API 欄位對照、錯誤處理與帳務或資料同步異常排查流程？ |
| 2 | 1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據 | 你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？ |
| 3 | 資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節 | 在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd36 證明遺留系統重構與B2B組織權限設計力
- 尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd36 展現嚴謹對照實驗與商業變現能力
- 1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd36 展現資安危機閉環與10單位治理效率

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：具備第三方金流 CodaPay 串接與撥款實收試算經驗，但未直接經手銀行端專線串接或電子支付機構內部代理收付清算系統；工具未直接點名 Jira/Confluence
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落
- 位置：1111 全球華人經歷第 1、2、4、6 點
  - 原句：整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：risk（本機實測 `resume-v10.2-twocol.pdf` 粗體疊字已完全修復，惟仍有雙欄跨頁斷句與 Type3 康熙部首字元風險） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 Resume_v10.2_twocol（jd40 【PMC】軟體產品經理 (PM / TPM)｜QuickClick快一點）｜第 12 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.2_twocol","job_id":"jd40","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd40-12","human_calibrated":false,"requirements":[{"id":"R01","text":"5年以上軟體產品、技術產品或技術專案管理經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗；約 50 項大項功能上線"],"blocks_interview":false,"reason":"年資近10年且大型系統改版與交付經驗扎實"},{"id":"R02","text":"參與產品從需求規劃到上線交付的完整流程","type":"required","status":"supported","evidence":["涵蓋系統分析、流程與畫面設計、PRD、Prototype、UAT"],"blocks_interview":false,"reason":"完整主導端到端產品開發與上線交付週期"},{"id":"R03","text":"能理解API、資料流程及系統串接邏輯","type":"required","status":"supported","evidence":["API 串接規劃、舊系統資料盤點與新舊流程銜接"],"blocks_interview":false,"reason":"具系統分析、API串接與資料庫欄位結構理解"},{"id":"R04","text":"具備需求拆解、優先順序判斷、跨團隊溝通及風險管理","type":"required","status":"supported","evidence":["依使用者旅程與工單問題安排優先級；於 2026/04 完成登入驗證調整"],"blocks_interview":false,"reason":"具體展現工單痛點優先排序、重複信箱處理與資安風控"},{"id":"R05","text":"KA客戶/客製化或NRE專案交付管理；支付/餐飲/零售/SaaS經驗","type":"required","status":"partial","evidence":["針對大型客戶依部門或分店分工的需求，規劃群組功能"],"blocks_interview":false,"reason":"具大型客戶群組功能與支付經驗，惟未呈現KA客戶NRE客製化合約範疇與變更控管"},{"id":"R06","text":"基本SQL查詢或資料分析能力；高階利害關係人溝通","type":"preferred","status":"partial","evidence":["向總經理、副總等主管匯報；與 DBA 協作取數"],"blocks_interview":false,"reason":"具向總經理/副總匯報與試算表分析經驗，SQL與DBA協作取數"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["系統服務逾 6 萬家活躍付費廠商（2026 Q3）"],"missing":["過往為標準平台產品迭代，未呈現餐飲POS硬體與KA客戶NRE專案交付經驗"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"足夠","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"missing":["職責要求參與 KA 客戶與 NRE 專案交付管理（管理客戶期待與需求變更），履歷未呈現外部客戶合約與 NRE 專案控管證據"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["廠商反映的溝通中斷問題，使我優先推進信件與即時通整合"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"足夠","evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"missing":["1111新系統與群組功能未列上線後採用數據"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"於 2026/04 完成登入驗證調整...至 2026/10 未再出現同類冒用","kinds":["output","outcome"]},{"quote":"兩案均在開發中，信件與即時通整合已進入公司內部封測","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"partial","resume_evidence":["近 10 年 PM 經驗；約 50 項大項功能上線"],"application_note":"對位 jd40 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 Product Owner，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["擬定資料表與欄位需求，與 DBA 協作取數"],"application_note":"清楚界定個人規劃與DBA/工程/DS分工"},{"rule_id":"HR04","status":"partial","resume_evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"application_note":"具處理週期與定價實驗數據，缺1111功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與E-mail登入驗證取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端成長型產品演進至B2B大型平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["透過互動原型與 FAQ 向客服、業務說明功能"],"application_note":"Scrum、原型、FAQ教學、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"application_note":"段落清楚，重點指標與背景脈絡易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["產品上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"主動標註行銷導流期間表現與開發中狀態"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd40 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"partial","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"application_note":"建議先釐清 jd40 關鍵條件再安排面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["針對大型客戶依部門或分店分工的需求，規劃群組功能"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線的新版第一階段、群組功能與 AI 推薦人才，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"partial","resume_evidence":["將業務規則轉為可與工程討論的條件描述"],"evidence_type":"output","source_ids":[],"interview_question":"請說明如何將業務規則轉為工程條件描述，以及是否具基礎 SQL/JSON 實作經驗？"},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"在 1111 規劃「大型客戶依部門或分店分工的群組功能」時，是否有直接面對大型企業客戶協商客製化範疇與交付時程的經驗？若面對餐飲連鎖 KA 客戶要求 NRE 客製開發，你如何控管需求變更？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd40 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定條件或技術工具細節待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"職缺核心職責包含「KA 與 NRE 交付管理（管理客戶期待與需求變更）」，履歷雖有規劃大型客戶分店群組功能，但未呈現直接管理外部 KA 客戶客製化合約（NRE）之經驗","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"1111上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 全球華人經歷第 1、2、4、6 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線","reason":"1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證"}],"decision":{"recommendation":"clarify_first","evidence":["近 10 年 PM 經驗；約 50 項大項功能上線","約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"blocking_unknowns":["職缺核心職責包含「KA 與 NRE 交付管理（管理客戶期待與需求變更）」，履歷雖有規劃大型客戶分店群組功能，但未呈現直接管理外部 KA 客戶客製化合約（NRE）之經驗"]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd40","具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗","已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環"],"key_gaps":["職缺核心職責包含「KA 與 NRE 交付管理（管理客戶期待與需求變更）」，履歷雖有規劃大型客戶分店群組功能，但未呈現直接管理外部 KA 客戶客製化合約（NRE）之經驗","1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據","資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節"],"strengths":["1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd40 證明遺留系統重構與B2B組織權限設計力","尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd40 展現嚴謹對照實驗與商業變現能力","1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd40 展現資安危機閉環與10單位治理效率"],"interview_questions":["在 1111 規劃「大型客戶依部門或分店分工的群組功能」時，是否有直接面對大型企業客戶協商客製化範疇與交付時程的經驗？若面對餐飲連鎖 KA 客戶要求 NRE 客製開發，你如何控管需求變更？","你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？","在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":7,"uncertainty_levels":1,"basis":"針對 jd40 具備多個已實現案例、清楚取捨與跨部門治理實證（惟1111功能缺上線後採用率outcome數據且開發中案例不撐起Level 9，故評為Level 7）"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：clarify_first
- Level：7（±1）
- 一句話理由：具「推動系統改版至前後端分離的新架構」與 50 項功能交付實績，惟缺 KA/NRE 客製化專案交付管理證據，建議先釐清。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 系統服務逾 6 萬家活躍付費廠商（2026 Q3） | 過往為標準平台產品迭代，未呈現餐飲POS硬體與KA客戶NRE專案交付經驗 |
| role_evidence | 足夠 | 近 10 年 PM 經驗，經手 6 款產品 | 職責要求參與 KA 客戶與 NRE 專案交付管理（管理客戶期待與需求變更），履歷未呈現外部客戶合約與 NRE 專案控管證據 |
| decision_depth | 強 | 廠商反映的溝通中斷問題，使我優先推進信件與即時通整合 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 足夠 | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 1111新系統與群組功能未列上線後採用數據 |
| ownership | 強 | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 5年以上軟體產品、技術產品或技術專案管理經驗 | 必要 | supported | 近 10 年 PM 經驗；約 50 項大項功能上線 | 年資近10年且大型系統改版與交付經驗扎實 |
| R02 參與產品從需求規劃到上線交付的完整流程 | 必要 | supported | 涵蓋系統分析、流程與畫面設計、PRD、Prototype、UAT | 完整主導端到端產品開發與上線交付週期 |
| R03 能理解API、資料流程及系統串接邏輯 | 必要 | supported | API 串接規劃、舊系統資料盤點與新舊流程銜接 | 具系統分析、API串接與資料庫欄位結構理解 |
| R04 具備需求拆解、優先順序判斷、跨團隊溝通及風險管理 | 必要 | supported | 依使用者旅程與工單問題安排優先級；於 2026/04 完成登入驗證調整 | 具體展現工單痛點優先排序、重複信箱處理與資安風控 |
| R05 KA客戶/客製化或NRE專案交付管理；支付/餐飲/零售/SaaS經驗 | 必要 | partial | 針對大型客戶依部門或分店分工的需求，規劃群組功能 | 具大型客戶群組功能與支付經驗，惟未呈現KA客戶NRE客製化合約範疇與變更控管 |
| R06 基本SQL查詢或資料分析能力；高階利害關係人溝通 | 加分 | partial | 向總經理、副總等主管匯報；與 DBA 協作取數 | 具向總經理/副總匯報與試算表分析經驗，SQL與DBA協作取數 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | partial | 近 10 年 PM 經驗；約 50 項大項功能上線 | 對位 jd40 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 Product Owner，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 擬定資料表與欄位需求，與 DBA 協作取數 | 清楚界定個人規劃與DBA/工程/DS分工 |
| HR04 | partial | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 具處理週期與定價實驗數據，缺1111功能採用率 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現功能優先序與E-mail登入驗證取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端成長型產品演進至B2B大型平台主任 |
| HR07 | supported | 透過互動原型與 FAQ 向客服、業務說明功能 | Scrum、原型、FAQ教學、AI與英文協作皆有實例 |
| HR08 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 段落清楚，重點指標與背景脈絡易讀 |
| HR09 | supported | 產品上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 主動標註行銷導流期間表現與開發中狀態 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd40 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | partial | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 建議先釐清 jd40 關鍵條件再安排面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 針對大型客戶依部門或分店分工的需求，規劃群組功能 | 能針對大客戶部門/分店分工痛點設計群組權限 |
| HM03 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與E-mail登入取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數付費牆與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18% | 定價實驗與處理週期基準清晰，缺1111功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整 | 具新舊系統並行相容、重複信箱驗證與防冒用閉環 |
| HM08 | partial | 將業務規則轉為可與工程討論的條件描述 | 能將業務規則轉為工程條件，惟取數與DBA協作 |
| HM09 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程 | 依客服回饋修正登入操作流程與AI推薦規則 |
| HM12 | supported | 具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd40 明文條件獨立取證判讀 | 僅依 jd40 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd40 |
| 2 | 具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗 |
| 3 | 已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 職缺核心職責包含「KA 與 NRE 交付管理（管理客戶期待與需求變更）」，履歷雖有規劃大型客戶分店群組功能，但未呈現直接管理外部 KA 客戶客製化合約（NRE）之經驗 | 在 1111 規劃「大型客戶依部門或分店分工的群組功能」時，是否有直接面對大型企業客戶協商客製化範疇與交付時程的經驗？若面對餐飲連鎖 KA 客戶要求 NRE 客製開發，你如何控管需求變更？ |
| 2 | 1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據 | 你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？ |
| 3 | 資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節 | 在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd40 證明遺留系統重構與B2B組織權限設計力
- 尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd40 展現嚴謹對照實驗與商業變現能力
- 1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd40 展現資安危機閉環與10單位治理效率

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：職缺核心職責包含「KA 與 NRE 交付管理（管理客戶期待與需求變更）」，履歷雖有規劃大型客戶分店群組功能，但未呈現直接管理外部 KA 客戶客製化合約（NRE）之經驗
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落
- 位置：1111 全球華人經歷第 1、2、4、6 點
  - 原句：整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：risk（本機實測 `resume-v10.2-twocol.pdf` 粗體疊字已完全修復，惟仍有雙欄跨頁斷句與 Type3 康熙部首字元風險） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 Resume_v10.2_twocol（jd43 Product Manager (Messenger & OA)｜LINE Taiwan）｜第 13 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.2_twocol","job_id":"jd43","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd43-13","human_calibrated":false,"requirements":[{"id":"R01","text":"5年以上網路或科技產業PM經驗，推動概念到上線優化","type":"required","status":"supported","evidence":["近 10 年 PM 經驗；約 50 項大項功能上線"],"blocks_interview":false,"reason":"10年網路與軟體平台PM經驗，完整覆蓋0到1與迭代"},{"id":"R02","text":"聚焦帳號安全、防詐騙專案及訊息體驗","type":"required","status":"supported","evidence":["於 2026/04 完成登入驗證調整...優先推進信件與即時通整合"],"blocks_interview":false,"reason":"直接具備帳號防冒用登入驗證調整閉環與信件即時通整合規劃"},{"id":"R03","text":"跨職能（含資安、法務、客服）與跨國團隊合作經驗","type":"required","status":"partial","evidence":["與 CodaPay 新加坡技術團隊協調串接；法務與稽核協作"],"blocks_interview":false,"reason":"具法務稽核客服跨職能協作，惟跨國團隊協作集中於2016–2021年"},{"id":"R04","text":"運用問卷、訪談、A/B test與行為分析做出數據決策","type":"required","status":"supported","evidence":["使用者訪談與問卷、競品實測、GA4、世代分析與對照組實驗"],"blocks_interview":false,"reason":"研究與量化實驗方法論完整且有跨國定價實驗佐證"},{"id":"R05","text":"熟悉Confluence、Jira、Figma、Codex等工具；英文流利","type":"required","status":"partial","evidence":["英文 TOEIC 980；Figma、內部工單與看板系統；Claude Code"],"blocks_interview":false,"reason":"英文检定高分且熟Figma與Claude Code，未點名Jira/Confluence"},{"id":"R06","text":"具AI產品開發或整合經驗；日文或韓文能力尤佳","type":"preferred","status":"partial","evidence":["上線公司簡介生成、職缺工作說明生成及 AI 推薦人才"],"blocks_interview":false,"reason":"具3項AI功能上線實績；曾推日韓在地化但未列日韓文能力"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["系統服務逾 6 萬家活躍付費廠商（2026 Q3）"],"missing":["跨國團隊協作經驗停留於2016–2021年，近4年為本土B2B系統團隊"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"足夠","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"missing":["訊息體驗相關之「信件與即時通整合」尚在公司內部封測中（預計 2026/11 底上線）；未明列 Confluence、Jira"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["廠商反映的溝通中斷問題，使我優先推進信件與即時通整合"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"於 2026/04 完成登入驗證調整...至 2026/10 未再出現同類冒用","kinds":["output","outcome"]},{"quote":"兩案均在開發中，信件與即時通整合已進入公司內部封測","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"partial","resume_evidence":["近 10 年 PM 經驗；約 50 項大項功能上線"],"application_note":"對位 jd43 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 Product Owner，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["擬定資料表與欄位需求，與 DBA 協作取數"],"application_note":"清楚界定個人規劃與DBA/工程/DS分工"},{"rule_id":"HR04","status":"partial","resume_evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"application_note":"具處理週期與定價實驗數據，缺1111功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與E-mail登入驗證取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端成長型產品演進至B2B大型平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["透過互動原型與 FAQ 向客服、業務說明功能"],"application_note":"Scrum、原型、FAQ教學、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"application_note":"段落清楚，重點指標與背景脈絡易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["產品上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"主動標註行銷導流期間表現與開發中狀態"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd43 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"partial","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"application_note":"建議先釐清 jd43 關鍵條件再安排面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["針對大型客戶依部門或分店分工的需求，規劃群組功能"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線的新版第一階段、群組功能與 AI 推薦人才，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["將業務規則轉為可與工程討論的條件描述"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"請以英文分享「信件與即時通整合」在內部封測階段收集到的回饋與預計追蹤的指標；另外在 2026/04 處理廠商帳號遭冒用並調整登入驗證時，如何平衡安全性與正常廠商的操作順暢度？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd43 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定條件或技術工具細節待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"訊息體驗核心案例「信件與即時通整合」目前處於公司內部封測階段（預計 2026/11 底上線），尚無上線後數據；且跨國團隊協作停留於 2016–2021 年，未明列 Confluence、Jira","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"1111上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 全球華人經歷第 1、2、4、6 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線","reason":"1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證"}],"decision":{"recommendation":"clarify_first","evidence":["近 10 年 PM 經驗；約 50 項大項功能上線","約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"blocking_unknowns":["訊息體驗核心案例「信件與即時通整合」目前處於公司內部封測階段（預計 2026/11 底上線），尚無上線後數據；且跨國團隊協作停留於 2016–2021 年，未明列 Confluence、Jira"]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd43","具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗","已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環"],"key_gaps":["訊息體驗核心案例「信件與即時通整合」目前處於公司內部封測階段（預計 2026/11 底上線），尚無上線後數據；且跨國團隊協作停留於 2016–2021 年，未明列 Confluence、Jira","1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據","資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節"],"strengths":["1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd43 證明遺留系統重構與B2B組織權限設計力","尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd43 展現嚴謹對照實驗與商業變現能力","1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd43 展現資安危機閉環與10單位治理效率"],"interview_questions":["請以英文分享「信件與即時通整合」在內部封測階段收集到的回饋與預計追蹤的指標；另外在 2026/04 處理廠商帳號遭冒用並調整登入驗證時，如何平衡安全性與正常廠商的操作順暢度？","你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？","在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":7,"uncertainty_levels":1,"basis":"針對 jd43 具備多個已實現案例、清楚取捨與跨部門治理實證（惟1111功能缺上線後採用率outcome數據且開發中案例不撐起Level 9，故評為Level 7）"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：clarify_first
- Level：7（±1）
- 一句話理由：具「2026/04 完成登入驗證調整」與「信件與即時通整合（內部封測中）」經驗，惟跨國協作集中於早期且工具未列 Confluence/Jira，建議先釐清。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 系統服務逾 6 萬家活躍付費廠商（2026 Q3） | 跨國團隊協作經驗停留於2016–2021年，近4年為本土B2B系統團隊 |
| role_evidence | 足夠 | 近 10 年 PM 經驗，經手 6 款產品 | 訊息體驗相關之「信件與即時通整合」尚在公司內部封測中（預計 2026/11 底上線）；未明列 Confluence、Jira |
| decision_depth | 強 | 廠商反映的溝通中斷問題，使我優先推進信件與即時通整合 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 5年以上網路或科技產業PM經驗，推動概念到上線優化 | 必要 | supported | 近 10 年 PM 經驗；約 50 項大項功能上線 | 10年網路與軟體平台PM經驗，完整覆蓋0到1與迭代 |
| R02 聚焦帳號安全、防詐騙專案及訊息體驗 | 必要 | supported | 於 2026/04 完成登入驗證調整...優先推進信件與即時通整合 | 直接具備帳號防冒用登入驗證調整閉環與信件即時通整合規劃 |
| R03 跨職能（含資安、法務、客服）與跨國團隊合作經驗 | 必要 | partial | 與 CodaPay 新加坡技術團隊協調串接；法務與稽核協作 | 具法務稽核客服跨職能協作，惟跨國團隊協作集中於2016–2021年 |
| R04 運用問卷、訪談、A/B test與行為分析做出數據決策 | 必要 | supported | 使用者訪談與問卷、競品實測、GA4、世代分析與對照組實驗 | 研究與量化實驗方法論完整且有跨國定價實驗佐證 |
| R05 熟悉Confluence、Jira、Figma、Codex等工具；英文流利 | 必要 | partial | 英文 TOEIC 980；Figma、內部工單與看板系統；Claude Code | 英文检定高分且熟Figma與Claude Code，未點名Jira/Confluence |
| R06 具AI產品開發或整合經驗；日文或韓文能力尤佳 | 加分 | partial | 上線公司簡介生成、職缺工作說明生成及 AI 推薦人才 | 具3項AI功能上線實績；曾推日韓在地化但未列日韓文能力 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | partial | 近 10 年 PM 經驗；約 50 項大項功能上線 | 對位 jd43 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 Product Owner，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 擬定資料表與欄位需求，與 DBA 協作取數 | 清楚界定個人規劃與DBA/工程/DS分工 |
| HR04 | partial | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 具處理週期與定價實驗數據，缺1111功能採用率 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現功能優先序與E-mail登入驗證取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端成長型產品演進至B2B大型平台主任 |
| HR07 | supported | 透過互動原型與 FAQ 向客服、業務說明功能 | Scrum、原型、FAQ教學、AI與英文協作皆有實例 |
| HR08 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 段落清楚，重點指標與背景脈絡易讀 |
| HR09 | supported | 產品上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 主動標註行銷導流期間表現與開發中狀態 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd43 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | partial | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 建議先釐清 jd43 關鍵條件再安排面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 針對大型客戶依部門或分店分工的需求，規劃群組功能 | 能針對大客戶部門/分店分工痛點設計群組權限 |
| HM03 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與E-mail登入取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數付費牆與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18% | 定價實驗與處理週期基準清晰，缺1111功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整 | 具新舊系統並行相容、重複信箱驗證與防冒用閉環 |
| HM08 | supported | 將業務規則轉為可與工程討論的條件描述 | 能將業務規則轉為工程條件，惟取數與DBA協作 |
| HM09 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程 | 依客服回饋修正登入操作流程與AI推薦規則 |
| HM12 | supported | 具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd43 明文條件獨立取證判讀 | 僅依 jd43 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd43 |
| 2 | 具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗 |
| 3 | 已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 訊息體驗核心案例「信件與即時通整合」目前處於公司內部封測階段（預計 2026/11 底上線），尚無上線後數據；且跨國團隊協作停留於 2016–2021 年，未明列 Confluence、Jira | 請以英文分享「信件與即時通整合」在內部封測階段收集到的回饋與預計追蹤的指標；另外在 2026/04 處理廠商帳號遭冒用並調整登入驗證時，如何平衡安全性與正常廠商的操作順暢度？ |
| 2 | 1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據 | 你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？ |
| 3 | 資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節 | 在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd43 證明遺留系統重構與B2B組織權限設計力
- 尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd43 展現嚴謹對照實驗與商業變現能力
- 1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd43 展現資安危機閉環與10單位治理效率

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：訊息體驗核心案例「信件與即時通整合」目前處於公司內部封測階段（預計 2026/11 底上線），尚無上線後數據；且跨國團隊協作停留於 2016–2021 年，未明列 Confluence、Jira
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落
- 位置：1111 全球華人經歷第 1、2、4、6 點
  - 原句：整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：risk（本機實測 `resume-v10.2-twocol.pdf` 粗體疊字已完全修復，惟仍有雙欄跨頁斷句與 Type3 康熙部首字元風險） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 Resume_v10.2_twocol（jd44 [Music] Senior Product Planner｜KKBOX (KKCompany)）｜第 14 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.2_twocol","job_id":"jd44","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd44-14","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上網路PM經驗，具策略思考與0到1及持續迭代能力","type":"required","status":"supported","evidence":["規劃 KOOL 網紅媒合平台；約 50 項大項功能上線"],"blocks_interview":false,"reason":"兼具KOOL從0到1商業模式設計與1111大型平台持續迭代"},{"id":"R02","text":"跨國跨職能協作，與外部廠商溝通共創產品概念","type":"required","status":"supported","evidence":["推進 SweetRing 7 市場在地化；與 CodaPay 協調串接"],"blocks_interview":false,"reason":"具跨7國市場在地化與跨國技術夥伴協作經驗"},{"id":"R03","text":"數據驅動決策，熟悉行為分析、A/B測試及關鍵指標","type":"required","status":"supported","evidence":["設計馬來西亞 iOS 定價實驗，以售價不變的 Android 作對照"],"blocks_interview":false,"reason":"具嚴謹跨國定價實驗、GA4與世代分析經驗"},{"id":"R04","text":"市場與競品分析能力；提升參與度與留存率","type":"required","status":"supported","evidence":["無直接競品可對照下，參考 Airbnb 與交友平台的媒合方式"],"blocks_interview":false,"reason":"具體展現跨領域競品參考、競品實測與訂閱留存優化"},{"id":"R05","text":"優異的英文溝通及寫作能力","type":"required","status":"supported","evidence":["英文 TOEIC 980、TOEFL iBT 93，以英文進行跨國協作"],"blocks_interview":false,"reason":"高分英檢、美國交換且具英文跨國協作實務"},{"id":"R06","text":"具音樂/內容/社群/娛樂或AI相關產品經驗；日文能力","type":"preferred","status":"supported","evidence":["經手交友、訂閱制內容 App 與網紅媒合平台；上線 AI 推薦"],"blocks_interview":false,"reason":"具訂閱制內容/社交媒合App與3項AI功能上線經驗，日文未呈現"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["系統服務逾 6 萬家活躍付費廠商（2026 Q3）"],"missing":["過往訂閱制為社交與網紅媒合 App，未直接經手音樂串流與版權曲庫領域；未呈現日文能力"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"足夠","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"missing":["KOOL 0 到 1 平台與 1111 AI 推薦功能在 v10.2 中未列出上線後的用戶規模或留存提升數字"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["廠商反映的溝通中斷問題，使我優先推進信件與即時通整合"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"於 2026/04 完成登入驗證調整...至 2026/10 未再出現同類冒用","kinds":["output","outcome"]},{"quote":"兩案均在開發中，信件與即時通整合已進入公司內部封測","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；約 50 項大項功能上線"],"application_note":"對位 jd44 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 Product Owner，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["擬定資料表與欄位需求，與 DBA 協作取數"],"application_note":"清楚界定個人規劃與DBA/工程/DS分工"},{"rule_id":"HR04","status":"partial","resume_evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"application_note":"具處理週期與定價實驗數據，缺1111功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與E-mail登入驗證取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端成長型產品演進至B2B大型平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["透過互動原型與 FAQ 向客服、業務說明功能"],"application_note":"Scrum、原型、FAQ教學、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"application_note":"段落清楚，重點指標與背景脈絡易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["產品上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"主動標註行銷導流期間表現與開發中狀態"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd44 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"application_note":"證據鏈完整支持安排 jd44 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["針對大型客戶依部門或分店分工的需求，規劃群組功能"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線的新版第一階段、群組功能與 AI 推薦人才，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["將業務規則轉為可與工程討論的條件描述"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"你在規劃 KOOL 網紅媒合平台（參考 Airbnb 與交友平台設計刊案、報名、邀約與 VIP/點數機制）上線後的實際媒合規模與付費表現如何？如何應用於音樂串流的藝人粉絲互動與 AI 個人化？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd44 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定條件或技術工具細節待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"KOOL 網紅媒合平台與 1111 AI 功能未在履歷中列出上線後的用戶參與度或留存數據；且過往訂閱制經驗集中於 2018–2022 年社交媒合領域","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"1111上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 全球華人經歷第 1、2、4、6 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線","reason":"1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["規劃 KOOL 網紅媒合平台；約 50 項大項功能上線","約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd44","具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗","已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環"],"key_gaps":["KOOL 網紅媒合平台與 1111 AI 功能未在履歷中列出上線後的用戶參與度或留存數據；且過往訂閱制經驗集中於 2018–2022 年社交媒合領域","1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據","資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節"],"strengths":["1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd44 證明遺留系統重構與B2B組織權限設計力","尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd44 展現嚴謹對照實驗與商業變現能力","1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd44 展現資安危機閉環與10單位治理效率"],"interview_questions":["你在規劃 KOOL 網紅媒合平台（參考 Airbnb 與交友平台設計刊案、報名、邀約與 VIP/點數機制）上線後的實際媒合規模與付費表現如何？如何應用於音樂串流的藝人粉絲互動與 AI 個人化？","你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？","在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":7,"uncertainty_levels":1,"basis":"針對 jd44 具備多個已實現案例、清楚取捨與跨部門治理實證（惟1111功能缺上線後採用率outcome數據且開發中案例不撐起Level 9，故評為Level 7）"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：7（±1）
- 一句話理由：具「規劃 KOOL 網紅媒合平台」0 到 1 經驗、馬來西亞定價實驗與 3 項 AI 功能上線實績，支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 系統服務逾 6 萬家活躍付費廠商（2026 Q3） | 過往訂閱制為社交與網紅媒合 App，未直接經手音樂串流與版權曲庫領域；未呈現日文能力 |
| role_evidence | 足夠 | 近 10 年 PM 經驗，經手 6 款產品 | KOOL 0 到 1 平台與 1111 AI 推薦功能在 v10.2 中未列出上線後的用戶規模或留存提升數字 |
| decision_depth | 強 | 廠商反映的溝通中斷問題，使我優先推進信件與即時通整合 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 3年以上網路PM經驗，具策略思考與0到1及持續迭代能力 | 必要 | supported | 規劃 KOOL 網紅媒合平台；約 50 項大項功能上線 | 兼具KOOL從0到1商業模式設計與1111大型平台持續迭代 |
| R02 跨國跨職能協作，與外部廠商溝通共創產品概念 | 必要 | supported | 推進 SweetRing 7 市場在地化；與 CodaPay 協調串接 | 具跨7國市場在地化與跨國技術夥伴協作經驗 |
| R03 數據驅動決策，熟悉行為分析、A/B測試及關鍵指標 | 必要 | supported | 設計馬來西亞 iOS 定價實驗，以售價不變的 Android 作對照 | 具嚴謹跨國定價實驗、GA4與世代分析經驗 |
| R04 市場與競品分析能力；提升參與度與留存率 | 必要 | supported | 無直接競品可對照下，參考 Airbnb 與交友平台的媒合方式 | 具體展現跨領域競品參考、競品實測與訂閱留存優化 |
| R05 優異的英文溝通及寫作能力 | 必要 | supported | 英文 TOEIC 980、TOEFL iBT 93，以英文進行跨國協作 | 高分英檢、美國交換且具英文跨國協作實務 |
| R06 具音樂/內容/社群/娛樂或AI相關產品經驗；日文能力 | 加分 | supported | 經手交友、訂閱制內容 App 與網紅媒合平台；上線 AI 推薦 | 具訂閱制內容/社交媒合App與3項AI功能上線經驗，日文未呈現 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 規劃 KOOL 網紅媒合平台；約 50 項大項功能上線 | 對位 jd44 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 Product Owner，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 擬定資料表與欄位需求，與 DBA 協作取數 | 清楚界定個人規劃與DBA/工程/DS分工 |
| HR04 | partial | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 具處理週期與定價實驗數據，缺1111功能採用率 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現功能優先序與E-mail登入驗證取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端成長型產品演進至B2B大型平台主任 |
| HR07 | supported | 透過互動原型與 FAQ 向客服、業務說明功能 | Scrum、原型、FAQ教學、AI與英文協作皆有實例 |
| HR08 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 段落清楚，重點指標與背景脈絡易讀 |
| HR09 | supported | 產品上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 主動標註行銷導流期間表現與開發中狀態 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd44 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 證據鏈完整支持安排 jd44 面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 針對大型客戶依部門或分店分工的需求，規劃群組功能 | 能針對大客戶部門/分店分工痛點設計群組權限 |
| HM03 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與E-mail登入取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數付費牆與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18% | 定價實驗與處理週期基準清晰，缺1111功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整 | 具新舊系統並行相容、重複信箱驗證與防冒用閉環 |
| HM08 | supported | 將業務規則轉為可與工程討論的條件描述 | 能將業務規則轉為工程條件，惟取數與DBA協作 |
| HM09 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程 | 依客服回饋修正登入操作流程與AI推薦規則 |
| HM12 | supported | 具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd44 明文條件獨立取證判讀 | 僅依 jd44 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd44 |
| 2 | 具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗 |
| 3 | 已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | KOOL 網紅媒合平台與 1111 AI 功能未在履歷中列出上線後的用戶參與度或留存數據；且過往訂閱制經驗集中於 2018–2022 年社交媒合領域 | 你在規劃 KOOL 網紅媒合平台（參考 Airbnb 與交友平台設計刊案、報名、邀約與 VIP/點數機制）上線後的實際媒合規模與付費表現如何？如何應用於音樂串流的藝人粉絲互動與 AI 個人化？ |
| 2 | 1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據 | 你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？ |
| 3 | 資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節 | 在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd44 證明遺留系統重構與B2B組織權限設計力
- 尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd44 展現嚴謹對照實驗與商業變現能力
- 1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd44 展現資安危機閉環與10單位治理效率

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：KOOL 網紅媒合平台與 1111 AI 功能未在履歷中列出上線後的用戶參與度或留存數據；且過往訂閱制經驗集中於 2018–2022 年社交媒合領域
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落
- 位置：1111 全球華人經歷第 1、2、4、6 點
  - 原句：整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：risk（本機實測 `resume-v10.2-twocol.pdf` 粗體疊字已完全修復，惟仍有雙欄跨頁斷句與 Type3 康熙部首字元風險） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 Resume_v10.2_twocol（jd47 產品經理｜Product Manager｜USPACE）｜第 15 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.2_twocol","job_id":"jd47","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd47-15","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上Software PM，具0到1探索驗證上線與成熟產品迭代經歷","type":"required","status":"supported","evidence":["規劃 KOOL 網紅媒合平台；約 50 項大項功能上線"],"blocks_interview":false,"reason":"同時具備KOOL 0到1完整週期與1111成熟產品50項大功能迭代"},{"id":"R02","text":"能寫清楚的規格文件（PRD、流程圖、資料結構）","type":"required","status":"supported","evidence":["流程圖／循序圖、PRD；擬定資料表與欄位需求"],"blocks_interview":false,"reason":"具PRD、循序圖、資料欄位對照與擬定資料表及欄位能力"},{"id":"R03","text":"理解API、JSON與基本SQL","type":"required","status":"partial","evidence":["API 串接規劃；擬定資料表與欄位需求，與 DBA 協作取數"],"blocks_interview":false,"reason":"具API與資料表欄位規劃，未明列JSON與自寫SQL"},{"id":"R04","text":"規劃並執行產品教育訓練，負責上線前測試與驗收","type":"required","status":"supported","evidence":["透過互動原型與 FAQ 向客服、業務說明功能"],"blocks_interview":false,"reason":"直接具備UAT制定、上線計畫與透過互動原型/FAQ向客服業務教育訓練實績"},{"id":"R05","text":"支付或FinTech經驗；AI/LLM工具規格撰寫與分析","type":"preferred","status":"supported","evidence":["以 Claude Code 建立協作流程與共用 skill"],"blocks_interview":false,"reason":"具CodaPay/網頁金流與Claude Code規格分析深度實作"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["系統服務逾 6 萬家活躍付費廠商（2026 Q3）"],"missing":["過往為純軟體平台與App，尚未接觸智慧停車或實體場域硬體整合"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"強","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"missing":["必備條件中之 JSON 未明文呈現，且資料庫查詢為與 DBA 協作取數而非自寫 SQL"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["廠商反映的溝通中斷問題，使我優先推進信件與即時通整合"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"於 2026/04 完成登入驗證調整...至 2026/10 未再出現同類冒用","kinds":["output","outcome"]},{"quote":"兩案均在開發中，信件與即時通整合已進入公司內部封測","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；約 50 項大項功能上線"],"application_note":"對位 jd47 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 Product Owner，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["擬定資料表與欄位需求，與 DBA 協作取數"],"application_note":"清楚界定個人規劃與DBA/工程/DS分工"},{"rule_id":"HR04","status":"partial","resume_evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"application_note":"具處理週期與定價實驗數據，缺1111功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與E-mail登入驗證取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端成長型產品演進至B2B大型平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["透過互動原型與 FAQ 向客服、業務說明功能"],"application_note":"Scrum、原型、FAQ教學、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"application_note":"段落清楚，重點指標與背景脈絡易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["產品上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"主動標註行銷導流期間表現與開發中狀態"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd47 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"application_note":"證據鏈完整支持安排 jd47 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["針對大型客戶依部門或分店分工的需求，規劃群組功能"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線的新版第一階段、群組功能與 AI 推薦人才，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"partial","resume_evidence":["將業務規則轉為可與工程討論的條件描述"],"evidence_type":"output","source_ids":[],"interview_question":"請說明如何將業務規則轉為工程條件描述，以及是否具基礎 SQL/JSON 實作經驗？"},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["結構分明，時序、實驗對照基準與新舊並行脈絡清晰"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"在推動 KOOL 0 到 1 上線與 1111 招募系統改版時，你如何「透過互動原型與 FAQ 向客服、業務說明功能」並收集回饋？另外能否說明 API JSON 格式與基礎 SQL 查詢經驗？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd47 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定條件或技術工具細節待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"必備條件要求「理解 API、JSON 與基本 SQL」，履歷雖載明 API 串接規劃與擬定資料表欄位與 DBA 協作取數，但未明文呈現 JSON 與自行撰寫 SQL","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"1111上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 全球華人經歷第 1、2、4、6 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線","reason":"1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["規劃 KOOL 網紅媒合平台；約 50 項大項功能上線","約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd47","具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗","已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環"],"key_gaps":["必備條件要求「理解 API、JSON 與基本 SQL」，履歷雖載明 API 串接規劃與擬定資料表欄位與 DBA 協作取數，但未明文呈現 JSON 與自行撰寫 SQL","1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據","資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節"],"strengths":["1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd47 證明遺留系統重構與B2B組織權限設計力","尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd47 展現嚴謹對照實驗與商業變現能力","1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd47 展現資安危機閉環與10單位治理效率"],"interview_questions":["在推動 KOOL 0 到 1 上線與 1111 招募系統改版時，你如何「透過互動原型與 FAQ 向客服、業務說明功能」並收集回饋？另外能否說明 API JSON 格式與基礎 SQL 查詢經驗？","你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？","在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd47 具備多個已實現案例、清楚取捨與跨部門治理實證（惟1111功能缺上線後採用率outcome數據且開發中案例不撐起Level 9，故評為Level 8）"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：兼具「規劃 KOOL 網紅媒合平台」0 到 1 與「約 50 項大項功能上線」及互動原型/FAQ 教育訓練實績，支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 系統服務逾 6 萬家活躍付費廠商（2026 Q3） | 過往為純軟體平台與App，尚未接觸智慧停車或實體場域硬體整合 |
| role_evidence | 強 | 近 10 年 PM 經驗，經手 6 款產品 | 必備條件中之 JSON 未明文呈現，且資料庫查詢為與 DBA 協作取數而非自寫 SQL |
| decision_depth | 強 | 廠商反映的溝通中斷問題，使我優先推進信件與即時通整合 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 3年以上Software PM，具0到1探索驗證上線與成熟產品迭代經歷 | 必要 | supported | 規劃 KOOL 網紅媒合平台；約 50 項大項功能上線 | 同時具備KOOL 0到1完整週期與1111成熟產品50項大功能迭代 |
| R02 能寫清楚的規格文件（PRD、流程圖、資料結構） | 必要 | supported | 流程圖／循序圖、PRD；擬定資料表與欄位需求 | 具PRD、循序圖、資料欄位對照與擬定資料表及欄位能力 |
| R03 理解API、JSON與基本SQL | 必要 | partial | API 串接規劃；擬定資料表與欄位需求，與 DBA 協作取數 | 具API與資料表欄位規劃，未明列JSON與自寫SQL |
| R04 規劃並執行產品教育訓練，負責上線前測試與驗收 | 必要 | supported | 透過互動原型與 FAQ 向客服、業務說明功能 | 直接具備UAT制定、上線計畫與透過互動原型/FAQ向客服業務教育訓練實績 |
| R05 支付或FinTech經驗；AI/LLM工具規格撰寫與分析 | 加分 | supported | 以 Claude Code 建立協作流程與共用 skill | 具CodaPay/網頁金流與Claude Code規格分析深度實作 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 規劃 KOOL 網紅媒合平台；約 50 項大項功能上線 | 對位 jd47 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 Product Owner，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 擬定資料表與欄位需求，與 DBA 協作取數 | 清楚界定個人規劃與DBA/工程/DS分工 |
| HR04 | partial | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 具處理週期與定價實驗數據，缺1111功能採用率 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現功能優先序與E-mail登入驗證取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端成長型產品演進至B2B大型平台主任 |
| HR07 | supported | 透過互動原型與 FAQ 向客服、業務說明功能 | Scrum、原型、FAQ教學、AI與英文協作皆有實例 |
| HR08 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 段落清楚，重點指標與背景脈絡易讀 |
| HR09 | supported | 產品上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 主動標註行銷導流期間表現與開發中狀態 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd47 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 證據鏈完整支持安排 jd47 面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 針對大型客戶依部門或分店分工的需求，規劃群組功能 | 能針對大客戶部門/分店分工痛點設計群組權限 |
| HM03 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與E-mail登入取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數付費牆與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較基準期增 5%，同期 Android 減 18% | 定價實驗與處理週期基準清晰，缺1111功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 處理新舊系統並行的相容性需求；於 2026/04 完成登入驗證調整 | 具新舊系統並行相容、重複信箱驗證與防冒用閉環 |
| HM08 | partial | 將業務規則轉為可與工程討論的條件描述 | 能將業務規則轉為工程條件，惟取數與DBA協作 |
| HM09 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 結構分明，時序、實驗對照基準與新舊並行脈絡清晰 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 完成登入驗證調整，並依客服回饋修正操作流程 | 依客服回饋修正登入操作流程與AI推薦規則 |
| HM12 | supported | 具KOOL 0到1、1111改版與群組權限、定價實驗與AI案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd47 明文條件獨立取證判讀 | 僅依 jd47 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 現任1111招募系統PO（服務逾6萬廠商、主責50項大功能上線、處理時間由100.4天降至30.9天），具備前後端分離改版與大客戶群組權限實績，契合 jd47 |
| 2 | 具備KOOL網紅媒合平台0到1規劃、馬來西亞iOS三階段定價實驗（相對營收多28%）、Peach內購轉網頁付款（24%→80%+）與CodaPay跨國金流串接經驗 |
| 3 | 已上線3項AI功能並以Claude Code建立協作流程與共用skill（將業務規則轉為工程討論條件），且具2026/04廠商帳號遭冒用之登入驗證調整閉環 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 必備條件要求「理解 API、JSON 與基本 SQL」，履歷雖載明 API 串接規劃與擬定資料表欄位與 DBA 協作取數，但未明文呈現 JSON 與自行撰寫 SQL | 在推動 KOOL 0 到 1 上線與 1111 招募系統改版時，你如何「透過互動原型與 FAQ 向客服、業務說明功能」並收集回饋？另外能否說明 API JSON 格式與基礎 SQL 查詢經驗？ |
| 2 | 1111 企業端上線功能（第一階段改版、大型客戶群組功能、3 項 AI 生成與推薦功能）未呈現上線後的實際客戶採用率或業務轉換成效數據 | 你在 1111 推動的「求才系統第一階段改版」、「大型客戶群組功能」與「AI 職缺生成／推薦人才」上線後，如何衡量成功？實際採用率數據表現如何？ |
| 3 | 資料庫查詢採「擬定資料表與欄位需求，與 DBA 協作取數」，未明載獨立手寫 SQL 與 JSON 規格細節 | 在 1111 擬定資料表與欄位需求與 DBA 協作取數時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 查詢驗證？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜重新制定業務流程、對照資料欄位並重構規格；規劃群組功能於 2025/09 完成上線｜對 jd47 證明遺留系統重構與B2B組織權限設計力
- 尚凡經歷｜設計馬來西亞 iOS 定價實驗...相對變化約多 28%；網頁付款占營收由 24% 升至 80% 以上｜對 jd47 展現嚴謹對照實驗與商業變現能力
- 1111經歷｜於 2026/04 完成登入驗證調整...未再出現同類冒用；平均處理時間由 100.4 天降至 30.9 天｜對 jd47 展現資安危機閉環與10單位治理效率

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：必備條件要求「理解 API、JSON 與基本 SQL」，履歷雖載明 API 串接規劃與擬定資料表欄位與 DBA 協作取數，但未明文呈現 JSON 與自行撰寫 SQL
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、定義 API JSON 欄位或直接訪談企業客戶之實例，建議直接補入對應段落
- 位置：1111 全球華人經歷第 1、2、4、6 點
  - 原句：整理帳號權限、職缺關聯與資料轉換規則，於 2025/09 上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之新版第一階段、群組功能與 AI 推薦人才僅列交付完成（output），未呈現客戶採用率或業務成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、新版切換率或 AI 推薦成效指標；開發中兩案則準備內部封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）、API JSON 欄位定義或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：強

### 8. 未測試聲明
PDF 抽字：risk（本機實測 `resume-v10.2-twocol.pdf` 粗體疊字已完全修復，惟仍有雙欄跨頁斷句與 Type3 康熙部首字元風險） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 附錄 B：執行檢查清單核對（對應套件 §10）
- [x] 單份審查 15 次，每次只放一份職缺條件獨立判讀，已記錄 `model_id: gemini-4-argon`（並於 §7 誠實揭露單一環境執行限制）
- [x] JSON 單行、欄位齊全、`human_calibrated=false`、`ai_authorship.probability=null`
- [x] 沒有做任何版本比較，也沒有引用其他對話的分數（100% 依據 `resume-v10.2-twocol.pdf` 實際內容重新取證）
- [x] 沒有把頁數、學歷、空窗、任職長短、關鍵字個數當缺失
- [x] 沒有拿 A 職缺的條件去扣 B 職缺；嚴格遵守硬性規則 2（進行中未上線或未附成果數字的案例不撐起 Level 9）
- [x] HR 12 題＋HM 13 題每次都列全；約談理由 ≤3、關鍵缺口 ≤3
- [x] ATS 五塊分開，沒有「ATS 分數」，並如實反映 `resume-v10.2-twocol.pdf` 粗體疊字已修復及剩餘跨頁斷句風險
- [x] 總報告依 §8 固定格式，附上 15 份原始 JSON 與完整單份審查評語（附錄 A）
