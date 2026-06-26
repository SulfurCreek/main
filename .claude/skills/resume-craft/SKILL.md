---
name: resume-craft
description: >
  撰寫、修改、批改、優化使用者**個人履歷／CV／LinkedIn／作品集（portfolio）**，或把職能、經歷、專案成果轉成
  履歷 bullet、依特定職缺（JD）客製化履歷時使用。只要任務涉及「履歷」「resume」「CV」「自傳」「作品集」「portfolio」
  「case study」「LinkedIn」「投遞」「應徵」「求職」「JD 客製」「把 F1–F11 職能或專案變成履歷條目」，務必使用本 skill
  —— 即使使用者沒有明講「履歷」兩個字。
  本 skill 依**大型企業招募標準**（ATS 解析、核心職能叢集、量化影響 bullet、作品集案例研究、Amazon Leadership
  Principles 等）優化；以 **Senior PM / Product** 視角為主，**雙語**（英文 ATS 版 + 繁中在地版）。
  證據來源為 `career/competency-framework.md`（F1–F11、Resume-Ready Extract、`〔待補數據〕` 誠實標記）。
  ⚠️ 這是 `career/` 個人職涯工具，**不是 1111 規格書**：請勿套用 `spec-doc-1111`，請勿推送至 HackMD `1111-jobdocs`。
---

<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

# resume-craft — 個人履歷／作品集優化（大企業標準）/ Résumé & Portfolio Craft (big-corp standard)

把使用者的職能與經歷，轉成**過得了 ATS、6 秒內打中招募者、且不浮誇**的履歷與作品集。
本 skill 是 `career/competency-framework.md` 的下游：框架是「證據庫」，本 skill 是「把證據變成履歷的方法」。
*Turn the user's competencies and experience into a résumé/portfolio that passes ATS, lands in a recruiter's
6-second scan, and never overstates. This skill is downstream of `career/competency-framework.md`.*

---

## ⚠️ 先選市場版本（必做第一步）/ Pick the market variant FIRST

兩個市場的規則會**直接衝突**（照片、個資、長度、格式），動筆前先確認要做哪一份，再選對應範本：

| 市場 / Market | 範本 / Template | 形象照 | 個人資料 | 長度 | 格式重點 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 國際／英文（ATS）| `assets/template-ats-en.md` | **絕不放** | 只放 email/phone/LinkedIn/作品集連結；**不放**年齡/性別/婚姻/照片 | 1–2 頁 | 單欄、標準標題、無圖表、輸出 PDF/.docx |
| 台灣在地（繁中）| `assets/template-tw-zh.md` | 視公司而定，可放 | 可含照片；其餘個資仍建議精簡 | 1–2 頁 | 104／CakeResume 風格、可稍有設計但仍以可讀為先 |
| 雙語維護兩份 | 兩份都用 | 各依該市場 | 各依該市場 | 各自 1–2 頁 | **同一批成就、兩套排版**；改 A 記得同步 B |

> 衝突點口訣：**英文 ATS 版＝去照片、去個資、純文字單欄；繁中在地版＝可放照片、可加自傳。** 內容（成就 bullet）共用，包裝不同。
> ⚠️ Firewall：本 skill 僅處理 `career/` 個人職涯檔，**非規格書**；勿套 `spec-doc-1111`、勿推 HackMD。

---

## 何時使用 / When to use

- 批改或改寫既有履歷（指出弱點、重寫 bullet、調整結構、做 ATS 檢查）。
- 從 `career/competency-framework.md` **產出一份新履歷**（把 F1–F11 與 Resume-Ready Extract 轉成條目）。
- 把某項職能（F#）、某個專案、某段經歷**轉成 1–3 條量化 bullet**。
- 撰寫作品集 case study（problem → research → approach → results）。
- **依特定 JD 客製**：抽關鍵字、改 top-third、重排 bullet 順序。
- 優化 LinkedIn headline / About 段落（與履歷共用同一批成就）。
- **逆向**：把一段日常產出（規格書／週報／Figma／工單紀錄／流程圖）反推成 XYZ 影響力 bullet（見下方「逆向模式」）。

---

## 核心原則 / Core principles

1. **成果 > 職責 / Outcomes over responsibilities**：寫「做到什麼結果」，不是「負責什麼」。`負責 roadmap` → `主導 227 項 roadmap、94% 準時上線`。
2. **量化一切，沒數字就用代理指標 / Quantify, with proxies when scarce**：%、$、人數、用戶數、時程；若無硬指標，用
   **規模**（團隊/預算大小）、**速度**（8 週 vs 12 週）、**廣度**（觸及人數/單位數）、**流程改善**（週期縮短 X%）。
