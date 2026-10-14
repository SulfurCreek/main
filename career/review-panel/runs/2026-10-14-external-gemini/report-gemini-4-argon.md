# 履歷驗證報告：8.1 版 vs 9.4 版｜2026-10-14｜model_id: gemini-4-argon｜human_calibration: not_run

## 1. 結論（≤5 行，先講答案）
- 兩版的招聘決定分布：8.1 版為 interview×3（100% 建議面試）；9.4 版為 interview×3（100% 建議面試）。
- Level 中位數與範圍：8.1 版中位數 Level 7（範圍 7–8）；9.4 版中位數 Level 7（範圍 7–8），兩版中位數差為 0。
- 整體判定：9.4 版略佔上風，9.4 版在 outcome_quality 與資安事件閉環提供更嚴謹的分母與時間窗，使面試驗證點更精確；8.1 版則在 decision_depth 保留了更多具體取捨細節。

## 2. 分數表
| 版本 | 輪數 | 招聘決定分布 | Level（中位數／範圍） | positioning | role_evidence | decision_depth | outcome_quality | ownership | readability |
| :-- | :-: | :-- | :-: | :-- | :-- | :-- | :-- | :-- | :-- |
| 8.1 版 | 3 | interview×3 | 7 (7–8) | 強×3 | 強×3 | 強×3 | 足夠×3 | 強×3 | 強×3 |
| 9.4 版 | 3 | interview×3 | 7 (7–8) | 強×3 | 強×3 | 足夠×3 | 強×3 | 強×3 | 強×3 |

## 3. HR／HM 兩版判定有差的題
| 題 | 8.1 | 9.4 | 差異的招聘意義 |
| :-- | :-- | :-- | :-- |
| HM02 使用者與問題理解 | supported（具體） | supported（概括） | 8.1 版具體引述客服反映配對「少又舊」查出修改日排序與實測競品，問題診斷生動；9.4 版改為概括性使用者旅程反思，具體洞察案例較淡。 |
| HM03 決策與取捨 | supported（雙案例） | supported（單案例） | 8.1 版在工作經歷載明「搜尋結果頁痛點改版排在職缺健檢之前」與「信件整合排在其他新功能之前」，取捨對照鮮明；9.4 版刪減搜尋改版排序，取捨僅留登入引導。 |
| HM05 結果與衡量 | partial / 足夠 | supported / 強 | 9.4 版補齊全站廠商分母基準（占 1.9%）、定價實驗各期天數（21 天）及非續訂營收相對變化拆解，並標示 Juicy 數據為行銷整體表現；8.1 版顆粒度較粗，9.4 版顯著更嚴謹。 |
| HM07 交付與風險 | supported（基本） | supported（閉環） | 9.4 版明訂簽章驗證上線日（2026/04/17）與觀察期（至 2026/10 未再出現），並交代統籌影響評估、時程、驗證與客服說明；8.1 版未載明確時程與觀察窗口。 |
| HM10 溝通與資訊取捨 | supported | supported（更優） | 9.4 版專業摘要結構化為 5 大要點，且將尚凡核心商業成果（定價實驗、網頁金流）置前，資訊掃描效率與重要性分級優於 8.1 版的段落式陳述。 |

## 4. 版本比較
合計：偏好 9.4 版 4 次（甲=9.4 時選甲 2 次、乙=9.4 時選乙 2 次）、偏好 8.1 版 0 次、無明確偏好 0 次、兩者均須先修正 0 次。
順序敏感：否（甲乙順序交換後，被偏好版本皆為 9.4 版，無順序偏誤）。
各輪偏好理由摘要：
- 第 1 輪（甲=8.1／乙=9.4，選乙）：乙版提供明確全站廠商分母（1.9%）、21 天定價實驗期與防冒用閉環上線日，面試驗證錨點更聚焦。
- 第 2 輪（甲=9.4／乙=8.1，選甲）：甲版拆解定價實驗營收波動公式（iOS +5%, Android -18%）並標示行銷導流歸因邊界，交付誠實度與信度更高。
- 第 3 輪（甲=8.1／乙=9.4，選乙）：乙版在商業金流與防詐事件的時間跨度完整（2020/11–2021/09、2026/04/17），時序查核成本大幅降低。
- 第 4 輪（甲=9.4／乙=8.1，選甲）：甲版摘要條列清晰且工具鏈補齊 Excel、Trello 等落地工具，整體可見性與衡量成熟度全面佔優。

## 5. 評語（合併後）

### 5.1 8.1 版：做得好／可改進
**做得好**：
- 1111經歷｜主導約 50 項大項功能上線...Roadmap 細項上線 111 項｜展示對接 16 個需求單位與跨單位大型模組之高頻繁交付能力。
- 1111經歷與自傳｜搜尋結果頁的痛點改版排在新功能職缺健檢之前；客服反映配對名單「少又舊」查出修改日排序｜生動呈現如何拆解使用者抱怨、實測競品並做出排定優先級的決策深度。
- 技能欄｜自建 Claude Code 協作流程（12 條分工、23 個共用 skill）｜清楚說明 AI 工作流具體落地細節與轉換衝突邏輯為工程條件的技術素養。

**可改進**：
- 位置：尚凡經歷
  - 原句：降價期 DAU +48%、非續訂營收相對對照組多約 28%
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：DAU 成長與營收變化混合陳述，且未交代各階段實驗天數與對照組基期營收波動，易引起主管對數據口徑之疑慮。
  - 建議方向：補充各期實驗天數（如 21 天）及 iOS/Android 個別營收增減幅度。
- 位置：1111經歷
  - 原句：需求流程服務過的 1,279 家付費廠商，年化留存 81.2%
  - 問題類型：measurement
  - 嚴重度：editorial
  - 影響：雖標明為觀察差異非因果，但缺乏母體全站廠商數之比例對照，難以客觀評估該族群之覆蓋深度。
  - 建議方向：補註占全站活躍付費廠商之比例（如約 1.9%）。
- 位置：1111經歷
  - 原句：統籌登入系統全面盤點，改用簽章驗證，之後未再發生
  - 問題類型：measurement
  - 嚴重度：editorial
  - 影響：防冒用處理未載明上線具體日期與觀察區間，使交付風險管控成果難以精確追蹤。
  - 建議方向：補註上線日期與截至特定月份未再發生之觀察期。

### 5.2 9.4 版：做得好／可改進
**做得好**：
- 尚凡經歷｜定價實驗採原價、iOS 降價、還原原價三階段（馬來西亞，2021/05–08，各期 21 天）...iOS 增 5%，Android 減 18%｜實驗口徑與對照組計算嚴謹透明，展現極高數據素養與業務核算成熟度。
- 1111經歷｜登入安全盤點源於 2026/04 十多家廠商帳號遭冒用...與工程協作於 2026/04/17 上線簽章驗證，至 2026/10 未再出現同類冒用｜交付閉環精準，包含影響評估、驗證流程、客服說明與長達半年的驗證期，高度對位防詐 BU 需求。
- 專業摘要｜現任 1111 招募系統 Product Owner...以 Kanban 推進瀑布式開發，運用 Claude Code 協作｜將原本密集段落拆為 5 點結構化清單，快速提煉產品跨度、金流成果與交付方法。

**可改進**：
- 位置：1111經歷與自傳
  - 原句：依使用者旅程與工單問題排定優先級
  - 問題類型：readability
  - 嚴重度：editorial
  - 影響：刪除了 8.1 版中「搜尋結果頁痛點 vs 職缺健檢排序」及自傳中「配對名單修改日排序實測競品」等具體案例，略微削弱日常 PO 決策之生動臨場感。
  - 建議方向：可於經歷或面試時適度帶出搜尋改版與排序規則調整之取捨實例。
- 位置：思維特經歷
  - 原句：SweetRing 在地化涵蓋美、墨、巴、印、馬、日、韓 7 市場
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：海外市場經驗屬 B2C App 在地化，非 JD 加分條件偏好之海外企業客戶（B2B/B2G）對接。
  - 建議方向：面試時主動說明跨國多市場協調與在地化需求轉譯能力如何套用於海外企業客戶。

### 5.3 若要合併兩版，建議保留／補回的內容（只能用兩份履歷已有的事實）
- 保留 9.4 版的嚴謹數據與邊界標示：保留全站廠商規模與占比（全站約 6.6 萬家、1,279 家占 1.9%）、定價實驗 21 天期與增減公式拆解、登入簽章 2026/04/17 上線日與至 2026/10 觀察期、Juicy 行銷導流整體表現標註。
- 保留 9.4 版的結構化專業摘要：維持 5 大重點條列式呈現，保持高掃描率。
- 補回 8.1 版具體的決策取捨條目：將 1111 經歷中「搜尋結果頁的痛點改版排在新功能職缺健檢之前（開發中）」補回經歷條列。
- 補回 8.1 版自傳的配對排序洞察：將自傳中「客服反映配對名單『少又舊』時，我先查出名單依履歷修改日排序，實測競品之後才改規則，也讓廠商可以自己切換排序」之具體產品洞察案例融入自傳。
- 補回 8.1 版技能欄的 AI 工具細節：在 Claude Code 項目中補回「12 條分工、23 個共用 skill、將衝突搜尋邏輯轉成工程條件」，強化技術協作硬實力。

## 6. 兩版共同缺口與面試追問（≤6 項）
| 缺口 | 影響 | 面試追問 | 需要使用者提供什麼事實 |
| :-- | :-- | :-- | :-- |
| 1. 海外 B2B/B2G 企業客戶經驗缺位 | JD 加分項偏好海外企業或政府客戶；候選人海外經驗為 B2C App，B2B 僅在台灣 | 過去在 SweetRing 跨 7 國協調與 CodaPay 新加坡技術對接中，是否有直接與海外企業或機構客戶溝通交付的經驗？如何轉移至海外防詐 B2B 客戶？ | 海外市場是否有涉及當地企業夥伴/機構窗口之商務或規格對接事實 |
| 2. SQL 與 BI 儀表板獨立查詢實績未載 | JD 必要條件要求能獨立使用 SQL/BI/試算表查詢分析；履歷僅列 GA4、Excel、對照組實驗與資料庫知識 | 在 1111 處理需求週報、1,857 張工單或付費廠商名冊留存比對時，是否親自編寫 SQL 撈取資料庫？常用的查詢語法與 BI 工具為何？ | 是否具備實際 SQL 撰寫或 BI 工具（Metabase/Tableau 等）之操作紀錄 |
| 3. 防詐與風控業務產品深度尚待檢驗 | 候選人防詐經驗聚焦於登入帳號遭冒用之簽章驗證（驗證層），尚未涉足詐騙偵測模型或防詐風險策略全貌 | 2026/04 處置十多家廠商帳號遭冒用時，簽章驗證防護了哪種攻擊手法（如撞庫/釣魚）？後續是否規劃更主動的異常行為偵測機制？ | 該起冒用事件之攻擊型態、防護技術架構及是否有其他風控專案事實 |
| 4. 瀑布+Kanban 交付中與 AI/RD 的具體協作邊界 | JD 要求 50% 專案管理並與 RD/QA/AI 團隊密切推進；需釐清 AI 推薦規則定義中的權責劃分 | 在與資料科學團隊上線推薦人才等 3 項 AI 功能時，AI 演算法評估指標（如準確率/召回率）由誰主導？客服回饋如何轉化為具體模型調整規則？ | 與資料科學家協作時的具體分工邊界、模型評估指標由誰制定 |
| 5. 跨 16 需求單位之分歧解決機制 | 候選人對接單位眾多，需確認面試中能否展現高難度利害關係人衝突化解案例 | 當業務單位要求特定客製化功能與客服反饋之系統溝通管道中斷產生資源衝突時，如何向副總及各處主管溝通並達成共識？ | 面對高層或跨部門重大利益分歧時之實際化解案例與溝通策略 |
| 6. 定價與成本利潤分析之 B2B 適用性 | 履歷定價實驗與 CodaPay 實收試算屬 B2C 訂閱制；JD 防詐 BU 涉及企業端產品報價與利潤分析 | 過去在 B2C 訂閱與手續費實收試算累積的定價思維，如何應用於防詐 B2B 企業方案（如 API 調用計費、階梯式授權或私有化部署）之報價規劃？ | 是否曾參與 1111 企業廠商招募方案之定價、搭售或成本效益估算 |

## 7. ATS 準備檢查（五塊，不加總）
| 塊 | 8.1 | 9.4 | 說明 |
| :-- | :-- | :-- | :-- |
| 1. 檔案接受 (File Acceptance) | not_tested | not_tested | 本次未提供二進位 PDF 或 DOCX 檔案實體，僅提供純文字；依規準標 `test_level: not_run`／`actual_ats_import_performed: false`。文字排版乾淨無加密或巨集限制。 |
| 2. 欄位解析 (Field Parsing) | pass | pass | 標準單欄時序型架構，姓名、聯絡方式、職稱—公司—起訖關係、教育背景與技能段落標籤明確，無複雜多欄、表格錯嵌或文字框干擾，解析器能正確建立時間軸。 |
| 3. 搜尋可見性 (Search Visibility) | pass | pass | JD 核心關鍵字對位完整（B2B、Product Owner、PRD、Roadmap、AI、登入安全、簽章驗證、金流、定價、Kanban、TOEIC 980），布林搜尋檢索可見度高。 |
| 4. 資格與流程條件 (Qualifications & Workflow) | pass | pass | 5 年以上 PM、B2B 招募全模組主導、近 10 年總經歷、高分英語檢定與無工作衝突之求職條件，可順暢通過系統基礎資格硬性篩選門檻。 |
| 5. 匹配功能與未知設定 (Matching & Unknown Config) | unknown | unknown | 雇主在 104 或企業內部 ATS（如 Greenhouse/Ashby）是否啟用 AI 履歷語意匹配、權重配比、自動化淘汰或發信規則皆屬未知，不預測或合成通用 ATS 分數。 |

## 8. 方法限制與未做項目
- 審查模型與是否為同一模型的新視窗：本審查全程由 `gemini-4-argon`（Gemini 4 Argon）於單一對話環境內執行；雖在結構上分離各輪審查與甲乙交換比較，但受單一對話模式限制，並非跨獨立物理視窗（非全新獨立 context）執行，同模型內可能存在前後記憶錨定效應。
- 未做項目：未執行真實 ATS 系統（104 企業後台／Greenhouse 實體環境）投遞匯入測試（無雇主授權與實體檔案，標 `actual_ats_import_performed: false`）；未進行真人招募團隊校準（`human_calibration: not_run`）；未進行跨模型（如 Claude / GPT 系列）交叉模型覆核。
- 技術失敗輪次：無（全 6 輪單份審查、4 輪版本比較及 ATS 文字層檢核皆順利完成，無 `technical_failure` 紀錄）。

# 附錄：① 獨立審查 A 明細（8.1 版 × 3 輪）

