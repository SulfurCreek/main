<!--markdownlint-disable MD013-->

> 本人 2026-10-23 提供，原樣保存；**產生 104 md 時必跑**（樣式＋`@104-directive`）。**範例文字只取格式，不取事實**（同 `content-spec-quill.md`；事實一律以 `../library/` 為準）。
>
> **Career Move 套用附註（衝突時以此為準）**
> 1. 範例中的成效數字與做法（提升結案效率 30%、降低申訴率 45%、多組 Email 綁定、異常行為偵測、每兩週 Sprint、JIRA、Git、Tableau、SimilarWeb 等）**library 皆無依據，不得照抄**。
> 2. 範例 `<li><strong>核心動詞</strong>：…` 的粗體開頭與 `verify_polish.py` 禁用的粗體摘要開頭衝突；正文 `<li>` 不用粗體前綴，粗體只用在段落小標（`<p><strong>【…】</strong></p>`）。
> 3. 專長卡片數依 `../library/decisions.md` §26（6 筆），不照範例的 4 張；卡片內容依 §28 寫跨職位通用能力。
> 4. 「主導」只用在 library 允許的事（decisions §1）；範例的「主導系統架構升級」不採用。
> 5. 標籤須同時符合 104 官方白名單**與** library 有使用紀錄；白名單裡有但本人沒用過的工具不放。

# 104 人力銀行全欄位格式設定與自動化指令指南 (104 Field Styling & Directive Guide)

> **版本**：2.0.0 (2026 最新版)  
> **適用平台**：104 會員中心履歷編輯器 (`https://pda.104.com.tw/profile/edit?vno={vno}`)  
> **核心用途**：提供給內容生成 AI（如 Claude Code / 履歷撰寫 Agent）與執行 Agent（Antigravity 104-resume-manager），定義 104 履歷每一欄位的資料型態、字數限制、Quill 富文本 HTML 排版語法、版型代碼、官方標籤白名單驗證，以及**在產出 `104.md` 草稿時直接嵌入機器可讀指令的標準語法**。

---

## 一、核心原則與安全約束

1. **嚴格白名單原則 (Strict Whitelist Enforcement)**：
   - 所有擅長工具與工作技能標籤（Tags），**嚴格只能從官方分類表挑選**（擅長工具 768 項、工作技能 1,328 項）。
   - **嚴禁自造、縮寫或任意更改標籤字串**（例如不可使用「UI/UX」，必須使用官方詞彙「使用者介面設計」；不可使用「CRM」當工具）。
2. **版型變更強制停詢原則**：
   - 凡涉及 `layout`、主題版型（Themes）或背景色變更，必須在指令中明確宣告或向使用者展示確認，未獲明確許可前嚴禁自行覆寫。
3. **未獲指示絕對不碰瀏覽器**：
   - 執行更新前須有明確 `/browser` 指示；未獲指示時，所有文稿與比對一律在本地端靜態驗證。

---

## 二、104 全欄位資料型態與規格總覽

