---
name: resume-craft
description: >
  撰寫、修改、批改使用者個人履歷／CV／LinkedIn／作品集，或把職能、經歷、專案成果轉成履歷 bullet、依 JD 客製化時使用。
  觸發詞：履歷、resume、CV、自傳、作品集、portfolio、case study、LinkedIn、投遞、應徵、求職、JD 客製、
  求職信、自我推薦信、推薦函、cover letter、應徵信、
  把 F1–F15 職能或專案變成履歷條目——使用者沒明講「履歷」兩字也算。
  以 Senior PM / Product 視角、大型企業招募標準（含 ATS 與 AI／LLM 履歷掃描）優化，雙語（英文 ATS 版 + 繁中在地版）。
  證據來源是 `career/` 的職能框架 wiki。
---

<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

# resume-craft — 個人履歷／作品集優化（大企業標準）

把使用者的職能與經歷，轉成**過得了 ATS（含 AI/LLM 掃描）、6 秒內打中招募者、且不浮誇**的履歷與作品集。
本 skill 是證據庫的下游：`career/library/`（**使用者確認過的現行事實與裁定，衝突時最優先**）→ `career/competency-framework.md`（wiki 入口）＋ `career/wiki/` 分頁存「證據」，
本 skill 是「把證據變成履歷的方法」。

## 🔁 標準工作流程（9 步，2026-10-08 使用者裁定、2026-10-09 修訂）

做履歷、自傳、求職信素材一律走這九步，不跳步、不只拿上一版刪修。詳細產出、出口條件、回退規則見 [`references/workflow.md`](references/workflow.md)（中間產物放 `career/drafts/<版本>/`）。

| # | 步驟 | 做什麼 | 工具／規則 |
| :-- | :--- | :--- | :--- |
| 1 | 調用職能與職缺 | 讀 `career/library/`、F01–F15、交付鏈 14 項；讀目標 JD（`career/104/jd-digest-A.md`），列必備詞與加分詞；職缺進 career-ops pipeline | 本檔「從職能框架產出」、career-ops |
| 2 | 蒐集證據 | 每職能一張證據表；缺口一次問一題，答案先寫 library | `superseded.md` 比對 |
| 3 | 每項目寫成小 essay | 150–400 字：處境、決定、做法與產出文件、協作、結果、角色邊界；對照 JD 加分條件；**文末標出 X 結果／Y 指標／Z 做法**；AI 要寫怎麼用、產出什麼 | `career/style/ats-2026-source.md`、`hr-6-second-source.md` |
| 4 | 精簡×20 版本 | 每個單位（摘要、每條條列、技能、自傳每段）寫 20 版，機械分＋人工分，**只留最高分**，組裝成最完整履歷；組裝時套 6 秒版面（抬頭職稱在左、相關性刪減） | `scripts/resume_score.py variants`、本檔 Bullet 公式與〈6 秒版面〉、`tw-voice.md` |
| 5 | 去 AI 感 | 讀者角度逐句標 AI 腔、整齊過頭、通用句、無來源感受 | `anti-ai-ats.md`、`career/style/resume-voice-zh.md` |
| 6 | HR 檢測 | **先做 6 秒 F 型初篩**（另一個模型只看 F 型視野），再做人資 H1–H10＋HR-A…J＋作廢比對＋覆蓋核對 | skill `resume-review-panel`（`scripts/f_scan.py`） |
| 7 | **ATS 檢測** | 依算分表 100 分：格式、關鍵字對應（不塞詞）、6 秒可讀（C v2）、量化、AI 實證 | `career/style/ats-2026-source.md`、career-ops `verify-ats`、`scripts/resume_score.py ats` |
| 8 | 用人主管檢測 | M1–M10＋HM-A…H（含交付鏈）；順序 HR → ATS → 主管 | skill `resume-review-panel` |
| 9 | 定版 | 閘門全過（含 ATS ≥ 75）＋使用者核可措辭，才產 txt／PDF、歸檔、更新指標；career-ops `verify-cv-facts` | `workflow.md` 步驟 9 |

> 6、7、8 發現問題依 `workflow.md`〈回退規則〉回到對應步驟；**不可只為審查分數改稿**，每個改動要對得回 library 事實或使用者裁定。