3. **ATS 安全 / ATS-safe**：單欄、標準標題、純文字、無圖表 icon；輸出 PDF 或 .docx。約 76% 履歷在見到人之前先被 ATS 刷掉。
4. **職能叢集，不是關鍵字清單 / Clusters, not a keyword dump**：技能分成 5–7 個職能叢集，每叢集附 1–2 個證據點。
5. **依 JD 客製 / Tailor per JD**：top-third（摘要＋前 2–3 條 bullet）鏡射 JD 用語；精準職稱 match 對命中率影響最大。
6. **誠實，絕不捏造 / No fabrication**：沿用框架的 `〔待補數據〕` 規則——**沒有的數字就標待補，不要編**。職稱用真實的；不確定是否主導就用 `contributed to` 而非 `led`。

---

## 履歷結構與順序 / Structure & order

實務上資深者用**混合式（hybrid）= 技能摘要在前 + 反時序工作經歷**最佳；**純功能式（functional）是地雷**（ATS 與招募者都不信任）。

| # | 區段（英文 ATS）| 區段（繁中在地）| 備註 |
| :-- | :--- | :--- | :--- |
| 1 | Contact + Headline | 姓名 + 一句定位 + 聯絡方式〔＋照片視情況〕| ATS 版去照片/個資 |
| 2 | Professional Summary（2–3 行）| 專業摘要 | **用摘要、不要 Objective**；含 2–3 個 JD 關鍵字 |
| 3 | Core Competencies（5–7 叢集）| 核心職能 | 叢集 + 證據點，非平鋪關鍵字 |
| 4 | Professional Experience（反時序）| 工作經歷（反時序）| 每段 3–6 條量化 bullet |
| 5 | Education & Certifications | 學歷 ／ 證照 | 年資 10+ 可移到經歷之後 |
| 6 | （選）作品集連結、發表、演講 | （選）自傳、作品集連結 | 繁中常見「自傳」；ATS 版不放自傳 |

> **Top-third 法則**：招募者前 6 秒以 F 型掃描第一頁上三分之一；最強的 2–3 個差異點**必須**出現在那裡。
> **長度**：中階 1 頁、資深（10+ 年）至多 2 頁；**絕不 3 頁**。

---

## ATS 規則 / ATS rules

| ✅ DO | ✗ DON'T |
| :--- | :--- |
| 單欄、左到右 | 多欄、側欄、文字方塊 |
| 標準標題（Experience / Education / Skills）| 自創標題（Wins / Highlights）|
| 標準字體（Arial/Calibri/Times，10–12pt）| 裝飾字體、彩色字、技能進度條 |
| 純文字 + 換行 | 圖片、icon、圖表、logo、表格化排版 |
| 日期/職稱平鋪 | 把日期塞進方框、用樣式藏資訊 |
| 輸出 **PDF 或 .docx** | HTML、把整頁存成圖片 |

**關鍵字策略（由高到低槓桿）**：① 精準鏡射 JD 的**職稱** → ② **Summary**（ATS 權重最高的段落）先放關鍵字 →
③ 硬技能關鍵字（軟技能初篩多被忽略）→ ④ **同時用** JD 的原句 + 語意等價詞（新系統懂語意、舊系統要原字）。

---

## Bullet 公式 / Bullet formula

**[強動詞] + [具體任務] + [量化結果]**，一條一個成就，1–3 行（約 30–40 字/words）。可套 **STAR**（情境-任務-行動-結果）。過去式寫過去職位、現在式寫現職。

**弱 → 強動詞 / Weak → strong verbs：**

| 弱 | 強（PM 適用）|
| :--- | :--- |
| Responsible for / 負責 | Owned, Spearheaded, Drove / 主導、推動 |
| Worked with / 協助 | Orchestrated, Aligned / 統籌、對齊 |
| Managed / 管理 | Led, Scaled, Directed / 帶領、規模化 |
| Increased / 增加 | Grew, Accelerated, Optimized / 提升、加速、優化 |
| Made / 做了 | Shipped, Architected, Validated / 交付、設計、驗證 |

