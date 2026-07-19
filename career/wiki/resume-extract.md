<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

> 🧭 [← 職能框架首頁 / Home](../competency-framework.md) ｜ `career/` 個人職涯 wiki 分頁，非 1111 規格文件（規則見 [`career/CLAUDE.md`](../CLAUDE.md)）

# 履歷可用摘要 / Resume-Ready Extract

> 動作＋範圍＋影響（action + scope + impact）。`〔待補數據〕` 處請補上實際數字後再對外使用。
> 產履歷時以本頁為 bullet 草稿基底，方法見 `resume-craft` skill（Bullet 公式／逆向模式／AI 掃描優化）。

- 端到端主導 **1111 求才（B 端）招募平台**的產品定義（公司／職缺／人才／聯繫／購買／紀錄各模組）並延伸負責求職端**公司頁**，
  從 user story／wireframe 到工程可實作的功能規格皆獨立產出，〔待補數據：本人撰寫份數〕。
  *Owned end-to-end product definition for the 1111 recruit (B-side) platform — plus the jobseeker company page —
  authoring specs from user story/wireframe through to engineering-ready, across 〔TODO: count〕 documents.*
- 定義並交付**跨系統即時訊息**旗艦功能，打通廠商端與求職者端兩套平台：以即時推送（SignalR）將原本分離的即時通與信件**兩條 legacy 通道**統一為單一對話流，建模跨系統訊息路由、邀約狀態機與跨系統面試行事曆寫入，並產出端到端 API 與**欄位級規格**、相容既有系統做漸進遷移。
  *Defined and shipped a flagship cross-system real-time messaging feature bridging the employer and jobseeker
  platforms: unified two separate legacy channels (instant messaging + mail) into one conversation stream via
  real-time push (SignalR), modeling cross-system message routing, an invitation state machine, and cross-system
  interview-calendar writes, with end-to-end API and field-level specs and backward-compatible incremental migration.*
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
- 主導 **227 項求才產品 Roadmap** 的優先級（P0–P3）與時間盒交付，**直屬管理 2 名企劃**（蔡育琳、楊丞佳）並委派工單給工程，近半年交付 **111 項上線、94%（84/89）準時或提前**。
  *Owned a 227-item product roadmap — prioritization (P0–P3) and time-boxed delivery — directly managing 2 product
  planners and delegating to engineering; shipped 111 items in ~5 months at 94% (84/89) on-or-ahead-of-schedule.*
- 作為求才產品需求單一窗口，對接 **16 個利害關係單位**（總裁／董事／策略長／協理副總到第一線客服），平衡上層指令與第一線需求，並以數據（投票）而非位階做決策；每週向**近 200 人業務團隊**做進度簡報。
  *Acted as single intake point across 16 stakeholder units (from C-suite/board down to frontline CS), balancing
  top-down mandates with bottom-up needs and deciding by data (votes) rather than hierarchy; briefed a ~200-person
  business team on progress weekly.*
- 作為求才系統維運單一窗口，年度累計處理 **1,279 張工單**（維運／企劃建議／工程 bug），**結案率約 88%**（1,131 張）；經與客戶名冊交叉實證，具名工單 **96.5% 來自開單當時付費中的廠商**、管線觸及 **1,109 家相異付費帳號**（公開牌價估算年約當刊登價值 **NT$3–5 千萬量級**），被服務客群至今仍付費比例 **85.5%（約為全體基準 44% 的 1.9 倍）**——以**工單 → Kanban → 上線**閉環與**根因定位**（配對信異常、AI 推薦名單過舊、代碼體系競品重整）維護付費客戶體驗、**支撐業務業績與續約**。
  *Ran point on recruit-system operations, resolving 1,279 tickets YTD at ~88% close rate (1,131); verified against
  the customer roster, 96.5% of vendor-named tickets came from accounts paying at filing time, the pipeline reached
  1,109 distinct paying employer accounts — an annualized posting value on the order of NT$30–56M (US$1M+) at list
  price — and serviced accounts remain paying at 85.5% today (~1.9× the 44% all-customer baseline) — via a
  ticket → Kanban → launch loop and root-cause fixes (matching-email anomaly, stale AI recommendations,
  competitor-benchmarked code-table overhaul), protecting paying-customer experience and the sales team's revenue
  retention.*

---

**相關分頁 / Related**：[旗艦專案 E.1](flagship-e1.md) ・ [學歷與證照](education-certifications.md) ・ [下一步補強建議](growth-edges.md)