---

## 🗺️ 任務路由 / Task routing

本檔只放**每次都用得到的核心**；其餘按需載入 `references/`：

| 任務 | 讀什麼 | 證據分頁（`career/`）|
| :--- | :--- | :--- |
| 產履歷／改版（任何版本） | **先走上方 9 步工作流程**，細節見 [`references/workflow.md`](references/workflow.md) | `career/library/` → `competency-framework.md` → 相關 F 分頁 |
| 改寫 bullet／把日常產出變 bullet | 本檔 Bullet 公式 ＋ [`references/reverse-xyz.md`](references/reverse-xyz.md) | 對應 `wiki/F0x-*.md` |
| 投遞硬技術公司（NVIDIA-tier）| [`references/reverse-xyz.md`](references/reverse-xyz.md) | `wiki/flagship-e1.md`、`wiki/F02`、`wiki/F10` |
| 依 JD 客製／ATS／HR 用 AI 掃履歷 | [`references/ats-and-ai-screening.md`](references/ats-and-ai-screening.md) | `wiki/resume-extract.md` |
| 作品集 case study | [`references/portfolio.md`](references/portfolio.md)（含市場路由、NDA 去識別化）＋ 範本：外商／英文 [`assets/portfolio-case-study.md`](assets/portfolio-case-study.md)；台灣本土／新創 [`assets/portfolio-case-study-tw.md`](assets/portfolio-case-study-tw.md) | `portfolio/e1-cross-system-messaging.md`（範例）。**內部版輸出位置固定在 `career/portfolio/`；要上網站的篇章另產對外版 `career/portfolio/public/`（規則見 `references/portfolio.md`〈對外版〉）；career 內容禁止寫入 HackMD**（`career/CLAUDE.md` 硬規則二）。 |
| 6 秒篩選、F 型版面、XYZ、相關性刪減（排版與組裝時必讀）| `career/style/hr-6-second-source.md`（原文＋與既有裁定的衝突處理）＋本檔〈6 秒版面〉 | — |
| 去 AI 感、ATS 格式、CAR 盤問（交付前必做）| [`references/anti-ai-ats.md`](references/anti-ai-ats.md)：掃禁用詞與破折號、空泛條目先停下來問 Context／Action／Result，問不到不補數字 |
| 撰寫中文履歷／自傳／專案說明（語氣與誇大護欄）| [`references/tw-voice.md`](references/tw-voice.md) | 數字與事實只取自 `wiki/` |
| 產生／填寫／驗證 **104 履歷** | 先讀 `career/104/README.md`（`fields-spec.md` 欄位規格、`resume-104.md` 內容、現行版見 README 標示（以 README 為準，不要寫死版本號））；**Cake Resume 另案，不得套用 104 的欄位規格與字數上限**；語氣依 [`references/tw-voice.md`](references/tw-voice.md) | 這些檔案在個人線分支 `claude/happy-lamport-ljis8c` 的 `career/104/` |
| 求職信：中文自我推薦信（英文 cover letter 走 career-ops `cover` 模式）| [`references/cover-letters.md`](references/cover-letters.md) ＋ 範本 [`assets/cover-letter-tw-zh.md`](assets/cover-letter-tw-zh.md) | `letters/story-bank.md`（數字唯一來源）；成品存 `letters/archive/` ＋ `letters/log.md` 加一列 |
| 目標公司價值觀對映（Amazon LP 等）| [`references/portfolio.md`](references/portfolio.md) | — |
| 高顏值可列印版（HTML／LaTeX）| [`references/visual-output.md`](references/visual-output.md) | 已定稿的內容版履歷 |
| 填學歷／證照 | 本檔結構與順序 | `wiki/education-certifications.md` |

---

## ⚠️ 先選市場版本（必做第一步）

兩個市場的規則會**直接衝突**（照片、個資、長度、格式），動筆前先確認做哪一份：