| 區塊 (Block) | 欄位路徑 (Field Path) | 資料型態 | 字數/數量限制 | 支援 Quill HTML | 呈現位置與視覺效果 |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **`info`** | `info.bio` | 純文字/HTML | 建議 150~250 字 | ⚠️ 部分支援 | 履歷最頂部名片卡個人摘要 |
| | `info.trait` | 字串陣列 | 上限 5 組，每組 15 字 | ❌ 否 | 頂部圓角特質標籤 |
| | `info.personalLink1~3` | URL 字串 | 最多 3 組 | ❌ 否 | 個人網站/GitHub/LinkedIn 連結 |
| **`experience`** | `experiences[i].companyName` | 純文字 | 60 字內 | ❌ 否 | 公司名稱 (結構欄位，通常鎖定) |
| | `experiences[i].jobName` | 純文字 | 60 字內 | ❌ 否 | 職務名稱 |
| | `experiences[i].duration` | 物件 `{start, end}` | 年月格式 `YYYY-MM` | ❌ 否 | 任職起訖年月、在職狀態 |
| | `experiences[i].management` | 物件 `{hasManage, count}`| 管理責任代碼 | ❌ 否 | 帶人實績（HR 後台硬篩選認證） |
| | `experiences[i].description` | **Quill 富文本 HTML** | 建議 800~1500 字 | **✅ 完整支援** | 工作說明主體 (支援標題、引用框、螢光標記、列表) |
| | `experiences[i].skill` | **字串陣列 (Tags)** | **每間填滿 6~8 項** | ❌ 否 | 經歷卡片底部 `#Tag` 圓角膠囊 |
| **`skill`** | `skills[i].name` | 純文字 | 15 字內 | ❌ 否 | 4 大專長卡片標題 |
| | `skills[i].desc` | 純文字 | 100~200 字 | ❌ 否 | 專長能力情境說明 |
| | `skills[i].tag` | **字串陣列 (Tags)** | **每卡填滿 8 項** | ❌ 否 | 專長卡片內標準技能膠囊標籤 |
| **`jobCondition`**| `jobCondition.preferJobTitle` | 字串陣列 | 最多 3 項 | ❌ 否 | 希望職稱 |
| | `jobCondition.preferJobContent`| **純文字 (換行)** | 500 字內 | ❌ 否 (僅支援換行) | 求職偏好詳細工作內容描述 |
| | `jobCondition.salary` | 物件 | 面議 / 範圍數值 | ❌ 否 | 希望待遇 |
| | `jobCondition.remoteWork` | 布林值 / 代碼 | 1 / 0 | ❌ 否 | 遠端工作意願 |
| **`bio`** | `bio.chi` | **Quill 富文本 HTML** | 建議 800~1200 字 | **✅ 完整支援** | 中文自傳全文 |
| | `bio.eng` | **Quill 富文本 HTML** | 建議 300~600 字 | **✅ 完整支援** | 英文自傳全文 |
| **`education`** | `educations[i].name` | 純文字 / 學校代碼 | 60 字內 | ❌ 否 | 學校名稱 (第 1 筆為最高學歷) |
| | `educations[i].departments`| 純文字 | 60 字內 | ❌ 否 | 科系所名稱 |
| | `educations[i].status` | 代碼 | 1:畢業, 2:肄業, 3:在學| ❌ 否 | 就學狀態 |
| **`project`** | `projects[i].name` | 純文字 | 40 字內 | ❌ 否 | 專案成就卡片標題 |
| | `projects[i].introduction`| **Quill 富文本 HTML** | 400~800 字 | **✅ 完整支援** | 專案成果、技術架構、量化績效 |
| | `projects[i].url` | URL 字串 | 網址 | ❌ 否 | 外部作品集或專案 DEMO 連結 |

---

## 三、各欄位格式規範與 Quill 富文本樣式庫

104 前端採用自研基於 Quill.js 的富文本引擎，對於支援富文本的欄位（`experience.description`、`bio.chi`、`project.introduction`），**直接提供標準 HTML 結構即可達到頂級視覺效果**。

### 1. 104 官方認可且完全支援之 HTML 樣式庫

| 樣式需求 | 官方推薦 HTML 語法 | 渲染效果與使用情境 |
| :--- | :--- | :--- |
| **核心職掌引言框** | `<blockquote><strong>【職掌範疇】</strong><br>負責...</blockquote>` | 淺灰底背景＋左側厚色條，非常適合作為工作經歷開頭的職務定位與團隊規模說明。 |
| **區塊大標題 (一級)** | `<p><span class="ql-size-large" style="color: #00afb8;"><strong>一、重大成果</strong></span></p>` | 104 專屬 `ql-size-large` 搭配官方湖水綠色標題，層次分明。 |
| **二級小標題** | `<p><strong>【核心系統重構】</strong></p>` | 標準粗體標題。 |
| **螢光筆亮點劃線 (金黃)** | `<span style="background-color: #fbf3db;">提升結案效率達 30%</span>` | 淡金黃底色，專門用於**數字、營收、日活躍增長率、節省時間**。 |
| **螢光筆輔助劃線 (晴藍)** | `<span style="background-color: #deebf1;">B2B SaaS 招募體系</span>` | 淡晴藍底色，用於**關鍵技術架構、核心商業模式**。 |
| **結構化項目列表** | `<ul><li><strong>核心動詞</strong>：量化實績與具體作為。</li></ul>` | 條列化 STAR 原則呈現，易讀性最高。 |
| **子項目縮排列表** | `<li class="ql-indent-1">子項目細部說明與配合事宜。</li>` | 縮排一層，凸顯主從從屬關係。 |
| **原生段落水平線** | `<hr class="ql-divider">` | 104 原生水平分隔 Blot，用來區分工作成果與底部工具列。 |
| **備註／底部標籤列** | `<p><small style="color: #7e7e7e;"><strong>核心工具</strong>：Axure・Figma・UML</small></p>` | 7e7e7e 淺灰小字，作補充收斂。 |

