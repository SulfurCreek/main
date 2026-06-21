<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

> ⚠️ **個人職涯資料，非 1111 規格文件 / Personal career material — NOT a 1111 spec.** 請勿套用 `spec-doc-1111`
> skill，也勿推送至 HackMD `1111-jobdocs` 團隊工作區。詳見 `career/CLAUDE.md`。
> *Do not apply the spec-doc-1111 skill or push to the HackMD team workspace; see `career/CLAUDE.md`.*

# 職能框架 / Competency Framework

> **用途 / Purpose**：作為下一步職涯（**資深產品經理 Senior PM** 或 **同領域轉職 same-craft move**）的職能盤點。
> 每一項職能都附上可追溯的工作證據（出自本 repo 的 `spec-doc-1111` skill 與 `tree.md` 文件清單中本人負責的範圍）。
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

---

## 職能對應下一步 / Function → Role Mapping

| 職能 / Function | 資深 PM 期待 / Senior PM lens | 同領域轉職 / Spec-specialist lens |
| :--- | :--- | :--- |
| F1 產品定義全鏈路 | 從需求源頭定義產品、握有 what/why 決策權 | 即戰力：能獨立把模糊需求變成完整規格 |
| F2 規格與系統思維 | 把策略拆解為可執行、可驗收的範圍 | 高品質規格、低反工，RD/QA 無痛接手 |
| F3 廠商端平台＋公司頁 | B 端平台級掌握、理解 B→C 曝光連動 | 招募／HR Tech B 端領域可直接上手 |
| F4 AI 產品企劃（求才側） | 帶生成式／推薦 AI 產品、轉譯模型能力為價值 | 稀缺的生成式 AI 規格經驗，跨產業可遷移 |
| F5 交付流程與品質 | 可治理交付、管理變更與風險 | 成熟的版本控管與缺口管理習慣 |
| F6 跨職能協作／交接 | 團隊樞紐、建立制度記憶 | 文件化與溝通能力，降低 onboarding 成本 |
| F7 流程標準化／工具化 | 設計流程、放大團隊產出（lead 訊號） | 能帶入並提升新團隊的規格標準 |

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

---

## 下一步補強建議 / Growth Edges

> 誠實盤點：以下是「資深 PM」常被期待、但目前 repo 證據尚未充分呈現的面向，建議刻意累積。
> Honest gaps a Senior PM move typically expects that the current evidence doesn't yet show — worth building on purpose.

- **量化商業影響 / Quantified business impact**：補上轉換率、留存、營收、採用率等指標，把「做了什麼」升級為「帶來什麼結果」。
  *Attach metrics (conversion, retention, revenue, adoption) to move from output to outcome.*
- **A/B 測試與數據決策 / Experimentation ownership**：`tree.md` 已見埋點與 A/B 分流（如職缺配對信、功能埋點），
  可進一步呈現**從假設 → 實驗 → 決策**的完整 ownership。
  *Show end-to-end experiment ownership (hypothesis → test → decision), building on the existing tracking/A-B work.*
- **優先級與路線圖 / Prioritization & roadmap**：補上需求排序框架、roadmap、trade-off 決策的產出物，
  證明在資源受限下做取捨的能力。
  *Add prioritization frameworks, roadmaps, and trade-off artifacts demonstrating resource-constrained decisions.*
- **跨團隊／向上影響 / Stakeholder & upward influence**：呈現對齊高層目標、協調多團隊、影響策略方向的案例。
  *Surface examples of aligning leadership goals and influencing strategy across teams.*

---

> 本文件依本 repo 既有證據（`spec-doc-1111` skill、`tree.md`）撰寫，未捏造任何數據；標示 `〔待補數據〕` 處為待補。
> Built solely from in-repo evidence; no metrics were invented — `〔待補數據〕` marks placeholders to fill in.
