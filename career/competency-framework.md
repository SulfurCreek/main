<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

> ⚠️ **個人職涯資料，非 1111 規格文件 / Personal career material — NOT a 1111 spec.** 請勿套用 `spec-doc-1111`
> skill，也勿推送至 HackMD `1111-jobdocs` 團隊工作區。詳見 `career/CLAUDE.md`。
> *Do not apply the spec-doc-1111 skill or push to the HackMD team workspace; see `career/CLAUDE.md`.*

# 職能框架 / Competency Framework

> **用途 / Purpose**：作為下一步職涯（**資深產品經理 Senior PM** 或 **同領域轉職 same-craft move**）的職能盤點。
> 每一項職能都附上可追溯的工作證據（出自本 repo 的 `spec-doc-1111` skill、`tree.md` 文件清單中本人負責的範圍，
> 本人 Figma 工作檔《求才用圖層》的第一手規格／流程內容，以及本人維護的**求才產品 Roadmap**（Google Sheet）的
> 專案清單與交付時程）。
> 可直接用於升遷評估、履歷／LinkedIn 撰寫、面試談資。

---

## 定位一句話 / Positioning Statement

**繁中**：我是能掌握「產品定義全鏈路」的產品企劃——從 **User Story → Wireframe → 功能規格 → 跨團隊交接**，
獨立負責 **1111 求才系統（recruit, B 端）的端到端產品定義**，並延伸負責求職端的**公司頁（公司在求職站的呈現）**，
同時規劃多項**求才側 AI 產品**（生成式與推薦類）。

**English**：A product planner who owns the **full definition pipeline** — *user story → wireframe → functional
spec → cross-team handoff* — for the **1111 recruit (employer, B-side) platform end-to-end**, extending to the
jobseeker-facing **company page (公司頁)**, plus a line of **employer-side AI products** (generative + recommendation).
I originate products from my own user stories and wireframes; I don't transcribe other people's.

---

## 概覽 / Profile Snapshot

| 維度 / Dimension | 內容 / Detail |
| :--- | :--- |
| 負責範圍 / Ownership | **求才系統（recruit, B 端）全系統**（A–M 各模組）＋ 求職端**公司頁**；本人撰寫份數〔待補數據 / TODO: count〕 |
| 平台定位 / Surface | 廠商端（B-side）平台主責；公司頁為連結至求職者端（C-side）的橋接面 |
| 產品線 / Product lines | 核心交易流程 ＋ **求才側 AI 產品**（職缺匯入、公司簡介生成、JD 生成、職缺健檢、AI 推薦人才） |
| 角色定位 / Role | 需求源頭 → 規格輸出 → 交接落地（originate → specify → hand off），非單純文件化 |
| 路線圖與團隊 / Roadmap & team | 主導 **227 項求才產品 Roadmap**（P0–P3 優先級、時間盒交付節奏）；委派工單給 **3 人企劃團隊**（本人＋育琳／小楊）與工程／QA；近半年 111 項上線、**94% 準時或提前** |
| 方法論 / Method | 狀態驅動規格、MECE 四狀態、權限代碼建模、分階段交付、版本控管、流程圖視覺化 |
| 工具化 / Tooling | 將自身規格慣例**標準化為可複用 skill**（`spec-doc-1111`）＋雙系統範本＋文件樹 |

> 註 / Note：HackMD `1111-jobdocs` 工作區共 307 份文件（`tree.md`），涵蓋多人；上表僅列**本人負責**範圍。
> *The HackMD workspace holds 307 docs across multiple people; the row above lists only what I own.*

---

## 核心職能 / Core Functions

> 每項職能格式：**定義 → 實際展現 → 工作證據 → 資深度訊號**
> Format per function: *definition → in practice → evidence → seniority signal*.

### F1. 產品定義全鏈路 / End-to-End Product Definition

**定義 / Definition**：從使用者需求出發，獨立完成 *User Story → Wireframe → 功能規格* 的產品定義，
作為需求的**源頭**而非下游文件化角色。
*Originate products end-to-end: user story → wireframe → functional spec, as the source of requirements rather
than a downstream documenter.*

- **實際展現 / In practice**：規格範本以 `User Story:`（Persona 視角）＋ `Use Case:`（系統視角）開場，
  將每個功能錨定在「為誰、解決什麼、達成什麼目標」；多數文件由我自己的 user story 或 wireframe 展開。