| 市場 | 範本 | 形象照 | 個人資料 | 格式重點 |
| :--- | :--- | :--- | :--- | :--- |
| 國際／英文（ATS）| [`assets/template-ats-en.md`](assets/template-ats-en.md) | **絕不放** | 只放 email/phone/LinkedIn/作品集連結；**不放**年齡/性別/婚姻 | 單欄、標準標題、無圖表、輸出 PDF/.docx |
| 台灣在地（繁中）| [`assets/template-tw-zh.md`](assets/template-tw-zh.md) | 視公司而定 | 可含照片；其餘個資仍精簡 | 104／CakeResume 風格，可稍有設計但可讀優先 |
| 雙語兩份 | 兩份都用 | 各依市場 | 各依市場 | **同一批成就、兩套排版**；改 A 記得同步 B |

> 口訣：**英文 ATS 版＝去照片、去個資、純文字單欄；繁中在地版＝可放照片、可加自傳。** 成就內容共用，包裝不同。
> ⚠️ Firewall：本 skill 只碰 `career/` 個人職涯檔，非規格書；勿套 `spec-doc-1111`、勿推 HackMD。

---

## 核心原則

1. **成果 > 職責**：寫做到什麼結果，不是負責什麼。`負責 roadmap` → `主導 227 項 roadmap、94% 準時上線`。
2. **量化一切，沒數字就用代理指標**：%、$、人數、時程；無硬指標時用**規模**（團隊/預算）、**速度**（8 週 vs 12 週）、**廣度**（觸及單位數）、**流程改善**（週期縮短 X%）。
3. **ATS 安全**：單欄、標準標題、純文字、無圖表 icon。約 76% 履歷在見到人之前先被 ATS 刷掉。
4. **職能叢集，不是關鍵字清單**：5–7 個叢集，每叢集附 1–2 個證據點。
5. **依 JD 客製**：top-third 鏡射 JD 用語；精準職稱 match 對命中率影響最大。
6. **誠實，絕不捏造**：沿用框架的 `〔待補數據〕` 規則——沒有的數字就標待補。職稱用真實的；不確定是否主導就用 `contributed to` 而非 `led`。

---

## 履歷結構與順序

資深者用**混合式（hybrid）＝ 技能摘要在前 ＋ 反時序工作經歷**最佳；**純功能式（functional）是地雷**（ATS 與招募者都不信任）。

| # | 英文 ATS | 繁中在地 | 備註 |
| :-- | :--- | :--- | :--- |
| 1 | Contact + Headline | 姓名 + 一句定位 + 聯絡方式〔＋照片視情況〕| ATS 版去照片/個資 |
| 2 | Professional Summary（2–3 行）| 專業摘要 | **用摘要、不要 Objective**；含 2–3 個 JD 關鍵字 |
| 3 | Core Competencies（5–7 叢集）| 核心職能 | 叢集 + 證據點 |
| 4 | Professional Experience（反時序）| 工作經歷（反時序）| 每段 3–6 條量化 bullet |
| 5 | Education & Certifications | 學歷／證照 | 年資 10+ 可移到經歷之後 |
| 6 | （選）作品集連結、發表、演講 | （選）自傳、作品集連結 | ATS 版不放自傳 |

> **Top-third 法則**：招募者前 6 秒以 F 型掃描第一頁上三分之一；最強的 2–3 個差異點**必須**在那裡。
> **長度**：中階 1 頁、資深至多 2 頁；**絕不 3 頁**。資深 2 頁時，第一屏（約前 1,400 字）必須單獨就能通過 6 秒篩選。

### 6 秒版面（2026-10-09，依 `career/style/hr-6-second-source.md`）

招募者初篩 6–10 秒、不讀只掃，視線走 F 型集中在左緣，先找**最近職稱、目前公司、起訖日期**，在找「快速說 yes 的理由」。

1. **經歷抬頭一律 `職稱｜公司｜起訖`**，職稱在最左；整行控制在日期落在前 24 字內（公司名用簡稱、上市櫃代號移到範圍行）。正式職稱與對外職稱不同時，抬頭放 `decisions.md` §3 允許的對外寫法，正式職稱放括號或第二行。
2. **摘要不是求職目標**：不寫「希望／尋求／期望／發揮所長」；第一句回答「能不能做這份工作」（職稱＋年資＋最強一項成果）。
3. **左緣 10 字**：每條條列的前 10 字要有結果數字、成果動詞（主導、上線、降到）或 JD 詞；目標 ≥ 60% 條列做到。
4. **範圍行**（抬頭下一行的職務範圍）不以「主責／負責」開頭，改寫成「規模＋角色」（例：`6.6 萬家付費廠商的企業端招募系統，向副總匯報、帶 2 名企劃`）。
5. **相關性刪減**：依目標職缺，刪掉 10 年前結束、與職缺無關的經歷（例：工讀）；兵役等解釋空窗的行保留。104 表單是否刪由使用者決定。
6. **自評**：`python3 .claude/skills/resume-review-panel/scripts/f_scan.py <resume.txt> --jd "<JD 詞>"` 看 F 型視野與抬頭檢查。

