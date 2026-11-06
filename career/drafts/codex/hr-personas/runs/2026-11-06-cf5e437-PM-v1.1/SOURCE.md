# R21｜候選固定快照

來源：cf5e43749e0075398d5e72956d5417fed12df8ad，career/02_codex_stage/104-PM-v1.1.md。
候選blob：f49f2a3979ba73d0b8050298128135da415a9764。以下原文保存供追溯，內含編輯及104操作註解；註解不當作外部HR可見實績。

<!--markdownlint-disable MD013 MD033-->

# 104 履歷｜PM 版 v1.1｜Writer 編輯候選

> 固定來源：`ad68d63` 的 `career/drafts/PM-v1.1/104-PM-v1.1.md`。治理讀取版本：`28100b76986dc26b2bc6f79a5c03ad3921b2b93d`。保留本輪 Marketer 新增內容與 104 結構；修改理由及待確認事項另附。
> 編輯裁定（2026-11-06，本人要求）：結案率維持季度窗口（介入前 2024 Q4–2025 Q3、介入後 2025 Q4–2026 Q3），52%→79% 不重算；後續不得自行改回月份。

> 排版依 `career/104/styling-directive-guide.md` v2.3.0：子項為獨立 `<li style="margin-left: 1em;">`、模組大標上下 `<p><br></p>` 留白（產出即定版，下游零加工原樣貼入）、金黃＝成果數字、晴藍＋粗體＝核心產品／系統、粗體＝專案／系統／產品／buzzword。**底色與粗體依 Codex 在定稿註解標的 [G]／[B]／[BT]**；依 v14 定稿及本人終修內容，配合 104 欄位重編。
> **專案圖片**：本檔與 `images/` 資料夾一起打包；每個專案的 directive 以 `image` 指定相對路徑：5.1→project1_justdating_juicy.png、5.2→project2_kool.png、5.3→project3_1111_recruit.png、5.4→project4_1111_recruit.png。
> 標籤只用 `career/104/tool_categories.md`／`skill_categories.md` 清單內名稱，找不到就略過。

---

## 0. 全站版型（需本人確認後才套用）

<!-- @104-directive
{"target_block": "layout", "action": "update_theme", "requires_confirmation": true, "theme_suggestion": "chronological", "skill_display": "SkillThemeCard", "accent_color": "#566876", "notes": "Senior PM／PO 定位：經歷時序式、專長卡片式、名片主題用沉穩商務色（煙燻冷藍）。版型變更須本人確認後才套用。"}
-->

---

## 1. 個人簡介

<!-- @104-directive
{"target_block": "info", "action": "replace_field", "field": "bio", "mode": "plain_text"}
-->

```text
資深產品經理，累積近 10 年 B2C 跨國訂閱 App 與 B2B 企業平台經驗，代表實績涵蓋 App 從 0 到 1 的產品規劃、訂閱變現與企業端招募系統翻新。在網紅媒合平台 KOOL 專案中，我先訪談商家，再獨立規劃平台定位、雙邊流程與付費機制，完成 iOS、Android App 與網頁版本上線；平台上線半年累積 8 萬多次合作報名。曾主導付款管道轉型，讓網頁付款營收占比從 24% 升至 80% 以上；也透過跨平台定價對照測試，為公司調整馬來西亞價格帶提供依據。

現任 1111 人力銀行企業端招募系統 Product Owner，帶領 2 名企劃、協調約 20 人跨部門團隊，主導服務約 6 萬家付費企業的系統翻新與 AI 功能上線。我把複雜商業規則轉成產品方案，深入與工程討論，帶領團隊完成交付。我也自建 AI Agent 工作流，用於規格、測試與近 19 萬筆搜尋及配對條件清洗，並將 skill 與方法帶給 2 名企劃，納入日常工作流程。TOEIC 980，曾以全英文協作完成 App 在 7 個海外市場的在地化。
```

### 1.1 個人特色（五個分開輸入，依序；2026-11-04 本人同意更換）

<!-- @104-directive
{"target_block": "info", "action": "replace_field", "field": "trait", "mode": "plain_text"}
-->