- **工作證據 / Evidence**：`spec-doc-1111` 範本骨架（User Story／Use Case 區塊）；求才系統各模組規格皆由本人的
  user story／wireframe 展開（見 `tree.md` 求才系統與公司頁範圍）。
- **資深度訊號 / Seniority signal**：擁有「定義權」——決定要做什麼、為什麼做，是 PM 角色的核心，而非 BA／文件職。

### F2. 功能規格與系統思維 / Functional Spec & Systems Thinking

**定義 / Definition**：以「狀態 → 行為」與「條件 → 結果」的方式描述規格，涵蓋邊界與例外，讓 RD/QA 可無歧義實作與驗收。
*Specify in state→behavior and condition→result terms, covering edge cases so engineers and QA can build and
verify without ambiguity.*

- **實際展現 / In practice**：
  - **MECE 四狀態**：所有非同步資料區塊一律覆蓋 `載入中／有資料／無資料／錯誤`（loading / data / empty / error）。
  - **權限代碼建模**：將散落的權限判斷集中為單一「權限判斷」表格，欄位以代碼建模（`oStatus:1`、`confirmed&4096`、`代碼54`）。
  - **條件邏輯**：巢狀條列描述「判斷 → 顯示／行為」，搭配狀態術語（default／disabled／Error／hover／toast）。
- **工作證據 / Evidence**：skill 核心原則（狀態驅動、欄位即真相、MECE）；`初始化` 三段式（進入路徑／權限判斷／資料載入）；
  `[REF] 求才系統權限代碼表`。
- **資深度訊號 / Seniority signal**：把模糊需求轉成**可驗收的系統規格**，降低反工與上線風險。

### F3. 廠商端平台深度 ＋ 公司頁橋接 / Employer-Side (B-Side) Platform Depth + Company-Page Bridge

**定義 / Definition**：完整掌握招募媒合平台**廠商端（B-side）**的商業邏輯與使用情境，並負責連結至求職者端的**公司頁**。
*Command the full business logic of the employer (B-side) of a recruitment platform, plus the jobseeker-facing
company page that bridges to the C-side.*

- **實際展現 / In practice**：
  - **求才 B 端 / Employer-side（主責）**：公司資料、職缺（新增／總覽／排序／移轉／廣告排程）、人才（搜尋／配對／追蹤／封鎖）、
    聯繫（信件訊息／範本）、購買（線上續約／合約）、紀錄統計。
  - **公司頁 / Company page（求職端唯一負責面）**：公司資料、相似公司、推薦職缺、品牌行銷子頁——
    廠商資料如何呈現給求職者的橋接面。
- **工作證據 / Evidence**：`tree.md` 求才系統（A–M 系列）；求職端「3. 公司頁」（3.2 公司資料、3.12 相似公司、
  3.13 推薦職缺、3.14 品牌行銷子頁），repo `.claude/assets/company-page/` 為其設計素材。
- **第一手證據 / First-party evidence**（本人 Figma 工作檔《求才用圖層》）：人才搜尋／配對（`配對條件設定：預設只看本國籍求職者`、
  `全文檢索`、欄位順序優化與展開／收折狀態）、聯繫即時通（「APP 語音通話的紀錄整合於聊天室內」）、
  購買與合約（`VIP求才招募系統`、Days Remaining／Expiration Date／Next Contract、排程 Calendar、Monthly Visits 數據）、
  進站導覽（`A. 新版進站彈窗`、Tour）、上傳／驗證流程（Upload File／Photo Capture／Verification & Send）。
- **資深度訊號 / Seniority signal**：對 B 端平台有端到端掌握，並透過公司頁理解 B→C 的曝光連動，具備平台級產品視野。

### F4. AI 產品企劃 / AI Product Planning

**定義 / Definition**：為 AI 驅動功能定義產品需求，涵蓋輸入／模型行為／結果呈現／失敗與邊界狀態。
*Define requirements for AI-driven features: inputs, model behavior, result presentation, and failure/edge states.*

- **實際展現 / In practice**：為**求才側**規格化生成式與推薦類 AI 功能，處理非確定性輸出的狀態設計
  （loading／成功／失敗／品質與邊界），把 LLM 能力轉成廠商可用的工作流。