---

## Bullet 公式

**[強動詞] + [具體任務] + [量化結果]**，一條一個成就，1–3 行。
等同 Google 招募團隊的 **XYZ：做到 X（結果）、以 Y 衡量（指標）、靠 Z 做到（做法）**。寫完每條自問三格是否都有；缺 Y 寫「指標待補」問使用者，不補數字。
**職責不是成果**：「負責／主責／協助／參與」開頭的句子只說明該做什麼，不說明做到什麼，一律改寫。
**交付鏈例外**（`library/decisions.md` §7）：產出物名稱優先放進 Z；每段經歷**至多 1 條**只有做法的條列，且不排在該段第一條。可套 **STAR** 或 **SOAR**（多一個「阻礙」、凸顯張力，
適合跨系統整合／代碼整併／跨部門協調的素材）。過去式寫過去職位、現在式寫現職。

| 弱 | 強（PM 適用）|
| :--- | :--- |
| Responsible for / 負責 | Owned, Drove, Led / 主導、推動 |
| Worked with / 協助 | Orchestrated, Aligned / 統籌、對齊 |
| Managed / 管理 | Led, Scaled, Directed / 帶領、規模化 |
| Increased / 增加 | Grew, Accelerated, Optimized / 提升、加速 |
| Made / 做了 | Shipped, Defined, Validated / 交付、定義、驗證 |

**Before → After：**

- ✗ `負責產品 roadmap` → ✅ `主導 227 項求才產品 roadmap，以 P0–P3 分級與時間盒交付，半年 111 項上線、94%（84/89）準時或提前`
- ✗ `Worked with engineering on a launch` → ✅ `Orchestrated a cross-functional launch (12 eng, 4 design, data) and shipped in 6 weeks vs. 12-week plan`
- ✗ `負責跨部門溝通` → ✅ `作為求才需求單一窗口，對接 16 個需求單位（總裁/董事/策略長到第一線客服），以數據（投票）化解衝突優先級`

**繁中在地版可改用結果前置（Result-First）**：104／Cake 的 HR 是用掃描的，第一眼要看到成果。
公式：`[成效] ｜ [主導的專案] ＋ [規模／方法]`。
例：`半年 111 項上線、94% 準時 ｜ 主導 227 項求才產品 roadmap，以 P0–P3 分級與時間盒交付`。
英文 ATS 版維持「動詞開頭」，因為 LLM 抽取 impact 靠句內因果，見 references/ats-and-ai-screening.md。

> 把日常產出（規格書／週報／流程圖）逆推成 bullet，見 [`references/reverse-xyz.md`](references/reverse-xyz.md)。

---

## 核心職能叢集

技能段落用 **5–7 個叢集**，每叢集 **1–2 個證據點**，而非 20 個散落關鍵字。
資深訊號＝**範圍、模糊度、跨職能影響、商業成果**。

