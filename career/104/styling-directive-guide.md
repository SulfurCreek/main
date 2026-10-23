<!--markdownlint-disable MD013-->

> 本人 2026-10-23 提供 v2.1.0，原樣保存，取代 v2.0.0；**產生 104 md 時必跑**。
>
> **Career Move 附註**：§三之 2 範例文字是舊版草稿（約 50 項、2023/12–2026/03、信件與即時通、199 件即時通相關建議），**只示範格式**；實際內文一律逐字取自已通過 `verify_polish.py` 的 `career/02_codex_stage/final_resume.md`（本指南 §一第 0 條）。

# 104 人力銀行全欄位格式設定與自動化指令指南 (104 Field Styling & Directive Guide)

> **版本**：2.1.0 (2026 管線對齊防呆版)  
> **適用平台**：104 會員中心履歷編輯器 (`https://pda.104.com.tw/profile/edit?vno={vno}`)  
> **核心用途**：提供給內容封裝 AI（Claude Code Stage 3）與瀏覽器執行 Agent（Antigravity + Gemini Flash），定義 104 履歷每一欄位的資料型態、Quill 富文本 HTML 排版語法、官方標籤白名單驗證，以及**在產出 `104.md` 時嵌入機器可讀指令的標準語法**。

---

## 一、核心原則與安全約束（最高鐵律，違反即中止）

0. **定稿文字絕對鎖定原則（Zero Text Mutation — 最重要！）**：
   - 轉為 `104.md` 與填入 104 網頁時，內文必須 **100% 逐字沿用 `career/02_codex_stage/final_resume.md` 已通過 `verify_polish.py` 驗收的定稿文字**！
   - **只准套用 HTML 視覺容器（如 `<blockquote>`、`<ul><li>`、`<span style="background-color:...">`），嚴禁增刪、改寫、摘要任何一個字，且絕對禁止在 `<li>` 開頭自行加上 `<strong>標題：</strong>` 分類前綴！**
1. **履歷真實性與白名單標籤原則（Zero Hallucination & Strict Whitelist）**：
   - 所有填寫進經歷標籤 (`experience.skill`) 或專長卡片 (`skill.skills[].tag`) 的標籤，**必須同時滿足：(A) 在求職者定稿內文中有明確佐證，且 (B) 存在於 104 官方標籤白名單（擅長工具 768 項、工作技能 1,328 項）**。
   - **嚴禁為了湊滿數量而塞入定稿未提及的工具**（例如：定稿中未使用 `JIRA`、`Tableau`、`SimilarWeb`、`Google Tag Manager`、`Xmind`、`Git`，**絕對禁止**填入標籤！僅能使用定稿有依據之工具如 `Figma`、`Axure RP`、`Wireframe`、`Trello`、`UML`、`Claude` 等）。
   - **寧缺勿濫**：若符合內文佐證的官方白名單標籤不足 8 項，有幾項就填幾項，嚴禁硬湊！
2. **專長卡片數量與順序鎖定**：
   - 嚴格依定稿之 **6 項專長**（`AI Agent 協作`、`產品規劃與交付`、`系統分析`、`UI/UX 規劃`、`跨部門協作與時程`、`App 產品與變現`）設定，不得擅自合併為 4 項或更改標題。
3. **版型變更強制停詢與瀏覽器安全**：
   - 凡涉及 `layout`、主題版型或背景色變更，未獲明確許可前嚴禁覆寫。
   - 未獲明確 `/browser` 指示時，一律僅在本地端產出與靜態驗證，絕不觸碰瀏覽器。

---

## 二、104 全欄位資料型態與規格總覽