**Before → After：**
- ✗ `負責產品 roadmap` → ✅ `主導 227 項求才產品 roadmap，以 P0–P3 分級與時間盒交付，半年 111 項上線、94%（84/89）準時或提前`
- ✗ `Worked with engineering on a launch` → ✅ `Orchestrated a cross-functional launch (12 eng, 4 design, data) and shipped in 6 weeks vs. 12-week plan`
- ✗ `負責跨部門溝通` → ✅ `作為求才需求單一窗口，對接 16 個需求單位（總裁/董事/策略長到第一線客服），以數據（投票）化解衝突優先級`

**沒硬指標時的代理指標**：規模（5 工程師 / $2M 預算 / 500K 用戶）、速度（8 週 vs 12 週）、廣度（16 單位 / 30+ PM 採用）、流程（規劃週期 6 週→2 週）。

---

## 核心職能叢集 / Core competency clusters

技能段落用 **5–7 個叢集**，每叢集 **1–2 個證據點**（規模/速度/成果），而非 20 個散落關鍵字。資深訊號＝**範圍、模糊度、跨職能影響、商業成果**。

| 叢集 / Cluster | 對應使用者職能 / Maps to | 證據點範例 |
| :--- | :--- | :--- |
| Product Strategy & Vision / 產品策略 | F1, F3 | roadmap/市場分析/多季規劃；平台級 B 端掌握 |
| Execution & Delivery / 執行與交付 | **F8**, F5 | 227 項 roadmap、94% 準時、版控與缺口治理 |
| Data & Experimentation / 數據與實驗 | F4（部分）, Growth Edge | A/B、埋點、SQL；〔待補：實驗數〕|
| Stakeholder Mgmt & Influence / 利害關係人與向上影響 | **F9**, F6 | 對接 16 單位、C-suite 對齊、數據決策 |
| Business Logic & Requirements / 業務邏輯梳理 | **F10**, F2 | 盤整權限／審核／配對／續約規則為 MECE 決策邏輯；多重條件建模；後端邏輯重構（追蹤識別碼定義與狀態拆分）、API 整合協定設計 |
| Technical Fluency / 技術素養 | F2, F4 | 狀態驅動規格、權限代碼建模、API 串接；循序圖／活動圖／使用案例圖／BPMN 建模、Markdown 規格書、設計稿轉前端規格、欄位檢核與防呆、AI 模組導入 |
| AI Product / AI 產品 | **F4** | 生成式（公司簡介/JD 生成）+ 推薦（AI 推薦人才）|
| Problem-Solving & Ops / 問題解決與維運 | **F11** | 年處理 1,279 工單、~88% 結案；工單→Kanban→上線閉環；根因定位；工單幾乎全來自付費廠商→連結客戶留存與業績 |
| Process & Tooling / 流程與工具化 | F7 | spec-doc-1111 skill、程式化重建文件樹 |

**叢集寫法（強）**：`執行與交付 — roadmap 優先級（P0–P3）、時間盒交付、版控治理；主導 227 項 roadmap，半年 111 項上線、94% 準時。`
**平鋪關鍵字（弱，勿用）**：`產品管理、roadmap、A/B、Agile、SQL、溝通、領導、策略…`

> **系統分析 (SA) 視角 / SA lens**：應徵偏系統分析／技術型 PM 時，特別凸顯三條證據線（皆已對映上表，與 F2／F10／F4 共用同一批成就）：
> - **系統架構與規格設計**：以 Markdown 撰寫高可讀性規格書；以 **循序圖（sequence）／活動圖（activity）／使用案例圖（use case）／BPMN** 建模系統互動與流程（循序圖、活動圖以 Mermaid 等 AI 工具加速，使用案例圖／BPMN 手繪）。
> - **技術整合與重構**：API 整合協定設計、後端邏輯重構（如追蹤識別碼定義與狀態拆分）、AI 模組導入。
> - **UI/UX 對接**：設計稿轉前端開發規格、建立欄位檢核標準與系統防呆機制。
>
> 寫成 bullet 時套「Bullet 公式」的 **STAR**：情境/任務（系統痛點，如重構舊有追蹤邏輯）→ 行動（重新定義單一識別碼架構、撰寫含 API 與資料庫綱要的技術規格書）→ 結果（確保開發邏輯合規、提升跨工程團隊對接效率）。

**Junior → Senior 訊號：**