| 叢集 | 對應職能 | 證據點 |
| :--- | :--- | :--- |
| Product Strategy & Vision | F1, F3 | roadmap／市場分析／多季規劃；平台級 B 端掌握 |
| Execution & Delivery | **F8**, F5 | 227 項 roadmap、94% 準時、版控與缺口治理 |
| Data & Experimentation | F4（部分）| A/B、埋點、SQL；〔待補：實驗數〕|
| Stakeholder Mgmt & Influence | **F9**, F6 | 對接 16 單位、C-suite 對齊、數據決策 |
| Business Logic & Requirements | **F10**, F2 | 權限／審核／配對／續約規則盤成 MECE；多重條件建模；後端邏輯重構、API 整合協定設計 |
| Technical Fluency | F2, F4 | 狀態驅動規格、權限代碼建模、API 串接；循序圖／活動圖／使用案例圖／BPMN；設計稿轉前端規格、欄位檢核與防呆 |
| AI Product | **F4** | 生成式（公司簡介／JD 生成）＋ 推薦（AI 推薦人才）|
| Problem-Solving & Ops | **F11** | 截至 2026/09 累計 1,857 張、處理率約 93%；週期 100.4→30.9 天；管線覆蓋 1,279 家付費廠商、年化留存 81.2% vs 全站 74.2% |
| Process & Tooling | F7 | `spec-doc-1111` skill、程式化重建文件樹 |
| 0→1 & Consumer Mobile | **F12** | 3 個 0→1 ＋ 4 個既有產品；iOS／Android／RWD 三端；MVP 交付 |
| Monetization & Pricing | **F13** | IAP 模型與價格點、第三方金流串接、配額計價、牌價結構分析 |
| Internationalization | **F14** | 7 市場在地化、跨文化團隊、TOEIC 980 |
| AI Workflow & Agent Governance | **F15** | 12 條分身／23 skill 的多代理系統；SSOT、重複偵測、事故後機制修復 |

**強寫法**：`執行與交付 — roadmap 優先級（P0–P3）、時間盒交付、版控治理；主導 227 項 roadmap，半年 111 項上線、94% 準時。`
**弱寫法（勿用）**：`產品管理、roadmap、A/B、Agile、SQL、溝通、領導、策略…`

> **系統分析（SA）視角**：應徵系統分析／技術型 PM 時凸顯三條證據線（與 F2／F10／F4 共用同一批成就）：
> ① **架構與規格設計**（Markdown 規格書、循序圖／活動圖／使用案例圖／BPMN 建模）；
> ② **技術整合與重構**（API 整合協定、後端邏輯重構、AI 模組導入）；
> ③ **UI/UX 對接**（設計稿轉前端規格、欄位檢核與防呆機制）。

**Junior → Senior 訊號：**

| Junior | Senior |
| :--- | :--- |
| 做使用者研究 | 綜整 100+ 訪談，重新定義產品策略 |
| 做 A/B 測試 | 建立實驗框架，年跑 50+ 實驗 |
| 排 roadmap | 帶 2 年策略歷經 3 次轉向，對齊 20 人團隊 |
| 跨部門溝通 | 取得 C-suite 信任、推動 2 個有爭議的 roadmap 轉向 |

---

## 從職能框架產出

> 本節是工作流程步驟 1、2、4 的操作細節；完整八步與產出檔見 [`references/workflow.md`](references/workflow.md)。

先讀 `career/library/decisions.md`＋對應 `facts-*.md`（現行事實；與 wiki 衝突以 library 為準，審稿對照 `superseded.md`），
再以 `career/competency-framework.md`（**wiki 入口**）依其路由表只載入需要的 `career/wiki/` 分頁：

1. 取 `wiki/resume-extract.md`（action+scope+impact 條目）作為 bullet 草稿基底。
2. 取 `wiki/F01…F15-*.md` → 映射到上方叢集表，挑 5–7 個最相關的。
3. 取入口的 Profile Snapshot／Positioning → 寫 Summary/Headline；學歷證照取 `wiki/education-certifications.md`。
4. 遇到 `〔待補數據〕`：先問使用者，**一次只問一題**，優先順序是商業影響 → 規模 → 方法／工具；拿不到就保留標記，不要編。
5. 依目標 JD 與市場版本選範本、客製 top-third。
6. 依 [`references/anti-ai-ats.md`](references/anti-ai-ats.md) 掃禁用詞與破折號；空泛條目先做 CAR 盤問（Context／Action／Result），問不到照實寫過程，不補數字；最後依 §6（V4 防禦型規則：職稱包裝、量級錨定、RACR、剔除弱訊號）做毒性稽核。與事實衝突時以事實為準。
7. **職能覆蓋檢查（2026-10-08 新增，必做）**：改稿一律從 library＋F 頁出發，不只從上一版刪修。逐項確認以下都看得到，缺的要補或說明理由：
   - **交付鏈**（`library/decisions.md` §7）：定義段（User Journey Map、User Story、Use Case、SA、Flowchart／Sequence、Wireframe、與 UI/UX 協作、Prototype、Stakeholder 匯報、Spec）與交付段（與工程追時程、與 QA 協作、上線計畫、完整交付），至少各一條條列，技能欄列產出物。
   - **F01–F15 對照**：列出本版涵蓋與刻意未放的職能，未放的寫理由（例如職缺不需要）。
   - 「少用技術詞」只針對工程實作與內部縮寫，**不得**因此刪掉 PM 產出物。