---

### 2. 工作經歷 (`experience.experiences[i].description`) 最佳實踐範本

```html
<blockquote><strong>【職掌範疇與管理責任】</strong><br>負責企業端招募管理系統（服務 60,000+ 付費企業），協同跨部門 10 個關係單位，帶領 2 名直屬產品企劃，主導系統架構升級與 AI 人才推薦落地。</blockquote>

<p><span class="ql-size-large" style="color: #00afb8;"><strong>一、核心系統架構升級與商業規則落地</strong></span></p>
<ul>
  <li><strong>新版求才系統架構規劃</strong>：主責逾 50 項核心功能規劃，重塑企業子帳號權限與計費體系，<span style="background-color: #fbf3db;">提升提案結案效率達 30%</span>。</li>
  <li><strong>產品規格與驗收標準化</strong>：獨立撰寫完整 PRD、Flowchart、Wireframe 與原型，協同 QA 制定測試案例，實現每兩週一次 Sprint 的穩定交付。</li>
  <li><strong>企業客戶商業需求響應</strong>：
    <ul>
      <li class="ql-indent-1">推動企業使用者多組 Email 登入綁定機制，解決長期跨部門共用痛點。</li>
      <li class="ql-indent-1">建立分層權限授權矩陣，降低帳號外洩風險。</li>
    </ul>
  </li>
</ul>

<p><span class="ql-size-large" style="color: #00afb8;"><strong>二、AI 智慧推薦整合與風險防護</strong></span></p>
<ul>
  <li><strong>AI 智慧人才推薦落地</strong>：協同資料科學團隊完成推薦模型整合，將候選人精準嵌入企業招募工作流，提升企業主動聯絡率。</li>
  <li><strong>資安冒用防護機制</strong>：建立異常行為偵測告警，<span style="background-color: #fbf3db;">降低客服進線申訴率 45%</span>。</li>
</ul>

<hr class="ql-divider">
<p><small style="color: #7e7e7e;"><strong>核心工具與專業</strong>：PRD・Wireframe・Axure RP・Figma・UML・Scrum・JIRA・Claude・LLM・B2B SaaS</small></p>
```

---

### 3. 專長模組 (`skill.skills[i]`) 4 大卡片與標籤「選好選滿」規範

- **前台展現**：104 專長模組建議設定為**卡片式 (`SkillThemeCard`)**，`tag` 會渲染為圓角彩色徽章。
- **後台篩選機制**：企業 HR 後台搜尋引擎（Solr）依據標籤進行精確比對。**每張卡片嚴格填滿 8 項標準標籤，4 張卡片共 32 項**。
- **PM 推薦 4 大專長「選好選滿」配置清單**：