| Junior | Senior |
| :--- | :--- |
| 做使用者研究 | 綜整 100+ 訪談，重新定義產品策略 |
| 做 A/B 測試 | 建立實驗框架，年跑 50+ 實驗 |
| 排 roadmap | 帶 2 年策略歷經 3 次轉向，對齊 20 人團隊 |
| 跨部門溝通 | 取得 C-suite 信任、推動 2 個有爭議的 roadmap 轉向 |

---

## 作品集 / Portfolio

**何時放連結**：資深 PM（5+ 年）**預期要有**；轉職進 PM、成長型角色也建議放。放在 **header**（與 LinkedIn 並列），勿塞進工作經歷 bullet。

**Case study 結構（problem → research → approach → results）**，每篇 400–800 字，詳見 `assets/portfolio-case-study.md`：
1. **問題/背景**：使用者痛點 + 量化現況（含 benchmark）。
2. **研究與洞察**：怎麼理解問題（訪談片段、漏斗、競品）——展示思路，不只結論。
3. **方法與取捨**：為何選這個解（wireframe、PRD 摘錄、假設、實驗設計、取捨）。
4. **結果與學習**：量化成果 + 學到什麼，**至少放一個誠實的失敗實驗**（比「完美」更可信）。

**履歷 ↔ 作品集分工：**

| 元素 | 履歷 | 作品集 |
| :--- | :--- | :--- |
| 內容 | 一行 + 量化結果 | 完整 problem→思路→結果 |
| 深度 | 只給結果 | 過程、取捨、迭代 |
| 素材 | 無 | wireframe/PRD/圖表/回饋 |
| 失敗/迭代 | 不提 | 核心，要展示 |
| 閱讀 | 6 秒掃 | 有興趣才細讀 5–15 分 |

**3–5 篇即可**（深度 > 數量）；用真實素材但**勿放機密 1111 資料**（去識別化或用個人專案）。

---

## 大企業訊號 / Big-corp signals

**Amazon Leadership Principles**（每關都考；讓 bullet 對映 4–5 條）：

| 原則 | 履歷訊號 | 範例 |
| :--- | :--- | :--- |
| Customer Obsession | 以用戶為中心、影響客戶指標 | 50+ 訪談洞察驅動功能，NPS +12、流失 -15% |
| Ownership | 端到端當責（owned 不是 supported）| 主導 onboarding，留存 +22pt |
| Invent and Simplify | 創新 + 化繁為簡 | 7 步簡化為 3 步，完成率 +60% |
| Dive Deep | 細節分析、非表面 | 分析 500K cohort + session 找出流失主因 |
| Bias for Action | 速度與決斷 | 驗證迴圈 2 週 vs 6 週 |
| Deliver Results | 量化成果、達標 | 12 功能準時、$3M ARR、零重大上線 bug |
| Earn Trust | 跨團隊信任 | C-suite 三項策略決策的信任顧問 |

**Google**：系統/規模思維、清楚的數據敘事、成長指標。 **Meta**：快速實驗、成長/互動、加速工程速度、排序/推薦系統。
**McKinsey（策略職）**：清楚商業影響、建議 > 執行、市場洞察、影響範圍（C-suite/跨組採用）。

---

## 依 JD 客製 / Tailor per JD（每次投遞 10–15 分）

1. 從 JD 抽關鍵字（職稱、硬技能、框架、動詞）。
2. 找差距：哪些 JD 用語履歷沒有？**屬實**就補上。
3. 改 top-third：Summary + 前 2–3 條 bullet 用 JD 語言。
4. 重排 bullet：把對應 JD 最高要求的成就放最前。
5. 過 ATS 檢查：單欄、標準字體、標準標題。

> 同時用 **JD 原句 + 語意等價詞**（如 "ARR growth" ≈ "revenue expansion"）以同時通過新舊系統。

---

## 反面模式 / Red flags（務必避免）

| 反面模式 | 為何傷 | 修法 |
| :--- | :--- | :--- |
| 職責而非成就 | `Responsible for…` 沒說明結果 | 改成量化成就 |
| Buzzword 堆砌、無數字 | 空泛、像低階 | 加人數/%/$/時程 |
| 多欄、圖表、icon | ATS 解析失敗 | 純文字單欄 |
| 平鋪關鍵字技能段 | 看起來 junior | 改職能叢集 + 證據點 |
| 資深卻無作品集 | 訊號薄弱 | 補 3–5 篇 case study |
| 灌水職稱 / 編造數字 | 被查核即失信，77% 招募者立刻刷 | **誠實**；不確定用 `contributed to` |
| 全通用、不客製 | ATS 與人都看得出 | 客製 top-third |
| AI 腔（realm/intricate/pivotal/showcasing）| 易被判 AI 生成 | 用自己的口吻、念出來檢查 |
| 錯字、文法 | 58% 招募者直接刷 | 校對 3 次 + 工具 + 真人 |

