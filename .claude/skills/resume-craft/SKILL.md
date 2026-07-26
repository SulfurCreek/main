---
name: resume-craft
description: >
  撰寫、修改、批改、優化使用者**個人履歷／CV／LinkedIn／作品集（portfolio）**，或把職能、經歷、專案成果轉成
  履歷 bullet、依特定職缺（JD）客製化履歷時使用。只要任務涉及「履歷」「resume」「CV」「自傳」「作品集」「portfolio」
  「case study」「LinkedIn」「投遞」「應徵」「求職」「JD 客製」「把 F1–F11 職能或專案變成履歷條目」，務必使用本 skill
  —— 即使使用者沒有明講「履歷」兩個字。
  本 skill 依**大型企業招募標準**（ATS 解析、AI／LLM 履歷掃描、核心職能叢集、量化影響 bullet、作品集案例研究、
  Amazon Leadership Principles 等）優化；以 **Senior PM / Product** 視角為主，**雙語**（英文 ATS 版 + 繁中在地版）。
  證據來源為 `career/competency-framework.md`（wiki 入口／路由表）＋ `career/wiki/` 分頁。
  ⚠️ 這是 `career/` 個人職涯工具，**不是 1111 規格書**：請勿套用 `spec-doc-1111`，請勿推送至 HackMD `1111-jobdocs`。
---

<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

# resume-craft — 個人履歷／作品集優化（大企業標準）

把使用者的職能與經歷，轉成**過得了 ATS（含 AI/LLM 掃描）、6 秒內打中招募者、且不浮誇**的履歷與作品集。
本 skill 是證據庫的下游：`career/competency-framework.md`（wiki 入口）＋ `career/wiki/` 分頁存「證據」，
本 skill 是「把證據變成履歷的方法」。

## 🗺️ 任務路由 / Task routing

本檔只放**每次都用得到的核心**；其餘按需載入 `references/`：

| 任務 | 讀什麼 | 證據分頁（`career/`）|
| :--- | :--- | :--- |
| 產第一版履歷 | 本檔全部 | `competency-framework.md` → `wiki/resume-extract.md` ＋ 相關 F 分頁 |
| 改寫 bullet／把日常產出變 bullet | 本檔 Bullet 公式 ＋ [`references/reverse-xyz.md`](references/reverse-xyz.md) | 對應 `wiki/F0x-*.md` |
| 投遞硬技術公司（NVIDIA-tier）| [`references/reverse-xyz.md`](references/reverse-xyz.md) | `wiki/flagship-e1.md`、`wiki/F02`、`wiki/F10` |
| 依 JD 客製／ATS／HR 用 AI 掃履歷 | [`references/ats-and-ai-screening.md`](references/ats-and-ai-screening.md) | `wiki/resume-extract.md` |
| 作品集 case study | [`references/portfolio.md`](references/portfolio.md) ＋ [`assets/portfolio-case-study.md`](assets/portfolio-case-study.md) | `portfolio/e1-cross-system-messaging.md`（範例）|
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
> **長度**：中階 1 頁、資深至多 2 頁；**絕不 3 頁**。

---

## Bullet 公式

**[強動詞] + [具體任務] + [量化結果]**，一條一個成就，1–3 行。可套 **STAR** 或 **SOAR**（多一個「阻礙」、凸顯張力，
適合跨系統整合／代碼整併／跨部門協調的素材）。過去式寫過去職位、現在式寫現職。

| 弱 | 強（PM 適用）|
| :--- | :--- |
| Responsible for / 負責 | Owned, Spearheaded, Drove / 主導、推動 |
| Worked with / 協助 | Orchestrated, Aligned / 統籌、對齊 |
| Managed / 管理 | Led, Scaled, Directed / 帶領、規模化 |
| Increased / 增加 | Grew, Accelerated, Optimized / 提升、加速 |
| Made / 做了 | Shipped, Architected, Validated / 交付、設計、驗證 |

**Before → After：**

- ✗ `負責產品 roadmap` → ✅ `主導 227 項求才產品 roadmap，以 P0–P3 分級與時間盒交付，半年 111 項上線、94%（84/89）準時或提前`
- ✗ `Worked with engineering on a launch` → ✅ `Orchestrated a cross-functional launch (12 eng, 4 design, data) and shipped in 6 weeks vs. 12-week plan`
- ✗ `負責跨部門溝通` → ✅ `作為求才需求單一窗口，對接 16 個需求單位（總裁/董事/策略長到第一線客服），以數據（投票）化解衝突優先級`

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
| Problem-Solving & Ops | **F11** | 1,279 工單／~88% 結案；工單→Kanban→上線閉環；96.5% 來自付費廠商、觸及 1,109 家付費帳號 |
| Process & Tooling | F7 | `spec-doc-1111` skill、程式化重建文件樹 |

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

以 `career/competency-framework.md`（**wiki 入口**）為唯一證據源，依其路由表只載入需要的 `career/wiki/` 分頁：

1. 取 `wiki/resume-extract.md`（action+scope+impact 條目）作為 bullet 草稿基底。
2. 取 `wiki/F01…F11-*.md` → 映射到上方叢集表，挑 5–7 個最相關的。
3. 取入口的 Profile Snapshot／Positioning → 寫 Summary/Headline；學歷證照取 `wiki/education-certifications.md`。
4. 遇到 `〔待補數據〕`：**先問使用者拿真實數字**；拿不到就保留標記，不要編。
5. 依目標 JD 與市場版本選範本、客製 top-third。
6. 跑下方檢查清單。

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
- [ ] **Bullet 公式**：每條 = 強動詞 + 任務 + 量化結果，1–3 行。
- [ ] **量化覆蓋**：≥ 80% bullet 有數字；無硬數據處用代理指標。
- [ ] **職能叢集**：5–7 叢集 + 證據點，已映射 F1–F11。
- [ ] **作品集**：資深者於 header 放連結；3–5 篇（含一個誠實的失敗實驗）。
- [ ] **大企業訊號**：對映 4–5 條目標公司價值；範圍、模糊度、跨職能影響、商業成果到位。
- [ ] **強動詞**：spearheaded／orchestrated／architected／shipped／scaled／validated。
- [ ] **無紅旗**：無錯字、無 buzzword 堆砌、**無捏造數字**、無 AI 腔、無未解釋空檔。
- [ ] **誠實**：所有 `〔待補數據〕` 要嘛填真實數字、要嘛保留標記；職稱屬實。
- [ ] **長度與格式**：1–2 頁；hybrid 或反時序。
- [ ] **雙語同步**（若維護兩份）：成就一致，僅包裝／語言不同。
- [ ] **視覺版／ATS 版分清**：視覺版僅供人看；ATS 上傳另備單欄純文字版；兩者數字一致。
- [ ] **AI 掃描自測**：LLM 自測迴圈三測全過；每條 bullet self-contained；經歷開頭為 `職稱｜公司｜起訖`；**無 prompt injection、無隱形文字**。