## 單份審查｜履歷 8.1｜第 1 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_8.1","job_id":"104_950oe_Gogolook_Senior_PM","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-8.1-01","human_calibrated":false,"requirements":[{"id":"R01","text":"5-8年以上B2B/B2G產品或專案管理經驗","type":"required","status":"supported","evidence":["Product Owner／PM｜1111 全球華人｜2022/08 - 迄今"],"blocks_interview":false,"reason":"近10年PM，企業招募系統PO近4年"},{"id":"R02","text":"接近母語等級英語口說與書寫","type":"required","status":"supported","evidence":["英文（TOEIC 980、TOEFL iBT 93）"],"blocks_interview":false,"reason":"高分英檢與美國交換及翻譯實務"},{"id":"R03","text":"優異的溝通與關係人管理能力","type":"required","status":"supported","evidence":["與工程、行銷、業務等 16 個需求單位對接"],"blocks_interview":false,"reason":"跨16單位協調並直接向副總匯報"},{"id":"R04","text":"扎實產品管理基礎（PRD/路線圖/風險控管）","type":"required","status":"supported","evidence":["主導約 50 項大項功能上線，從 PRD 到 UAT"],"blocks_interview":false,"reason":"完整涵蓋需求分析、規格與上線驗收"},{"id":"R05","text":"強烈的數據敏感度（SQL/BI/試算表分析）","type":"required","status":"partial","evidence":["數據分析（GA4、世代分析、對照組實驗）"],"blocks_interview":false,"reason":"具試算與實驗分析，未明載SQL與BI工具"},{"id":"R06","text":"熟悉AI工具與工作流整合","type":"required","status":"supported","evidence":["自建 Claude Code 協作流程（12條分工、23個skill）"],"blocks_interview":false,"reason":"建置AI協作工作流並落地3項AI功能"},{"id":"R07","text":"對防詐與風險偵測有真正熱情","type":"required","status":"supported","evidence":["十多家廠商帳號遭冒用，統籌登入系統全面盤點"],"blocks_interview":false,"reason":"具防冒用安全盤點與簽章驗證實績"},{"id":"R08","text":"具防詐、資安、風險管理或信任類產品經驗","type":"preferred","status":"supported","evidence":["改用簽章驗證，之後未再發生"],"blocks_interview":false,"reason":"實際處理企業帳號冒用並完成技術防護"},{"id":"R09","text":"曾服務企業客戶或政府機關，尤其海外市場","type":"preferred","status":"partial","evidence":["完成 SweetRing 美、墨、巴、印、馬、日、韓7市場在地化"],"blocks_interview":false,"reason":"具海外7國B2C與台灣B2B，缺海外B2B客戶"},{"id":"R10","text":"技術背景或曾與RD/AI團隊密切合作","type":"preferred","status":"supported","evidence":["與資料科學團隊上線 3 項 AI 功能"],"blocks_interview":false,"reason":"與工程及資料科學團隊密切協作並具AWS證照"},{"id":"R11","text":"具Agile/Scrum與Jira專案管理經驗","type":"preferred","status":"supported","evidence":["瀑布開發搭配 Kanban 與 Daily stand-up"],"blocks_interview":false,"reason":"具Kanban、站會與回顧實務，未明列Jira字樣"},{"id":"R12","text":"具產品定價、報價或成本利潤分析經驗","type":"preferred","status":"supported","evidence":["設計馬來西亞 iOS 三階段定價實驗...實收試算"],"blocks_interview":false,"reason":"具三階段定價實驗與跨國金流抽成稅費試算"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["企業端招募系統全模組（近 6.6 萬家活躍付費廠商）"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"強","evidence":["主導約 50 項大項功能上線，細項 111 項"],"missing":["未明列SQL與Jira工具字樣"],"issue_ids":[]},{"id":"decision_depth","rating":"強","evidence":["信件與即時通整合排在其他新功能之前"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"足夠","evidence":["需求平均處理週期從 100.4 天降到 30.9 天"],"missing":["定價實驗缺天數與基期拆解；留存缺全站分母占比"],"issue_ids":["I01","I02","I03"]},{"id":"ownership","rating":"強","evidence":["團隊 3 名企劃，直接向組織副總匯報"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["段落清晰，專案交付脈絡與數據易於檢索"],"missing":[],"issue_ids":[]}],"results":[{"quote":"需求平均處理週期從 100.4 天降到 30.9 天","kinds":["outcome"]},{"quote":"2026 年截至 9 月累計 1,857 張，完成 1,726 張","kinds":["output"]},{"quote":"年化留存 81.2%，同期全站 74.2%（觀察差異）","kinds":["outcome","context"]},{"quote":"降價期 DAU +48%、非續訂營收相對多約 28%","kinds":["outcome"]},{"quote":"Peach 網頁付款占比 24% → 八成以上","kinds":["outcome"]},{"quote":"2025/10 離峰切換上線，停機約 1.5 小時","kinds":["output","context"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"符合5年以上PM與B2B經驗要求"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 16 個需求單位"],"application_note":"近4年主責6.6萬家廠商招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["團隊 3 名企劃，直接向組織副總匯報"],"application_note":"個人負責規格、驗收與跨單位排程"},{"rule_id":"HR04","status":"supported","resume_evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"application_note":"交付週期縮短與留存率具明確紀錄"},{"rule_id":"HR05","status":"supported","resume_evidence":["盤點出上千組重複 E-mail，選擇首次登入引導確認"],"application_note":"兼顧系統轉換與廠商使用連續性"},{"rule_id":"HR06","status":"supported","resume_evidence":["從思維特助理PM、尚凡PM到1111企劃主任"],"application_note":"職涯由C端成長型產品演進至B2B平台"},{"rule_id":"HR07","status":"supported","resume_evidence":["寫成 PRD 與 Axure Prototype；和 QA 寫 UAT"],"application_note":"技能欄所列工具皆在經歷中有對應實作"},{"rule_id":"HR08","status":"supported","resume_evidence":["依摘要、工作經歷、學歷、專業技能、自傳分段"],"application_note":"結構清楚，重點與量化指標易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["年化留存 81.2%，同期全站 74.2%（非因果）"],"application_note":"誠實標註觀察差異，無誇大矛盾"},{"rule_id":"HR10","status":"supported","resume_evidence":["想在更早階段參與產品方向，從定義問題開始"],"application_note":"轉職動機與資深PM職責高度相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["雙北、可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點與到職時間無衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["具B2B大模組交付、登入防冒用與AI工作流實績"],"application_note":"證據充分，強烈建議安排面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["企業端招募系統全模組（約 6.6 萬家活躍付費廠商）"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["廠商抱怨溝通管道中斷，信件與即時通整合排最前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁痛點改版排在職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["馬來西亞 iOS 三階段定價實驗；網頁付款占八成"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"supported","resume_evidence":["處理週期 100.4 降至 30.9 天；留存為觀察差異"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["與 16 個需求單位對接，直接向組織副總匯報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["2025/10 離峰切換停機 1.5 小時；上線簽章驗證"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["與資料科學團隊上線 3 項 AI 功能；具 AWS 證照"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["主導約 50 項大項功能上線，細項 111 項"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["清楚交代問題背景、個人行動、結果與非因果限制"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依客服測試回饋調整規則；還原原價後全面調降"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["登入簽章驗證、AI推薦規則、定價實驗具追問價值"],"evidence_type":"context","source_ids":[],"interview_question":"請說明2026/04廠商帳號遭冒用之攻擊手法與簽章驗證架構細節"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["全項判讀均對齊職缺條件與履歷原文，未推測空窗"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HM05","source_ids":[],"application_note":"定價實驗缺實驗天數與基期拆解","context_limit":"尚凡經歷","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"降價期 DAU +48%、非續訂營收相對對照組多約 28%","reason":"未交代各期天數及iOS/Android各自基期漲跌，易生口徑疑問","suggestion":"補充實驗天數與對照組各別增減百分比"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"留存率缺全站母體分母占比","context_limit":"1111經歷","category":"measurement","severity":"editorial","block_target":null,"claim":"需求流程服務過的 1,279 家付費廠商，年化留存 81.2%","reason":"未標示1,279家占全站活躍廠商之比例","suggestion":"補註占全站活躍付費廠商之比例"},{"id":"I03","rule_id":"HM07","source_ids":[],"application_note":"防冒用簽章未標上線日與觀察期","context_limit":"1111經歷","category":"measurement","severity":"editorial","block_target":null,"claim":"統籌登入系統全面盤點，改用簽章驗證，之後未再發生","reason":"未載明上線日期與後續觀察時間長度","suggestion":"補充上線具體日期與觀察截止月份"}],"decision":{"recommendation":"interview","evidence":["主導約 50 項大項功能上線，具簽章驗證與 AI 實績"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["主導1111企業招募系統50大項功能與16單位協調，符合50%專案交付與跨部門要求","統籌2026/04廠商帳號遭冒用危機並上線簽章驗證，具防詐與資安實戰經驗","深度運用Claude Code建置工作流並與DS團隊落地3項AI功能，符合AI工具整合條件"],"key_gaps":["海外7國經驗為B2C社交App，缺乏直接面向海外B2B企業或政府機關客戶之交付案例","數據工具列GA4、Excel與對照實驗，未明文記載獨立撰寫SQL或BI儀表板查詢","防詐經驗集中於登入簽章驗證，需於面試確認對通訊防詐與風險偵測模型之理解深度"],"strengths":["1111經歷｜主導約 50 項大項功能上線｜展現大型B2B系統穩定交付力","1111經歷與自傳｜信件整合排新功能前、查出配對依修改日排序｜決策取捨具體生動","專業技能｜自建 Claude Code 協作流程（12條分工、23個skill）｜AI整合深入"],"interview_questions":["過去在SweetRing與CodaPay的海外經驗，如何轉移至東南亞或日韓B2B企業客戶需求收集？","在1111分析1,857張需求單與名冊留存時，是否親自使用SQL撈取資料？","2026/04廠商帳號冒用事件中，攻擊途徑為何？簽章驗證在架構上如何設計與驗收？","如何將Claude Code工作流與團隊既有專案管理工具（如Jira/Kanban）串接？"],"editorial_appendix":["可於技能欄明確標示SQL/BI熟練度，並補充專案管理工具名稱（如Jira）"],"spectrum":{"level":7,"uncertainty_levels":1,"basis":"具多個完整B2B交付與實驗案例支持面試，且有清楚取捨與衡量限制說明"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"not_tested","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：7（±1）
- 一句話理由：「主導約 50 項大項功能上線」且具防冒用簽章驗證與 AI 協作實績，足以支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 企業端招募系統全模組（近 6.6 萬家活躍付費廠商） | 無關鍵缺口，可於面試深化 |
| role_evidence | 強 | 主導約 50 項大項功能上線，細項 111 項 | 未明列SQL與Jira工具字樣 |
| decision_depth | 強 | 信件與即時通整合排在其他新功能之前 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 足夠 | 需求平均處理週期從 100.4 天降到 30.9 天 | 定價實驗缺天數與基期拆解；留存缺全站分母占比 |
| ownership | 強 | 團隊 3 名企劃，直接向組織副總匯報 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 段落清晰，專案交付脈絡與數據易於檢索 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 5-8年以上B2B/B2G產品或專案管理經驗 | 必要 | supported | Product Owner／PM｜1111 全球華人｜2022/08 - 迄今 | 近10年PM，企業招募系統PO近4年 |
| R02 接近母語等級英語口說與書寫 | 必要 | supported | 英文（TOEIC 980、TOEFL iBT 93） | 高分英檢與美國交換及翻譯實務 |
| R03 優異的溝通與關係人管理能力 | 必要 | supported | 與工程、行銷、業務等 16 個需求單位對接 | 跨16單位協調並直接向副總匯報 |
| R04 扎實產品管理基礎（PRD/路線圖/風險控管） | 必要 | supported | 主導約 50 項大項功能上線，從 PRD 到 UAT | 完整涵蓋需求分析、規格與上線驗收 |
| R05 強烈的數據敏感度（SQL/BI/試算表分析） | 必要 | partial | 數據分析（GA4、世代分析、對照組實驗） | 具試算與實驗分析，未明載SQL與BI工具 |
| R06 熟悉AI工具與工作流整合 | 必要 | supported | 自建 Claude Code 協作流程（12條分工、23個skill） | 建置AI協作工作流並落地3項AI功能 |
| R07 對防詐與風險偵測有真正熱情 | 必要 | supported | 十多家廠商帳號遭冒用，統籌登入系統全面盤點 | 具防冒用安全盤點與簽章驗證實績 |
| R08 具防詐、資安、風險管理或信任類產品經驗 | 加分 | supported | 改用簽章驗證，之後未再發生 | 實際處理企業帳號冒用並完成技術防護 |
| R09 曾服務企業客戶或政府機關，尤其海外市場 | 加分 | partial | 完成 SweetRing 美、墨、巴、印、馬、日、韓7市場在地化 | 具海外7國B2C與台灣B2B，缺海外B2B客戶 |
| R10 技術背景或曾與RD/AI團隊密切合作 | 加分 | supported | 與資料科學團隊上線 3 項 AI 功能 | 與工程及資料科學團隊密切協作並具AWS證照 |
| R11 具Agile/Scrum與Jira專案管理經驗 | 加分 | supported | 瀑布開發搭配 Kanban 與 Daily stand-up | 具Kanban、站會與回顧實務，未明列Jira字樣 |
| R12 具產品定價、報價或成本利潤分析經驗 | 加分 | supported | 設計馬來西亞 iOS 三階段定價實驗...實收試算 | 具三階段定價實驗與跨國金流抽成稅費試算 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 符合5年以上PM與B2B經驗要求 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 16 個需求單位 | 近4年主責6.6萬家廠商招募系統 |
| HR03 | supported | 團隊 3 名企劃，直接向組織副總匯報 | 個人負責規格、驗收與跨單位排程 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 交付週期縮短與留存率具明確紀錄 |
| HR05 | supported | 盤點出上千組重複 E-mail，選擇首次登入引導確認 | 兼顧系統轉換與廠商使用連續性 |
| HR06 | supported | 從思維特助理PM、尚凡PM到1111企劃主任 | 職涯由C端成長型產品演進至B2B平台 |
| HR07 | supported | 寫成 PRD 與 Axure Prototype；和 QA 寫 UAT | 技能欄所列工具皆在經歷中有對應實作 |
| HR08 | supported | 依摘要、工作經歷、學歷、專業技能、自傳分段 | 結構清楚，重點與量化指標易讀 |
| HR09 | supported | 年化留存 81.2%，同期全站 74.2%（非因果） | 誠實標註觀察差異，無誇大矛盾 |
| HR10 | supported | 想在更早階段參與產品方向，從定義問題開始 | 轉職動機與資深PM職責高度相容 |
| HR11 | supported | 雙北、可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點與到職時間無衝突 |
| HR12 | supported | 具B2B大模組交付、登入防冒用與AI工作流實績 | 證據充分，強烈建議安排面試 |
| HM01 | supported | 企業端招募系統全模組（約 6.6 萬家活躍付費廠商） | B2B招募系統全模組與雙邊平台經驗高度相關 |
| HM02 | supported | 廠商抱怨溝通管道中斷，信件與即時通整合排最前 | 工單痛點與配對排序查核展現問題拆解力 |
| HM03 | supported | 搜尋結果頁痛點改版排在職缺健檢之前 | 信件整合與搜尋改版排序及首登引導取捨清晰 |
| HM04 | supported | 馬來西亞 iOS 三階段定價實驗；網頁付款占八成 | 定價實驗、點數付費牆與網頁金流具商業敏銳度 |
| HM05 | supported | 處理週期 100.4 降至 30.9 天；留存為觀察差異 | 處理週期縮短與留存率具量化紀錄，標明非因果 |
| HM06 | supported | 與 16 個需求單位對接，直接向組織副總匯報 | 對接16單位、帶3名企劃並直報副總，權責明確 |
| HM07 | supported | 2025/10 離峰切換停機 1.5 小時；上線簽章驗證 | 離峰切換停機1.5小時與簽章驗證展現交付風控 |
| HM08 | supported | 與資料科學團隊上線 3 項 AI 功能；具 AWS 證照 | 與DS合作3項AI功能並具AWS證照，協作順暢 |
| HM09 | supported | 主導約 50 項大項功能上線，細項 111 項 | 主導50大項功能與6.6萬廠商系統，符合資深範圍 |
| HM10 | supported | 清楚交代問題背景、個人行動、結果與非因果限制 | 結構清楚，重點成果與限制條件易於檢索 |
| HM11 | supported | 依客服測試回饋調整規則；還原原價後全面調降 | 依客服測試回饋調整AI規則，具迭代修正機制 |
| HM12 | supported | 登入簽章驗證、AI推薦規則、定價實驗具追問價值 | 防冒用架構、AI工作流與定價細節值得面試深挖 |
| HM13 | supported | 全項判讀均對齊職缺條件與履歷原文，未推測空窗 | 依職缺標準客觀取證，無不當推論 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 主導1111企業招募系統50大項功能與16單位協調，符合50%專案交付與跨部門要求 |
| 2 | 統籌2026/04廠商帳號遭冒用危機並上線簽章驗證，具防詐與資安實戰經驗 |
| 3 | 深度運用Claude Code建置工作流並與DS團隊落地3項AI功能，符合AI工具整合條件 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 海外7國經驗為B2C社交App，缺乏直接面向海外B2B企業或政府機關客戶之交付案例 | 過去在SweetRing與CodaPay的海外經驗，如何轉移至東南亞或日韓B2B企業客戶需求收集？ |
| 2 | 數據工具列GA4、Excel與對照實驗，未明文記載獨立撰寫SQL或BI儀表板查詢 | 在1111分析1,857張需求單與名冊留存時，是否親自使用SQL撈取資料？ |
| 3 | 防詐經驗集中於登入簽章驗證，需於面試確認對通訊防詐與風險偵測模型之理解深度 | 2026/04廠商帳號冒用事件中，攻擊途徑為何？簽章驗證在架構上如何設計與驗收？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜主導約 50 項大項功能上線｜展現大型B2B系統穩定交付力
- 1111經歷與自傳｜信件整合排新功能前、查出配對依修改日排序｜決策取捨具體生動
- 專業技能｜自建 Claude Code 協作流程（12條分工、23個skill）｜AI整合深入

**可改進（≤5 點）**：
- 位置：尚凡經歷
  - 原句：降價期 DAU +48%、非續訂營收相對對照組多約 28%
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：未交代各期天數及iOS/Android各自基期漲跌，易生口徑疑問
  - 建議方向：補充實驗天數與對照組各別增減百分比
- 位置：1111經歷
  - 原句：需求流程服務過的 1,279 家付費廠商，年化留存 81.2%
  - 問題類型：measurement
  - 嚴重度：editorial
  - 影響：未標示1,279家占全站活躍廠商之比例
  - 建議方向：補註占全站活躍付費廠商之比例
- 位置：1111經歷
  - 原句：統籌登入系統全面盤點，改用簽章驗證，之後未再發生
  - 問題類型：measurement
  - 嚴重度：editorial
  - 影響：未載明上線日期與後續觀察時間長度
  - 建議方向：補充上線具體日期與觀察截止月份