```text
訂閱變現與跨國定價
從0到1新產品規劃
大型B2B系統翻新
自建AI Agent工作流
TOEIC 980全英文協作
```

---

## 2. 工作經歷

### 2.1 Product Owner／PM｜1111 全球華人｜2022/08–迄今

▼ management：**有管理責任，1~5 人**（直屬 2 名產品企劃）

<!-- @104-directive
{"target_block": "experience", "index": 0, "action": "replace_description", "mode": "quill_html", "tags": ["製作規格說明書", "Prototype", "Systems Analysis", "專案溝通╱整合管理", "生成式AI", "推薦系統", "工作任務╱業績項目分配", "客訴案件處理"], "locked_fields": ["companyName", "jobName", "duration", "workArea", "management"]}
-->

```html
<blockquote>我擔任企業端招募系統的 <strong>Product Owner</strong>（正式職稱：產品企劃主任），系統服務約 6 萬家付費企業。帶領 2 名直屬企劃，協調工程、設計、QA 與維運約 20 人，主導約 70 項主要功能的需求分析與規格規劃。</blockquote>
<p><br></p>
<p><span class="ql-size-large" style="color: #00afb8;"><strong>一、產品翻新與 AI</strong></span></p>
<p><br></p>
<ul>
<li><strong>接手停滯改版，主導舊系統翻新與分階段上線，回應企業 <span style="background-color: #fbf3db;">743 件</span>痛點</strong>：我接手這個停滯的改版案時，權限與商業規則沒有文件，卻必須沿用既有資料庫。我先透過實測與內部訪談盤點、還原舊系統規則，再決定採取分階段替換的方式，維持線上服務，逐步換上新版功能。封測後，分別於 2025/10、2026/01 在離峰時段切換上線。企業針對帳號與公司資料累積提出 840 件建議，每一件都是使用上的痛點；這次改版已完成 743 件（88%）。</li>
<li><strong>主導 AI 招募上線，重構推薦邏輯</strong>：先後主導<strong><span style="background-color: #deebf1;">職缺工作說明生成</span></strong>（2024/10）與<strong><span style="background-color: #deebf1;">AI 推薦人才</span></strong>（2025/11）上線，也帶領企劃完成公司簡介生成（2026/06）。我也為這些功能訂定勞動法規合規驗收標準。職類推薦串接資料科學團隊 API 時，我把人機協作邊界訂清楚：系統預設帶入推薦內容，企業手動修改後就不再覆蓋。針對人才推薦名單「少又舊」的問題，追查原因並實測主要競品，再重訂排序與重複曝光規則。</li>
<li><strong>規劃企業群組權限，支援大型企業跨部門／分店共同招募</strong>：原系統只有全公司與個人兩種資料範圍，我規劃群組權限，讓大型企業能按部門或分店共同招募。在<strong><span style="background-color: #deebf1;">群組功能</span></strong>中，訂出帳號、職缺與履歷的存取關係，以及舊資料轉換規則。功能在 2025/09 上線，回應自 2020/12 起累積的 55 件廠商建議。</li>
</ul>
<p><br></p>
<p><span class="ql-size-large" style="color: #00afb8;"><strong>二、團隊效能與服務韌性</strong></span></p>
<p><br></p>
<ul>
<li><strong>自建 AI 工作流，清洗近 19 萬筆搜尋與配對條件</strong>：企業反映搜尋語法老舊、常搜不到人，我便配合語法改版，從規則與業務邏輯盤點著手，和工程釐清前端設定如何對應搜尋引擎 <strong>Solr</strong> 的語法。用 <strong>Antigravity</strong> 試驗新語法與搜尋邏輯，取出資料庫中的廠商關鍵字，由 AI 判讀錯誤輸入的意圖，產出修正值並轉成新語法。轉換品質則用 <strong>Claude</strong> 全量交叉比對修正值與原意，針對差異反覆修正，最後由我把關，在測試環境驗證新語法的搜尋結果。這次共處理<span style="background-color: #fbf3db;">近 19 萬筆</span>搜尋與配對條件，產出<span style="background-color: #fbf3db;">逾 2 萬筆</span>修正值，也找出 7 項搜尋解析問題，列入工程待修。這套方法也用於 15 張類別代碼表對照，並提供 skill 與方法，帶 2 名直屬企劃使用，已納入工作流程。</li>
<li><strong>重整企業提案處理，30 天結案率由 52% 升至 79%</strong>：面對 880 件積壓提案，我依客戶提案優先原則排定處理順序、分派案件，帶領 2 名直屬企劃在 2025/11–12 兩個月清理 625 件。結案率比較介入前 2024 Q4–2025 Q3 與介入後 2025 Q4–2026 Q3，只計提案滿 30 天的案件。另外觀察兩群付費企業的留存：有提案獲處理的企業，年化留存率為 <span style="background-color: #fbf3db;">79.5%</span>；其餘付費企業為 74.8%，兩者相差 <span style="background-color: #fbf3db;">4.7 個百分點</span>。</li>
<li><strong>主導帳號冒用應變，補強登入防線</strong>：2026/03–04 十多家廠商招募帳號遭冒用登入，我帶領工程與客服釐清影響範圍，再設計新裝置 <strong>OTP</strong> 驗證與自助解鎖流程，補強登入防線。功能上線後一週內，便依客服回饋調整。至 2026/10，客服未再接獲廠商回報同類冒用。</li>
</ul>
```