- **工作證據 / Evidence（求才側 AI）**：
  - **生成式 / Generative**：**公司簡介生成**、**JD（職缺描述）生成**、**職缺匯入**（自動解析既有職缺）、**職缺健檢**。
  - **推薦 / Recommendation**：`3.2.6 AI 推薦人才名單`。
  - 相關提案／延伸：職缺審核導入 AI、AI 履歷&職缺打標、求才智能客服。
- **第一手證據 / First-party evidence**（本人 Figma 工作檔《求才用圖層》）：`AI一鍵優化職缺`、`AI智能徵才 – 立刻體驗！`、
  行銷訴求「1111 招募系統整合多樣智能招募利器，使用 AI 工具不用再剪剪貼貼」、AI 推薦人才調整
  （技能／證照推薦、推薦與建議移除樣式、AI icon）——可佐證生成式與推薦 AI 的實際規格產出。
- **資深度訊號 / Seniority signal**：能將生成式模型能力（公司簡介／JD 自動生成）轉譯為可落地的廠商價值與規格——
  當前最稀缺的 PM 能力之一。

### F5. 交付流程與品質 / Delivery Process & Quality

**定義 / Definition**：以可控、可追溯、可驗收的流程交付規格，管理變更與缺口。
*Deliver specs through a controlled, traceable, verifiable process; manage change and gaps.*

- **實際展現 / In practice**：
  - **版本控管**：每次發布更新版控表，調整說明採 `[異動區段] 內容摘要`，可 diff、可回溯。
  - **缺口管理**：規格缺口以 🚧 `:::warning` 區塊記錄（現況／缺口／待確認 checkbox／來源），而非孤立的「待補」。
  - **分階段交付**：第二階段內容拆為獨立文件並記錄出處，第一階段保留入口連結。
  - **變更標紅**：本版調整一律紅字，方便 RD/QA 一眼辨識差異。
- **工作證據 / Evidence**：skill「修改既有規格時」「版控紀錄」「階段拆分」「待補規則區塊」章節；交付前檢查清單。
- **資深度訊號 / Seniority signal**：把「寫規格」提升為**可治理的交付流程**，是帶人／帶專案的基礎。

### F6. 跨職能協作與知識交接 / Cross-Functional Collaboration & Knowledge Transfer

**定義 / Definition**：作為 PM／RD／QA／設計之間的樞紐，並把知識結構化交接，降低團隊對個人的依賴。
*Act as the hub across PM/RD/QA/design and structure knowledge for handoff, reducing key-person risk.*

- **實際展現 / In practice**：撰寫交接文件、功能說明頁、競品分析；維護跨組同步會議記錄；定義共用 API 規格。
- **工作證據 / Evidence**：`凱文交接文件`、`楊工作交接整理`、`11. 功能說明頁`、`競品分析`（網站指引／配對信／身分驗證）、
  `求才、求職組同步會議`（03/25、04/08、04/15）、`求職求才API > 廠商活躍度API`。
- **資深度訊號 / Seniority signal**：主動降低團隊風險、建立制度記憶——資深／lead 的關鍵行為。

### F7. 流程標準化與工具化 / Process Design & Tooling

**定義 / Definition**：不只完成任務，更把自身工作方法**抽象成可複用的標準與工具**，放大團隊產出。
*Don't just do the work — abstract your method into reusable standards and tooling that scale the team.*

- **實際展現 / In practice**：把規格慣例封裝成 `spec-doc-1111` skill（含求才／求職兩套範本與專案判別規則）；
  以 HackMD Folder API（`parentFolderId`／`folder-order`）程式化重建 307 份文件的**真實資料夾樹** `tree.md`。
- **工作證據 / Evidence**：`.claude/skills/spec-doc-1111/`（SKILL.md ＋ `template.md` ＋ `template-jobseeker.md`）；
  `tree.md`（由 Folder API 即時擷取重建）。
- **資深度訊號 / Seniority signal**：**元能力**——設計流程而不只執行流程；這是從資深個人貢獻者邁向 lead/PM 的分水嶺。

### F8. 專案管理：優先級、路線圖與交付節奏 / Roadmap Prioritization & Delivery Management