---

## 從職能框架產出 / Build from the competency framework

要產出或更新履歷時，以 `career/competency-framework.md` 為唯一證據源：

1. 取 **Resume-Ready Extract**（7 條 action+scope+impact）作為 bullet 草稿基底。
2. 取 **F1–F11** → 映射到上方「核心職能叢集」表，挑 5–7 個最相關的成叢集。
3. 取 **Profile Snapshot / Positioning** → 寫 Summary/Headline。
4. 遇到 `〔待補數據〕`：**先問使用者拿真實數字**；拿不到就**保留待補標記**，不要編。
5. 依目標 JD 與市場版本（ATS/繁中）選範本、客製 top-third。
6. 產出後跑下方檢查清單。

> ⚠️ 框架與履歷都遵守「不捏造」契約：量化數字必須有來源（roadmap、Figma、實際指標）。

---

## 逆向模式：產出 → XYZ 影響力 bullet / Reverse mode: raw output → XYZ impact bullet

「正向」是框架 → 履歷；「逆向」是把一段**日常產出**（規格書、週報、Figma、工單紀錄、流程圖）反推成履歷 bullet。
扮演角色：**精通矽谷科技業標準的資深獵頭／履歷教練**。三步驟：

1. **職能萃取 / Competency extraction**：從產出中用到的**工具與思維**（Mermaid／循序圖、Markdown 規格、權限代碼建模、Kanban 工單治理、資料結構重構…）反推對應 PM 職能，並**對映回 F1–F11**——不要發明新職能，先連回框架。
2. **XYZ 句型重構 / XYZ formula**：`達成／主導 [X 影響力或產品模組]，透過 [Z 技術／管理方法]，解決了 [Y 複雜度或痛點]`。
   等價於 Google XYZ：*Accomplished [X] by doing [Z], solving [Y]*。**X＝結果、Z＝方法、Y＝痛點/複雜度**。
3. **技術 × 商業雙語轉譯 / Bilingual PM pitch**：同一條 bullet 同時帶**商業價值**（營收保護、續約、降低溝通成本、定價策略）與**技術含金量**（API 串接邏輯、防呆機制、資料結構重構、狀態建模），並產出**中英兩版**。

### 輸出格式 / Output format

- **【原產出概述】**：一句話描述輸入素材。
- **【展現的核心職能】**：2–3 個 PM 關鍵能力（標註對映 `F#`）。
- **【履歷黃金亮點】**：**3 種不同動詞強度**的選項（穩健 → 進取 → 主導），讓使用者挑語氣。

> ⚠️ **誠實護欄（沿用全域不捏造契約）**：XYZ 的 X／Y 若無真實數字，用**代理指標**（規模／速度／廣度／流程改善）或保留 `〔待補數據〕`，**絕不為了句型漂亮而編造**。技術詞也須屬實——手繪 vs AI 輔助、`contributed` vs `led`、結案率有來源才寫。

### 範例 / Worked example（取自 F11 維運工單）

- **【原產出概述】**：每週求才系統週報——工單量統計＋已上線／待上線清單；工單幾乎全來自付費中廠商。
- **【展現的核心職能】**：問題解決與維運交付（F11）、利害關係人溝通（F9）、根因分析（F11／F2）。
- **【履歷黃金亮點】**
  1. （穩健）*Resolved 1,279 paying-customer support tickets at ~88% close rate via a ticket→Kanban→launch loop, protecting account experience and renewals.*
  2. （進取）*Drove a ~88% close rate across 1,279 paying-account tickets by standing up a ticket→Kanban→launch ops loop with root-cause fixes — safeguarding the sales team's revenue retention.*
  3. （主導）*Owned recruit-system operations end-to-end as single intake, clearing 1,279 paying-customer tickets (~88% closed) through root-cause remediation (matching engine, AI recommendations, code-table overhaul) to defend renewal revenue.*
  - 中文（主導版）：**主導**求才維運單一窗口，以「工單→Kanban→上線」閉環與根因修復清理 **1,279 張付費廠商工單（~88% 結案）**，守住續約營收。

### NVIDIA-tier（硬技術、零廢話升級版）/ Deep-tech zero-fluff escalation