### 2.2 Product Manager｜尚凡國際創新科技｜2018/01–2022/03

▼ management：**無管理責任**

<!-- @104-directive
{"target_block": "experience", "index": 1, "action": "replace_description", "mode": "quill_html", "tags": ["市場調查企劃與執行", "產品策略", "產品營運", "數據分析", "專案時間╱進度控管", "Electronic Payment", "iOS", "Android"], "locked_fields": ["companyName", "jobName", "duration", "workArea", "management"]}
-->

```html
<blockquote>在尚凡，我負責公司主力訂閱交友 App <strong><span style="background-color: #deebf1;">JustDating</span></strong>，以及訂閱內容 App <strong>Peach</strong>、網紅媒合平台 <strong>KOOL</strong>。JustDating 依公司公開資料，曾長期位居台灣約會類暢銷榜第一；工作中也曾以英文與歐洲金流商視訊洽談合作。</blockquote>
<p><br></p>
<p><span class="ql-size-large" style="color: #00afb8;"><strong>一、付款、定價與產品承接</strong></span></p>
<p><br></p>
<ul>
<li><strong>主導付款轉型，網頁付款營收占比最高達 91%</strong>：App 商店抽成高於網頁金流費率，我因此為 <strong><span style="background-color: #deebf1;">Peach</span></strong> 規劃付款轉型，把用戶從 App 內購導向網頁付款，並完成<strong>智冠</strong>金流串接。轉型後，網頁付款營收占比從 2020/11 的 24% 升至 2021/09 的 80% 以上，2022/02 最高達 <span style="background-color: #fbf3db;">91%</span>。</li>
<li><strong>主導 JustDating 跨平台定價對照測試，改變馬來西亞價格帶</strong>：我在 2021/05–08 主導 iOS 定價測試，依序測試原價、降價與恢復原價，並以維持原價的 <strong>Android</strong> 作為對照。結果顯示，降價期的 iOS 非續訂營收比原價期<span style="background-color: #fbf3db;">增加 5%</span>，同期 Android 卻<span style="background-color: #fbf3db;">減少 18%</span>。當 iOS 恢復原價，非續訂營收反而比原價期下滑 65%。公司根據測試結果調整馬來西亞價格帶，從原先與新加坡同級的高價區，改為與印尼、越南、泰國相同的低價帶。</li>
<li><strong>主導兩次下架承接，守住主力營收產品</strong>：JustDating 因政策遭 <strong>App Store</strong> 下架時，我主導推出沿用同一後端的 <strong><span style="background-color: #deebf1;">Juicy</span></strong> 接續服務；其後 Juicy 也遭下架，再推動 JustDating 重新上架。上線與導流期間快速拉升用戶規模：Juicy 男性 DAU 在 6 週內從約 3,200 增至 <span style="background-color: #fbf3db;">1.25 萬</span>（近 4 倍）；JustDating 在 12 週內從約 1,500 增至 <span style="background-color: #fbf3db;">1.2 萬</span>（8 倍）。</li>
</ul>
<p><br></p>
<p><span class="ql-size-large" style="color: #00afb8;"><strong>二、網紅媒合平台 0 到 1</strong></span></p>
<p><br></p>
<ul>
<li><strong>從 0 到 1 獨立規劃 <span style="background-color: #deebf1;">KOOL</span>，半年 <span style="background-color: #fbf3db;">8 萬多次</span>合作報名</strong>：沒有直接競品可參考，我先訪談商家行銷單位，摸清需求、定義平台定位，再把商家邀約與網紅報名串成雙邊流程，設計 VIP 訂閱、點數付費牆與精選曝光等付費機制。統籌設計與工程完成上線後，平台累積約 <span style="background-color: #fbf3db;">1.6 萬份</span>網紅檔案。</li>
</ul>
```