#### 卡片 1：產品策略與商業變現 (8 項填滿)
- **卡片名稱**：`產品策略與商業變現`
- **能力說明**：具備 B2B SaaS 與訂閱制定價實驗、VIP 付費牆規劃、海外金流串接及數據指標監控實績。
- **標準標籤 (#Tags)**：
  `Tableau`、`Google Analytics`、`SaaS`、`SimilarWeb`、`產品策略`、`產品定位`、`產品營運`、`數據分析`

#### 卡片 2：產品規劃與架構設計 (8 項填滿)
- **卡片名稱**：`產品規劃與架構設計`
- **能力說明**：精通從需求訪談、用戶旅程拆解到撰寫標準 PRD、Flowchart、Wireframe 與互動原型，建立完整驗收標準。
- **標準標籤 (#Tags)**：
  `Figma`、`Axure RP`、`Wireframe`、`Prototype`、`UML`、`Systems Analysis`、`製作規格說明書`、`軟體工程系統開發`

#### 卡片 3：跨部門推進與敏捷專案管理 (8 項填滿)
- **卡片名稱**：`跨部門推進與敏捷專案管理`
- **能力說明**：具備協同跨職能（工程、UIUX、業務、法務、資料）團隊推進 Scrum 雙週迭代與進度風險控管能力。
- **標準標籤 (#Tags)**：
  `Scrum`、`JIRA`、`Git`、`Xmind`、`專案溝通╱整合管理`、`專案規劃執行╱範圍管理`、`專案時間╱進度控管`、`功能測試(function test)`

#### 卡片 4：生成式 AI 與數據驅動創新 (8 項填滿)
- **卡片名稱**：`生成式 AI 與數據驅動創新`
- **能力說明**：深度運用生成式 AI（Claude, ChatGPT）輔助競品分析、PRD 產出與驗收案例制定，並具備 AI 人才推薦模型落地實務。
- **標準標籤 (#Tags)**：
  `ChatGPT`、`Claude`、`Gemini`、`LLM`、`Prompt`、`Google Tag Manager`、`Machine Learning`、`機器學習`

---

### 4. 求職條件 (`jobCondition`) 填寫規範

- **工作內容描述 (`preferJobContent`)**：
  - **型態**：純文字（支援一般換行，**不支援 HTML 標籤**）。
  - **規範**：條列化呈現目標職務之職能範疇，例如：
    ```text
    1. 負責 B2B SaaS / 平台型產品之產品架構規劃、規格撰寫 (PRD/Wireframe) 與敏捷交付管理。
    2. 主導商業模式變現機制、訂閱制計費邏輯與定價實驗。
    3. 推動生成式 AI 與數據驅動應用落地，優化使用者體驗與營運效率。
    4. 橫向跨部門協調整合工程、UI/UX、商業營運與客服單位，確保產品按時上線與達成商業目標。
    ```
- **希望待遇 (`salary`)**：若無特殊指定，一律保持 `面議`。
- **上班地點與可上班日**：嚴格鎖定使用者偏好，未經指示不得更動。

---

## 四、草稿 `104.md` 內嵌指令語法規格 (Directive Specification)

當另一位 Agent（如 Claude）或您在撰寫履歷草稿 `104-vXX.md` 時，**請在文檔中使用以下標準指令區塊（Directives）**。
Antigravity 104-resume-manager 能直接解析這些指令，精準、無誤地執行自動化更新：

### 1. 指令區塊語法結構
採用標準 HTML 註釋包裹 JSON 結構：

```markdown
<!-- @104-directive
{
  "target_block": "experience",
  "index": 0,
  "action": "replace_description",
  "mode": "quill_html",
  "tags": ["Scrum", "Claude", "Wireframe", "Figma", "專案溝通╱整合管理", "製作規格說明書"],
  "locked_fields": ["companyName", "jobName", "duration", "workArea"],
  "notes": "回應企業客戶需縮排一層；不可留下空白圓點"
}
-->
```

### 2. 指令核心欄位說明表

| 指令屬性 | 可選值 | 意義與行為說明 |
| :--- | :--- | :--- |
| `target_block` | `experience` \| `skill` \| `jobCondition` \| `bio` \| `education` \| `project` \| `layout` | 目標 104 模組區塊 |
| `index` | 整數 `0`, `1`, `2`... | 目標項目的索引陣列位置（例如第 0 筆為當前最新經歷） |
| `action` | `replace_description` \| `replace_tags` \| `replace_all` \| `append` \| `update_theme` | 指定執行動作 |
| `mode` | `quill_html` \| `plain_text` \| `json_object` | 內文格式型態。若為 `quill_html`，執行時將直接保留 HTML 標籤寫入。 |
| `tags` | 字串陣列 `["Tag1", "Tag2"...]` | 指定寫入之 104 官方標準標籤（須符合 768/1,328 字典） |
| `locked_fields`| 字串陣列 `["companyName", "duration"...]` | 強制鎖定不可更動之欄位 |
| `theme_suggestion` | 主題代碼（如 `"chronological"` 或 `3`） | 建議套用之版型（執行前仍會依鐵律提示確認） |

---

## 五、實戰範例：帶有標準指令的 `104-vXX.md` 完整範本

以下為產出 `104-vXX.md` 時推薦的標準 Markdown 結構：

````markdown
# 104 履歷版本更新草稿 (v11.4)

> 目標履歷：76js7patq
> 變更範疇：更新 3 筆工作經歷說明、4 大專長卡片標籤選好選滿、更新求職偏好工作內容。

---

## 區塊一：工作經歷 (Experience)

### 1. 全球華人股份有限公司 (經歷 0)

<!-- @104-directive
{
  "target_block": "experience",
  "index": 0,
  "action": "replace_description",
  "mode": "quill_html",
  "tags": ["Scrum", "Claude", "Wireframe", "Figma", "專案溝通╱整合管理", "製作規格說明書", "系統架構規劃", "軟體工程系統開發"],
  "locked_fields": ["companyName", "jobName", "duration", "workArea", "management"]
}
-->

▼ 【以下內容以 Quill HTML 模式貼入 description 欄位】
```html
<blockquote><strong>【職掌範疇與管理責任】</strong><br>負責企業端招募系統，協調 10 個關係單位，帶領 2 名企劃。</blockquote>
<p><span class="ql-size-large" style="color: #00afb8;"><strong>一、核心系統重構與商業落地</strong></span></p>
<ul>
  <li><strong>新版求才系統架構規劃</strong>：主責 50 項主要功能規劃，<span style="background-color: #fbf3db;">提升結案效率達 30%</span>。</li>
  <li><strong>產品規格與驗收標準化</strong>：獨立撰寫 PRD、Flowchart、Wireframe 與原型。</li>
  <li><strong>企業需求深度響應</strong>：
    <ul>
      <li class="ql-indent-1">多組 Email 登入綁定機制，解決長期帳號共用痛點。</li>
      <li class="ql-indent-1">分層權限授權矩陣，降低外洩風險。</li>
    </ul>
  </li>
</ul>
<hr class="ql-divider">
<p><small style="color: #7e7e7e;"><strong>核心工具</strong>：PRD・Wireframe・Axure RP・Figma・UML・Claude・Scrum</small></p>
```

---

## 區塊二：專長與技能 (Skill)

<!-- @104-directive
{
  "target_block": "skill",
  "action": "replace_tags",
  "mode": "json_object",
  "notes": "4 大卡片各選滿 8 項標準標籤，共 32 項官方 Tag"
}
-->

### 專長卡片「選好選滿」配置清單：
1. **產品策略與商業變現**
   - 標籤：`#Tableau` `#Google Analytics` `#SaaS` `#SimilarWeb` `#產品策略` `#產品定位` `#產品營運` `#數據分析`
2. **產品規劃與架構設計**
   - 標籤：`#Figma` `#Axure RP` `#Wireframe` `#Prototype` `#UML` `#Systems Analysis` `#製作規格說明書` `#軟體工程系統開發`
3. **跨部門推進與敏捷專案管理**
   - 標籤：`#Scrum` `#JIRA` `#Git` `#Xmind` `#專案溝通╱整合管理` `#專案規劃執行╱範圍管理` `#專案時間╱進度控管` `#功能測試(function test)`
4. **生成式 AI 與數據驅動創新**
   - 標籤：`#ChatGPT` `#Claude` `#Gemini` `#LLM` `#Prompt` `#Google Tag Manager` `#Machine Learning` `#機器學習`

---

## 區塊三：求職條件 (Job Condition)

<!-- @104-directive
{
  "target_block": "jobCondition",
  "action": "replace_field",
  "field": "preferJobContent",
  "mode": "plain_text",
  "locked_fields": ["preferJobTitle", "salary", "workArea", "onboardDate", "remoteWork"]
}
-->

▼ 【以下內容以純文字模式替換 preferJobContent】
```text
1. 負責 B2B SaaS / 平台型產品之產品架構規劃、規格撰寫 (PRD/Wireframe) 與敏捷交付管理。
2. 主導商業模式變現機制、訂閱制計費邏輯與定價實驗。
3. 推動生成式 AI 與數據驅動應用落地，優化使用者體驗與營運效率。
4. 橫向跨部門協調整合工程、UI/UX、商業營運與客服單位，確保產品按時上線與達成商業目標。
```
````

---

## 六、排版避坑與嚴禁事項清單

1. **嚴禁留下空的清單項 (`<li></li>` 或 `• ` 空圓點)**：
   - 104 Quill 編輯器遇到空行或空白的 `<li>` 會在前台渲染出孤立的黑色圓點，嚴重破壞版面專業度。輸出 HTML 前務必確認每個 `<li>` 內皆有有效文字。
2. **純文字欄位嚴禁填入 HTML 標籤**：
   - `jobCondition.preferJobContent` 與 `skill.skills[i].desc` 為純文字欄位。填入 `<p>` 或 `<strong>` 會直接原樣噴出角括號原始碼！
3. **嚴禁更動結構化欄位 (Locked Fields)**：
   - 公司全名、就任年月、學校全名、希望待遇（面議）、希望工作地點，均為驗證與篩選硬欄位，嚴禁擅自修改。
4. **標籤字串嚴格一致**：
   - 104 系統不會模糊容錯，`Axure RP` 不可寫成 `Axure`，`Google Analytics` 不可寫成 `GA`。必須嚴格遵循官方字典。
