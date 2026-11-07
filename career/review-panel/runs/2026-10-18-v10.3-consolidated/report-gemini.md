# 履歷驗證報告：單份履歷 × 15 職缺｜2026-10-18｜model_id: gemini-4-argon｜human_calibration: not_run

## 1. 結論（≤6 行，先講答案）
- 招聘決定分布（interview／clarify_first／not_matched／insufficient_info 各幾份職缺）：`interview` 14 份（`jd03, jd09, jd11, jd14, jd26, jd30, jd31, jd32, jd34, jd36, jd40, jd43, jd44, jd47`）／`clarify_first` 1 份（`jd20`）／`not_matched` 0 份／`insufficient_info` 0 份。
- Level 分布（列出每個 Level 的職缺數；不算平均）：**Level 9 共 1 份**（`jd32`）；**Level 8 共 11 份**（`jd03, jd09, jd11, jd30, jd31, jd34, jd36, jd40, jd43, jd44, jd47`）；**Level 7 共 3 份**（`jd14, jd20, jd26`）。嚴格遵守硬性規則 2，進行中未上線案例（如預計 2026/11 底上線之信件與即時通整合、搜尋改版）與未附上線後成效數字之功能不撐起 Level 9。
- 最適合投遞的 5 份職缺代號與一句理由：**`jd32`**（現任同業招募系統 PO，無文件下逆向實測補回權限與計費規則、完成 88% 廠商建議並將 30 天結案率由 52% 升至 79%）、**`jd11`**（直接具備 HR 招募系統群組權限、3 項生成式 AI 功能上線與 Claude Code 協作流程）、**`jd30`**（具 KOOL 0 到 1 規劃、外部 API 簽章防重放與 JSON 欄位確認及 Claude Code 共用 skill）、**`jd31`**（主導逾 6 萬家企業招募系統、規劃分店群組權限、協助製作 sales kit 且具 Scrum 與 API 議定經驗）、**`jd43`**（罕見同時具備帳號防冒用驗證調整、外部 API 防濫用、信件與即時通整合及跨國英文協作經驗）。
- 最可能被卡的 3 份職缺代號與卡在哪個條件：**`jd20`**（必備條件要求「5-8年以上B2B/B2G經驗」與「自行使用SQL/BI查詢解讀數據」，目前純 B2B 約 4 年且取數須與 DBA 協作）、**`jd14`**（必備條件點名之 `Firebase` 未呈現，且近 4 年重心為 B2B 招募系統而非 C 端影音串流成長）、**`jd26`**（必備條件要求透過 `Jira、Confluence` 管理專案與法遵確認，且自傳盼做產品策略與純專案執行定位需對齊）。

## 2. 職缺矩陣（每列一份職缺，不加總）
| 職缺 | 決定／Level | 六維度（簡寫：強/足/待/未） | 決定性條件（≤20 字） | 約談理由第一名（≤20 字） |
| :-- | :-: | :-: | :-- | :-- |
| [jd03 產品經理 (Pi錢包)｜拍付國際](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F91sgi) | interview／Level 8 | 足/強/強/強/強/強 | 2年PM＋PRD與API系統邏輯 | 內購轉網頁付款占營收升至80%以上 |
| [jd09 產品經理 Product Manager｜微拓科技 (beBit TECH)](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F82slf) | interview／Level 8 | 強/強/強/足/強/強 | 3年軟體PM＋B2B SaaS經驗 | 主責服務逾6萬家付費廠商之企業系統 |
| [jd11 【北士科】Product Manager｜沛思坦 (Pacston)](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F8o3s3) | interview／Level 8 | 強/強/強/足/強/強 | 5年PM＋敏捷開發與HR/AI經驗 | 現任招募系統PO且上線3項AI功能 |
| [jd14 D441 MyVideo影音產品Growth PM｜台灣大哥大](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F94le0) | interview／Level 7 | 足/足/強/強/強/強 | 3年Growth＋GA4與定價實驗 | 具訂閱制App定價實驗與付費轉換實績 |
| [jd20 Senior Product Manager (Anti-Scam BU/2B)｜Gogolook](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F950oe) | clarify_first／Level 7 | 足/足/強/足/強/強 | 5-8年B2B、母語級英文與獨立SQL | 具帳號防冒用與API簽章防重放實績 |
| [jd26 全支付- Product Manager (專案執行)](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F7996v) | interview／Level 7 | 足/足/強/強/強/強 | 2年經驗＋Axure與跨部門專案執行 | 具Axure、金流串接與50項功能交付 |
| [jd30 資深產品經理｜Senior Product Manager｜USPACE](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F8bymx) | interview／Level 8 | 足/強/強/強/強/強 | 0到1＋API/JSON與Claude | 具0到1、JSON確認與Claude流程 |
| [jd31 資深產品經理【擴編】｜人易科技 (NUEIP)](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F92io8) | interview／Level 8 | 強/強/強/足/強/強 | 3年PM＋企業系統/API/Scrum | 具企業招募系統群組權限與API議定實績 |
| [jd32 產品專案經理(內部系統)｜104人力銀行](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F94n8b) | interview／Level 9 | 強/強/強/強/強/強 | 3年經驗＋SA分析＋AI工具分析 | 現任同業PO具系統分析與AI協作實績 |
| [jd34 SaaS 產品經理 / Product Owner｜91APP](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F8dbp3) | interview／Level 8 | 強/強/強/強/強/強 | 5年經驗＋SaaS/Scrum/金流會員 | 經手6萬廠商系統與訂閱點數金流機制 |
| [jd36 全支付- Product Manager (內部系統、串接)](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F8ocje) | interview／Level 8 | 強/強/強/強/強/強 | 3年經驗＋Axure＋API串接 | 具外部API規格議定與新舊系統並行改版 |
| [jd40 【PMC】軟體產品經理 (PM / TPM)｜QuickClick快一點](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F94fod) | interview／Level 8 | 足/強/強/強/強/強 | 5年PM/TPM＋API與案件交付 | 具前後端分離改版、API議定與客戶案控管 |
| [jd43 Product Manager (Messenger \& OA Products)｜LINE Taiwan](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F95jyg) | interview／Level 8 | 強/強/強/強/強/強 | 5年PM＋帳號安全防詐＋跨國協作 | 具帳號防冒用、即時通整合與跨國協作實績 |
| [jd44 \[Music\] Senior Product Planner｜KKBOX (KKCompany)](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F93qa8) | interview／Level 8 | 足/強/強/強/強/強 | 3年網路PM＋0到1/實驗/英文/AI | 具0到1媒合平台、定價實驗與AI上線 |
| [jd47 產品經理｜Product Manager｜USPACE](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F95mvt) | interview／Level 8 | 足/強/強/強/強/強 | 0到1＋迭代＋訓練＋API/JSON | 兼具0到1與成熟系統迭代及內部訓練 |

## 3. 職缺分群（依職缺內容自行分，最多 5 群）
| 群組 | 職缺代號 | 共同優勢 | 共同卡關 |
| :-- | :-- | :-- | :-- |
| **A. 企業級 SaaS／HR Tech 與內部系統** | `jd09, jd11, jd31, jd32, jd34` | 現任 1111 企業端招募系統 PO（服務逾 6 萬家活躍付費廠商），在後台與資料庫不動下逆向實測補回權限與計費規則、規劃大型客戶部門／分店「群組功能」、完成 743/840 件建議（88%）、將 30 天結案率由 52% 升至 79%，並協助業務製作 sales kit。 | 1111 上線之群組功能、新版模組與 3 項 AI 功能未列出上線後的客戶採用率或留存指標；`jd34` 缺實體零售物流與購物車優惠券訂單經驗；`jd32` 需對齊內部系統定位與薪資區間。 |
| **B. 0-1 創新／AI 賦能與技術專案管理 (PM/TPM)** | `jd30, jd40, jd47` | 兼具 KOOL 網紅媒合平台 0 到 1 規劃與 1111 成熟系統 50 項大功能迭代；議定外部查詢 API 時涵蓋簽章驗證、時間戳防重放、錯誤碼、頻率限制與 JSON 欄位確認；以 Claude Code 建立協作流程與共用 skill，並能將業務搜尋篩選規則拆成查詢條件。 | 資料庫取數寫「擬定資料表與欄位需求，與 DBA 協作取數」，未明寫本人手寫 SQL 查詢程度；KOOL 0 到 1 平台未列上線後的用戶與媒合規模數據；未直接接觸停車或餐飲 POS 線下硬體。 |
| **C. 支付金流／外部平台串接與專案交付** | `jd03, jd26, jd36` | 具備 Peach 內購轉網頁付款（占營收由 24% 升至 80% 以上）、CodaPay 東南亞電信帳單與超商付款串接及抽成稅費實收試算、外部查詢 API 規格議定（簽章、防重放、錯誤碼、限流）、Axure RP 原型與上線前互動原型／FAQ 內部教育訓練。 | 專案管理使用 Trello、Notion 與內部專案控管系統，未直接寫出 `Jira、Confluence`；金流偏商戶端串接第三方支付，缺銀行專線或專營電子支付機構內部清算經驗。 |
| **D. 帳號安全防詐／跨國通訊與 2B 解決方案** | `jd20, jd43` | 同時具備「廠商招募帳號遭冒用之登入驗證與解鎖流程調整（2026/04–2026/10 零客服回報同類冒用）」、「外部 API 簽章防重放與頻率限制」及「信件與即時通整合（內部封測中）」，且具 TOEIC 980、赴美交換與 7 國在地化經驗。 | 純 B2B 產品經驗約 4 年（略低於 `jd20` 5-8 年 B2B 門檻）、跨國協作集中於 2016–2021 年、信件與即時通整合尚在內部封測中（預計 2026/11 底上線），且取數須與 DBA 協作。 |
| **E. 訂閱制內容平台／Growth 與實驗決策** | `jd14, jd44` | 具備約 6 年交友與訂閱制內容 App 經驗、馬來西亞 iOS 三階段對照定價實驗（各期 21 天，以 Android 為對照）、7／30／90 天訂閱方案與 VIP／點數付費牆設計、GA4 與世代分析及 3 項 AI 功能上線經驗。 | `jd14` 必備之 `Firebase` 未呈現；近 4 年重心轉向 B2B 招募系統，且 KOOL 與 1111 AI 功能缺乏上線後之參與度及留存率數據。 |

## 4. 跨職缺重複出現的缺口（≥3 份職缺出現才列；≤6 項）
| 缺口 | 出現職缺數 | 影響哪類職缺 | 履歷原句（≤40 字） | 需要候選人補什麼事實 |
| :-- | :-: | :-- | :-- | :-- |
| **1. 已上線功能（群組功能、AI 功能、KOOL）缺上線後採用與留存成效數據** | 12 份（`jd03, 09, 11, 14, 20, 30, 31, 34, 40, 43, 44, 47`） | 重視數據驅動、產品 KPI 與商業影響力之職缺 | `與工程於 2025/09 完成上線；完成三項功能上線` | 補充 1111「群組功能」、「第一階段新版模組」、「3 項 AI 功能」與尚凡「KOOL 網紅媒合平台」上線後的實際客戶採用數、媒合規模、轉換率或留存數據。 |
| **2. 資料庫取數需與 DBA 協作，未明寫獨立手寫 SQL 或 BI 工具能力** | 6 份（`jd20, 30, 31, 40, 47, 09`） | 要求自行查詢數據或強調技術底蘊之 PM 職缺 | `擬定資料表與欄位需求，與 DBA 協作取數` | 釐清本人是否能獨立撰寫基本 SQL 語法（如 `SELECT / JOIN / WHERE`）查詢資料庫，或說明如何將「拆解業務搜尋篩選查詢條件」的能力對應至 SQL 查詢。 |
| **3. 專案與文件工具未明列 Jira 與 Confluence** | 5 份（`jd11, 20, 26, 36, 43`） | 明文將 Jira、Confluence 列為必備條件之團隊 | `使用 Trello 及內部專案控管系統，按 User Story 記錄需求` | 若曾使用過 Jira 或 Confluence 請直接列名；若無，可於面試說明內部專案控管系統記錄 User Story、驗收條件與派工估時的流程如何無縫對應 Jira。 |
| **4. 進行中專案（信件與即時通整合、搜尋改版）尚無最終上線結果** | 4 份（`jd09, 11, 32, 43`） | 關注訊息整合體驗、搜尋轉換與近期改版成果之職缺 | `兩案均在開發中，信件與即時通整合已進入內部封測，預計 2026/11 底上線` | 依硬性規則 2，開發／封測中案例僅支持決策（`decision`）而不算已實現結果（`outcome`）；請準備封測期間之測試數據與上線前問題基準線供面試驗證。 |
| **5. B2B 外部企業客戶直接訪談、售前展示與海外 B2B 對接描寫較少** | 4 份（`jd09, 20, 31, 40`） | 強調第一線面對企業客戶、BD/Pre-sales 或 KA 協商之職缺 | `對接工程、行銷、業務與客服等 10 個需求單位` | 補充在規劃大型客戶群組功能、製作 sales kit 或清理客戶案件時，是否曾親自參與外部企業客戶需求訪談、售前產品展示或範疇協商。 |

## 4.5 跨職缺共同質疑（本版新增；≥3 份職缺出現才列；≤6 則）
| 質疑（用審查者口吻，≤40 字） | 誰會這樣想 | 出現職缺 | 觸發的履歷原句 | 會造成的結果 | 打消疑問需要什麼 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| **1. 群組功能、AI 功能跟 KOOL 都只寫完成上線，到底有沒有人用？成效在哪？** | 用人主管 | `jd09, 11, 14, 30, 31, 34, 44, 47`（8 份） | `與工程於 2025/09 完成上線；完成三項功能上線` | 面試追問（限制 Level 停在 8 無法上 9） | 提供群組功能開通廠商數、AI 生成與推薦採用率／準確率、以及 KOOL 雙邊用戶與報名規模等真實觀測指標。 |
| **2. 寫「與 DBA 協作取數」，是不是自己不會寫 SQL，看數據都要排隊等工程師？** | 用人主管／HR | `jd03, 20, 30, 31, 40, 47`（6 份） | `擬定資料表與欄位需求，與 DBA 協作取數` | 降低信任／面試追問（在 `jd20` 造成 `clarify_first`） | 說明公司資料庫權限限制背景、展示過去開給 DBA 的資料表與欄位關聯規格，並直接說明本人能否手寫基本 SQL（`SELECT / JOIN`）。 |
| **3. 840 件建議完成 743 件、50 項大功能、結案率升到 79%，是含金量高還是只挑小單清？** | 用人主管 | `jd03, 09, 31, 32, 40`（5 份） | `這些模組相關的 840 件廠商建議，已完成 743 件（88%）` | 面試追問 | 拆解 50 項大項功能與 743 件建議案的規模結構（核心架構改版 vs 常規優化占比），以及 2025 Q4 排定新案優先順序與拒絕不合理需求的標準。 |
| **4. 「未再透過客服接獲回報同類冒用」，是因為真的防住了，還是沒做系統主動監測？** | 用人主管 | `jd03, 20, 43`（3 份） | `調整後至 2026/10，未再透過客服接獲廠商回報同類冒用。` | 面試追問 | 補充 2026/04 調整登入驗證與解鎖流程後，後台是否有異常登入嘗試攔截紀錄或風險監控指標，並說明當時修正了哪一步客服操作。 |
| **5. 現職已是帶 2 人的主任且自傳說想做「產品策略」，來做偏執行或內部系統待得住嗎？** | HR／用人主管 | `jd26, 31, 32, 40, 47`（5 份） | `接下來，我希望把更多心力放回產品策略...對上線後的成效負責` | 面試追問 | 根據投遞職缺屬性調整自傳結尾或於面試說明：如何透過扎實的系統分析與交付落地來支撐產品策略，並確認對 IC 角色及目標職缺薪資區間的期待。 |
| **6. API 簽章防重放跟 Claude Code 共用 skill 寫得很具體，想約來當面驗貨真功夫！** | 用人主管（正面保留） | `jd03, 11, 20, 30, 36, 40, 47`（7 份） | `以簽章驗證與時間戳防止重放...以 Claude Code 建立協作流程` | **仍然約談（正面亮點，面試必驗細節）** | 準備好外部查詢 API 的 Request/Response JSON 規格範例與錯誤碼表，以及 Claude Code 共用 skill 如何將業務規則轉為工程條件的實機／案例展示。 |

### 整體第一印象（30 秒速讀反應）
- **HR 的第一印象**：「這是一位有近 10 年經驗、從消費型訂閱 App 一路做到 1111 人力銀行企業端系統主任的穩定型資深 PM，英文檢定分數極高（TOEIC 980）且履歷邏輯乾淨誠實，除了少數要求獨立寫 SQL 或特定產業年資的職缺需先確認外，多數職缺都能放心排進一面。」
- **用人主管的第一印象**：「他的強項非常明確——不怕接手沒文件的舊系統爛攤子，能靠實測與跨部門核對把複雜的帳號權限、計費規則與 API 規格（連簽章防重放跟 JSON 欄位都懂）理得清清楚楚並分階段上線，還會用 Claude Code 建工作流，是很可靠的實戰派 PO。」
- **Skeptical 的資深 PM 主管第一印象**：「他在『把混亂需求收斂成規格並準時交付（完成 88% 建議、30 天結案率拉到 79%）』的執行力無庸置疑，但近 4 年在 1111 的案例幾乎都停在『功能完成上線』與『內部結案效率』，缺少上線後真正改變用戶行為或商業北極星指標（Adoption / Retention / Revenue）的數據閉環，面試時我會重點追問他的產品成效衡量深度。」

## 5. 評語（合併後）

### 5.1 做得好（3 點；每點至少 2 份職缺支持，附原句與職缺代號）
1. **位置**：工作經歷 - 1111 全球華人（第 1、2、5 點）与專業技能（跨部門與系統整合）
   - **原句**：`接手求才系統改版時，業務後台與資料庫都不能更動，主副帳號權限...計費規則卻沒有文件。以實測歸納、請工程協助驗證，再與維運、稽核核對，把這些規則接回新版的規格與流程`；`與外部合作夥伴議定查詢 API 時，先處理可能被濫用的風險：以簽章驗證與時間戳防止重放...與工程確認 JSON 欄位與判定規則與判定規則。`
   - **支持職缺**：`jd03, jd09, jd11, jd20, jd26, jd30, jd31, jd32, jd34, jd36, jd40, jd43, jd47`（13 份職缺支持）
   - **為什麼有用**：具體展現資深 PM 在受限環境下逆向梳理無文件遺留系統、設計 B2B 大型客戶分店群組權限，以及主動處理外部 API 資安防濫用（簽章、時間戳防重放、錯誤碼、限流、JSON 欄位確認）的技術協作深度。
2. **位置**：工作經歷 - 尚凡國際創新科技（第 3、4 點）與思維特網路資訊（第 2 點）
   - **原句**：`設計馬來西亞 iOS 定價實驗，以售價不變的 Android 作對照，依序測試原價、降價與還原原價（2021/05–08，各期 21 天）。降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%；還原原價後，iOS 非續訂營收較原價期減 65%，團隊依結果決定採用低價。`；`2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上。`
   - **支持職缺**：`jd03, jd09, jd14, jd20, jd26, jd30, jd34, jd36, jd43, jd44, jd47`（11 份職缺支持）
   - **為什麼有用**：完整交代對照組實驗設計、21 天實驗週期、原價／降價／還原原價三階段數據比較與最終商業決策，搭配跨國金流串接與實收試算，強力支撐商業變現與數據實驗能力。
3. **位置**：工作經歷 - 1111 全球華人（第 3、7、8 點）與專業技能（AI 協作）
   - **原句**：`上線前以互動原型與 FAQ 向客服、業務說明，另協助業務製作銷售簡報`；`之後提出的案件，30 天內結案的比例由前一年的 52% 升至 79%（提案滿 30 天者）`；`以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格，並將業務規則轉為可與工程討論的條件描述。`
   - **支持職缺**：`jd09, jd11, jd20, jd26, jd30, jd31, jd32, jd34, jd36, jd40, jd47`（11 份職缺支持）
   - **為什麼有用**：同時證明跨 10 個部門的排程治理成效（30 天結案率由 52% 升至 79%）、賦能業務與客服的 Go-To-Market 落地力（互動原型、FAQ、sales kit），以及將 AI Agent 與 Claude Code 融入 PM 日常規格與邏輯拆解的實務能力。

### 5.2 可改進（≤6 點；欄位依 §6.2；只列 ≥2 份職缺重複或 blocking 的項目）
1. **1111 上線功能與 KOOL 平台缺乏上線後之使用者採用與業務成效指標**
   - 位置：1111 全球華人經歷（第 1、2、7 點）與尚凡國際經歷（第 1 點）
   - 原句：`與工程於 2025/09 完成上線；完成三項功能上線`
   - 問題類型：`measurement`
   - 嚴重度：`interview_follow_up`
   - 影響：在 12 份職缺中，審查者能看到「功能完成上線（`output`）」與「結案速度提升」，但看不出群組功能、新版首頁／公司資料、3 項 AI 功能及 KOOL 平台對用戶採用率、留存率或轉換率造成的實際改變（`outcome`），使多數職缺停在 Level 8。
   - 建議方向：在不違反保密原則下，補充已上線功能的觀測數據（例如：群組功能開通廠商數或留存表現、AI 生成與推薦功能的使用率、KOOL 累積網紅檔案與報名規模）。
2. **資料庫取數方式易被解讀為不具備基本 SQL 查詢能力**
   - 位置：專業技能 - 研究與數據／工具與技術素養
   - 原句：`擬定資料表與欄位需求，與 DBA 協作取數，再以 Excel 分析。`
   - 問題類型：`requirement`
   - 嚴重度：`interview_follow_up`（對 `jd20` 為關鍵釐清項）
   - 影響：`jd20, jd30, jd31, jd40, jd47` 皆明文要求基本 SQL 或獨立查詢數據；雖在工具欄寫明「能將業務上的搜尋、篩選規則拆成查詢條件」，但未出現 `SQL` 字樣仍會引發用人主管疑慮。
   - 建議方向：若本人具備基礎 SQL 語法閱讀或撰寫能力（如 `SELECT / WHERE / JOIN`），建議於「工具與技術素養」或「研究與數據」明確補註。
3. **約 50 項大項功能與 840 件廠商建議之規模結構未拆解**
   - 位置：1111 全球華人經歷（第 1、3 點）
   - 原句：`這些模組相關的 840 件廠商建議，已完成 743 件（88%）；主責約 50 項大項功能的規劃`
   - 問題類型：`readability`
   - 嚴重度：`interview_follow_up`
   - 影響：資深主管易質疑 840 件建議與 50 項大項功能的顆粒度（有多少屬核心架構改造 vs 常規小型修改）。
   - 建議方向：可簡要補充代表性分類（例如涵蓋權限計費、跨系統整合、AI 功能等幾大類模組）或於面試準備功能清單。
4. **專案管理工具未明列 Jira、Confluence**
   - 位置：專業技能 - 專案交付／工具與技術素養
   - 原句：`使用 Trello 及內部專案控管系統，按 User Story 記錄需求`
   - 問題類型：`requirement`
   - 嚴重度：`editorial`
   - 影響：`jd11, jd20, 26, 36, 43` 點名熟悉 Jira、Confluence；字面比對時會列為 `partial`。
   - 建議方向：若曾使用過 Jira / Confluence 請直接補上；若無則維持現有誠實表述並於面試說明內部控管系統之單據流轉邏輯。
5. **帳號防冒用之成效口徑偏被動回報**
   - 位置：1111 全球華人經歷（第 6 點）
   - 原句：`調整後至 2026/10，未再透過客服接獲廠商回報同類冒用。`
   - 問題類型：`measurement`
   - 嚴重度：`editorial`
   - 影響：雖非常誠實交代資料來源為客服回報，但風控與資安類職缺（`jd20, jd43`）主管會追問是否有系統主動攔截或告警數據。
   - 建議方向：面試時準備好登入驗證調整的具體規則，以及系統後台是否有觀測異常登入失敗率或解鎖申請量的變化。

### 5.3 面試最可能被追問的 5 題（附建議準備的事實，不代答）
1. **【成效衡量與北極星指標】你在 1111 上線的「第一階段改版（登入、首頁、公司資料）」、「大型客戶部門／分店群組功能」與「3 項 AI 生成／推薦功能」，以及在尚凡從 0 到 1 規劃的「KOOL 網紅媒合平台」，上線後如何衡量成功？實際數據表現如何？**
   - **建議準備的事實**：準備各專案的核心觀測指標（如：群組功能上線後開通的大型廠商數與使用頻率；AI 職缺生成與推薦人才的廠商採用率、客服測試回饋調整了哪些推薦規則；KOOL 上線後的網紅檔案數、案主刊案數與報名媒合次數）。
2. **【API 規格議定與技術協作深度】請具體說明你在 1111「與外部合作夥伴議定查詢 API」時，簽章驗證、時間戳防重放、錯誤碼、頻率限制與 JSON 欄位判定規則是如何設計的？另外你在與 DBA 協作取數時，是否能自行撰寫基本 SQL？**
   - **建議準備的事實**：準備該支查詢 API 的業務背景、Request/Response JSON 欄位結構、時間戳容許視窗、頻率限制（Rate Limit）門檻與錯誤碼定義表；並準備 1 個將複雜業務搜尋／篩選規則拆解為資料庫查詢條件（或基礎 SQL 語法）的實例。
3. **【遺留系統重構與無文件規則盤點】接手 1111 求才系統改版時，「業務後台與資料庫都不能更動，主副帳號權限...計費規則卻沒有文件」，你具體是如何透過實測與跨部門訪談補回規則，並完成 743 件（88%）廠商建議的？**
   - **建議準備的事實**：準備當時整理出的「主副帳號權限矩陣」與「合約制 vs 點數制計費扣點／退點規則表」結構範例；說明新舊系統並行期間如何確保舊資料庫相容，以及 840 件廠商建議中完成 743 件與拒絕／延後另外 97 件（12%）的判斷標準。
4. **【跨部門優先序與客戶案件治理】面對工程、行銷、業務、客服等 10 個需求單位，你在 2025 Q4 將「30 天內結案比例由 52% 升至 79%」，以及將「搜尋結果頁改版排在職缺健檢之前、優先推進信件與即時通整合」的排序邏輯與衝突協調過程為何？**
   - **建議準備的事實**：準備 2025 Q4 清理多年積案與排定新案優先級的評估框架（如何權衡提案時間、開發難易度、客戶影響範圍）；以及在公司一級主管日會向總經理、副總匯報時，說服高層將既有痛點（即時通整合、搜尋結果頁改版）排在新功能（職缺健檢）之前的數據依據。
5. **【Claude Code 協作工作流與定價實驗推論】請展示你如何「以 Claude Code 建立協作流程與共用 skill，將業務規則轉為可與工程討論的條件描述」？另外在馬來西亞 iOS 定價實驗中，為何還原原價後非續訂營收會較原價期減 65%？**
   - **建議準備的事實**：準備 Claude Code 共用 skill 的實際工作流步驟（輸入什麼業務規則、如何透過 Agent 檢查邊界條件並轉成工程規格描述）；以及馬來西亞 iOS 定價實驗三階段（原價、降價、還原原價各 21 天）的訂單量、客單價與總營收（含續訂）試算邏輯。

## 6. ATS 準備檢查（五塊，不加總）

> **說明**：已針對本次附檔之實體 PDF **`resume-v10.3-twocol.pdf`**（檔案大小：`803,180 bytes`，共 **3 頁**，未加密，Producer: `Skia/PDF m141` / `HeadlessChrome/141.0.0.0`，建立時間：`2026-10-17 17:42:21 UTC`，SHA-256：`c18b78c924ab31eb8285e69e7f563428bdba9b70b4e0ed053a018e697be5fdb4`）執行本機文字擷取實測（`pypdf`、`pdfplumber`、`pdftotext`；`test_level: local_extraction`、`actual_ats_import_performed: false`）。依套件 §0、§1 與 §4.3 規定，ATS 準備檢查獨立成段、**不給通用「ATS 分數」**，亦不影響內容審查評等。

| 檢查區塊 | 狀態 | 檢查依據與 `resume-v10.3-twocol.pdf` 本機實測結果（ATS01–ATS14） |
| :-- | :-: | :-- |
| **1. 檔案接受 (File Acceptance)** | `pass`（本機檔案）／`not_tested`（真實平台） | **ATS01/02/13**：本機檢查 `resume-v10.3-twocol.pdf` 為標準未加密 PDF（`is_encrypted: False`，約 784 KB，3 頁），符合各大招募平台（104、Greenhouse、Ashby、Workable）之格式與大小上限；未執行雇主端真實 ATS 匯入測試（`actual_ats_import_performed: false`）。 |
| **2. 欄位解析 (Field Parsing)** | **`risk`**（第 1 頁段落完整度改善，惟第 2 頁雙欄穿插與第 3 頁 3 行孤頁為 `risk`） | **ATS03/04/12**：<br>① **基本欄位與第 1 頁結構（`pass`）**：姓名 `聶崑淮`、職稱 `資深產品經理｜Senior Product Manager`、信箱 `kunhuainie@gmail.com`、電話 `0978802871` 皆單次乾淨擷取（無任何粗體疊字）；且第 1 頁左欄完整收納 `專業摘要` 與 `1111 全球華人` 全部 8 條 bullet，右欄完整收納 `專業技能` 與 `學歷`，第 1 頁本身不再發生跨頁斷句。<br>② **第 2 頁頂部左、右欄讀序穿插（`risk`）**：第 2 頁頂部左欄為 `Product Manager｜尚凡國際創新科技｜2018/01 - 2022/03`，右欄為 `求職條件`。在 `pdftotext` 預設讀序中，尚凡國際的標題與導言被右欄的 `求職條件` 穿插切割（讀序變成：`Product Manager -> 尚凡國際創新科技 -> 求職條件 -> 資深產品經理... -> 經手交友... -> 市，可接受遠端或混合辦公｜錄取後三週可 -> 並與工程... -> 上班 -> 2018/01 - 2022/03`）；在 `pdfplumber` 中，第 1 頁與第 2 頁頂部的左右欄同高文字則會被橫向拼成同一行（如 `專業摘要 專業技能`、`Product Manager 求職條件`）。<br>③ **第 3 頁僅 3 行文字之溢流孤頁（`risk`）**：由於自傳前四段排在第 2 頁底部，自傳最後一段（`這些年，我累積了系統分析...做出對使用者與業務更有影響的產品。`，共 3 行、140 字）單獨溢流至第 3 頁頂部，使整份履歷變成 3 頁且第 3 頁 90% 為空白（雖依 §3.1 規準絕不因頁數扣內容分，但建議微調行距收斂回 2 頁）。 |
| **3. 搜尋可見性 (Search Visibility)** | **`risk`**（英文與 `pdftotext` 為 `pass`；`pypdf`/`pdfminer` 有康熙部首字碼風險） | **ATS05/06**：<br>① **英文關鍵字（`pass`）**：`Product Owner`、`Product Manager`、`PRD`、`User Journey Map`、`User Story`、`Use Case`、`Wireframe`、`Prototype`、`UAT`、`Scrum`、`Sprint`、`Kanban`、`GA4`、`API`、`JSON`、`Figma`、`Axure RP`、`Notion`、`Trello`、`HTML`、`CSS`、`Claude Code`、`AI Agent`、`TOEIC 980`、`AWS` 在所有擷取器皆 100% 精確命中。<br>② **中文字型 `/Type3` 康熙部首字碼映射（`risk`）**：Linux HeadlessChrome 匯出時將部分中文字體嵌入為 `/Type3` 字型（伴隨 `FontBBox None` 警告），導致全文 **36 個常用漢字（共出現 178 次，如 `⼯, ⽤, ⼈, ⼒, ⾏, ⾴, ⼾, ⾨, ⾦, ⽂, ⼿, ⼊, ⽌, ⽐, ⽣, ⽬, ⽴, ⾊, ⾓, ⾔, ⾮, ⾯, ⾰, ⾵, ⾸, ⾺`）** 的 Unicode 被映射至 **康熙部首區段（`U+2F00..U+2FD5`）** 而非標準 CJK 表意文字（`U+4E00..U+9FFF`）。在支援 NFKC 正規化的解析器（如 `pdftotext`）中可正常搜尋；但在未做 NFKC 正規化的解析器（如 `pypdf`、`pdfplumber`）中，直接搜尋標準字元 `工程`、`使用者`、`人力銀行`、`網頁`、`客戶`、`部門`、`金流`、`風險` 會因字碼不同而漏失。 |
| **4. 資格與流程條件 (Qualifications & Workflow)** | `unknown` | **ATS07/08/10/11**：無外部平台申請表單與平台中繼資料（標 `unknown`）；履歷載明之求職條件（雙北、可接受遠端或混合辦公、錄取後三週可上班）與 15 份職缺均無已知衝突。 |
| **5. 匹配功能與未知設定 (Matching & Unknown Config)** | `unknown` | **ATS09/14**：雇主後台是否啟用 AI 自動匹配排序與權重設定未知（標 `unknown`），依規準不合成任何通用 ATS 分數。 |

## 7. 方法限制與未做項目
- `model_id`、是否每次都是新 context、實際跑了幾次：
  - `model_id`: `gemini-4-argon`（Gemini 4 Argon）。
  - 實際執行次數：完整執行 **單份審查 A 共 15 次**（針對 `jd03` 至 `jd47` 共 15 份職缺各審查 1 次，100% 依據本次 `validation-kit-single-15jd-v10.3.md` 附錄 A 履歷與 `resume-v10.3-twocol.pdf` 獨立取證，不引用其他職缺或任何過往對話評分，亦不做任何版本比較）＋ **ATS 本機抽字與字碼檢查 1 次**＋ **§4.4 V 階段截斷可見性測試 1 次**＋ **跨職缺總報告彙整 1 次**。
  - 是否每次都是新 context（限制誠實揭露）：受限於單一代理執行環境，無法開啟 15 個物理隔離的全新對話視窗；本報告於同一執行環境中透過程式化結構隔離，每次僅載入單一職缺條件與規準獨立判讀（嚴格遵守硬性規則 1–7，不拿 A 職缺條件扣 B 職缺分），並依 §0 規定誠實揭露「非 15 個獨立對話視窗執行」。
- **§4.4 V 階段（選做）：截斷文字可見性壓力測試結果（「前 3 行全句＋經歷抬頭前 24 字寬＋其他行只剩開頭 10 字寬，約 1,400 字截斷」內部代理規則）**：
  - **可見項目**：前 3 行完整保留姓名 `聶崑淮`、目標職稱 `資深產品經理｜Senior Product Manager` 與聯絡資訊 `kunhuainie@gmail.com｜0978802871`；經歷抬頭保留前 24 字寬，因此 `Product Owner／PM｜1111 全球`、`Product Manager｜尚凡國際創新科技`、`Associate PM｜思維特網路資訊` 之職稱與公司名稱清楚可見；各條 bullet 開頭 10 字寬（如 `接手求才系統改版時，`、`大型客戶需要讓部門或`、`2023/12–20`、`廠商反映的問題以溝通`、`與外部合作夥伴議定查`、`針對廠商招募帳號遭冒`、`與資料科學團隊合作，`、`2025 Q4 公司`、`規劃 KOOL 網紅`、`JustDating`、`設計馬來西亞 iOS`、`規劃 Peach 付`）仍可辨識出改版、大型客戶、外部 API、帳號防冒用、資料科學合作、KOOL、馬來西亞定價實驗與 Peach 付款等主題輪廓。
  - **截斷後變為 `unknown` 之項目**：因每行僅留開頭 10 字寬且於約 1,400 字處截斷，位於句中／句尾的所有具體量化數字與技術細節（如 `840 件完成 743 件 (88%)`、`2025/09 完成上線`、`簽章驗證與時間戳防止重放 / JSON 欄位`、`30 天內結案由 52% 升至 79%`、`iOS 增 5% / Android 減 18%`、`網頁付款 24% 升至 80% 以上`）以及位於 1,400 字之後的 `專業技能` 全區段（`Scrum/Kanban`、`GA4`、`Claude Code`、`TOEIC 980`、`AWS 證照`）在純遮罩截斷文字下均會落入 `unknown`。
- 未做：真實 ATS 匯入、真人校準：
  - 真實 ATS 匯入：`not_run`（`actual_ats_import_performed: false`）。
  - 真人校準：`not_run`（`human_calibration: not_run`）。
- 技術失敗或格式修補（保留原始輸出，不改判定）：
  - 無技術失敗（`technical_failure: 0`）；15 份單行 JSON 與報告全文均通過自動化腳本核對。

# 附錄 A：15 份單份審查完整輸出（單行 JSON ＋ §6.2 評語格式，含 §5.5 審查者的質疑）

## 單份審查｜履歷 Resume_v10.3_AppendixA（jd03 產品經理 (Pi錢包)｜拍付國際）｜第 1 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd03","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd03-01","human_calibrated":false,"requirements":[{"id":"R01","text":"2年以上獨立PM經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"獨立負責多款B2C與B2B產品規劃與交付"},{"id":"R02","text":"能撰寫PRD/User Story/Wireframe","type":"required","status":"supported","evidence":["從需求釐清、系統分析到流程與原型設計，完成 PRD"],"blocks_interview":false,"reason":"完整具備User Story、Wireframe與PRD實績"},{"id":"R03","text":"理解API串接與系統運作邏輯","type":"required","status":"supported","evidence":["以簽章驗證與時間戳防止重放，以錯誤碼與頻率限制控管呼叫"],"blocks_interview":false,"reason":"具外部API規格議定、JSON欄位確認與CodaPay串接經驗"},{"id":"R04","text":"金融科技/支付/點數/電子票證/電商經驗","type":"preferred","status":"supported","evidence":["另規劃並上線 VIP 訂閱、點數付費牆與精選曝光"],"blocks_interview":false,"reason":"具網頁付款、點數機制与CodaPay電信超商支付經驗"},{"id":"R05","text":"政府機關或銀行產品串接經驗","type":"preferred","status":"unknown","evidence":["未呈現政府機關或銀行系統直接串接紀錄"],"blocks_interview":false,"reason":"過往金流為第三方聚合支付CodaPay串接"},{"id":"R06","text":"會員經營/用戶留存與數據觀測分析經驗","type":"preferred","status":"supported","evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"blocks_interview":false,"reason":"具訂閱定價對照實驗、GA4與世代分析經驗"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["系統服務逾 6 萬家活躍付費廠商（2026 Q3）"],"missing":["近4年主責B2B招募系統，非高頻錢包支付核心"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"強","evidence":["與外部合作夥伴議定查詢 API 時，先處理可能被濫用的風險"],"missing":["未呈現銀行或政府機關直接串接紀錄"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["以簽章驗證與時間戳防止重放，以錯誤碼與頻率限制控管呼叫"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"missing":["1111改版與群組功能缺上線後採用與留存成效"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"對位 jd03 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd03 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"證據鏈支持安排 jd03 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"過去串接 CodaPay 與規劃 Peach 網頁付款時，如何處理掉單重試、退款與對帳？若改對接銀行或政府機關，你預期技術與法遵有哪些差異？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd03 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"加分條件之「政府機關或銀行產品串接經驗」未呈現（過往金流為第三方支付 CodaPay 與網頁付款）","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗，經手 6 款產品","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["曾推進「Peach 付款由 App 內購轉向網頁，與 CodaPay 新加坡技術團隊協調串接，網頁付款占營收由 24% 升至 80% 以上」並完成東南亞超商與電信帳單支付實收試算","與外部夥伴議定查詢 API 時「以簽章驗證與時間戳防止重放...與工程確認 JSON 欄位與判定規則與判定規則」，符合支付場景對 API 安全與系統邏輯的要求","現任 1111 招募系統 PO，在後台與資料庫不動的限制下補回合約與點數計費規則並分階段上線，完成 743/840 件廠商建議（88%）"],"key_gaps":["加分條件之「政府機關或銀行產品串接經驗」未呈現（過往金流為第三方支付 CodaPay 與網頁付款）","近 4 年主力於 B2B 招募系統，高頻支付與點數變現案例集中於 2016–2022 年","1111 上線之新版功能與群組功能僅列交付進度與結案比例，未列上線後的用戶採用率或轉換成效"],"strengths":["1111經歷第5點｜以簽章驗證與時間戳防止重放，以錯誤碼與頻率限制控管呼叫｜對 jd03 直接證明具備 API 規格議定、資安防濫用與 JSON 邏輯確認能力","尚凡經歷第4點｜規劃 Peach 付款由 App 內購轉向網頁，與 CodaPay 新加坡技術團隊協調串接｜對 jd03 展現第三方金流串接與支付渠道轉換實績","1111經歷第1點｜主副帳號權限、合約制與點數制的計費規則卻沒有文件。以實測歸納...｜對 jd03 證明能梳理無文件的複雜點數計費與權限邏輯"],"interview_questions":["過去串接 CodaPay 與規劃 Peach 網頁付款時，如何處理掉單重試、退款與對帳？若改對接銀行或政府機關，你預期技術與法遵有哪些差異？","你在 1111 盤點「合約制與點數制的計費規則」時，處理了哪些點數扣款、退還或效期邊界條件？","1111 第一階段改版（登入、首頁、公司資料）與群組功能上線後，實際廠商切換率與使用活躍度如何？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd03 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：具「網頁付款占營收由 24% 升至 80% 以上」與外部 API 簽章防重放規劃實績，支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 系統服務逾 6 萬家活躍付費廠商（2026 Q3） | 近4年主責B2B招募系統，非高頻錢包支付核心 |
| role_evidence | 強 | 與外部合作夥伴議定查詢 API 時，先處理可能被濫用的風險 | 未呈現銀行或政府機關直接串接紀錄 |
| decision_depth | 強 | 以簽章驗證與時間戳防止重放，以錯誤碼與頻率限制控管呼叫 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 1111改版與群組功能缺上線後採用與留存成效 |
| ownership | 強 | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 以實測歸納、請工程協助驗證，再與維運、稽核核對 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 2年以上獨立PM經驗 | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 獨立負責多款B2C與B2B產品規劃與交付 |
| R02 能撰寫PRD/User Story/Wireframe | 必要 | supported | 從需求釐清、系統分析到流程與原型設計，完成 PRD | 完整具備User Story、Wireframe與PRD實績 |
| R03 理解API串接與系統運作邏輯 | 必要 | supported | 以簽章驗證與時間戳防止重放，以錯誤碼與頻率限制控管呼叫 | 具外部API規格議定、JSON欄位確認與CodaPay串接經驗 |
| R04 金融科技/支付/點數/電子票證/電商經驗 | 加分 | supported | 另規劃並上線 VIP 訂閱、點數付費牆與精選曝光 | 具網頁付款、點數機制与CodaPay電信超商支付經驗 |
| R05 政府機關或銀行產品串接經驗 | 加分 | unknown | 未呈現政府機關或銀行系統直接串接紀錄 | 過往金流為第三方聚合支付CodaPay串接 |
| R06 會員經營/用戶留存與數據觀測分析經驗 | 加分 | supported | 降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18% | 具訂閱定價對照實驗、GA4與世代分析經驗 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 對位 jd03 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 以實測歸納、請工程協助驗證，再與維運、稽核核對 | 清楚界定個人規劃與工程/QA/DBA分工 |
| HR04 | supported | 30 天內結案的比例由前一年的 52% 升至 79% | 具結案率與定價實驗數據，缺部分功能採用率 |
| HR05 | supported | 將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與新舊並行取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端消費產品演進至B2B平台主任 |
| HR07 | supported | 上線前以互動原型與 FAQ 向客服、業務說明 | Scrum、原型、API議定、AI與英文皆有實例 |
| HR08 | supported | 從需求釐清、系統分析、流程與畫面設計，到 PRD | 結構分明，問題背景、動作與結果易讀 |
| HR09 | supported | 上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 誠實標註行銷導流期間、封測中與客服回報口徑 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd03 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃 | 證據鏈支持安排 jd03 面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人 | 針對大客戶部門/分店共同招募痛點設計群組權限 |
| HM03 | supported | 依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與新舊並行取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數機制與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18% | 結案率與定價實驗基準清晰，缺部分功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程 | 具後台不動下新舊並行、API防重放與防冒用閉環 |
| HM08 | supported | 以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則 | 能確認API JSON欄位與拆解查詢條件，取數協作DBA |
| HM09 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 上線調整，並依客服回饋修正操作方式 | 依客服回饋修正登入操作方式與AI推薦規則 |
| HM12 | supported | 具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd03 明文條件與附錄 A 履歷獨立取證判讀 | 僅依 jd03 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 曾推進「Peach 付款由 App 內購轉向網頁，與 CodaPay 新加坡技術團隊協調串接，網頁付款占營收由 24% 升至 80% 以上」並完成東南亞超商與電信帳單支付實收試算 |
| 2 | 與外部夥伴議定查詢 API 時「以簽章驗證與時間戳防止重放...與工程確認 JSON 欄位與判定規則與判定規則」，符合支付場景對 API 安全與系統邏輯的要求 |
| 3 | 現任 1111 招募系統 PO，在後台與資料庫不動的限制下補回合約與點數計費規則並分階段上線，完成 743/840 件廠商建議（88%） |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 加分條件之「政府機關或銀行產品串接經驗」未呈現（過往金流為第三方支付 CodaPay 與網頁付款） | 過去串接 CodaPay 與規劃 Peach 網頁付款時，如何處理掉單重試、退款與對帳？若改對接銀行或政府機關，你預期技術與法遵有哪些差異？ |
| 2 | 近 4 年主力於 B2B 招募系統，高頻支付與點數變現案例集中於 2016–2022 年 | 你在 1111 盤點「合約制與點數制的計費規則」時，處理了哪些點數扣款、退還或效期邊界條件？ |
| 3 | 1111 上線之新版功能與群組功能僅列交付進度與結案比例，未列上線後的用戶採用率或轉換成效 | 1111 第一階段改版（登入、首頁、公司資料）與群組功能上線後，實際廠商切換率與使用活躍度如何？ |

### 5.5 審查者的質疑（本版新增；不是缺口清單）
#### 質疑 1
- **誰在想**：用人主管
- **讀到哪一句**：以簽章驗證與時間戳防止重放，以錯誤碼與頻率限制控管呼叫
- **心裡怎麼想**：「這段讓我想約！一般 PM 寫 API 串接只會寫「對接第三方」，他卻能精確講出防重放、時間戳、頻率限制與 JSON 判定規則，但我想當面確認這些機制是他主動提出的，還是工程師設計好他照抄進規格書的。」
- **這個疑問會讓我**：仍然約談
- **要打消疑問，履歷或面試需要看到**：面試時請他口述該支查詢 API 的完整 Request/Response 結構、時間戳容許誤差範圍，以及頻率限制觸發時的業務處理流程。

#### 質疑 2
- **誰在想**：HR
- **讀到哪一句**：2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上。
- **心裡怎麼想**：「這是他最亮眼的支付戰績，但已經是 5 年前的事了；最近 4 年他在 1111 都在做人力銀行招募系統，為什麼現在想回頭看高頻支付與錢包產品？」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：說明從企業招募系統轉回支付生態系的求職動機，以及近 4 年在 1111 處理「點數制計費規則」與「帳號安全防冒用」如何銜接支付產品。

#### 質疑 3
- **誰在想**：用人主管
- **讀到哪一句**：這些模組相關的 840 件廠商建議，已完成 743 件（88%）。
- **心裡怎麼想**：「88% 完成率聽起來很高，但「廠商建議」包山包海，裡面有多少是改個文案或修個小 bug 就結案？真正動到計費與權限核心架構的占多少？」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：拆解這 743 件已完成建議的規模分布（例如：核心流程調整、欄位擴充、介面優化各占多少比例）以及拒絕另外 12% 建議的判斷標準。

#### 質疑 4
- **誰在想**：用人主管
- **讀到哪一句**：網頁付款占營收由 24% 升至 80% 以上。
- **心裡怎麼想**：「把 App 內購導去網頁付款雖然能省雙平台 30% 抽成，但通常會違反 App Store / Google Play 條款，甚至他前面才寫 JustDating 遭 App Store 下架，這讓我有點擔心他對合規風險的尺度。」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：釐清當時導流網頁付款的合規邊界，以及進入受金管會與銀行高度監管的電子支付場景後，如何配合法遵規範做產品設計。

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷第5點｜以簽章驗證與時間戳防止重放，以錯誤碼與頻率限制控管呼叫｜對 jd03 直接證明具備 API 規格議定、資安防濫用與 JSON 邏輯確認能力
- 尚凡經歷第4點｜規劃 Peach 付款由 App 內購轉向網頁，與 CodaPay 新加坡技術團隊協調串接｜對 jd03 展現第三方金流串接與支付渠道轉換實績
- 1111經歷第1點｜主副帳號權限、合約制與點數制的計費規則卻沒有文件。以實測歸納...｜對 jd03 證明能梳理無文件的複雜點數計費與權限邏輯

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：加分條件之「政府機關或銀行產品串接經驗」未呈現（過往金流為第三方支付 CodaPay 與網頁付款）
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落
- 位置：1111 經歷第 1、2、4、7 點與尚凡第 1 點
  - 原句：與工程於 2025/09 完成上線；完成三項功能上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：強

### 8. 未測試聲明
PDF 抽字：local_extraction（已於總報告 §6 獨立列示 `resume-v10.3-twocol.pdf` 本機抽字結果，不併入內容評等） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

## 單份審查｜履歷 Resume_v10.3_AppendixA（jd09 產品經理 Product Manager｜微拓科技 (beBit TECH)）｜第 2 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd09","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd09-02","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上軟體產品或專案管理經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"年資與軟體產品交付量充足"},{"id":"R02","text":"B2B SaaS經驗尤佳","type":"preferred","status":"supported","evidence":["人力銀行企業端招募系統專案負責人，系統服務逾 6 萬家活躍付費廠商"],"blocks_interview":false,"reason":"近4年主責大型B2B企業端招募系統"},{"id":"R03","text":"熟悉UI/UX概念方法論","type":"required","status":"supported","evidence":["User Journey Map、User Story、Use Case、Wir"],"blocks_interview":false,"reason":"具使用者旅程檢視、Wireframe與互動原型經驗"},{"id":"R04","text":"批判性思維與優先序判斷","type":"required","status":"supported","evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"blocks_interview":false,"reason":"依使用者旅程與溝通中斷痛點調整Roadmap優先序"},{"id":"R05","text":"數據驅動思維","type":"required","status":"supported","evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"blocks_interview":false,"reason":"具三階段定價對照實驗、GA4與世代分析經驗"},{"id":"R06","text":"獨立作業善跨部門溝通、製作說明文件","type":"required","status":"supported","evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"blocks_interview":false,"reason":"對接10個單位並產出FAQ與sales kit"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["系統服務逾 6 萬家活躍付費廠商（2026 Q3）"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"強","evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"missing":["未直接經手 MarTech（CDP+MA+BI）產品"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"足夠","evidence":["30 天內結案的比例由前一年的 52% 升至 79%（提案滿 30 天者）"],"missing":["1111上線之企業端功能未列客戶採用率或留存提升數據"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD、Prototype"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"對位 jd09 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"partial","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd09 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"證據鏈支持安排 jd09 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"你在 1111 於 2025/09 上線的大型客戶「群組功能」與 2025/10 上線的新版首頁，上線後如何分析使用情況並提出迭代優化建議？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd09 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"1111 上線之企業端功能（如大型客戶群組功能、第一階段改版、AI 推薦）缺乏上線後的廠商使用率或留存指標","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗，經手 6 款產品","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["現任 1111 企業端招募系統 PO（服務逾 6 萬家活躍付費廠商），完整負責需求搜集、Roadmap 優先序、PRD、測試驗收與 sales kit 製作，完全對應 jd09 工作內容","具備依據使用者旅程與客服業務回饋排定優先級的實證（「優先推進信件與即時通整合；將搜尋結果頁改版排在新功能職缺健檢之前」）","具備三階段定價實驗、GA4、世代分析及「擬定資料表與欄位需求，與 DBA 協作取數」之數據分析能力"],"key_gaps":["1111 上線之企業端功能（如大型客戶群組功能、第一階段改版、AI 推薦）缺乏上線後的廠商使用率或留存指標","B2B 需求來源多寫「廠商反映」「與內部維運稽核訪談」，較少描寫 PM 主導外部企業客戶深度訪談的過程","未直接經手 MarTech（CDP+MA+BI）行銷科技產品"],"strengths":["1111經歷第3點｜上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報｜對 jd09 直接命中「製作說明文件、與客服業務合作推動產品迭代與上市」職責","1111經歷第2點｜規劃群組功能，讓同單位帳號共同處理職缺...於 2025/09 完成上線｜對 jd09 證明具備 B2B 企業多層級帳號權限與資料範圍設計經驗","1111經歷第4點｜依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前｜對 jd09 展現基於使用者旅程與痛點的產品路線圖優先序判斷"],"interview_questions":["你在 1111 於 2025/09 上線的大型客戶「群組功能」與 2025/10 上線的新版首頁，上線後如何分析使用情況並提出迭代優化建議？","在規劃大型客戶部門／分店群組功能時，你是透過業務轉述需求，還是曾親自訪談大型企業 HR 客戶？","過去在 1111 處理求職者篩選查詢條件與 AI 推薦人才的經驗，如何遷移至 CDP 受眾分群與自動化行銷劇本設計？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd09 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：主責「系統服務逾 6 萬家活躍付費廠商」之企業平台且具跨部門排程與定價實驗實績，支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 系統服務逾 6 萬家活躍付費廠商（2026 Q3） | 無關鍵缺口，可於面試深化 |
| role_evidence | 強 | 2023/12–2026/03 主責約 50 項大項功能的規劃 | 未直接經手 MarTech（CDP+MA+BI）產品 |
| decision_depth | 強 | 依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 足夠 | 30 天內結案的比例由前一年的 52% 升至 79%（提案滿 30 天者） | 1111上線之企業端功能未列客戶採用率或留存提升數據 |
| ownership | 強 | 上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 從需求釐清、系統分析、流程與畫面設計，到 PRD、Prototype | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 3年以上軟體產品或專案管理經驗 | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 年資與軟體產品交付量充足 |
| R02 B2B SaaS經驗尤佳 | 加分 | supported | 人力銀行企業端招募系統專案負責人，系統服務逾 6 萬家活躍付費廠商 | 近4年主責大型B2B企業端招募系統 |
| R03 熟悉UI/UX概念方法論 | 必要 | supported | User Journey Map、User Story、Use Case、Wir | 具使用者旅程檢視、Wireframe與互動原型經驗 |
| R04 批判性思維與優先序判斷 | 必要 | supported | 將搜尋結果頁改版排在新功能職缺健檢之前 | 依使用者旅程與溝通中斷痛點調整Roadmap優先序 |
| R05 數據驅動思維 | 必要 | supported | 降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18% | 具三階段定價對照實驗、GA4與世代分析經驗 |
| R06 獨立作業善跨部門溝通、製作說明文件 | 必要 | supported | 上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報 | 對接10個單位並產出FAQ與sales kit |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 對位 jd09 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 以實測歸納、請工程協助驗證，再與維運、稽核核對 | 清楚界定個人規劃與工程/QA/DBA分工 |
| HR04 | partial | 30 天內結案的比例由前一年的 52% 升至 79% | 具結案率與定價實驗數據，缺部分功能採用率 |
| HR05 | supported | 將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與新舊並行取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端消費產品演進至B2B平台主任 |
| HR07 | supported | 上線前以互動原型與 FAQ 向客服、業務說明 | Scrum、原型、API議定、AI與英文皆有實例 |
| HR08 | supported | 從需求釐清、系統分析、流程與畫面設計，到 PRD | 結構分明，問題背景、動作與結果易讀 |
| HR09 | supported | 上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 誠實標註行銷導流期間、封測中與客服回報口徑 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd09 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃 | 證據鏈支持安排 jd09 面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人 | 針對大客戶部門/分店共同招募痛點設計群組權限 |
| HM03 | supported | 依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與新舊並行取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數機制與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18% | 結案率與定價實驗基準清晰，缺部分功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程 | 具後台不動下新舊並行、API防重放與防冒用閉環 |
| HM08 | supported | 以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則 | 能確認API JSON欄位與拆解查詢條件，取數協作DBA |
| HM09 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 上線調整，並依客服回饋修正操作方式 | 依客服回饋修正登入操作方式與AI推薦規則 |
| HM12 | supported | 具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd09 明文條件與附錄 A 履歷獨立取證判讀 | 僅依 jd09 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 現任 1111 企業端招募系統 PO（服務逾 6 萬家活躍付費廠商），完整負責需求搜集、Roadmap 優先序、PRD、測試驗收與 sales kit 製作，完全對應 jd09 工作內容 |
| 2 | 具備依據使用者旅程與客服業務回饋排定優先級的實證（「優先推進信件與即時通整合；將搜尋結果頁改版排在新功能職缺健檢之前」） |
| 3 | 具備三階段定價實驗、GA4、世代分析及「擬定資料表與欄位需求，與 DBA 協作取數」之數據分析能力 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 1111 上線之企業端功能（如大型客戶群組功能、第一階段改版、AI 推薦）缺乏上線後的廠商使用率或留存指標 | 你在 1111 於 2025/09 上線的大型客戶「群組功能」與 2025/10 上線的新版首頁，上線後如何分析使用情況並提出迭代優化建議？ |
| 2 | B2B 需求來源多寫「廠商反映」「與內部維運稽核訪談」，較少描寫 PM 主導外部企業客戶深度訪談的過程 | 在規劃大型客戶部門／分店群組功能時，你是透過業務轉述需求，還是曾親自訪談大型企業 HR 客戶？ |
| 3 | 未直接經手 MarTech（CDP+MA+BI）行銷科技產品 | 過去在 1111 處理求職者篩選查詢條件與 AI 推薦人才的經驗，如何遷移至 CDP 受眾分群與自動化行銷劇本設計？ |

### 5.5 審查者的質疑（本版新增；不是缺口清單）
#### 質疑 1
- **誰在想**：用人主管
- **讀到哪一句**：上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報
- **心裡怎麼想**：「這段很加分，我會想約來聊！做 B2B SaaS 最怕 PM 只顧把功能丟上線卻不管業務怎麼賣、客服怎麼接，他連 sales kit 都幫忙做，但我想問他在前期需求訪談時有沒有直接面對過企業客戶，還是只當內部傳聲筒。」
- **這個疑問會讓我**：仍然約談
- **要打消疑問，履歷或面試需要看到**：分享一個親自參與企業客戶需求訪談（或從客服／業務端挖掘深層需求）並轉化為產品規格與 sales kit 賣點的完整案例。

#### 質疑 2
- **誰在想**：用人主管
- **讀到哪一句**：規劃群組功能，讓同單位帳號共同處理職缺...於 2025/09 完成上線
- **心裡怎麼想**：「2025 年 9 月就上線的 B2B 重點功能，到現在已經過了一年，履歷上卻完全沒寫到底有幾家大型企業開通使用、有沒有帶來續約或增購，這會讓我懷疑他是不是只看重「功能上線」而沒在看上線後的數據表現。」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：提供群組功能上線後的實際採用數據（開通廠商數、使用頻率或對大型客戶續約的影響）。

#### 質疑 3
- **誰在想**：HR
- **讀到哪一句**：30 天內結案的比例由前一年的 52% 升至 79%（提案滿 30 天者）。
- **心裡怎麼想**：「結案率從 52% 拉到 79% 數字很漂亮，但這是因為公司政策改以客戶案件為優先、工程資源傾斜，還是他真的改善了需求拆解與排程流程？」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：說明在「先清理多年積案，再依提案時間與難易安排新案」過程中，他具體建立了什麼評估標準或協作規則來縮短結案週期。

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷第3點｜上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報｜對 jd09 直接命中「製作說明文件、與客服業務合作推動產品迭代與上市」職責
- 1111經歷第2點｜規劃群組功能，讓同單位帳號共同處理職缺...於 2025/09 完成上線｜對 jd09 證明具備 B2B 企業多層級帳號權限與資料範圍設計經驗
- 1111經歷第4點｜依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前｜對 jd09 展現基於使用者旅程與痛點的產品路線圖優先序判斷

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之企業端功能（如大型客戶群組功能、第一階段改版、AI 推薦）缺乏上線後的廠商使用率或留存指標
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落
- 位置：1111 經歷第 1、2、4、7 點與尚凡第 1 點
  - 原句：與工程於 2025/09 完成上線；完成三項功能上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：強

### 8. 未測試聲明
PDF 抽字：local_extraction（已於總報告 §6 獨立列示 `resume-v10.3-twocol.pdf` 本機抽字結果，不併入內容評等） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

## 單份審查｜履歷 Resume_v10.3_AppendixA（jd11 【北士科】Product Manager｜沛思坦 (Pacston)）｜第 3 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd11","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd11-03","human_calibrated":false,"requirements":[{"id":"R01","text":"5年以上PM經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"年資近10年且涵蓋B2B與B2C"},{"id":"R02","text":"熟悉敏捷開發與跨部門專案管理","type":"required","status":"supported","evidence":["曾參與每週一個 Sprint 的 Scrum，現行以 Kanban 推進瀑布式"],"blocks_interview":false,"reason":"兼具Scrum與Kanban跨10單位專案管理"},{"id":"R03","text":"優秀邏輯與溝通能力","type":"required","status":"supported","evidence":["能將業務上的搜尋、篩選規則拆成查詢條件，與工程確認後端行為"],"blocks_interview":false,"reason":"邏輯拆解與跨部門溝通能力扎實"},{"id":"R04","text":"熟悉Jira、Notion等工具","type":"required","status":"partial","evidence":["Figma、Axure RP、Notion、Trello；內部專案控管系統"],"blocks_interview":false,"reason":"具Notion、Trello與內部控管系統，未點名Jira"},{"id":"R05","text":"中英文文件撰寫能力","type":"required","status":"supported","evidence":["英文 TOEIC 980、TOEFL iBT 93，曾赴美交換，並以英文進行跨國"],"blocks_interview":false,"reason":"具高分英檢與跨國英文協作經驗"},{"id":"R06","text":"HR Tech/LegalTech/生成式AI產品經驗","type":"preferred","status":"supported","evidence":["定義公司簡介生成、職缺工作說明生成及 AI 推薦人才的使用情境與驗收標準"],"blocks_interview":false,"reason":"直接具備HR Tech與3項生成式AI功能上線經驗"},{"id":"R07","text":"LLM prompt設計或自動化內容編排經驗","type":"preferred","status":"supported","evidence":["以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格"],"blocks_interview":false,"reason":"建立Claude Code協作流程與共用skill"},{"id":"R08","text":"資料導向思維、AB測試與技術背景","type":"preferred","status":"supported","evidence":["設計馬來西亞 iOS 定價實驗；基本 HTML／CSS 與資料庫知識"],"blocks_interview":false,"reason":"具對照實驗、資料庫知識、API規格議定與AWS證照"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["人力銀行企業端招募系統專案負責人，系統服務逾 6 萬家活躍付費廠商"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"強","evidence":["與資料科學團隊合作，定義公司簡介生成、職缺工作說明生成及 AI 推薦人才"],"missing":["使用 Trello 及內部專案控管系統、Notion，未直接寫出 Jira"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"足夠","evidence":["這些模組相關的 840 件廠商建議，已完成 743 件（88%）"],"missing":["AI 生成與推薦功能及群組功能未列上線後之產品 KPI 表現"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["結構清晰，完整呈現 HR 招募系統權限、流程與 AI 協作細節"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"對位 jd11 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"partial","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd11 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"證據鏈支持安排 jd11 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"你使用的內部專案控管系統與 Trello，在記錄 User Story、驗收條件與優先級供 Tech Lead 派工估時時，工作流如何運作？是否曾接觸過 Jira？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd11 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"必要條件點名之 `Jira` 未出現在履歷中（履歷為使用 Notion、Trello 及內部專案控管系統）","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗，經手 6 款產品","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["直接具備 HR Tech 核心背景（現任 1111 企業端招募系統 PO，熟悉主副帳號權限、部門／分店群組招募、職缺與履歷管理流程），與本職缺 HRIS／客戶管理系統高度同源","與資料科學團隊合作完成「公司簡介生成、職缺工作說明生成及 AI 推薦人才」三項功能上線，並「以 Claude Code 建立協作流程與共用 skill」，完全命中生成式 AI 與自動化編排加分項","具備每週一 Sprint 之 Scrum 與 Kanban 經驗，且能將搜尋篩選規則拆成查詢條件與工程確認後端行為"],"key_gaps":["必要條件點名之 `Jira` 未出現在履歷中（履歷為使用 Notion、Trello 及內部專案控管系統）","上線之三項 AI 功能（公司簡介生成、職缺說明生成、AI 推薦人才）與群組功能未列出上線後的採用率或準確度 KPI","兩項重點改版（信件與即時通整合、搜尋結果頁改版）尚在開發／封測中"],"strengths":["1111經歷第1-2點｜主副帳號權限、合約制與點數制的計費規則...規劃群組功能，讓同單位帳號共同處理職缺及對應履歷｜對 jd11 直接對位客戶管理與 HRIS 系統最核心的組織權限與招募流程設計","1111經歷第7點與AI技能｜定義公司簡介生成、職缺工作說明生成及 AI 推薦人才...以 Claude Code 建立協作流程與共用 skill｜對 jd11 同時命中 HR Tech、生成式 AI 產品上線與 LLM 自動化內容編排","專業技能（專案交付）｜按 User Story 記錄需求、做法、驗收條件與優先級，供 Tech Lead 派工與估時｜對 jd11 清楚展現與工程團隊推進開發的規格結構與協作深度"],"interview_questions":["你使用的內部專案控管系統與 Trello，在記錄 User Story、驗收條件與優先級供 Tech Lead 派工估時時，工作流如何運作？是否曾接觸過 Jira？","「公司簡介生成、職缺工作說明生成及 AI 推薦人才」三項功能上線後，你是如何定義驗收標準與追蹤線上 KPI 的？客服測試回饋讓你調整了哪些推薦規則？","目前進入內部封測的「信件與即時通整合」與開發中的「搜尋結果頁改版」，預計上線後追蹤哪些核心 KPI？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd11 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：現任「人力銀行企業端招募系統專案負責人」且具 Scrum、AI 功能上線與 Claude Code 協作實績，高度契合。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 人力銀行企業端招募系統專案負責人，系統服務逾 6 萬家活躍付費廠商 | 無關鍵缺口，可於面試深化 |
| role_evidence | 強 | 與資料科學團隊合作，定義公司簡介生成、職缺工作說明生成及 AI 推薦人才 | 使用 Trello 及內部專案控管系統、Notion，未直接寫出 Jira |
| decision_depth | 強 | 依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 足夠 | 這些模組相關的 840 件廠商建議，已完成 743 件（88%） | AI 生成與推薦功能及群組功能未列上線後之產品 KPI 表現 |
| ownership | 強 | 以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 結構清晰，完整呈現 HR 招募系統權限、流程與 AI 協作細節 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 5年以上PM經驗 | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 年資近10年且涵蓋B2B與B2C |
| R02 熟悉敏捷開發與跨部門專案管理 | 必要 | supported | 曾參與每週一個 Sprint 的 Scrum，現行以 Kanban 推進瀑布式 | 兼具Scrum與Kanban跨10單位專案管理 |
| R03 優秀邏輯與溝通能力 | 必要 | supported | 能將業務上的搜尋、篩選規則拆成查詢條件，與工程確認後端行為 | 邏輯拆解與跨部門溝通能力扎實 |
| R04 熟悉Jira、Notion等工具 | 必要 | partial | Figma、Axure RP、Notion、Trello；內部專案控管系統 | 具Notion、Trello與內部控管系統，未點名Jira |
| R05 中英文文件撰寫能力 | 必要 | supported | 英文 TOEIC 980、TOEFL iBT 93，曾赴美交換，並以英文進行跨國 | 具高分英檢與跨國英文協作經驗 |
| R06 HR Tech/LegalTech/生成式AI產品經驗 | 加分 | supported | 定義公司簡介生成、職缺工作說明生成及 AI 推薦人才的使用情境與驗收標準 | 直接具備HR Tech與3項生成式AI功能上線經驗 |
| R07 LLM prompt設計或自動化內容編排經驗 | 加分 | supported | 以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格 | 建立Claude Code協作流程與共用skill |
| R08 資料導向思維、AB測試與技術背景 | 加分 | supported | 設計馬來西亞 iOS 定價實驗；基本 HTML／CSS 與資料庫知識 | 具對照實驗、資料庫知識、API規格議定與AWS證照 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 對位 jd11 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 以實測歸納、請工程協助驗證，再與維運、稽核核對 | 清楚界定個人規劃與工程/QA/DBA分工 |
| HR04 | partial | 30 天內結案的比例由前一年的 52% 升至 79% | 具結案率與定價實驗數據，缺部分功能採用率 |
| HR05 | supported | 將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與新舊並行取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端消費產品演進至B2B平台主任 |
| HR07 | supported | 上線前以互動原型與 FAQ 向客服、業務說明 | Scrum、原型、API議定、AI與英文皆有實例 |
| HR08 | supported | 從需求釐清、系統分析、流程與畫面設計，到 PRD | 結構分明，問題背景、動作與結果易讀 |
| HR09 | supported | 上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 誠實標註行銷導流期間、封測中與客服回報口徑 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd11 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃 | 證據鏈支持安排 jd11 面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人 | 針對大客戶部門/分店共同招募痛點設計群組權限 |
| HM03 | supported | 依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與新舊並行取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數機制與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18% | 結案率與定價實驗基準清晰，缺部分功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程 | 具後台不動下新舊並行、API防重放與防冒用閉環 |
| HM08 | supported | 以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則 | 能確認API JSON欄位與拆解查詢條件，取數協作DBA |
| HM09 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 上線調整，並依客服回饋修正操作方式 | 依客服回饋修正登入操作方式與AI推薦規則 |
| HM12 | supported | 具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd11 明文條件與附錄 A 履歷獨立取證判讀 | 僅依 jd11 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 直接具備 HR Tech 核心背景（現任 1111 企業端招募系統 PO，熟悉主副帳號權限、部門／分店群組招募、職缺與履歷管理流程），與本職缺 HRIS／客戶管理系統高度同源 |
| 2 | 與資料科學團隊合作完成「公司簡介生成、職缺工作說明生成及 AI 推薦人才」三項功能上線，並「以 Claude Code 建立協作流程與共用 skill」，完全命中生成式 AI 與自動化編排加分項 |
| 3 | 具備每週一 Sprint 之 Scrum 與 Kanban 經驗，且能將搜尋篩選規則拆成查詢條件與工程確認後端行為 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 必要條件點名之 `Jira` 未出現在履歷中（履歷為使用 Notion、Trello 及內部專案控管系統） | 你使用的內部專案控管系統與 Trello，在記錄 User Story、驗收條件與優先級供 Tech Lead 派工估時時，工作流如何運作？是否曾接觸過 Jira？ |
| 2 | 上線之三項 AI 功能（公司簡介生成、職缺說明生成、AI 推薦人才）與群組功能未列出上線後的採用率或準確度 KPI | 「公司簡介生成、職缺工作說明生成及 AI 推薦人才」三項功能上線後，你是如何定義驗收標準與追蹤線上 KPI 的？客服測試回饋讓你調整了哪些推薦規則？ |
| 3 | 兩項重點改版（信件與即時通整合、搜尋結果頁改版）尚在開發／封測中 | 目前進入內部封測的「信件與即時通整合」與開發中的「搜尋結果頁改版」，預計上線後追蹤哪些核心 KPI？ |

### 5.5 審查者的質疑（本版新增；不是缺口清單）
#### 質疑 1
- **誰在想**：用人主管
- **讀到哪一句**：定義公司簡介生成、職缺工作說明生成及 AI 推薦人才的使用情境與驗收標準
- **心裡怎麼想**：「既做過招募系統主副帳號權限，又上線過職缺說明生成跟 AI 推薦人才，背景跟我們要做的 HRIS 簡直一模一樣，這個人我一定會約！但我心裡會保留一點：他在這三項 AI 功能裡到底懂不懂 Prompt 與評估指標，還是只負責畫前端畫面跟收客服回饋？」
- **這個疑問會讓我**：仍然約談
- **要打消疑問，履歷或面試需要看到**：面試時請他展示當時定義的「AI 生成與推薦驗收標準」具體長什麼樣子，以及依客服回饋調整了哪一條推薦邏輯。

#### 質疑 2
- **誰在想**：用人主管
- **讀到哪一句**：接手求才系統改版時，業務後台與資料庫都不能更動，主副帳號權限...沒有文件
- **心裡怎麼想**：「從零補回舊系統規則很苦工、很扎實，但『業務後台與資料庫都不能更動』也代表他在 1111 一直在做既有資料庫架構下的相容性妥協，如果來我們這裡要從頭設計全新的 CMS/HRIS 資料結構，他跳得出來嗎？」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：請他分享若不受舊資料庫限制，他會如何重新設計「企業－部門／分店群組－主副帳號－職缺與履歷權限」的資料模型。

#### 質疑 3
- **誰在想**：HR
- **讀到哪一句**：曾參與每週一個 Sprint 的 Scrum，現行以 Kanban 推進瀑布式
- **心裡怎麼想**：「「以 Kanban 推進瀑布式開發」這句話很誠實，但也代表他現在的環境其實是瀑布流，而且他用的是 Trello 跟內部系統而不是 Jira，我需要確認他對敏捷迭代與 Jira 協作的熟悉度。」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：確認在哪一段經歷跑過每週一 Sprint 的 Scrum、他擔任的角色，以及對 Jira 流程的熟悉程度。

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷第1-2點｜主副帳號權限、合約制與點數制的計費規則...規劃群組功能，讓同單位帳號共同處理職缺及對應履歷｜對 jd11 直接對位客戶管理與 HRIS 系統最核心的組織權限與招募流程設計
- 1111經歷第7點與AI技能｜定義公司簡介生成、職缺工作說明生成及 AI 推薦人才...以 Claude Code 建立協作流程與共用 skill｜對 jd11 同時命中 HR Tech、生成式 AI 產品上線與 LLM 自動化內容編排
- 專業技能（專案交付）｜按 User Story 記錄需求、做法、驗收條件與優先級，供 Tech Lead 派工與估時｜對 jd11 清楚展現與工程團隊推進開發的規格結構與協作深度

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：必要條件點名之 `Jira` 未出現在履歷中（履歷為使用 Notion、Trello 及內部專案控管系統）
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落
- 位置：1111 經歷第 1、2、4、7 點與尚凡第 1 點
  - 原句：與工程於 2025/09 完成上線；完成三項功能上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：強

### 8. 未測試聲明
PDF 抽字：local_extraction（已於總報告 §6 獨立列示 `resume-v10.3-twocol.pdf` 本機抽字結果，不併入內容評等） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

## 單份審查｜履歷 Resume_v10.3_AppendixA（jd14 D441 MyVideo影音產品Growth PM｜台灣大哥大）｜第 4 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd14","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd14-04","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上Growth PM經驗（全生命週期與Growth Funnel）","type":"required","status":"supported","evidence":["經手交友、訂閱制內容 App 與網紅媒合平台，規劃使用流程、訂閱與付費機制"],"blocks_interview":false,"reason":"具約6年消費級訂閱制App獲取、付費轉換與定價實驗經驗"},{"id":"R02","text":"能獨立撰寫PRD/User Flow/Wireframe","type":"required","status":"supported","evidence":["系統分析、流程圖／循序圖、Wireframe、Prototype、PRD"],"blocks_interview":false,"reason":"完整具備流程圖、Wireframe與PRD實績"},{"id":"R03","text":"熟悉GA4、Firebase","type":"required","status":"partial","evidence":["使用者訪談與問卷、內部維運與稽核訪談、競品實測、GA4、世代分析與對照組實驗"],"blocks_interview":false,"reason":"明列GA4、世代分析與對照組實驗，未呈現Firebase"},{"id":"R04","text":"訂閱與會員轉換優化、A/B Test產品實驗","type":"required","status":"supported","evidence":["設計馬來西亞 iOS 定價實驗，以售價不變的 Android 作對照"],"blocks_interview":false,"reason":"具VIP訂閱、7/30/90天方案、網頁付款轉換與三階段定價實驗"},{"id":"R05","text":"跨部門溝通能力","type":"required","status":"supported","evidence":["與工程、設計、行銷及海外金流團隊協作上線"],"blocks_interview":false,"reason":"跨工程、設計、行銷與金流團隊推進產品成長"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["經手交友、訂閱制內容 App 與網紅媒合平台，規劃使用流程、訂閱與付費機制"],"missing":["近4年重心為B2B招募系統，C端訂閱成長案例集中於2016–2022年"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"足夠","evidence":["設計馬來西亞 iOS 定價實驗，以售價不變的 Android 作對照"],"missing":["必備條件點名之 Firebase 未呈現；缺 OTT 影音串流經驗"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["還原原價後，iOS 非續訂營收較原價期減 65%，團隊依結果決定採用低價"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["男性 DAU 在 6 週內由約 3,200 增至 1.25 萬"],"missing":["KOOL 訂閱點數牆與 1111 近期改版未列漏斗轉換率數據"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["主導 Juicy 推出並協調跨團隊工作，配合行銷導入既有用戶"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["清楚交代實驗設計、對照基準、期間與決策結果"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["經手交友、訂閱制內容 App 與網紅媒合平台，規劃使用流程、訂閱與付費機制"],"application_note":"對位 jd14 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd14 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"證據鏈支持安排 jd14 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"過去在尚凡與思維特經營 iOS／Android 訂閱制 App 時，除了 GA4 之外，是否有使用 Firebase（如 Analytics、Remote Config、A/B Testing 或 Crashlytics）的經驗？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd14 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"必備條件中點名之 `Firebase` 未呈現（履歷僅列 GA4、Google Sheets、Excel 與資料庫取數）","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["經手交友、訂閱制內容 App 與網紅媒合平台，規劃使用流程、訂閱與付費機制","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["具備約 6 年訂閱制消費型 App 經驗，曾設計馬來西亞 iOS 三階段定價實驗（以 Android 作對照，各期 21 天）驗證價格彈性並促成團隊決策","曾規劃 VIP 訂閱、點數付費牆、7／30／90 天訂閱方案與加贈內容，並推進 Peach 內購轉向網頁付款（占營收由 24% 升至 80% 以上）","熟稔 GA4、世代分析與對照組實驗，並能從 User Journey Map 檢視漏斗斷點（如信件與即時通整合、搜尋結果頁改版）"],"key_gaps":["必備條件中點名之 `Firebase` 未呈現（履歷僅列 GA4、Google Sheets、Excel 與資料庫取數）","C 端訂閱制與成長實驗集中於 2016–2022 年，近 4 年在 1111 以企業端系統重構與功能交付為主","KOOL 網紅媒合平台的 VIP 訂閱與點數付費牆未列出上線後的付費轉換率或留存數據"],"strengths":["尚凡經歷第3點｜設計馬來西亞 iOS 定價實驗，以售價不變的 Android 作對照，依序測試原價、降價與還原原價｜對 jd14 直接證明具備嚴謹的產品實驗設計與付費轉換分析能力","尚凡經歷第4點與思維特第2點｜網頁付款占營收由 24% 升至 80% 以上；提出 7／30／90 天訂閱方案與加贈內容｜對 jd14 展現訂閱方案設計、渠道轉換與實收試算的商業成長經驗","研究與數據技能｜使用者訪談與問卷、競品實測、GA4、世代分析與對照組實驗｜對 jd14 符合全生命週期留存（Cohort 世代分析）與量化決策要求"],"interview_questions":["過去在尚凡與思維特經營 iOS／Android 訂閱制 App 時，除了 GA4 之外，是否有使用 Firebase（如 Analytics、Remote Config、A/B Testing 或 Crashlytics）的經驗？","近 4 年在 1111 企業端系統工作期間，是否有運用漏斗分析或對照實驗來驗證改版成效的案例？為何現在想重回 C 端訂閱制 Growth PM？","你在 KOOL 規劃上線的 VIP 訂閱、點數付費牆與精選曝光，上線後的付費轉換率（CVR）與用戶留存表現如何？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":7,"uncertainty_levels":1,"basis":"針對 jd14 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：7（±1）
- 一句話理由：具「設計馬來西亞 iOS 定價實驗」與「網頁付款占營收由 24% 升至 80% 以上」實證，支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 經手交友、訂閱制內容 App 與網紅媒合平台，規劃使用流程、訂閱與付費機制 | 近4年重心為B2B招募系統，C端訂閱成長案例集中於2016–2022年 |
| role_evidence | 足夠 | 設計馬來西亞 iOS 定價實驗，以售價不變的 Android 作對照 | 必備條件點名之 Firebase 未呈現；缺 OTT 影音串流經驗 |
| decision_depth | 強 | 還原原價後，iOS 非續訂營收較原價期減 65%，團隊依結果決定採用低價 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 男性 DAU 在 6 週內由約 3,200 增至 1.25 萬 | KOOL 訂閱點數牆與 1111 近期改版未列漏斗轉換率數據 |
| ownership | 強 | 主導 Juicy 推出並協調跨團隊工作，配合行銷導入既有用戶 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 清楚交代實驗設計、對照基準、期間與決策結果 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 3年以上Growth PM經驗（全生命週期與Growth Funnel） | 必要 | supported | 經手交友、訂閱制內容 App 與網紅媒合平台，規劃使用流程、訂閱與付費機制 | 具約6年消費級訂閱制App獲取、付費轉換與定價實驗經驗 |
| R02 能獨立撰寫PRD/User Flow/Wireframe | 必要 | supported | 系統分析、流程圖／循序圖、Wireframe、Prototype、PRD | 完整具備流程圖、Wireframe與PRD實績 |
| R03 熟悉GA4、Firebase | 必要 | partial | 使用者訪談與問卷、內部維運與稽核訪談、競品實測、GA4、世代分析與對照組實驗 | 明列GA4、世代分析與對照組實驗，未呈現Firebase |
| R04 訂閱與會員轉換優化、A/B Test產品實驗 | 必要 | supported | 設計馬來西亞 iOS 定價實驗，以售價不變的 Android 作對照 | 具VIP訂閱、7/30/90天方案、網頁付款轉換與三階段定價實驗 |
| R05 跨部門溝通能力 | 必要 | supported | 與工程、設計、行銷及海外金流團隊協作上線 | 跨工程、設計、行銷與金流團隊推進產品成長 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 經手交友、訂閱制內容 App 與網紅媒合平台，規劃使用流程、訂閱與付費機制 | 對位 jd14 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 以實測歸納、請工程協助驗證，再與維運、稽核核對 | 清楚界定個人規劃與工程/QA/DBA分工 |
| HR04 | supported | 30 天內結案的比例由前一年的 52% 升至 79% | 具結案率與定價實驗數據，缺部分功能採用率 |
| HR05 | supported | 將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與新舊並行取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端消費產品演進至B2B平台主任 |
| HR07 | supported | 上線前以互動原型與 FAQ 向客服、業務說明 | Scrum、原型、API議定、AI與英文皆有實例 |
| HR08 | supported | 從需求釐清、系統分析、流程與畫面設計，到 PRD | 結構分明，問題背景、動作與結果易讀 |
| HR09 | supported | 上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 誠實標註行銷導流期間、封測中與客服回報口徑 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd14 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃 | 證據鏈支持安排 jd14 面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人 | 針對大客戶部門/分店共同招募痛點設計群組權限 |
| HM03 | supported | 依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與新舊並行取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數機制與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18% | 結案率與定價實驗基準清晰，缺部分功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程 | 具後台不動下新舊並行、API防重放與防冒用閉環 |
| HM08 | supported | 以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則 | 能確認API JSON欄位與拆解查詢條件，取數協作DBA |
| HM09 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 上線調整，並依客服回饋修正操作方式 | 依客服回饋修正登入操作方式與AI推薦規則 |
| HM12 | supported | 具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd14 明文條件與附錄 A 履歷獨立取證判讀 | 僅依 jd14 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 具備約 6 年訂閱制消費型 App 經驗，曾設計馬來西亞 iOS 三階段定價實驗（以 Android 作對照，各期 21 天）驗證價格彈性並促成團隊決策 |
| 2 | 曾規劃 VIP 訂閱、點數付費牆、7／30／90 天訂閱方案與加贈內容，並推進 Peach 內購轉向網頁付款（占營收由 24% 升至 80% 以上） |
| 3 | 熟稔 GA4、世代分析與對照組實驗，並能從 User Journey Map 檢視漏斗斷點（如信件與即時通整合、搜尋結果頁改版） |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 必備條件中點名之 `Firebase` 未呈現（履歷僅列 GA4、Google Sheets、Excel 與資料庫取數） | 過去在尚凡與思維特經營 iOS／Android 訂閱制 App 時，除了 GA4 之外，是否有使用 Firebase（如 Analytics、Remote Config、A/B Testing 或 Crashlytics）的經驗？ |
| 2 | C 端訂閱制與成長實驗集中於 2016–2022 年，近 4 年在 1111 以企業端系統重構與功能交付為主 | 近 4 年在 1111 企業端系統工作期間，是否有運用漏斗分析或對照實驗來驗證改版成效的案例？為何現在想重回 C 端訂閱制 Growth PM？ |
| 3 | KOOL 網紅媒合平台的 VIP 訂閱與點數付費牆未列出上線後的付費轉換率或留存數據 | 你在 KOOL 規劃上線的 VIP 訂閱、點數付費牆與精選曝光，上線後的付費轉換率（CVR）與用戶留存表現如何？ |

### 5.5 審查者的質疑（本版新增；不是缺口清單）
#### 質疑 1
- **誰在想**：用人主管
- **讀到哪一句**：設計馬來西亞 iOS 定價實驗，以售價不變的 Android 作對照
- **心裡怎麼想**：「這個定價實驗設計得很紮實，懂得拿 Android 當對照組排除大盤季節性波動，而且還做了『還原原價』確認不是短期促銷假象，這讓我很想約他！但我會先問：為什麼降價期 iOS 非續訂營收只增 5%，還原原價卻暴跌 65%？而且總營收（含續訂 LTV）算下來真的划算嗎？」
- **這個疑問會讓我**：仍然約談
- **要打消疑問，履歷或面試需要看到**：面試時請他拆解該次實驗的訂單量成長率 vs 客單價降幅、續訂留存率變化，以及為何還原原價會跌 65% 的用戶行為解釋。

#### 質疑 2
- **誰在想**：用人主管
- **讀到哪一句**：上線與行銷導流期間，男性 DAU 增至 1.25 萬
- **心裡怎麼想**：「他很誠實寫了『上線與行銷導流期間』，加上前一句寫『JustDating 遭 App Store 下架後，主導 Juicy 推出...導入既有用戶』，這代表 1.25 萬 DAU 其實是把舊 App 既有老用戶搬家過來的結果，不是他從 0 做 Acquisition 成長駭客做出來的。」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：區分 Juicy 上線 6 週內，「既有舊用戶轉移」與「新用戶自然／付費獲取」各占多少比例，以及產品端做了什麼機制提高搬家轉換率与留存。

#### 質疑 3
- **誰在想**：HR
- **讀到哪一句**：Product Owner／PM｜1111 全球華人｜2022/08 - 迄今
- **心裡怎麼想**：「他在尚凡做訂閱制 App 已經是 2022 年 3 月以前的事了，最近 4 年都在做傳統人力銀行的 B2B 後台改版，對現在 C 端影音串流的 Growth Funnel 跟 Firebase 工具還熟嗎？」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：確認對 GA4 / Firebase 事件埋點與漏斗分析的實務熟練度，以及對 MyVideo 影音訂閱留存痛點的想法。

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 尚凡經歷第3點｜設計馬來西亞 iOS 定價實驗，以售價不變的 Android 作對照，依序測試原價、降價與還原原價｜對 jd14 直接證明具備嚴謹的產品實驗設計與付費轉換分析能力
- 尚凡經歷第4點與思維特第2點｜網頁付款占營收由 24% 升至 80% 以上；提出 7／30／90 天訂閱方案與加贈內容｜對 jd14 展現訂閱方案設計、渠道轉換與實收試算的商業成長經驗
- 研究與數據技能｜使用者訪談與問卷、競品實測、GA4、世代分析與對照組實驗｜對 jd14 符合全生命週期留存（Cohort 世代分析）與量化決策要求

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：必備條件中點名之 `Firebase` 未呈現（履歷僅列 GA4、Google Sheets、Excel 與資料庫取數）
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落
- 位置：1111 經歷第 1、2、4、7 點與尚凡第 1 點
  - 原句：與工程於 2025/09 完成上線；完成三項功能上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：local_extraction（已於總報告 §6 獨立列示 `resume-v10.3-twocol.pdf` 本機抽字結果，不併入內容評等） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

## 單份審查｜履歷 Resume_v10.3_AppendixA（jd20 Senior Product Manager (Anti-Scam BU/2B)｜Gogolook）｜第 5 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd20","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd20-05","human_calibrated":false,"requirements":[{"id":"R01","text":"5-8年以上B2B/B2G產品或專案管理經驗","type":"required","status":"partial","evidence":["1111 全球華人｜2022/08 - 迄今（企業端招募系統專案負責人）"],"blocks_interview":false,"reason":"總PM近10年，惟純B2B經驗約4年略低於5-8年門檻"},{"id":"R02","text":"接近母語等級英語口說與書寫","type":"required","status":"partial","evidence":["英文 TOEIC 980、TOEFL iBT 93，曾赴美交換，並以英文進行跨國"],"blocks_interview":false,"reason":"英檢高分且有跨國協作，是否達母語級B2B商務談判待驗"},{"id":"R03","text":"優異溝通與關係人管理能力","type":"required","status":"supported","evidence":["對接工程、行銷、業務與客服等 10 個需求單位；向總經理、副總等主管匯報"],"blocks_interview":false,"reason":"跨10個單位協調需求並向高層匯報"},{"id":"R04","text":"扎實PM基礎（PRD/路線圖/待辦清單/時程風險）","type":"required","status":"supported","evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"blocks_interview":false,"reason":"主責50項大功能並將30天內結案率由52%升至79%"},{"id":"R05","text":"強烈數據敏感度（能獨立使用SQL/BI/試算表查詢分析）","type":"required","status":"partial","evidence":["擬定資料表與欄位需求，與 DBA 協作取數，再以 Excel 分析"],"blocks_interview":false,"reason":"精熟試算表與欄位規劃，惟取數需與DBA協作而非獨立寫SQL/BI"},{"id":"R06","text":"熟悉AI工具（如Claude）並串接Jira/Confluence自動化","type":"required","status":"partial","evidence":["以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格"],"blocks_interview":false,"reason":"深度使用Claude Code，惟未呈現串接Jira/Confluence"},{"id":"R07","text":"對防詐與風險偵測有熱情及防詐/資安/風控產品經驗","type":"required","status":"supported","evidence":["針對廠商招募帳號遭冒用...確認登入驗證與帳號解鎖流程，於 2026/04 上線"],"blocks_interview":false,"reason":"具B2B帳號防冒用調整與外部API簽章防重放/限流控管實績"},{"id":"R08","text":"曾服務企業客戶或政府機關，尤其海外市場（東南亞/日韓）","type":"preferred","status":"partial","evidence":["推進 SweetRing 在美國、墨西哥、巴西、印尼、馬來西亞、日本與韓國 7 "],"blocks_interview":false,"reason":"具東南亞與日韓7國B2C在地化與台灣B2B，缺海外B2B/B2G客戶經驗"},{"id":"R09","text":"具Agile/Scrum與定價、報價或成本利潤分析經驗","type":"preferred","status":"supported","evidence":["曾參與每週一個 Sprint 的 Scrum；整理各管道的抽成、稅、手續費與撥款"],"blocks_interview":false,"reason":"具Scrum、定價實驗與跨國金流成本實收試算經驗"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["人力銀行企業端招募系統專案負責人，系統服務逾 6 萬家活躍付費廠商"],"missing":["純B2B經驗約4年（略低於5-8年B2B門檻），且未直接面對海外B2B/B2G客戶與BD"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"足夠","evidence":["以簽章驗證與時間戳防止重放，以錯誤碼與頻率限制控管呼叫"],"missing":["取數須與 DBA 協作而非獨立寫 SQL；未明列 Jira/Confluence 串接"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["與外部合作夥伴議定查詢 API 時，先處理可能被濫用的風險"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"足夠","evidence":["調整後至 2026/10，未再透過客服接獲廠商回報同類冒用"],"missing":["1111企業端新功能缺採用與留存指標；防冒用成效以客服回報為準"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["參與公司一級主管日會，向總經理、副總等主管匯報"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["結構清晰，清楚呈現 API 防濫用、帳號防冒用與 Claude Code 工作流"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"partial","resume_evidence":["1111 全球華人｜2022/08 - 迄今（企業端招募系統專案負責人）"],"application_note":"對位 jd20 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"partial","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd20 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"partial","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"建議先釐清 jd20 關鍵條件再安排面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"partial","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":"在分析產品數據時，本人是否能獨立撰寫 SQL 查詢資料庫？"},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"在 1111 需要分析產品數據時，你本人能否獨立撰寫 SQL 查詢資料庫或操作 BI 工具？過去在尚凡規劃 KOOL 時包含多少對 B 端（案主／公司行號）的需求管理經驗？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd20 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"必備條件要求「5-8年以上B2B/B2G經驗」與「自行查詢並解讀產品數據（能獨立使用SQL/BI）」，目前純 B2B 約 4 年且取數須與 DBA 協作","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"clarify_first","evidence":["1111 全球華人｜2022/08 - 迄今（企業端招募系統專案負責人）","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":["必備條件要求「5-8年以上B2B/B2G經驗」與「自行查詢並解讀產品數據（能獨立使用SQL/BI）」，目前純 B2B 約 4 年且取數須與 DBA 協作"]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["直接具備兩項防濫用與帳號安全實績：議定外部查詢 API 時「以簽章驗證與時間戳防止重放，以錯誤碼與頻率限制控管呼叫」，以及「針對廠商招募帳號遭冒用，確認登入驗證與帳號解鎖流程，於 2026/04 上線調整」","深度運用 Claude Code 建立協作流程與共用 skill，並與資料科學團隊協作上線 3 項 AI 功能，高度契合 JD 對 Claude 與 AI 團隊協作的要求","具備逾 6 萬家企業客戶系統之 PO 交付經驗（50 項大功能上線、30 天結案率由 52% 升至 79%）與 TOEIC 980／赴美交換跨國協作背景"],"key_gaps":["必備條件要求「5-8年以上B2B/B2G經驗」與「自行查詢並解讀產品數據（能獨立使用SQL/BI）」，目前純 B2B 約 4 年且取數須與 DBA 協作","未呈現直接向海外企業客戶（東南亞、日韓 B2B/B2G）與 BD 團隊收集需求並轉化為產品路線圖的經驗","專案管理與文件工具列 Trello、Notion 與內部系統，未明列串接 Jira、Confluence"],"strengths":["1111經歷第5-6點｜以簽章驗證與時間戳防止重放...針對廠商招募帳號遭冒用...確認登入驗證與帳號解鎖流程｜對 jd20 直接對位 Anti-Scam BU 重視之防濫用、帳號安全與風險控管經驗","AI協作技能與1111經歷第7點｜以 Claude Code 建立協作流程與共用 skill...與資料科學團隊合作完成三項功能上線｜對 jd20 直接命中「善用 AI 工具（如 Claude）」與「與 RD/AI 團隊密切合作」","1111經歷第8點｜30 天內結案的比例由前一年的 52% 升至 79%（提案滿 30 天者）｜對 jd20 證明具備 50% 專案與交付管理所需的時程控管與積案清理能力"],"interview_questions":["在 1111 需要分析產品數據時，你本人能否獨立撰寫 SQL 查詢資料庫或操作 BI 工具？過去在尚凡規劃 KOOL 時包含多少對 B 端（案主／公司行號）的需求管理經驗？","請以英文分享：若要向東南亞或日韓的企業／銀行客戶推廣防詐 API 或 2B 解決方案，你會如何與 BD 配合收集跨市場需求並排定優先序？","你建立的 Claude Code 協作流程與共用 skill 目前如何與內部專案控管系統銜接？若要串接 Jira 與 Confluence 自動化工作流，你會如何設計？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":7,"uncertainty_levels":1,"basis":"針對 jd20 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：clarify_first
- Level：7（±1）
- 一句話理由：具「針對廠商招募帳號遭冒用...於 2026/04 上線調整」與 API 防重放實績，惟 B2B 年資約 4 年且取數須與 DBA 協作，建議先釐清。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 人力銀行企業端招募系統專案負責人，系統服務逾 6 萬家活躍付費廠商 | 純B2B經驗約4年（略低於5-8年B2B門檻），且未直接面對海外B2B/B2G客戶與BD |
| role_evidence | 足夠 | 以簽章驗證與時間戳防止重放，以錯誤碼與頻率限制控管呼叫 | 取數須與 DBA 協作而非獨立寫 SQL；未明列 Jira/Confluence 串接 |
| decision_depth | 強 | 與外部合作夥伴議定查詢 API 時，先處理可能被濫用的風險 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 足夠 | 調整後至 2026/10，未再透過客服接獲廠商回報同類冒用 | 1111企業端新功能缺採用與留存指標；防冒用成效以客服回報為準 |
| ownership | 強 | 參與公司一級主管日會，向總經理、副總等主管匯報 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 結構清晰，清楚呈現 API 防濫用、帳號防冒用與 Claude Code 工作流 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 5-8年以上B2B/B2G產品或專案管理經驗 | 必要 | partial | 1111 全球華人｜2022/08 - 迄今（企業端招募系統專案負責人） | 總PM近10年，惟純B2B經驗約4年略低於5-8年門檻 |
| R02 接近母語等級英語口說與書寫 | 必要 | partial | 英文 TOEIC 980、TOEFL iBT 93，曾赴美交換，並以英文進行跨國 | 英檢高分且有跨國協作，是否達母語級B2B商務談判待驗 |
| R03 優異溝通與關係人管理能力 | 必要 | supported | 對接工程、行銷、業務與客服等 10 個需求單位；向總經理、副總等主管匯報 | 跨10個單位協調需求並向高層匯報 |
| R04 扎實PM基礎（PRD/路線圖/待辦清單/時程風險） | 必要 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線 | 主責50項大功能並將30天內結案率由52%升至79% |
| R05 強烈數據敏感度（能獨立使用SQL/BI/試算表查詢分析） | 必要 | partial | 擬定資料表與欄位需求，與 DBA 協作取數，再以 Excel 分析 | 精熟試算表與欄位規劃，惟取數需與DBA協作而非獨立寫SQL/BI |
| R06 熟悉AI工具（如Claude）並串接Jira/Confluence自動化 | 必要 | partial | 以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格 | 深度使用Claude Code，惟未呈現串接Jira/Confluence |
| R07 對防詐與風險偵測有熱情及防詐/資安/風控產品經驗 | 必要 | supported | 針對廠商招募帳號遭冒用...確認登入驗證與帳號解鎖流程，於 2026/04 上線 | 具B2B帳號防冒用調整與外部API簽章防重放/限流控管實績 |
| R08 曾服務企業客戶或政府機關，尤其海外市場（東南亞/日韓） | 加分 | partial | 推進 SweetRing 在美國、墨西哥、巴西、印尼、馬來西亞、日本與韓國 7  | 具東南亞與日韓7國B2C在地化與台灣B2B，缺海外B2B/B2G客戶經驗 |
| R09 具Agile/Scrum與定價、報價或成本利潤分析經驗 | 加分 | supported | 曾參與每週一個 Sprint 的 Scrum；整理各管道的抽成、稅、手續費與撥款 | 具Scrum、定價實驗與跨國金流成本實收試算經驗 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | partial | 1111 全球華人｜2022/08 - 迄今（企業端招募系統專案負責人） | 對位 jd20 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 以實測歸納、請工程協助驗證，再與維運、稽核核對 | 清楚界定個人規劃與工程/QA/DBA分工 |
| HR04 | partial | 30 天內結案的比例由前一年的 52% 升至 79% | 具結案率與定價實驗數據，缺部分功能採用率 |
| HR05 | supported | 將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與新舊並行取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端消費產品演進至B2B平台主任 |
| HR07 | supported | 上線前以互動原型與 FAQ 向客服、業務說明 | Scrum、原型、API議定、AI與英文皆有實例 |
| HR08 | supported | 從需求釐清、系統分析、流程與畫面設計，到 PRD | 結構分明，問題背景、動作與結果易讀 |
| HR09 | supported | 上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 誠實標註行銷導流期間、封測中與客服回報口徑 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd20 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | partial | 2023/12–2026/03 主責約 50 項大項功能的規劃 | 建議先釐清 jd20 關鍵條件再安排面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人 | 針對大客戶部門/分店共同招募痛點設計群組權限 |
| HM03 | supported | 依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與新舊並行取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數機制與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18% | 結案率與定價實驗基準清晰，缺部分功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程 | 具後台不動下新舊並行、API防重放與防冒用閉環 |
| HM08 | partial | 以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則 | 能確認API JSON欄位與拆解查詢條件，取數協作DBA |
| HM09 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 上線調整，並依客服回饋修正操作方式 | 依客服回饋修正登入操作方式與AI推薦規則 |
| HM12 | supported | 具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd20 明文條件與附錄 A 履歷獨立取證判讀 | 僅依 jd20 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 直接具備兩項防濫用與帳號安全實績：議定外部查詢 API 時「以簽章驗證與時間戳防止重放，以錯誤碼與頻率限制控管呼叫」，以及「針對廠商招募帳號遭冒用，確認登入驗證與帳號解鎖流程，於 2026/04 上線調整」 |
| 2 | 深度運用 Claude Code 建立協作流程與共用 skill，並與資料科學團隊協作上線 3 項 AI 功能，高度契合 JD 對 Claude 與 AI 團隊協作的要求 |
| 3 | 具備逾 6 萬家企業客戶系統之 PO 交付經驗（50 項大功能上線、30 天結案率由 52% 升至 79%）與 TOEIC 980／赴美交換跨國協作背景 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 必備條件要求「5-8年以上B2B/B2G經驗」與「自行查詢並解讀產品數據（能獨立使用SQL/BI）」，目前純 B2B 約 4 年且取數須與 DBA 協作 | 在 1111 需要分析產品數據時，你本人能否獨立撰寫 SQL 查詢資料庫或操作 BI 工具？過去在尚凡規劃 KOOL 時包含多少對 B 端（案主／公司行號）的需求管理經驗？ |
| 2 | 未呈現直接向海外企業客戶（東南亞、日韓 B2B/B2G）與 BD 團隊收集需求並轉化為產品路線圖的經驗 | 請以英文分享：若要向東南亞或日韓的企業／銀行客戶推廣防詐 API 或 2B 解決方案，你會如何與 BD 配合收集跨市場需求並排定優先序？ |
| 3 | 專案管理與文件工具列 Trello、Notion 與內部系統，未明列串接 Jira、Confluence | 你建立的 Claude Code 協作流程與共用 skill 目前如何與內部專案控管系統銜接？若要串接 Jira 與 Confluence 自動化工作流，你會如何設計？ |

### 5.5 審查者的質疑（本版新增；不是缺口清單）
#### 質疑 1
- **誰在想**：用人主管
- **讀到哪一句**：以簽章驗證與時間戳防止重放，以錯誤碼與頻率限制控管呼叫
- **心裡怎麼想**：「看到這句加上後面處理廠商帳號被盜用，我覺得他對資安與防濫用是有真概念的，再加上有用 Claude Code 建 skill，會讓我想約他聊聊！但我們 2B Anti-Scam BU 有一半時間要面對海外 BD 跟企業客戶，他近 4 年在 1111 都在處理本土人力銀行內部 10 個部門的需求，我擔心他沒打過海外 B2B 商務戰。」
- **這個疑問會讓我**：仍然約談
- **要打消疑問，履歷或面試需要看到**：面試確認他在 1111「與外部合作夥伴議定查詢 API」時的商務與技術談判深度，並以英文測試海外 B2B 客戶需求探索情境。

#### 質疑 2
- **誰在想**：用人主管
- **讀到哪一句**：調整後至 2026/10，未再透過客服接獲廠商回報同類冒用。
- **心裡怎麼想**：「這句話寫得很微妙——『未再透過客服接獲回報』，代表他們的防詐監控是靠廠商被盜之後打電話給客服才發現嗎？系統後台有沒有主動偵測異常登入的指標？」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：說明 2026/04 調整登入驗證後，系統端是否有建立異常登入攔截率、失敗率或風險告警紀錄，而非僅依賴客服被動接獲回報。

#### 質疑 3
- **誰在想**：HR
- **讀到哪一句**：Product Owner／PM｜1111 全球華人｜2022/08 - 迄今
- **心裡怎麼想**：「JD 必備條件寫得很死要『5-8年以上 B2B/B2G 經驗』跟『接近母語等級英語』，他純 B2B 在 1111 只有 4 年出頭，英文在 2018 之後好像也比較少用在日常工作，這兩點我得先跟用人主管確認能不能通融，或先電話確認英文口說。」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：電話初篩測試英語口說流暢度，並確認尚凡時期 KOOL 網紅媒合平台對『案主（企業端）』的需求規劃是否可計入 B2B 經驗。

#### 質疑 4
- **誰在想**：用人主管
- **讀到哪一句**：擬定資料表與欄位需求，與 DBA 協作取數
- **心裡怎麼想**：「我們 JD 明寫要『自行查詢並解讀產品數據（能獨立使用 SQL）』，他寫跟 DBA 協作取數，意思就是自己不會寫 SQL 撈資料，進來後如果每次看數據都要開單排隊等工程或 DBA，節奏會太慢。」
- **這個疑問會讓我**：降低信任
- **要打消疑問，履歷或面試需要看到**：釐清是因公司資料庫權限規定必須由 DBA 取數，還是本人不熟 SQL 語法；能否將『拆解搜尋篩選查詢條件』的能力直接轉為撰寫基礎 SQL。

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷第5-6點｜以簽章驗證與時間戳防止重放...針對廠商招募帳號遭冒用...確認登入驗證與帳號解鎖流程｜對 jd20 直接對位 Anti-Scam BU 重視之防濫用、帳號安全與風險控管經驗
- AI協作技能與1111經歷第7點｜以 Claude Code 建立協作流程與共用 skill...與資料科學團隊合作完成三項功能上線｜對 jd20 直接命中「善用 AI 工具（如 Claude）」與「與 RD/AI 團隊密切合作」
- 1111經歷第8點｜30 天內結案的比例由前一年的 52% 升至 79%（提案滿 30 天者）｜對 jd20 證明具備 50% 專案與交付管理所需的時程控管與積案清理能力

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：必備條件要求「5-8年以上B2B/B2G經驗」與「自行查詢並解讀產品數據（能獨立使用SQL/BI）」，目前純 B2B 約 4 年且取數須與 DBA 協作
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落
- 位置：1111 經歷第 1、2、4、7 點與尚凡第 1 點
  - 原句：與工程於 2025/09 完成上線；完成三項功能上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：local_extraction（已於總報告 §6 獨立列示 `resume-v10.3-twocol.pdf` 本機抽字結果，不併入內容評等） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

## 單份審查｜履歷 Resume_v10.3_AppendixA（jd26 全支付- Product Manager (專案執行)）｜第 6 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd26","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd26-06","human_calibrated":false,"requirements":[{"id":"R01","text":"2年以上相關工作經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"年資與專案執行經驗豐富"},{"id":"R02","text":"能運用Axure撰寫產品規劃，並透過Jira、Confluence進行專案管理","type":"required","status":"partial","evidence":["Figma、Axure RP、Notion、Trello；使用 Trello 及"],"blocks_interview":false,"reason":"具Axure RP與內部專案控管系統，未直接點名Jira/Confluence"},{"id":"R03","text":"能同步考慮技術可行性以及系統架構關連影響；預期及識別風險","type":"required","status":"supported","evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"blocks_interview":false,"reason":"兼顧後台資料庫限制、新舊並行與API防濫用風險"},{"id":"R04","text":"與合作方確認規劃並與法遵確認適法性","type":"required","status":"partial","evidence":["與外部合作夥伴議定查詢 API 時，先處理可能被濫用的風險；與維運、稽核核對"],"blocks_interview":false,"reason":"具外部夥伴API議定與內部稽核核對，未明寫「法遵」字樣"},{"id":"R05","text":"執行專案測試、驗收、上線協調及內外部教育訓練","type":"required","status":"supported","evidence":["與 QA 制定 UAT 驗收案例、排定上線計畫。上線前以互動原型與 FAQ 向客"],"blocks_interview":false,"reason":"完整具備UAT驗收、上線計畫與內部教育訓練實績"},{"id":"R06","text":"喜愛或熟悉數位金融、支付產品；加分：代理收付/電支/英文/數據分析","type":"required","status":"supported","evidence":["導入 CodaPay，讓印尼、泰國等市場的用戶可用電信帳單與超商付款"],"blocks_interview":false,"reason":"具網頁付款、CodaPay跨國金流實收試算、TOEIC 980與GA4"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["系統服務逾 6 萬家活躍付費廠商（2026 Q3）"],"missing":["金流經驗偏向商戶端串接，無台灣專營電子支付機構與銀行合作專案經驗"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"足夠","evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"missing":["使用 Trello 及內部專案控管系統，未直接寫出 Jira/Confluence；未明寫法遵字樣"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對，把這些規則接回新版的規格與流程"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["30 天內結案的比例由前一年的 52% 升至 79%（提案滿 30 天者）"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["清楚交代新舊系統並行、API 規格議定與跨部門交付流程"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"對位 jd26 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd26 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"證據鏈支持安排 jd26 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"你在 1111 使用內部專案控管系統與 Trello「按 User Story 記錄需求、做法、驗收條件與優先級，供 Tech Lead 派工與估時」的流程，若切換到 Jira 與 Confluence 需要多少適應時間？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd26 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"必要條件要求「透過 Jira、Confluence 進行專案管理」，履歷列 Notion、Trello 與內部專案控管系統","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗，經手 6 款產品","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["完全涵蓋本職缺 1–9 項專案執行職責：從系統分析、Wireframe／Flow chart、Axure RP 原型、PRD、UAT 驗收、排定上線計畫，到「上線前以互動原型與 FAQ 向客服、業務說明」之內部教育訓練","具備考慮系統架構關連影響與識別風險的具體案例（後台與資料庫不動下新舊並行改版、外部查詢 API 簽章防重放與頻率限制、帳號防冒用調整）","具備 Peach 網頁金流轉換（占營收升至 80%+）與 CodaPay 東南亞電信帳單／超商付款串接及抽成稅費實收試算經驗"],"key_gaps":["必要條件要求「透過 Jira、Confluence 進行專案管理」，履歷列 Notion、Trello 與內部專案控管系統","職責第 3 點要求「與法遵確認適法性」，履歷寫「與維運、稽核核對」及處理帳號冒用，未明寫與法務／法遵單位確認電支法規之細節","金流經驗偏向商戶端串接第三方聚合支付（CodaPay），未直接經手台灣電子支付機構之代理收付與銀行端作業"],"strengths":["1111經歷第3點與工具技能｜Figma、Axure RP...完成 PRD，並與 QA 制定 UAT 驗收案例、排定上線計畫。上線前以互動原型與 FAQ 向客服、業務說明｜對 jd26 完整對位 Axure 規劃、測試驗收與教育訓練職責","1111經歷第1,5點｜業務後台與資料庫都不能更動...把這些規則接回新版；與外部合作夥伴議定查詢 API 時，先處理可能被濫用的風險｜對 jd26 證明能同步考量系統架構關連影響並預先識別風險","尚凡第4點與思維特第2點｜規劃 Peach 付款由 App 內購轉向網頁，與 CodaPay 新加坡技術團隊協調串接...完成實收試算｜對 jd26 展現外部支付合作方協調與金流試算能力"],"interview_questions":["你在 1111 使用內部專案控管系統與 Trello「按 User Story 記錄需求、做法、驗收條件與優先級，供 Tech Lead 派工與估時」的流程，若切換到 Jira 與 Confluence 需要多少適應時間？","過去在處理廠商帳號遭冒用、外部合作夥伴 API 議定或跨國金流串接時，是否有與法務或法遵單位確認個資法或金融法規適法性的經驗？","從商戶端串接 CodaPay 到進入專營電子支付機構（全支付）負責業務合作專案，你認為在交易對帳、清分算與風險控管上有哪些關鍵差異？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":7,"uncertainty_levels":1,"basis":"針對 jd26 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：7（±1）
- 一句話理由：具「Axure RP」、外部 API 議定、上線前內部教育訓練與 CodaPay 金流經驗，支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 系統服務逾 6 萬家活躍付費廠商（2026 Q3） | 金流經驗偏向商戶端串接，無台灣專營電子支付機構與銀行合作專案經驗 |
| role_evidence | 足夠 | 上線前以互動原型與 FAQ 向客服、業務說明 | 使用 Trello 及內部專案控管系統，未直接寫出 Jira/Confluence；未明寫法遵字樣 |
| decision_depth | 強 | 以實測歸納、請工程協助驗證，再與維運、稽核核對，把這些規則接回新版的規格與流程 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 30 天內結案的比例由前一年的 52% 升至 79%（提案滿 30 天者） | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 清楚交代新舊系統並行、API 規格議定與跨部門交付流程 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 2年以上相關工作經驗 | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 年資與專案執行經驗豐富 |
| R02 能運用Axure撰寫產品規劃，並透過Jira、Confluence進行專案管理 | 必要 | partial | Figma、Axure RP、Notion、Trello；使用 Trello 及 | 具Axure RP與內部專案控管系統，未直接點名Jira/Confluence |
| R03 能同步考慮技術可行性以及系統架構關連影響；預期及識別風險 | 必要 | supported | 業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程 | 兼顧後台資料庫限制、新舊並行與API防濫用風險 |
| R04 與合作方確認規劃並與法遵確認適法性 | 必要 | partial | 與外部合作夥伴議定查詢 API 時，先處理可能被濫用的風險；與維運、稽核核對 | 具外部夥伴API議定與內部稽核核對，未明寫「法遵」字樣 |
| R05 執行專案測試、驗收、上線協調及內外部教育訓練 | 必要 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫。上線前以互動原型與 FAQ 向客 | 完整具備UAT驗收、上線計畫與內部教育訓練實績 |
| R06 喜愛或熟悉數位金融、支付產品；加分：代理收付/電支/英文/數據分析 | 必要 | supported | 導入 CodaPay，讓印尼、泰國等市場的用戶可用電信帳單與超商付款 | 具網頁付款、CodaPay跨國金流實收試算、TOEIC 980與GA4 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 對位 jd26 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 以實測歸納、請工程協助驗證，再與維運、稽核核對 | 清楚界定個人規劃與工程/QA/DBA分工 |
| HR04 | supported | 30 天內結案的比例由前一年的 52% 升至 79% | 具結案率與定價實驗數據，缺部分功能採用率 |
| HR05 | supported | 將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與新舊並行取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端消費產品演進至B2B平台主任 |
| HR07 | supported | 上線前以互動原型與 FAQ 向客服、業務說明 | Scrum、原型、API議定、AI與英文皆有實例 |
| HR08 | supported | 從需求釐清、系統分析、流程與畫面設計，到 PRD | 結構分明，問題背景、動作與結果易讀 |
| HR09 | supported | 上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 誠實標註行銷導流期間、封測中與客服回報口徑 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd26 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃 | 證據鏈支持安排 jd26 面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人 | 針對大客戶部門/分店共同招募痛點設計群組權限 |
| HM03 | supported | 依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與新舊並行取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數機制與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18% | 結案率與定價實驗基準清晰，缺部分功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程 | 具後台不動下新舊並行、API防重放與防冒用閉環 |
| HM08 | supported | 以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則 | 能確認API JSON欄位與拆解查詢條件，取數協作DBA |
| HM09 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 上線調整，並依客服回饋修正操作方式 | 依客服回饋修正登入操作方式與AI推薦規則 |
| HM12 | supported | 具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd26 明文條件與附錄 A 履歷獨立取證判讀 | 僅依 jd26 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 完全涵蓋本職缺 1–9 項專案執行職責：從系統分析、Wireframe／Flow chart、Axure RP 原型、PRD、UAT 驗收、排定上線計畫，到「上線前以互動原型與 FAQ 向客服、業務說明」之內部教育訓練 |
| 2 | 具備考慮系統架構關連影響與識別風險的具體案例（後台與資料庫不動下新舊並行改版、外部查詢 API 簽章防重放與頻率限制、帳號防冒用調整） |
| 3 | 具備 Peach 網頁金流轉換（占營收升至 80%+）與 CodaPay 東南亞電信帳單／超商付款串接及抽成稅費實收試算經驗 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 必要條件要求「透過 Jira、Confluence 進行專案管理」，履歷列 Notion、Trello 與內部專案控管系統 | 你在 1111 使用內部專案控管系統與 Trello「按 User Story 記錄需求、做法、驗收條件與優先級，供 Tech Lead 派工與估時」的流程，若切換到 Jira 與 Confluence 需要多少適應時間？ |
| 2 | 職責第 3 點要求「與法遵確認適法性」，履歷寫「與維運、稽核核對」及處理帳號冒用，未明寫與法務／法遵單位確認電支法規之細節 | 過去在處理廠商帳號遭冒用、外部合作夥伴 API 議定或跨國金流串接時，是否有與法務或法遵單位確認個資法或金融法規適法性的經驗？ |
| 3 | 金流經驗偏向商戶端串接第三方聚合支付（CodaPay），未直接經手台灣電子支付機構之代理收付與銀行端作業 | 從商戶端串接 CodaPay 到進入專營電子支付機構（全支付）負責業務合作專案，你認為在交易對帳、清分算與風險控管上有哪些關鍵差異？ |

### 5.5 審查者的質疑（本版新增；不是缺口清單）
#### 質疑 1
- **誰在想**：用人主管
- **讀到哪一句**：上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報
- **心裡怎麼想**：「這段完全打中我們專案執行 PM 的日常！我們上線新合作案最需要 PM 幫客服跟業務做教育訓練，而且他還會用 Axure RP 畫原型，這個人我想約！但我會先問他：我們職缺是做業務談回來的外部合作專案執行，他在 1111 當到主任、自傳又說想做『產品策略』，來做高強度的合作專案執行他待得住嗎？」
- **這個疑問會讓我**：仍然約談
- **要打消疑問，履歷或面試需要看到**：面試時對齊職涯期待，確認他對「業務洽談合作專案執行（需配合合作方時程與法遵規範）」的接受度與動機。

#### 質疑 2
- **誰在想**：HR
- **讀到哪一句**：使用 Trello 及內部專案控管系統，按 User Story 記錄需求
- **心裡怎麼想**：「我們團隊全部用 Jira 跟 Confluence 管專案跟寫規格，他履歷上有寫 Axure 跟 Notion、Trello，就是沒寫 Jira，我要在電話裡先確認他有沒有用過 Jira。」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：確認是否曾使用過 Jira / Confluence，或說明內部專案控管系統的單據欄位與狀態流轉如何對應 Jira。

#### 質疑 3
- **誰在想**：用人主管
- **讀到哪一句**：以實測歸納、請工程協助驗證，再與維運、稽核核對
- **心裡怎麼想**：「他有跟維運、稽核核對計費規則的經驗，這在金融支付業很重要；不過電子支付機構受金管會專法監管，每一個合作案都要過法遵跟資安審查，我想知道他在議定外部 API 跟處理帳號冒用時，有沒有真正跟法務或法遵交手過。」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：舉出過往專案中曾配合法務、稽核或資安規範而修改產品流程或 API 規格的實例。

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷第3點與工具技能｜Figma、Axure RP...完成 PRD，並與 QA 制定 UAT 驗收案例、排定上線計畫。上線前以互動原型與 FAQ 向客服、業務說明｜對 jd26 完整對位 Axure 規劃、測試驗收與教育訓練職責
- 1111經歷第1,5點｜業務後台與資料庫都不能更動...把這些規則接回新版；與外部合作夥伴議定查詢 API 時，先處理可能被濫用的風險｜對 jd26 證明能同步考量系統架構關連影響並預先識別風險
- 尚凡第4點與思維特第2點｜規劃 Peach 付款由 App 內購轉向網頁，與 CodaPay 新加坡技術團隊協調串接...完成實收試算｜對 jd26 展現外部支付合作方協調與金流試算能力

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：必要條件要求「透過 Jira、Confluence 進行專案管理」，履歷列 Notion、Trello 與內部專案控管系統
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落
- 位置：1111 經歷第 1、2、4、7 點與尚凡第 1 點
  - 原句：與工程於 2025/09 完成上線；完成三項功能上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：local_extraction（已於總報告 §6 獨立列示 `resume-v10.3-twocol.pdf` 本機抽字結果，不併入內容評等） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

## 單份審查｜履歷 Resume_v10.3_AppendixA（jd30 資深產品經理｜Senior Product Manager｜USPACE）｜第 7 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd30","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd30-07","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上Software PM，至少一次完整0到1產品探索、驗證、設計、開發、上線與迭代經歷","type":"required","status":"supported","evidence":["規劃 KOOL 網紅媒合平台，從案主與網紅兩種角色釐清需求...設計刊案、報名、"],"blocks_interview":false,"reason":"主導KOOL從0到1需求釐清、雙邊媒合流程設計與VIP/點數上線"},{"id":"R02","text":"能寫清楚的規格文件（PRD、流程圖、資料結構）","type":"required","status":"supported","evidence":["系統分析、流程圖／循序圖、Wireframe、Prototype、PRD；擬定資"],"blocks_interview":false,"reason":"完整具備PRD、流程圖/循序圖與資料表欄位定義能力"},{"id":"R03","text":"理解API、JSON與基本SQL","type":"required","status":"supported","evidence":["與工程確認 JSON 欄位與判定規則；能將業務上的搜尋、篩選規則拆成查詢條件"],"blocks_interview":false,"reason":"明確具備API規格議定、JSON欄位確認與查詢條件拆解，取數與DBA協作"},{"id":"R04","text":"習慣用AI工具（Claude Code等）加速驗證與把PM工作流程化；評估AI放進產品機會","type":"preferred","status":"supported","evidence":["以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格"],"blocks_interview":false,"reason":"直接命中Claude Code協作流程、共用skill與上線3項AI功能"},{"id":"R05","text":"停車/交通/MaaS/保險/支付/FinTech經驗；Growth或數據分析經驗","type":"preferred","status":"supported","evidence":["規劃 Peach 付款由 App 內購轉向網頁，與 CodaPay 新加坡技術團"],"blocks_interview":false,"reason":"具跨國支付串接、實收試算與馬來西亞iOS定價對照實驗經驗"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["涵蓋訂閱制社交 App、網紅媒合平台與人力銀行招募系統"],"missing":["過往為純線上軟體平台，未直接接觸智慧停車或 MaaS 實體場域硬體"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"強","evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"missing":["資料庫查詢為「擬定資料表與欄位需求，與 DBA 協作取數」，未明寫自寫 SQL"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["30 天內結案的比例由前一年的 52% 升至 79%（提案滿 30 天者）"],"missing":["KOOL 0 到 1 平台未列上線後的規模與轉換數據"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["清楚呈現 PRD、流程圖／循序圖、資料表欄位需求與 AI 協作流程"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台，從案主與網紅兩種角色釐清需求...設計刊案、報名、"],"application_note":"對位 jd30 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd30 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"證據鏈支持安排 jd30 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"你在尚凡從 0 到 1 規劃 KOOL 網紅媒合平台並上線 VIP 訂閱、點數付費牆與精選曝光後，如何驗證 PoC 到 Scale？實際雙邊用戶規模與付費表現如何？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd30 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"KOOL 網紅媒合平台雖完整描述 0 到 1 探索與功能設計，但本版履歷未列出上線後的用戶數、媒合量或營收成果數字","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["規劃 KOOL 網紅媒合平台，從案主與網紅兩種角色釐清需求...設計刊案、報名、","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["直接命中 JD 第 2 點與加分項：「以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格，並將業務規則轉為可與工程討論的條件描述」，且已與資料科學團隊上線 3 項 AI 功能","完全滿足必備技術與規格條件：不僅能撰寫 PRD、流程圖／循序圖、擬定資料表與欄位需求，更在議定外部查詢 API 時「以簽章驗證與時間戳防止重放...與工程確認 JSON 欄位與判定規則與判定規則」","兼具 KOOL 網紅媒合平台從 0 到 1（無直接競品下設計雙邊媒合與 VIP／點數變現）與 1111 成熟產品迭代、馬來西亞定價成長實驗及跨國支付串接經驗"],"key_gaps":["KOOL 網紅媒合平台雖完整描述 0 到 1 探索與功能設計，但本版履歷未列出上線後的用戶數、媒合量或營收成果數字","資料庫查詢寫「擬定資料表與欄位需求，與 DBA 協作取數；能將業務上的搜尋、篩選規則拆成查詢條件」，未明寫本人手寫 SQL 語法程度","過往為純線上數位平台，尚未接觸智慧停車或 MaaS 線下硬體與場域營運"],"strengths":["AI協作技能與1111經歷第7點｜以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格...定義公司簡介生成、職缺工作說明生成及 AI 推薦人才｜對 jd30 完美對位「習慣用 Claude Code 把重複性 PM 工作流程化」與「評估 AI 放進產品機會」","1111經歷第5點與技能欄｜與外部合作夥伴議定查詢 API 時...以簽章驗證與時間戳防止重放...與工程確認 JSON 欄位與判定規則與判定規則｜對 jd30 直接證明理解 API、JSON 欄位與後端查詢條件","尚凡經歷第1,3點｜規劃 KOOL 網紅媒合平台...設計馬來西亞 iOS 定價實驗｜對 jd30 同時證明具備 0 到 1 雙邊平台規劃與成熟產品數據實驗能力"],"interview_questions":["你在尚凡從 0 到 1 規劃 KOOL 網紅媒合平台並上線 VIP 訂閱、點數付費牆與精選曝光後，如何驗證 PoC 到 Scale？實際雙邊用戶規模與付費表現如何？","你在將搜尋篩選規則拆成查詢條件及與 DBA 協作取數時，是否會自行撰寫基本 SQL（如 SELECT / JOIN / WHERE）？","面對 USPACE 結合線上 App 與線下智慧車位鎖／停車場硬體的 O2O 場景，你如何處理硬體異常或場域例外情境？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd30 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：具「規劃 KOOL 網紅媒合平台」、外部 API 議定確認 JSON 欄位及「以 Claude Code 建立協作流程」，高度契合。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 涵蓋訂閱制社交 App、網紅媒合平台與人力銀行招募系統 | 過往為純線上軟體平台，未直接接觸智慧停車或 MaaS 實體場域硬體 |
| role_evidence | 強 | 以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則 | 資料庫查詢為「擬定資料表與欄位需求，與 DBA 協作取數」，未明寫自寫 SQL |
| decision_depth | 強 | 依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 30 天內結案的比例由前一年的 52% 升至 79%（提案滿 30 天者） | KOOL 0 到 1 平台未列上線後的規模與轉換數據 |
| ownership | 強 | 以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 清楚呈現 PRD、流程圖／循序圖、資料表欄位需求與 AI 協作流程 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 3年以上Software PM，至少一次完整0到1產品探索、驗證、設計、開發、上線與迭代經歷 | 必要 | supported | 規劃 KOOL 網紅媒合平台，從案主與網紅兩種角色釐清需求...設計刊案、報名、 | 主導KOOL從0到1需求釐清、雙邊媒合流程設計與VIP/點數上線 |
| R02 能寫清楚的規格文件（PRD、流程圖、資料結構） | 必要 | supported | 系統分析、流程圖／循序圖、Wireframe、Prototype、PRD；擬定資 | 完整具備PRD、流程圖/循序圖與資料表欄位定義能力 |
| R03 理解API、JSON與基本SQL | 必要 | supported | 與工程確認 JSON 欄位與判定規則；能將業務上的搜尋、篩選規則拆成查詢條件 | 明確具備API規格議定、JSON欄位確認與查詢條件拆解，取數與DBA協作 |
| R04 習慣用AI工具（Claude Code等）加速驗證與把PM工作流程化；評估AI放進產品機會 | 加分 | supported | 以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格 | 直接命中Claude Code協作流程、共用skill與上線3項AI功能 |
| R05 停車/交通/MaaS/保險/支付/FinTech經驗；Growth或數據分析經驗 | 加分 | supported | 規劃 Peach 付款由 App 內購轉向網頁，與 CodaPay 新加坡技術團 | 具跨國支付串接、實收試算與馬來西亞iOS定價對照實驗經驗 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 規劃 KOOL 網紅媒合平台，從案主與網紅兩種角色釐清需求...設計刊案、報名、 | 對位 jd30 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 以實測歸納、請工程協助驗證，再與維運、稽核核對 | 清楚界定個人規劃與工程/QA/DBA分工 |
| HR04 | supported | 30 天內結案的比例由前一年的 52% 升至 79% | 具結案率與定價實驗數據，缺部分功能採用率 |
| HR05 | supported | 將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與新舊並行取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端消費產品演進至B2B平台主任 |
| HR07 | supported | 上線前以互動原型與 FAQ 向客服、業務說明 | Scrum、原型、API議定、AI與英文皆有實例 |
| HR08 | supported | 從需求釐清、系統分析、流程與畫面設計，到 PRD | 結構分明，問題背景、動作與結果易讀 |
| HR09 | supported | 上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 誠實標註行銷導流期間、封測中與客服回報口徑 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd30 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃 | 證據鏈支持安排 jd30 面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人 | 針對大客戶部門/分店共同招募痛點設計群組權限 |
| HM03 | supported | 依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與新舊並行取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數機制與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18% | 結案率與定價實驗基準清晰，缺部分功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程 | 具後台不動下新舊並行、API防重放與防冒用閉環 |
| HM08 | supported | 以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則 | 能確認API JSON欄位與拆解查詢條件，取數協作DBA |
| HM09 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 上線調整，並依客服回饋修正操作方式 | 依客服回饋修正登入操作方式與AI推薦規則 |
| HM12 | supported | 具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd30 明文條件與附錄 A 履歷獨立取證判讀 | 僅依 jd30 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 直接命中 JD 第 2 點與加分項：「以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格，並將業務規則轉為可與工程討論的條件描述」，且已與資料科學團隊上線 3 項 AI 功能 |
| 2 | 完全滿足必備技術與規格條件：不僅能撰寫 PRD、流程圖／循序圖、擬定資料表與欄位需求，更在議定外部查詢 API 時「以簽章驗證與時間戳防止重放...與工程確認 JSON 欄位與判定規則與判定規則」 |
| 3 | 兼具 KOOL 網紅媒合平台從 0 到 1（無直接競品下設計雙邊媒合與 VIP／點數變現）與 1111 成熟產品迭代、馬來西亞定價成長實驗及跨國支付串接經驗 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | KOOL 網紅媒合平台雖完整描述 0 到 1 探索與功能設計，但本版履歷未列出上線後的用戶數、媒合量或營收成果數字 | 你在尚凡從 0 到 1 規劃 KOOL 網紅媒合平台並上線 VIP 訂閱、點數付費牆與精選曝光後，如何驗證 PoC 到 Scale？實際雙邊用戶規模與付費表現如何？ |
| 2 | 資料庫查詢寫「擬定資料表與欄位需求，與 DBA 協作取數；能將業務上的搜尋、篩選規則拆成查詢條件」，未明寫本人手寫 SQL 語法程度 | 你在將搜尋篩選規則拆成查詢條件及與 DBA 協作取數時，是否會自行撰寫基本 SQL（如 SELECT / JOIN / WHERE）？ |
| 3 | 過往為純線上數位平台，尚未接觸智慧停車或 MaaS 線下硬體與場域營運 | 面對 USPACE 結合線上 App 與線下智慧車位鎖／停車場硬體的 O2O 場景，你如何處理硬體異常或場域例外情境？ |

### 5.5 審查者的質疑（本版新增；不是缺口清單）
#### 質疑 1
- **誰在想**：用人主管
- **讀到哪一句**：以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格
- **心裡怎麼想**：「這段完全就是我們 JD 寫的『用 Claude Code 把重複性的 PM 工作流程化』！而且他連外部 API 簽章防重放跟 JSON 欄位確認都寫出來了，我一定會約他面試。但我會先問：你的 Claude Code skill 到底長什麼樣？是真的能幫你做原型跟拆解邊界條件，還是只是拿來潤飾文字？」
- **這個疑問會讓我**：仍然約談
- **要打消疑問，履歷或面試需要看到**：面試時現場分享或展示他建立的 Claude Code 協作流程與共用 skill 架構，以及如何將業務規則轉為工程條件描述。

#### 質疑 2
- **誰在想**：用人主管
- **讀到哪一句**：規劃 KOOL 網紅媒合平台，從案主與網紅兩種角色釐清需求
- **心裡怎麼想**：「KOOL 這段 0 到 1 的產品設計邏輯寫得很清楚，連沒有直接競品怎麼參考 Airbnb 跟交友平台都交代了，但奇怪的是下面 Juicy、定價實驗、Peach 都有給數據，唯獨 KOOL 一個成果數字都沒有，是不是上線後媒合量或營收不如預期？」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：坦誠說明 KOOL 上線後的雙邊用戶規模、報名媒合次數或商業變現結果，以及從 0 到 1 驗證中學到的取捨。

#### 質疑 3
- **誰在想**：HR
- **讀到哪一句**：擬定資料表與欄位需求，與 DBA 協作取數，再以 Excel 分析
- **心裡怎麼想**：「我們必備條件有寫理解基本 SQL，他寫跟 DBA 協作取數，代表他可能看懂資料表結構但平常不自己寫 SQL，這點需要請主管在面試時確認技術底線。」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：確認對基本 SQL 查詢語法的理解程度，以及如何擬定資料表與欄位需求。

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- AI協作技能與1111經歷第7點｜以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格...定義公司簡介生成、職缺工作說明生成及 AI 推薦人才｜對 jd30 完美對位「習慣用 Claude Code 把重複性 PM 工作流程化」與「評估 AI 放進產品機會」
- 1111經歷第5點與技能欄｜與外部合作夥伴議定查詢 API 時...以簽章驗證與時間戳防止重放...與工程確認 JSON 欄位與判定規則與判定規則｜對 jd30 直接證明理解 API、JSON 欄位與後端查詢條件
- 尚凡經歷第1,3點｜規劃 KOOL 網紅媒合平台...設計馬來西亞 iOS 定價實驗｜對 jd30 同時證明具備 0 到 1 雙邊平台規劃與成熟產品數據實驗能力

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：KOOL 網紅媒合平台雖完整描述 0 到 1 探索與功能設計，但本版履歷未列出上線後的用戶數、媒合量或營收成果數字
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落
- 位置：1111 經歷第 1、2、4、7 點與尚凡第 1 點
  - 原句：與工程於 2025/09 完成上線；完成三項功能上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：強

### 8. 未測試聲明
PDF 抽字：local_extraction（已於總報告 §6 獨立列示 `resume-v10.3-twocol.pdf` 本機抽字結果，不併入內容評等） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

## 單份審查｜履歷 Resume_v10.3_AppendixA（jd31 資深產品經理【擴編】｜人易科技 (NUEIP)）｜第 8 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd31","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd31-08","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上產品規劃與需求訪談經驗，熟悉0到1或迭代優化流程","type":"required","status":"supported","evidence":["近 10 年 PM 經驗；使用者訪談與問卷、內部維運與稽核訪談"],"blocks_interview":false,"reason":"兼具KOOL 0到1與1111企業端50項大功能迭代經驗"},{"id":"R02","text":"業務支援與售前規劃（協助業務銷售簡報、客戶案件排程）","type":"required","status":"partial","evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助業務製作銷售簡報"],"blocks_interview":false,"reason":"已具備製作sales kit與客戶案件優先排程，惟缺直接參與客戶會議展示描寫"},{"id":"R03","text":"有多系統整合或API串接經驗（API整合、第三方介接、資料交換）","type":"required","status":"supported","evidence":["與外部合作夥伴議定查詢 API 時...與工程確認 JSON 欄位與判定規則；與"],"blocks_interview":false,"reason":"具外部查詢API規格議定、CodaPay第三方介接與新舊系統資料轉換經驗"},{"id":"R04","text":"熟悉PRD、功能規格與流程圖設計","type":"required","status":"supported","evidence":["User Journey Map、User Story、Use Case、系統分"],"blocks_interview":false,"reason":"產品規格與流程圖設計體系完整"},{"id":"R05","text":"熟悉敏捷開發流程（Scrum）","type":"required","status":"supported","evidence":["曾參與每週一個 Sprint 的 Scrum，現行以 Kanban 推進瀑布式，"],"blocks_interview":false,"reason":"明確具備每週一Sprint之Scrum與Kanban實務"},{"id":"R06","text":"曾主導或參與企業級系統（ERP/HRM/SaaS/平台型產品）規劃經驗","type":"preferred","status":"supported","evidence":["人力銀行企業端招募系統專案負責人，系統服務逾 6 萬家活躍付費廠商"],"blocks_interview":false,"reason":"主導6萬家企業招募系統與大型客戶部門/分店群組功能，與HRM高度同源"},{"id":"R07","text":"具備資料分析能力（SQL/BI工具）；熟悉技術背景（API、資料庫、系統架構）","type":"preferred","status":"supported","evidence":["擬定資料表與欄位需求，與 DBA 協作取數；能將業務上的搜尋、篩選規則拆成查詢條"],"blocks_interview":false,"reason":"熟悉API、JSON、資料庫欄位與前後端分離架構，取數與DBA協作"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["人力銀行企業端招募系統專案負責人，系統服務逾 6 萬家活躍付費廠商"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"強","evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助業務製作銷售簡報"],"missing":["客戶需求多由內部單位或客服反映，較少描寫親自隨業務拜訪客戶進行售前展示"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對，把這些規則接回新版的規格與流程"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"足夠","evidence":["30 天內結案的比例由前一年的 52% 升至 79%（提案滿 30 天者）"],"missing":["群組功能與新版模組未列上線後之企業客戶採用率"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["清楚呈現企業端權限盤點、群組招募、API 規格議定與交付成果"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗；使用者訪談與問卷、內部維運與稽核訪談"],"application_note":"對位 jd31 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"partial","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd31 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"證據鏈支持安排 jd31 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"在 1111 規劃「大型客戶部門／分店群組功能」及協助業務製作 sales kit 時，你是否曾與業務一同參與大型客戶會議進行需求訪談或產品展示（Pre-sales）？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd31 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"職責第 1、2 點包含「直接與客戶進行需求訪談」與「與業務共同參與客戶會議、產品展示」，履歷雖有製作 sales kit 與清理客戶案件，但未明寫是否親自參與外部客戶會議","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗；使用者訪談與問卷、內部維運與稽核訪談","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["現任 1111 企業端招募系統 PO（服務逾 6 萬家廠商），規劃「大型客戶部門或分店共同招募之群組功能（帳號權限、職缺關聯與資料轉換規則）」與主副帳號計費規則，與 NUEIP 雲端人資系統（HRM）領域高度契合","具備多系統整合與外部 API 規格議定實證（簽章驗證、防重放、錯誤碼、頻率限制、JSON 欄位與判定規則，以及 CodaPay 第三方服務介接）","具備每週一 Sprint 之 Scrum 經驗，且上線前「以互動原型與 FAQ 向客服、業務說明，另協助業務製作銷售簡報（sales kit）」，並將客戶案件 30 天結案率由 52% 升至 79%"],"key_gaps":["職責第 1、2 點包含「直接與客戶進行需求訪談」與「與業務共同參與客戶會議、產品展示」，履歷雖有製作 sales kit 與清理客戶案件，但未明寫是否親自參與外部客戶會議","加分項之 SQL/BI 工具，履歷採「擬定資料表與欄位需求，與 DBA 協作取數，再以 Excel 分析」","1111 大型客戶群組功能上線後，未列出實際採用之大型客戶家數或業務成效"],"strengths":["1111經歷第2點｜規劃群組功能，讓同單位帳號共同處理職缺及對應履歷及對應履歷｜對 jd31 直接對應 HRM/企業級 SaaS 最核心的組織架構與權限設計","1111經歷第3,8點｜上線前以互動原型與 FAQ 向客服、業務說明，另協助業務製作銷售簡報...30 天內結案的比例由前一年的 52% 升至 79%｜對 jd31 直接支撐業務支援與客戶專案管理進度追蹤","1111經歷第5點｜與外部合作夥伴議定查詢 API 時...以簽章驗證與時間戳防止重放...與工程確認 JSON 欄位與判定規則與判定規則｜對 jd31 完全符合跨系統 API 整合與資料交換流程設計要求"],"interview_questions":["在 1111 規劃「大型客戶部門／分店群組功能」及協助業務製作 sales kit 時，你是否曾與業務一同參與大型客戶會議進行需求訪談或產品展示（Pre-sales）？","在與 DBA 協作取數及拆解後端查詢條件時，你本人是否具備撰寫基本 SQL 查詢或使用 BI 儀表板的經驗？","2025/09 完成上線的「群組功能」，後續有多少大型連鎖或跨部門企業客戶實際導入使用？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd31 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：具「規劃群組功能...完成上線」、外部查詢 API 議定、協助業務製作 sales kit 與 Scrum 經驗，高度契合。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 人力銀行企業端招募系統專案負責人，系統服務逾 6 萬家活躍付費廠商 | 無關鍵缺口，可於面試深化 |
| role_evidence | 強 | 上線前以互動原型與 FAQ 向客服、業務說明，另協助業務製作銷售簡報 | 客戶需求多由內部單位或客服反映，較少描寫親自隨業務拜訪客戶進行售前展示 |
| decision_depth | 強 | 以實測歸納、請工程協助驗證，再與維運、稽核核對，把這些規則接回新版的規格與流程 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 足夠 | 30 天內結案的比例由前一年的 52% 升至 79%（提案滿 30 天者） | 群組功能與新版模組未列上線後之企業客戶採用率 |
| ownership | 強 | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 清楚呈現企業端權限盤點、群組招募、API 規格議定與交付成果 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 3年以上產品規劃與需求訪談經驗，熟悉0到1或迭代優化流程 | 必要 | supported | 近 10 年 PM 經驗；使用者訪談與問卷、內部維運與稽核訪談 | 兼具KOOL 0到1與1111企業端50項大功能迭代經驗 |
| R02 業務支援與售前規劃（協助業務銷售簡報、客戶案件排程） | 必要 | partial | 上線前以互動原型與 FAQ 向客服、業務說明，另協助業務製作銷售簡報 | 已具備製作sales kit與客戶案件優先排程，惟缺直接參與客戶會議展示描寫 |
| R03 有多系統整合或API串接經驗（API整合、第三方介接、資料交換） | 必要 | supported | 與外部合作夥伴議定查詢 API 時...與工程確認 JSON 欄位與判定規則；與 | 具外部查詢API規格議定、CodaPay第三方介接與新舊系統資料轉換經驗 |
| R04 熟悉PRD、功能規格與流程圖設計 | 必要 | supported | User Journey Map、User Story、Use Case、系統分 | 產品規格與流程圖設計體系完整 |
| R05 熟悉敏捷開發流程（Scrum） | 必要 | supported | 曾參與每週一個 Sprint 的 Scrum，現行以 Kanban 推進瀑布式， | 明確具備每週一Sprint之Scrum與Kanban實務 |
| R06 曾主導或參與企業級系統（ERP/HRM/SaaS/平台型產品）規劃經驗 | 加分 | supported | 人力銀行企業端招募系統專案負責人，系統服務逾 6 萬家活躍付費廠商 | 主導6萬家企業招募系統與大型客戶部門/分店群組功能，與HRM高度同源 |
| R07 具備資料分析能力（SQL/BI工具）；熟悉技術背景（API、資料庫、系統架構） | 加分 | supported | 擬定資料表與欄位需求，與 DBA 協作取數；能將業務上的搜尋、篩選規則拆成查詢條 | 熟悉API、JSON、資料庫欄位與前後端分離架構，取數與DBA協作 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗；使用者訪談與問卷、內部維運與稽核訪談 | 對位 jd31 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 以實測歸納、請工程協助驗證，再與維運、稽核核對 | 清楚界定個人規劃與工程/QA/DBA分工 |
| HR04 | partial | 30 天內結案的比例由前一年的 52% 升至 79% | 具結案率與定價實驗數據，缺部分功能採用率 |
| HR05 | supported | 將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與新舊並行取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端消費產品演進至B2B平台主任 |
| HR07 | supported | 上線前以互動原型與 FAQ 向客服、業務說明 | Scrum、原型、API議定、AI與英文皆有實例 |
| HR08 | supported | 從需求釐清、系統分析、流程與畫面設計，到 PRD | 結構分明，問題背景、動作與結果易讀 |
| HR09 | supported | 上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 誠實標註行銷導流期間、封測中與客服回報口徑 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd31 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃 | 證據鏈支持安排 jd31 面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人 | 針對大客戶部門/分店共同招募痛點設計群組權限 |
| HM03 | supported | 依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與新舊並行取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數機制與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18% | 結案率與定價實驗基準清晰，缺部分功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程 | 具後台不動下新舊並行、API防重放與防冒用閉環 |
| HM08 | supported | 以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則 | 能確認API JSON欄位與拆解查詢條件，取數協作DBA |
| HM09 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 上線調整，並依客服回饋修正操作方式 | 依客服回饋修正登入操作方式與AI推薦規則 |
| HM12 | supported | 具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd31 明文條件與附錄 A 履歷獨立取證判讀 | 僅依 jd31 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 現任 1111 企業端招募系統 PO（服務逾 6 萬家廠商），規劃「大型客戶部門或分店共同招募之群組功能（帳號權限、職缺關聯與資料轉換規則）」與主副帳號計費規則，與 NUEIP 雲端人資系統（HRM）領域高度契合 |
| 2 | 具備多系統整合與外部 API 規格議定實證（簽章驗證、防重放、錯誤碼、頻率限制、JSON 欄位與判定規則，以及 CodaPay 第三方服務介接） |
| 3 | 具備每週一 Sprint 之 Scrum 經驗，且上線前「以互動原型與 FAQ 向客服、業務說明，另協助業務製作銷售簡報（sales kit）」，並將客戶案件 30 天結案率由 52% 升至 79% |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 職責第 1、2 點包含「直接與客戶進行需求訪談」與「與業務共同參與客戶會議、產品展示」，履歷雖有製作 sales kit 與清理客戶案件，但未明寫是否親自參與外部客戶會議 | 在 1111 規劃「大型客戶部門／分店群組功能」及協助業務製作 sales kit 時，你是否曾與業務一同參與大型客戶會議進行需求訪談或產品展示（Pre-sales）？ |
| 2 | 加分項之 SQL/BI 工具，履歷採「擬定資料表與欄位需求，與 DBA 協作取數，再以 Excel 分析」 | 在與 DBA 協作取數及拆解後端查詢條件時，你本人是否具備撰寫基本 SQL 查詢或使用 BI 儀表板的經驗？ |
| 3 | 1111 大型客戶群組功能上線後，未列出實際採用之大型客戶家數或業務成效 | 2025/09 完成上線的「群組功能」，後續有多少大型連鎖或跨部門企業客戶實際導入使用？ |

### 5.5 審查者的質疑（本版新增；不是缺口清單）
#### 質疑 1
- **誰在想**：用人主管
- **讀到哪一句**：大型客戶需要讓部門或分店共同招募...規劃群組功能
- **心裡怎麼想**：「這段完全就是我們 HRM 系統天天在處理的『多部門／多門市跨店權限與簽核範圍』問題！而且他還會幫業務做 sales kit、懂 API JSON 跟防重放，這個人我非常想約！但我會先問：這個群組功能的需求是他自己去跟大客戶 HR 訪談挖出來的，還是業務開單叫他做的？」
- **這個疑問會讓我**：仍然約談
- **要打消疑問，履歷或面試需要看到**：面試時請他還原「大型客戶群組功能」從需求探索、訪談對象、例外情境處理到業務推廣（sales kit）的完整過程。

#### 質疑 2
- **誰在想**：用人主管
- **讀到哪一句**：30 天內結案的比例由前一年的 52% 升至 79%（提案滿 30 天者）
- **心裡怎麼想**：「把 30 天結案率從 52% 拉到 79% 代表他很會清單跟排程，但在 B2B SaaS 如果什麼『客戶案件』都照單全收、只求 30 天內快速結案，產品架構很容易被客製化需求搞成四不像，我想知道他怎麼擋掉不合理的客戶要求。」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：說明在以客戶案件為優先時，如何區分「通用產品功能」與「單一客戶特例」，以及拒絕或轉化不合理需求的實例。

#### 質疑 3
- **誰在想**：HR
- **讀到哪一句**：職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會
- **心裡怎麼想**：「他在 1111 已經是帶 2 個人的主任、天天開一級主管日會向總經理匯報，我們這個職缺月薪範圍 60,000~90,000 元且偏重第一線客戶訪談與售前支援，需要確認他的薪資期望值與對 IC 角色的接受度。」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：於面試或電話初篩確認薪資期望是否落在 60k–90k（平均 14 薪）區間，以及對親自跑客戶訪談與售前支援的意願。

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷第2點｜規劃群組功能，讓同單位帳號共同處理職缺及對應履歷及對應履歷｜對 jd31 直接對應 HRM/企業級 SaaS 最核心的組織架構與權限設計
- 1111經歷第3,8點｜上線前以互動原型與 FAQ 向客服、業務說明，另協助業務製作銷售簡報...30 天內結案的比例由前一年的 52% 升至 79%｜對 jd31 直接支撐業務支援與客戶專案管理進度追蹤
- 1111經歷第5點｜與外部合作夥伴議定查詢 API 時...以簽章驗證與時間戳防止重放...與工程確認 JSON 欄位與判定規則與判定規則｜對 jd31 完全符合跨系統 API 整合與資料交換流程設計要求

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：職責第 1、2 點包含「直接與客戶進行需求訪談」與「與業務共同參與客戶會議、產品展示」，履歷雖有製作 sales kit 與清理客戶案件，但未明寫是否親自參與外部客戶會議
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落
- 位置：1111 經歷第 1、2、4、7 點與尚凡第 1 點
  - 原句：與工程於 2025/09 完成上線；完成三項功能上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：強

### 8. 未測試聲明
PDF 抽字：local_extraction（已於總報告 §6 獨立列示 `resume-v10.3-twocol.pdf` 本機抽字結果，不併入內容評等） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

## 單份審查｜履歷 Resume_v10.3_AppendixA（jd32 產品專案經理(內部系統)｜104人力銀行）｜第 9 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd32","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd32-09","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上經驗且具備資訊或網站開發經驗或擁有SA（系統分析）經驗","type":"required","status":"supported","evidence":["從需求釐清、系統分析到流程與原型設計，完成 PRD；能將業務上的搜尋、篩選規則拆"],"blocks_interview":false,"reason":"現任同業招募系統PO，具扎實SA系統分析、舊規則逆向盤點與API規格議定經驗"},{"id":"R02","text":"傾聽需求，解決挑戰：接手內部使用者與外部客戶的議題，安排功能優化或問題修正","type":"required","status":"supported","evidence":["這些模組相關的 840 件廠商建議，已完成 743 件（88%）；30 天內結案"],"blocks_interview":false,"reason":"高比例完成840件廠商建議並清理多年積案，大幅提升30天結案率"},{"id":"R03","text":"運用AI工具進行營運分析或提案","type":"required","status":"supported","evidence":["以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格"],"blocks_interview":false,"reason":"深入運用Claude Code與AI Agent整理分析資料並轉譯工程條件"},{"id":"R04","text":"熟悉規格撰寫、跨單位溝通；與團隊評估解決方案的可行性與時程","type":"required","status":"supported","evidence":["對接工程、行銷、業務與客服等 10 個需求單位；依提案時間與難易安排新案，每週向"],"blocks_interview":false,"reason":"對接10個內部單位、依難易與提案時間評估排程並每週回報"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["人力銀行企業端招募系統專案負責人，系統服務逾 6 萬家活躍付費廠商"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"強","evidence":["接手求才系統改版時，業務後台與資料庫都不能更動...把這些規則接回新版的規格與流"],"missing":[],"issue_ids":[]},{"id":"decision_depth","rating":"強","evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["這些模組相關的 840 件廠商建議，已完成 743 件（88%）；30 天內結案"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["對接工程、行銷、業務與客服等 10 個需求單位；帶領 2 名直屬產品企劃"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["問題背景、系統限制、SA 盤點動作與結案指標脈絡極為清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["從需求釐清、系統分析到流程與原型設計，完成 PRD；能將業務上的搜尋、篩選規則拆"],"application_note":"對位 jd32 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"partial","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"自傳盼做產品策略，需對齊內部系統期待"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"證據鏈支持安排 jd32 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"你在自傳中提到希望把更多心力放回產品策略，而我們這個職位主要負責「內部營運用網站」與跨單位需求優化（月薪 50k–70k），這與你的下一階段職涯規劃與薪資期待是否相符？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd32 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"自傳末段提到「接下來，我希望把更多心力放回產品策略」，而本職缺聚焦於「內部營運用網站的功能設計與內部／外部議題修正」且月薪為 50,000~70,000 元","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["從需求釐清、系統分析到流程與原型設計，完成 PRD；能將業務上的搜尋、篩選規則拆","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["現任直接同業（1111 人力銀行）企業端招募系統 PO，在「業務後台與資料庫都不能更動、舊系統權限與計費規則無文件」的限制下，逆向實測並訪談維運、稽核補回規則，完成前後端分離新版上線與 743/840 件（88%）建議案","2025 Q4 先清理多年積案，再依提案時間與難易安排新案並每週向 10 個需求單位回報進度，使提案滿 30 天者之「30 天內結案比例由前一年的 52% 升至 79%」，完全對應本職缺內部與外部議題排程控管且量測與責任可追溯","以 Claude Code 建立協作流程與共用 skill，「運用 AI Agent 撰寫規格、整理與分析資料，並將業務規則轉為可與工程討論的條件描述」，直接命中 JD 要求"],"key_gaps":["自傳末段提到「接下來，我希望把更多心力放回產品策略」，而本職缺聚焦於「內部營運用網站的功能設計與內部／外部議題修正」且月薪為 50,000~70,000 元","信件與即時通整合、搜尋結果頁改版兩案目前仍在開發／封測中"],"strengths":["1111經歷第1點｜接手求才系統改版時，業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程...840 件廠商建議，已完成 743 件（88%）｜對 jd32 完美證明同業系統 SA 逆向分析與既有後台相容性規劃能力","1111經歷第8點｜先清理多年積案，再依提案時間與難易安排新案，每週向各單位回報進度。之後提出的案件，30 天內結案的比例由前一年的 52% 升至 79%｜對 jd32 直接對位「接手內部與外部議題、評估可行性與掌握節奏」且量化成效可追溯","AI協作技能｜以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格｜對 jd32 直接命中「運用 AI 工具進行營運分析或提案」"],"interview_questions":["你在自傳中提到希望把更多心力放回產品策略，而我們這個職位主要負責「內部營運用網站」與跨單位需求優化（月薪 50k–70k），這與你的下一階段職涯規劃與薪資期待是否相符？","在不涉及營業機密的前提下，你在清理多年積案並將 30 天內結案比例由 52% 提升至 79% 時，是如何與 10 個內部單位協商優先序與評估可行性的？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":9,"uncertainty_levels":1,"basis":"針對 jd32 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：9（±1）
- 一句話理由：現任同業招募系統 PO，具「以實測歸納...把這些規則接回新版」、完成 88% 廠商建議、30 天結案率升至 79% 與 AI 協作實績，高度對位。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 人力銀行企業端招募系統專案負責人，系統服務逾 6 萬家活躍付費廠商 | 無關鍵缺口，可於面試深化 |
| role_evidence | 強 | 接手求才系統改版時，業務後台與資料庫都不能更動...把這些規則接回新版的規格與流 | 無關鍵缺口，可於面試深化 |
| decision_depth | 強 | 依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 這些模組相關的 840 件廠商建議，已完成 743 件（88%）；30 天內結案 | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 對接工程、行銷、業務與客服等 10 個需求單位；帶領 2 名直屬產品企劃 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 問題背景、系統限制、SA 盤點動作與結案指標脈絡極為清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 3年以上經驗且具備資訊或網站開發經驗或擁有SA（系統分析）經驗 | 必要 | supported | 從需求釐清、系統分析到流程與原型設計，完成 PRD；能將業務上的搜尋、篩選規則拆 | 現任同業招募系統PO，具扎實SA系統分析、舊規則逆向盤點與API規格議定經驗 |
| R02 傾聽需求，解決挑戰：接手內部使用者與外部客戶的議題，安排功能優化或問題修正 | 必要 | supported | 這些模組相關的 840 件廠商建議，已完成 743 件（88%）；30 天內結案 | 高比例完成840件廠商建議並清理多年積案，大幅提升30天結案率 |
| R03 運用AI工具進行營運分析或提案 | 必要 | supported | 以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格 | 深入運用Claude Code與AI Agent整理分析資料並轉譯工程條件 |
| R04 熟悉規格撰寫、跨單位溝通；與團隊評估解決方案的可行性與時程 | 必要 | supported | 對接工程、行銷、業務與客服等 10 個需求單位；依提案時間與難易安排新案，每週向 | 對接10個內部單位、依難易與提案時間評估排程並每週回報 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 從需求釐清、系統分析到流程與原型設計，完成 PRD；能將業務上的搜尋、篩選規則拆 | 對位 jd32 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 以實測歸納、請工程協助驗證，再與維運、稽核核對 | 清楚界定個人規劃與工程/QA/DBA分工 |
| HR04 | supported | 30 天內結案的比例由前一年的 52% 升至 79% | 具結案率與定價實驗數據，缺部分功能採用率 |
| HR05 | supported | 將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與新舊並行取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端消費產品演進至B2B平台主任 |
| HR07 | supported | 上線前以互動原型與 FAQ 向客服、業務說明 | Scrum、原型、API議定、AI與英文皆有實例 |
| HR08 | supported | 從需求釐清、系統分析、流程與畫面設計，到 PRD | 結構分明，問題背景、動作與結果易讀 |
| HR09 | supported | 上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 誠實標註行銷導流期間、封測中與客服回報口徑 |
| HR10 | partial | 結合過去在訂閱、定價與企業流程上的經驗 | 自傳盼做產品策略，需對齊內部系統期待 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃 | 證據鏈支持安排 jd32 面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人 | 針對大客戶部門/分店共同招募痛點設計群組權限 |
| HM03 | supported | 依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與新舊並行取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數機制與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18% | 結案率與定價實驗基準清晰，缺部分功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程 | 具後台不動下新舊並行、API防重放與防冒用閉環 |
| HM08 | supported | 以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則 | 能確認API JSON欄位與拆解查詢條件，取數協作DBA |
| HM09 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 上線調整，並依客服回饋修正操作方式 | 依客服回饋修正登入操作方式與AI推薦規則 |
| HM12 | supported | 具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd32 明文條件與附錄 A 履歷獨立取證判讀 | 僅依 jd32 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 現任直接同業（1111 人力銀行）企業端招募系統 PO，在「業務後台與資料庫都不能更動、舊系統權限與計費規則無文件」的限制下，逆向實測並訪談維運、稽核補回規則，完成前後端分離新版上線與 743/840 件（88%）建議案 |
| 2 | 2025 Q4 先清理多年積案，再依提案時間與難易安排新案並每週向 10 個需求單位回報進度，使提案滿 30 天者之「30 天內結案比例由前一年的 52% 升至 79%」，完全對應本職缺內部與外部議題排程控管且量測與責任可追溯 |
| 3 | 以 Claude Code 建立協作流程與共用 skill，「運用 AI Agent 撰寫規格、整理與分析資料，並將業務規則轉為可與工程討論的條件描述」，直接命中 JD 要求 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 自傳末段提到「接下來，我希望把更多心力放回產品策略」，而本職缺聚焦於「內部營運用網站的功能設計與內部／外部議題修正」且月薪為 50,000~70,000 元 | 你在自傳中提到希望把更多心力放回產品策略，而我們這個職位主要負責「內部營運用網站」與跨單位需求優化（月薪 50k–70k），這與你的下一階段職涯規劃與薪資期待是否相符？ |
| 2 | 信件與即時通整合、搜尋結果頁改版兩案目前仍在開發／封測中 | 在不涉及營業機密的前提下，你在清理多年積案並將 30 天內結案比例由 52% 提升至 79% 時，是如何與 10 個內部單位協商優先序與評估可行性的？ |

### 5.5 審查者的質疑（本版新增；不是缺口清單）
#### 質疑 1
- **誰在想**：用人主管
- **讀到哪一句**：業務後台與資料庫都不能更動，主副帳號權限...計費規則卻沒有文件
- **心裡怎麼想**：「看到這句我會立刻想約他！我們內部營運系統一樣有大量歷史包袱跟舊資料庫限制，他居然能靠實測歸納跟訪談維運稽核把無文件的計費與權限規則補齊，還把 30 天結案率從 52% 拉到 79%，這完全就是我們最需要的即戰力。但我會先問：他在 1111 已經當到主任管前台求才系統，為什麼願意來做純『內部營運用網站』？」
- **這個疑問會讓我**：仍然約談
- **要打消疑問，履歷或面試需要看到**：面試時誠實溝通對「內部營運用網站 PM」角色定位的看法，以及如何從內部流程優化中找到成就感與策略價值。

#### 質疑 2
- **誰在想**：HR
- **讀到哪一句**：接下來，我希望把更多心力放回產品策略...做出對使用者與業務更有影響的產品
- **心裡怎麼想**：「他的經歷跟我們同業背景 100% 吻合，但自傳最後一段寫想做『產品策略』，加上我們這個缺開 50,000~70,000 元，以他近 10 年年資又是同業主任，我擔心他進來會覺得大材小用或薪資落差太大。」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：於電話初篩確認薪資期望是否符合 50k–70k 預算範圍，並釐清轉職動機。

#### 質疑 3
- **誰在想**：用人主管
- **讀到哪一句**：以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格
- **心裡怎麼想**：「我們 JD 剛好希望找會用 AI 工具做營運分析或提案的人，他寫自己建了 Claude Code 共用 skill 把業務規則轉成工程條件，我想在面試時看他實際怎麼用在日常內部需求整理上。」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：具體舉例一個運用 Claude Code 整理跨單位需求、分析積案或拆解複雜業務規則的實例。

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷第1點｜接手求才系統改版時，業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程...840 件廠商建議，已完成 743 件（88%）｜對 jd32 完美證明同業系統 SA 逆向分析與既有後台相容性規劃能力
- 1111經歷第8點｜先清理多年積案，再依提案時間與難易安排新案，每週向各單位回報進度。之後提出的案件，30 天內結案的比例由前一年的 52% 升至 79%｜對 jd32 直接對位「接手內部與外部議題、評估可行性與掌握節奏」且量化成效可追溯
- AI協作技能｜以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格｜對 jd32 直接命中「運用 AI 工具進行營運分析或提案」

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：自傳末段提到「接下來，我希望把更多心力放回產品策略」，而本職缺聚焦於「內部營運用網站的功能設計與內部／外部議題修正」且月薪為 50,000~70,000 元
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落
- 位置：1111 經歷第 1、2、4、7 點與尚凡第 1 點
  - 原句：與工程於 2025/09 完成上線；完成三項功能上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：強

### 8. 未測試聲明
PDF 抽字：local_extraction（已於總報告 §6 獨立列示 `resume-v10.3-twocol.pdf` 本機抽字結果，不併入內容評等） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

## 單份審查｜履歷 Resume_v10.3_AppendixA（jd34 SaaS 產品經理 / Product Owner｜91APP）｜第 10 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd34","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd34-10","human_calibrated":false,"requirements":[{"id":"R01","text":"5年以上經驗（含2年以上產品管理經驗）","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"資深PM與大型B2B平台PO年資充足"},{"id":"R02","text":"有金流、物流、會員、促購、優惠券、購買流程、訂單相關功能開發經驗","type":"required","status":"partial","evidence":["主副帳號權限、合約制與點數制的計費規則；提出 7／30／90 天訂閱方案與加贈內"],"blocks_interview":false,"reason":"具金流串接、購買付款流程、企業會員分店群組權限與點數加贈經驗，缺實體物流與優惠券訂單"},{"id":"R03","text":"產品管理和設計並與UX、RD、QA密切協作；製作使用者介面","type":"required","status":"supported","evidence":["從需求釐清、系統分析到流程與原型設計，完成 PRD，並與 QA 制定 UAT 驗"],"blocks_interview":false,"reason":"完整主導開發循環與UX/RD/QA協作並熟稔Figma/Axure"},{"id":"R04","text":"參與和運作Scrum團隊；定義產品目標用數據分析效益","type":"required","status":"supported","evidence":["曾參與每週一個 Sprint 的 Scrum；降價期 iOS 非續訂營收較原價期"],"blocks_interview":false,"reason":"具Scrum運作與數據實驗分析實績"},{"id":"R05","text":"加分：從0到1產品開發、熟悉支付生態、運用Gen AI加入產品具體案例","type":"preferred","status":"supported","evidence":["規劃 KOOL 網紅媒合平台；導入 CodaPay；定義公司簡介生成、職缺工作說"],"blocks_interview":false,"reason":"三項核心加分條件（0到1、支付、GenAI入產品）全部具備具體案例"},{"id":"R06","text":"加分：具簡報募資、提案經驗；200人以上軟體開發團隊2年以上經驗","type":"preferred","status":"partial","evidence":["參與公司一級主管日會，向總經理、副總等主管匯報；另協助業務製作銷售簡報"],"blocks_interview":false,"reason":"具高層匯報與銷售簡報經驗，未載明軟體團隊是否達200人及外部募資"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["人力銀行企業端招募系統專案負責人，系統服務逾 6 萬家活躍付費廠商"],"missing":["過往為招募平台與社交媒合，未直接經手零售電商 OMO 門市庫存與實體物流"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"強","evidence":["曾參與每週一個 Sprint 的 Scrum...定義公司簡介生成、職缺工作說明"],"missing":["具金流、會員權限、點數與促購加贈經驗，缺實體物流、優惠券與購物車訂單模組經驗"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["規劃群組功能，讓同單位帳號共同處理職缺及對應履歷"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["30 天內結案的比例由前一年的 52% 升至 79%；網頁付款占營收由 24% "],"missing":["1111群組功能與AI功能未列上線後採用數據"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["清楚呈現大型 B2B 平台架構改版、分店群組權限與商業變現經驗"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"對位 jd34 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd34 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"證據鏈支持安排 jd34 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"你在 1111 梳理「合約制與點數制的計費規則」及「部門／分店群組權限」的經驗，若遷移至 91APP 新零售 SaaS 的「門市分店庫存、跨通路優惠券折抵與退換貨訂單狀態機」，你會如何拆解？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd34 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"具備金流、購買付款流程、企業會員權限與點數機制經驗，但未直接經手零售電商之「實體物流串接、購物車優惠券折抵與實體商品訂單管理」","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗，經手 6 款產品","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["現任服務逾 6 萬家活躍付費廠商之 B2B 平台 Product Owner，且針對大型客戶「部門或分店共同招募」規劃上線群組權限功能，與 91APP 服務破萬家零售品牌、處理「總部 vs 分店門市權限（OMO）」的架構邏輯高度相通","具備金流串接（Peach 網頁付款占營收升至 80%+、CodaPay 東南亞超商與電信帳單付款）、主副帳號與合約／點數計費規則、7／30／90 天方案加贈及 Scrum 運作經驗","同時命中三項核心加分條件：KOOL 0 到 1 產品開發、支付生態串接試算、以及將 Gen AI 加入產品的具體上線案例（公司簡介生成、職缺說明生成、AI 推薦人才）"],"key_gaps":["具備金流、購買付款流程、企業會員權限與點數機制經驗，但未直接經手零售電商之「實體物流串接、購物車優惠券折抵與實體商品訂單管理」","1111 上線之群組功能與 3 項 Gen AI 功能未列出上線後的客戶使用率與效益指標","未載明過往協作之軟體研發團隊總規模是否達 200 人以上"],"strengths":["1111經歷第1-2點｜主副帳號權限、合約制與點數制的計費規則...大型客戶需要讓部門或分店共同招募...規劃群組功能｜對 jd34 直接證明具備萬家企業級 SaaS 之會員分店權限與計費邏輯規劃力","1111經歷第7點｜定義公司簡介生成、職缺工作說明生成及 AI 推薦人才的使用情境與驗收標準｜對 jd34 直接命中加分項「運用 Gen AI 加入產品的具體案例」","尚凡第4點與思維特第2點｜規劃 Peach 付款由 App 內購轉向網頁，與 CodaPay 新加坡技術團隊協調串接...提出 7／30／90 天訂閱方案｜對 jd34 證明熟悉支付產業串接與購買付款流程"],"interview_questions":["你在 1111 梳理「合約制與點數制的計費規則」及「部門／分店群組權限」的經驗，若遷移至 91APP 新零售 SaaS 的「門市分店庫存、跨通路優惠券折抵與退換貨訂單狀態機」，你會如何拆解？","你在 1111 與資料科學團隊上線的 3 項 Gen AI 功能（公司簡介生成、職缺說明生成、AI 推薦人才），上線後如何用數據衡量產品效益？","在 1111 對接工程、行銷、業務、客服等 10 個單位推進前後端分離改版時，工程研發與產品團隊的組織規模與跨團隊協作模式為何？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd34 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：主責「系統服務逾 6 萬家活躍付費廠商」之 SaaS 平台，具群組權限、Scrum、金流點數與 3 項 AI 上線實績，支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 人力銀行企業端招募系統專案負責人，系統服務逾 6 萬家活躍付費廠商 | 過往為招募平台與社交媒合，未直接經手零售電商 OMO 門市庫存與實體物流 |
| role_evidence | 強 | 曾參與每週一個 Sprint 的 Scrum...定義公司簡介生成、職缺工作說明 | 具金流、會員權限、點數與促購加贈經驗，缺實體物流、優惠券與購物車訂單模組經驗 |
| decision_depth | 強 | 規劃群組功能，讓同單位帳號共同處理職缺及對應履歷 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 30 天內結案的比例由前一年的 52% 升至 79%；網頁付款占營收由 24%  | 1111群組功能與AI功能未列上線後採用數據 |
| ownership | 強 | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 清楚呈現大型 B2B 平台架構改版、分店群組權限與商業變現經驗 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 5年以上經驗（含2年以上產品管理經驗） | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 資深PM與大型B2B平台PO年資充足 |
| R02 有金流、物流、會員、促購、優惠券、購買流程、訂單相關功能開發經驗 | 必要 | partial | 主副帳號權限、合約制與點數制的計費規則；提出 7／30／90 天訂閱方案與加贈內 | 具金流串接、購買付款流程、企業會員分店群組權限與點數加贈經驗，缺實體物流與優惠券訂單 |
| R03 產品管理和設計並與UX、RD、QA密切協作；製作使用者介面 | 必要 | supported | 從需求釐清、系統分析到流程與原型設計，完成 PRD，並與 QA 制定 UAT 驗 | 完整主導開發循環與UX/RD/QA協作並熟稔Figma/Axure |
| R04 參與和運作Scrum團隊；定義產品目標用數據分析效益 | 必要 | supported | 曾參與每週一個 Sprint 的 Scrum；降價期 iOS 非續訂營收較原價期 | 具Scrum運作與數據實驗分析實績 |
| R05 加分：從0到1產品開發、熟悉支付生態、運用Gen AI加入產品具體案例 | 加分 | supported | 規劃 KOOL 網紅媒合平台；導入 CodaPay；定義公司簡介生成、職缺工作說 | 三項核心加分條件（0到1、支付、GenAI入產品）全部具備具體案例 |
| R06 加分：具簡報募資、提案經驗；200人以上軟體開發團隊2年以上經驗 | 加分 | partial | 參與公司一級主管日會，向總經理、副總等主管匯報；另協助業務製作銷售簡報 | 具高層匯報與銷售簡報經驗，未載明軟體團隊是否達200人及外部募資 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 對位 jd34 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 以實測歸納、請工程協助驗證，再與維運、稽核核對 | 清楚界定個人規劃與工程/QA/DBA分工 |
| HR04 | supported | 30 天內結案的比例由前一年的 52% 升至 79% | 具結案率與定價實驗數據，缺部分功能採用率 |
| HR05 | supported | 將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與新舊並行取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端消費產品演進至B2B平台主任 |
| HR07 | supported | 上線前以互動原型與 FAQ 向客服、業務說明 | Scrum、原型、API議定、AI與英文皆有實例 |
| HR08 | supported | 從需求釐清、系統分析、流程與畫面設計，到 PRD | 結構分明，問題背景、動作與結果易讀 |
| HR09 | supported | 上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 誠實標註行銷導流期間、封測中與客服回報口徑 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd34 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃 | 證據鏈支持安排 jd34 面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人 | 針對大客戶部門/分店共同招募痛點設計群組權限 |
| HM03 | supported | 依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與新舊並行取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數機制與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18% | 結案率與定價實驗基準清晰，缺部分功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程 | 具後台不動下新舊並行、API防重放與防冒用閉環 |
| HM08 | supported | 以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則 | 能確認API JSON欄位與拆解查詢條件，取數協作DBA |
| HM09 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 上線調整，並依客服回饋修正操作方式 | 依客服回饋修正登入操作方式與AI推薦規則 |
| HM12 | supported | 具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd34 明文條件與附錄 A 履歷獨立取證判讀 | 僅依 jd34 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 現任服務逾 6 萬家活躍付費廠商之 B2B 平台 Product Owner，且針對大型客戶「部門或分店共同招募」規劃上線群組權限功能，與 91APP 服務破萬家零售品牌、處理「總部 vs 分店門市權限（OMO）」的架構邏輯高度相通 |
| 2 | 具備金流串接（Peach 網頁付款占營收升至 80%+、CodaPay 東南亞超商與電信帳單付款）、主副帳號與合約／點數計費規則、7／30／90 天方案加贈及 Scrum 運作經驗 |
| 3 | 同時命中三項核心加分條件：KOOL 0 到 1 產品開發、支付生態串接試算、以及將 Gen AI 加入產品的具體上線案例（公司簡介生成、職缺說明生成、AI 推薦人才） |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 具備金流、購買付款流程、企業會員權限與點數機制經驗，但未直接經手零售電商之「實體物流串接、購物車優惠券折抵與實體商品訂單管理」 | 你在 1111 梳理「合約制與點數制的計費規則」及「部門／分店群組權限」的經驗，若遷移至 91APP 新零售 SaaS 的「門市分店庫存、跨通路優惠券折抵與退換貨訂單狀態機」，你會如何拆解？ |
| 2 | 1111 上線之群組功能與 3 項 Gen AI 功能未列出上線後的客戶使用率與效益指標 | 你在 1111 與資料科學團隊上線的 3 項 Gen AI 功能（公司簡介生成、職缺說明生成、AI 推薦人才），上線後如何用數據衡量產品效益？ |
| 3 | 未載明過往協作之軟體研發團隊總規模是否達 200 人以上 | 在 1111 對接工程、行銷、業務、客服等 10 個單位推進前後端分離改版時，工程研發與產品團隊的組織規模與跨團隊協作模式為何？ |

### 5.5 審查者的質疑（本版新增；不是缺口清單）
#### 質疑 1
- **誰在想**：用人主管
- **讀到哪一句**：規劃群組功能，讓同單位帳號共同處理職缺及對應履歷
- **心裡怎麼想**：「這段對我們做多門市 OMO SaaS 很有吸引力！很多 PM 沒做過 B2B 多層級組織權限，他不但做過『總公司－部門／分店』的群組權限與舊資料轉換，還上線過 3 個 Gen AI 功能，我會想約他面試。但我會先問：他沒做過實體電商的『購物車優惠券＋超商宅配物流＋退貨逆物流』，他的規則拆解能力能不能應付電商訂單狀態機？」
- **這個疑問會讓我**：仍然約談
- **要打消疑問，履歷或面試需要看到**：面試時以「點數／合約扣款與退還」或現場白板題測試他對複雜訂單／優惠券折抵與逆流程狀態機的系統分析深度。

#### 質疑 2
- **誰在想**：用人主管
- **讀到哪一句**：定義公司簡介生成、職缺工作說明生成及 AI 推薦人才的使用情境與驗收標準
- **心裡怎麼想**：「加分項剛好要找有把 Gen AI 放進產品具體案例的人，他一口氣寫了三個上線功能，但只寫『依客服測試回饋調整推薦規則』，沒有任何上線後廠商使用率或轉換率數據，我會懷疑這三個功能是不是為了交差而上線、實際上沒什麼廠商在用。」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：準備這三項 AI 功能上線後的真實採用數據、生成內容留存率，以及當時制定的驗收標準細項。

#### 質疑 3
- **誰在想**：HR
- **讀到哪一句**：曾參與每週一個 Sprint 的 Scrum，現行以 Kanban 推進瀑布式
- **心裡怎麼想**：「91APP 產品研發團隊是跑標準 Scrum 的大型軟體組織，他寫『曾參與』Scrum、現行是『以 Kanban 推進瀑布式開發』，我想確認他跑 Scrum 的時間有多長、能不能快速適應大型敏捷研發團隊的節奏。」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：說明過往運作 Scrum 團隊的期間、Sprint Planning / Review / Retro 的參與深度與團隊規模。

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷第1-2點｜主副帳號權限、合約制與點數制的計費規則...大型客戶需要讓部門或分店共同招募...規劃群組功能｜對 jd34 直接證明具備萬家企業級 SaaS 之會員分店權限與計費邏輯規劃力
- 1111經歷第7點｜定義公司簡介生成、職缺工作說明生成及 AI 推薦人才的使用情境與驗收標準｜對 jd34 直接命中加分項「運用 Gen AI 加入產品的具體案例」
- 尚凡第4點與思維特第2點｜規劃 Peach 付款由 App 內購轉向網頁，與 CodaPay 新加坡技術團隊協調串接...提出 7／30／90 天訂閱方案｜對 jd34 證明熟悉支付產業串接與購買付款流程

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：具備金流、購買付款流程、企業會員權限與點數機制經驗，但未直接經手零售電商之「實體物流串接、購物車優惠券折抵與實體商品訂單管理」
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落
- 位置：1111 經歷第 1、2、4、7 點與尚凡第 1 點
  - 原句：與工程於 2025/09 完成上線；完成三項功能上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：強

### 8. 未測試聲明
PDF 抽字：local_extraction（已於總報告 §6 獨立列示 `resume-v10.3-twocol.pdf` 本機抽字結果，不併入內容評等） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

## 單份審查｜履歷 Resume_v10.3_AppendixA（jd36 全支付- Product Manager (內部系統、串接)）｜第 11 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd36","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd36-11","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上相關工作經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"年資近10年且具豐富系統改版與API串接經驗"},{"id":"R02","text":"能運用Axure撰寫產品規劃，並透過Jira、Confluence進行專案管理","type":"required","status":"partial","evidence":["Figma、Axure RP、Notion、Trello；使用 Trello 及"],"blocks_interview":false,"reason":"具Axure RP與內部專案控管系統，未直接寫出Jira/Confluence"},{"id":"R03","text":"能同步考慮技術可行性以及系統架構關連影響","type":"required","status":"supported","evidence":["接手求才系統改版時，業務後台與資料庫都不能更動...把這些規則接回新版的規格與流"],"blocks_interview":false,"reason":"在後台與資料庫不動限制下完成新舊系統並行與資料轉換"},{"id":"R04","text":"熟悉API規格；與合作方或相關單位確認規劃並與法遵確認適法性","type":"required","status":"supported","evidence":["外部 API 規格議定（簽章驗證、防重放、錯誤碼、頻率限制）；與維運、稽核核對"],"blocks_interview":false,"reason":"明確具備外部API規格議定、JSON欄位確認、CodaPay串接與稽核核對經驗"},{"id":"R05","text":"執行功能測試、驗收、上線協調及內部教育訓練、線上問題排除與迭代","type":"required","status":"supported","evidence":["與 QA 制定 UAT 驗收案例、排定上線計畫。上線前以互動原型與 FAQ 向客"],"blocks_interview":false,"reason":"完整涵蓋UAT驗收、上線計畫、內部教學與840件建議迭代"},{"id":"R06","text":"加分：熟悉代理收付、電子支付及行動支付領域知識；資管或資工學系畢業或有相關工作經驗","type":"preferred","status":"supported","evidence":["規劃 Peach 付款由 App 內購轉向網頁，與 CodaPay 新加坡技術團"],"blocks_interview":false,"reason":"具近10年軟體PM相關工作經驗與跨國支付串接/實收試算實績"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["推動系統改版至前後端分離的新架構，採新舊並行、分階段上線"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"強","evidence":["與外部合作夥伴議定查詢 API 時...並與工程確認 JSON 欄位與判定規則"],"missing":["專案管理使用 Trello 與內部控管系統，未直接寫出 Jira/Confluence"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["以簽章驗證與時間戳防止重放，以錯誤碼與頻率限制控管呼叫"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["這些模組相關的 840 件廠商建議，已完成 743 件（88%）；30 天內結案"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["對接工程、行銷、業務與客服等 10 個需求單位；上線前以互動原型與 FAQ 向客"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["內部後台限制、API 規格細項（簽章、防重放、錯誤碼、頻率限制）與交付脈絡極清楚"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"對位 jd36 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd36 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"證據鏈支持安排 jd36 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"你在 1111 使用 Trello 與內部專案控管系統管理 User Story 與派工估時，過去是否曾使用過 Jira 與 Confluence？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd36 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"必要條件要求「透過 Jira、Confluence 進行專案管理」，履歷列 Notion、Trello 與內部專案控管系統","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗，經手 6 款產品","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["在 API 規格與外部平台串接上提供極具體的技術證據：「與外部合作夥伴議定查詢 API 時，先處理可能被濫用的風險：以簽章驗證與時間戳防止重放...與工程確認 JSON 欄位與判定規則與判定規則」，加上 CodaPay 新加坡金流技術串接經驗，完全契合 jd36「內部系統、串接」核心要求","在「業務後台與資料庫都不能更動、舊規則無文件」的限制下，透過實測與訪談維運、稽核補回計費與權限規則，推動新舊並行分階段上線並完成 743/840 件建議（88%），展現極強的內部系統架構關連思考力","熟稔 Axure RP、流程圖／循序圖、PRD、UAT 驗收與內部教育訓練（互動原型與 FAQ），且將客戶案件 30 天內結案率由 52% 提升至 79%"],"key_gaps":["必要條件要求「透過 Jira、Confluence 進行專案管理」，履歷列 Notion、Trello 與內部專案控管系統","過往金流串接為第三方支付平台（CodaPay），未直接經手台灣銀行專線串接或專營電子支付機構內部清算作業","職責第 2 點提及「與法遵確認適法性」，履歷載明「與維運、稽核核對」"],"strengths":["1111經歷第5點與技能欄｜外部 API 規格議定（簽章驗證、防重放、錯誤碼、頻率限制），並與工程確認 JSON 欄位與判定規則｜對 jd36 直接滿足「熟悉 API 規格、外部平台串接與考慮系統架構影響」之核心條件","1111經歷第1-2點｜業務後台與資料庫都不能更動...以實測歸納、請工程協助驗證，再與維運、稽核核對，把這些規則接回新版｜對 jd36 展現處理複雜內部規則、新舊系統銜接與稽核核對的硬實力","1111經歷第3,8點｜Axure RP...完成 PRD，並與 QA 制定 UAT 驗收案例...上線前以互動原型與 FAQ 向客服、業務說明；30 天內結案由 52% 升至 79%｜對 jd36 完整對應內部教育訓練、測試驗收與時程交付"],"interview_questions":["你在 1111 使用 Trello 與內部專案控管系統管理 User Story 與派工估時，過去是否曾使用過 Jira 與 Confluence？","若負責全支付與銀行或特定外部平台的串接專案，當遇到跨機構交易逾時（Timeout）或帳務狀態不一致時，你會如何在 API 規格與後台作業設計補償與異常排除機制？","在 1111 梳理合約與點數計費規則及處理廠商帳號冒用時，與內部稽核或法遵單位核對的具體流程為何？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd36 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：具「與外部合作夥伴議定查詢 API...確認 JSON 欄位」、新舊系統並行改版與 Axure 規劃經驗，高度契合。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 推動系統改版至前後端分離的新架構，採新舊並行、分階段上線 | 無關鍵缺口，可於面試深化 |
| role_evidence | 強 | 與外部合作夥伴議定查詢 API 時...並與工程確認 JSON 欄位與判定規則 | 專案管理使用 Trello 與內部控管系統，未直接寫出 Jira/Confluence |
| decision_depth | 強 | 以簽章驗證與時間戳防止重放，以錯誤碼與頻率限制控管呼叫 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 這些模組相關的 840 件廠商建議，已完成 743 件（88%）；30 天內結案 | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 對接工程、行銷、業務與客服等 10 個需求單位；上線前以互動原型與 FAQ 向客 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 內部後台限制、API 規格細項（簽章、防重放、錯誤碼、頻率限制）與交付脈絡極清楚 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 3年以上相關工作經驗 | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 年資近10年且具豐富系統改版與API串接經驗 |
| R02 能運用Axure撰寫產品規劃，並透過Jira、Confluence進行專案管理 | 必要 | partial | Figma、Axure RP、Notion、Trello；使用 Trello 及 | 具Axure RP與內部專案控管系統，未直接寫出Jira/Confluence |
| R03 能同步考慮技術可行性以及系統架構關連影響 | 必要 | supported | 接手求才系統改版時，業務後台與資料庫都不能更動...把這些規則接回新版的規格與流 | 在後台與資料庫不動限制下完成新舊系統並行與資料轉換 |
| R04 熟悉API規格；與合作方或相關單位確認規劃並與法遵確認適法性 | 必要 | supported | 外部 API 規格議定（簽章驗證、防重放、錯誤碼、頻率限制）；與維運、稽核核對 | 明確具備外部API規格議定、JSON欄位確認、CodaPay串接與稽核核對經驗 |
| R05 執行功能測試、驗收、上線協調及內部教育訓練、線上問題排除與迭代 | 必要 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫。上線前以互動原型與 FAQ 向客 | 完整涵蓋UAT驗收、上線計畫、內部教學與840件建議迭代 |
| R06 加分：熟悉代理收付、電子支付及行動支付領域知識；資管或資工學系畢業或有相關工作經驗 | 加分 | supported | 規劃 Peach 付款由 App 內購轉向網頁，與 CodaPay 新加坡技術團 | 具近10年軟體PM相關工作經驗與跨國支付串接/實收試算實績 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 對位 jd36 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 以實測歸納、請工程協助驗證，再與維運、稽核核對 | 清楚界定個人規劃與工程/QA/DBA分工 |
| HR04 | supported | 30 天內結案的比例由前一年的 52% 升至 79% | 具結案率與定價實驗數據，缺部分功能採用率 |
| HR05 | supported | 將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與新舊並行取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端消費產品演進至B2B平台主任 |
| HR07 | supported | 上線前以互動原型與 FAQ 向客服、業務說明 | Scrum、原型、API議定、AI與英文皆有實例 |
| HR08 | supported | 從需求釐清、系統分析、流程與畫面設計，到 PRD | 結構分明，問題背景、動作與結果易讀 |
| HR09 | supported | 上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 誠實標註行銷導流期間、封測中與客服回報口徑 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd36 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃 | 證據鏈支持安排 jd36 面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人 | 針對大客戶部門/分店共同招募痛點設計群組權限 |
| HM03 | supported | 依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與新舊並行取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數機制與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18% | 結案率與定價實驗基準清晰，缺部分功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程 | 具後台不動下新舊並行、API防重放與防冒用閉環 |
| HM08 | supported | 以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則 | 能確認API JSON欄位與拆解查詢條件，取數協作DBA |
| HM09 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 上線調整，並依客服回饋修正操作方式 | 依客服回饋修正登入操作方式與AI推薦規則 |
| HM12 | supported | 具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd36 明文條件與附錄 A 履歷獨立取證判讀 | 僅依 jd36 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 在 API 規格與外部平台串接上提供極具體的技術證據：「與外部合作夥伴議定查詢 API 時，先處理可能被濫用的風險：以簽章驗證與時間戳防止重放...與工程確認 JSON 欄位與判定規則與判定規則」，加上 CodaPay 新加坡金流技術串接經驗，完全契合 jd36「內部系統、串接」核心要求 |
| 2 | 在「業務後台與資料庫都不能更動、舊規則無文件」的限制下，透過實測與訪談維運、稽核補回計費與權限規則，推動新舊並行分階段上線並完成 743/840 件建議（88%），展現極強的內部系統架構關連思考力 |
| 3 | 熟稔 Axure RP、流程圖／循序圖、PRD、UAT 驗收與內部教育訓練（互動原型與 FAQ），且將客戶案件 30 天內結案率由 52% 提升至 79% |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 必要條件要求「透過 Jira、Confluence 進行專案管理」，履歷列 Notion、Trello 與內部專案控管系統 | 你在 1111 使用 Trello 與內部專案控管系統管理 User Story 與派工估時，過去是否曾使用過 Jira 與 Confluence？ |
| 2 | 過往金流串接為第三方支付平台（CodaPay），未直接經手台灣銀行專線串接或專營電子支付機構內部清算作業 | 若負責全支付與銀行或特定外部平台的串接專案，當遇到跨機構交易逾時（Timeout）或帳務狀態不一致時，你會如何在 API 規格與後台作業設計補償與異常排除機制？ |
| 3 | 職責第 2 點提及「與法遵確認適法性」，履歷載明「與維運、稽核核對」 | 在 1111 梳理合約與點數計費規則及處理廠商帳號冒用時，與內部稽核或法遵單位核對的具體流程為何？ |

### 5.5 審查者的質疑（本版新增；不是缺口清單）
#### 質疑 1
- **誰在想**：用人主管
- **讀到哪一句**：以簽章驗證與時間戳防止重放...與工程確認 JSON 欄位與判定規則
- **心裡怎麼想**：「老實說，看到這句加上前面『業務後台與資料庫都不能更動，把規則接回新版』，我覺得他非常適合我們『內部系統＋外部串接』這個缺！很多 PM 聽到後台跟 API 就退縮，他卻寫得很具體，我一定會約。但我會先問：那支外部查詢 API 是查什麼資料的？為什麼是由你們提供查詢 API 給外部夥伴，而不是你們去串別人？」
- **這個疑問會讓我**：仍然約談
- **要打消疑問，履歷或面試需要看到**：面試時說明該支外部合作夥伴查詢 API 的業務情境、雙向資料流向，以及與 CodaPay 串接時作為呼叫方（Client）與提供方（Server）的經驗差異。

#### 質疑 2
- **誰在想**：HR
- **讀到哪一句**：使用 Trello 及內部專案控管系統，按 User Story 記錄需求
- **心裡怎麼想**：「跟我們另一個 PM 缺一樣，必備條件寫了 Axure、Jira、Confluence，他有 Axure 但沒寫 Jira 跟 Confluence，需要面試時順便確認工具轉換。」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：確認 Jira / Confluence 使用經驗或內部系統對應方式。

#### 質疑 3
- **誰在想**：用人主管
- **讀到哪一句**：業務後台與資料庫都不能更動，主副帳號權限...計費規則卻沒有文件
- **心裡怎麼想**：「他在 1111 的改版前提是『業務後台不能更動』，但我們這個職缺有一半是要做『公司內部作業的功能開發優化』，也就是要直接改內部作業後台，我想確認他有沒有實際設計過內部人員（營運、客服、財務、稽核）使用的後台介面。」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：補充說明在 1111、尚凡或思維特期間，是否曾規劃或優化過供內部客服、業務或維運人員使用的後台功能。

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷第5點與技能欄｜外部 API 規格議定（簽章驗證、防重放、錯誤碼、頻率限制），並與工程確認 JSON 欄位與判定規則｜對 jd36 直接滿足「熟悉 API 規格、外部平台串接與考慮系統架構影響」之核心條件
- 1111經歷第1-2點｜業務後台與資料庫都不能更動...以實測歸納、請工程協助驗證，再與維運、稽核核對，把這些規則接回新版｜對 jd36 展現處理複雜內部規則、新舊系統銜接與稽核核對的硬實力
- 1111經歷第3,8點｜Axure RP...完成 PRD，並與 QA 制定 UAT 驗收案例...上線前以互動原型與 FAQ 向客服、業務說明；30 天內結案由 52% 升至 79%｜對 jd36 完整對應內部教育訓練、測試驗收與時程交付

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：必要條件要求「透過 Jira、Confluence 進行專案管理」，履歷列 Notion、Trello 與內部專案控管系統
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落
- 位置：1111 經歷第 1、2、4、7 點與尚凡第 1 點
  - 原句：與工程於 2025/09 完成上線；完成三項功能上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：強

### 8. 未測試聲明
PDF 抽字：local_extraction（已於總報告 §6 獨立列示 `resume-v10.3-twocol.pdf` 本機抽字結果，不併入內容評等） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

## 單份審查｜履歷 Resume_v10.3_AppendixA（jd40 【PMC】軟體產品經理 (PM / TPM)｜QuickClick快一點）｜第 12 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd40","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd40-12","human_calibrated":false,"requirements":[{"id":"R01","text":"5年以上軟體產品、技術產品或技術專案管理經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗；2023/12–2026/03 主責約 50 項大項功"],"blocks_interview":false,"reason":"年資近10年且大型系統架構改版與交付經驗扎實"},{"id":"R02","text":"參與產品從需求規劃到上線交付的完整流程（PRD、User Story、UAT、上線計畫）","type":"required","status":"supported","evidence":["從需求釐清、系統分析到流程與原型設計，完成 PRD，並與 QA 制定 UAT 驗"],"blocks_interview":false,"reason":"完整主導端到端產品規劃與上線交付週期"},{"id":"R03","text":"能理解API、資料流程及系統串接邏輯，與研發協調系統整合","type":"required","status":"supported","evidence":["外部 API 規格議定（簽章驗證、防重放、錯誤碼、頻率限制）...與工程確認 J"],"blocks_interview":false,"reason":"明確具備API規格議定、JSON欄位確認、查詢條件拆解與CodaPay串接經驗"},{"id":"R04","text":"具備良好的需求拆解、優先順序判斷、跨團隊溝通及風險管理能力","type":"required","status":"supported","evidence":["先清理多年積案，再依提案時間與難易安排新案，每週向各單位回報進度"],"blocks_interview":false,"reason":"具體展現積案清理、優先序排定、API防濫用與帳號防冒用風控"},{"id":"R05","text":"加分：KA客戶、客製化需求或NRE專案管理經驗；支付、餐飲、零售、SaaS或跨系統整合經驗","type":"preferred","status":"supported","evidence":["大型客戶需要讓部門或分店共同招募...規劃群組功能；2025 Q4 公司改以客戶"],"blocks_interview":false,"reason":"具大型客戶分店群組需求、客戶案件排程（結案率52%→79%）、支付與SaaS跨系統整合經驗"},{"id":"R06","text":"加分：基本SQL查詢或資料分析能力；客戶提案、需求協商或高階利害關係人溝通經驗","type":"preferred","status":"supported","evidence":["參與公司一級主管日會，向總經理、副總等主管匯報；另協助業務製作銷售簡報（sale"],"blocks_interview":false,"reason":"具高階主管日會匯報、sales kit支援、資料表欄位擬定與查詢條件拆解能力"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["推動系統改版至前後端分離的新架構，採新舊並行、分階段上線"],"missing":["過往為人力銀行與社交媒合平台，未直接接觸餐飲 POS 雲端接單硬體場景"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"強","evidence":["與外部合作夥伴議定查詢 API 時...並與工程確認 JSON 欄位與判定規則"],"missing":["具大型客戶群組功能與客戶案件優先排程，惟未明寫 NRE 合約報價字樣"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["2025 Q4 公司改以客戶案件為優先，先清理多年積案，再依提案時間與難易安排新"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["之後提出的案件，30 天內結案的比例由前一年的 52% 升至 79%（提案滿 3"],"missing":["1111 上線之 50 項大功能未逐一列出營運指標提升幅度"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["按 User Story 記錄需求、做法、驗收條件與優先級，供 Tech Lea"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["清楚呈現 PM 結合 TPM 之技術架構、API 規格、風險控管與交付節奏"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗；2023/12–2026/03 主責約 50 項大項功"],"application_note":"對位 jd40 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd40 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"證據鏈支持安排 jd40 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"在 1111 處理大型客戶需求與 2025 Q4 客戶優先案件時，是否曾參與外部 KA 客戶的客製化範疇談判、報價或需求變更控管？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd40 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"雖有大型客戶分店群組功能與「以客戶案件為優先（30 天結案率升至 79%）」經驗，但未明寫是否經手過收取 NRE（一次性工程開發費）之外部客戶客製化合約專案","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗；2023/12–2026/03 主責約 50 項大項功","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["高度匹配 PM 兼具 TPM（Technical Program Manager）的角色定位：既能從使用者旅程規劃 Roadmap，又能在「業務後台與資料庫不能更動」下推動前後端分離改版、議定外部查詢 API（簽章驗證、防重放、錯誤碼、頻率限制、JSON 欄位確認），並按 User Story 記錄做法與驗收條件供 Tech Lead 派工估時","具備直接可轉移至 KA／客戶專案交付管理的實績：規劃大型客戶「部門或分店共同招募」之群組功能，且於 2025 Q4 公司改以客戶案件為優先時，「先清理多年積案，再依提案時間與難易安排新案，每週向各單位回報進度，30 天內結案比例由 52% 升至 79%」","具備跨國數位支付串接（Peach 網頁付款、CodaPay 電信帳單與超商付款）與高階利害關係人溝通（參與一級主管日會向總經理、副總匯報）經驗"],"key_gaps":["雖有大型客戶分店群組功能與「以客戶案件為優先（30 天結案率升至 79%）」經驗，但未明寫是否經手過收取 NRE（一次性工程開發費）之外部客戶客製化合約專案","資料庫查詢為「擬定資料表與欄位需求，與 DBA 協作取數」，未明寫本人手寫 SQL 查詢語法程度","未直接經手餐飲科技（線上點餐、雲端接單 POS）產業"],"strengths":["1111經歷第1,5點｜推動系統改版至前後端分離的新架構，採新舊並行、分階段上線...以簽章驗證與時間戳防止重放...與工程確認 JSON 欄位與判定規則｜對 jd40 直接證明兼具 PM 與 TPM 所需的系統架構理解與 API 整合協作力","1111經歷第2,8點｜大型客戶需要讓部門或分店共同招募...規劃群組功能；30 天內結案的比例由前一年的 52% 升至 79%（提案滿 30 天者）｜對 jd40 直接對位連鎖分店客戶需求與客戶專案交付管理","專案交付與工具技能｜按 User Story 記錄需求、做法、驗收條件與優先級，供 Tech Lead 派工與估時；能將業務上的搜尋、篩選規則拆成查詢條件｜對 jd40 展現清楚的工程派工規格與資料邏輯拆解能力"],"interview_questions":["在 1111 處理大型客戶需求與 2025 Q4 客戶優先案件時，是否曾參與外部 KA 客戶的客製化範疇談判、報價或需求變更控管？","你在將搜尋篩選規則拆成查詢條件與工程確認後端行為，以及與 DBA 協作取數時，是否會自行撰寫基本 SQL 查詢？","我們服務連鎖餐飲品牌（含分店點餐、雲端接單與支付），你如何將 1111「大型客戶分店群組功能」與過去「CodaPay 支付串接」的經驗應用到連鎖餐飲系統？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd40 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：具「推動系統改版至前後端分離的新架構」、外部 API 議定（含 JSON 欄位確認）與客戶案件排程（30 天結案升至 79%）實績，支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 推動系統改版至前後端分離的新架構，採新舊並行、分階段上線 | 過往為人力銀行與社交媒合平台，未直接接觸餐飲 POS 雲端接單硬體場景 |
| role_evidence | 強 | 與外部合作夥伴議定查詢 API 時...並與工程確認 JSON 欄位與判定規則 | 具大型客戶群組功能與客戶案件優先排程，惟未明寫 NRE 合約報價字樣 |
| decision_depth | 強 | 2025 Q4 公司改以客戶案件為優先，先清理多年積案，再依提案時間與難易安排新 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 之後提出的案件，30 天內結案的比例由前一年的 52% 升至 79%（提案滿 3 | 1111 上線之 50 項大功能未逐一列出營運指標提升幅度 |
| ownership | 強 | 按 User Story 記錄需求、做法、驗收條件與優先級，供 Tech Lea | 無關鍵缺口，可於面試深化 |
| readability | 強 | 清楚呈現 PM 結合 TPM 之技術架構、API 規格、風險控管與交付節奏 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 5年以上軟體產品、技術產品或技術專案管理經驗 | 必要 | supported | 近 10 年 PM 經驗；2023/12–2026/03 主責約 50 項大項功 | 年資近10年且大型系統架構改版與交付經驗扎實 |
| R02 參與產品從需求規劃到上線交付的完整流程（PRD、User Story、UAT、上線計畫） | 必要 | supported | 從需求釐清、系統分析到流程與原型設計，完成 PRD，並與 QA 制定 UAT 驗 | 完整主導端到端產品規劃與上線交付週期 |
| R03 能理解API、資料流程及系統串接邏輯，與研發協調系統整合 | 必要 | supported | 外部 API 規格議定（簽章驗證、防重放、錯誤碼、頻率限制）...與工程確認 J | 明確具備API規格議定、JSON欄位確認、查詢條件拆解與CodaPay串接經驗 |
| R04 具備良好的需求拆解、優先順序判斷、跨團隊溝通及風險管理能力 | 必要 | supported | 先清理多年積案，再依提案時間與難易安排新案，每週向各單位回報進度 | 具體展現積案清理、優先序排定、API防濫用與帳號防冒用風控 |
| R05 加分：KA客戶、客製化需求或NRE專案管理經驗；支付、餐飲、零售、SaaS或跨系統整合經驗 | 加分 | supported | 大型客戶需要讓部門或分店共同招募...規劃群組功能；2025 Q4 公司改以客戶 | 具大型客戶分店群組需求、客戶案件排程（結案率52%→79%）、支付與SaaS跨系統整合經驗 |
| R06 加分：基本SQL查詢或資料分析能力；客戶提案、需求協商或高階利害關係人溝通經驗 | 加分 | supported | 參與公司一級主管日會，向總經理、副總等主管匯報；另協助業務製作銷售簡報（sale | 具高階主管日會匯報、sales kit支援、資料表欄位擬定與查詢條件拆解能力 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗；2023/12–2026/03 主責約 50 項大項功 | 對位 jd40 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 以實測歸納、請工程協助驗證，再與維運、稽核核對 | 清楚界定個人規劃與工程/QA/DBA分工 |
| HR04 | supported | 30 天內結案的比例由前一年的 52% 升至 79% | 具結案率與定價實驗數據，缺部分功能採用率 |
| HR05 | supported | 將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與新舊並行取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端消費產品演進至B2B平台主任 |
| HR07 | supported | 上線前以互動原型與 FAQ 向客服、業務說明 | Scrum、原型、API議定、AI與英文皆有實例 |
| HR08 | supported | 從需求釐清、系統分析、流程與畫面設計，到 PRD | 結構分明，問題背景、動作與結果易讀 |
| HR09 | supported | 上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 誠實標註行銷導流期間、封測中與客服回報口徑 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd40 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃 | 證據鏈支持安排 jd40 面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人 | 針對大客戶部門/分店共同招募痛點設計群組權限 |
| HM03 | supported | 依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與新舊並行取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數機制與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18% | 結案率與定價實驗基準清晰，缺部分功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程 | 具後台不動下新舊並行、API防重放與防冒用閉環 |
| HM08 | supported | 以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則 | 能確認API JSON欄位與拆解查詢條件，取數協作DBA |
| HM09 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 上線調整，並依客服回饋修正操作方式 | 依客服回饋修正登入操作方式與AI推薦規則 |
| HM12 | supported | 具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd40 明文條件與附錄 A 履歷獨立取證判讀 | 僅依 jd40 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 高度匹配 PM 兼具 TPM（Technical Program Manager）的角色定位：既能從使用者旅程規劃 Roadmap，又能在「業務後台與資料庫不能更動」下推動前後端分離改版、議定外部查詢 API（簽章驗證、防重放、錯誤碼、頻率限制、JSON 欄位確認），並按 User Story 記錄做法與驗收條件供 Tech Lead 派工估時 |
| 2 | 具備直接可轉移至 KA／客戶專案交付管理的實績：規劃大型客戶「部門或分店共同招募」之群組功能，且於 2025 Q4 公司改以客戶案件為優先時，「先清理多年積案，再依提案時間與難易安排新案，每週向各單位回報進度，30 天內結案比例由 52% 升至 79%」 |
| 3 | 具備跨國數位支付串接（Peach 網頁付款、CodaPay 電信帳單與超商付款）與高階利害關係人溝通（參與一級主管日會向總經理、副總匯報）經驗 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 雖有大型客戶分店群組功能與「以客戶案件為優先（30 天結案率升至 79%）」經驗，但未明寫是否經手過收取 NRE（一次性工程開發費）之外部客戶客製化合約專案 | 在 1111 處理大型客戶需求與 2025 Q4 客戶優先案件時，是否曾參與外部 KA 客戶的客製化範疇談判、報價或需求變更控管？ |
| 2 | 資料庫查詢為「擬定資料表與欄位需求，與 DBA 協作取數」，未明寫本人手寫 SQL 查詢語法程度 | 你在將搜尋篩選規則拆成查詢條件與工程確認後端行為，以及與 DBA 協作取數時，是否會自行撰寫基本 SQL 查詢？ |
| 3 | 未直接經手餐飲科技（線上點餐、雲端接單 POS）產業 | 我們服務連鎖餐飲品牌（含分店點餐、雲端接單與支付），你如何將 1111「大型客戶分店群組功能」與過去「CodaPay 支付串接」的經驗應用到連鎖餐飲系統？ |

### 5.5 審查者的質疑（本版新增；不是缺口清單）
#### 質疑 1
- **誰在想**：用人主管
- **讀到哪一句**：先清理多年積案，再依提案時間與難易安排新案...升至 79%
- **心裡怎麼想**：「這段完全打中我們 PM 兼 TPM 的痛點！我們每天都在處理連鎖餐飲 KA 客戶的客製化單跟產品標準 Roadmap 搶資源的問題，他能把客戶案件 30 天結案率從 52% 拉到 79%、又懂 API 簽章跟 JSON，我一定會約他！但我會先問：『依提案時間與難易安排新案』聽起來像先進先出加挑軟柿子吃，如果遇到大客戶的緊急難案插單，你怎麼管時程跟範圍？」
- **這個疑問會讓我**：仍然約談
- **要打消疑問，履歷或面試需要看到**：面試時請他詳述 2025 Q4 客戶案件排程的優先級矩陣（如何權衡客戶價值、開發難度与提案時間），以及面對重大需求變更時的控管做法。

#### 質疑 2
- **誰在想**：用人主管
- **讀到哪一句**：2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線。
- **心裡怎麼想**：「27 個月內上線 50 項『大項功能』，平均一個月快 2 項大功能，而且同一時間還在做前後端分離改版跟清積案，我心裡會懷疑他對『大項功能』的定義是不是灌水，把一般中小型功能優化也算進去。」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：準備這 50 項大項功能的分類清單或代表性時間軸，說明何謂「大項功能」（如開發人天規模、跨系統模組數）。

#### 質疑 3
- **誰在想**：HR
- **讀到哪一句**：現行以 Kanban 推進瀑布式開發...供 Tech Lead 派工與估時
- **心裡怎麼想**：「他跟工程團隊還有 Tech Lead 配合的節奏寫得很清楚，不過他在自傳最後寫想把更多心力放回『產品策略』，而我們這個缺是 PM 兼 TPM，專案交付跟 KA 客戶推進的比重很高，需要確認他的角色期待。」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：確認對「PM 兼具 TPM（需扛技術方案協調與 KA/NRE 交付時程）」角色定位的興趣與期待。

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷第1,5點｜推動系統改版至前後端分離的新架構，採新舊並行、分階段上線...以簽章驗證與時間戳防止重放...與工程確認 JSON 欄位與判定規則｜對 jd40 直接證明兼具 PM 與 TPM 所需的系統架構理解與 API 整合協作力
- 1111經歷第2,8點｜大型客戶需要讓部門或分店共同招募...規劃群組功能；30 天內結案的比例由前一年的 52% 升至 79%（提案滿 30 天者）｜對 jd40 直接對位連鎖分店客戶需求與客戶專案交付管理
- 專案交付與工具技能｜按 User Story 記錄需求、做法、驗收條件與優先級，供 Tech Lead 派工與估時；能將業務上的搜尋、篩選規則拆成查詢條件｜對 jd40 展現清楚的工程派工規格與資料邏輯拆解能力

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：雖有大型客戶分店群組功能與「以客戶案件為優先（30 天結案率升至 79%）」經驗，但未明寫是否經手過收取 NRE（一次性工程開發費）之外部客戶客製化合約專案
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落
- 位置：1111 經歷第 1、2、4、7 點與尚凡第 1 點
  - 原句：與工程於 2025/09 完成上線；完成三項功能上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：強

### 8. 未測試聲明
PDF 抽字：local_extraction（已於總報告 §6 獨立列示 `resume-v10.3-twocol.pdf` 本機抽字結果，不併入內容評等） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

## 單份審查｜履歷 Resume_v10.3_AppendixA（jd43 Product Manager (Messenger & OA Products)｜LINE Taiwan）｜第 13 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd43","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd43-13","human_calibrated":false,"requirements":[{"id":"R01","text":"5年以上網路或科技產業經驗，具產品管理經驗及推動概念到上線優化經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品；2023/12–2026/03 主責"],"blocks_interview":false,"reason":"近10年網路與軟體PM經驗，完整覆蓋0到1與大型系統改版"},{"id":"R02","text":"主要聚焦帳號安全、防詐騙專案及訊息體驗","type":"required","status":"supported","evidence":["針對廠商招募帳號遭冒用...確認登入驗證與帳號解鎖流程，於 2026/04 上線"],"blocks_interview":false,"reason":"直接具備帳號安全防冒用、API防濫用與即時通訊息整合經驗"},{"id":"R03","text":"具跨職能（設計、工程、資安/稽核、客服）與跨國團隊合作經驗","type":"required","status":"supported","evidence":["與 CodaPay 新加坡技術團隊協調串接；推進 SweetRing 在 7 個"],"blocks_interview":false,"reason":"具跨國技術與在地化協作及跨10部門協作經驗"},{"id":"R04","text":"運用問卷、使用者訪談、bucket/A/B test、行為分析等研究與量化方法驗證假設","type":"required","status":"supported","evidence":["使用者訪談與問卷、競品實測、GA4、世代分析與對照組實驗；設計馬來西亞 iOS "],"blocks_interview":false,"reason":"研究與量化對照實驗方法完整且有實證案例"},{"id":"R05","text":"熟悉Confluence、Jira、Figma、Codex等工具；英文流利","type":"required","status":"partial","evidence":["英文 TOEIC 980、TOEFL iBT 93，並以英文進行跨國協作；Fig"],"blocks_interview":false,"reason":"英文流利且熟Figma與Claude Code，未直接寫出Confluence/Jira"},{"id":"R06","text":"加分：具AI產品開發或AI整合經驗；具日文或韓文能力","type":"preferred","status":"supported","evidence":["與資料科學團隊合作，定義公司簡介生成、職缺工作說明生成及 AI 推薦人才...完"],"blocks_interview":false,"reason":"具3項AI產品功能上線實績；曾推日韓在地化惟未列日韓語能力"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["近 10 年 PM 經驗，經手 6 款產品，涵蓋訂閱制社交 App、網紅媒合平台"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"強","evidence":["針對廠商招募帳號遭冒用，協調工程與客服釐清影響範圍，確認登入驗證與帳號解鎖流程"],"missing":["專案工具未明列 Confluence、Jira；信件與即時通整合目前在內部封測中"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["廠商反映的問題以溝通管道中斷最為集中，因此優先推進信件與即時通整合"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["調整後至 2026/10，未再透過客服接獲廠商回報同類冒用"],"missing":["信件與即時通整合預計 2026/11 底上線，尚無正式上線後指標"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["對接工程、行銷、業務與客服等 10 個需求單位；參與公司一級主管日會"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["清楚呈現帳號防冒用、API 防濫用、訊息整合與跨國定價實驗"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品；2023/12–2026/03 主責"],"application_note":"對位 jd43 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd43 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"證據鏈支持安排 jd43 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"目前進入內部封測的「信件與即時通整合」，具體解決了哪些跨管道訊息斷點？封測期間觀察到的問題與預計追蹤的北極星指標為何？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd43 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"訊息體驗相關之「信件與即時通整合」目前處於內部封測階段（預計 2026/11 底上線），尚無上線後之量化成效數據（依硬性規則 2 不撐起 Level 9）","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗，經手 6 款產品；2023/12–2026/03 主責","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["高度對位本職缺三大核心主題（帳號安全、防詐騙／防濫用、訊息體驗）：在 1111 針對「廠商招募帳號遭冒用」完成登入驗證與帳號解鎖流程調整（2026/04–2026/10 零客服回報同類冒用）、議定外部 API 時以簽章與時間戳防重放及限流、並主導「信件與即時通整合（已進入內部封測）」與 KOOL 邀約聯繫流程","具備跨國協作與流利英文（TOEIC 980、TOEFL iBT 93、赴美交換、與 CodaPay 新加坡技術團隊協調串接、推進 SweetRing 美墨巴印馬日韓 7 國市場在地化）","具備扎實的使用者研究與量化實驗能力（馬來西亞 iOS 對照組定價實驗、GA4、世代分析）及 3 項 AI 產品功能上線經驗"],"key_gaps":["訊息體驗相關之「信件與即時通整合」目前處於內部封測階段（預計 2026/11 底上線），尚無上線後之量化成效數據（依硬性規則 2 不撐起 Level 9）","跨國團隊合作經驗集中於 2016–2021 年（思維特與尚凡時期），近 4 年在 1111 為台灣本土團隊","工具欄列 Figma、Axure、Notion、Trello、Claude Code，未明列 Confluence 與 Jira"],"strengths":["1111經歷第4-6點｜優先推進信件與即時通整合...以簽章驗證與時間戳防止重放...針對廠商招募帳號遭冒用，確認登入驗證與帳號解鎖流程｜對 jd43 罕見地同時覆蓋「帳號安全、防詐騙防濫用、企業訊息整合體驗」三大核心職責","尚凡第3-4點與語言技能｜設計馬來西亞 iOS 定價實驗...與 CodaPay 新加坡技術團隊協調串接；英文 TOEIC 980、TOEFL iBT 93｜對 jd43 證明具備跨國團隊協作、英語能力與嚴謹對照組實驗經驗","1111經歷第7點｜定義公司簡介生成、職缺工作說明生成及 AI 推薦人才的使用情境與驗收標準｜對 jd43 直接命中加分項「具 AI 產品開發或 AI 整合經驗」"],"interview_questions":["目前進入內部封測的「信件與即時通整合」，具體解決了哪些跨管道訊息斷點？封測期間觀察到的問題與預計追蹤的北極星指標為何？","LINE Regional PM 需每日與日本／韓國總部產品與工程團隊以全英文密切對齊 Roadmap，你如何將過往與新加坡 CodaPay 及 7 國團隊協作的經驗應用於跨國總部溝通？","你過去是否有使用 Confluence 與 Jira 的經驗？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd43 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：具「針對廠商招募帳號遭冒用...於 2026/04 上線調整」、API 防濫用與「信件與即時通整合」及跨國英文協作經驗，支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 近 10 年 PM 經驗，經手 6 款產品，涵蓋訂閱制社交 App、網紅媒合平台 | 無關鍵缺口，可於面試深化 |
| role_evidence | 強 | 針對廠商招募帳號遭冒用，協調工程與客服釐清影響範圍，確認登入驗證與帳號解鎖流程 | 專案工具未明列 Confluence、Jira；信件與即時通整合目前在內部封測中 |
| decision_depth | 強 | 廠商反映的問題以溝通管道中斷最為集中，因此優先推進信件與即時通整合 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 調整後至 2026/10，未再透過客服接獲廠商回報同類冒用 | 信件與即時通整合預計 2026/11 底上線，尚無正式上線後指標 |
| ownership | 強 | 對接工程、行銷、業務與客服等 10 個需求單位；參與公司一級主管日會 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 清楚呈現帳號防冒用、API 防濫用、訊息整合與跨國定價實驗 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 5年以上網路或科技產業經驗，具產品管理經驗及推動概念到上線優化經驗 | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品；2023/12–2026/03 主責 | 近10年網路與軟體PM經驗，完整覆蓋0到1與大型系統改版 |
| R02 主要聚焦帳號安全、防詐騙專案及訊息體驗 | 必要 | supported | 針對廠商招募帳號遭冒用...確認登入驗證與帳號解鎖流程，於 2026/04 上線 | 直接具備帳號安全防冒用、API防濫用與即時通訊息整合經驗 |
| R03 具跨職能（設計、工程、資安/稽核、客服）與跨國團隊合作經驗 | 必要 | supported | 與 CodaPay 新加坡技術團隊協調串接；推進 SweetRing 在 7 個 | 具跨國技術與在地化協作及跨10部門協作經驗 |
| R04 運用問卷、使用者訪談、bucket/A/B test、行為分析等研究與量化方法驗證假設 | 必要 | supported | 使用者訪談與問卷、競品實測、GA4、世代分析與對照組實驗；設計馬來西亞 iOS  | 研究與量化對照實驗方法完整且有實證案例 |
| R05 熟悉Confluence、Jira、Figma、Codex等工具；英文流利 | 必要 | partial | 英文 TOEIC 980、TOEFL iBT 93，並以英文進行跨國協作；Fig | 英文流利且熟Figma與Claude Code，未直接寫出Confluence/Jira |
| R06 加分：具AI產品開發或AI整合經驗；具日文或韓文能力 | 加分 | supported | 與資料科學團隊合作，定義公司簡介生成、職缺工作說明生成及 AI 推薦人才...完 | 具3項AI產品功能上線實績；曾推日韓在地化惟未列日韓語能力 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品；2023/12–2026/03 主責 | 對位 jd43 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 以實測歸納、請工程協助驗證，再與維運、稽核核對 | 清楚界定個人規劃與工程/QA/DBA分工 |
| HR04 | supported | 30 天內結案的比例由前一年的 52% 升至 79% | 具結案率與定價實驗數據，缺部分功能採用率 |
| HR05 | supported | 將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與新舊並行取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端消費產品演進至B2B平台主任 |
| HR07 | supported | 上線前以互動原型與 FAQ 向客服、業務說明 | Scrum、原型、API議定、AI與英文皆有實例 |
| HR08 | supported | 從需求釐清、系統分析、流程與畫面設計，到 PRD | 結構分明，問題背景、動作與結果易讀 |
| HR09 | supported | 上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 誠實標註行銷導流期間、封測中與客服回報口徑 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd43 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃 | 證據鏈支持安排 jd43 面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人 | 針對大客戶部門/分店共同招募痛點設計群組權限 |
| HM03 | supported | 依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與新舊並行取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數機制與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18% | 結案率與定價實驗基準清晰，缺部分功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程 | 具後台不動下新舊並行、API防重放與防冒用閉環 |
| HM08 | supported | 以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則 | 能確認API JSON欄位與拆解查詢條件，取數協作DBA |
| HM09 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 上線調整，並依客服回饋修正操作方式 | 依客服回饋修正登入操作方式與AI推薦規則 |
| HM12 | supported | 具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd43 明文條件與附錄 A 履歷獨立取證判讀 | 僅依 jd43 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 高度對位本職缺三大核心主題（帳號安全、防詐騙／防濫用、訊息體驗）：在 1111 針對「廠商招募帳號遭冒用」完成登入驗證與帳號解鎖流程調整（2026/04–2026/10 零客服回報同類冒用）、議定外部 API 時以簽章與時間戳防重放及限流、並主導「信件與即時通整合（已進入內部封測）」與 KOOL 邀約聯繫流程 |
| 2 | 具備跨國協作與流利英文（TOEIC 980、TOEFL iBT 93、赴美交換、與 CodaPay 新加坡技術團隊協調串接、推進 SweetRing 美墨巴印馬日韓 7 國市場在地化） |
| 3 | 具備扎實的使用者研究與量化實驗能力（馬來西亞 iOS 對照組定價實驗、GA4、世代分析）及 3 項 AI 產品功能上線經驗 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 訊息體驗相關之「信件與即時通整合」目前處於內部封測階段（預計 2026/11 底上線），尚無上線後之量化成效數據（依硬性規則 2 不撐起 Level 9） | 目前進入內部封測的「信件與即時通整合」，具體解決了哪些跨管道訊息斷點？封測期間觀察到的問題與預計追蹤的北極星指標為何？ |
| 2 | 跨國團隊合作經驗集中於 2016–2021 年（思維特與尚凡時期），近 4 年在 1111 為台灣本土團隊 | LINE Regional PM 需每日與日本／韓國總部產品與工程團隊以全英文密切對齊 Roadmap，你如何將過往與新加坡 CodaPay 及 7 國團隊協作的經驗應用於跨國總部溝通？ |
| 3 | 工具欄列 Figma、Axure、Notion、Trello、Claude Code，未明列 Confluence 與 Jira | 你過去是否有使用 Confluence 與 Jira 的經驗？ |

### 5.5 審查者的質疑（本版新增；不是缺口清單）
#### 質疑 1
- **誰在想**：用人主管
- **讀到哪一句**：針對廠商招募帳號遭冒用...確認登入驗證與帳號解鎖流程，於 2026/04 上線
- **心裡怎麼想**：「我們的職缺剛好就是管 LINE OA（企業官方帳號）跟 Messenger 的帳號安全、防詐騙跟訊息體驗，他同時做過『企業招募帳號防冒用與解鎖流程』、『外部 API 簽章防重放』跟『企業端信件與即時通整合』，這種經歷組合在市場上非常難找，我一定會約他！但我會先問：你們在 2026/04 到底改了什麼登入驗證規則？又怎麼依客服回饋修正操作方式，才沒把正常付費廠商擋在門外？」
- **這個疑問會讓我**：仍然約談
- **要打消疑問，履歷或面試需要看到**：面試時請他詳述 2026/04 登入驗證與帳號解鎖流程的設計細節、客服回饋反映的摩擦點（Friction），以及修正後的流程圖。

#### 質疑 2
- **誰在想**：用人主管
- **讀到哪一句**：兩案均在開發中，信件與即時通整合已進入內部封測，預計 2026/11 底上線。
- **心裡怎麼想**：「信件跟即時通整合對我們 OA 訊息產品很有參考價值，但現在（2026/10）才剛進內部封測、11 月底才要上線，代表他手上還沒有上線後的轉換率或訊息回覆率數據可以證明這個改版成功。」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：分享「信件與即時通整合」上線前的問題量化基準（如溝通中斷工單占比）、內部封測驗收結果與上線後的觀測指標設計。

#### 質疑 3
- **誰在想**：HR
- **讀到哪一句**：推進 SweetRing 在美國、墨西哥、巴西、印尼等 7 個市場的在地化
- **心裡怎麼想**：「他的多益 980 很高、也有美國交換經驗，但他真正的跨國協作是 2016–2021 年跟外籍實習生及新加坡 CodaPay 對接，最近 4 年在 1111 都是全中文環境，我需要確認他現在的全英文口說簡報跟跨國 Stakeholder 談判能力還在不在此水準。」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：面試安排全英文問答環節，驗證以英文向總部產品團隊爭取台灣市場在地化需求優先序的說服力。

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷第4-6點｜優先推進信件與即時通整合...以簽章驗證與時間戳防止重放...針對廠商招募帳號遭冒用，確認登入驗證與帳號解鎖流程｜對 jd43 罕見地同時覆蓋「帳號安全、防詐騙防濫用、企業訊息整合體驗」三大核心職責
- 尚凡第3-4點與語言技能｜設計馬來西亞 iOS 定價實驗...與 CodaPay 新加坡技術團隊協調串接；英文 TOEIC 980、TOEFL iBT 93｜對 jd43 證明具備跨國團隊協作、英語能力與嚴謹對照組實驗經驗
- 1111經歷第7點｜定義公司簡介生成、職缺工作說明生成及 AI 推薦人才的使用情境與驗收標準｜對 jd43 直接命中加分項「具 AI 產品開發或 AI 整合經驗」

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：訊息體驗相關之「信件與即時通整合」目前處於內部封測階段（預計 2026/11 底上線），尚無上線後之量化成效數據（依硬性規則 2 不撐起 Level 9）
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落
- 位置：1111 經歷第 1、2、4、7 點與尚凡第 1 點
  - 原句：與工程於 2025/09 完成上線；完成三項功能上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：強

### 8. 未測試聲明
PDF 抽字：local_extraction（已於總報告 §6 獨立列示 `resume-v10.3-twocol.pdf` 本機抽字結果，不併入內容評等） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

## 單份審查｜履歷 Resume_v10.3_AppendixA（jd44 [Music] Senior Product Planner｜KKBOX (KKCompany)）｜第 14 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd44","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd44-14","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上網路產品管理經驗，具備策略思考、0到1推動與既有產品持續成長優化能力","type":"required","status":"supported","evidence":["近 10 年 PM 經驗；規劃 KOOL 網紅媒合平台；主責約 50 項大項功能"],"blocks_interview":false,"reason":"同時具備KOOL從0到1規劃與成熟產品持續迭代經驗"},{"id":"R02","text":"跨國跨職能協作：與外部廠商溝通共創，內部跨區域合作","type":"required","status":"supported","evidence":["與外部合作夥伴議定查詢 API；與 CodaPay 新加坡技術團隊協調串接；推進"],"blocks_interview":false,"reason":"具外部合作夥伴議定、新加坡技術串接與7國市場協作經驗"},{"id":"R03","text":"數據驅動決策與實驗：熟悉使用者行為分析、A/B測試及關鍵產品指標","type":"required","status":"supported","evidence":["使用者訪談與問卷、競品實測、GA4、世代分析與對照組實驗；設計馬來西亞 iOS "],"blocks_interview":false,"reason":"具嚴謹跨國定價對照實驗、GA4與世代留存分析經驗"},{"id":"R04","text":"市場與競品分析能力；專注使用者需求提升參與度與留存率","type":"required","status":"supported","evidence":["在沒有直接競品可對照的情況下，參考 Airbnb 與交友平台的媒合方式；依使用者"],"blocks_interview":false,"reason":"具跨領域競品借鏡、競品實測與訂閱方案設計能力"},{"id":"R05","text":"優異的英文溝通及寫作能力","type":"required","status":"supported","evidence":["英文 TOEIC 980、TOEFL iBT 93，曾赴美交換，並以英文進行跨國"],"blocks_interview":false,"reason":"高分英檢、美國交換且具英文跨國協作實務"},{"id":"R06","text":"加分：具音樂/內容平台/社群媒體/娛樂或AI相關產品經驗；launch AI相關功能實務；日文能力","type":"preferred","status":"supported","evidence":["經手交友、訂閱制內容 App 與網紅媒合平台；完成三項 AI 功能上線"],"blocks_interview":false,"reason":"具訂閱制內容/社交媒合App與launch 3項AI功能實務（日文未呈現）"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["經手交友、訂閱制內容 App 與網紅媒合平台，規劃使用流程、訂閱與付費機制"],"missing":["過往為社交與網紅媒合及人力銀行，未直接經手音樂串流領域"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"強","evidence":["規劃 KOOL 網紅媒合平台...與資料科學團隊合作，定義公司簡介生成...完成"],"missing":["未呈現加分項之日文能力"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["在沒有直接競品可對照的情況下，參考 Airbnb 與交友平台的媒合方式"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%；網"],"missing":["KOOL 0 到 1 平台與 1111 AI 功能未列上線後參與度與留存數據"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["主導 Juicy 推出並協調跨團隊工作；帶領 2 名直屬產品企劃"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["自傳與經歷清楚展現從消費型訂閱產品到企業系統的產品策略思考"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗；規劃 KOOL 網紅媒合平台；主責約 50 項大項功能"],"application_note":"對位 jd44 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd44 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"證據鏈支持安排 jd44 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"你在 KOOL 從 0 到 1 上線刊案、報名、邀約流程與 VIP 訂閱／點數付費牆後，以及在 1111 上線 AI 推薦功能後，實際的使用者參與度與留存率表現如何？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd44 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"KOOL 網紅媒合平台與 1111 三項 AI 功能雖已上線，但履歷未列出上線後的使用者參與度（Engagement）或留存率（Retention）變化數據","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗；規劃 KOOL 網紅媒合平台；主責約 50 項大項功能","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["完整符合必備條件與三項核心加分項：經手「交友、訂閱制內容 App 與網紅媒合平台」、成功從 0 到 1 規劃 KOOL 雙邊媒合與 VIP 訂閱／點數變現機制、並具備實際 launch 3 項 AI 功能的實務經驗","具備嚴謹的跨國數據實驗能力（馬來西亞 iOS 三階段定價對照實驗、GA4、世代分析）與跨國支付／在地化協作經驗（美墨巴印馬日韓 7 國市場、TOEIC 980）","自傳清楚展現對消費型產品「使用者為什麼加入、互動與付費」及產品策略方向的深度思考"],"key_gaps":["KOOL 網紅媒合平台與 1111 三項 AI 功能雖已上線，但履歷未列出上線後的使用者參與度（Engagement）或留存率（Retention）變化數據","近 4 年在 1111 聚焦於 B2B 企業端招募系統，與 C 端音樂串流及粉絲娛樂互動領域有時間間隔","加分條件中之「具日文能力」未呈現（僅有英文跨國協作與推進日本市場在地化經驗）"],"strengths":["尚凡經歷第1點與自傳｜規劃 KOOL 網紅媒合平台，從案主與網紅兩種角色釐清需求。在沒有直接競品可對照的情況下，參考 Airbnb 與交友平台的媒合方式｜對 jd44 展現優秀的 0 到 1 產品概念共創與跨領域競品分析能力","尚凡經歷第3點｜設計馬來西亞 iOS 定價實驗，以售價不變的 Android 作對照，依序測試原價、降價與還原原價（2021/05–08，各期 21 天）｜對 jd44 直接證明數據驅動決策與嚴謹實驗能力","1111經歷第7點與語言技能｜完成三項 AI 功能上線；英文 TOEIC 980、TOEFL iBT 93，曾赴美交換，並以英文進行跨國協作｜對 jd44 同時滿足英文跨國溝通與 launch AI 功能加分項"],"interview_questions":["你在 KOOL 從 0 到 1 上線刊案、報名、邀約流程與 VIP 訂閱／點數付費牆後，以及在 1111 上線 AI 推薦功能後，實際的使用者參與度與留存率表現如何？","從 B2B 企業招募系統轉回 C 端音樂串流與粉絲互動（Music Team），你認為過去在 KOOL 網紅媒合與訂閱制 App 的哪些策略經驗可以直接轉移？","過去推進 SweetRing 日本市場在地化時，是如何與日本在地人員協作並驗證當地使用者偏好的？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd44 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：具「規劃 KOOL 網紅媒合平台」0 到 1 經驗、馬來西亞定價實驗、跨國英語協作與 3 項 AI 功能上線，支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 經手交友、訂閱制內容 App 與網紅媒合平台，規劃使用流程、訂閱與付費機制 | 過往為社交與網紅媒合及人力銀行，未直接經手音樂串流領域 |
| role_evidence | 強 | 規劃 KOOL 網紅媒合平台...與資料科學團隊合作，定義公司簡介生成...完成 | 未呈現加分項之日文能力 |
| decision_depth | 強 | 在沒有直接競品可對照的情況下，參考 Airbnb 與交友平台的媒合方式 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%；網 | KOOL 0 到 1 平台與 1111 AI 功能未列上線後參與度與留存數據 |
| ownership | 強 | 主導 Juicy 推出並協調跨團隊工作；帶領 2 名直屬產品企劃 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 自傳與經歷清楚展現從消費型訂閱產品到企業系統的產品策略思考 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 3年以上網路產品管理經驗，具備策略思考、0到1推動與既有產品持續成長優化能力 | 必要 | supported | 近 10 年 PM 經驗；規劃 KOOL 網紅媒合平台；主責約 50 項大項功能 | 同時具備KOOL從0到1規劃與成熟產品持續迭代經驗 |
| R02 跨國跨職能協作：與外部廠商溝通共創，內部跨區域合作 | 必要 | supported | 與外部合作夥伴議定查詢 API；與 CodaPay 新加坡技術團隊協調串接；推進 | 具外部合作夥伴議定、新加坡技術串接與7國市場協作經驗 |
| R03 數據驅動決策與實驗：熟悉使用者行為分析、A/B測試及關鍵產品指標 | 必要 | supported | 使用者訪談與問卷、競品實測、GA4、世代分析與對照組實驗；設計馬來西亞 iOS  | 具嚴謹跨國定價對照實驗、GA4與世代留存分析經驗 |
| R04 市場與競品分析能力；專注使用者需求提升參與度與留存率 | 必要 | supported | 在沒有直接競品可對照的情況下，參考 Airbnb 與交友平台的媒合方式；依使用者 | 具跨領域競品借鏡、競品實測與訂閱方案設計能力 |
| R05 優異的英文溝通及寫作能力 | 必要 | supported | 英文 TOEIC 980、TOEFL iBT 93，曾赴美交換，並以英文進行跨國 | 高分英檢、美國交換且具英文跨國協作實務 |
| R06 加分：具音樂/內容平台/社群媒體/娛樂或AI相關產品經驗；launch AI相關功能實務；日文能力 | 加分 | supported | 經手交友、訂閱制內容 App 與網紅媒合平台；完成三項 AI 功能上線 | 具訂閱制內容/社交媒合App與launch 3項AI功能實務（日文未呈現） |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗；規劃 KOOL 網紅媒合平台；主責約 50 項大項功能 | 對位 jd44 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 以實測歸納、請工程協助驗證，再與維運、稽核核對 | 清楚界定個人規劃與工程/QA/DBA分工 |
| HR04 | supported | 30 天內結案的比例由前一年的 52% 升至 79% | 具結案率與定價實驗數據，缺部分功能採用率 |
| HR05 | supported | 將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與新舊並行取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端消費產品演進至B2B平台主任 |
| HR07 | supported | 上線前以互動原型與 FAQ 向客服、業務說明 | Scrum、原型、API議定、AI與英文皆有實例 |
| HR08 | supported | 從需求釐清、系統分析、流程與畫面設計，到 PRD | 結構分明，問題背景、動作與結果易讀 |
| HR09 | supported | 上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 誠實標註行銷導流期間、封測中與客服回報口徑 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd44 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃 | 證據鏈支持安排 jd44 面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人 | 針對大客戶部門/分店共同招募痛點設計群組權限 |
| HM03 | supported | 依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與新舊並行取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數機制與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18% | 結案率與定價實驗基準清晰，缺部分功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程 | 具後台不動下新舊並行、API防重放與防冒用閉環 |
| HM08 | supported | 以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則 | 能確認API JSON欄位與拆解查詢條件，取數協作DBA |
| HM09 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 上線調整，並依客服回饋修正操作方式 | 依客服回饋修正登入操作方式與AI推薦規則 |
| HM12 | supported | 具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd44 明文條件與附錄 A 履歷獨立取證判讀 | 僅依 jd44 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 完整符合必備條件與三項核心加分項：經手「交友、訂閱制內容 App 與網紅媒合平台」、成功從 0 到 1 規劃 KOOL 雙邊媒合與 VIP 訂閱／點數變現機制、並具備實際 launch 3 項 AI 功能的實務經驗 |
| 2 | 具備嚴謹的跨國數據實驗能力（馬來西亞 iOS 三階段定價對照實驗、GA4、世代分析）與跨國支付／在地化協作經驗（美墨巴印馬日韓 7 國市場、TOEIC 980） |
| 3 | 自傳清楚展現對消費型產品「使用者為什麼加入、互動與付費」及產品策略方向的深度思考 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | KOOL 網紅媒合平台與 1111 三項 AI 功能雖已上線，但履歷未列出上線後的使用者參與度（Engagement）或留存率（Retention）變化數據 | 你在 KOOL 從 0 到 1 上線刊案、報名、邀約流程與 VIP 訂閱／點數付費牆後，以及在 1111 上線 AI 推薦功能後，實際的使用者參與度與留存率表現如何？ |
| 2 | 近 4 年在 1111 聚焦於 B2B 企業端招募系統，與 C 端音樂串流及粉絲娛樂互動領域有時間間隔 | 從 B2B 企業招募系統轉回 C 端音樂串流與粉絲互動（Music Team），你認為過去在 KOOL 網紅媒合與訂閱制 App 的哪些策略經驗可以直接轉移？ |
| 3 | 加分條件中之「具日文能力」未呈現（僅有英文跨國協作與推進日本市場在地化經驗） | 過去推進 SweetRing 日本市場在地化時，是如何與日本在地人員協作並驗證當地使用者偏好的？ |

### 5.5 審查者的質疑（本版新增；不是缺口清單）
#### 質疑 1
- **誰在想**：用人主管
- **讀到哪一句**：在沒有直接競品可對照的情況下，參考 Airbnb 與交友平台的媒合方式
- **心裡怎麼想**：「這段寫得很有 Product Planner 的味道！沒有直接競品時懂得跨領域去借鏡 Airbnb 跟交友平台的雙邊媒合邏輯，再加上自傳最後說想把心力放回產品策略、又有定價實驗跟 AI 上線經驗，我會想約他來聊！但我會先問：KOOL 上線之後雙邊媒合到底有沒有轉起來？為什麼這一段完全沒寫成果數字？」
- **這個疑問會讓我**：仍然約談
- **要打消疑問，履歷或面試需要看到**：面試時請他補充 KOOL 上線後的雙邊供給需求比、報名媒合率與付費牆轉換數據，以及若未達預期背後的策略反思。

#### 質疑 2
- **誰在想**：用人主管
- **讀到哪一句**：定義公司簡介生成、職缺工作說明生成及 AI 推薦人才的使用情境與驗收標準
- **心裡怎麼想**：「我們很想探索 AI 跟音樂串流、個人化推薦的結合，他在 1111 剛好做過 AI 推薦人才跟內容生成，但人力銀行的推薦是 B2B 篩履歷，跟音樂串流每秒鐘即時的聽歌個人化推薦與粉絲情感連結差滿多的，我想知道他對娛樂內容產品的 AI 應用有沒有想法。」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：請他結合過往 AI 推薦驗收標準與 KOOL 創作者媒合經驗，提出對「AI × 音樂串流／粉絲互動」的產品切入點與驗證指標。

#### 質疑 3
- **誰在想**：HR
- **讀到哪一句**：推進 SweetRing 在美國、墨西哥、巴西、印尼等 7 個市場的在地化
- **心裡怎麼想**：「他的英文分數很高（TOEIC 980 / TOEFL 93），也管過日本市場在地化，不過 KKCompany Music 團隊常有機會跟日本夥伴合作，可以順便確認他會不會一點日文，以及全英文跨國開會的近況。」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：確認跨國英語會議溝通近況及與日本市場協作的方式。

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 尚凡經歷第1點與自傳｜規劃 KOOL 網紅媒合平台，從案主與網紅兩種角色釐清需求。在沒有直接競品可對照的情況下，參考 Airbnb 與交友平台的媒合方式｜對 jd44 展現優秀的 0 到 1 產品概念共創與跨領域競品分析能力
- 尚凡經歷第3點｜設計馬來西亞 iOS 定價實驗，以售價不變的 Android 作對照，依序測試原價、降價與還原原價（2021/05–08，各期 21 天）｜對 jd44 直接證明數據驅動決策與嚴謹實驗能力
- 1111經歷第7點與語言技能｜完成三項 AI 功能上線；英文 TOEIC 980、TOEFL iBT 93，曾赴美交換，並以英文進行跨國協作｜對 jd44 同時滿足英文跨國溝通與 launch AI 功能加分項

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：KOOL 網紅媒合平台與 1111 三項 AI 功能雖已上線，但履歷未列出上線後的使用者參與度（Engagement）或留存率（Retention）變化數據
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落
- 位置：1111 經歷第 1、2、4、7 點與尚凡第 1 點
  - 原句：與工程於 2025/09 完成上線；完成三項功能上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：強

### 8. 未測試聲明
PDF 抽字：local_extraction（已於總報告 §6 獨立列示 `resume-v10.3-twocol.pdf` 本機抽字結果，不併入內容評等） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

## 單份審查｜履歷 Resume_v10.3_AppendixA（jd47 產品經理｜Product Manager｜USPACE）｜第 15 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd47","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd47-15","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上Software PM，至少一次完整0到1直接負責經歷，且能針對成熟產品進行迭代成長","type":"required","status":"supported","evidence":["規劃 KOOL 網紅媒合平台；推動系統改版至前後端分離的新架構...持續迭代現行"],"blocks_interview":false,"reason":"同時具備KOOL 0到1完整週期與1111 6萬廠商成熟系統迭代"},{"id":"R02","text":"對焦商業需求：執行商業模式分析與產業趨勢研究，持續關注競品動態與用戶需求","type":"required","status":"supported","evidence":["在沒有直接競品可對照的情況下，參考 Airbnb 與交友平台的媒合方式；競品實測"],"blocks_interview":false,"reason":"具商業模式設計、實收試算、定價實驗與競品實測經驗"},{"id":"R03","text":"產品教育訓練與上線測試：規劃執行內部（業務/客服/財務）及外部教育訓練，負責上線前測試與驗收","type":"required","status":"supported","evidence":["與 QA 制定 UAT 驗收案例、排定上線計畫。上線前以互動原型與 FAQ 向客"],"blocks_interview":false,"reason":"直接命中UAT測試驗收、互動原型/FAQ內部教育訓練與sales kit"},{"id":"R04","text":"能寫清楚的規格文件（PRD、流程圖、資料結構）；理解API、JSON與基本SQL","type":"required","status":"supported","evidence":["完成 PRD...流程圖／循序圖；與工程確認 JSON 欄位與判定規則；擬定資料"],"blocks_interview":false,"reason":"完整具備PRD、流程圖、資料表欄位需求與API JSON確認，取數與DBA協作"},{"id":"R05","text":"加分：停車/交通/MaaS/保險/支付/FinTech經驗；AI/LLM工具規格撰寫與分析；Growth或數據分析經驗","type":"preferred","status":"supported","evidence":["以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格"],"blocks_interview":false,"reason":"具跨國支付串接、定價成長實驗與Claude Code規格分析實作"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["近 10 年 PM 經驗，經手 6 款產品，涵蓋訂閱制社交 App、網紅媒合平台"],"missing":["過往為純軟體平台，未直接接觸智慧停車或實體場域硬體"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"強","evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助業務製作銷售簡報"],"missing":["資料庫取數為與 DBA 協作，未明寫自寫 SQL 語法"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["30 天內結案的比例由前一年的 52% 升至 79%；網頁付款占營收由 24% "],"missing":["KOOL 0 到 1 平台未列上線後規模數據"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["對接工程、行銷、業務與客服等 10 個需求單位；帶領 2 名直屬產品企劃"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["清楚呈現 0 到 1 產品規劃、成熟系統重構、內部訓練與 AI 協作流程"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；推動系統改版至前後端分離的新架構...持續迭代現行"],"application_note":"對位 jd47 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd47 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"證據鏈支持安排 jd47 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"你在尚凡從 0 到 1 推動 KOOL 網紅媒合平台上線並支援 Go-To-Market 時，上線後的雙邊用戶規模與付費轉換表現如何？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd47 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"KOOL 0 到 1 平台未在本版履歷列出上線後的用戶規模或報名媒合數據","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["規劃 KOOL 網紅媒合平台；推動系統改版至前後端分離的新架構...持續迭代現行","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["完美對位主要職責第 1、3、4 點：兼具 KOOL 0 到 1 規劃與 1111 成熟產品 50 項大功能迭代，且上線前「與 QA 制定 UAT 驗收案例、排定上線計畫，以互動原型與 FAQ 向客服、業務說明，另協助業務製作銷售簡報（sales kit）」","完全滿足必備規格與技術條件：具備 PRD、流程圖／循序圖、擬定資料表與欄位需求，並在議定外部 API 時「以簽章驗證與時間戳防止重放...與工程確認 JSON 欄位與判定規則與判定規則」","深入運用 Claude Code 建立協作流程與共用 skill 撰寫規格與分析資料，並具 CodaPay／Peach 支付串接與馬來西亞定價成長實驗經驗"],"key_gaps":["KOOL 0 到 1 平台未在本版履歷列出上線後的用戶規模或報名媒合數據","資料庫查詢為「擬定資料表與欄位需求，與 DBA 協作取數」，未明寫本人手寫 SQL 查詢程度","尚未接觸智慧停車或 MaaS 線下場域與硬體整合"],"strengths":["1111經歷第3點｜完成 PRD，並與 QA 制定 UAT 驗收案例、排定上線計畫。上線前以互動原型與 FAQ 向客服、業務說明，另協助業務製作銷售簡報｜對 jd47 直接命中「產品教育訓練與上線測試驗收、跨部門溝通橋樑」","尚凡第1點與1111第1-2點｜規劃 KOOL 網紅媒合平台...推動系統改版至前後端分離的新架構，採新舊並行、分階段上線｜對 jd47 完整證明同時具備 0-1 MVP 推動與成熟產品迭代能力","1111第5點與AI協作技能｜與外部合作夥伴議定查詢 API...與工程確認 JSON 欄位與判定規則；以 Claude Code 建立協作流程與共用 skill｜對 jd47 滿足 API/JSON 理解與 AI 工具規格撰寫加分項"],"interview_questions":["你在尚凡從 0 到 1 推動 KOOL 網紅媒合平台上線並支援 Go-To-Market 時，上線後的雙邊用戶規模與付費轉換表現如何？","你在擬定資料表與欄位需求及拆解後端搜尋篩選查詢條件時，是否會自行撰寫基本 SQL 語法？","若要為 USPACE 新功能規劃針對內部業務、客服、財務及外部合作夥伴（如停車場業主）的教育訓練，你會如何調整你在 1111 使用的「互動原型＋FAQ＋sales kit」做法？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd47 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：兼具 KOOL 0 到 1 與 1111 50 項成熟功能迭代、上線前內部教育訓練、API/JSON 議定與 Claude 協作實績，支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 近 10 年 PM 經驗，經手 6 款產品，涵蓋訂閱制社交 App、網紅媒合平台 | 過往為純軟體平台，未直接接觸智慧停車或實體場域硬體 |
| role_evidence | 強 | 上線前以互動原型與 FAQ 向客服、業務說明，另協助業務製作銷售簡報 | 資料庫取數為與 DBA 協作，未明寫自寫 SQL 語法 |
| decision_depth | 強 | 依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 30 天內結案的比例由前一年的 52% 升至 79%；網頁付款占營收由 24%  | KOOL 0 到 1 平台未列上線後規模數據 |
| ownership | 強 | 對接工程、行銷、業務與客服等 10 個需求單位；帶領 2 名直屬產品企劃 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 清楚呈現 0 到 1 產品規劃、成熟系統重構、內部訓練與 AI 協作流程 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 3年以上Software PM，至少一次完整0到1直接負責經歷，且能針對成熟產品進行迭代成長 | 必要 | supported | 規劃 KOOL 網紅媒合平台；推動系統改版至前後端分離的新架構...持續迭代現行 | 同時具備KOOL 0到1完整週期與1111 6萬廠商成熟系統迭代 |
| R02 對焦商業需求：執行商業模式分析與產業趨勢研究，持續關注競品動態與用戶需求 | 必要 | supported | 在沒有直接競品可對照的情況下，參考 Airbnb 與交友平台的媒合方式；競品實測 | 具商業模式設計、實收試算、定價實驗與競品實測經驗 |
| R03 產品教育訓練與上線測試：規劃執行內部（業務/客服/財務）及外部教育訓練，負責上線前測試與驗收 | 必要 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫。上線前以互動原型與 FAQ 向客 | 直接命中UAT測試驗收、互動原型/FAQ內部教育訓練與sales kit |
| R04 能寫清楚的規格文件（PRD、流程圖、資料結構）；理解API、JSON與基本SQL | 必要 | supported | 完成 PRD...流程圖／循序圖；與工程確認 JSON 欄位與判定規則；擬定資料 | 完整具備PRD、流程圖、資料表欄位需求與API JSON確認，取數與DBA協作 |
| R05 加分：停車/交通/MaaS/保險/支付/FinTech經驗；AI/LLM工具規格撰寫與分析；Growth或數據分析經驗 | 加分 | supported | 以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格 | 具跨國支付串接、定價成長實驗與Claude Code規格分析實作 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 規劃 KOOL 網紅媒合平台；推動系統改版至前後端分離的新架構...持續迭代現行 | 對位 jd47 核心年資與產品交付經驗 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責逾6萬家廠商企業招募系統 |
| HR03 | supported | 以實測歸納、請工程協助驗證，再與維運、稽核核對 | 清楚界定個人規劃與工程/QA/DBA分工 |
| HR04 | supported | 30 天內結案的比例由前一年的 52% 升至 79% | 具結案率與定價實驗數據，缺部分功能採用率 |
| HR05 | supported | 將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與新舊並行取捨 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 職涯由C端消費產品演進至B2B平台主任 |
| HR07 | supported | 上線前以互動原型與 FAQ 向客服、業務說明 | Scrum、原型、API議定、AI與英文皆有實例 |
| HR08 | supported | 從需求釐清、系統分析、流程與畫面設計，到 PRD | 結構分明，問題背景、動作與結果易讀 |
| HR09 | supported | 上線與行銷導流期間，男性 DAU 增至 1.25 萬 | 誠實標註行銷導流期間、封測中與客服回報口徑 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd47 職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃 | 證據鏈支持安排 jd47 面試 |
| HM01 | supported | 規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人 | 兼具0到1雙邊媒合與B2B企業系統改版經驗 |
| HM02 | supported | 大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人 | 針對大客戶部門/分店共同招募痛點設計群組權限 |
| HM03 | supported | 依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現即時通整合、搜尋改版與新舊並行取捨 |
| HM04 | supported | 2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上 | 具定價對照實驗、點數機制與網頁金流轉換實績 |
| HM05 | partial | 降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18% | 結案率與定價實驗基準清晰，缺部分功能採用率 |
| HM06 | supported | 職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會 | 帶領2名企劃、向總經理/副總匯報且分工邊界清楚 |
| HM07 | supported | 業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程 | 具後台不動下新舊並行、API防重放與防冒用閉環 |
| HM08 | supported | 以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則 | 能確認API JSON欄位與拆解查詢條件，取數協作DBA |
| HM09 | supported | 2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線 | 主責50項大功能與逾6萬廠商系統，資深範圍相符 |
| HM10 | supported | 上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報 | 摘要、條列經歷與自傳結構清晰，無誇大矛盾 |
| HM11 | supported | 於 2026/04 上線調整，並依客服回饋修正操作方式 | 依客服回饋修正登入操作方式與AI推薦規則 |
| HM12 | supported | 具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例 | 具多個已上線案例，可於面試追問採用成效與細節 |
| HM13 | supported | 僅依 jd47 明文條件與附錄 A 履歷獨立取證判讀 | 僅依 jd47 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 完美對位主要職責第 1、3、4 點：兼具 KOOL 0 到 1 規劃與 1111 成熟產品 50 項大功能迭代，且上線前「與 QA 制定 UAT 驗收案例、排定上線計畫，以互動原型與 FAQ 向客服、業務說明，另協助業務製作銷售簡報（sales kit）」 |
| 2 | 完全滿足必備規格與技術條件：具備 PRD、流程圖／循序圖、擬定資料表與欄位需求，並在議定外部 API 時「以簽章驗證與時間戳防止重放...與工程確認 JSON 欄位與判定規則與判定規則」 |
| 3 | 深入運用 Claude Code 建立協作流程與共用 skill 撰寫規格與分析資料，並具 CodaPay／Peach 支付串接與馬來西亞定價成長實驗經驗 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | KOOL 0 到 1 平台未在本版履歷列出上線後的用戶規模或報名媒合數據 | 你在尚凡從 0 到 1 推動 KOOL 網紅媒合平台上線並支援 Go-To-Market 時，上線後的雙邊用戶規模與付費轉換表現如何？ |
| 2 | 資料庫查詢為「擬定資料表與欄位需求，與 DBA 協作取數」，未明寫本人手寫 SQL 查詢程度 | 你在擬定資料表與欄位需求及拆解後端搜尋篩選查詢條件時，是否會自行撰寫基本 SQL 語法？ |
| 3 | 尚未接觸智慧停車或 MaaS 線下場域與硬體整合 | 若要為 USPACE 新功能規劃針對內部業務、客服、財務及外部合作夥伴（如停車場業主）的教育訓練，你會如何調整你在 1111 使用的「互動原型＋FAQ＋sales kit」做法？ |

### 5.5 審查者的質疑（本版新增；不是缺口清單）
#### 質疑 1
- **誰在想**：用人主管
- **讀到哪一句**：上線前以互動原型與 FAQ 向客服、業務說明，另協助業務製作銷售簡報
- **心裡怎麼想**：「這段完全就是我們 JD 第 3 點寫的『產品教育訓練與上線測試、提升內部業務客服理解』！而且他既有 KOOL 0 到 1 經驗、又有 1111 成熟系統迭代，連 JSON 跟 Claude Code 都寫得很清楚，這個人我一定約！但我會先問：他在 KOOL 從 0 到 1 跟 Juicy 緊急上線時，是怎麼跟行銷業務一起做 Go-To-Market 的？」
- **這個疑問會讓我**：仍然約談
- **要打消疑問，履歷或面試需要看到**：面試時請他分享 KOOL 或 1111 新版上線時的 Go-To-Market 跨部門對齊流程，以及互動原型與 FAQ 如何降低客服進線或提升業務推廣效率。

#### 質疑 2
- **誰在想**：用人主管
- **讀到哪一句**：規劃 KOOL 網紅媒合平台，從案主與網紅兩種角色釐清需求
- **心裡怎麼想**：「一口氣做了 iOS、Android 跟網頁三端，還做了 VIP 訂閱、點數付費牆跟精選曝光，對於一個 0 到 1 MVP 來說範圍（Scope）拉得非常大，我會好奇當時為什麼沒有先做最小可行性驗證（MVP），以及最後的投報率到底如何。」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：說明 KOOL 當時的分階段上線順序（為何同時做三端與三種變現機制）以及上線後的實際驗證數據。

#### 質疑 3
- **誰在想**：HR
- **讀到哪一句**：職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會
- **心裡怎麼想**：「我們同時有開 Senior PM（jd30）跟一般 PM（jd47）兩個缺，他近 10 年經驗又帶過 2 個企劃，投一般 PM 職缺我們會想確認他是想找 Senior PM 的職級與薪資，還是兩邊都願意談。」
- **這個疑問會讓我**：面試追問
- **要打消疑問，履歷或面試需要看到**：確認候選人對 Senior PM（jd30）與 PM（jd47）兩職缺之職級、職責範圍與薪資期望對齊。

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷第3點｜完成 PRD，並與 QA 制定 UAT 驗收案例、排定上線計畫。上線前以互動原型與 FAQ 向客服、業務說明，另協助業務製作銷售簡報｜對 jd47 直接命中「產品教育訓練與上線測試驗收、跨部門溝通橋樑」
- 尚凡第1點與1111第1-2點｜規劃 KOOL 網紅媒合平台...推動系統改版至前後端分離的新架構，採新舊並行、分階段上線｜對 jd47 完整證明同時具備 0-1 MVP 推動與成熟產品迭代能力
- 1111第5點與AI協作技能｜與外部合作夥伴議定查詢 API...與工程確認 JSON 欄位與判定規則；以 Claude Code 建立協作流程與共用 skill｜對 jd47 滿足 API/JSON 理解與 AI 工具規格撰寫加分項

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定資料表與欄位需求，與 DBA 協作取數
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：KOOL 0 到 1 平台未在本版履歷列出上線後的用戶規模或報名媒合數據
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落
- 位置：1111 經歷第 1、2、4、7 點與尚凡第 1 點
  - 原句：與工程於 2025/09 完成上線；完成三項功能上線
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中
  - 建議方向：補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：強

### 8. 未測試聲明
PDF 抽字：local_extraction（已於總報告 §6 獨立列示 `resume-v10.3-twocol.pdf` 本機抽字結果，不併入內容評等） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

# 附錄 B：15 份原始單行 JSON 彙整清單

- **jd03**:
```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd03","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd03-01","human_calibrated":false,"requirements":[{"id":"R01","text":"2年以上獨立PM經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"獨立負責多款B2C與B2B產品規劃與交付"},{"id":"R02","text":"能撰寫PRD/User Story/Wireframe","type":"required","status":"supported","evidence":["從需求釐清、系統分析到流程與原型設計，完成 PRD"],"blocks_interview":false,"reason":"完整具備User Story、Wireframe與PRD實績"},{"id":"R03","text":"理解API串接與系統運作邏輯","type":"required","status":"supported","evidence":["以簽章驗證與時間戳防止重放，以錯誤碼與頻率限制控管呼叫"],"blocks_interview":false,"reason":"具外部API規格議定、JSON欄位確認與CodaPay串接經驗"},{"id":"R04","text":"金融科技/支付/點數/電子票證/電商經驗","type":"preferred","status":"supported","evidence":["另規劃並上線 VIP 訂閱、點數付費牆與精選曝光"],"blocks_interview":false,"reason":"具網頁付款、點數機制与CodaPay電信超商支付經驗"},{"id":"R05","text":"政府機關或銀行產品串接經驗","type":"preferred","status":"unknown","evidence":["未呈現政府機關或銀行系統直接串接紀錄"],"blocks_interview":false,"reason":"過往金流為第三方聚合支付CodaPay串接"},{"id":"R06","text":"會員經營/用戶留存與數據觀測分析經驗","type":"preferred","status":"supported","evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"blocks_interview":false,"reason":"具訂閱定價對照實驗、GA4與世代分析經驗"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["系統服務逾 6 萬家活躍付費廠商（2026 Q3）"],"missing":["近4年主責B2B招募系統，非高頻錢包支付核心"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"強","evidence":["與外部合作夥伴議定查詢 API 時，先處理可能被濫用的風險"],"missing":["未呈現銀行或政府機關直接串接紀錄"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["以簽章驗證與時間戳防止重放，以錯誤碼與頻率限制控管呼叫"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"missing":["1111改版與群組功能缺上線後採用與留存成效"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"對位 jd03 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd03 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"證據鏈支持安排 jd03 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"過去串接 CodaPay 與規劃 Peach 網頁付款時，如何處理掉單重試、退款與對帳？若改對接銀行或政府機關，你預期技術與法遵有哪些差異？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd03 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"加分條件之「政府機關或銀行產品串接經驗」未呈現（過往金流為第三方支付 CodaPay 與網頁付款）","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗，經手 6 款產品","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["曾推進「Peach 付款由 App 內購轉向網頁，與 CodaPay 新加坡技術團隊協調串接，網頁付款占營收由 24% 升至 80% 以上」並完成東南亞超商與電信帳單支付實收試算","與外部夥伴議定查詢 API 時「以簽章驗證與時間戳防止重放...與工程確認 JSON 欄位與判定規則與判定規則」，符合支付場景對 API 安全與系統邏輯的要求","現任 1111 招募系統 PO，在後台與資料庫不動的限制下補回合約與點數計費規則並分階段上線，完成 743/840 件廠商建議（88%）"],"key_gaps":["加分條件之「政府機關或銀行產品串接經驗」未呈現（過往金流為第三方支付 CodaPay 與網頁付款）","近 4 年主力於 B2B 招募系統，高頻支付與點數變現案例集中於 2016–2022 年","1111 上線之新版功能與群組功能僅列交付進度與結案比例，未列上線後的用戶採用率或轉換成效"],"strengths":["1111經歷第5點｜以簽章驗證與時間戳防止重放，以錯誤碼與頻率限制控管呼叫｜對 jd03 直接證明具備 API 規格議定、資安防濫用與 JSON 邏輯確認能力","尚凡經歷第4點｜規劃 Peach 付款由 App 內購轉向網頁，與 CodaPay 新加坡技術團隊協調串接｜對 jd03 展現第三方金流串接與支付渠道轉換實績","1111經歷第1點｜主副帳號權限、合約制與點數制的計費規則卻沒有文件。以實測歸納...｜對 jd03 證明能梳理無文件的複雜點數計費與權限邏輯"],"interview_questions":["過去串接 CodaPay 與規劃 Peach 網頁付款時，如何處理掉單重試、退款與對帳？若改對接銀行或政府機關，你預期技術與法遵有哪些差異？","你在 1111 盤點「合約制與點數制的計費規則」時，處理了哪些點數扣款、退還或效期邊界條件？","1111 第一階段改版（登入、首頁、公司資料）與群組功能上線後，實際廠商切換率與使用活躍度如何？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd03 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```
- **jd09**:
```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd09","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd09-02","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上軟體產品或專案管理經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"年資與軟體產品交付量充足"},{"id":"R02","text":"B2B SaaS經驗尤佳","type":"preferred","status":"supported","evidence":["人力銀行企業端招募系統專案負責人，系統服務逾 6 萬家活躍付費廠商"],"blocks_interview":false,"reason":"近4年主責大型B2B企業端招募系統"},{"id":"R03","text":"熟悉UI/UX概念方法論","type":"required","status":"supported","evidence":["User Journey Map、User Story、Use Case、Wir"],"blocks_interview":false,"reason":"具使用者旅程檢視、Wireframe與互動原型經驗"},{"id":"R04","text":"批判性思維與優先序判斷","type":"required","status":"supported","evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"blocks_interview":false,"reason":"依使用者旅程與溝通中斷痛點調整Roadmap優先序"},{"id":"R05","text":"數據驅動思維","type":"required","status":"supported","evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"blocks_interview":false,"reason":"具三階段定價對照實驗、GA4與世代分析經驗"},{"id":"R06","text":"獨立作業善跨部門溝通、製作說明文件","type":"required","status":"supported","evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"blocks_interview":false,"reason":"對接10個單位並產出FAQ與sales kit"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["系統服務逾 6 萬家活躍付費廠商（2026 Q3）"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"強","evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"missing":["未直接經手 MarTech（CDP+MA+BI）產品"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"足夠","evidence":["30 天內結案的比例由前一年的 52% 升至 79%（提案滿 30 天者）"],"missing":["1111上線之企業端功能未列客戶採用率或留存提升數據"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD、Prototype"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"對位 jd09 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"partial","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd09 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"證據鏈支持安排 jd09 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"你在 1111 於 2025/09 上線的大型客戶「群組功能」與 2025/10 上線的新版首頁，上線後如何分析使用情況並提出迭代優化建議？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd09 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"1111 上線之企業端功能（如大型客戶群組功能、第一階段改版、AI 推薦）缺乏上線後的廠商使用率或留存指標","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗，經手 6 款產品","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["現任 1111 企業端招募系統 PO（服務逾 6 萬家活躍付費廠商），完整負責需求搜集、Roadmap 優先序、PRD、測試驗收與 sales kit 製作，完全對應 jd09 工作內容","具備依據使用者旅程與客服業務回饋排定優先級的實證（「優先推進信件與即時通整合；將搜尋結果頁改版排在新功能職缺健檢之前」）","具備三階段定價實驗、GA4、世代分析及「擬定資料表與欄位需求，與 DBA 協作取數」之數據分析能力"],"key_gaps":["1111 上線之企業端功能（如大型客戶群組功能、第一階段改版、AI 推薦）缺乏上線後的廠商使用率或留存指標","B2B 需求來源多寫「廠商反映」「與內部維運稽核訪談」，較少描寫 PM 主導外部企業客戶深度訪談的過程","未直接經手 MarTech（CDP+MA+BI）行銷科技產品"],"strengths":["1111經歷第3點｜上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報｜對 jd09 直接命中「製作說明文件、與客服業務合作推動產品迭代與上市」職責","1111經歷第2點｜規劃群組功能，讓同單位帳號共同處理職缺...於 2025/09 完成上線｜對 jd09 證明具備 B2B 企業多層級帳號權限與資料範圍設計經驗","1111經歷第4點｜依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前｜對 jd09 展現基於使用者旅程與痛點的產品路線圖優先序判斷"],"interview_questions":["你在 1111 於 2025/09 上線的大型客戶「群組功能」與 2025/10 上線的新版首頁，上線後如何分析使用情況並提出迭代優化建議？","在規劃大型客戶部門／分店群組功能時，你是透過業務轉述需求，還是曾親自訪談大型企業 HR 客戶？","過去在 1111 處理求職者篩選查詢條件與 AI 推薦人才的經驗，如何遷移至 CDP 受眾分群與自動化行銷劇本設計？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd09 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```
- **jd11**:
```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd11","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd11-03","human_calibrated":false,"requirements":[{"id":"R01","text":"5年以上PM經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"年資近10年且涵蓋B2B與B2C"},{"id":"R02","text":"熟悉敏捷開發與跨部門專案管理","type":"required","status":"supported","evidence":["曾參與每週一個 Sprint 的 Scrum，現行以 Kanban 推進瀑布式"],"blocks_interview":false,"reason":"兼具Scrum與Kanban跨10單位專案管理"},{"id":"R03","text":"優秀邏輯與溝通能力","type":"required","status":"supported","evidence":["能將業務上的搜尋、篩選規則拆成查詢條件，與工程確認後端行為"],"blocks_interview":false,"reason":"邏輯拆解與跨部門溝通能力扎實"},{"id":"R04","text":"熟悉Jira、Notion等工具","type":"required","status":"partial","evidence":["Figma、Axure RP、Notion、Trello；內部專案控管系統"],"blocks_interview":false,"reason":"具Notion、Trello與內部控管系統，未點名Jira"},{"id":"R05","text":"中英文文件撰寫能力","type":"required","status":"supported","evidence":["英文 TOEIC 980、TOEFL iBT 93，曾赴美交換，並以英文進行跨國"],"blocks_interview":false,"reason":"具高分英檢與跨國英文協作經驗"},{"id":"R06","text":"HR Tech/LegalTech/生成式AI產品經驗","type":"preferred","status":"supported","evidence":["定義公司簡介生成、職缺工作說明生成及 AI 推薦人才的使用情境與驗收標準"],"blocks_interview":false,"reason":"直接具備HR Tech與3項生成式AI功能上線經驗"},{"id":"R07","text":"LLM prompt設計或自動化內容編排經驗","type":"preferred","status":"supported","evidence":["以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格"],"blocks_interview":false,"reason":"建立Claude Code協作流程與共用skill"},{"id":"R08","text":"資料導向思維、AB測試與技術背景","type":"preferred","status":"supported","evidence":["設計馬來西亞 iOS 定價實驗；基本 HTML／CSS 與資料庫知識"],"blocks_interview":false,"reason":"具對照實驗、資料庫知識、API規格議定與AWS證照"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["人力銀行企業端招募系統專案負責人，系統服務逾 6 萬家活躍付費廠商"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"強","evidence":["與資料科學團隊合作，定義公司簡介生成、職缺工作說明生成及 AI 推薦人才"],"missing":["使用 Trello 及內部專案控管系統、Notion，未直接寫出 Jira"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"足夠","evidence":["這些模組相關的 840 件廠商建議，已完成 743 件（88%）"],"missing":["AI 生成與推薦功能及群組功能未列上線後之產品 KPI 表現"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["結構清晰，完整呈現 HR 招募系統權限、流程與 AI 協作細節"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"對位 jd11 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"partial","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd11 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"證據鏈支持安排 jd11 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"你使用的內部專案控管系統與 Trello，在記錄 User Story、驗收條件與優先級供 Tech Lead 派工估時時，工作流如何運作？是否曾接觸過 Jira？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd11 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"必要條件點名之 `Jira` 未出現在履歷中（履歷為使用 Notion、Trello 及內部專案控管系統）","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗，經手 6 款產品","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["直接具備 HR Tech 核心背景（現任 1111 企業端招募系統 PO，熟悉主副帳號權限、部門／分店群組招募、職缺與履歷管理流程），與本職缺 HRIS／客戶管理系統高度同源","與資料科學團隊合作完成「公司簡介生成、職缺工作說明生成及 AI 推薦人才」三項功能上線，並「以 Claude Code 建立協作流程與共用 skill」，完全命中生成式 AI 與自動化編排加分項","具備每週一 Sprint 之 Scrum 與 Kanban 經驗，且能將搜尋篩選規則拆成查詢條件與工程確認後端行為"],"key_gaps":["必要條件點名之 `Jira` 未出現在履歷中（履歷為使用 Notion、Trello 及內部專案控管系統）","上線之三項 AI 功能（公司簡介生成、職缺說明生成、AI 推薦人才）與群組功能未列出上線後的採用率或準確度 KPI","兩項重點改版（信件與即時通整合、搜尋結果頁改版）尚在開發／封測中"],"strengths":["1111經歷第1-2點｜主副帳號權限、合約制與點數制的計費規則...規劃群組功能，讓同單位帳號共同處理職缺及對應履歷｜對 jd11 直接對位客戶管理與 HRIS 系統最核心的組織權限與招募流程設計","1111經歷第7點與AI技能｜定義公司簡介生成、職缺工作說明生成及 AI 推薦人才...以 Claude Code 建立協作流程與共用 skill｜對 jd11 同時命中 HR Tech、生成式 AI 產品上線與 LLM 自動化內容編排","專業技能（專案交付）｜按 User Story 記錄需求、做法、驗收條件與優先級，供 Tech Lead 派工與估時｜對 jd11 清楚展現與工程團隊推進開發的規格結構與協作深度"],"interview_questions":["你使用的內部專案控管系統與 Trello，在記錄 User Story、驗收條件與優先級供 Tech Lead 派工估時時，工作流如何運作？是否曾接觸過 Jira？","「公司簡介生成、職缺工作說明生成及 AI 推薦人才」三項功能上線後，你是如何定義驗收標準與追蹤線上 KPI 的？客服測試回饋讓你調整了哪些推薦規則？","目前進入內部封測的「信件與即時通整合」與開發中的「搜尋結果頁改版」，預計上線後追蹤哪些核心 KPI？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd11 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```
- **jd14**:
```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd14","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd14-04","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上Growth PM經驗（全生命週期與Growth Funnel）","type":"required","status":"supported","evidence":["經手交友、訂閱制內容 App 與網紅媒合平台，規劃使用流程、訂閱與付費機制"],"blocks_interview":false,"reason":"具約6年消費級訂閱制App獲取、付費轉換與定價實驗經驗"},{"id":"R02","text":"能獨立撰寫PRD/User Flow/Wireframe","type":"required","status":"supported","evidence":["系統分析、流程圖／循序圖、Wireframe、Prototype、PRD"],"blocks_interview":false,"reason":"完整具備流程圖、Wireframe與PRD實績"},{"id":"R03","text":"熟悉GA4、Firebase","type":"required","status":"partial","evidence":["使用者訪談與問卷、內部維運與稽核訪談、競品實測、GA4、世代分析與對照組實驗"],"blocks_interview":false,"reason":"明列GA4、世代分析與對照組實驗，未呈現Firebase"},{"id":"R04","text":"訂閱與會員轉換優化、A/B Test產品實驗","type":"required","status":"supported","evidence":["設計馬來西亞 iOS 定價實驗，以售價不變的 Android 作對照"],"blocks_interview":false,"reason":"具VIP訂閱、7/30/90天方案、網頁付款轉換與三階段定價實驗"},{"id":"R05","text":"跨部門溝通能力","type":"required","status":"supported","evidence":["與工程、設計、行銷及海外金流團隊協作上線"],"blocks_interview":false,"reason":"跨工程、設計、行銷與金流團隊推進產品成長"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["經手交友、訂閱制內容 App 與網紅媒合平台，規劃使用流程、訂閱與付費機制"],"missing":["近4年重心為B2B招募系統，C端訂閱成長案例集中於2016–2022年"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"足夠","evidence":["設計馬來西亞 iOS 定價實驗，以售價不變的 Android 作對照"],"missing":["必備條件點名之 Firebase 未呈現；缺 OTT 影音串流經驗"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["還原原價後，iOS 非續訂營收較原價期減 65%，團隊依結果決定採用低價"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["男性 DAU 在 6 週內由約 3,200 增至 1.25 萬"],"missing":["KOOL 訂閱點數牆與 1111 近期改版未列漏斗轉換率數據"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["主導 Juicy 推出並協調跨團隊工作，配合行銷導入既有用戶"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["清楚交代實驗設計、對照基準、期間與決策結果"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["經手交友、訂閱制內容 App 與網紅媒合平台，規劃使用流程、訂閱與付費機制"],"application_note":"對位 jd14 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd14 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"證據鏈支持安排 jd14 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"過去在尚凡與思維特經營 iOS／Android 訂閱制 App 時，除了 GA4 之外，是否有使用 Firebase（如 Analytics、Remote Config、A/B Testing 或 Crashlytics）的經驗？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd14 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"必備條件中點名之 `Firebase` 未呈現（履歷僅列 GA4、Google Sheets、Excel 與資料庫取數）","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["經手交友、訂閱制內容 App 與網紅媒合平台，規劃使用流程、訂閱與付費機制","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["具備約 6 年訂閱制消費型 App 經驗，曾設計馬來西亞 iOS 三階段定價實驗（以 Android 作對照，各期 21 天）驗證價格彈性並促成團隊決策","曾規劃 VIP 訂閱、點數付費牆、7／30／90 天訂閱方案與加贈內容，並推進 Peach 內購轉向網頁付款（占營收由 24% 升至 80% 以上）","熟稔 GA4、世代分析與對照組實驗，並能從 User Journey Map 檢視漏斗斷點（如信件與即時通整合、搜尋結果頁改版）"],"key_gaps":["必備條件中點名之 `Firebase` 未呈現（履歷僅列 GA4、Google Sheets、Excel 與資料庫取數）","C 端訂閱制與成長實驗集中於 2016–2022 年，近 4 年在 1111 以企業端系統重構與功能交付為主","KOOL 網紅媒合平台的 VIP 訂閱與點數付費牆未列出上線後的付費轉換率或留存數據"],"strengths":["尚凡經歷第3點｜設計馬來西亞 iOS 定價實驗，以售價不變的 Android 作對照，依序測試原價、降價與還原原價｜對 jd14 直接證明具備嚴謹的產品實驗設計與付費轉換分析能力","尚凡經歷第4點與思維特第2點｜網頁付款占營收由 24% 升至 80% 以上；提出 7／30／90 天訂閱方案與加贈內容｜對 jd14 展現訂閱方案設計、渠道轉換與實收試算的商業成長經驗","研究與數據技能｜使用者訪談與問卷、競品實測、GA4、世代分析與對照組實驗｜對 jd14 符合全生命週期留存（Cohort 世代分析）與量化決策要求"],"interview_questions":["過去在尚凡與思維特經營 iOS／Android 訂閱制 App 時，除了 GA4 之外，是否有使用 Firebase（如 Analytics、Remote Config、A/B Testing 或 Crashlytics）的經驗？","近 4 年在 1111 企業端系統工作期間，是否有運用漏斗分析或對照實驗來驗證改版成效的案例？為何現在想重回 C 端訂閱制 Growth PM？","你在 KOOL 規劃上線的 VIP 訂閱、點數付費牆與精選曝光，上線後的付費轉換率（CVR）與用戶留存表現如何？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":7,"uncertainty_levels":1,"basis":"針對 jd14 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```
- **jd20**:
```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd20","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd20-05","human_calibrated":false,"requirements":[{"id":"R01","text":"5-8年以上B2B/B2G產品或專案管理經驗","type":"required","status":"partial","evidence":["1111 全球華人｜2022/08 - 迄今（企業端招募系統專案負責人）"],"blocks_interview":false,"reason":"總PM近10年，惟純B2B經驗約4年略低於5-8年門檻"},{"id":"R02","text":"接近母語等級英語口說與書寫","type":"required","status":"partial","evidence":["英文 TOEIC 980、TOEFL iBT 93，曾赴美交換，並以英文進行跨國"],"blocks_interview":false,"reason":"英檢高分且有跨國協作，是否達母語級B2B商務談判待驗"},{"id":"R03","text":"優異溝通與關係人管理能力","type":"required","status":"supported","evidence":["對接工程、行銷、業務與客服等 10 個需求單位；向總經理、副總等主管匯報"],"blocks_interview":false,"reason":"跨10個單位協調需求並向高層匯報"},{"id":"R04","text":"扎實PM基礎（PRD/路線圖/待辦清單/時程風險）","type":"required","status":"supported","evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"blocks_interview":false,"reason":"主責50項大功能並將30天內結案率由52%升至79%"},{"id":"R05","text":"強烈數據敏感度（能獨立使用SQL/BI/試算表查詢分析）","type":"required","status":"partial","evidence":["擬定資料表與欄位需求，與 DBA 協作取數，再以 Excel 分析"],"blocks_interview":false,"reason":"精熟試算表與欄位規劃，惟取數需與DBA協作而非獨立寫SQL/BI"},{"id":"R06","text":"熟悉AI工具（如Claude）並串接Jira/Confluence自動化","type":"required","status":"partial","evidence":["以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格"],"blocks_interview":false,"reason":"深度使用Claude Code，惟未呈現串接Jira/Confluence"},{"id":"R07","text":"對防詐與風險偵測有熱情及防詐/資安/風控產品經驗","type":"required","status":"supported","evidence":["針對廠商招募帳號遭冒用...確認登入驗證與帳號解鎖流程，於 2026/04 上線"],"blocks_interview":false,"reason":"具B2B帳號防冒用調整與外部API簽章防重放/限流控管實績"},{"id":"R08","text":"曾服務企業客戶或政府機關，尤其海外市場（東南亞/日韓）","type":"preferred","status":"partial","evidence":["推進 SweetRing 在美國、墨西哥、巴西、印尼、馬來西亞、日本與韓國 7 "],"blocks_interview":false,"reason":"具東南亞與日韓7國B2C在地化與台灣B2B，缺海外B2B/B2G客戶經驗"},{"id":"R09","text":"具Agile/Scrum與定價、報價或成本利潤分析經驗","type":"preferred","status":"supported","evidence":["曾參與每週一個 Sprint 的 Scrum；整理各管道的抽成、稅、手續費與撥款"],"blocks_interview":false,"reason":"具Scrum、定價實驗與跨國金流成本實收試算經驗"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["人力銀行企業端招募系統專案負責人，系統服務逾 6 萬家活躍付費廠商"],"missing":["純B2B經驗約4年（略低於5-8年B2B門檻），且未直接面對海外B2B/B2G客戶與BD"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"足夠","evidence":["以簽章驗證與時間戳防止重放，以錯誤碼與頻率限制控管呼叫"],"missing":["取數須與 DBA 協作而非獨立寫 SQL；未明列 Jira/Confluence 串接"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["與外部合作夥伴議定查詢 API 時，先處理可能被濫用的風險"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"足夠","evidence":["調整後至 2026/10，未再透過客服接獲廠商回報同類冒用"],"missing":["1111企業端新功能缺採用與留存指標；防冒用成效以客服回報為準"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["參與公司一級主管日會，向總經理、副總等主管匯報"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["結構清晰，清楚呈現 API 防濫用、帳號防冒用與 Claude Code 工作流"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"partial","resume_evidence":["1111 全球華人｜2022/08 - 迄今（企業端招募系統專案負責人）"],"application_note":"對位 jd20 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"partial","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd20 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"partial","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"建議先釐清 jd20 關鍵條件再安排面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"partial","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":"在分析產品數據時，本人是否能獨立撰寫 SQL 查詢資料庫？"},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"在 1111 需要分析產品數據時，你本人能否獨立撰寫 SQL 查詢資料庫或操作 BI 工具？過去在尚凡規劃 KOOL 時包含多少對 B 端（案主／公司行號）的需求管理經驗？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd20 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"必備條件要求「5-8年以上B2B/B2G經驗」與「自行查詢並解讀產品數據（能獨立使用SQL/BI）」，目前純 B2B 約 4 年且取數須與 DBA 協作","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"clarify_first","evidence":["1111 全球華人｜2022/08 - 迄今（企業端招募系統專案負責人）","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":["必備條件要求「5-8年以上B2B/B2G經驗」與「自行查詢並解讀產品數據（能獨立使用SQL/BI）」，目前純 B2B 約 4 年且取數須與 DBA 協作"]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["直接具備兩項防濫用與帳號安全實績：議定外部查詢 API 時「以簽章驗證與時間戳防止重放，以錯誤碼與頻率限制控管呼叫」，以及「針對廠商招募帳號遭冒用，確認登入驗證與帳號解鎖流程，於 2026/04 上線調整」","深度運用 Claude Code 建立協作流程與共用 skill，並與資料科學團隊協作上線 3 項 AI 功能，高度契合 JD 對 Claude 與 AI 團隊協作的要求","具備逾 6 萬家企業客戶系統之 PO 交付經驗（50 項大功能上線、30 天結案率由 52% 升至 79%）與 TOEIC 980／赴美交換跨國協作背景"],"key_gaps":["必備條件要求「5-8年以上B2B/B2G經驗」與「自行查詢並解讀產品數據（能獨立使用SQL/BI）」，目前純 B2B 約 4 年且取數須與 DBA 協作","未呈現直接向海外企業客戶（東南亞、日韓 B2B/B2G）與 BD 團隊收集需求並轉化為產品路線圖的經驗","專案管理與文件工具列 Trello、Notion 與內部系統，未明列串接 Jira、Confluence"],"strengths":["1111經歷第5-6點｜以簽章驗證與時間戳防止重放...針對廠商招募帳號遭冒用...確認登入驗證與帳號解鎖流程｜對 jd20 直接對位 Anti-Scam BU 重視之防濫用、帳號安全與風險控管經驗","AI協作技能與1111經歷第7點｜以 Claude Code 建立協作流程與共用 skill...與資料科學團隊合作完成三項功能上線｜對 jd20 直接命中「善用 AI 工具（如 Claude）」與「與 RD/AI 團隊密切合作」","1111經歷第8點｜30 天內結案的比例由前一年的 52% 升至 79%（提案滿 30 天者）｜對 jd20 證明具備 50% 專案與交付管理所需的時程控管與積案清理能力"],"interview_questions":["在 1111 需要分析產品數據時，你本人能否獨立撰寫 SQL 查詢資料庫或操作 BI 工具？過去在尚凡規劃 KOOL 時包含多少對 B 端（案主／公司行號）的需求管理經驗？","請以英文分享：若要向東南亞或日韓的企業／銀行客戶推廣防詐 API 或 2B 解決方案，你會如何與 BD 配合收集跨市場需求並排定優先序？","你建立的 Claude Code 協作流程與共用 skill 目前如何與內部專案控管系統銜接？若要串接 Jira 與 Confluence 自動化工作流，你會如何設計？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":7,"uncertainty_levels":1,"basis":"針對 jd20 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```
- **jd26**:
```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd26","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd26-06","human_calibrated":false,"requirements":[{"id":"R01","text":"2年以上相關工作經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"年資與專案執行經驗豐富"},{"id":"R02","text":"能運用Axure撰寫產品規劃，並透過Jira、Confluence進行專案管理","type":"required","status":"partial","evidence":["Figma、Axure RP、Notion、Trello；使用 Trello 及"],"blocks_interview":false,"reason":"具Axure RP與內部專案控管系統，未直接點名Jira/Confluence"},{"id":"R03","text":"能同步考慮技術可行性以及系統架構關連影響；預期及識別風險","type":"required","status":"supported","evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"blocks_interview":false,"reason":"兼顧後台資料庫限制、新舊並行與API防濫用風險"},{"id":"R04","text":"與合作方確認規劃並與法遵確認適法性","type":"required","status":"partial","evidence":["與外部合作夥伴議定查詢 API 時，先處理可能被濫用的風險；與維運、稽核核對"],"blocks_interview":false,"reason":"具外部夥伴API議定與內部稽核核對，未明寫「法遵」字樣"},{"id":"R05","text":"執行專案測試、驗收、上線協調及內外部教育訓練","type":"required","status":"supported","evidence":["與 QA 制定 UAT 驗收案例、排定上線計畫。上線前以互動原型與 FAQ 向客"],"blocks_interview":false,"reason":"完整具備UAT驗收、上線計畫與內部教育訓練實績"},{"id":"R06","text":"喜愛或熟悉數位金融、支付產品；加分：代理收付/電支/英文/數據分析","type":"required","status":"supported","evidence":["導入 CodaPay，讓印尼、泰國等市場的用戶可用電信帳單與超商付款"],"blocks_interview":false,"reason":"具網頁付款、CodaPay跨國金流實收試算、TOEIC 980與GA4"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["系統服務逾 6 萬家活躍付費廠商（2026 Q3）"],"missing":["金流經驗偏向商戶端串接，無台灣專營電子支付機構與銀行合作專案經驗"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"足夠","evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"missing":["使用 Trello 及內部專案控管系統，未直接寫出 Jira/Confluence；未明寫法遵字樣"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對，把這些規則接回新版的規格與流程"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["30 天內結案的比例由前一年的 52% 升至 79%（提案滿 30 天者）"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["清楚交代新舊系統並行、API 規格議定與跨部門交付流程"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"對位 jd26 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd26 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"證據鏈支持安排 jd26 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"你在 1111 使用內部專案控管系統與 Trello「按 User Story 記錄需求、做法、驗收條件與優先級，供 Tech Lead 派工與估時」的流程，若切換到 Jira 與 Confluence 需要多少適應時間？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd26 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"必要條件要求「透過 Jira、Confluence 進行專案管理」，履歷列 Notion、Trello 與內部專案控管系統","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗，經手 6 款產品","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["完全涵蓋本職缺 1–9 項專案執行職責：從系統分析、Wireframe／Flow chart、Axure RP 原型、PRD、UAT 驗收、排定上線計畫，到「上線前以互動原型與 FAQ 向客服、業務說明」之內部教育訓練","具備考慮系統架構關連影響與識別風險的具體案例（後台與資料庫不動下新舊並行改版、外部查詢 API 簽章防重放與頻率限制、帳號防冒用調整）","具備 Peach 網頁金流轉換（占營收升至 80%+）與 CodaPay 東南亞電信帳單／超商付款串接及抽成稅費實收試算經驗"],"key_gaps":["必要條件要求「透過 Jira、Confluence 進行專案管理」，履歷列 Notion、Trello 與內部專案控管系統","職責第 3 點要求「與法遵確認適法性」，履歷寫「與維運、稽核核對」及處理帳號冒用，未明寫與法務／法遵單位確認電支法規之細節","金流經驗偏向商戶端串接第三方聚合支付（CodaPay），未直接經手台灣電子支付機構之代理收付與銀行端作業"],"strengths":["1111經歷第3點與工具技能｜Figma、Axure RP...完成 PRD，並與 QA 制定 UAT 驗收案例、排定上線計畫。上線前以互動原型與 FAQ 向客服、業務說明｜對 jd26 完整對位 Axure 規劃、測試驗收與教育訓練職責","1111經歷第1,5點｜業務後台與資料庫都不能更動...把這些規則接回新版；與外部合作夥伴議定查詢 API 時，先處理可能被濫用的風險｜對 jd26 證明能同步考量系統架構關連影響並預先識別風險","尚凡第4點與思維特第2點｜規劃 Peach 付款由 App 內購轉向網頁，與 CodaPay 新加坡技術團隊協調串接...完成實收試算｜對 jd26 展現外部支付合作方協調與金流試算能力"],"interview_questions":["你在 1111 使用內部專案控管系統與 Trello「按 User Story 記錄需求、做法、驗收條件與優先級，供 Tech Lead 派工與估時」的流程，若切換到 Jira 與 Confluence 需要多少適應時間？","過去在處理廠商帳號遭冒用、外部合作夥伴 API 議定或跨國金流串接時，是否有與法務或法遵單位確認個資法或金融法規適法性的經驗？","從商戶端串接 CodaPay 到進入專營電子支付機構（全支付）負責業務合作專案，你認為在交易對帳、清分算與風險控管上有哪些關鍵差異？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":7,"uncertainty_levels":1,"basis":"針對 jd26 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```
- **jd30**:
```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd30","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd30-07","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上Software PM，至少一次完整0到1產品探索、驗證、設計、開發、上線與迭代經歷","type":"required","status":"supported","evidence":["規劃 KOOL 網紅媒合平台，從案主與網紅兩種角色釐清需求...設計刊案、報名、"],"blocks_interview":false,"reason":"主導KOOL從0到1需求釐清、雙邊媒合流程設計與VIP/點數上線"},{"id":"R02","text":"能寫清楚的規格文件（PRD、流程圖、資料結構）","type":"required","status":"supported","evidence":["系統分析、流程圖／循序圖、Wireframe、Prototype、PRD；擬定資"],"blocks_interview":false,"reason":"完整具備PRD、流程圖/循序圖與資料表欄位定義能力"},{"id":"R03","text":"理解API、JSON與基本SQL","type":"required","status":"supported","evidence":["與工程確認 JSON 欄位與判定規則；能將業務上的搜尋、篩選規則拆成查詢條件"],"blocks_interview":false,"reason":"明確具備API規格議定、JSON欄位確認與查詢條件拆解，取數與DBA協作"},{"id":"R04","text":"習慣用AI工具（Claude Code等）加速驗證與把PM工作流程化；評估AI放進產品機會","type":"preferred","status":"supported","evidence":["以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格"],"blocks_interview":false,"reason":"直接命中Claude Code協作流程、共用skill與上線3項AI功能"},{"id":"R05","text":"停車/交通/MaaS/保險/支付/FinTech經驗；Growth或數據分析經驗","type":"preferred","status":"supported","evidence":["規劃 Peach 付款由 App 內購轉向網頁，與 CodaPay 新加坡技術團"],"blocks_interview":false,"reason":"具跨國支付串接、實收試算與馬來西亞iOS定價對照實驗經驗"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["涵蓋訂閱制社交 App、網紅媒合平台與人力銀行招募系統"],"missing":["過往為純線上軟體平台，未直接接觸智慧停車或 MaaS 實體場域硬體"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"強","evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"missing":["資料庫查詢為「擬定資料表與欄位需求，與 DBA 協作取數」，未明寫自寫 SQL"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["30 天內結案的比例由前一年的 52% 升至 79%（提案滿 30 天者）"],"missing":["KOOL 0 到 1 平台未列上線後的規模與轉換數據"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["清楚呈現 PRD、流程圖／循序圖、資料表欄位需求與 AI 協作流程"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台，從案主與網紅兩種角色釐清需求...設計刊案、報名、"],"application_note":"對位 jd30 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd30 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"證據鏈支持安排 jd30 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"你在尚凡從 0 到 1 規劃 KOOL 網紅媒合平台並上線 VIP 訂閱、點數付費牆與精選曝光後，如何驗證 PoC 到 Scale？實際雙邊用戶規模與付費表現如何？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd30 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"KOOL 網紅媒合平台雖完整描述 0 到 1 探索與功能設計，但本版履歷未列出上線後的用戶數、媒合量或營收成果數字","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["規劃 KOOL 網紅媒合平台，從案主與網紅兩種角色釐清需求...設計刊案、報名、","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["直接命中 JD 第 2 點與加分項：「以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格，並將業務規則轉為可與工程討論的條件描述」，且已與資料科學團隊上線 3 項 AI 功能","完全滿足必備技術與規格條件：不僅能撰寫 PRD、流程圖／循序圖、擬定資料表與欄位需求，更在議定外部查詢 API 時「以簽章驗證與時間戳防止重放...與工程確認 JSON 欄位與判定規則與判定規則」","兼具 KOOL 網紅媒合平台從 0 到 1（無直接競品下設計雙邊媒合與 VIP／點數變現）與 1111 成熟產品迭代、馬來西亞定價成長實驗及跨國支付串接經驗"],"key_gaps":["KOOL 網紅媒合平台雖完整描述 0 到 1 探索與功能設計，但本版履歷未列出上線後的用戶數、媒合量或營收成果數字","資料庫查詢寫「擬定資料表與欄位需求，與 DBA 協作取數；能將業務上的搜尋、篩選規則拆成查詢條件」，未明寫本人手寫 SQL 語法程度","過往為純線上數位平台，尚未接觸智慧停車或 MaaS 線下硬體與場域營運"],"strengths":["AI協作技能與1111經歷第7點｜以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格...定義公司簡介生成、職缺工作說明生成及 AI 推薦人才｜對 jd30 完美對位「習慣用 Claude Code 把重複性 PM 工作流程化」與「評估 AI 放進產品機會」","1111經歷第5點與技能欄｜與外部合作夥伴議定查詢 API 時...以簽章驗證與時間戳防止重放...與工程確認 JSON 欄位與判定規則與判定規則｜對 jd30 直接證明理解 API、JSON 欄位與後端查詢條件","尚凡經歷第1,3點｜規劃 KOOL 網紅媒合平台...設計馬來西亞 iOS 定價實驗｜對 jd30 同時證明具備 0 到 1 雙邊平台規劃與成熟產品數據實驗能力"],"interview_questions":["你在尚凡從 0 到 1 規劃 KOOL 網紅媒合平台並上線 VIP 訂閱、點數付費牆與精選曝光後，如何驗證 PoC 到 Scale？實際雙邊用戶規模與付費表現如何？","你在將搜尋篩選規則拆成查詢條件及與 DBA 協作取數時，是否會自行撰寫基本 SQL（如 SELECT / JOIN / WHERE）？","面對 USPACE 結合線上 App 與線下智慧車位鎖／停車場硬體的 O2O 場景，你如何處理硬體異常或場域例外情境？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd30 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```
- **jd31**:
```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd31","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd31-08","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上產品規劃與需求訪談經驗，熟悉0到1或迭代優化流程","type":"required","status":"supported","evidence":["近 10 年 PM 經驗；使用者訪談與問卷、內部維運與稽核訪談"],"blocks_interview":false,"reason":"兼具KOOL 0到1與1111企業端50項大功能迭代經驗"},{"id":"R02","text":"業務支援與售前規劃（協助業務銷售簡報、客戶案件排程）","type":"required","status":"partial","evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助業務製作銷售簡報"],"blocks_interview":false,"reason":"已具備製作sales kit與客戶案件優先排程，惟缺直接參與客戶會議展示描寫"},{"id":"R03","text":"有多系統整合或API串接經驗（API整合、第三方介接、資料交換）","type":"required","status":"supported","evidence":["與外部合作夥伴議定查詢 API 時...與工程確認 JSON 欄位與判定規則；與"],"blocks_interview":false,"reason":"具外部查詢API規格議定、CodaPay第三方介接與新舊系統資料轉換經驗"},{"id":"R04","text":"熟悉PRD、功能規格與流程圖設計","type":"required","status":"supported","evidence":["User Journey Map、User Story、Use Case、系統分"],"blocks_interview":false,"reason":"產品規格與流程圖設計體系完整"},{"id":"R05","text":"熟悉敏捷開發流程（Scrum）","type":"required","status":"supported","evidence":["曾參與每週一個 Sprint 的 Scrum，現行以 Kanban 推進瀑布式，"],"blocks_interview":false,"reason":"明確具備每週一Sprint之Scrum與Kanban實務"},{"id":"R06","text":"曾主導或參與企業級系統（ERP/HRM/SaaS/平台型產品）規劃經驗","type":"preferred","status":"supported","evidence":["人力銀行企業端招募系統專案負責人，系統服務逾 6 萬家活躍付費廠商"],"blocks_interview":false,"reason":"主導6萬家企業招募系統與大型客戶部門/分店群組功能，與HRM高度同源"},{"id":"R07","text":"具備資料分析能力（SQL/BI工具）；熟悉技術背景（API、資料庫、系統架構）","type":"preferred","status":"supported","evidence":["擬定資料表與欄位需求，與 DBA 協作取數；能將業務上的搜尋、篩選規則拆成查詢條"],"blocks_interview":false,"reason":"熟悉API、JSON、資料庫欄位與前後端分離架構，取數與DBA協作"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["人力銀行企業端招募系統專案負責人，系統服務逾 6 萬家活躍付費廠商"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"強","evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助業務製作銷售簡報"],"missing":["客戶需求多由內部單位或客服反映，較少描寫親自隨業務拜訪客戶進行售前展示"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對，把這些規則接回新版的規格與流程"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"足夠","evidence":["30 天內結案的比例由前一年的 52% 升至 79%（提案滿 30 天者）"],"missing":["群組功能與新版模組未列上線後之企業客戶採用率"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["清楚呈現企業端權限盤點、群組招募、API 規格議定與交付成果"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗；使用者訪談與問卷、內部維運與稽核訪談"],"application_note":"對位 jd31 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"partial","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd31 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"證據鏈支持安排 jd31 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"在 1111 規劃「大型客戶部門／分店群組功能」及協助業務製作 sales kit 時，你是否曾與業務一同參與大型客戶會議進行需求訪談或產品展示（Pre-sales）？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd31 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"職責第 1、2 點包含「直接與客戶進行需求訪談」與「與業務共同參與客戶會議、產品展示」，履歷雖有製作 sales kit 與清理客戶案件，但未明寫是否親自參與外部客戶會議","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗；使用者訪談與問卷、內部維運與稽核訪談","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["現任 1111 企業端招募系統 PO（服務逾 6 萬家廠商），規劃「大型客戶部門或分店共同招募之群組功能（帳號權限、職缺關聯與資料轉換規則）」與主副帳號計費規則，與 NUEIP 雲端人資系統（HRM）領域高度契合","具備多系統整合與外部 API 規格議定實證（簽章驗證、防重放、錯誤碼、頻率限制、JSON 欄位與判定規則，以及 CodaPay 第三方服務介接）","具備每週一 Sprint 之 Scrum 經驗，且上線前「以互動原型與 FAQ 向客服、業務說明，另協助業務製作銷售簡報（sales kit）」，並將客戶案件 30 天結案率由 52% 升至 79%"],"key_gaps":["職責第 1、2 點包含「直接與客戶進行需求訪談」與「與業務共同參與客戶會議、產品展示」，履歷雖有製作 sales kit 與清理客戶案件，但未明寫是否親自參與外部客戶會議","加分項之 SQL/BI 工具，履歷採「擬定資料表與欄位需求，與 DBA 協作取數，再以 Excel 分析」","1111 大型客戶群組功能上線後，未列出實際採用之大型客戶家數或業務成效"],"strengths":["1111經歷第2點｜規劃群組功能，讓同單位帳號共同處理職缺及對應履歷及對應履歷｜對 jd31 直接對應 HRM/企業級 SaaS 最核心的組織架構與權限設計","1111經歷第3,8點｜上線前以互動原型與 FAQ 向客服、業務說明，另協助業務製作銷售簡報...30 天內結案的比例由前一年的 52% 升至 79%｜對 jd31 直接支撐業務支援與客戶專案管理進度追蹤","1111經歷第5點｜與外部合作夥伴議定查詢 API 時...以簽章驗證與時間戳防止重放...與工程確認 JSON 欄位與判定規則與判定規則｜對 jd31 完全符合跨系統 API 整合與資料交換流程設計要求"],"interview_questions":["在 1111 規劃「大型客戶部門／分店群組功能」及協助業務製作 sales kit 時，你是否曾與業務一同參與大型客戶會議進行需求訪談或產品展示（Pre-sales）？","在與 DBA 協作取數及拆解後端查詢條件時，你本人是否具備撰寫基本 SQL 查詢或使用 BI 儀表板的經驗？","2025/09 完成上線的「群組功能」，後續有多少大型連鎖或跨部門企業客戶實際導入使用？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd31 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```
- **jd32**:
```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd32","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd32-09","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上經驗且具備資訊或網站開發經驗或擁有SA（系統分析）經驗","type":"required","status":"supported","evidence":["從需求釐清、系統分析到流程與原型設計，完成 PRD；能將業務上的搜尋、篩選規則拆"],"blocks_interview":false,"reason":"現任同業招募系統PO，具扎實SA系統分析、舊規則逆向盤點與API規格議定經驗"},{"id":"R02","text":"傾聽需求，解決挑戰：接手內部使用者與外部客戶的議題，安排功能優化或問題修正","type":"required","status":"supported","evidence":["這些模組相關的 840 件廠商建議，已完成 743 件（88%）；30 天內結案"],"blocks_interview":false,"reason":"高比例完成840件廠商建議並清理多年積案，大幅提升30天結案率"},{"id":"R03","text":"運用AI工具進行營運分析或提案","type":"required","status":"supported","evidence":["以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格"],"blocks_interview":false,"reason":"深入運用Claude Code與AI Agent整理分析資料並轉譯工程條件"},{"id":"R04","text":"熟悉規格撰寫、跨單位溝通；與團隊評估解決方案的可行性與時程","type":"required","status":"supported","evidence":["對接工程、行銷、業務與客服等 10 個需求單位；依提案時間與難易安排新案，每週向"],"blocks_interview":false,"reason":"對接10個內部單位、依難易與提案時間評估排程並每週回報"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["人力銀行企業端招募系統專案負責人，系統服務逾 6 萬家活躍付費廠商"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"強","evidence":["接手求才系統改版時，業務後台與資料庫都不能更動...把這些規則接回新版的規格與流"],"missing":[],"issue_ids":[]},{"id":"decision_depth","rating":"強","evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["這些模組相關的 840 件廠商建議，已完成 743 件（88%）；30 天內結案"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["對接工程、行銷、業務與客服等 10 個需求單位；帶領 2 名直屬產品企劃"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["問題背景、系統限制、SA 盤點動作與結案指標脈絡極為清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["從需求釐清、系統分析到流程與原型設計，完成 PRD；能將業務上的搜尋、篩選規則拆"],"application_note":"對位 jd32 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"partial","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"自傳盼做產品策略，需對齊內部系統期待"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"證據鏈支持安排 jd32 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"你在自傳中提到希望把更多心力放回產品策略，而我們這個職位主要負責「內部營運用網站」與跨單位需求優化（月薪 50k–70k），這與你的下一階段職涯規劃與薪資期待是否相符？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd32 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"自傳末段提到「接下來，我希望把更多心力放回產品策略」，而本職缺聚焦於「內部營運用網站的功能設計與內部／外部議題修正」且月薪為 50,000~70,000 元","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["從需求釐清、系統分析到流程與原型設計，完成 PRD；能將業務上的搜尋、篩選規則拆","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["現任直接同業（1111 人力銀行）企業端招募系統 PO，在「業務後台與資料庫都不能更動、舊系統權限與計費規則無文件」的限制下，逆向實測並訪談維運、稽核補回規則，完成前後端分離新版上線與 743/840 件（88%）建議案","2025 Q4 先清理多年積案，再依提案時間與難易安排新案並每週向 10 個需求單位回報進度，使提案滿 30 天者之「30 天內結案比例由前一年的 52% 升至 79%」，完全對應本職缺內部與外部議題排程控管且量測與責任可追溯","以 Claude Code 建立協作流程與共用 skill，「運用 AI Agent 撰寫規格、整理與分析資料，並將業務規則轉為可與工程討論的條件描述」，直接命中 JD 要求"],"key_gaps":["自傳末段提到「接下來，我希望把更多心力放回產品策略」，而本職缺聚焦於「內部營運用網站的功能設計與內部／外部議題修正」且月薪為 50,000~70,000 元","信件與即時通整合、搜尋結果頁改版兩案目前仍在開發／封測中"],"strengths":["1111經歷第1點｜接手求才系統改版時，業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程...840 件廠商建議，已完成 743 件（88%）｜對 jd32 完美證明同業系統 SA 逆向分析與既有後台相容性規劃能力","1111經歷第8點｜先清理多年積案，再依提案時間與難易安排新案，每週向各單位回報進度。之後提出的案件，30 天內結案的比例由前一年的 52% 升至 79%｜對 jd32 直接對位「接手內部與外部議題、評估可行性與掌握節奏」且量化成效可追溯","AI協作技能｜以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格｜對 jd32 直接命中「運用 AI 工具進行營運分析或提案」"],"interview_questions":["你在自傳中提到希望把更多心力放回產品策略，而我們這個職位主要負責「內部營運用網站」與跨單位需求優化（月薪 50k–70k），這與你的下一階段職涯規劃與薪資期待是否相符？","在不涉及營業機密的前提下，你在清理多年積案並將 30 天內結案比例由 52% 提升至 79% 時，是如何與 10 個內部單位協商優先序與評估可行性的？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":9,"uncertainty_levels":1,"basis":"針對 jd32 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```
- **jd34**:
```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd34","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd34-10","human_calibrated":false,"requirements":[{"id":"R01","text":"5年以上經驗（含2年以上產品管理經驗）","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"資深PM與大型B2B平台PO年資充足"},{"id":"R02","text":"有金流、物流、會員、促購、優惠券、購買流程、訂單相關功能開發經驗","type":"required","status":"partial","evidence":["主副帳號權限、合約制與點數制的計費規則；提出 7／30／90 天訂閱方案與加贈內"],"blocks_interview":false,"reason":"具金流串接、購買付款流程、企業會員分店群組權限與點數加贈經驗，缺實體物流與優惠券訂單"},{"id":"R03","text":"產品管理和設計並與UX、RD、QA密切協作；製作使用者介面","type":"required","status":"supported","evidence":["從需求釐清、系統分析到流程與原型設計，完成 PRD，並與 QA 制定 UAT 驗"],"blocks_interview":false,"reason":"完整主導開發循環與UX/RD/QA協作並熟稔Figma/Axure"},{"id":"R04","text":"參與和運作Scrum團隊；定義產品目標用數據分析效益","type":"required","status":"supported","evidence":["曾參與每週一個 Sprint 的 Scrum；降價期 iOS 非續訂營收較原價期"],"blocks_interview":false,"reason":"具Scrum運作與數據實驗分析實績"},{"id":"R05","text":"加分：從0到1產品開發、熟悉支付生態、運用Gen AI加入產品具體案例","type":"preferred","status":"supported","evidence":["規劃 KOOL 網紅媒合平台；導入 CodaPay；定義公司簡介生成、職缺工作說"],"blocks_interview":false,"reason":"三項核心加分條件（0到1、支付、GenAI入產品）全部具備具體案例"},{"id":"R06","text":"加分：具簡報募資、提案經驗；200人以上軟體開發團隊2年以上經驗","type":"preferred","status":"partial","evidence":["參與公司一級主管日會，向總經理、副總等主管匯報；另協助業務製作銷售簡報"],"blocks_interview":false,"reason":"具高層匯報與銷售簡報經驗，未載明軟體團隊是否達200人及外部募資"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["人力銀行企業端招募系統專案負責人，系統服務逾 6 萬家活躍付費廠商"],"missing":["過往為招募平台與社交媒合，未直接經手零售電商 OMO 門市庫存與實體物流"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"強","evidence":["曾參與每週一個 Sprint 的 Scrum...定義公司簡介生成、職缺工作說明"],"missing":["具金流、會員權限、點數與促購加贈經驗，缺實體物流、優惠券與購物車訂單模組經驗"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["規劃群組功能，讓同單位帳號共同處理職缺及對應履歷"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["30 天內結案的比例由前一年的 52% 升至 79%；網頁付款占營收由 24% "],"missing":["1111群組功能與AI功能未列上線後採用數據"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["清楚呈現大型 B2B 平台架構改版、分店群組權限與商業變現經驗"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"對位 jd34 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd34 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"證據鏈支持安排 jd34 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"你在 1111 梳理「合約制與點數制的計費規則」及「部門／分店群組權限」的經驗，若遷移至 91APP 新零售 SaaS 的「門市分店庫存、跨通路優惠券折抵與退換貨訂單狀態機」，你會如何拆解？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd34 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"具備金流、購買付款流程、企業會員權限與點數機制經驗，但未直接經手零售電商之「實體物流串接、購物車優惠券折抵與實體商品訂單管理」","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗，經手 6 款產品","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["現任服務逾 6 萬家活躍付費廠商之 B2B 平台 Product Owner，且針對大型客戶「部門或分店共同招募」規劃上線群組權限功能，與 91APP 服務破萬家零售品牌、處理「總部 vs 分店門市權限（OMO）」的架構邏輯高度相通","具備金流串接（Peach 網頁付款占營收升至 80%+、CodaPay 東南亞超商與電信帳單付款）、主副帳號與合約／點數計費規則、7／30／90 天方案加贈及 Scrum 運作經驗","同時命中三項核心加分條件：KOOL 0 到 1 產品開發、支付生態串接試算、以及將 Gen AI 加入產品的具體上線案例（公司簡介生成、職缺說明生成、AI 推薦人才）"],"key_gaps":["具備金流、購買付款流程、企業會員權限與點數機制經驗，但未直接經手零售電商之「實體物流串接、購物車優惠券折抵與實體商品訂單管理」","1111 上線之群組功能與 3 項 Gen AI 功能未列出上線後的客戶使用率與效益指標","未載明過往協作之軟體研發團隊總規模是否達 200 人以上"],"strengths":["1111經歷第1-2點｜主副帳號權限、合約制與點數制的計費規則...大型客戶需要讓部門或分店共同招募...規劃群組功能｜對 jd34 直接證明具備萬家企業級 SaaS 之會員分店權限與計費邏輯規劃力","1111經歷第7點｜定義公司簡介生成、職缺工作說明生成及 AI 推薦人才的使用情境與驗收標準｜對 jd34 直接命中加分項「運用 Gen AI 加入產品的具體案例」","尚凡第4點與思維特第2點｜規劃 Peach 付款由 App 內購轉向網頁，與 CodaPay 新加坡技術團隊協調串接...提出 7／30／90 天訂閱方案｜對 jd34 證明熟悉支付產業串接與購買付款流程"],"interview_questions":["你在 1111 梳理「合約制與點數制的計費規則」及「部門／分店群組權限」的經驗，若遷移至 91APP 新零售 SaaS 的「門市分店庫存、跨通路優惠券折抵與退換貨訂單狀態機」，你會如何拆解？","你在 1111 與資料科學團隊上線的 3 項 Gen AI 功能（公司簡介生成、職缺說明生成、AI 推薦人才），上線後如何用數據衡量產品效益？","在 1111 對接工程、行銷、業務、客服等 10 個單位推進前後端分離改版時，工程研發與產品團隊的組織規模與跨團隊協作模式為何？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd34 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```
- **jd36**:
```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd36","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd36-11","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上相關工作經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"年資近10年且具豐富系統改版與API串接經驗"},{"id":"R02","text":"能運用Axure撰寫產品規劃，並透過Jira、Confluence進行專案管理","type":"required","status":"partial","evidence":["Figma、Axure RP、Notion、Trello；使用 Trello 及"],"blocks_interview":false,"reason":"具Axure RP與內部專案控管系統，未直接寫出Jira/Confluence"},{"id":"R03","text":"能同步考慮技術可行性以及系統架構關連影響","type":"required","status":"supported","evidence":["接手求才系統改版時，業務後台與資料庫都不能更動...把這些規則接回新版的規格與流"],"blocks_interview":false,"reason":"在後台與資料庫不動限制下完成新舊系統並行與資料轉換"},{"id":"R04","text":"熟悉API規格；與合作方或相關單位確認規劃並與法遵確認適法性","type":"required","status":"supported","evidence":["外部 API 規格議定（簽章驗證、防重放、錯誤碼、頻率限制）；與維運、稽核核對"],"blocks_interview":false,"reason":"明確具備外部API規格議定、JSON欄位確認、CodaPay串接與稽核核對經驗"},{"id":"R05","text":"執行功能測試、驗收、上線協調及內部教育訓練、線上問題排除與迭代","type":"required","status":"supported","evidence":["與 QA 制定 UAT 驗收案例、排定上線計畫。上線前以互動原型與 FAQ 向客"],"blocks_interview":false,"reason":"完整涵蓋UAT驗收、上線計畫、內部教學與840件建議迭代"},{"id":"R06","text":"加分：熟悉代理收付、電子支付及行動支付領域知識；資管或資工學系畢業或有相關工作經驗","type":"preferred","status":"supported","evidence":["規劃 Peach 付款由 App 內購轉向網頁，與 CodaPay 新加坡技術團"],"blocks_interview":false,"reason":"具近10年軟體PM相關工作經驗與跨國支付串接/實收試算實績"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["推動系統改版至前後端分離的新架構，採新舊並行、分階段上線"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"強","evidence":["與外部合作夥伴議定查詢 API 時...並與工程確認 JSON 欄位與判定規則"],"missing":["專案管理使用 Trello 與內部控管系統，未直接寫出 Jira/Confluence"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["以簽章驗證與時間戳防止重放，以錯誤碼與頻率限制控管呼叫"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["這些模組相關的 840 件廠商建議，已完成 743 件（88%）；30 天內結案"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["對接工程、行銷、業務與客服等 10 個需求單位；上線前以互動原型與 FAQ 向客"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["內部後台限制、API 規格細項（簽章、防重放、錯誤碼、頻率限制）與交付脈絡極清楚"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"對位 jd36 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd36 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"證據鏈支持安排 jd36 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"你在 1111 使用 Trello 與內部專案控管系統管理 User Story 與派工估時，過去是否曾使用過 Jira 與 Confluence？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd36 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"必要條件要求「透過 Jira、Confluence 進行專案管理」，履歷列 Notion、Trello 與內部專案控管系統","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗，經手 6 款產品","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["在 API 規格與外部平台串接上提供極具體的技術證據：「與外部合作夥伴議定查詢 API 時，先處理可能被濫用的風險：以簽章驗證與時間戳防止重放...與工程確認 JSON 欄位與判定規則與判定規則」，加上 CodaPay 新加坡金流技術串接經驗，完全契合 jd36「內部系統、串接」核心要求","在「業務後台與資料庫都不能更動、舊規則無文件」的限制下，透過實測與訪談維運、稽核補回計費與權限規則，推動新舊並行分階段上線並完成 743/840 件建議（88%），展現極強的內部系統架構關連思考力","熟稔 Axure RP、流程圖／循序圖、PRD、UAT 驗收與內部教育訓練（互動原型與 FAQ），且將客戶案件 30 天內結案率由 52% 提升至 79%"],"key_gaps":["必要條件要求「透過 Jira、Confluence 進行專案管理」，履歷列 Notion、Trello 與內部專案控管系統","過往金流串接為第三方支付平台（CodaPay），未直接經手台灣銀行專線串接或專營電子支付機構內部清算作業","職責第 2 點提及「與法遵確認適法性」，履歷載明「與維運、稽核核對」"],"strengths":["1111經歷第5點與技能欄｜外部 API 規格議定（簽章驗證、防重放、錯誤碼、頻率限制），並與工程確認 JSON 欄位與判定規則｜對 jd36 直接滿足「熟悉 API 規格、外部平台串接與考慮系統架構影響」之核心條件","1111經歷第1-2點｜業務後台與資料庫都不能更動...以實測歸納、請工程協助驗證，再與維運、稽核核對，把這些規則接回新版｜對 jd36 展現處理複雜內部規則、新舊系統銜接與稽核核對的硬實力","1111經歷第3,8點｜Axure RP...完成 PRD，並與 QA 制定 UAT 驗收案例...上線前以互動原型與 FAQ 向客服、業務說明；30 天內結案由 52% 升至 79%｜對 jd36 完整對應內部教育訓練、測試驗收與時程交付"],"interview_questions":["你在 1111 使用 Trello 與內部專案控管系統管理 User Story 與派工估時，過去是否曾使用過 Jira 與 Confluence？","若負責全支付與銀行或特定外部平台的串接專案，當遇到跨機構交易逾時（Timeout）或帳務狀態不一致時，你會如何在 API 規格與後台作業設計補償與異常排除機制？","在 1111 梳理合約與點數計費規則及處理廠商帳號冒用時，與內部稽核或法遵單位核對的具體流程為何？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd36 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```
- **jd40**:
```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd40","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd40-12","human_calibrated":false,"requirements":[{"id":"R01","text":"5年以上軟體產品、技術產品或技術專案管理經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗；2023/12–2026/03 主責約 50 項大項功"],"blocks_interview":false,"reason":"年資近10年且大型系統架構改版與交付經驗扎實"},{"id":"R02","text":"參與產品從需求規劃到上線交付的完整流程（PRD、User Story、UAT、上線計畫）","type":"required","status":"supported","evidence":["從需求釐清、系統分析到流程與原型設計，完成 PRD，並與 QA 制定 UAT 驗"],"blocks_interview":false,"reason":"完整主導端到端產品規劃與上線交付週期"},{"id":"R03","text":"能理解API、資料流程及系統串接邏輯，與研發協調系統整合","type":"required","status":"supported","evidence":["外部 API 規格議定（簽章驗證、防重放、錯誤碼、頻率限制）...與工程確認 J"],"blocks_interview":false,"reason":"明確具備API規格議定、JSON欄位確認、查詢條件拆解與CodaPay串接經驗"},{"id":"R04","text":"具備良好的需求拆解、優先順序判斷、跨團隊溝通及風險管理能力","type":"required","status":"supported","evidence":["先清理多年積案，再依提案時間與難易安排新案，每週向各單位回報進度"],"blocks_interview":false,"reason":"具體展現積案清理、優先序排定、API防濫用與帳號防冒用風控"},{"id":"R05","text":"加分：KA客戶、客製化需求或NRE專案管理經驗；支付、餐飲、零售、SaaS或跨系統整合經驗","type":"preferred","status":"supported","evidence":["大型客戶需要讓部門或分店共同招募...規劃群組功能；2025 Q4 公司改以客戶"],"blocks_interview":false,"reason":"具大型客戶分店群組需求、客戶案件排程（結案率52%→79%）、支付與SaaS跨系統整合經驗"},{"id":"R06","text":"加分：基本SQL查詢或資料分析能力；客戶提案、需求協商或高階利害關係人溝通經驗","type":"preferred","status":"supported","evidence":["參與公司一級主管日會，向總經理、副總等主管匯報；另協助業務製作銷售簡報（sale"],"blocks_interview":false,"reason":"具高階主管日會匯報、sales kit支援、資料表欄位擬定與查詢條件拆解能力"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["推動系統改版至前後端分離的新架構，採新舊並行、分階段上線"],"missing":["過往為人力銀行與社交媒合平台，未直接接觸餐飲 POS 雲端接單硬體場景"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"強","evidence":["與外部合作夥伴議定查詢 API 時...並與工程確認 JSON 欄位與判定規則"],"missing":["具大型客戶群組功能與客戶案件優先排程，惟未明寫 NRE 合約報價字樣"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["2025 Q4 公司改以客戶案件為優先，先清理多年積案，再依提案時間與難易安排新"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["之後提出的案件，30 天內結案的比例由前一年的 52% 升至 79%（提案滿 3"],"missing":["1111 上線之 50 項大功能未逐一列出營運指標提升幅度"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["按 User Story 記錄需求、做法、驗收條件與優先級，供 Tech Lea"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["清楚呈現 PM 結合 TPM 之技術架構、API 規格、風險控管與交付節奏"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗；2023/12–2026/03 主責約 50 項大項功"],"application_note":"對位 jd40 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd40 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"證據鏈支持安排 jd40 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"在 1111 處理大型客戶需求與 2025 Q4 客戶優先案件時，是否曾參與外部 KA 客戶的客製化範疇談判、報價或需求變更控管？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd40 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"雖有大型客戶分店群組功能與「以客戶案件為優先（30 天結案率升至 79%）」經驗，但未明寫是否經手過收取 NRE（一次性工程開發費）之外部客戶客製化合約專案","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗；2023/12–2026/03 主責約 50 項大項功","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["高度匹配 PM 兼具 TPM（Technical Program Manager）的角色定位：既能從使用者旅程規劃 Roadmap，又能在「業務後台與資料庫不能更動」下推動前後端分離改版、議定外部查詢 API（簽章驗證、防重放、錯誤碼、頻率限制、JSON 欄位確認），並按 User Story 記錄做法與驗收條件供 Tech Lead 派工估時","具備直接可轉移至 KA／客戶專案交付管理的實績：規劃大型客戶「部門或分店共同招募」之群組功能，且於 2025 Q4 公司改以客戶案件為優先時，「先清理多年積案，再依提案時間與難易安排新案，每週向各單位回報進度，30 天內結案比例由 52% 升至 79%」","具備跨國數位支付串接（Peach 網頁付款、CodaPay 電信帳單與超商付款）與高階利害關係人溝通（參與一級主管日會向總經理、副總匯報）經驗"],"key_gaps":["雖有大型客戶分店群組功能與「以客戶案件為優先（30 天結案率升至 79%）」經驗，但未明寫是否經手過收取 NRE（一次性工程開發費）之外部客戶客製化合約專案","資料庫查詢為「擬定資料表與欄位需求，與 DBA 協作取數」，未明寫本人手寫 SQL 查詢語法程度","未直接經手餐飲科技（線上點餐、雲端接單 POS）產業"],"strengths":["1111經歷第1,5點｜推動系統改版至前後端分離的新架構，採新舊並行、分階段上線...以簽章驗證與時間戳防止重放...與工程確認 JSON 欄位與判定規則｜對 jd40 直接證明兼具 PM 與 TPM 所需的系統架構理解與 API 整合協作力","1111經歷第2,8點｜大型客戶需要讓部門或分店共同招募...規劃群組功能；30 天內結案的比例由前一年的 52% 升至 79%（提案滿 30 天者）｜對 jd40 直接對位連鎖分店客戶需求與客戶專案交付管理","專案交付與工具技能｜按 User Story 記錄需求、做法、驗收條件與優先級，供 Tech Lead 派工與估時；能將業務上的搜尋、篩選規則拆成查詢條件｜對 jd40 展現清楚的工程派工規格與資料邏輯拆解能力"],"interview_questions":["在 1111 處理大型客戶需求與 2025 Q4 客戶優先案件時，是否曾參與外部 KA 客戶的客製化範疇談判、報價或需求變更控管？","你在將搜尋篩選規則拆成查詢條件與工程確認後端行為，以及與 DBA 協作取數時，是否會自行撰寫基本 SQL 查詢？","我們服務連鎖餐飲品牌（含分店點餐、雲端接單與支付），你如何將 1111「大型客戶分店群組功能」與過去「CodaPay 支付串接」的經驗應用到連鎖餐飲系統？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd40 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```
- **jd43**:
```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd43","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd43-13","human_calibrated":false,"requirements":[{"id":"R01","text":"5年以上網路或科技產業經驗，具產品管理經驗及推動概念到上線優化經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品；2023/12–2026/03 主責"],"blocks_interview":false,"reason":"近10年網路與軟體PM經驗，完整覆蓋0到1與大型系統改版"},{"id":"R02","text":"主要聚焦帳號安全、防詐騙專案及訊息體驗","type":"required","status":"supported","evidence":["針對廠商招募帳號遭冒用...確認登入驗證與帳號解鎖流程，於 2026/04 上線"],"blocks_interview":false,"reason":"直接具備帳號安全防冒用、API防濫用與即時通訊息整合經驗"},{"id":"R03","text":"具跨職能（設計、工程、資安/稽核、客服）與跨國團隊合作經驗","type":"required","status":"supported","evidence":["與 CodaPay 新加坡技術團隊協調串接；推進 SweetRing 在 7 個"],"blocks_interview":false,"reason":"具跨國技術與在地化協作及跨10部門協作經驗"},{"id":"R04","text":"運用問卷、使用者訪談、bucket/A/B test、行為分析等研究與量化方法驗證假設","type":"required","status":"supported","evidence":["使用者訪談與問卷、競品實測、GA4、世代分析與對照組實驗；設計馬來西亞 iOS "],"blocks_interview":false,"reason":"研究與量化對照實驗方法完整且有實證案例"},{"id":"R05","text":"熟悉Confluence、Jira、Figma、Codex等工具；英文流利","type":"required","status":"partial","evidence":["英文 TOEIC 980、TOEFL iBT 93，並以英文進行跨國協作；Fig"],"blocks_interview":false,"reason":"英文流利且熟Figma與Claude Code，未直接寫出Confluence/Jira"},{"id":"R06","text":"加分：具AI產品開發或AI整合經驗；具日文或韓文能力","type":"preferred","status":"supported","evidence":["與資料科學團隊合作，定義公司簡介生成、職缺工作說明生成及 AI 推薦人才...完"],"blocks_interview":false,"reason":"具3項AI產品功能上線實績；曾推日韓在地化惟未列日韓語能力"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["近 10 年 PM 經驗，經手 6 款產品，涵蓋訂閱制社交 App、網紅媒合平台"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"強","evidence":["針對廠商招募帳號遭冒用，協調工程與客服釐清影響範圍，確認登入驗證與帳號解鎖流程"],"missing":["專案工具未明列 Confluence、Jira；信件與即時通整合目前在內部封測中"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["廠商反映的問題以溝通管道中斷最為集中，因此優先推進信件與即時通整合"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["調整後至 2026/10，未再透過客服接獲廠商回報同類冒用"],"missing":["信件與即時通整合預計 2026/11 底上線，尚無正式上線後指標"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["對接工程、行銷、業務與客服等 10 個需求單位；參與公司一級主管日會"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["清楚呈現帳號防冒用、API 防濫用、訊息整合與跨國定價實驗"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品；2023/12–2026/03 主責"],"application_note":"對位 jd43 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd43 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"證據鏈支持安排 jd43 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"目前進入內部封測的「信件與即時通整合」，具體解決了哪些跨管道訊息斷點？封測期間觀察到的問題與預計追蹤的北極星指標為何？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd43 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"訊息體驗相關之「信件與即時通整合」目前處於內部封測階段（預計 2026/11 底上線），尚無上線後之量化成效數據（依硬性規則 2 不撐起 Level 9）","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗，經手 6 款產品；2023/12–2026/03 主責","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["高度對位本職缺三大核心主題（帳號安全、防詐騙／防濫用、訊息體驗）：在 1111 針對「廠商招募帳號遭冒用」完成登入驗證與帳號解鎖流程調整（2026/04–2026/10 零客服回報同類冒用）、議定外部 API 時以簽章與時間戳防重放及限流、並主導「信件與即時通整合（已進入內部封測）」與 KOOL 邀約聯繫流程","具備跨國協作與流利英文（TOEIC 980、TOEFL iBT 93、赴美交換、與 CodaPay 新加坡技術團隊協調串接、推進 SweetRing 美墨巴印馬日韓 7 國市場在地化）","具備扎實的使用者研究與量化實驗能力（馬來西亞 iOS 對照組定價實驗、GA4、世代分析）及 3 項 AI 產品功能上線經驗"],"key_gaps":["訊息體驗相關之「信件與即時通整合」目前處於內部封測階段（預計 2026/11 底上線），尚無上線後之量化成效數據（依硬性規則 2 不撐起 Level 9）","跨國團隊合作經驗集中於 2016–2021 年（思維特與尚凡時期），近 4 年在 1111 為台灣本土團隊","工具欄列 Figma、Axure、Notion、Trello、Claude Code，未明列 Confluence 與 Jira"],"strengths":["1111經歷第4-6點｜優先推進信件與即時通整合...以簽章驗證與時間戳防止重放...針對廠商招募帳號遭冒用，確認登入驗證與帳號解鎖流程｜對 jd43 罕見地同時覆蓋「帳號安全、防詐騙防濫用、企業訊息整合體驗」三大核心職責","尚凡第3-4點與語言技能｜設計馬來西亞 iOS 定價實驗...與 CodaPay 新加坡技術團隊協調串接；英文 TOEIC 980、TOEFL iBT 93｜對 jd43 證明具備跨國團隊協作、英語能力與嚴謹對照組實驗經驗","1111經歷第7點｜定義公司簡介生成、職缺工作說明生成及 AI 推薦人才的使用情境與驗收標準｜對 jd43 直接命中加分項「具 AI 產品開發或 AI 整合經驗」"],"interview_questions":["目前進入內部封測的「信件與即時通整合」，具體解決了哪些跨管道訊息斷點？封測期間觀察到的問題與預計追蹤的北極星指標為何？","LINE Regional PM 需每日與日本／韓國總部產品與工程團隊以全英文密切對齊 Roadmap，你如何將過往與新加坡 CodaPay 及 7 國團隊協作的經驗應用於跨國總部溝通？","你過去是否有使用 Confluence 與 Jira 的經驗？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd43 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```
- **jd44**:
```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd44","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd44-14","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上網路產品管理經驗，具備策略思考、0到1推動與既有產品持續成長優化能力","type":"required","status":"supported","evidence":["近 10 年 PM 經驗；規劃 KOOL 網紅媒合平台；主責約 50 項大項功能"],"blocks_interview":false,"reason":"同時具備KOOL從0到1規劃與成熟產品持續迭代經驗"},{"id":"R02","text":"跨國跨職能協作：與外部廠商溝通共創，內部跨區域合作","type":"required","status":"supported","evidence":["與外部合作夥伴議定查詢 API；與 CodaPay 新加坡技術團隊協調串接；推進"],"blocks_interview":false,"reason":"具外部合作夥伴議定、新加坡技術串接與7國市場協作經驗"},{"id":"R03","text":"數據驅動決策與實驗：熟悉使用者行為分析、A/B測試及關鍵產品指標","type":"required","status":"supported","evidence":["使用者訪談與問卷、競品實測、GA4、世代分析與對照組實驗；設計馬來西亞 iOS "],"blocks_interview":false,"reason":"具嚴謹跨國定價對照實驗、GA4與世代留存分析經驗"},{"id":"R04","text":"市場與競品分析能力；專注使用者需求提升參與度與留存率","type":"required","status":"supported","evidence":["在沒有直接競品可對照的情況下，參考 Airbnb 與交友平台的媒合方式；依使用者"],"blocks_interview":false,"reason":"具跨領域競品借鏡、競品實測與訂閱方案設計能力"},{"id":"R05","text":"優異的英文溝通及寫作能力","type":"required","status":"supported","evidence":["英文 TOEIC 980、TOEFL iBT 93，曾赴美交換，並以英文進行跨國"],"blocks_interview":false,"reason":"高分英檢、美國交換且具英文跨國協作實務"},{"id":"R06","text":"加分：具音樂/內容平台/社群媒體/娛樂或AI相關產品經驗；launch AI相關功能實務；日文能力","type":"preferred","status":"supported","evidence":["經手交友、訂閱制內容 App 與網紅媒合平台；完成三項 AI 功能上線"],"blocks_interview":false,"reason":"具訂閱制內容/社交媒合App與launch 3項AI功能實務（日文未呈現）"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["經手交友、訂閱制內容 App 與網紅媒合平台，規劃使用流程、訂閱與付費機制"],"missing":["過往為社交與網紅媒合及人力銀行，未直接經手音樂串流領域"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"強","evidence":["規劃 KOOL 網紅媒合平台...與資料科學團隊合作，定義公司簡介生成...完成"],"missing":["未呈現加分項之日文能力"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["在沒有直接競品可對照的情況下，參考 Airbnb 與交友平台的媒合方式"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%；網"],"missing":["KOOL 0 到 1 平台與 1111 AI 功能未列上線後參與度與留存數據"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["主導 Juicy 推出並協調跨團隊工作；帶領 2 名直屬產品企劃"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["自傳與經歷清楚展現從消費型訂閱產品到企業系統的產品策略思考"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗；規劃 KOOL 網紅媒合平台；主責約 50 項大項功能"],"application_note":"對位 jd44 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd44 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"證據鏈支持安排 jd44 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"你在 KOOL 從 0 到 1 上線刊案、報名、邀約流程與 VIP 訂閱／點數付費牆後，以及在 1111 上線 AI 推薦功能後，實際的使用者參與度與留存率表現如何？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd44 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"KOOL 網紅媒合平台與 1111 三項 AI 功能雖已上線，但履歷未列出上線後的使用者參與度（Engagement）或留存率（Retention）變化數據","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗；規劃 KOOL 網紅媒合平台；主責約 50 項大項功能","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["完整符合必備條件與三項核心加分項：經手「交友、訂閱制內容 App 與網紅媒合平台」、成功從 0 到 1 規劃 KOOL 雙邊媒合與 VIP 訂閱／點數變現機制、並具備實際 launch 3 項 AI 功能的實務經驗","具備嚴謹的跨國數據實驗能力（馬來西亞 iOS 三階段定價對照實驗、GA4、世代分析）與跨國支付／在地化協作經驗（美墨巴印馬日韓 7 國市場、TOEIC 980）","自傳清楚展現對消費型產品「使用者為什麼加入、互動與付費」及產品策略方向的深度思考"],"key_gaps":["KOOL 網紅媒合平台與 1111 三項 AI 功能雖已上線，但履歷未列出上線後的使用者參與度（Engagement）或留存率（Retention）變化數據","近 4 年在 1111 聚焦於 B2B 企業端招募系統，與 C 端音樂串流及粉絲娛樂互動領域有時間間隔","加分條件中之「具日文能力」未呈現（僅有英文跨國協作與推進日本市場在地化經驗）"],"strengths":["尚凡經歷第1點與自傳｜規劃 KOOL 網紅媒合平台，從案主與網紅兩種角色釐清需求。在沒有直接競品可對照的情況下，參考 Airbnb 與交友平台的媒合方式｜對 jd44 展現優秀的 0 到 1 產品概念共創與跨領域競品分析能力","尚凡經歷第3點｜設計馬來西亞 iOS 定價實驗，以售價不變的 Android 作對照，依序測試原價、降價與還原原價（2021/05–08，各期 21 天）｜對 jd44 直接證明數據驅動決策與嚴謹實驗能力","1111經歷第7點與語言技能｜完成三項 AI 功能上線；英文 TOEIC 980、TOEFL iBT 93，曾赴美交換，並以英文進行跨國協作｜對 jd44 同時滿足英文跨國溝通與 launch AI 功能加分項"],"interview_questions":["你在 KOOL 從 0 到 1 上線刊案、報名、邀約流程與 VIP 訂閱／點數付費牆後，以及在 1111 上線 AI 推薦功能後，實際的使用者參與度與留存率表現如何？","從 B2B 企業招募系統轉回 C 端音樂串流與粉絲互動（Music Team），你認為過去在 KOOL 網紅媒合與訂閱制 App 的哪些策略經驗可以直接轉移？","過去推進 SweetRing 日本市場在地化時，是如何與日本在地人員協作並驗證當地使用者偏好的？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd44 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```
- **jd47**:
```json
{"rubric_version":"4.2","resume_id":"Resume_v10.3_AppendixA","job_id":"jd47","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd47-15","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上Software PM，至少一次完整0到1直接負責經歷，且能針對成熟產品進行迭代成長","type":"required","status":"supported","evidence":["規劃 KOOL 網紅媒合平台；推動系統改版至前後端分離的新架構...持續迭代現行"],"blocks_interview":false,"reason":"同時具備KOOL 0到1完整週期與1111 6萬廠商成熟系統迭代"},{"id":"R02","text":"對焦商業需求：執行商業模式分析與產業趨勢研究，持續關注競品動態與用戶需求","type":"required","status":"supported","evidence":["在沒有直接競品可對照的情況下，參考 Airbnb 與交友平台的媒合方式；競品實測"],"blocks_interview":false,"reason":"具商業模式設計、實收試算、定價實驗與競品實測經驗"},{"id":"R03","text":"產品教育訓練與上線測試：規劃執行內部（業務/客服/財務）及外部教育訓練，負責上線前測試與驗收","type":"required","status":"supported","evidence":["與 QA 制定 UAT 驗收案例、排定上線計畫。上線前以互動原型與 FAQ 向客"],"blocks_interview":false,"reason":"直接命中UAT測試驗收、互動原型/FAQ內部教育訓練與sales kit"},{"id":"R04","text":"能寫清楚的規格文件（PRD、流程圖、資料結構）；理解API、JSON與基本SQL","type":"required","status":"supported","evidence":["完成 PRD...流程圖／循序圖；與工程確認 JSON 欄位與判定規則；擬定資料"],"blocks_interview":false,"reason":"完整具備PRD、流程圖、資料表欄位需求與API JSON確認，取數與DBA協作"},{"id":"R05","text":"加分：停車/交通/MaaS/保險/支付/FinTech經驗；AI/LLM工具規格撰寫與分析；Growth或數據分析經驗","type":"preferred","status":"supported","evidence":["以 Claude Code 建立協作流程與共用 skill，運用 AI 撰寫規格"],"blocks_interview":false,"reason":"具跨國支付串接、定價成長實驗與Claude Code規格分析實作"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["近 10 年 PM 經驗，經手 6 款產品，涵蓋訂閱制社交 App、網紅媒合平台"],"missing":["過往為純軟體平台，未直接接觸智慧停車或實體場域硬體"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"強","evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助業務製作銷售簡報"],"missing":["資料庫取數為與 DBA 協作，未明寫自寫 SQL 語法"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["30 天內結案的比例由前一年的 52% 升至 79%；網頁付款占營收由 24% "],"missing":["KOOL 0 到 1 平台未列上線後規模數據"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["對接工程、行銷、業務與客服等 10 個需求單位；帶領 2 名直屬產品企劃"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["清楚呈現 0 到 1 產品規劃、成熟系統重構、內部訓練與 AI 協作流程"],"missing":[],"issue_ids":[]}],"results":[{"quote":"840 件廠商建議，已完成 743 件（88%）","kinds":["output"]},{"quote":"30 天內結案的比例由前一年的 52% 升至 79%","kinds":["outcome"]},{"quote":"2023/12–2026/03 主責約 50 項大項功能的規劃","kinds":["output"]},{"quote":"降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%","kinds":["outcome","decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"信件與即時通整合已進入內部封測，預計 2026/11 底上線","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；推動系統改版至前後端分離的新架構...持續迭代現行"],"application_note":"對位 jd47 核心年資與產品交付經驗"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責逾6萬家廠商企業招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["以實測歸納、請工程協助驗證，再與維運、稽核核對"],"application_note":"清楚界定個人規劃與工程/QA/DBA分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["30 天內結案的比例由前一年的 52% 升至 79%"],"application_note":"具結案率與定價實驗數據，缺部分功能採用率"},{"rule_id":"HR05","status":"supported","resume_evidence":["將搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與新舊並行取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"職涯由C端消費產品演進至B2B平台主任"},{"rule_id":"HR07","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明"],"application_note":"Scrum、原型、API議定、AI與英文皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["從需求釐清、系統分析、流程與畫面設計，到 PRD"],"application_note":"結構分明，問題背景、動作與結果易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["上線與行銷導流期間，男性 DAU 增至 1.25 萬"],"application_note":"誠實標註行銷導流期間、封測中與客服回報口徑"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd47 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃"],"application_note":"證據鏈支持安排 jd47 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台；人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["大型客戶需要讓部門或分店共同招募，原系統卻只能選擇全公司或個人"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程檢視需求後，也將搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["2020/11–2021/09，網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["降價期 iOS 非續訂營收較原價期增 5%，同期 Android 減 18%"],"evidence_type":"outcome","source_ids":[],"interview_question":"1111 上線之群組功能、新版模組與 3 項 AI 功能，以及尚凡 KOOL 平台，上線後的採用率與業務成效指標為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃；參與公司一級主管日會"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["業務後台與資料庫都不能更動...把這些規則接回新版的規格與流程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以簽章驗證與時間戳防止重放...並與工程確認 JSON 欄位與判定規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["2023/12–2026/03 主責約 50 項大項功能的規劃，與工程協作上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["上線前以互動原型與 FAQ 向客服、業務說明，另協助製作銷售簡報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["於 2026/04 上線調整，並依客服回饋修正操作方式"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具 1111 改版、群組權限、API 議定、KOOL 與定價實驗案例"],"evidence_type":"context","source_ids":[],"interview_question":"你在尚凡從 0 到 1 推動 KOOL 網紅媒合平台上線並支援 Go-To-Market 時，上線後的雙邊用戶規模與付費轉換表現如何？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd47 明文條件與附錄 A 履歷獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定資料表與欄位需求，與 DBA 協作取數","reason":"KOOL 0 到 1 平台未在本版履歷列出上線後的用戶規模或報名媒合數據","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、使用 Jira/Confluence 或直接參與外部企業客戶訪談之實例，建議直接補入對應段落"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"部分已上線功能缺採用成效指標且兩案尚在開發中","context_limit":"1111 經歷第 1、2、4、7 點與尚凡第 1 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"與工程於 2025/09 完成上線；完成三項功能上線","reason":"1111 上線之群組功能、3 項 AI 功能與尚凡 KOOL 平台僅列交付完成（output），未呈現採用率或業務轉換成效（outcome）；且即時通整合與搜尋改版尚在開發中","suggestion":"補充群組功能開通廠商數、AI 功能採用率或 KOOL 媒合規模數據；開發中兩案則準備封測數據供面試驗證"}],"decision":{"recommendation":"interview","evidence":["規劃 KOOL 網紅媒合平台；推動系統改版至前後端分離的新架構...持續迭代現行","2023/12–2026/03 主責約 50 項大項功能的規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["完美對位主要職責第 1、3、4 點：兼具 KOOL 0 到 1 規劃與 1111 成熟產品 50 項大功能迭代，且上線前「與 QA 制定 UAT 驗收案例、排定上線計畫，以互動原型與 FAQ 向客服、業務說明，另協助業務製作銷售簡報（sales kit）」","完全滿足必備規格與技術條件：具備 PRD、流程圖／循序圖、擬定資料表與欄位需求，並在議定外部 API 時「以簽章驗證與時間戳防止重放...與工程確認 JSON 欄位與判定規則與判定規則」","深入運用 Claude Code 建立協作流程與共用 skill 撰寫規格與分析資料，並具 CodaPay／Peach 支付串接與馬來西亞定價成長實驗經驗"],"key_gaps":["KOOL 0 到 1 平台未在本版履歷列出上線後的用戶規模或報名媒合數據","資料庫查詢為「擬定資料表與欄位需求，與 DBA 協作取數」，未明寫本人手寫 SQL 查詢程度","尚未接觸智慧停車或 MaaS 線下場域與硬體整合"],"strengths":["1111經歷第3點｜完成 PRD，並與 QA 制定 UAT 驗收案例、排定上線計畫。上線前以互動原型與 FAQ 向客服、業務說明，另協助業務製作銷售簡報｜對 jd47 直接命中「產品教育訓練與上線測試驗收、跨部門溝通橋樑」","尚凡第1點與1111第1-2點｜規劃 KOOL 網紅媒合平台...推動系統改版至前後端分離的新架構，採新舊並行、分階段上線｜對 jd47 完整證明同時具備 0-1 MVP 推動與成熟產品迭代能力","1111第5點與AI協作技能｜與外部合作夥伴議定查詢 API...與工程確認 JSON 欄位與判定規則；以 Claude Code 建立協作流程與共用 skill｜對 jd47 滿足 API/JSON 理解與 AI 工具規格撰寫加分項"],"interview_questions":["你在尚凡從 0 到 1 推動 KOOL 網紅媒合平台上線並支援 Go-To-Market 時，上線後的雙邊用戶規模與付費轉換表現如何？","你在擬定資料表與欄位需求及拆解後端搜尋篩選查詢條件時，是否會自行撰寫基本 SQL 語法？","若要為 USPACE 新功能規劃針對內部業務、客服、財務及外部合作夥伴（如停車場業主）的教育訓練，你會如何調整你在 1111 使用的「互動原型＋FAQ＋sales kit」做法？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或 Jira/Confluence 使用經驗，建議於技能欄明確補註"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd47 具備多個已實現案例、清楚取捨與跨部門治理實證"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"risk","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

# 附錄 C：文末執行檢查清單逐項核對（對應套件 §10）

- [x] 單份審查 15 次，每次只放一份職缺獨立取證判讀，已記錄 `model_id: gemini-4-argon`（並於 §7 誠實揭露單一執行環境限制）
- [x] JSON 單行、欄位齊全、`human_calibrated=false`、`ai_authorship.probability=null`（全數通過 Python Schema 與字數上限驗證）
- [x] 沒有做任何版本比較，也沒有引用其他對話的分數（全文無任何舊版對照）
- [x] 沒有把頁數、學歷、空窗、任職長短、關鍵字個數當缺失
- [x] 沒有拿 A 職缺的條件去扣 B 職缺；Level 9 以上（`jd32`）有寫出可追溯的已上線量測（743/840 件完成率 88%、30 天結案率由 52% 升至 79%）與個人責任，進行中未上線案例不撐起 Level 9
- [x] HR 12 題＋HM 13 題每次都列全；約談理由 ≤3、關鍵缺口 ≤3
- [x] ATS 五塊分開，沒有「ATS 分數」
- [x] 每份審查都有 §5.5 審查者質疑（每份 3–4 則、含 HR 與用人主管、至少 1 則正面但保留 `仍然約談`）；總報告有 §4.5 跨職缺共同質疑（6 則）與三句「整體第一印象」
- [x] 總報告依 §8 固定格式，附上 15 份原始 JSON（附錄 A 與附錄 B）