### 2.3 Associate PM｜思維特網路資訊｜2016/06–2018/01

▼ management：**無管理責任**

<!-- @104-directive
{"target_block": "experience", "index": 2, "action": "replace_description", "mode": "quill_html", "tags": ["專案溝通╱整合管理", "數據分析", "Electronic Payment", "Android"], "locked_fields": ["companyName", "jobName", "duration", "workArea", "management"]}
-->

```html
<blockquote>我負責交友 App <strong><span style="background-color: #deebf1;">SweetRing</span></strong> 的產品維運、支付與在地化規劃，App 市場涵蓋美國、墨西哥、巴西、印尼、馬來西亞、日本與韓國等 7 國。</blockquote>
<p><br></p>
<p><span class="ql-size-large" style="color: #00afb8;"><strong>一、在地支付與市場在地化</strong></span></p>
<p><br></p>
<ul>
<li><strong>開通 8 種在地付款管道，規劃訂閱方案</strong>：我為印尼、泰國導入第三方支付 <strong><span style="background-color: #deebf1;">CodaPay</span></strong>，開通電信帳單、ATM、電子錢包、便利商店、銀行轉帳等 <span style="background-color: #fbf3db;">8 種</span>在地付款管道。訂閱方案則從實收出發：比較各管道手續費率與撥款結算週期，試算淨實收，提出 7／30／90 天方案，再完成 SweetRing Android 加值頁與付款流程的規劃、上線。</li>
<li><strong>以英文協作，完成 7 個海外市場在地化</strong>：App 在地化方面，我與最多約 10 位外籍實習生以全英文會議協作，翻譯 App 介面文字及行銷素材，完成適合 7 個海外市場的在地版本。另負責 SweetRing 多國 Facebook 粉絲專頁的內容營運，最多時涵蓋 12 國：貼文內容由中文翻成英文，並監督翻譯品質。</li>
</ul>
```

### 2.4 翻譯工讀生｜台灣新蛋｜2014/08–2015/01

▼ management：**無管理責任**

<!-- @104-directive
{"target_block": "experience", "index": 3, "action": "replace_description", "mode": "quill_html", "tags": [], "locked_fields": ["companyName", "jobName", "duration", "workArea", "management"]}
-->

```html
<p>Newegg.com 商品資訊英翻中與校對。</p>
```

---

## 3. 專長（6 筆，順序與標題不動；desc 純文字）

### 3.1 AI Agent 協作

<!-- @104-directive
{"target_block": "skill", "index": 0, "action": "replace_all", "mode": "plain_text", "name": "AI Agent 協作", "tags": ["Claude", "生成式AI", "AI"]}
-->