**定義 / Definition**：維護產品路線圖，將大量需求依優先級與工作量排序、分配至時間盒交付節奏，並追蹤計畫 vs 實際上線以確保準時交付。
*Own a product roadmap: rank a large request backlog by priority and effort, slot it into time-boxed delivery
cadences, and track planned-vs-actual launch to deliver on time.*

- **實際展現 / In practice**：
  - **優先級模型**：以 `P0–P3` 分級（P0＝資安／緊急，如 auth token httponly、封鎖詐騙 IP、移除 password）＋ `難易 0–3` 工作量評分。
  - **交付節奏**：以時間盒分級需求——`公司急件／2 週內交付／4 週內交付／排隊中`。
  - **狀態工作流**：`待辦 → 工程待辦 → 企劃執行 → 前／後端執行 → QA／企劃測試 → 待上線 → 已上線`；`暫停／取消` 一律附決策理由。
  - **計畫 vs 實際**：以 `封測日期／預計上線／實際上線` 三欄追蹤——**94%（84/89）準時或提前上線**；滑期項目記錄原因
    （如「公司簡介生成 API」預計 5/20 → 實際 6/4，因 QA 返修）。
  - **跨團隊關鍵路徑**：為含外部相依的專案排程（如「職缺健檢 API」5/5–6/17：開設計工單 → 串接資科 API → 切版 → 後端 → QA → 上線）。
  - **平行發布列車**：同時管理 `現版／新版／API／客服後台／TCode` 多軌；與 APP／求職主網跨產品同步上線。
  - **委派治理**：主導 **227 項 master roadmap**，將工單委派給 **3 人企劃團隊**（本人＋育琳／小楊）與工程，自身聚焦優先級與交付治理。
- **工作證據 / Evidence**：本人維護的**求才產品 Roadmap**（Google Sheet），227 項、111 項已上線（2026/01–06，約 5 個月）。
- **資深度訊號 / Seniority signal**：從「寫規格」躍升到「管路線圖、配資源、追準時、帶團隊委派」——**94% 準時交付**為可量化的交付績效，是帶專案、做取捨的 lead 行為。

### F9. 利害關係人管理與向上影響 / Stakeholder Management & Upward Influence

**定義 / Definition**：作為求才產品需求的單一窗口，平衡由上而下的高層指令與由下而上的第一線／客戶需求，透過例行溝通與數據決策對齊各方。
*Be the single intake point for a product's demand: balance top-down executive mandates against bottom-up
frontline/customer needs, aligning everyone through regular communication and data-driven decisions.*

- **實際展現 / In practice**：
  - **利害關係人廣度**：對接 **16 個需求單位**，從**總裁／董事長／策略長／多位協理副總**（C-suite 與董事層）
    到求才客服（109 件需求）、工程部、行動發展部、求職主網、稽核單位、系統中心。
  - **雙向需求匯流**：由上而下（策略長／董事的戰略指令）＋ 由下而上（**需求許願池／Team-Suggest** 的具名第一線建議），每筆需求皆可溯源。
  - **溝通節奏與共識**：每週固定向**近 200 人的業務團隊**做進度簡報（說明已上線與預計上線項目），並以 `晨會說明 → 蒐集建議 → 反修 → 收斂` 的回饋迴圈對齊需求方。
  - **以數據而非位階決策**：設計**結構化投票**讓近 200 人團隊共同決策（如「多筆職缺修改」審核機制、廠商「已下架」圖片標籤樣式、職缺須審核廠商的搜尋規則、求職／求才職缺瀏覽數顯示規則統一），如「AI 推薦人才：改為精準度排序」依「客服 5/26 投票結果」確定執行。
  - **取捨與衝突管理**：`暫停／取消` 一律附理由（如「系統內問卷系統」因 surveycake 已可串接而取消；「履歷新增證件資料」因求職流程調整先串接但暫不驗收）。
- **工作證據 / Evidence**：求才產品 Roadmap 的 `需求單位／需求來源／附註` 欄位（需求廣度、來源可溯、決策與取捨紀錄）。
- **資深度訊號 / Seniority signal**：對齊高層目標、協調多團隊、以數據而非位階做決策——資深 PM 最被期待的**向上與橫向影響力**。

### F10. 業務邏輯梳理 / Business-Logic Untangling