應徵**硬技術公司／技術型 PM**（NVIDIA、平台／基礎設施、infra）時，把上面的 XYZ 再升一級。
扮演角色：深諳 NVIDIA 價值觀（**Intellectual Honesty、Deep Tech Competence、Speed & Agility**）的首席技術招募官。

1. **剔除冗餘 ＋ 誠實盤點 / Intellectual honesty check**：刪掉所有空泛形容詞（成功地／極大地／successfully／significantly），盤點**真實技術細節**——特定 API 協議與端點、系統代碼對照、資料庫欄位規則、驗證邊界條件。
2. **架構 → 商業瓶頸掛鉤 / Tech-to-business**：把系統架構對應到它解掉的商業瓶頸（跨系統串接延遲、計價精準度、付費客戶留存）。
3. **XYZ（NVIDIA 定義）**：**X**＝具體系統優化／商業規模；**Y**＝克服的高複雜度歷史包袱或架構限制；**Z**＝制定的核心系統規範或技術實作路徑。

**輸出格式 / Output format：**

- **【技術深度盤點】**：條列硬核 PM 職能（API 邏輯定義、資料結構設計、複雜業務邏輯降維、跨系統訊息路由建模…）。
- **【Nvidia-Tier 履歷亮點】**：3 句，每句必含**具體資料流向／系統機制／計價模型**；**嚴禁** AI 客套與華麗修辭（realm／intricate／pivotal／seamlessly／成功地／極大地）。

> ⚠️ **對外履歷務必抽象化專有資訊**：可寫「整合兩條 legacy 通道為單一即時對話流」，但**勿外露** 1111 內部 API 名、欄位名、權限代碼（機密）。Intellectual Honesty ≠ 揭露公司機密。

**範例 / Worked example（取自旗艦專案：跨系統聯絡人才，已抽象化）：**

- **【技術深度盤點】**：跨系統即時訊息架構（B 端 ↔ C 端）、即時推送機制、雙來源訊息流合併（即時通＋信件）、邀約狀態機、跨系統面試行事曆寫入、欄位級 API 規格與向後相容遷移。
- **【Nvidia-Tier 履歷亮點】**
  1. *Unified two previously separate messaging channels (instant messaging + mail) into a single real-time conversation stream across the employer and jobseeker platforms, defining the message-routing model and dual-view data structures that eliminated cross-system sync gaps.*
  2. *Specified end-to-end APIs (list + conversation-detail) down to field-level contracts and an invitation state machine, enabling engineers to build cross-system real-time delivery (SignalR) without ambiguity.*
  3. *Drove backward-compatible incremental migration — bridging the legacy system via embedded iframes while shipping the new unified chatroom — so no existing recruiter workflow broke during cutover.*

---

## 交付前檢查清單 / Pre-delivery checklist

- [ ] **市場版本已選**（ATS-EN / 繁中 / 雙語），用對應範本；ATS 版已去照片與個資。
- [ ] **ATS 格式**：單欄、標準字體、標準標題、無圖表 icon、輸出 PDF/.docx。
- [ ] **Top-third 衝擊**：Summary + 前 2–3 bullet 鏡射 JD、6 秒看得到 2–3 個差異點。
- [ ] **Bullet 公式**：每條 = 強動詞 + 任務 + 量化結果，1–3 行。
- [ ] **量化覆蓋**：≥ 80% bullet 有數字（%/$/人數/時程/用戶/留存）；無硬數據處用代理指標。
- [ ] **職能叢集**：5–7 叢集 + 證據點，非平鋪關鍵字；已映射 F1–F11。
- [ ] **作品集**：資深者於 header 放連結；3–5 篇 problem→research→approach→results（含一個失敗實驗）。
- [ ] **大企業訊號**：對映 4–5 條 Amazon LP / 目標公司價值；範圍、模糊度、跨職能影響、商業成果到位。
- [ ] **強動詞**：spearheaded/orchestrated/architected/shipped/scaled/validated，非 responsible for/helped。
- [ ] **無紅旗**：無錯字、無 buzzword 堆砌、**無捏造數字**、無 AI 腔、無未解釋空檔。
- [ ] **誠實**：所有 `〔待補數據〕` 要嘛填真實數字、要嘛保留標記；職稱屬實。
- [ ] **長度與格式**：1–2 頁；hybrid 或反時序（非純 functional）。
- [ ] **雙語同步**（若維護兩份）：成就一致，僅包裝/語言不同。
