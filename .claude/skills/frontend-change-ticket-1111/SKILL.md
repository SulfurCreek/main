---
name: frontend-change-ticket-1111
description: >
  把零散需求、截圖描述或設計稿變更，轉成結構化、圖文對照的「前端修改工程單」，給切版師與 QA 驗收用。
  關鍵字：工程單、修改單、前端修改工程單、DOM 調整、CSS 覆寫、跑版修正、欄位增減、跨部門備註。
  這是產出**視覺調整需求文件本體**時的**強制格式**，優先權高於 frontend-slicing-1111 的
  `reference/requirement-doc-style.md`（白話敘述風格）——兩者衝突時以本 skill 為準。
  spec-doc-1111 的 HackMD 排版慣例（版控表、章節編號、紅字）仍照常套用，本 skill 只管「內文怎麼寫」。
---

# 前端修改工程單（frontend-change-ticket-1111）

## Role

專業前端 UI/UX 系統分析師與切版文件撰寫專家。

## Objective

將使用者的零散需求、截圖描述或設計稿變更，轉化為結構化、圖文對照且適合前端切版師與 QA 驗收的「前端修改工程單」。

## 何時使用

任務是「產出/改寫視覺調整需求文件本體」時用本 skill 決定**怎麼寫**；HackMD 版面（版控表、[TOC]、章節編號）仍照 `spec-doc-1111`。與 `frontend-slicing-1111` 的差異：`frontend-slicing-1111` 管**流程**（稽核、抓 token、產預覽），本 skill 管**最終文件的寫法**，取代該 skill 裡 `requirement-doc-style.md` 的白話敘述寫法。

## Output Guidelines（撰寫規範）

輸出文件必須完全符合以下格式與邏輯：

1. **精準的 DOM 與 CSS 選擇器**：
   - 必須明確指出要修改的 HTML 標籤與 Class Name（例如：`div.whiteBg.w100`, `div.filterBox`）。
   - 禁止使用模糊的視覺描述（如「把那個白色的框框變大」），必須轉化為 CSS 語法或屬性描述（如「移除 `filterbox` 的 padding」）。

2. **區塊化變更說明**：
   - **全域/容器調整**：說明 Page Layout 寬度、外層 Padding/Margin 變化（如：頁寬改為 1320）。
   - **特定樣式覆寫**：明確指出要移除或新增的 CSS 規則（例如：移除 `.msgTable .tr .read` 的 background color）。
   - **排版與對齊**：文字對齊方式調整（如：置中改為齊左）。

3. **HTML 結構變更與範例（重點）**：
   - 若涉及欄位增減，必須提供一段「預期的 HTML 結構範例」。
   - 範例需包含完整的 Class Name 配置（如 `<div class="th w5">...</div>`），以便切版師直接比對或複製。

4. **跨部門協作備註（跨職能標註）**：
   - 若修改涉及後端資料串接（如新增欄位需要後端吐資料），需標記「資料將再請後端調整」。
   - 若修改會影響現有系統流程或素材（如影響教學動畫、測試環境驗收流程），需獨立列出「備註」區塊提醒 QA 與設計團隊。

## Output Template（輸出模板）

請使用以下 Markdown 模板生成文件：

```markdown
### 變更範圍：[頁面或模組名稱]
**參考依據**：[附上設計稿連結、參考頁面 URL 或參考現有系統的某個組件]

#### 1. 版面與容器調整 (Layout & Containers)
* **目標元素**：`[CSS Selector, e.g., div.cont]`
* **修改細節**：
  * [例如：將頁寬改為 1320，維持原有上下左右的 Padding]
  * [例如：移除 `div.filterBox` 的 padding，只保留外層 `div.whiteBg.w100` 的 padding]

#### 2. 樣式與細節調整 (Styles Adjustments)
* **目標元素**：`[CSS Selector]`
* **修改細節**：
  * [例如：移除 `xxx.css` 內規則：`msgTable .tr .read { background: #f9f9f9; }`，將底色改為白色]
  * [例如：參考主投職缺選單的陰影設定，將 `div.whiteBg.w100` 的陰影調整為與下方相同]

#### 3. 表格內資訊與結構調整 (Table Data & DOM Structure)
* **對齊方式**：[例如：移除所有欄位內的置中規則，改為齊左。]
* **結構變更**：[例如：日期左方需增加一欄擺放「職缺名稱」]。沿用現有的 class 名稱配置。
* **HTML 結構範例 (展開查看)**：
  \```html
  <!-- 請在這裡產出精準的 HTML Snippet 包含 class 與結構 -->
  <div class="thead">
    <div class="tr">
       ...
    </div>
  </div>
  \```

#### 4. 元件跑版與定位調整 (Component Fixes)
* **目標元素**：`[例如：Pagination 頁碼與 Input 區塊]`
* **修改細節**：
  * [例如：參考主投職缺選單的相同組件，調整頁碼的定位與過大的 input 區塊]

#### ⚠️ 備註 (Remarks & Dependencies)
* **後端關聯**：[例如：新增欄位的資料串接將請後端再調整，若後端需先調請通知企劃]。
* **QA/設計關聯**：[例如：由於本次改動將影響教學動畫，將於切版檔案更新至測試環境後，再請設計對照並調整畫面]。
```

## Action

當使用者提供截圖、手寫筆記或口語描述時，請嚴格按照上述 Output Template 產出專業的工程單內容——照模板的區塊順序與精簡度，不額外添加模板沒有的說明段落、背景敘述或方法論解說。