**定義 / Definition**：把散落、互相矛盾、隱含的業務規則，**盤整成窮盡且互斥（MECE）的決策邏輯**，作為規格與工程實作前的「單一真相來源」。這是 F2 的**上游**——先把業務真相釐清，才寫得出可驗收的規格。
*Untangle scattered, contradictory, and implicit business rules into a single MECE decision model — the source of
truth that precedes specs and engineering. This is upstream of F2: clarify the business truth before writing the spec.*

- **實際展現 / In practice**：
  - **規則盤整**：把分散在權限、審核、配對、續約等處的判斷，集中成單一規則集（如「權限判斷」表、職缺是否進審核的條件、配對的全文檢索／國籍／證照 AND 邏輯）。
  - **多重條件建模**：為複雜情境窮舉巢狀條件（如求職者「停權／關閉履歷」依姓名真偽 × 年齡 × 久未登入 × 註冊年資的多條件規則；論件薪資與薪資區間警示；語文證照分數顯示格式）。
  - **矛盾與邊界釐清**：找出規則衝突與例外並收斂（如香港公司完整地址不加東北亞、特定產業統編不撈商業司資料、過期廠商不顯示可暫停日期）。
  - **規則演進**：把人工／正則規則升級為系統或 AI 判斷（正則檢查改 AI 檢查、職缺審核導入 AI、AI 履歷／職缺打標）。
- **工作證據 / Evidence**：求才產品 Roadmap 與規格中的權限判斷、配對條件、審核規則、續約與資料清理條件；F2 的「權限代碼建模」即為本能力的輸出產物。
- **資深度訊號 / Seniority signal**：在規格之前先把「業務真相」釐清——降低反工與上線風險的**根因能力**，是把模糊變確定的源頭，而非下游的文件化。

### F11. 問題解決與維運交付 / Problem-Solving & Operational Delivery

**定義 / Definition**：作為求才系統維運與需求的單一處理窗口，接收第一線（業務／客服）與工程開立的工單，
快速**定位根因 → 拆解為可執行方案 → 以看板（Kanban）追蹤至上線結案**，在高工單量下維持高結案率。
*Single intake point for recruit-system ops and requests: triage incoming tickets (maintenance issues, planning
suggestions, engineering bugs), diagnose root cause, break them into actionable fixes, and track to launch on a
Kanban board while sustaining a high close rate under heavy ticket volume.*

- **實際展現 / In practice**：
  - **規模與結案率**：2026 年至今累計處理 **1,279 張工單**（維運問題／企劃建議／工程 bug），完成 **1,131 張、結案率約 88%**；每週穩定新增約 50–70 張、完成約 40–52 張。
  - **工單 → 看板 → 上線閉環**：接收業務團隊／客服開立的**具名、可溯源**工單（Team-Suggest 建議單，可追溯至公司與單號，如 `k=6237`／`6301`／`6252`），以 Kanban 追蹤狀態至上線並每週回報結案。
  - **根因定位（非表面修補）**：凌晨配對信數量異常 → 與工程調整配對機制並**持續監測至月底**驗證；AI 推薦人才名單過舊（多家廠商回報）→ 調整鄰近地區規則與名單排序邏輯；代碼體系老化 → 重整證照／工作專長／電腦專長／兼職職類代碼，並以**競品比對**補齊「對手有、我們沒有」的類別。
  - **缺陷處理廣度**：錯誤代碼、信件副本收件人刪除、即時通畫面裁切、感謝函範本無法帶入、紅利點數 hover 失效、過期廠商未發信客服等多類 bug 的定位與修復追蹤。
- **工作證據 / Evidence**：求才**週報**（每週「已處理項目／預計上線項目」清單與工單量統計：總量／已完成／未完成）、Team-Suggest 具名建議單、Kanban 專案看板。
- **資深度訊號 / Seniority signal**：在高工單量下維持約 **88% 結案率**，並把「修 bug」升級為「**根因定位＋機制調整＋上線驗證**」的閉環——可量化的維運交付績效。