**編輯附件**（語氣、用詞微調；不影響判斷）：可於技能欄明確標示SQL/BI熟練度，並補充專案管理工具名稱（如Jira）

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 8.1｜第 2 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_8.1","job_id":"104_950oe_Gogolook_Senior_PM","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-8.1-02","human_calibrated":false,"requirements":[{"id":"R01","text":"5-8年以上B2B/B2G產品或專案管理經驗","type":"required","status":"supported","evidence":["Product Owner／PM｜1111 全球華人｜2022/08 - 迄今"],"blocks_interview":false,"reason":"近10年PM，企業招募系統PO近4年"},{"id":"R02","text":"接近母語等級英語口說與書寫","type":"required","status":"supported","evidence":["英文（TOEIC 980、TOEFL iBT 93）"],"blocks_interview":false,"reason":"高分英檢與美國交換及翻譯實務"},{"id":"R03","text":"優異的溝通與關係人管理能力","type":"required","status":"supported","evidence":["與工程、行銷、業務等 16 個需求單位對接"],"blocks_interview":false,"reason":"跨16單位協調並直接向副總匯報"},{"id":"R04","text":"扎實產品管理基礎（PRD/路線圖/風險控管）","type":"required","status":"supported","evidence":["主導約 50 項大項功能上線，從 PRD 到 UAT"],"blocks_interview":false,"reason":"完整涵蓋需求分析、規格與上線驗收"},{"id":"R05","text":"強烈的數據敏感度（SQL/BI/試算表分析）","type":"required","status":"partial","evidence":["數據分析（GA4、世代分析、對照組實驗）"],"blocks_interview":false,"reason":"具試算與實驗分析，未明載SQL與BI工具"},{"id":"R06","text":"熟悉AI工具與工作流整合","type":"required","status":"supported","evidence":["自建 Claude Code 協作流程（12條分工、23個skill）"],"blocks_interview":false,"reason":"建置AI協作工作流並落地3項AI功能"},{"id":"R07","text":"對防詐與風險偵測有真正熱情","type":"required","status":"supported","evidence":["十多家廠商帳號遭冒用，統籌登入系統全面盤點"],"blocks_interview":false,"reason":"具防冒用安全盤點與簽章驗證實績"},{"id":"R08","text":"具防詐、資安、風險管理或信任類產品經驗","type":"preferred","status":"supported","evidence":["改用簽章驗證，之後未再發生"],"blocks_interview":false,"reason":"實際處理企業帳號冒用並完成技術防護"},{"id":"R09","text":"曾服務企業客戶或政府機關，尤其海外市場","type":"preferred","status":"partial","evidence":["完成 SweetRing 美、墨、巴、印、馬、日、韓7市場在地化"],"blocks_interview":false,"reason":"具海外7國B2C與台灣B2B，缺海外B2B客戶"},{"id":"R10","text":"技術背景或曾與RD/AI團隊密切合作","type":"preferred","status":"supported","evidence":["與資料科學團隊上線 3 項 AI 功能"],"blocks_interview":false,"reason":"與工程及資料科學團隊密切協作並具AWS證照"},{"id":"R11","text":"具Agile/Scrum與Jira專案管理經驗","type":"preferred","status":"supported","evidence":["瀑布開發搭配 Kanban 與 Daily stand-up"],"blocks_interview":false,"reason":"具Kanban、站會與回顧實務，未明列Jira字樣"},{"id":"R12","text":"具產品定價、報價或成本利潤分析經驗","type":"preferred","status":"supported","evidence":["設計馬來西亞 iOS 三階段定價實驗...實收試算"],"blocks_interview":false,"reason":"具三階段定價實驗與跨國金流抽成稅費試算"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["企業端招募系統全模組（近 6.6 萬家活躍付費廠商）"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"強","evidence":["主導約 50 項大項功能上線，細項 111 項"],"missing":["未明列SQL與Jira工具字樣"],"issue_ids":[]},{"id":"decision_depth","rating":"強","evidence":["信件與即時通整合排在其他新功能之前"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"足夠","evidence":["需求平均處理週期從 100.4 天降到 30.9 天"],"missing":["定價實驗缺天數與基期拆解；留存缺全站分母占比"],"issue_ids":["I01","I02","I03"]},{"id":"ownership","rating":"強","evidence":["團隊 3 名企劃，直接向組織副總匯報"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["段落清晰，專案交付脈絡與數據易於檢索"],"missing":[],"issue_ids":[]}],"results":[{"quote":"需求平均處理週期從 100.4 天降到 30.9 天","kinds":["outcome"]},{"quote":"2026 年截至 9 月累計 1,857 張，完成 1,726 張","kinds":["output"]},{"quote":"年化留存 81.2%，同期全站 74.2%（觀察差異）","kinds":["outcome","context"]},{"quote":"降價期 DAU +48%、非續訂營收相對多約 28%","kinds":["outcome"]},{"quote":"Peach 網頁付款占比 24% → 八成以上","kinds":["outcome"]},{"quote":"2025/10 離峰切換上線，停機約 1.5 小時","kinds":["output","context"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"符合5年以上PM與B2B經驗要求"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 16 個需求單位"],"application_note":"近4年主責6.6萬家廠商招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["團隊 3 名企劃，直接向組織副總匯報"],"application_note":"個人負責規格、驗收與跨單位排程"},{"rule_id":"HR04","status":"supported","resume_evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"application_note":"交付週期縮短與留存率具明確紀錄"},{"rule_id":"HR05","status":"supported","resume_evidence":["盤點出上千組重複 E-mail，選擇首次登入引導確認"],"application_note":"兼顧系統轉換與廠商使用連續性"},{"rule_id":"HR06","status":"supported","resume_evidence":["從思維特助理PM、尚凡PM到1111企劃主任"],"application_note":"職涯由C端成長型產品演進至B2B平台"},{"rule_id":"HR07","status":"supported","resume_evidence":["寫成 PRD 與 Axure Prototype；和 QA 寫 UAT"],"application_note":"技能欄所列工具皆在經歷中有對應實作"},{"rule_id":"HR08","status":"supported","resume_evidence":["依摘要、工作經歷、學歷、專業技能、自傳分段"],"application_note":"結構清楚，重點與量化指標易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["年化留存 81.2%，同期全站 74.2%（非因果）"],"application_note":"誠實標註觀察差異，無誇大矛盾"},{"rule_id":"HR10","status":"supported","resume_evidence":["想在更早階段參與產品方向，從定義問題開始"],"application_note":"轉職動機與資深PM職責高度相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["雙北、可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點與到職時間無衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["具B2B大模組交付、登入防冒用與AI工作流實績"],"application_note":"證據充分，強烈建議安排面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["企業端招募系統全模組（約 6.6 萬家活躍付費廠商）"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["廠商抱怨溝通管道中斷，信件與即時通整合排最前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁痛點改版排在職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["馬來西亞 iOS 三階段定價實驗；網頁付款占八成"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"supported","resume_evidence":["處理週期 100.4 降至 30.9 天；留存為觀察差異"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["與 16 個需求單位對接，直接向組織副總匯報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["2025/10 離峰切換停機 1.5 小時；上線簽章驗證"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["與資料科學團隊上線 3 項 AI 功能；具 AWS 證照"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["主導約 50 項大項功能上線，細項 111 項"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["清楚交代問題背景、個人行動、結果與非因果限制"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依客服測試回饋調整規則；還原原價後全面調降"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["登入簽章驗證、AI推薦規則、定價實驗具追問價值"],"evidence_type":"context","source_ids":[],"interview_question":"請說明2026/04廠商帳號遭冒用之攻擊手法與簽章驗證架構細節"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["全項判讀均對齊職缺條件與履歷原文，未推測空窗"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HM05","source_ids":[],"application_note":"定價實驗缺實驗天數與基期拆解","context_limit":"尚凡經歷","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"降價期 DAU +48%、非續訂營收相對對照組多約 28%","reason":"未交代各期天數及iOS/Android各自基期漲跌，易生口徑疑問","suggestion":"補充實驗天數與對照組各別增減百分比"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"留存率缺全站母體分母占比","context_limit":"1111經歷","category":"measurement","severity":"editorial","block_target":null,"claim":"需求流程服務過的 1,279 家付費廠商，年化留存 81.2%","reason":"未標示1,279家占全站活躍廠商之比例","suggestion":"補註占全站活躍付費廠商之比例"},{"id":"I03","rule_id":"HM07","source_ids":[],"application_note":"防冒用簽章未標上線日與觀察期","context_limit":"1111經歷","category":"measurement","severity":"editorial","block_target":null,"claim":"統籌登入系統全面盤點，改用簽章驗證，之後未再發生","reason":"未載明上線日期與後續觀察時間長度","suggestion":"補充上線具體日期與觀察截止月份"}],"decision":{"recommendation":"interview","evidence":["主導約 50 項大項功能上線，具簽章驗證與 AI 實績"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["主導1111企業招募系統50大項功能與16單位協調，符合50%專案交付與跨部門要求","統籌2026/04廠商帳號遭冒用危機並上線簽章驗證，具防詐與資安實戰經驗","深度運用Claude Code建置工作流並與DS團隊落地3項AI功能，符合AI工具整合條件"],"key_gaps":["海外7國經驗為B2C社交App，缺乏直接面向海外B2B企業或政府機關客戶之交付案例","數據工具列GA4、Excel與對照實驗，未明文記載獨立撰寫SQL或BI儀表板查詢","防詐經驗集中於登入簽章驗證，需於面試確認對通訊防詐與風險偵測模型之理解深度"],"strengths":["1111經歷｜主導約 50 項大項功能上線｜展現大型B2B系統穩定交付力","1111經歷與自傳｜信件整合排新功能前、查出配對依修改日排序｜決策取捨具體生動","專業技能｜自建 Claude Code 協作流程（12條分工、23個skill）｜AI整合深入"],"interview_questions":["過去在SweetRing與CodaPay的海外經驗，如何轉移至東南亞或日韓B2B企業客戶需求收集？","在1111分析1,857張需求單與名冊留存時，是否親自使用SQL撈取資料？","2026/04廠商帳號冒用事件中，攻擊途徑為何？簽章驗證在架構上如何設計與驗收？","如何將Claude Code工作流與團隊既有專案管理工具（如Jira/Kanban）串接？"],"editorial_appendix":["可於技能欄明確標示SQL/BI熟練度，並補充專案管理工具名稱（如Jira）"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"具多個完整B2B交付與實驗案例支持面試，且有清楚取捨與衡量限制說明"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"not_tested","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「主導約 50 項大項功能上線」且具防冒用簽章驗證與 AI 協作實績，足以支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 企業端招募系統全模組（近 6.6 萬家活躍付費廠商） | 無關鍵缺口，可於面試深化 |
| role_evidence | 強 | 主導約 50 項大項功能上線，細項 111 項 | 未明列SQL與Jira工具字樣 |
| decision_depth | 強 | 信件與即時通整合排在其他新功能之前 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 足夠 | 需求平均處理週期從 100.4 天降到 30.9 天 | 定價實驗缺天數與基期拆解；留存缺全站分母占比 |
| ownership | 強 | 團隊 3 名企劃，直接向組織副總匯報 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 段落清晰，專案交付脈絡與數據易於檢索 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 5-8年以上B2B/B2G產品或專案管理經驗 | 必要 | supported | Product Owner／PM｜1111 全球華人｜2022/08 - 迄今 | 近10年PM，企業招募系統PO近4年 |
| R02 接近母語等級英語口說與書寫 | 必要 | supported | 英文（TOEIC 980、TOEFL iBT 93） | 高分英檢與美國交換及翻譯實務 |
| R03 優異的溝通與關係人管理能力 | 必要 | supported | 與工程、行銷、業務等 16 個需求單位對接 | 跨16單位協調並直接向副總匯報 |
| R04 扎實產品管理基礎（PRD/路線圖/風險控管） | 必要 | supported | 主導約 50 項大項功能上線，從 PRD 到 UAT | 完整涵蓋需求分析、規格與上線驗收 |
| R05 強烈的數據敏感度（SQL/BI/試算表分析） | 必要 | partial | 數據分析（GA4、世代分析、對照組實驗） | 具試算與實驗分析，未明載SQL與BI工具 |
| R06 熟悉AI工具與工作流整合 | 必要 | supported | 自建 Claude Code 協作流程（12條分工、23個skill） | 建置AI協作工作流並落地3項AI功能 |
| R07 對防詐與風險偵測有真正熱情 | 必要 | supported | 十多家廠商帳號遭冒用，統籌登入系統全面盤點 | 具防冒用安全盤點與簽章驗證實績 |
| R08 具防詐、資安、風險管理或信任類產品經驗 | 加分 | supported | 改用簽章驗證，之後未再發生 | 實際處理企業帳號冒用並完成技術防護 |
| R09 曾服務企業客戶或政府機關，尤其海外市場 | 加分 | partial | 完成 SweetRing 美、墨、巴、印、馬、日、韓7市場在地化 | 具海外7國B2C與台灣B2B，缺海外B2B客戶 |
| R10 技術背景或曾與RD/AI團隊密切合作 | 加分 | supported | 與資料科學團隊上線 3 項 AI 功能 | 與工程及資料科學團隊密切協作並具AWS證照 |
| R11 具Agile/Scrum與Jira專案管理經驗 | 加分 | supported | 瀑布開發搭配 Kanban 與 Daily stand-up | 具Kanban、站會與回顧實務，未明列Jira字樣 |
| R12 具產品定價、報價或成本利潤分析經驗 | 加分 | supported | 設計馬來西亞 iOS 三階段定價實驗...實收試算 | 具三階段定價實驗與跨國金流抽成稅費試算 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 符合5年以上PM與B2B經驗要求 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 16 個需求單位 | 近4年主責6.6萬家廠商招募系統 |
| HR03 | supported | 團隊 3 名企劃，直接向組織副總匯報 | 個人負責規格、驗收與跨單位排程 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 交付週期縮短與留存率具明確紀錄 |
| HR05 | supported | 盤點出上千組重複 E-mail，選擇首次登入引導確認 | 兼顧系統轉換與廠商使用連續性 |
| HR06 | supported | 從思維特助理PM、尚凡PM到1111企劃主任 | 職涯由C端成長型產品演進至B2B平台 |
| HR07 | supported | 寫成 PRD 與 Axure Prototype；和 QA 寫 UAT | 技能欄所列工具皆在經歷中有對應實作 |
| HR08 | supported | 依摘要、工作經歷、學歷、專業技能、自傳分段 | 結構清楚，重點與量化指標易讀 |
| HR09 | supported | 年化留存 81.2%，同期全站 74.2%（非因果） | 誠實標註觀察差異，無誇大矛盾 |
| HR10 | supported | 想在更早階段參與產品方向，從定義問題開始 | 轉職動機與資深PM職責高度相容 |
| HR11 | supported | 雙北、可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點與到職時間無衝突 |
| HR12 | supported | 具B2B大模組交付、登入防冒用與AI工作流實績 | 證據充分，強烈建議安排面試 |
| HM01 | supported | 企業端招募系統全模組（約 6.6 萬家活躍付費廠商） | B2B招募系統全模組與雙邊平台經驗高度相關 |
| HM02 | supported | 廠商抱怨溝通管道中斷，信件與即時通整合排最前 | 工單痛點與配對排序查核展現問題拆解力 |
| HM03 | supported | 搜尋結果頁痛點改版排在職缺健檢之前 | 信件整合與搜尋改版排序及首登引導取捨清晰 |
| HM04 | supported | 馬來西亞 iOS 三階段定價實驗；網頁付款占八成 | 定價實驗、點數付費牆與網頁金流具商業敏銳度 |
| HM05 | supported | 處理週期 100.4 降至 30.9 天；留存為觀察差異 | 處理週期縮短與留存率具量化紀錄，標明非因果 |
| HM06 | supported | 與 16 個需求單位對接，直接向組織副總匯報 | 對接16單位、帶3名企劃並直報副總，權責明確 |
| HM07 | supported | 2025/10 離峰切換停機 1.5 小時；上線簽章驗證 | 離峰切換停機1.5小時與簽章驗證展現交付風控 |
| HM08 | supported | 與資料科學團隊上線 3 項 AI 功能；具 AWS 證照 | 與DS合作3項AI功能並具AWS證照，協作順暢 |
| HM09 | supported | 主導約 50 項大項功能上線，細項 111 項 | 主導50大項功能與6.6萬廠商系統，符合資深範圍 |
| HM10 | supported | 清楚交代問題背景、個人行動、結果與非因果限制 | 結構清楚，重點成果與限制條件易於檢索 |
| HM11 | supported | 依客服測試回饋調整規則；還原原價後全面調降 | 依客服測試回饋調整AI規則，具迭代修正機制 |
| HM12 | supported | 登入簽章驗證、AI推薦規則、定價實驗具追問價值 | 防冒用架構、AI工作流與定價細節值得面試深挖 |
| HM13 | supported | 全項判讀均對齊職缺條件與履歷原文，未推測空窗 | 依職缺標準客觀取證，無不當推論 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 主導1111企業招募系統50大項功能與16單位協調，符合50%專案交付與跨部門要求 |
| 2 | 統籌2026/04廠商帳號遭冒用危機並上線簽章驗證，具防詐與資安實戰經驗 |
| 3 | 深度運用Claude Code建置工作流並與DS團隊落地3項AI功能，符合AI工具整合條件 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 海外7國經驗為B2C社交App，缺乏直接面向海外B2B企業或政府機關客戶之交付案例 | 過去在SweetRing與CodaPay的海外經驗，如何轉移至東南亞或日韓B2B企業客戶需求收集？ |
| 2 | 數據工具列GA4、Excel與對照實驗，未明文記載獨立撰寫SQL或BI儀表板查詢 | 在1111分析1,857張需求單與名冊留存時，是否親自使用SQL撈取資料？ |
| 3 | 防詐經驗集中於登入簽章驗證，需於面試確認對通訊防詐與風險偵測模型之理解深度 | 2026/04廠商帳號冒用事件中，攻擊途徑為何？簽章驗證在架構上如何設計與驗收？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜主導約 50 項大項功能上線｜展現大型B2B系統穩定交付力
- 1111經歷與自傳｜信件整合排新功能前、查出配對依修改日排序｜決策取捨具體生動
- 專業技能｜自建 Claude Code 協作流程（12條分工、23個skill）｜AI整合深入

**可改進（≤5 點）**：
- 位置：尚凡經歷
  - 原句：降價期 DAU +48%、非續訂營收相對對照組多約 28%
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：未交代各期天數及iOS/Android各自基期漲跌，易生口徑疑問
  - 建議方向：補充實驗天數與對照組各別增減百分比
- 位置：1111經歷
  - 原句：需求流程服務過的 1,279 家付費廠商，年化留存 81.2%
  - 問題類型：measurement
  - 嚴重度：editorial
  - 影響：未標示1,279家占全站活躍廠商之比例
  - 建議方向：補註占全站活躍付費廠商之比例
- 位置：1111經歷
  - 原句：統籌登入系統全面盤點，改用簽章驗證，之後未再發生
  - 問題類型：measurement
  - 嚴重度：editorial
  - 影響：未載明上線日期與後續觀察時間長度
  - 建議方向：補充上線具體日期與觀察截止月份

**編輯附件**（語氣、用詞微調；不影響判斷）：可於技能欄明確標示SQL/BI熟練度，並補充專案管理工具名稱（如Jira）

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 8.1｜第 3 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_8.1","job_id":"104_950oe_Gogolook_Senior_PM","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-8.1-03","human_calibrated":false,"requirements":[{"id":"R01","text":"5-8年以上B2B/B2G產品或專案管理經驗","type":"required","status":"supported","evidence":["Product Owner／PM｜1111 全球華人｜2022/08 - 迄今"],"blocks_interview":false,"reason":"近10年PM，企業招募系統PO近4年"},{"id":"R02","text":"接近母語等級英語口說與書寫","type":"required","status":"supported","evidence":["英文（TOEIC 980、TOEFL iBT 93）"],"blocks_interview":false,"reason":"高分英檢與美國交換及翻譯實務"},{"id":"R03","text":"優異的溝通與關係人管理能力","type":"required","status":"supported","evidence":["與工程、行銷、業務等 16 個需求單位對接"],"blocks_interview":false,"reason":"跨16單位協調並直接向副總匯報"},{"id":"R04","text":"扎實產品管理基礎（PRD/路線圖/風險控管）","type":"required","status":"supported","evidence":["主導約 50 項大項功能上線，從 PRD 到 UAT"],"blocks_interview":false,"reason":"完整涵蓋需求分析、規格與上線驗收"},{"id":"R05","text":"強烈的數據敏感度（SQL/BI/試算表分析）","type":"required","status":"partial","evidence":["數據分析（GA4、世代分析、對照組實驗）"],"blocks_interview":false,"reason":"具試算與實驗分析，未明載SQL與BI工具"},{"id":"R06","text":"熟悉AI工具與工作流整合","type":"required","status":"supported","evidence":["自建 Claude Code 協作流程（12條分工、23個skill）"],"blocks_interview":false,"reason":"建置AI協作工作流並落地3項AI功能"},{"id":"R07","text":"對防詐與風險偵測有真正熱情","type":"required","status":"supported","evidence":["十多家廠商帳號遭冒用，統籌登入系統全面盤點"],"blocks_interview":false,"reason":"具防冒用安全盤點與簽章驗證實績"},{"id":"R08","text":"具防詐、資安、風險管理或信任類產品經驗","type":"preferred","status":"supported","evidence":["改用簽章驗證，之後未再發生"],"blocks_interview":false,"reason":"實際處理企業帳號冒用並完成技術防護"},{"id":"R09","text":"曾服務企業客戶或政府機關，尤其海外市場","type":"preferred","status":"partial","evidence":["完成 SweetRing 美、墨、巴、印、馬、日、韓7市場在地化"],"blocks_interview":false,"reason":"具海外7國B2C與台灣B2B，缺海外B2B客戶"},{"id":"R10","text":"技術背景或曾與RD/AI團隊密切合作","type":"preferred","status":"supported","evidence":["與資料科學團隊上線 3 項 AI 功能"],"blocks_interview":false,"reason":"與工程及資料科學團隊密切協作並具AWS證照"},{"id":"R11","text":"具Agile/Scrum與Jira專案管理經驗","type":"preferred","status":"supported","evidence":["瀑布開發搭配 Kanban 與 Daily stand-up"],"blocks_interview":false,"reason":"具Kanban、站會與回顧實務，未明列Jira字樣"},{"id":"R12","text":"具產品定價、報價或成本利潤分析經驗","type":"preferred","status":"supported","evidence":["設計馬來西亞 iOS 三階段定價實驗...實收試算"],"blocks_interview":false,"reason":"具三階段定價實驗與跨國金流抽成稅費試算"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["企業端招募系統全模組（近 6.6 萬家活躍付費廠商）"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"強","evidence":["主導約 50 項大項功能上線，細項 111 項"],"missing":["未明列SQL與Jira工具字樣"],"issue_ids":[]},{"id":"decision_depth","rating":"強","evidence":["信件與即時通整合排在其他新功能之前"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"足夠","evidence":["需求平均處理週期從 100.4 天降到 30.9 天"],"missing":["定價實驗缺天數與基期拆解；留存缺全站分母占比"],"issue_ids":["I01","I02","I03"]},{"id":"ownership","rating":"強","evidence":["團隊 3 名企劃，直接向組織副總匯報"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["段落清晰，專案交付脈絡與數據易於檢索"],"missing":[],"issue_ids":[]}],"results":[{"quote":"需求平均處理週期從 100.4 天降到 30.9 天","kinds":["outcome"]},{"quote":"2026 年截至 9 月累計 1,857 張，完成 1,726 張","kinds":["output"]},{"quote":"年化留存 81.2%，同期全站 74.2%（觀察差異）","kinds":["outcome","context"]},{"quote":"降價期 DAU +48%、非續訂營收相對多約 28%","kinds":["outcome"]},{"quote":"Peach 網頁付款占比 24% → 八成以上","kinds":["outcome"]},{"quote":"2025/10 離峰切換上線，停機約 1.5 小時","kinds":["output","context"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"符合5年以上PM與B2B經驗要求"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 16 個需求單位"],"application_note":"近4年主責6.6萬家廠商招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["團隊 3 名企劃，直接向組織副總匯報"],"application_note":"個人負責規格、驗收與跨單位排程"},{"rule_id":"HR04","status":"supported","resume_evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"application_note":"交付週期縮短與留存率具明確紀錄"},{"rule_id":"HR05","status":"supported","resume_evidence":["盤點出上千組重複 E-mail，選擇首次登入引導確認"],"application_note":"兼顧系統轉換與廠商使用連續性"},{"rule_id":"HR06","status":"supported","resume_evidence":["從思維特助理PM、尚凡PM到1111企劃主任"],"application_note":"職涯由C端成長型產品演進至B2B平台"},{"rule_id":"HR07","status":"supported","resume_evidence":["寫成 PRD 與 Axure Prototype；和 QA 寫 UAT"],"application_note":"技能欄所列工具皆在經歷中有對應實作"},{"rule_id":"HR08","status":"supported","resume_evidence":["依摘要、工作經歷、學歷、專業技能、自傳分段"],"application_note":"結構清楚，重點與量化指標易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["年化留存 81.2%，同期全站 74.2%（非因果）"],"application_note":"誠實標註觀察差異，無誇大矛盾"},{"rule_id":"HR10","status":"supported","resume_evidence":["想在更早階段參與產品方向，從定義問題開始"],"application_note":"轉職動機與資深PM職責高度相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["雙北、可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點與到職時間無衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["具B2B大模組交付、登入防冒用與AI工作流實績"],"application_note":"證據充分，強烈建議安排面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["企業端招募系統全模組（約 6.6 萬家活躍付費廠商）"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["廠商抱怨溝通管道中斷，信件與即時通整合排最前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["搜尋結果頁痛點改版排在職缺健檢之前"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["馬來西亞 iOS 三階段定價實驗；網頁付款占八成"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"supported","resume_evidence":["處理週期 100.4 降至 30.9 天；留存為觀察差異"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["與 16 個需求單位對接，直接向組織副總匯報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["2025/10 離峰切換停機 1.5 小時；上線簽章驗證"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["與資料科學團隊上線 3 項 AI 功能；具 AWS 證照"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["主導約 50 項大項功能上線，細項 111 項"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["清楚交代問題背景、個人行動、結果與非因果限制"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依客服測試回饋調整規則；還原原價後全面調降"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["登入簽章驗證、AI推薦規則、定價實驗具追問價值"],"evidence_type":"context","source_ids":[],"interview_question":"請說明2026/04廠商帳號遭冒用之攻擊手法與簽章驗證架構細節"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["全項判讀均對齊職缺條件與履歷原文，未推測空窗"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HM05","source_ids":[],"application_note":"定價實驗缺實驗天數與基期拆解","context_limit":"尚凡經歷","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"降價期 DAU +48%、非續訂營收相對對照組多約 28%","reason":"未交代各期天數及iOS/Android各自基期漲跌，易生口徑疑問","suggestion":"補充實驗天數與對照組各別增減百分比"},{"id":"I02","rule_id":"HM05","source_ids":[],"application_note":"留存率缺全站母體分母占比","context_limit":"1111經歷","category":"measurement","severity":"editorial","block_target":null,"claim":"需求流程服務過的 1,279 家付費廠商，年化留存 81.2%","reason":"未標示1,279家占全站活躍廠商之比例","suggestion":"補註占全站活躍付費廠商之比例"},{"id":"I03","rule_id":"HM07","source_ids":[],"application_note":"防冒用簽章未標上線日與觀察期","context_limit":"1111經歷","category":"measurement","severity":"editorial","block_target":null,"claim":"統籌登入系統全面盤點，改用簽章驗證，之後未再發生","reason":"未載明上線日期與後續觀察時間長度","suggestion":"補充上線具體日期與觀察截止月份"}],"decision":{"recommendation":"interview","evidence":["主導約 50 項大項功能上線，具簽章驗證與 AI 實績"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["主導1111企業招募系統50大項功能與16單位協調，符合50%專案交付與跨部門要求","統籌2026/04廠商帳號遭冒用危機並上線簽章驗證，具防詐與資安實戰經驗","深度運用Claude Code建置工作流並與DS團隊落地3項AI功能，符合AI工具整合條件"],"key_gaps":["海外7國經驗為B2C社交App，缺乏直接面向海外B2B企業或政府機關客戶之交付案例","數據工具列GA4、Excel與對照實驗，未明文記載獨立撰寫SQL或BI儀表板查詢","防詐經驗集中於登入簽章驗證，需於面試確認對通訊防詐與風險偵測模型之理解深度"],"strengths":["1111經歷｜主導約 50 項大項功能上線｜展現大型B2B系統穩定交付力","1111經歷與自傳｜信件整合排新功能前、查出配對依修改日排序｜決策取捨具體生動","專業技能｜自建 Claude Code 協作流程（12條分工、23個skill）｜AI整合深入"],"interview_questions":["過去在SweetRing與CodaPay的海外經驗，如何轉移至東南亞或日韓B2B企業客戶需求收集？","在1111分析1,857張需求單與名冊留存時，是否親自使用SQL撈取資料？","2026/04廠商帳號冒用事件中，攻擊途徑為何？簽章驗證在架構上如何設計與驗收？","如何將Claude Code工作流與團隊既有專案管理工具（如Jira/Kanban）串接？"],"editorial_appendix":["可於技能欄明確標示SQL/BI熟練度，並補充專案管理工具名稱（如Jira）"],"spectrum":{"level":7,"uncertainty_levels":1,"basis":"具多個完整B2B交付與實驗案例支持面試，且有清楚取捨與衡量限制說明"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"not_tested","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：7（±1）
- 一句話理由：「主導約 50 項大項功能上線」且具防冒用簽章驗證與 AI 協作實績，足以支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 企業端招募系統全模組（近 6.6 萬家活躍付費廠商） | 無關鍵缺口，可於面試深化 |
| role_evidence | 強 | 主導約 50 項大項功能上線，細項 111 項 | 未明列SQL與Jira工具字樣 |
| decision_depth | 強 | 信件與即時通整合排在其他新功能之前 | 無關鍵缺口，可於面試深化 |
| outcome_quality | 足夠 | 需求平均處理週期從 100.4 天降到 30.9 天 | 定價實驗缺天數與基期拆解；留存缺全站分母占比 |
| ownership | 強 | 團隊 3 名企劃，直接向組織副總匯報 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 段落清晰，專案交付脈絡與數據易於檢索 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 5-8年以上B2B/B2G產品或專案管理經驗 | 必要 | supported | Product Owner／PM｜1111 全球華人｜2022/08 - 迄今 | 近10年PM，企業招募系統PO近4年 |
| R02 接近母語等級英語口說與書寫 | 必要 | supported | 英文（TOEIC 980、TOEFL iBT 93） | 高分英檢與美國交換及翻譯實務 |
| R03 優異的溝通與關係人管理能力 | 必要 | supported | 與工程、行銷、業務等 16 個需求單位對接 | 跨16單位協調並直接向副總匯報 |
| R04 扎實產品管理基礎（PRD/路線圖/風險控管） | 必要 | supported | 主導約 50 項大項功能上線，從 PRD 到 UAT | 完整涵蓋需求分析、規格與上線驗收 |
| R05 強烈的數據敏感度（SQL/BI/試算表分析） | 必要 | partial | 數據分析（GA4、世代分析、對照組實驗） | 具試算與實驗分析，未明載SQL與BI工具 |
| R06 熟悉AI工具與工作流整合 | 必要 | supported | 自建 Claude Code 協作流程（12條分工、23個skill） | 建置AI協作工作流並落地3項AI功能 |
| R07 對防詐與風險偵測有真正熱情 | 必要 | supported | 十多家廠商帳號遭冒用，統籌登入系統全面盤點 | 具防冒用安全盤點與簽章驗證實績 |
| R08 具防詐、資安、風險管理或信任類產品經驗 | 加分 | supported | 改用簽章驗證，之後未再發生 | 實際處理企業帳號冒用並完成技術防護 |
| R09 曾服務企業客戶或政府機關，尤其海外市場 | 加分 | partial | 完成 SweetRing 美、墨、巴、印、馬、日、韓7市場在地化 | 具海外7國B2C與台灣B2B，缺海外B2B客戶 |
| R10 技術背景或曾與RD/AI團隊密切合作 | 加分 | supported | 與資料科學團隊上線 3 項 AI 功能 | 與工程及資料科學團隊密切協作並具AWS證照 |
| R11 具Agile/Scrum與Jira專案管理經驗 | 加分 | supported | 瀑布開發搭配 Kanban 與 Daily stand-up | 具Kanban、站會與回顧實務，未明列Jira字樣 |
| R12 具產品定價、報價或成本利潤分析經驗 | 加分 | supported | 設計馬來西亞 iOS 三階段定價實驗...實收試算 | 具三階段定價實驗與跨國金流抽成稅費試算 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 符合5年以上PM與B2B經驗要求 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 16 個需求單位 | 近4年主責6.6萬家廠商招募系統 |
| HR03 | supported | 團隊 3 名企劃，直接向組織副總匯報 | 個人負責規格、驗收與跨單位排程 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 交付週期縮短與留存率具明確紀錄 |
| HR05 | supported | 盤點出上千組重複 E-mail，選擇首次登入引導確認 | 兼顧系統轉換與廠商使用連續性 |
| HR06 | supported | 從思維特助理PM、尚凡PM到1111企劃主任 | 職涯由C端成長型產品演進至B2B平台 |
| HR07 | supported | 寫成 PRD 與 Axure Prototype；和 QA 寫 UAT | 技能欄所列工具皆在經歷中有對應實作 |
| HR08 | supported | 依摘要、工作經歷、學歷、專業技能、自傳分段 | 結構清楚，重點與量化指標易讀 |
| HR09 | supported | 年化留存 81.2%，同期全站 74.2%（非因果） | 誠實標註觀察差異，無誇大矛盾 |
| HR10 | supported | 想在更早階段參與產品方向，從定義問題開始 | 轉職動機與資深PM職責高度相容 |
| HR11 | supported | 雙北、可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點與到職時間無衝突 |
| HR12 | supported | 具B2B大模組交付、登入防冒用與AI工作流實績 | 證據充分，強烈建議安排面試 |
| HM01 | supported | 企業端招募系統全模組（約 6.6 萬家活躍付費廠商） | B2B招募系統全模組與雙邊平台經驗高度相關 |
| HM02 | supported | 廠商抱怨溝通管道中斷，信件與即時通整合排最前 | 工單痛點與配對排序查核展現問題拆解力 |
| HM03 | supported | 搜尋結果頁痛點改版排在職缺健檢之前 | 信件整合與搜尋改版排序及首登引導取捨清晰 |
| HM04 | supported | 馬來西亞 iOS 三階段定價實驗；網頁付款占八成 | 定價實驗、點數付費牆與網頁金流具商業敏銳度 |
| HM05 | supported | 處理週期 100.4 降至 30.9 天；留存為觀察差異 | 處理週期縮短與留存率具量化紀錄，標明非因果 |
| HM06 | supported | 與 16 個需求單位對接，直接向組織副總匯報 | 對接16單位、帶3名企劃並直報副總，權責明確 |
| HM07 | supported | 2025/10 離峰切換停機 1.5 小時；上線簽章驗證 | 離峰切換停機1.5小時與簽章驗證展現交付風控 |
| HM08 | supported | 與資料科學團隊上線 3 項 AI 功能；具 AWS 證照 | 與DS合作3項AI功能並具AWS證照，協作順暢 |
| HM09 | supported | 主導約 50 項大項功能上線，細項 111 項 | 主導50大項功能與6.6萬廠商系統，符合資深範圍 |
| HM10 | supported | 清楚交代問題背景、個人行動、結果與非因果限制 | 結構清楚，重點成果與限制條件易於檢索 |
| HM11 | supported | 依客服測試回饋調整規則；還原原價後全面調降 | 依客服測試回饋調整AI規則，具迭代修正機制 |
| HM12 | supported | 登入簽章驗證、AI推薦規則、定價實驗具追問價值 | 防冒用架構、AI工作流與定價細節值得面試深挖 |
| HM13 | supported | 全項判讀均對齊職缺條件與履歷原文，未推測空窗 | 依職缺標準客觀取證，無不當推論 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 主導1111企業招募系統50大項功能與16單位協調，符合50%專案交付與跨部門要求 |
| 2 | 統籌2026/04廠商帳號遭冒用危機並上線簽章驗證，具防詐與資安實戰經驗 |
| 3 | 深度運用Claude Code建置工作流並與DS團隊落地3項AI功能，符合AI工具整合條件 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 海外7國經驗為B2C社交App，缺乏直接面向海外B2B企業或政府機關客戶之交付案例 | 過去在SweetRing與CodaPay的海外經驗，如何轉移至東南亞或日韓B2B企業客戶需求收集？ |
| 2 | 數據工具列GA4、Excel與對照實驗，未明文記載獨立撰寫SQL或BI儀表板查詢 | 在1111分析1,857張需求單與名冊留存時，是否親自使用SQL撈取資料？ |
| 3 | 防詐經驗集中於登入簽章驗證，需於面試確認對通訊防詐與風險偵測模型之理解深度 | 2026/04廠商帳號冒用事件中，攻擊途徑為何？簽章驗證在架構上如何設計與驗收？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111經歷｜主導約 50 項大項功能上線｜展現大型B2B系統穩定交付力
- 1111經歷與自傳｜信件整合排新功能前、查出配對依修改日排序｜決策取捨具體生動
- 專業技能｜自建 Claude Code 協作流程（12條分工、23個skill）｜AI整合深入

**可改進（≤5 點）**：
- 位置：尚凡經歷
  - 原句：降價期 DAU +48%、非續訂營收相對對照組多約 28%
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：未交代各期天數及iOS/Android各自基期漲跌，易生口徑疑問
  - 建議方向：補充實驗天數與對照組各別增減百分比
- 位置：1111經歷
  - 原句：需求流程服務過的 1,279 家付費廠商，年化留存 81.2%
  - 問題類型：measurement
  - 嚴重度：editorial
  - 影響：未標示1,279家占全站活躍廠商之比例
  - 建議方向：補註占全站活躍付費廠商之比例
- 位置：1111經歷
  - 原句：統籌登入系統全面盤點，改用簽章驗證，之後未再發生
  - 問題類型：measurement
  - 嚴重度：editorial
  - 影響：未載明上線日期與後續觀察時間長度
  - 建議方向：補充上線具體日期與觀察截止月份

**編輯附件**（語氣、用詞微調；不影響判斷）：可於技能欄明確標示SQL/BI熟練度，並補充專案管理工具名稱（如Jira）

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

# 附錄：① 獨立審查 A 明細（9.4 版 × 3 輪）

## 單份審查｜履歷 9.4｜第 1 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_9.4","job_id":"104_950oe_Gogolook_Senior_PM","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-9.4-01","human_calibrated":false,"requirements":[{"id":"R01","text":"5-8年以上B2B/B2G產品或專案管理經驗","type":"required","status":"supported","evidence":["Product Owner／PM｜1111 全球華人｜2022/08 - 迄今"],"blocks_interview":false,"reason":"近10年PM，企業招募系統PO近4年"},{"id":"R02","text":"接近母語等級英語口說與書寫","type":"required","status":"supported","evidence":["英文 TOEIC 980、TOEFL iBT 93"],"blocks_interview":false,"reason":"高分英檢與美國交換及翻譯實務"},{"id":"R03","text":"優異的溝通與關係人管理能力","type":"required","status":"supported","evidence":["對接 16 個需求單位，依使用者旅程排優先級"],"blocks_interview":false,"reason":"跨16單位協調並直接向副總匯報"},{"id":"R04","text":"扎實產品管理基礎（PRD/路線圖/風險控管）","type":"required","status":"supported","evidence":["主責約 50 項大項功能規劃，掌握驗收與交付"],"blocks_interview":false,"reason":"完整涵蓋需求分析、規格與上線驗收"},{"id":"R05","text":"強烈的數據敏感度（SQL/BI/試算表分析）","type":"required","status":"partial","evidence":["GA4、世代分析、對照組實驗、Excel"],"blocks_interview":false,"reason":"具試算與實驗分析，未明載SQL與BI工具"},{"id":"R06","text":"熟悉AI工具與工作流整合","type":"required","status":"supported","evidence":["Claude Code 多分支流程與共用 skill 庫"],"blocks_interview":false,"reason":"建置AI協作工作流並落地3項AI功能"},{"id":"R07","text":"對防詐與風險偵測有真正熱情","type":"required","status":"supported","evidence":["登入安全盤點源於 2026/04 十多家廠商帳號遭冒用"],"blocks_interview":false,"reason":"具防冒用安全盤點與簽章驗證實績"},{"id":"R08","text":"具防詐、資安、風險管理或信任類產品經驗","type":"preferred","status":"supported","evidence":["與工程協作於 2026/04/17 上線簽章驗證"],"blocks_interview":false,"reason":"實際處理企業帳號冒用並完成技術防護"},{"id":"R09","text":"曾服務企業客戶或政府機關，尤其海外市場","type":"preferred","status":"partial","evidence":["SweetRing 在地化涵蓋美、墨、巴、印、馬、日、韓7市場"],"blocks_interview":false,"reason":"具海外7國B2C與台灣B2B，缺海外B2B客戶"},{"id":"R10","text":"技術背景或曾與RD/AI團隊密切合作","type":"preferred","status":"supported","evidence":["AI 功能已上線...與資料科學團隊合作"],"blocks_interview":false,"reason":"與工程及資料科學團隊密切協作並具AWS證照"},{"id":"R11","text":"具Agile/Scrum與Jira專案管理經驗","type":"preferred","status":"supported","evidence":["Kanban 搭配瀑布式開發、Daily stand-up"],"blocks_interview":false,"reason":"具Kanban、站會與回顧實務，未明列Jira字樣"},{"id":"R12","text":"具產品定價、報價或成本利潤分析經驗","type":"preferred","status":"supported","evidence":["定價實驗採原價、iOS 降價、還原原價三階段"],"blocks_interview":false,"reason":"具三階段定價實驗與跨國金流抽成稅費試算"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["全站活躍付費廠商約 6.6 萬家（2026/04/30）"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"強","evidence":["約 50 項大項功能上線，上線 111 項細項"],"missing":["未明列SQL與Jira工具字樣"],"issue_ids":["I02"]},{"id":"decision_depth","rating":"足夠","evidence":["選擇首次登入引導確認、不強迫修改"],"missing":["刪減了搜尋改版排序與配對規則修改細節"],"issue_ids":["I01"]},{"id":"outcome_quality","rating":"強","evidence":["管線觸及 1,279 家，約占全站 66,150 家 1.9%"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["團隊 3 名企劃，直接向組織副總匯報"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["段落清晰，專案交付脈絡與數據易於檢索"],"missing":[],"issue_ids":[]}],"results":[{"quote":"需求平均處理週期由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"截至 09/29，完成 1,726／1,857 張需求與問題單","kinds":["output"]},{"quote":"觸及 1,279 家活躍付費廠商，約占全站 1.9%","kinds":["context","outcome"]},{"quote":"iOS 非續訂營收增 5%，Android 減 18%，相對多 28%","kinds":["outcome"]},{"quote":"Peach 網頁付款占營收由 24% 至 80% 以上","kinds":["outcome"]},{"quote":"2026/04/17 上線簽章驗證，至 10 月未再出現冒用","kinds":["output","outcome"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"符合5年以上PM與B2B經驗要求"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 16 個需求單位"],"application_note":"近4年主責6.6萬家廠商招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["團隊 3 名企劃，直接向組織副總匯報"],"application_note":"個人負責規格、驗收與跨單位排程"},{"rule_id":"HR04","status":"supported","resume_evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"application_note":"交付週期縮短與留存率具明確紀錄"},{"rule_id":"HR05","status":"supported","resume_evidence":["盤點出上千組重複 E-mail，選擇首次登入引導確認"],"application_note":"兼顧系統轉換與廠商使用連續性"},{"rule_id":"HR06","status":"supported","resume_evidence":["從思維特助理PM、尚凡PM到1111企劃主任"],"application_note":"職涯由C端成長型產品演進至B2B平台"},{"rule_id":"HR07","status":"supported","resume_evidence":["寫成 PRD 與 Axure Prototype；和 QA 寫 UAT"],"application_note":"技能欄所列工具皆在經歷中有對應實作"},{"rule_id":"HR08","status":"supported","resume_evidence":["依摘要、工作經歷、學歷、專業技能、自傳分段"],"application_note":"結構清楚，重點與量化指標易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["年化留存 81.2%，同期全站 74.2%（非因果）"],"application_note":"誠實標註觀察差異，無誇大矛盾"},{"rule_id":"HR10","status":"supported","resume_evidence":["想在更早階段參與產品方向，從定義問題開始"],"application_note":"轉職動機與資深PM職責高度相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["雙北、可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點與到職時間無衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["具B2B大模組交付、登入防冒用與AI工作流實績"],"application_note":"證據充分，強烈建議安排面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["企業端招募系統全模組（約 6.6 萬家活躍付費廠商）"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程與工單問題排定優先級"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["選擇首次登入引導確認、不強迫修改"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["馬來西亞 iOS 三階段定價實驗；網頁付款占八成"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"supported","resume_evidence":["處理週期 100.4 降至 30.9 天；留存為觀察差異"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["與 16 個需求單位對接，直接向組織副總匯報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["2025/10 離峰切換停機 1.5 小時；上線簽章驗證"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["與資料科學團隊上線 3 項 AI 功能；具 AWS 證照"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["主導約 50 項大項功能上線，細項 111 項"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["清楚交代問題背景、個人行動、結果與非因果限制"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依客服測試回饋調整規則；還原原價後全面調降"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["登入簽章驗證、AI推薦規則、定價實驗具追問價值"],"evidence_type":"context","source_ids":[],"interview_question":"請說明2026/04廠商帳號遭冒用之攻擊手法與簽章驗證架構細節"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["全項判讀均對齊職缺條件與履歷原文，未推測空窗"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HM03","source_ids":[],"application_note":"刪減搜尋改版與配對排序決策案例","context_limit":"1111經歷與自傳","category":"readability","severity":"editorial","block_target":null,"claim":"依使用者旅程與工單問題排定優先級","reason":"較8.1版少了一組具體功能取捨與規則修改案例","suggestion":"可於面試或經歷中補回搜尋改版與配對排序實例"},{"id":"I02","rule_id":"HR01","source_ids":[],"application_note":"海外經驗屬B2C而非B2B企業客戶","context_limit":"思維特經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"SweetRing 在地化涵蓋美、墨、巴、印、馬、日、韓 7 市場","reason":"JD加分項偏好海外企業或政府客戶，此為C端產品","suggestion":"於面試強調跨國需求協調如何轉移至B2B場景"}],"decision":{"recommendation":"interview","evidence":["主導約 50 項大項功能上線，具簽章驗證與 AI 實績"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["主導1111企業招募系統50大項功能與16單位協調，符合50%專案交付與跨部門要求","統籌2026/04廠商帳號遭冒用危機並上線簽章驗證，具防詐與資安實戰經驗","深度運用Claude Code建置工作流並與DS團隊落地3項AI功能，符合AI工具整合條件"],"key_gaps":["海外7國經驗為B2C社交App，缺乏直接面向海外B2B企業或政府機關客戶之交付案例","數據工具列GA4、Excel與對照實驗，未明文記載獨立撰寫SQL或BI儀表板查詢","防詐經驗集中於登入簽章驗證，需於面試確認對通訊防詐與風險偵測模型之理解深度"],"strengths":["尚凡經歷｜定價實驗三階段（各期 21 天）iOS增5%、Android減18%｜衡量邊界極嚴謹","1111經歷｜2026/04/17 上線簽章驗證，至 2026/10 未再出現冒用｜資安交付閉環明確","專業摘要｜5 點結構化條列呈現核心成果與方法｜視覺掃描與資訊階層清晰"],"interview_questions":["過去在SweetRing與CodaPay的海外經驗，如何轉移至東南亞或日韓B2B企業客戶需求收集？","在1111分析1,857張需求單與名冊留存時，是否親自使用SQL撈取資料？","2026/04廠商帳號冒用事件中，攻擊途徑為何？簽章驗證在架構上如何設計與驗收？","如何將Claude Code工作流與團隊既有專案管理工具（如Jira/Kanban）串接？"],"editorial_appendix":["可於技能欄明確標示SQL/BI熟練度，並補充專案管理工具名稱（如Jira）"],"spectrum":{"level":7,"uncertainty_levels":1,"basis":"具多個完整B2B交付與實驗案例支持面試，且有清楚取捨與衡量限制說明"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"not_tested","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：7（±1）
- 一句話理由：「約 50 項大項功能上線」且「2026/04/17 上線簽章驗證」衡量與閉環嚴謹，支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 全站活躍付費廠商約 6.6 萬家（2026/04/30） | 無關鍵缺口，可於面試深化 |
| role_evidence | 強 | 約 50 項大項功能上線，上線 111 項細項 | 未明列SQL與Jira工具字樣 |
| decision_depth | 足夠 | 選擇首次登入引導確認、不強迫修改 | 刪減了搜尋改版排序與配對規則修改細節 |
| outcome_quality | 強 | 管線觸及 1,279 家，約占全站 66,150 家 1.9% | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 團隊 3 名企劃，直接向組織副總匯報 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 段落清晰，專案交付脈絡與數據易於檢索 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 5-8年以上B2B/B2G產品或專案管理經驗 | 必要 | supported | Product Owner／PM｜1111 全球華人｜2022/08 - 迄今 | 近10年PM，企業招募系統PO近4年 |
| R02 接近母語等級英語口說與書寫 | 必要 | supported | 英文 TOEIC 980、TOEFL iBT 93 | 高分英檢與美國交換及翻譯實務 |
| R03 優異的溝通與關係人管理能力 | 必要 | supported | 對接 16 個需求單位，依使用者旅程排優先級 | 跨16單位協調並直接向副總匯報 |
| R04 扎實產品管理基礎（PRD/路線圖/風險控管） | 必要 | supported | 主責約 50 項大項功能規劃，掌握驗收與交付 | 完整涵蓋需求分析、規格與上線驗收 |
| R05 強烈的數據敏感度（SQL/BI/試算表分析） | 必要 | partial | GA4、世代分析、對照組實驗、Excel | 具試算與實驗分析，未明載SQL與BI工具 |
| R06 熟悉AI工具與工作流整合 | 必要 | supported | Claude Code 多分支流程與共用 skill 庫 | 建置AI協作工作流並落地3項AI功能 |
| R07 對防詐與風險偵測有真正熱情 | 必要 | supported | 登入安全盤點源於 2026/04 十多家廠商帳號遭冒用 | 具防冒用安全盤點與簽章驗證實績 |
| R08 具防詐、資安、風險管理或信任類產品經驗 | 加分 | supported | 與工程協作於 2026/04/17 上線簽章驗證 | 實際處理企業帳號冒用並完成技術防護 |
| R09 曾服務企業客戶或政府機關，尤其海外市場 | 加分 | partial | SweetRing 在地化涵蓋美、墨、巴、印、馬、日、韓7市場 | 具海外7國B2C與台灣B2B，缺海外B2B客戶 |
| R10 技術背景或曾與RD/AI團隊密切合作 | 加分 | supported | AI 功能已上線...與資料科學團隊合作 | 與工程及資料科學團隊密切協作並具AWS證照 |
| R11 具Agile/Scrum與Jira專案管理經驗 | 加分 | supported | Kanban 搭配瀑布式開發、Daily stand-up | 具Kanban、站會與回顧實務，未明列Jira字樣 |
| R12 具產品定價、報價或成本利潤分析經驗 | 加分 | supported | 定價實驗採原價、iOS 降價、還原原價三階段 | 具三階段定價實驗與跨國金流抽成稅費試算 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 符合5年以上PM與B2B經驗要求 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 16 個需求單位 | 近4年主責6.6萬家廠商招募系統 |
| HR03 | supported | 團隊 3 名企劃，直接向組織副總匯報 | 個人負責規格、驗收與跨單位排程 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 交付週期縮短與留存率具明確紀錄 |
| HR05 | supported | 盤點出上千組重複 E-mail，選擇首次登入引導確認 | 兼顧系統轉換與廠商使用連續性 |
| HR06 | supported | 從思維特助理PM、尚凡PM到1111企劃主任 | 職涯由C端成長型產品演進至B2B平台 |
| HR07 | supported | 寫成 PRD 與 Axure Prototype；和 QA 寫 UAT | 技能欄所列工具皆在經歷中有對應實作 |
| HR08 | supported | 依摘要、工作經歷、學歷、專業技能、自傳分段 | 結構清楚，重點與量化指標易讀 |
| HR09 | supported | 年化留存 81.2%，同期全站 74.2%（非因果） | 誠實標註觀察差異，無誇大矛盾 |
| HR10 | supported | 想在更早階段參與產品方向，從定義問題開始 | 轉職動機與資深PM職責高度相容 |
| HR11 | supported | 雙北、可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點與到職時間無衝突 |
| HR12 | supported | 具B2B大模組交付、登入防冒用與AI工作流實績 | 證據充分，強烈建議安排面試 |
| HM01 | supported | 企業端招募系統全模組（約 6.6 萬家活躍付費廠商） | B2B招募系統全模組與雙邊平台經驗高度相關 |
| HM02 | supported | 依使用者旅程與工單問題排定優先級 | 依旅程與工單排優先級，具問題導向意識 |
| HM03 | supported | 選擇首次登入引導確認、不強迫修改 | 首登引導確認不強迫修改，兼顧轉換與體驗 |
| HM04 | supported | 馬來西亞 iOS 三階段定價實驗；網頁付款占八成 | 定價實驗、點數付費牆與網頁金流具商業敏銳度 |
| HM05 | supported | 處理週期 100.4 降至 30.9 天；留存為觀察差異 | 分母占比、實驗天數與基期變化拆解極為嚴謹 |
| HM06 | supported | 與 16 個需求單位對接，直接向組織副總匯報 | 對接16單位、帶3名企劃並直報副總，權責明確 |
| HM07 | supported | 2025/10 離峰切換停機 1.5 小時；上線簽章驗證 | 離峰切換停機1.5小時與簽章驗證展現交付風控 |
| HM08 | supported | 與資料科學團隊上線 3 項 AI 功能；具 AWS 證照 | 與DS合作3項AI功能並具AWS證照，協作順暢 |
| HM09 | supported | 主導約 50 項大項功能上線，細項 111 項 | 主導50大項功能與6.6萬廠商系統，符合資深範圍 |
| HM10 | supported | 清楚交代問題背景、個人行動、結果與非因果限制 | 結構清楚，重點成果與限制條件易於檢索 |
| HM11 | supported | 依客服測試回饋調整規則；還原原價後全面調降 | 依客服測試回饋調整AI規則，具迭代修正機制 |
| HM12 | supported | 登入簽章驗證、AI推薦規則、定價實驗具追問價值 | 防冒用架構、AI工作流與定價細節值得面試深挖 |
| HM13 | supported | 全項判讀均對齊職缺條件與履歷原文，未推測空窗 | 依職缺標準客觀取證，無不當推論 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 主導1111企業招募系統50大項功能與16單位協調，符合50%專案交付與跨部門要求 |
| 2 | 統籌2026/04廠商帳號遭冒用危機並上線簽章驗證，具防詐與資安實戰經驗 |
| 3 | 深度運用Claude Code建置工作流並與DS團隊落地3項AI功能，符合AI工具整合條件 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 海外7國經驗為B2C社交App，缺乏直接面向海外B2B企業或政府機關客戶之交付案例 | 過去在SweetRing與CodaPay的海外經驗，如何轉移至東南亞或日韓B2B企業客戶需求收集？ |
| 2 | 數據工具列GA4、Excel與對照實驗，未明文記載獨立撰寫SQL或BI儀表板查詢 | 在1111分析1,857張需求單與名冊留存時，是否親自使用SQL撈取資料？ |
| 3 | 防詐經驗集中於登入簽章驗證，需於面試確認對通訊防詐與風險偵測模型之理解深度 | 2026/04廠商帳號冒用事件中，攻擊途徑為何？簽章驗證在架構上如何設計與驗收？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 尚凡經歷｜定價實驗三階段（各期 21 天）iOS增5%、Android減18%｜衡量邊界極嚴謹
- 1111經歷｜2026/04/17 上線簽章驗證，至 2026/10 未再出現冒用｜資安交付閉環明確
- 專業摘要｜5 點結構化條列呈現核心成果與方法｜視覺掃描與資訊階層清晰

**可改進（≤5 點）**：
- 位置：1111經歷與自傳
  - 原句：依使用者旅程與工單問題排定優先級
  - 問題類型：readability
  - 嚴重度：editorial
  - 影響：較8.1版少了一組具體功能取捨與規則修改案例
  - 建議方向：可於面試或經歷中補回搜尋改版與配對排序實例
- 位置：思維特經歷
  - 原句：SweetRing 在地化涵蓋美、墨、巴、印、馬、日、韓 7 市場
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：JD加分項偏好海外企業或政府客戶，此為C端產品
  - 建議方向：於面試強調跨國需求協調如何轉移至B2B場景


**編輯附件**（語氣、用詞微調；不影響判斷）：可於技能欄明確標示SQL/BI熟練度，並補充專案管理工具名稱（如Jira）

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 9.4｜第 2 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_9.4","job_id":"104_950oe_Gogolook_Senior_PM","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-9.4-02","human_calibrated":false,"requirements":[{"id":"R01","text":"5-8年以上B2B/B2G產品或專案管理經驗","type":"required","status":"supported","evidence":["Product Owner／PM｜1111 全球華人｜2022/08 - 迄今"],"blocks_interview":false,"reason":"近10年PM，企業招募系統PO近4年"},{"id":"R02","text":"接近母語等級英語口說與書寫","type":"required","status":"supported","evidence":["英文 TOEIC 980、TOEFL iBT 93"],"blocks_interview":false,"reason":"高分英檢與美國交換及翻譯實務"},{"id":"R03","text":"優異的溝通與關係人管理能力","type":"required","status":"supported","evidence":["對接 16 個需求單位，依使用者旅程排優先級"],"blocks_interview":false,"reason":"跨16單位協調並直接向副總匯報"},{"id":"R04","text":"扎實產品管理基礎（PRD/路線圖/風險控管）","type":"required","status":"supported","evidence":["主責約 50 項大項功能規劃，掌握驗收與交付"],"blocks_interview":false,"reason":"完整涵蓋需求分析、規格與上線驗收"},{"id":"R05","text":"強烈的數據敏感度（SQL/BI/試算表分析）","type":"required","status":"partial","evidence":["GA4、世代分析、對照組實驗、Excel"],"blocks_interview":false,"reason":"具試算與實驗分析，未明載SQL與BI工具"},{"id":"R06","text":"熟悉AI工具與工作流整合","type":"required","status":"supported","evidence":["Claude Code 多分支流程與共用 skill 庫"],"blocks_interview":false,"reason":"建置AI協作工作流並落地3項AI功能"},{"id":"R07","text":"對防詐與風險偵測有真正熱情","type":"required","status":"supported","evidence":["登入安全盤點源於 2026/04 十多家廠商帳號遭冒用"],"blocks_interview":false,"reason":"具防冒用安全盤點與簽章驗證實績"},{"id":"R08","text":"具防詐、資安、風險管理或信任類產品經驗","type":"preferred","status":"supported","evidence":["與工程協作於 2026/04/17 上線簽章驗證"],"blocks_interview":false,"reason":"實際處理企業帳號冒用並完成技術防護"},{"id":"R09","text":"曾服務企業客戶或政府機關，尤其海外市場","type":"preferred","status":"partial","evidence":["SweetRing 在地化涵蓋美、墨、巴、印、馬、日、韓7市場"],"blocks_interview":false,"reason":"具海外7國B2C與台灣B2B，缺海外B2B客戶"},{"id":"R10","text":"技術背景或曾與RD/AI團隊密切合作","type":"preferred","status":"supported","evidence":["AI 功能已上線...與資料科學團隊合作"],"blocks_interview":false,"reason":"與工程及資料科學團隊密切協作並具AWS證照"},{"id":"R11","text":"具Agile/Scrum與Jira專案管理經驗","type":"preferred","status":"supported","evidence":["Kanban 搭配瀑布式開發、Daily stand-up"],"blocks_interview":false,"reason":"具Kanban、站會與回顧實務，未明列Jira字樣"},{"id":"R12","text":"具產品定價、報價或成本利潤分析經驗","type":"preferred","status":"supported","evidence":["定價實驗採原價、iOS 降價、還原原價三階段"],"blocks_interview":false,"reason":"具三階段定價實驗與跨國金流抽成稅費試算"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["全站活躍付費廠商約 6.6 萬家（2026/04/30）"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"強","evidence":["約 50 項大項功能上線，上線 111 項細項"],"missing":["未明列SQL與Jira工具字樣"],"issue_ids":["I02"]},{"id":"decision_depth","rating":"足夠","evidence":["選擇首次登入引導確認、不強迫修改"],"missing":["刪減了搜尋改版排序與配對規則修改細節"],"issue_ids":["I01"]},{"id":"outcome_quality","rating":"強","evidence":["管線觸及 1,279 家，約占全站 66,150 家 1.9%"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["團隊 3 名企劃，直接向組織副總匯報"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["段落清晰，專案交付脈絡與數據易於檢索"],"missing":[],"issue_ids":[]}],"results":[{"quote":"需求平均處理週期由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"截至 09/29，完成 1,726／1,857 張需求與問題單","kinds":["output"]},{"quote":"觸及 1,279 家活躍付費廠商，約占全站 1.9%","kinds":["context","outcome"]},{"quote":"iOS 非續訂營收增 5%，Android 減 18%，相對多 28%","kinds":["outcome"]},{"quote":"Peach 網頁付款占營收由 24% 至 80% 以上","kinds":["outcome"]},{"quote":"2026/04/17 上線簽章驗證，至 10 月未再出現冒用","kinds":["output","outcome"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"符合5年以上PM與B2B經驗要求"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 16 個需求單位"],"application_note":"近4年主責6.6萬家廠商招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["團隊 3 名企劃，直接向組織副總匯報"],"application_note":"個人負責規格、驗收與跨單位排程"},{"rule_id":"HR04","status":"supported","resume_evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"application_note":"交付週期縮短與留存率具明確紀錄"},{"rule_id":"HR05","status":"supported","resume_evidence":["盤點出上千組重複 E-mail，選擇首次登入引導確認"],"application_note":"兼顧系統轉換與廠商使用連續性"},{"rule_id":"HR06","status":"supported","resume_evidence":["從思維特助理PM、尚凡PM到1111企劃主任"],"application_note":"職涯由C端成長型產品演進至B2B平台"},{"rule_id":"HR07","status":"supported","resume_evidence":["寫成 PRD 與 Axure Prototype；和 QA 寫 UAT"],"application_note":"技能欄所列工具皆在經歷中有對應實作"},{"rule_id":"HR08","status":"supported","resume_evidence":["依摘要、工作經歷、學歷、專業技能、自傳分段"],"application_note":"結構清楚，重點與量化指標易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["年化留存 81.2%，同期全站 74.2%（非因果）"],"application_note":"誠實標註觀察差異，無誇大矛盾"},{"rule_id":"HR10","status":"supported","resume_evidence":["想在更早階段參與產品方向，從定義問題開始"],"application_note":"轉職動機與資深PM職責高度相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["雙北、可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點與到職時間無衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["具B2B大模組交付、登入防冒用與AI工作流實績"],"application_note":"證據充分，強烈建議安排面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["企業端招募系統全模組（約 6.6 萬家活躍付費廠商）"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程與工單問題排定優先級"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["選擇首次登入引導確認、不強迫修改"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["馬來西亞 iOS 三階段定價實驗；網頁付款占八成"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"supported","resume_evidence":["處理週期 100.4 降至 30.9 天；留存為觀察差異"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["與 16 個需求單位對接，直接向組織副總匯報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["2025/10 離峰切換停機 1.5 小時；上線簽章驗證"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["與資料科學團隊上線 3 項 AI 功能；具 AWS 證照"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["主導約 50 項大項功能上線，細項 111 項"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["清楚交代問題背景、個人行動、結果與非因果限制"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依客服測試回饋調整規則；還原原價後全面調降"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["登入簽章驗證、AI推薦規則、定價實驗具追問價值"],"evidence_type":"context","source_ids":[],"interview_question":"請說明2026/04廠商帳號遭冒用之攻擊手法與簽章驗證架構細節"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["全項判讀均對齊職缺條件與履歷原文，未推測空窗"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HM03","source_ids":[],"application_note":"刪減搜尋改版與配對排序決策案例","context_limit":"1111經歷與自傳","category":"readability","severity":"editorial","block_target":null,"claim":"依使用者旅程與工單問題排定優先級","reason":"較8.1版少了一組具體功能取捨與規則修改案例","suggestion":"可於面試或經歷中補回搜尋改版與配對排序實例"},{"id":"I02","rule_id":"HR01","source_ids":[],"application_note":"海外經驗屬B2C而非B2B企業客戶","context_limit":"思維特經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"SweetRing 在地化涵蓋美、墨、巴、印、馬、日、韓 7 市場","reason":"JD加分項偏好海外企業或政府客戶，此為C端產品","suggestion":"於面試強調跨國需求協調如何轉移至B2B場景"}],"decision":{"recommendation":"interview","evidence":["主導約 50 項大項功能上線，具簽章驗證與 AI 實績"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["主導1111企業招募系統50大項功能與16單位協調，符合50%專案交付與跨部門要求","統籌2026/04廠商帳號遭冒用危機並上線簽章驗證，具防詐與資安實戰經驗","深度運用Claude Code建置工作流並與DS團隊落地3項AI功能，符合AI工具整合條件"],"key_gaps":["海外7國經驗為B2C社交App，缺乏直接面向海外B2B企業或政府機關客戶之交付案例","數據工具列GA4、Excel與對照實驗，未明文記載獨立撰寫SQL或BI儀表板查詢","防詐經驗集中於登入簽章驗證，需於面試確認對通訊防詐與風險偵測模型之理解深度"],"strengths":["尚凡經歷｜定價實驗三階段（各期 21 天）iOS增5%、Android減18%｜衡量邊界極嚴謹","1111經歷｜2026/04/17 上線簽章驗證，至 2026/10 未再出現冒用｜資安交付閉環明確","專業摘要｜5 點結構化條列呈現核心成果與方法｜視覺掃描與資訊階層清晰"],"interview_questions":["過去在SweetRing與CodaPay的海外經驗，如何轉移至東南亞或日韓B2B企業客戶需求收集？","在1111分析1,857張需求單與名冊留存時，是否親自使用SQL撈取資料？","2026/04廠商帳號冒用事件中，攻擊途徑為何？簽章驗證在架構上如何設計與驗收？","如何將Claude Code工作流與團隊既有專案管理工具（如Jira/Kanban）串接？"],"editorial_appendix":["可於技能欄明確標示SQL/BI熟練度，並補充專案管理工具名稱（如Jira）"],"spectrum":{"level":7,"uncertainty_levels":1,"basis":"具多個完整B2B交付與實驗案例支持面試，且有清楚取捨與衡量限制說明"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"not_tested","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：7（±1）
- 一句話理由：「約 50 項大項功能上線」且「2026/04/17 上線簽章驗證」衡量與閉環嚴謹，支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 全站活躍付費廠商約 6.6 萬家（2026/04/30） | 無關鍵缺口，可於面試深化 |
| role_evidence | 強 | 約 50 項大項功能上線，上線 111 項細項 | 未明列SQL與Jira工具字樣 |
| decision_depth | 足夠 | 選擇首次登入引導確認、不強迫修改 | 刪減了搜尋改版排序與配對規則修改細節 |
| outcome_quality | 強 | 管線觸及 1,279 家，約占全站 66,150 家 1.9% | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 團隊 3 名企劃，直接向組織副總匯報 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 段落清晰，專案交付脈絡與數據易於檢索 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 5-8年以上B2B/B2G產品或專案管理經驗 | 必要 | supported | Product Owner／PM｜1111 全球華人｜2022/08 - 迄今 | 近10年PM，企業招募系統PO近4年 |
| R02 接近母語等級英語口說與書寫 | 必要 | supported | 英文 TOEIC 980、TOEFL iBT 93 | 高分英檢與美國交換及翻譯實務 |
| R03 優異的溝通與關係人管理能力 | 必要 | supported | 對接 16 個需求單位，依使用者旅程排優先級 | 跨16單位協調並直接向副總匯報 |
| R04 扎實產品管理基礎（PRD/路線圖/風險控管） | 必要 | supported | 主責約 50 項大項功能規劃，掌握驗收與交付 | 完整涵蓋需求分析、規格與上線驗收 |
| R05 強烈的數據敏感度（SQL/BI/試算表分析） | 必要 | partial | GA4、世代分析、對照組實驗、Excel | 具試算與實驗分析，未明載SQL與BI工具 |
| R06 熟悉AI工具與工作流整合 | 必要 | supported | Claude Code 多分支流程與共用 skill 庫 | 建置AI協作工作流並落地3項AI功能 |
| R07 對防詐與風險偵測有真正熱情 | 必要 | supported | 登入安全盤點源於 2026/04 十多家廠商帳號遭冒用 | 具防冒用安全盤點與簽章驗證實績 |
| R08 具防詐、資安、風險管理或信任類產品經驗 | 加分 | supported | 與工程協作於 2026/04/17 上線簽章驗證 | 實際處理企業帳號冒用並完成技術防護 |
| R09 曾服務企業客戶或政府機關，尤其海外市場 | 加分 | partial | SweetRing 在地化涵蓋美、墨、巴、印、馬、日、韓7市場 | 具海外7國B2C與台灣B2B，缺海外B2B客戶 |
| R10 技術背景或曾與RD/AI團隊密切合作 | 加分 | supported | AI 功能已上線...與資料科學團隊合作 | 與工程及資料科學團隊密切協作並具AWS證照 |
| R11 具Agile/Scrum與Jira專案管理經驗 | 加分 | supported | Kanban 搭配瀑布式開發、Daily stand-up | 具Kanban、站會與回顧實務，未明列Jira字樣 |
| R12 具產品定價、報價或成本利潤分析經驗 | 加分 | supported | 定價實驗採原價、iOS 降價、還原原價三階段 | 具三階段定價實驗與跨國金流抽成稅費試算 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 符合5年以上PM與B2B經驗要求 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 16 個需求單位 | 近4年主責6.6萬家廠商招募系統 |
| HR03 | supported | 團隊 3 名企劃，直接向組織副總匯報 | 個人負責規格、驗收與跨單位排程 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 交付週期縮短與留存率具明確紀錄 |
| HR05 | supported | 盤點出上千組重複 E-mail，選擇首次登入引導確認 | 兼顧系統轉換與廠商使用連續性 |
| HR06 | supported | 從思維特助理PM、尚凡PM到1111企劃主任 | 職涯由C端成長型產品演進至B2B平台 |
| HR07 | supported | 寫成 PRD 與 Axure Prototype；和 QA 寫 UAT | 技能欄所列工具皆在經歷中有對應實作 |
| HR08 | supported | 依摘要、工作經歷、學歷、專業技能、自傳分段 | 結構清楚，重點與量化指標易讀 |
| HR09 | supported | 年化留存 81.2%，同期全站 74.2%（非因果） | 誠實標註觀察差異，無誇大矛盾 |
| HR10 | supported | 想在更早階段參與產品方向，從定義問題開始 | 轉職動機與資深PM職責高度相容 |
| HR11 | supported | 雙北、可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點與到職時間無衝突 |
| HR12 | supported | 具B2B大模組交付、登入防冒用與AI工作流實績 | 證據充分，強烈建議安排面試 |
| HM01 | supported | 企業端招募系統全模組（約 6.6 萬家活躍付費廠商） | B2B招募系統全模組與雙邊平台經驗高度相關 |
| HM02 | supported | 依使用者旅程與工單問題排定優先級 | 依旅程與工單排優先級，具問題導向意識 |
| HM03 | supported | 選擇首次登入引導確認、不強迫修改 | 首登引導確認不強迫修改，兼顧轉換與體驗 |
| HM04 | supported | 馬來西亞 iOS 三階段定價實驗；網頁付款占八成 | 定價實驗、點數付費牆與網頁金流具商業敏銳度 |
| HM05 | supported | 處理週期 100.4 降至 30.9 天；留存為觀察差異 | 分母占比、實驗天數與基期變化拆解極為嚴謹 |
| HM06 | supported | 與 16 個需求單位對接，直接向組織副總匯報 | 對接16單位、帶3名企劃並直報副總，權責明確 |
| HM07 | supported | 2025/10 離峰切換停機 1.5 小時；上線簽章驗證 | 離峰切換停機1.5小時與簽章驗證展現交付風控 |
| HM08 | supported | 與資料科學團隊上線 3 項 AI 功能；具 AWS 證照 | 與DS合作3項AI功能並具AWS證照，協作順暢 |
| HM09 | supported | 主導約 50 項大項功能上線，細項 111 項 | 主導50大項功能與6.6萬廠商系統，符合資深範圍 |
| HM10 | supported | 清楚交代問題背景、個人行動、結果與非因果限制 | 結構清楚，重點成果與限制條件易於檢索 |
| HM11 | supported | 依客服測試回饋調整規則；還原原價後全面調降 | 依客服測試回饋調整AI規則，具迭代修正機制 |
| HM12 | supported | 登入簽章驗證、AI推薦規則、定價實驗具追問價值 | 防冒用架構、AI工作流與定價細節值得面試深挖 |
| HM13 | supported | 全項判讀均對齊職缺條件與履歷原文，未推測空窗 | 依職缺標準客觀取證，無不當推論 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 主導1111企業招募系統50大項功能與16單位協調，符合50%專案交付與跨部門要求 |
| 2 | 統籌2026/04廠商帳號遭冒用危機並上線簽章驗證，具防詐與資安實戰經驗 |
| 3 | 深度運用Claude Code建置工作流並與DS團隊落地3項AI功能，符合AI工具整合條件 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 海外7國經驗為B2C社交App，缺乏直接面向海外B2B企業或政府機關客戶之交付案例 | 過去在SweetRing與CodaPay的海外經驗，如何轉移至東南亞或日韓B2B企業客戶需求收集？ |
| 2 | 數據工具列GA4、Excel與對照實驗，未明文記載獨立撰寫SQL或BI儀表板查詢 | 在1111分析1,857張需求單與名冊留存時，是否親自使用SQL撈取資料？ |
| 3 | 防詐經驗集中於登入簽章驗證，需於面試確認對通訊防詐與風險偵測模型之理解深度 | 2026/04廠商帳號冒用事件中，攻擊途徑為何？簽章驗證在架構上如何設計與驗收？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 尚凡經歷｜定價實驗三階段（各期 21 天）iOS增5%、Android減18%｜衡量邊界極嚴謹
- 1111經歷｜2026/04/17 上線簽章驗證，至 2026/10 未再出現冒用｜資安交付閉環明確
- 專業摘要｜5 點結構化條列呈現核心成果與方法｜視覺掃描與資訊階層清晰

**可改進（≤5 點）**：
- 位置：1111經歷與自傳
  - 原句：依使用者旅程與工單問題排定優先級
  - 問題類型：readability
  - 嚴重度：editorial
  - 影響：較8.1版少了一組具體功能取捨與規則修改案例
  - 建議方向：可於面試或經歷中補回搜尋改版與配對排序實例
- 位置：思維特經歷
  - 原句：SweetRing 在地化涵蓋美、墨、巴、印、馬、日、韓 7 市場
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：JD加分項偏好海外企業或政府客戶，此為C端產品
  - 建議方向：於面試強調跨國需求協調如何轉移至B2B場景


**編輯附件**（語氣、用詞微調；不影響判斷）：可於技能欄明確標示SQL/BI熟練度，並補充專案管理工具名稱（如Jira）

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


## 單份審查｜履歷 9.4｜第 3 輪｜model_id: gemini-4-argon

```json
{"rubric_version":"4.2","resume_id":"Resume_9.4","job_id":"104_950oe_Gogolook_Senior_PM","job_input":"summary","model_id":"gemini-4-argon","run_id":"A-9.4-03","human_calibrated":false,"requirements":[{"id":"R01","text":"5-8年以上B2B/B2G產品或專案管理經驗","type":"required","status":"supported","evidence":["Product Owner／PM｜1111 全球華人｜2022/08 - 迄今"],"blocks_interview":false,"reason":"近10年PM，企業招募系統PO近4年"},{"id":"R02","text":"接近母語等級英語口說與書寫","type":"required","status":"supported","evidence":["英文 TOEIC 980、TOEFL iBT 93"],"blocks_interview":false,"reason":"高分英檢與美國交換及翻譯實務"},{"id":"R03","text":"優異的溝通與關係人管理能力","type":"required","status":"supported","evidence":["對接 16 個需求單位，依使用者旅程排優先級"],"blocks_interview":false,"reason":"跨16單位協調並直接向副總匯報"},{"id":"R04","text":"扎實產品管理基礎（PRD/路線圖/風險控管）","type":"required","status":"supported","evidence":["主責約 50 項大項功能規劃，掌握驗收與交付"],"blocks_interview":false,"reason":"完整涵蓋需求分析、規格與上線驗收"},{"id":"R05","text":"強烈的數據敏感度（SQL/BI/試算表分析）","type":"required","status":"partial","evidence":["GA4、世代分析、對照組實驗、Excel"],"blocks_interview":false,"reason":"具試算與實驗分析，未明載SQL與BI工具"},{"id":"R06","text":"熟悉AI工具與工作流整合","type":"required","status":"supported","evidence":["Claude Code 多分支流程與共用 skill 庫"],"blocks_interview":false,"reason":"建置AI協作工作流並落地3項AI功能"},{"id":"R07","text":"對防詐與風險偵測有真正熱情","type":"required","status":"supported","evidence":["登入安全盤點源於 2026/04 十多家廠商帳號遭冒用"],"blocks_interview":false,"reason":"具防冒用安全盤點與簽章驗證實績"},{"id":"R08","text":"具防詐、資安、風險管理或信任類產品經驗","type":"preferred","status":"supported","evidence":["與工程協作於 2026/04/17 上線簽章驗證"],"blocks_interview":false,"reason":"實際處理企業帳號冒用並完成技術防護"},{"id":"R09","text":"曾服務企業客戶或政府機關，尤其海外市場","type":"preferred","status":"partial","evidence":["SweetRing 在地化涵蓋美、墨、巴、印、馬、日、韓7市場"],"blocks_interview":false,"reason":"具海外7國B2C與台灣B2B，缺海外B2B客戶"},{"id":"R10","text":"技術背景或曾與RD/AI團隊密切合作","type":"preferred","status":"supported","evidence":["AI 功能已上線...與資料科學團隊合作"],"blocks_interview":false,"reason":"與工程及資料科學團隊密切協作並具AWS證照"},{"id":"R11","text":"具Agile/Scrum與Jira專案管理經驗","type":"preferred","status":"supported","evidence":["Kanban 搭配瀑布式開發、Daily stand-up"],"blocks_interview":false,"reason":"具Kanban、站會與回顧實務，未明列Jira字樣"},{"id":"R12","text":"具產品定價、報價或成本利潤分析經驗","type":"preferred","status":"supported","evidence":["定價實驗採原價、iOS 降價、還原原價三階段"],"blocks_interview":false,"reason":"具三階段定價實驗與跨國金流抽成稅費試算"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["全站活躍付費廠商約 6.6 萬家（2026/04/30）"],"missing":[],"issue_ids":[]},{"id":"role_evidence","rating":"強","evidence":["約 50 項大項功能上線，上線 111 項細項"],"missing":["未明列SQL與Jira工具字樣"],"issue_ids":["I02"]},{"id":"decision_depth","rating":"足夠","evidence":["選擇首次登入引導確認、不強迫修改"],"missing":["刪減了搜尋改版排序與配對規則修改細節"],"issue_ids":["I01"]},{"id":"outcome_quality","rating":"強","evidence":["管線觸及 1,279 家，約占全站 66,150 家 1.9%"],"missing":[],"issue_ids":[]},{"id":"ownership","rating":"強","evidence":["團隊 3 名企劃，直接向組織副總匯報"],"missing":[],"issue_ids":[]},{"id":"readability","rating":"強","evidence":["段落清晰，專案交付脈絡與數據易於檢索"],"missing":[],"issue_ids":[]}],"results":[{"quote":"需求平均處理週期由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"截至 09/29，完成 1,726／1,857 張需求與問題單","kinds":["output"]},{"quote":"觸及 1,279 家活躍付費廠商，約占全站 1.9%","kinds":["context","outcome"]},{"quote":"iOS 非續訂營收增 5%，Android 減 18%，相對多 28%","kinds":["outcome"]},{"quote":"Peach 網頁付款占營收由 24% 至 80% 以上","kinds":["outcome"]},{"quote":"2026/04/17 上線簽章驗證，至 10 月未再出現冒用","kinds":["output","outcome"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"符合5年以上PM與B2B經驗要求"},{"rule_id":"HR02","status":"supported","resume_evidence":["現任 1111 招募系統 PO，對接 16 個需求單位"],"application_note":"近4年主責6.6萬家廠商招募系統"},{"rule_id":"HR03","status":"supported","resume_evidence":["團隊 3 名企劃，直接向組織副總匯報"],"application_note":"個人負責規格、驗收與跨單位排程"},{"rule_id":"HR04","status":"supported","resume_evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"application_note":"交付週期縮短與留存率具明確紀錄"},{"rule_id":"HR05","status":"supported","resume_evidence":["盤點出上千組重複 E-mail，選擇首次登入引導確認"],"application_note":"兼顧系統轉換與廠商使用連續性"},{"rule_id":"HR06","status":"supported","resume_evidence":["從思維特助理PM、尚凡PM到1111企劃主任"],"application_note":"職涯由C端成長型產品演進至B2B平台"},{"rule_id":"HR07","status":"supported","resume_evidence":["寫成 PRD 與 Axure Prototype；和 QA 寫 UAT"],"application_note":"技能欄所列工具皆在經歷中有對應實作"},{"rule_id":"HR08","status":"supported","resume_evidence":["依摘要、工作經歷、學歷、專業技能、自傳分段"],"application_note":"結構清楚，重點與量化指標易讀"},{"rule_id":"HR09","status":"supported","resume_evidence":["年化留存 81.2%，同期全站 74.2%（非因果）"],"application_note":"誠實標註觀察差異，無誇大矛盾"},{"rule_id":"HR10","status":"supported","resume_evidence":["想在更早階段參與產品方向，從定義問題開始"],"application_note":"轉職動機與資深PM職責高度相容"},{"rule_id":"HR11","status":"supported","resume_evidence":["雙北、可接受遠端或混合辦公｜錄取後三週可上班"],"application_note":"工作地點與到職時間無衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["具B2B大模組交付、登入防冒用與AI工作流實績"],"application_note":"證據充分，強烈建議安排面試"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["企業端招募系統全模組（約 6.6 萬家活躍付費廠商）"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依使用者旅程與工單問題排定優先級"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["選擇首次登入引導確認、不強迫修改"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["馬來西亞 iOS 三階段定價實驗；網頁付款占八成"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"supported","resume_evidence":["處理週期 100.4 降至 30.9 天；留存為觀察差異"],"evidence_type":"outcome","source_ids":[],"interview_question":null},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["與 16 個需求單位對接，直接向組織副總匯報"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["2025/10 離峰切換停機 1.5 小時；上線簽章驗證"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"supported","resume_evidence":["與資料科學團隊上線 3 項 AI 功能；具 AWS 證照"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM09","primary_dimension":"positioning","status":"supported","resume_evidence":["主導約 50 項大項功能上線，細項 111 項"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["清楚交代問題背景、個人行動、結果與非因果限制"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依客服測試回饋調整規則；還原原價後全面調降"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["登入簽章驗證、AI推薦規則、定價實驗具追問價值"],"evidence_type":"context","source_ids":[],"interview_question":"請說明2026/04廠商帳號遭冒用之攻擊手法與簽章驗證架構細節"},{"rule_id":"HM13","primary_dimension":"role_evidence","status":"supported","resume_evidence":["全項判讀均對齊職缺條件與履歷原文，未推測空窗"],"evidence_type":"context","source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HM03","source_ids":[],"application_note":"刪減搜尋改版與配對排序決策案例","context_limit":"1111經歷與自傳","category":"readability","severity":"editorial","block_target":null,"claim":"依使用者旅程與工單問題排定優先級","reason":"較8.1版少了一組具體功能取捨與規則修改案例","suggestion":"可於面試或經歷中補回搜尋改版與配對排序實例"},{"id":"I02","rule_id":"HR01","source_ids":[],"application_note":"海外經驗屬B2C而非B2B企業客戶","context_limit":"思維特經歷","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"SweetRing 在地化涵蓋美、墨、巴、印、馬、日、韓 7 市場","reason":"JD加分項偏好海外企業或政府客戶，此為C端產品","suggestion":"於面試強調跨國需求協調如何轉移至B2B場景"}],"decision":{"recommendation":"interview","evidence":["主導約 50 項大項功能上線，具簽章驗證與 AI 實績"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["主導1111企業招募系統50大項功能與16單位協調，符合50%專案交付與跨部門要求","統籌2026/04廠商帳號遭冒用危機並上線簽章驗證，具防詐與資安實戰經驗","深度運用Claude Code建置工作流並與DS團隊落地3項AI功能，符合AI工具整合條件"],"key_gaps":["海外7國經驗為B2C社交App，缺乏直接面向海外B2B企業或政府機關客戶之交付案例","數據工具列GA4、Excel與對照實驗，未明文記載獨立撰寫SQL或BI儀表板查詢","防詐經驗集中於登入簽章驗證，需於面試確認對通訊防詐與風險偵測模型之理解深度"],"strengths":["尚凡經歷｜定價實驗三階段（各期 21 天）iOS增5%、Android減18%｜衡量邊界極嚴謹","1111經歷｜2026/04/17 上線簽章驗證，至 2026/10 未再出現冒用｜資安交付閉環明確","專業摘要｜5 點結構化條列呈現核心成果與方法｜視覺掃描與資訊階層清晰"],"interview_questions":["過去在SweetRing與CodaPay的海外經驗，如何轉移至東南亞或日韓B2B企業客戶需求收集？","在1111分析1,857張需求單與名冊留存時，是否親自使用SQL撈取資料？","2026/04廠商帳號冒用事件中，攻擊途徑為何？簽章驗證在架構上如何設計與驗收？","如何將Claude Code工作流與團隊既有專案管理工具（如Jira/Kanban）串接？"],"editorial_appendix":["可於技能欄明確標示SQL/BI熟練度，並補充專案管理工具名稱（如Jira）"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"具多個完整B2B交付與實驗案例支持面試，且有清楚取捨與衡量限制說明"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"not_tested","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「約 50 項大項功能上線」且「2026/04/17 上線簽章驗證」衡量與閉環嚴謹，支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 全站活躍付費廠商約 6.6 萬家（2026/04/30） | 無關鍵缺口，可於面試深化 |
| role_evidence | 強 | 約 50 項大項功能上線，上線 111 項細項 | 未明列SQL與Jira工具字樣 |
| decision_depth | 足夠 | 選擇首次登入引導確認、不強迫修改 | 刪減了搜尋改版排序與配對規則修改細節 |
| outcome_quality | 強 | 管線觸及 1,279 家，約占全站 66,150 家 1.9% | 無關鍵缺口，可於面試深化 |
| ownership | 強 | 團隊 3 名企劃，直接向組織副總匯報 | 無關鍵缺口，可於面試深化 |
| readability | 強 | 段落清晰，專案交付脈絡與數據易於檢索 | 無關鍵缺口，可於面試深化 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 5-8年以上B2B/B2G產品或專案管理經驗 | 必要 | supported | Product Owner／PM｜1111 全球華人｜2022/08 - 迄今 | 近10年PM，企業招募系統PO近4年 |
| R02 接近母語等級英語口說與書寫 | 必要 | supported | 英文 TOEIC 980、TOEFL iBT 93 | 高分英檢與美國交換及翻譯實務 |
| R03 優異的溝通與關係人管理能力 | 必要 | supported | 對接 16 個需求單位，依使用者旅程排優先級 | 跨16單位協調並直接向副總匯報 |
| R04 扎實產品管理基礎（PRD/路線圖/風險控管） | 必要 | supported | 主責約 50 項大項功能規劃，掌握驗收與交付 | 完整涵蓋需求分析、規格與上線驗收 |
| R05 強烈的數據敏感度（SQL/BI/試算表分析） | 必要 | partial | GA4、世代分析、對照組實驗、Excel | 具試算與實驗分析，未明載SQL與BI工具 |
| R06 熟悉AI工具與工作流整合 | 必要 | supported | Claude Code 多分支流程與共用 skill 庫 | 建置AI協作工作流並落地3項AI功能 |
| R07 對防詐與風險偵測有真正熱情 | 必要 | supported | 登入安全盤點源於 2026/04 十多家廠商帳號遭冒用 | 具防冒用安全盤點與簽章驗證實績 |
| R08 具防詐、資安、風險管理或信任類產品經驗 | 加分 | supported | 與工程協作於 2026/04/17 上線簽章驗證 | 實際處理企業帳號冒用並完成技術防護 |
| R09 曾服務企業客戶或政府機關，尤其海外市場 | 加分 | partial | SweetRing 在地化涵蓋美、墨、巴、印、馬、日、韓7市場 | 具海外7國B2C與台灣B2B，缺海外B2B客戶 |
| R10 技術背景或曾與RD/AI團隊密切合作 | 加分 | supported | AI 功能已上線...與資料科學團隊合作 | 與工程及資料科學團隊密切協作並具AWS證照 |
| R11 具Agile/Scrum與Jira專案管理經驗 | 加分 | supported | Kanban 搭配瀑布式開發、Daily stand-up | 具Kanban、站會與回顧實務，未明列Jira字樣 |
| R12 具產品定價、報價或成本利潤分析經驗 | 加分 | supported | 定價實驗採原價、iOS 降價、還原原價三階段 | 具三階段定價實驗與跨國金流抽成稅費試算 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 符合5年以上PM與B2B經驗要求 |
| HR02 | supported | 現任 1111 招募系統 PO，對接 16 個需求單位 | 近4年主責6.6萬家廠商招募系統 |
| HR03 | supported | 團隊 3 名企劃，直接向組織副總匯報 | 個人負責規格、驗收與跨單位排程 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 交付週期縮短與留存率具明確紀錄 |
| HR05 | supported | 盤點出上千組重複 E-mail，選擇首次登入引導確認 | 兼顧系統轉換與廠商使用連續性 |
| HR06 | supported | 從思維特助理PM、尚凡PM到1111企劃主任 | 職涯由C端成長型產品演進至B2B平台 |
| HR07 | supported | 寫成 PRD 與 Axure Prototype；和 QA 寫 UAT | 技能欄所列工具皆在經歷中有對應實作 |
| HR08 | supported | 依摘要、工作經歷、學歷、專業技能、自傳分段 | 結構清楚，重點與量化指標易讀 |
| HR09 | supported | 年化留存 81.2%，同期全站 74.2%（非因果） | 誠實標註觀察差異，無誇大矛盾 |
| HR10 | supported | 想在更早階段參與產品方向，從定義問題開始 | 轉職動機與資深PM職責高度相容 |
| HR11 | supported | 雙北、可接受遠端或混合辦公｜錄取後三週可上班 | 工作地點與到職時間無衝突 |
| HR12 | supported | 具B2B大模組交付、登入防冒用與AI工作流實績 | 證據充分，強烈建議安排面試 |
| HM01 | supported | 企業端招募系統全模組（約 6.6 萬家活躍付費廠商） | B2B招募系統全模組與雙邊平台經驗高度相關 |
| HM02 | supported | 依使用者旅程與工單問題排定優先級 | 依旅程與工單排優先級，具問題導向意識 |
| HM03 | supported | 選擇首次登入引導確認、不強迫修改 | 首登引導確認不強迫修改，兼顧轉換與體驗 |
| HM04 | supported | 馬來西亞 iOS 三階段定價實驗；網頁付款占八成 | 定價實驗、點數付費牆與網頁金流具商業敏銳度 |
| HM05 | supported | 處理週期 100.4 降至 30.9 天；留存為觀察差異 | 分母占比、實驗天數與基期變化拆解極為嚴謹 |
| HM06 | supported | 與 16 個需求單位對接，直接向組織副總匯報 | 對接16單位、帶3名企劃並直報副總，權責明確 |
| HM07 | supported | 2025/10 離峰切換停機 1.5 小時；上線簽章驗證 | 離峰切換停機1.5小時與簽章驗證展現交付風控 |
| HM08 | supported | 與資料科學團隊上線 3 項 AI 功能；具 AWS 證照 | 與DS合作3項AI功能並具AWS證照，協作順暢 |
| HM09 | supported | 主導約 50 項大項功能上線，細項 111 項 | 主導50大項功能與6.6萬廠商系統，符合資深範圍 |
| HM10 | supported | 清楚交代問題背景、個人行動、結果與非因果限制 | 結構清楚，重點成果與限制條件易於檢索 |
| HM11 | supported | 依客服測試回饋調整規則；還原原價後全面調降 | 依客服測試回饋調整AI規則，具迭代修正機制 |
| HM12 | supported | 登入簽章驗證、AI推薦規則、定價實驗具追問價值 | 防冒用架構、AI工作流與定價細節值得面試深挖 |
| HM13 | supported | 全項判讀均對齊職缺條件與履歷原文，未推測空窗 | 依職缺標準客觀取證，無不當推論 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 主導1111企業招募系統50大項功能與16單位協調，符合50%專案交付與跨部門要求 |
| 2 | 統籌2026/04廠商帳號遭冒用危機並上線簽章驗證，具防詐與資安實戰經驗 |
| 3 | 深度運用Claude Code建置工作流並與DS團隊落地3項AI功能，符合AI工具整合條件 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 海外7國經驗為B2C社交App，缺乏直接面向海外B2B企業或政府機關客戶之交付案例 | 過去在SweetRing與CodaPay的海外經驗，如何轉移至東南亞或日韓B2B企業客戶需求收集？ |
| 2 | 數據工具列GA4、Excel與對照實驗，未明文記載獨立撰寫SQL或BI儀表板查詢 | 在1111分析1,857張需求單與名冊留存時，是否親自使用SQL撈取資料？ |
| 3 | 防詐經驗集中於登入簽章驗證，需於面試確認對通訊防詐與風險偵測模型之理解深度 | 2026/04廠商帳號冒用事件中，攻擊途徑為何？簽章驗證在架構上如何設計與驗收？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 尚凡經歷｜定價實驗三階段（各期 21 天）iOS增5%、Android減18%｜衡量邊界極嚴謹
- 1111經歷｜2026/04/17 上線簽章驗證，至 2026/10 未再出現冒用｜資安交付閉環明確
- 專業摘要｜5 點結構化條列呈現核心成果與方法｜視覺掃描與資訊階層清晰

**可改進（≤5 點）**：
- 位置：1111經歷與自傳
  - 原句：依使用者旅程與工單問題排定優先級
  - 問題類型：readability
  - 嚴重度：editorial
  - 影響：較8.1版少了一組具體功能取捨與規則修改案例
  - 建議方向：可於面試或經歷中補回搜尋改版與配對排序實例
- 位置：思維特經歷
  - 原句：SweetRing 在地化涵蓋美、墨、巴、印、馬、日、韓 7 市場
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：JD加分項偏好海外企業或政府客戶，此為C端產品
  - 建議方向：於面試強調跨國需求協調如何轉移至B2B場景


**編輯附件**（語氣、用詞微調；不影響判斷）：可於技能欄明確標示SQL/BI熟練度，並補充專案管理工具名稱（如Jira）

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

# 附錄：② 版本比較 B 明細（4 輪甲乙交換）

## 版本比較｜第 1 輪｜順序 甲=8.1/乙=9.4｜model_id: gemini-4-argon

```json
{"order":"甲=8.1/乙=9.4","differences":[{"what":"乙版補齊全站廠商分母（占1.9%）與定價實驗天數（21天）及增減拆解","hiring_meaning":"衡量邊界與基期明確，成果可信度高，方便主管直接核驗實驗顯著性","type":"measurement"},{"what":"乙版明載登入簽章驗證上線日（2026/04/17）與觀察期（至2026/10未再發生）","hiring_meaning":"提供完整交付風險控制閉環，切合防詐BU對資安處置時效之關注","type":"capability"},{"what":"甲版保留搜尋痛點改版排在職缺健檢之前與配對名單修改日排序等細節","hiring_meaning":"甲版更能直接看見日常功能排序與規則修改之取捨過程","type":"capability"}],"preference":"乙","reason":"乙版在成果衡量品質、分母透明度與資安防冒用閉環上顯著更嚴謹，便於主管直接錨定面試驗證點；甲版雖決策取捨生動，但數據顆粒度略粗。","evidence_甲":["需求流程服務過的 1,279 家付費廠商，年化留存 81.2%","改用簽章驗證，之後未再發生"],"evidence_乙":["觸及 1,279 家活躍付費廠商，約占全站 66,150 家的 1.9%","與工程協作於 2026/04/17 上線簽章驗證"]}
```

- 偏好：乙

| # | 差異 | 招聘意義 | 類型（capability/measurement/readability/tone） | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 乙版補齊全站廠商分母（占1.9%）與定價實驗天數（21天）及增減拆解 | 衡量邊界與基期明確，成果可信度高，方便主管直接核驗實驗顯著性 | measurement | 需求流程服務過的 1,279 家付費廠商，年化留存 81.2% | 觸及 1,279 家活躍付費廠商，約占全站 66,150 家的 1.9% |
| 2 | 乙版明載登入簽章驗證上線日（2026/04/17）與觀察期（至2026/10未再發生） | 提供完整交付風險控制閉環，切合防詐BU對資安處置時效之關注 | capability | 改用簽章驗證，之後未再發生 | 與工程協作於 2026/04/17 上線簽章驗證 |
| 3 | 甲版保留搜尋痛點改版排在職缺健檢之前與配對名單修改日排序等細節 | 甲版更能直接看見日常功能排序與規則修改之取捨過程 | capability | 改用簽章驗證，之後未再發生 | 與工程協作於 2026/04/17 上線簽章驗證 |

- 理由（≤120 字）：乙版在成果衡量品質、分母透明度與資安防冒用閉環上顯著更嚴謹，便於主管直接錨定面試驗證點；甲版雖決策取捨生動，但數據顆粒度略粗。
- 偏好若成立，另一版若採用此版長處，可補強的方向（不編造事實）：8.1 版可補入 9.4 版的全站廠商分母（66,150 家占 1.9%）、定價實驗 21 天期與增減公式拆解、以及登入簽章上線日期（2026/04/17）；9.4 版則可補回 8.1 版的搜尋痛點改版排序、配對名單修改日排查案例與 Claude Code 12 條分工細節。


## 版本比較｜第 2 輪｜順序 甲=9.4/乙=8.1｜model_id: gemini-4-argon

```json
{"order":"甲=9.4/乙=8.1","differences":[{"what":"甲版以iOS增5%、Android減18%拆解相對28%變化，並標註21天實驗期","hiring_meaning":"排除外部干擾，展示成熟的對照實驗設計與數據素養","type":"measurement"},{"what":"甲版登入安全明確載明統籌影響評估、範圍時程、驗證流程與客服說明","hiring_meaning":"清楚界定個人統籌範圍與跨部門協作邊界","type":"capability"},{"what":"甲版專業摘要拆為5點結構化清單，乙版為單一段落","hiring_meaning":"甲版視覺掃描效率較高，重點戰績一目了然","type":"readability"}],"preference":"甲","reason":"甲版在數據口徑、歸因邊界與資安事件交付時程上提供高可信度證據，有效減輕面試查核成本；乙版具備豐富決策細節，但指標嚴謹度略遜。","evidence_甲":["定價實驗採原價、iOS 降價、還原原價三階段（各期 21 天）","統籌影響評估、範圍與時程、驗證流程及客服說明"],"evidence_乙":["設計馬來西亞 iOS 三階段定價實驗，同期 Android 當對照組","統籌登入系統全面盤點，改用簽章驗證，之後未再發生"]}
```

- 偏好：甲

| # | 差異 | 招聘意義 | 類型（capability/measurement/readability/tone） | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 甲版以iOS增5%、Android減18%拆解相對28%變化，並標註21天實驗期 | 排除外部干擾，展示成熟的對照實驗設計與數據素養 | measurement | 定價實驗採原價、iOS 降價、還原原價三階段（各期 21 天） | 設計馬來西亞 iOS 三階段定價實驗，同期 Android 當對照組 |
| 2 | 甲版登入安全明確載明統籌影響評估、範圍時程、驗證流程與客服說明 | 清楚界定個人統籌範圍與跨部門協作邊界 | capability | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 統籌登入系統全面盤點，改用簽章驗證，之後未再發生 |
| 3 | 甲版專業摘要拆為5點結構化清單，乙版為單一段落 | 甲版視覺掃描效率較高，重點戰績一目了然 | readability | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 統籌登入系統全面盤點，改用簽章驗證，之後未再發生 |

- 理由（≤120 字）：甲版在數據口徑、歸因邊界與資安事件交付時程上提供高可信度證據，有效減輕面試查核成本；乙版具備豐富決策細節，但指標嚴謹度略遜。
- 偏好若成立，另一版若採用此版長處，可補強的方向（不編造事實）：8.1 版可補入 9.4 版的全站廠商分母（66,150 家占 1.9%）、定價實驗 21 天期與增減公式拆解、以及登入簽章上線日期（2026/04/17）；9.4 版則可補回 8.1 版的搜尋痛點改版排序、配對名單修改日排查案例與 Claude Code 12 條分工細節。


## 版本比較｜第 3 輪｜順序 甲=8.1/乙=9.4｜model_id: gemini-4-argon

```json
{"order":"甲=8.1/乙=9.4","differences":[{"what":"乙版在Juicy成效標註「為產品上線與行銷導流期間的整體表現」","hiring_meaning":"誠實區隔個人產品規劃與行銷導流之貢獻邊界","type":"measurement"},{"what":"乙版在Peach金流標註確切時間窗（2020/11–2021/09）","hiring_meaning":"時間跨度具體，便於核對職涯時序與產品生命週期","type":"measurement"},{"what":"甲版自傳保留「客服反映配對名單少又舊查出修改日排序並實測競品」","hiring_meaning":"甲版在問題排查與競品實測之描述更具臨場感","type":"capability"}],"preference":"乙","reason":"乙版在歸因誠實度與時間指標標註上展現更高專業水準，成果信度更高；甲版決策故事精彩，但乙版更能代表資深PM的嚴謹度。","evidence_甲":["Juicy 上線 6 週男性 DAU 約 3,200 → 1.25 萬","客服反映配對名單少又舊時，我先查出名單依履歷修改日排序"],"evidence_乙":["為產品上線與行銷導流期間的整體表現","Peach 網頁付款占營收由 24% 至 80% 以上（2020/11–2021/09）"]}
```

- 偏好：乙

| # | 差異 | 招聘意義 | 類型（capability/measurement/readability/tone） | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 乙版在Juicy成效標註「為產品上線與行銷導流期間的整體表現」 | 誠實區隔個人產品規劃與行銷導流之貢獻邊界 | measurement | Juicy 上線 6 週男性 DAU 約 3,200 → 1.25 萬 | 為產品上線與行銷導流期間的整體表現 |
| 2 | 乙版在Peach金流標註確切時間窗（2020/11–2021/09） | 時間跨度具體，便於核對職涯時序與產品生命週期 | measurement | 客服反映配對名單少又舊時，我先查出名單依履歷修改日排序 | Peach 網頁付款占營收由 24% 至 80% 以上（2020/11–2021/09） |
| 3 | 甲版自傳保留「客服反映配對名單少又舊查出修改日排序並實測競品」 | 甲版在問題排查與競品實測之描述更具臨場感 | capability | 客服反映配對名單少又舊時，我先查出名單依履歷修改日排序 | Peach 網頁付款占營收由 24% 至 80% 以上（2020/11–2021/09） |

- 理由（≤120 字）：乙版在歸因誠實度與時間指標標註上展現更高專業水準，成果信度更高；甲版決策故事精彩，但乙版更能代表資深PM的嚴謹度。
- 偏好若成立，另一版若採用此版長處，可補強的方向（不編造事實）：8.1 版可補入 9.4 版的全站廠商分母（66,150 家占 1.9%）、定價實驗 21 天期與增減公式拆解、以及登入簽章上線日期（2026/04/17）；9.4 版則可補回 8.1 版的搜尋痛點改版排序、配對名單修改日排查案例與 Claude Code 12 條分工細節。


## 版本比較｜第 4 輪｜順序 甲=9.4/乙=8.1｜model_id: gemini-4-argon

```json
{"order":"甲=9.4/乙=8.1","differences":[{"what":"甲版明確定義全站廠商規模基準日（2026/04/30）與管線觸及占比","hiring_meaning":"讓主管立刻掌握系統真實影響範圍與樣本代表性","type":"measurement"},{"what":"甲版技能欄補入Excel、Notion、Trello等日常工具","hiring_meaning":"補足日常專案管理與試算表工具鏈","type":"readability"},{"what":"乙版AI技能欄明載「12條分工、23個共用skill、轉衝突邏輯為工程條件」","hiring_meaning":"乙版AI工具實踐細節更具體，甲版改為多分支與共用skill庫較概括","type":"capability"}],"preference":"甲","reason":"甲版在指標邊界、協作工具盤點與排版條理性上全面佔優，面試驗證錨點清晰；乙版在AI細節雖具亮點，但整體嚴謹度以甲版為佳。","evidence_甲":["全站活躍付費廠商約 6.6 萬家（2026/04/30，系統規模）","Figma、Axure RP、Notion、Trello、Markdown"],"evidence_乙":["目前近 6.6 萬家活躍付費廠商","自建 Claude Code 協作流程（12 條分工、23 個共用 skill）"]}
```

- 偏好：甲

| # | 差異 | 招聘意義 | 類型（capability/measurement/readability/tone） | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 甲版明確定義全站廠商規模基準日（2026/04/30）與管線觸及占比 | 讓主管立刻掌握系統真實影響範圍與樣本代表性 | measurement | 全站活躍付費廠商約 6.6 萬家（2026/04/30，系統規模） | 目前近 6.6 萬家活躍付費廠商 |
| 2 | 甲版技能欄補入Excel、Notion、Trello等日常工具 | 補足日常專案管理與試算表工具鏈 | readability | Figma、Axure RP、Notion、Trello、Markdown | 自建 Claude Code 協作流程（12 條分工、23 個共用 skill） |
| 3 | 乙版AI技能欄明載「12條分工、23個共用skill、轉衝突邏輯為工程條件」 | 乙版AI工具實踐細節更具體，甲版改為多分支與共用skill庫較概括 | capability | Figma、Axure RP、Notion、Trello、Markdown | 自建 Claude Code 協作流程（12 條分工、23 個共用 skill） |

- 理由（≤120 字）：甲版在指標邊界、協作工具盤點與排版條理性上全面佔優，面試驗證錨點清晰；乙版在AI細節雖具亮點，但整體嚴謹度以甲版為佳。
- 偏好若成立，另一版若採用此版長處，可補強的方向（不編造事實）：8.1 版可補入 9.4 版的全站廠商分母（66,150 家占 1.9%）、定價實驗 21 天期與增減公式拆解、以及登入簽章上線日期（2026/04/17）；9.4 版則可補回 8.1 版的搜尋痛點改版排序、配對名單修改日排查案例與 Claude Code 12 條分工細節。

## 附錄：③ ATS 準備檢查逐題明細（ATS01–ATS14）

- `test_level`: `not_run`（僅執行純文字層面結構與詞彙檢查，未執行二進位 PDF 擷取或真實 ATS 匯入）
- `actual_ats_import_performed`: `false`

| 規則 ID | 狀態 (8.1 / 9.4) | 檢查與判讀紀錄 |
| :-- | :-- | :-- |
| ATS01 系統與功能識別 | unknown / unknown | 職缺來源為 104 人力銀行（連結代碼 950oe），雇主內部是否同步串接 Greenhouse/Ashby/Workable 未知。 |
| ATS02 接受檔案與解析分開 | not_tested / not_tested | 本次輸入為純文字（附錄 A、B），未提供實體 PDF/DOCX 檔案，故檔案大小與加密檢查標 not_tested。 |
| ATS03 欄位與讀序 | pass / pass | 姓名、聯絡資訊、職稱—公司—起訖日期、學歷、專業技能、自傳皆為單欄純文字順向排列，百分比與比較基準清楚，無錯序風險。 |
| ATS04 語言與結構資料 | pass / pass | 繁體中文為主，保留真實英文職稱與技能名詞（Product Owner, PRD, Axure, UAT, Claude Code, AWS），符合雙語檢索習慣。 |
| ATS05 搜尋路徑 | pass / pass | 全文涵蓋 B2B、Product Manager、PRD、Roadmap、UAT、AI、Claude、登入安全、簽章驗證、TOEIC 等核心檢索詞。 |
| ATS06 用詞對位 | pass / pass | 需求原句與履歷證據自然對位，無隱藏文字、白字或機械式重複堆砌關鍵字；可自然補入 SQL、Jira（若有實務經驗）。 |
| ATS07 申請表與資格 | unknown / unknown | 本次無平台申請表問答欄位資料，附件內求職條件與職缺地點（雙北）、年資（5 年以上）一致。 |
| ATS08 自動化流程 | unknown / unknown | 雇主是否配置自動推進或排程規則屬未知，不妄加推論。 |
| ATS09 匹配／排序 | unknown / unknown | 雇主後台匹配權重未知，依規準不合成通用 ATS 百分比分數。 |
| ATS10 重複申請 | unknown / unknown | 無歷史投遞與候選人池合併設定資料。 |
| ATS11 自動投遞／詐騙 | unknown / unknown | 無平台中繼資料；文字內部時序、職稱演進與量化邏輯一致，不從文風推論 AI 作者機率。 |
| ATS12 摘要與資料完整性 | pass / pass | 兩版摘要數據（50 項功能、16 需求單位、24%→80% 網頁金流）與正文完全吻合，無前後矛盾。 |
| ATS13 測試層級 | not_tested / not_tested | 本次為文字層檢核，標明未執行真實 ATS 匯入測試。 |
| ATS14 未知與覆核 | pass / pass | 關鍵缺口（海外 B2B、SQL/BI 實作）均已明確列為人工面試追問項，不因未寫直接判定不合格。 |

## 附錄 C：執行檢查清單核對
- [x] 每份履歷 ≥3 輪獨立審查（已記錄 `model_id: gemini-4-argon`，並於 §8 誠實揭露單一視窗限制）
- [x] B 比較 ≥4 輪，甲乙順序逐輪交換（第 1、3 輪 甲=8.1/乙=9.4；第 2、4 輪 甲=9.4/乙=8.1）
- [x] 所有輸出 JSON 為單行，欄位齊全、`human_calibrated=false`、`ai_authorship.probability=null`
- [x] 沒有任何輪次把頁數、學歷、空窗、任職長短、關鍵字個數當缺失
- [x] HR 12 題＋HM 13 題每輪都列全
- [x] 約談理由 ≤3、關鍵缺口 ≤3
- [x] ATS 五塊分開，無「ATS 分數」；沒實測就標 `not_tested`
- [x] 總報告依 §8 固定格式，且有「方法限制與未做項目」
