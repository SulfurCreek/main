# 履歷驗證報告：單份履歷 × 15 職缺｜2026-10-16｜model_id: gemini-4-argon｜human_calibration: not_run

## 1. 結論（≤6 行，先講答案）
- 招聘決定分布（interview／clarify_first／not_matched／insufficient_info 各幾份職缺）：`interview`×15、`clarify_first`×0、`not_matched`×0、`insufficient_info`×0（15 份職缺皆無 contradicted 明文必要條件，證據足以支持面試）。
- Level 分布（列出每個 Level 的職缺數；不算平均）：**Level 9×3 份**（`jd11`、`jd31`、`jd32`）、**Level 8×9 份**（`jd09`、`jd20`、`jd26`、`jd30`、`jd36`、`jd40`、`jd43`、`jd44`、`jd47`）、**Level 7×3 份**（`jd03`、`jd14`、`jd34`）；嚴格執行硬性規則 2，進行中未上線案例（如信件與即時通整合、搜尋改版）不單獨支撐 Level 9。
- 最適合投遞的 5 份職缺代號與一句理由：`jd32`（同業招募系統 PO 且具 SA 系統分析、1,726 張工單交付與 Claude Code 實績）、`jd11`（直接具備 HR 招募系統 PO、Scrum/Kanban、3 項 GenAI 上線與 Claude Code 多分支流程）、`jd31`（主導 6.6 萬家企業平台改版、具備完整 Scrum 儀式與 KOOL 0 到 1 經驗）、`jd43`（具備 2026/04 帳號防冒用簽章驗證上線閉環、跨國協作與訊息整合規劃）、`jd30`（具備 KOOL 0 到 1 探索驗證 8 萬次報名、Claude Code 工作流與跨國金流經驗）。
- 最可能被卡的 3 份職缺代號與卡在哪個條件：`jd34`（卡在必備條件之「零售電商物流、購物車結帳、優惠券與門市 OMO 訂單功能經驗」未呈現）、`jd14`（卡在必備條件點名之「熟悉 Firebase」未呈現且近 4 年重心為 B2B 平台而非 OTT 影音成長）、`jd20`（卡在必備條件要求「獨立使用 SQL/BI 查詢」而履歷為擬定資料表欄位交 DBA 撈取，且純 B2B 年資約 3 年 10 個月略低於 5 年門檻）。