```text
我的 AI Agent 工作流從釐清問題開始：先定義業務規則與驗證要求，再以 Claude Code、Antigravity 串起產品規劃、規格與測試。我將 skill 與方法論提供給 2 名直屬企劃，帶他們用於資料整理、規格、Wireframe 與原型，已納入工作流程。從規則盤點、資料整理及清洗，到商業邏輯與修改需求，我先把內容理清，再交由 Agent 製作 Wireframe、流程圖、Prototype、Proposal、PRD 與規格，並以 Claude 驗證結果。我依規格請 AI 產出測試案例交給 QA，也請 Agent 按案例測試；Happy Path 與 Smoke Test 則由我手動執行。這套工作流也用來整理數據、製作 one-pager 與 dashboard。
```

### 3.2 產品規劃與交付

<!-- @104-directive
{"target_block": "skill", "index": 1, "action": "replace_all", "mode": "plain_text", "name": "產品規劃與交付", "tags": ["製作規格說明書", "Prototype", "功能測試(function test)", "專案規劃執行╱範圍管理"]}
-->

```text
從 0 到 1 規劃雙邊媒合平台，我會先訪談使用者，摸清雙方需求，再定義互動流程與付費機制。將需求訪談整理成 User Journey、User Story 與 Use Case，再寫成 PRD，與 QA 一起依規格推導驗收案例、安排分階段上線。對客服、業務等內部單位，則用互動原型與 FAQ 說明新功能。
```

### 3.3 系統分析

<!-- @104-directive
{"target_block": "skill", "index": 2, "action": "replace_all", "mode": "plain_text", "name": "系統分析", "tags": ["Systems Analysis", "UML", "系統整合分析"]}
-->

```text
面對沒有文件的既有系統，我先從實際操作與內部訪談盤點、還原業務規則，再把商業邏輯拆成查詢條件，與工程確認後端如何處理。流程與系統如何互動，會透過循序圖、活動圖、使用案例圖、BPMN 及泳道圖說明；串接時，則與工程議定 API 的簽章驗證、防重放、錯誤碼、頻率限制，以及資料轉換規則。
```

### 3.4 UI/UX 規劃

<!-- @104-directive
{"target_block": "skill", "index": 3, "action": "replace_all", "mode": "plain_text", "name": "UI/UX 規劃", "tags": ["Figma", "Axure RP", "Wireframe", "Prototype", "使用者介面設計", "使用者體驗設計", "iOS", "Android"]}
-->

```text
規劃 iOS、Android App 與 Web，我會先把使用流程想清楚，以 Miro、FigJam 繪製 Flowchart，再用 Figma 畫跨裝置介面的 Wireframe、Axure RP 製作互動原型。視覺畫面則與設計師協作完成。
```

### 3.5 跨部門協作與時程

<!-- @104-directive
{"target_block": "skill", "index": 4, "action": "replace_all", "mode": "plain_text", "name": "跨部門協作與時程", "tags": ["專案溝通╱整合管理", "專案時間╱進度控管", "決策能力"]}
-->

```text
面對行銷、CRM、設計與技術等單位的需求，我依使用者旅程、開發複雜度與業務單位共識判斷取捨，再排定優先序。帶領 2 名直屬企劃交付，並協調工程、設計、QA 與維運約 20 人的工作；用甘特圖及 Trello 掌握時程，熟悉 Kanban 與瀑布式開發流程。
```

### 3.6 App 產品與變現

<!-- @104-directive
{"target_block": "skill", "index": 5, "action": "replace_all", "mode": "plain_text", "name": "App 產品與變現", "tags": ["產品策略", "產品營運", "數據分析", "Electronic Payment", "iOS", "Android"]}
-->

```text
規劃變現時，我會把訂閱定價和付款成本一起算：比較 App 內購（IAP）與網頁付款的抽成、稅、手續費及撥款週期，試算淨實收，再提出訂閱方案。曾串接本地與海外第三方金流，也以英文與歐洲金流商視訊洽談合作。曾主導訂閱內容 App Peach 的付款管道轉型，網頁付款營收占比從 24% 升至最高 91%。定價方面，以 Android 為對照組設計跨平台定價對照測試，為公司調整馬來西亞價格帶提供依據。分析交友 App JustDating、Juicy 時，追蹤註冊到首次付費的時間、付費留存率及用戶終身價值（LTV）。分析發現，用戶多在註冊後 1 週至 14 天內決定是否購買，這段期間購買者較可能續訂，否則多半流失；流失後再列為再行銷對象。付費機制的設計也涵蓋 VIP 訂閱、點數付費牆及精選曝光，並熟悉 App Store／Google Play 的審核政策與上架溝通。
```