| 職能 / Function | 資深 PM 期待 / Senior PM lens | 同領域轉職 / Spec-specialist lens |
| :--- | :--- | :--- |
| F1 產品定義全鏈路 | 從需求源頭定義產品、握有 what/why 決策權 | 即戰力：能獨立把模糊需求變成完整規格 |
| F2 規格與系統思維 | 把策略拆解為可執行、可驗收的範圍 | 高品質規格、低反工，RD/QA 無痛接手 |
| F3 廠商端平台＋公司頁 | B 端平台級掌握、理解 B→C 曝光連動 | 招募／HR Tech B 端領域可直接上手 |
| F4 AI 產品企劃（求才側） | 帶生成式／推薦 AI 產品、轉譯模型能力為價值 | 稀缺的生成式 AI 規格經驗，跨產業可遷移 |
| F5 交付流程與品質 | 可治理交付、管理變更與風險 | 成熟的版本控管與缺口管理習慣 |
| F6 跨職能協作／交接 | 團隊樞紐、建立制度記憶 | 文件化與溝通能力，降低 onboarding 成本 |
| F7 流程標準化／工具化 | 設計流程、放大團隊產出（lead 訊號） | 能帶入並提升新團隊的規格標準 |
| F8 專案管理／路線圖交付 | 管路線圖、配資源、追準時（94% on-time）、帶團隊委派 | 成熟的優先級與交付節奏管理，可直接接手 backlog |
| F9 利害關係人／向上影響 | 對齊 C-suite 目標、協調多團隊、用數據做決策 | 跨層級溝通與需求匯流能力，降低協作成本 |
| F10 業務邏輯梳理 | 把混亂規則盤成 MECE 決策邏輯、降低反工根因 | 規格上游的需求分析力，複雜規則一手接管 |
| F11 問題解決與維運交付 | 高工單量下根因定位、~88% 結案、看板追蹤至上線 | 即戰力維運窗口，工單→Kanban→上線閉環可直接接手 |

---

## 履歷可用摘要 / Resume-Ready Extract

> 動作＋範圍＋影響（action + scope + impact）。`〔待補數據〕` 處請補上實際數字後再對外使用。

- 端到端主導 **1111 求才（B 端）招募平台**的產品定義（公司／職缺／人才／聯繫／購買／紀錄各模組）並延伸負責求職端**公司頁**，
  從 user story／wireframe 到工程可實作的功能規格皆獨立產出，〔待補數據：本人撰寫份數〕。
  *Owned end-to-end product definition for the 1111 recruit (B-side) platform — plus the jobseeker company page —
  authoring specs from user story/wireframe through to engineering-ready, across 〔TODO: count〕 documents.*
- 定義並交付多項**求才側 AI 功能**：**公司簡介生成、JD 生成、職缺匯入、職缺健檢**（生成式）與 **AI 推薦人才名單**（推薦），
  將 LLM 能力轉譯為廠商可用的工作流，〔待補數據：採用率／使用量 adoption/usage〕。
  *Defined and shipped multiple employer-side AI features — company-profile generation, JD generation, job import,
  job health-check (generative) and AI talent recommendation — translating model capabilities into usable workflows.*
- **梳理複雜業務邏輯**：將散落於權限、審核、配對、續約等處互相矛盾的規則，盤整為窮盡互斥（MECE）的決策邏輯，
  作為規格與工程的單一真相來源，〔待補數據：涉及規則／模組數〕。
  *Untangled tangled business rules across permissions, review, matching, and renewal into a single MECE decision
  model — the source of truth for specs and engineering.*
- 建立**狀態驅動的規格方法論**（MECE 四狀態、權限代碼建模、條件邏輯），降低 RD/QA 反工與上線風險，
  〔待補數據：缺陷率／反工率下降 %〕。
  *Established a state-driven spec methodology (MECE four-state coverage, permission-code modeling) that reduced
  rework and release risk.*
- 設計可治理的**交付流程**（版本控管、🚧 缺口追蹤、分階段交付、變更標紅），讓規格可 diff、可追溯、可驗收。
  *Designed a governable delivery process (version control, gap tracking, staged delivery) making specs diffable,
  traceable, and verifiable.*
- 將個人規格慣例**標準化為可複用工具**（`spec-doc-1111` skill ＋ 雙系統範本 ＋ 程式化重建的文件樹），
  提升團隊規格一致性，〔待補數據：覆蓋人數／文件一致率〕。
  *Codified personal spec conventions into reusable tooling (a skill + dual-system templates + a programmatically
  rebuilt doc tree), lifting team-wide consistency.*