## 2. 職缺矩陣（每列一份職缺，不加總）
| 職缺 | 決定／Level | 六維度（簡寫：強/足/待/未） | 決定性條件（≤20 字） | 約談理由第一名（≤20 字） |
| :-- | :-: | :-: | :-- | :-- |
| [jd03 產品經理 (Pi錢包)｜拍付國際](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F91sgi) | interview／Level 7 | 足/強/強/強/強/強 | 2年PM＋API：supported | 具網頁金流與跨國支付串接實績 |
| [jd09 產品經理 Product Manager｜微拓科技 (beBit TECH)](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F82slf) | interview／Level 8 | 強/足/強/強/強/強 | 3年PM＋B2B：supported | 主責6.6萬廠商平台與配對優化 |
| [jd11 【北士科】Product Manager｜沛思坦 (Pacston)](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F8o3s3) | interview／Level 9 | 強/強/強/強/強/強 | 5年PM＋HR系統：supported | 現任招募PO且上線3項AI功能 |
| [jd14 D441 MyVideo影音產品Growth PM｜台灣大哥大](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F94le0) | interview／Level 7 | 足/足/強/強/強/強 | 3年成長＋GA4：partial | 具三階段定價實驗與網頁金流轉換實績 |
| [jd20 Senior Product Manager (Anti-Scam BU/2B)｜Gogolook](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F950oe) | interview／Level 8 | 強/足/強/強/強/強 | B2B＋防冒用：supported | 具帳號防冒用簽章驗證與AI |
| [jd26 全支付- Product Manager (專案執行)](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F7996v) | interview／Level 8 | 強/足/強/強/強/強 | Axure＋風險：supported | 熟稔Axure與全國封測上線 |
| [jd30 資深產品經理｜Senior Product Manager｜USPACE](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F8bymx) | interview／Level 8 | 強/足/強/強/強/強 | 0到1＋AI流程：supported | 具KOOL 0到1與AI工作流 |
| [jd31 資深產品經理【擴編】｜人易科技 (NUEIP)](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F92io8) | interview／Level 9 | 強/強/強/強/強/強 | 企業系統＋Scrum：supported | 主導6.6萬廠商系統與Scrum |
| [jd32 產品專案經理(內部系統)｜104人力銀行](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F94n8b) | interview／Level 9 | 強/強/強/強/強/強 | 同業PO＋SA＋AI：supported | 同業招募PO具SA與AI實績 |
| [jd34 SaaS 產品經理 / Product Owner｜91APP](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F8dbp3) | interview／Level 7 | 足/足/強/強/強/強 | 電商金流物流訂單：partial | 具6.6萬廠商B2B平台與Scrum經驗 |
| [jd36 全支付- Product Manager (內部系統、串接)](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F8ocje) | interview／Level 8 | 強/足/強/強/強/強 | Axure＋系統串接：supported | 熟稔系統分析、Axure與金流串接 |
| [jd40 【PMC】軟體產品經理 (PM / TPM)｜QuickClick快一點](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F94fod) | interview／Level 8 | 強/足/強/強/強/強 | 5年PM＋系統整合：supported | 具50大項功能交付與系統分析控管 |
| [jd43 Product Manager (Messenger \& OA)｜LINE Taiwan](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F95jyg) | interview／Level 8 | 強/強/強/強/強/強 | 防冒用＋跨國：supported | 具帳號防冒用簽章驗證與即時通規劃 |
| [jd44 \[Music\] Senior Product Planner｜KKBOX (KKCompany)](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F93qa8) | interview／Level 8 | 強/強/強/強/強/強 | 0到1＋實驗：supported | 具0到1、定價實驗與AI上線 |
| [jd47 產品經理｜Product Manager｜USPACE](https://www.google.com/search?q=https%3A%2F%2Fwww.104.com.tw%2Fjob%2F95mvt) | interview／Level 8 | 強/足/強/強/強/強 | 0到1＋迭代：supported | 兼具KOOL 0到1與系統迭代 |

## 3. 職缺分群（依職缺內容自行分，最多 5 群）
| 群組 | 職缺代號 | 共同優勢 | 共同卡關 |
| :-- | :-- | :-- | :-- |
| 1. B2B SaaS 與企業系統 | `jd09`、`jd11`、`jd31`、`jd32`、`jd34` | 現任 1111 企業端招募系統與求職端公司頁 PO（服務 6.6 萬家活躍付費廠商），主責約 50 項大項功能與 111 項細項上線、規劃部門／分店群組權限功能並完成上線、處理週期由 100.4 天降至 30.9 天，且具備入職初期完整 Scrum（一週一 Sprint）與現行 Kanban 經驗，`jd11`、`jd31`、`jd32` 高度對位達 Level 9。 | `jd34` 要求零售電商實體物流、優惠券與 OMO 訂單經驗；`jd09` 為 CDP+MA 行銷自動化領域；部分職缺點名外部 Jira/BI 工具。 |
| 2. AI 賦能與技術型 PM | `jd30`、`jd40`、`jd47` | 同時具備 KOOL 從 0 到 1 探索商業模式（1.6 萬網紅檔案、半年 8 萬多次報名）與 1111 成熟產品迭代；自建 Claude Code 12 條分支與 23 個共用 skill，並能「把衝突的搜尋邏輯轉成工程條件」及擬定資料庫資料表與欄位。 | `jd30`、`jd47` 必備條件要求理解 JSON 與基本 SQL，履歷雖證明懂資料表與欄位結構，但取數交由 DBA 撈取且未明寫 JSON 字樣；`jd40` 偏好 KA/NRE 合約管理經驗。 |
| 3. 防詐資安與跨國通訊產品 | `jd20`、`jd43` | 具備 2026/04 十多家廠商帳號遭冒用之求職者個資風險評估、04/17 上線簽章驗證且至 10 月零復發之完整閉環；另有信件與即時通整合規劃、7 國市場在地化與 TOEIC 980 英語協作實務。 | 「信件與即時通整合」尚在開發中（依規準不能支撐 Level 9）；`jd20` 要求獨立 SQL/BI 查詢、5 年以上純 B2B 經驗與海外企業/政府客戶對接。 |
| 4. C 端訂閱成長與內容平台 | `jd14`、`jd44` | 具備馬來西亞 iOS 三階段定價實驗（21 天期對照組拆解）、Peach 網頁付款占營收由 24% 升至 80% 以上、KOOL 0 到 1 雙邊媒合市集（8 萬次報名）與競品實測反推配對排序規則。 | `jd14` 必備條件點名 Firebase 未呈現，且近 4 年重心轉向 B2B 企業系統；兩職缺分屬 OTT 影音與音樂串流，與過往社交媒合領域有產業差異。 |
| 5. 支付與金融生態 | `jd03`、`jd26`、`jd36` | 具備 CodaPay 東南亞電信帳單與超商付款串接、抽成稅費與撥款週期實收試算、Peach 網頁金流規劃、Axure 原型與 PRD 撰寫、法務稽核協作，以及全國客服封測後離峰停機 1.5 小時切換上線。 | `jd03` 偏好銀行或政府機關直接串接；`jd26`、`jd36` 偏好專營電子支付機構代理收付帳務知識且必備條件點名 Jira/Confluence（履歷使用內部 ticket 系統與 Notion/Trello）。 |

## 4. 跨職缺重複出現的缺口（≥3 份職缺出現才列；≤6 項）
| 缺口 | 出現職缺數 | 影響哪類職缺 | 履歷原句（≤40 字） | 需要候選人補什麼事實 |
| :-- | :-: | :-- | :-- | :-- |
| 1. 資料庫取數交由 DBA 撈取，未明載本人手寫 SQL 語法或 BI 儀表板操作 | 6 份（`jd20`、`jd30`、`jd31`、`jd40`、`jd47`、`jd09`） | 防詐 B2B、技術型 PM 與企業 SaaS | `由我擬定取數的資料表與欄位，交 DBA 撈取` | 若本人具備撰寫基礎 SQL（如 `SELECT / JOIN / WHERE`）驗證資料或操作 BI 工具之經驗，請補充具體查詢情境；若無則維持現狀並於面試展示 Schema 設計邏輯。 |
| 2. 專案管理使用公司內部 ticket／卡片系統與 Notion/Trello，未直接寫出 Jira／Confluence | 5 份（`jd11`、`jd20`、`jd26`、`jd36`、`jd43`） | 外商、支付機構與點名 Atlassian 工具之職缺 | `Notion、Trello、公司內部專案系統（ticket追蹤）` | 若過往任一階段曾使用 Jira 或 Confluence，可直接列名；若僅使用內部 ticket 系統，面試時說明 ticket 狀態流、權限與 Sprint/Kanban 看板運作方式即可。 |
| 3. 即時通整合與搜尋結果頁改版兩案尚在「開發中」，無上線後量化結果 | 4 份（`jd20`、`jd32`、`jd40`、`jd43`） | 關注近期通訊體驗、搜尋轉換或大型專案結案之職缺 | `信件與即時通整合、搜尋改版（兩案皆開發中）` | 依硬性規則 2，開發中案例僅支持決策取捨（`decision`）而不計入已實現成果（`outcome`）；請準備兩案的最新上線進度、UAT 驗收標準與預計追蹤之北極星指標。 |
| 4. 金流與海外經驗集中於 B2C 商戶端與第三方聚合支付，缺銀行／電支清算與海外 B2B 客戶實績 | 5 份（`jd03`、`jd20`、`jd26`、`jd34`、`jd36`） | 電子支付機構、海外 B2B 防詐與新零售 OMO 職缺 | `導入 CodaPay，開放印尼、泰國電信帳單與超商付款` | 請準備 CodaPay 跨國對帳、異常退款處理與 1111 企業客戶權限風控之細節，說明如何遷移至銀行串接、電支清算或海外企業客戶場景。 |
| 5. API 規格未明文提及 JSON 資料格式與欄位定義細節 | 3 份（`jd30`、`jd36`、`jd47`） | 要求理解 API、JSON 與系統介接規格之技術型 PM 職缺 | `API 串接規劃、舊系統資料盤點` | 若在串接 CodaPay、社群認證或內部系統時曾參與定義或檢視 API Request/Response JSON 欄位與錯誤碼，建議於技能欄或面試中具體說明。 |

## 5. 評語（合併後）

### 5.1 做得好（3 點；每點至少 2 份職缺支持，附原句與職缺代號）
- **1111 全球華人經歷（B2B 大型系統交付、排程提速與問題拆解已上線）**：
  - 原句：`約 50 項大項功能上線（2023/12–2026/03）`；`需求平均處理週期由 100.4 天降至 30.9 天`；`查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序...廠商也能自行切換排序（已上線）`
  - 支持職缺：`jd09`、`jd11`、`jd31`、`jd32`、`jd40`（共 15 份職缺全數支持）
  - 為什麼有用：同時提供高吞吐交付量（50 大項功能、1,726/1,857 張單）、處理週期縮短近 70% 的效率成果，以及從客服抱怨追查排序邏輯根因並反推競品完成上線的完整閉環，且清楚標註母體基準日（`2026/04/30` 全站 約 6.6 萬家）與留存率非因果聲明（`144 天後仍付費 91.4% vs 同期其餘廠商 89.2%`），衡量品質極高。
- **尚凡國際經歷（KOOL 從 0 到 1 雙邊媒合市集探索與三階段定價實驗）**：
  - 原句：`KOOL 從 0 到 1 探索商業模式：由公司行號尋找微型網紅合作...網紅檔案約 1.6 萬份，半年累計 8 萬多次報名`；`定價實驗採原價、iOS 降價、還原原價三階段，以 Android 售價不變作對照（馬來西亞，2021/05–08，各期 21 天）`
  - 支持職缺：`jd03`、`jd14`、`jd30`、`jd31`、`jd34`、`jd44`、`jd47`
  - 為什麼有用：具體交代 0 到 1 產品如何參考 Airbnb 與交友配對機制設計雙邊市場、設定精選網紅資格門檻並取得 1.6 萬份檔案與 8 萬次報名的實績；定價實驗則完整呈現 21 天實驗期、對照組基準（iOS +5% vs Android -18%）與最終決策，直接滿足 0 到 1 與 Growth 實驗要求。
- **1111 經歷與專業技能（資安防冒用閉環、完整 Scrum 儀式與 Claude Code 工程邏輯轉譯）**：
  - 原句：`求才端可存取大量求職者個資，冒用登入即有外洩風險...與工程協作於 2026/04/17 上線簽章驗證`；`入職初期跑過完整 Scrum（一週一個 Sprint、Daily stand-up、Review 與 Retro）`；`自建 Claude Code 協作流程（12 條分支、23 個共用 skill）...把衝突的搜尋邏輯轉成工程條件`
  - 支持職缺：`jd11`、`jd20`、`jd26`、`jd30`、`jd31`、`jd32`、`jd36`、`jd43`、`jd47`
  - 為什麼有用：不僅展示資安危機影響評估與長達半年的零冒用觀察期，更清楚交代 Scrum 與 Kanban 雙重敏捷實務、公司內部 ticket 追蹤系統，以及將 AI 工具用於轉譯複雜工程條件與落地 3 項 AI 產品功能的實戰深度。

### 5.2 可改進（≤6 點；欄位依 §6.2；只列 ≥2 份職缺重複或 blocking 的項目）
- 位置：專業技能（研究與數據）與 1111 經歷第 7 點
  - 原句：`由我擬定取數的資料表與欄位，交 DBA 撈取，再以 Google Sheet 比對`
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：在 `jd20`、`jd30`、`jd31`、`jd40`、`jd47` 等要求「理解基本 SQL」或「獨立使用 SQL/BI 查詢」的職缺中，雖能證明理解資料表與欄位結構，但仍會被判定為 `partial` 並在面試中被追問是否具備手寫 SQL 能力。
  - 建議方向：若本人實際會寫基礎 SQL（如 `SELECT / JOIN / GROUP BY`）或曾在測試環境自行查詢驗證，建議直接補入「研究與數據」或「工具與技術素養」欄；若完全由 DBA 撰寫語法，則維持現有誠實表述即可。
- 位置：專業技能（工具與技術素養／跨部門與整合）
  - 原句：`API 串接規劃、舊系統資料盤點`；`Markdown、基本 HTML／CSS、資料庫知識`
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：在 `jd30`、`jd36`、`jd47` 等明文要求「理解 API、JSON」或「熟悉 API 規格」的職缺中，因未提及 `JSON` 或 API 規格欄位定義，導致該項必要條件僅能判為 `partial`。
  - 建議方向：若在規劃 CodaPay 金流串接、社群認證或內部系統介接時，曾實際檢視或定義 API JSON 格式與狀態碼，建議將原句微調補充具體事實（例如標註含 JSON 欄位對照或錯誤碼定義）。
- 位置：1111 全球華人經歷第 5 點
  - 原句：`信件與即時通整合排在其他新功能之前；搜尋結果頁...改版排在新功能職缺健檢之前（兩案皆開發中）`
  - 問題類型：`measurement`
  - 嚴重度：`interview_follow_up`
  - 影響：依硬性規則 2，開發中案例僅能支持決策與優先序取捨（`decision`），不能算已實現結果（`outcome`），使仰賴即時通體驗的 `jd43` 維持在 Level 8 而非 Level 9。
  - 建議方向：若任一案近期已完成封測或部分上線，可更新上線日期與初步數據；若仍在開發中，無須編造結果，於面試準備好預計追蹤的成功指標（如抱怨工單降幅、搜尋點擊轉換率）即可。
- 位置：專業技能（工具與技術素養）
  - 原句：`Figma、Axure RP、Notion、Trello、公司內部專案系統（各單位需求以 ticket 與卡片追蹤）`
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：在點名 `Jira、Confluence` 的 5 份職缺（`jd11`、`jd20`、`jd26`、`jd36`、`jd43`）中，雖已透過「以 ticket 與卡片追蹤」證明具備同類 Issue Tracking 概念，但字面比對仍屬 `partial`。
  - 建議方向：若過往在尚凡或思維特曾使用 Jira/Confluence 可直接補上名稱；若無則保留現有誠實描述，不捏造未用過之軟體名稱。

### 5.3 面試最可能被追問的 5 題（附建議準備的事實，不代答）
1. **資料庫結構與 SQL 取數邊界（對應 `jd20`、`jd30`、`jd31`、`jd40`、`jd47`）**：
   - **追問問題**：「你在 1111 撈取 2026/04/30 與 09/21 廠商名冊時，提到『由我擬定取數的資料表與欄位，交 DBA 撈取』——請問你如何得知有哪些資料表與欄位可用？遇到跨表關聯或邊界條件（如退費、展延廠商）時如何定義？你本人是否會寫基礎 SQL？」
   - **建議準備的事實**：準備當時開給 DBA 的取數需求單規格結構（包含實際用到的 Table 類型、主鍵關聯邏輯、活躍付費狀態的篩選條件，以及拿到快照後如何在 Google Sheet 檢查異常值與計算 144 天留存率（91.4% vs 其餘廠商 89.2%））。
2. **Claude Code 12 條分支流程與「把衝突搜尋邏輯轉成工程條件」（對應 `jd11`、`jd20`、`jd30`、`jd32`、`jd47`）**：
   - **追問問題**：「請具體說明你自建的 Claude Code 12 條分支與 23 個共用 skill 是如何運作的？『把衝突的搜尋邏輯轉成工程條件』具體解決了什麼衝突？」
   - **建議準備的事實**：準備該次搜尋邏輯衝突的真實背景（原本哪兩個條件互相衝突、業務或用戶期待什麼、如何用 Claude Code 窮舉邊界案例並轉化為工程師可直接實作的布林條件／權重或狀態機表）。
3. **2026/04 廠商帳號遭冒用危機處置與簽章驗證架構（對應 `jd20`、`jd26`、`jd36`、`jd43`）**：
   - **追問問題**：「2026/04 十多家廠商帳號遭冒用時，攻擊者是透過什麼漏洞或路徑登入？你在 04/17 上線的『簽章驗證』在前端、後端與舊系統相容性上做了什麼設計？如何確認不會誤擋正常付費廠商？」
   - **建議準備的事實**：準備冒用事件的排查時間軸、求職者個資外洩風險的盤點範圍、簽章驗證的技術機制（Token/Signature 驗簽時機）、全國客服溝通話術，以及上線後監控異常登入的指標。
4. **KOOL 從 0 到 1 商業模式探索與 8 萬次報名的漏斗設計（對應 `jd14`、`jd30`、`jd31`、`jd34`、`jd44`、`jd47`）**：
   - **追問問題**：「KOOL 在尚凡從 0 到 1 探索雙邊媒合商業模式時，初期如何解決雙邊市場的冷啟動問題（先有公司合作案還是先有 1.6 萬份網紅檔案）？為何設定『檔案完成、社群認證及照片門檻』才開放精選網紅資格？VIP 訂閱與點數付費牆的轉換表現如何？」
   - **建議準備的事實**：準備 KOOL 冷啟動階段的供給端與需求端獲取順序、門檻設計前後對媒合品質或回覆率的影響，以及當時追蹤的核心北極星指標與付費轉換觀察。
5. **入職初期完整 Scrum 與現行 Kanban 搭配瀑布式開發的轉換脈絡（對應 `jd11`、`jd20`、`jd31`、`jd34`、`jd40`）**：
   - **追問問題**：「你在入職初期跑過一週一個 Sprint 的完整 Scrum（含 Daily stand-up、Review 與 Retro），後來為何改為 Kanban 搭配瀑布式開發，並在 2026 重新導入 Daily stand-up？在對接 10 個需求單位、把處理週期從 100.4 天降到 30.9 天的過程中，這兩種流程各自解決了什麼問題？」
   - **建議準備的事實**：準備兩種開發模式在團隊組織、需求變動頻率與系統改版階段上的適用差異，以及你如何透過每週處理週報、內部 ticket 系統與重啟 Daily stand-up 將平均處理週期壓低近 70%。

## 6. ATS 準備檢查（五塊，不加總）

> **說明**：已針對上傳之實體 PDF 檔案 **`resume-v10-twocol.pdf`**（833,292 bytes，2 頁，Producer: `Skia/PDF m141` / `HeadlessChrome/141.0.0.0`）執行本機擷取實測（`pypdf`、`pdfplumber`、`pdftotext`、`pdftotext -layout`；`test_level: local_extraction_only`、`actual_ats_import_performed: false`）。依 **ATS02（接受檔案與解析分開）** 與 **硬性規則 1**，PDF 解析瑕疵與人類內容評分（Level 7–9）嚴格分開列示、不扣減內容維度評等，但本機抽字實測檢出 **2 項會直接破壞 ATS 自動解析的嚴重技術問題（`tests.pdf_extraction: fail`）**：

| 檢查區塊 | 狀態 | 檢查依據與 `resume-v10-twocol.pdf` 本機實測結果（ATS01–ATS14） |
| :-- | :-: | :-- |
| 1. 檔案接受 (File Acceptance) | `pass`（本機檔案）／`not_tested`（真實平台） | **ATS01/02/13**：本機檢查 `resume-v10-twocol.pdf` 為標準未加密 PDF（`is_encrypted: False`，檔案大小約 814 KB，共 2 頁），符合常見上傳格式與大小限制；惟未向 104 或企業內部 ATS（Greenhouse/Ashby/Workable）執行真實投遞匯入（`actual_ats_import_performed: false`）。 |
| 2. 欄位解析 (Field Parsing) | **`fail`**（本機抽字實測失敗） | **ATS03/04/12**：本機以 3 套工具實測檢出兩大解析失敗：<br>① **粗體字雙層重疊（Fake-Bold / Type3 重複繪製）**：因 Linux `HeadlessChrome` 使用無獨立粗體字重檔之 `WenQuanYiZenHei` 進行合成粗體，產生 70+ 個 `/Type3` 字型並將所有粗體字寫入 PDF 文字流兩次——在 `pypdf` 抽字中，姓名、Email、電話與職稱整串黏合重複（`聶崑淮聶崑淮`、`kunhuainie@gmail.comkunhuainie@gmail.com`、`09788028710978802871`），導致 Email 網域被誤判為 `.comkunhuainie`、電話變 20 碼；在 `pdfplumber` 與 OCR 文字層中則逐字重疊（`kkuunnhhuuaaiinniiee@@ggmmaaiill..ccoomm`、`00997788880022887711`、`PPrroodduucctt OOwwnneerr／／PPMM`、`11111111 全全球球華華人人`），聯絡資訊與職稱自動填入必敗。<br>② **第 1 頁雙欄排版造成讀序交錯與「尚凡經歷」跨頁斷裂**：在 `pdfplumber` 與 `pdftotext -layout` 中，第 1 頁左欄（摘要／1111 經歷）與右欄（技能／學歷／求職條件）同高度文字被橫向拼成同一行（如 `涵蓋訂閱制交友 App、網紅媒合 App 及人力銀 產產品品文文件件`）；在 `pypdf` 與 `pdftotext` 預設模式中，第 1 頁左欄底部先讀完 `Product Manager｜尚凡國際創新科技｜2018/01 - 2022/03` 標題與導言後，**中間被插入整欄右欄（專業技能 → 學歷 → 求職條件）**，直到第 2 頁才出現尚凡的 4 條核心實績（定價實驗、Peach、KOOL 0 到 1、Juicy），導致時間軸解析器將尚凡的 4 條成果誤歸入「求職條件」或「學歷」之下。 |
| 3. 搜尋可見性 (Search Visibility) | **`warning`**（內文關鍵字 `pass`，粗體職稱／公司名在部分解析器受損） | **ATS05/06**：一般內文（非粗體）之關鍵字（如 `Product Owner`、`PRD`、`Use Case`、`Wireframe`、`Scrum`、`Sprint`、`Kanban`、`GA4`、`Claude Code`、`AWS`、`TOEIC 980`）在文字流中正常可檢索；但所有設為**粗體**的職稱與公司名在 `pdfplumber`/`pdfminer` 系解析器中變成疊字（如 `SSeenniioorr PPrroodduucctt MMaannaaggeerr`、`AAssssoocciiaattee PPMM`、`尚尚凡凡國國際際創創新新科科技技`、`CCaalliiffoorrnniiaa SSttaattee UUnniivveerrssiittyy`），在依賴 `pdfminer` 的檢索系統中無法命中這些粗體詞彙。 |
| 4. 資格與流程條件 (Qualifications & Workflow) | `unknown` | **ATS07/08/10/11**：無外部平台申請表問答欄位與平台中繼資料（標 `unknown`）；履歷內載明之求職條件（雙北、可接受遠端或混合辦公、錄取後三週可上班）與 15 份職缺均無已知衝突。 |
| 5. 匹配功能與未知設定 (Matching & Unknown Config) | `unknown` | **ATS09/14**：雇主後台是否啟用 AI 排序與權重設定未知（標 `unknown`），不合成通用 ATS 分數；但若雇主啟用自動欄位擷取，第 2 塊之粗體疊字與雙欄斷裂將嚴重影響結構化欄位品質。 |

## 7. 方法限制、執行模式 V（截斷與亂序可見性測試）與修復建議
- `model_id`、是否每次都是新 context、實際跑了幾次：
  - `model_id`: `gemini-4-argon`（Gemini 4 Argon）。
  - 實際執行次數：完成 **單份審查 A 共 15 次**（15 份職缺各 1 次）＋ **`resume-v10-twocol.pdf` 本機多工具抽字與 ATS 準備檢查 1 次**＋ **執行模式 V（`V-raw-extract`、`V-1page`、`V-300`）可見性壓力測試 1 次**＋ **跨職缺彙整報告 1 次**。本次依指示**不做任何版本比較**，亦未引用任何其他對話或舊版評分。
  - 是否每次都是新 context（限制誠實揭露）：受限於單一代理執行環境，無法開啟 15 個物理隔離的全新對話視窗；本報告於同一執行環境中透過程式化結構隔離逐一針對每份職缺的明文條件獨立取證判讀（嚴格遵守硬性規則 1、2、4、5，不拿 A 職缺條件扣 B 職缺分），但依 §0 規定誠實揭露「非 15 個獨立對話視窗執行」。
- **執行模式 V：截斷文字與原始抽字的可見性測試（依 §7 預先聲明三項固定規則對照）**：
  1. **`V-raw-extract`（無座標修正原始輸出：`pypdf` / `pdftotext` / `pdfplumber`）**：
     - **實測結果**：出現「粗體字雙重疊字」與「第 1 頁雙欄讀序穿插」。特別是 `尚凡國際創新科技（2018/01 - 2022/03）` 的標題位於第 1 頁左欄底部，而其 4 條核心成果 bullet（定價實驗、Peach 金流、KOOL 0 到 1、Juicy）位於第 2 頁頂部，中間被第 1 頁右欄的 `專業技能 → 學歷 → 求職條件` 完全隔開。若招募系統僅以無座標修正之段落流解析，候選人在尚凡的 4 年成果會與尚凡職稱脫鉤。
  2. **`V-1page`（只保留第一頁擷取出的文字）**：
     - **實測結果**：由於第 1 頁右欄佔用約 35% 寬度放置技能與學歷，左欄僅容納「專業摘要、1111 經歷、尚凡標題與導言」。若審查者或預覽系統只看第 1 頁，**以下關鍵證據在第 1 頁出現次數為 0（完全不可見）**：
       - `KOOL 從 0 到 1 探索商業模式`、`1.6 萬份網紅檔案`、`半年累計 8 萬多次報名`（直接影響要求 0 到 1 完整經歷之 `jd30`、`jd31`、`jd34`、`jd44`、`jd47`）。
       - 馬來西亞三階段定價實驗之完整對照數據（`21 天`、`iOS 增 5%、Android 減 18%、相對多 28%`，影響 `jd14`、`jd44`）。
       - `CodaPay 新加坡技術團隊協調串接` 與 `印尼、泰國電信帳單與超商付款`（第 1 頁僅右欄出現名詞 `CodaPay 實收試算`，影響 `jd03`、`jd26`、`jd36`）。
       - `SweetRing 7 個市場在地化` 與 `以英文分派 UI/UX 翻譯`（影響 `jd20`、`jd43`、`jd44`）。
  3. **`V-300`（只保留純文字前 300 字）**：
     - **實測結果**：因開頭姓名、職稱、Email、電話與標題全部雙重重複，平白消耗約 130 字元；在 `pypdf` 前 300 字僅讀到 `2023/12–2026/03 主責約 5` 即被截斷（連「50 項大項功能」、「Peach 24%→80%」、「Scrum/Kanban」、「AI Agent」皆未進入前 300 字）；在 `pdfplumber` 前 300 字更因雙欄同行合併而混入右欄 `產產品品文文件件`。
- **給候選人的 PDF 匯出技術修復建議（不改動任何履歷文字內容即可 100% 修復）**：
  1. **消除粗體疊字（修復 `kkuunnhhuuaaiinniiee` 與 `聶崑淮聶崑淮`）**：產生此 PDF 的環境為 Linux `HeadlessChrome`，所用的 `WenQuanYi Zen Hei（文泉驛正黑）` 只有 Regular 單一字重，當 CSS 設定 `font-weight: bold / 600 / 700` 時，Chromium Skia 會以「偏移重繪兩次（Synthetic Bold）」模擬粗體並產生 `/Type3` 字型。請在生成 PDF 的環境改用具備原生多字重（Regular + Bold）之字型（如 **`Noto Sans CJK TC` / `Source Han Sans TC`**），或在 CSS 中對無原生粗體的字型關閉合成粗體（`font-synthesis: none;`）。
  2. **避免跨欄／跨頁切斷「尚凡國際」經歷**：若維持雙欄排版，建議將「尚凡國際創新科技」整段標題與導言移至第 2 頁頂部（不在第 1 頁左欄底部只留標題而把 bullet 放到第 2 頁），或改回單欄排版，即可徹底消除右欄（技能／學歷）插斷尚凡經歷的讀序問題。
- 未做：真實 ATS 匯入、真人校準：
  - 真實 ATS 匯入：`not_run`（`actual_ats_import_performed: false`）。
  - 真人校準：`not_run`（`human_calibration: not_run`）。
- 技術失敗或格式修補（保留原始輸出，不改判定）：
  - 無審查 `technical_failure`；15 份單行 JSON 全數通過欄位完整性、`human_calibrated=false`、`ai_authorship.probability=null`、`tests.pdf_extraction="fail"` 與字數上限程式檢核。

# 附錄 A：15 份單份審查完整輸出（單行 JSON ＋ §6.2 評語格式）

## 單份審查｜履歷 Resume_AppendixA（jd03 產品經理 (Pi錢包)｜拍付國際）｜第 1 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_AppendixA","job_id":"jd03","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd03-01","human_calibrated":false,"requirements":[{"id":"R01","text":"2年以上獨立PM經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"獨立負責多款產品規劃與交付"},{"id":"R02","text":"能撰寫PRD/User Story/Wireframe","type":"required","status":"supported","evidence":["以 Use Case、Wireframe 定義業務流程"],"blocks_interview":false,"reason":"完整具備PRD與原型實作案例"},{"id":"R03","text":"理解API串接與系統運作邏輯","type":"required","status":"supported","evidence":["與 CodaPay 新加坡技術團隊協調串接"],"blocks_interview":false,"reason":"具跨國第三方金流API串接經驗"},{"id":"R04","text":"金融科技/支付/點數/电子票證/電商經驗","type":"preferred","status":"supported","evidence":["規劃 VIP 訂閱、點數付費牆與精選置頂曝光"],"blocks_interview":false,"reason":"具網頁付款、點數牆與超商帳單支付經驗"},{"id":"R05","text":"政府機關或銀行產品串接經驗","type":"preferred","status":"unknown","evidence":["未呈現銀行或政府機關直接串接紀錄"],"blocks_interview":false,"reason":"僅列第三方金流CodaPay串接"},{"id":"R06","text":"會員經營/用戶留存與數據觀測分析經驗","type":"preferred","status":"supported","evidence":["144 天後仍付費 91.4%，同期其餘廠商 89.2%"],"blocks_interview":false,"reason":"具付費廠商留存追蹤與定價實驗分析"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["全站約有 6.6 萬家活躍付費廠商（2026/04/30）"],"missing":["近4年主責B2B招募系統，非高頻錢包支付核心"],"issue_ids":["I02"]},{"id":"role_evidence","rating":"強","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"missing":["未呈現銀行或政府機關系統直接串接紀錄"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"需求平均處理週期由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"截至 09/29，完成 1,726／1,857 張需求與問題單","kinds":["output"]},{"quote":"973 家活躍付費廠商，144 天後仍付費 91.4%","kinds":["context","outcome"]},{"quote":"網紅檔案約 1.6 萬份，半年累計 8 萬多次報名","kinds":["outcome"]},{"quote":"廠商也能自行切換排序（已上線）","kinds":["decision","output"]},{"quote":"信件與即時通整合、搜尋改版（兩案皆開發中）","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"符合 jd03 核心PM年資與交付要求"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責6.6萬家廠商招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"application_note":"清楚界定個人規劃與DBA/工程分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"application_note":"交付週期、留存與媒合規模具明確基準"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與首登引導取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從思維特助理PM、尚凡PM到1111企劃主任"],"application_note":"職涯由C端0到1演進至B2B大型平台"},{"rule_id":"HR07","status":"supported","resume_evidence":["入職初期跑過完整 Scrum；把衝突邏輯轉工程條件"],"application_note":"Scrum、原型、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"application_note":"結構分明，重點指標與限制條件易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["144 天後仍付費 91.4%，同期其餘廠商 89.2%"],"application_note":"主動標註觀察差異非因果，口徑可信"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd03 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["雙北，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["主責約 50 項大項功能規劃，掌握驗收與交付"],"application_note":"證據鏈完整支持安排 jd03 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["Peach 網頁付款占營收由 24% 至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"supported","resume_evidence":["973 家活躍付費廠商，144 天後仍付費 91.4%"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["求才端可存取大量求職者個資，冒用即有外洩風險"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["把衝突的搜尋邏輯轉成工程條件；設每日配對上限"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能上線，另上線 111 項細項"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["摘要與經歷清楚交代0到1、144天留存基準與非因果"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["改依職缺上線日排序；廠商也能自行切換排序（已上線）"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、50項B2B交付、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"過去串接 CodaPay 與規劃 Peach 網頁付款時，如何處理交易異常、掉單重試與對帳流程？若改對接銀行端或政府機關，你預期技術與法遵流程有哪些差異？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd03 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定取數需求（資料表／欄位）交 DBA 撈取","reason":"未呈現銀行或政府機關產品直接串接經驗（過往金流為第三方聚合支付 CodaPay 與網頁付款）","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄"},{"id":"I02","rule_id":"HM07","source_ids":[],"application_note":"開發中專案尚無上線後成效數據","context_limit":"1111 全球華人經歷第 5 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"信件與即時通整合、搜尋結果頁改版（兩案皆開發中）","reason":"兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9","suggestion":"面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗，經手 6 款產品","主責約 50 項大項功能規劃，掌握驗收與交付"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd03","具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗","已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績"],"key_gaps":["未呈現銀行或政府機關產品直接串接經驗（過往金流為第三方聚合支付 CodaPay 與網頁付款）","資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢","「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字"],"strengths":["1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd03 證明大型系統高密度交付與排程控管力","尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd03 展現完整 0 到 1 商業探索與雙邊媒合成果","1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd03 展現問題拆解、競品反推與嚴謹實驗能力"],"interview_questions":["過去串接 CodaPay 與規劃 Peach 網頁付款時，如何處理交易異常、掉單重試與對帳流程？若改對接銀行端或政府機關，你預期技術與法遵流程有哪些差異？","在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？","「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例"],"spectrum":{"level":7,"uncertainty_levels":1,"basis":"針對 jd03 具備多個已實現案例、清楚取捨與嚴謹衡量支持面試，惟部分工具字面條件或次領域經驗待面試補驗"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"fail","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：7（±1）
- 一句話理由：「Peach 網頁付款占營收由 24% 至 80% 以上」且具 CodaPay 串接經驗，支持約談。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 全站約有 6.6 萬家活躍付費廠商（2026/04/30） | 近4年主責B2B招募系統，非高頻錢包支付核心 |
| role_evidence | 強 | 近 10 年 PM 經驗，經手 6 款產品 | 未呈現銀行或政府機關系統直接串接紀錄 |
| decision_depth | 強 | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 需求平均處理週期由 100.4 天降至 30.9 天 | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 2年以上獨立PM經驗 | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 獨立負責多款產品規劃與交付 |
| R02 能撰寫PRD/User Story/Wireframe | 必要 | supported | 以 Use Case、Wireframe 定義業務流程 | 完整具備PRD與原型實作案例 |
| R03 理解API串接與系統運作邏輯 | 必要 | supported | 與 CodaPay 新加坡技術團隊協調串接 | 具跨國第三方金流API串接經驗 |
| R04 金融科技/支付/點數/电子票證/電商經驗 | 加分 | supported | 規劃 VIP 訂閱、點數付費牆與精選置頂曝光 | 具網頁付款、點數牆與超商帳單支付經驗 |
| R05 政府機關或銀行產品串接經驗 | 加分 | unknown | 未呈現銀行或政府機關直接串接紀錄 | 僅列第三方金流CodaPay串接 |
| R06 會員經營/用戶留存與數據觀測分析經驗 | 加分 | supported | 144 天後仍付費 91.4%，同期其餘廠商 89.2% | 具付費廠商留存追蹤與定價實驗分析 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 符合 jd03 核心PM年資與交付要求 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責6.6萬家廠商招募系統 |
| HR03 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃與DBA/工程分工 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 交付週期、留存與媒合規模具明確基準 |
| HR05 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HR06 | supported | 從思維特助理PM、尚凡PM到1111企劃主任 | 職涯由C端0到1演進至B2B大型平台 |
| HR07 | supported | 入職初期跑過完整 Scrum；把衝突邏輯轉工程條件 | Scrum、原型、AI與英文協作皆有實例 |
| HR08 | supported | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 結構分明，重點指標與限制條件易讀 |
| HR09 | supported | 144 天後仍付費 91.4%，同期其餘廠商 89.2% | 主動標註觀察差異非因果，口徑可信 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd03 職責相容 |
| HR11 | supported | 雙北，可接受遠端或混合辦公｜錄取後三週可上班 | 地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 主責約 50 項大項功能規劃，掌握驗收與交付 | 證據鏈完整支持安排 jd03 面試 |
| HM01 | supported | KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO | 兼具0到1雙邊媒合與B2B企業系統經驗 |
| HM02 | supported | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 從客服訊號查明配對排序根因並實測競品 |
| HM03 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HM04 | supported | Peach 網頁付款占營收由 24% 至 80% 以上 | 具定價實驗、付費牆與網頁金流轉換實績 |
| HM05 | supported | 973 家活躍付費廠商，144 天後仍付費 91.4% | 交代期間、分母占比與非因果觀察限制 |
| HM06 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃、DBA取數與工程協作 |
| HM07 | supported | 求才端可存取大量求職者個資，冒用即有外洩風險 | 具重複信箱處理、離峰切換與防冒用閉環 |
| HM08 | supported | 把衝突的搜尋邏輯轉成工程條件；設每日配對上限 | 能將衝突邏輯轉工程條件，SQL由DBA代撈 |
| HM09 | supported | 約 50 項大項功能上線，另上線 111 項細項 | 主責50大項功能與6.6萬廠商系統，範圍相符 |
| HM10 | supported | 摘要與經歷清楚交代0到1、144天留存基準與非因果 | 摘要與條列經歷層次分明易檢索 |
| HM11 | supported | 改依職缺上線日排序；廠商也能自行切換排序（已上線） | 依客服回饋與還原原價結果修正產品規則 |
| HM12 | supported | 具KOOL 0到1、50項B2B交付、定價實驗與AI案例 | 具多個已上線案例，可於面試追問遷移細節 |
| HM13 | supported | 僅依 jd03 明文條件獨立取證判讀 | 僅依 jd03 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd03 |
| 2 | 具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗 |
| 3 | 已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 未呈現銀行或政府機關產品直接串接經驗（過往金流為第三方聚合支付 CodaPay 與網頁付款） | 過去串接 CodaPay 與規劃 Peach 網頁付款時，如何處理交易異常、掉單重試與對帳流程？若改對接銀行端或政府機關，你預期技術與法遵流程有哪些差異？ |
| 2 | 資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢 | 在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？ |
| 3 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd03 證明大型系統高密度交付與排程控管力
- 尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd03 展現完整 0 到 1 商業探索與雙邊媒合成果
- 1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd03 展現問題拆解、競品反推與嚴謹實驗能力

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定取數需求（資料表／欄位）交 DBA 撈取
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：未呈現銀行或政府機關產品直接串接經驗（過往金流為第三方聚合支付 CodaPay 與網頁付款）
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄
- 位置：1111 全球華人經歷第 5 點
  - 原句：信件與即時通整合、搜尋結果頁改版（兩案皆開發中）
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9
  - 建議方向：面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：fail（本機實測 `resume-v10-twocol.pdf` 檢出粗體雙重疊字與雙欄讀序斷裂） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 Resume_AppendixA（jd09 產品經理 Product Manager｜微拓科技 (beBit TECH)）｜第 2 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_AppendixA","job_id":"jd09","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd09-02","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上軟體產品或專案管理經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"年資與軟體產品交付量充足"},{"id":"R02","text":"B2B SaaS經驗尤佳","type":"preferred","status":"supported","evidence":["全站約有 6.6 萬家活躍付費廠商"],"blocks_interview":false,"reason":"近4年主責大型B2B企業端招募系統"},{"id":"R03","text":"熟悉UI/UX概念方法論","type":"required","status":"supported","evidence":["從 User Story、Wireframe 到 Figma／Axure"],"blocks_interview":false,"reason":"具旅程地圖、原型設計與競品實測經驗"},{"id":"R04","text":"批判性思維與問題拆解","type":"required","status":"supported","evidence":["查出根因是名單依履歷修改日排序"],"blocks_interview":false,"reason":"查明配對少又舊根因並反推競品改規則上線"},{"id":"R05","text":"數據驅動思維","type":"required","status":"supported","evidence":["GA4、世代分析、對照組實驗；擬定取數需求"],"blocks_interview":false,"reason":"具三階段定價實驗與名冊快照留存比對"},{"id":"R06","text":"獨立作業善跨部門溝通","type":"required","status":"supported","evidence":["對接工程、行銷、業務（客服）等 10 個需求單位"],"blocks_interview":false,"reason":"獨立統籌50大項功能並跨10單位協作"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["全站約有 6.6 萬家活躍付費廠商（2026/04/30）"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"足夠","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"missing":["未直接經手 MarTech（CDP+MA+BI）行銷自動化領域產品"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"需求平均處理週期由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"截至 09/29，完成 1,726／1,857 張需求與問題單","kinds":["output"]},{"quote":"973 家活躍付費廠商，144 天後仍付費 91.4%","kinds":["context","outcome"]},{"quote":"網紅檔案約 1.6 萬份，半年累計 8 萬多次報名","kinds":["outcome"]},{"quote":"廠商也能自行切換排序（已上線）","kinds":["decision","output"]},{"quote":"信件與即時通整合、搜尋改版（兩案皆開發中）","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"符合 jd09 核心PM年資與交付要求"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責6.6萬家廠商招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"application_note":"清楚界定個人規劃與DBA/工程分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"application_note":"交付週期、留存與媒合規模具明確基準"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與首登引導取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從思維特助理PM、尚凡PM到1111企劃主任"],"application_note":"職涯由C端0到1演進至B2B大型平台"},{"rule_id":"HR07","status":"supported","resume_evidence":["入職初期跑過完整 Scrum；把衝突邏輯轉工程條件"],"application_note":"Scrum、原型、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"application_note":"結構分明，重點指標與限制條件易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["144 天後仍付費 91.4%，同期其餘廠商 89.2%"],"application_note":"主動標註觀察差異非因果，口徑可信"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd09 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["雙北，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["主責約 50 項大項功能規劃，掌握驗收與交付"],"application_note":"證據鏈完整支持安排 jd09 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["Peach 網頁付款占營收由 24% 至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"supported","resume_evidence":["973 家活躍付費廠商，144 天後仍付費 91.4%"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["求才端可存取大量求職者個資，冒用即有外洩風險"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["把衝突的搜尋邏輯轉成工程條件；設每日配對上限"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能上線，另上線 111 項細項"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["摘要與經歷清楚交代0到1、144天留存基準與非因果"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["改依職缺上線日排序；廠商也能自行切換排序（已上線）"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、50項B2B交付、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"你在 1111 規劃企業端「群組功能」與「推薦人才配對規則」時，如何設計分群標籤與觸發條件？這套邏輯如何遷移至 CDP+MA 行銷自動化場景？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd09 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定取數需求（資料表／欄位）交 DBA 撈取","reason":"B2B 經驗集中於人力銀行企業招募系統，尚未直接經手 MarTech（CDP 客戶數據平台與行銷自動化）產品","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄"},{"id":"I02","rule_id":"HM07","source_ids":[],"application_note":"開發中專案尚無上線後成效數據","context_limit":"1111 全球華人經歷第 5 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"信件與即時通整合、搜尋結果頁改版（兩案皆開發中）","reason":"兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9","suggestion":"面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗，經手 6 款產品","主責約 50 項大項功能規劃，掌握驗收與交付"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd09","具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗","已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績"],"key_gaps":["B2B 經驗集中於人力銀行企業招募系統，尚未直接經手 MarTech（CDP 客戶數據平台與行銷自動化）產品","資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢","「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字"],"strengths":["1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd09 證明大型系統高密度交付與排程控管力","尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd09 展現完整 0 到 1 商業探索與雙邊媒合成果","1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd09 展現問題拆解、競品反推與嚴謹實驗能力"],"interview_questions":["你在 1111 規劃企業端「群組功能」與「推薦人才配對規則」時，如何設計分群標籤與觸發條件？這套邏輯如何遷移至 CDP+MA 行銷自動化場景？","在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？","「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd09 具備多個已實現案例、清楚取捨與嚴謹衡量支持面試，惟部分工具字面條件或次領域經驗待面試補驗"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"fail","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「主責約 50 項大項功能規劃」且具 B2B 平台問題拆解與留存分析實績，支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 全站約有 6.6 萬家活躍付費廠商（2026/04/30） | 無關鍵缺口，可於面試深化 |
| role_evidence | 足夠 | 近 10 年 PM 經驗，經手 6 款產品 | 未直接經手 MarTech（CDP+MA+BI）行銷自動化領域產品 |
| decision_depth | 強 | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 需求平均處理週期由 100.4 天降至 30.9 天 | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 3年以上軟體產品或專案管理經驗 | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 年資與軟體產品交付量充足 |
| R02 B2B SaaS經驗尤佳 | 加分 | supported | 全站約有 6.6 萬家活躍付費廠商 | 近4年主責大型B2B企業端招募系統 |
| R03 熟悉UI/UX概念方法論 | 必要 | supported | 從 User Story、Wireframe 到 Figma／Axure | 具旅程地圖、原型設計與競品實測經驗 |
| R04 批判性思維與問題拆解 | 必要 | supported | 查出根因是名單依履歷修改日排序 | 查明配對少又舊根因並反推競品改規則上線 |
| R05 數據驅動思維 | 必要 | supported | GA4、世代分析、對照組實驗；擬定取數需求 | 具三階段定價實驗與名冊快照留存比對 |
| R06 獨立作業善跨部門溝通 | 必要 | supported | 對接工程、行銷、業務（客服）等 10 個需求單位 | 獨立統籌50大項功能並跨10單位協作 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 符合 jd09 核心PM年資與交付要求 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責6.6萬家廠商招募系統 |
| HR03 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃與DBA/工程分工 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 交付週期、留存與媒合規模具明確基準 |
| HR05 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HR06 | supported | 從思維特助理PM、尚凡PM到1111企劃主任 | 職涯由C端0到1演進至B2B大型平台 |
| HR07 | supported | 入職初期跑過完整 Scrum；把衝突邏輯轉工程條件 | Scrum、原型、AI與英文協作皆有實例 |
| HR08 | supported | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 結構分明，重點指標與限制條件易讀 |
| HR09 | supported | 144 天後仍付費 91.4%，同期其餘廠商 89.2% | 主動標註觀察差異非因果，口徑可信 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd09 職責相容 |
| HR11 | supported | 雙北，可接受遠端或混合辦公｜錄取後三週可上班 | 地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 主責約 50 項大項功能規劃，掌握驗收與交付 | 證據鏈完整支持安排 jd09 面試 |
| HM01 | supported | KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO | 兼具0到1雙邊媒合與B2B企業系統經驗 |
| HM02 | supported | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 從客服訊號查明配對排序根因並實測競品 |
| HM03 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HM04 | supported | Peach 網頁付款占營收由 24% 至 80% 以上 | 具定價實驗、付費牆與網頁金流轉換實績 |
| HM05 | supported | 973 家活躍付費廠商，144 天後仍付費 91.4% | 交代期間、分母占比與非因果觀察限制 |
| HM06 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃、DBA取數與工程協作 |
| HM07 | supported | 求才端可存取大量求職者個資，冒用即有外洩風險 | 具重複信箱處理、離峰切換與防冒用閉環 |
| HM08 | supported | 把衝突的搜尋邏輯轉成工程條件；設每日配對上限 | 能將衝突邏輯轉工程條件，SQL由DBA代撈 |
| HM09 | supported | 約 50 項大項功能上線，另上線 111 項細項 | 主責50大項功能與6.6萬廠商系統，範圍相符 |
| HM10 | supported | 摘要與經歷清楚交代0到1、144天留存基準與非因果 | 摘要與條列經歷層次分明易檢索 |
| HM11 | supported | 改依職缺上線日排序；廠商也能自行切換排序（已上線） | 依客服回饋與還原原價結果修正產品規則 |
| HM12 | supported | 具KOOL 0到1、50項B2B交付、定價實驗與AI案例 | 具多個已上線案例，可於面試追問遷移細節 |
| HM13 | supported | 僅依 jd09 明文條件獨立取證判讀 | 僅依 jd09 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd09 |
| 2 | 具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗 |
| 3 | 已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | B2B 經驗集中於人力銀行企業招募系統，尚未直接經手 MarTech（CDP 客戶數據平台與行銷自動化）產品 | 你在 1111 規劃企業端「群組功能」與「推薦人才配對規則」時，如何設計分群標籤與觸發條件？這套邏輯如何遷移至 CDP+MA 行銷自動化場景？ |
| 2 | 資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢 | 在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？ |
| 3 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd09 證明大型系統高密度交付與排程控管力
- 尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd09 展現完整 0 到 1 商業探索與雙邊媒合成果
- 1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd09 展現問題拆解、競品反推與嚴謹實驗能力

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定取數需求（資料表／欄位）交 DBA 撈取
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：B2B 經驗集中於人力銀行企業招募系統，尚未直接經手 MarTech（CDP 客戶數據平台與行銷自動化）產品
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄
- 位置：1111 全球華人經歷第 5 點
  - 原句：信件與即時通整合、搜尋結果頁改版（兩案皆開發中）
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9
  - 建議方向：面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：fail（本機實測 `resume-v10-twocol.pdf` 檢出粗體雙重疊字與雙欄讀序斷裂） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 Resume_AppendixA（jd11 【北士科】Product Manager｜沛思坦 (Pacston)）｜第 3 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_AppendixA","job_id":"jd11","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd11-03","human_calibrated":false,"requirements":[{"id":"R01","text":"5年以上PM經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"年資近10年且涵蓋B2B與B2C"},{"id":"R02","text":"熟悉敏捷開發與跨部門專案管理","type":"required","status":"supported","evidence":["入職初期跑過完整 Scrum（一週一個 Sprint）"],"blocks_interview":false,"reason":"兼具完整Scrum與Kanban跨10單位管理"},{"id":"R03","text":"優秀邏輯與溝通能力","type":"required","status":"supported","evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"blocks_interview":false,"reason":"跨部門排程與把衝突搜尋邏輯轉成工程條件"},{"id":"R04","text":"熟悉Jira、Notion等工具","type":"required","status":"partial","evidence":["Notion、Trello、公司內部專案系統（ticket追蹤）"],"blocks_interview":false,"reason":"具Notion與內部ticket系統，未點名Jira"},{"id":"R05","text":"中英文文件撰寫能力","type":"required","status":"partial","evidence":["英文 TOEIC 980；以英文分派 UI/UX 翻譯"],"blocks_interview":false,"reason":"具高分英檢與英文任務分派，缺英文PRD樣本"},{"id":"R06","text":"HR Tech/LegalTech/生成式AI產品經驗","type":"preferred","status":"supported","evidence":["AI 功能已上線公司簡介、職缺說明及推薦人才"],"blocks_interview":false,"reason":"直接具備HR招募系統與3項GenAI上線實績"},{"id":"R07","text":"LLM prompt設計或自動化內容編排經驗","type":"preferred","status":"supported","evidence":["自建 Claude Code 協作流程（12條分支、23個skill）"],"blocks_interview":false,"reason":"自建多分支Claude Code與共用skill庫"},{"id":"R08","text":"資料導向思維、AB測試與技術背景","type":"preferred","status":"supported","evidence":["定價實驗採原價、iOS 降價、還原原價三階段"],"blocks_interview":false,"reason":"具對照實驗、基本HTML/CSS、DB知識與AWS證照"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["全站約有 6.6 萬家活躍付費廠商（2026/04/30）"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"強","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"missing":["使用內部 ticket 系統與 Notion，未直接寫出 Jira 字樣；未附英文 PRD 範例"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"需求平均處理週期由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"截至 09/29，完成 1,726／1,857 張需求與問題單","kinds":["output"]},{"quote":"973 家活躍付費廠商，144 天後仍付費 91.4%","kinds":["context","outcome"]},{"quote":"網紅檔案約 1.6 萬份，半年累計 8 萬多次報名","kinds":["outcome"]},{"quote":"廠商也能自行切換排序（已上線）","kinds":["decision","output"]},{"quote":"信件與即時通整合、搜尋改版（兩案皆開發中）","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"符合 jd11 核心PM年資與交付要求"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責6.6萬家廠商招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"application_note":"清楚界定個人規劃與DBA/工程分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"application_note":"交付週期、留存與媒合規模具明確基準"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與首登引導取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從思維特助理PM、尚凡PM到1111企劃主任"],"application_note":"職涯由C端0到1演進至B2B大型平台"},{"rule_id":"HR07","status":"supported","resume_evidence":["入職初期跑過完整 Scrum；把衝突邏輯轉工程條件"],"application_note":"Scrum、原型、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"application_note":"結構分明，重點指標與限制條件易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["144 天後仍付費 91.4%，同期其餘廠商 89.2%"],"application_note":"主動標註觀察差異非因果，口徑可信"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd11 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["雙北，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["主責約 50 項大項功能規劃，掌握驗收與交付"],"application_note":"證據鏈完整支持安排 jd11 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["Peach 網頁付款占營收由 24% 至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"supported","resume_evidence":["973 家活躍付費廠商，144 天後仍付費 91.4%"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["求才端可存取大量求職者個資，冒用即有外洩風險"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["把衝突的搜尋邏輯轉成工程條件；設每日配對上限"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能上線，另上線 111 項細項"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["摘要與經歷清楚交代0到1、144天留存基準與非因果"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["改依職缺上線日排序；廠商也能自行切換排序（已上線）"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、50項B2B交付、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"在 1111 與資料科學團隊合作上線「公司簡介生成、職缺說明生成及推薦人才」3 項 AI 功能時，你如何設計驗收標準並依客服回饋迭代規則？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd11 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定取數需求（資料表／欄位）交 DBA 撈取","reason":"專案追蹤使用 Notion、Trello 與公司內部 ticket/卡片系統，未直接點名外部 Jira；英文雖達 TOEIC 980 但未明列撰寫全英文 PRD 經驗","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄"},{"id":"I02","rule_id":"HM07","source_ids":[],"application_note":"開發中專案尚無上線後成效數據","context_limit":"1111 全球華人經歷第 5 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"信件與即時通整合、搜尋結果頁改版（兩案皆開發中）","reason":"兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9","suggestion":"面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗，經手 6 款產品","主責約 50 項大項功能規劃，掌握驗收與交付"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd11","具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗","已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績"],"key_gaps":["專案追蹤使用 Notion、Trello 與公司內部 ticket/卡片系統，未直接點名外部 Jira；英文雖達 TOEIC 980 但未明列撰寫全英文 PRD 經驗","資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢","「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字"],"strengths":["1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd11 證明大型系統高密度交付與排程控管力","尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd11 展現完整 0 到 1 商業探索與雙邊媒合成果","1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd11 展現問題拆解、競品反推與嚴謹實驗能力"],"interview_questions":["在 1111 與資料科學團隊合作上線「公司簡介生成、職缺說明生成及推薦人才」3 項 AI 功能時，你如何設計驗收標準並依客服回饋迭代規則？","在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？","「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例"],"spectrum":{"level":9,"uncertainty_levels":1,"basis":"針對 jd11 具備完整已上線之B2B平台與0到1量化實績（50大項功能、週期降至30.9天、8萬次報名），關鍵量測與責任可追溯"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"fail","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：9（±1）
- 一句話理由：「擔任企業端招募系統 PO」且「AI 功能已上線公司簡介生成...推薦人才」，高度對應本職缺。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 全站約有 6.6 萬家活躍付費廠商（2026/04/30） | 無關鍵缺口，可於面試深化 |
| role_evidence | 強 | 近 10 年 PM 經驗，經手 6 款產品 | 使用內部 ticket 系統與 Notion，未直接寫出 Jira 字樣；未附英文 PRD 範例 |
| decision_depth | 強 | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 需求平均處理週期由 100.4 天降至 30.9 天 | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 5年以上PM經驗 | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 年資近10年且涵蓋B2B與B2C |
| R02 熟悉敏捷開發與跨部門專案管理 | 必要 | supported | 入職初期跑過完整 Scrum（一週一個 Sprint） | 兼具完整Scrum與Kanban跨10單位管理 |
| R03 優秀邏輯與溝通能力 | 必要 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 跨部門排程與把衝突搜尋邏輯轉成工程條件 |
| R04 熟悉Jira、Notion等工具 | 必要 | partial | Notion、Trello、公司內部專案系統（ticket追蹤） | 具Notion與內部ticket系統，未點名Jira |
| R05 中英文文件撰寫能力 | 必要 | partial | 英文 TOEIC 980；以英文分派 UI/UX 翻譯 | 具高分英檢與英文任務分派，缺英文PRD樣本 |
| R06 HR Tech/LegalTech/生成式AI產品經驗 | 加分 | supported | AI 功能已上線公司簡介、職缺說明及推薦人才 | 直接具備HR招募系統與3項GenAI上線實績 |
| R07 LLM prompt設計或自動化內容編排經驗 | 加分 | supported | 自建 Claude Code 協作流程（12條分支、23個skill） | 自建多分支Claude Code與共用skill庫 |
| R08 資料導向思維、AB測試與技術背景 | 加分 | supported | 定價實驗採原價、iOS 降價、還原原價三階段 | 具對照實驗、基本HTML/CSS、DB知識與AWS證照 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 符合 jd11 核心PM年資與交付要求 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責6.6萬家廠商招募系統 |
| HR03 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃與DBA/工程分工 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 交付週期、留存與媒合規模具明確基準 |
| HR05 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HR06 | supported | 從思維特助理PM、尚凡PM到1111企劃主任 | 職涯由C端0到1演進至B2B大型平台 |
| HR07 | supported | 入職初期跑過完整 Scrum；把衝突邏輯轉工程條件 | Scrum、原型、AI與英文協作皆有實例 |
| HR08 | supported | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 結構分明，重點指標與限制條件易讀 |
| HR09 | supported | 144 天後仍付費 91.4%，同期其餘廠商 89.2% | 主動標註觀察差異非因果，口徑可信 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd11 職責相容 |
| HR11 | supported | 雙北，可接受遠端或混合辦公｜錄取後三週可上班 | 地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 主責約 50 項大項功能規劃，掌握驗收與交付 | 證據鏈完整支持安排 jd11 面試 |
| HM01 | supported | KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO | 兼具0到1雙邊媒合與B2B企業系統經驗 |
| HM02 | supported | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 從客服訊號查明配對排序根因並實測競品 |
| HM03 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HM04 | supported | Peach 網頁付款占營收由 24% 至 80% 以上 | 具定價實驗、付費牆與網頁金流轉換實績 |
| HM05 | supported | 973 家活躍付費廠商，144 天後仍付費 91.4% | 交代期間、分母占比與非因果觀察限制 |
| HM06 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃、DBA取數與工程協作 |
| HM07 | supported | 求才端可存取大量求職者個資，冒用即有外洩風險 | 具重複信箱處理、離峰切換與防冒用閉環 |
| HM08 | supported | 把衝突的搜尋邏輯轉成工程條件；設每日配對上限 | 能將衝突邏輯轉工程條件，SQL由DBA代撈 |
| HM09 | supported | 約 50 項大項功能上線，另上線 111 項細項 | 主責50大項功能與6.6萬廠商系統，範圍相符 |
| HM10 | supported | 摘要與經歷清楚交代0到1、144天留存基準與非因果 | 摘要與條列經歷層次分明易檢索 |
| HM11 | supported | 改依職缺上線日排序；廠商也能自行切換排序（已上線） | 依客服回饋與還原原價結果修正產品規則 |
| HM12 | supported | 具KOOL 0到1、50項B2B交付、定價實驗與AI案例 | 具多個已上線案例，可於面試追問遷移細節 |
| HM13 | supported | 僅依 jd11 明文條件獨立取證判讀 | 僅依 jd11 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd11 |
| 2 | 具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗 |
| 3 | 已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 專案追蹤使用 Notion、Trello 與公司內部 ticket/卡片系統，未直接點名外部 Jira；英文雖達 TOEIC 980 但未明列撰寫全英文 PRD 經驗 | 在 1111 與資料科學團隊合作上線「公司簡介生成、職缺說明生成及推薦人才」3 項 AI 功能時，你如何設計驗收標準並依客服回饋迭代規則？ |
| 2 | 資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢 | 在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？ |
| 3 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd11 證明大型系統高密度交付與排程控管力
- 尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd11 展現完整 0 到 1 商業探索與雙邊媒合成果
- 1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd11 展現問題拆解、競品反推與嚴謹實驗能力

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定取數需求（資料表／欄位）交 DBA 撈取
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：專案追蹤使用 Notion、Trello 與公司內部 ticket/卡片系統，未直接點名外部 Jira；英文雖達 TOEIC 980 但未明列撰寫全英文 PRD 經驗
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄
- 位置：1111 全球華人經歷第 5 點
  - 原句：信件與即時通整合、搜尋結果頁改版（兩案皆開發中）
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9
  - 建議方向：面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：強

### 8. 未測試聲明
PDF 抽字：fail（本機實測 `resume-v10-twocol.pdf` 檢出粗體雙重疊字與雙欄讀序斷裂） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 Resume_AppendixA（jd14 D441 MyVideo影音產品Growth PM｜台灣大哥大）｜第 4 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_AppendixA","job_id":"jd14","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd14-04","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上Growth PM經驗（全生命週期漏斗）","type":"required","status":"supported","evidence":["網紅檔案約 1.6 萬份，半年累計 8 萬多次報名"],"blocks_interview":false,"reason":"具KOOL雙邊獲取活化、定價實驗與留存經驗"},{"id":"R02","text":"能獨立撰寫PRD/User Flow/Wireframe","type":"required","status":"supported","evidence":["以 Use Case、Wireframe 定義業務流程與畫面"],"blocks_interview":false,"reason":"完整具備流程圖、Wireframe與PRD實績"},{"id":"R03","text":"熟悉GA4、Firebase","type":"required","status":"partial","evidence":["使用者訪談與問卷、競品實測、GA4、世代分析"],"blocks_interview":false,"reason":"明列GA4與世代分析，未呈現Firebase"},{"id":"R04","text":"訂閱與會員轉換優化、A/B Test產品實驗","type":"required","status":"supported","evidence":["Peach 網頁付款占營收由 24% 至 80% 以上"],"blocks_interview":false,"reason":"具VIP訂閱、點數牆、網頁金流與三階段定價實驗"},{"id":"R05","text":"跨部門溝通能力","type":"required","status":"supported","evidence":["對接工程、行銷、業務（客服）等 10 個需求單位"],"blocks_interview":false,"reason":"跨工程、設計、行銷與金流團隊推進交付"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["全站約有 6.6 萬家活躍付費廠商（2026/04/30）"],"missing":["近4年重心為B2B企業招募系統，C端訂閱成長案例集中於2018–2022年"],"issue_ids":["I02"]},{"id":"role_evidence","rating":"足夠","evidence":["網紅檔案約 1.6 萬份，半年累計 8 萬多次報名"],"missing":["未呈現 Firebase 操作經驗與 OTT 影音串流產業經驗"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"需求平均處理週期由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"截至 09/29，完成 1,726／1,857 張需求與問題單","kinds":["output"]},{"quote":"973 家活躍付費廠商，144 天後仍付費 91.4%","kinds":["context","outcome"]},{"quote":"網紅檔案約 1.6 萬份，半年累計 8 萬多次報名","kinds":["outcome"]},{"quote":"廠商也能自行切換排序（已上線）","kinds":["decision","output"]},{"quote":"信件與即時通整合、搜尋改版（兩案皆開發中）","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["網紅檔案約 1.6 萬份，半年累計 8 萬多次報名"],"application_note":"符合 jd14 核心PM年資與交付要求"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責6.6萬家廠商招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"application_note":"清楚界定個人規劃與DBA/工程分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"application_note":"交付週期、留存與媒合規模具明確基準"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與首登引導取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從思維特助理PM、尚凡PM到1111企劃主任"],"application_note":"職涯由C端0到1演進至B2B大型平台"},{"rule_id":"HR07","status":"supported","resume_evidence":["入職初期跑過完整 Scrum；把衝突邏輯轉工程條件"],"application_note":"Scrum、原型、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"application_note":"結構分明，重點指標與限制條件易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["144 天後仍付費 91.4%，同期其餘廠商 89.2%"],"application_note":"主動標註觀察差異非因果，口徑可信"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd14 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["雙北，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["主責約 50 項大項功能規劃，掌握驗收與交付"],"application_note":"證據鏈完整支持安排 jd14 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["Peach 網頁付款占營收由 24% 至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"supported","resume_evidence":["973 家活躍付費廠商，144 天後仍付費 91.4%"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["求才端可存取大量求職者個資，冒用即有外洩風險"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["把衝突的搜尋邏輯轉成工程條件；設每日配對上限"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能上線，另上線 111 項細項"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["摘要與經歷清楚交代0到1、144天留存基準與非因果"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["改依職缺上線日排序；廠商也能自行切換排序（已上線）"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、50項B2B交付、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"在 KOOL 累積 1.6 萬份網紅檔案與半年 8 萬多次報名的過程中，你如何追蹤 Acquisition 到 Activation 的轉化漏斗？是否有使用 Firebase Events 的經驗？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd14 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定取數需求（資料表／欄位）交 DBA 撈取","reason":"必備條件點名之 Firebase 未呈現；且近 4 年重心為 B2B 企業系統，C 端訂閱案例為社交與網紅媒合而非 OTT 影音串流","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄"},{"id":"I02","rule_id":"HM07","source_ids":[],"application_note":"開發中專案尚無上線後成效數據","context_limit":"1111 全球華人經歷第 5 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"信件與即時通整合、搜尋結果頁改版（兩案皆開發中）","reason":"兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9","suggestion":"面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）"}],"decision":{"recommendation":"interview","evidence":["網紅檔案約 1.6 萬份，半年累計 8 萬多次報名","主責約 50 項大項功能規劃，掌握驗收與交付"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd14","具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗","已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績"],"key_gaps":["必備條件點名之 Firebase 未呈現；且近 4 年重心為 B2B 企業系統，C 端訂閱案例為社交與網紅媒合而非 OTT 影音串流","資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢","「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字"],"strengths":["1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd14 證明大型系統高密度交付與排程控管力","尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd14 展現完整 0 到 1 商業探索與雙邊媒合成果","1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd14 展現問題拆解、競品反推與嚴謹實驗能力"],"interview_questions":["在 KOOL 累積 1.6 萬份網紅檔案與半年 8 萬多次報名的過程中，你如何追蹤 Acquisition 到 Activation 的轉化漏斗？是否有使用 Firebase Events 的經驗？","在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？","「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例"],"spectrum":{"level":7,"uncertainty_levels":1,"basis":"針對 jd14 具備多個已實現案例、清楚取捨與嚴謹衡量支持面試，惟部分工具字面條件或次領域經驗待面試補驗"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"fail","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：7（±1）
- 一句話理由：「定價實驗採原價、iOS 降價、還原原價三階段」與 KOOL 雙邊媒合具成長實證，支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 全站約有 6.6 萬家活躍付費廠商（2026/04/30） | 近4年重心為B2B企業招募系統，C端訂閱成長案例集中於2018–2022年 |
| role_evidence | 足夠 | 網紅檔案約 1.6 萬份，半年累計 8 萬多次報名 | 未呈現 Firebase 操作經驗與 OTT 影音串流產業經驗 |
| decision_depth | 強 | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 需求平均處理週期由 100.4 天降至 30.9 天 | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 3年以上Growth PM經驗（全生命週期漏斗） | 必要 | supported | 網紅檔案約 1.6 萬份，半年累計 8 萬多次報名 | 具KOOL雙邊獲取活化、定價實驗與留存經驗 |
| R02 能獨立撰寫PRD/User Flow/Wireframe | 必要 | supported | 以 Use Case、Wireframe 定義業務流程與畫面 | 完整具備流程圖、Wireframe與PRD實績 |
| R03 熟悉GA4、Firebase | 必要 | partial | 使用者訪談與問卷、競品實測、GA4、世代分析 | 明列GA4與世代分析，未呈現Firebase |
| R04 訂閱與會員轉換優化、A/B Test產品實驗 | 必要 | supported | Peach 網頁付款占營收由 24% 至 80% 以上 | 具VIP訂閱、點數牆、網頁金流與三階段定價實驗 |
| R05 跨部門溝通能力 | 必要 | supported | 對接工程、行銷、業務（客服）等 10 個需求單位 | 跨工程、設計、行銷與金流團隊推進交付 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 網紅檔案約 1.6 萬份，半年累計 8 萬多次報名 | 符合 jd14 核心PM年資與交付要求 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責6.6萬家廠商招募系統 |
| HR03 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃與DBA/工程分工 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 交付週期、留存與媒合規模具明確基準 |
| HR05 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HR06 | supported | 從思維特助理PM、尚凡PM到1111企劃主任 | 職涯由C端0到1演進至B2B大型平台 |
| HR07 | supported | 入職初期跑過完整 Scrum；把衝突邏輯轉工程條件 | Scrum、原型、AI與英文協作皆有實例 |
| HR08 | supported | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 結構分明，重點指標與限制條件易讀 |
| HR09 | supported | 144 天後仍付費 91.4%，同期其餘廠商 89.2% | 主動標註觀察差異非因果，口徑可信 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd14 職責相容 |
| HR11 | supported | 雙北，可接受遠端或混合辦公｜錄取後三週可上班 | 地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 主責約 50 項大項功能規劃，掌握驗收與交付 | 證據鏈完整支持安排 jd14 面試 |
| HM01 | supported | KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO | 兼具0到1雙邊媒合與B2B企業系統經驗 |
| HM02 | supported | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 從客服訊號查明配對排序根因並實測競品 |
| HM03 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HM04 | supported | Peach 網頁付款占營收由 24% 至 80% 以上 | 具定價實驗、付費牆與網頁金流轉換實績 |
| HM05 | supported | 973 家活躍付費廠商，144 天後仍付費 91.4% | 交代期間、分母占比與非因果觀察限制 |
| HM06 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃、DBA取數與工程協作 |
| HM07 | supported | 求才端可存取大量求職者個資，冒用即有外洩風險 | 具重複信箱處理、離峰切換與防冒用閉環 |
| HM08 | supported | 把衝突的搜尋邏輯轉成工程條件；設每日配對上限 | 能將衝突邏輯轉工程條件，SQL由DBA代撈 |
| HM09 | supported | 約 50 項大項功能上線，另上線 111 項細項 | 主責50大項功能與6.6萬廠商系統，範圍相符 |
| HM10 | supported | 摘要與經歷清楚交代0到1、144天留存基準與非因果 | 摘要與條列經歷層次分明易檢索 |
| HM11 | supported | 改依職缺上線日排序；廠商也能自行切換排序（已上線） | 依客服回饋與還原原價結果修正產品規則 |
| HM12 | supported | 具KOOL 0到1、50項B2B交付、定價實驗與AI案例 | 具多個已上線案例，可於面試追問遷移細節 |
| HM13 | supported | 僅依 jd14 明文條件獨立取證判讀 | 僅依 jd14 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd14 |
| 2 | 具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗 |
| 3 | 已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 必備條件點名之 Firebase 未呈現；且近 4 年重心為 B2B 企業系統，C 端訂閱案例為社交與網紅媒合而非 OTT 影音串流 | 在 KOOL 累積 1.6 萬份網紅檔案與半年 8 萬多次報名的過程中，你如何追蹤 Acquisition 到 Activation 的轉化漏斗？是否有使用 Firebase Events 的經驗？ |
| 2 | 資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢 | 在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？ |
| 3 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd14 證明大型系統高密度交付與排程控管力
- 尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd14 展現完整 0 到 1 商業探索與雙邊媒合成果
- 1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd14 展現問題拆解、競品反推與嚴謹實驗能力

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定取數需求（資料表／欄位）交 DBA 撈取
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：必備條件點名之 Firebase 未呈現；且近 4 年重心為 B2B 企業系統，C 端訂閱案例為社交與網紅媒合而非 OTT 影音串流
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄
- 位置：1111 全球華人經歷第 5 點
  - 原句：信件與即時通整合、搜尋結果頁改版（兩案皆開發中）
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9
  - 建議方向：面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：fail（本機實測 `resume-v10-twocol.pdf` 檢出粗體雙重疊字與雙欄讀序斷裂） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 Resume_AppendixA（jd20 Senior Product Manager (Anti-Scam BU/2B)｜Gogolook）｜第 5 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_AppendixA","job_id":"jd20","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd20-05","human_calibrated":false,"requirements":[{"id":"R01","text":"5-8年以上B2B/B2G產品或專案管理經驗","type":"required","status":"partial","evidence":["Product Owner／PM｜1111 全球華人｜2022/08 - 迄今"],"blocks_interview":false,"reason":"總PM近10年，惟純B2B PO年資約3年10個月"},{"id":"R02","text":"接近母語等級英語口說與書寫","type":"required","status":"partial","evidence":["英文 TOEIC 980、TOEFL iBT 93；曾赴美交換"],"blocks_interview":false,"reason":"高分英檢與英文分派任務，母語級B2B商務待驗"},{"id":"R03","text":"優異溝通與關係人管理能力","type":"required","status":"supported","evidence":["對接 10 個需求單位；直接向組織副總匯報"],"blocks_interview":false,"reason":"跨10個部門協調需求並向高層匯報"},{"id":"R04","text":"扎實PM基礎（PRD/路線圖/待辦清單/時程風險）","type":"required","status":"supported","evidence":["主責約 50 項大項功能規劃，掌握驗收與交付"],"blocks_interview":false,"reason":"主責50大項功能與111項Roadmap細項"},{"id":"R05","text":"強烈數據敏感度（能獨立使用SQL/BI/試算表）","type":"required","status":"partial","evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"blocks_interview":false,"reason":"懂資料表欄位並精熟Sheet/Excel，惟非自寫SQL"},{"id":"R06","text":"熟悉AI工具（如Claude）與Jira/Confluence串接","type":"required","status":"partial","evidence":["自建 Claude Code 協作流程（12條分支、23個skill）"],"blocks_interview":false,"reason":"Claude Code應用深入，惟未列串接Jira自動化"},{"id":"R07","text":"對防詐與風險偵測有熱情及相關產品經驗","type":"required","status":"supported","evidence":["十多家廠商帳號遭冒用...上線簽章驗證"],"blocks_interview":false,"reason":"親歷B2B帳號冒用個資風險控管並完成簽章驗證"},{"id":"R08","text":"曾服務海外企業客戶或政府機關","type":"preferred","status":"partial","evidence":["SweetRing 在地化涵蓋美、墨、巴、印、馬、日、韓7市場"],"blocks_interview":false,"reason":"具7國B2C在地化與台灣B2B，缺海外B2B客戶"},{"id":"R09","text":"具Agile/Scrum與產品定價成本利潤分析經驗","type":"preferred","status":"supported","evidence":["入職初期跑過完整 Scrum；依抽成稅費做實收試算"],"blocks_interview":false,"reason":"具完整Scrum經歷、定價實驗與跨國金流實收試算"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["全站約有 6.6 萬家活躍付費廠商（2026/04/30）"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"足夠","evidence":["Product Owner／PM｜1111 全球華人｜2022/08 - 迄今"],"missing":["資料庫取數交由 DBA 撈取而非獨立寫 SQL；海外經驗為 B2C 而非海外 B2B/B2G 客戶"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"需求平均處理週期由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"截至 09/29，完成 1,726／1,857 張需求與問題單","kinds":["output"]},{"quote":"973 家活躍付費廠商，144 天後仍付費 91.4%","kinds":["context","outcome"]},{"quote":"網紅檔案約 1.6 萬份，半年累計 8 萬多次報名","kinds":["outcome"]},{"quote":"廠商也能自行切換排序（已上線）","kinds":["decision","output"]},{"quote":"信件與即時通整合、搜尋改版（兩案皆開發中）","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["Product Owner／PM｜1111 全球華人｜2022/08 - 迄今"],"application_note":"符合 jd20 核心PM年資與交付要求"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責6.6萬家廠商招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"application_note":"清楚界定個人規劃與DBA/工程分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"application_note":"交付週期、留存與媒合規模具明確基準"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與首登引導取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從思維特助理PM、尚凡PM到1111企劃主任"],"application_note":"職涯由C端0到1演進至B2B大型平台"},{"rule_id":"HR07","status":"supported","resume_evidence":["入職初期跑過完整 Scrum；把衝突邏輯轉工程條件"],"application_note":"Scrum、原型、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"application_note":"結構分明，重點指標與限制條件易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["144 天後仍付費 91.4%，同期其餘廠商 89.2%"],"application_note":"主動標註觀察差異非因果，口徑可信"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd20 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["雙北，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["主責約 50 項大項功能規劃，掌握驗收與交付"],"application_note":"證據鏈完整支持安排 jd20 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["Peach 網頁付款占營收由 24% 至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"supported","resume_evidence":["973 家活躍付費廠商，144 天後仍付費 91.4%"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["求才端可存取大量求職者個資，冒用即有外洩風險"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"partial","resume_evidence":["把衝突的搜尋邏輯轉成工程條件；設每日配對上限"],"evidence_type":"output","source_ids":[],"interview_question":"請說明如何將衝突搜尋邏輯轉成工程條件，以及是否具基礎 SQL/JSON 實作經驗？"},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能上線，另上線 111 項細項"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["摘要與經歷清楚交代0到1、144天留存基準與非因果"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["改依職缺上線日排序；廠商也能自行切換排序（已上線）"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、50項B2B交付、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"請以英文簡述 2026/04 1111 廠商帳號遭冒用事件中，你如何評估求職者個資外洩風險、協調工程於 04/17 上線簽章驗證，以及後續如何設計主動偵測機制？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd20 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定取數需求（資料表／欄位）交 DBA 撈取","reason":"資料庫取數為「擬定資料表與欄位交 DBA 撈取」而非獨立撰寫 SQL；且海外 7 國經驗為 B2C App，尚未直接對接海外 B2B/B2G 企業客戶","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄"},{"id":"I02","rule_id":"HM07","source_ids":[],"application_note":"開發中專案尚無上線後成效數據","context_limit":"1111 全球華人經歷第 5 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"信件與即時通整合、搜尋結果頁改版（兩案皆開發中）","reason":"兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9","suggestion":"面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）"}],"decision":{"recommendation":"interview","evidence":["Product Owner／PM｜1111 全球華人｜2022/08 - 迄今","主責約 50 項大項功能規劃，掌握驗收與交付"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd20","具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗","已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績"],"key_gaps":["資料庫取數為「擬定資料表與欄位交 DBA 撈取」而非獨立撰寫 SQL；且海外 7 國經驗為 B2C App，尚未直接對接海外 B2B/B2G 企業客戶","資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢","「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字"],"strengths":["1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd20 證明大型系統高密度交付與排程控管力","尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd20 展現完整 0 到 1 商業探索與雙邊媒合成果","1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd20 展現問題拆解、競品反推與嚴謹實驗能力"],"interview_questions":["請以英文簡述 2026/04 1111 廠商帳號遭冒用事件中，你如何評估求職者個資外洩風險、協調工程於 04/17 上線簽章驗證，以及後續如何設計主動偵測機制？","在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？","「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd20 具備多個已實現案例、清楚取捨與嚴謹衡量支持面試，惟部分工具字面條件或次領域經驗待面試補驗"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"fail","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「統籌影響評估...上線簽章驗證」且具近 4 年 B2B PO 與 Claude Code 流程，支持約談。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 全站約有 6.6 萬家活躍付費廠商（2026/04/30） | 無關鍵缺口，可於面試深化 |
| role_evidence | 足夠 | Product Owner／PM｜1111 全球華人｜2022/08 - 迄今 | 資料庫取數交由 DBA 撈取而非獨立寫 SQL；海外經驗為 B2C 而非海外 B2B/B2G 客戶 |
| decision_depth | 強 | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 需求平均處理週期由 100.4 天降至 30.9 天 | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 5-8年以上B2B/B2G產品或專案管理經驗 | 必要 | partial | Product Owner／PM｜1111 全球華人｜2022/08 - 迄今 | 總PM近10年，惟純B2B PO年資約3年10個月 |
| R02 接近母語等級英語口說與書寫 | 必要 | partial | 英文 TOEIC 980、TOEFL iBT 93；曾赴美交換 | 高分英檢與英文分派任務，母語級B2B商務待驗 |
| R03 優異溝通與關係人管理能力 | 必要 | supported | 對接 10 個需求單位；直接向組織副總匯報 | 跨10個部門協調需求並向高層匯報 |
| R04 扎實PM基礎（PRD/路線圖/待辦清單/時程風險） | 必要 | supported | 主責約 50 項大項功能規劃，掌握驗收與交付 | 主責50大項功能與111項Roadmap細項 |
| R05 強烈數據敏感度（能獨立使用SQL/BI/試算表） | 必要 | partial | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 懂資料表欄位並精熟Sheet/Excel，惟非自寫SQL |
| R06 熟悉AI工具（如Claude）與Jira/Confluence串接 | 必要 | partial | 自建 Claude Code 協作流程（12條分支、23個skill） | Claude Code應用深入，惟未列串接Jira自動化 |
| R07 對防詐與風險偵測有熱情及相關產品經驗 | 必要 | supported | 十多家廠商帳號遭冒用...上線簽章驗證 | 親歷B2B帳號冒用個資風險控管並完成簽章驗證 |
| R08 曾服務海外企業客戶或政府機關 | 加分 | partial | SweetRing 在地化涵蓋美、墨、巴、印、馬、日、韓7市場 | 具7國B2C在地化與台灣B2B，缺海外B2B客戶 |
| R09 具Agile/Scrum與產品定價成本利潤分析經驗 | 加分 | supported | 入職初期跑過完整 Scrum；依抽成稅費做實收試算 | 具完整Scrum經歷、定價實驗與跨國金流實收試算 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | Product Owner／PM｜1111 全球華人｜2022/08 - 迄今 | 符合 jd20 核心PM年資與交付要求 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責6.6萬家廠商招募系統 |
| HR03 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃與DBA/工程分工 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 交付週期、留存與媒合規模具明確基準 |
| HR05 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HR06 | supported | 從思維特助理PM、尚凡PM到1111企劃主任 | 職涯由C端0到1演進至B2B大型平台 |
| HR07 | supported | 入職初期跑過完整 Scrum；把衝突邏輯轉工程條件 | Scrum、原型、AI與英文協作皆有實例 |
| HR08 | supported | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 結構分明，重點指標與限制條件易讀 |
| HR09 | supported | 144 天後仍付費 91.4%，同期其餘廠商 89.2% | 主動標註觀察差異非因果，口徑可信 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd20 職責相容 |
| HR11 | supported | 雙北，可接受遠端或混合辦公｜錄取後三週可上班 | 地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 主責約 50 項大項功能規劃，掌握驗收與交付 | 證據鏈完整支持安排 jd20 面試 |
| HM01 | supported | KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO | 兼具0到1雙邊媒合與B2B企業系統經驗 |
| HM02 | supported | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 從客服訊號查明配對排序根因並實測競品 |
| HM03 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HM04 | supported | Peach 網頁付款占營收由 24% 至 80% 以上 | 具定價實驗、付費牆與網頁金流轉換實績 |
| HM05 | supported | 973 家活躍付費廠商，144 天後仍付費 91.4% | 交代期間、分母占比與非因果觀察限制 |
| HM06 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃、DBA取數與工程協作 |
| HM07 | supported | 求才端可存取大量求職者個資，冒用即有外洩風險 | 具重複信箱處理、離峰切換與防冒用閉環 |
| HM08 | partial | 把衝突的搜尋邏輯轉成工程條件；設每日配對上限 | 能將衝突邏輯轉工程條件，SQL由DBA代撈 |
| HM09 | supported | 約 50 項大項功能上線，另上線 111 項細項 | 主責50大項功能與6.6萬廠商系統，範圍相符 |
| HM10 | supported | 摘要與經歷清楚交代0到1、144天留存基準與非因果 | 摘要與條列經歷層次分明易檢索 |
| HM11 | supported | 改依職缺上線日排序；廠商也能自行切換排序（已上線） | 依客服回饋與還原原價結果修正產品規則 |
| HM12 | supported | 具KOOL 0到1、50項B2B交付、定價實驗與AI案例 | 具多個已上線案例，可於面試追問遷移細節 |
| HM13 | supported | 僅依 jd20 明文條件獨立取證判讀 | 僅依 jd20 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd20 |
| 2 | 具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗 |
| 3 | 已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 資料庫取數為「擬定資料表與欄位交 DBA 撈取」而非獨立撰寫 SQL；且海外 7 國經驗為 B2C App，尚未直接對接海外 B2B/B2G 企業客戶 | 請以英文簡述 2026/04 1111 廠商帳號遭冒用事件中，你如何評估求職者個資外洩風險、協調工程於 04/17 上線簽章驗證，以及後續如何設計主動偵測機制？ |
| 2 | 資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢 | 在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？ |
| 3 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd20 證明大型系統高密度交付與排程控管力
- 尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd20 展現完整 0 到 1 商業探索與雙邊媒合成果
- 1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd20 展現問題拆解、競品反推與嚴謹實驗能力

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定取數需求（資料表／欄位）交 DBA 撈取
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：資料庫取數為「擬定資料表與欄位交 DBA 撈取」而非獨立撰寫 SQL；且海外 7 國經驗為 B2C App，尚未直接對接海外 B2B/B2G 企業客戶
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄
- 位置：1111 全球華人經歷第 5 點
  - 原句：信件與即時通整合、搜尋結果頁改版（兩案皆開發中）
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9
  - 建議方向：面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：fail（本機實測 `resume-v10-twocol.pdf` 檢出粗體雙重疊字與雙欄讀序斷裂） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 Resume_AppendixA（jd26 全支付- Product Manager (專案執行)）｜第 6 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_AppendixA","job_id":"jd26","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd26-06","human_calibrated":false,"requirements":[{"id":"R01","text":"2年以上相關工作經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"年資與專案推進經驗豐富"},{"id":"R02","text":"能運用Axure撰寫規劃，透過Jira/Confluence管理","type":"required","status":"partial","evidence":["整理為 PRD 與 Axure Prototype；內部系統 ticket 追蹤"],"blocks_interview":false,"reason":"Axure實務極強，惟使用內部ticket系統非Jira"},{"id":"R03","text":"同步考慮技術可行性及系統架構關連影響","type":"required","status":"supported","evidence":["盤點出上千組重複 E-mail，選擇首次登入引導確認"],"blocks_interview":false,"reason":"兼顧新舊系統銜接與舊資料相容性"},{"id":"R04","text":"與合作方確認需求並與法遵確認適法性","type":"required","status":"supported","evidence":["工程、設計、QA、資料科學、客服、業務、法務與稽核協作"],"blocks_interview":false,"reason":"明列法務與稽核協作及外部金流團隊對接"},{"id":"R05","text":"執行專案測試、驗收、上線協調與教育訓練","type":"required","status":"supported","evidence":["全國客服封測後，第一階段於 2025/10 離峰切換上線"],"blocks_interview":false,"reason":"具UAT案例制定、全國客服封測說明與離峰上線"},{"id":"R06","text":"喜愛或熟悉數位金融、支付產品","type":"required","status":"supported","evidence":["導入 CodaPay，開放印尼、泰國等電信帳單與超商付款"],"blocks_interview":false,"reason":"具網頁付款、App內購與跨國替代支付串接經驗"},{"id":"R07","text":"熟悉代理收付、電子支付領域知識；精通英文","type":"preferred","status":"partial","evidence":["依抽成、稅、手續費及撥款週期做實收試算；TOEIC 980"],"blocks_interview":false,"reason":"具金流撥款實收試算與高分英文，無電支清算後台"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["全站約有 6.6 萬家活躍付費廠商（2026/04/30）"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"足夠","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"missing":["使用內部專案 ticket 系統與 Notion/Trello，未直接寫出 Jira/Confluence；無專營電支機構內部代理收付經驗"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"需求平均處理週期由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"截至 09/29，完成 1,726／1,857 張需求與問題單","kinds":["output"]},{"quote":"973 家活躍付費廠商，144 天後仍付費 91.4%","kinds":["context","outcome"]},{"quote":"網紅檔案約 1.6 萬份，半年累計 8 萬多次報名","kinds":["outcome"]},{"quote":"廠商也能自行切換排序（已上線）","kinds":["decision","output"]},{"quote":"信件與即時通整合、搜尋改版（兩案皆開發中）","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"符合 jd26 核心PM年資與交付要求"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責6.6萬家廠商招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"application_note":"清楚界定個人規劃與DBA/工程分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"application_note":"交付週期、留存與媒合規模具明確基準"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與首登引導取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從思維特助理PM、尚凡PM到1111企劃主任"],"application_note":"職涯由C端0到1演進至B2B大型平台"},{"rule_id":"HR07","status":"supported","resume_evidence":["入職初期跑過完整 Scrum；把衝突邏輯轉工程條件"],"application_note":"Scrum、原型、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"application_note":"結構分明，重點指標與限制條件易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["144 天後仍付費 91.4%，同期其餘廠商 89.2%"],"application_note":"主動標註觀察差異非因果，口徑可信"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd26 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["雙北，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["主責約 50 項大項功能規劃，掌握驗收與交付"],"application_note":"證據鏈完整支持安排 jd26 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["Peach 網頁付款占營收由 24% 至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"supported","resume_evidence":["973 家活躍付費廠商，144 天後仍付費 91.4%"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["求才端可存取大量求職者個資，冒用即有外洩風險"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["把衝突的搜尋邏輯轉成工程條件；設每日配對上限"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能上線，另上線 111 項細項"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["摘要與經歷清楚交代0到1、144天留存基準與非因果"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["改依職缺上線日排序；廠商也能自行切換排序（已上線）"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、50項B2B交付、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"在 1111 招募系統改版與過往 CodaPay 金流串接中，你如何與法務稽核確認適法性，並在離峰切換上線前完成全國客服的教育訓練？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd26 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定取數需求（資料表／欄位）交 DBA 撈取","reason":"專案追蹤採用公司內部 ticket 系統與 Notion/Trello，未明列 Jira/Confluence；金流經驗偏商戶端串接而非專營電子支付機構代理收付帳務","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄"},{"id":"I02","rule_id":"HM07","source_ids":[],"application_note":"開發中專案尚無上線後成效數據","context_limit":"1111 全球華人經歷第 5 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"信件與即時通整合、搜尋結果頁改版（兩案皆開發中）","reason":"兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9","suggestion":"面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗，經手 6 款產品","主責約 50 項大項功能規劃，掌握驗收與交付"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd26","具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗","已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績"],"key_gaps":["專案追蹤採用公司內部 ticket 系統與 Notion/Trello，未明列 Jira/Confluence；金流經驗偏商戶端串接而非專營電子支付機構代理收付帳務","資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢","「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字"],"strengths":["1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd26 證明大型系統高密度交付與排程控管力","尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd26 展現完整 0 到 1 商業探索與雙邊媒合成果","1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd26 展現問題拆解、競品反推與嚴謹實驗能力"],"interview_questions":["在 1111 招募系統改版與過往 CodaPay 金流串接中，你如何與法務稽核確認適法性，並在離峰切換上線前完成全國客服的教育訓練？","在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？","「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd26 具備多個已實現案例、清楚取捨與嚴謹衡量支持面試，惟部分工具字面條件或次領域經驗待面試補驗"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"fail","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「整理為 PRD 與 Axure Prototype」並統籌全國客服封測與離峰切換上線，契合專案執行。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 全站約有 6.6 萬家活躍付費廠商（2026/04/30） | 無關鍵缺口，可於面試深化 |
| role_evidence | 足夠 | 近 10 年 PM 經驗，經手 6 款產品 | 使用內部專案 ticket 系統與 Notion/Trello，未直接寫出 Jira/Confluence；無專營電支機構內部代理收付經驗 |
| decision_depth | 強 | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 需求平均處理週期由 100.4 天降至 30.9 天 | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 2年以上相關工作經驗 | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 年資與專案推進經驗豐富 |
| R02 能運用Axure撰寫規劃，透過Jira/Confluence管理 | 必要 | partial | 整理為 PRD 與 Axure Prototype；內部系統 ticket 追蹤 | Axure實務極強，惟使用內部ticket系統非Jira |
| R03 同步考慮技術可行性及系統架構關連影響 | 必要 | supported | 盤點出上千組重複 E-mail，選擇首次登入引導確認 | 兼顧新舊系統銜接與舊資料相容性 |
| R04 與合作方確認需求並與法遵確認適法性 | 必要 | supported | 工程、設計、QA、資料科學、客服、業務、法務與稽核協作 | 明列法務與稽核協作及外部金流團隊對接 |
| R05 執行專案測試、驗收、上線協調與教育訓練 | 必要 | supported | 全國客服封測後，第一階段於 2025/10 離峰切換上線 | 具UAT案例制定、全國客服封測說明與離峰上線 |
| R06 喜愛或熟悉數位金融、支付產品 | 必要 | supported | 導入 CodaPay，開放印尼、泰國等電信帳單與超商付款 | 具網頁付款、App內購與跨國替代支付串接經驗 |
| R07 熟悉代理收付、電子支付領域知識；精通英文 | 加分 | partial | 依抽成、稅、手續費及撥款週期做實收試算；TOEIC 980 | 具金流撥款實收試算與高分英文，無電支清算後台 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 符合 jd26 核心PM年資與交付要求 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責6.6萬家廠商招募系統 |
| HR03 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃與DBA/工程分工 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 交付週期、留存與媒合規模具明確基準 |
| HR05 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HR06 | supported | 從思維特助理PM、尚凡PM到1111企劃主任 | 職涯由C端0到1演進至B2B大型平台 |
| HR07 | supported | 入職初期跑過完整 Scrum；把衝突邏輯轉工程條件 | Scrum、原型、AI與英文協作皆有實例 |
| HR08 | supported | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 結構分明，重點指標與限制條件易讀 |
| HR09 | supported | 144 天後仍付費 91.4%，同期其餘廠商 89.2% | 主動標註觀察差異非因果，口徑可信 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd26 職責相容 |
| HR11 | supported | 雙北，可接受遠端或混合辦公｜錄取後三週可上班 | 地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 主責約 50 項大項功能規劃，掌握驗收與交付 | 證據鏈完整支持安排 jd26 面試 |
| HM01 | supported | KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO | 兼具0到1雙邊媒合與B2B企業系統經驗 |
| HM02 | supported | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 從客服訊號查明配對排序根因並實測競品 |
| HM03 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HM04 | supported | Peach 網頁付款占營收由 24% 至 80% 以上 | 具定價實驗、付費牆與網頁金流轉換實績 |
| HM05 | supported | 973 家活躍付費廠商，144 天後仍付費 91.4% | 交代期間、分母占比與非因果觀察限制 |
| HM06 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃、DBA取數與工程協作 |
| HM07 | supported | 求才端可存取大量求職者個資，冒用即有外洩風險 | 具重複信箱處理、離峰切換與防冒用閉環 |
| HM08 | supported | 把衝突的搜尋邏輯轉成工程條件；設每日配對上限 | 能將衝突邏輯轉工程條件，SQL由DBA代撈 |
| HM09 | supported | 約 50 項大項功能上線，另上線 111 項細項 | 主責50大項功能與6.6萬廠商系統，範圍相符 |
| HM10 | supported | 摘要與經歷清楚交代0到1、144天留存基準與非因果 | 摘要與條列經歷層次分明易檢索 |
| HM11 | supported | 改依職缺上線日排序；廠商也能自行切換排序（已上線） | 依客服回饋與還原原價結果修正產品規則 |
| HM12 | supported | 具KOOL 0到1、50項B2B交付、定價實驗與AI案例 | 具多個已上線案例，可於面試追問遷移細節 |
| HM13 | supported | 僅依 jd26 明文條件獨立取證判讀 | 僅依 jd26 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd26 |
| 2 | 具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗 |
| 3 | 已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 專案追蹤採用公司內部 ticket 系統與 Notion/Trello，未明列 Jira/Confluence；金流經驗偏商戶端串接而非專營電子支付機構代理收付帳務 | 在 1111 招募系統改版與過往 CodaPay 金流串接中，你如何與法務稽核確認適法性，並在離峰切換上線前完成全國客服的教育訓練？ |
| 2 | 資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢 | 在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？ |
| 3 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd26 證明大型系統高密度交付與排程控管力
- 尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd26 展現完整 0 到 1 商業探索與雙邊媒合成果
- 1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd26 展現問題拆解、競品反推與嚴謹實驗能力

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定取數需求（資料表／欄位）交 DBA 撈取
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：專案追蹤採用公司內部 ticket 系統與 Notion/Trello，未明列 Jira/Confluence；金流經驗偏商戶端串接而非專營電子支付機構代理收付帳務
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄
- 位置：1111 全球華人經歷第 5 點
  - 原句：信件與即時通整合、搜尋結果頁改版（兩案皆開發中）
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9
  - 建議方向：面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：fail（本機實測 `resume-v10-twocol.pdf` 檢出粗體雙重疊字與雙欄讀序斷裂） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 Resume_AppendixA（jd30 資深產品經理｜Senior Product Manager｜USPACE）｜第 7 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_AppendixA","job_id":"jd30","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd30-07","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上Software PM且至少一次完整0到1直接負責經歷","type":"required","status":"supported","evidence":["KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名"],"blocks_interview":false,"reason":"完整主導KOOL從0到1探索、原型、上線與雙邊媒合"},{"id":"R02","text":"能寫清楚的規格文件（PRD、流程圖、資料結構）","type":"required","status":"supported","evidence":["流程圖／循序圖、PRD；擬定取數的資料表與欄位"],"blocks_interview":false,"reason":"具PRD、循序圖與擬定資料庫資料表及欄位能力"},{"id":"R03","text":"理解API、JSON與基本SQL","type":"required","status":"partial","evidence":["API 串接規劃、資料庫知識；擬定資料表欄位交 DBA"],"blocks_interview":false,"reason":"具API與資料表欄位規劃，未明列JSON與自寫SQL"},{"id":"R04","text":"習慣用AI工具（Claude Code等）把工作流程化","type":"preferred","status":"supported","evidence":["自建 Claude Code 協作流程（12條分支、23個skill）"],"blocks_interview":false,"reason":"直接命中Claude Code多分支流程與轉譯工程條件"},{"id":"R05","text":"支付或FinTech經驗、Growth或數據分析經驗","type":"preferred","status":"supported","evidence":["Peach 網頁付款占營收由 24% 至 80% 以上"],"blocks_interview":false,"reason":"具網頁金流、CodaPay串接與三階段定價實驗"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["全站約有 6.6 萬家活躍付費廠商（2026/04/30）"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"足夠","evidence":["KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名"],"missing":["必備條件中之 JSON 未明文呈現，且資料庫查詢為擬定資料表欄位交 DBA 撈取而非自寫 SQL"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"需求平均處理週期由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"截至 09/29，完成 1,726／1,857 張需求與問題單","kinds":["output"]},{"quote":"973 家活躍付費廠商，144 天後仍付費 91.4%","kinds":["context","outcome"]},{"quote":"網紅檔案約 1.6 萬份，半年累計 8 萬多次報名","kinds":["outcome"]},{"quote":"廠商也能自行切換排序（已上線）","kinds":["decision","output"]},{"quote":"信件與即時通整合、搜尋改版（兩案皆開發中）","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名"],"application_note":"符合 jd30 核心PM年資與交付要求"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責6.6萬家廠商招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"application_note":"清楚界定個人規劃與DBA/工程分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"application_note":"交付週期、留存與媒合規模具明確基準"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與首登引導取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從思維特助理PM、尚凡PM到1111企劃主任"],"application_note":"職涯由C端0到1演進至B2B大型平台"},{"rule_id":"HR07","status":"supported","resume_evidence":["入職初期跑過完整 Scrum；把衝突邏輯轉工程條件"],"application_note":"Scrum、原型、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"application_note":"結構分明，重點指標與限制條件易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["144 天後仍付費 91.4%，同期其餘廠商 89.2%"],"application_note":"主動標註觀察差異非因果，口徑可信"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd30 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["雙北，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["主責約 50 項大項功能規劃，掌握驗收與交付"],"application_note":"證據鏈完整支持安排 jd30 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["Peach 網頁付款占營收由 24% 至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"supported","resume_evidence":["973 家活躍付費廠商，144 天後仍付費 91.4%"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["求才端可存取大量求職者個資，冒用即有外洩風險"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"partial","resume_evidence":["把衝突的搜尋邏輯轉成工程條件；設每日配對上限"],"evidence_type":"output","source_ids":[],"interview_question":"請說明如何將衝突搜尋邏輯轉成工程條件，以及是否具基礎 SQL/JSON 實作經驗？"},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能上線，另上線 111 項細項"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["摘要與經歷清楚交代0到1、144天留存基準與非因果"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["改依職缺上線日排序；廠商也能自行切換排序（已上線）"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、50項B2B交付、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"請分享你自建 Claude Code 12 條分支與 23 個共用 skill 的具體架構，以及如何用它「把衝突的搜尋邏輯轉成工程條件」？另外能否現場說明 API JSON 結構與基礎 SQL JOIN 邏輯？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd30 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定取數需求（資料表／欄位）交 DBA 撈取","reason":"必備條件要求理解 API、JSON 與基本 SQL，履歷雖載明 API 串接規劃與擬定資料表欄位交 DBA 撈取，但未呈現 JSON 與親自撰寫 SQL 查詢紀錄","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄"},{"id":"I02","rule_id":"HM07","source_ids":[],"application_note":"開發中專案尚無上線後成效數據","context_limit":"1111 全球華人經歷第 5 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"信件與即時通整合、搜尋結果頁改版（兩案皆開發中）","reason":"兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9","suggestion":"面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）"}],"decision":{"recommendation":"interview","evidence":["KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名","主責約 50 項大項功能規劃，掌握驗收與交付"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd30","具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗","已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績"],"key_gaps":["必備條件要求理解 API、JSON 與基本 SQL，履歷雖載明 API 串接規劃與擬定資料表欄位交 DBA 撈取，但未呈現 JSON 與親自撰寫 SQL 查詢紀錄","資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢","「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字"],"strengths":["1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd30 證明大型系統高密度交付與排程控管力","尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd30 展現完整 0 到 1 商業探索與雙邊媒合成果","1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd30 展現問題拆解、競品反推與嚴謹實驗能力"],"interview_questions":["請分享你自建 Claude Code 12 條分支與 23 個共用 skill 的具體架構，以及如何用它「把衝突的搜尋邏輯轉成工程條件」？另外能否現場說明 API JSON 結構與基礎 SQL JOIN 邏輯？","在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？","「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd30 具備多個已實現案例、清楚取捨與嚴謹衡量支持面試，惟部分工具字面條件或次領域經驗待面試補驗"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"fail","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名」且自建 Claude Code 流程，支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 全站約有 6.6 萬家活躍付費廠商（2026/04/30） | 無關鍵缺口，可於面試深化 |
| role_evidence | 足夠 | KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名 | 必備條件中之 JSON 未明文呈現，且資料庫查詢為擬定資料表欄位交 DBA 撈取而非自寫 SQL |
| decision_depth | 強 | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 需求平均處理週期由 100.4 天降至 30.9 天 | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 3年以上Software PM且至少一次完整0到1直接負責經歷 | 必要 | supported | KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名 | 完整主導KOOL從0到1探索、原型、上線與雙邊媒合 |
| R02 能寫清楚的規格文件（PRD、流程圖、資料結構） | 必要 | supported | 流程圖／循序圖、PRD；擬定取數的資料表與欄位 | 具PRD、循序圖與擬定資料庫資料表及欄位能力 |
| R03 理解API、JSON與基本SQL | 必要 | partial | API 串接規劃、資料庫知識；擬定資料表欄位交 DBA | 具API與資料表欄位規劃，未明列JSON與自寫SQL |
| R04 習慣用AI工具（Claude Code等）把工作流程化 | 加分 | supported | 自建 Claude Code 協作流程（12條分支、23個skill） | 直接命中Claude Code多分支流程與轉譯工程條件 |
| R05 支付或FinTech經驗、Growth或數據分析經驗 | 加分 | supported | Peach 網頁付款占營收由 24% 至 80% 以上 | 具網頁金流、CodaPay串接與三階段定價實驗 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名 | 符合 jd30 核心PM年資與交付要求 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責6.6萬家廠商招募系統 |
| HR03 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃與DBA/工程分工 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 交付週期、留存與媒合規模具明確基準 |
| HR05 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HR06 | supported | 從思維特助理PM、尚凡PM到1111企劃主任 | 職涯由C端0到1演進至B2B大型平台 |
| HR07 | supported | 入職初期跑過完整 Scrum；把衝突邏輯轉工程條件 | Scrum、原型、AI與英文協作皆有實例 |
| HR08 | supported | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 結構分明，重點指標與限制條件易讀 |
| HR09 | supported | 144 天後仍付費 91.4%，同期其餘廠商 89.2% | 主動標註觀察差異非因果，口徑可信 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd30 職責相容 |
| HR11 | supported | 雙北，可接受遠端或混合辦公｜錄取後三週可上班 | 地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 主責約 50 項大項功能規劃，掌握驗收與交付 | 證據鏈完整支持安排 jd30 面試 |
| HM01 | supported | KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO | 兼具0到1雙邊媒合與B2B企業系統經驗 |
| HM02 | supported | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 從客服訊號查明配對排序根因並實測競品 |
| HM03 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HM04 | supported | Peach 網頁付款占營收由 24% 至 80% 以上 | 具定價實驗、付費牆與網頁金流轉換實績 |
| HM05 | supported | 973 家活躍付費廠商，144 天後仍付費 91.4% | 交代期間、分母占比與非因果觀察限制 |
| HM06 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃、DBA取數與工程協作 |
| HM07 | supported | 求才端可存取大量求職者個資，冒用即有外洩風險 | 具重複信箱處理、離峰切換與防冒用閉環 |
| HM08 | partial | 把衝突的搜尋邏輯轉成工程條件；設每日配對上限 | 能將衝突邏輯轉工程條件，SQL由DBA代撈 |
| HM09 | supported | 約 50 項大項功能上線，另上線 111 項細項 | 主責50大項功能與6.6萬廠商系統，範圍相符 |
| HM10 | supported | 摘要與經歷清楚交代0到1、144天留存基準與非因果 | 摘要與條列經歷層次分明易檢索 |
| HM11 | supported | 改依職缺上線日排序；廠商也能自行切換排序（已上線） | 依客服回饋與還原原價結果修正產品規則 |
| HM12 | supported | 具KOOL 0到1、50項B2B交付、定價實驗與AI案例 | 具多個已上線案例，可於面試追問遷移細節 |
| HM13 | supported | 僅依 jd30 明文條件獨立取證判讀 | 僅依 jd30 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd30 |
| 2 | 具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗 |
| 3 | 已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 必備條件要求理解 API、JSON 與基本 SQL，履歷雖載明 API 串接規劃與擬定資料表欄位交 DBA 撈取，但未呈現 JSON 與親自撰寫 SQL 查詢紀錄 | 請分享你自建 Claude Code 12 條分支與 23 個共用 skill 的具體架構，以及如何用它「把衝突的搜尋邏輯轉成工程條件」？另外能否現場說明 API JSON 結構與基礎 SQL JOIN 邏輯？ |
| 2 | 資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢 | 在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？ |
| 3 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd30 證明大型系統高密度交付與排程控管力
- 尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd30 展現完整 0 到 1 商業探索與雙邊媒合成果
- 1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd30 展現問題拆解、競品反推與嚴謹實驗能力

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定取數需求（資料表／欄位）交 DBA 撈取
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：必備條件要求理解 API、JSON 與基本 SQL，履歷雖載明 API 串接規劃與擬定資料表欄位交 DBA 撈取，但未呈現 JSON 與親自撰寫 SQL 查詢紀錄
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄
- 位置：1111 全球華人經歷第 5 點
  - 原句：信件與即時通整合、搜尋結果頁改版（兩案皆開發中）
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9
  - 建議方向：面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：fail（本機實測 `resume-v10-twocol.pdf` 檢出粗體雙重疊字與雙欄讀序斷裂） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 Resume_AppendixA（jd31 資深產品經理【擴編】｜人易科技 (NUEIP)）｜第 8 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_AppendixA","job_id":"jd31","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd31-08","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上產品規劃與需求訪談、熟悉0到1或迭代流程","type":"required","status":"supported","evidence":["KOOL 從 0 到 1 探索商業模式；約 50 項大項功能上線"],"blocks_interview":false,"reason":"同時具備KOOL 0到1與1111大型系統迭代實績"},{"id":"R02","text":"具備專案管理與風險管理經驗","type":"required","status":"supported","evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"blocks_interview":false,"reason":"具50大項功能時程控管、離峰上線與防冒用風控"},{"id":"R03","text":"有多系統整合或API串接經驗","type":"required","status":"supported","evidence":["API 串接規劃、舊系統資料盤點；CodaPay 串接"],"blocks_interview":false,"reason":"具新舊系統漸進替換、社群認證與跨國金流串接"},{"id":"R04","text":"熟悉PRD、功能規格與流程圖設計","type":"required","status":"supported","evidence":["Use Case、流程圖／循序圖、Wireframe、PRD"],"blocks_interview":false,"reason":"產品規格與流程圖產出體系完整"},{"id":"R05","text":"熟悉敏捷開發流程（Scrum）","type":"required","status":"supported","evidence":["入職初期完整 Scrum（一週一個 Sprint）"],"blocks_interview":false,"reason":"明確具備完整Scrum儀式與Kanban雙重實務"},{"id":"R06","text":"曾主導企業級系統（ERP/HRM/SaaS/平台）規劃","type":"preferred","status":"supported","evidence":["擔任企業端招募系統 PO；全站約 6.6 萬家活躍付費廠商"],"blocks_interview":false,"reason":"直接主導企業招募平台，與雲端人資HRM高度同源"},{"id":"R07","text":"具備資料分析能力（SQL/BI工具）與技術背景","type":"preferred","status":"partial","evidence":["擬定取數需求（資料表／欄位）交 DBA 撈取，以 Excel 分析"],"blocks_interview":false,"reason":"懂資料庫欄位、API與系統分析，惟非自寫SQL/BI"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["全站約有 6.6 萬家活躍付費廠商（2026/04/30）"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"強","evidence":["KOOL 從 0 到 1 探索商業模式；約 50 項大項功能上線"],"missing":["加分項之 SQL/BI 採擬定資料表欄位交 DBA 撈取並以 Google Sheet/Excel 分析"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"需求平均處理週期由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"截至 09/29，完成 1,726／1,857 張需求與問題單","kinds":["output"]},{"quote":"973 家活躍付費廠商，144 天後仍付費 91.4%","kinds":["context","outcome"]},{"quote":"網紅檔案約 1.6 萬份，半年累計 8 萬多次報名","kinds":["outcome"]},{"quote":"廠商也能自行切換排序（已上線）","kinds":["decision","output"]},{"quote":"信件與即時通整合、搜尋改版（兩案皆開發中）","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["KOOL 從 0 到 1 探索商業模式；約 50 項大項功能上線"],"application_note":"符合 jd31 核心PM年資與交付要求"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責6.6萬家廠商招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"application_note":"清楚界定個人規劃與DBA/工程分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"application_note":"交付週期、留存與媒合規模具明確基準"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與首登引導取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從思維特助理PM、尚凡PM到1111企劃主任"],"application_note":"職涯由C端0到1演進至B2B大型平台"},{"rule_id":"HR07","status":"supported","resume_evidence":["入職初期跑過完整 Scrum；把衝突邏輯轉工程條件"],"application_note":"Scrum、原型、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"application_note":"結構分明，重點指標與限制條件易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["144 天後仍付費 91.4%，同期其餘廠商 89.2%"],"application_note":"主動標註觀察差異非因果，口徑可信"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd31 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["雙北，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["主責約 50 項大項功能規劃，掌握驗收與交付"],"application_note":"證據鏈完整支持安排 jd31 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["Peach 網頁付款占營收由 24% 至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"supported","resume_evidence":["973 家活躍付費廠商，144 天後仍付費 91.4%"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["求才端可存取大量求職者個資，冒用即有外洩風險"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["把衝突的搜尋邏輯轉成工程條件；設每日配對上限"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能上線，另上線 111 項細項"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["摘要與經歷清楚交代0到1、144天留存基準與非因果"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["改依職缺上線日排序；廠商也能自行切換排序（已上線）"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、50項B2B交付、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"在 1111 推進三階段企業端招募系統改版、同時保留舊服務並銜接新系統的過程中，你如何進行系統分析與跨系統資料交換設計？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd31 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定取數需求（資料表／欄位）交 DBA 撈取","reason":"必要條件全數支持；加分項之資料分析採「擬定資料表與欄位交 DBA 撈取、以 Sheet/Excel 分析」模式，未明列獨立撰寫 SQL 或 BI 視覺化工具","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄"},{"id":"I02","rule_id":"HM07","source_ids":[],"application_note":"開發中專案尚無上線後成效數據","context_limit":"1111 全球華人經歷第 5 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"信件與即時通整合、搜尋結果頁改版（兩案皆開發中）","reason":"兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9","suggestion":"面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）"}],"decision":{"recommendation":"interview","evidence":["KOOL 從 0 到 1 探索商業模式；約 50 項大項功能上線","主責約 50 項大項功能規劃，掌握驗收與交付"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd31","具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗","已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績"],"key_gaps":["必要條件全數支持；加分項之資料分析採「擬定資料表與欄位交 DBA 撈取、以 Sheet/Excel 分析」模式，未明列獨立撰寫 SQL 或 BI 視覺化工具","資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢","「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字"],"strengths":["1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd31 證明大型系統高密度交付與排程控管力","尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd31 展現完整 0 到 1 商業探索與雙邊媒合成果","1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd31 展現問題拆解、競品反推與嚴謹實驗能力"],"interview_questions":["在 1111 推進三階段企業端招募系統改版、同時保留舊服務並銜接新系統的過程中，你如何進行系統分析與跨系統資料交換設計？","在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？","「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例"],"spectrum":{"level":9,"uncertainty_levels":1,"basis":"針對 jd31 具備完整已上線之B2B平台與0到1量化實績（50大項功能、週期降至30.9天、8萬次報名），關鍵量測與責任可追溯"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"fail","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：9（±1）
- 一句話理由：「擔任企業端招募系統 PO」主責 50 大項功能上線且「入職初期跑過完整 Scrum」，高度契合。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 全站約有 6.6 萬家活躍付費廠商（2026/04/30） | 無關鍵缺口，可於面試深化 |
| role_evidence | 強 | KOOL 從 0 到 1 探索商業模式；約 50 項大項功能上線 | 加分項之 SQL/BI 採擬定資料表欄位交 DBA 撈取並以 Google Sheet/Excel 分析 |
| decision_depth | 強 | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 需求平均處理週期由 100.4 天降至 30.9 天 | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 3年以上產品規劃與需求訪談、熟悉0到1或迭代流程 | 必要 | supported | KOOL 從 0 到 1 探索商業模式；約 50 項大項功能上線 | 同時具備KOOL 0到1與1111大型系統迭代實績 |
| R02 具備專案管理與風險管理經驗 | 必要 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 具50大項功能時程控管、離峰上線與防冒用風控 |
| R03 有多系統整合或API串接經驗 | 必要 | supported | API 串接規劃、舊系統資料盤點；CodaPay 串接 | 具新舊系統漸進替換、社群認證與跨國金流串接 |
| R04 熟悉PRD、功能規格與流程圖設計 | 必要 | supported | Use Case、流程圖／循序圖、Wireframe、PRD | 產品規格與流程圖產出體系完整 |
| R05 熟悉敏捷開發流程（Scrum） | 必要 | supported | 入職初期完整 Scrum（一週一個 Sprint） | 明確具備完整Scrum儀式與Kanban雙重實務 |
| R06 曾主導企業級系統（ERP/HRM/SaaS/平台）規劃 | 加分 | supported | 擔任企業端招募系統 PO；全站約 6.6 萬家活躍付費廠商 | 直接主導企業招募平台，與雲端人資HRM高度同源 |
| R07 具備資料分析能力（SQL/BI工具）與技術背景 | 加分 | partial | 擬定取數需求（資料表／欄位）交 DBA 撈取，以 Excel 分析 | 懂資料庫欄位、API與系統分析，惟非自寫SQL/BI |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | KOOL 從 0 到 1 探索商業模式；約 50 項大項功能上線 | 符合 jd31 核心PM年資與交付要求 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責6.6萬家廠商招募系統 |
| HR03 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃與DBA/工程分工 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 交付週期、留存與媒合規模具明確基準 |
| HR05 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HR06 | supported | 從思維特助理PM、尚凡PM到1111企劃主任 | 職涯由C端0到1演進至B2B大型平台 |
| HR07 | supported | 入職初期跑過完整 Scrum；把衝突邏輯轉工程條件 | Scrum、原型、AI與英文協作皆有實例 |
| HR08 | supported | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 結構分明，重點指標與限制條件易讀 |
| HR09 | supported | 144 天後仍付費 91.4%，同期其餘廠商 89.2% | 主動標註觀察差異非因果，口徑可信 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd31 職責相容 |
| HR11 | supported | 雙北，可接受遠端或混合辦公｜錄取後三週可上班 | 地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 主責約 50 項大項功能規劃，掌握驗收與交付 | 證據鏈完整支持安排 jd31 面試 |
| HM01 | supported | KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO | 兼具0到1雙邊媒合與B2B企業系統經驗 |
| HM02 | supported | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 從客服訊號查明配對排序根因並實測競品 |
| HM03 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HM04 | supported | Peach 網頁付款占營收由 24% 至 80% 以上 | 具定價實驗、付費牆與網頁金流轉換實績 |
| HM05 | supported | 973 家活躍付費廠商，144 天後仍付費 91.4% | 交代期間、分母占比與非因果觀察限制 |
| HM06 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃、DBA取數與工程協作 |
| HM07 | supported | 求才端可存取大量求職者個資，冒用即有外洩風險 | 具重複信箱處理、離峰切換與防冒用閉環 |
| HM08 | supported | 把衝突的搜尋邏輯轉成工程條件；設每日配對上限 | 能將衝突邏輯轉工程條件，SQL由DBA代撈 |
| HM09 | supported | 約 50 項大項功能上線，另上線 111 項細項 | 主責50大項功能與6.6萬廠商系統，範圍相符 |
| HM10 | supported | 摘要與經歷清楚交代0到1、144天留存基準與非因果 | 摘要與條列經歷層次分明易檢索 |
| HM11 | supported | 改依職缺上線日排序；廠商也能自行切換排序（已上線） | 依客服回饋與還原原價結果修正產品規則 |
| HM12 | supported | 具KOOL 0到1、50項B2B交付、定價實驗與AI案例 | 具多個已上線案例，可於面試追問遷移細節 |
| HM13 | supported | 僅依 jd31 明文條件獨立取證判讀 | 僅依 jd31 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd31 |
| 2 | 具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗 |
| 3 | 已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 必要條件全數支持；加分項之資料分析採「擬定資料表與欄位交 DBA 撈取、以 Sheet/Excel 分析」模式，未明列獨立撰寫 SQL 或 BI 視覺化工具 | 在 1111 推進三階段企業端招募系統改版、同時保留舊服務並銜接新系統的過程中，你如何進行系統分析與跨系統資料交換設計？ |
| 2 | 資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢 | 在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？ |
| 3 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd31 證明大型系統高密度交付與排程控管力
- 尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd31 展現完整 0 到 1 商業探索與雙邊媒合成果
- 1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd31 展現問題拆解、競品反推與嚴謹實驗能力

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定取數需求（資料表／欄位）交 DBA 撈取
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：必要條件全數支持；加分項之資料分析採「擬定資料表與欄位交 DBA 撈取、以 Sheet/Excel 分析」模式，未明列獨立撰寫 SQL 或 BI 視覺化工具
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄
- 位置：1111 全球華人經歷第 5 點
  - 原句：信件與即時通整合、搜尋結果頁改版（兩案皆開發中）
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9
  - 建議方向：面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：強

### 8. 未測試聲明
PDF 抽字：fail（本機實測 `resume-v10-twocol.pdf` 檢出粗體雙重疊字與雙欄讀序斷裂） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 Resume_AppendixA（jd32 產品專案經理(內部系統)｜104人力銀行）｜第 9 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_AppendixA","job_id":"jd32","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd32-09","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上經驗且具網站開發或SA系統分析經驗","type":"required","status":"supported","evidence":["釐清需求與系統分析後，以 Use Case 定義業務流程"],"blocks_interview":false,"reason":"現任同業招募系統PO且親自執行系統分析與舊資料盤點"},{"id":"R02","text":"接手內部使用者與外部客戶議題並安排優化或修正","type":"required","status":"supported","evidence":["對接 10 個需求單位；完成 1,726／1,857 張需求與問題單"],"blocks_interview":false,"reason":"高密度處理內部10單位與外部付費廠商問題單，完成率93%"},{"id":"R03","text":"運用AI工具進行營運分析或提案","type":"required","status":"supported","evidence":["自建 Claude Code 協作流程，把衝突搜尋邏輯轉工程條件"],"blocks_interview":false,"reason":"深入運用Claude Code於規格、資料分析與邏輯轉譯"},{"id":"R04","text":"熟悉規格撰寫、跨單位溝通與評估時程可行性","type":"required","status":"supported","evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"blocks_interview":false,"reason":"規格完整且將需求處理週期大幅縮短近70%"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["全站約有 6.6 萬家活躍付費廠商（2026/04/30）"],"missing":["現職同時負責外部企業端與求職端，轉任純內部營運系統之職涯期待可於面試確認"],"issue_ids":["I02"]},{"id":"role_evidence","rating":"強","evidence":["釐清需求與系統分析後，以 Use Case 定義業務流程"],"missing":[],"issue_ids":[]},{"id":"decision_depth","rating":"強","evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"需求平均處理週期由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"截至 09/29，完成 1,726／1,857 張需求與問題單","kinds":["output"]},{"quote":"973 家活躍付費廠商，144 天後仍付費 91.4%","kinds":["context","outcome"]},{"quote":"網紅檔案約 1.6 萬份，半年累計 8 萬多次報名","kinds":["outcome"]},{"quote":"廠商也能自行切換排序（已上線）","kinds":["decision","output"]},{"quote":"信件與即時通整合、搜尋改版（兩案皆開發中）","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["釐清需求與系統分析後，以 Use Case 定義業務流程"],"application_note":"符合 jd32 核心PM年資與交付要求"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責6.6萬家廠商招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"application_note":"清楚界定個人規劃與DBA/工程分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"application_note":"交付週期、留存與媒合規模具明確基準"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與首登引導取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從思維特助理PM、尚凡PM到1111企劃主任"],"application_note":"職涯由C端0到1演進至B2B大型平台"},{"rule_id":"HR07","status":"supported","resume_evidence":["入職初期跑過完整 Scrum；把衝突邏輯轉工程條件"],"application_note":"Scrum、原型、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"application_note":"結構分明，重點指標與限制條件易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["144 天後仍付費 91.4%，同期其餘廠商 89.2%"],"application_note":"主動標註觀察差異非因果，口徑可信"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd32 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["雙北，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["主責約 50 項大項功能規劃，掌握驗收與交付"],"application_note":"證據鏈完整支持安排 jd32 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["Peach 網頁付款占營收由 24% 至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"supported","resume_evidence":["973 家活躍付費廠商，144 天後仍付費 91.4%"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["求才端可存取大量求職者個資，冒用即有外洩風險"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["把衝突的搜尋邏輯轉成工程條件；設每日配對上限"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能上線，另上線 111 項細項"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["摘要與經歷清楚交代0到1、144天留存基準與非因果"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["改依職缺上線日排序；廠商也能自行切換排序（已上線）"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、50項B2B交付、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"你在 1111 將需求平均處理週期由 100.4 天降至 30.9 天並完成 1,726 張單的具體排程機制為何？如何運用 Claude Code 協助內部營運需求分析與規格拆解？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd32 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定取數需求（資料表／欄位）交 DBA 撈取","reason":"職缺明文條件全數符合；唯一需在面試確認的是候選人自傳期望「把更多心力放回產品策略」，與本職缺偏向「內部營運系統問題修正與優化」之期望對齊","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄"},{"id":"I02","rule_id":"HM07","source_ids":[],"application_note":"開發中專案尚無上線後成效數據","context_limit":"1111 全球華人經歷第 5 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"信件與即時通整合、搜尋結果頁改版（兩案皆開發中）","reason":"兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9","suggestion":"面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）"}],"decision":{"recommendation":"interview","evidence":["釐清需求與系統分析後，以 Use Case 定義業務流程","主責約 50 項大項功能規劃，掌握驗收與交付"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"強"},"interview_reasons":["兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd32","具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗","已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績"],"key_gaps":["職缺明文條件全數符合；唯一需在面試確認的是候選人自傳期望「把更多心力放回產品策略」，與本職缺偏向「內部營運系統問題修正與優化」之期望對齊","資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢","「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字"],"strengths":["1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd32 證明大型系統高密度交付與排程控管力","尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd32 展現完整 0 到 1 商業探索與雙邊媒合成果","1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd32 展現問題拆解、競品反推與嚴謹實驗能力"],"interview_questions":["你在 1111 將需求平均處理週期由 100.4 天降至 30.9 天並完成 1,726 張單的具體排程機制為何？如何運用 Claude Code 協助內部營運需求分析與規格拆解？","在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？","「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例"],"spectrum":{"level":9,"uncertainty_levels":1,"basis":"針對 jd32 具備完整已上線之B2B平台與0到1量化實績（50大項功能、週期降至30.9天、8萬次報名），關鍵量測與責任可追溯"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"fail","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：9（±1）
- 一句話理由：現任同業招募系統 PO，「完成 1,726／1,857 張需求與問題單」且具系統分析與 Claude Code 實績。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 全站約有 6.6 萬家活躍付費廠商（2026/04/30） | 現職同時負責外部企業端與求職端，轉任純內部營運系統之職涯期待可於面試確認 |
| role_evidence | 強 | 釐清需求與系統分析後，以 Use Case 定義業務流程 | 無關鍵缺口，可於面試深化 |
| decision_depth | 強 | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 需求平均處理週期由 100.4 天降至 30.9 天 | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 3年以上經驗且具網站開發或SA系統分析經驗 | 必要 | supported | 釐清需求與系統分析後，以 Use Case 定義業務流程 | 現任同業招募系統PO且親自執行系統分析與舊資料盤點 |
| R02 接手內部使用者與外部客戶議題並安排優化或修正 | 必要 | supported | 對接 10 個需求單位；完成 1,726／1,857 張需求與問題單 | 高密度處理內部10單位與外部付費廠商問題單，完成率93% |
| R03 運用AI工具進行營運分析或提案 | 必要 | supported | 自建 Claude Code 協作流程，把衝突搜尋邏輯轉工程條件 | 深入運用Claude Code於規格、資料分析與邏輯轉譯 |
| R04 熟悉規格撰寫、跨單位溝通與評估時程可行性 | 必要 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 規格完整且將需求處理週期大幅縮短近70% |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 釐清需求與系統分析後，以 Use Case 定義業務流程 | 符合 jd32 核心PM年資與交付要求 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責6.6萬家廠商招募系統 |
| HR03 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃與DBA/工程分工 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 交付週期、留存與媒合規模具明確基準 |
| HR05 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HR06 | supported | 從思維特助理PM、尚凡PM到1111企劃主任 | 職涯由C端0到1演進至B2B大型平台 |
| HR07 | supported | 入職初期跑過完整 Scrum；把衝突邏輯轉工程條件 | Scrum、原型、AI與英文協作皆有實例 |
| HR08 | supported | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 結構分明，重點指標與限制條件易讀 |
| HR09 | supported | 144 天後仍付費 91.4%，同期其餘廠商 89.2% | 主動標註觀察差異非因果，口徑可信 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd32 職責相容 |
| HR11 | supported | 雙北，可接受遠端或混合辦公｜錄取後三週可上班 | 地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 主責約 50 項大項功能規劃，掌握驗收與交付 | 證據鏈完整支持安排 jd32 面試 |
| HM01 | supported | KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO | 兼具0到1雙邊媒合與B2B企業系統經驗 |
| HM02 | supported | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 從客服訊號查明配對排序根因並實測競品 |
| HM03 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HM04 | supported | Peach 網頁付款占營收由 24% 至 80% 以上 | 具定價實驗、付費牆與網頁金流轉換實績 |
| HM05 | supported | 973 家活躍付費廠商，144 天後仍付費 91.4% | 交代期間、分母占比與非因果觀察限制 |
| HM06 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃、DBA取數與工程協作 |
| HM07 | supported | 求才端可存取大量求職者個資，冒用即有外洩風險 | 具重複信箱處理、離峰切換與防冒用閉環 |
| HM08 | supported | 把衝突的搜尋邏輯轉成工程條件；設每日配對上限 | 能將衝突邏輯轉工程條件，SQL由DBA代撈 |
| HM09 | supported | 約 50 項大項功能上線，另上線 111 項細項 | 主責50大項功能與6.6萬廠商系統，範圍相符 |
| HM10 | supported | 摘要與經歷清楚交代0到1、144天留存基準與非因果 | 摘要與條列經歷層次分明易檢索 |
| HM11 | supported | 改依職缺上線日排序；廠商也能自行切換排序（已上線） | 依客服回饋與還原原價結果修正產品規則 |
| HM12 | supported | 具KOOL 0到1、50項B2B交付、定價實驗與AI案例 | 具多個已上線案例，可於面試追問遷移細節 |
| HM13 | supported | 僅依 jd32 明文條件獨立取證判讀 | 僅依 jd32 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd32 |
| 2 | 具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗 |
| 3 | 已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 職缺明文條件全數符合；唯一需在面試確認的是候選人自傳期望「把更多心力放回產品策略」，與本職缺偏向「內部營運系統問題修正與優化」之期望對齊 | 你在 1111 將需求平均處理週期由 100.4 天降至 30.9 天並完成 1,726 張單的具體排程機制為何？如何運用 Claude Code 協助內部營運需求分析與規格拆解？ |
| 2 | 資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢 | 在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？ |
| 3 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd32 證明大型系統高密度交付與排程控管力
- 尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd32 展現完整 0 到 1 商業探索與雙邊媒合成果
- 1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd32 展現問題拆解、競品反推與嚴謹實驗能力

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定取數需求（資料表／欄位）交 DBA 撈取
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：職缺明文條件全數符合；唯一需在面試確認的是候選人自傳期望「把更多心力放回產品策略」，與本職缺偏向「內部營運系統問題修正與優化」之期望對齊
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄
- 位置：1111 全球華人經歷第 5 點
  - 原句：信件與即時通整合、搜尋結果頁改版（兩案皆開發中）
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9
  - 建議方向：面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：強

### 8. 未測試聲明
PDF 抽字：fail（本機實測 `resume-v10-twocol.pdf` 檢出粗體雙重疊字與雙欄讀序斷裂） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 Resume_AppendixA（jd34 SaaS 產品經理 / Product Owner｜91APP）｜第 10 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_AppendixA","job_id":"jd34","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd34-10","human_calibrated":false,"requirements":[{"id":"R01","text":"5年以上經驗（含2年以上產品管理經驗）","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"資深PM與B2B平台PO年資充足"},{"id":"R02","text":"金流、物流、會員、促購、優惠券、購買流程、訂單經驗","type":"required","status":"partial","evidence":["規劃 VIP 訂閱、點數付費牆；7／30／90 天方案與加贈"],"blocks_interview":false,"reason":"具金流、會員訂閱與加贈方案，缺電商實體物流與庫存訂單"},{"id":"R03","text":"產品管理和設計並與UX/RD/QA密切協作、製作介面","type":"required","status":"supported","evidence":["整理為 PRD 與 Axure Prototype；與 QA 制定 UAT"],"blocks_interview":false,"reason":"完整主導開發循環與UX/RD/QA協作"},{"id":"R04","text":"參與和運作Scrum團隊；定義目標並用數據分析效益","type":"required","status":"supported","evidence":["入職初期跑過完整 Scrum（一週一個 Sprint）"],"blocks_interview":false,"reason":"具完整Scrum經驗與留存率/定價實驗效益分析"},{"id":"R05","text":"從0到1開發經驗、支付生態、運用Gen AI加入產品案例","type":"preferred","status":"supported","evidence":["KOOL 從 0 到 1 探索商業模式；AI 功能已上線 3 項"],"blocks_interview":false,"reason":"同時具備KOOL 0到1市集媒合與3項GenAI上線案例"},{"id":"R06","text":"簡報募資提案經驗；200人以上軟體團隊2年以上經驗","type":"preferred","status":"unknown","evidence":["直接向組織副總匯報；未呈現研發團隊總人數與募資簡報"],"blocks_interview":false,"reason":"具高層匯報經驗，未載明軟體團隊是否逾200人"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["全站約有 6.6 萬家活躍付費廠商（2026/04/30）"],"missing":["過往為人力銀行與社交媒合平台，未直接經手零售電商 OMO 虛實融合場景"],"issue_ids":["I02"]},{"id":"role_evidence","rating":"足夠","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"missing":["缺乏零售電商之實體物流、門市庫存、購物車結帳與訂單管理模組經驗"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"需求平均處理週期由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"截至 09/29，完成 1,726／1,857 張需求與問題單","kinds":["output"]},{"quote":"973 家活躍付費廠商，144 天後仍付費 91.4%","kinds":["context","outcome"]},{"quote":"網紅檔案約 1.6 萬份，半年累計 8 萬多次報名","kinds":["outcome"]},{"quote":"廠商也能自行切換排序（已上線）","kinds":["decision","output"]},{"quote":"信件與即時通整合、搜尋改版（兩案皆開發中）","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"符合 jd34 核心PM年資與交付要求"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責6.6萬家廠商招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"application_note":"清楚界定個人規劃與DBA/工程分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"application_note":"交付週期、留存與媒合規模具明確基準"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與首登引導取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從思維特助理PM、尚凡PM到1111企劃主任"],"application_note":"職涯由C端0到1演進至B2B大型平台"},{"rule_id":"HR07","status":"supported","resume_evidence":["入職初期跑過完整 Scrum；把衝突邏輯轉工程條件"],"application_note":"Scrum、原型、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"application_note":"結構分明，重點指標與限制條件易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["144 天後仍付費 91.4%，同期其餘廠商 89.2%"],"application_note":"主動標註觀察差異非因果，口徑可信"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd34 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["雙北，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["主責約 50 項大項功能規劃，掌握驗收與交付"],"application_note":"證據鏈完整支持安排 jd34 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["Peach 網頁付款占營收由 24% 至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"supported","resume_evidence":["973 家活躍付費廠商，144 天後仍付費 91.4%"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["求才端可存取大量求職者個資，冒用即有外洩風險"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["把衝突的搜尋邏輯轉成工程條件；設每日配對上限"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能上線，另上線 111 項細項"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["摘要與經歷清楚交代0到1、144天留存基準與非因果"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["改依職缺上線日排序；廠商也能自行切換排序（已上線）"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、50項B2B交付、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"你在 1111 管理 6.6 萬家付費廠商平台與在 KOOL 設計雙邊媒合交易規則的經驗，如何遷移至 91APP 複雜的「全通路零售優惠券、購物車結帳與門市物流訂單」場景？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd34 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定取數需求（資料表／欄位）交 DBA 撈取","reason":"具備金流、訂閱會員與雙邊媒合市集經驗，但缺乏零售電商核心之「物流串接、門市 OMO 虛實融合、優惠券折抵規則與實體商品訂單管理」直接經驗","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄"},{"id":"I02","rule_id":"HM07","source_ids":[],"application_note":"開發中專案尚無上線後成效數據","context_limit":"1111 全球華人經歷第 5 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"信件與即時通整合、搜尋結果頁改版（兩案皆開發中）","reason":"兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9","suggestion":"面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗，經手 6 款產品","主責約 50 項大項功能規劃，掌握驗收與交付"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd34","具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗","已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績"],"key_gaps":["具備金流、訂閱會員與雙邊媒合市集經驗，但缺乏零售電商核心之「物流串接、門市 OMO 虛實融合、優惠券折抵規則與實體商品訂單管理」直接經驗","資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢","「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字"],"strengths":["1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd34 證明大型系統高密度交付與排程控管力","尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd34 展現完整 0 到 1 商業探索與雙邊媒合成果","1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd34 展現問題拆解、競品反推與嚴謹實驗能力"],"interview_questions":["你在 1111 管理 6.6 萬家付費廠商平台與在 KOOL 設計雙邊媒合交易規則的經驗，如何遷移至 91APP 複雜的「全通路零售優惠券、購物車結帳與門市物流訂單」場景？","在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？","「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例"],"spectrum":{"level":7,"uncertainty_levels":1,"basis":"針對 jd34 具備多個已實現案例、清楚取捨與嚴謹衡量支持面試，惟部分工具字面條件或次領域經驗待面試補驗"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"fail","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：7（±1）
- 一句話理由：具 B2B 平台 PO、Scrum 與 3 項 GenAI 上線實績，惟缺零售 OMO 實體物流與訂單經驗，支持約談。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 全站約有 6.6 萬家活躍付費廠商（2026/04/30） | 過往為人力銀行與社交媒合平台，未直接經手零售電商 OMO 虛實融合場景 |
| role_evidence | 足夠 | 近 10 年 PM 經驗，經手 6 款產品 | 缺乏零售電商之實體物流、門市庫存、購物車結帳與訂單管理模組經驗 |
| decision_depth | 強 | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 需求平均處理週期由 100.4 天降至 30.9 天 | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 5年以上經驗（含2年以上產品管理經驗） | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 資深PM與B2B平台PO年資充足 |
| R02 金流、物流、會員、促購、優惠券、購買流程、訂單經驗 | 必要 | partial | 規劃 VIP 訂閱、點數付費牆；7／30／90 天方案與加贈 | 具金流、會員訂閱與加贈方案，缺電商實體物流與庫存訂單 |
| R03 產品管理和設計並與UX/RD/QA密切協作、製作介面 | 必要 | supported | 整理為 PRD 與 Axure Prototype；與 QA 制定 UAT | 完整主導開發循環與UX/RD/QA協作 |
| R04 參與和運作Scrum團隊；定義目標並用數據分析效益 | 必要 | supported | 入職初期跑過完整 Scrum（一週一個 Sprint） | 具完整Scrum經驗與留存率/定價實驗效益分析 |
| R05 從0到1開發經驗、支付生態、運用Gen AI加入產品案例 | 加分 | supported | KOOL 從 0 到 1 探索商業模式；AI 功能已上線 3 項 | 同時具備KOOL 0到1市集媒合與3項GenAI上線案例 |
| R06 簡報募資提案經驗；200人以上軟體團隊2年以上經驗 | 加分 | unknown | 直接向組織副總匯報；未呈現研發團隊總人數與募資簡報 | 具高層匯報經驗，未載明軟體團隊是否逾200人 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 符合 jd34 核心PM年資與交付要求 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責6.6萬家廠商招募系統 |
| HR03 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃與DBA/工程分工 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 交付週期、留存與媒合規模具明確基準 |
| HR05 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HR06 | supported | 從思維特助理PM、尚凡PM到1111企劃主任 | 職涯由C端0到1演進至B2B大型平台 |
| HR07 | supported | 入職初期跑過完整 Scrum；把衝突邏輯轉工程條件 | Scrum、原型、AI與英文協作皆有實例 |
| HR08 | supported | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 結構分明，重點指標與限制條件易讀 |
| HR09 | supported | 144 天後仍付費 91.4%，同期其餘廠商 89.2% | 主動標註觀察差異非因果，口徑可信 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd34 職責相容 |
| HR11 | supported | 雙北，可接受遠端或混合辦公｜錄取後三週可上班 | 地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 主責約 50 項大項功能規劃，掌握驗收與交付 | 證據鏈完整支持安排 jd34 面試 |
| HM01 | supported | KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO | 兼具0到1雙邊媒合與B2B企業系統經驗 |
| HM02 | supported | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 從客服訊號查明配對排序根因並實測競品 |
| HM03 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HM04 | supported | Peach 網頁付款占營收由 24% 至 80% 以上 | 具定價實驗、付費牆與網頁金流轉換實績 |
| HM05 | supported | 973 家活躍付費廠商，144 天後仍付費 91.4% | 交代期間、分母占比與非因果觀察限制 |
| HM06 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃、DBA取數與工程協作 |
| HM07 | supported | 求才端可存取大量求職者個資，冒用即有外洩風險 | 具重複信箱處理、離峰切換與防冒用閉環 |
| HM08 | supported | 把衝突的搜尋邏輯轉成工程條件；設每日配對上限 | 能將衝突邏輯轉工程條件，SQL由DBA代撈 |
| HM09 | supported | 約 50 項大項功能上線，另上線 111 項細項 | 主責50大項功能與6.6萬廠商系統，範圍相符 |
| HM10 | supported | 摘要與經歷清楚交代0到1、144天留存基準與非因果 | 摘要與條列經歷層次分明易檢索 |
| HM11 | supported | 改依職缺上線日排序；廠商也能自行切換排序（已上線） | 依客服回饋與還原原價結果修正產品規則 |
| HM12 | supported | 具KOOL 0到1、50項B2B交付、定價實驗與AI案例 | 具多個已上線案例，可於面試追問遷移細節 |
| HM13 | supported | 僅依 jd34 明文條件獨立取證判讀 | 僅依 jd34 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd34 |
| 2 | 具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗 |
| 3 | 已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 具備金流、訂閱會員與雙邊媒合市集經驗，但缺乏零售電商核心之「物流串接、門市 OMO 虛實融合、優惠券折抵規則與實體商品訂單管理」直接經驗 | 你在 1111 管理 6.6 萬家付費廠商平台與在 KOOL 設計雙邊媒合交易規則的經驗，如何遷移至 91APP 複雜的「全通路零售優惠券、購物車結帳與門市物流訂單」場景？ |
| 2 | 資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢 | 在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？ |
| 3 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd34 證明大型系統高密度交付與排程控管力
- 尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd34 展現完整 0 到 1 商業探索與雙邊媒合成果
- 1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd34 展現問題拆解、競品反推與嚴謹實驗能力

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定取數需求（資料表／欄位）交 DBA 撈取
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：具備金流、訂閱會員與雙邊媒合市集經驗，但缺乏零售電商核心之「物流串接、門市 OMO 虛實融合、優惠券折抵規則與實體商品訂單管理」直接經驗
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄
- 位置：1111 全球華人經歷第 5 點
  - 原句：信件與即時通整合、搜尋結果頁改版（兩案皆開發中）
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9
  - 建議方向：面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：fail（本機實測 `resume-v10-twocol.pdf` 檢出粗體雙重疊字與雙欄讀序斷裂） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 Resume_AppendixA（jd36 全支付- Product Manager (內部系統、串接)）｜第 11 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_AppendixA","job_id":"jd36","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd36-11","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上相關工作經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"年資近10年且具豐富後台與系統改版經驗"},{"id":"R02","text":"能運用Axure撰寫規劃，透過Jira/Confluence管理","type":"required","status":"partial","evidence":["整理為 PRD 與 Axure Prototype；內部系統 ticket 追蹤"],"blocks_interview":false,"reason":"Axure原型與PRD經驗豐富，惟使用內部ticket系統非Jira"},{"id":"R03","text":"同步考慮技術可行性及系統架構關連影響","type":"required","status":"supported","evidence":["重新盤點既有資料、業務規則，同時推進新舊系統"],"blocks_interview":false,"reason":"親做系統分析、舊資料盤點與新舊系統漸進替換"},{"id":"R04","text":"熟悉API規格；與合作方確認需求並與法遵確認適法性","type":"required","status":"supported","evidence":["API 串接規劃；法務與稽核協作；與 CodaPay 協調串接"],"blocks_interview":false,"reason":"具API串接規劃、外部技術團隊對接與法務稽核協作"},{"id":"R05","text":"執行測試驗收、上線協調與內部教育訓練","type":"required","status":"supported","evidence":["與 QA 制定 UAT 驗收案例；全國客服封測後離峰切換上線"],"blocks_interview":false,"reason":"具UAT制定、全國客服封測訓練與離峰停機1.5小時切換"},{"id":"R06","text":"熟悉代理收付、電子支付領域知識；資管或資工畢或相關經驗","type":"preferred","status":"partial","evidence":["導入 CodaPay，依抽成、稅、手續費及撥款週期做實收試算"],"blocks_interview":false,"reason":"具金流撥款試算與軟體PM經驗，無銀行核心或電支清算後台"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["全站約有 6.6 萬家活躍付費廠商（2026/04/30）"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"足夠","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"missing":["未直接經手銀行端串接或專營電子支付機構內部清算後台；專案工具為內部 ticket 系統而非 Jira"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"需求平均處理週期由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"截至 09/29，完成 1,726／1,857 張需求與問題單","kinds":["output"]},{"quote":"973 家活躍付費廠商，144 天後仍付費 91.4%","kinds":["context","outcome"]},{"quote":"網紅檔案約 1.6 萬份，半年累計 8 萬多次報名","kinds":["outcome"]},{"quote":"廠商也能自行切換排序（已上線）","kinds":["decision","output"]},{"quote":"信件與即時通整合、搜尋改版（兩案皆開發中）","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"符合 jd36 核心PM年資與交付要求"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責6.6萬家廠商招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"application_note":"清楚界定個人規劃與DBA/工程分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"application_note":"交付週期、留存與媒合規模具明確基準"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與首登引導取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從思維特助理PM、尚凡PM到1111企劃主任"],"application_note":"職涯由C端0到1演進至B2B大型平台"},{"rule_id":"HR07","status":"supported","resume_evidence":["入職初期跑過完整 Scrum；把衝突邏輯轉工程條件"],"application_note":"Scrum、原型、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"application_note":"結構分明，重點指標與限制條件易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["144 天後仍付費 91.4%，同期其餘廠商 89.2%"],"application_note":"主動標註觀察差異非因果，口徑可信"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd36 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["雙北，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["主責約 50 項大項功能規劃，掌握驗收與交付"],"application_note":"證據鏈完整支持安排 jd36 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["Peach 網頁付款占營收由 24% 至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"supported","resume_evidence":["973 家活躍付費廠商，144 天後仍付費 91.4%"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["求才端可存取大量求職者個資，冒用即有外洩風險"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["把衝突的搜尋邏輯轉成工程條件；設每日配對上限"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能上線，另上線 111 項細項"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["摘要與經歷清楚交代0到1、144天留存基準與非因果"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["改依職缺上線日排序；廠商也能自行切換排序（已上線）"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、50項B2B交付、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"過去在進行 CodaPay 跨國金流 API 串接與 1111 新舊系統漸進替換時，你如何定義 API 錯誤碼處理、資料同步機制與帳務異常排查流程？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd36 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定取數需求（資料表／欄位）交 DBA 撈取","reason":"具備第三方金流 CodaPay 串接與撥款實收試算經驗，但未直接經手銀行端專線串接或電子支付機構內部代理收付清算系統；工具未直接點名 Jira","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄"},{"id":"I02","rule_id":"HM07","source_ids":[],"application_note":"開發中專案尚無上線後成效數據","context_limit":"1111 全球華人經歷第 5 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"信件與即時通整合、搜尋結果頁改版（兩案皆開發中）","reason":"兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9","suggestion":"面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗，經手 6 款產品","主責約 50 項大項功能規劃，掌握驗收與交付"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd36","具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗","已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績"],"key_gaps":["具備第三方金流 CodaPay 串接與撥款實收試算經驗，但未直接經手銀行端專線串接或電子支付機構內部代理收付清算系統；工具未直接點名 Jira","資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢","「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字"],"strengths":["1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd36 證明大型系統高密度交付與排程控管力","尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd36 展現完整 0 到 1 商業探索與雙邊媒合成果","1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd36 展現問題拆解、競品反推與嚴謹實驗能力"],"interview_questions":["過去在進行 CodaPay 跨國金流 API 串接與 1111 新舊系統漸進替換時，你如何定義 API 錯誤碼處理、資料同步機制與帳務異常排查流程？","在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？","「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd36 具備多個已實現案例、清楚取捨與嚴謹衡量支持面試，惟部分工具字面條件或次領域經驗待面試補驗"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"fail","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「以系統分析重整規劃...整理為 PRD 與 Axure Prototype」且具跨國金流串接經驗，支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 全站約有 6.6 萬家活躍付費廠商（2026/04/30） | 無關鍵缺口，可於面試深化 |
| role_evidence | 足夠 | 近 10 年 PM 經驗，經手 6 款產品 | 未直接經手銀行端串接或專營電子支付機構內部清算後台；專案工具為內部 ticket 系統而非 Jira |
| decision_depth | 強 | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 需求平均處理週期由 100.4 天降至 30.9 天 | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 3年以上相關工作經驗 | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 年資近10年且具豐富後台與系統改版經驗 |
| R02 能運用Axure撰寫規劃，透過Jira/Confluence管理 | 必要 | partial | 整理為 PRD 與 Axure Prototype；內部系統 ticket 追蹤 | Axure原型與PRD經驗豐富，惟使用內部ticket系統非Jira |
| R03 同步考慮技術可行性及系統架構關連影響 | 必要 | supported | 重新盤點既有資料、業務規則，同時推進新舊系統 | 親做系統分析、舊資料盤點與新舊系統漸進替換 |
| R04 熟悉API規格；與合作方確認需求並與法遵確認適法性 | 必要 | supported | API 串接規劃；法務與稽核協作；與 CodaPay 協調串接 | 具API串接規劃、外部技術團隊對接與法務稽核協作 |
| R05 執行測試驗收、上線協調與內部教育訓練 | 必要 | supported | 與 QA 制定 UAT 驗收案例；全國客服封測後離峰切換上線 | 具UAT制定、全國客服封測訓練與離峰停機1.5小時切換 |
| R06 熟悉代理收付、電子支付領域知識；資管或資工畢或相關經驗 | 加分 | partial | 導入 CodaPay，依抽成、稅、手續費及撥款週期做實收試算 | 具金流撥款試算與軟體PM經驗，無銀行核心或電支清算後台 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 符合 jd36 核心PM年資與交付要求 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責6.6萬家廠商招募系統 |
| HR03 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃與DBA/工程分工 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 交付週期、留存與媒合規模具明確基準 |
| HR05 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HR06 | supported | 從思維特助理PM、尚凡PM到1111企劃主任 | 職涯由C端0到1演進至B2B大型平台 |
| HR07 | supported | 入職初期跑過完整 Scrum；把衝突邏輯轉工程條件 | Scrum、原型、AI與英文協作皆有實例 |
| HR08 | supported | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 結構分明，重點指標與限制條件易讀 |
| HR09 | supported | 144 天後仍付費 91.4%，同期其餘廠商 89.2% | 主動標註觀察差異非因果，口徑可信 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd36 職責相容 |
| HR11 | supported | 雙北，可接受遠端或混合辦公｜錄取後三週可上班 | 地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 主責約 50 項大項功能規劃，掌握驗收與交付 | 證據鏈完整支持安排 jd36 面試 |
| HM01 | supported | KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO | 兼具0到1雙邊媒合與B2B企業系統經驗 |
| HM02 | supported | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 從客服訊號查明配對排序根因並實測競品 |
| HM03 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HM04 | supported | Peach 網頁付款占營收由 24% 至 80% 以上 | 具定價實驗、付費牆與網頁金流轉換實績 |
| HM05 | supported | 973 家活躍付費廠商，144 天後仍付費 91.4% | 交代期間、分母占比與非因果觀察限制 |
| HM06 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃、DBA取數與工程協作 |
| HM07 | supported | 求才端可存取大量求職者個資，冒用即有外洩風險 | 具重複信箱處理、離峰切換與防冒用閉環 |
| HM08 | supported | 把衝突的搜尋邏輯轉成工程條件；設每日配對上限 | 能將衝突邏輯轉工程條件，SQL由DBA代撈 |
| HM09 | supported | 約 50 項大項功能上線，另上線 111 項細項 | 主責50大項功能與6.6萬廠商系統，範圍相符 |
| HM10 | supported | 摘要與經歷清楚交代0到1、144天留存基準與非因果 | 摘要與條列經歷層次分明易檢索 |
| HM11 | supported | 改依職缺上線日排序；廠商也能自行切換排序（已上線） | 依客服回饋與還原原價結果修正產品規則 |
| HM12 | supported | 具KOOL 0到1、50項B2B交付、定價實驗與AI案例 | 具多個已上線案例，可於面試追問遷移細節 |
| HM13 | supported | 僅依 jd36 明文條件獨立取證判讀 | 僅依 jd36 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd36 |
| 2 | 具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗 |
| 3 | 已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 具備第三方金流 CodaPay 串接與撥款實收試算經驗，但未直接經手銀行端專線串接或電子支付機構內部代理收付清算系統；工具未直接點名 Jira | 過去在進行 CodaPay 跨國金流 API 串接與 1111 新舊系統漸進替換時，你如何定義 API 錯誤碼處理、資料同步機制與帳務異常排查流程？ |
| 2 | 資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢 | 在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？ |
| 3 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd36 證明大型系統高密度交付與排程控管力
- 尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd36 展現完整 0 到 1 商業探索與雙邊媒合成果
- 1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd36 展現問題拆解、競品反推與嚴謹實驗能力

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定取數需求（資料表／欄位）交 DBA 撈取
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：具備第三方金流 CodaPay 串接與撥款實收試算經驗，但未直接經手銀行端專線串接或電子支付機構內部代理收付清算系統；工具未直接點名 Jira
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄
- 位置：1111 全球華人經歷第 5 點
  - 原句：信件與即時通整合、搜尋結果頁改版（兩案皆開發中）
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9
  - 建議方向：面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：fail（本機實測 `resume-v10-twocol.pdf` 檢出粗體雙重疊字與雙欄讀序斷裂） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 Resume_AppendixA（jd40 【PMC】軟體產品經理 (PM / TPM)｜QuickClick快一點）｜第 12 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_AppendixA","job_id":"jd40","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd40-12","human_calibrated":false,"requirements":[{"id":"R01","text":"5年以上軟體產品、技術產品或技術專案管理經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗；主責約 50 項大項功能規劃"],"blocks_interview":false,"reason":"年資近10年且大型系統改版與交付經驗扎實"},{"id":"R02","text":"參與產品從需求規劃到上線交付的完整流程","type":"required","status":"supported","evidence":["從需求釐清、系統分析到 PRD、原型、UAT 與上線計畫"],"blocks_interview":false,"reason":"完整主導端到端產品開發與上線交付週期"},{"id":"R03","text":"能理解API、資料流程及系統串接邏輯","type":"required","status":"supported","evidence":["API 串接規劃、舊系統資料盤點；擬定取數的資料表與欄位"],"blocks_interview":false,"reason":"具系統分析、API串接與資料庫欄位結構理解"},{"id":"R04","text":"具備需求拆解、優先順序判斷、跨團隊溝通及風險管理","type":"required","status":"supported","evidence":["信件與即時通整合排在其他新功能之前；離峰切換上線"],"blocks_interview":false,"reason":"具體展現工單痛點優先排序、重複信箱處理與資安風控"},{"id":"R05","text":"KA客戶/客製化或NRE專案經驗；支付/餐飲/零售/SaaS經驗","type":"preferred","status":"partial","evidence":["完成 1,726／1,857 張需求與問題單；規劃轉向網頁付款"],"blocks_interview":false,"reason":"具B2B廠商需求單管線與支付經驗，無餐飲POS與NRE合約報價"},{"id":"R06","text":"基本SQL查詢或資料分析能力；高階利害關係人溝通","type":"preferred","status":"partial","evidence":["直接向組織副總匯報；擬定取數資料表與欄位交 DBA 撈取"],"blocks_interview":false,"reason":"具高層匯報與試算表留存分析，SQL由DBA代撈"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["全站約有 6.6 萬家活躍付費廠商（2026/04/30）"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"足夠","evidence":["近 10 年 PM 經驗；主責約 50 項大項功能規劃"],"missing":["未呈現 KA 大客戶 NRE 客製化合約專案管理與餐飲 POS 領域經驗；SQL 由 DBA 代撈"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"需求平均處理週期由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"截至 09/29，完成 1,726／1,857 張需求與問題單","kinds":["output"]},{"quote":"973 家活躍付費廠商，144 天後仍付費 91.4%","kinds":["context","outcome"]},{"quote":"網紅檔案約 1.6 萬份，半年累計 8 萬多次報名","kinds":["outcome"]},{"quote":"廠商也能自行切換排序（已上線）","kinds":["decision","output"]},{"quote":"信件與即時通整合、搜尋改版（兩案皆開發中）","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗；主責約 50 項大項功能規劃"],"application_note":"符合 jd40 核心PM年資與交付要求"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責6.6萬家廠商招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"application_note":"清楚界定個人規劃與DBA/工程分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"application_note":"交付週期、留存與媒合規模具明確基準"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與首登引導取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從思維特助理PM、尚凡PM到1111企劃主任"],"application_note":"職涯由C端0到1演進至B2B大型平台"},{"rule_id":"HR07","status":"supported","resume_evidence":["入職初期跑過完整 Scrum；把衝突邏輯轉工程條件"],"application_note":"Scrum、原型、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"application_note":"結構分明，重點指標與限制條件易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["144 天後仍付費 91.4%，同期其餘廠商 89.2%"],"application_note":"主動標註觀察差異非因果，口徑可信"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd40 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["雙北，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["主責約 50 項大項功能規劃，掌握驗收與交付"],"application_note":"證據鏈完整支持安排 jd40 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["Peach 網頁付款占營收由 24% 至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"supported","resume_evidence":["973 家活躍付費廠商，144 天後仍付費 91.4%"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["求才端可存取大量求職者個資，冒用即有外洩風險"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["把衝突的搜尋邏輯轉成工程條件；設每日配對上限"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能上線，另上線 111 項細項"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["摘要與經歷清楚交代0到1、144天留存基準與非因果"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["改依職缺上線日排序；廠商也能自行切換排序（已上線）"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、50項B2B交付、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"在 1111 面對業務單位為大型付費廠商提出的客製化需求時，你如何評估是否納入標準 Roadmap、如何控管開發範圍變更，以及如何與工程團隊敲定技術方案？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd40 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定取數需求（資料表／欄位）交 DBA 撈取","reason":"具備高吞吐 B2B 需求單管理（1,857 張單）與支付串接經驗，但未明文呈現餐飲門市 POS 系統或 KA 大客戶 NRE 客製化專案範疇控管紀錄","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄"},{"id":"I02","rule_id":"HM07","source_ids":[],"application_note":"開發中專案尚無上線後成效數據","context_limit":"1111 全球華人經歷第 5 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"信件與即時通整合、搜尋結果頁改版（兩案皆開發中）","reason":"兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9","suggestion":"面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗；主責約 50 項大項功能規劃","主責約 50 項大項功能規劃，掌握驗收與交付"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd40","具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗","已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績"],"key_gaps":["具備高吞吐 B2B 需求單管理（1,857 張單）與支付串接經驗，但未明文呈現餐飲門市 POS 系統或 KA 大客戶 NRE 客製化專案範疇控管紀錄","資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢","「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字"],"strengths":["1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd40 證明大型系統高密度交付與排程控管力","尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd40 展現完整 0 到 1 商業探索與雙邊媒合成果","1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd40 展現問題拆解、競品反推與嚴謹實驗能力"],"interview_questions":["在 1111 面對業務單位為大型付費廠商提出的客製化需求時，你如何評估是否納入標準 Roadmap、如何控管開發範圍變更，以及如何與工程團隊敲定技術方案？","在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？","「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd40 具備多個已實現案例、清楚取捨與嚴謹衡量支持面試，惟部分工具字面條件或次領域經驗待面試補驗"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"fail","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「主責約 50 項大項功能規劃，掌握驗收與交付時程」且具系統分析與金流經驗，支持約談。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 全站約有 6.6 萬家活躍付費廠商（2026/04/30） | 無關鍵缺口，可於面試深化 |
| role_evidence | 足夠 | 近 10 年 PM 經驗；主責約 50 項大項功能規劃 | 未呈現 KA 大客戶 NRE 客製化合約專案管理與餐飲 POS 領域經驗；SQL 由 DBA 代撈 |
| decision_depth | 強 | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 需求平均處理週期由 100.4 天降至 30.9 天 | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 5年以上軟體產品、技術產品或技術專案管理經驗 | 必要 | supported | 近 10 年 PM 經驗；主責約 50 項大項功能規劃 | 年資近10年且大型系統改版與交付經驗扎實 |
| R02 參與產品從需求規劃到上線交付的完整流程 | 必要 | supported | 從需求釐清、系統分析到 PRD、原型、UAT 與上線計畫 | 完整主導端到端產品開發與上線交付週期 |
| R03 能理解API、資料流程及系統串接邏輯 | 必要 | supported | API 串接規劃、舊系統資料盤點；擬定取數的資料表與欄位 | 具系統分析、API串接與資料庫欄位結構理解 |
| R04 具備需求拆解、優先順序判斷、跨團隊溝通及風險管理 | 必要 | supported | 信件與即時通整合排在其他新功能之前；離峰切換上線 | 具體展現工單痛點優先排序、重複信箱處理與資安風控 |
| R05 KA客戶/客製化或NRE專案經驗；支付/餐飲/零售/SaaS經驗 | 加分 | partial | 完成 1,726／1,857 張需求與問題單；規劃轉向網頁付款 | 具B2B廠商需求單管線與支付經驗，無餐飲POS與NRE合約報價 |
| R06 基本SQL查詢或資料分析能力；高階利害關係人溝通 | 加分 | partial | 直接向組織副總匯報；擬定取數資料表與欄位交 DBA 撈取 | 具高層匯報與試算表留存分析，SQL由DBA代撈 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗；主責約 50 項大項功能規劃 | 符合 jd40 核心PM年資與交付要求 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責6.6萬家廠商招募系統 |
| HR03 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃與DBA/工程分工 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 交付週期、留存與媒合規模具明確基準 |
| HR05 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HR06 | supported | 從思維特助理PM、尚凡PM到1111企劃主任 | 職涯由C端0到1演進至B2B大型平台 |
| HR07 | supported | 入職初期跑過完整 Scrum；把衝突邏輯轉工程條件 | Scrum、原型、AI與英文協作皆有實例 |
| HR08 | supported | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 結構分明，重點指標與限制條件易讀 |
| HR09 | supported | 144 天後仍付費 91.4%，同期其餘廠商 89.2% | 主動標註觀察差異非因果，口徑可信 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd40 職責相容 |
| HR11 | supported | 雙北，可接受遠端或混合辦公｜錄取後三週可上班 | 地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 主責約 50 項大項功能規劃，掌握驗收與交付 | 證據鏈完整支持安排 jd40 面試 |
| HM01 | supported | KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO | 兼具0到1雙邊媒合與B2B企業系統經驗 |
| HM02 | supported | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 從客服訊號查明配對排序根因並實測競品 |
| HM03 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HM04 | supported | Peach 網頁付款占營收由 24% 至 80% 以上 | 具定價實驗、付費牆與網頁金流轉換實績 |
| HM05 | supported | 973 家活躍付費廠商，144 天後仍付費 91.4% | 交代期間、分母占比與非因果觀察限制 |
| HM06 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃、DBA取數與工程協作 |
| HM07 | supported | 求才端可存取大量求職者個資，冒用即有外洩風險 | 具重複信箱處理、離峰切換與防冒用閉環 |
| HM08 | supported | 把衝突的搜尋邏輯轉成工程條件；設每日配對上限 | 能將衝突邏輯轉工程條件，SQL由DBA代撈 |
| HM09 | supported | 約 50 項大項功能上線，另上線 111 項細項 | 主責50大項功能與6.6萬廠商系統，範圍相符 |
| HM10 | supported | 摘要與經歷清楚交代0到1、144天留存基準與非因果 | 摘要與條列經歷層次分明易檢索 |
| HM11 | supported | 改依職缺上線日排序；廠商也能自行切換排序（已上線） | 依客服回饋與還原原價結果修正產品規則 |
| HM12 | supported | 具KOOL 0到1、50項B2B交付、定價實驗與AI案例 | 具多個已上線案例，可於面試追問遷移細節 |
| HM13 | supported | 僅依 jd40 明文條件獨立取證判讀 | 僅依 jd40 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd40 |
| 2 | 具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗 |
| 3 | 已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 具備高吞吐 B2B 需求單管理（1,857 張單）與支付串接經驗，但未明文呈現餐飲門市 POS 系統或 KA 大客戶 NRE 客製化專案範疇控管紀錄 | 在 1111 面對業務單位為大型付費廠商提出的客製化需求時，你如何評估是否納入標準 Roadmap、如何控管開發範圍變更，以及如何與工程團隊敲定技術方案？ |
| 2 | 資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢 | 在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？ |
| 3 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd40 證明大型系統高密度交付與排程控管力
- 尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd40 展現完整 0 到 1 商業探索與雙邊媒合成果
- 1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd40 展現問題拆解、競品反推與嚴謹實驗能力

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定取數需求（資料表／欄位）交 DBA 撈取
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：具備高吞吐 B2B 需求單管理（1,857 張單）與支付串接經驗，但未明文呈現餐飲門市 POS 系統或 KA 大客戶 NRE 客製化專案範疇控管紀錄
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄
- 位置：1111 全球華人經歷第 5 點
  - 原句：信件與即時通整合、搜尋結果頁改版（兩案皆開發中）
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9
  - 建議方向：面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：fail（本機實測 `resume-v10-twocol.pdf` 檢出粗體雙重疊字與雙欄讀序斷裂） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 Resume_AppendixA（jd43 Product Manager (Messenger & OA)｜LINE Taiwan）｜第 13 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_AppendixA","job_id":"jd43","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd43-13","human_calibrated":false,"requirements":[{"id":"R01","text":"5年以上網路或科技產業PM經驗，推動概念到上線優化","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品；約 50 項大項功能上線"],"blocks_interview":false,"reason":"10年網路與軟體平台PM經驗，完整覆蓋0到1與迭代"},{"id":"R02","text":"聚焦帳號安全、防詐騙專案及訊息體驗","type":"required","status":"supported","evidence":["上線簽章驗證...未再出現同類帳號冒用；信件與即時通整合"],"blocks_interview":false,"reason":"直接具備帳號防冒用簽章驗證上線閉環與即時通整合規劃"},{"id":"R03","text":"跨職能（含資安、法務、客服）與跨國團隊合作經驗","type":"required","status":"supported","evidence":["與 CodaPay 新加坡技術團隊協調；法務與稽核協作"],"blocks_interview":false,"reason":"具跨國技術團隊、7國在地化及法務稽核客服跨職能協作"},{"id":"R04","text":"運用問卷、訪談、A/B test与行為分析做出數據決策","type":"required","status":"supported","evidence":["使用者訪談與問卷、競品實測、GA4、世代分析、對照組實驗"],"blocks_interview":false,"reason":"研究與量化實驗方法論完整且有跨國定價實驗佐證"},{"id":"R05","text":"熟悉Confluence、Jira、Figma、Codex等工具；英文流利","type":"required","status":"partial","evidence":["英文 TOEIC 980；Figma、內部專案系統（ticket追蹤）"],"blocks_interview":false,"reason":"英文流利且熟Figma與Claude Code，未點名Jira/Confluence"},{"id":"R06","text":"具AI產品開發或整合經驗；日文或韓文能力尤佳","type":"preferred","status":"partial","evidence":["AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才"],"blocks_interview":false,"reason":"具3項AI功能上線實績；曾推日韓在地化但未列日韓文能力"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["全站約有 6.6 萬家活躍付費廠商（2026/04/30）"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"強","evidence":["近 10 年 PM 經驗，經手 6 款產品；約 50 項大項功能上線"],"missing":["「信件與即時通整合」目前尚在開發中（未上線無成效數字，依硬性規則 2 不列入 Level 9）；未呈現日韓文與 Jira 字樣"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"需求平均處理週期由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"截至 09/29，完成 1,726／1,857 張需求與問題單","kinds":["output"]},{"quote":"973 家活躍付費廠商，144 天後仍付費 91.4%","kinds":["context","outcome"]},{"quote":"網紅檔案約 1.6 萬份，半年累計 8 萬多次報名","kinds":["outcome"]},{"quote":"廠商也能自行切換排序（已上線）","kinds":["decision","output"]},{"quote":"信件與即時通整合、搜尋改版（兩案皆開發中）","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品；約 50 項大項功能上線"],"application_note":"符合 jd43 核心PM年資與交付要求"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責6.6萬家廠商招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"application_note":"清楚界定個人規劃與DBA/工程分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"application_note":"交付週期、留存與媒合規模具明確基準"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與首登引導取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從思維特助理PM、尚凡PM到1111企劃主任"],"application_note":"職涯由C端0到1演進至B2B大型平台"},{"rule_id":"HR07","status":"supported","resume_evidence":["入職初期跑過完整 Scrum；把衝突邏輯轉工程條件"],"application_note":"Scrum、原型、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"application_note":"結構分明，重點指標與限制條件易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["144 天後仍付費 91.4%，同期其餘廠商 89.2%"],"application_note":"主動標註觀察差異非因果，口徑可信"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd43 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["雙北，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["主責約 50 項大項功能規劃，掌握驗收與交付"],"application_note":"證據鏈完整支持安排 jd43 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["Peach 網頁付款占營收由 24% 至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"supported","resume_evidence":["973 家活躍付費廠商，144 天後仍付費 91.4%"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["求才端可存取大量求職者個資，冒用即有外洩風險"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["把衝突的搜尋邏輯轉成工程條件；設每日配對上限"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能上線，另上線 111 項細項"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["摘要與經歷清楚交代0到1、144天留存基準與非因果"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["改依職缺上線日排序；廠商也能自行切換排序（已上線）"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、50項B2B交付、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"請分享「信件與即時通整合」目前的設計架構與預計觀察的核心指標；另外在 2026/04 處置廠商帳號遭冒用並上線簽章驗證時，如何平衡安全性與正常用戶的登入順暢度？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd43 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定取數需求（資料表／欄位）交 DBA 撈取","reason":"訊息體驗相關之「信件與即時通整合」目前為開發中（依規準進行中案例不計入已實現結果與 Level 9）；且未直接點名 Confluence/Jira 與日韓語能力","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄"},{"id":"I02","rule_id":"HM07","source_ids":[],"application_note":"開發中專案尚無上線後成效數據","context_limit":"1111 全球華人經歷第 5 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"信件與即時通整合、搜尋結果頁改版（兩案皆開發中）","reason":"兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9","suggestion":"面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）"}],"decision":{"recommendation":"interview","evidence":["近 10 年 PM 經驗，經手 6 款產品；約 50 項大項功能上線","主責約 50 項大項功能規劃，掌握驗收與交付"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd43","具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗","已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績"],"key_gaps":["訊息體驗相關之「信件與即時通整合」目前為開發中（依規準進行中案例不計入已實現結果與 Level 9）；且未直接點名 Confluence/Jira 與日韓語能力","資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢","「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字"],"strengths":["1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd43 證明大型系統高密度交付與排程控管力","尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd43 展現完整 0 到 1 商業探索與雙邊媒合成果","1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd43 展現問題拆解、競品反推與嚴謹實驗能力"],"interview_questions":["請分享「信件與即時通整合」目前的設計架構與預計觀察的核心指標；另外在 2026/04 處置廠商帳號遭冒用並上線簽章驗證時，如何平衡安全性與正常用戶的登入順暢度？","在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？","「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd43 具備多個已實現案例、清楚取捨與嚴謹衡量支持面試，惟部分工具字面條件或次領域經驗待面試補驗"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"fail","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「於 2026/04/17 上線簽章驗證」且具跨國協作與「信件與即時通整合」規劃，契合度高。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 全站約有 6.6 萬家活躍付費廠商（2026/04/30） | 無關鍵缺口，可於面試深化 |
| role_evidence | 強 | 近 10 年 PM 經驗，經手 6 款產品；約 50 項大項功能上線 | 「信件與即時通整合」目前尚在開發中（未上線無成效數字，依硬性規則 2 不列入 Level 9）；未呈現日韓文與 Jira 字樣 |
| decision_depth | 強 | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 需求平均處理週期由 100.4 天降至 30.9 天 | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 5年以上網路或科技產業PM經驗，推動概念到上線優化 | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品；約 50 項大項功能上線 | 10年網路與軟體平台PM經驗，完整覆蓋0到1與迭代 |
| R02 聚焦帳號安全、防詐騙專案及訊息體驗 | 必要 | supported | 上線簽章驗證...未再出現同類帳號冒用；信件與即時通整合 | 直接具備帳號防冒用簽章驗證上線閉環與即時通整合規劃 |
| R03 跨職能（含資安、法務、客服）與跨國團隊合作經驗 | 必要 | supported | 與 CodaPay 新加坡技術團隊協調；法務與稽核協作 | 具跨國技術團隊、7國在地化及法務稽核客服跨職能協作 |
| R04 運用問卷、訪談、A/B test与行為分析做出數據決策 | 必要 | supported | 使用者訪談與問卷、競品實測、GA4、世代分析、對照組實驗 | 研究與量化實驗方法論完整且有跨國定價實驗佐證 |
| R05 熟悉Confluence、Jira、Figma、Codex等工具；英文流利 | 必要 | partial | 英文 TOEIC 980；Figma、內部專案系統（ticket追蹤） | 英文流利且熟Figma與Claude Code，未點名Jira/Confluence |
| R06 具AI產品開發或整合經驗；日文或韓文能力尤佳 | 加分 | partial | AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才 | 具3項AI功能上線實績；曾推日韓在地化但未列日韓文能力 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品；約 50 項大項功能上線 | 符合 jd43 核心PM年資與交付要求 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責6.6萬家廠商招募系統 |
| HR03 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃與DBA/工程分工 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 交付週期、留存與媒合規模具明確基準 |
| HR05 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HR06 | supported | 從思維特助理PM、尚凡PM到1111企劃主任 | 職涯由C端0到1演進至B2B大型平台 |
| HR07 | supported | 入職初期跑過完整 Scrum；把衝突邏輯轉工程條件 | Scrum、原型、AI與英文協作皆有實例 |
| HR08 | supported | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 結構分明，重點指標與限制條件易讀 |
| HR09 | supported | 144 天後仍付費 91.4%，同期其餘廠商 89.2% | 主動標註觀察差異非因果，口徑可信 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd43 職責相容 |
| HR11 | supported | 雙北，可接受遠端或混合辦公｜錄取後三週可上班 | 地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 主責約 50 項大項功能規劃，掌握驗收與交付 | 證據鏈完整支持安排 jd43 面試 |
| HM01 | supported | KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO | 兼具0到1雙邊媒合與B2B企業系統經驗 |
| HM02 | supported | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 從客服訊號查明配對排序根因並實測競品 |
| HM03 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HM04 | supported | Peach 網頁付款占營收由 24% 至 80% 以上 | 具定價實驗、付費牆與網頁金流轉換實績 |
| HM05 | supported | 973 家活躍付費廠商，144 天後仍付費 91.4% | 交代期間、分母占比與非因果觀察限制 |
| HM06 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃、DBA取數與工程協作 |
| HM07 | supported | 求才端可存取大量求職者個資，冒用即有外洩風險 | 具重複信箱處理、離峰切換與防冒用閉環 |
| HM08 | supported | 把衝突的搜尋邏輯轉成工程條件；設每日配對上限 | 能將衝突邏輯轉工程條件，SQL由DBA代撈 |
| HM09 | supported | 約 50 項大項功能上線，另上線 111 項細項 | 主責50大項功能與6.6萬廠商系統，範圍相符 |
| HM10 | supported | 摘要與經歷清楚交代0到1、144天留存基準與非因果 | 摘要與條列經歷層次分明易檢索 |
| HM11 | supported | 改依職缺上線日排序；廠商也能自行切換排序（已上線） | 依客服回饋與還原原價結果修正產品規則 |
| HM12 | supported | 具KOOL 0到1、50項B2B交付、定價實驗與AI案例 | 具多個已上線案例，可於面試追問遷移細節 |
| HM13 | supported | 僅依 jd43 明文條件獨立取證判讀 | 僅依 jd43 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd43 |
| 2 | 具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗 |
| 3 | 已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 訊息體驗相關之「信件與即時通整合」目前為開發中（依規準進行中案例不計入已實現結果與 Level 9）；且未直接點名 Confluence/Jira 與日韓語能力 | 請分享「信件與即時通整合」目前的設計架構與預計觀察的核心指標；另外在 2026/04 處置廠商帳號遭冒用並上線簽章驗證時，如何平衡安全性與正常用戶的登入順暢度？ |
| 2 | 資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢 | 在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？ |
| 3 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd43 證明大型系統高密度交付與排程控管力
- 尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd43 展現完整 0 到 1 商業探索與雙邊媒合成果
- 1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd43 展現問題拆解、競品反推與嚴謹實驗能力

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定取數需求（資料表／欄位）交 DBA 撈取
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：訊息體驗相關之「信件與即時通整合」目前為開發中（依規準進行中案例不計入已實現結果與 Level 9）；且未直接點名 Confluence/Jira 與日韓語能力
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄
- 位置：1111 全球華人經歷第 5 點
  - 原句：信件與即時通整合、搜尋結果頁改版（兩案皆開發中）
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9
  - 建議方向：面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：fail（本機實測 `resume-v10-twocol.pdf` 檢出粗體雙重疊字與雙欄讀序斷裂） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 Resume_AppendixA（jd44 [Music] Senior Product Planner｜KKBOX (KKCompany)）｜第 14 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_AppendixA","job_id":"jd44","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd44-14","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上網路PM經驗，具策略思考與0到1及持續迭代能力","type":"required","status":"supported","evidence":["KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名"],"blocks_interview":false,"reason":"兼具KOOL從0到1共創商業模式與1111大型平台持續迭代"},{"id":"R02","text":"跨國跨職能協作，與外部廠商溝通共創產品概念","type":"required","status":"supported","evidence":["SweetRing 在地化涵蓋 7 個市場；與 CodaPay 新加坡串接"],"blocks_interview":false,"reason":"具跨7國市場協調、跨國金流串接與B2B外部廠商需求共創"},{"id":"R03","text":"數據驅動決策，熟悉行為分析、A/B測試及關鍵指標","type":"required","status":"supported","evidence":["定價實驗採原價、iOS 降價、還原原價三階段（各期 21 天）"],"blocks_interview":false,"reason":"具嚴謹跨國定價實驗、世代留存分析與付費轉換追蹤"},{"id":"R04","text":"市場與競品分析能力；提升參與度與留存率","type":"required","status":"supported","evidence":["實測競品反推規則，改依職缺上線日排序（已上線）"],"blocks_interview":false,"reason":"具體展現實測競品反推演算法規則並優化配對留存"},{"id":"R05","text":"優異的英文溝通及寫作能力","type":"required","status":"supported","evidence":["英文 TOEIC 980、TOEFL iBT 93；以英文分派翻譯任務"],"blocks_interview":false,"reason":"高分英檢、美國交換一年半且具英文跨國協作實務"},{"id":"R06","text":"具音樂/內容/社群/娛樂或AI相關產品經驗；日文能力","type":"preferred","status":"supported","evidence":["AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才"],"blocks_interview":false,"reason":"具訂閱制社交媒合與3項AI功能上線經驗，日文未呈現"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["全站約有 6.6 萬家活躍付費廠商（2026/04/30）"],"missing":["過往訂閱制為社交與網紅媒合 App，未直接經手音樂串流與版權曲庫領域；未呈現日文能力"],"issue_ids":["I02"]},{"id":"role_evidence","rating":"強","evidence":["KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名"],"missing":[],"issue_ids":[]},{"id":"decision_depth","rating":"強","evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"需求平均處理週期由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"截至 09/29，完成 1,726／1,857 張需求與問題單","kinds":["output"]},{"quote":"973 家活躍付費廠商，144 天後仍付費 91.4%","kinds":["context","outcome"]},{"quote":"網紅檔案約 1.6 萬份，半年累計 8 萬多次報名","kinds":["outcome"]},{"quote":"廠商也能自行切換排序（已上線）","kinds":["decision","output"]},{"quote":"信件與即時通整合、搜尋改版（兩案皆開發中）","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名"],"application_note":"符合 jd44 核心PM年資與交付要求"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責6.6萬家廠商招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"application_note":"清楚界定個人規劃與DBA/工程分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"application_note":"交付週期、留存與媒合規模具明確基準"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與首登引導取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從思維特助理PM、尚凡PM到1111企劃主任"],"application_note":"職涯由C端0到1演進至B2B大型平台"},{"rule_id":"HR07","status":"supported","resume_evidence":["入職初期跑過完整 Scrum；把衝突邏輯轉工程條件"],"application_note":"Scrum、原型、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"application_note":"結構分明，重點指標與限制條件易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["144 天後仍付費 91.4%，同期其餘廠商 89.2%"],"application_note":"主動標註觀察差異非因果，口徑可信"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd44 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["雙北，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["主責約 50 項大項功能規劃，掌握驗收與交付"],"application_note":"證據鏈完整支持安排 jd44 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["Peach 網頁付款占營收由 24% 至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"supported","resume_evidence":["973 家活躍付費廠商，144 天後仍付費 91.4%"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["求才端可存取大量求職者個資，冒用即有外洩風險"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["把衝突的搜尋邏輯轉成工程條件；設每日配對上限"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能上線，另上線 111 項細項"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["摘要與經歷清楚交代0到1、144天留存基準與非因果"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["改依職缺上線日排序；廠商也能自行切換排序（已上線）"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、50項B2B交付、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"你在 KOOL 從 0 到 1 探索「公司行號尋找微型網紅合作（累積 1.6 萬網紅、半年 8 萬次報名）」的雙邊媒合與 VIP 付費牆經驗，如何轉化為音樂串流平台的藝人粉絲互動與 AI 個人化產品提案？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd44 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定取數需求（資料表／欄位）交 DBA 撈取","reason":"過往 C 端訂閱與媒合經驗集中於社交及微型網紅平台，尚未直接經手音樂串流與粉絲娛樂產業；加分項之日文能力未呈現","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄"},{"id":"I02","rule_id":"HM07","source_ids":[],"application_note":"開發中專案尚無上線後成效數據","context_limit":"1111 全球華人經歷第 5 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"信件與即時通整合、搜尋結果頁改版（兩案皆開發中）","reason":"兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9","suggestion":"面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）"}],"decision":{"recommendation":"interview","evidence":["KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名","主責約 50 項大項功能規劃，掌握驗收與交付"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd44","具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗","已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績"],"key_gaps":["過往 C 端訂閱與媒合經驗集中於社交及微型網紅平台，尚未直接經手音樂串流與粉絲娛樂產業；加分項之日文能力未呈現","資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢","「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字"],"strengths":["1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd44 證明大型系統高密度交付與排程控管力","尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd44 展現完整 0 到 1 商業探索與雙邊媒合成果","1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd44 展現問題拆解、競品反推與嚴謹實驗能力"],"interview_questions":["你在 KOOL 從 0 到 1 探索「公司行號尋找微型網紅合作（累積 1.6 萬網紅、半年 8 萬次報名）」的雙邊媒合與 VIP 付費牆經驗，如何轉化為音樂串流平台的藝人粉絲互動與 AI 個人化產品提案？","在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？","「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd44 具備多個已實現案例、清楚取捨與嚴謹衡量支持面試，惟部分工具字面條件或次領域經驗待面試補驗"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"fail","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名」且具跨國定價實驗與 3 項 AI 上線。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 全站約有 6.6 萬家活躍付費廠商（2026/04/30） | 過往訂閱制為社交與網紅媒合 App，未直接經手音樂串流與版權曲庫領域；未呈現日文能力 |
| role_evidence | 強 | KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名 | 無關鍵缺口，可於面試深化 |
| decision_depth | 強 | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 需求平均處理週期由 100.4 天降至 30.9 天 | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 3年以上網路PM經驗，具策略思考與0到1及持續迭代能力 | 必要 | supported | KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名 | 兼具KOOL從0到1共創商業模式與1111大型平台持續迭代 |
| R02 跨國跨職能協作，與外部廠商溝通共創產品概念 | 必要 | supported | SweetRing 在地化涵蓋 7 個市場；與 CodaPay 新加坡串接 | 具跨7國市場協調、跨國金流串接與B2B外部廠商需求共創 |
| R03 數據驅動決策，熟悉行為分析、A/B測試及關鍵指標 | 必要 | supported | 定價實驗採原價、iOS 降價、還原原價三階段（各期 21 天） | 具嚴謹跨國定價實驗、世代留存分析與付費轉換追蹤 |
| R04 市場與競品分析能力；提升參與度與留存率 | 必要 | supported | 實測競品反推規則，改依職缺上線日排序（已上線） | 具體展現實測競品反推演算法規則並優化配對留存 |
| R05 優異的英文溝通及寫作能力 | 必要 | supported | 英文 TOEIC 980、TOEFL iBT 93；以英文分派翻譯任務 | 高分英檢、美國交換一年半且具英文跨國協作實務 |
| R06 具音樂/內容/社群/娛樂或AI相關產品經驗；日文能力 | 加分 | supported | AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才 | 具訂閱制社交媒合與3項AI功能上線經驗，日文未呈現 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名 | 符合 jd44 核心PM年資與交付要求 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責6.6萬家廠商招募系統 |
| HR03 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃與DBA/工程分工 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 交付週期、留存與媒合規模具明確基準 |
| HR05 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HR06 | supported | 從思維特助理PM、尚凡PM到1111企劃主任 | 職涯由C端0到1演進至B2B大型平台 |
| HR07 | supported | 入職初期跑過完整 Scrum；把衝突邏輯轉工程條件 | Scrum、原型、AI與英文協作皆有實例 |
| HR08 | supported | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 結構分明，重點指標與限制條件易讀 |
| HR09 | supported | 144 天後仍付費 91.4%，同期其餘廠商 89.2% | 主動標註觀察差異非因果，口徑可信 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd44 職責相容 |
| HR11 | supported | 雙北，可接受遠端或混合辦公｜錄取後三週可上班 | 地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 主責約 50 項大項功能規劃，掌握驗收與交付 | 證據鏈完整支持安排 jd44 面試 |
| HM01 | supported | KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO | 兼具0到1雙邊媒合與B2B企業系統經驗 |
| HM02 | supported | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 從客服訊號查明配對排序根因並實測競品 |
| HM03 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HM04 | supported | Peach 網頁付款占營收由 24% 至 80% 以上 | 具定價實驗、付費牆與網頁金流轉換實績 |
| HM05 | supported | 973 家活躍付費廠商，144 天後仍付費 91.4% | 交代期間、分母占比與非因果觀察限制 |
| HM06 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃、DBA取數與工程協作 |
| HM07 | supported | 求才端可存取大量求職者個資，冒用即有外洩風險 | 具重複信箱處理、離峰切換與防冒用閉環 |
| HM08 | supported | 把衝突的搜尋邏輯轉成工程條件；設每日配對上限 | 能將衝突邏輯轉工程條件，SQL由DBA代撈 |
| HM09 | supported | 約 50 項大項功能上線，另上線 111 項細項 | 主責50大項功能與6.6萬廠商系統，範圍相符 |
| HM10 | supported | 摘要與經歷清楚交代0到1、144天留存基準與非因果 | 摘要與條列經歷層次分明易檢索 |
| HM11 | supported | 改依職缺上線日排序；廠商也能自行切換排序（已上線） | 依客服回饋與還原原價結果修正產品規則 |
| HM12 | supported | 具KOOL 0到1、50項B2B交付、定價實驗與AI案例 | 具多個已上線案例，可於面試追問遷移細節 |
| HM13 | supported | 僅依 jd44 明文條件獨立取證判讀 | 僅依 jd44 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd44 |
| 2 | 具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗 |
| 3 | 已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 過往 C 端訂閱與媒合經驗集中於社交及微型網紅平台，尚未直接經手音樂串流與粉絲娛樂產業；加分項之日文能力未呈現 | 你在 KOOL 從 0 到 1 探索「公司行號尋找微型網紅合作（累積 1.6 萬網紅、半年 8 萬次報名）」的雙邊媒合與 VIP 付費牆經驗，如何轉化為音樂串流平台的藝人粉絲互動與 AI 個人化產品提案？ |
| 2 | 資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢 | 在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？ |
| 3 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd44 證明大型系統高密度交付與排程控管力
- 尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd44 展現完整 0 到 1 商業探索與雙邊媒合成果
- 1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd44 展現問題拆解、競品反推與嚴謹實驗能力

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定取數需求（資料表／欄位）交 DBA 撈取
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：過往 C 端訂閱與媒合經驗集中於社交及微型網紅平台，尚未直接經手音樂串流與粉絲娛樂產業；加分項之日文能力未呈現
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄
- 位置：1111 全球華人經歷第 5 點
  - 原句：信件與即時通整合、搜尋結果頁改版（兩案皆開發中）
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9
  - 建議方向：面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：fail（本機實測 `resume-v10-twocol.pdf` 檢出粗體雙重疊字與雙欄讀序斷裂） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 Resume_AppendixA（jd47 產品經理｜Product Manager｜USPACE）｜第 15 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_AppendixA","job_id":"jd47","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-jd47-15","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上Software PM，具0到1探索驗證上線與成熟產品迭代經歷","type":"required","status":"supported","evidence":["KOOL 從 0 到 1 探索商業模式；約 50 項大項功能上線"],"blocks_interview":false,"reason":"同時具備KOOL 0到1完整週期與1111成熟產品50項大功能迭代"},{"id":"R02","text":"能寫清楚的規格文件（PRD、流程圖、資料結構）","type":"required","status":"supported","evidence":["流程圖／循序圖、PRD；擬定取數的資料表與欄位"],"blocks_interview":false,"reason":"具PRD、循序圖與擬定資料庫資料表及欄位能力"},{"id":"R03","text":"理解API、JSON與基本SQL","type":"required","status":"partial","evidence":["API 串接規劃、資料庫知識；擬定資料表欄位交 DBA"],"blocks_interview":false,"reason":"具API與資料表欄位規劃，未明列JSON與自寫SQL"},{"id":"R04","text":"規劃並執行產品教育訓練，負責上線前測試與驗收","type":"required","status":"supported","evidence":["與 QA 制定 UAT 驗收案例；全國客服封測後離峰切換上線"],"blocks_interview":false,"reason":"具UAT制定、全國客服封測說明與上線驗證統籌實績"},{"id":"R05","text":"支付或FinTech經驗；AI/LLM工具規格撰寫與分析","type":"preferred","status":"supported","evidence":["自建 Claude Code 協作流程，把衝突搜尋邏輯轉工程條件"],"blocks_interview":false,"reason":"具CodaPay/網頁金流與Claude Code規格分析深度實作"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["全站約有 6.6 萬家活躍付費廠商（2026/04/30）"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"足夠","evidence":["KOOL 從 0 到 1 探索商業模式；約 50 項大項功能上線"],"missing":["必備條件中之 JSON 未明文呈現，且資料庫查詢為擬定資料表欄位交 DBA 撈取而非自寫 SQL"],"issue_ids":["I01"]},{"id":"decision_depth","rating":"強","evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"missing":[],"issue_ids":[]}],"results":[{"quote":"需求平均處理週期由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"截至 09/29，完成 1,726／1,857 張需求與問題單","kinds":["output"]},{"quote":"973 家活躍付費廠商，144 天後仍付費 91.4%","kinds":["context","outcome"]},{"quote":"網紅檔案約 1.6 萬份，半年累計 8 萬多次報名","kinds":["outcome"]},{"quote":"廠商也能自行切換排序（已上線）","kinds":["decision","output"]},{"quote":"信件與即時通整合、搜尋改版（兩案皆開發中）","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["KOOL 從 0 到 1 探索商業模式；約 50 項大項功能上線"],"application_note":"符合 jd47 核心PM年資與交付要求"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 10 個需求單位"],"application_note":"近4年主責6.6萬家廠商招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"application_note":"清楚界定個人規劃與DBA/工程分工"},{"rule_id":"HR04","status":"supported","resume_evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"application_note":"交付週期、留存與媒合規模具明確基準"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"application_note":"具體呈現功能優先序與首登引導取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從思維特助理PM、尚凡PM到1111企劃主任"],"application_note":"職涯由C端0到1演進至B2B大型平台"},{"rule_id":"HR07","status":"supported","resume_evidence":["入職初期跑過完整 Scrum；把衝突邏輯轉工程條件"],"application_note":"Scrum、原型、AI與英文協作皆有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["摘要與經歷結構分明，時序、母體基準與非因果清晰"],"application_note":"結構分明，重點指標與限制條件易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["144 天後仍付費 91.4%，同期其餘廠商 89.2%"],"application_note":"主動標註觀察差異非因果，口徑可信"},{"rule_id":"HR10","status":"supported","resume_evidence":["結合過去在訂閱、定價與企業流程上的經驗"],"application_note":"轉職方向與 jd47 職責相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["雙北，可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"地點、遠端彈性與到職日無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["主責約 50 項大項功能規劃，掌握驗收與交付"],"application_note":"證據鏈完整支持安排 jd47 面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["查出根因是名單依履歷修改日排序；廠商能切換排序"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁改版排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["Peach 網頁付款占營收由 24% 至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"supported","resume_evidence":["973 家活躍付費廠商，144 天後仍付費 91.4%"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位，交 DBA 撈取"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["求才端可存取大量求職者個資，冒用即有外洩風險"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"partial","resume_evidence":["把衝突的搜尋邏輯轉成工程條件；設每日配對上限"],"evidence_type":"output","source_ids":[],"interview_question":"請說明如何將衝突搜尋邏輯轉成工程條件，以及是否具基礎 SQL/JSON 實作經驗？"},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["約 50 項大項功能上線，另上線 111 項細項"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["摘要與經歷清楚交代0到1、144天留存基準與非因果"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["改依職缺上線日排序；廠商也能自行切換排序（已上線）"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["具KOOL 0到1、50項B2B交付、定價實驗與AI案例"],"evidence_type":"context","source_ids":[],"interview_question":"在推動 KOOL 0 到 1 上線與 1111 招募系統三階段改版時，你如何向內部業務、客服與外部合作夥伴進行產品教育訓練與 Go-To-Market 對齊？"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["僅依 jd47 明文條件獨立取證判讀"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"職缺特定工具或次領域經驗待面試確認","context_limit":"專業技能與工作經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"擬定取數需求（資料表／欄位）交 DBA 撈取","reason":"必備條件要求理解 API、JSON 與基本 SQL，履歷雖載明 API 串接規劃與擬定資料表欄位交 DBA 撈取，但未呈現 JSON 與親自撰寫 SQL 查詢紀錄","suggestion":"若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄"},{"id":"I02","rule_id":"HM07","source_ids":[],"application_note":"開發中專案尚無上線後成效數據","context_limit":"1111 全球華人經歷第 5 點","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"信件與即時通整合、搜尋結果頁改版（兩案皆開發中）","reason":"兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9","suggestion":"面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）"}],"decision":{"recommendation":"interview","evidence":["KOOL 從 0 到 1 探索商業模式；約 50 項大項功能上線","主責約 50 項大項功能規劃，掌握驗收與交付"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd47","具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗","已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績"],"key_gaps":["必備條件要求理解 API、JSON 與基本 SQL，履歷雖載明 API 串接規劃與擬定資料表欄位交 DBA 撈取，但未呈現 JSON 與親自撰寫 SQL 查詢紀錄","資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢","「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字"],"strengths":["1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd47 證明大型系統高密度交付與排程控管力","尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd47 展現完整 0 到 1 商業探索與雙邊媒合成果","1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd47 展現問題拆解、競品反推與嚴謹實驗能力"],"interview_questions":["在推動 KOOL 0 到 1 上線與 1111 招募系統三階段改版時，你如何向內部業務、客服與外部合作夥伴進行產品教育訓練與 Go-To-Market 對齊？","在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？","「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？"],"editorial_appendix":["若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"針對 jd47 具備多個已實現案例、清楚取捨與嚴謹衡量支持面試，惟部分工具字面條件或次領域經驗待面試補驗"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"fail","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「KOOL 從 0 到 1 探索商業模式」結合「約 50 項大項功能上線」與全國客服封測，支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 全站約有 6.6 萬家活躍付費廠商（2026/04/30） | 無關鍵缺口，可於面試深化 |
| role_evidence | 足夠 | KOOL 從 0 到 1 探索商業模式；約 50 項大項功能上線 | 必備條件中之 JSON 未明文呈現，且資料庫查詢為擬定資料表欄位交 DBA 撈取而非自寫 SQL |
| decision_depth | 強 | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 強 | 需求平均處理週期由 100.4 天降至 30.9 天 | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 3年以上Software PM，具0到1探索驗證上線與成熟產品迭代經歷 | 必要 | supported | KOOL 從 0 到 1 探索商業模式；約 50 項大項功能上線 | 同時具備KOOL 0到1完整週期與1111成熟產品50項大功能迭代 |
| R02 能寫清楚的規格文件（PRD、流程圖、資料結構） | 必要 | supported | 流程圖／循序圖、PRD；擬定取數的資料表與欄位 | 具PRD、循序圖與擬定資料庫資料表及欄位能力 |
| R03 理解API、JSON與基本SQL | 必要 | partial | API 串接規劃、資料庫知識；擬定資料表欄位交 DBA | 具API與資料表欄位規劃，未明列JSON與自寫SQL |
| R04 規劃並執行產品教育訓練，負責上線前測試與驗收 | 必要 | supported | 與 QA 制定 UAT 驗收案例；全國客服封測後離峰切換上線 | 具UAT制定、全國客服封測說明與上線驗證統籌實績 |
| R05 支付或FinTech經驗；AI/LLM工具規格撰寫與分析 | 加分 | supported | 自建 Claude Code 協作流程，把衝突搜尋邏輯轉工程條件 | 具CodaPay/網頁金流與Claude Code規格分析深度實作 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | KOOL 從 0 到 1 探索商業模式；約 50 項大項功能上線 | 符合 jd47 核心PM年資與交付要求 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 10 個需求單位 | 近4年主責6.6萬家廠商招募系統 |
| HR03 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃與DBA/工程分工 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 交付週期、留存與媒合規模具明確基準 |
| HR05 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HR06 | supported | 從思維特助理PM、尚凡PM到1111企劃主任 | 職涯由C端0到1演進至B2B大型平台 |
| HR07 | supported | 入職初期跑過完整 Scrum；把衝突邏輯轉工程條件 | Scrum、原型、AI與英文協作皆有實例 |
| HR08 | supported | 摘要與經歷結構分明，時序、母體基準與非因果清晰 | 結構分明，重點指標與限制條件易讀 |
| HR09 | supported | 144 天後仍付費 91.4%，同期其餘廠商 89.2% | 主動標註觀察差異非因果，口徑可信 |
| HR10 | supported | 結合過去在訂閱、定價與企業流程上的經驗 | 轉職方向與 jd47 職責相容 |
| HR11 | supported | 雙北，可接受遠端或混合辦公｜錄取後三週可上班 | 地點、遠端彈性與到職日無已知衝突 |
| HR12 | supported | 主責約 50 項大項功能規劃，掌握驗收與交付 | 證據鏈完整支持安排 jd47 面試 |
| HM01 | supported | KOOL 從 0 到 1 探索商業模式；企業端招募系統 PO | 兼具0到1雙邊媒合與B2B企業系統經驗 |
| HM02 | supported | 查出根因是名單依履歷修改日排序；廠商能切換排序 | 從客服訊號查明配對排序根因並實測競品 |
| HM03 | supported | 搜尋結果頁改版排在新功能職缺健檢之前 | 具體呈現功能優先序與首登引導取捨 |
| HM04 | supported | Peach 網頁付款占營收由 24% 至 80% 以上 | 具定價實驗、付費牆與網頁金流轉換實績 |
| HM05 | supported | 973 家活躍付費廠商，144 天後仍付費 91.4% | 交代期間、分母占比與非因果觀察限制 |
| HM06 | supported | 由我擬定取數的資料表與欄位，交 DBA 撈取 | 清楚界定個人規劃、DBA取數與工程協作 |
| HM07 | supported | 求才端可存取大量求職者個資，冒用即有外洩風險 | 具重複信箱處理、離峰切換與防冒用閉環 |
| HM08 | partial | 把衝突的搜尋邏輯轉成工程條件；設每日配對上限 | 能將衝突邏輯轉工程條件，SQL由DBA代撈 |
| HM09 | supported | 約 50 項大項功能上線，另上線 111 項細項 | 主責50大項功能與6.6萬廠商系統，範圍相符 |
| HM10 | supported | 摘要與經歷清楚交代0到1、144天留存基準與非因果 | 摘要與條列經歷層次分明易檢索 |
| HM11 | supported | 改依職缺上線日排序；廠商也能自行切換排序（已上線） | 依客服回饋與還原原價結果修正產品規則 |
| HM12 | supported | 具KOOL 0到1、50項B2B交付、定價實驗與AI案例 | 具多個已上線案例，可於面試追問遷移細節 |
| HM13 | supported | 僅依 jd47 明文條件獨立取證判讀 | 僅依 jd47 明文條件獨立取證判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 兼具1111大型B2B平台（6.6萬廠商、50大項功能上線）與KOOL從0到1雙邊媒合（8萬次報名）實績，契合 jd47 |
| 2 | 具備完整Scrum（一週一Sprint）與Kanban實務、三階段定價實驗、網頁金流（24%→80%）與CodaPay跨國串接經驗 |
| 3 | 已上線3項生成式AI功能並自建Claude Code流程（把衝突搜尋邏輯轉成工程條件），且具帳號防冒用簽章驗證實績 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 必備條件要求理解 API、JSON 與基本 SQL，履歷雖載明 API 串接規劃與擬定資料表欄位交 DBA 撈取，但未呈現 JSON 與親自撰寫 SQL 查詢紀錄 | 在推動 KOOL 0 到 1 上線與 1111 招募系統三階段改版時，你如何向內部業務、客服與外部合作夥伴進行產品教育訓練與 Go-To-Market 對齊？ |
| 2 | 資料庫查詢採「本人擬定資料表與欄位交 DBA 撈取，以 Google Sheet/Excel 分析」模式，未明載獨立手寫 SQL 查詢 | 在 1111 擬定取數的資料表與欄位交 DBA 撈取時，你如何確認資料表關聯與欄位定義？是否曾自行撰寫基礎 SQL 驗證？ |
| 3 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前仍在開發中，尚無上線後量化成效數字 | 「信件與即時通整合」與「搜尋結果頁改版」兩案目前開發進度為何？預計上線後用哪些量化指標驗證成功？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜約 50 項大項功能上線；處理週期由 100.4 天降至 30.9 天｜對 jd47 證明大型系統高密度交付與排程控管力
- 尚凡經歷｜KOOL 從 0 到 1 探索商業模式...半年累計 8 萬多次報名｜對 jd47 展現完整 0 到 1 商業探索與雙邊媒合成果
- 1111與尚凡｜查出根因是名單依履歷修改日排序（已上線）；三階段定價實驗｜對 jd47 展現問題拆解、競品反推與嚴謹實驗能力

**可改進（≤5 點）**：
- 位置：專業技能與工作經歷
  - 原句：擬定取數需求（資料表／欄位）交 DBA 撈取
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：必備條件要求理解 API、JSON 與基本 SQL，履歷雖載明 API 串接規劃與擬定資料表欄位交 DBA 撈取，但未呈現 JSON 與親自撰寫 SQL 查詢紀錄
  - 建議方向：若有親自撰寫基礎 SQL（如 SELECT/JOIN）、閱讀 API JSON 規格或使用過對應工具之實例，建議直接補入技能欄
- 位置：1111 全球華人經歷第 5 點
  - 原句：信件與即時通整合、搜尋結果頁改版（兩案皆開發中）
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：兩案目前僅能支持優先序取捨（decision），尚無上線後成效數字（outcome），依規準不能單獨支撐 Level 9
  - 建議方向：面試時主動說明兩案預計上線時程、驗收條件及上線後擬追蹤之核心指標（如工單下降率或搜尋轉換率）

**編輯附件**（語氣、用詞微調；不影響判斷）：若具備基礎 SQL 語法（SELECT/JOIN）或閱讀 API JSON 結構經驗，建議於技能欄明確補註一筆實例

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：fail（本機實測 `resume-v10-twocol.pdf` 檢出粗體雙重疊字與雙欄讀序斷裂） ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 附錄 B：執行檢查清單核對（對應套件 §10）
- [x] 單份審查 15 次，只放一份職缺條件獨立判讀，已記錄 `model_id: gemini-4-argon`（並於 §7 誠實揭露單一環境執行限制）
- [x] JSON 單行、欄位齊全、`human_calibrated=false`、`ai_authorship.probability=null`
- [x] 沒有做任何版本比較，也沒有引用其他對話的分數
- [x] 沒有把頁數、學歷、空窗、任職長短、關鍵字個數當缺失
- [x] 沒有拿 A 職缺的條件去扣 B 職缺；Level 9 以上（`jd11`、`jd31`、`jd32`）皆有寫出可追溯的已上線量測與責任，開發中案例不撐起 Level 9
- [x] HR 12 題＋HM 13 題每次都列全；約談理由 ≤3、關鍵缺口 ≤3
- [x] ATS 五塊分開，沒有「ATS 分數」
- [x] 總報告依 §8 固定格式，附上 15 份原始 JSON 與完整單份審查評語（附錄 A）