---

## 4. 自傳

<!-- @104-directive
{"target_block": "bio", "action": "replace_field", "field": "chi", "mode": "quill_html"}
-->

```html
<p>遇到還沒成形的產品想法，我會先弄清楚各個角色想完成什麼、受到哪些限制，再思考彼此該如何互動，逐步形成能運作的產品。向團隊說明方案時，我會把流程和背後的考量一起說清楚，讓大家知道為什麼這樣設計。做過交友與訂閱制 App、網紅媒合平台，也做企業招募系統，我始終在意兩件事：使用者能不能完成想做的事，以及產品能不能支持公司持續經營。</p>
<p><br></p>
<p>規劃 <strong>KOOL</strong> 的經驗，讓我確定自己喜歡的工作：從真實需求出發，想透媒合雙方各自要完成的事。當時找不到直接競品可參考，我便從商家訪談開始，弄清楚商家要找哪一類網紅、網紅想接什麼合作，再從 0 到 1 獨立規劃平台定位、雙邊流程與付費機制，統籌設計與工程完成上線。半年內，平台累積 8 萬多次合作報名。</p>
<p><br></p>
<p>在尚凡，我負責的 <strong>JustDating</strong> 是公司的主力交友 App，具有高 DAU 與營收規模。當它遭 App Store 下架，我主導推出 <strong>Juicy</strong> 接續服務；後來 Juicy 也下架，我再推動 JustDating 重新上架。兩次都要由我串起各團隊的工作與交付，配合行銷承接既有用戶與營收，守住公司的主力營收產品。我因此熟悉了如何與 App Store 溝通、處理上架問題，也學會在延續服務與承接營收的壓力下，整合各方工作，朝共同目標完成交付。</p>
<p><br></p>
<p>我加入 <strong>1111</strong>，想參與的是整套招募系統的革新。2024 年底專案重啟後，我接手並主導企業端招募系統全面翻新。這次改版必須沿用業務後台與底層資料庫，但帳號權限怎麼運作、商業模式有哪些規則，都沒有文件可查。我從實際操作開始歸納規則，請工程確認，再找維運與稽核核對，把原本分散在舊系統與各單位經驗裡的資訊，整理成新版流程與規格。我選擇在服務持續運作的情況下改版，與工程團隊一邊調整現行功能，一邊分階段替換，於 2025/10、2026/01 完成帳號登入及企業資料等功能改版。</p>
<p><br></p>
<p>從網紅媒合走到企業招募，我看到兩種產品的共同點：先讓雙方找到彼此，再把雙方各自的操作接起來。到了企業招募，還要進一步想清楚職缺、履歷和搜尋配對之間如何連動。大型客戶需要按部門或分店共同招募，但原系統只能選全公司或個人的資料範圍。我便從帳號、職缺與履歷的關係切入，規劃<strong>群組功能</strong>，補上這一層需求。這也是我喜歡先把關係和例外想透，再向團隊說清楚的原因：讓使用者少花時間停下來摸索。</p>
<p><br></p>
<p>帶團隊使用 <strong>AI Agent</strong>，我不只看工具產出了什麼，也重視同仁是否懂得運用方法、判斷結果。同仁處理大量資料遇到困難時，我先了解他卡在哪裡，再提供自己整理的 skill 與作業方法，讓他能接著處理。產出結果仍由同仁自己判斷，少數例外再一起討論，直到工作完成交付。對我來說，AI 換了產出工作的方式，但釐清問題、想出解法、判斷結果，仍然要由人掌握。</p>
<p><br></p>
<p>訂閱變現、新產品規劃與複雜系統翻新，是我能帶進下一個團隊的實務經驗。我能從問題與規則形成產品方案，串起工程與跨部門交付，也能把 AI 方法帶進團隊的工作。在現職，系統如何翻新、需求如何排序，都是我已做過的決定。接下來，我要負責產品線或主要模組，持續把產品判斷連到使用者與商業結果。</p>
```