| 區塊 (Block) | 欄位路徑 (Field Path) | 資料型態 | 字數/數量限制 | 支援 Quill HTML | 呈現位置與視覺效果 |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **`info`** | `info.bio` | 純文字/HTML | 依定稿完整填入 | ⚠️ 部分支援 | 履歷最頂部名片卡個人簡介 |
| | `info.trait` | 字串陣列 | 鎖定定稿 5 組 | ❌ 否 | 頂部圓角個人特色標籤（LOCKED） |
| | `info.personalLink1~3` | URL 字串 | 最多 3 組 | ❌ 否 | 個人作品集網站連結 |
| **`experience`** | `experiences[i].companyName` | 純文字 | 結構欄位鎖定 | ❌ 否 | 公司名稱（嚴禁更動） |
| | `experiences[i].jobName` | 純文字 | 結構欄位鎖定 | ❌ 否 | 職務名稱（嚴禁更動） |
| | `experiences[i].duration` | 物件 `{start, end}` | `YYYY-MM`（鎖定） | ❌ 否 | 任職起訖年月、在職狀態 |
| | `experiences[i].management` | 物件 `{hasManage, count}`| 管理責任代碼（鎖定）| ❌ 否 | 帶人實績 |
| | `experiences[i].description` | **Quill 富文本 HTML** | 依定稿完整填入 | **✅ 完整支援** | 工作說明主體（職位範疇用引言框，成果用列表＋重點底色） |
| | `experiences[i].skill` | **字串陣列 (Tags)** | 僅填有佐證之官方標籤 | ❌ 否 | 經歷卡片底部 `#Tag` 圓角膠囊 |
| **`skill`** | `skills[i].name` | 純文字 | 鎖定定稿 6 項標題 | ❌ 否 | 6 大專長卡片標題 |
| | `skills[i].desc` | **純文字** | 依定稿完整填入 | **❌ 否 (禁 HTML)**| 專長能力說明（填 HTML 會直接露出原始碼！） |
| | `skills[i].tag` | **字串陣列 (Tags)** | 僅填有佐證之官方標籤 | ❌ 否 | 專長卡片內標準技能膠囊標籤 |
| **`jobCondition`**| `jobCondition.preferJobTitle` | 字串陣列 | 鎖定使用者設定 | ❌ 否 | 希望職稱 |
| | `jobCondition.preferJobContent`| **純文字 (換行)** | 500 字內 | **❌ 否 (禁 HTML)**| 求職偏好詳細工作內容描述 |
| | `jobCondition.salary` | 物件 | 鎖定使用者設定 | ❌ 否 | 希望待遇 |
| **`bio`** | `bio.chi` | **Quill 富文本 HTML** | 依定稿完整填入 | **✅ 完整支援** | 中文自傳全文（每段以 `<p>` 包裹） |
| **`project`** | `projects[i].name` | 純文字 | 鎖定定稿 4 項標題 | ❌ 否 | 專案成就卡片標題 |
| | `projects[i].introduction`| **Quill 富文本 HTML** | 依定稿完整填入 | **✅ 完整支援** | 專案背景與具體內容 |

---

## 三、Quill 富文本 HTML 樣式規範（僅包裝視覺，不改內文）

104 前端採用基於 Quill.js 的富文本引擎。在將 `final_resume.md` 轉為 `104.md` 的 Quill HTML 時，請嚴格遵守以下標籤映射規則：

### 1. 官方支援之 HTML 視覺映射表

| 原稿結構 | 轉換後之 104 Quill HTML 語法 | 規範與注意事項 |
| :--- | :--- | :--- |
| **職位範疇（第一點）** | `<blockquote>職位範疇：負責人力銀行企業端招募系統...</blockquote>` | 將各職位的第一點「職位範疇」放入 `<blockquote>` 引言框中，文字一字不改。 |
| **一般經歷列點** | `<ul><li>原稿句子一字不改。</li></ul>` | **嚴禁**在 `<li>` 開頭無中生有加上 `<strong>標題：</strong>`！ |
| **父子縮排子項目** | `<li class="ql-indent-1">原稿子項句子一字不改。</li>` | **注意**：必須直接放在同一個 `<ul>` 下並加上 `class="ql-indent-1"`，**嚴禁在 `<li>` 內再包一層 `<ul>`**（會導致 Quill 渲染錯誤）。 |
| **關鍵數據螢光筆 (金黃)** | `<span style="background-color: #fbf3db;">743 件（88%）</span>` | 僅包裹原稿已存在的**核心量化數據或指標變化**，不改動文字。 |
| **核心產品/功能標記 (晴藍)**| `<span style="background-color: #deebf1;">新版求才系統</span>` | 僅包裹原稿已存在的**核心產品名或關鍵模組名**，每點最多 1 處，避免畫面花俏。 |
| **自傳段落** | `<p>原稿自然段文字...</p><p><br></p>` | 自傳每段以 `<p>` 包裹，段落間可用 `<p><br></p>` 維持呼吸感。 |

