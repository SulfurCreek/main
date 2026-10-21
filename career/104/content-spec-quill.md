<!--markdownlint-disable MD013-->

> 本人 2026-10-20 提供，原樣保存。**範例文字只取格式，不取事實**（見 `../library/decisions.md` §20）；事實一律以 `../library/` 為準。

# 104 人力銀行履歷欄位規格與內容特化撰寫指南 (給 Claude Code / 內容生成 Agent)

> **目標讀者**：負責為求職者生成、潤飾與特化 104 履歷內容的 AI Agent（例如 Claude Code）。  
> **核心目標**：指導 Agent 如何針對 104 平台的**系統演算法比對**、**企業端 HR 篩選器**與 **Quill 前端渲染機制**，產出視覺專業、高度結構化、且精準命中職缺的頂級履歷內容。  
> **適用履歷代碼**：`76js7patq` (104 會員中心格式)

---

## 目錄
1. [104 內容生成核心心法與演算法邏輯](#1-104-內容生成核心心法與演算法邏輯)
2. [Quill 富文本 HTML 排版語法庫 (必用樣式)](#2-quill-富文本-html-排版語法庫-必用樣式)
3. [各欄位規格、撰寫規範與特化範例](#3-各欄位規格撰寫規範與特化範例)
   - [3.1 個人自述摘要 (Info Bio)](#31-個人自述摘要-info-bio)
   - [3.2 工作經歷 (Experience Description)](#32-工作經歷-experience-description)
   - [3.3 專長與技能 (Skills & Tags)](#33-專長與技能-skills--tags)
   - [3.4 自傳 (Chinese & English Bio)](#34-自傳-chinese--english-bio)
   - [3.5 專案成就 (Project Achievements)](#35-專案成就-project-achievements)
   - [3.6 求職條件內容 (Job Condition Content)](#36-求職條件內容-job-condition-content)
4. [不可觸碰的資料與欄位約束](#4-不可觸碰的資料與欄位約束)

---

## 1. 104 內容生成核心心法與演算法邏輯

當你在為 104 撰寫內容時，必須理解 104 企業端後台有兩道篩選關卡：

### 關卡 A：系統機器人硬篩選 (Hard Filters & Keyword Matching)
1. **技能代碼標籤比對 (`skill.tag`)**：104 的職缺推薦並非只做全文檢索，而是強烈依賴「標準技能標籤代碼」。例如 `Figma` (`12002004009`)、`Wireframe` (`12002004013`)、`Claude` (`12001002021`)。撰寫專長時，務必提醒或搭配標準 Tag。
2. **結構化管理責任 (`experience.management`)**：HR 勾選「需具管理經驗」時，後台只認結構化欄位。在描述有帶人經歷的工作時，必須同步將 management 設定為有管理責任（如 1~5 人）。

### 關卡 B：HR 人眼 5 秒掃視原則 (Scannability & Visual Hierarchy)
- **拒絕純文字一坨到底**：密密麻麻的純文字段落會讓 HR 在 3 秒內關掉履歷。
- **善用 104 Quill 支援的 HTML 標籤**：使用 `<blockquote>` 凸顯核心職掌，使用 `<span class="ql-size-large" style="color: #00afb8;">` 建立清晰二級標題，使用 `style="background-color: #fbf3db;"` 在量化數據上劃螢光重點。

---

## 2. Quill 富文本 HTML 排版語法庫 (必用樣式)

104 的經歷、自傳、專案成就欄位支援完整 HTML 解析。Claude Code 在輸出欄位字串時，**請直接輸出包含以下標準標籤的 HTML 字串**：

| 排版需求 | HTML 語法與樣式代碼 | 渲染效果與使用情境 |
| :--- | :--- | :--- |
| **核心職掌／引言** | `<blockquote><strong>【職掌重點】</strong><br>內文...</blockquote>` | 灰底背景＋左側深色直線，適合放職務定位與一句話戰績 |
| **區塊大標題** | `<p><span class="ql-size-large" style="color: #00afb8;"><strong>一、重大成果</strong></span></p>` | 104 官方科技湖水綠大字標題，建立清晰視覺層級 |
| **小標題／加粗** | `<strong>【專案名稱】</strong>` 或 `<strong>• 項目名稱</strong>` | 段落重點提示 |
| **螢光筆劃重點** | `<span style="background-color: #fbf3db;">量化成果字串</span>` | 淡金黃色螢光標記，專門用於**數字、營收、日活躍增長率** |
| **輔助螢光標記** | `<span style="background-color: #deebf1;">重要關鍵字</span>` | 淡晴藍色螢光標記，用於技術架構或重要專有名詞 |
| **條列項目清單** | `<ul><li><strong>核心動詞</strong>：成果描述與量化指標。</li></ul>` | 條列化展現 STAR 原則，易讀性最高 |
| **段落分隔線** | `<hr class="ql-divider">` | 104 原生水平分隔線，用於區分工作職責與技術工具清單 |
| **備註／工具列** | `<p><small style="color: #7e7e7e;"><strong>核心工具</strong>：Axure・Figma・UML</small></p>` | 灰色小字，收斂工具與關鍵字 |

---

## 3. 各欄位規格、撰寫規範與特化範例

### 3.1 個人自述摘要 (Info Bio)
- **所屬區塊**：`info.info.bio`
- **呈現位置**：履歷最頂部「個人名片卡」中，HR 打開履歷第一眼看到的第一屏。
- **字數限制**：建議 150 ~ 250 字（不宜過長，精煉有力）。
- **撰寫公式**：`[資歷年限與領域定位] + [代表性爆發實績 (0到1/危機逆轉)] + [核心方法論與技術工具] + [能為企業帶來的價值]`
- **特化 HTML 範例**：
```html
<p>我擁有近十年的產品經理經驗，曾負責 6 款產品，橫跨 <strong>B2B SaaS 企業系統、訂閱制社群交友與網紅媒合平台</strong>。在公司主力 App 遭下架時，曾主導接續產品於 3 週內快速上線，成功承接逾千萬既有營收；現任知名招募平台企業端產品負責人，主導系統重新架構與 AI 人才推薦落地。具備<strong>定價實驗、計費與訂閱機制、流程規格化及跨國多市場在地化</strong>經驗，能精準將商業策略轉化為高質量的產品交付。</p>
```

---

### 3.2 工作經歷 (Experience Description)
- **所屬區塊**：`experience.experiences[i].description`
- **呈現位置**：履歷核心主體「工作經歷」之詳細說明。
- **撰寫原則**：
  1. 頂部必須有 `<blockquote>` 交代**業務範疇、服務規模與團隊管理權責**。
  2. 內文拆分為 2~3 個主題標題（例如：`商業成果與危機逆轉`、`系統架構與產品迭代`、`跨部門協同與敏捷管理`）。
  3. 全面貫徹 **STAR 原則**（Situation, Task, Action, Result），每項成就必須包含動詞＋量化數據（%，金額，家數，天數）。
  4. 底部用 `<hr class="ql-divider">` 與 `<small>` 標註核心技能與工具。
- **特化 HTML 範例 (以資深 PM / 全球華人經歷為例)**：
```html
<blockquote><strong>【職位範疇與管理責任】</strong><br>負責人力銀行企業端招募系統（服務 60,000+ 家付費企業），協調工程、行銷、業務、資料科學與客服等 10 個關係單位。帶領 2 名直屬產品企劃，參與高層營運會議並向總經理定期匯報。</blockquote>

<p><span class="ql-size-large" style="color: #00afb8;"><strong>一、核心系統重構與商業規則落地</strong></span></p>
<ul>
  <li><strong>新版求才系統架構規劃</strong>：主責逾 50 項主要功能規劃，重塑企業子帳號權限、E-mail 登入體系與全新計費邏輯，<span style="background-color: #fbf3db;">提升提案結案效率達 30%</span>。</li>
  <li><strong>產品規格與驗收標準化</strong>：獨立撰寫完整 PRD、Flowchart、Wireframe 與原型，協同 QA 制定測試案例，實現每兩週一次 Sprint 的穩定交付。</li>
</ul>

<p><span class="ql-size-large" style="color: #00afb8;"><strong>二、AI 應用整合與關鍵問題解決</strong></span></p>
<ul>
  <li><strong>AI 智慧推薦人才功能</strong>：協同資料科學團隊完成推薦模型落地，將 AI 候選人推薦嵌入企業招募工作流，提升企業主動聯絡率。</li>
  <li><strong>廠商帳號資安冒用防護</strong>：主導帳號驗證與異常行為告警機制，<span style="background-color: #fbf3db;">成功降低客服相關進線申訴率 45%</span>。</li>
</ul>

<hr class="ql-divider">
<p><small style="color: #7e7e7e;"><strong>核心工具與專業</strong>：PRD・Wireframe・Axure RP・Figma・UML・AI Workflow・Claude・B2B SaaS</small></p>
```

---

### 3.3 專長與技能 (Skills & Tags)
- **所屬區塊**：`skill.skills[]`
- **結構**：
  - `name`：專長類別標題（15 字內，如「產品規劃與交付」）
  - `desc`：詳細能力敘述（100~200 字，具體描述使用情境）
  - `tag`：關聯之 104 標準代碼標籤（**必須填滿，讓系統演算法抓取**）
- **PM 推薦 4 大專長設定組合**：
  1. **專長一：產品策略與商業化變現 (Monetization)**
     - 敘述：具備訂閱制（Subscription）、VIP 付費牆、定價實驗（A/B Testing）與第三方海外金流整合實戰實績。
     - 標籤 (#Tags)：`產品策略`、`產品定位`、`產品營運`、`數據分析`、`市場調查`
  2. **專長二：產品規劃與系統架構 (0 to 1 Delivery)**
     - 敘述：精通從需求訪談、用戶旅程、User Story 拆解，到產出 PRD、流程圖、互動原型與驗收標準。
     - 標籤 (#Tags)：`Figma`、`Axure RP`、`Wireframe`、`Prototype`、`UML`、`Systems Analyst`
  3. **專長三：跨部門協作與敏捷專案管理 (Agile & Stakeholder Management)**
     - 敘述：具備帶領產品團隊並橫向協調工程、UIUX、商業業務、法務、資料團隊之高情商溝通與進度控管能力。
     - 標籤 (#Tags)：`專案溝通╱整合管理`、`製作規格說明書`、`決策能力`、`專案時程編製╱調配`
  4. **專長四：AI 工作流與新技術整合 (AI & Modern Tooling)**
     - 敘述：深度運用生成式 AI（Claude, ChatGPT）輔助競品分析、PRD 產出與驗收案例制定；具備 AI 模型與推薦系統落地經驗。
     - 標籤 (#Tags)：`AI`、`LLM`、`ChatGPT`、`Gemini`、`Claude`

---

### 3.4 自傳 (Chinese & English Bio)
- **所屬區塊**：`bio.bio.chi` (中文自傳)、`bio.bio.eng` (英文自傳)

#### 中文自傳 (`chi`)
- **建議字數**：800 ~ 1200 字。
- **結構模組**：
  1. **【職涯摘要與個人定位】**：10 年 PM 資歷、涵蓋領域與核心價值觀。
  2. **【關鍵實績一：商業變現與危機破局】**：詳述主力產品下架時，如何主導替代產品快速上市並保住營收的具體心法。
  3. **【關鍵實績二：大型複雜系統重構】**：詳述企業端 B2B 招募系統逾 50 項模組的規格化與跨部門推進。
  4. **【跨國協作與海外市場經驗】**：CSU Sacramento 交換背景、全英文協同 7 國在地化。
  5. **【未來展望與工作期許】**：願景與能為目標企業創造的貢獻。

#### 英文自傳 (`eng`)
- **重要性**：外商（Yahoo, Klook, LINE, Shopee）與跨國 SaaS 極度看重，能直接驗證求職者多益 980 的實戰書寫能力。
- **建議字數**：300 ~ 450 字。
- **特化英文自傳範本**：
```text
I am a Senior Product Manager with nearly a decade of experience driving the 0-to-1 launch, monetization, and scaling of software products across B2B SaaS platforms, subscription-based social applications, and creator matchmaking ecosystems.

Throughout my product career, I have thrived in high-stakes and fast-paced environments. When our flagship dating app, JustDating—previously ranked #1 in Taiwan's dating grossing charts—faced sudden App Store delisting, I spearheaded the rapid delivery and user migration to a successor product, Juicy, successfully preserving millions in subscription revenue within three weeks. In my current role at 1111 Job Bank, I lead the enterprise recruitment platform serving over 60,000 paid corporate accounts, overseeing the end-to-end redesign of complex billing architectures, permission hierarchies, and the integration of AI-driven talent recommendation engines.

My core competencies include:
• Monetization & Growth: Proven track record in A/B price elasticity experiments, paywall optimization, and multi-market payment gateway integrations (e.g., CodaPay).
• Agile Delivery & Stakeholder Alignment: Leading cross-functional squads comprising engineering, UX, data science, and business development to deliver bi-weekly iterative sprints.
• Global Mindset: Educated at California State University, Sacramento, with extensive experience driving localization across 7 international markets in English-speaking environments.

I am dedicated to combining user-centric design with disciplined commercial execution to build resilient, high-impact digital products.
```

---

### 3.5 專案成就 (Project Achievements)
- **所屬區塊**：`project.projects[]`
- **欄位結構**：
  - `name`：專案名稱 (如 `「Juicy」訂閱制 App 危機接續與營收承接`)
  - `duration`：起訖年月 (`startYear`, `startMonth`, `endYear`, `endMonth`)
  - `isInProgress`：是否進行中
  - `url`：專案成果外部連結
  - `introduction`：專案成果詳細描述 (支援富文本 HTML)
- **撰寫範例 (introduction HTML)**：
```html
<blockquote><strong>專案使命</strong>：於原主力交友 App 遭下架之突發危機下，在最短時限內推出承接產品，確保數萬名付費會員無痛轉移並維繫公司核心現金流。</blockquote>
<p><span class="ql-size-large" style="color: #00afb8;"><strong>關鍵行動與實績指標</strong></span></p>
<ul>
  <li><strong>3 週敏捷上線</strong>：迅速梳理會員轉移路徑與付費機制，完成接續產品 Juicy 的流程設計與海外金流串接。</li>
  <li><strong>營收承接率 85%+</strong>：透過定價實驗與專屬導流策略，成功承接絕大多數既有活躍付費用戶，男性日活躍用戶數顯著成長。</li>
  <li><strong>網頁付款佔比提升</strong>：因應平台政策，推動 Web 網頁付款機制，有效降低對雙平台抽成之依賴。</li>
</ul>
```

---

### 3.6 求職條件內容 (Job Condition Content)
- **所屬區塊**：`jobCondition.jobCondition.preferJobContent`
- **目標**：向企業明確表達自己的擅長領域、求職偏好與工作期待。
- **範例字串**：
```text
期待尋求「產品經理 (Product Manager / Senior PM)」或「產品負責人 (Product Owner)」職務。
專長於：
1. 數位產品（Web/APP/SaaS）之 0 到 1 規劃、流程架構梳理、PRD 規格撰寫與敏捷交付。
2. 訂閱制商業變現、付費流程設計、定價實驗與數據分析優化。
3. 跨部門（工程、設計、商業、資料、營運）溝通整合與專案推進。
開放接受具成長動能之網際網路、軟體 SaaS、金融科技或數位轉型團隊，支援混合辦公（Hybrid）或辦公室協作。
```

---

## 4. 不可觸碰的資料與欄位約束

當 Agent 產出履歷資料時，請切記以下**絕對邊界**：
1. **不得偽造個人真實資料**：姓名、通訊地址（北投區）、畢業學校（淡江大學、CSU Sacramento）、任職公司名（全球華人、尚凡、思維特、新蛋）、任職年月份皆不可變造。
2. **遵守 104 字符長度上限**：
   - 專長名稱 (`skill.name`)：15 字內
   - 專案名稱 (`project.name`)：30 字內
   - 個人簡介 (`info.bio`)：建議 300 字內（純文字計算）
   - 單筆經歷內文 (`experience.description`)：建議 1500 字內

---

## 5. Career Move 增補規則：個人簡介與頂部個人特色（2026-10-21，本人回饋整理；優先於上方 §3.1 範例公式）

> 上方 §1–§4 為本人 2026-10-20 提供的原文，保留不改。本節是共用規格，`career/skills/104resume/SKILL.md` 與 `career/codex-skills/polish-104/SKILL.md` 均引用本節，不另立公式。

> **強制門檻（2026-10-21）**：本規格各欄位都先過 `career/skills/resume-causal-logic-compiler/SKILL.md` 的對外選材與 T1–T6。

### 5.1 個人簡介（`info.info.bio`）

- 一個連貫短段（一個 `<p>`），交代年資、產品範圍、商業經驗、現職與管理責任、主要產出及交付能力；依本人定位取捨，不強迫逐項填滿。
- 「一小段」是閱讀結構，不是越短越好：精簡要保留辨識度與必要限定，不以縮字百分比當品質標準。
- 代表經驗濃縮成一個事實主張；**不強迫「爆發實績／危機逆轉」公式**，不展開情境、步驟與完整案例。
- 分工：簡介＝整體輪廓；經歷＝代表做法與成果；自傳＝思路與動機。同一經驗可支撐不同層次，不為避免重複而刪掉商業責任與產品判斷。
- 全份履歷仍呈現交付鏈；簡介不必堆全套文件與工具名。AI 寫目前工作方式與用途，不推定工程開發或量化效率。
- 長度：專案編輯範圍 300 字內，150–250 字為建議，**250 不是硬限制**；300 也不是 104 畫面上限（本人截圖可輸入 1000 字）。
- Quill：沿用 `<strong>` 標產品範圍與商業經驗；不加小標、條列或整段螢光。

### 5.2 頂部個人特色 chip

- 與專長的標準技能 tag（`skill.tag`）分開處理；位置在個人簡介下方、履歷最上方。
- 可用短句、有記憶點（punch line），但每句要有經歷支撐；不承諾搜尋排名、點閱或面試成效；不加自誇形容詞或未確認成果。
- 單一 chip 容量以填表時實測為準；有硬限制只回報，不擅自截斷。
- 2026-10-21 版五句與 Client／Business 用語是本版選定文字，**不是**所有職缺的永久模板；也不據此改動英文履歷或其他文件的 B2C／B2B 用法。

| chip | 經歷支撐（library） |
| :-- | :-- |
| 把構想變成產品 | KOOL 0→1（商家訪談、Airbnb 參考、Miro 流程、簡報與上線） |
| 兼具Client與Business視角（104 字數限制，本人 2026-10-21 由「懂 Client 體驗，也懂 Business 流程」改） | 消費型訂閱／付費產品＋企業招募系統 |
| 把商業邏輯說清楚（本人 2026-10-21 由「把複雜規則說清楚」改） | 還原無文件的權限與計費規則、整理成流程與規格；訂閱方案實收試算；互動原型與 FAQ 向客服、業務說明 |
| 從規劃推進到上線 | 與設計、工程、QA 協作分階段上線 |
| 帶團隊用 AI 解題 | 指導同仁以 AI Agent 完成職務類別代碼對照（同仁做最後判斷） |