---

## 5. 專案成就

### 5.1 主導 JustDating／Juicy 下架承接，守住主力營收產品

- 起訖：2020/01 – 2020/06｜isInProgress：否｜url：留空
- 圖片：`images/project1_justdating_juicy.png`（104「專案素材」選「上傳圖片或影片」，把此檔上傳到「素材檔」；每個專案只放這一張）

<!-- @104-directive
{"target_block": "project", "index": 0, "action": "replace_all", "mode": "quill_html", "name": "JustDating／Juicy 下架後兩次服務承接", "media_type": "上傳圖片或影片", "image": "images/project1_justdating_juicy.png", "image_action": "upload_replace"}
-->

```html
<blockquote><strong>主導兩次主力 App 下架承接，守住主力營收產品。</strong>這個專案處理的是公司主力、高營收的訂閱制交友 App <strong><span style="background-color: #deebf1;">JustDating</span></strong>；依公司公開資料，它曾長期位居台灣約會類暢銷榜第一。因應 <strong>App Store</strong> 下架，我主導推出沿用同一套後端的 <strong><span style="background-color: #deebf1;">Juicy</span></strong> 接續服務，串起跨團隊交付與行銷導流，承接既有用戶與營收。上線與導流期間，Juicy 男性 DAU 在 6 週內由約 3,200 增至 <span style="background-color: #fbf3db;">1.25 萬</span>（近 4 倍，2020/01–02）。</blockquote>
<p>接著 <strong>Juicy</strong> 也遭下架，再推動 <strong>JustDating</strong> 重新上架。上線與導流期間，男性 DAU 在 12 週內從約 1,500 回升至 <span style="background-color: #fbf3db;">1.2 萬</span>（8 倍，2020/04–06）。</p>
<p>兩款產品的上架問題，由我與 <strong>App Store</strong> 溝通處理。在台灣以外市場，兩款產品透過 <strong>CodaPay</strong> 收款，我也負責網頁加值頁規劃、商品定價與商務合作洽談，並擔任雙方工程串接的溝通窗口。</p>
```

### 5.2 KOOL 網紅媒合平台 0 到 1 規劃

- 起訖：2018/05 – 2022/03｜isInProgress：否｜url：留空
- 圖片：`images/project2_kool.png`（104「專案素材」選「上傳圖片或影片」，把此檔上傳到「素材檔」；每個專案只放這一張）

<!-- @104-directive
{"target_block": "project", "index": 1, "action": "replace_all", "mode": "quill_html", "name": "KOOL 網紅媒合平台 0 到 1 規劃", "media_type": "上傳圖片或影片", "image": "images/project2_kool.png", "image_action": "upload_replace"}
-->

```html
<blockquote><strong>從 0 到 1 獨立規劃網紅媒合平台，半年 8 萬多次合作報名。</strong>規劃 <strong><span style="background-color: #deebf1;">KOOL</span></strong> 時，我把「網紅人力銀行」的構想轉成雙邊媒合平台：商家刊登合作邀約，網紅可以報名，也能接受商家邀請。由於沒有直接競品可參考，先訪談商家行銷單位，了解他們如何在 <strong>Instagram</strong> 尋找網紅，再參考 <strong>Airbnb</strong> 房東刊登房源的模式，設計商家與網紅的雙邊流程。</blockquote>
<p>從刊登、邀請、報名到聯繫，逐一安排商家與網紅的操作，定義雙方的操作與付費規則，再用 <strong>Miro</strong> 畫出流程圖，搭配規劃簡報向團隊說明。專案於 2018/05 啟動，由我統籌產品、設計與程式部門完成上線。平台累積約 <span style="background-color: #fbf3db;">1.6 萬份</span>網紅檔案，上線半年累計 <span style="background-color: #fbf3db;">8 萬多次</span>合作案報名。</p>
<p>付費設計包括 VIP 訂閱、點數付費牆及精選曝光；功能則加入評價、工作地點地圖、手機認證與網紅作品集，完成 iOS、Android 與網頁版本上線。</p>
```