---

### 2. 工作經歷 (`experience.experiences[i].description`) 正確轉換範例（100% 忠於定稿）

```html
<blockquote>職位範疇：負責人力銀行企業端招募系統（企業刊登職缺、處理應徵與聯繫求職者，服務約 6 萬家活躍付費廠商，2026 Q3），擔任 Product Owner（正式職稱：產品企劃主任），帶領 2 名直屬產品企劃，協調工程、設計、業務、客服等單位，負責既有服務迭代與新版規劃。</blockquote>
<ul>
  <li>主責企業端招募系統的需求分析、流程與原型設計、規格撰寫，與 QA 制定驗收案例並與工程團隊協作，完成<span style="background-color: #fbf3db;">約 50 項主要功能上線（2023/12–2026/03）</span>。</li>
  <li>接手企業端招募系統改版（<span style="background-color: #deebf1;">新版求才系統</span>），在須沿用既有業務後台與資料庫的限制下，以實測與內部訪談還原缺乏文件的權限及計費規則，整理成新版流程與規格，與工程團隊分階段完成帳號登入、企業資料等功能改版；帳號、登入、公司資料、聯絡人相關的 <span style="background-color: #fbf3db;">840 件廠商建議已完成 743 件（88%）</span>。</li>
  <li>回應企業客戶多年反映、懸而未決的商業需求（企業端招募系統），規劃兩個方案：</li>
  <li class="ql-indent-1">針對 2021–2026/10 累積的 <span style="background-color: #fbf3db;">199 件即時通相關建議</span>，規劃整合原本分散於信件與即時通兩個重複功能的聯繫流程，讓求職者與企業順利邀約面試，協調工程與相關單位推進，目前開發中。</li>
  <li class="ql-indent-1">回應自 2020/12 起累積的 <span style="background-color: #fbf3db;">55 件相關廠商建議</span>，規劃<span style="background-color: #deebf1;">群組功能</span>，讓大型企業按部門或分店共同處理招募，定義帳號、職缺與履歷的存取關係及既有資料轉換方式，補足原系統只有全公司與個人兩種資料範圍的限制，與工程團隊協作上線。</li>
</ul>
```

---

## 四、草稿 `104.md` 內嵌指令語法規格 (Directive Specification)

在產出 `104.md` 時，於各區塊上方嵌入以下 HTML 註解包裹之 JSON 指令，供執行 Agent 直接解析填表：

```markdown
<!-- @104-directive
{
  "target_block": "experience",
  "index": 0,
  "action": "replace_description",
  "mode": "quill_html",
  "tags": ["Claude", "Wireframe", "Figma", "Axure RP", "專案溝通╱整合管理", "製作規格說明書"],
  "locked_fields": ["companyName", "jobName", "duration", "workArea", "management"]
}
-->
```

---

## 五、排版避坑與 Flash 執行防呆清單（必讀）

1. **嚴禁留下空的清單項 (`<li></li>` 或 `<p></p>` 空標籤)**：
   - 104 Quill 編輯器遇到空白的 `<li>` 會在前台渲染出孤立的黑色圓點。
2. **純文字欄位嚴禁填入 HTML 標籤**：
   - `skill.skills[i].desc`（專長說明）、`info.trait`（個人特色）、`jobCondition.preferJobContent` 為**純文字欄位**，嚴禁放入 `<p>`、`<strong>` 或 `<span>`，否則前台會直接印出 HTML 原始碼！
3. **禁止巢狀 `<ul><ul>`**：
   - 子項目縮排請一律使用扁平 `<ul>` 搭配 `<li class="ql-indent-1">`。
4. **嚴禁自行捏造標籤或改動定稿文字**：
   - 執行 Agent（Flash）的工作是**「精準搬運工」**，直接讀取區塊內的 HTML / 純文字貼入對應欄位，不得自行增刪字句或填入未經授權之標籤。