- 擔任 **PM／RD／QA／設計**間的樞紐，產出交接文件、功能說明頁、競品分析與跨組同步會議記錄，降低 key-person 風險。
  *Served as the cross-functional hub, producing handoff docs, feature guides, competitive analyses, and sync
  meeting notes that reduced key-person risk.*
- 主導 **227 項求才產品 Roadmap** 的優先級（P0–P3）與時間盒交付，委派工單給 3 人企劃團隊與工程，近半年交付 **111 項上線、94%（84/89）準時或提前**。
  *Owned a 227-item product roadmap — prioritization (P0–P3) and time-boxed delivery — delegating tickets to a
  3-person planning team and engineering; shipped 111 items in ~5 months at 94% (84/89) on-or-ahead-of-schedule.*
- 作為求才產品需求單一窗口，對接 **16 個利害關係單位**（總裁／董事／策略長／協理副總到第一線客服），平衡上層指令與第一線需求，並以數據（投票）而非位階做決策；每週向**近 200 人業務團隊**做進度簡報。
  *Acted as single intake point across 16 stakeholder units (from C-suite/board down to frontline CS), balancing
  top-down mandates with bottom-up needs and deciding by data (votes) rather than hierarchy; briefed a ~200-person
  business team on progress weekly.*
- 作為求才系統維運單一窗口，年度累計處理 **1,279 張工單**（維運／企劃建議／工程 bug），**結案率約 88%**（1,131 張），以**工單 → Kanban → 上線**閉環追蹤，並做**根因定位**（如配對信異常、AI 推薦名單過舊、代碼體系競品重整）而非表面修補。
  *Ran point on recruit-system operations, handling 1,279 tickets YTD (maintenance / planning / engineering bugs)
  at ~88% close rate (1,131 resolved), tracked ticket → Kanban → launch, and drove root-cause fixes (matching-email
  anomaly, stale AI recommendations, competitor-benchmarked code-table overhaul) rather than surface patches.*

---

## 下一步補強建議 / Growth Edges

> 誠實盤點：以下是「資深 PM」常被期待、但目前 repo 證據尚未充分呈現的面向，建議刻意累積。
> Honest gaps a Senior PM move typically expects that the current evidence doesn't yet show — worth building on purpose.

- **量化商業影響 / Quantified business impact**：補上轉換率、留存、營收、採用率等指標，把「做了什麼」升級為「帶來什麼結果」。
  *Attach metrics (conversion, retention, revenue, adoption) to move from output to outcome.*
- **A/B 測試與數據決策 / Experimentation ownership**：`tree.md` 已見埋點與 A/B 分流（如職缺配對信、功能埋點），
  可進一步呈現**從假設 → 實驗 → 決策**的完整 ownership。
  *Show end-to-end experiment ownership (hypothesis → test → decision), building on the existing tracking/A-B work.*
> ✅ 原列為缺口的 **優先級與路線圖** 及 **跨團隊／向上影響**，已由 **F8／F9**（求才產品 Roadmap 證據）補齊；
> **量化的維運交付結果**（1,279 工單／~88% 結案）亦由 **F11**（週報證據）部分補上。
> 下一步可再補上**商業／使用者指標**（轉換、留存、營收、AI 功能採用率），把交付與影響力連結到商業成效。
> *The former gaps "prioritization & roadmap" and "stakeholder & upward influence" are now covered by F8/F9
> (roadmap evidence), and quantified operational delivery (1,279 tickets / ~88% close rate) is partly covered by F11
> (weekly-report evidence); the remaining edge is tying this to business/user metrics (conversion, retention,
> revenue, AI-feature adoption).*

---

> 本文件依本 repo 既有證據（`spec-doc-1111` skill、`tree.md`）與本人第一手工作檔（Figma《求才用圖層》、求才產品 Roadmap）撰寫，
> 未捏造任何數據（量化數字均來自上述來源）；標示 `〔待補數據〕` 處為待補。
> Built from in-repo evidence (`spec-doc-1111` skill, `tree.md`) and the author's own first-party work files
> (the Figma《求才用圖層》file and the recruit product Roadmap); no metrics were invented — `〔待補數據〕` marks placeholders.