### 5.3 1111 新版求才系統重整

- 起訖：2024/12 – ｜isInProgress：**是**｜url：留空
- 圖片：`images/project3_1111_recruit.png`（104「專案素材」選「上傳圖片或影片」，把此檔上傳到「素材檔」；每個專案只放這一張）

<!-- @104-directive
{"target_block": "project", "index": 2, "action": "replace_all", "mode": "quill_html", "name": "1111 新版求才系統重整", "media_type": "上傳圖片或影片", "image": "images/project3_1111_recruit.png", "image_action": "upload_replace"}
-->

```html
<blockquote><strong>主導無文件舊系統全面翻新，維持服務、分階段上線。</strong>服務約 6 萬家付費企業的招募系統，前期已有全面翻新規劃，卻遲遲未能落地。我在 2024/12 接手主導重整，先透過實際操作與內部訪談，還原沒有文件的權限及商業規則。既有業務後台與底層資料庫必須沿用，我決定不推倒重來，維持線上服務，分階段換上新版功能。</blockquote>
<p>將還原出的規則寫成新版流程與規格，上線前進行封測，確認後再於離峰時段切換。第一階段於 2025/10 上線，涵蓋登入、首頁、帳號、聯絡人、功能選單、公告與通知；公司資料則在 2026/01 接續上線。企業針對帳號與公司資料累積提出 840 件建議，每一件都是使用上的痛點；這次已完成 <span style="background-color: #fbf3db;">743 件（88%）</span>。</p>
<p>企業多年反映招募溝通不便，2021 年起累積 199 件合併建議。下一階段便規劃把兩套功能重複工具的傳訊息流程整合，讓企業更方便邀約求職者面試；目前與工程及相關單位協作，仍在開發中。</p>
```

### 5.4 1111 企業群組共同招募

- 起訖：2025/03 – 2025/09｜isInProgress：否（104 只收年月）｜url：留空
- 圖片：`images/project4_1111_recruit.png`（104「專案素材」選「上傳圖片或影片」，把此檔上傳到「素材檔」；每個專案只放這一張）

<!-- @104-directive
{"target_block": "project", "index": 3, "action": "replace_all", "mode": "quill_html", "name": "1111 企業群組共同招募", "media_type": "上傳圖片或影片", "image": "images/project4_1111_recruit.png", "image_action": "upload_replace"}
-->

```html
<blockquote><strong>規劃企業群組權限，讓大型企業跨部門／分店共同招募。</strong>連鎖與大型企業希望分店同仁能共用職缺與履歷，但原系統只提供全公司或個人兩種資料範圍，無法按分店共用。我規劃<strong><span style="background-color: #deebf1;">群組功能</span></strong>，補上部門／分店這一層資料範圍，重新定義帳號、職缺與履歷的權限關聯及舊資料轉換規則，讓既有帳號、職缺能直接加入群組。與工程團隊協作，於 2025/09 完成上線，回應自 2020/12 起累積的 55 件廠商建議。</blockquote>

```

---

## 6. 求職條件（工作內容，純文字；其餘求職條件欄位不動）

<!-- @104-directive
{"target_block": "jobCondition", "action": "replace_field", "field": "preferJobContent", "mode": "plain_text", "locked_fields": ["preferJobTitle", "salary", "workArea", "onboardDate", "remoteWork"]}
-->

```text
我希望以產品經理的角色，負責整個產品、產品線或主要模組，並依團隊規模承擔帶人責任。
從需求取捨與產品方向判斷開始，把構想及需求轉成團隊能討論、執行的規則和流程，並承接規格、驗收、時程與跨部門交付。從規劃到上線持續投入，為產品與商業方向帶來正向影響。
```