8. 跑下方檢查清單。

---

## 反面模式 / Red flags

| 反面模式 | 為何傷 | 修法 |
| :--- | :--- | :--- |
| 職責而非成就 | `Responsible for…` 沒說明結果 | 改成量化成就 |
| Buzzword 堆砌、無數字 | 空泛、像低階 | 加人數/%/$/時程 |
| 多欄、圖表、icon | ATS 與 LLM 解析都會失敗 | 純文字單欄 |
| 平鋪關鍵字技能段 | 看起來 junior | 改職能叢集 + 證據點 |
| 資深卻無作品集 | 訊號薄弱 | 補 3–5 篇 case study |
| 灌水職稱／編造數字 | 被查核即失信，77% 招募者立刻刷 | **誠實**；不確定用 `contributed to` |
| 全通用、不客製 | ATS 與人都看得出 | 客製 top-third |
| AI 腔（realm／intricate／pivotal／showcasing）| 易被判 AI 生成 | 用自己的口吻、念出來檢查 |
| 錯字、文法 | 58% 招募者直接刷 | 校對 3 次 + 工具 + 真人 |

---

## 交付前檢查清單

- [ ] **市場版本已選**（ATS-EN／繁中／雙語），用對應範本；ATS 版已去照片與個資。
- [ ] **ATS 格式**：單欄、標準字體、標準標題、無圖表 icon、輸出 PDF/.docx。
- [ ] **Top-third 衝擊**：Summary + 前 2–3 bullet 鏡射 JD、6 秒看得到 2–3 個差異點。
- [ ] **6 秒版面**：抬頭 `職稱｜公司｜起訖` 且日期在前 24 字內；摘要無求職目標語；左緣 10 字有訊號 ≥ 60%；範圍行不以職責開頭；已做相關性刪減（`f_scan.py` 全 ✅ 或有理由）。
- [ ] **XYZ**：每條拆得出 X／Y／Z；職責式開頭 0 條；只有做法的條列每段 ≤ 1 且不在第一條。
- [ ] **Bullet 公式**：每條 = 強動詞 + 任務 + 量化結果，1–3 行。
- [ ] **量化覆蓋**：≥ 80% bullet 有數字；無硬數據處用代理指標。
- [ ] **職能叢集**：5–7 叢集 + 證據點，已映射 F1–F15。
- [ ] **交付鏈與產出物**：定義段、交付段各至少一條；技能欄列出產出物（`library/decisions.md` §7）。
- [ ] **作品集**：資深者於 header 放連結；3–5 篇（含一個誠實的失敗實驗）。
- [ ] **大企業訊號**：對映 4–5 條目標公司價值；範圍、模糊度、跨職能影響、商業成果到位。
- [ ] **強動詞**：drove／orchestrated／defined／shipped／scaled／validated（不用 Spearheaded、Architected，見 `career/library/decisions.md` §1）。
- [ ] **無紅旗**：無錯字、無 buzzword 堆砌、**無捏造數字**、無 AI 腔、無未解釋空檔。
- [ ] **誠實**：所有 `〔待補數據〕` 要嘛填真實數字、要嘛保留標記；職稱屬實。
- [ ] **長度與格式**：1–2 頁；hybrid 或反時序。
- [ ] **雙語同步**（若維護兩份）：成就一致，僅包裝／語言不同。
- [ ] **視覺版／ATS 版分清**：視覺版僅供人看；ATS 上傳另備單欄純文字版；兩者數字一致。
- [ ] **AI 掃描自測**：LLM 自測迴圈三測全過；每條 bullet self-contained；經歷開頭為 `職稱｜公司｜起訖`；**無 prompt injection、無隱形文字**。
