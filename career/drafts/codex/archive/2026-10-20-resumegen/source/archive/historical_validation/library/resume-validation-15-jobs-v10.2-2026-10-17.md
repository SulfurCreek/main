# 履歷驗證報告：單份履歷 × 15 職缺｜2026-10-17｜model_id: unknown｜human_calibration: not_run

## 1. 結論（≤6 行，先講答案）

- 招聘決定分布：interview 14／clarify_first 1／not_matched 0／insufficient_info 0；唯一先釐清的是 jd20。
- Level 分布：7 × 3（jd14、jd20、jd30）；8 × 12；各 ±1，未計平均、總分或錄取率。
- 最適合投遞的 5 份（不排序）：jd11 招募系統與 AI 可轉 HRIS；jd31 企業流程與整合相近；jd32 系統分析及驗收對位；jd40 產品與技術交付兼具；jd09 B2B 需求、規格及迭代對位。
- 最可能被卡的 3 份：jd20 的 B2B/B2G 年資、近母語英文及獨立查詢待先釐清；jd14 的 Growth 責任範圍與 Firebase 待核；jd30 的 JSON／基本 SQL 與完整新產品驗證鏈待核。後兩份仍為 interview，沒有據此判定不符合。
- 最值得補的是成果的計算口徑與限制、本人決策邊界、可展示的工具／規格工作樣本；不是增加術語或把協作改寫成個人實作。
- 本次為模型結構化判讀；15 個新審查上下文、無真人校準、無真實 ATS 匯入。PDF 本機抽字有跨欄／跨頁讀序風險，與內容評等分開。

## 2. 職缺矩陣（每列一份職缺，不加總）

六維度順序固定：定位／職缺證據／決策／成果／權責／可讀性。「足」＝足夠、「待」＝待補。Level 僅概括該職缺證據，不用來跨職缺排名。下列「決定性條件」包括已支持與待核對條件，不等同淘汰條件。

| 職缺 | 決定／Level | 六維度（定位／職缺／決策／成果／權責／可讀） | 決定性條件（≤20 字） | 約談理由第一名（≤20 字） |
| :-- | :-- | :-- | :-- | :-- |
| jd03｜Pi 錢包 | interview／8 | 足／足／強／足／足／強 | 支付與API可轉移 | 付款渠道與訂閱案例 |
| jd09｜beBit TECH | interview／8 | 強／足／強／足／強／足 | B2B需求到交付 | 企業需求與完整交付 |
| jd11｜Pacston | interview／8 | 強／足／強／足／強／足 | HR系統與AI可轉移 | 招募系統流程與權限 |
| jd14｜MyVideo | interview／7 | 足／足／足／待／足／強 | Growth漏斗與Firebase待核 | 訂閱及定價實驗 |
| jd20｜Gogolook | clarify_first／7 | 足／待／強／足／強／足 | 年資／英文／獨立查詢待核 | B2B交付與帳號風險 |
| jd26｜全支付・專案 | interview／8 | 足／足／強／足／強／強 | 支付交付／指定工具待核 | 付款串接與驗收交付 |
| jd30｜USPACE・資深 | interview／7 | 足／足／強／足／強／足 | JSON／SQL及驗證鏈待核 | 系統規格與定價實驗 |
| jd31｜NUEIP | interview／8 | 強／足／強／足／強／足 | 企業流程／客訪售前待核 | 權限與跨系統規劃 |
| jd32｜104・內部系統 | interview／8 | 足／強／強／足／強／足 | SA與驗收直接對位 | 規格到驗收鏈條 |
| jd34｜91APP | interview／8 | 足／足／強／足／強／足 | 金流會員／OMO廣度待核 | 付款與完整產品交付 |
| jd36｜全支付・內部串接 | interview／8 | 足／足／強／足／強／強 | API／指定工具待核 | 系統交付與金流串接 |
| jd40｜QuickClick | interview／8 | 強／足／強／足／強／足 | 產品與技術交付對位 | 相容性與跨隊交付 |
| jd43｜LINE | interview／8 | 足／足／強／足／強／足 | 安全／訊息與區域協作 | 帳號風險與驗證調整 |
| jd44｜KKBOX | interview／8 | 足／足／強／足／強／足 | 內容訂閱／留存策略待核 | 訂閱與跨國協作 |
| jd47｜USPACE・PM | interview／8 | 強／足／強／足／足／足 | 完整產品／JSON SQL待核 | 規格、付費與交付 |



### 六維度與資深能力分布（只列次數）

| 維度 | 強 | 足夠 | 待補 | 未呈現 | 不適用 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| positioning | 5 | 10 | 0 | 0 | 0 |
| role_evidence | 1 | 13 | 1 | 0 | 0 |
| decision_depth | 14 | 1 | 0 | 0 | 0 |
| outcome_quality | 0 | 14 | 1 | 0 | 0 |
| ownership | 12 | 3 | 0 | 0 | 0 |
| readability | 4 | 11 | 0 | 0 | 0 |



| 資深能力分布 | 強 | 足夠 | 待補 | 未呈現 |
| :-- | :-- | :-- | :-- | :-- |
| delivery | 15 | 0 | 0 | 0 |
| po_coordination | 15 | 0 | 0 | 0 |
| direction_resources | 0 | 11 | 4 | 0 |



## 3. 職缺分群（最多 5 群）

| 群組 | 職缺代號 | 共同優勢 | 共同卡關／追問 |
| :-- | :-- | :-- | :-- |
| 企業流程、HR 與 MarTech | jd09、jd11、jd31、jd32 | 企業招募流程、資料權限、規格驗收、需求整合 | 各領域產品情境、直接客訪／售前或內部營運角色；部分需英文文件及 AI 工作樣本 |
| 支付與商務平台 | jd03、jd26、jd34、jd36 | CodaPay、付款渠道、訂閱點數、商業試算及交付 | 銀行／支付法遵、API 規格、指定工具；零售職另核物流訂單與 OMO，不跨群套用 |
| 完整軟體產品與系統交付 | jd30、jd40、jd47 | 新舊並行、資料關聯、規格到上線、商業實驗 | USPACE 需核 JSON／基本 SQL 與完整新產品驗證鏈；QuickClick 需核 KA／NRE 與技術契約深度 |
| 消費成長與內容產品 | jd14、jd44 | 訂閱付費、定價實驗、內容／社交產品、跨國協作 | Activation／Retention 與實驗限制；Firebase 僅 jd14，音樂情境及英文口寫另核 jd44 |
| 安全、防詐與區域協作 | jd20、jd43 | 帳號冒用處理、驗證調整、跨團隊交付；jd43 另有訊息整合決策線索 | 冒用監測來源及權責；jd20 的特定年資與語言門檻不套用 jd43，總部協商要求亦各別看待 |

## 4. 跨職缺重複出現的缺口（≥3 份才列；≤6 項）

計數以每份審查的 issues、key_gaps 為依據，相關 requirements 作對照；同一主題在同一職缺只算一次。這是整理優先度，重複出現不代表判斷已經真人驗證。不同主題不加總，數量也不作能力分數。

| 缺口 | 出現職缺數（明列範圍） | 影響哪類職缺 | 履歷原句（≤40 字） | 需要候選人補什麼事實 |
| :-- | :-- | :-- | :-- | :-- |
| 成果母體、可比性與歸因限制 | 15（全部） | 所有職缺的結果查核；Growth 尤需追問 | 「平均處理時間由 100.4 天降至 30.9 天」 | 兩季件數、計時起訖、結案／未結案納入、案件組成及清積案影響；實驗另補樣本與同期活動 |
| API 規格、資料與獨立取數的本人深度 | 7（jd03、20、30、31、36、40、47） | 支付、系統整合、技術產品 | 「API 串接規劃」 | 展示欄位、狀態、錯誤與驗收；只在 JD 要求時核 SQL／JSON，區分本人操作與 DBA 工作 |
| 研究到方案／新產品驗證的完整鏈 | 7（jd09、11、14、30、31、43、47） | 客訪、成長、Regional PM、新產品 | 「使用者訪談與問卷」 | 誰的哪一步、本人主持或分析、洞察如何改方案；新產品補驗證與一次上線後迭代，不把方法清單當閉環 |
| 方向、資源與決策核准邊界 | 7（jd09、30、32、34、43、44、47） | 資深、策略、跨總部或多專案角色 | 「公司決定採新舊並行」 | 一次本人提案、替代方案、資源衝突、可決定事項及最終核准者；不以主管會議或人數代替證據 |
| 指定工具或 AI 工作流程的實際產物 | 7（jd11、14、20、26、30、32、36） | 有指定工具、AI 編排／原型／營運分析要求者 | 「以 Claude Code 建立協作流程與共用 skill」 | 按各 JD 分別提供已使用工具、輸入輸出、人工驗收與操作；Firebase、Jira／Confluence、快速原型不是同一能力 |
| 英文產品口寫的工作樣本 | 3（jd11、20、44） | 有英文文件、近母語或優異口寫要求者 | 「並以英文進行跨國協作」 | 去識別英文需求文件、英文決策說明或需求訪談；考試與協作已有支持，仍不自動證成各職缺的特定門檻 |

單一重大事實矛盾：本次 15 份審查未提出候選人的 blocking 事實矛盾，也沒有 required＋contradicted 的條件。此結論僅限文本內部，並非外部查證。jd20 清楚可辨的企業招募系統經歷為 2022/08 起，其他平台的 B2B 性質與期間尚未完整呈現，故是待核對，不能直接算已滿五年，也不能推定一定不足。

### 重複出現的 HR／HM 題（僅展開 partial／unknown／contradicted ≥3 份）

| 題 | 不足／未知職缺數 | 狀態分布 | 職缺 | 面試意義 |
| :-- | :-- | :-- | :-- | :-- |
| HR01 | 3 | partial 3 | jd20、jd31、jd34 | 核心資格與子領域分別核對，不把部分對位當不符。 |
| HR04 | 15 | partial 15 | 全部15份 | 結果有線索；母體、干擾或指標涵義須補。 |
| HR09 | 15 | partial 15 | 全部15份 | 核對來源、觀察範圍；不是事實造假的判斷。 |
| HR10 | 4 | partial 4 | jd20、jd26、jd32、jd36 | 核對防詐或策略期待與執行／內部系統重心。 |
| HR11 | 12 | partial 2；unknown 10 | jd03、jd09、jd20、jd26、jd30、jd31、jd32、jd34、jd36、jd40、jd44、jd47 | 多為申請條件未知；英文門檻另以工作樣本確認。 |
| HM01 | 3 | partial 3 | jd20、jd34、jd43 | 確認B2B門檻、OMO或區域總部情境。 |
| HM02 | 4 | partial 4 | jd09、jd11、jd14、jd31 | 補研究／回饋如何改變實際方案。 |
| HM05 | 15 | partial 15 | 全部15份 | 與HR04/09同一量測缺口，只在主要維度判一次。 |
| HM08 | 7 | partial 7 | jd03、jd14、jd30、jd31、jd36、jd40、jd47 | 核對API、資料／工具或指定技術深度。 |
| HM09 | 3 | partial 3 | jd14、jd30、jd47 | 核對Growth完整責任與資源決策範圍。 |



HR04、HR09、HM05 大量指向同一組量測問題；只在 outcome_quality 作主要判斷，不重複扣在其他維度。HR11 的 unknown 多是 JD 摘要與實際申請條件未齊，不是候選人有已知衝突，也不一律要求在 PDF 補寫。

## 5. 評語（合併後）

### 5.1 做得好（3 點；至少 2 份支持）

1. **企業系統交付與責任邊界能對上具體工作。** 1111 群組功能的「整理帳號權限、職缺關聯與既有資料轉換規則」，以及「再與 QA 制定 UAT 驗收案例、排定上線計畫」，讓人能追問實際規格、驗收與新舊資料限制。jd11、jd31、jd32、jd40 均有支持；價值來自工作證據，不是服務規模或管理人數。
2. **取捨有問題來源，且沒有把未完成的案子當成果。** 「搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。」呈現既有痛點與新功能之間的排序，後文保留兩案開發中。jd09、jd30、jd43、jd47 支持決策訊號；這能作面試入口，但不能當成已提升留存或營收。
3. **商業選擇有比較設計，也交代團隊歸屬。** 「以售價不變的 Android 作對照」與「團隊依結果決定採用低價。」連結定價、比較及採用決策；「網頁付款占營收由 24% 升至 80% 以上」則清楚指出量的是渠道占比。jd03、jd14、jd34、jd44 可用於商業或成長討論；仍需保留因果與淨效益限制。

### 5.2 可改進（≤6 點；只列重複 ≥2 份或 blocking）

**1. 案件週期數字補一組可核對口徑。**（15 份的量測追問）

- 位置：1111 最後一點。
- 原句：「平均處理時間由 100.4 天降至 30.9 天」
- 問題類型：measurement。
- 嚴重度：interview_follow_up。
- 影響：可支持觀察到的流程變化，但不足以判定案件可比或全部由本人措施造成；要追問計算方式，不是否定數字。
- 建議方向：補兩季件數、開始與結束事件、未結案納入方式、案件組成及清積案影響。可放短註或面試材料，不必公開內部原始資料。

**2. 占比與實驗，分別補能回答的商業問題。**（jd03、09、11、14、26、34、36、40、44、47 等）

- 位置：尚凡 Peach 與定價實驗兩點。
- 原句：「網頁付款占營收由 24% 升至 80% 以上」
- 問題類型：measurement。
- 嚴重度：interview_follow_up。
- 影響：占比不能代替總營收、淨實收或轉換；跨平台分期比較不能直接當隨機 A/B 的因果結論。Growth 面試會深入核對。
- 建議方向：渠道案例如確有資料，補總體趨勢、費率或成功率的觀察；定價案例補樣本、流量／活動、非續訂定義及公式。28% 可由 1.05÷0.82−1 得到約 28.05%，不是 23 個百分點；算式吻合不等於因果已證明。

**3. 用一份實際工作樣本，釐清技術與 AI 的本人範圍。**（jd03、11、20、30、31、32、36、40、47 等）

- 位置：技能／API、AI 協作，以及系統整合案例。
- 原句：「將業務規則轉為可與工程討論的條件描述」
- 問題類型：requirement。
- 嚴重度：interview_follow_up。
- 影響：目前支持規劃與協作，不代表已獨立查 SQL、實作 Agent／RAG、做快速程式原型或操作各指定工具；特定必要技能需驗證。
- 建議方向：按 JD 準備去識別 PRD、API 欄位／錯誤規則、驗收案例或 AI 輸入輸出與人工檢查。使用與 DBA 協作取數的真實流程即可；只有實際做過才補 SQL、JSON、Firebase、Jira、Confluence、Codex 等名稱。

**4. 研究與新產品經驗，用單一案例串完。**（jd09、11、14、30、31、43、47）

- 位置：研究與數據／尚凡 KOOL。
- 原句：「規劃 KOOL 網紅媒合平台」
- 問題類型：requirement。
- 嚴重度：interview_follow_up。
- 影響：已有需求、設計與上線的證據；直接客訪、驗證方式及上線後迭代仍不完整。需核對，不能以多款產品的片段代替同一產品的完整週期。
- 建議方向：補同一產品的一次核心假設、研究／原型驗證、本人與工程／行銷分工、上線後回饋與一次修改；沒有某項資料就明確說明限制。

**5. 策略取捨補本人可決定與須核准的部分。**（jd09、30、32、34、43、44、47）

- 位置：1111 改版與自傳的產品策略期待。
- 原句：「公司決定採新舊並行」
- 問題類型：ownership。
- 嚴重度：interview_follow_up。
- 影響：已證明本人規格與交付責任，但不能從公司決定、匯報主管或帶人推論本人掌握方向與資源；資深或區域角色會追問。
- 建議方向：補一次本人提出的選項與建議、為何延後另一件事、所需資源、協調過程及最後誰核准。保留公司、工程與本人邊界。

**6. 英文依工作門檻驗證，避免用測驗分數替代。**（jd11、20、44）

- 位置：語言技能與跨國協作。
- 原句：「並以英文進行跨國協作」
- 問題類型：requirement。
- 嚴重度：interview_follow_up。
- 影響：英文使用已有證據；jd20 的近母語口寫是會改變面試判斷的未知，jd11／44 則適合用文件或面試核對。
- 建議方向：備妥一份本人撰寫的英文需求文件，並以英文說明需求衝突、取捨與驗收。無需替自己新增未驗證的語言等級。

以上都是應補的工作事實，不是全文改寫指令。語氣偏好不列為招聘缺口；未據文風評作者是否為 AI。

### 5.3 面試最可能被追問的 5 題（準備事實，不代答）

| 題目 | 建議準備的事實 |
| :-- | :-- |
| 1. 100.4 天與 30.9 天如何計算？改善了什麼，哪些不能歸因你？ | 各季案件數、計時起訖、案件類型、未結案與積案、採取的措施與其他共同因素 |
| 2. 定價為什麼選 Android 對照？28% 怎麼算？付款占比上升回答哪個商業問題？ | 各期原始定義與樣本、相對比值、同期活動、平台差異、團隊決策；渠道占比與總體／淨實收分開 |
| 3. 群組或登入改版，請從資料規則講到驗收。你與工程各決定什麼？ | 帳號—群組—職缺—履歷關聯、轉換與例外、API 規格／資料限制、驗收與上線、權限及核准人 |
| 4. 一次研究或驗證如何改變方案？一次資源衝突如何排序？ | 同一案的使用者問題、訪談／工單／原型證據、原方案與修改、被延後事項、本人提案與最終裁決；未上線部分保持未完成 |
| 5. 能否用工作樣本證明這份 JD 最關鍵、目前還未知的條件？ | 依職缺擇一：jd20 的 B2B 年資起訖、英文需求討論與獨立查詢；jd14 的漏斗與 Firebase；jd30／47 的 JSON／SQL、新產品驗證鏈；其他職缺依各自缺口，不要求每場全交 |


## 6. ATS 準備檢查（五塊，不加總）

`test_level: local_extraction`；`actual_ats_import_performed: false`；真實 ATS 匯入：`not_run`。以下 pass 僅限明確執行的本機檢查；未知設定不視為通過或失敗。內容審查使用附錄 A；本節單獨使用附件 PDF。

輸入：`resume-v10.2-twocol.pdf`，793,878 bytes，2 頁，PDF 1.4，未加密、未標記結構（Tagged: no）。SHA-256：`71f037d52ada7e651e5308aff09829dac1c82cde3973b00cb99a173070451a80`。查閱日：2026-10-17（Asia/Taipei）。工具：Poppler `pdftotext 24.02.0`（`-raw` 與 `-layout`）、`pdfinfo 24.02.0`；另以 `pdftoppm` 渲染兩頁核對版面。無 OCR、無真實申請、無雇主系統權限。

### 6.1 檔案接受

| 規則 | 狀態 | 本次依據 | 影響、補證方式與責任人 |
| :-- | :-- | :-- | :-- |
| ATS01 系統與功能識別 | unknown | 15 份均為使用者提供的 104 職缺摘要；實際接收系統 vendor、module、版本、語言、設定來源皆 unknown | 104 職缺連結不證明履歷後續進入哪個系統；申請者在實際申請頁確認，招聘端確認後台設定 |
| ATS02 接受與解析分開 | unknown | 本機可開啟未加密 PDF，大小如上；未檢查各申請頁格式／大小限制 | 不能把本機開啟視為雇主可接收；申請者投遞前查該頁規則，附件接受與欄位解析分開驗證 |

### 6.2 欄位解析

| 規則 | 狀態 | 本次依據 | 影響、補證方式與責任人 |
| :-- | :-- | :-- | :-- |
| ATS03 姓名、聯絡資料 | pass（本機） | `-raw` 可完整找到姓名、email、電話 | 僅證明文字存在；實際表單是否填對仍 unknown，申請者核對預覽 |
| ATS03 職稱—公司—起訖 | pass（本機辨識）／risk（連續讀序） | 1111、尚凡、思維特、台灣新蛋的職稱、公司與日期可辨識；尚凡首段在頁一結束、頁二接續，中間穿插右欄技能、學歷與求職條件 | 解析器可能誤綁職務說明；文件作者可避免段落跨頁，申請者核對匯入後逐筆經歷 |
| ATS03 章節與雙欄讀序 | risk | `-layout` 將左右欄併列；`-raw` 在尚凡說明中插入右欄，再接頁二。不是單憑雙欄判定風險 | 實際觀察到段落中斷；文件作者可準備依章節連續輸出的版本並重測，非要求一律改單欄 |
| ATS03 到職條件 | risk | 頁一「錄取後三週可」、頁二右上「上班」；`-raw` 中間夾入多段工作經歷 | 完整片語搜尋未命中；文件作者將完整句留同頁，申請者於表單確認三週到職 |
| ATS03 重要數字 | pass（本機字串） | 100.4／30.9、24%／80%、28%、2025/09、2026/04、TOEIC 980、TOEFL iBT 93 均可找到 | 不代表分母、因果或資料口徑已查證；招聘端仍需面試核對 |
| ATS04 語言與結構資料 | unknown | 本機繁體文字可擷取；目標解析器的公開語言範圍、實際填入欄位皆未取得 | 不從中文介面推論支援繁體；申請者預覽，招聘端向供應商核對 |
| ATS12 摘要與完整性 | unknown（平台摘要）／risk（本機重排） | 未取得平台或 AI 摘要；附件主體與附錄 A 核對未見實質敘述差異，但有上述重排 | 不能把摘要省略當候選人缺能力；招聘端回查原文，文件作者修正跨頁完整性 |

未計算「還原率」作通過門檻，也不以大量可還原文字掩蓋到職條件與工作段落中斷。未發現姓名、email、電話的本機遺漏；完整句搜尋失敗與文字完全不存在是不同情況。

### 6.3 搜尋可見性

| 規則 | 狀態 | 本次依據 | 影響、補證方式與責任人 |
| :-- | :-- | :-- | :-- |
| ATS05 搜尋路徑 | pass（下列本機模擬）／unknown（雇主搜尋） | 僅查 `-raw` 抽出的附件全文；候選人欄位、備註、申請答案、歷史候選人均未測 | 未命中不代表被淘汰，命中不代表能力通過；招聘端確認實際索引與查詢 |
| ATS06 用詞對位 | risk（特定查詢） | PRD、API、GA4、Axure、Claude Code 有對應；SQL、Firebase、Jira、Confluence 未出現 | 先核實經驗才補寫；不得為命中加入未使用工具。只有確有查詢條件時才有具體搜尋影響 |

可重現查詢：範圍固定為本機 `-raw` 附件全文；所有查詢皆 AND、無 OR／NOT、不分大小寫、移除所有空白後做連續子字串比對、無模糊比對。這是透明的情境測試，並非招聘者的真實查詢或任何 ATS 搜尋語法。

| 查詢 ID | 完整詞項與運算 | 結果 | 解讀 |
| :-- | :-- | :-- | :-- |
| Q01 | PRD AND UAT | 命中 | 兩詞皆存在 |
| Q02 | API AND Axure | 命中 | 兩詞皆存在 |
| Q03 | GA4 AND Firebase | 未命中 | GA4 存在，Firebase 未出現 |
| Q04 | Jira AND Confluence | 未命中 | 兩詞均未出現 |
| Q05 | Claude Code AND AI Agent | 命中 | 兩詞皆存在 |
| Q06 | SQL | 未命中 | 字詞未出現，不證明不會 SQL |
| Q07 | 錄取後三週可上班 | 未命中 | 跨頁讀序切斷，文字分散存在 |
| Q08 | TOEIC AND CodaPay | 命中 | 兩詞皆存在 |

| JD 需求原句／術語 | 附錄 A 證據 | 合理對位／限制 |
| :-- | :-- | :-- |
| PRD／User Story／Wireframe（多職缺） | 「User Journey Map、User Story、Use Case」；技能與交付段列 PRD、Wireframe | 現有術語可直接對位，不需重複堆詞 |
| 追蹤進度、測試驗收（jd26/36/40 等） | 「與 QA 制定 UAT 驗收案例、排定上線計畫」 | UAT 可自然補中文驗收含義，不能等同所有測試策略 |
| GA4、Firebase（jd14） | 「競品實測、GA4、世代分析與對照組實驗」 | GA4 有線索；Firebase 未呈現，不能靠同類工具替代 |
| 理解 API、JSON、基本 SQL（jd30/47） | 「API 串接規劃」；「與 DBA 協作取數」 | API 有對位；JSON／SQL 須另核實，DBA 協作不等自行 SQL |
| AI 工具與工作流（jd20/30/43/47） | 「以 Claude Code 建立協作流程與共用 skill」 | AI Agent 有線索，不自動等同 Codex、RAG 或 Jira/Confluence 整合 |
| Jira、Confluence（jd26/36/43 等） | 「Notion、Trello、內部工單與看板系統」 | 同類任務可轉移，不是已用指定工具的證明 |

### 6.4 資格與流程條件

| 規則 | 狀態 | 本次依據 | 影響、補證方式與責任人 |
| :-- | :-- | :-- | :-- |
| ATS07 申請表與資格 | unknown | 未取得實際問題、答案、必要資格組合 | 不能預測自動淘汰；申請者如實填答並核對附件一致性 |
| ATS08 自動化流程 | unknown | 無表單規則、AI 設定、推進／拒絕／發信排程資料 | 無法由拒信速度歸因；招聘端確認規則與人工覆核 |
| ATS10 重複申請 | unknown | 無候選人合併、重投、來源、流程狀態設定 | 不建議反覆投遞或多帳號；申請者與招聘端確認既有申請狀態 |
| ATS11 自動投遞／詐騙 | unknown | 無平台中繼資料、模式或身分驗證訊號 | 文風與 AI 潤稿不等同詐騙或自動申請；招聘端用可驗證資料查核 |

### 6.5 匹配功能與未知設定

| 規則 | 狀態 | 本次依據 | 影響、補證方式與責任人 |
| :-- | :-- | :-- | :-- |
| ATS09 匹配／排序 | unknown | 輸入、權重、尺度、人工覆核途徑均 unknown | 不產生通用 ATS 分數；招聘端確認是否啟用及顯示方式 |
| ATS13 測試層級 | pass（紀錄） | 已記工具版本、hash、兩種本機抽字與查詢；真實匯入 false | 不宣稱 104 或任何供應商實測通過；真實解析由授權招聘端／申請預覽確認 |
| ATS14 未知與覆核 | pass（本報告紀錄）／unknown（雇主覆核） | 每項風險列依據、影響、補證與責任人；未知保留 | 不將錯誤、缺分或未啟用 AI 當低能力；不能從本次推論系統公平性 |

本次沒有任何可據以宣稱「雇主 ATS 通過」的測試，也沒有證據顯示 PDF 檔案本身不可讀。最明確的修正點是完整句及工作段落的跨頁讀序。

## 7. 方法限制與未做項目

- **模型紀錄**：15 輪與彙整的實際可識別 `model_id` 均為 `unknown`。執行環境未向審查員提供可驗證的精確模型識別碼，沒有用產品名、agent 名稱或推測名稱代填。`human_calibrated=false`，AI 作者機率一律 `null`。
- **實際執行**：15 次內容審查，每個職缺一個新 agent／新 context，皆以 `fork_turns=none` 啟動，不繼承主對話。每輪只指定讀取一份輸入檔（同一附錄 A、凍結規準／輸出契約、該輪唯一 JD），禁止讀其他職缺或審查輸出。未將主對話記憶或其他版本評分交給審查員。實際為 6／6／3 批啟動；批次只是併發安排，不是同一 context 連評。
- **隔離的界線**：屬新模型上下文與讀取指示的隔離，工作空間共享，未做作業系統層檔案權限隔離；不是 15 位真人或 15 個不同模型。新 context 可減少看見其他判斷的影響，不能據此宣稱統計獨立、無偏誤或招聘效度。彙整只以各輪輸出與另做的本機 ATS 紀錄為依據，不回調各輪分數。
- **輸入轉錄**：為建立單職缺輸入，將使用者提供的 JD 摘要與規準轉錄，同主題條件合併表達，保留工作內容、必要／加分與門檻；不是 104 原始全文，也未另行擷取最新職缺。requirements 以最多 12 列容納，複合條件在 reason 區分已支持與未呈現部分。未查證職缺目前仍開放；本報告的 5 份建議僅依本次提供內容，並非外部市場搜尋。
- **履歷來源**：內容審查採本訊息附錄 A；附件只用於獨立 PDF 檢查。沒有比較任何履歷版本，也未用先前對話的數字、名稱修正或評分補充本次事實。文件自述、作品與外部查證仍是不同證據層級。
- **未做**：真實 ATS 匯入、真實申請、表單規則或排名測試、真人校準、招聘結果追蹤、履歷事實外部查核、合成履歷規準校準／holdout、作者來源鑑定皆 `not_run`／`not_tested`。未做選配 V 截斷可見性測試；沒有宣稱真人限時掃讀通過。
- **評等限制**：依本次 4.2 規準，Level 是次要概括、各 ±1，非信賴區間、百分位或成功率。未作跨職缺 Level 平均、加權或排名；投遞建議依工作對位與待補成本，不以單一數字排序。各輪 Level 未達 9，進行中專案僅用於已發生的決策，不當作已實現成果。
- **判斷差異保留**：例如 jd30 為 Level 7、jd47 為 Level 8，兩職缺有相近必要條件，但職責重心不同；兩輪又是各別判讀。保留原始判斷與 ±1 不確定，不為整齊而追改。不能從這個差異推論候選人對兩個工作有可靠的精確高低。
- **技術失敗／格式修補**：15 輪皆完成，無遺失或無效 JSON。初版 jd34、jd43 的 `decision.evidence` 各有三句評語摘要，未符合原句證據要求。已分別保留初版，再由原審查員只把這三句改成 ≤40 字連續履歷原句；其餘欄位、決定、Level、維度不變。修補前原始 JSON 另收於附錄 B，不併入 15 輪統計，沒有刪除紀錄或重跑求高分。
- **格式檢查與展示**：彙整端檢查 15 份 JSON 可解析、單行、必要頂層欄位、6 維度、12＋13 題、數量上限、固定真假值、blocking 限制、引句長度及空白正規化後是否為附錄 A 子字串，最後通過。附錄評語統一排成 §6.2 八節、補原句位置與表格；不改原審查決定。原始 JSON 的 `validation.structural_checks=not_run` 保留，指該內容審查員本身未執行程式檢查；本段記錄的是之後由彙整端完成的格式核對，不冒稱已做行為回歸或真人驗證。
- **重複缺口的界線**：§4 題目分布直接從 15 輪狀態計數；主題缺口由 issues／key_gaps 歸類並明列職缺範圍。重複只表示值得優先準備，不是規準已校準或缺口必然成立。HR/HM 是取證，不另計分；同一量測問題不重複當多個維度扣分。

### 交件檢查清單

- [x] 單份審查 15 次，每次新 context，只放一份職缺；model_id 如實列 unknown，未猜測。
- [x] 15 份正式 JSON 皆單行、欄位齊全；human_calibrated=false、ai_authorship.probability=null。
- [x] 未做版本比較、未引用其他對話分數。
- [x] 未把頁數、學歷、空窗、任職長短、關鍵字數當缺失。
- [x] 每職缺各自判斷；未把其他 JD 的條件套來淘汰，沒有 Level 9 以上判定。
- [x] 每輪 HR 12 題＋HM 13 題全列；約談理由與關鍵缺口各 ≤3。
- [x] ATS 五塊分開、test_level=local_extraction，未產生 ATS 分數或宣稱真實匯入通過。
- [x] 總報告按 §8 七節；附錄 A 收 15 份正式原始 JSON 與各輪八節評語，附錄 B 保留兩份格式修補前輸出。

## 附錄 A：15 份原始 JSON 與單份審查評語

以下 JSON 為各審查員交付的原始單行資料（jd34、jd43 為已記錄的證據引句修補後原檔），不經彙整端重寫。每份隨後列八節評語；題目狀態、維度、決定與 Level 以該份 JSON 為準。內容輪次的 PDF not_tested 與總報告另做的 local_extraction 屬不同階段，並不衝突。

### A.01｜jd03｜原始單行 JSON

```json
{"rubric_version":"4.2","resume_id":"appendix-A-v10.2","job_id":"jd03","job_input":"summary","model_id":"unknown","run_id":"jd03-A-01","human_calibrated":false,"requirements":[{"id":"R01","text":"2年以上獨立PM","type":"required","status":"supported","evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃。"],"blocks_interview":false,"reason":"2018年起任PM，近期多項功能本人主責規劃，足以支持獨立PM經驗。"},{"id":"R02","text":"PRD／User Story／Wireframe","type":"required","status":"partial","evidence":["設計流程與畫面、撰寫 PRD 與製作 Prototype"],"blocks_interview":false,"reason":"PRD有實際交付案例；User Story與Wireframe列於技能，未呈現具體內容，可面試看去識別作品。"},{"id":"R03","text":"理解API串接與系統邏輯","type":"required","status":"supported","evidence":["並與 CodaPay 新加坡技術團隊協調串接。"],"blocks_interview":false,"reason":"付款串接與新舊資料規則提供相關證據；介面契約、異常處理及驗收細節可面試核對。"},{"id":"R04","text":"支付與合作生態規劃、與銀行／政府／合作夥伴對接","type":"required","status":"partial","evidence":["整理抽成、稅、手續費與撥款週期，完成實收試算"],"blocks_interview":false,"reason":"支付方案和CodaPay合作有實例；銀行、政府直接對接未呈現，不視為不符或獨立硬門檻。"},{"id":"R05","text":"追蹤進度及時程、跨部門溝通整合、協作流程優化","type":"required","status":"supported","evidence":["追蹤處理進度並每週回報"],"blocks_interview":false,"reason":"有分階段上線、工單追蹤及工程客服協作，支持進度與流程管理。"},{"id":"R06","text":"優化數據分析、產品營運策略定位與競品分析","type":"required","status":"supported","evidence":["以售價不變的 Android 作對照"],"blocks_interview":false,"reason":"定價實驗與付款渠道決策支持分析及營運；KOOL參考其他平台的媒合方式支持競品與定位思考。"},{"id":"R07","text":"金融科技／支付／點數／票證／電商經驗","type":"preferred","status":"supported","evidence":["另規劃並上線 VIP 訂閱、點數付費牆與精選曝光"],"blocks_interview":false,"reason":"具付款與點數經驗，符合此類領域加分；票證、電商與完整金融科技平台未呈現。"},{"id":"R08","text":"政府或銀行串接經驗","type":"preferred","status":"unknown","evidence":["並與 CodaPay 新加坡技術團隊協調串接。"],"blocks_interview":false,"reason":"僅第三方支付合作，不能等同政府或銀行串接；可追問是否曾直接對接。"},{"id":"R09","text":"會員經營與留存","type":"preferred","status":"partial","evidence":["配合行銷導入既有用戶，承接服務與營收。"],"blocks_interview":false,"reason":"有會員移轉與訂閱機制，會員分群、留存指標及改善成效未呈現。"},{"id":"R10","text":"數據觀測","type":"preferred","status":"supported","evidence":["持續追蹤案件處理週期"],"blocks_interview":false,"reason":"有持續處理週期追蹤及定價實驗；支付成功率等本職指標需追問。"},{"id":"R11","text":"UI／UX","type":"preferred","status":"supported","evidence":["透過互動原型與 FAQ 向客服、業務說明功能。"],"blocks_interview":false,"reason":"使用旅程、畫面流程及互動原型有實例；不推論本人擔任視覺設計。"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["曾規劃雙邊媒合與付費機制、設計定價實驗"],"missing":["近期B2B招募系統與高頻支付差異需面試核對"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"足夠","evidence":["並與 CodaPay 新加坡技術團隊協調串接。"],"missing":["銀行政府串接與支付核心API細節","User Story及Wireframe作品"],"issue_ids":["I01","I02"]},{"id":"decision_depth","rating":"強","evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。"],"missing":["支付風險、可靠性與商業價值如何排序"],"issue_ids":[]},{"id":"outcome_quality","rating":"足夠","evidence":["網頁付款占營收由 24% 升至 80% 以上。"],"missing":["交易量、成功率及總營收變動","工單母體與統計口徑"],"issue_ids":["I03","I04","I05"]},{"id":"ownership","rating":"足夠","evidence":["定義使用情境與驗收標準"],"missing":["支付串接分工、本人決策授權與工程責任界線"],"issue_ids":["I02"]},{"id":"readability","rating":"強","evidence":["工作涵蓋系統分析、流程與畫面設計、PRD、Prototype、UAT 與上線計畫"],"missing":["付款核心能力可集中呈現以利快速核對"],"issue_ids":[]}],"results":[{"quote":"系統服務逾 6 萬家活躍付費廠商（2026 Q3）","kinds":["context"]},{"quote":"與工程於 2025/09 完成上線。","kinds":["output"]},{"quote":"兩案均在開發中","kinds":["decision","in_progress"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上。","kinds":["outcome"]},{"quote":"團隊依結果決定採用低價。","kinds":["decision"]},{"quote":"2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天。","kinds":["outcome"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["並與 CodaPay 新加坡技術團隊協調串接。"],"application_note":"支付相關可轉移，銀行串接待追問"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 Product Owner"],"application_note":"近期B2B系統與高頻支付有差異"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我主責規劃。"],"application_note":"本人規劃明確，串接分工再核對"},{"rule_id":"HR04","status":"partial","resume_evidence":["網頁付款占營收由 24% 升至 80% 以上。"],"application_note":"渠道改變有證據，總營收影響待核"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。"],"application_note":"可驗證問題優先級及取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從 SweetRing 的海外市場開始累積產品經驗"],"application_note":"從在地化至系統PO，責任有演變"},{"rule_id":"HR07","status":"supported","resume_evidence":["與 QA 制定 UAT 驗收案例、排定上線計畫"],"application_note":"具協作情境，文件細節可驗證"},{"rule_id":"HR08","status":"supported","resume_evidence":["曾規劃雙邊媒合與付費機制、設計定價實驗"],"application_note":"摘要能找到付款及決策代表作"},{"rule_id":"HR09","status":"partial","resume_evidence":["依目前掌握的情況"],"application_note":"口述限制明示，需核對資料來源"},{"rule_id":"HR10","status":"supported","resume_evidence":["承擔更完整的問題定義、方向選擇與成效責任"],"application_note":"策略方向相容，支付動機可追問"},{"rule_id":"HR11","status":"unknown","resume_evidence":["台北市、新北市，可接受遠端或混合辦公"],"application_note":"JD工作條件未詳列，無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["規劃 Peach 付款由 App 內購轉向網頁"],"application_note":"支持約談，核心細節在面試驗證"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃 Peach 付款由 App 內購轉向網頁"],"evidence_type":"context","source_ids":[],"interview_question":"如何將付款渠道經驗轉到高頻交易與會員核心產品？"},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["廠商反映的溝通中斷問題，使我優先推進信件與即時通整合"],"evidence_type":"decision","source_ids":[],"interview_question":"哪些使用者證據改變原定優先級？"},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。"],"evidence_type":"decision","source_ids":[],"interview_question":"如何比較兩案價值、風險與資源，最終由誰決定？"},{"rule_id":"HM04","primary_dimension":"role_evidence","status":"supported","resume_evidence":["整理抽成、稅、手續費與撥款週期，完成實收試算"],"evidence_type":"decision","source_ids":[],"interview_question":"實收試算如何改變訂閱方案或付款合作選擇？"},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["網頁付款占營收由 24% 升至 80% 以上。"],"evidence_type":"outcome","source_ids":[],"interview_question":"付款占比期間的交易成功率、總營收及用戶數如何變化？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["與工程、設計、行銷及海外金流團隊協作完成上線"],"evidence_type":"output","source_ids":[],"interview_question":"串接時本人、工程及合作商如何分工處理分歧？"},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["處理新舊系統並行的相容性需求。"],"evidence_type":"output","source_ids":[],"interview_question":"如何界定上線範圍、回退條件與資料遷移驗收？"},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"partial","resume_evidence":["API 串接規劃、舊系統資料盤點與新舊流程銜接。"],"evidence_type":"context","source_ids":[],"interview_question":"用CodaPay案例說明狀態、回呼、重試及對帳的規格與驗收。"},{"rule_id":"HM09","primary_dimension":"ownership","status":"supported","resume_evidence":["重新制定業務流程、對照資料欄位並重構規格"],"evidence_type":"output","source_ids":[],"interview_question":"本人能決定的範圍、需升級決策及資源分配邊界為何？"},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["曾規劃雙邊媒合與付費機制、設計定價實驗"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["並依客服回饋修正操作流程。"],"evidence_type":"decision","source_ids":[],"interview_question":"何項回饋改變原方案，後續如何驗證修正？"},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["撰寫 PRD 與製作 Prototype"],"evidence_type":"output","source_ids":[],"interview_question":"能否提供去識別付款PRD及Wireframe，說明異常情境？"},{"rule_id":"HM13","primary_dimension":"method","status":"supported","resume_evidence":["兩案均在開發中"],"evidence_type":"in_progress","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HM01","source_ids":[],"application_note":"面試追問；不阻擋邀約","context_limit":"主要記於職務對位；非必要資格不符。","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"並與 CodaPay 新加坡技術團隊協調串接。","reason":"第三方支付合作不等同銀行政府直接串接，高頻支付場景尚待驗證。","suggestion":"補本人直接對接的機構、支付流程及責任；若無則說明可轉移經驗。"},{"id":"I02","rule_id":"HM08","source_ids":[],"application_note":"面試追問；不阻擋邀約","context_limit":"理解串接有支持；不因細節未知否定能力。","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"API 串接規劃、舊系統資料盤點與新舊流程銜接。","reason":"API為技能與合作線索，交易狀態、異常及驗收深度不明。","suggestion":"面試以去識別PRD、User Story及Wireframe核對介面規則與本人邊界。"},{"id":"I03","rule_id":"HM05","source_ids":[],"application_note":"面試追問；不阻擋邀約","context_limit":"已有期間；缺口限成效解釋。","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"網頁付款占營收由 24% 升至 80% 以上。","reason":"渠道占比變化不能單獨證明總營收或支付成功率改善。","suggestion":"補期間總營收、交易數、成功率及渠道推進範圍。"},{"id":"I04","rule_id":"HM05","source_ids":[],"application_note":"面試追問；不阻擋邀約","context_limit":"支持流程改變，不能全部歸因本人。","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天。","reason":"平均週期有期間，但案件類型、樣本數與積案口徑未呈現。","suggestion":"補Q1/Q2母體、起訖定義、樣本數及清案影響。"},{"id":"I05","rule_id":"HR09","source_ids":[],"application_note":"面試追問；不阻擋邀約","context_limit":"原文已限縮，不構成事實矛盾。","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"調整後至 2026/10 未再出現同類冒用。","reason":"以目前掌握情況為限，非完整監測紀錄或零風險證明。","suggestion":"補客服通報、監測來源、涵蓋帳號與觀察窗口。"}],"decision":{"recommendation":"interview","evidence":["規劃 Peach 付款由 App 內購轉向網頁","以售價不變的 Android 作對照","由我主責規劃。"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["「規劃 Peach 付款由 App 內購轉向網頁」提供支付產品相關案例。","「以售價不變的 Android 作對照」支持以分析處理商業選擇。","「重新制定業務流程、對照資料欄位並重構規格」支持核心系統交付。"],"key_gaps":["銀行／政府直接串接與高頻交易未呈現；追問對接機構及交易風險。","API異常與付款規格細節待核；請以PRD及Wireframe說明本人邊界。","付款占比與流程改善的量測限制待補；追問母體、分母與歸因。"],"strengths":["付款與點數機制有實際合作交付案例。","有對照實驗與問題優先級取捨，支持商業判斷。","新舊系統相容與分階段上線有明確本人行動。"],"interview_questions":["如何將付款渠道經驗轉到高頻交易與會員核心產品？","如何比較兩案價值、風險與資源，最終由誰決定？","實收試算如何改變訂閱方案或付款合作選擇？","付款占比期間的交易成功率、總營收及用戶數如何變化？","串接時本人、工程及合作商如何分工處理分歧？","如何界定上線範圍、回退條件與資料遷移驗收？","用CodaPay案例說明狀態、回呼、重試及對帳的規格與驗收。","能否提供去識別付款PRD及Wireframe，說明異常情境？"],"editorial_appendix":[],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"多案例涵蓋支付、點數、系統交付；具問題排序、定價對照與量測限制的專業模式。銀行政府、高頻交易及API細節待驗證，未達關鍵量測責任完整可追溯的9級。進行中案例僅支持決策。"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"not_tested","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"passed","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 單份審查｜履歷 appendix-A-v10.2｜第 1 輪｜model_id: unknown

#### 1. 結論

- 招聘決定：`interview`
- Level：8（±1）
- 一句話理由：「規劃 Peach 付款由 App 內購轉向網頁」支持面試，缺口依下表核對。

#### 2. 六維度

| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 曾規劃雙邊媒合與付費機制、設計定價實驗 | 近期B2B招募系統與高頻支付差異需面試核對 |
| role_evidence | 足夠 | 並與 CodaPay 新加坡技術團隊協調串接。 | 銀行政府串接與支付核心API細節；User Story及Wireframe作品 |
| decision_depth | 強 | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。 | 支付風險、可靠性與商業價值如何排序 |
| outcome_quality | 足夠 | 網頁付款占營收由 24% 升至 80% 以上。 | 交易量、成功率及總營收變動；工單母體與統計口徑 |
| ownership | 足夠 | 定義使用情境與驗收標準 | 支付串接分工、本人決策授權與工程責任界線 |
| readability | 強 | 工作涵蓋系統分析、流程與畫面設計、PRD、Prototype、UAT 與上線計畫 | 付款核心能力可集中呈現以利快速核對 |

#### 3. JD 條件對照

| 條件 | 必要／加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 2年以上獨立PM | 必要 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃。 | 2018年起任PM，近期多項功能本人主責規劃，足以支持獨立PM經驗。 |
| PRD／User Story／Wireframe | 必要 | partial | 設計流程與畫面、撰寫 PRD 與製作 Prototype | PRD有實際交付案例；User Story與Wireframe列於技能，未呈現具體內容，可面試看去識別作品。 |
| 理解API串接與系統邏輯 | 必要 | supported | 並與 CodaPay 新加坡技術團隊協調串接。 | 付款串接與新舊資料規則提供相關證據；介面契約、異常處理及驗收細節可面試核對。 |
| 支付與合作生態規劃、與銀行／政府／合作夥伴對接 | 必要 | partial | 整理抽成、稅、手續費與撥款週期，完成實收試算 | 支付方案和CodaPay合作有實例；銀行、政府直接對接未呈現，不視為不符或獨立硬門檻。 |
| 追蹤進度及時程、跨部門溝通整合、協作流程優化 | 必要 | supported | 追蹤處理進度並每週回報 | 有分階段上線、工單追蹤及工程客服協作，支持進度與流程管理。 |
| 優化數據分析、產品營運策略定位與競品分析 | 必要 | supported | 以售價不變的 Android 作對照 | 定價實驗與付款渠道決策支持分析及營運；KOOL參考其他平台的媒合方式支持競品與定位思考。 |
| 金融科技／支付／點數／票證／電商經驗 | 加分 | supported | 另規劃並上線 VIP 訂閱、點數付費牆與精選曝光 | 具付款與點數經驗，符合此類領域加分；票證、電商與完整金融科技平台未呈現。 |
| 政府或銀行串接經驗 | 加分 | unknown | 並與 CodaPay 新加坡技術團隊協調串接。 | 僅第三方支付合作，不能等同政府或銀行串接；可追問是否曾直接對接。 |
| 會員經營與留存 | 加分 | partial | 配合行銷導入既有用戶，承接服務與營收。 | 有會員移轉與訂閱機制，會員分群、留存指標及改善成效未呈現。 |
| 數據觀測 | 加分 | supported | 持續追蹤案件處理週期 | 有持續處理週期追蹤及定價實驗；支付成功率等本職指標需追問。 |
| UI／UX | 加分 | supported | 透過互動原型與 FAQ 向客服、業務說明功能。 | 使用旅程、畫面流程及互動原型有實例；不推論本人擔任視覺設計。 |

#### 4. HR 十二問／HM 十三問

| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 並與 CodaPay 新加坡技術團隊協調串接。 | 支付相關可轉移，銀行串接待追問 |
| HR02 | supported | 現任 1111 招募系統 Product Owner | 近期B2B系統與高頻支付有差異 |
| HR03 | supported | 由我主責規劃。 | 本人規劃明確，串接分工再核對 |
| HR04 | partial | 網頁付款占營收由 24% 升至 80% 以上。 | 渠道改變有證據，總營收影響待核 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。 | 可驗證問題優先級及取捨 |
| HR06 | supported | 從 SweetRing 的海外市場開始累積產品經驗 | 從在地化至系統PO，責任有演變 |
| HR07 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 具協作情境，文件細節可驗證 |
| HR08 | supported | 曾規劃雙邊媒合與付費機制、設計定價實驗 | 摘要能找到付款及決策代表作 |
| HR09 | partial | 依目前掌握的情況 | 口述限制明示，需核對資料來源 |
| HR10 | supported | 承擔更完整的問題定義、方向選擇與成效責任 | 策略方向相容，支付動機可追問 |
| HR11 | unknown | 台北市、新北市，可接受遠端或混合辦公 | JD工作條件未詳列，無已知衝突 |
| HR12 | supported | 規劃 Peach 付款由 App 內購轉向網頁 | 支持約談，核心細節在面試驗證 |
| HM01 | supported | 規劃 Peach 付款由 App 內購轉向網頁 | 消費支付可轉移，核對高頻場景 |
| HM02 | supported | 廠商反映的溝通中斷問題，使我優先推進信件與即時通整合 | 用戶問題驅動，核對證據來源 |
| HM03 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。 | 取捨可成立，開發中不算成果 |
| HM04 | supported | 整理抽成、稅、手續費與撥款週期，完成實收試算 | 定價與實收支持商業思考 |
| HM05 | partial | 網頁付款占營收由 24% 升至 80% 以上。 | 占比非總營收，核對分母 |
| HM06 | supported | 與工程、設計、行銷及海外金流團隊協作完成上線 | 協作清楚，核對支付分工 |
| HM07 | supported | 處理新舊系統並行的相容性需求。 | 有相容風險處理與階段交付 |
| HM08 | partial | API 串接規劃、舊系統資料盤點與新舊流程銜接。 | 技術理解有線索，核對異常規格 |
| HM09 | supported | 重新制定業務流程、對照資料欄位並重構規格 | 自主交付有證據，資源授權待核 |
| HM10 | supported | 曾規劃雙邊媒合與付費機制、設計定價實驗 | 摘要可定位本職相關案例 |
| HM11 | supported | 並依客服回饋修正操作流程。 | 回饋修正有實例，可追問驗證 |
| HM12 | supported | 撰寫 PRD 與製作 Prototype | 以作品核對核心能力，支持邀約 |
| HM13 | supported | 兩案均在開發中 | 按凍結規準；未把進行中當成果 |

#### 5. 約談理由（≤3）與關鍵缺口（≤3）

| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「規劃 Peach 付款由 App 內購轉向網頁」提供支付產品相關案例。 |
| 2 | 「以售價不變的 Android 作對照」支持以分析處理商業選擇。 |
| 3 | 「重新制定業務流程、對照資料欄位並重構規格」支持核心系統交付。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 銀行／政府直接串接與高頻交易未呈現；追問對接機構及交易風險。 | 如何將付款渠道經驗轉到高頻交易與會員核心產品？ |
| 2 | API異常與付款規格細節待核；請以PRD及Wireframe說明本人邊界。 | 如何比較兩案價值、風險與資源，最終由誰決定？ |
| 3 | 付款占比與流程改善的量測限制待補；追問母體、分母與歸因。 | 實收試算如何改變訂閱方案或付款合作選擇？ |

#### 6. 評語（給寫稿者的具體回饋）

**做得好（3 點）**

- 專業摘要｜「曾規劃雙邊媒合與付費機制、設計定價實驗」｜付款與點數機制有實際合作交付案例。
- Product Manager｜尚凡國際創新科技｜「並與 CodaPay 新加坡技術團隊協調串接。」｜有對照實驗與問題優先級取捨，支持商業判斷。
- Product Owner／PM｜1111 全球華人｜「搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。」｜新舊系統相容與分階段上線有明確本人行動。

**可改進（≤5 點）**

- 位置：Product Manager｜尚凡國際創新科技
  - 原句：「並與 CodaPay 新加坡技術團隊協調串接。」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：第三方支付合作不等同銀行政府直接串接，高頻支付場景尚待驗證。 面試追問；不阻擋邀約
  - 建議方向：補本人直接對接的機構、支付流程及責任；若無則說明可轉移經驗。

- 位置：專業技能
  - 原句：「API 串接規劃、舊系統資料盤點與新舊流程銜接。」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：API為技能與合作線索，交易狀態、異常及驗收深度不明。 面試追問；不阻擋邀約
  - 建議方向：面試以去識別PRD、User Story及Wireframe核對介面規則與本人邊界。

- 位置：Product Manager｜尚凡國際創新科技
  - 原句：「網頁付款占營收由 24% 升至 80% 以上。」
  - 問題類型：`measurement`
  - 嚴重度：`interview_follow_up`
  - 影響：渠道占比變化不能單獨證明總營收或支付成功率改善。 面試追問；不阻擋邀約
  - 建議方向：補期間總營收、交易數、成功率及渠道推進範圍。

- 位置：Product Owner／PM｜1111 全球華人
  - 原句：「2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天。」
  - 問題類型：`measurement`
  - 嚴重度：`interview_follow_up`
  - 影響：平均週期有期間，但案件類型、樣本數與積案口徑未呈現。 面試追問；不阻擋邀約
  - 建議方向：補Q1/Q2母體、起訖定義、樣本數及清案影響。

- 位置：Product Owner／PM｜1111 全球華人
  - 原句：「調整後至 2026/10 未再出現同類冒用。」
  - 問題類型：`measurement`
  - 嚴重度：`interview_follow_up`
  - 影響：以目前掌握情況為限，非完整監測紀錄或零風險證明。 面試追問；不阻擋邀約
  - 建議方向：補客服通報、監測來源、涵蓋帳號與觀察窗口。

**編輯附件**：無。

#### 7. 資深能力分布

delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

#### 8. 未測試聲明

PDF 抽字：本內容審查 `not_tested`（另見總報告 §6 的 `local_extraction`）／ATS 匯入：`not_tested`／AI 作者判讀：不可由文字判定／真人校準：`not_run`。

### A.02｜jd09｜原始單行 JSON

```json
{"rubric_version":"4.2","resume_id":"appendix-A-v10.2","job_id":"jd09","job_input":"summary","model_id":"unknown","run_id":"jd09-A-01","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上軟體產品或專案經驗","type":"required","status":"supported","evidence":["Product Owner／PM｜1111 全球華人｜2022/08 - 迄今"],"blocks_interview":false,"reason":"1111任期本身已逾三年，另有App軟體產品案例。"},{"id":"R02","text":"與客服業務蒐集需求、主導訪談","type":"required","status":"partial","evidence":["透過互動原型與 FAQ 向客服、業務說明功能"],"blocks_interview":false,"reason":"客服業務需求與回饋有情境；訪談僅技能列示，未呈現主導訪談及洞察如何改變方案。"},{"id":"R03","text":"分析市場競品、提出創新方案","type":"required","status":"supported","evidence":["參考 Airbnb 與交友平台的媒合方式"],"blocks_interview":false,"reason":"KOOL有跨類別參照與雙邊媒合設計；可面試驗證競品分析產物及市場判斷。"},{"id":"R04","text":"Roadmap、跨部門排序與PRD","type":"required","status":"supported","evidence":["依使用者旅程與工單問題安排優先級"],"blocks_interview":false,"reason":"有明確先後排序、PRD及分階段交付；長期Roadmap可追問。"},{"id":"R05","text":"規格、進度、測試驗收","type":"required","status":"supported","evidence":["再與 QA 制定 UAT 驗收案例、排定上線計畫"],"blocks_interview":false,"reason":"有系統分析、規格重構、驗收及實際上線案例。"},{"id":"R06","text":"說明文件與使用分析優化","type":"required","status":"partial","evidence":["透過互動原型與 FAQ 向客服、業務說明功能"],"blocks_interview":false,"reason":"說明文件已支持；產品使用行為分析如何觸發持續優化仍待案例。"},{"id":"R07","text":"B2B SaaS經驗尤佳","type":"preferred","status":"partial","evidence":["人力銀行企業端招募系統專案負責人"],"blocks_interview":false,"reason":"有企業付費軟體與客戶流程經驗；未直接交代SaaS模式或MarTech產品。"},{"id":"R08","text":"UI/UX概念方法論","type":"required","status":"supported","evidence":["設計流程與畫面、撰寫 PRD 與製作 Prototype"],"blocks_interview":false,"reason":"有旅程、流程、畫面、互動原型實作；足以支持面試。"},{"id":"R09","text":"批判思維與數據驅動","type":"required","status":"supported","evidence":["以售價不變的 Android 作對照"],"blocks_interview":false,"reason":"定價實驗呈現對照、還原與採用決定；排序也有痛點依據。"},{"id":"R10","text":"獨立跨部門溝通、顧客關係","type":"required","status":"supported","evidence":["我協調工程與客服，釐清受影響範圍"],"blocks_interview":false,"reason":"主責規劃、客服業務說明及事故協調支持自主協作；直接客戶關係深度可核對。"},{"id":"R11","text":"時程範圍整合管理、專案架構說明","type":"required","status":"supported","evidence":["處理新舊系統並行的相容性需求"],"blocks_interview":false,"reason":"新舊架構銜接、資料轉換、分階段上線與文件支持整合管理。"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["人力銀行企業端招募系統專案負責人"],"missing":["MarTech與SaaS環境差異需面試核對"],"issue_ids":[]},{"id":"role_evidence","rating":"足夠","evidence":["再與 QA 制定 UAT 驗收案例、排定上線計畫"],"missing":["主導訪談與使用行為分析案例"],"issue_ids":["I01","I02"]},{"id":"decision_depth","rating":"強","evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。"],"missing":["優先級選項的量化價值與資源成本可追問"],"issue_ids":[]},{"id":"outcome_quality","rating":"足夠","evidence":["平均處理時間由 100.4 天降至 30.9 天。"],"missing":["案件母體、統計口徑及清理積案影響"],"issue_ids":["I03","I04"]},{"id":"ownership","rating":"強","evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃。"],"missing":["公司決策與本人方向資源決策界線"],"issue_ids":["I05"]},{"id":"readability","rating":"足夠","evidence":["工作涵蓋系統分析、流程與畫面設計、PRD、Prototype、UAT 與上線計畫"],"missing":["可選擇強化最相關MarTech轉移案例；不影響面試"],"issue_ids":[]}],"results":[{"quote":"系統服務逾 6 萬家活躍付費廠商（2026 Q3）","kinds":["context"]},{"quote":"與工程於 2025/09 完成上線。","kinds":["output"]},{"quote":"平均處理時間由 100.4 天降至 30.9 天。","kinds":["outcome"]},{"quote":"團隊依結果決定採用低價。","kinds":["decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上。","kinds":["outcome"]},{"quote":"兩案均在開發中","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["工作涵蓋系統分析、流程與畫面設計、PRD、Prototype、UAT 與上線計畫"],"application_note":"交付能力對位；研究案例待補"},{"rule_id":"HR02","status":"supported","resume_evidence":["人力銀行企業端招募系統專案負責人"],"application_note":"企業流程可轉移至B2B工具"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我主責規劃"],"application_note":"主責清楚；方向權限另核對"},{"rule_id":"HR04","status":"partial","resume_evidence":["平均處理時間由 100.4 天降至 30.9 天。"],"application_note":"有改變；母體口徑需核對"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。"],"application_note":"有痛點排序與替代項目"},{"rule_id":"HR06","status":"supported","resume_evidence":["從 SweetRing 的海外市場開始累積產品經驗"],"application_note":"從在地化到企業系統責任"},{"rule_id":"HR07","status":"supported","resume_evidence":["與 CodaPay 新加坡技術團隊協調串接。"],"application_note":"協作及系統整合有實例"},{"rule_id":"HR08","status":"supported","resume_evidence":["現任 1111 招募系統 Product Owner"],"application_note":"近期定位與案例容易辨識"},{"rule_id":"HR09","status":"partial","resume_evidence":["相對變化約多 28%"],"application_note":"需核對計算及同期限制"},{"rule_id":"HR10","status":"supported","resume_evidence":["接下來，我希望把更多心力放回產品策略"],"application_note":"與產品方向工作相容"},{"rule_id":"HR11","status":"unknown","resume_evidence":["台北市、新北市，可接受遠端或混合辦公"],"application_note":"JD未提供工作條件，不能判衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["再與 QA 制定 UAT 驗收案例、排定上線計畫"],"application_note":"交付與判斷足以支持面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":"企業招募工具經驗如何轉用至CDP、MA、BI客戶情境？"},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"partial","resume_evidence":["依使用者旅程與工單問題安排優先級。"],"evidence_type":"decision","source_ids":[],"interview_question":"請提供主導客戶訪談並因此改變方案的案例。"},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。"],"evidence_type":"decision","source_ids":[],"interview_question":"如何比較兩案的價值、成本與風險？"},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["團隊依結果決定採用低價。"],"evidence_type":"decision","source_ids":[],"interview_question":"定價選項、商業目標及決策權如何分工？"},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["平均處理時間由 100.4 天降至 30.9 天。"],"evidence_type":"outcome","source_ids":[],"interview_question":"兩季案件母體與起迄點如何定義？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["再與 QA 制定 UAT 驗收案例、排定上線計畫"],"evidence_type":"output","source_ids":[],"interview_question":"產品、QA與工程的驗收及上線權責如何劃分？"},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["處理新舊系統並行的相容性需求。"],"evidence_type":"output","source_ids":[],"interview_question":"如何管理資料相容性及分階段上線風險？"},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["從舊帳號信箱並非唯一值的限制出發"],"evidence_type":"decision","source_ids":[],"interview_question":"驗證流程有哪些替代方案及驗收邊界？"},{"rule_id":"HM09","primary_dimension":"ownership","status":"supported","resume_evidence":["由我主責規劃"],"evidence_type":"context","source_ids":[],"interview_question":"請說明你自主決定方向與取得資源的一次案例。"},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["現任 1111 招募系統 Product Owner"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["並依客服測試回饋調整推薦規則。"],"evidence_type":"decision","source_ids":[],"interview_question":"哪項回饋推翻原先假設，後續如何驗證？"},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["設計流程與畫面、撰寫 PRD 與製作 Prototype"],"evidence_type":"output","source_ids":[],"interview_question":"可否以匿名PRD、訪談紀錄與使用分析作品驗證？"},{"rule_id":"HM13","primary_dimension":"method","status":"supported","resume_evidence":["兩案均在開發中"],"evidence_type":"in_progress","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HM02","source_ids":[],"application_note":"主導訪談案例不足","context_limit":"限研究證據；不否定客服需求蒐集","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"使用者訪談與問卷","reason":"訪談只在技能清單出現；不能確認本人主持、樣本及洞察轉方案。","suggestion":"補一件主持訪談的對象、發現及方案變化。"},{"id":"I02","rule_id":"HM12","source_ids":[],"application_note":"使用分析優化待驗證","context_limit":"主要計入role_evidence","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"GA4、世代分析與對照組實驗","reason":"工具列示與定價實驗不能直接證明企業產品使用行為分析的優化循環。","suggestion":"補使用事件、行為問題、調整與追蹤結果。"},{"id":"I03","rule_id":"HM05","source_ids":[],"application_note":"流程成效口徑待核對","context_limit":"不將平均下降全數歸因個人","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"平均處理時間由 100.4 天降至 30.9 天。","reason":"未交代案件數、結案口徑及積案清理對跨季比較的影響。","suggestion":"補各季案件數、統計範圍及可比性限制。"},{"id":"I04","rule_id":"HM05","source_ids":[],"application_note":"定價因果限制待說明","context_limit":"數據支持決策；非已證明因果","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"相對變化約多 28%","reason":"有對照與期間，但用戶組成、事件干擾、計算方式仍需說明。","suggestion":"補相對變化公式、樣本與干擾限制。"},{"id":"I05","rule_id":"HM09","source_ids":[],"application_note":"方向資源權責待補","context_limit":"不重複扣交付能力","category":"ownership","severity":"interview_follow_up","block_target":null,"claim":"公司決定採新舊並行","reason":"已呈現交付與協調；此案策略決定屬公司，不能據此推論本人完整方向資源責任。","suggestion":"補本人可決定的方向範圍、資源取捨與核准界線。"}],"decision":{"recommendation":"interview","evidence":["由我主責規劃","以售價不變的 Android 作對照","再與 QA 制定 UAT 驗收案例、排定上線計畫"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["「由我主責規劃」支持企業軟體需求到驗收交付的責任。","「搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。」支持問題驅動排序。","「以售價不變的 Android 作對照」支持數據驅動商業決策。"],"key_gaps":["主導訪談與使用分析的具體產物不足：追問研究如何改變方案及追蹤。","量測可比較性仍有限：追問案件母體與定價實驗干擾。","MarTech及方向資源責任尚需核對：追問領域轉移與本人決策邊界。"],"strengths":["企業系統的流程、資料與驗收交付證據具體。","痛點排序與定價實驗呈現不同類型的決策。","客服、業務、工程及QA協作能對位職務。"],"interview_questions":["企業招募工具經驗如何轉用至CDP、MA、BI客戶情境？","請提供主導客戶訪談並因此改變方案的案例。","如何比較兩案的價值、成本與風險？","兩季案件母體與起迄點如何定義？","如何管理資料相容性及分階段上線風險？","驗證流程有哪些替代方案及驗收邊界？","請說明你自主決定方向與取得資源的一次案例。","可否以匿名PRD、訪談紀錄與使用分析作品驗證？"],"editorial_appendix":[],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"多個企業系統與商業實驗案例支持面試，呈現清楚排序、對照及交付責任；訪談、使用分析、量測母體與MarTech適配仍需核對，未把進行中功能當實現成果。"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"not_tested","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 單份審查｜履歷 appendix-A-v10.2｜第 2 輪｜model_id: unknown

#### 1. 結論

- 招聘決定：`interview`
- Level：8（±1）
- 一句話理由：「由我主責規劃」支持面試，缺口依下表核對。

#### 2. 六維度

| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 人力銀行企業端招募系統專案負責人 | MarTech與SaaS環境差異需面試核對 |
| role_evidence | 足夠 | 再與 QA 制定 UAT 驗收案例、排定上線計畫 | 主導訪談與使用行為分析案例 |
| decision_depth | 強 | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。 | 優先級選項的量化價值與資源成本可追問 |
| outcome_quality | 足夠 | 平均處理時間由 100.4 天降至 30.9 天。 | 案件母體、統計口徑及清理積案影響 |
| ownership | 強 | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃。 | 公司決策與本人方向資源決策界線 |
| readability | 足夠 | 工作涵蓋系統分析、流程與畫面設計、PRD、Prototype、UAT 與上線計畫 | 可選擇強化最相關MarTech轉移案例；不影響面試 |

#### 3. JD 條件對照

| 條件 | 必要／加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 3年以上軟體產品或專案經驗 | 必要 | supported | Product Owner／PM｜1111 全球華人｜2022/08 - 迄今 | 1111任期本身已逾三年，另有App軟體產品案例。 |
| 與客服業務蒐集需求、主導訪談 | 必要 | partial | 透過互動原型與 FAQ 向客服、業務說明功能 | 客服業務需求與回饋有情境；訪談僅技能列示，未呈現主導訪談及洞察如何改變方案。 |
| 分析市場競品、提出創新方案 | 必要 | supported | 參考 Airbnb 與交友平台的媒合方式 | KOOL有跨類別參照與雙邊媒合設計；可面試驗證競品分析產物及市場判斷。 |
| Roadmap、跨部門排序與PRD | 必要 | supported | 依使用者旅程與工單問題安排優先級 | 有明確先後排序、PRD及分階段交付；長期Roadmap可追問。 |
| 規格、進度、測試驗收 | 必要 | supported | 再與 QA 制定 UAT 驗收案例、排定上線計畫 | 有系統分析、規格重構、驗收及實際上線案例。 |
| 說明文件與使用分析優化 | 必要 | partial | 透過互動原型與 FAQ 向客服、業務說明功能 | 說明文件已支持；產品使用行為分析如何觸發持續優化仍待案例。 |
| B2B SaaS經驗尤佳 | 加分 | partial | 人力銀行企業端招募系統專案負責人 | 有企業付費軟體與客戶流程經驗；未直接交代SaaS模式或MarTech產品。 |
| UI/UX概念方法論 | 必要 | supported | 設計流程與畫面、撰寫 PRD 與製作 Prototype | 有旅程、流程、畫面、互動原型實作；足以支持面試。 |
| 批判思維與數據驅動 | 必要 | supported | 以售價不變的 Android 作對照 | 定價實驗呈現對照、還原與採用決定；排序也有痛點依據。 |
| 獨立跨部門溝通、顧客關係 | 必要 | supported | 我協調工程與客服，釐清受影響範圍 | 主責規劃、客服業務說明及事故協調支持自主協作；直接客戶關係深度可核對。 |
| 時程範圍整合管理、專案架構說明 | 必要 | supported | 處理新舊系統並行的相容性需求 | 新舊架構銜接、資料轉換、分階段上線與文件支持整合管理。 |

#### 4. HR 十二問／HM 十三問

| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 工作涵蓋系統分析、流程與畫面設計、PRD、Prototype、UAT 與上線計畫 | 交付能力對位；研究案例待補 |
| HR02 | supported | 人力銀行企業端招募系統專案負責人 | 企業流程可轉移至B2B工具 |
| HR03 | supported | 由我主責規劃 | 主責清楚；方向權限另核對 |
| HR04 | partial | 平均處理時間由 100.4 天降至 30.9 天。 | 有改變；母體口徑需核對 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。 | 有痛點排序與替代項目 |
| HR06 | supported | 從 SweetRing 的海外市場開始累積產品經驗 | 從在地化到企業系統責任 |
| HR07 | supported | 與 CodaPay 新加坡技術團隊協調串接。 | 協作及系統整合有實例 |
| HR08 | supported | 現任 1111 招募系統 Product Owner | 近期定位與案例容易辨識 |
| HR09 | partial | 相對變化約多 28% | 需核對計算及同期限制 |
| HR10 | supported | 接下來，我希望把更多心力放回產品策略 | 與產品方向工作相容 |
| HR11 | unknown | 台北市、新北市，可接受遠端或混合辦公 | JD未提供工作條件，不能判衝突 |
| HR12 | supported | 再與 QA 制定 UAT 驗收案例、排定上線計畫 | 交付與判斷足以支持面試 |
| HM01 | supported | 人力銀行企業端招募系統專案負責人 | 企業工具可轉移；領域可學 |
| HM02 | partial | 依使用者旅程與工單問題安排優先級。 | 訪談需補實例，不阻擋面試 |
| HM03 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。 | 排序與替代項目支持判斷 |
| HM04 | supported | 團隊依結果決定採用低價。 | 有商業選擇，不額外要求P&L |
| HM05 | partial | 平均處理時間由 100.4 天降至 30.9 天。 | 量測限制需核對 |
| HM06 | supported | 再與 QA 制定 UAT 驗收案例、排定上線計畫 | 協作與本人邊界清楚 |
| HM07 | supported | 處理新舊系統並行的相容性需求。 | 新舊並行具交付風險管理 |
| HM08 | supported | 從舊帳號信箱並非唯一值的限制出發 | 規則及資料限制具體 |
| HM09 | supported | 由我主責規劃 | 不以年資或人數決定Level |
| HM10 | supported | 現任 1111 招募系統 Product Owner | 定位與交付證據可快速辨識 |
| HM11 | supported | 並依客服測試回饋調整推薦規則。 | 客服反饋確有觸發調整 |
| HM12 | supported | 設計流程與畫面、撰寫 PRD 與製作 Prototype | 可用匿名作品驗證關鍵缺口 |
| HM13 | supported | 兩案均在開發中 | 進行中不當成果；未外部查證 |

#### 5. 約談理由（≤3）與關鍵缺口（≤3）

| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「由我主責規劃」支持企業軟體需求到驗收交付的責任。 |
| 2 | 「搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。」支持問題驅動排序。 |
| 3 | 「以售價不變的 Android 作對照」支持數據驅動商業決策。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 主導訪談與使用分析的具體產物不足：追問研究如何改變方案及追蹤。 | 企業招募工具經驗如何轉用至CDP、MA、BI客戶情境？ |
| 2 | 量測可比較性仍有限：追問案件母體與定價實驗干擾。 | 請提供主導客戶訪談並因此改變方案的案例。 |
| 3 | MarTech及方向資源責任尚需核對：追問領域轉移與本人決策邊界。 | 如何比較兩案的價值、成本與風險？ |

#### 6. 評語（給寫稿者的具體回饋）

**做得好（3 點）**

- Product Owner／PM｜1111 全球華人｜「人力銀行企業端招募系統專案負責人」｜企業系統的流程、資料與驗收交付證據具體。
- Product Owner／PM｜1111 全球華人｜「再與 QA 制定 UAT 驗收案例、排定上線計畫」｜痛點排序與定價實驗呈現不同類型的決策。
- Product Owner／PM｜1111 全球華人｜「搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。」｜客服、業務、工程及QA協作能對位職務。

**可改進（≤5 點）**

- 位置：專業技能
  - 原句：「使用者訪談與問卷」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：訪談只在技能清單出現；不能確認本人主持、樣本及洞察轉方案。 主導訪談案例不足
  - 建議方向：補一件主持訪談的對象、發現及方案變化。

- 位置：專業技能
  - 原句：「GA4、世代分析與對照組實驗」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：工具列示與定價實驗不能直接證明企業產品使用行為分析的優化循環。 使用分析優化待驗證
  - 建議方向：補使用事件、行為問題、調整與追蹤結果。

- 位置：Product Owner／PM｜1111 全球華人
  - 原句：「平均處理時間由 100.4 天降至 30.9 天。」
  - 問題類型：`measurement`
  - 嚴重度：`interview_follow_up`
  - 影響：未交代案件數、結案口徑及積案清理對跨季比較的影響。 流程成效口徑待核對
  - 建議方向：補各季案件數、統計範圍及可比性限制。

- 位置：Product Manager｜尚凡國際創新科技
  - 原句：「相對變化約多 28%」
  - 問題類型：`measurement`
  - 嚴重度：`interview_follow_up`
  - 影響：有對照與期間，但用戶組成、事件干擾、計算方式仍需說明。 定價因果限制待說明
  - 建議方向：補相對變化公式、樣本與干擾限制。

- 位置：自傳
  - 原句：「公司決定採新舊並行」
  - 問題類型：`ownership`
  - 嚴重度：`interview_follow_up`
  - 影響：已呈現交付與協調；此案策略決定屬公司，不能據此推論本人完整方向資源責任。 方向資源權責待補
  - 建議方向：補本人可決定的方向範圍、資源取捨與核准界線。

**編輯附件**：無。

#### 7. 資深能力分布

delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

#### 8. 未測試聲明

PDF 抽字：本內容審查 `not_tested`（另見總報告 §6 的 `local_extraction`）／ATS 匯入：`not_tested`／AI 作者判讀：不可由文字判定／真人校準：`not_run`。

### A.03｜jd11｜原始單行 JSON

```json
{"rubric_version":"4.2","resume_id":"appendix-A-v10.2","job_id":"jd11","job_input":"summary","model_id":"unknown","run_id":"jd11-A-01","human_calibrated":false,"requirements":[{"id":"R01","text":"規劃推動客戶管理系統或HRIS，持續優化CMS/HRIS","type":"required","status":"partial","evidence":["人力銀行企業端招募系統專案負責人","同時持續迭代現行服務"],"blocks_interview":false,"reason":"企業招募系統與HR Tech相鄰且有持續迭代；未直接呈現CMS或完整HRIS模組，面試核對流程差異。"},{"id":"R02","text":"使用者訪談、PRD、流程圖、使用者故事","type":"required","status":"partial","evidence":["設計流程與畫面、撰寫 PRD 與製作 Prototype","使用者訪談與問卷"],"blocks_interview":false,"reason":"PRD與流程設計有實作案例；訪談、流程圖與User Story有技能線索，缺訪談如何改變規格及故事樣本。"},{"id":"R03","text":"協同UX與工程、追蹤KPI及反饋、roadmap","type":"required","status":"supported","evidence":["與工程、設計、行銷及海外金流團隊協作完成上線","依使用者旅程與工單問題安排優先級","持續追蹤案件處理週期"],"blocks_interview":false,"reason":"工程設計協作、優先順序、分階段交付與追蹤週期均有證據；產品採用KPI可再核對。"},{"id":"R04","text":"5年以上PM","type":"required","status":"supported","evidence":["近 10 年 PM 經驗"],"blocks_interview":false,"reason":"2016/06起PM職務時序支持五年以上，不以年資單獨判資深程度。"},{"id":"R05","text":"敏捷與跨部門專案經驗","type":"required","status":"supported","evidence":["曾參與每週一個 Sprint 的 Scrum","對接工程、行銷、業務與客服等 10 個需求單位"],"blocks_interview":false,"reason":"敏捷參與有明文且跨部門交付有案例；現行混合流程不構成不符。"},{"id":"R06","text":"邏輯溝通、溝通整合、人力資源、談判及範圍管理","type":"required","status":"partial","evidence":["整理帳號權限、職缺關聯與既有資料轉換規則","透過互動原型與 FAQ 向客服、業務說明功能"],"blocks_interview":false,"reason":"邏輯、溝通整合與範圍拆解有實例；招募領域支持人資相關性，完整人資流程及談判權責需核對。"},{"id":"R07","text":"Jira、Notion等工具","type":"required","status":"partial","evidence":["Figma、Axure RP、Notion、Trello、內部工單與看板系統"],"blocks_interview":false,"reason":"Notion及類似看板工具明示；Jira未提供，工具未知不是能力不符。"},{"id":"R08","text":"中英文文件能力","type":"required","status":"partial","evidence":["Newegg.com 商品資訊英翻中與校對。","並以英文進行跨國協作"],"blocks_interview":false,"reason":"中文規格、英翻中與英文協作有證據；英文PRD等產品文件樣本未呈現。"},{"id":"R09","text":"HR Tech／LegalTech／生成式AI產品經驗","type":"preferred","status":"supported","evidence":["上線公司簡介生成、職缺工作說明生成及 AI 推薦人才"],"blocks_interview":false,"reason":"招募系統及生成式內容產品直接相關；LegalTech未呈現，列舉方向毋須全部具備。"},{"id":"R10","text":"LLM prompt設計或自動化內容編排","type":"preferred","status":"partial","evidence":["以 Claude Code 建立協作流程與共用 skill"],"blocks_interview":false,"reason":"支持AI協作流程線索，未呈現prompt設計、內容編排架構及評估方法。"},{"id":"R11","text":"數據導向AB測試","type":"preferred","status":"partial","evidence":["以售價不變的 Android 作對照"],"blocks_interview":false,"reason":"有跨平台對照及分期價格實驗；非已證明隨機AB，平台差異及混雜因素需核對。"},{"id":"R12","text":"前後端背景","type":"preferred","status":"partial","evidence":["基本 HTML／CSS 與資料庫知識","API 串接規劃、舊系統資料盤點與新舊流程銜接"],"blocks_interview":false,"reason":"具系統分析及基礎技術素養，未呈現前後端開發實務，不以協作等同實作。"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["現任 1111 招募系統 Product Owner"],"missing":["CMS／完整HRIS環境差異待面試核對"],"issue_ids":[]},{"id":"role_evidence","rating":"足夠","evidence":["設計流程與畫面、撰寫 PRD 與製作 Prototype"],"missing":["英文產品文件、Jira、訪談實例與prompt評估待核對"],"issue_ids":["I03","I04"]},{"id":"decision_depth","rating":"強","evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"missing":["優先級影響及資源取捨可面試加深"],"issue_ids":[]},{"id":"outcome_quality","rating":"足夠","evidence":["平均處理時間由 100.4 天降至 30.9 天"],"missing":["處理週期母體口徑及實驗混雜限制待核對"],"issue_ids":["I01","I02"]},{"id":"ownership","rating":"強","evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃。"],"missing":["部門方向、資源配置最終權限未完整呈現"],"issue_ids":[]},{"id":"readability","rating":"足夠","evidence":["工作涵蓋系統分析、流程與畫面設計、PRD、Prototype、UAT 與上線計畫"],"missing":["自傳與經歷重複可精簡，屬編輯事項"],"issue_ids":[]}],"results":[{"quote":"系統服務逾 6 萬家活躍付費廠商（2026 Q3）","kinds":["context"]},{"quote":"與工程於 2025/09 完成上線","kinds":["output"]},{"quote":"平均處理時間由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"團隊依結果決定採用低價","kinds":["decision"]},{"quote":"兩案均在開發中","kinds":["in_progress"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["人力銀行企業端招募系統專案負責人"],"application_note":"HR Tech及系統規劃直接相關"},{"rule_id":"HR02","status":"supported","resume_evidence":["同時持續迭代現行服務"],"application_note":"近期兼顧改版與既有客戶"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我主責規劃"],"application_note":"規劃責任清楚，工程實作另屬團隊"},{"rule_id":"HR04","status":"partial","resume_evidence":["平均處理時間由 100.4 天降至 30.9 天"],"application_note":"變化明確，核對母體與口徑"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"application_note":"有實際優先順序理由"},{"rule_id":"HR06","status":"supported","resume_evidence":["到了企業端，更常思考的是"],"application_note":"由消費產品轉企業流程脈絡清楚"},{"rule_id":"HR07","status":"supported","resume_evidence":["與 CodaPay 新加坡技術團隊協調串接"],"application_note":"跨國技術協作有情境"},{"rule_id":"HR08","status":"supported","resume_evidence":["資深產品經理｜Senior Product Manager"],"application_note":"主軸明確，部分內容重複"},{"rule_id":"HR09","status":"partial","resume_evidence":["依目前掌握的情況"],"application_note":"安全改善屬觀察，需核對紀錄"},{"rule_id":"HR10","status":"supported","resume_evidence":["承擔更完整的問題定義、方向選擇與成效責任"],"application_note":"方向與產品職相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公"],"application_note":"地點無已知衝突，語文文件待核對"},{"rule_id":"HR12","status":"supported","resume_evidence":["定義使用情境與驗收標準"],"application_note":"支持面試，非錄取率預測"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":"招募系統哪些流程可移轉至本職CMS／HRIS？"},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"partial","resume_evidence":["廠商反映的溝通中斷問題"],"evidence_type":"decision","source_ids":[],"interview_question":"挑一個訪談，說明使用者哪一步受阻、如何改變規格？"},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":"排序時如何比較影響、成本及資源限制？"},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["團隊依結果決定採用低價"],"evidence_type":"decision","source_ids":[],"interview_question":"如何將價格實驗的商業判斷轉用於企業系統？"},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["平均處理時間由 100.4 天降至 30.9 天"],"evidence_type":"outcome","source_ids":[],"interview_question":"案件週期的起訖、件數及新舊案組成為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["再與 QA 制定 UAT 驗收案例、排定上線計畫"],"evidence_type":"output","source_ids":[],"interview_question":"你與工程、設計及主管分別有哪些決策權？"},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["處理新舊系統並行的相容性需求"],"evidence_type":"output","source_ids":[],"interview_question":"如何定義遷移驗收、回復及上線品質門檻？"},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["從舊帳號信箱並非唯一值的限制出發"],"evidence_type":"decision","source_ids":[],"interview_question":"展示驗證流程規則、替代方案及驗收案例。"},{"rule_id":"HM09","primary_dimension":"ownership","status":"supported","resume_evidence":["帶領 2 名直屬產品企劃"],"evidence_type":"context","source_ids":[],"interview_question":"你如何安排團隊工作及協商跨專案資源？"},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["工作涵蓋系統分析、流程與畫面設計、PRD、Prototype、UAT 與上線計畫"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["並依客服測試回饋調整推薦規則"],"evidence_type":"decision","source_ids":[],"interview_question":"回饋造成哪條規則改變，如何確認修正有效？"},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["上線公司簡介生成、職缺工作說明生成及 AI 推薦人才"],"evidence_type":"output","source_ids":[],"interview_question":"展示一份英文PRD及AI功能的prompt與驗收樣本。"},{"rule_id":"HM13","primary_dimension":"method","status":"supported","resume_evidence":["現行以 Kanban 推進瀑布式開發"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HM05","source_ids":[],"application_note":"量測口徑待面試核對","context_limit":"2026 Q1至Q2案件週期","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"平均處理時間由 100.4 天降至 30.9 天","reason":"有期間與前後值，但件數、起訖及清理積案後組成未知；不能全歸本人因果。","suggestion":"補案件數、起訖定義、分布與案件組成。"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"對照實驗不直接視為隨機AB","context_limit":"馬來西亞iOS分期定價","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"以售價不變的 Android 作對照","reason":"跨平台分期比較有判斷價值，但非隨機AB證據，促銷及用戶結構差異未知。","suggestion":"補樣本、同期活動、平台差異與決策限制。"},{"id":"I03","rule_id":"HR01","source_ids":[],"application_note":"必要工具與英文文件尚待核對","context_limit":"Jira與中英文文件要求","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"並以英文進行跨國協作","reason":"協作與翻譯支持語言能力，但不等於英文產品規格實績；Notion已列，Jira未知。","suggestion":"面試展示英文產品文件，說明工具操作與遷移能力。"},{"id":"I04","rule_id":"HM12","source_ids":[],"application_note":"生成式AI加分深度未完整呈現","context_limit":"prompt或自動化內容編排加分","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"以 Claude Code 建立協作流程與共用 skill","reason":"有AI協作與生成產品，尚無prompt版本、內容編排及品質評估細節。","suggestion":"展示本人設計的prompt或編排與品質驗收方式。"}],"decision":{"recommendation":"interview","evidence":["人力銀行企業端招募系統專案負責人","定義使用情境與驗收標準","依使用者旅程與工單問題安排優先級"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["「人力銀行企業端招募系統專案負責人」直接支持HR Tech流程經驗。","「定義使用情境與驗收標準」支持生成式AI產品協作。","「搜尋結果頁的既有痛點，也排在新功能職缺健檢之前」顯示需求取捨。"],"key_gaps":["量測口徑與實驗限制：追問案件母體及跨平台混雜。","英文規格及工具實務：追問英文PRD與Jira／類似工具操作。","訪談與AI編排深度：追問如何改變需求與prompt驗收。"],"strengths":["招募系統改版、群組權限及舊資料銜接與本職相近。","有可辨識需求優先級、規格、驗收與分階段交付責任。","兼有生成式內容功能與商業對照實驗經驗。"],"interview_questions":["展示一份PRD、流程圖及User Story，說明訪談如何改變需求。","案件週期起訖、母體件數、案件組成及限制是什麼？","跨平台價格實驗如何處理混雜，為何採低價？","展示英文產品文件並說明Jira或類似工具操作。","AI生成產品中本人如何設計prompt、編排及驗收？","HRIS與現有招募系統的差異及學習優先級是什麼？","取捨搜尋優化與職缺健檢時如何分配資源？","帶領企劃與跨單位談判時，最終權責邊界在哪？"],"editorial_appendix":[],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"多個相關系統與AI案例，需求取捨、交付責任及含限制的實驗支持專業模式；量測口徑、英文文件及AI編排深度待核對，未達關鍵量測與責任全面可追溯的9。進行中功能僅支持決策，不當成果。"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"not_tested","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 單份審查｜履歷 appendix-A-v10.2｜第 3 輪｜model_id: unknown

#### 1. 結論

- 招聘決定：`interview`
- Level：8（±1）
- 一句話理由：「人力銀行企業端招募系統專案負責人」支持面試，缺口依下表核對。

#### 2. 六維度

| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 現任 1111 招募系統 Product Owner | CMS／完整HRIS環境差異待面試核對 |
| role_evidence | 足夠 | 設計流程與畫面、撰寫 PRD 與製作 Prototype | 英文產品文件、Jira、訪談實例與prompt評估待核對 |
| decision_depth | 強 | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 優先級影響及資源取捨可面試加深 |
| outcome_quality | 足夠 | 平均處理時間由 100.4 天降至 30.9 天 | 處理週期母體口徑及實驗混雜限制待核對 |
| ownership | 強 | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃。 | 部門方向、資源配置最終權限未完整呈現 |
| readability | 足夠 | 工作涵蓋系統分析、流程與畫面設計、PRD、Prototype、UAT 與上線計畫 | 自傳與經歷重複可精簡，屬編輯事項 |

#### 3. JD 條件對照

| 條件 | 必要／加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 規劃推動客戶管理系統或HRIS，持續優化CMS/HRIS | 必要 | partial | 人力銀行企業端招募系統專案負責人；同時持續迭代現行服務 | 企業招募系統與HR Tech相鄰且有持續迭代；未直接呈現CMS或完整HRIS模組，面試核對流程差異。 |
| 使用者訪談、PRD、流程圖、使用者故事 | 必要 | partial | 設計流程與畫面、撰寫 PRD 與製作 Prototype；使用者訪談與問卷 | PRD與流程設計有實作案例；訪談、流程圖與User Story有技能線索，缺訪談如何改變規格及故事樣本。 |
| 協同UX與工程、追蹤KPI及反饋、roadmap | 必要 | supported | 與工程、設計、行銷及海外金流團隊協作完成上線；依使用者旅程與工單問題安排優先級；持續追蹤案件處理週期 | 工程設計協作、優先順序、分階段交付與追蹤週期均有證據；產品採用KPI可再核對。 |
| 5年以上PM | 必要 | supported | 近 10 年 PM 經驗 | 2016/06起PM職務時序支持五年以上，不以年資單獨判資深程度。 |
| 敏捷與跨部門專案經驗 | 必要 | supported | 曾參與每週一個 Sprint 的 Scrum；對接工程、行銷、業務與客服等 10 個需求單位 | 敏捷參與有明文且跨部門交付有案例；現行混合流程不構成不符。 |
| 邏輯溝通、溝通整合、人力資源、談判及範圍管理 | 必要 | partial | 整理帳號權限、職缺關聯與既有資料轉換規則；透過互動原型與 FAQ 向客服、業務說明功能 | 邏輯、溝通整合與範圍拆解有實例；招募領域支持人資相關性，完整人資流程及談判權責需核對。 |
| Jira、Notion等工具 | 必要 | partial | Figma、Axure RP、Notion、Trello、內部工單與看板系統 | Notion及類似看板工具明示；Jira未提供，工具未知不是能力不符。 |
| 中英文文件能力 | 必要 | partial | Newegg.com 商品資訊英翻中與校對。；並以英文進行跨國協作 | 中文規格、英翻中與英文協作有證據；英文PRD等產品文件樣本未呈現。 |
| HR Tech／LegalTech／生成式AI產品經驗 | 加分 | supported | 上線公司簡介生成、職缺工作說明生成及 AI 推薦人才 | 招募系統及生成式內容產品直接相關；LegalTech未呈現，列舉方向毋須全部具備。 |
| LLM prompt設計或自動化內容編排 | 加分 | partial | 以 Claude Code 建立協作流程與共用 skill | 支持AI協作流程線索，未呈現prompt設計、內容編排架構及評估方法。 |
| 數據導向AB測試 | 加分 | partial | 以售價不變的 Android 作對照 | 有跨平台對照及分期價格實驗；非已證明隨機AB，平台差異及混雜因素需核對。 |
| 前後端背景 | 加分 | partial | 基本 HTML／CSS 與資料庫知識；API 串接規劃、舊系統資料盤點與新舊流程銜接 | 具系統分析及基礎技術素養，未呈現前後端開發實務，不以協作等同實作。 |

#### 4. HR 十二問／HM 十三問

| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 人力銀行企業端招募系統專案負責人 | HR Tech及系統規劃直接相關 |
| HR02 | supported | 同時持續迭代現行服務 | 近期兼顧改版與既有客戶 |
| HR03 | supported | 由我主責規劃 | 規劃責任清楚，工程實作另屬團隊 |
| HR04 | partial | 平均處理時間由 100.4 天降至 30.9 天 | 變化明確，核對母體與口徑 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 有實際優先順序理由 |
| HR06 | supported | 到了企業端，更常思考的是 | 由消費產品轉企業流程脈絡清楚 |
| HR07 | supported | 與 CodaPay 新加坡技術團隊協調串接 | 跨國技術協作有情境 |
| HR08 | supported | 資深產品經理｜Senior Product Manager | 主軸明確，部分內容重複 |
| HR09 | partial | 依目前掌握的情況 | 安全改善屬觀察，需核對紀錄 |
| HR10 | supported | 承擔更完整的問題定義、方向選擇與成效責任 | 方向與產品職相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公 | 地點無已知衝突，語文文件待核對 |
| HR12 | supported | 定義使用情境與驗收標準 | 支持面試，非錄取率預測 |
| HM01 | supported | 人力銀行企業端招募系統專案負責人 | HR Tech直接對應，CMS差異可學 |
| HM02 | partial | 廠商反映的溝通中斷問題 | 訪談具體改變待核對 |
| HM03 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 可用進行中案例核對取捨 |
| HM04 | supported | 團隊依結果決定採用低價 | 有商業判斷；本職不強求P&L |
| HM05 | partial | 平均處理時間由 100.4 天降至 30.9 天 | 核對母體與混雜限制 |
| HM06 | supported | 再與 QA 制定 UAT 驗收案例、排定上線計畫 | 本人規劃與團隊交付可分 |
| HM07 | supported | 處理新舊系統並行的相容性需求 | 具新舊系統銜接實例 |
| HM08 | supported | 從舊帳號信箱並非唯一值的限制出發 | 技術規則可面試深入 |
| HM09 | supported | 帶領 2 名直屬產品企劃 | 不以人數年資直接決定Level |
| HM10 | supported | 工作涵蓋系統分析、流程與畫面設計、PRD、Prototype、UAT 與上線計畫 | 重點可讀，重複屬編輯事項 |
| HM11 | supported | 並依客服測試回饋調整推薦規則 | 具回饋修正，可追問成效 |
| HM12 | supported | 上線公司簡介生成、職缺工作說明生成及 AI 推薦人才 | 值得約談並看文件作品 |
| HM13 | supported | 現行以 Kanban 推進瀑布式開發 | 依凍結準則，不當真人效度 |

#### 5. 約談理由（≤3）與關鍵缺口（≤3）

| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「人力銀行企業端招募系統專案負責人」直接支持HR Tech流程經驗。 |
| 2 | 「定義使用情境與驗收標準」支持生成式AI產品協作。 |
| 3 | 「搜尋結果頁的既有痛點，也排在新功能職缺健檢之前」顯示需求取捨。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 量測口徑與實驗限制：追問案件母體及跨平台混雜。 | 展示一份PRD、流程圖及User Story，說明訪談如何改變需求。 |
| 2 | 英文規格及工具實務：追問英文PRD與Jira／類似工具操作。 | 案件週期起訖、母體件數、案件組成及限制是什麼？ |
| 3 | 訪談與AI編排深度：追問如何改變需求與prompt驗收。 | 跨平台價格實驗如何處理混雜，為何採低價？ |

#### 6. 評語（給寫稿者的具體回饋）

**做得好（3 點）**

- 1111經歷｜「整理帳號權限、職缺關聯與既有資料轉換規則」｜支持本職系統流程與範圍規劃。
- 1111經歷｜「定義使用情境與驗收標準」｜支持生成式AI功能與工程合作。
- 1111經歷｜「搜尋結果頁的既有痛點，也排在新功能職缺健檢之前」｜支持roadmap取捨。

**可改進（≤5 點）**

- 位置：Product Owner／PM｜1111 全球華人
  - 原句：「平均處理時間由 100.4 天降至 30.9 天」
  - 問題類型：`measurement`
  - 嚴重度：`interview_follow_up`
  - 影響：有期間與前後值，但件數、起訖及清理積案後組成未知；不能全歸本人因果。 量測口徑待面試核對
  - 建議方向：補案件數、起訖定義、分布與案件組成。

- 位置：Product Manager｜尚凡國際創新科技
  - 原句：「以售價不變的 Android 作對照」
  - 問題類型：`measurement`
  - 嚴重度：`interview_follow_up`
  - 影響：跨平台分期比較有判斷價值，但非隨機AB證據，促銷及用戶結構差異未知。 對照實驗不直接視為隨機AB
  - 建議方向：補樣本、同期活動、平台差異與決策限制。

- 位置：專業技能
  - 原句：「並以英文進行跨國協作」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：協作與翻譯支持語言能力，但不等於英文產品規格實績；Notion已列，Jira未知。 必要工具與英文文件尚待核對
  - 建議方向：面試展示英文產品文件，說明工具操作與遷移能力。

- 位置：專業技能
  - 原句：「以 Claude Code 建立協作流程與共用 skill」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：有AI協作與生成產品，尚無prompt版本、內容編排及品質評估細節。 生成式AI加分深度未完整呈現
  - 建議方向：展示本人設計的prompt或編排與品質驗收方式。

**編輯附件**：無。

#### 7. 資深能力分布

delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

#### 8. 未測試聲明

PDF 抽字：本內容審查 `not_tested`（另見總報告 §6 的 `local_extraction`）／ATS 匯入：`not_tested`／AI 作者判讀：不可由文字判定／真人校準：`not_run`。

### A.04｜jd14｜原始單行 JSON

```json
{"rubric_version":"4.2","resume_id":"appendix-A-v10.2","job_id":"jd14","job_input":"summary","model_id":"unknown","run_id":"jd14-A-01","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上Growth PM","type":"required","status":"partial","evidence":["Product Manager｜尚凡國際創新科技","2018/01 - 2022/03"],"blocks_interview":false,"reason":"逾三年消費型產品PM經驗並有成長案例；未交代三年以上持續Growth責任及指標範圍。"},{"id":"R02","text":"Acquisition／Activation／Retention全生命週期Growth Funnel","type":"required","status":"partial","evidence":["配合行銷導入既有用戶","規劃使用流程、訂閱與付費機制"],"blocks_interview":false,"reason":"有導流及付費流程經驗；獲客來源、啟動與留存漏斗串接及長期責任未呈現。"},{"id":"R03","text":"訂閱會員轉換與付費轉換","type":"required","status":"supported","evidence":["另規劃並上線 VIP 訂閱、點數付費牆與精選曝光"],"blocks_interview":false,"reason":"具訂閱及付費機制交付；實際會員轉換率需面試核對。"},{"id":"R04","text":"用戶成長、留存與營收成效","type":"required","status":"partial","evidence":["男性 DAU 在 6 週內由約 3,200 增至 1.25 萬"],"blocks_interview":false,"reason":"有活躍及營收變化；DAU含服務承接與行銷，留存結果未提供。"},{"id":"R05","text":"新成長機會與商業模式","type":"required","status":"supported","evidence":["設計刊案、報名、邀約與聯繫流程","另規劃並上線 VIP 訂閱、點數付費牆與精選曝光"],"blocks_interview":false,"reason":"雙邊媒合及多種付費機制可轉移；影音情境可於面試驗證。"},{"id":"R06","text":"A/B Test產品實驗","type":"required","status":"partial","evidence":["以售價不變的 Android 作對照"],"blocks_interview":false,"reason":"有跨平台對照、時序定價實驗及採用決策；非已證實隨機分流A/B，需核對實驗設計能力。"},{"id":"R07","text":"獨立PRD、User Flow、Wireframe與跨部門交付","type":"required","status":"supported","evidence":["由我主責規劃","設計流程與畫面、撰寫 PRD 與製作 Prototype","Wireframe"],"blocks_interview":false,"reason":"主責案例支持流程與文件獨立規劃；Wireframe列於技能，可面試看作品。"},{"id":"R08","text":"熟悉GA4、Firebase","type":"required","status":"partial","evidence":["GA4"],"blocks_interview":false,"reason":"GA4僅技能清單，熟悉程度未知；Firebase未呈現。非有不符證據。"},{"id":"R09","text":"數據分析","type":"required","status":"supported","evidence":["依序測試原價、降價與還原原價","與 DBA 協作取數"],"blocks_interview":false,"reason":"定價比較與取數分析流程具案例，可追問口徑及因果限制。"},{"id":"R10","text":"跨部門溝通","type":"required","status":"supported","evidence":["與工程、設計、行銷及海外金流團隊協作完成上線"],"blocks_interview":false,"reason":"多職能與跨國金流上線案例直接相關。"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["經手交友、訂閱制內容 App 與網紅媒合平台"],"missing":["近期企業端經驗需轉接影音用戶成長；Growth年資責任待核對。"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"足夠","evidence":["另規劃並上線 VIP 訂閱、點數付費牆與精選曝光"],"missing":["Firebase未呈現、GA4實用深度及隨機A/B待核對。"],"issue_ids":["I02","I03"]},{"id":"decision_depth","rating":"足夠","evidence":["團隊依結果決定採用低價","搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"missing":["定價的替代解釋、本人決策權及漏斗權衡待釐清。"],"issue_ids":["I03"]},{"id":"outcome_quality","rating":"待補","evidence":["網頁付款占營收由 24% 升至 80% 以上"],"missing":["缺轉換、留存口徑；渠道占比不等營收增長，DAU歸因待核對。"],"issue_ids":["I04","I05"]},{"id":"ownership","rating":"足夠","evidence":["由我主責規劃","與工程、設計、行銷及海外金流團隊協作完成上線"],"missing":["成長目標、預算與團隊資源決策權未清楚。"],"issue_ids":["I01"]},{"id":"readability","rating":"強","evidence":["工作涵蓋系統分析、流程與畫面設計、PRD、Prototype"],"missing":[],"issue_ids":[]}],"results":[{"quote":"另規劃並上線 VIP 訂閱、點數付費牆與精選曝光","kinds":["output"]},{"quote":"男性 DAU 在 6 週內由約 3,200 增至 1.25 萬","kinds":["outcome"]},{"quote":"團隊依結果決定採用低價","kinds":["decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"兩案均在開發中","kinds":["in_progress"]},{"quote":"平均處理時間由 100.4 天降至 30.9 天","kinds":["outcome"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["規劃使用流程、訂閱與付費機制"],"application_note":"訂閱付費經驗支持面試；工具待核對。"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 Product Owner"],"application_note":"近期B2B交付與過往B2C成長並存。"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我主責規劃"],"application_note":"本人規劃與協作交付範圍清楚。"},{"rule_id":"HR04","status":"partial","resume_evidence":["網頁付款占營收由 24% 升至 80% 以上"],"application_note":"占比改變成立；不直接等於新增營收。"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"application_note":"有優先級依據；可追問成長取捨。"},{"rule_id":"HR06","status":"supported","resume_evidence":["從 SweetRing 的海外市場開始累積產品經驗"],"application_note":"由海外消費產品轉企業系統。"},{"rule_id":"HR07","status":"partial","resume_evidence":["GA4"],"application_note":"工具有線索；Firebase與實用深度待問。"},{"rule_id":"HR08","status":"supported","resume_evidence":["工作涵蓋系統分析、流程與畫面設計、PRD、Prototype"],"application_note":"結構清楚，成長案例可快速定位。"},{"rule_id":"HR09","status":"partial","resume_evidence":["以售價不變的 Android 作對照"],"application_note":"需查實驗口徑及同期變因。"},{"rule_id":"HR10","status":"supported","resume_evidence":["我希望把更多心力放回產品策略"],"application_note":"策略及成效方向與成長職位相容。"},{"rule_id":"HR11","status":"supported","resume_evidence":["可接受遠端或混合辦公"],"application_note":"工作方式相容，無已知條件衝突。"},{"rule_id":"HR12","status":"supported","resume_evidence":["團隊依結果決定採用低價"],"application_note":"支持約談；補工具及留存案例。"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["經手交友、訂閱制內容 App 與網紅媒合平台"],"evidence_type":"context","source_ids":[],"interview_question":"如何把訂閱社交產品經驗轉用影音會員成長？"},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"partial","resume_evidence":["依使用者旅程與工單問題安排優先級"],"evidence_type":"decision","source_ids":[],"interview_question":"哪些資料改變過你的啟動或留存方案？"},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["團隊依結果決定採用低價"],"evidence_type":"decision","source_ids":[],"interview_question":"定價結果如何權衡留存、長期價值及毛利？"},{"rule_id":"HM04","primary_dimension":"role_evidence","status":"supported","resume_evidence":["另規劃並上線 VIP 訂閱、點數付費牆與精選曝光"],"evidence_type":"output","source_ids":[],"interview_question":"商業模式如何選擇，如何評估採用與收入？"},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":"渠道轉移前後總營收、轉換及留存如何變化？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["與工程、設計、行銷及海外金流團隊協作完成上線"],"evidence_type":"output","source_ids":[],"interview_question":"成長專案中你、行銷與工程的責任如何劃分？"},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["再與 QA 制定 UAT 驗收案例、排定上線計畫"],"evidence_type":"output","source_ids":[],"interview_question":"付費實驗如何定義驗收與上線回滾條件？"},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"partial","resume_evidence":["GA4"],"evidence_type":"context","source_ids":[],"interview_question":"請展示GA4事件漏斗設計；是否實際使用Firebase？"},{"rule_id":"HM09","primary_dimension":"ownership","status":"partial","resume_evidence":["由我主責規劃"],"evidence_type":"context","source_ids":[],"interview_question":"你持有過哪些成長目標、資源與決策權？"},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["規劃使用流程、訂閱與付費機制"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["並依客服測試回饋調整推薦規則"],"evidence_type":"decision","source_ids":[],"interview_question":"一次反證如何改變你的產品實驗設計？"},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以售價不變的 Android 作對照"],"evidence_type":"decision","source_ids":[],"interview_question":"請用一項實驗作品核對分流、指標及判讀。"},{"rule_id":"HM13","primary_dimension":"method","status":"supported","resume_evidence":["兩案均在開發中"],"evidence_type":"in_progress","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"面試核對成長職能與量測，不直接淘汰。","context_limit":"未呈現不等於未做；影響Growth資歷深度核對。","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"規劃使用流程、訂閱與付費機制","reason":"消費產品經驗期間超過三年，但完整Growth漏斗與目標權責未明。","suggestion":"補各年度成長責任、Activation與Retention案例。"},{"id":"I02","rule_id":"HM08","source_ids":[],"application_note":"面試核對成長職能與量測，不直接淘汰。","context_limit":"工具未知可面試釐清，不以未知判不符。","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"GA4","reason":"GA4只有清單線索；Firebase未出現，無法證成熟悉程度。","suggestion":"補GA4與Firebase實際操作、事件設計與分析作品。"},{"id":"I03","rule_id":"HM03","source_ids":[],"application_note":"面試核對成長職能與量測，不直接淘汰。","context_limit":"實驗能支持決策；因果強度與A/B能力需另核對。","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"以售價不變的 Android 作對照","reason":"跨平台且依序比較，未證實隨機分流A/B與同期控制充分。","suggestion":"補樣本、分流、平台差異、指標及採用低價權責。"},{"id":"I04","rule_id":"HM05","source_ids":[],"application_note":"面試核對成長職能與量測，不直接淘汰。","context_limit":"已有期間及占比，不否定其渠道交付。","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"網頁付款占營收由 24% 升至 80% 以上","reason":"渠道占比變動不能單獨證實總營收、轉換或留存改善。","suggestion":"補總營收、毛利、付費轉換及留存的期間分母。"},{"id":"I05","rule_id":"HM05","source_ids":[],"application_note":"面試核對成長職能與量測，不直接淘汰。","context_limit":"觀察到成長可用；不全歸產品或本人。","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"男性 DAU 在 6 週內由約 3,200 增至 1.25 萬","reason":"DAU發生於承接服務與行銷導流期間，未拆新增、搬移與持續留存。","suggestion":"補用戶來源、啟動與留存世代及本人影響邊界。"}],"decision":{"recommendation":"interview","evidence":["規劃使用流程、訂閱與付費機制","團隊依結果決定採用低價","由我主責規劃"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"待補"},"interview_reasons":["「規劃使用流程、訂閱與付費機制」支持訂閱轉換職能。","「團隊依結果決定採用低價」提供數據導向決策案例。","「由我主責規劃」及跨職能上線案例支持獨立交付。"],"key_gaps":["完整漏斗及三年以上Growth責任待核對：請說明Activation與Retention目標。","GA4深度與Firebase未知：請展示埋點、漏斗及實際工具操作。","A/B因果與成長衡量待補：請提供分流、轉換留存及渠道變動分母。"],"strengths":["訂閱、付費牆與渠道調整案例直接對應變現。","定價實驗有期間、對照與採用決策。","主責規格、流程及跨部門交付證據明確。"],"interview_questions":["如何把訂閱社交產品經驗轉用影音會員成長？","哪些資料改變過你的啟動或留存方案？","定價結果如何權衡留存、長期價值及毛利？","商業模式如何選擇，如何評估採用與收入？","渠道轉移前後總營收、轉換及留存如何變化？","成長專案中你、行銷與工程的責任如何劃分？","付費實驗如何定義驗收與上線回滾條件？","請展示GA4事件漏斗設計；是否實際使用Firebase？"],"editorial_appendix":[],"spectrum":{"level":7,"uncertainty_levels":1,"basis":"多個訂閱變現、數據決策與獨立交付案例支持面試；完整Growth漏斗、工具實用與因果衡量限制未清，不足支持8或9。"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"not_tested","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 單份審查｜履歷 appendix-A-v10.2｜第 4 輪｜model_id: unknown

#### 1. 結論

- 招聘決定：`interview`
- Level：7（±1）
- 一句話理由：「規劃使用流程、訂閱與付費機制」支持面試，缺口依下表核對。

#### 2. 六維度

| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 經手交友、訂閱制內容 App 與網紅媒合平台 | 近期企業端經驗需轉接影音用戶成長；Growth年資責任待核對。 |
| role_evidence | 足夠 | 另規劃並上線 VIP 訂閱、點數付費牆與精選曝光 | Firebase未呈現、GA4實用深度及隨機A/B待核對。 |
| decision_depth | 足夠 | 團隊依結果決定採用低價；搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 定價的替代解釋、本人決策權及漏斗權衡待釐清。 |
| outcome_quality | 待補 | 網頁付款占營收由 24% 升至 80% 以上 | 缺轉換、留存口徑；渠道占比不等營收增長，DAU歸因待核對。 |
| ownership | 足夠 | 由我主責規劃；與工程、設計、行銷及海外金流團隊協作完成上線 | 成長目標、預算與團隊資源決策權未清楚。 |
| readability | 強 | 工作涵蓋系統分析、流程與畫面設計、PRD、Prototype | 無新增缺口；以現有自述支持面試。 |

#### 3. JD 條件對照

| 條件 | 必要／加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 3年以上Growth PM | 必要 | partial | Product Manager｜尚凡國際創新科技；2018/01 - 2022/03 | 逾三年消費型產品PM經驗並有成長案例；未交代三年以上持續Growth責任及指標範圍。 |
| Acquisition／Activation／Retention全生命週期Growth Funnel | 必要 | partial | 配合行銷導入既有用戶；規劃使用流程、訂閱與付費機制 | 有導流及付費流程經驗；獲客來源、啟動與留存漏斗串接及長期責任未呈現。 |
| 訂閱會員轉換與付費轉換 | 必要 | supported | 另規劃並上線 VIP 訂閱、點數付費牆與精選曝光 | 具訂閱及付費機制交付；實際會員轉換率需面試核對。 |
| 用戶成長、留存與營收成效 | 必要 | partial | 男性 DAU 在 6 週內由約 3,200 增至 1.25 萬 | 有活躍及營收變化；DAU含服務承接與行銷，留存結果未提供。 |
| 新成長機會與商業模式 | 必要 | supported | 設計刊案、報名、邀約與聯繫流程；另規劃並上線 VIP 訂閱、點數付費牆與精選曝光 | 雙邊媒合及多種付費機制可轉移；影音情境可於面試驗證。 |
| A/B Test產品實驗 | 必要 | partial | 以售價不變的 Android 作對照 | 有跨平台對照、時序定價實驗及採用決策；非已證實隨機分流A/B，需核對實驗設計能力。 |
| 獨立PRD、User Flow、Wireframe與跨部門交付 | 必要 | supported | 由我主責規劃；設計流程與畫面、撰寫 PRD 與製作 Prototype；Wireframe | 主責案例支持流程與文件獨立規劃；Wireframe列於技能，可面試看作品。 |
| 熟悉GA4、Firebase | 必要 | partial | GA4 | GA4僅技能清單，熟悉程度未知；Firebase未呈現。非有不符證據。 |
| 數據分析 | 必要 | supported | 依序測試原價、降價與還原原價；與 DBA 協作取數 | 定價比較與取數分析流程具案例，可追問口徑及因果限制。 |
| 跨部門溝通 | 必要 | supported | 與工程、設計、行銷及海外金流團隊協作完成上線 | 多職能與跨國金流上線案例直接相關。 |

#### 4. HR 十二問／HM 十三問

| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 規劃使用流程、訂閱與付費機制 | 訂閱付費經驗支持面試；工具待核對。 |
| HR02 | supported | 現任 1111 招募系統 Product Owner | 近期B2B交付與過往B2C成長並存。 |
| HR03 | supported | 由我主責規劃 | 本人規劃與協作交付範圍清楚。 |
| HR04 | partial | 網頁付款占營收由 24% 升至 80% 以上 | 占比改變成立；不直接等於新增營收。 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 有優先級依據；可追問成長取捨。 |
| HR06 | supported | 從 SweetRing 的海外市場開始累積產品經驗 | 由海外消費產品轉企業系統。 |
| HR07 | partial | GA4 | 工具有線索；Firebase與實用深度待問。 |
| HR08 | supported | 工作涵蓋系統分析、流程與畫面設計、PRD、Prototype | 結構清楚，成長案例可快速定位。 |
| HR09 | partial | 以售價不變的 Android 作對照 | 需查實驗口徑及同期變因。 |
| HR10 | supported | 我希望把更多心力放回產品策略 | 策略及成效方向與成長職位相容。 |
| HR11 | supported | 可接受遠端或混合辦公 | 工作方式相容，無已知條件衝突。 |
| HR12 | supported | 團隊依結果決定採用低價 | 支持約談；補工具及留存案例。 |
| HM01 | supported | 經手交友、訂閱制內容 App 與網紅媒合平台 | 消費訂閱可轉移；影音差異面試核對。 |
| HM02 | partial | 依使用者旅程與工單問題安排優先級 | 使用者線索有，漏斗洞察待補。 |
| HM03 | supported | 團隊依結果決定採用低價 | 有採用決策，需核對權衡。 |
| HM04 | supported | 另規劃並上線 VIP 訂閱、點數付費牆與精選曝光 | 多種變現模式可轉移。 |
| HM05 | partial | 網頁付款占營收由 24% 升至 80% 以上 | 渠道占比與總成長分開。 |
| HM06 | supported | 與工程、設計、行銷及海外金流團隊協作完成上線 | 跨職能分工清楚，成長權責待問。 |
| HM07 | supported | 再與 QA 制定 UAT 驗收案例、排定上線計畫 | 規格驗收上線支持交付。 |
| HM08 | partial | GA4 | GA4深度與Firebase待核對。 |
| HM09 | partial | 由我主責規劃 | 交付強，方向資源權責待補。 |
| HM10 | supported | 規劃使用流程、訂閱與付費機制 | 可定位相關經驗。 |
| HM11 | supported | 並依客服測試回饋調整推薦規則 | 回饋修正有案例。 |
| HM12 | supported | 以售價不變的 Android 作對照 | 作品可驗證實驗深度。 |
| HM13 | supported | 兩案均在開發中 | 依JD獨立判讀；未將進行中當成果。 |

#### 5. 約談理由（≤3）與關鍵缺口（≤3）

| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「規劃使用流程、訂閱與付費機制」支持訂閱轉換職能。 |
| 2 | 「團隊依結果決定採用低價」提供數據導向決策案例。 |
| 3 | 「由我主責規劃」及跨職能上線案例支持獨立交付。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 完整漏斗及三年以上Growth責任待核對：請說明Activation與Retention目標。 | 如何把訂閱社交產品經驗轉用影音會員成長？ |
| 2 | GA4深度與Firebase未知：請展示埋點、漏斗及實際工具操作。 | 哪些資料改變過你的啟動或留存方案？ |
| 3 | A/B因果與成長衡量待補：請提供分流、轉換留存及渠道變動分母。 | 定價結果如何權衡留存、長期價值及毛利？ |

#### 6. 評語（給寫稿者的具體回饋）

**做得好（3 點）**

- Product Manager｜尚凡國際創新科技｜「經手交友、訂閱制內容 App 與網紅媒合平台」｜訂閱、付費牆與渠道調整案例直接對應變現。
- Product Manager｜尚凡國際創新科技｜「另規劃並上線 VIP 訂閱、點數付費牆與精選曝光」｜定價實驗有期間、對照與採用決策。
- Product Manager｜尚凡國際創新科技｜「團隊依結果決定採用低價」｜主責規格、流程及跨部門交付證據明確。

**可改進（≤5 點）**

- 位置：Product Manager｜尚凡國際創新科技
  - 原句：「規劃使用流程、訂閱與付費機制」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：消費產品經驗期間超過三年，但完整Growth漏斗與目標權責未明。 面試核對成長職能與量測，不直接淘汰。
  - 建議方向：補各年度成長責任、Activation與Retention案例。

- 位置：專業技能
  - 原句：「GA4」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：GA4只有清單線索；Firebase未出現，無法證成熟悉程度。 面試核對成長職能與量測，不直接淘汰。
  - 建議方向：補GA4與Firebase實際操作、事件設計與分析作品。

- 位置：Product Manager｜尚凡國際創新科技
  - 原句：「以售價不變的 Android 作對照」
  - 問題類型：`measurement`
  - 嚴重度：`interview_follow_up`
  - 影響：跨平台且依序比較，未證實隨機分流A/B與同期控制充分。 面試核對成長職能與量測，不直接淘汰。
  - 建議方向：補樣本、分流、平台差異、指標及採用低價權責。

- 位置：專業摘要
  - 原句：「網頁付款占營收由 24% 升至 80% 以上」
  - 問題類型：`measurement`
  - 嚴重度：`interview_follow_up`
  - 影響：渠道占比變動不能單獨證實總營收、轉換或留存改善。 面試核對成長職能與量測，不直接淘汰。
  - 建議方向：補總營收、毛利、付費轉換及留存的期間分母。

- 位置：Product Manager｜尚凡國際創新科技
  - 原句：「男性 DAU 在 6 週內由約 3,200 增至 1.25 萬」
  - 問題類型：`measurement`
  - 嚴重度：`interview_follow_up`
  - 影響：DAU發生於承接服務與行銷導流期間，未拆新增、搬移與持續留存。 面試核對成長職能與量測，不直接淘汰。
  - 建議方向：補用戶來源、啟動與留存世代及本人影響邊界。

**編輯附件**：無。

#### 7. 資深能力分布

delivery：強 ／ po_coordination：強 ／ direction_resources：待補

#### 8. 未測試聲明

PDF 抽字：本內容審查 `not_tested`（另見總報告 §6 的 `local_extraction`）／ATS 匯入：`not_tested`／AI 作者判讀：不可由文字判定／真人校準：`not_run`。

### A.05｜jd20｜原始單行 JSON

```json
{"rubric_version":"4.2","resume_id":"appendix-A-v10.2","job_id":"jd20","job_input":"summary","model_id":"unknown","run_id":"jd20-A-01","human_calibrated":false,"requirements":[{"id":"R01","text":"5–8年以上B2B/B2G產品或專案管理；經歷欄5年以上","type":"required","status":"partial","evidence":["人力銀行企業端招募系統專案負責人"],"blocks_interview":false,"reason":"總PM年資符合；企業招募系統自2022/08起約4年，KOOL案主端是否計入B2B及期間未明，不能直接判年資不符。"},{"id":"R02","text":"近母語英語口說與寫作","type":"required","status":"partial","evidence":["並以英文進行跨國協作"],"blocks_interview":false,"reason":"英文測驗及跨國合作有支持，但不足證成近母語口寫，需實際驗證。"},{"id":"R03","text":"溝通與關係人管理、跨部門協作、各市場客戶及BD需求澄清","type":"required","status":"supported","evidence":["對接工程、行銷、業務與客服等 10 個需求單位"],"blocks_interview":false,"reason":"內外需求與大型客戶分工情境具體；海外BD需求實務可追問。"},{"id":"R04","text":"需求、roadmap、PRD、待辦優先級；設計實作測試發布；時程風險品質與RD/QA/AI交付","type":"required","status":"supported","evidence":["再與 QA 制定 UAT 驗收案例、排定上線計畫"],"blocks_interview":false,"reason":"規格到分階段發布及相容性風險有案例；AI驗收有具體責任。"},{"id":"R05","text":"強數據敏感度，能獨立以SQL/BI/試算表查詢、解讀與分析","type":"required","status":"partial","evidence":["與 DBA 協作取數，再以 Google Sheets、Excel 分析"],"blocks_interview":false,"reason":"試算表分析與對照實驗支持；獨立取得及查詢資料能力未知，協作取數不等於不會。"},{"id":"R06","text":"Claude等AI工具工作流整合，串接Jira/Confluence自動化","type":"required","status":"partial","evidence":["以 Claude Code 建立協作流程與共用 skill"],"blocks_interview":false,"reason":"AI流程整合有線索；未呈現Jira/Confluence串接自動化，需核對可轉用程度。"},{"id":"R07","text":"對防詐與風險議題有熱情","type":"required","status":"unknown","evidence":["廠商招募帳號遭冒用，帶來求職者個資外洩風險"],"blocks_interview":false,"reason":"有相關處理經驗，未表達投入防詐領域的動機，不能由任務推定熱情。"},{"id":"R08","text":"防詐、資安、風險或信任產品經驗","type":"preferred","status":"supported","evidence":["於 2026/04 完成登入驗證調整"],"blocks_interview":false,"reason":"帳號冒用與個資風險處理直接相關，但不是完整防詐產品經驗。"},{"id":"R09","text":"企業或政府客戶，尤其SEA、日本、韓國市場","type":"preferred","status":"partial","evidence":["推進 SweetRing 在美國、墨西哥、巴西、印尼、馬來西亞、日本與韓國"],"blocks_interview":false,"reason":"企業端與指定海外市場各有經驗；未呈現當地企業政府客戶，不能合併當成同一經驗。"},{"id":"R10","text":"技術背景或密切RD/AI團隊協作","type":"preferred","status":"supported","evidence":["定義使用情境與驗收標準"],"blocks_interview":false,"reason":"系統改版、資料規則、資料科學團隊驗收及推薦規則調整支持。"},{"id":"R11","text":"Agile/Scrum/Jira","type":"preferred","status":"partial","evidence":["曾參與每週一個 Sprint 的 Scrum"],"blocks_interview":false,"reason":"Scrum有使用敘述與現行Kanban方式；Jira未呈現。"},{"id":"R12","text":"定價、報價、成本與利潤","type":"preferred","status":"partial","evidence":["整理抽成、稅、手續費與撥款週期，完成實收試算"],"blocks_interview":false,"reason":"定價實驗與成本實收計算具體；企業報價及利潤責任未呈現。"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["現任 1111 招募系統 Product Owner"],"missing":["B2B年資認定、對防詐職涯動機需釐清"],"issue_ids":["I01","I05"]},{"id":"role_evidence","rating":"待補","evidence":["以 Claude Code 建立協作流程與共用 skill"],"missing":["近母語英語、獨立查詢、指定自動化串接為核心資格待核對"],"issue_ids":["I01","I02","I03","I04","I05"]},{"id":"decision_depth","rating":"強","evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。"],"missing":["可追問優先級依據、定價實驗混雜因素"],"issue_ids":[]},{"id":"outcome_quality","rating":"足夠","evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天。"],"missing":["案件數、納入規則及同類冒用監測範圍"],"issue_ids":["I06"]},{"id":"ownership","rating":"強","evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃。"],"missing":["完整roadmap與資源配置最終權責仍可追問"],"issue_ids":[]},{"id":"readability","rating":"足夠","evidence":["工作涵蓋系統分析、流程與畫面設計、PRD、Prototype、UAT 與上線計畫"],"missing":["摘要、自傳重複，核心資格可更明確標示"],"issue_ids":[]}],"results":[{"quote":"系統服務逾 6 萬家活躍付費廠商（2026 Q3）","kinds":["context"]},{"quote":"與工程於 2025/09 完成上線。","kinds":["output"]},{"quote":"兩案均在開發中","kinds":["decision","in_progress"]},{"quote":"調整後至 2026/10 未再出現同類冒用。","kinds":["outcome"]},{"quote":"平均處理時間由 100.4 天降至 30.9 天。","kinds":["outcome"]},{"quote":"團隊依結果決定採用低價。","kinds":["decision"]}],"hr_questions":[{"rule_id":"HR01","status":"partial","resume_evidence":["現任 1111 招募系統 Product Owner"],"application_note":"企業端相關；核心資格需核對"},{"rule_id":"HR02","status":"supported","resume_evidence":["人力銀行企業端招募系統專案負責人"],"application_note":"企業流程可轉移至2B產品"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我主責規劃"],"application_note":"本人規劃與工程交付邊界可辨"},{"rule_id":"HR04","status":"partial","resume_evidence":["平均處理時間由 100.4 天降至 30.9 天。"],"application_note":"有成果；分母及組成仍需核對"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。"],"application_note":"有優先次序及問題依據"},{"rule_id":"HR06","status":"supported","resume_evidence":["到了企業端，更常思考的是"],"application_note":"消費產品轉企業流程脈絡清楚"},{"rule_id":"HR07","status":"partial","resume_evidence":["與 DBA 協作取數"],"application_note":"使用情境具體；獨立查詢未明"},{"rule_id":"HR08","status":"supported","resume_evidence":["資深產品經理｜Senior Product Manager"],"application_note":"近期責任與代表作可辨"},{"rule_id":"HR09","status":"partial","resume_evidence":["依目前掌握的情況"],"application_note":"觀察範圍與來源需面試釐清"},{"rule_id":"HR10","status":"partial","resume_evidence":["我希望把更多心力放回產品策略"],"application_note":"方向相容；50%專案投入需確認"},{"rule_id":"HR11","status":"partial","resume_evidence":["並以英文進行跨國協作"],"application_note":"近母語要求尚待口寫驗證"},{"rule_id":"HR12","status":"partial","resume_evidence":["定義使用情境與驗收標準"],"application_note":"有面試價值；先核對核心資格"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"partial","resume_evidence":["人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":"企業端年資與KOOL案主服務期間各多久？"},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["廠商反映的溝通中斷問題"],"evidence_type":"decision","source_ids":[],"interview_question":"工單與旅程證據如何決定優先修整合？"},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。"],"evidence_type":"decision","source_ids":[],"interview_question":"優先級如何比較價值、成本與風險？"},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["團隊依結果決定採用低價。"],"evidence_type":"decision","source_ids":[],"interview_question":"定價實驗如何排除同期混雜因素？"},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["平均處理時間由 100.4 天降至 30.9 天。"],"evidence_type":"outcome","source_ids":[],"interview_question":"兩季案件分母與結案納入規則為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["與內部工程團隊分階段交付"],"evidence_type":"output","source_ids":[],"interview_question":"roadmap、人力與時程由誰最終拍板？"},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["處理新舊系統並行的相容性需求。"],"evidence_type":"output","source_ids":[],"interview_question":"發布門檻、回滾與QA責任怎麼定？"},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["整理帳號權限、職缺關聯與既有資料轉換規則"],"evidence_type":"output","source_ids":[],"interview_question":"規則衝突如何與RD確認並驗收？"},{"rule_id":"HM09","primary_dimension":"ownership","status":"supported","resume_evidence":["重新制定業務流程、對照資料欄位並重構規格"],"evidence_type":"output","source_ids":[],"interview_question":"哪些方向與資源取捨可自主決定？"},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["並依客服測試回饋調整推薦規則。"],"evidence_type":"decision","source_ids":[],"interview_question":"哪條回饋改變了規則與驗收？"},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"partial","resume_evidence":["與 DBA 協作取數"],"evidence_type":"context","source_ids":[],"interview_question":"能否展示獨立查詢與AI串接自動化案例？"},{"rule_id":"HM13","primary_dimension":"method","status":"supported","resume_evidence":["兩案均在開發中"],"evidence_type":"in_progress","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"先核對核心資格再決定約談","context_limit":"文件未呈現不等於能力不符","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"人力銀行企業端招募系統專案負責人","reason":"清楚可辨企業端約4年，未能確認達必要B2B/B2G五年以上。","suggestion":"補KOOL案主端產品責任與起迄期間；核對JD年資採認。"},{"id":"I02","rule_id":"HR11","source_ids":[],"application_note":"先核對核心資格再決定約談","context_limit":"文件未呈現不等於能力不符","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"並以英文進行跨國協作","reason":"工作英語不直接證成近母語口寫。","suggestion":"以英文需求討論及短PRD樣本核對。"},{"id":"I03","rule_id":"HM12","source_ids":[],"application_note":"先核對核心資格再決定約談","context_limit":"文件未呈現不等於能力不符","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"與 DBA 協作取數","reason":"已支持試算表分析，獨立查詢仍未知。","suggestion":"提供自行取數查詢與分析範例，釐清DBA協作邊界。"},{"id":"I04","rule_id":"HM08","source_ids":[],"application_note":"先核對核心資格再決定約談","context_limit":"文件未呈現不等於能力不符","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"以 Claude Code 建立協作流程與共用 skill","reason":"未呈現Jira/Confluence實際串接與自動化。","suggestion":"補流程輸入輸出、API串接、例外處理及本人實作邊界。"},{"id":"I05","rule_id":"HR10","source_ids":[],"application_note":"先核對核心資格再決定約談","context_limit":"文件未呈現不等於能力不符","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"我希望把更多心力放回產品策略","reason":"未表達防詐風險領域投入動機；不能推定無興趣。","suggestion":"說明防詐動機與接受一半專案交付的原因。"},{"id":"I06","rule_id":"HM05","source_ids":[],"application_note":"先核對核心資格再決定約談","context_limit":"不推定零事件或單一改動的因果效果","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"依目前掌握的情況，調整後至 2026/10 未再出現同類冒用。","reason":"這是掌握範圍內的觀察，非完整監測；案件週期亦缺分母及組成。","suggestion":"補冒用回報來源與涵蓋範圍、兩季案件量與納入規則。"}],"decision":{"recommendation":"clarify_first","evidence":["人力銀行企業端招募系統專案負責人","與 DBA 協作取數","以 Claude Code 建立協作流程與共用 skill"],"blocking_unknowns":["B2B/B2G五年以上是否達標","近母語英文口寫能力","獨立資料查詢及指定AI自動化串接適配程度","防詐風險領域動機"]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["「與內部工程團隊分階段交付」支持大型既有系統交付。","「團隊依結果決定採用低價。」支持數據導向商業取捨。","「於 2026/04 完成登入驗證調整」提供信任風險相關案例。"],"key_gaps":["資格門檻：核對B2B年資、近母語英文及防詐動機。","工具實務：追問獨立查詢及Jira/Confluence自動化串接。","量測：追問處理時間分母、案件組成與冒用觀察來源。"],"strengths":["企業系統改版從規格到分階段上線完整。","優先級及定價取捨具有具體依據。","帳號風險與AI驗收提供直接可轉移經驗。"],"interview_questions":["KOOL案主端責任期間能否連同1111達五年B2B？","請以英文說明需求取捨並提供英文PRD片段。","請展示不依賴DBA代取的查詢與試算表分析流程。","Claude流程如何串接Jira/Confluence及處理例外？","為何投入防詐領域，如何看待50%專案交付？","兩季案件平均處理時間的分母與納入規則為何？","冒用觀察來自哪些來源，哪些範圍無法監測？","定價實驗與roadmap的取捨及最終權責為何？"],"editorial_appendix":[],"spectrum":{"level":7,"uncertainty_levels":1,"basis":"多個企業交付、取捨、AI協作與風險案例支持面試價值；核心資格及量測邊界仍需核對，未達高度貼合本職。"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"not_tested","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 單份審查｜履歷 appendix-A-v10.2｜第 5 輪｜model_id: unknown

#### 1. 結論

- 招聘決定：`clarify_first`
- Level：7（±1）
- 一句話理由：「人力銀行企業端招募系統專案負責人」有相關性，核心必要條件待釐清。

#### 2. 六維度

| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 現任 1111 招募系統 Product Owner | B2B年資認定、對防詐職涯動機需釐清 |
| role_evidence | 待補 | 以 Claude Code 建立協作流程與共用 skill | 近母語英語、獨立查詢、指定自動化串接為核心資格待核對 |
| decision_depth | 強 | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。 | 可追問優先級依據、定價實驗混雜因素 |
| outcome_quality | 足夠 | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天。 | 案件數、納入規則及同類冒用監測範圍 |
| ownership | 強 | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃。 | 完整roadmap與資源配置最終權責仍可追問 |
| readability | 足夠 | 工作涵蓋系統分析、流程與畫面設計、PRD、Prototype、UAT 與上線計畫 | 摘要、自傳重複，核心資格可更明確標示 |

#### 3. JD 條件對照

| 條件 | 必要／加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 5–8年以上B2B/B2G產品或專案管理；經歷欄5年以上 | 必要 | partial | 人力銀行企業端招募系統專案負責人 | 總PM年資符合；企業招募系統自2022/08起約4年，KOOL案主端是否計入B2B及期間未明，不能直接判年資不符。 |
| 近母語英語口說與寫作 | 必要 | partial | 並以英文進行跨國協作 | 英文測驗及跨國合作有支持，但不足證成近母語口寫，需實際驗證。 |
| 溝通與關係人管理、跨部門協作、各市場客戶及BD需求澄清 | 必要 | supported | 對接工程、行銷、業務與客服等 10 個需求單位 | 內外需求與大型客戶分工情境具體；海外BD需求實務可追問。 |
| 需求、roadmap、PRD、待辦優先級；設計實作測試發布；時程風險品質與RD/QA/AI交付 | 必要 | supported | 再與 QA 制定 UAT 驗收案例、排定上線計畫 | 規格到分階段發布及相容性風險有案例；AI驗收有具體責任。 |
| 強數據敏感度，能獨立以SQL/BI/試算表查詢、解讀與分析 | 必要 | partial | 與 DBA 協作取數，再以 Google Sheets、Excel 分析 | 試算表分析與對照實驗支持；獨立取得及查詢資料能力未知，協作取數不等於不會。 |
| Claude等AI工具工作流整合，串接Jira/Confluence自動化 | 必要 | partial | 以 Claude Code 建立協作流程與共用 skill | AI流程整合有線索；未呈現Jira/Confluence串接自動化，需核對可轉用程度。 |
| 對防詐與風險議題有熱情 | 必要 | unknown | 廠商招募帳號遭冒用，帶來求職者個資外洩風險 | 有相關處理經驗，未表達投入防詐領域的動機，不能由任務推定熱情。 |
| 防詐、資安、風險或信任產品經驗 | 加分 | supported | 於 2026/04 完成登入驗證調整 | 帳號冒用與個資風險處理直接相關，但不是完整防詐產品經驗。 |
| 企業或政府客戶，尤其SEA、日本、韓國市場 | 加分 | partial | 推進 SweetRing 在美國、墨西哥、巴西、印尼、馬來西亞、日本與韓國 | 企業端與指定海外市場各有經驗；未呈現當地企業政府客戶，不能合併當成同一經驗。 |
| 技術背景或密切RD/AI團隊協作 | 加分 | supported | 定義使用情境與驗收標準 | 系統改版、資料規則、資料科學團隊驗收及推薦規則調整支持。 |
| Agile/Scrum/Jira | 加分 | partial | 曾參與每週一個 Sprint 的 Scrum | Scrum有使用敘述與現行Kanban方式；Jira未呈現。 |
| 定價、報價、成本與利潤 | 加分 | partial | 整理抽成、稅、手續費與撥款週期，完成實收試算 | 定價實驗與成本實收計算具體；企業報價及利潤責任未呈現。 |

#### 4. HR 十二問／HM 十三問

| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | partial | 現任 1111 招募系統 Product Owner | 企業端相關；核心資格需核對 |
| HR02 | supported | 人力銀行企業端招募系統專案負責人 | 企業流程可轉移至2B產品 |
| HR03 | supported | 由我主責規劃 | 本人規劃與工程交付邊界可辨 |
| HR04 | partial | 平均處理時間由 100.4 天降至 30.9 天。 | 有成果；分母及組成仍需核對 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。 | 有優先次序及問題依據 |
| HR06 | supported | 到了企業端，更常思考的是 | 消費產品轉企業流程脈絡清楚 |
| HR07 | partial | 與 DBA 協作取數 | 使用情境具體；獨立查詢未明 |
| HR08 | supported | 資深產品經理｜Senior Product Manager | 近期責任與代表作可辨 |
| HR09 | partial | 依目前掌握的情況 | 觀察範圍與來源需面試釐清 |
| HR10 | partial | 我希望把更多心力放回產品策略 | 方向相容；50%專案投入需確認 |
| HR11 | partial | 並以英文進行跨國協作 | 近母語要求尚待口寫驗證 |
| HR12 | partial | 定義使用情境與驗收標準 | 有面試價值；先核對核心資格 |
| HM01 | partial | 人力銀行企業端招募系統專案負責人 | 確認年資與企業市場轉移 |
| HM02 | supported | 廠商反映的溝通中斷問題 | 問題證據能支撐需求定義 |
| HM03 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。 | 具取捨，仍需比較成本風險 |
| HM04 | supported | 團隊依結果決定採用低價。 | 變現能力可轉移至定價 |
| HM05 | partial | 平均處理時間由 100.4 天降至 30.9 天。 | 量測分母與觀察範圍需補 |
| HM06 | supported | 與內部工程團隊分階段交付 | 規劃協作邊界清楚 |
| HM07 | supported | 處理新舊系統並行的相容性需求。 | 既有系統交付風險具體 |
| HM08 | supported | 整理帳號權限、職缺關聯與既有資料轉換規則 | 技術規則可驗收 |
| HM09 | supported | 重新制定業務流程、對照資料欄位並重構規格 | 交付與協調強，資源權責待核 |
| HM10 | supported | 約 50 項大項功能於 2023/12–2026/03 上線 | 代表作可辨 |
| HM11 | supported | 並依客服測試回饋調整推薦規則。 | 回饋有轉成規則調整 |
| HM12 | partial | 與 DBA 協作取數 | 先核對核心工具資格 |
| HM13 | supported | 兩案均在開發中 | 進行中不當成成果；未外部查證 |

#### 5. 約談理由（≤3）與關鍵缺口（≤3）

| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「與內部工程團隊分階段交付」支持大型既有系統交付。 |
| 2 | 「團隊依結果決定採用低價。」支持數據導向商業取捨。 |
| 3 | 「於 2026/04 完成登入驗證調整」提供信任風險相關案例。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 資格門檻：核對B2B年資、近母語英文及防詐動機。 | KOOL案主端責任期間能否連同1111達五年B2B？ |
| 2 | 工具實務：追問獨立查詢及Jira/Confluence自動化串接。 | 請以英文說明需求取捨並提供英文PRD片段。 |
| 3 | 量測：追問處理時間分母、案件組成與冒用觀察來源。 | 請展示不依賴DBA代取的查詢與試算表分析流程。 |

#### 6. 評語（給寫稿者的具體回饋）

**做得好（3 點）**

- 1111改版｜「與內部工程團隊分階段交付」｜適用本職需求到發布及存量風險管理。
- 尚凡定價｜「團隊依結果決定採用低價。」｜適用商業選擇與數據討論。
- 1111風險｜「於 2026/04 完成登入驗證調整」｜適用防詐與信任產品問題協作。

**可改進（≤5 點）**

- 位置：Product Owner／PM｜1111 全球華人
  - 原句：「人力銀行企業端招募系統專案負責人」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：清楚可辨企業端約4年，未能確認達必要B2B/B2G五年以上。 先核對核心資格再決定約談
  - 建議方向：補KOOL案主端產品責任與起迄期間；核對JD年資採認。

- 位置：專業技能
  - 原句：「並以英文進行跨國協作」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：工作英語不直接證成近母語口寫。 先核對核心資格再決定約談
  - 建議方向：以英文需求討論及短PRD樣本核對。

- 位置：專業技能
  - 原句：「與 DBA 協作取數」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：已支持試算表分析，獨立查詢仍未知。 先核對核心資格再決定約談
  - 建議方向：提供自行取數查詢與分析範例，釐清DBA協作邊界。

- 位置：專業技能
  - 原句：「以 Claude Code 建立協作流程與共用 skill」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：未呈現Jira/Confluence實際串接與自動化。 先核對核心資格再決定約談
  - 建議方向：補流程輸入輸出、API串接、例外處理及本人實作邊界。

- 位置：自傳
  - 原句：「我希望把更多心力放回產品策略」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：未表達防詐風險領域投入動機；不能推定無興趣。 先核對核心資格再決定約談
  - 建議方向：說明防詐動機與接受一半專案交付的原因。

其餘取證項保留於本輪 JSON issues；評語依上限列 5 點。

**編輯附件**：無。

#### 7. 資深能力分布

delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

#### 8. 未測試聲明

PDF 抽字：本內容審查 `not_tested`（另見總報告 §6 的 `local_extraction`）／ATS 匯入：`not_tested`／AI 作者判讀：不可由文字判定／真人校準：`not_run`。

### A.06｜jd26｜原始單行 JSON

```json
{"rubric_version":"4.2","resume_id":"appendix-A-v10.2","job_id":"jd26","job_input":"summary","model_id":"unknown","run_id":"jd26-A-01","human_calibrated":false,"requirements":[{"id":"R01","text":"2年以上產品／專案經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗"],"blocks_interview":false,"reason":"時序與多個交付案例支持年資要求。"},{"id":"R02","text":"需求、資料架構、Wireframe、Flow chart、UX設計規格；前端Hybrid App及後台","type":"required","status":"partial","evidence":["重新制定業務流程、對照資料欄位並重構規格","設計流程與畫面、撰寫 PRD 與製作 Prototype"],"blocks_interview":false,"reason":"需求、資料關聯及規格有實例；Wireframe與流程圖列於技能，App與企業系統可轉移，但Hybrid App及後台特定規格未明示。"},{"id":"R03","text":"兼顧合作方、公司與用戶；跨部門同理心及內外溝通","type":"required","status":"supported","evidence":["從案主與網紅兩種角色釐清需求","並與 CodaPay 新加坡技術團隊協調串接"],"blocks_interview":false,"reason":"雙邊需求、跨國外部串接及客服回饋有具體情境，支持協作；不以形容詞判同理心。"},{"id":"R04","text":"合作與法遵確認","type":"required","status":"partial","evidence":["法務與稽核協作"],"blocks_interview":false,"reason":"外部合作有串接實例；法務稽核僅清單，支付法遵確認的議題與責任待問。"},{"id":"R05","text":"時程交付、測試驗收上線及迭代","type":"required","status":"supported","evidence":["再與 QA 制定 UAT 驗收案例、排定上線計畫","公司資料於 2026/01 接續上線"],"blocks_interview":false,"reason":"多階段上線及現行服務迭代支持執行鏈。"},{"id":"R06","text":"教育訓練與線上問題排除","type":"required","status":"supported","evidence":["透過互動原型與 FAQ 向客服、業務說明功能","於 2026/04 完成登入驗證調整"],"blocks_interview":false,"reason":"內部功能說明可轉移教育訓練；帳號冒用處理支持線上排障，正式訓練範圍仍可問。"},{"id":"R07","text":"Axure規劃與Jira、Confluence專案管理","type":"required","status":"partial","evidence":["Figma、Axure RP、Notion、Trello"],"blocks_interview":false,"reason":"Axure只列工具，使用深度未知；Jira及Confluence未呈現，不能視為不會，面試核對轉移與實作。"},{"id":"R08","text":"技術可行性、系統架構關聯與執行風險識別","type":"required","status":"supported","evidence":["處理新舊系統並行的相容性需求","舊帳號信箱並非唯一值的限制"],"blocks_interview":false,"reason":"欄位、權限、資料轉換、驗證限制與分階段交付支持技術協作與風險意識，未稱本人寫程式。"},{"id":"R09","text":"喜愛且熟悉數位金融支付","type":"required","status":"partial","evidence":["App 內購與網頁付款、CodaPay 實收試算"],"blocks_interview":false,"reason":"支付渠道與結算試算相關；數位金融服務的熟悉廣度及投入動機未明示，尚非完全未知。"},{"id":"R10","text":"代理收付／電子行動支付經驗","type":"preferred","status":"partial","evidence":["用戶可用電信帳單與超商付款"],"blocks_interview":false,"reason":"有支付串接與替代支付經驗；代理收付業務責任與電子支付機構場景未呈現。"},{"id":"R11","text":"精通英文","type":"preferred","status":"supported","evidence":["英文 TOEIC 980、TOEFL iBT 93","並以英文進行跨國協作"],"blocks_interview":false,"reason":"測驗與跨國工作使用共同支持；專業協商深度面試可驗證。"},{"id":"R12","text":"實際數據分析工具與迭代","type":"preferred","status":"supported","evidence":["再以 Google Sheets、Excel 分析","團隊依結果決定採用低價"],"blocks_interview":false,"reason":"工具使用敘述、對照定價實驗與採用決策相互支持；GA4具體運用可追問。"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["現任 1111 招募系統 Product Owner","並推進 App 內購轉向網頁付款"],"missing":["企業系統及付款整合可轉移，支付專案執行動機與金融領域廣度待問。"],"issue_ids":["I03"]},{"id":"role_evidence","rating":"足夠","evidence":["再與 QA 制定 UAT 驗收案例、排定上線計畫"],"missing":["Jira、Confluence及Axure案例、支付法遵及Hybrid App規格需核對。"],"issue_ids":["I01","I02","I03"]},{"id":"decision_depth","rating":"強","evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前","舊帳號信箱並非唯一值的限制"],"missing":["可追問優先級證據、替代驗證方案及付款串接取捨。"],"issue_ids":[]},{"id":"outcome_quality","rating":"足夠","evidence":["平均處理時間由 100.4 天降至 30.9 天","各期 21 天"],"missing":["處理週期母體與案件組成、付款占比的淨效益待核實。"],"issue_ids":["I04","I05"]},{"id":"ownership","rating":"強","evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃","公司決定採新舊並行"],"missing":["付款及法遵決策批准界面可由案例進一步釐清。"],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["工作涵蓋系統分析、流程與畫面設計、PRD"],"missing":["可把支付合作案集中作為本職代表案例；屬編輯選擇，不影響約談。"],"issue_ids":[]}],"results":[{"quote":"系統服務逾 6 萬家活躍付費廠商（2026 Q3）","kinds":["context"]},{"quote":"公司資料於 2026/01 接續上線","kinds":["output"]},{"quote":"團隊依結果決定採用低價","kinds":["decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"兩案均在開發中","kinds":["in_progress","decision"]},{"quote":"平均處理時間由 100.4 天降至 30.9 天","kinds":["outcome"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["再與 QA 制定 UAT 驗收案例、排定上線計畫"],"application_note":"交付與支付整合足以支持面試。"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 Product Owner"],"application_note":"近期企業系統可轉移，金融場景待問。"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我主責規劃"],"application_note":"規劃與QA工程分工有交代。"},{"rule_id":"HR04","status":"partial","resume_evidence":["平均處理時間由 100.4 天降至 30.9 天"],"application_note":"有變化，仍需確認母體。"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"application_note":"有優先級與系統限制判斷。"},{"rule_id":"HR06","status":"supported","resume_evidence":["從 SweetRing 的海外市場開始累積產品經驗"],"application_note":"由在地化走向系統主責的脈絡清楚。"},{"rule_id":"HR07","status":"supported","resume_evidence":["並與 CodaPay 新加坡技術團隊協調串接"],"application_note":"技能具應用，指定工具另追問。"},{"rule_id":"HR08","status":"supported","resume_evidence":["工作涵蓋系統分析、流程與畫面設計、PRD"],"application_note":"摘要與工作案例能快速定位。"},{"rule_id":"HR09","status":"partial","resume_evidence":["依目前掌握的情況"],"application_note":"口述未再發生不等監測證明。"},{"rule_id":"HR10","status":"partial","resume_evidence":["接下來，我希望把更多心力放回產品策略"],"application_note":"需核對策略期望與執行職的相容性。"},{"rule_id":"HR11","status":"unknown","resume_evidence":["台北市、新北市，可接受遠端或混合辦公"],"application_note":"JD未列條件，無已知衝突。"},{"rule_id":"HR12","status":"supported","resume_evidence":["再與 QA 制定 UAT 驗收案例、排定上線計畫"],"application_note":"建議約談，缺口可面試核對。"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["規劃使用流程、訂閱與付費機制"],"evidence_type":"context","source_ids":[],"interview_question":"如何把訂閱支付經驗轉用到金融合作專案？"},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["廠商反映的溝通中斷問題"],"evidence_type":"decision","source_ids":[],"interview_question":"哪些用戶資料改變了原先排序？"},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":"如何比較價值、資源與延後風險？"},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["整理抽成、稅、手續費與撥款週期"],"evidence_type":"decision","source_ids":[],"interview_question":"付款渠道與方案的成本取捨如何形成？"},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["平均處理時間由 100.4 天降至 30.9 天"],"evidence_type":"outcome","source_ids":[],"interview_question":"週期指標的分母、案件組成與納入規則是什麼？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["與內部工程團隊分階段交付"],"evidence_type":"output","source_ids":[],"interview_question":"付款合作案中你、工程與合作方各自決定什麼？"},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["處理新舊系統並行的相容性需求"],"evidence_type":"output","source_ids":[],"interview_question":"如何安排驗收、回滾及既有客戶風險？"},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["舊帳號信箱並非唯一值的限制"],"evidence_type":"decision","source_ids":[],"interview_question":"請展示資料關聯、替代流程及驗收條件。"},{"rule_id":"HM09","primary_dimension":"ownership","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"evidence_type":"output","source_ids":[],"interview_question":"哪些範圍自主決定，哪些需主管批准？"},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["工作涵蓋系統分析、流程與畫面設計、PRD"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["並依客服回饋修正操作流程"],"evidence_type":"decision","source_ids":[],"interview_question":"回饋如何改變驗證流程，又如何驗證改善？"},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["並與 CodaPay 新加坡技術團隊協調串接"],"evidence_type":"output","source_ids":[],"interview_question":"請用作品說明支付串接、法遵核對與指定工具。"},{"rule_id":"HM13","primary_dimension":"method","status":"supported","resume_evidence":["公司決定採新舊並行"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR07","source_ids":[],"application_note":"面試追問，不直接否定","context_limit":"未列工具不代表能力不符。","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"Figma、Axure RP、Notion、Trello","reason":"Axure只列工具，Jira與Confluence未呈現。","suggestion":"補Axure作品與Jira、Confluence實際管理任務或轉移經驗。"},{"id":"I02","rule_id":"HM08","source_ids":[],"application_note":"面試追問，不直接否定","context_limit":"技能清單是線索，不是完整案例。","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"法務與稽核協作","reason":"缺支付合作的法遵確認及Hybrid App規格案例。","suggestion":"補法遵議題、核對對象、責任與特定前後台規格。"},{"id":"I03","rule_id":"HR10","source_ids":[],"application_note":"面試追問，不直接否定","context_limit":"不把未提供動機當成無興趣。","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"接下來，我希望把更多心力放回產品策略","reason":"數位金融熟悉度與執行職動機尚需連結。","suggestion":"說明支付服務理解與接受合作專案執行重心的原因。"},{"id":"I04","rule_id":"HM05","source_ids":[],"application_note":"面試追問，不直接否定","context_limit":"數值是觀察結果，因果仍待核對。","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"平均處理時間由 100.4 天降至 30.9 天","reason":"提供季度與數值，未列案件母體及組成變化。","suggestion":"補案件數、納入規則、平均計算及積案清理影響。"},{"id":"I05","rule_id":"HM05","source_ids":[],"application_note":"面試追問，不直接否定","context_limit":"占比上升不能推論整體成長。","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"網頁付款占營收由 24% 升至 80% 以上","reason":"有期間與占比，但非總營收、淨利或支付成功率結果。","suggestion":"補總額、淨實收、手續費及遷移作用與限制。"}],"decision":{"recommendation":"interview","evidence":["再與 QA 制定 UAT 驗收案例、排定上線計畫","並與 CodaPay 新加坡技術團隊協調串接"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["「再與 QA 制定 UAT 驗收案例、排定上線計畫」支持端到端專案執行。","「並與 CodaPay 新加坡技術團隊協調串接」提供支付合作轉移經驗。","「舊帳號信箱並非唯一值的限制」呈現系統限制下的可行性判斷。"],"key_gaps":["指定工具深度未知：請展示Axure、Jira及Confluence使用或可轉移管理流程。","金融與法遵不足：追問支付法遵核對、Hybrid App規格及數位金融理解。","動機及量測需釐清：追問執行職接受度與案件週期母體、付款淨效益。"],"strengths":["多階段交付、UAT與內部功能說明形成完整執行鏈。","支付串接與結算試算可轉移到合作專案。","能連結資料限制、權限與使用情境形成規格。"],"interview_questions":["請展示Axure規劃作品，並說明Jira與Confluence的實際使用或轉移方案。","支付合作中法務、稽核確認什麼，你負責哪些規則與驗收？","請說明Hybrid App與後台的資料、流程、規格及技術限制。","如何兼顧合作方、公司與用戶利益，發生衝突如何取捨？","請展開帳號驗證方案的替代選項、風險與驗收。","案件處理週期的母體、樣本數與積案清理影響是什麼？","付款占比變化如何影響淨實收與成功率，哪些變化由你推動？","對數位金融支付哪些服務最熟悉，為何選擇專案執行重心？"],"editorial_appendix":[],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"多案例涵蓋規格、協作、交付、支付及系統取捨；定價實驗有對照和期間，成果限制可辨。指定工具、支付法遵與部分量測責任仍待核對，未達高度對應且完整可追溯的9級。進行中整合僅支持判斷，不當成已實現成果。"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"not_tested","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 單份審查｜履歷 appendix-A-v10.2｜第 6 輪｜model_id: unknown

#### 1. 結論

- 招聘決定：`interview`
- Level：8（±1）
- 一句話理由：「再與 QA 制定 UAT 驗收案例、排定上線計畫」支持面試，缺口依下表核對。

#### 2. 六維度

| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 現任 1111 招募系統 Product Owner；並推進 App 內購轉向網頁付款 | 企業系統及付款整合可轉移，支付專案執行動機與金融領域廣度待問。 |
| role_evidence | 足夠 | 再與 QA 制定 UAT 驗收案例、排定上線計畫 | Jira、Confluence及Axure案例、支付法遵及Hybrid App規格需核對。 |
| decision_depth | 強 | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前；舊帳號信箱並非唯一值的限制 | 可追問優先級證據、替代驗證方案及付款串接取捨。 |
| outcome_quality | 足夠 | 平均處理時間由 100.4 天降至 30.9 天；各期 21 天 | 處理週期母體與案件組成、付款占比的淨效益待核實。 |
| ownership | 強 | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃；公司決定採新舊並行 | 付款及法遵決策批准界面可由案例進一步釐清。 |
| readability | 強 | 工作涵蓋系統分析、流程與畫面設計、PRD | 可把支付合作案集中作為本職代表案例；屬編輯選擇，不影響約談。 |

#### 3. JD 條件對照

| 條件 | 必要／加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 2年以上產品／專案經驗 | 必要 | supported | 近 10 年 PM 經驗 | 時序與多個交付案例支持年資要求。 |
| 需求、資料架構、Wireframe、Flow chart、UX設計規格；前端Hybrid App及後台 | 必要 | partial | 重新制定業務流程、對照資料欄位並重構規格；設計流程與畫面、撰寫 PRD 與製作 Prototype | 需求、資料關聯及規格有實例；Wireframe與流程圖列於技能，App與企業系統可轉移，但Hybrid App及後台特定規格未明示。 |
| 兼顧合作方、公司與用戶；跨部門同理心及內外溝通 | 必要 | supported | 從案主與網紅兩種角色釐清需求；並與 CodaPay 新加坡技術團隊協調串接 | 雙邊需求、跨國外部串接及客服回饋有具體情境，支持協作；不以形容詞判同理心。 |
| 合作與法遵確認 | 必要 | partial | 法務與稽核協作 | 外部合作有串接實例；法務稽核僅清單，支付法遵確認的議題與責任待問。 |
| 時程交付、測試驗收上線及迭代 | 必要 | supported | 再與 QA 制定 UAT 驗收案例、排定上線計畫；公司資料於 2026/01 接續上線 | 多階段上線及現行服務迭代支持執行鏈。 |
| 教育訓練與線上問題排除 | 必要 | supported | 透過互動原型與 FAQ 向客服、業務說明功能；於 2026/04 完成登入驗證調整 | 內部功能說明可轉移教育訓練；帳號冒用處理支持線上排障，正式訓練範圍仍可問。 |
| Axure規劃與Jira、Confluence專案管理 | 必要 | partial | Figma、Axure RP、Notion、Trello | Axure只列工具，使用深度未知；Jira及Confluence未呈現，不能視為不會，面試核對轉移與實作。 |
| 技術可行性、系統架構關聯與執行風險識別 | 必要 | supported | 處理新舊系統並行的相容性需求；舊帳號信箱並非唯一值的限制 | 欄位、權限、資料轉換、驗證限制與分階段交付支持技術協作與風險意識，未稱本人寫程式。 |
| 喜愛且熟悉數位金融支付 | 必要 | partial | App 內購與網頁付款、CodaPay 實收試算 | 支付渠道與結算試算相關；數位金融服務的熟悉廣度及投入動機未明示，尚非完全未知。 |
| 代理收付／電子行動支付經驗 | 加分 | partial | 用戶可用電信帳單與超商付款 | 有支付串接與替代支付經驗；代理收付業務責任與電子支付機構場景未呈現。 |
| 精通英文 | 加分 | supported | 英文 TOEIC 980、TOEFL iBT 93；並以英文進行跨國協作 | 測驗與跨國工作使用共同支持；專業協商深度面試可驗證。 |
| 實際數據分析工具與迭代 | 加分 | supported | 再以 Google Sheets、Excel 分析；團隊依結果決定採用低價 | 工具使用敘述、對照定價實驗與採用決策相互支持；GA4具體運用可追問。 |

#### 4. HR 十二問／HM 十三問

| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 再與 QA 制定 UAT 驗收案例、排定上線計畫 | 交付與支付整合足以支持面試。 |
| HR02 | supported | 現任 1111 招募系統 Product Owner | 近期企業系統可轉移，金融場景待問。 |
| HR03 | supported | 由我主責規劃 | 規劃與QA工程分工有交代。 |
| HR04 | partial | 平均處理時間由 100.4 天降至 30.9 天 | 有變化，仍需確認母體。 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 有優先級與系統限制判斷。 |
| HR06 | supported | 從 SweetRing 的海外市場開始累積產品經驗 | 由在地化走向系統主責的脈絡清楚。 |
| HR07 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 技能具應用，指定工具另追問。 |
| HR08 | supported | 工作涵蓋系統分析、流程與畫面設計、PRD | 摘要與工作案例能快速定位。 |
| HR09 | partial | 依目前掌握的情況 | 口述未再發生不等監測證明。 |
| HR10 | partial | 接下來，我希望把更多心力放回產品策略 | 需核對策略期望與執行職的相容性。 |
| HR11 | unknown | 台北市、新北市，可接受遠端或混合辦公 | JD未列條件，無已知衝突。 |
| HR12 | supported | 再與 QA 制定 UAT 驗收案例、排定上線計畫 | 建議約談，缺口可面試核對。 |
| HM01 | supported | 規劃使用流程、訂閱與付費機制 | 企業系統與支付經驗可轉移。 |
| HM02 | supported | 廠商反映的溝通中斷問題 | 使用者問題有進入優先級。 |
| HM03 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 取捨具體，細節可追問。 |
| HM04 | supported | 整理抽成、稅、手續費與撥款週期 | 成本試算相關，無需要求P&L。 |
| HM05 | partial | 平均處理時間由 100.4 天降至 30.9 天 | 結果有期間，分母與限制待問。 |
| HM06 | supported | 與內部工程團隊分階段交付 | 本人規劃與團隊交付可區分。 |
| HM07 | supported | 處理新舊系統並行的相容性需求 | 交付與相容風險有實例。 |
| HM08 | supported | 舊帳號信箱並非唯一值的限制 | 規則限制支持技術協作。 |
| HM09 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 自主責任支持資深執行。 |
| HM10 | supported | 工作涵蓋系統分析、流程與畫面設計、PRD | 摘要與案例能辨識本人作用。 |
| HM11 | supported | 並依客服回饋修正操作流程 | 回饋修正具體，可驗證轉用。 |
| HM12 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 作品與指定工具仍有核對價值。 |
| HM13 | supported | 公司決定採新舊並行 | 只依本JD；未將公司決策歸本人。 |

#### 5. 約談理由（≤3）與關鍵缺口（≤3）

| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「再與 QA 制定 UAT 驗收案例、排定上線計畫」支持端到端專案執行。 |
| 2 | 「並與 CodaPay 新加坡技術團隊協調串接」提供支付合作轉移經驗。 |
| 3 | 「舊帳號信箱並非唯一值的限制」呈現系統限制下的可行性判斷。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 指定工具深度未知：請展示Axure、Jira及Confluence使用或可轉移管理流程。 | 請展示Axure規劃作品，並說明Jira與Confluence的實際使用或轉移方案。 |
| 2 | 金融與法遵不足：追問支付法遵核對、Hybrid App規格及數位金融理解。 | 支付合作中法務、稽核確認什麼，你負責哪些規則與驗收？ |
| 3 | 動機及量測需釐清：追問執行職接受度與案件週期母體、付款淨效益。 | 請說明Hybrid App與後台的資料、流程、規格及技術限制。 |

#### 6. 評語（給寫稿者的具體回饋）

**做得好（3 點）**

- 1111功能交付｜「再與 QA 制定 UAT 驗收案例、排定上線計畫」｜支持測試、時程與上線協作。
- 尚凡付款｜「並與 CodaPay 新加坡技術團隊協調串接」｜支持外部支付合作。
- 自傳系統改版｜「舊帳號信箱並非唯一值的限制」｜支持資料限制下的可行規格。

**可改進（≤5 點）**

- 位置：專業技能
  - 原句：「Figma、Axure RP、Notion、Trello」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：Axure只列工具，Jira與Confluence未呈現。 面試追問，不直接否定
  - 建議方向：補Axure作品與Jira、Confluence實際管理任務或轉移經驗。

- 位置：專業技能
  - 原句：「法務與稽核協作」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：缺支付合作的法遵確認及Hybrid App規格案例。 面試追問，不直接否定
  - 建議方向：補法遵議題、核對對象、責任與特定前後台規格。

- 位置：自傳
  - 原句：「接下來，我希望把更多心力放回產品策略」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：數位金融熟悉度與執行職動機尚需連結。 面試追問，不直接否定
  - 建議方向：說明支付服務理解與接受合作專案執行重心的原因。

- 位置：Product Owner／PM｜1111 全球華人
  - 原句：「平均處理時間由 100.4 天降至 30.9 天」
  - 問題類型：`measurement`
  - 嚴重度：`interview_follow_up`
  - 影響：提供季度與數值，未列案件母體及組成變化。 面試追問，不直接否定
  - 建議方向：補案件數、納入規則、平均計算及積案清理影響。

- 位置：專業摘要
  - 原句：「網頁付款占營收由 24% 升至 80% 以上」
  - 問題類型：`measurement`
  - 嚴重度：`interview_follow_up`
  - 影響：有期間與占比，但非總營收、淨利或支付成功率結果。 面試追問，不直接否定
  - 建議方向：補總額、淨實收、手續費及遷移作用與限制。

**編輯附件**：無。

#### 7. 資深能力分布

delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

#### 8. 未測試聲明

PDF 抽字：本內容審查 `not_tested`（另見總報告 §6 的 `local_extraction`）／ATS 匯入：`not_tested`／AI 作者判讀：不可由文字判定／真人校準：`not_run`。

### A.07｜jd30｜原始單行 JSON

```json
{"rubric_version":"4.2","resume_id":"appendix-A-v10.2","job_id":"jd30","job_input":"summary","model_id":"unknown","run_id":"jd30-A-01","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上Software PM","type":"required","status":"supported","evidence":["近 10 年 PM 經驗"],"blocks_interview":false,"reason":"2016年至今多款軟體產品經歷，且有具體交付案例。"},{"id":"R02","text":"至少一次完整新產品探索、驗證、設計、開發、上線、迭代直接負責","type":"required","status":"partial","evidence":["規劃 KOOL 網紅媒合平台"],"blocks_interview":false,"reason":"KOOL支持需求探索、設計與上線；Juicy支持主導推出，完整驗證與迭代鏈仍需核對。"},{"id":"R03","text":"清楚PRD、流程圖、資料結構","type":"required","status":"supported","evidence":["整理帳號權限、職缺關聯與既有資料轉換規則"],"blocks_interview":false,"reason":"PRD及流程圖有明示，群組案例有資料關聯與轉換規則；可面試看實際產物。"},{"id":"R04","text":"理解API、JSON、基本SQL","type":"required","status":"partial","evidence":["API 串接規劃"],"blocks_interview":false,"reason":"API有實際金流串接情境；JSON與SQL未明示，與DBA協作取數不能等同本人會SQL。"},{"id":"R05","text":"業務客服財務情境排序PRD；時程範圍溝通、專案架構與產品策略","type":"required","status":"supported","evidence":["依使用者旅程與工單問題安排優先級"],"blocks_interview":false,"reason":"業務客服排序與規格交付直接支持；實收試算補足財務考量，策略範圍面試核對。"},{"id":"R06","text":"Claude Code、Codex快速原型及AI機會PM流程化","type":"required","status":"partial","evidence":["以 Claude Code 建立協作流程與共用 skill"],"blocks_interview":false,"reason":"Claude Code流程化明示；Codex及以程式生成可運行原型未呈現。"},{"id":"R07","text":"測試驗收、成熟產品數據成長、新產品PoC→Pilot→Scale","type":"required","status":"partial","evidence":["再與 QA 制定 UAT 驗收案例"],"blocks_interview":false,"reason":"UAT與既有產品成長有案例；PoC、Pilot、Scale各階段門檻和承接責任待補。"},{"id":"R08","text":"工程技術方案與商務、營運、財務優先級協作","type":"required","status":"supported","evidence":["整理抽成、稅、手續費與撥款週期"],"blocks_interview":false,"reason":"系統限制、金流實收與商務排序跨案例支持；非完整資源決策權證據。"},{"id":"R09","text":"停車、交通、MaaS、保險、支付或FinTech經驗","type":"preferred","status":"supported","evidence":["並與 CodaPay 新加坡技術團隊協調串接"],"blocks_interview":false,"reason":"支付相關經驗符合加分之一；停車與MaaS未呈現。"},{"id":"R10","text":"Prompt、RAG或Agent實作","type":"preferred","status":"partial","evidence":["運用 AI Agent 撰寫規格、整理與分析資料"],"blocks_interview":false,"reason":"Agent應用與共用skill有線索；Prompt產物、RAG與Agent實作深度待看。"},{"id":"R11","text":"Growth數據","type":"preferred","status":"supported","evidence":["設計馬來西亞 iOS 定價實驗"],"blocks_interview":false,"reason":"有對照組、測試期間及價格採用決策；因果限制仍需追問。"},{"id":"R12","text":"AI/LLM規格、資料自動化與原型","type":"preferred","status":"partial","evidence":["將業務規則轉為可與工程討論的條件描述"],"blocks_interview":false,"reason":"規格及資料AI協作支持，實際自動化流程及可運行原型未提供。"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["涵蓋訂閱制社交 App、網紅媒合平台與人力銀行招募系統。"],"missing":["停車與MaaS環境轉移需核對"],"issue_ids":[]},{"id":"role_evidence","rating":"足夠","evidence":["工作涵蓋系統分析、流程與畫面設計、PRD、Prototype、UAT 與上線計畫"],"missing":["JSON、SQL、程式原型及完整新產品驗證鏈"],"issue_ids":["I01","I02","I03"]},{"id":"decision_depth","rating":"強","evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。"],"missing":["補優先級量化依據與替代方案"],"issue_ids":[]},{"id":"outcome_quality","rating":"足夠","evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天。"],"missing":["處理案件母體、週期口徑及實驗限制"],"issue_ids":["I04"]},{"id":"ownership","rating":"強","evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃。"],"missing":["資源配置及最終決策權"],"issue_ids":["I05"]},{"id":"readability","rating":"足夠","evidence":["現任 1111 招募系統 Product Owner"],"missing":["可補本職對位作品索引"],"issue_ids":[]}],"results":[{"quote":"兩案均在開發中","kinds":["decision","in_progress"]},{"quote":"第一階段的登入、首頁、帳號、聯絡人、功能選單與公告通知於 2025/10 上線","kinds":["output"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"團隊依結果決定採用低價。","kinds":["decision"]},{"quote":"平均處理時間由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"調整後至 2026/10 未再出現同類冒用。","kinds":["outcome"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["API 串接規劃"],"application_note":"支付、規格與交付可轉移"},{"rule_id":"HR02","status":"supported","resume_evidence":["人力銀行企業端招募系統專案負責人"],"application_note":"近期B2B系統經驗清楚"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我主責規劃"],"application_note":"本人規劃與協作邊界可追問"},{"rule_id":"HR04","status":"partial","resume_evidence":["平均處理時間由 100.4 天降至 30.9 天"],"application_note":"數值有期間，母體待核對"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。"],"application_note":"可追問排序依據"},{"rule_id":"HR06","status":"supported","resume_evidence":["從 SweetRing 的海外市場開始累積產品經驗"],"application_note":"責任由在地化轉向系統負責"},{"rule_id":"HR07","status":"supported","resume_evidence":["並與 CodaPay 新加坡技術團隊協調串接"],"application_note":"技術協作有實際情境"},{"rule_id":"HR08","status":"supported","resume_evidence":["工作涵蓋系統分析、流程與畫面設計、PRD"],"application_note":"結構能辨識主要能力"},{"rule_id":"HR09","status":"partial","resume_evidence":["調整後至 2026/10 未再出現同類冒用。"],"application_note":"口述觀察需核對監測範圍"},{"rule_id":"HR10","status":"supported","resume_evidence":["我希望把更多心力放回產品策略"],"application_note":"方向與完整產品責任相容"},{"rule_id":"HR11","status":"unknown","resume_evidence":["台北市、新北市，可接受遠端或混合辦公"],"application_note":"JD地點語言條件未提供"},{"rule_id":"HR12","status":"supported","resume_evidence":["設計馬來西亞 iOS 定價實驗"],"application_note":"支持邀約核對技術與新產品鏈"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["涵蓋訂閱制社交 App、網紅媒合平台與人力銀行招募系統。"],"evidence_type":"context","source_ids":[],"interview_question":"如何把支付與企業流程經驗轉用於停車MaaS？"},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["廠商反映的溝通中斷問題，使我優先推進信件與即時通整合"],"evidence_type":"decision","source_ids":[],"interview_question":"哪些資料改變原先優先級？"},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["團隊依結果決定採用低價。"],"evidence_type":"decision","source_ids":[],"interview_question":"低價有哪些替代方案與代價，誰拍板？"},{"rule_id":"HM04","primary_dimension":"role_evidence","status":"supported","resume_evidence":["完成實收試算"],"evidence_type":"decision","source_ids":[],"interview_question":"實收試算如何影響訂閱方案？"},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["相對變化約多 28%"],"evidence_type":"outcome","source_ids":[],"interview_question":"價格實驗如何控制季節、渠道與樣本差異？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["與內部工程團隊分階段交付"],"evidence_type":"output","source_ids":[],"interview_question":"規劃、技術與上線決策由誰負責？"},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["處理新舊系統並行的相容性需求。"],"evidence_type":"output","source_ids":[],"interview_question":"資料轉換與回退驗收如何設計？"},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"partial","resume_evidence":["API 串接規劃"],"evidence_type":"output","source_ids":[],"interview_question":"請用金流案例展示JSON與基本SQL理解。"},{"rule_id":"HM09","primary_dimension":"ownership","status":"partial","resume_evidence":["帶領 2 名直屬產品企劃"],"evidence_type":"context","source_ids":[],"interview_question":"如何配置資源與對成效負責？"},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["工作涵蓋系統分析、流程與畫面設計、PRD"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["並依客服回饋修正操作流程。"],"evidence_type":"decision","source_ids":[],"interview_question":"哪項回饋推翻原設計，之後如何沿用？"},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["以 Claude Code 建立協作流程與共用 skill"],"evidence_type":"output","source_ids":[],"interview_question":"請展示AI協作產物及一個完整新產品案例。"},{"rule_id":"HM13","primary_dimension":"method","status":"supported","resume_evidence":["近 10 年 PM 經驗"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HM08","source_ids":[],"application_note":"面試核對，不直接否定","context_limit":"文件未列不代表不會","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"API 串接規劃","reason":"JSON、SQL未提供，API協作不能代替全部技術必要條件。","suggestion":"補JSON資料範例與本人SQL使用情境。"},{"id":"I02","rule_id":"HM12","source_ids":[],"application_note":"面試核對，不直接否定","context_limit":"不把工具名稱當能力","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"以 Claude Code 建立協作流程與共用 skill","reason":"流程化有證據，但Codex和可運行快速原型未知。","suggestion":"展示具體原型、驗收及Agent分工。"},{"id":"I03","rule_id":"HM01","source_ids":[],"application_note":"面試核對，不直接否定","context_limit":"不是沒有完整週期能力","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"規劃 KOOL 網紅媒合平台","reason":"需求、設計、上線可見，完整驗證迭代與PoC到Scale門檻不完整。","suggestion":"補單一產品探索驗證到迭代時間軸與決策。"},{"id":"I04","rule_id":"HM05","source_ids":[],"application_note":"面試核對，不直接否定","context_limit":"相對變化不是淨增收入證明","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"相對變化約多 28%","reason":"有對照與期間，但樣本量、收入母體及同期混雜因素未列。","suggestion":"補分母、實驗口徑與限制。"},{"id":"I05","rule_id":"HM09","source_ids":[],"application_note":"面試核對，不直接否定","context_limit":"不以主管會議或人數定級","category":"ownership","severity":"interview_follow_up","block_target":null,"claim":"參與公司一級主管日會","reason":"匯報與管理情境不等於擁有方向、預算與資源決策權。","suggestion":"補一項資源衝突中的本人提案、權責與結果。"}],"decision":{"recommendation":"interview","evidence":["設計馬來西亞 iOS 定價實驗","整理帳號權限、職缺關聯與既有資料轉換規則"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"待補"},"interview_reasons":["「整理帳號權限、職缺關聯與既有資料轉換規則」支持複雜系統規格。","「設計馬來西亞 iOS 定價實驗」支持商業與Growth判斷。","「以 Claude Code 建立協作流程與共用 skill」支持AI工作流程線索。"],"key_gaps":["JSON與基本SQL：請展示API資料及查詢情境。","Codex與AI快速原型：請展示可運行產物與驗收方式。","完整新產品週期：請以一案交代探索驗證、Pilot與Scale門檻。"],"strengths":["系統資料關聯與分階段交付具體。","定價實驗能連接衡量與產品決策。","支付整合與實收試算可轉移。"],"interview_questions":["請完整走讀KOOL從問題驗證、開發上線到迭代的責任與證據。","請展示JSON及本人寫過或解讀過的基本SQL。","請展示Claude Code或Codex生成原型及測試方法。","新產品PoC、Pilot與Scale的決策門檻如何設定？","定價實驗樣本、收入母體與混雜因素為何？","新舊系統資料轉換的驗收與回退方案為何？","請舉資源衝突案例，說明本人決策權與取捨。","招募系統優先級如何連結商業、營運與財務？"],"editorial_appendix":[],"spectrum":{"level":7,"uncertainty_levels":1,"basis":"多個系統、支付與定價案例足以面試；本職AI快速原型、JSON/SQL與完整新產品驗證鏈仍待補，尚不足高度對應。"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"not_tested","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 單份審查｜履歷 appendix-A-v10.2｜第 7 輪｜model_id: unknown

#### 1. 結論

- 招聘決定：`interview`
- Level：7（±1）
- 一句話理由：「設計馬來西亞 iOS 定價實驗」支持面試，缺口依下表核對。

#### 2. 六維度

| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 涵蓋訂閱制社交 App、網紅媒合平台與人力銀行招募系統。 | 停車與MaaS環境轉移需核對 |
| role_evidence | 足夠 | 工作涵蓋系統分析、流程與畫面設計、PRD、Prototype、UAT 與上線計畫 | JSON、SQL、程式原型及完整新產品驗證鏈 |
| decision_depth | 強 | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。 | 補優先級量化依據與替代方案 |
| outcome_quality | 足夠 | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天。 | 處理案件母體、週期口徑及實驗限制 |
| ownership | 強 | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃。 | 資源配置及最終決策權 |
| readability | 足夠 | 現任 1111 招募系統 Product Owner | 可補本職對位作品索引 |

#### 3. JD 條件對照

| 條件 | 必要／加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 3年以上Software PM | 必要 | supported | 近 10 年 PM 經驗 | 2016年至今多款軟體產品經歷，且有具體交付案例。 |
| 至少一次完整新產品探索、驗證、設計、開發、上線、迭代直接負責 | 必要 | partial | 規劃 KOOL 網紅媒合平台 | KOOL支持需求探索、設計與上線；Juicy支持主導推出，完整驗證與迭代鏈仍需核對。 |
| 清楚PRD、流程圖、資料結構 | 必要 | supported | 整理帳號權限、職缺關聯與既有資料轉換規則 | PRD及流程圖有明示，群組案例有資料關聯與轉換規則；可面試看實際產物。 |
| 理解API、JSON、基本SQL | 必要 | partial | API 串接規劃 | API有實際金流串接情境；JSON與SQL未明示，與DBA協作取數不能等同本人會SQL。 |
| 業務客服財務情境排序PRD；時程範圍溝通、專案架構與產品策略 | 必要 | supported | 依使用者旅程與工單問題安排優先級 | 業務客服排序與規格交付直接支持；實收試算補足財務考量，策略範圍面試核對。 |
| Claude Code、Codex快速原型及AI機會PM流程化 | 必要 | partial | 以 Claude Code 建立協作流程與共用 skill | Claude Code流程化明示；Codex及以程式生成可運行原型未呈現。 |
| 測試驗收、成熟產品數據成長、新產品PoC→Pilot→Scale | 必要 | partial | 再與 QA 制定 UAT 驗收案例 | UAT與既有產品成長有案例；PoC、Pilot、Scale各階段門檻和承接責任待補。 |
| 工程技術方案與商務、營運、財務優先級協作 | 必要 | supported | 整理抽成、稅、手續費與撥款週期 | 系統限制、金流實收與商務排序跨案例支持；非完整資源決策權證據。 |
| 停車、交通、MaaS、保險、支付或FinTech經驗 | 加分 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 支付相關經驗符合加分之一；停車與MaaS未呈現。 |
| Prompt、RAG或Agent實作 | 加分 | partial | 運用 AI Agent 撰寫規格、整理與分析資料 | Agent應用與共用skill有線索；Prompt產物、RAG與Agent實作深度待看。 |
| Growth數據 | 加分 | supported | 設計馬來西亞 iOS 定價實驗 | 有對照組、測試期間及價格採用決策；因果限制仍需追問。 |
| AI/LLM規格、資料自動化與原型 | 加分 | partial | 將業務規則轉為可與工程討論的條件描述 | 規格及資料AI協作支持，實際自動化流程及可運行原型未提供。 |

#### 4. HR 十二問／HM 十三問

| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | API 串接規劃 | 支付、規格與交付可轉移 |
| HR02 | supported | 人力銀行企業端招募系統專案負責人 | 近期B2B系統經驗清楚 |
| HR03 | supported | 由我主責規劃 | 本人規劃與協作邊界可追問 |
| HR04 | partial | 平均處理時間由 100.4 天降至 30.9 天 | 數值有期間，母體待核對 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。 | 可追問排序依據 |
| HR06 | supported | 從 SweetRing 的海外市場開始累積產品經驗 | 責任由在地化轉向系統負責 |
| HR07 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 技術協作有實際情境 |
| HR08 | supported | 工作涵蓋系統分析、流程與畫面設計、PRD | 結構能辨識主要能力 |
| HR09 | partial | 調整後至 2026/10 未再出現同類冒用。 | 口述觀察需核對監測範圍 |
| HR10 | supported | 我希望把更多心力放回產品策略 | 方向與完整產品責任相容 |
| HR11 | unknown | 台北市、新北市，可接受遠端或混合辦公 | JD地點語言條件未提供 |
| HR12 | supported | 設計馬來西亞 iOS 定價實驗 | 支持邀約核對技術與新產品鏈 |
| HM01 | supported | 涵蓋訂閱制社交 App、網紅媒合平台與人力銀行招募系統。 | 跨領域可轉移，需核對MaaS |
| HM02 | supported | 廠商反映的溝通中斷問題，使我優先推進信件與即時通整合 | 痛點有影響排序 |
| HM03 | supported | 團隊依結果決定採用低價。 | 決策有依據，追問權責 |
| HM04 | supported | 完成實收試算 | 商業試算可支持產品選擇 |
| HM05 | partial | 相對變化約多 28% | 核對量測母體與實驗限制 |
| HM06 | supported | 與內部工程團隊分階段交付 | 交付分工清楚，資源權待補 |
| HM07 | supported | 處理新舊系統並行的相容性需求。 | 支持複雜系統交付 |
| HM08 | partial | API 串接規劃 | 追問JSON、SQL實際理解 |
| HM09 | partial | 帶領 2 名直屬產品企劃 | 不以年資、人數決定資深程度 |
| HM10 | supported | 工作涵蓋系統分析、流程與畫面設計、PRD | 重點可辨識 |
| HM11 | supported | 並依客服回饋修正操作流程。 | 有回饋修正線索 |
| HM12 | supported | 以 Claude Code 建立協作流程與共用 skill | 作品可驗證AI與產品鏈 |
| HM13 | supported | 近 10 年 PM 經驗 | 僅依凍結準則做內容審查 |

#### 5. 約談理由（≤3）與關鍵缺口（≤3）

| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「整理帳號權限、職缺關聯與既有資料轉換規則」支持複雜系統規格。 |
| 2 | 「設計馬來西亞 iOS 定價實驗」支持商業與Growth判斷。 |
| 3 | 「以 Claude Code 建立協作流程與共用 skill」支持AI工作流程線索。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | JSON與基本SQL：請展示API資料及查詢情境。 | 請完整走讀KOOL從問題驗證、開發上線到迭代的責任與證據。 |
| 2 | Codex與AI快速原型：請展示可運行產物與驗收方式。 | 請展示JSON及本人寫過或解讀過的基本SQL。 |
| 3 | 完整新產品週期：請以一案交代探索驗證、Pilot與Scale門檻。 | 請展示Claude Code或Codex生成原型及測試方法。 |

#### 6. 評語（給寫稿者的具體回饋）

**做得好（3 點）**

- 1111群組功能｜「整理帳號權限、職缺關聯與既有資料轉換規則」｜支持本職資料結構與規格溝通。
- 尚凡定價實驗｜「設計馬來西亞 iOS 定價實驗」｜支持成熟產品Growth與商業決策。
- 思維特支付｜「完成實收試算」｜支持商務與財務取捨。

**可改進（≤5 點）**

- 位置：專業技能
  - 原句：「API 串接規劃」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：JSON、SQL未提供，API協作不能代替全部技術必要條件。 面試核對，不直接否定
  - 建議方向：補JSON資料範例與本人SQL使用情境。

- 位置：專業技能
  - 原句：「以 Claude Code 建立協作流程與共用 skill」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：流程化有證據，但Codex和可運行快速原型未知。 面試核對，不直接否定
  - 建議方向：展示具體原型、驗收及Agent分工。

- 位置：Product Manager｜尚凡國際創新科技
  - 原句：「規劃 KOOL 網紅媒合平台」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：需求、設計、上線可見，完整驗證迭代與PoC到Scale門檻不完整。 面試核對，不直接否定
  - 建議方向：補單一產品探索驗證到迭代時間軸與決策。

- 位置：Product Manager｜尚凡國際創新科技
  - 原句：「相對變化約多 28%」
  - 問題類型：`measurement`
  - 嚴重度：`interview_follow_up`
  - 影響：有對照與期間，但樣本量、收入母體及同期混雜因素未列。 面試核對，不直接否定
  - 建議方向：補分母、實驗口徑與限制。

- 位置：Product Owner／PM｜1111 全球華人
  - 原句：「參與公司一級主管日會」
  - 問題類型：`ownership`
  - 嚴重度：`interview_follow_up`
  - 影響：匯報與管理情境不等於擁有方向、預算與資源決策權。 面試核對，不直接否定
  - 建議方向：補一項資源衝突中的本人提案、權責與結果。

**編輯附件**：無。

#### 7. 資深能力分布

delivery：強 ／ po_coordination：強 ／ direction_resources：待補

#### 8. 未測試聲明

PDF 抽字：本內容審查 `not_tested`（另見總報告 §6 的 `local_extraction`）／ATS 匯入：`not_tested`／AI 作者判讀：不可由文字判定／真人校準：`not_run`。

### A.08｜jd31｜原始單行 JSON

```json
{"rubric_version":"4.2","resume_id":"appendix-A-v10.2","job_id":"jd31","job_input":"summary","model_id":"unknown","run_id":"jd31-A-01","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上產品規劃與訪談；熟悉新產品或迭代","type":"required","status":"partial","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"年資與新產品、迭代案例支持規劃經驗；訪談僅技能列示，直接訪談對象、頻率與如何轉為方案待釐清。"},{"id":"R02","text":"直接客戶訪談、分析方案並轉為規格開發項","type":"required","status":"partial","evidence":["釐清需求並完成系統分析後"],"blocks_interview":false,"reason":"需求轉規格與開發項有具體流程；直接訪談仍未提供案例，與R01共用I01缺口。"},{"id":"R03","text":"業務售前會議與產品展示","type":"required","status":"partial","evidence":["透過互動原型與 FAQ 向客服、業務說明功能"],"blocks_interview":false,"reason":"有內部業務功能說明；未明示參與外部客戶售前會議及現場展示，不推論不具能力。"},{"id":"R04","text":"Roadmap需求設計與持續迭代","type":"required","status":"supported","evidence":["依使用者旅程與工單問題安排優先級"],"blocks_interview":false,"reason":"有優先級、流程設計及分階段上線案例，支持迭代與路線規劃。"},{"id":"R05","text":"多系統/API第三方資料交換與跨系統整合","type":"required","status":"supported","evidence":["並與 CodaPay 新加坡技術團隊協調串接"],"blocks_interview":false,"reason":"第三方金流串接、新舊系統資料欄位及流程銜接支持；交換協定與錯誤處理深度可面試驗證。"},{"id":"R06","text":"專案管理、里程碑、進度及風險控制","type":"required","status":"supported","evidence":["採新舊並行、分階段上線"],"blocks_interview":false,"reason":"具上線時序、UAT、進度追蹤及相容性風險處理案例。"},{"id":"R07","text":"PRD、規格與流程設計","type":"required","status":"supported","evidence":["設計流程與畫面、撰寫 PRD 與製作 Prototype"],"blocks_interview":false,"reason":"具體描述從分析至驗收的交付工作，符合必要條件。"},{"id":"R08","text":"敏捷Scrum","type":"required","status":"supported","evidence":["曾參與每週一個 Sprint 的 Scrum"],"blocks_interview":false,"reason":"有實際參與敘述；現職混合流程不構成矛盾，角色及典型儀式可追問。"},{"id":"R09","text":"企業ERP/HRM/SaaS平台經驗","type":"preferred","status":"partial","evidence":["人力銀行企業端招募系統專案負責人"],"blocks_interview":false,"reason":"企業招募流程可轉移至HRM；未明示ERP或完整HRM/SaaS平台範圍。"},{"id":"R10","text":"SQL/BI分析","type":"preferred","status":"partial","evidence":["與 DBA 協作取數，再以 Google Sheets、Excel 分析"],"blocks_interview":false,"reason":"具取數規劃及分析；本人SQL查詢與BI工具操作未知，不作必要條件。"},{"id":"R11","text":"API、資料庫架構技術","type":"preferred","status":"partial","evidence":["API 串接規劃、舊系統資料盤點與新舊流程銜接"],"blocks_interview":false,"reason":"串接與資料規則有線索；架構設計、資料模型與技術權責待補。"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["現任 1111 招募系統 Product Owner"],"missing":["由招募流程移轉到HRM產品的領域學習可面試確認。"],"issue_ids":[]},{"id":"role_evidence","rating":"足夠","evidence":["設計流程與畫面、撰寫 PRD 與製作 Prototype"],"missing":["直接訪談與售前情境需核對；SQL/BI及架構深度為加分待補。"],"issue_ids":["I01","I02","I03"]},{"id":"decision_depth","rating":"強","evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"missing":["可補需求價值、資源與替代方案的比較依據。"],"issue_ids":[]},{"id":"outcome_quality","rating":"足夠","evidence":["平均處理時間由 100.4 天降至 30.9 天"],"missing":["案件分母、類型及統計口徑；安全事件觀察來源。"],"issue_ids":["I04","I05"]},{"id":"ownership","rating":"強","evidence":["由我主責規劃"],"missing":["可面試驗證API及Scrum情境中的具體本人責任。"],"issue_ids":[]},{"id":"readability","rating":"足夠","evidence":["工作涵蓋系統分析、流程與畫面設計、PRD"],"missing":["可將客戶訪談與售前代表作提前，降低JD對位搜尋成本。"],"issue_ids":[]}],"results":[{"quote":"系統服務逾 6 萬家活躍付費廠商（2026 Q3）","kinds":["context"]},{"quote":"公司資料於 2026/01 接續上線","kinds":["output"]},{"quote":"兩案均在開發中","kinds":["in_progress"]},{"quote":"搜尋結果頁的既有痛點，也排在新功能職缺健檢之前","kinds":["decision"]},{"quote":"平均處理時間由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]}],"hr_questions":[{"rule_id":"HR01","status":"partial","resume_evidence":["API 串接規劃"],"application_note":"核心交付相符，客訪售前待核對"},{"rule_id":"HR02","status":"supported","resume_evidence":["人力銀行企業端招募系統專案負責人"],"application_note":"企業流程經驗可轉移"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我主責規劃"],"application_note":"本人規劃與工程交付可區分"},{"rule_id":"HR04","status":"partial","resume_evidence":["平均處理時間由 100.4 天降至 30.9 天"],"application_note":"結果具期間，案件口徑待補"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"application_note":"呈現問題導向的先後判斷"},{"rule_id":"HR06","status":"supported","resume_evidence":["從 SweetRing 的海外市場開始累積產品經驗"],"application_note":"從消費端走向企業流程"},{"rule_id":"HR07","status":"supported","resume_evidence":["曾參與每週一個 Sprint 的 Scrum"],"application_note":"實際敏捷參與值得核對"},{"rule_id":"HR08","status":"supported","resume_evidence":["設計流程與畫面、撰寫 PRD 與製作 Prototype"],"application_note":"交付鏈清楚可快速定位"},{"rule_id":"HR09","status":"partial","resume_evidence":["依目前掌握的情況"],"application_note":"觀察來源宜核對非直接否定"},{"rule_id":"HR10","status":"supported","resume_evidence":["承擔更完整的問題定義、方向選擇與成效責任"],"application_note":"方向與資深產品工作相容"},{"rule_id":"HR11","status":"unknown","resume_evidence":["可接受遠端或混合辦公"],"application_note":"地點形式相容，薪資期望未知"},{"rule_id":"HR12","status":"supported","resume_evidence":["與工程於 2025/09 完成上線"],"application_note":"支持邀約驗證客訪與技術深度"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":"轉到HRM時，哪些企業流程可直接沿用？"},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"partial","resume_evidence":["使用者訪談與問卷"],"evidence_type":"context","source_ids":[],"interview_question":"請還原一次直接客訪，客戶原話如何改變方案及規格？"},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":"當時如何比較價值、成本與風險，誰決定取捨？"},{"rule_id":"HM04","primary_dimension":"role_evidence","status":"supported","resume_evidence":["團隊依結果決定採用低價"],"evidence_type":"decision","source_ids":[],"interview_question":"定價實驗有哪些混雜因素，如何用於企業產品？"},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["平均處理時間由 100.4 天降至 30.9 天"],"evidence_type":"outcome","source_ids":[],"interview_question":"兩季樣本、起迄點及案件類型是否一致？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["與 QA 制定 UAT 驗收案例"],"evidence_type":"output","source_ids":[],"interview_question":"你與工程、QA及兩名產品企劃如何分工與處理分歧？"},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["處理新舊系統並行的相容性需求"],"evidence_type":"output","source_ids":[],"interview_question":"分階段切換的驗收門檻、回滾與風險如何管理？"},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"partial","resume_evidence":["並與 CodaPay 新加坡技術團隊協調串接"],"evidence_type":"output","source_ids":[],"interview_question":"請展示資料交換規格及失敗重試、對帳驗收規則。"},{"rule_id":"HM09","primary_dimension":"ownership","status":"supported","resume_evidence":["重新制定業務流程、對照資料欄位並重構規格"],"evidence_type":"output","source_ids":[],"interview_question":"哪些方向由你決定，哪些由主管或工程決定？"},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["設計流程與畫面、撰寫 PRD 與製作 Prototype"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["並依客服回饋修正操作流程"],"evidence_type":"decision","source_ids":[],"interview_question":"哪個回饋推翻原方案，後來如何轉用？"},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["透過互動原型與 FAQ 向客服、業務說明功能"],"evidence_type":"output","source_ids":[],"interview_question":"請用產品展示還原一次售前場景及客戶提問。"},{"rule_id":"HM13","primary_dimension":"method","status":"supported","resume_evidence":["兩案均在開發中"],"evidence_type":"in_progress","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HM02","source_ids":[],"application_note":"面試核對，不直接否定","context_limit":"必要條件僅部分支持；未提供不等於沒做過。","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"使用者訪談與問卷","reason":"技能列示未交代直接客訪的對象、方法及轉規格過程。","suggestion":"補一次客訪、洞察改案與PRD對應案例。"},{"id":"I02","rule_id":"HM12","source_ids":[],"application_note":"面試核對，不直接否定","context_limit":"內部說明不能直接代替客戶售前。","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"透過互動原型與 FAQ 向客服、業務說明功能","reason":"證明內部業務賦能，未明示外部售前會議與展示。","suggestion":"補客戶售前會議本人角色及展示後需求取捨。"},{"id":"I03","rule_id":"HM08","source_ids":[],"application_note":"面試核對，不直接否定","context_limit":"多系統必要已有案例；深度多屬加分。","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"API 串接規劃","reason":"支持整合經驗，SQL/BI實作與資料庫架構深度仍未知。","suggestion":"以去識別規格說明資料映射、異常處理與本人權責。"},{"id":"I04","rule_id":"HM05","source_ids":[],"application_note":"面試核對，不直接否定","context_limit":"不能單獨歸因本人或推論客戶成效。","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"平均處理時間由 100.4 天降至 30.9 天","reason":"有期間及前後值，但母體、結案口徑與案件組成未交代。","suggestion":"補案件數、計時規則及跨季可比限制。"},{"id":"I05","rule_id":"HR09","source_ids":[],"application_note":"面試核對，不直接否定","context_limit":"不等同完整安全監測或零事件證明。","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"調整後至 2026/10 未再出現同類冒用","reason":"是掌握範圍內觀察，未提供監測來源及通報覆蓋。","suggestion":"補觀察來源、覆蓋範圍及可能漏報限制。"}],"decision":{"recommendation":"interview","evidence":["設計流程與畫面、撰寫 PRD 與製作 Prototype","並與 CodaPay 新加坡技術團隊協調串接","搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["「設計流程與畫面、撰寫 PRD 與製作 Prototype」支持需求至驗收交付。","「並與 CodaPay 新加坡技術團隊協調串接」支持第三方整合。","「搜尋結果頁的既有痛點，也排在新功能職缺健檢之前」支持優先級判斷。"],"key_gaps":["直接客訪與售前案例未具體：追問客戶洞察如何轉規格並展示。","SQL/BI與API架構深度待補：追問本人資料規格及技術邊界。","成效口徑待補：追問處理週期母體及安全事件觀察來源。"],"strengths":["企業招募流程與舊系統迭代具直接可轉移性。","需求分析、規格、UAT及分段交付責任清楚。","有優先級取捨與對照實驗，區分決策和已實現結果。"],"interview_questions":["還原一次直接客訪：誰、什麼問題、哪個洞察改變方案與規格？","曾如何參與業務售前及產品展示，面對客戶異議如何處理？","CodaPay串接如何定義欄位、失敗處理、對帳與驗收？","Scrum中本人角色、迭代目標及變更處理方式為何？","新舊並行的里程碑、回滾門檻及跨部門分歧如何決定？","處理時間兩季的案件數、類型和計時口徑是否一致？","你實際操作哪些SQL/BI工作，DBA與你各負責什麼？","請說明一次資源取捨及未採方案，哪些方向由你決定？"],"editorial_appendix":[],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"多案例支持企業流程、交付、整合與優先級取捨；定價有比較衡量及限制可追問。直接客訪售前及量測追溯未全，進行中整合不計已實現成效，不足以支持9。"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"not_tested","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 單份審查｜履歷 appendix-A-v10.2｜第 8 輪｜model_id: unknown

#### 1. 結論

- 招聘決定：`interview`
- Level：8（±1）
- 一句話理由：「設計流程與畫面、撰寫 PRD 與製作 Prototype」支持面試，缺口依下表核對。

#### 2. 六維度

| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 現任 1111 招募系統 Product Owner | 由招募流程移轉到HRM產品的領域學習可面試確認。 |
| role_evidence | 足夠 | 設計流程與畫面、撰寫 PRD 與製作 Prototype | 直接訪談與售前情境需核對；SQL/BI及架構深度為加分待補。 |
| decision_depth | 強 | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 可補需求價值、資源與替代方案的比較依據。 |
| outcome_quality | 足夠 | 平均處理時間由 100.4 天降至 30.9 天 | 案件分母、類型及統計口徑；安全事件觀察來源。 |
| ownership | 強 | 由我主責規劃 | 可面試驗證API及Scrum情境中的具體本人責任。 |
| readability | 足夠 | 工作涵蓋系統分析、流程與畫面設計、PRD | 可將客戶訪談與售前代表作提前，降低JD對位搜尋成本。 |

#### 3. JD 條件對照

| 條件 | 必要／加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 3年以上產品規劃與訪談；熟悉新產品或迭代 | 必要 | partial | 近 10 年 PM 經驗，經手 6 款產品 | 年資與新產品、迭代案例支持規劃經驗；訪談僅技能列示，直接訪談對象、頻率與如何轉為方案待釐清。 |
| 直接客戶訪談、分析方案並轉為規格開發項 | 必要 | partial | 釐清需求並完成系統分析後 | 需求轉規格與開發項有具體流程；直接訪談仍未提供案例，與R01共用I01缺口。 |
| 業務售前會議與產品展示 | 必要 | partial | 透過互動原型與 FAQ 向客服、業務說明功能 | 有內部業務功能說明；未明示參與外部客戶售前會議及現場展示，不推論不具能力。 |
| Roadmap需求設計與持續迭代 | 必要 | supported | 依使用者旅程與工單問題安排優先級 | 有優先級、流程設計及分階段上線案例，支持迭代與路線規劃。 |
| 多系統/API第三方資料交換與跨系統整合 | 必要 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 第三方金流串接、新舊系統資料欄位及流程銜接支持；交換協定與錯誤處理深度可面試驗證。 |
| 專案管理、里程碑、進度及風險控制 | 必要 | supported | 採新舊並行、分階段上線 | 具上線時序、UAT、進度追蹤及相容性風險處理案例。 |
| PRD、規格與流程設計 | 必要 | supported | 設計流程與畫面、撰寫 PRD 與製作 Prototype | 具體描述從分析至驗收的交付工作，符合必要條件。 |
| 敏捷Scrum | 必要 | supported | 曾參與每週一個 Sprint 的 Scrum | 有實際參與敘述；現職混合流程不構成矛盾，角色及典型儀式可追問。 |
| 企業ERP/HRM/SaaS平台經驗 | 加分 | partial | 人力銀行企業端招募系統專案負責人 | 企業招募流程可轉移至HRM；未明示ERP或完整HRM/SaaS平台範圍。 |
| SQL/BI分析 | 加分 | partial | 與 DBA 協作取數，再以 Google Sheets、Excel 分析 | 具取數規劃及分析；本人SQL查詢與BI工具操作未知，不作必要條件。 |
| API、資料庫架構技術 | 加分 | partial | API 串接規劃、舊系統資料盤點與新舊流程銜接 | 串接與資料規則有線索；架構設計、資料模型與技術權責待補。 |

#### 4. HR 十二問／HM 十三問

| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | partial | API 串接規劃 | 核心交付相符，客訪售前待核對 |
| HR02 | supported | 人力銀行企業端招募系統專案負責人 | 企業流程經驗可轉移 |
| HR03 | supported | 由我主責規劃 | 本人規劃與工程交付可區分 |
| HR04 | partial | 平均處理時間由 100.4 天降至 30.9 天 | 結果具期間，案件口徑待補 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 呈現問題導向的先後判斷 |
| HR06 | supported | 從 SweetRing 的海外市場開始累積產品經驗 | 從消費端走向企業流程 |
| HR07 | supported | 曾參與每週一個 Sprint 的 Scrum | 實際敏捷參與值得核對 |
| HR08 | supported | 設計流程與畫面、撰寫 PRD 與製作 Prototype | 交付鏈清楚可快速定位 |
| HR09 | partial | 依目前掌握的情況 | 觀察來源宜核對非直接否定 |
| HR10 | supported | 承擔更完整的問題定義、方向選擇與成效責任 | 方向與資深產品工作相容 |
| HR11 | unknown | 可接受遠端或混合辦公 | 地點形式相容，薪資期望未知 |
| HR12 | supported | 與工程於 2025/09 完成上線 | 支持邀約驗證客訪與技術深度 |
| HM01 | supported | 人力銀行企業端招募系統專案負責人 | 企業流程可轉移，HRM可學 |
| HM02 | partial | 使用者訪談與問卷 | 直接客訪深度面試驗證 |
| HM03 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 取捨成立，進行中非成果 |
| HM04 | supported | 團隊依結果決定採用低價 | 商業實驗可轉移，未要求P&L |
| HM05 | partial | 平均處理時間由 100.4 天降至 30.9 天 | 期間已述，母體待補 |
| HM06 | supported | 與 QA 制定 UAT 驗收案例 | 協作與本人責任可區分 |
| HM07 | supported | 處理新舊系統並行的相容性需求 | 上線及相容性支持風險管理 |
| HM08 | partial | 並與 CodaPay 新加坡技術團隊協調串接 | 整合支持，技術深度待核對 |
| HM09 | supported | 重新制定業務流程、對照資料欄位並重構規格 | 複雜度支持資深，非以年資判 |
| HM10 | supported | 設計流程與畫面、撰寫 PRD 與製作 Prototype | 規劃到驗收脈絡清楚 |
| HM11 | supported | 並依客服回饋修正操作流程 | 有回饋改流程的行動 |
| HM12 | supported | 透過互動原型與 FAQ 向客服、業務說明功能 | 面試核對售前及客訪能力 |
| HM13 | supported | 兩案均在開發中 | 凍結準則；模型一致非真人效度 |

#### 5. 約談理由（≤3）與關鍵缺口（≤3）

| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「設計流程與畫面、撰寫 PRD 與製作 Prototype」支持需求至驗收交付。 |
| 2 | 「並與 CodaPay 新加坡技術團隊協調串接」支持第三方整合。 |
| 3 | 「搜尋結果頁的既有痛點，也排在新功能職缺健檢之前」支持優先級判斷。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 直接客訪與售前案例未具體：追問客戶洞察如何轉規格並展示。 | 還原一次直接客訪：誰、什麼問題、哪個洞察改變方案與規格？ |
| 2 | SQL/BI與API架構深度待補：追問本人資料規格及技術邊界。 | 曾如何參與業務售前及產品展示，面對客戶異議如何處理？ |
| 3 | 成效口徑待補：追問處理週期母體及安全事件觀察來源。 | CodaPay串接如何定義欄位、失敗處理、對帳與驗收？ |

#### 6. 評語（給寫稿者的具體回饋）

**做得好（3 點）**

- 專業摘要｜「現任 1111 招募系統 Product Owner」｜企業招募流程與舊系統迭代具直接可轉移性。
- Product Owner／PM｜1111 全球華人｜「設計流程與畫面、撰寫 PRD 與製作 Prototype」｜需求分析、規格、UAT及分段交付責任清楚。
- Product Owner／PM｜1111 全球華人｜「搜尋結果頁的既有痛點，也排在新功能職缺健檢之前」｜有優先級取捨與對照實驗，區分決策和已實現結果。

**可改進（≤5 點）**

- 位置：專業技能
  - 原句：「使用者訪談與問卷」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：技能列示未交代直接客訪的對象、方法及轉規格過程。 面試核對，不直接否定
  - 建議方向：補一次客訪、洞察改案與PRD對應案例。

- 位置：Product Owner／PM｜1111 全球華人
  - 原句：「透過互動原型與 FAQ 向客服、業務說明功能」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：證明內部業務賦能，未明示外部售前會議與展示。 面試核對，不直接否定
  - 建議方向：補客戶售前會議本人角色及展示後需求取捨。

- 位置：專業技能
  - 原句：「API 串接規劃」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：支持整合經驗，SQL/BI實作與資料庫架構深度仍未知。 面試核對，不直接否定
  - 建議方向：以去識別規格說明資料映射、異常處理與本人權責。

- 位置：Product Owner／PM｜1111 全球華人
  - 原句：「平均處理時間由 100.4 天降至 30.9 天」
  - 問題類型：`measurement`
  - 嚴重度：`interview_follow_up`
  - 影響：有期間及前後值，但母體、結案口徑與案件組成未交代。 面試核對，不直接否定
  - 建議方向：補案件數、計時規則及跨季可比限制。

- 位置：Product Owner／PM｜1111 全球華人
  - 原句：「調整後至 2026/10 未再出現同類冒用」
  - 問題類型：`measurement`
  - 嚴重度：`interview_follow_up`
  - 影響：是掌握範圍內觀察，未提供監測來源及通報覆蓋。 面試核對，不直接否定
  - 建議方向：補觀察來源、覆蓋範圍及可能漏報限制。

**編輯附件**：無。

#### 7. 資深能力分布

delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

#### 8. 未測試聲明

PDF 抽字：本內容審查 `not_tested`（另見總報告 §6 的 `local_extraction`）／ATS 匯入：`not_tested`／AI 作者判讀：不可由文字判定／真人校準：`not_run`。

### A.09｜jd32｜原始單行 JSON

```json
{"rubric_version":"4.2","resume_id":"appendix-A-v10.2","job_id":"jd32","job_input":"summary","model_id":"unknown","run_id":"jd32-A-01","human_calibrated":false,"requirements":[{"id":"R01","text":"經歷3年以上","type":"required","status":"supported","evidence":["Product Owner／PM｜1111 全球華人｜2022/08 - 迄今"],"blocks_interview":false,"reason":"最近一段職務已超過3年；不以年資推定資深能力。"},{"id":"R02","text":"內部營運網站設計、規格與驗收","type":"required","status":"partial","evidence":["再與 QA 制定 UAT 驗收案例、排定上線計畫"],"blocks_interview":false,"reason":"網站系統流程、PRD及驗收有案例；目前主要為企業客戶端系統，純內部營運網站用途尚待釐清。"},{"id":"R03","text":"內外議題優化修正","type":"required","status":"supported","evidence":["並依客服回饋修正操作流程"],"blocks_interview":false,"reason":"帳號冒用處理與客服回饋迭代直接對位。"},{"id":"R04","text":"跨單位產品整合提案","type":"required","status":"supported","evidence":["使我優先推進信件與即時通整合"],"blocks_interview":false,"reason":"有跨部門需求及整合提案；此整合仍開發中，僅支持決策與進度。"},{"id":"R05","text":"與團隊評估可行性與時程","type":"required","status":"supported","evidence":["處理新舊系統並行的相容性需求"],"blocks_interview":false,"reason":"有相容性分析及分階段上線；估時協商與資源限制可於面試深化。"},{"id":"R06","text":"資訊／網站開發經驗或SA","type":"preferred","status":"supported","evidence":["重新制定業務流程、對照資料欄位並重構規格"],"blocks_interview":false,"reason":"以實際系統分析支持SA分支，不要求另證明資訊學歷或程式實作。"},{"id":"R07","text":"AI營運分析或提案","type":"preferred","status":"partial","evidence":["運用 AI Agent 撰寫規格、整理與分析資料"],"blocks_interview":false,"reason":"有AI協作及AI產品情境驗收；營運分析的具體輸入、判讀及提案成效待補。"},{"id":"R08","text":"規格與跨單位溝通","type":"preferred","status":"supported","evidence":["透過互動原型與 FAQ 向客服、業務說明功能"],"blocks_interview":false,"reason":"有文件、原型、QA與客服業務溝通案例。"},{"id":"R09","text":"細心、耐心、團隊導向","type":"preferred","status":"partial","evidence":["逐一對照資料欄位並重構規格"],"blocks_interview":false,"reason":"欄位盤點與協作是行為線索；不能從文風確證人格，適合面試情境核對。"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["人力銀行企業端招募系統專案負責人"],"missing":["企業端經驗可轉移；須確認對內部營運系統的動機。"],"issue_ids":["I03"]},{"id":"role_evidence","rating":"強","evidence":["設計流程與畫面、撰寫 PRD 與製作 Prototype"],"missing":["內部營運情境及AI分析實例待核對。"],"issue_ids":["I01","I04"]},{"id":"decision_depth","rating":"強","evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"missing":["可追問估時、替代方案及決策權限。"],"issue_ids":["I05"]},{"id":"outcome_quality","rating":"足夠","evidence":["平均處理時間由 100.4 天降至 30.9 天"],"missing":["案件分母、起訖定義及積案清理影響未列。"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃。"],"missing":["資源配置與估時核定權限待補。"],"issue_ids":["I05"]},{"id":"readability","rating":"足夠","evidence":["工作涵蓋系統分析、流程與畫面設計、PRD、Prototype、UAT 與上線計畫"],"missing":["摘要可更突出內部營運問題與案例。"],"issue_ids":[]}],"results":[{"quote":"系統服務逾 6 萬家活躍付費廠商（2026 Q3）","kinds":["context"]},{"quote":"與工程於 2025/09 完成上線。","kinds":["output"]},{"quote":"平均處理時間由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"搜尋結果頁的既有痛點，也排在新功能職缺健檢之前","kinds":["decision"]},{"quote":"兩案均在開發中","kinds":["in_progress"]},{"quote":"調整後至 2026/10 未再出現同類冒用。","kinds":["outcome"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["設計流程與畫面、撰寫 PRD 與製作 Prototype"],"application_note":"規格與驗收直接對位"},{"rule_id":"HR02","status":"supported","resume_evidence":["人力銀行企業端招募系統專案負責人"],"application_note":"企業端與內部營運差異待談"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我主責規劃"],"application_note":"本人規劃與工程交付有區分"},{"rule_id":"HR04","status":"partial","resume_evidence":["平均處理時間由 100.4 天降至 30.9 天"],"application_note":"需核對案件範圍與計算口徑"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"application_note":"有優先級依據，可深入取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從 SweetRing 的海外市場開始累積產品經驗"],"application_note":"由在地化轉向企業系統"},{"rule_id":"HR07","status":"supported","resume_evidence":["與資料科學團隊合作"],"application_note":"AI與工程協作有情境"},{"rule_id":"HR08","status":"supported","resume_evidence":["工作涵蓋系統分析、流程與畫面設計、PRD、Prototype、UAT 與上線計畫"],"application_note":"核心工作可快速辨識"},{"rule_id":"HR09","status":"partial","resume_evidence":["依目前掌握的情況"],"application_note":"安全結果屬有限觀察待核對"},{"rule_id":"HR10","status":"partial","resume_evidence":["接下來，我希望把更多心力放回產品策略"],"application_note":"確認內部系統交付與策略期待"},{"rule_id":"HR11","status":"partial","resume_evidence":["台北市、新北市，可接受遠端或混合辦公"],"application_note":"地點大致相容；薪資通勤待談"},{"rule_id":"HR12","status":"supported","resume_evidence":["再與 QA 制定 UAT 驗收案例、排定上線計畫"],"application_note":"支持約談，缺口可面試釐清"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":"請比較企業客戶招募系統與內部營運網站的需求差異。"},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程與工單問題安排優先級。"],"evidence_type":"decision","source_ids":[],"interview_question":"哪一類工單改變了原本的需求排序？"},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":"如何比較兩案價值、成本及風險，誰核定排序？"},{"rule_id":"HM04","primary_dimension":"role_evidence","status":"supported","resume_evidence":["整理抽成、稅、手續費與撥款週期"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["平均處理時間由 100.4 天降至 30.9 天"],"evidence_type":"outcome","source_ids":[],"interview_question":"案件起訖、分母、類型及清理積案如何影響均值？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["再與 QA 制定 UAT 驗收案例、排定上線計畫"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["採新舊並行、分階段上線"],"evidence_type":"output","source_ids":[],"interview_question":"請展示規格、驗收及上線風險管理案例。"},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["舊帳號信箱並非唯一值的限制"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"ownership","status":"supported","resume_evidence":["重新制定業務流程、對照資料欄位並重構規格"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["現任 1111 招募系統 Product Owner"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["並依客服測試回饋調整推薦規則。"],"evidence_type":"decision","source_ids":[],"interview_question":"哪項測試反證原本規則，改動後如何驗收？"},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["定義使用情境與驗收標準"],"evidence_type":"output","source_ids":[],"interview_question":"請提供AI營運分析或提案的輸入、檢核與採用案例。"},{"rule_id":"HM13","primary_dimension":"method","status":"supported","resume_evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃。"],"evidence_type":"output","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HM01","source_ids":[],"application_note":"企業端可轉移但情境待核對","context_limit":"本職為內部營運網站","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"人力銀行企業端招募系統專案負責人","reason":"企業端工作不等於內部營運網站；已有系統分析與跨單位案例，仍值得約談。","suggestion":"補一項內部作業人員使用情境與其流程改變。"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"結果量測口徑須核對","context_limit":"積案清理後追蹤Q1至Q2均值","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"平均處理時間由 100.4 天降至 30.9 天","reason":"有期間及均值，未列件數、起訖與案件組成，不能全歸因個人；主要計於成果品質。","suggestion":"補各季案件數、計時定義及積案或案件組成變化。"},{"id":"I03","rule_id":"HR10","source_ids":[],"application_note":"確認職務期待","context_limit":"職缺以內部系統專案交付為主","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"接下來，我希望把更多心力放回產品策略","reason":"策略期待與內部系統日常是否相容未明，不構成無興趣或不符。","suggestion":"說明願意承擔的營運優化、交付與策略工作比例。"},{"id":"I04","rule_id":"HM12","source_ids":[],"application_note":"AI分析深度可追問","context_limit":"JD希望AI營運分析或提案","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"運用 AI Agent 撰寫規格、整理與分析資料","reason":"有工具應用及AI產品驗收，尚缺營運分析如何轉成提案的實例；不阻擋面試。","suggestion":"補資料來源、分析發現、人工核對及提案採用情況。"},{"id":"I05","rule_id":"HM03","source_ids":[],"application_note":"深化可行性與時程判斷","context_limit":"已有分階段交付案例","category":"ownership","severity":"interview_follow_up","block_target":null,"claim":"與內部工程團隊分階段交付","reason":"時程與交付已呈現，估時方式、資源取捨及本人核定權限未展開；主要計於決策深化。","suggestion":"補一例估時分歧、範圍縮減或延期決策及核定邊界。"}],"decision":{"recommendation":"interview","evidence":["設計流程與畫面、撰寫 PRD 與製作 Prototype","再與 QA 制定 UAT 驗收案例、排定上線計畫","搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"待補"},"interview_reasons":["「再與 QA 制定 UAT 驗收案例、排定上線計畫」支持規格驗收交付。","「舊帳號信箱並非唯一值的限制」支持在既有系統限制下分析。","「透過互動原型與 FAQ 向客服、業務說明功能」支持跨單位溝通。"],"key_gaps":["內部營運使用情境與策略期待：追問日常任務及投入比例。","AI營運分析：追問資料、人工核對、洞察與提案採用。","量測與資源邊界：追問案件均值口徑及估時核定責任。"],"strengths":["規格、原型、驗收與上線鏈條完整。","能把權限、資料與相容性限制轉為可交付流程。","具跨單位協調及依工單決定優先級的實例。"],"interview_questions":["請比較企業客戶招募系統與內部營運網站的需求差異。","哪一類工單改變了原本的需求排序？","如何比較兩案價值、成本及風險，誰核定排序？","案件起訖、分母、類型及清理積案如何影響均值？","請展示規格、驗收及上線風險管理案例。","哪項測試反證原本規則，改動後如何驗收？","請提供AI營運分析或提案的輸入、檢核與採用案例。"],"editorial_appendix":[],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"多個系統分析、協作與交付案例，並有優先級取捨及帶期間的成果。內部營運情境、AI分析深度、成果分母與資源核定邊界待核；進行中整合僅作決策證據，未當成結果，不支持9。"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"not_tested","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 單份審查｜履歷 appendix-A-v10.2｜第 9 輪｜model_id: unknown

#### 1. 結論

- 招聘決定：`interview`
- Level：8（±1）
- 一句話理由：「設計流程與畫面、撰寫 PRD 與製作 Prototype」支持面試，缺口依下表核對。

#### 2. 六維度

| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 人力銀行企業端招募系統專案負責人 | 企業端經驗可轉移；須確認對內部營運系統的動機。 |
| role_evidence | 強 | 設計流程與畫面、撰寫 PRD 與製作 Prototype | 內部營運情境及AI分析實例待核對。 |
| decision_depth | 強 | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 可追問估時、替代方案及決策權限。 |
| outcome_quality | 足夠 | 平均處理時間由 100.4 天降至 30.9 天 | 案件分母、起訖定義及積案清理影響未列。 |
| ownership | 強 | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃。 | 資源配置與估時核定權限待補。 |
| readability | 足夠 | 工作涵蓋系統分析、流程與畫面設計、PRD、Prototype、UAT 與上線計畫 | 摘要可更突出內部營運問題與案例。 |

#### 3. JD 條件對照

| 條件 | 必要／加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 經歷3年以上 | 必要 | supported | Product Owner／PM｜1111 全球華人｜2022/08 - 迄今 | 最近一段職務已超過3年；不以年資推定資深能力。 |
| 內部營運網站設計、規格與驗收 | 必要 | partial | 再與 QA 制定 UAT 驗收案例、排定上線計畫 | 網站系統流程、PRD及驗收有案例；目前主要為企業客戶端系統，純內部營運網站用途尚待釐清。 |
| 內外議題優化修正 | 必要 | supported | 並依客服回饋修正操作流程 | 帳號冒用處理與客服回饋迭代直接對位。 |
| 跨單位產品整合提案 | 必要 | supported | 使我優先推進信件與即時通整合 | 有跨部門需求及整合提案；此整合仍開發中，僅支持決策與進度。 |
| 與團隊評估可行性與時程 | 必要 | supported | 處理新舊系統並行的相容性需求 | 有相容性分析及分階段上線；估時協商與資源限制可於面試深化。 |
| 資訊／網站開發經驗或SA | 加分 | supported | 重新制定業務流程、對照資料欄位並重構規格 | 以實際系統分析支持SA分支，不要求另證明資訊學歷或程式實作。 |
| AI營運分析或提案 | 加分 | partial | 運用 AI Agent 撰寫規格、整理與分析資料 | 有AI協作及AI產品情境驗收；營運分析的具體輸入、判讀及提案成效待補。 |
| 規格與跨單位溝通 | 加分 | supported | 透過互動原型與 FAQ 向客服、業務說明功能 | 有文件、原型、QA與客服業務溝通案例。 |
| 細心、耐心、團隊導向 | 加分 | partial | 逐一對照資料欄位並重構規格 | 欄位盤點與協作是行為線索；不能從文風確證人格，適合面試情境核對。 |

#### 4. HR 十二問／HM 十三問

| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 設計流程與畫面、撰寫 PRD 與製作 Prototype | 規格與驗收直接對位 |
| HR02 | supported | 人力銀行企業端招募系統專案負責人 | 企業端與內部營運差異待談 |
| HR03 | supported | 由我主責規劃 | 本人規劃與工程交付有區分 |
| HR04 | partial | 平均處理時間由 100.4 天降至 30.9 天 | 需核對案件範圍與計算口徑 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 有優先級依據，可深入取捨 |
| HR06 | supported | 從 SweetRing 的海外市場開始累積產品經驗 | 由在地化轉向企業系統 |
| HR07 | supported | 與資料科學團隊合作 | AI與工程協作有情境 |
| HR08 | supported | 工作涵蓋系統分析、流程與畫面設計、PRD、Prototype、UAT 與上線計畫 | 核心工作可快速辨識 |
| HR09 | partial | 依目前掌握的情況 | 安全結果屬有限觀察待核對 |
| HR10 | partial | 接下來，我希望把更多心力放回產品策略 | 確認內部系統交付與策略期待 |
| HR11 | partial | 台北市、新北市，可接受遠端或混合辦公 | 地點大致相容；薪資通勤待談 |
| HR12 | supported | 再與 QA 制定 UAT 驗收案例、排定上線計畫 | 支持約談，缺口可面試釐清 |
| HM01 | supported | 人力銀行企業端招募系統專案負責人 | 核心需系統規格協作；內部情境可學 |
| HM02 | supported | 依使用者旅程與工單問題安排優先級。 | 使用者問題可追到排序 |
| HM03 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 進行中案僅支持取捨 |
| HM04 | supported | 整理抽成、稅、手續費與撥款週期 | 成本思考可轉移；不要求P&L |
| HM05 | partial | 平均處理時間由 100.4 天降至 30.9 天 | 均值與有限觀察需核對 |
| HM06 | supported | 再與 QA 制定 UAT 驗收案例、排定上線計畫 | 分工明確，非工程本人實作 |
| HM07 | supported | 採新舊並行、分階段上線 | 交付風險有具體案例 |
| HM08 | supported | 舊帳號信箱並非唯一值的限制 | 技術協作足夠，不強求程式 |
| HM09 | supported | 重新制定業務流程、對照資料欄位並重構規格 | 交付與協調強，資源權待補 |
| HM10 | supported | 現任 1111 招募系統 Product Owner | 摘要與案例可辨認職責 |
| HM11 | supported | 並依客服測試回饋調整推薦規則。 | 有回饋修正，需深化反證 |
| HM12 | supported | 定義使用情境與驗收標準 | 案例足以約談，AI分析待核 |
| HM13 | supported | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃。 | 固定規準判讀，非真人效度 |

#### 5. 約談理由（≤3）與關鍵缺口（≤3）

| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「再與 QA 制定 UAT 驗收案例、排定上線計畫」支持規格驗收交付。 |
| 2 | 「舊帳號信箱並非唯一值的限制」支持在既有系統限制下分析。 |
| 3 | 「透過互動原型與 FAQ 向客服、業務說明功能」支持跨單位溝通。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 內部營運使用情境與策略期待：追問日常任務及投入比例。 | 請比較企業客戶招募系統與內部營運網站的需求差異。 |
| 2 | AI營運分析：追問資料、人工核對、洞察與提案採用。 | 哪一類工單改變了原本的需求排序？ |
| 3 | 量測與資源邊界：追問案件均值口徑及估時核定責任。 | 如何比較兩案價值、成本及風險，誰核定排序？ |

#### 6. 評語（給寫稿者的具體回饋）

**做得好（3 點）**

- Product Owner／PM｜1111 全球華人｜「人力銀行企業端招募系統專案負責人」｜規格、原型、驗收與上線鏈條完整。
- Product Owner／PM｜1111 全球華人｜「設計流程與畫面、撰寫 PRD 與製作 Prototype」｜能把權限、資料與相容性限制轉為可交付流程。
- Product Owner／PM｜1111 全球華人｜「搜尋結果頁的既有痛點，也排在新功能職缺健檢之前」｜具跨單位協調及依工單決定優先級的實例。

**可改進（≤5 點）**

- 位置：Product Owner／PM｜1111 全球華人
  - 原句：「人力銀行企業端招募系統專案負責人」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：企業端工作不等於內部營運網站；已有系統分析與跨單位案例，仍值得約談。 企業端可轉移但情境待核對
  - 建議方向：補一項內部作業人員使用情境與其流程改變。

- 位置：Product Owner／PM｜1111 全球華人
  - 原句：「平均處理時間由 100.4 天降至 30.9 天」
  - 問題類型：`measurement`
  - 嚴重度：`interview_follow_up`
  - 影響：有期間及均值，未列件數、起訖與案件組成，不能全歸因個人；主要計於成果品質。 結果量測口徑須核對
  - 建議方向：補各季案件數、計時定義及積案或案件組成變化。

- 位置：自傳
  - 原句：「接下來，我希望把更多心力放回產品策略」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：策略期待與內部系統日常是否相容未明，不構成無興趣或不符。 確認職務期待
  - 建議方向：說明願意承擔的營運優化、交付與策略工作比例。

- 位置：專業技能
  - 原句：「運用 AI Agent 撰寫規格、整理與分析資料」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：有工具應用及AI產品驗收，尚缺營運分析如何轉成提案的實例；不阻擋面試。 AI分析深度可追問
  - 建議方向：補資料來源、分析發現、人工核對及提案採用情況。

- 位置：Product Owner／PM｜1111 全球華人
  - 原句：「與內部工程團隊分階段交付」
  - 問題類型：`ownership`
  - 嚴重度：`interview_follow_up`
  - 影響：時程與交付已呈現，估時方式、資源取捨及本人核定權限未展開；主要計於決策深化。 深化可行性與時程判斷
  - 建議方向：補一例估時分歧、範圍縮減或延期決策及核定邊界。

**編輯附件**：無。

#### 7. 資深能力分布

delivery：強 ／ po_coordination：強 ／ direction_resources：待補

#### 8. 未測試聲明

PDF 抽字：本內容審查 `not_tested`（另見總報告 §6 的 `local_extraction`）／ATS 匯入：`not_tested`／AI 作者判讀：不可由文字判定／真人校準：`not_run`。

### A.10｜jd34｜原始單行 JSON

```json
{"rubric_version":"4.2","resume_id":"appendix-A-v10.2","job_id":"jd34","job_input":"summary","model_id":"unknown","run_id":"jd34-A-01","human_calibrated":false,"requirements":[{"id":"R01","text":"產品管理內文2年以上；經歷欄5年以上（兩者並列）","type":"required","status":"supported","evidence":["近 10 年 PM 經驗"],"blocks_interview":false,"reason":"2016年至今的PM經歷支持兩項年資條件，資深程度另依案例判讀。"},{"id":"R02","text":"金流、物流、會員、促購優惠券、購買流程、訂單相關功能經驗","type":"required","status":"partial","evidence":["規劃使用流程、訂閱與付費機制"],"blocks_interview":false,"reason":"金流、付費購買流程與訂閱有案例；會員僅帳號權限可轉移；物流、優惠券及訂單未明示。JD未明示每項均為硬門檻，面試釐清廣度。"},{"id":"R03","text":"完整週期交付上市；新產品完整開發","type":"required","status":"supported","evidence":["主導 Juicy 推出"],"blocks_interview":false,"reason":"上市、PRD、UAT與上線計畫均有證據；新產品亦有KOOL與Juicy案例。"},{"id":"R04","text":"商業模式、關係人需求與規格；UX、RD、QA及設計合作","type":"required","status":"supported","evidence":["與 QA 制定 UAT 驗收案例"],"blocks_interview":false,"reason":"付費模式、10個需求單位、工程設計合作及規格交付可對位。"},{"id":"R05","text":"定義目標並衡量數據效益；維運優化指標效率","type":"required","status":"supported","evidence":["平均處理時間由 100.4 天降至 30.9 天"],"blocks_interview":false,"reason":"定價實驗及處理週期支持；營運效益的母體與歸因仍需追問。"},{"id":"R06","text":"UI製作","type":"required","status":"supported","evidence":["設計流程與畫面"],"blocks_interview":false,"reason":"實際畫面、Prototype規劃與工具支持UI製作；可用作品確認細節。"},{"id":"R07","text":"參與運作Scrum","type":"required","status":"supported","evidence":["曾參與每週一個 Sprint 的 Scrum"],"blocks_interview":false,"reason":"符合參與經驗；現況為Kanban搭配瀑布，面試追問Scrum職責。"},{"id":"R08","text":"支付生態趨勢","type":"preferred","status":"partial","evidence":["整理抽成、稅、手續費與撥款週期"],"blocks_interview":false,"reason":"支持支付方案商業理解；未提供近期生態趨勢洞察。"},{"id":"R09","text":"募資提案簡報","type":"preferred","status":"unknown","evidence":[],"blocks_interview":false,"reason":"未呈現募資提案；主管匯報不等同募資。"},{"id":"R10","text":"200人以上軟體開發團隊工作2年以上","type":"preferred","status":"unknown","evidence":[],"blocks_interview":false,"reason":"履歷未呈現開發團隊人數，不能以公司規模推定。"},{"id":"R11","text":"GenAI產品案例","type":"preferred","status":"supported","evidence":["上線公司簡介生成、職缺工作說明生成及 AI 推薦人才"],"blocks_interview":false,"reason":"生成式功能已上線，定義情境與驗收責任有述；不把AI工具使用等同產品成果。"},{"id":"R12","text":"全通路新零售SaaS商業方向及Commerce Cloud、G11N、OMO情境","type":"required","status":"partial","evidence":["讓印尼、泰國等市場的用戶可用電信帳單與超商付款"],"blocks_interview":false,"reason":"企業流程、跨市場支付可轉移；未直接呈現零售OMO與商家營運案例。"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["現任 1111 招募系統 Product Owner"],"missing":["零售全通路SaaS的直接情境待面試對位"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"足夠","evidence":["設計流程與畫面"],"missing":["部分商務模組及加分條件未呈現"],"issue_ids":["I01","I03","I04"]},{"id":"decision_depth","rating":"強","evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"足夠","evidence":["平均處理時間由 100.4 天降至 30.9 天"],"missing":["處理案件母體、支付占比與實驗限制待核對"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃。"],"missing":["資源與方向決策最終權責待確認"],"issue_ids":["I05"]},{"id":"readability","rating":"足夠","evidence":["工作涵蓋系統分析、流程與畫面設計、PRD、Prototype、UAT 與上線計畫"],"missing":[],"issue_ids":[]}],"results":[{"quote":"系統服務逾 6 萬家活躍付費廠商（2026 Q3）","kinds":["context"]},{"quote":"平均處理時間由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"團隊依結果決定採用低價","kinds":["decision","outcome"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"兩案均在開發中","kinds":["in_progress","decision"]},{"quote":"上線公司簡介生成、職缺工作說明生成及 AI 推薦人才","kinds":["output"]}],"hr_questions":[{"rule_id":"HR01","status":"partial","resume_evidence":["規劃使用流程、訂閱與付費機制"],"application_note":"支付交付可轉移，商務模組廣度待問"},{"rule_id":"HR02","status":"supported","resume_evidence":["人力銀行企業端招募系統專案負責人"],"application_note":"企業流程明確，零售客群不同"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我主責規劃"],"application_note":"本人規劃與工程交付邊界可見"},{"rule_id":"HR04","status":"partial","resume_evidence":["平均處理時間由 100.4 天降至 30.9 天"],"application_note":"有結果與期間，母體仍待核對"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。"],"application_note":"支持問題優先於新功能的取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從 SweetRing 的海外市場開始累積產品經驗"],"application_note":"消費產品到企業系統脈絡完整"},{"rule_id":"HR07","status":"supported","resume_evidence":["與 CodaPay 新加坡技術團隊協調串接"],"application_note":"實際跨境支付協作可確認"},{"rule_id":"HR08","status":"supported","resume_evidence":["資深產品經理｜Senior Product Manager"],"application_note":"角色與代表作容易定位"},{"rule_id":"HR09","status":"partial","resume_evidence":["網頁付款占營收由 24% 升至 80% 以上"],"application_note":"需核對占比母體與業務效益"},{"rule_id":"HR10","status":"supported","resume_evidence":["接下來，我希望把更多心力放回產品策略"],"application_note":"方向相容，零售動機可追問"},{"rule_id":"HR11","status":"unknown","resume_evidence":["台北市、新北市，可接受遠端或混合辦公"],"application_note":"JD未列完整條件，無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["規劃 Peach 付款由 App 內購轉向網頁"],"application_note":"足以約談，非招聘結果預測"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"partial","resume_evidence":["人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":"如何把企業流程與跨境支付經驗轉用全通路零售？"},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["廠商反映的溝通中斷問題，使我優先推進信件與即時通整合"],"evidence_type":"decision","source_ids":[],"interview_question":"哪些使用者資料改變原先優先序？"},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。"],"evidence_type":"decision","source_ids":[],"interview_question":"如何比較既有痛點與新功能的價值和成本？"},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["團隊依結果決定採用低價"],"evidence_type":"decision","source_ids":[],"interview_question":"定價結果如何連結毛利、續訂與後續策略？"},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["相對變化約多 28%"],"evidence_type":"outcome","source_ids":[],"interview_question":"實驗各期樣本、母體與同期干擾為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["定義使用情境與驗收標準"],"evidence_type":"output","source_ids":[],"interview_question":"AI案例中你與資料科學團隊如何分工？"},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["處理新舊系統並行的相容性需求"],"evidence_type":"output","source_ids":[],"interview_question":"資料轉換與分階段上線如何驗收與回復？"},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["從舊帳號信箱並非唯一值的限制出發"],"evidence_type":"decision","source_ids":[],"interview_question":"驗證流程有哪些替代方案與工程限制？"},{"rule_id":"HM09","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃"],"evidence_type":"context","source_ids":[],"interview_question":"需求衝突時誰有最終資源與方向決定權？"},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["並依客服回饋修正操作流程"],"evidence_type":"decision","source_ids":[],"interview_question":"回饋如何轉為規則修正並驗證有效？"},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["製作 Prototype"],"evidence_type":"output","source_ids":[],"interview_question":"可否展示支付或生成式功能的規格與驗收案例？"},{"rule_id":"HM13","primary_dimension":"method","status":"supported","resume_evidence":["規劃 Peach 付款由 App 內購轉向網頁"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"商務領域轉移需面試核對","context_limit":"非能力不符；JD未明示所有模組皆硬門檻","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"規劃使用流程、訂閱與付費機制","reason":"金流付費支持，但物流、訂單、優惠券與直接OMO情境未呈現。","suggestion":"補充實際商務模組與零售流程案例；若未做過，說明可轉移的規則設計。"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"結果可用，量測限制待核對","context_limit":"占比不等於總營收成長；口述非監測紀錄","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"網頁付款占營收由 24% 升至 80% 以上","reason":"付款占比支持渠道轉移，尚未呈現淨收入與成本；處理週期亦缺案件母體。","suggestion":"補支付總額、淨收入與費率；補處理週期案件數、起訖定義及積案影響。"},{"id":"I03","rule_id":"HR01","source_ids":[],"application_note":"加分未知不阻擋面試","context_limit":"不由主管匯報推定募資或由公司名推定人數","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"向總經理、副總等主管匯報","reason":"未呈現募資提案與200人以上開發團隊兩年以上經驗。","suggestion":"若有，補募資對象、提案作用及開發團隊口徑與任期。"},{"id":"I04","rule_id":"HM08","source_ids":[],"application_note":"Scrum已有參與線索","context_limit":"現行Kanban不否定過去Scrum經驗","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"曾參與每週一個 Sprint 的 Scrum","reason":"參與年期與在Scrum事件、Backlog中的實際責任尚未展開。","suggestion":"補一個Scrum迭代中需求排序、驗收與回顧的實際例子。"},{"id":"I05","rule_id":"HM09","source_ids":[],"application_note":"方向與資源權責仍需確認","context_limit":"人數與主管匯報本身不決定資深程度","category":"ownership","severity":"interview_follow_up","block_target":null,"claim":"公司決定採新舊並行","reason":"規劃交付責任清楚；公司架構決策不宜歸為本人方向決策。","suggestion":"補本人提出的方向選項、資源配置及最終決策權責。"}],"decision":{"recommendation":"interview","evidence":["規劃 Peach 付款由 App 內購轉向網頁","與 QA 制定 UAT 驗收案例","團隊依結果決定採用低價"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["「規劃 Peach 付款由 App 內購轉向網頁」支持支付與商業流程。","「與 QA 制定 UAT 驗收案例」支持完整週期與跨部門交付。","「團隊依結果決定採用低價」支持以實驗推動商業決策。"],"key_gaps":["零售OMO、物流訂單與優惠券廣度：追問最接近案例與轉移方式。","付款與處理週期成果：追問母體、淨效益與干擾因素。","方向與資源權責：追問自主選項、取捨與最終決策人。"],"strengths":["支付渠道與定價有商業決策案例。","企業系統規格、畫面、驗收及遷移交付具體。","使用者問題排序及生成式功能協作可面試驗證。"],"interview_questions":["請展開最接近訂單、會員、優惠券或OMO的案例與責任。","付款渠道轉移後淨收入、費率與付款轉換如何變化？","處理週期的案件數、定義與積案結構如何比較？","定價實驗各期樣本與季節干擾如何控制？","Scrum中你如何排序Backlog、驗收與回顧？","生成式功能如何驗收品質、風險與使用效益？","哪些資源或產品方向由你決定，哪些由主管決定？","是否有募資提案、大型開發團隊經歷或近期支付趨勢判斷？"],"editorial_appendix":[],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"多個交付、支付、定價與使用者優先序案例構成一致模式；取捨及對照衡量具體。零售直接經驗、量測母體與方向權責待核對，不支持9。"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"not_tested","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 單份審查｜履歷 appendix-A-v10.2｜第 10 輪｜model_id: unknown

#### 1. 結論

- 招聘決定：`interview`
- Level：8（±1）
- 一句話理由：「規劃 Peach 付款由 App 內購轉向網頁」支持面試，缺口依下表核對。

#### 2. 六維度

| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 現任 1111 招募系統 Product Owner | 零售全通路SaaS的直接情境待面試對位 |
| role_evidence | 足夠 | 設計流程與畫面 | 部分商務模組及加分條件未呈現 |
| decision_depth | 強 | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。 | 無新增缺口；以現有自述支持面試。 |
| outcome_quality | 足夠 | 平均處理時間由 100.4 天降至 30.9 天 | 處理案件母體、支付占比與實驗限制待核對 |
| ownership | 強 | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃。 | 資源與方向決策最終權責待確認 |
| readability | 足夠 | 工作涵蓋系統分析、流程與畫面設計、PRD、Prototype、UAT 與上線計畫 | 無新增缺口；以現有自述支持面試。 |

#### 3. JD 條件對照

| 條件 | 必要／加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 產品管理內文2年以上；經歷欄5年以上（兩者並列） | 必要 | supported | 近 10 年 PM 經驗 | 2016年至今的PM經歷支持兩項年資條件，資深程度另依案例判讀。 |
| 金流、物流、會員、促購優惠券、購買流程、訂單相關功能經驗 | 必要 | partial | 規劃使用流程、訂閱與付費機制 | 金流、付費購買流程與訂閱有案例；會員僅帳號權限可轉移；物流、優惠券及訂單未明示。JD未明示每項均為硬門檻，面試釐清廣度。 |
| 完整週期交付上市；新產品完整開發 | 必要 | supported | 主導 Juicy 推出 | 上市、PRD、UAT與上線計畫均有證據；新產品亦有KOOL與Juicy案例。 |
| 商業模式、關係人需求與規格；UX、RD、QA及設計合作 | 必要 | supported | 與 QA 制定 UAT 驗收案例 | 付費模式、10個需求單位、工程設計合作及規格交付可對位。 |
| 定義目標並衡量數據效益；維運優化指標效率 | 必要 | supported | 平均處理時間由 100.4 天降至 30.9 天 | 定價實驗及處理週期支持；營運效益的母體與歸因仍需追問。 |
| UI製作 | 必要 | supported | 設計流程與畫面 | 實際畫面、Prototype規劃與工具支持UI製作；可用作品確認細節。 |
| 參與運作Scrum | 必要 | supported | 曾參與每週一個 Sprint 的 Scrum | 符合參與經驗；現況為Kanban搭配瀑布，面試追問Scrum職責。 |
| 支付生態趨勢 | 加分 | partial | 整理抽成、稅、手續費與撥款週期 | 支持支付方案商業理解；未提供近期生態趨勢洞察。 |
| 募資提案簡報 | 加分 | unknown |  | 未呈現募資提案；主管匯報不等同募資。 |
| 200人以上軟體開發團隊工作2年以上 | 加分 | unknown |  | 履歷未呈現開發團隊人數，不能以公司規模推定。 |
| GenAI產品案例 | 加分 | supported | 上線公司簡介生成、職缺工作說明生成及 AI 推薦人才 | 生成式功能已上線，定義情境與驗收責任有述；不把AI工具使用等同產品成果。 |
| 全通路新零售SaaS商業方向及Commerce Cloud、G11N、OMO情境 | 必要 | partial | 讓印尼、泰國等市場的用戶可用電信帳單與超商付款 | 企業流程、跨市場支付可轉移；未直接呈現零售OMO與商家營運案例。 |

#### 4. HR 十二問／HM 十三問

| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | partial | 規劃使用流程、訂閱與付費機制 | 支付交付可轉移，商務模組廣度待問 |
| HR02 | supported | 人力銀行企業端招募系統專案負責人 | 企業流程明確，零售客群不同 |
| HR03 | supported | 由我主責規劃 | 本人規劃與工程交付邊界可見 |
| HR04 | partial | 平均處理時間由 100.4 天降至 30.9 天 | 有結果與期間，母體仍待核對 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。 | 支持問題優先於新功能的取捨 |
| HR06 | supported | 從 SweetRing 的海外市場開始累積產品經驗 | 消費產品到企業系統脈絡完整 |
| HR07 | supported | 與 CodaPay 新加坡技術團隊協調串接 | 實際跨境支付協作可確認 |
| HR08 | supported | 資深產品經理｜Senior Product Manager | 角色與代表作容易定位 |
| HR09 | partial | 網頁付款占營收由 24% 升至 80% 以上 | 需核對占比母體與業務效益 |
| HR10 | supported | 接下來，我希望把更多心力放回產品策略 | 方向相容，零售動機可追問 |
| HR11 | unknown | 台北市、新北市，可接受遠端或混合辦公 | JD未列完整條件，無已知衝突 |
| HR12 | supported | 規劃 Peach 付款由 App 內購轉向網頁 | 足以約談，非招聘結果預測 |
| HM01 | partial | 人力銀行企業端招募系統專案負責人 | 企業SaaS可轉移，零售情境待核對 |
| HM02 | supported | 廠商反映的溝通中斷問題，使我優先推進信件與即時通整合 | 使用者問題影響優先序 |
| HM03 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。 | 進行中取捨可判，不當作成果 |
| HM04 | supported | 團隊依結果決定採用低價 | 商業實驗支持，無需額外要求P&L |
| HM05 | partial | 相對變化約多 28% | 母體與干擾留面試核對 |
| HM06 | supported | 定義使用情境與驗收標準 | 分工可見，不把工程實作歸本人 |
| HM07 | supported | 處理新舊系統並行的相容性需求 | 遷移與驗收風險有具體經驗 |
| HM08 | supported | 從舊帳號信箱並非唯一值的限制出發 | 系統限制與規則可支援技術協作 |
| HM09 | supported | 職稱為主任，帶領 2 名直屬產品企劃 | 交付與協調強，方向權責待問 |
| HM10 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 角色與重點可辨識 |
| HM11 | supported | 並依客服回饋修正操作流程 | 客服回饋有修正動作 |
| HM12 | supported | 製作 Prototype | 作品與規格值得面試驗證 |
| HM13 | supported | 規劃 Peach 付款由 App 內購轉向網頁 | 依凍結規準獨立判讀，非真人效度 |

#### 5. 約談理由（≤3）與關鍵缺口（≤3）

| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「規劃 Peach 付款由 App 內購轉向網頁」支持支付與商業流程。 |
| 2 | 「與 QA 制定 UAT 驗收案例」支持完整週期與跨部門交付。 |
| 3 | 「團隊依結果決定採用低價」支持以實驗推動商業決策。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 零售OMO、物流訂單與優惠券廣度：追問最接近案例與轉移方式。 | 請展開最接近訂單、會員、優惠券或OMO的案例與責任。 |
| 2 | 付款與處理週期成果：追問母體、淨效益與干擾因素。 | 付款渠道轉移後淨收入、費率與付款轉換如何變化？ |
| 3 | 方向與資源權責：追問自主選項、取捨與最終決策人。 | 處理週期的案件數、定義與積案結構如何比較？ |

#### 6. 評語（給寫稿者的具體回饋）

**做得好（3 點）**

- 尚凡／Peach｜「規劃 Peach 付款由 App 內購轉向網頁」｜支持支付購買流程與跨境串接。
- 1111／交付｜「與 QA 制定 UAT 驗收案例」｜支持SaaS規格、品質與上市協作。
- 尚凡／定價｜「團隊依結果決定採用低價」｜支持商業衡量與方向選擇。

**可改進（≤5 點）**

- 位置：Product Manager｜尚凡國際創新科技
  - 原句：「規劃使用流程、訂閱與付費機制」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：金流付費支持，但物流、訂單、優惠券與直接OMO情境未呈現。 商務領域轉移需面試核對
  - 建議方向：補充實際商務模組與零售流程案例；若未做過，說明可轉移的規則設計。

- 位置：專業摘要
  - 原句：「網頁付款占營收由 24% 升至 80% 以上」
  - 問題類型：`measurement`
  - 嚴重度：`interview_follow_up`
  - 影響：付款占比支持渠道轉移，尚未呈現淨收入與成本；處理週期亦缺案件母體。 結果可用，量測限制待核對
  - 建議方向：補支付總額、淨收入與費率；補處理週期案件數、起訖定義及積案影響。

- 位置：Product Owner／PM｜1111 全球華人
  - 原句：「向總經理、副總等主管匯報」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：未呈現募資提案與200人以上開發團隊兩年以上經驗。 加分未知不阻擋面試
  - 建議方向：若有，補募資對象、提案作用及開發團隊口徑與任期。

- 位置：專業技能
  - 原句：「曾參與每週一個 Sprint 的 Scrum」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：參與年期與在Scrum事件、Backlog中的實際責任尚未展開。 Scrum已有參與線索
  - 建議方向：補一個Scrum迭代中需求排序、驗收與回顧的實際例子。

- 位置：自傳
  - 原句：「公司決定採新舊並行」
  - 問題類型：`ownership`
  - 嚴重度：`interview_follow_up`
  - 影響：規劃交付責任清楚；公司架構決策不宜歸為本人方向決策。 方向與資源權責仍需確認
  - 建議方向：補本人提出的方向選項、資源配置及最終決策權責。

**編輯附件**：無。

#### 7. 資深能力分布

delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

#### 8. 未測試聲明

PDF 抽字：本內容審查 `not_tested`（另見總報告 §6 的 `local_extraction`）／ATS 匯入：`not_tested`／AI 作者判讀：不可由文字判定／真人校準：`not_run`。

### A.11｜jd36｜原始單行 JSON

```json
{"rubric_version":"4.2","resume_id":"appendix-A-v10.2","job_id":"jd36","job_input":"summary","model_id":"unknown","run_id":"jd36-A-01","human_calibrated":false,"requirements":[{"id":"R01","text":"PM經驗：內文3年以上；經歷欄2年以上，兩者均保留","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"履歷時序支持超過3年，亦超過欄位2年；不以年資直接決定Level。"},{"id":"R02","text":"Axure、Jira、Confluence","type":"required","status":"partial","evidence":["Figma、Axure RP、Notion、Trello"],"blocks_interview":false,"reason":"Axure有列示；Jira與Confluence未呈現，不能由其他看板工具推定熟悉，面試核對實際使用及轉移成本。"},{"id":"R03","text":"技術可行性與架構關聯；熟悉API規格","type":"required","status":"partial","evidence":["處理新舊系統並行的相容性需求","API 串接規劃、舊系統資料盤點與新舊流程銜接"],"blocks_interview":false,"reason":"新舊欄位、帳號驗證與資料關聯支持技術可行性討論；有金流串接實例，但API契約、欄位、錯誤處理及驗收細節未呈現，需作品核對。"},{"id":"R04","text":"團隊協作、溝通與同理","type":"required","status":"supported","evidence":["與 QA 制定 UAT 驗收案例","並依客服回饋修正操作流程"],"blocks_interview":false,"reason":"跨工程客服QA協作並依回饋修正流程，能支持協作與理解使用情境；不從形容詞推人格。"},{"id":"R05","text":"內部作業優化、銀行／平台串接、需求規劃開發上線持續迭代","type":"required","status":"partial","evidence":["與 CodaPay 新加坡技術團隊協調串接","重新制定業務流程、對照資料欄位並重構規格"],"blocks_interview":false,"reason":"流程優化、平台串接和迭代有案例；銀行端直接串接未知，銀行結算差異需面試追問。"},{"id":"R06","text":"資料架構、Wireframe、Flow chart、UX規格，涵蓋前端Hybrid與後台","type":"required","status":"partial","evidence":["整理帳號權限、職缺關聯與既有資料轉換規則","Wireframe、Prototype、PRD"],"blocks_interview":false,"reason":"資料關聯、流程畫面及文件有證據；Hybrid及後台操作規格未有具體樣本，不從App經驗直接推定。"},{"id":"R07","text":"合作與法遵；內外溝通","type":"required","status":"partial","evidence":["工程、設計、QA、資料科學、客服、業務、法務與稽核協作","與 CodaPay 新加坡技術團隊協調串接"],"blocks_interview":false,"reason":"內外合作明確；法務稽核僅技能列示，支付法遵如何轉成規格與稽核軌跡未知。"},{"id":"R08","text":"時程規劃、測試驗收與上線","type":"required","status":"supported","evidence":["與 QA 制定 UAT 驗收案例、排定上線計畫"],"blocks_interview":false,"reason":"有分階段交付日期與UAT、上線規劃，足以支持交付面試。"},{"id":"R09","text":"內訓、線上問題處理與依反饋迭代","type":"required","status":"supported","evidence":["透過互動原型與 FAQ 向客服、業務說明功能","於 2026/04 完成登入驗證調整"],"blocks_interview":false,"reason":"有內部功能說明、帳號事件應對及客服回饋修正；正式內訓形式與事故分級可面試補足。"},{"id":"R10","text":"代理收付、電子支付或行動支付經驗","type":"preferred","status":"partial","evidence":["導入 CodaPay","讓印尼、泰國等市場的用戶可用電信帳單與超商付款"],"blocks_interview":false,"reason":"具有第三方金流導入、渠道與費用試算；未證明台灣代理收付或電子支付核心帳務領域經驗。"},{"id":"R11","text":"資管資工背景或相關工作","type":"preferred","status":"supported","evidence":["私立淡江大學｜國際企業學系","系統分析、流程與畫面設計、PRD、Prototype"],"blocks_interview":false,"reason":"本科非資管資工，但條件含相關工作，系統分析與串接規劃經歷可支持，不以學校名氣加分。"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["現任 1111 招募系統 Product Owner"],"missing":["近期為企業招募系統，與支付內部作業可轉移；銀行與支付法遵差異見I02。"],"issue_ids":["I02"]},{"id":"role_evidence","rating":"足夠","evidence":["與 CodaPay 新加坡技術團隊協調串接","與 QA 制定 UAT 驗收案例、排定上線計畫"],"missing":["工具、API規格及金融領域細節需核對，見I01至I03。"],"issue_ids":["I01","I02","I03"]},{"id":"decision_depth","rating":"強","evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前","從舊帳號信箱並非唯一值的限制出發"],"missing":["已見問題優先級與系統限制推導；支付串接取捨可用作品深化。"],"issue_ids":[]},{"id":"outcome_quality","rating":"足夠","evidence":["平均處理時間由 100.4 天降至 30.9 天","網頁付款占營收由 24% 升至 80% 以上"],"missing":["處理時間母體與觀測口徑、付款占比與淨收入關係需核對。"],"issue_ids":["I04","I05"]},{"id":"ownership","rating":"強","evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃","公司決定採新舊並行"],"missing":["規劃、工程、QA與公司決策已有邊界；可追問外部供應商責任分配。"],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["設計流程與畫面、撰寫 PRD 與製作 Prototype"],"missing":["可快速定位代表交付與本人作用；可將API與法遵案例提前以利本職判讀。"],"issue_ids":[]}],"results":[{"quote":"系統服務逾 6 萬家活躍付費廠商（2026 Q3）","kinds":["context"]},{"quote":"於 2025/09 完成上線","kinds":["output"]},{"quote":"平均處理時間由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"團隊依結果決定採用低價","kinds":["decision"]},{"quote":"兩案均在開發中","kinds":["in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["與 CodaPay 新加坡技術團隊協調串接"],"application_note":"串接與系統交付相關，可約談"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 Product Owner"],"application_note":"近期企業流程可轉移，金融差異待核"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我主責規劃"],"application_note":"本人規劃與工程交付邊界可辨"},{"rule_id":"HR04","status":"partial","resume_evidence":["平均處理時間由 100.4 天降至 30.9 天"],"application_note":"有觀測改變，母體口徑待核"},{"rule_id":"HR05","status":"supported","resume_evidence":["從舊帳號信箱並非唯一值的限制出發"],"application_note":"有系統限制下判斷線索"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App、網紅媒合平台，到企業招募系統"],"application_note":"領域及責任演變清楚"},{"rule_id":"HR07","status":"supported","resume_evidence":["與 QA 制定 UAT 驗收案例"],"application_note":"有實際協作情境"},{"rule_id":"HR08","status":"supported","resume_evidence":["設計流程與畫面、撰寫 PRD 與製作 Prototype"],"application_note":"工作動作和交付清楚"},{"rule_id":"HR09","status":"partial","resume_evidence":["調整後至 2026/10 未再出現同類冒用"],"application_note":"自述觀測需核對監測來源"},{"rule_id":"HR10","status":"partial","resume_evidence":["希望把更多心力放回產品策略"],"application_note":"可問內部系統工作與方向相容性"},{"rule_id":"HR11","status":"unknown","resume_evidence":["台北市、新北市，可接受遠端或混合辦公"],"application_note":"JD未列地點等條件，無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["API 串接規劃、舊系統資料盤點與新舊流程銜接"],"application_note":"支持約談並核對API與金融深度"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["現任 1111 招募系統 Product Owner"],"evidence_type":"context","source_ids":[],"interview_question":"如何把企業流程經驗轉到支付內部作業？"},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["廠商反映的溝通中斷問題"],"evidence_type":"decision","source_ids":[],"interview_question":"哪類工單證據改變了優先級？"},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":"當時比較哪些價值、資源與風險？"},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["整理抽成、稅、手續費與撥款週期"],"evidence_type":"decision","source_ids":[],"interview_question":"結算成本如何影響付款方案及產品選擇？"},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["平均處理時間由 100.4 天降至 30.9 天"],"evidence_type":"outcome","source_ids":[],"interview_question":"案件母體、結案定義與積案清理效應為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["公司決定採新舊並行"],"evidence_type":"context","source_ids":[],"interview_question":"你與工程、QA及供應商分別決定什麼？"},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["與 QA 制定 UAT 驗收案例、排定上線計畫"],"evidence_type":"output","source_ids":[],"interview_question":"如何設定放行標準、回滾與例外處理？"},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"partial","resume_evidence":["與 CodaPay 新加坡技術團隊協調串接"],"evidence_type":"output","source_ids":[],"interview_question":"請展示API欄位、驗證、錯誤及驗收案例。"},{"rule_id":"HM09","primary_dimension":"ownership","status":"supported","resume_evidence":["重新制定業務流程、對照資料欄位並重構規格"],"evidence_type":"output","source_ids":[],"interview_question":"複雜規格如何拆解，哪些由你自主定案？"},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["設計流程與畫面、撰寫 PRD 與製作 Prototype"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["並依客服測試回饋調整推薦規則"],"evidence_type":"decision","source_ids":[],"interview_question":"哪項反饋推翻原先假設，後續如何驗證？"},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["整理帳號權限、職缺關聯與既有資料轉換規則"],"evidence_type":"output","source_ids":[],"interview_question":"請以去識別化規格核對API與法遵深度。"},{"rule_id":"HM13","primary_dimension":"method","status":"supported","resume_evidence":["API 串接規劃、舊系統資料盤點與新舊流程銜接"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR07","source_ids":[],"application_note":"指定工具經驗","context_limit":"工具未知不代表能力不符","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"Figma、Axure RP、Notion、Trello","reason":"Jira、Confluence未列示；Axure列示不等於全部指定工具均熟悉。","suggestion":"補工具實際用法、場景與可轉移操作；面試核對即可。"},{"id":"I02","rule_id":"HM01","source_ids":[],"application_note":"金融與產品環境差異","context_limit":"未呈現不等於缺乏能力","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"與 CodaPay 新加坡技術團隊協調串接","reason":"金流渠道串接不等同銀行串接或支付法遵落地；Hybrid與後台規格亦無具體樣本。","suggestion":"追問銀行／平台分工、對帳結算、法遵需求及Hybrid後台規格案例。"},{"id":"I03","rule_id":"HM08","source_ids":[],"application_note":"API深度核對","context_limit":"有線索而非完全未知","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"API 串接規劃、舊系統資料盤點與新舊流程銜接","reason":"有串接規劃實例，但未展示閱讀API規格與技術可行性驗收細節。","suggestion":"以去識別化規格說明欄位映射、驗證、錯誤處理及驗收。"},{"id":"I04","rule_id":"HM05","source_ids":[],"application_note":"處理週期口徑","context_limit":"不直接歸因於單一個人","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"平均處理時間由 100.4 天降至 30.9 天","reason":"已有2026 Q1至Q2期間，但案件數、計算口徑、積案及案件組成影響未述。","suggestion":"補各期案件數、起訖點、未結案處理及變化限制。"},{"id":"I05","rule_id":"HR09","source_ids":[],"application_note":"結果邊界","context_limit":"不把占比或未通報當因果證明","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"網頁付款占營收由 24% 升至 80% 以上","reason":"付款渠道占比有期間，不能推定總營收或淨實收成長；安全事件亦僅口述觀察。","suggestion":"核對營收母體與渠道總額；安全觀測補資料來源及通報範圍。"}],"decision":{"recommendation":"interview","evidence":["與 CodaPay 新加坡技術團隊協調串接","與 QA 制定 UAT 驗收案例、排定上線計畫","從舊帳號信箱並非唯一值的限制出發"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["「與 CodaPay 新加坡技術團隊協調串接」支持外部平台協作的轉移性。","「與 QA 制定 UAT 驗收案例、排定上線計畫」直接對應交付驗收。","「從舊帳號信箱並非唯一值的限制出發」支持依系統限制規劃流程。"],"key_gaps":["Jira與Confluence使用未知；追問實際文件、需求追蹤與協作工作流。","API規格及銀行支付法遵深度待補；追問欄位、錯誤、對帳與法遵驗收。","成效母體與歸因限制待補；追問處理時間案件組成及付款占比的總額。"],"strengths":["流程、欄位及權限重構可對應內部作業需求。","跨外部金流團隊協作與渠道成本試算有具體情境。","規劃、QA驗收、上線及客服說明涵蓋完整交付鏈。"],"interview_questions":["請展示一次串接規格，說明欄位映射、驗證、錯誤與驗收分工。","曾否做銀行串接、對帳結算或支付法遵？你負責哪些決策？","Jira、Confluence各用於什麼工作？若未用過如何轉移現行流程？","請展示Hybrid或後台操作流程、資料關聯與例外規格。","哪項工單或用戶證據使你把搜尋痛點排在職缺健檢之前？","處理時間兩期的案件數、結案定義、積案與組成差異為何？","付款渠道占比的營收母體及淨實收如何變化？","你希望投入產品策略，如何看待此職內部系統維運與法遵工作的比例？"],"editorial_appendix":[],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"多案例呈現系統限制、優先級與定價取捨，交付及責任邊界清楚，足以支持8；支付API與銀行法遵深度及量測口徑未可追溯，不支持9。進行中整合僅支持決策，不列實現成果。"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"not_tested","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"passed","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 單份審查｜履歷 appendix-A-v10.2｜第 11 輪｜model_id: unknown

#### 1. 結論

- 招聘決定：`interview`
- Level：8（±1）
- 一句話理由：「與 CodaPay 新加坡技術團隊協調串接」支持面試，缺口依下表核對。

#### 2. 六維度

| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 現任 1111 招募系統 Product Owner | 近期為企業招募系統，與支付內部作業可轉移；銀行與支付法遵差異見I02。 |
| role_evidence | 足夠 | 與 CodaPay 新加坡技術團隊協調串接；與 QA 制定 UAT 驗收案例、排定上線計畫 | 工具、API規格及金融領域細節需核對，見I01至I03。 |
| decision_depth | 強 | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前；從舊帳號信箱並非唯一值的限制出發 | 已見問題優先級與系統限制推導；支付串接取捨可用作品深化。 |
| outcome_quality | 足夠 | 平均處理時間由 100.4 天降至 30.9 天；網頁付款占營收由 24% 升至 80% 以上 | 處理時間母體與觀測口徑、付款占比與淨收入關係需核對。 |
| ownership | 強 | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃；公司決定採新舊並行 | 規劃、工程、QA與公司決策已有邊界；可追問外部供應商責任分配。 |
| readability | 強 | 設計流程與畫面、撰寫 PRD 與製作 Prototype | 可快速定位代表交付與本人作用；可將API與法遵案例提前以利本職判讀。 |

#### 3. JD 條件對照

| 條件 | 必要／加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| PM經驗：內文3年以上；經歷欄2年以上，兩者均保留 | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 履歷時序支持超過3年，亦超過欄位2年；不以年資直接決定Level。 |
| Axure、Jira、Confluence | 必要 | partial | Figma、Axure RP、Notion、Trello | Axure有列示；Jira與Confluence未呈現，不能由其他看板工具推定熟悉，面試核對實際使用及轉移成本。 |
| 技術可行性與架構關聯；熟悉API規格 | 必要 | partial | 處理新舊系統並行的相容性需求；API 串接規劃、舊系統資料盤點與新舊流程銜接 | 新舊欄位、帳號驗證與資料關聯支持技術可行性討論；有金流串接實例，但API契約、欄位、錯誤處理及驗收細節未呈現，需作品核對。 |
| 團隊協作、溝通與同理 | 必要 | supported | 與 QA 制定 UAT 驗收案例；並依客服回饋修正操作流程 | 跨工程客服QA協作並依回饋修正流程，能支持協作與理解使用情境；不從形容詞推人格。 |
| 內部作業優化、銀行／平台串接、需求規劃開發上線持續迭代 | 必要 | partial | 與 CodaPay 新加坡技術團隊協調串接；重新制定業務流程、對照資料欄位並重構規格 | 流程優化、平台串接和迭代有案例；銀行端直接串接未知，銀行結算差異需面試追問。 |
| 資料架構、Wireframe、Flow chart、UX規格，涵蓋前端Hybrid與後台 | 必要 | partial | 整理帳號權限、職缺關聯與既有資料轉換規則；Wireframe、Prototype、PRD | 資料關聯、流程畫面及文件有證據；Hybrid及後台操作規格未有具體樣本，不從App經驗直接推定。 |
| 合作與法遵；內外溝通 | 必要 | partial | 工程、設計、QA、資料科學、客服、業務、法務與稽核協作；與 CodaPay 新加坡技術團隊協調串接 | 內外合作明確；法務稽核僅技能列示，支付法遵如何轉成規格與稽核軌跡未知。 |
| 時程規劃、測試驗收與上線 | 必要 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 有分階段交付日期與UAT、上線規劃，足以支持交付面試。 |
| 內訓、線上問題處理與依反饋迭代 | 必要 | supported | 透過互動原型與 FAQ 向客服、業務說明功能；於 2026/04 完成登入驗證調整 | 有內部功能說明、帳號事件應對及客服回饋修正；正式內訓形式與事故分級可面試補足。 |
| 代理收付、電子支付或行動支付經驗 | 加分 | partial | 導入 CodaPay；讓印尼、泰國等市場的用戶可用電信帳單與超商付款 | 具有第三方金流導入、渠道與費用試算；未證明台灣代理收付或電子支付核心帳務領域經驗。 |
| 資管資工背景或相關工作 | 加分 | supported | 私立淡江大學｜國際企業學系；系統分析、流程與畫面設計、PRD、Prototype | 本科非資管資工，但條件含相關工作，系統分析與串接規劃經歷可支持，不以學校名氣加分。 |

#### 4. HR 十二問／HM 十三問

| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 與 CodaPay 新加坡技術團隊協調串接 | 串接與系統交付相關，可約談 |
| HR02 | supported | 現任 1111 招募系統 Product Owner | 近期企業流程可轉移，金融差異待核 |
| HR03 | supported | 由我主責規劃 | 本人規劃與工程交付邊界可辨 |
| HR04 | partial | 平均處理時間由 100.4 天降至 30.9 天 | 有觀測改變，母體口徑待核 |
| HR05 | supported | 從舊帳號信箱並非唯一值的限制出發 | 有系統限制下判斷線索 |
| HR06 | supported | 從交友與訂閱制 App、網紅媒合平台，到企業招募系統 | 領域及責任演變清楚 |
| HR07 | supported | 與 QA 制定 UAT 驗收案例 | 有實際協作情境 |
| HR08 | supported | 設計流程與畫面、撰寫 PRD 與製作 Prototype | 工作動作和交付清楚 |
| HR09 | partial | 調整後至 2026/10 未再出現同類冒用 | 自述觀測需核對監測來源 |
| HR10 | partial | 希望把更多心力放回產品策略 | 可問內部系統工作與方向相容性 |
| HR11 | unknown | 台北市、新北市，可接受遠端或混合辦公 | JD未列地點等條件，無已知衝突 |
| HR12 | supported | API 串接規劃、舊系統資料盤點與新舊流程銜接 | 支持約談並核對API與金融深度 |
| HM01 | supported | 現任 1111 招募系統 Product Owner | 企業系統可轉移，支付情境需核 |
| HM02 | supported | 廠商反映的溝通中斷問題 | 用戶痛點能影響優先級 |
| HM03 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 有具體排序，資源比較可追問 |
| HM04 | supported | 整理抽成、稅、手續費與撥款週期 | 金流成本連結產品選擇，不要求P&L |
| HM05 | partial | 平均處理時間由 100.4 天降至 30.9 天 | 觀測結果有數字，母體待核 |
| HM06 | supported | 公司決定採新舊並行 | 公司、本人與工程邊界可辨 |
| HM07 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 交付及驗收支持直接約談 |
| HM08 | partial | 與 CodaPay 新加坡技術團隊協調串接 | API規格深度需樣本核對 |
| HM09 | supported | 重新制定業務流程、對照資料欄位並重構規格 | 自主重構多流程，支持資深交付 |
| HM10 | supported | 設計流程與畫面、撰寫 PRD 與製作 Prototype | 代表作與本人作用易辨 |
| HM11 | supported | 並依客服測試回饋調整推薦規則 | 客服回饋導致規則修正 |
| HM12 | supported | 整理帳號權限、職缺關聯與既有資料轉換規則 | 以規格作品補足金融與API細節 |
| HM13 | supported | API 串接規劃、舊系統資料盤點與新舊流程銜接 | 只依凍結JD與原文，不代表真人效度 |

#### 5. 約談理由（≤3）與關鍵缺口（≤3）

| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「與 CodaPay 新加坡技術團隊協調串接」支持外部平台協作的轉移性。 |
| 2 | 「與 QA 制定 UAT 驗收案例、排定上線計畫」直接對應交付驗收。 |
| 3 | 「從舊帳號信箱並非唯一值的限制出發」支持依系統限制規劃流程。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | Jira與Confluence使用未知；追問實際文件、需求追蹤與協作工作流。 | 請展示一次串接規格，說明欄位映射、驗證、錯誤與驗收分工。 |
| 2 | API規格及銀行支付法遵深度待補；追問欄位、錯誤、對帳與法遵驗收。 | 曾否做銀行串接、對帳結算或支付法遵？你負責哪些決策？ |
| 3 | 成效母體與歸因限制待補；追問處理時間案件組成及付款占比的總額。 | Jira、Confluence各用於什麼工作？若未用過如何轉移現行流程？ |

#### 6. 評語（給寫稿者的具體回饋）

**做得好（3 點）**

- 1111改版｜「重新制定業務流程、對照資料欄位並重構規格」｜支持內部系統流程與資料關聯規劃。
- Peach付款｜「與 CodaPay 新加坡技術團隊協調串接」｜支持外部平台溝通與串接協作。
- 1111功能交付｜「與 QA 制定 UAT 驗收案例、排定上線計畫」｜對應時程、驗收與上線責任。

**可改進（≤5 點）**

- 位置：專業技能
  - 原句：「Figma、Axure RP、Notion、Trello」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：Jira、Confluence未列示；Axure列示不等於全部指定工具均熟悉。 指定工具經驗
  - 建議方向：補工具實際用法、場景與可轉移操作；面試核對即可。

- 位置：Product Manager｜尚凡國際創新科技
  - 原句：「與 CodaPay 新加坡技術團隊協調串接」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：金流渠道串接不等同銀行串接或支付法遵落地；Hybrid與後台規格亦無具體樣本。 金融與產品環境差異
  - 建議方向：追問銀行／平台分工、對帳結算、法遵需求及Hybrid後台規格案例。

- 位置：專業技能
  - 原句：「API 串接規劃、舊系統資料盤點與新舊流程銜接」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：有串接規劃實例，但未展示閱讀API規格與技術可行性驗收細節。 API深度核對
  - 建議方向：以去識別化規格說明欄位映射、驗證、錯誤處理及驗收。

- 位置：Product Owner／PM｜1111 全球華人
  - 原句：「平均處理時間由 100.4 天降至 30.9 天」
  - 問題類型：`measurement`
  - 嚴重度：`interview_follow_up`
  - 影響：已有2026 Q1至Q2期間，但案件數、計算口徑、積案及案件組成影響未述。 處理週期口徑
  - 建議方向：補各期案件數、起訖點、未結案處理及變化限制。

- 位置：專業摘要
  - 原句：「網頁付款占營收由 24% 升至 80% 以上」
  - 問題類型：`measurement`
  - 嚴重度：`interview_follow_up`
  - 影響：付款渠道占比有期間，不能推定總營收或淨實收成長；安全事件亦僅口述觀察。 結果邊界
  - 建議方向：核對營收母體與渠道總額；安全觀測補資料來源及通報範圍。

**編輯附件**：無。

#### 7. 資深能力分布

delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

#### 8. 未測試聲明

PDF 抽字：本內容審查 `not_tested`（另見總報告 §6 的 `local_extraction`）／ATS 匯入：`not_tested`／AI 作者判讀：不可由文字判定／真人校準：`not_run`。

### A.12｜jd40｜原始單行 JSON

```json
{"rubric_version":"4.2","resume_id":"appendix-A-v10.2","job_id":"jd40","job_input":"summary","model_id":"unknown","run_id":"jd40-A-01","human_calibrated":false,"requirements":[{"id":"R01","text":"5年以上軟體／技術產品或技術專案經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗","工作涵蓋系統分析、流程與畫面設計、PRD"],"blocks_interview":false,"reason":"2016年至今的軟體產品經歷及具體系統交付支持年資與相關性。"},{"id":"R02","text":"完整需求到上線；需求流程、驗收、PRD、User Story","type":"required","status":"supported","evidence":["再與 QA 制定 UAT 驗收案例、排定上線計畫","設計流程與畫面、撰寫 PRD 與製作 Prototype"],"blocks_interview":false,"reason":"需求釐清至規格、驗收和上線有完整案例；User Story另於技能列明，可面試看作品。"},{"id":"R03","text":"理解API、資料流程、系統架構與第三方串接","type":"required","status":"partial","evidence":["並與 CodaPay 新加坡技術團隊協調串接","整理帳號權限、職缺關聯與既有資料轉換規則"],"blocks_interview":false,"reason":"第三方金流串接與資料轉換支持基本整合理解；API契約、錯誤處理及架構取捨深度待核對。"},{"id":"R04","text":"需求拆解排序、跨隊協作、風險管理","type":"required","status":"supported","evidence":["依使用者旅程與工單問題安排優先級","我協調工程與客服，釐清受影響範圍"],"blocks_interview":false,"reason":"優先順序、跨隊交付及帳號冒用風險處置均有案例。"},{"id":"R05","text":"市場／用戶／營運／商務／客戶探索與roadmap；策略、生命週期、競品、UX","type":"required","status":"partial","evidence":["從案主與網紅兩種角色釐清需求","參考 Airbnb 與交友平台的媒合方式"],"blocks_interview":false,"reason":"雙邊探索、競品借鑑、UX及roadmap排序可見；餐飲市場探索與客戶商務共同訂roadmap未呈現。"},{"id":"R06","text":"範圍、計畫、里程碑、時程、客戶期待及變更；成本品質風險","type":"required","status":"partial","evidence":["採新舊並行、分階段上線","整理抽成、稅、手續費與撥款週期"],"blocks_interview":false,"reason":"分階段交付、成本試算及品質風險有證據；客戶變更協商、範圍基準和里程碑控制細節待補。"},{"id":"R07","text":"測試策略、驗收、上線問題與使用／營運指標迭代","type":"required","status":"supported","evidence":["並依客服測試回饋調整推薦規則","2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"blocks_interview":false,"reason":"驗收案例、封測、上線後回饋與處理週期追蹤支持；完整測試分層可面試釐清。"},{"id":"R08","text":"KA客製與NRE","type":"preferred","status":"partial","evidence":["針對大型客戶依部門或分店分工的需求"],"blocks_interview":false,"reason":"大型客戶需求轉產品可轉移；未提供客製合約、NRE估價及驗收經驗。"},{"id":"R09","text":"支付、餐飲、零售或SaaS整合","type":"preferred","status":"partial","evidence":["規劃 Peach 付款由 App 內購轉向網頁","導入 CodaPay"],"blocks_interview":false,"reason":"支付整合直接相關；餐飲零售與SaaS對外整合未呈現，不視為不符。"},{"id":"R10","text":"基本SQL或資料分析","type":"preferred","status":"supported","evidence":["與 DBA 協作取數，再以 Google Sheets、Excel 分析"],"blocks_interview":false,"reason":"資料分析分支已支持；SQL實作未呈現，但條件為或。"},{"id":"R11","text":"提案協商及高階關係人","type":"preferred","status":"partial","evidence":["向總經理、副總等主管匯報","據此提出 7／30／90 天訂閱方案與加贈內容"],"blocks_interview":false,"reason":"高階匯報與方案提案有證據，對外商務協商及衝突處理權責待核對。"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["現任 1111 招募系統 Product Owner","曾規劃雙邊媒合與付費機制"],"missing":["餐飲營運場景需轉移學習"],"issue_ids":[]},{"id":"role_evidence","rating":"足夠","evidence":["並與 CodaPay 新加坡技術團隊協調串接","再與 QA 制定 UAT 驗收案例、排定上線計畫"],"missing":["API細節、KA/NRE商務交付治理"],"issue_ids":["I01","I02"]},{"id":"decision_depth","rating":"強","evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前","團隊依結果決定採用低價"],"missing":["工程資源與客戶時程衝突的取捨細節"],"issue_ids":["I02"]},{"id":"outcome_quality","rating":"足夠","evidence":["網頁付款占營收由 24% 升至 80% 以上","各期 21 天"],"missing":["處理週期分母及案件組成、支付總額及因果限制"],"issue_ids":["I03","I04"]},{"id":"ownership","rating":"強","evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃","定義使用情境與驗收標準"],"missing":["對外客戶承諾與NRE責任範圍見I02"],"issue_ids":["I02"]},{"id":"readability","rating":"足夠","evidence":["資深產品經理｜Senior Product Manager","工作涵蓋系統分析、流程與畫面設計、PRD"],"missing":["本職相關整合與客戶交付證據分散，可集中呈現"],"issue_ids":[]}],"results":[{"quote":"系統服務逾 6 萬家活躍付費廠商（2026 Q3）","kinds":["context"]},{"quote":"約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃","kinds":["output"]},{"quote":"兩案均在開發中","kinds":["decision","in_progress"]},{"quote":"團隊依結果決定採用低價","kinds":["decision"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天","kinds":["outcome"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["並與 CodaPay 新加坡技術團隊協調串接"],"application_note":"支付整合與交付可轉移，值得約談"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 Product Owner"],"application_note":"企業流程產品相關，餐飲場景需適應"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我主責規劃"],"application_note":"規劃責任清楚，工程分工可追問"},{"rule_id":"HR04","status":"partial","resume_evidence":["網頁付款占營收由 24% 升至 80% 以上"],"application_note":"有渠道結果，總營收及歸因待核對"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"application_note":"排序有依據，可討論資源取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從 SweetRing 的海外市場開始累積產品經驗"],"application_note":"從海外支付進展到企業系統主責"},{"rule_id":"HR07","status":"supported","resume_evidence":["與 DBA 協作取數，再以 Google Sheets、Excel 分析"],"application_note":"分析與跨隊有情境，SQL未知不阻擋"},{"rule_id":"HR08","status":"supported","resume_evidence":["設計流程與畫面、撰寫 PRD 與製作 Prototype"],"application_note":"交付脈絡易讀，可集中技術整合"},{"rule_id":"HR09","status":"partial","resume_evidence":["依目前掌握的情況"],"application_note":"觀察性結果應核對監測來源"},{"rule_id":"HR10","status":"supported","resume_evidence":["承擔更完整的問題定義、方向選擇與成效責任"],"application_note":"方向相容，兼技術專案比重可談"},{"rule_id":"HR11","status":"unknown","resume_evidence":["台北市、新北市，可接受遠端或混合辦公"],"application_note":"JD未載地點語言條件，無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["再與 QA 制定 UAT 驗收案例、排定上線計畫"],"application_note":"核心交付可支持邀約，缺口面試釐清"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":"如何轉用企業流程與支付經驗到餐飲KA場景？"},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["廠商反映的溝通中斷問題，使我優先推進信件與即時通整合"],"evidence_type":"decision","source_ids":[],"interview_question":"哪類工單或用戶證據改變了原先規劃？"},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":"工程資源有限時如何估價值與排期，誰有最終決定權？"},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["團隊依結果決定採用低價"],"evidence_type":"decision","source_ids":[],"interview_question":"定價實驗的付費母體與同期干擾因素如何影響選擇？"},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["網頁付款占營收由 24% 升至 80% 以上"],"evidence_type":"outcome","source_ids":[],"interview_question":"付款轉移的總營收、淨收入及同期變化為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["與工程、設計、行銷及海外金流團隊協作完成上線"],"evidence_type":"output","source_ids":[],"interview_question":"金流整合中你與工程、供應商的責任界線及分歧是什麼？"},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"partial","resume_evidence":["採新舊並行、分階段上線"],"evidence_type":"output","source_ids":[],"interview_question":"如何管理範圍變更、里程碑、回滾與客戶期待？"},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"partial","resume_evidence":["並與 CodaPay 新加坡技術團隊協調串接"],"evidence_type":"output","source_ids":[],"interview_question":"請用API契約、付款狀態與失敗補償說明一次整合方案。"},{"rule_id":"HM09","primary_dimension":"ownership","status":"supported","resume_evidence":["重新制定業務流程、對照資料欄位並重構規格"],"evidence_type":"output","source_ids":[],"interview_question":"重啟專案中哪些方向與資源由你決定，哪些需主管核准？"},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["工作涵蓋系統分析、流程與畫面設計、PRD"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["並依客服回饋修正操作流程"],"evidence_type":"decision","source_ids":[],"interview_question":"哪項客服回饋推翻原設計，修正後如何驗證？"},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["再與 QA 制定 UAT 驗收案例、排定上線計畫"],"evidence_type":"output","source_ids":[],"interview_question":"可否展示去識別化PRD、資料流程與UAT案例？"},{"rule_id":"HM13","primary_dimension":"method","status":"supported","resume_evidence":["兩案均在開發中"],"evidence_type":"in_progress","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HM08","source_ids":[],"application_note":"API深度於面試核對","context_limit":"有金流串接案例，非完全未知","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"並與 CodaPay 新加坡技術團隊協調串接","reason":"未說明契約、狀態流、異常處理與本人技術判斷，TPM深度仍需確認。","suggestion":"補一個API資料流程、限制、替代方案和驗收事實。"},{"id":"I02","rule_id":"HM07","source_ids":[],"application_note":"KA/NRE治理待面試","context_limit":"KA客製NRE是加分，非硬性門檻","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"針對大型客戶依部門或分店分工的需求","reason":"需求產品化可見，未說明NRE報價、範圍變更、客戶承諾與里程碑協商。","suggestion":"補客戶驗收、變更及成本時程責任；若無NRE經驗如實交代。"},{"id":"I03","rule_id":"HM05","source_ids":[],"application_note":"處理週期分母待核對","context_limit":"流程結果不直接代表產品使用成效","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天","reason":"已有期間與基準，但無案件數、組成、計時口徑及清積案影響。","suggestion":"補案件母體、起訖定義及不同案型分布。"},{"id":"I04","rule_id":"HM05","source_ids":[],"application_note":"渠道占比非淨收入增幅","context_limit":"有期間及占比，但非對照實驗","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"網頁付款占營收由 24% 升至 80% 以上","reason":"可支持支付渠道轉移，不能直接推定總營收、節費或淨收入增加。","suggestion":"如有資料補同期總額、費率及轉換差異；否則保留占比結論。"}],"decision":{"recommendation":"interview","evidence":["再與 QA 制定 UAT 驗收案例、排定上線計畫","並與 CodaPay 新加坡技術團隊協調串接","搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["「再與 QA 制定 UAT 驗收案例、排定上線計畫」支持完整產品交付。","「並與 CodaPay 新加坡技術團隊協調串接」提供支付第三方整合基礎。","「團隊依結果決定採用低價」與排序案例支持商業與產品判斷。"],"key_gaps":["API契約、異常與資料一致性：請展開本人整合判斷。","KA/NRE交付治理：請說明報價、變更及客戶里程碑協商。","結果量測口徑：請補處理週期分母及支付總額限制。"],"strengths":["規格、驗收與上線責任連貫，適合PM／TPM混合職責。","支付整合與實收成本試算能轉移至支付產品。","企業權限資料規則與跨隊排序兼具，取捨有具體依據。"],"interview_questions":["請用API契約、付款狀態與失敗補償說明一次整合方案。","KA客戶要求變更時，如何估NRE、談驗收及調整里程碑？","新舊系統並行的資料轉換、相容性、回滾如何驗收？","搜尋優先於職缺健檢的價值、資源及風險如何評估？","案件週期的分母、起訖與積案組成如何定義？","付款占比轉移是否伴隨總營收、淨收入或轉換率改變？","定價實驗各期母體及外部干擾如何處理？","請展示去識別化PRD、資料流程和UAT案例並界定本人貢獻。"],"editorial_appendix":[],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"多案例支持完整交付、支付整合、資料規則及明確排序；定價有對照與期間，結果限制可辨。API深度、KA/NRE治理和量測追溯待驗，未達高度對應本職的9。"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"not_tested","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 單份審查｜履歷 appendix-A-v10.2｜第 12 輪｜model_id: unknown

#### 1. 結論

- 招聘決定：`interview`
- Level：8（±1）
- 一句話理由：「再與 QA 制定 UAT 驗收案例、排定上線計畫」支持面試，缺口依下表核對。

#### 2. 六維度

| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 現任 1111 招募系統 Product Owner；曾規劃雙邊媒合與付費機制 | 餐飲營運場景需轉移學習 |
| role_evidence | 足夠 | 並與 CodaPay 新加坡技術團隊協調串接；再與 QA 制定 UAT 驗收案例、排定上線計畫 | API細節、KA/NRE商務交付治理 |
| decision_depth | 強 | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前；團隊依結果決定採用低價 | 工程資源與客戶時程衝突的取捨細節 |
| outcome_quality | 足夠 | 網頁付款占營收由 24% 升至 80% 以上；各期 21 天 | 處理週期分母及案件組成、支付總額及因果限制 |
| ownership | 強 | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃；定義使用情境與驗收標準 | 對外客戶承諾與NRE責任範圍見I02 |
| readability | 足夠 | 資深產品經理｜Senior Product Manager；工作涵蓋系統分析、流程與畫面設計、PRD | 本職相關整合與客戶交付證據分散，可集中呈現 |

#### 3. JD 條件對照

| 條件 | 必要／加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 5年以上軟體／技術產品或技術專案經驗 | 必要 | supported | 近 10 年 PM 經驗；工作涵蓋系統分析、流程與畫面設計、PRD | 2016年至今的軟體產品經歷及具體系統交付支持年資與相關性。 |
| 完整需求到上線；需求流程、驗收、PRD、User Story | 必要 | supported | 再與 QA 制定 UAT 驗收案例、排定上線計畫；設計流程與畫面、撰寫 PRD 與製作 Prototype | 需求釐清至規格、驗收和上線有完整案例；User Story另於技能列明，可面試看作品。 |
| 理解API、資料流程、系統架構與第三方串接 | 必要 | partial | 並與 CodaPay 新加坡技術團隊協調串接；整理帳號權限、職缺關聯與既有資料轉換規則 | 第三方金流串接與資料轉換支持基本整合理解；API契約、錯誤處理及架構取捨深度待核對。 |
| 需求拆解排序、跨隊協作、風險管理 | 必要 | supported | 依使用者旅程與工單問題安排優先級；我協調工程與客服，釐清受影響範圍 | 優先順序、跨隊交付及帳號冒用風險處置均有案例。 |
| 市場／用戶／營運／商務／客戶探索與roadmap；策略、生命週期、競品、UX | 必要 | partial | 從案主與網紅兩種角色釐清需求；參考 Airbnb 與交友平台的媒合方式 | 雙邊探索、競品借鑑、UX及roadmap排序可見；餐飲市場探索與客戶商務共同訂roadmap未呈現。 |
| 範圍、計畫、里程碑、時程、客戶期待及變更；成本品質風險 | 必要 | partial | 採新舊並行、分階段上線；整理抽成、稅、手續費與撥款週期 | 分階段交付、成本試算及品質風險有證據；客戶變更協商、範圍基準和里程碑控制細節待補。 |
| 測試策略、驗收、上線問題與使用／營運指標迭代 | 必要 | supported | 並依客服測試回饋調整推薦規則；2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 驗收案例、封測、上線後回饋與處理週期追蹤支持；完整測試分層可面試釐清。 |
| KA客製與NRE | 加分 | partial | 針對大型客戶依部門或分店分工的需求 | 大型客戶需求轉產品可轉移；未提供客製合約、NRE估價及驗收經驗。 |
| 支付、餐飲、零售或SaaS整合 | 加分 | partial | 規劃 Peach 付款由 App 內購轉向網頁；導入 CodaPay | 支付整合直接相關；餐飲零售與SaaS對外整合未呈現，不視為不符。 |
| 基本SQL或資料分析 | 加分 | supported | 與 DBA 協作取數，再以 Google Sheets、Excel 分析 | 資料分析分支已支持；SQL實作未呈現，但條件為或。 |
| 提案協商及高階關係人 | 加分 | partial | 向總經理、副總等主管匯報；據此提出 7／30／90 天訂閱方案與加贈內容 | 高階匯報與方案提案有證據，對外商務協商及衝突處理權責待核對。 |

#### 4. HR 十二問／HM 十三問

| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 支付整合與交付可轉移，值得約談 |
| HR02 | supported | 現任 1111 招募系統 Product Owner | 企業流程產品相關，餐飲場景需適應 |
| HR03 | supported | 由我主責規劃 | 規劃責任清楚，工程分工可追問 |
| HR04 | partial | 網頁付款占營收由 24% 升至 80% 以上 | 有渠道結果，總營收及歸因待核對 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 排序有依據，可討論資源取捨 |
| HR06 | supported | 從 SweetRing 的海外市場開始累積產品經驗 | 從海外支付進展到企業系統主責 |
| HR07 | supported | 與 DBA 協作取數，再以 Google Sheets、Excel 分析 | 分析與跨隊有情境，SQL未知不阻擋 |
| HR08 | supported | 設計流程與畫面、撰寫 PRD 與製作 Prototype | 交付脈絡易讀，可集中技術整合 |
| HR09 | partial | 依目前掌握的情況 | 觀察性結果應核對監測來源 |
| HR10 | supported | 承擔更完整的問題定義、方向選擇與成效責任 | 方向相容，兼技術專案比重可談 |
| HR11 | unknown | 台北市、新北市，可接受遠端或混合辦公 | JD未載地點語言條件，無已知衝突 |
| HR12 | supported | 再與 QA 制定 UAT 驗收案例、排定上線計畫 | 核心交付可支持邀約，缺口面試釐清 |
| HM01 | supported | 人力銀行企業端招募系統專案負責人 | 企業系統與支付可轉移，餐飲可學 |
| HM02 | supported | 廠商反映的溝通中斷問題，使我優先推進信件與即時通整合 | 用戶問題能改變優先級 |
| HM03 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 取捨有依據，資源權責待核 |
| HM04 | supported | 團隊依結果決定採用低價 | 定價與成本支持商業判斷 |
| HM05 | partial | 網頁付款占營收由 24% 升至 80% 以上 | 占比與週期口徑待核對 |
| HM06 | supported | 與工程、設計、行銷及海外金流團隊協作完成上線 | 協作有分工，非本人寫程式 |
| HM07 | partial | 採新舊並行、分階段上線 | 交付成立，客戶變更治理待核 |
| HM08 | partial | 並與 CodaPay 新加坡技術團隊協調串接 | 有串接經驗，API深度待核 |
| HM09 | supported | 重新制定業務流程、對照資料欄位並重構規格 | 自主規劃與交付支持資深 |
| HM10 | supported | 工作涵蓋系統分析、流程與畫面設計、PRD | 角色清楚，相關案例可集中 |
| HM11 | supported | 並依客服回饋修正操作流程 | 回饋促修正，可追問驗證 |
| HM12 | supported | 再與 QA 制定 UAT 驗收案例、排定上線計畫 | 值得約談並看去識別化作品 |
| HM13 | supported | 兩案均在開發中 | 進行中不當成果，方法不加分 |

#### 5. 約談理由（≤3）與關鍵缺口（≤3）

| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「再與 QA 制定 UAT 驗收案例、排定上線計畫」支持完整產品交付。 |
| 2 | 「並與 CodaPay 新加坡技術團隊協調串接」提供支付第三方整合基礎。 |
| 3 | 「團隊依結果決定採用低價」與排序案例支持商業與產品判斷。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | API契約、異常與資料一致性：請展開本人整合判斷。 | 請用API契約、付款狀態與失敗補償說明一次整合方案。 |
| 2 | KA/NRE交付治理：請說明報價、變更及客戶里程碑協商。 | KA客戶要求變更時，如何估NRE、談驗收及調整里程碑？ |
| 3 | 結果量測口徑：請補處理週期分母及支付總額限制。 | 新舊系統並行的資料轉換、相容性、回滾如何驗收？ |

#### 6. 評語（給寫稿者的具體回饋）

**做得好（3 點）**

- 專業摘要｜「現任 1111 招募系統 Product Owner」｜規格、驗收與上線責任連貫，適合PM／TPM混合職責。
- Product Manager｜尚凡國際創新科技｜「並與 CodaPay 新加坡技術團隊協調串接」｜支付整合與實收成本試算能轉移至支付產品。
- Product Owner／PM｜1111 全球華人｜「搜尋結果頁的既有痛點，也排在新功能職缺健檢之前」｜企業權限資料規則與跨隊排序兼具，取捨有具體依據。

**可改進（≤5 點）**

- 位置：Product Manager｜尚凡國際創新科技
  - 原句：「並與 CodaPay 新加坡技術團隊協調串接」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：未說明契約、狀態流、異常處理與本人技術判斷，TPM深度仍需確認。 API深度於面試核對
  - 建議方向：補一個API資料流程、限制、替代方案和驗收事實。

- 位置：Product Owner／PM｜1111 全球華人
  - 原句：「針對大型客戶依部門或分店分工的需求」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：需求產品化可見，未說明NRE報價、範圍變更、客戶承諾與里程碑協商。 KA/NRE治理待面試
  - 建議方向：補客戶驗收、變更及成本時程責任；若無NRE經驗如實交代。

- 位置：Product Owner／PM｜1111 全球華人
  - 原句：「2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天」
  - 問題類型：`measurement`
  - 嚴重度：`interview_follow_up`
  - 影響：已有期間與基準，但無案件數、組成、計時口徑及清積案影響。 處理週期分母待核對
  - 建議方向：補案件母體、起訖定義及不同案型分布。

- 位置：專業摘要
  - 原句：「網頁付款占營收由 24% 升至 80% 以上」
  - 問題類型：`measurement`
  - 嚴重度：`interview_follow_up`
  - 影響：可支持支付渠道轉移，不能直接推定總營收、節費或淨收入增加。 渠道占比非淨收入增幅
  - 建議方向：如有資料補同期總額、費率及轉換差異；否則保留占比結論。

**編輯附件**：無。

#### 7. 資深能力分布

delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

#### 8. 未測試聲明

PDF 抽字：本內容審查 `not_tested`（另見總報告 §6 的 `local_extraction`）／ATS 匯入：`not_tested`／AI 作者判讀：不可由文字判定／真人校準：`not_run`。

### A.13｜jd43｜原始單行 JSON

```json
{"rubric_version":"4.2","resume_id":"appendix-A-v10.2","job_id":"jd43","job_input":"summary","model_id":"unknown","run_id":"jd43-A-01","human_calibrated":false,"requirements":[{"id":"R01","text":"5年以上網路科技產品相關經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"工作時序與網路App、平台及招募系統案例支持相關經驗；年資本身不判資深程度。"},{"id":"R02","text":"策略及台灣本地需求、期待與PRD；與總部roadmap優先級及里程碑對齊","type":"required","status":"partial","evidence":["從使用者旅程釐清需求、協調優先級"],"blocks_interview":false,"reason":"本地需求、PRD與階段交付有案例；總部roadmap協商、台灣市場策略權責未具體呈現。"},{"id":"R03","text":"用研、競品、問卷訪談、bucket/A/B研究","type":"required","status":"partial","evidence":["使用者訪談與問卷、競品實測"],"blocks_interview":false,"reason":"訪談問卷競品主要為技能線索；定價對照實驗有案例，但分桶、隨機化與質性研究如何改變產品選擇待核對。"},{"id":"R04","text":"跨產品設計、工程、資安、法務及客服，概念到上線","type":"required","status":"partial","evidence":["工程、設計、QA、資料科學、客服、業務、法務與稽核協作"],"blocks_interview":false,"reason":"工程客服及設計合作有上線案例；法務僅清單，資安專業團隊協作未呈現。"},{"id":"R05","text":"概念到上線、全週期評估與持續優化","type":"required","status":"supported","evidence":["與 QA 制定 UAT 驗收案例、排定上線計畫"],"blocks_interview":false,"reason":"從雙邊平台規劃到上線及現有服務迭代有證據；上線後量測深度另見I01。"},{"id":"R06","text":"KPI、A/B及行為資料分析","type":"required","status":"partial","evidence":["以售價不變的 Android 作對照"],"blocks_interview":false,"reason":"營收與DAU指標及對照實驗具體；嚴格A/B設計、Messenger安全與訊息體驗KPI需驗證。"},{"id":"R07","text":"跨職能、跨國協作","type":"required","status":"supported","evidence":["與 CodaPay 新加坡技術團隊協調串接"],"blocks_interview":false,"reason":"跨職能有工程QA客服案例；跨國有新加坡金流及海外在地化案例。"},{"id":"R08","text":"分析解題、溝通與關係人管理","type":"required","status":"supported","evidence":["整理帳號權限、職缺關聯與既有資料轉換規則"],"blocks_interview":false,"reason":"群組與資料相容性顯示分析解題；優先級協調及對客服業務說明支持關係人溝通。"},{"id":"R09","text":"Confluence、Jira、Figma、Codex等工具","type":"required","status":"partial","evidence":["Figma、Axure RP、Notion、Trello"],"blocks_interview":false,"reason":"Figma明列；Confluence、Jira、Codex未呈現。Claude Code可轉移，不能等同已用Codex。"},{"id":"R10","text":"英文流利","type":"required","status":"supported","evidence":["並以英文進行跨國協作"],"blocks_interview":false,"reason":"英文跨國工作及測驗支持面試；實際總部會議、寫作與協商可用英文核對。"},{"id":"R11","text":"AI產品或整合經驗","type":"preferred","status":"supported","evidence":["上線公司簡介生成、職缺工作說明生成及 AI 推薦人才"],"blocks_interview":false,"reason":"有AI產品使用情境、驗收與規則調整，亦有Agent協作。"},{"id":"R12","text":"日語或韓語","type":"preferred","status":"unknown","evidence":["中文母語；英文 TOEIC 980、TOEFL iBT 93"],"blocks_interview":false,"reason":"未列日韓語能力；海外市場經驗不能代替語言證據。"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["涵蓋訂閱制社交 App、網紅媒合平台與人力銀行招募系統。"],"missing":["總部協作的區域產品策略權責與近期消費型訊息情境待核對。"],"issue_ids":["I03"]},{"id":"role_evidence","rating":"足夠","evidence":["我協調工程與客服，釐清受影響範圍"],"missing":["資安法務深度、正式用研及工具經驗待面試補充。"],"issue_ids":["I04","I05"]},{"id":"decision_depth","rating":"強","evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。"],"missing":["可補總部與本地需求衝突時的決策依據。"],"issue_ids":["I03"]},{"id":"outcome_quality","rating":"足夠","evidence":["平均處理時間由 100.4 天降至 30.9 天。"],"missing":["處理週期母體、冒用事件監測與實驗可比性需核對。"],"issue_ids":["I01","I02"]},{"id":"ownership","rating":"強","evidence":["由我主責規劃。"],"missing":["策略核准與工程資安責任邊界可在案例面談釐清。"],"issue_ids":["I03","I04"]},{"id":"readability","rating":"足夠","evidence":["資深產品經理｜Senior Product Manager"],"missing":[],"issue_ids":[]}],"results":[{"quote":"系統服務逾 6 萬家活躍付費廠商（2026 Q3）","kinds":["context"]},{"quote":"於 2026/04 完成登入驗證調整","kinds":["output"]},{"quote":"調整後至 2026/10 未再出現同類冒用。","kinds":["outcome"]},{"quote":"兩案均在開發中","kinds":["in_progress"]},{"quote":"團隊依結果決定採用低價。","kinds":["decision"]},{"quote":"平均處理時間由 100.4 天降至 30.9 天。","kinds":["outcome"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["並依客服測試回饋調整推薦規則。"],"application_note":"安全、訊息與AI案例可轉移。"},{"rule_id":"HR02","status":"supported","resume_evidence":["人力銀行企業端招募系統專案負責人"],"application_note":"近期企業端與消費訊息情境有差異。"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我主責規劃。"],"application_note":"規劃、驗收與工程分工明確。"},{"rule_id":"HR04","status":"partial","resume_evidence":["平均處理時間由 100.4 天降至 30.9 天。"],"application_note":"週期下降可追問母體與定義。"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。"],"application_note":"優先級選擇有問題依據。"},{"rule_id":"HR06","status":"supported","resume_evidence":["從 SweetRing 的海外市場開始累積產品經驗"],"application_note":"時序呈現海外到企業系統責任。"},{"rule_id":"HR07","status":"supported","resume_evidence":["與 CodaPay 新加坡技術團隊協調串接。"],"application_note":"跨國整合具體；工具有待核對。"},{"rule_id":"HR08","status":"supported","resume_evidence":["工作涵蓋系統分析、流程與畫面設計、PRD"],"application_note":"摘要與案例可辨識工作重點。"},{"rule_id":"HR09","status":"partial","resume_evidence":["調整後至 2026/10 未再出現同類冒用。"],"application_note":"口述觀察需核對監測來源。"},{"rule_id":"HR10","status":"supported","resume_evidence":["接下來，我希望把更多心力放回產品策略"],"application_note":"方向相容，動機可接職缺追問。"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公"],"application_note":"已知地點方向相容，無明文衝突。"},{"rule_id":"HR12","status":"supported","resume_evidence":["定義使用情境與驗收標準"],"application_note":"支持約談，驗證總部及安全深度。"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"partial","resume_evidence":["涵蓋訂閱制社交 App、網紅媒合平台與人力銀行招募系統。"],"evidence_type":"context","source_ids":[],"interview_question":"請說明消費App及企業帳號經驗如何轉用Messenger與OA的台灣市場策略。"},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["廠商反映的溝通中斷問題，使我優先推進信件與即時通整合"],"evidence_type":"decision","source_ids":[],"interview_question":"你如何取得並分類使用者研究資料，哪些反證改變了訊息整合方案？"},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。"],"evidence_type":"decision","source_ids":[],"interview_question":"請重建搜尋改善與職缺健檢的比較依據、資源限制及決策權。"},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["團隊依結果決定採用低價。"],"evidence_type":"decision","source_ids":[],"interview_question":"定價實驗如何影響商業策略，如何處理平台差異與外在變化？"},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["平均處理時間由 100.4 天降至 30.9 天。"],"evidence_type":"outcome","source_ids":[],"interview_question":"案件母體、起訖、未結案及清案後組成變化如何處理？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["再與 QA 制定 UAT 驗收案例、排定上線計畫"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["處理新舊系統並行的相容性需求。"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["從舊帳號信箱並非唯一值的限制出發"],"evidence_type":"decision","source_ids":[],"interview_question":"請以登入驗證說明資安、法務、工程分工及驗收和回滾條件。"},{"rule_id":"HM09","primary_dimension":"ownership","status":"supported","resume_evidence":["重新制定業務流程、對照資料欄位並重構規格"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["工作涵蓋系統分析、流程與畫面設計、PRD"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["並依客服回饋修正操作流程。"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["定義使用情境與驗收標準"],"evidence_type":"output","source_ids":[],"interview_question":"可否展示去識別PRD、研究結論與上線評估，並說明本人決策範圍？"},{"rule_id":"HM13","primary_dimension":"method","status":"supported","resume_evidence":["兩案均在開發中"],"evidence_type":"in_progress","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HM05","source_ids":[],"application_note":"可於面試核對，不構成直接否定。","context_limit":"定價實驗亦需核對對照可比性；此為主要量測缺口。","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"平均處理時間由 100.4 天降至 30.9 天。","reason":"有期間與結果，但案件分母、統計定義及組成變化未交代；不能直接歸因流程改善。","suggestion":"補案件數、起訖及未結案處理，說明清案與案件組成的影響。"},{"id":"I02","rule_id":"HR09","source_ids":[],"application_note":"可於面試核對，不構成直接否定。","context_limit":"不能據此認定零事件或防詐能力不足。","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"調整後至 2026/10 未再出現同類冒用。","reason":"已限定目前掌握情況，但客服回報或觀察不等於完整安全監測。","suggestion":"說明事件定義、資料來源、觀察窗、偵測與漏報限制。"},{"id":"I03","rule_id":"HM01","source_ids":[],"application_note":"可於面試核對，不構成直接否定。","context_limit":"跨國金流合作支持可轉移性，但不等同總部產品策略。","category":"ownership","severity":"interview_follow_up","block_target":null,"claim":"從使用者旅程釐清需求、協調優先級","reason":"有需求協調與交付，尚未呈現區域PM與總部roadmap談判及策略核准邊界。","suggestion":"補本地需求與跨國總部衝突、選項、本人權責與里程碑協商案例。"},{"id":"I04","rule_id":"HM08","source_ids":[],"application_note":"可於面試核對，不構成直接否定。","context_limit":"不要求本人實作資安；未知不判不符。","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"我協調工程與客服，釐清受影響範圍","reason":"帳號安全案例直接相關，但資安專業、法務的實際參與與驗收責任不清楚。","suggestion":"補威脅情境、風險取捨及資安法務工程分工。"},{"id":"I05","rule_id":"HR07","source_ids":[],"application_note":"可於面試核對，不構成直接否定。","context_limit":"對照定價案例有支持，非完全未知。","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"使用者訪談與問卷、競品實測","reason":"方法清單尚不足顯示研究抽樣、洞察及bucket/A/B如何影響選擇。","suggestion":"補一個研究問題、抽樣與分組、洞察到決策及量測限制案例。"}],"decision":{"recommendation":"interview","evidence":["我協調工程與客服，釐清受影響範圍","以售價不變的 Android 作對照","與 CodaPay 新加坡技術團隊協調串接。"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["「我協調工程與客服，釐清受影響範圍」對應帳號安全與跨職能。","「以售價不變的 Android 作對照」提供實驗決策面談材料。","「與 CodaPay 新加坡技術團隊協調串接。」支持跨國協作。"],"key_gaps":["總部roadmap與台灣策略權責：追問需求衝突、資源與里程碑協商。","量測與安全觀察限制：追問案件母體、對照可比性及冒用監測來源。","研究及資安法務深度：追問抽樣分組、洞察與跨專業驗收。"],"strengths":["帳號驗證與訊息整合可轉移至安全及訊息體驗。","取捨、定價實驗與AI驗收有具體行動。","規格、相容性、UAT與階段上線責任明確。"],"interview_questions":["請重建台灣需求與總部roadmap衝突的一次決策，說明本人權責及資源里程碑協商。","登入驗證調整如何定義威脅、評估使用摩擦，與資安法務工程如何分工？","未再發生同類冒用的資料來源、偵測覆蓋與漏報限制是什麼？","處理週期的案件數、起訖定義、未結案與清案後組成如何處理？","定價各期與平台如何確保可比，還有哪些變因及替代解釋？","提供訪談問卷到決策案例，說明抽樣、洞察、分桶及A/B設計。","用英文說明跨國整合中的需求分歧、書面PRD及協商結果。","請展示去識別PRD與上線評估，並核對Jira、Confluence、Codex及AI整合使用深度。"],"editorial_appendix":[],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"多案例支持相關交付、跨國協作與安全訊息轉移；有優先級取捨、對照實驗及限制語句。總部策略權責及量測可追溯性仍待核對，不以進行中訊息整合當成已實現成果。"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"not_tested","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"passed","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 單份審查｜履歷 appendix-A-v10.2｜第 13 輪｜model_id: unknown

#### 1. 結論

- 招聘決定：`interview`
- Level：8（±1）
- 一句話理由：「我協調工程與客服，釐清受影響範圍」支持面試，缺口依下表核對。

#### 2. 六維度

| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 涵蓋訂閱制社交 App、網紅媒合平台與人力銀行招募系統。 | 總部協作的區域產品策略權責與近期消費型訊息情境待核對。 |
| role_evidence | 足夠 | 我協調工程與客服，釐清受影響範圍 | 資安法務深度、正式用研及工具經驗待面試補充。 |
| decision_depth | 強 | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。 | 可補總部與本地需求衝突時的決策依據。 |
| outcome_quality | 足夠 | 平均處理時間由 100.4 天降至 30.9 天。 | 處理週期母體、冒用事件監測與實驗可比性需核對。 |
| ownership | 強 | 由我主責規劃。 | 策略核准與工程資安責任邊界可在案例面談釐清。 |
| readability | 足夠 | 資深產品經理｜Senior Product Manager | 無新增缺口；以現有自述支持面試。 |

#### 3. JD 條件對照

| 條件 | 必要／加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 5年以上網路科技產品相關經驗 | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 工作時序與網路App、平台及招募系統案例支持相關經驗；年資本身不判資深程度。 |
| 策略及台灣本地需求、期待與PRD；與總部roadmap優先級及里程碑對齊 | 必要 | partial | 從使用者旅程釐清需求、協調優先級 | 本地需求、PRD與階段交付有案例；總部roadmap協商、台灣市場策略權責未具體呈現。 |
| 用研、競品、問卷訪談、bucket/A/B研究 | 必要 | partial | 使用者訪談與問卷、競品實測 | 訪談問卷競品主要為技能線索；定價對照實驗有案例，但分桶、隨機化與質性研究如何改變產品選擇待核對。 |
| 跨產品設計、工程、資安、法務及客服，概念到上線 | 必要 | partial | 工程、設計、QA、資料科學、客服、業務、法務與稽核協作 | 工程客服及設計合作有上線案例；法務僅清單，資安專業團隊協作未呈現。 |
| 概念到上線、全週期評估與持續優化 | 必要 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 從雙邊平台規劃到上線及現有服務迭代有證據；上線後量測深度另見I01。 |
| KPI、A/B及行為資料分析 | 必要 | partial | 以售價不變的 Android 作對照 | 營收與DAU指標及對照實驗具體；嚴格A/B設計、Messenger安全與訊息體驗KPI需驗證。 |
| 跨職能、跨國協作 | 必要 | supported | 與 CodaPay 新加坡技術團隊協調串接 | 跨職能有工程QA客服案例；跨國有新加坡金流及海外在地化案例。 |
| 分析解題、溝通與關係人管理 | 必要 | supported | 整理帳號權限、職缺關聯與既有資料轉換規則 | 群組與資料相容性顯示分析解題；優先級協調及對客服業務說明支持關係人溝通。 |
| Confluence、Jira、Figma、Codex等工具 | 必要 | partial | Figma、Axure RP、Notion、Trello | Figma明列；Confluence、Jira、Codex未呈現。Claude Code可轉移，不能等同已用Codex。 |
| 英文流利 | 必要 | supported | 並以英文進行跨國協作 | 英文跨國工作及測驗支持面試；實際總部會議、寫作與協商可用英文核對。 |
| AI產品或整合經驗 | 加分 | supported | 上線公司簡介生成、職缺工作說明生成及 AI 推薦人才 | 有AI產品使用情境、驗收與規則調整，亦有Agent協作。 |
| 日語或韓語 | 加分 | unknown | 中文母語；英文 TOEIC 980、TOEFL iBT 93 | 未列日韓語能力；海外市場經驗不能代替語言證據。 |

#### 4. HR 十二問／HM 十三問

| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 並依客服測試回饋調整推薦規則。 | 安全、訊息與AI案例可轉移。 |
| HR02 | supported | 人力銀行企業端招募系統專案負責人 | 近期企業端與消費訊息情境有差異。 |
| HR03 | supported | 由我主責規劃。 | 規劃、驗收與工程分工明確。 |
| HR04 | partial | 平均處理時間由 100.4 天降至 30.9 天。 | 週期下降可追問母體與定義。 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。 | 優先級選擇有問題依據。 |
| HR06 | supported | 從 SweetRing 的海外市場開始累積產品經驗 | 時序呈現海外到企業系統責任。 |
| HR07 | supported | 與 CodaPay 新加坡技術團隊協調串接。 | 跨國整合具體；工具有待核對。 |
| HR08 | supported | 工作涵蓋系統分析、流程與畫面設計、PRD | 摘要與案例可辨識工作重點。 |
| HR09 | partial | 調整後至 2026/10 未再出現同類冒用。 | 口述觀察需核對監測來源。 |
| HR10 | supported | 接下來，我希望把更多心力放回產品策略 | 方向相容，動機可接職缺追問。 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公 | 已知地點方向相容，無明文衝突。 |
| HR12 | supported | 定義使用情境與驗收標準 | 支持約談，驗證總部及安全深度。 |
| HM01 | partial | 涵蓋訂閱制社交 App、網紅媒合平台與人力銀行招募系統。 | 消費與企業經驗可轉移，區域策略待核對。 |
| HM02 | supported | 廠商反映的溝通中斷問題，使我優先推進信件與即時通整合 | 有使用問題到優先級的鏈結。 |
| HM03 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。 | 具取捨依據，可面談權責與資源。 |
| HM04 | supported | 團隊依結果決定採用低價。 | 商業實驗相關，無須另要求P&L。 |
| HM05 | partial | 平均處理時間由 100.4 天降至 30.9 天。 | 有結果，分母與可比性待補。 |
| HM06 | supported | 再與 QA 制定 UAT 驗收案例、排定上線計畫 | 規劃驗收及協作邊界有證據。 |
| HM07 | supported | 處理新舊系統並行的相容性需求。 | 具新舊並行交付經驗。 |
| HM08 | supported | 從舊帳號信箱並非唯一值的限制出發 | 規則限制具體，資安法務深度待補。 |
| HM09 | supported | 重新制定業務流程、對照資料欄位並重構規格 | 複雜度與自主規劃支持資深面談。 |
| HM10 | supported | 工作涵蓋系統分析、流程與畫面設計、PRD | 重點可辨識，無頁數淘汰。 |
| HM11 | supported | 並依客服回饋修正操作流程。 | 有依回饋修正流程。 |
| HM12 | supported | 定義使用情境與驗收標準 | 值得以作品與案例核對能力。 |
| HM13 | supported | 兩案均在開發中 | 進行中獨立分類，非已實現成果。 |

#### 5. 約談理由（≤3）與關鍵缺口（≤3）

| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「我協調工程與客服，釐清受影響範圍」對應帳號安全與跨職能。 |
| 2 | 「以售價不變的 Android 作對照」提供實驗決策面談材料。 |
| 3 | 「與 CodaPay 新加坡技術團隊協調串接。」支持跨國協作。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 總部roadmap與台灣策略權責：追問需求衝突、資源與里程碑協商。 | 請重建台灣需求與總部roadmap衝突的一次決策，說明本人權責及資源里程碑協商。 |
| 2 | 量測與安全觀察限制：追問案件母體、對照可比性及冒用監測來源。 | 登入驗證調整如何定義威脅、評估使用摩擦，與資安法務工程如何分工？ |
| 3 | 研究及資安法務深度：追問抽樣分組、洞察與跨專業驗收。 | 未再發生同類冒用的資料來源、偵測覆蓋與漏報限制是什麼？ |

#### 6. 評語（給寫稿者的具體回饋）

**做得好（3 點）**

- 專業摘要｜「涵蓋訂閱制社交 App、網紅媒合平台與人力銀行招募系統。」｜帳號驗證與訊息整合可轉移至安全及訊息體驗。
- Product Owner／PM｜1111 全球華人｜「我協調工程與客服，釐清受影響範圍」｜取捨、定價實驗與AI驗收有具體行動。
- Product Owner／PM｜1111 全球華人｜「搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。」｜規格、相容性、UAT與階段上線責任明確。

**可改進（≤5 點）**

- 位置：Product Owner／PM｜1111 全球華人
  - 原句：「平均處理時間由 100.4 天降至 30.9 天。」
  - 問題類型：`measurement`
  - 嚴重度：`interview_follow_up`
  - 影響：有期間與結果，但案件分母、統計定義及組成變化未交代；不能直接歸因流程改善。 可於面試核對，不構成直接否定。
  - 建議方向：補案件數、起訖及未結案處理，說明清案與案件組成的影響。

- 位置：Product Owner／PM｜1111 全球華人
  - 原句：「調整後至 2026/10 未再出現同類冒用。」
  - 問題類型：`measurement`
  - 嚴重度：`interview_follow_up`
  - 影響：已限定目前掌握情況，但客服回報或觀察不等於完整安全監測。 可於面試核對，不構成直接否定。
  - 建議方向：說明事件定義、資料來源、觀察窗、偵測與漏報限制。

- 位置：專業摘要
  - 原句：「從使用者旅程釐清需求、協調優先級」
  - 問題類型：`ownership`
  - 嚴重度：`interview_follow_up`
  - 影響：有需求協調與交付，尚未呈現區域PM與總部roadmap談判及策略核准邊界。 可於面試核對，不構成直接否定。
  - 建議方向：補本地需求與跨國總部衝突、選項、本人權責與里程碑協商案例。

- 位置：Product Owner／PM｜1111 全球華人
  - 原句：「我協調工程與客服，釐清受影響範圍」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：帳號安全案例直接相關，但資安專業、法務的實際參與與驗收責任不清楚。 可於面試核對，不構成直接否定。
  - 建議方向：補威脅情境、風險取捨及資安法務工程分工。

- 位置：專業技能
  - 原句：「使用者訪談與問卷、競品實測」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：方法清單尚不足顯示研究抽樣、洞察及bucket/A/B如何影響選擇。 可於面試核對，不構成直接否定。
  - 建議方向：補一個研究問題、抽樣與分組、洞察到決策及量測限制案例。

**編輯附件**：無。

#### 7. 資深能力分布

delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

#### 8. 未測試聲明

PDF 抽字：本內容審查 `not_tested`（另見總報告 §6 的 `local_extraction`）／ATS 匯入：`not_tested`／AI 作者判讀：不可由文字判定／真人校準：`not_run`。

### A.14｜jd44｜原始單行 JSON

```json
{"rubric_version":"4.2","resume_id":"appendix-A-v10.2","job_id":"jd44","job_input":"summary","model_id":"unknown","run_id":"jd44-A-01","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上網路產品PM經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"具體App、平台與招募系統經歷支持年資及網路產品情境。"},{"id":"R02","text":"用戶中心；需求行為理解；參與及留存成長","type":"required","status":"partial","evidence":["依使用者旅程與工單問題安排優先級"],"blocks_interview":false,"reason":"旅程、工單與大型客戶需求有實例；DAU成長含導流，未呈現參與及留存改善。"},{"id":"R03","text":"市場、競品與數據形成長期roadmap策略；策略執行","type":"required","status":"partial","evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"blocks_interview":false,"reason":"有優先級與市場類比及交付；長期策略、競爭定位與目標串連待補。"},{"id":"R04","text":"數據行為、用研、A/B與KPI衡量","type":"required","status":"partial","evidence":["以售價不變的 Android 作對照"],"blocks_interview":false,"reason":"具定價對照實驗與指標；非同時隨機A/B，行為研究及留存KPI設計待驗證。"},{"id":"R05","text":"跨國跨職能及外部廠商概念、設計、工程、行銷業務協作","type":"required","status":"supported","evidence":["並與 CodaPay 新加坡技術團隊協調串接"],"blocks_interview":false,"reason":"跨部門、海外金流及在地化實例支持協作；外部廠商共同探索概念深度可追問。"},{"id":"R06","text":"完整產品週期與新產品迭代","type":"required","status":"supported","evidence":["主導 Juicy 推出"],"blocks_interview":false,"reason":"KOOL規劃至上線、Juicy推出及現有產品迭代具體，支持完整週期。"},{"id":"R07","text":"AI個人化串流與粉絲互動產品規劃","type":"required","status":"partial","evidence":["定義使用情境與驗收標準"],"blocks_interview":false,"reason":"AI推薦與社交媒合可轉移；音樂串流及粉絲互動應用未呈現，非已知不符。"},{"id":"R08","text":"優異英文口說與書寫","type":"required","status":"partial","evidence":["並以英文進行跨國協作"],"blocks_interview":false,"reason":"英文跨國分派、翻譯與檢定具線索，優異產品策略口寫程度仍需實作面試。"},{"id":"R09","text":"音樂、內容、社群、娛樂或AI經驗","type":"preferred","status":"supported","evidence":["經手交友、訂閱制內容 App 與網紅媒合平台"],"blocks_interview":false,"reason":"內容、社交娛樂及AI推薦有相關實例；音樂領域未呈現。"},{"id":"R10","text":"日文能力","type":"preferred","status":"unknown","evidence":[],"blocks_interview":false,"reason":"日本在地化經驗不能證明本人日文，僅加分條件未提供。"},{"id":"R11","text":"AI熱忱或AI產品launch實務；成功新產品或核心功能上線","type":"preferred","status":"supported","evidence":["上線公司簡介生成、職缺工作說明生成及 AI 推薦人才"],"blocks_interview":false,"reason":"AI實際上線與多項核心功能交付支持；商業成功程度仍依各案量測判斷。 "}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["經手交友、訂閱制內容 App 與網紅媒合平台"],"missing":["音樂串流情境與長期策略責任需釐清"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"足夠","evidence":["以售價不變的 Android 作對照"],"missing":["留存與行為A/B實務、英文策略溝通深度"],"issue_ids":["I02","I03"]},{"id":"decision_depth","rating":"強","evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"missing":["長期策略的替代選項與資源配置"],"issue_ids":["I01"]},{"id":"outcome_quality","rating":"足夠","evidence":["各期 21 天"],"missing":["DAU來源、實驗可比性、留存與AI成效"],"issue_ids":["I02","I04"]},{"id":"ownership","rating":"強","evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"missing":["跨公司共同探索及策略最終決策權可面試核對"],"issue_ids":[]},{"id":"readability","rating":"足夠","evidence":["工作涵蓋系統分析、流程與畫面設計、PRD、Prototype、UAT 與上線計畫"],"missing":["可集中呈現與音樂產品相關的策略及成長案例"],"issue_ids":[]}],"results":[{"quote":"兩案均在開發中","kinds":["decision","in_progress"]},{"quote":"平均處理時間由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"團隊依結果決定採用低價","kinds":["decision"]},{"quote":"上線公司簡介生成、職缺工作說明生成及 AI 推薦人才","kinds":["output"]},{"quote":"男性 DAU 在 6 週內由約 3,200 增至 1.25 萬","kinds":["outcome"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"網路PM及內容經驗可轉移"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 Product Owner"],"application_note":"近期企業端，過往消費端可銜接"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我主責規劃"],"application_note":"本人規劃與工程交付可區分"},{"rule_id":"HR04","status":"partial","resume_evidence":["平均處理時間由 100.4 天降至 30.9 天"],"application_note":"有改變，仍需量測口徑"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"application_note":"支持優先級判斷"},{"rule_id":"HR06","status":"supported","resume_evidence":["從 SweetRing 的海外市場開始累積產品經驗"],"application_note":"責任由在地化轉到產品規劃"},{"rule_id":"HR07","status":"supported","resume_evidence":["並與 CodaPay 新加坡技術團隊協調串接"],"application_note":"跨國協作有具體用途"},{"rule_id":"HR08","status":"supported","resume_evidence":["資深產品經理｜Senior Product Manager"],"application_note":"職務與案例易定位"},{"rule_id":"HR09","status":"partial","resume_evidence":["男性 DAU 在 6 週內由約 3,200 增至 1.25 萬"],"application_note":"需核對導流、留存與歸因"},{"rule_id":"HR10","status":"supported","resume_evidence":["我希望把更多心力放回產品策略"],"application_note":"方向相容但非音樂動機證據"},{"rule_id":"HR11","status":"unknown","resume_evidence":["台北市、新北市，可接受遠端或混合辦公"],"application_note":"JD未列地點，未見已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["主導 Juicy 推出"],"application_note":"支持邀約驗證策略及成長"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["經手交友、訂閱制內容 App 與網紅媒合平台"],"evidence_type":"context","source_ids":[],"interview_question":"如何將訂閱社交經驗轉為音樂串流與粉絲需求假設？"},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程與工單問題安排優先級"],"evidence_type":"decision","source_ids":[],"interview_question":"哪項用戶證據改變了原本計畫，如何確認代表性？"},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":"如何比較兩案價值、成本與風險，誰決定資源？"},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["團隊依結果決定採用低價"],"evidence_type":"decision","source_ids":[],"interview_question":"定價實驗如何連結長期收入、訂閱留存與市場策略？"},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["各期 21 天"],"evidence_type":"context","source_ids":[],"interview_question":"如何排除平台人群、行銷及時間變動對實驗的影響？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["與 QA 制定 UAT 驗收案例"],"evidence_type":"output","source_ids":[],"interview_question":"本人、工程、行銷及外部廠商各自擁有哪些決策權？"},{"rule_id":"HM07","primary_dimension":"ownership","status":"supported","resume_evidence":["處理新舊系統並行的相容性需求"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["整理帳號權限、職缺關聯與既有資料轉換規則"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"ownership","status":"supported","resume_evidence":["重新制定業務流程、對照資料欄位並重構規格"],"evidence_type":"output","source_ids":[],"interview_question":"請用一份roadmap說明跨期目標與資源配置責任。"},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["曾規劃雙邊媒合與付費機制、設計定價實驗"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["並依客服測試回饋調整推薦規則"],"evidence_type":"decision","source_ids":[],"interview_question":"哪些回饋或反證改變推薦規則，如何驗證修正效果？"},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["並以英文進行跨國協作"],"evidence_type":"context","source_ids":[],"interview_question":"請用英文說明一項產品取捨及其驗證指標。"},{"rule_id":"HM13","primary_dimension":"method","status":"supported","resume_evidence":["兩案均在開發中"],"evidence_type":"in_progress","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HM03","source_ids":[],"application_note":"長期方向能力需案例驗證","context_limit":"短期功能取捨不等同長期市場策略","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"我希望把更多心力放回產品策略","reason":"表達方向與JD相容，但市場定位、長期roadmap及資源配置的既有責任未充分呈現。","suggestion":"補一個由市場及用戶證據導出年度方向、替代方案與資源安排的案例。"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"實驗與留存能力值得追問","context_limit":"序列測試加跨平台對照，非隨機A/B","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"以售價不變的 Android 作對照","reason":"實驗有期間與基準，但平台差異、樣本及同期因素未交代；未展示留存成效。","suggestion":"補樣本、付費人群、流量來源、可比性限制及參與留存KPI。"},{"id":"I03","rule_id":"HR11","source_ids":[],"application_note":"英文以面試實作核對","context_limit":"檢定與協作經驗非優異口寫直接測試","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"並以英文進行跨國協作","reason":"英文使用有支持，但JD優異口寫需以產品討論與書面樣本確認，非不符。","suggestion":"提供英文需求文件或以英文講解產品決策。"},{"id":"I04","rule_id":"HM05","source_ids":[],"application_note":"DAU不能單獨證明持續成長","context_limit":"履歷明列產品上線與行銷導流期間","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"男性 DAU 在 6 週內由約 3,200 增至 1.25 萬","reason":"上線及導流共同發生，缺同期流量與留存口徑，不能全歸本人或解讀為持續成長。","suggestion":"補遷移、新客、投放及留存拆解，區分本人交付與團隊成長結果。"}],"decision":{"recommendation":"interview","evidence":["主導 Juicy 推出","團隊依結果決定採用低價","定義使用情境與驗收標準"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"待補"},"interview_reasons":["「主導 Juicy 推出」及KOOL上線支持新產品全週期交付。","「以售價不變的 Android 作對照」支持商業數據判斷。","「定義使用情境與驗收標準」與跨國金流協作可轉移至AI音樂產品。"],"key_gaps":["長期市場策略與資源配置：追問年度roadmap及決策權。","參與留存與A/B：追問用戶行為、樣本與混雜因素。","領域及英文：驗證音樂粉絲問題理解及英文口寫實作。"],"strengths":["具訂閱、內容社交、媒合與支付的相關產品案例。","能用具體限制與使用情境說明優先級及規格判斷。","AI產品、跨國及跨職能協作均有落地線索。"],"interview_questions":["如何將訂閱社交經驗轉為音樂串流與粉絲需求假設？","哪項用戶證據改變了原本計畫，如何確認代表性？","如何比較兩案價值、成本與風險，誰決定資源？","定價實驗如何連結長期收入、訂閱留存與市場策略？","如何排除平台人群、行銷及時間變動對實驗的影響？","本人、工程、行銷及外部廠商各自擁有哪些決策權？","請用一份roadmap說明跨期目標與資源配置責任。","哪些回饋或反證改變推薦規則，如何驗證修正效果？"],"editorial_appendix":[],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"多產品交付、定價對照及使用者痛點取捨形成一致可轉移模式；量測限制可辨識。長期音樂策略、留存及資源責任仍待驗證，不支持9。"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"not_tested","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 單份審查｜履歷 appendix-A-v10.2｜第 14 輪｜model_id: unknown

#### 1. 結論

- 招聘決定：`interview`
- Level：8（±1）
- 一句話理由：「主導 Juicy 推出」支持面試，缺口依下表核對。

#### 2. 六維度

| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 經手交友、訂閱制內容 App 與網紅媒合平台 | 音樂串流情境與長期策略責任需釐清 |
| role_evidence | 足夠 | 以售價不變的 Android 作對照 | 留存與行為A/B實務、英文策略溝通深度 |
| decision_depth | 強 | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 長期策略的替代選項與資源配置 |
| outcome_quality | 足夠 | 各期 21 天 | DAU來源、實驗可比性、留存與AI成效 |
| ownership | 強 | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 跨公司共同探索及策略最終決策權可面試核對 |
| readability | 足夠 | 工作涵蓋系統分析、流程與畫面設計、PRD、Prototype、UAT 與上線計畫 | 可集中呈現與音樂產品相關的策略及成長案例 |

#### 3. JD 條件對照

| 條件 | 必要／加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 3年以上網路產品PM經驗 | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 具體App、平台與招募系統經歷支持年資及網路產品情境。 |
| 用戶中心；需求行為理解；參與及留存成長 | 必要 | partial | 依使用者旅程與工單問題安排優先級 | 旅程、工單與大型客戶需求有實例；DAU成長含導流，未呈現參與及留存改善。 |
| 市場、競品與數據形成長期roadmap策略；策略執行 | 必要 | partial | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 有優先級與市場類比及交付；長期策略、競爭定位與目標串連待補。 |
| 數據行為、用研、A/B與KPI衡量 | 必要 | partial | 以售價不變的 Android 作對照 | 具定價對照實驗與指標；非同時隨機A/B，行為研究及留存KPI設計待驗證。 |
| 跨國跨職能及外部廠商概念、設計、工程、行銷業務協作 | 必要 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 跨部門、海外金流及在地化實例支持協作；外部廠商共同探索概念深度可追問。 |
| 完整產品週期與新產品迭代 | 必要 | supported | 主導 Juicy 推出 | KOOL規劃至上線、Juicy推出及現有產品迭代具體，支持完整週期。 |
| AI個人化串流與粉絲互動產品規劃 | 必要 | partial | 定義使用情境與驗收標準 | AI推薦與社交媒合可轉移；音樂串流及粉絲互動應用未呈現，非已知不符。 |
| 優異英文口說與書寫 | 必要 | partial | 並以英文進行跨國協作 | 英文跨國分派、翻譯與檢定具線索，優異產品策略口寫程度仍需實作面試。 |
| 音樂、內容、社群、娛樂或AI經驗 | 加分 | supported | 經手交友、訂閱制內容 App 與網紅媒合平台 | 內容、社交娛樂及AI推薦有相關實例；音樂領域未呈現。 |
| 日文能力 | 加分 | unknown |  | 日本在地化經驗不能證明本人日文，僅加分條件未提供。 |
| AI熱忱或AI產品launch實務；成功新產品或核心功能上線 | 加分 | supported | 上線公司簡介生成、職缺工作說明生成及 AI 推薦人才 | AI實際上線與多項核心功能交付支持；商業成功程度仍依各案量測判斷。  |

#### 4. HR 十二問／HM 十三問

| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 網路PM及內容經驗可轉移 |
| HR02 | supported | 現任 1111 招募系統 Product Owner | 近期企業端，過往消費端可銜接 |
| HR03 | supported | 由我主責規劃 | 本人規劃與工程交付可區分 |
| HR04 | partial | 平均處理時間由 100.4 天降至 30.9 天 | 有改變，仍需量測口徑 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 支持優先級判斷 |
| HR06 | supported | 從 SweetRing 的海外市場開始累積產品經驗 | 責任由在地化轉到產品規劃 |
| HR07 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 跨國協作有具體用途 |
| HR08 | supported | 資深產品經理｜Senior Product Manager | 職務與案例易定位 |
| HR09 | partial | 男性 DAU 在 6 週內由約 3,200 增至 1.25 萬 | 需核對導流、留存與歸因 |
| HR10 | supported | 我希望把更多心力放回產品策略 | 方向相容但非音樂動機證據 |
| HR11 | unknown | 台北市、新北市，可接受遠端或混合辦公 | JD未列地點，未見已知衝突 |
| HR12 | supported | 主導 Juicy 推出 | 支持邀約驗證策略及成長 |
| HM01 | supported | 經手交友、訂閱制內容 App 與網紅媒合平台 | 訂閱社交可轉移，音樂領域待驗證 |
| HM02 | supported | 依使用者旅程與工單問題安排優先級 | 用戶痛點有改變優先級 |
| HM03 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 具取捨，長期資源方向待問 |
| HM04 | supported | 團隊依結果決定採用低價 | 商業判斷有實例，不要求P&L |
| HM05 | partial | 各期 21 天 | 指標有期間，因果及留存待問 |
| HM06 | supported | 與 QA 制定 UAT 驗收案例 | 分工與本人規劃可區分 |
| HM07 | supported | 處理新舊系統並行的相容性需求 | 相容性及分段交付具體 |
| HM08 | supported | 整理帳號權限、職缺關聯與既有資料轉換規則 | 規則與資料限制支持技術協作 |
| HM09 | supported | 重新制定業務流程、對照資料欄位並重構規格 | 交付協調強，方向資源待補 |
| HM10 | supported | 曾規劃雙邊媒合與付費機制、設計定價實驗 | 代表案例清楚且與職務相關 |
| HM11 | supported | 並依客服測試回饋調整推薦規則 | 回饋改規則，效果仍待驗證 |
| HM12 | supported | 並以英文進行跨國協作 | 值得面試與英文作品驗證 |
| HM13 | supported | 兩案均在開發中 | 依JD判讀，進行中不當成果 |

#### 5. 約談理由（≤3）與關鍵缺口（≤3）

| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「主導 Juicy 推出」及KOOL上線支持新產品全週期交付。 |
| 2 | 「以售價不變的 Android 作對照」支持商業數據判斷。 |
| 3 | 「定義使用情境與驗收標準」與跨國金流協作可轉移至AI音樂產品。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 長期市場策略與資源配置：追問年度roadmap及決策權。 | 如何將訂閱社交經驗轉為音樂串流與粉絲需求假設？ |
| 2 | 參與留存與A/B：追問用戶行為、樣本與混雜因素。 | 哪項用戶證據改變了原本計畫，如何確認代表性？ |
| 3 | 領域及英文：驗證音樂粉絲問題理解及英文口寫實作。 | 如何比較兩案價值、成本與風險，誰決定資源？ |

#### 6. 評語（給寫稿者的具體回饋）

**做得好（3 點）**

- 尚凡經歷｜「主導 Juicy 推出」｜支持新產品與跨職能交付。
- 定價實驗｜「團隊依結果決定採用低價」｜連接數據及商業選擇。
- 1111 AI功能｜「定義使用情境與驗收標準」｜支持AI產品需求與驗收協作。

**可改進（≤5 點）**

- 位置：自傳
  - 原句：「我希望把更多心力放回產品策略」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：表達方向與JD相容，但市場定位、長期roadmap及資源配置的既有責任未充分呈現。 長期方向能力需案例驗證
  - 建議方向：補一個由市場及用戶證據導出年度方向、替代方案與資源安排的案例。

- 位置：Product Manager｜尚凡國際創新科技
  - 原句：「以售價不變的 Android 作對照」
  - 問題類型：`measurement`
  - 嚴重度：`interview_follow_up`
  - 影響：實驗有期間與基準，但平台差異、樣本及同期因素未交代；未展示留存成效。 實驗與留存能力值得追問
  - 建議方向：補樣本、付費人群、流量來源、可比性限制及參與留存KPI。

- 位置：專業技能
  - 原句：「並以英文進行跨國協作」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：英文使用有支持，但JD優異口寫需以產品討論與書面樣本確認，非不符。 英文以面試實作核對
  - 建議方向：提供英文需求文件或以英文講解產品決策。

- 位置：Product Manager｜尚凡國際創新科技
  - 原句：「男性 DAU 在 6 週內由約 3,200 增至 1.25 萬」
  - 問題類型：`measurement`
  - 嚴重度：`interview_follow_up`
  - 影響：上線及導流共同發生，缺同期流量與留存口徑，不能全歸本人或解讀為持續成長。 DAU不能單獨證明持續成長
  - 建議方向：補遷移、新客、投放及留存拆解，區分本人交付與團隊成長結果。

**編輯附件**：無。

#### 7. 資深能力分布

delivery：強 ／ po_coordination：強 ／ direction_resources：待補

#### 8. 未測試聲明

PDF 抽字：本內容審查 `not_tested`（另見總報告 §6 的 `local_extraction`）／ATS 匯入：`not_tested`／AI 作者判讀：不可由文字判定／真人校準：`not_run`。

### A.15｜jd47｜原始單行 JSON

```json
{"rubric_version":"4.2","resume_id":"appendix-A-v10.2","job_id":"jd47","job_input":"summary","model_id":"unknown","run_id":"jd47-A-01","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上Software PM","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"2016年至今軟體產品經歷及具體交付支持年資要求。"},{"id":"R02","text":"至少一次完整新產品探索、驗證、設計、開發、上線、迭代直接負責","type":"required","status":"partial","evidence":["規劃 KOOL 網紅媒合平台"],"blocks_interview":false,"reason":"KOOL支持雙角色探索、流程設計與商業功能上線；Juicy支持主導推出。單一產品的驗證、開發責任及上線後迭代閉環仍需追問，未見不符證據。"},{"id":"R03","text":"清楚PRD、流程圖、資料結構","type":"required","status":"supported","evidence":["整理帳號權限、職缺關聯與既有資料轉換規則"],"blocks_interview":false,"reason":"有重構規格、PRD、流程設計及關聯與資料轉換案例；技能列流程圖，文件清楚程度可用作品確認。"},{"id":"R04","text":"理解API、JSON、基本SQL","type":"required","status":"partial","evidence":["API 串接規劃、舊系統資料盤點與新舊流程銜接"],"blocks_interview":false,"reason":"API由跨國金流串接規劃支持；JSON未呈現，基本SQL未呈現，與DBA取數不能代替SQL能力。列面試核對，不推定不符。"},{"id":"R05","text":"新產品MVP、成熟產品成長、策略多元專案Go-To-Market與Growth、資源排序上線迭代","type":"required","status":"supported","evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"blocks_interview":false,"reason":"KOOL及Juicy支持新產品推出，定價及付款支持成熟成長；Juicy與行銷導流支持GTM協作，工單排序與分階段交付支持資源安排；跨產品策略自主程度需核對。"},{"id":"R06","text":"商業模式、產業競品、需求分析與產品策略","type":"required","status":"supported","evidence":["參考 Airbnb 與交友平台的媒合方式"],"blocks_interview":false,"reason":"有跨平台類比、雙邊付費機制、定價實驗與需求旅程；停車產業策略需學習。"},{"id":"R07","text":"內部業務客服財務、外部夥伴教育訓練與測試驗收；內外跨部門協作","type":"required","status":"partial","evidence":["透過互動原型與 FAQ 向客服、業務說明功能"],"blocks_interview":false,"reason":"業務客服說明及QA/UAT有直接證據；外部金流協作成立，財務協作與外部夥伴教育訓練未呈現。"},{"id":"R08","text":"停車、交通、MaaS、保險、支付、FinTech領域經驗","type":"preferred","status":"supported","evidence":["導入 CodaPay"],"blocks_interview":false,"reason":"支付導入及付款渠道轉換直接相關；停車、交通、MaaS、保險未呈現，無須全部具備才成立領域加分。"},{"id":"R09","text":"Prompt、RAG、Agent實作","type":"preferred","status":"partial","evidence":["以 Claude Code 建立協作流程與共用 skill"],"blocks_interview":false,"reason":"Agent協作流程有自述實作；Prompt設計細節、RAG未呈現，可展示流程核對深度。"},{"id":"R10","text":"Growth數據","type":"preferred","status":"supported","evidence":["以售價不變的 Android 作對照"],"blocks_interview":false,"reason":"定價實驗有對照、期間及收入變化；DAU導流與付款占比另提供成長數據，歸因仍有限制。"},{"id":"R11","text":"AI/LLM規格、資料自動化、原型","type":"preferred","status":"partial","evidence":["運用 AI Agent 撰寫規格、整理與分析資料"],"blocks_interview":false,"reason":"AI規格與資料協作有證據；資料自動化程度及AI原型未明，不能將一般Prototype視為AI原型。"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["曾規劃雙邊媒合與付費機制、設計定價實驗"],"missing":["轉入停車交通產業的需求理解需面試驗證。"],"issue_ids":[]},{"id":"role_evidence","rating":"足夠","evidence":["設計流程與畫面、撰寫 PRD 與製作 Prototype"],"missing":["單一新產品完整驗證迭代閉環、JSON與SQL證據。"],"issue_ids":["I01","I02"]},{"id":"decision_depth","rating":"強","evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"missing":["可進一步釐清策略資源決策權。"],"issue_ids":[]},{"id":"outcome_quality","rating":"足夠","evidence":["2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天"],"missing":["案件分母與統計口徑、實驗同期差異及歸因限制。"],"issue_ids":["I03","I04"]},{"id":"ownership","rating":"足夠","evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃"],"missing":["跨產品方向和資源配置最終決策邊界。"],"issue_ids":["I05"]},{"id":"readability","rating":"足夠","evidence":["工作涵蓋系統分析、流程與畫面設計、PRD、Prototype、UAT 與上線計畫"],"missing":[],"issue_ids":[]}],"results":[{"quote":"系統服務逾 6 萬家活躍付費廠商（2026 Q3）","kinds":["context"]},{"quote":"與工程於 2025/09 完成上線","kinds":["output"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"團隊依結果決定採用低價","kinds":["decision"]},{"quote":"兩案均在開發中","kinds":["in_progress"]},{"quote":"平均處理時間由 100.4 天降至 30.9 天","kinds":["outcome"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["曾規劃雙邊媒合與付費機制、設計定價實驗"],"application_note":"商業成長與支付可轉移。"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 Product Owner"],"application_note":"近期企業端迭代範圍清楚。"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我主責規劃"],"application_note":"本人規劃與工程協作可區分。"},{"rule_id":"HR04","status":"partial","resume_evidence":["平均處理時間由 100.4 天降至 30.9 天"],"application_note":"改善有期間，分母口徑待問。"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前"],"application_note":"可追問排序依據及機會成本。"},{"rule_id":"HR06","status":"supported","resume_evidence":["從 SweetRing 的海外市場開始累積產品經驗"],"application_note":"由市場支付擴至系統責任。"},{"rule_id":"HR07","status":"supported","resume_evidence":["與 CodaPay 新加坡技術團隊協調串接"],"application_note":"跨國技術協作有情境。"},{"rule_id":"HR08","status":"supported","resume_evidence":["資深產品經理｜Senior Product Manager"],"application_note":"結構可辨，重點案例可定位。"},{"rule_id":"HR09","status":"partial","resume_evidence":["依目前掌握的情況"],"application_note":"口述觀察不能當監測紀錄。"},{"rule_id":"HR10","status":"supported","resume_evidence":["接下來，我希望把更多心力放回產品策略"],"application_note":"策略與成效方向相容。"},{"rule_id":"HR11","status":"unknown","resume_evidence":["台北市、新北市，可接受遠端或混合辦公"],"application_note":"JD未列地點語言到職限制。"},{"rule_id":"HR12","status":"supported","resume_evidence":["主導 Juicy 推出"],"application_note":"多個相關案例支持約談。"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["經手交友、訂閱制內容 App 與網紅媒合平台"],"evidence_type":"context","source_ids":[],"interview_question":"如何把支付與訂閱經驗轉用於停車交通場景？"},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["廠商反映的溝通中斷問題"],"evidence_type":"decision","source_ids":[],"interview_question":"工單中哪些使用者證據改變了原定排序？"},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["團隊依結果決定採用低價"],"evidence_type":"decision","source_ids":[],"interview_question":"低價方案如何權衡收入、轉換和續訂風險？"},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["完成實收試算"],"evidence_type":"decision","source_ids":[],"interview_question":"付款渠道與訂閱方案如何依成本及實收決定？"},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["各期 21 天"],"evidence_type":"outcome","source_ids":[],"interview_question":"實驗各期樣本量、季節性和行銷差異如何處理？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["與內部工程團隊分階段交付"],"evidence_type":"output","source_ids":[],"interview_question":"你與工程、設計及行銷的決策邊界各是什麼？"},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["處理新舊系統並行的相容性需求"],"evidence_type":"output","source_ids":[],"interview_question":"如何定義相容性驗收及回滾條件？"},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"partial","resume_evidence":["API 串接規劃"],"evidence_type":"output","source_ids":[],"interview_question":"請展示JSON請求回應，並用基本SQL回答產品問題。"},{"rule_id":"HM09","primary_dimension":"ownership","status":"partial","resume_evidence":["公司決定採新舊並行"],"evidence_type":"context","source_ids":[],"interview_question":"你直接決定哪些方向、人力或預算，哪些需主管裁決？"},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["工作涵蓋系統分析、流程與畫面設計"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["並依客服回饋修正操作流程"],"evidence_type":"decision","source_ids":[],"interview_question":"哪項回饋讓你改變原設計，後續如何確認有效？"},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["規劃 KOOL 網紅媒合平台"],"evidence_type":"output","source_ids":[],"interview_question":"請用KOOL展示探索、驗證、開發到上線迭代的完整責任。"},{"rule_id":"HM13","primary_dimension":"method","status":"supported","resume_evidence":["以售價不變的 Android 作對照"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HM08","source_ids":[],"application_note":"面試追問，不據未知直接否定。","context_limit":"只判文件證據，不推定不會。","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"與 DBA 協作取數","reason":"JSON與基本SQL為必要能力，現有取數協作不足以確認本人理解。","suggestion":"補一個JSON欄位/錯誤處理案例及本人SQL查詢。"},{"id":"I02","rule_id":"HM12","source_ids":[],"application_note":"面試追問，不據未知直接否定。","context_limit":"多案例不能自動拼成完整單一週期。","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"規劃 KOOL 網紅媒合平台","reason":"單一新產品從探索驗證到上線迭代的直接責任尚未完整串起。","suggestion":"補KOOL驗證方法、開發分工及上線後一次迭代。"},{"id":"I03","rule_id":"HM05","source_ids":[],"application_note":"面試追問，不據未知直接否定。","context_limit":"可支持流程改善線索，不能單獨歸因本人。","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"平均處理時間由 100.4 天降至 30.9 天","reason":"有期間及變化，案件量、結案定義、積案清理和案件組成仍未明。","suggestion":"補兩季案件數、起訖定義及清理效應。"},{"id":"I04","rule_id":"HM05","source_ids":[],"application_note":"面試追問，不據未知直接否定。","context_limit":"28%可為比例比值，不直接判算錯。","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"相對變化約多 28%","reason":"對照與還原設計清楚，但非隨機跨平台比較，樣本與同期干擾未交代。","suggestion":"補各期樣本、投放或產品變動，以及相對比值算法。"},{"id":"I05","rule_id":"HM09","source_ids":[],"application_note":"面試追問，不據未知直接否定。","context_limit":"公司決定不抹去本人方案與交付責任。","category":"ownership","severity":"interview_follow_up","block_target":null,"claim":"公司決定採新舊並行","reason":"有規劃交付責任，方向與資源取捨的最終權限尚有限定。","suggestion":"補本人提出的方案、資源請求及誰作最終裁決。"}],"decision":{"recommendation":"interview","evidence":["主導 Juicy 推出","以售價不變的 Android 作對照","與 CodaPay 新加坡技術團隊協調串接"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["「主導 Juicy 推出」支持新產品推出與GTM協作。","「以售價不變的 Android 作對照」支持Growth決策。","「與 CodaPay 新加坡技術團隊協調串接」支持支付與外部協作。"],"key_gaps":["JSON與基本SQL未呈現：以實際請求回應與查詢追問。","KOOL完整驗證到迭代責任：請沿同一產品展示閉環。","成效口徑與策略權限：追問案件分母、實驗干擾和資源決策邊界。"],"strengths":["商業定價實驗有對照、期間、還原及後續決策。","新舊系統資料及驗收交付具體。","支付渠道與跨國技術協作可轉移本職。"],"interview_questions":["如何把支付與訂閱經驗轉用於停車交通場景？","工單中哪些使用者證據改變了原定排序？","低價方案如何權衡收入、轉換和續訂風險？","實驗各期樣本量、季節性和行銷差異如何處理？","如何定義相容性驗收及回滾條件？","請展示JSON請求回應，並用基本SQL回答產品問題。","你直接決定哪些方向、人力或預算，哪些需主管裁決？","請用KOOL展示探索、驗證、開發到上線迭代的完整責任。"],"editorial_appendix":[],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"多個相關案例、明確排序與對照實驗支持一致判斷模式。量測口徑、完整新產品驗證迭代及JSON/SQL待核對，未達高度可追溯的9級；進行中整合只作決策證據。"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"not_tested","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 單份審查｜履歷 appendix-A-v10.2｜第 15 輪｜model_id: unknown

#### 1. 結論

- 招聘決定：`interview`
- Level：8（±1）
- 一句話理由：「主導 Juicy 推出」支持面試，缺口依下表核對。

#### 2. 六維度

| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 曾規劃雙邊媒合與付費機制、設計定價實驗 | 轉入停車交通產業的需求理解需面試驗證。 |
| role_evidence | 足夠 | 設計流程與畫面、撰寫 PRD 與製作 Prototype | 單一新產品完整驗證迭代閉環、JSON與SQL證據。 |
| decision_depth | 強 | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 可進一步釐清策略資源決策權。 |
| outcome_quality | 足夠 | 2026 Q1 至 Q2 的平均處理時間由 100.4 天降至 30.9 天 | 案件分母與統計口徑、實驗同期差異及歸因限制。 |
| ownership | 足夠 | 約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃 | 跨產品方向和資源配置最終決策邊界。 |
| readability | 足夠 | 工作涵蓋系統分析、流程與畫面設計、PRD、Prototype、UAT 與上線計畫 | 無新增缺口；以現有自述支持面試。 |

#### 3. JD 條件對照

| 條件 | 必要／加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 3年以上Software PM | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 2016年至今軟體產品經歷及具體交付支持年資要求。 |
| 至少一次完整新產品探索、驗證、設計、開發、上線、迭代直接負責 | 必要 | partial | 規劃 KOOL 網紅媒合平台 | KOOL支持雙角色探索、流程設計與商業功能上線；Juicy支持主導推出。單一產品的驗證、開發責任及上線後迭代閉環仍需追問，未見不符證據。 |
| 清楚PRD、流程圖、資料結構 | 必要 | supported | 整理帳號權限、職缺關聯與既有資料轉換規則 | 有重構規格、PRD、流程設計及關聯與資料轉換案例；技能列流程圖，文件清楚程度可用作品確認。 |
| 理解API、JSON、基本SQL | 必要 | partial | API 串接規劃、舊系統資料盤點與新舊流程銜接 | API由跨國金流串接規劃支持；JSON未呈現，基本SQL未呈現，與DBA取數不能代替SQL能力。列面試核對，不推定不符。 |
| 新產品MVP、成熟產品成長、策略多元專案Go-To-Market與Growth、資源排序上線迭代 | 必要 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | KOOL及Juicy支持新產品推出，定價及付款支持成熟成長；Juicy與行銷導流支持GTM協作，工單排序與分階段交付支持資源安排；跨產品策略自主程度需核對。 |
| 商業模式、產業競品、需求分析與產品策略 | 必要 | supported | 參考 Airbnb 與交友平台的媒合方式 | 有跨平台類比、雙邊付費機制、定價實驗與需求旅程；停車產業策略需學習。 |
| 內部業務客服財務、外部夥伴教育訓練與測試驗收；內外跨部門協作 | 必要 | partial | 透過互動原型與 FAQ 向客服、業務說明功能 | 業務客服說明及QA/UAT有直接證據；外部金流協作成立，財務協作與外部夥伴教育訓練未呈現。 |
| 停車、交通、MaaS、保險、支付、FinTech領域經驗 | 加分 | supported | 導入 CodaPay | 支付導入及付款渠道轉換直接相關；停車、交通、MaaS、保險未呈現，無須全部具備才成立領域加分。 |
| Prompt、RAG、Agent實作 | 加分 | partial | 以 Claude Code 建立協作流程與共用 skill | Agent協作流程有自述實作；Prompt設計細節、RAG未呈現，可展示流程核對深度。 |
| Growth數據 | 加分 | supported | 以售價不變的 Android 作對照 | 定價實驗有對照、期間及收入變化；DAU導流與付款占比另提供成長數據，歸因仍有限制。 |
| AI/LLM規格、資料自動化、原型 | 加分 | partial | 運用 AI Agent 撰寫規格、整理與分析資料 | AI規格與資料協作有證據；資料自動化程度及AI原型未明，不能將一般Prototype視為AI原型。 |

#### 4. HR 十二問／HM 十三問

| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 曾規劃雙邊媒合與付費機制、設計定價實驗 | 商業成長與支付可轉移。 |
| HR02 | supported | 現任 1111 招募系統 Product Owner | 近期企業端迭代範圍清楚。 |
| HR03 | supported | 由我主責規劃 | 本人規劃與工程協作可區分。 |
| HR04 | partial | 平均處理時間由 100.4 天降至 30.9 天 | 改善有期間，分母口徑待問。 |
| HR05 | supported | 搜尋結果頁的既有痛點，也排在新功能職缺健檢之前 | 可追問排序依據及機會成本。 |
| HR06 | supported | 從 SweetRing 的海外市場開始累積產品經驗 | 由市場支付擴至系統責任。 |
| HR07 | supported | 與 CodaPay 新加坡技術團隊協調串接 | 跨國技術協作有情境。 |
| HR08 | supported | 資深產品經理｜Senior Product Manager | 結構可辨，重點案例可定位。 |
| HR09 | partial | 依目前掌握的情況 | 口述觀察不能當監測紀錄。 |
| HR10 | supported | 接下來，我希望把更多心力放回產品策略 | 策略與成效方向相容。 |
| HR11 | unknown | 台北市、新北市，可接受遠端或混合辦公 | JD未列地點語言到職限制。 |
| HR12 | supported | 主導 Juicy 推出 | 多個相關案例支持約談。 |
| HM01 | supported | 經手交友、訂閱制內容 App 與網紅媒合平台 | 消費與企業產品經驗可轉移。 |
| HM02 | supported | 廠商反映的溝通中斷問題 | 使用者痛點有影響排序。 |
| HM03 | supported | 團隊依結果決定採用低價 | 取捨有實驗及優先級證據。 |
| HM04 | supported | 完成實收試算 | 有收入成本與商業模式案例。 |
| HM05 | partial | 各期 21 天 | 量測限制需追問。 |
| HM06 | supported | 與內部工程團隊分階段交付 | 協作不等於本人完成工程。 |
| HM07 | supported | 處理新舊系統並行的相容性需求 | 相容性與上線風險具體。 |
| HM08 | partial | API 串接規劃 | API有線索，JSON/SQL待核對。 |
| HM09 | partial | 公司決定採新舊並行 | 方向資源權限仍需確認。 |
| HM10 | supported | 工作涵蓋系統分析、流程與畫面設計 | 重點與責任可快速辨識。 |
| HM11 | supported | 並依客服回饋修正操作流程 | 回饋後修正有直接證據。 |
| HM12 | supported | 規劃 KOOL 網紅媒合平台 | 約談驗證完整新產品週期。 |
| HM13 | supported | 以售價不變的 Android 作對照 | 凍結準則獨立判讀，無外部效度。 |

#### 5. 約談理由（≤3）與關鍵缺口（≤3）

| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「主導 Juicy 推出」支持新產品推出與GTM協作。 |
| 2 | 「以售價不變的 Android 作對照」支持Growth決策。 |
| 3 | 「與 CodaPay 新加坡技術團隊協調串接」支持支付與外部協作。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | JSON與基本SQL未呈現：以實際請求回應與查詢追問。 | 如何把支付與訂閱經驗轉用於停車交通場景？ |
| 2 | KOOL完整驗證到迭代責任：請沿同一產品展示閉環。 | 工單中哪些使用者證據改變了原定排序？ |
| 3 | 成效口徑與策略權限：追問案件分母、實驗干擾和資源決策邊界。 | 低價方案如何權衡收入、轉換和續訂風險？ |

#### 6. 評語（給寫稿者的具體回饋）

**做得好（3 點）**

- 專業摘要｜「曾規劃雙邊媒合與付費機制、設計定價實驗」｜商業定價實驗有對照、期間、還原及後續決策。
- Product Owner／PM｜1111 全球華人｜「設計流程與畫面、撰寫 PRD 與製作 Prototype」｜新舊系統資料及驗收交付具體。
- Product Owner／PM｜1111 全球華人｜「搜尋結果頁的既有痛點，也排在新功能職缺健檢之前」｜支付渠道與跨國技術協作可轉移本職。

**可改進（≤5 點）**

- 位置：專業技能
  - 原句：「與 DBA 協作取數」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：JSON與基本SQL為必要能力，現有取數協作不足以確認本人理解。 面試追問，不據未知直接否定。
  - 建議方向：補一個JSON欄位/錯誤處理案例及本人SQL查詢。

- 位置：Product Manager｜尚凡國際創新科技
  - 原句：「規劃 KOOL 網紅媒合平台」
  - 問題類型：`requirement`
  - 嚴重度：`interview_follow_up`
  - 影響：單一新產品從探索驗證到上線迭代的直接責任尚未完整串起。 面試追問，不據未知直接否定。
  - 建議方向：補KOOL驗證方法、開發分工及上線後一次迭代。

- 位置：Product Owner／PM｜1111 全球華人
  - 原句：「平均處理時間由 100.4 天降至 30.9 天」
  - 問題類型：`measurement`
  - 嚴重度：`interview_follow_up`
  - 影響：有期間及變化，案件量、結案定義、積案清理和案件組成仍未明。 面試追問，不據未知直接否定。
  - 建議方向：補兩季案件數、起訖定義及清理效應。

- 位置：Product Manager｜尚凡國際創新科技
  - 原句：「相對變化約多 28%」
  - 問題類型：`measurement`
  - 嚴重度：`interview_follow_up`
  - 影響：對照與還原設計清楚，但非隨機跨平台比較，樣本與同期干擾未交代。 面試追問，不據未知直接否定。
  - 建議方向：補各期樣本、投放或產品變動，以及相對比值算法。

- 位置：自傳
  - 原句：「公司決定採新舊並行」
  - 問題類型：`ownership`
  - 嚴重度：`interview_follow_up`
  - 影響：有規劃交付責任，方向與資源取捨的最終權限尚有限定。 面試追問，不據未知直接否定。
  - 建議方向：補本人提出的方案、資源請求及誰作最終裁決。

**編輯附件**：無。

#### 7. 資深能力分布

delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

#### 8. 未測試聲明

PDF 抽字：本內容審查 `not_tested`（另見總報告 §6 的 `local_extraction`）／ATS 匯入：`not_tested`／AI 作者判讀：不可由文字判定／真人校準：`not_run`。

## 附錄 B：格式修補前原始輸出（不納入統計）

### jd34｜technical_failure: evidence_format（已修補）

僅 decision.evidence 三句由摘要改原文；決定與評等未變更。以下保留修補前的完整單行 JSON。

```json
{"rubric_version":"4.2","resume_id":"appendix-A-v10.2","job_id":"jd34","job_input":"summary","model_id":"unknown","run_id":"jd34-A-01","human_calibrated":false,"requirements":[{"id":"R01","text":"產品管理內文2年以上；經歷欄5年以上（兩者並列）","type":"required","status":"supported","evidence":["近 10 年 PM 經驗"],"blocks_interview":false,"reason":"2016年至今的PM經歷支持兩項年資條件，資深程度另依案例判讀。"},{"id":"R02","text":"金流、物流、會員、促購優惠券、購買流程、訂單相關功能經驗","type":"required","status":"partial","evidence":["規劃使用流程、訂閱與付費機制"],"blocks_interview":false,"reason":"金流、付費購買流程與訂閱有案例；會員僅帳號權限可轉移；物流、優惠券及訂單未明示。JD未明示每項均為硬門檻，面試釐清廣度。"},{"id":"R03","text":"完整週期交付上市；新產品完整開發","type":"required","status":"supported","evidence":["主導 Juicy 推出"],"blocks_interview":false,"reason":"上市、PRD、UAT與上線計畫均有證據；新產品亦有KOOL與Juicy案例。"},{"id":"R04","text":"商業模式、關係人需求與規格；UX、RD、QA及設計合作","type":"required","status":"supported","evidence":["與 QA 制定 UAT 驗收案例"],"blocks_interview":false,"reason":"付費模式、10個需求單位、工程設計合作及規格交付可對位。"},{"id":"R05","text":"定義目標並衡量數據效益；維運優化指標效率","type":"required","status":"supported","evidence":["平均處理時間由 100.4 天降至 30.9 天"],"blocks_interview":false,"reason":"定價實驗及處理週期支持；營運效益的母體與歸因仍需追問。"},{"id":"R06","text":"UI製作","type":"required","status":"supported","evidence":["設計流程與畫面"],"blocks_interview":false,"reason":"實際畫面、Prototype規劃與工具支持UI製作；可用作品確認細節。"},{"id":"R07","text":"參與運作Scrum","type":"required","status":"supported","evidence":["曾參與每週一個 Sprint 的 Scrum"],"blocks_interview":false,"reason":"符合參與經驗；現況為Kanban搭配瀑布，面試追問Scrum職責。"},{"id":"R08","text":"支付生態趨勢","type":"preferred","status":"partial","evidence":["整理抽成、稅、手續費與撥款週期"],"blocks_interview":false,"reason":"支持支付方案商業理解；未提供近期生態趨勢洞察。"},{"id":"R09","text":"募資提案簡報","type":"preferred","status":"unknown","evidence":[],"blocks_interview":false,"reason":"未呈現募資提案；主管匯報不等同募資。"},{"id":"R10","text":"200人以上軟體開發團隊工作2年以上","type":"preferred","status":"unknown","evidence":[],"blocks_interview":false,"reason":"履歷未呈現開發團隊人數，不能以公司規模推定。"},{"id":"R11","text":"GenAI產品案例","type":"preferred","status":"supported","evidence":["上線公司簡介生成、職缺工作說明生成及 AI 推薦人才"],"blocks_interview":false,"reason":"生成式功能已上線，定義情境與驗收責任有述；不把AI工具使用等同產品成果。"},{"id":"R12","text":"全通路新零售SaaS商業方向及Commerce Cloud、G11N、OMO情境","type":"required","status":"partial","evidence":["讓印尼、泰國等市場的用戶可用電信帳單與超商付款"],"blocks_interview":false,"reason":"企業流程、跨市場支付可轉移；未直接呈現零售OMO與商家營運案例。"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["現任 1111 招募系統 Product Owner"],"missing":["零售全通路SaaS的直接情境待面試對位"],"issue_ids":["I01"]},{"id":"role_evidence","rating":"足夠","evidence":["設計流程與畫面"],"missing":["部分商務模組及加分條件未呈現"],"issue_ids":["I01","I03","I04"]},{"id":"decision_depth","rating":"強","evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"足夠","evidence":["平均處理時間由 100.4 天降至 30.9 天"],"missing":["處理案件母體、支付占比與實驗限制待核對"],"issue_ids":["I02"]},{"id":"ownership","rating":"強","evidence":["約 50 項大項功能於 2023/12–2026/03 上線，由我主責規劃。"],"missing":["資源與方向決策最終權責待確認"],"issue_ids":["I05"]},{"id":"readability","rating":"足夠","evidence":["工作涵蓋系統分析、流程與畫面設計、PRD、Prototype、UAT 與上線計畫"],"missing":[],"issue_ids":[]}],"results":[{"quote":"系統服務逾 6 萬家活躍付費廠商（2026 Q3）","kinds":["context"]},{"quote":"平均處理時間由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"團隊依結果決定採用低價","kinds":["decision","outcome"]},{"quote":"網頁付款占營收由 24% 升至 80% 以上","kinds":["outcome"]},{"quote":"兩案均在開發中","kinds":["in_progress","decision"]},{"quote":"上線公司簡介生成、職缺工作說明生成及 AI 推薦人才","kinds":["output"]}],"hr_questions":[{"rule_id":"HR01","status":"partial","resume_evidence":["規劃使用流程、訂閱與付費機制"],"application_note":"支付交付可轉移，商務模組廣度待問"},{"rule_id":"HR02","status":"supported","resume_evidence":["人力銀行企業端招募系統專案負責人"],"application_note":"企業流程明確，零售客群不同"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我主責規劃"],"application_note":"本人規劃與工程交付邊界可見"},{"rule_id":"HR04","status":"partial","resume_evidence":["平均處理時間由 100.4 天降至 30.9 天"],"application_note":"有結果與期間，母體仍待核對"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。"],"application_note":"支持問題優先於新功能的取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從 SweetRing 的海外市場開始累積產品經驗"],"application_note":"消費產品到企業系統脈絡完整"},{"rule_id":"HR07","status":"supported","resume_evidence":["與 CodaPay 新加坡技術團隊協調串接"],"application_note":"實際跨境支付協作可確認"},{"rule_id":"HR08","status":"supported","resume_evidence":["資深產品經理｜Senior Product Manager"],"application_note":"角色與代表作容易定位"},{"rule_id":"HR09","status":"partial","resume_evidence":["網頁付款占營收由 24% 升至 80% 以上"],"application_note":"需核對占比母體與業務效益"},{"rule_id":"HR10","status":"supported","resume_evidence":["接下來，我希望把更多心力放回產品策略"],"application_note":"方向相容，零售動機可追問"},{"rule_id":"HR11","status":"unknown","resume_evidence":["台北市、新北市，可接受遠端或混合辦公"],"application_note":"JD未列完整條件，無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["規劃 Peach 付款由 App 內購轉向網頁"],"application_note":"足以約談，非招聘結果預測"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"partial","resume_evidence":["人力銀行企業端招募系統專案負責人"],"evidence_type":"context","source_ids":[],"interview_question":"如何把企業流程與跨境支付經驗轉用全通路零售？"},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["廠商反映的溝通中斷問題，使我優先推進信件與即時通整合"],"evidence_type":"decision","source_ids":[],"interview_question":"哪些使用者資料改變原先優先序？"},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。"],"evidence_type":"decision","source_ids":[],"interview_question":"如何比較既有痛點與新功能的價值和成本？"},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["團隊依結果決定採用低價"],"evidence_type":"decision","source_ids":[],"interview_question":"定價結果如何連結毛利、續訂與後續策略？"},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["相對變化約多 28%"],"evidence_type":"outcome","source_ids":[],"interview_question":"實驗各期樣本、母體與同期干擾為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["定義使用情境與驗收標準"],"evidence_type":"output","source_ids":[],"interview_question":"AI案例中你與資料科學團隊如何分工？"},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["處理新舊系統並行的相容性需求"],"evidence_type":"output","source_ids":[],"interview_question":"資料轉換與分階段上線如何驗收與回復？"},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["從舊帳號信箱並非唯一值的限制出發"],"evidence_type":"decision","source_ids":[],"interview_question":"驗證流程有哪些替代方案與工程限制？"},{"rule_id":"HM09","primary_dimension":"ownership","status":"supported","resume_evidence":["職稱為主任，帶領 2 名直屬產品企劃"],"evidence_type":"context","source_ids":[],"interview_question":"需求衝突時誰有最終資源與方向決定權？"},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["並依客服回饋修正操作流程"],"evidence_type":"decision","source_ids":[],"interview_question":"回饋如何轉為規則修正並驗證有效？"},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["製作 Prototype"],"evidence_type":"output","source_ids":[],"interview_question":"可否展示支付或生成式功能的規格與驗收案例？"},{"rule_id":"HM13","primary_dimension":"method","status":"supported","resume_evidence":["規劃 Peach 付款由 App 內購轉向網頁"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HR01","source_ids":[],"application_note":"商務領域轉移需面試核對","context_limit":"非能力不符；JD未明示所有模組皆硬門檻","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"規劃使用流程、訂閱與付費機制","reason":"金流付費支持，但物流、訂單、優惠券與直接OMO情境未呈現。","suggestion":"補充實際商務模組與零售流程案例；若未做過，說明可轉移的規則設計。"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"結果可用，量測限制待核對","context_limit":"占比不等於總營收成長；口述非監測紀錄","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"網頁付款占營收由 24% 升至 80% 以上","reason":"付款占比支持渠道轉移，尚未呈現淨收入與成本；處理週期亦缺案件母體。","suggestion":"補支付總額、淨收入與費率；補處理週期案件數、起訖定義及積案影響。"},{"id":"I03","rule_id":"HR01","source_ids":[],"application_note":"加分未知不阻擋面試","context_limit":"不由主管匯報推定募資或由公司名推定人數","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"向總經理、副總等主管匯報","reason":"未呈現募資提案與200人以上開發團隊兩年以上經驗。","suggestion":"若有，補募資對象、提案作用及開發團隊口徑與任期。"},{"id":"I04","rule_id":"HM08","source_ids":[],"application_note":"Scrum已有參與線索","context_limit":"現行Kanban不否定過去Scrum經驗","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"曾參與每週一個 Sprint 的 Scrum","reason":"參與年期與在Scrum事件、Backlog中的實際責任尚未展開。","suggestion":"補一個Scrum迭代中需求排序、驗收與回顧的實際例子。"},{"id":"I05","rule_id":"HM09","source_ids":[],"application_note":"方向與資源權責仍需確認","context_limit":"人數與主管匯報本身不決定資深程度","category":"ownership","severity":"interview_follow_up","block_target":null,"claim":"公司決定採新舊並行","reason":"規劃交付責任清楚；公司架構決策不宜歸為本人方向決策。","suggestion":"補本人提出的方向選項、資源配置及最終決策權責。"}],"decision":{"recommendation":"interview","evidence":["付款與定價案例對位商務變現","PRD、UI、UAT、上線與跨部門協作支持完整交付","生成式功能與問題排序有具體責任"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["「規劃 Peach 付款由 App 內購轉向網頁」支持支付與商業流程。","「與 QA 制定 UAT 驗收案例」支持完整週期與跨部門交付。","「團隊依結果決定採用低價」支持以實驗推動商業決策。"],"key_gaps":["零售OMO、物流訂單與優惠券廣度：追問最接近案例與轉移方式。","付款與處理週期成果：追問母體、淨效益與干擾因素。","方向與資源權責：追問自主選項、取捨與最終決策人。"],"strengths":["支付渠道與定價有商業決策案例。","企業系統規格、畫面、驗收及遷移交付具體。","使用者問題排序及生成式功能協作可面試驗證。"],"interview_questions":["請展開最接近訂單、會員、優惠券或OMO的案例與責任。","付款渠道轉移後淨收入、費率與付款轉換如何變化？","處理週期的案件數、定義與積案結構如何比較？","定價實驗各期樣本與季節干擾如何控制？","Scrum中你如何排序Backlog、驗收與回顧？","生成式功能如何驗收品質、風險與使用效益？","哪些資源或產品方向由你決定，哪些由主管決定？","是否有募資提案、大型開發團隊經歷或近期支付趨勢判斷？"],"editorial_appendix":[],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"多個交付、支付、定價與使用者優先序案例構成一致模式；取捨及對照衡量具體。零售直接經驗、量測母體與方向權責待核對，不支持9。"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"not_tested","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### jd43｜technical_failure: evidence_format（已修補）

僅 decision.evidence 三句由摘要改原文；決定與評等未變更。以下保留修補前的完整單行 JSON。

```json
{"rubric_version":"4.2","resume_id":"appendix-A-v10.2","job_id":"jd43","job_input":"summary","model_id":"unknown","run_id":"jd43-A-01","human_calibrated":false,"requirements":[{"id":"R01","text":"5年以上網路科技產品相關經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"工作時序與網路App、平台及招募系統案例支持相關經驗；年資本身不判資深程度。"},{"id":"R02","text":"策略及台灣本地需求、期待與PRD；與總部roadmap優先級及里程碑對齊","type":"required","status":"partial","evidence":["從使用者旅程釐清需求、協調優先級"],"blocks_interview":false,"reason":"本地需求、PRD與階段交付有案例；總部roadmap協商、台灣市場策略權責未具體呈現。"},{"id":"R03","text":"用研、競品、問卷訪談、bucket/A/B研究","type":"required","status":"partial","evidence":["使用者訪談與問卷、競品實測"],"blocks_interview":false,"reason":"訪談問卷競品主要為技能線索；定價對照實驗有案例，但分桶、隨機化與質性研究如何改變產品選擇待核對。"},{"id":"R04","text":"跨產品設計、工程、資安、法務及客服，概念到上線","type":"required","status":"partial","evidence":["工程、設計、QA、資料科學、客服、業務、法務與稽核協作"],"blocks_interview":false,"reason":"工程客服及設計合作有上線案例；法務僅清單，資安專業團隊協作未呈現。"},{"id":"R05","text":"概念到上線、全週期評估與持續優化","type":"required","status":"supported","evidence":["與 QA 制定 UAT 驗收案例、排定上線計畫"],"blocks_interview":false,"reason":"從雙邊平台規劃到上線及現有服務迭代有證據；上線後量測深度另見I01。"},{"id":"R06","text":"KPI、A/B及行為資料分析","type":"required","status":"partial","evidence":["以售價不變的 Android 作對照"],"blocks_interview":false,"reason":"營收與DAU指標及對照實驗具體；嚴格A/B設計、Messenger安全與訊息體驗KPI需驗證。"},{"id":"R07","text":"跨職能、跨國協作","type":"required","status":"supported","evidence":["與 CodaPay 新加坡技術團隊協調串接"],"blocks_interview":false,"reason":"跨職能有工程QA客服案例；跨國有新加坡金流及海外在地化案例。"},{"id":"R08","text":"分析解題、溝通與關係人管理","type":"required","status":"supported","evidence":["整理帳號權限、職缺關聯與既有資料轉換規則"],"blocks_interview":false,"reason":"群組與資料相容性顯示分析解題；優先級協調及對客服業務說明支持關係人溝通。"},{"id":"R09","text":"Confluence、Jira、Figma、Codex等工具","type":"required","status":"partial","evidence":["Figma、Axure RP、Notion、Trello"],"blocks_interview":false,"reason":"Figma明列；Confluence、Jira、Codex未呈現。Claude Code可轉移，不能等同已用Codex。"},{"id":"R10","text":"英文流利","type":"required","status":"supported","evidence":["並以英文進行跨國協作"],"blocks_interview":false,"reason":"英文跨國工作及測驗支持面試；實際總部會議、寫作與協商可用英文核對。"},{"id":"R11","text":"AI產品或整合經驗","type":"preferred","status":"supported","evidence":["上線公司簡介生成、職缺工作說明生成及 AI 推薦人才"],"blocks_interview":false,"reason":"有AI產品使用情境、驗收與規則調整，亦有Agent協作。"},{"id":"R12","text":"日語或韓語","type":"preferred","status":"unknown","evidence":["中文母語；英文 TOEIC 980、TOEFL iBT 93"],"blocks_interview":false,"reason":"未列日韓語能力；海外市場經驗不能代替語言證據。"}],"dimensions":[{"id":"positioning","rating":"足夠","evidence":["涵蓋訂閱制社交 App、網紅媒合平台與人力銀行招募系統。"],"missing":["總部協作的區域產品策略權責與近期消費型訊息情境待核對。"],"issue_ids":["I03"]},{"id":"role_evidence","rating":"足夠","evidence":["我協調工程與客服，釐清受影響範圍"],"missing":["資安法務深度、正式用研及工具經驗待面試補充。"],"issue_ids":["I04","I05"]},{"id":"decision_depth","rating":"強","evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。"],"missing":["可補總部與本地需求衝突時的決策依據。"],"issue_ids":["I03"]},{"id":"outcome_quality","rating":"足夠","evidence":["平均處理時間由 100.4 天降至 30.9 天。"],"missing":["處理週期母體、冒用事件監測與實驗可比性需核對。"],"issue_ids":["I01","I02"]},{"id":"ownership","rating":"強","evidence":["由我主責規劃。"],"missing":["策略核准與工程資安責任邊界可在案例面談釐清。"],"issue_ids":["I03","I04"]},{"id":"readability","rating":"足夠","evidence":["資深產品經理｜Senior Product Manager"],"missing":[],"issue_ids":[]}],"results":[{"quote":"系統服務逾 6 萬家活躍付費廠商（2026 Q3）","kinds":["context"]},{"quote":"於 2026/04 完成登入驗證調整","kinds":["output"]},{"quote":"調整後至 2026/10 未再出現同類冒用。","kinds":["outcome"]},{"quote":"兩案均在開發中","kinds":["in_progress"]},{"quote":"團隊依結果決定採用低價。","kinds":["decision"]},{"quote":"平均處理時間由 100.4 天降至 30.9 天。","kinds":["outcome"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["並依客服測試回饋調整推薦規則。"],"application_note":"安全、訊息與AI案例可轉移。"},{"rule_id":"HR02","status":"supported","resume_evidence":["人力銀行企業端招募系統專案負責人"],"application_note":"近期企業端與消費訊息情境有差異。"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我主責規劃。"],"application_note":"規劃、驗收與工程分工明確。"},{"rule_id":"HR04","status":"partial","resume_evidence":["平均處理時間由 100.4 天降至 30.9 天。"],"application_note":"週期下降可追問母體與定義。"},{"rule_id":"HR05","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。"],"application_note":"優先級選擇有問題依據。"},{"rule_id":"HR06","status":"supported","resume_evidence":["從 SweetRing 的海外市場開始累積產品經驗"],"application_note":"時序呈現海外到企業系統責任。"},{"rule_id":"HR07","status":"supported","resume_evidence":["與 CodaPay 新加坡技術團隊協調串接。"],"application_note":"跨國整合具體；工具有待核對。"},{"rule_id":"HR08","status":"supported","resume_evidence":["工作涵蓋系統分析、流程與畫面設計、PRD"],"application_note":"摘要與案例可辨識工作重點。"},{"rule_id":"HR09","status":"partial","resume_evidence":["調整後至 2026/10 未再出現同類冒用。"],"application_note":"口述觀察需核對監測來源。"},{"rule_id":"HR10","status":"supported","resume_evidence":["接下來，我希望把更多心力放回產品策略"],"application_note":"方向相容，動機可接職缺追問。"},{"rule_id":"HR11","status":"supported","resume_evidence":["台北市、新北市，可接受遠端或混合辦公"],"application_note":"已知地點方向相容，無明文衝突。"},{"rule_id":"HR12","status":"supported","resume_evidence":["定義使用情境與驗收標準"],"application_note":"支持約談，驗證總部及安全深度。"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"partial","resume_evidence":["涵蓋訂閱制社交 App、網紅媒合平台與人力銀行招募系統。"],"evidence_type":"context","source_ids":[],"interview_question":"請說明消費App及企業帳號經驗如何轉用Messenger與OA的台灣市場策略。"},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["廠商反映的溝通中斷問題，使我優先推進信件與即時通整合"],"evidence_type":"decision","source_ids":[],"interview_question":"你如何取得並分類使用者研究資料，哪些反證改變了訊息整合方案？"},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁的既有痛點，也排在新功能職缺健檢之前。"],"evidence_type":"decision","source_ids":[],"interview_question":"請重建搜尋改善與職缺健檢的比較依據、資源限制及決策權。"},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["團隊依結果決定採用低價。"],"evidence_type":"decision","source_ids":[],"interview_question":"定價實驗如何影響商業策略，如何處理平台差異與外在變化？"},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"partial","resume_evidence":["平均處理時間由 100.4 天降至 30.9 天。"],"evidence_type":"outcome","source_ids":[],"interview_question":"案件母體、起訖、未結案及清案後組成變化如何處理？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["再與 QA 制定 UAT 驗收案例、排定上線計畫"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["處理新舊系統並行的相容性需求。"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["從舊帳號信箱並非唯一值的限制出發"],"evidence_type":"decision","source_ids":[],"interview_question":"請以登入驗證說明資安、法務、工程分工及驗收和回滾條件。"},{"rule_id":"HM09","primary_dimension":"ownership","status":"supported","resume_evidence":["重新制定業務流程、對照資料欄位並重構規格"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["工作涵蓋系統分析、流程與畫面設計、PRD"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["並依客服回饋修正操作流程。"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["定義使用情境與驗收標準"],"evidence_type":"output","source_ids":[],"interview_question":"可否展示去識別PRD、研究結論與上線評估，並說明本人決策範圍？"},{"rule_id":"HM13","primary_dimension":"method","status":"supported","resume_evidence":["兩案均在開發中"],"evidence_type":"in_progress","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HM05","source_ids":[],"application_note":"可於面試核對，不構成直接否定。","context_limit":"定價實驗亦需核對對照可比性；此為主要量測缺口。","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"平均處理時間由 100.4 天降至 30.9 天。","reason":"有期間與結果，但案件分母、統計定義及組成變化未交代；不能直接歸因流程改善。","suggestion":"補案件數、起訖及未結案處理，說明清案與案件組成的影響。"},{"id":"I02","rule_id":"HR09","source_ids":[],"application_note":"可於面試核對，不構成直接否定。","context_limit":"不能據此認定零事件或防詐能力不足。","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"調整後至 2026/10 未再出現同類冒用。","reason":"已限定目前掌握情況，但客服回報或觀察不等於完整安全監測。","suggestion":"說明事件定義、資料來源、觀察窗、偵測與漏報限制。"},{"id":"I03","rule_id":"HM01","source_ids":[],"application_note":"可於面試核對，不構成直接否定。","context_limit":"跨國金流合作支持可轉移性，但不等同總部產品策略。","category":"ownership","severity":"interview_follow_up","block_target":null,"claim":"從使用者旅程釐清需求、協調優先級","reason":"有需求協調與交付，尚未呈現區域PM與總部roadmap談判及策略核准邊界。","suggestion":"補本地需求與跨國總部衝突、選項、本人權責與里程碑協商案例。"},{"id":"I04","rule_id":"HM08","source_ids":[],"application_note":"可於面試核對，不構成直接否定。","context_limit":"不要求本人實作資安；未知不判不符。","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"我協調工程與客服，釐清受影響範圍","reason":"帳號安全案例直接相關，但資安專業、法務的實際參與與驗收責任不清楚。","suggestion":"補威脅情境、風險取捨及資安法務工程分工。"},{"id":"I05","rule_id":"HR07","source_ids":[],"application_note":"可於面試核對，不構成直接否定。","context_limit":"對照定價案例有支持，非完全未知。","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"使用者訪談與問卷、競品實測","reason":"方法清單尚不足顯示研究抽樣、洞察及bucket/A/B如何影響選擇。","suggestion":"補一個研究問題、抽樣與分組、洞察到決策及量測限制案例。"}],"decision":{"recommendation":"interview","evidence":["帳號冒用處理與訊息整合對應安全及訊息體驗。","具跨國整合、定價實驗與全週期交付案例。","六維度足夠以上，無必要條件有明文不符證據。"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["「我協調工程與客服，釐清受影響範圍」對應帳號安全與跨職能。","「以售價不變的 Android 作對照」提供實驗決策面談材料。","「與 CodaPay 新加坡技術團隊協調串接。」支持跨國協作。"],"key_gaps":["總部roadmap與台灣策略權責：追問需求衝突、資源與里程碑協商。","量測與安全觀察限制：追問案件母體、對照可比性及冒用監測來源。","研究及資安法務深度：追問抽樣分組、洞察與跨專業驗收。"],"strengths":["帳號驗證與訊息整合可轉移至安全及訊息體驗。","取捨、定價實驗與AI驗收有具體行動。","規格、相容性、UAT與階段上線責任明確。"],"interview_questions":["請重建台灣需求與總部roadmap衝突的一次決策，說明本人權責及資源里程碑協商。","登入驗證調整如何定義威脅、評估使用摩擦，與資安法務工程如何分工？","未再發生同類冒用的資料來源、偵測覆蓋與漏報限制是什麼？","處理週期的案件數、起訖定義、未結案與清案後組成如何處理？","定價各期與平台如何確保可比，還有哪些變因及替代解釋？","提供訪談問卷到決策案例，說明抽樣、洞察、分桶及A/B設計。","用英文說明跨國整合中的需求分歧、書面PRD及協商結果。","請展示去識別PRD與上線評估，並核對Jira、Confluence、Codex及AI整合使用深度。"],"editorial_appendix":[],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"多案例支持相關交付、跨國協作與安全訊息轉移；有優先級取捨、對照實驗及限制語句。總部策略權責及量測可追溯性仍待核對，不以進行中訊息整合當成已實現成果。"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"not_tested","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"passed","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

## 附錄 C：輸入與輸出紀錄

輸入 hash 是單職缺轉錄檔的 SHA-256，供辨識本次給各審查員的資料；不代表職缺或履歷已外部查證。輸出 hash 對應附錄 A 的正式原始 JSON 檔（含檔案原有結尾換行，如有）。

| 職缺 | 輸入 SHA-256 | 原始 JSON SHA-256 |
| :-- | :-- | :-- |
| jd03 | d2dd4893b742830d8a1300dedf6ff8903de3b6b415e607f022f2b00f2c8d5462 | 02da3e1de418a601a442ed9a1703b05adf3bbd85b920a54888602c31afd63426 |
| jd09 | 4d97e932bc405583847df003250912dbfc68352d28f089fc3f29282b347009fe | 56fc6d1b79821e4230ede3cb18b5060da66835cbb0e059b86a6f35df0d84e135 |
| jd11 | c8121691db5cfde0b1aadca5ea67272d4998c0c5967708073153c7637460891c | 30962d532daaa9e9790ac864d0e51cad467176d6a988e243c38d682616704a3d |
| jd14 | c9ebd894d82a49bf4c5b2db2b087f94f73d2ecbe9051916f25281dd9818422d3 | b2124627e799ae265e0c31a535b337899b181b02f52af98e76d78f4ae98f6c5f |
| jd20 | be7a4a8593cbd9550722fee48325149a5eb7b715f855b6a6508229d8fee9d6e7 | 5110a78e3c8307fc0f5e36064e0f29e542b2fada4477b0ed000076ae009041a0 |
| jd26 | dd297a930f0d2966b29319d8f6586a4e9d8d581f100b23dd46912ed72139a969 | 7b153103539e6d920078ce7da7d76a1f37f67697f65c02a0ec831904c869082e |
| jd30 | 5ec59b05f464ede7926d408d9701ecffc1f037e3d71d3f87fbca46c2e53bdfca | 164543c2ff4b8e5be5fefe3f4d016d4ffd5e530a54a9c5723c677392d4f7e47f |
| jd31 | 17a49ada26ed1869897c92787f5928fac4295262ac64ab4dc21259c4f7260d38 | bb6f71da3a79b2c73aeff7d5bb53d743447c7a8b7e89ffe5a7a5fa6a90582221 |
| jd32 | 9f2f29f5680fde6cfe42b8974ee3a38038176390a2bf44e3e0d7a33f145543f5 | 6d3a34f987f164a45a8adc52e0a44cf584160669d26d4ed68ff5c7950063cd07 |
| jd34 | 085062add0212d285e02fc7eb51f29f8285e2ff47343791137dedf494ff2e1b5 | ebd7d14f7896d46d5b707235459b5d134bfa2a089088731eb69c6cfeed5d1e52 |
| jd36 | cd3310a419df7f383ce01ad9881b0118275ec832ad7fe34b4aa3b691510450e0 | 2f171d1dfd06724589d28c177cfbbfcc7faae71ab2e527e9e52202b0cdbe4825 |
| jd40 | 28fb0acbb296f87ca5492c39745804aa9e1d7490f67bb6c3f696c24bdc941b50 | d95f399b654b70f6668bd3e14dd1123e8f17cae4dbe4fbb095a7006d7cd99f0e |
| jd43 | e3c1db11b1ba7f8a1394a58e8cb4568689c04b8c576f28be03832c51beb43eb8 | 9db1c743eeafab1f0bfc334d3d555e7ce018a36c0e879896d1748790de314118 |
| jd44 | cafff7e70ceaa9687cba59d834ace7553f77859a59f86fa118f4e299b7164d5c | 16a54841964faa0abb533ea45687aafcfdbf817ded84e7df8f24a0e538ffb6e7 |
| jd47 | 29119bc219d5e3726400ee1fbc43a032755fcc7df64ca51ed806aee28429ed2d | 859372dc51fca0e71e09b0dd82151e2ff6fd1565e82f5f5094cda8f238984f3b |

