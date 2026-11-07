<!--markdownlint-disable MD013 MD033-->

# 給 Antigravity：104 履歷填寫指令（第一部分）

> 個資檔，不外流，不得貼到任何公開位置或 HackMD；不產生 PDF。
> 是 `career/104/styling-directive-guide.md` v2.3.0 的增補；衝突時以本檔「最高鐵律」為準。
> 內文唯一來源：本檔「第二部分：履歷內容」（圖片在 `career/104/images/`）。本檔把填寫指令與履歷內容合併為單一檔案。
> 去識別化（公司名等公開處理）由你在填表時依 `career/104/antigravity-public-redaction-skill.md` 處理；本檔不另產公開版。除該處理外，內文一律不改。

## 一、範圍（全中文，不放英文）

| # | 欄位 | 內容區塊 | 方式 | 上限 / 目前純文字字數 |
| :-- | :-- | :-- | :-- | :-- |
| 1 | 個人簡介 `info.bio` | `## 1.` 的 ```text | 純文字 | 1,000 / 414 |
| 2 | 個人特色 `trait`（5 個，分開輸入依序） | `### 1.1` 的 ```text，每行一個 | 純文字 | — |
| 3–6 | 工作經歷 `experiences[0..3].description` | `### 2.1`–`2.4` 的 ```html | Quill HTML | 2,000 / 1929、894、423、22 |
| 7–12 | 專長 `skills[0..5].desc` | `### 3.1`–`3.6` 的 ```text | 純文字 | 1,000 / 377、179、230、121、129、353 |
| 13 | 自傳 `bio.chi` | `## 4.` 的 ```html | Quill HTML | 4,000 / 1,096 |
| 14–17 | 專案成就 `projects[0..3].introduction` | `### 5.1`–`5.4` 的 ```html | Quill HTML | 2,000 / 299、322、229、135 |
| 18 | 求職條件「工作內容」`preferJobContent` | `## 6.` 的 ```text | 純文字 | 未知 / 123 |

專案另需（依各 directive）：名稱、起訖（5.1 2020/01–2020/06、5.2 2018/05–2022/03、5.3 2024/12–迄今、5.4 2025/03–2025/09，104 只收年月）、圖片（5.1→`career/104/images/project1_justdating_juicy.png`、5.2→`project2_kool.png`、5.3→`project3_1111_recruit.png`、5.4→`project4_1111_recruit.png`；素材選「上傳圖片或影片」、每專案一張）、網址留空。
專長名稱與標籤、經歷標籤：依第二部分各 directive 的 `name`／`tags`；標籤只用 `career/104/skill_categories.md`／`tool_categories.md` 內名稱，找不到就略過；與頁面現況不同處**停下回報，不自行改**。
公司名稱、職稱、起訖、管理責任（2.1：有管理責任 1~5 人，直屬 2 名）不動，只核對與第二部分一致。
`## 0.` 全站版型維持 104 現況，不套用、不修改（本人 2026-11-05 裁示）。

## 二、最高鐵律（違反即中止）

1. **Zero Text Mutation**：內文逐字取自第二部分對應區塊，不得改寫、翻譯、摘要、補字、改標點或換行（去識別化處理除外）。不在腳本硬編碼履歷文字。
2. **寫入後斷言**：每欄寫入後讀回 DOM 純文字，需等於 內容區塊純文字（Quill 欄位去標籤、合併空白後比較）。不相等就停止、不儲存，回報欄位與差異。
3. **字數先查再貼**：超過上限或頁面上限與上表不同就停，回報欄位、上限、目前字數，不截斷、不刪減。
4. **不按任何送出／公開／投遞**。每欄通過斷言後列出「欄位＝前 40 字…共 N 字」，等我說「OK 儲存」才按該欄儲存。
5. **覆蓋前備份**：把目前純文字貼進回報，供還原。
6. **不確定就停**：找不到欄位、貼入後樣式或縮排跑掉、跳驗證碼，停下描述畫面。
7. **範圍外欄位不碰**，看到不一致也不要順手修。
8. **子項縮排**：帶 `style="margin-left: 1em;"` 的 `<li>` 貼入後仍須是縮排子項；純文字欄位（如專長 3.1）的空行與分段原樣保留；金黃（成果數字）、晴藍＋粗體（核心名詞）已寫在 HTML，原樣貼入，不自己加粗或改色。

## 三、準備

1. 我提供已登入的 104 履歷編輯頁網址；沒有網址不要自己搜尋。
2. 只處理第二部分內這些 directive：`info`／`bio`、`info`／`trait`、`experience` 0–3、`skill` 0–5、`bio`／`chi`、`project` 0–3、`jobCondition`／`preferJobContent`；其餘整段略過。
3. 檢查頁面：四筆經歷順序與第二部分 2.1–2.4 一致、公司名稱與第二部分標題一致（或為「公司名暫不公開」）。不一致就停。

## 四、每一步

備份 → 貼入 → 純文字斷言 → 列出摘要 → 等「OK 儲存」→ 儲存 → 重新讀回確認。建議順序：簡介 → 個人特色 → 經歷 0–3 → 專長 0–5 → 自傳 → 專案 0–3（含圖片）→ 求職條件。

## 五、已知事實邊界（不要在頁面上補寫）

內文的人稱已定稿：自傳用第一人稱「我」，簡介、經歷、專長、專案、求職條件用省略主詞寫法（不寫「我」也不寫「本人」）。逐字貼入，不改人稱。

逾 2 萬筆修正值尚未寫回正式資料庫，履歷不寫「已套用／已上線」；不新增第二部分以外的任何數字、期間或成果。

## 六、完成後回報

- 各欄位字數與儲存狀態。
- 跳過或停下的欄位與原因（含標籤與頁面不一致處）。
- 圖片上傳結果。
- 確認未按送出、公開、投遞。

---

# 104 履歷內容（第二部分）｜PM 版 v1.19｜可填表（現行版）





> PM 版 v1.19（2026-11-07）：承 v1.18（HR 配對複驗選用版），三處微調——①簡介第二段補回「也帶 2 名企劃將 AI 納入日常工作流程」（簡介約 414 字，仍在 1,000 上限內，一個短子句，不算過長）②3.1 測試句改為「主要操作流程與基本功能檢查（Happy Path、Smoke Test）」，3.3 API 句用白話解釋＋括號保留術語 ③5.1 粗體句改為「主導兩次 App 下架危機的審核溝通與海外收款串接，守住主力產品營收」。逾 2 萬筆修正值尚未寫回正式資料庫，正文不寫已套用；結案率依本人裁示用季度，不重算。

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
資深產品經理，累積近 10 年 B2C 跨國訂閱 App 與 B2B 企業平台經驗，代表實績涵蓋 App 從 0 到 1 的產品規劃、訂閱變現與企業端招募系統翻新。獨立規劃商家與網紅的合作媒合平台 KOOL，上線半年累積 8 萬多次合作報名。曾主導付款管道轉型，讓網頁付款營收占比從 24% 升至 80% 以上；也透過跨平台定價對照測試，為公司調整馬來西亞價格帶提供依據。

現任 1111 人力銀行企業端招募系統 Product Owner，帶領 2 名企劃、協調約 20 人跨部門團隊，主導服務約 6 萬家付費企業的系統翻新（已分階段上線）與 AI 功能上線。接下長年卡關的企業人才搜尋改版，以自建 AI Agent 工作流找出搜尋問題，並將企業儲存的近 19 萬筆舊搜尋條件轉為新版語法，讓舊設定能在新版搜尋中沿用，也帶 2 名企劃將 AI 納入日常工作流程。TOEIC 980，曾以全英文協作完成 7 個海外市場在地化。
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
<blockquote>擔任服務約 6 萬家付費企業的招募系統 <strong>Product Owner</strong>，正式職稱為產品企劃主任。帶領 2 名直屬企劃，協調工程、設計、QA 與維運約 20 人，主導約 70 項主要功能的需求分析與規格規劃。</blockquote>
<p><br></p>
<p><span class="ql-size-large" style="color: #00afb8;"><strong>一、產品翻新與 AI</strong></span></p>
<p><br></p>
<ul>
<li><strong>接手停滯的舊系統改版，還原無文件規則並主導分階段上線</strong>：已分階段上線帳號登入與企業資料等功能，整體翻新仍持續進行。接手時，系統的權限與商業規則沒有文件可查，改版卻必須沿用既有資料庫。先靠實測與內部訪談還原規則，再選擇維持線上服務、分階段換上新版功能的做法。封測後，分別於 2025/10、2026/01 在離峰時段切換上線。針對帳號與公司資料的使用痛點，企業累積提出 840 件建議；這次改版已完成 <span style="background-color: #fbf3db;">743 件（88%）</span>。</li>
<li><strong>主導 AI 招募功能上線，調整職務類別與人才推薦規則</strong>：刊登文字方面，主導<strong><span style="background-color: #deebf1;">職缺工作說明生成</span></strong>（2024/10）上線，並帶領企劃完成公司簡介生成（2026/06）；為這兩項文字生成功能訂定勞動法規合規驗收標準。職務類別推薦則串接資料科學團隊 API，為企業預設帶入刊登職缺時要選的分類。企業手動修改類別後，系統就不再覆蓋，保留企業自行調整的結果。人才名單方面，主導<strong><span style="background-color: #deebf1;">AI 推薦人才</span></strong>（2025/11）上線。針對名單「少又舊」的問題，追查原因並實測主要競品，再重訂人才名單的排序與重複曝光規則。</li>
<li><strong>規劃企業群組權限，支援大型企業跨部門／分店共同招募</strong>：原系統只能在全公司與個人兩種資料範圍之間選擇。為讓大型企業按部門或分店共同招募，規劃<strong><span style="background-color: #deebf1;">群組功能</span></strong>，訂出帳號、職缺與履歷的存取關係，以及舊資料轉換規則。功能在 2025/09 上線，回應自 2020/12 起累積的 55 件廠商建議。</li>
</ul>
<p><br></p>
<p><span class="ql-size-large" style="color: #00afb8;"><strong>二、搜尋與分類整頓、提案處理與帳號安全</strong></span></p>
<p><br></p>
<ul>
<li><strong>接下長年卡關的人才搜尋改版：找出 7 項問題、轉換近 19 萬筆舊搜尋條件</strong>：企業用來找人才的搜尋功能，長期因語法難用、規則混亂，導致廠商容易輸錯語法而搜不到人；改版又因缺人手與分析工具，遲遲無法啟動。接下改版後，分兩條線進行：</li>
<li style="margin-left: 1em;"><strong>找出搜尋規則的問題</strong>：先盤點規則與業務邏輯，和工程釐清企業在畫面上設定的搜尋條件，如何轉成搜尋引擎 <strong>Solr</strong> 使用的語法，再用 <strong>Antigravity</strong> 在測試環境逐組比對搜尋結果。同一組混用符號的條件，依規格應搜出 <span style="background-color: #fbf3db;">111 人</span>，修正前卻只搜到 <span style="background-color: #fbf3db;">44 人</span>。依這類比對整理出 7 項解析問題，交工程修正。</li>
<li style="margin-left: 1em;"><strong>轉換企業儲存的舊搜尋條件</strong>：新語法不支援括號，不能直接逐一替換符號，還得先判斷廠商原本想搜什麼。用自建 AI 工作流判讀錯誤輸入的意圖，產出修正值並轉成新語法，再由 <strong>Claude</strong> 全量比對修正值與原意。針對差異反覆修正後，親自把關並在測試環境驗證搜尋結果。共處理<span style="background-color: #fbf3db;">近 19 萬筆</span>，產出<span style="background-color: #fbf3db;">逾 2 萬筆</span>修正值。</li>
<li><strong>扛起職缺與履歷分類整頓，整併重複選項、補上新類別</strong>：企業刊登職缺、求職者填履歷時，都會勾選分類，供系統搜尋與配對使用。分類卻長年缺乏審核，有需求就新增，留下少人使用或重複的選項；AI、雲端相關職類被切得過度發散，電腦工具類別卻停留在舊世代，新世代工具反而沒得選。接手整頓後，先調出自家使用數據、參考競品，再召集各大主管共同決議整併範圍。依決議收斂少人使用或重複的類別（如 AI 與雲端相關職類）、補上新世代工具類別，並調整原有類別的歸屬。從類別對照、新增一路負責到交付工程，由工程團隊寫入類別表、清洗既有職缺與履歷，讓搜尋與配對回到乾淨可用的分類基準。</li>
<li style="margin-left: 1em;">維護職務、證照、技能、福利等分類時，收攏新增、編輯、合併與刪除需求，沿用前述搜尋改版的 AI 資料比對方法，檢視儲存這些分類的 15 張類別代碼表、整理異動所需的欄位對照。例如福利類別，就整理調整前後的對應關係與畫面上的顯示順序，交工程更新分類資料。</li>
<li><strong>重整企業提案處理，30 天結案率由 52% 升至 79%</strong>：接手 880 件積壓提案後，以客戶提出的案件為優先，重新排定順序、分派案件，帶領 2 名直屬企劃在 2025/11–12 兩個月清理 625 件。以提案滿 30 天的案件計算，30 天結案率從介入前（2024 Q4–2025 Q3）的 52%，升至介入後（2025 Q4–2026 Q3）的 79%。另外觀察兩群付費企業的留存：有提案獲處理的企業，年化留存率為 <span style="background-color: #fbf3db;">79.5%</span>；其餘付費企業為 74.8%，兩者相差 <span style="background-color: #fbf3db;">4.7 個百分點</span>。</li>
<li><strong>主導帳號冒用應變，補強登入防線</strong>：2026/03–04 十多家廠商招募帳號遭冒用登入，帶領工程與客服釐清影響範圍，再設計新裝置 <strong>OTP</strong> 驗證及自助解鎖流程，補強登入防線。功能上線後一週內，便依客服回饋調整。至 2026/10，客服未再接獲廠商回報同類冒用。</li>
</ul>
```

### 2.2 Product Manager｜尚凡國際創新科技｜2018/01–2022/03

▼ management：**無管理責任**

<!-- @104-directive
{"target_block": "experience", "index": 1, "action": "replace_description", "mode": "quill_html", "tags": ["市場調查企劃與執行", "產品策略", "產品營運", "數據分析", "專案時間╱進度控管", "Electronic Payment", "iOS", "Android"], "locked_fields": ["companyName", "jobName", "duration", "workArea", "management"]}
-->

```html
<blockquote>負責公司主力訂閱交友 App <strong><span style="background-color: #deebf1;">JustDating</span></strong>，以及訂閱內容 App <strong>Peach</strong>、網紅媒合平台 <strong>KOOL</strong>。JustDating 依公司公開資料，曾長期位居台灣約會類暢銷榜第一；工作中也曾以英文與歐洲金流商視訊洽談合作。</blockquote>
<p><br></p>
<p><span class="ql-size-large" style="color: #00afb8;"><strong>一、付款、定價與下架後延續服務</strong></span></p>
<p><br></p>
<ul>
<li><strong>主導付款轉型，網頁付款營收占比最高達 91%</strong>：考量 App 商店抽成高於網頁金流費率，為 <strong><span style="background-color: #deebf1;">Peach</span></strong> 規劃新的付款流程，將用戶從 App 內購導向網頁付款，並完成<strong>智冠</strong>金流串接。轉型後，網頁付款營收占比從 2020/11 的 24% 升至 2021/09 的 80% 以上，2022/02 最高達 <span style="background-color: #fbf3db;">91%</span>。</li>
<li><strong>主導 JustDating 跨平台定價對照測試，改變馬來西亞價格帶</strong>：在 2021/05–08 主導 iOS 定價測試，依序測試原價、降價與恢復原價，並以維持原價的 <strong>Android</strong> 作為對照。結果顯示，降價期的 iOS 非續訂（單次購買）營收比原價期<span style="background-color: #fbf3db;">增加 5%</span>，同期 Android 卻<span style="background-color: #fbf3db;">減少 18%</span>。當 iOS 恢復原價，非續訂（單次購買）營收反而比原價期下滑 65%。公司根據測試結果調整馬來西亞價格帶，從原先與新加坡同級的高價區，改為與印尼、越南、泰國相同的低價帶。</li>
<li><strong>主導兩次下架承接，守住主力營收產品</strong>：JustDating 因政策遭 <strong>App Store</strong> 下架，便推出沿用同一後端的 <strong><span style="background-color: #deebf1;">Juicy</span></strong> 接續服務；其後 Juicy 也遭下架，再推動 JustDating 重新上架。上線與導流期間快速拉升用戶規模：Juicy 男性每日活躍用戶（DAU）在 6 週內從約 3,200 增至 <span style="background-color: #fbf3db;">1.25 萬</span>（近 4 倍）；JustDating 在 12 週內從約 1,500 增至 <span style="background-color: #fbf3db;">1.2 萬</span>（8 倍）。</li>
</ul>
<p><br></p>
<p><span class="ql-size-large" style="color: #00afb8;"><strong>二、網紅媒合平台 0 到 1</strong></span></p>
<p><br></p>
<ul>
<li><strong>從 0 到 1 獨立規劃 <span style="background-color: #deebf1;">KOOL</span>，半年 <span style="background-color: #fbf3db;">8 萬多次</span>合作報名</strong>：沒有直接競品可參考，便從商家行銷單位的訪談釐清需求，定義平台定位，再規劃商家邀約、網紅報名的雙邊流程，以及 VIP 訂閱、點數付費牆、精選曝光等付費機制。統籌設計與工程完成上線後，平台累積約 <span style="background-color: #fbf3db;">1.6 萬份</span>網紅檔案。</li>
</ul>
```

### 2.3 Associate PM｜思維特網路資訊｜2016/06–2018/01

▼ management：**無管理責任**

<!-- @104-directive
{"target_block": "experience", "index": 2, "action": "replace_description", "mode": "quill_html", "tags": ["專案溝通╱整合管理", "數據分析", "Electronic Payment", "Android"], "locked_fields": ["companyName", "jobName", "duration", "workArea", "management"]}
-->

```html
<blockquote>為交友 App <strong><span style="background-color: #deebf1;">SweetRing</span></strong> 負責產品維運、支付與在地化規劃。App 在地化涵蓋美國、墨西哥、巴西、印尼、馬來西亞、日本與韓國等 7 個市場；支付導入另見下列印尼、泰國案例。</blockquote>
<p><br></p>
<p><span class="ql-size-large" style="color: #00afb8;"><strong>一、在地支付與市場在地化</strong></span></p>
<p><br></p>
<ul>
<li><strong>開通 8 種在地付款管道，規劃訂閱方案</strong>：為印尼、泰國導入第三方支付 <strong><span style="background-color: #deebf1;">CodaPay</span></strong>，讓用戶可透過電信帳單、ATM、電子錢包、便利商店、銀行轉帳等 <span style="background-color: #fbf3db;">8 種</span>在地管道付款。訂閱方案則從實收出發：比較各管道手續費率與撥款結算週期，試算淨實收，提出 7／30／90 天方案，再完成 SweetRing Android 加值頁與付款流程的規劃、上線。</li>
<li><strong>以英文協作，完成 7 個海外市場在地化</strong>：與最多約 10 位外籍實習生以全英文會議協作，翻譯 App 介面文字與行銷素材，把產品轉為適合各市場的在地版本。另負責 SweetRing 多國 Facebook 粉絲專頁的內容營運，最多時涵蓋 12 國：貼文內容由中文翻成英文，並監督翻譯品質。</li>
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
用 AI Agent 做產品規劃、規格與測試時，先釐清問題、盤點商業邏輯與業務規則，整理及清洗資料，再定義修改需求與驗證要求。接著用 Claude Code、Antigravity 讓 Agent 依規則產出畫面與流程（Wireframe、流程圖、Prototype），以及提案與需求文件（Proposal、PRD、規格），並用 Claude 驗證結果。同一套工作流也延伸用於數據整理，製作一頁式摘要（one-pager）與數據看板（dashboard）。

測試案例由 AI 依規格產出後交給 QA，也請 Agent 按案例測試；主要操作流程與基本功能檢查（Happy Path、Smoke Test），則親自手動執行。

把這套做法整理為 skill 與工作方法，帶 2 名直屬企劃用在資料整理、規格、Wireframe 與原型，已納入團隊工作流程。
```

### 3.2 產品規劃與交付

<!-- @104-directive
{"target_block": "skill", "index": 1, "action": "replace_all", "mode": "plain_text", "name": "產品規劃與交付", "tags": ["製作規格說明書", "Prototype", "功能測試(function test)", "專案規劃執行╱範圍管理"]}
-->

```text
規劃雙邊媒合平台時，先訪談商家行銷單位，了解商家的需求。再從產品使用的角度，想清楚商家與網紅各自要完成的事，從 0 到 1 定義互動流程與付費機制。把這些需求整理成 User Journey、User Story 與 Use Case，再寫成 PRD，和 QA 依規格推導驗收案例，安排分階段上線。對客服、業務等內部單位，則用互動原型與 FAQ 說明新功能。
```

### 3.3 系統分析

<!-- @104-directive
{"target_block": "skill", "index": 2, "action": "replace_all", "mode": "plain_text", "name": "系統分析", "tags": ["Systems Analysis", "UML", "系統整合分析"]}
-->

```text
接手沒有文件的既有系統，先靠實際操作與內部訪談摸清業務規則，再將商業邏輯拆成查詢條件，和工程逐項確認後端如何處理。用循序圖、活動圖、使用案例圖、BPMN 及泳道圖，向團隊說明操作流程與系統如何互動。規劃系統與外部合作夥伴串接 API 時，為確保資料傳輸安全與穩定，先和工程議定如何確認對方身分、避免舊請求被重複送出（簽章驗證、防重放），以及出錯時回覆的訊息與代碼（錯誤碼）、每段時間可傳送的次數（頻率限制）和雙方資料格式的轉換規則，一併寫進 API 串接規格。
```

### 3.4 UI/UX 規劃

<!-- @104-directive
{"target_block": "skill", "index": 3, "action": "replace_all", "mode": "plain_text", "name": "UI/UX 規劃", "tags": ["Figma", "Axure RP", "Wireframe", "Prototype", "使用者介面設計", "使用者體驗設計", "iOS", "Android"]}
-->

```text
規劃 iOS、Android App 與 Web，先用 Miro、FigJam 畫出 Flowchart，釐清使用流程，再以 Figma 繪製跨裝置介面的 Wireframe，並用 Axure RP 製作互動原型。視覺畫面則與設計師協作完成。
```

### 3.5 跨部門協作與時程

<!-- @104-directive
{"target_block": "skill", "index": 4, "action": "replace_all", "mode": "plain_text", "name": "跨部門協作與時程", "tags": ["專案溝通╱整合管理", "專案時間╱進度控管", "決策能力"]}
-->

```text
整合行銷、CRM、設計與技術等單位的需求時，從使用者旅程、開發複雜度與業務單位共識判斷取捨，排定優先序。帶領 2 名直屬企劃完成交付，並協調工程、設計、QA 與維運約 20 人的工作；用甘特圖及 Trello 掌握時程，熟悉 Kanban 與瀑布式開發流程。
```

### 3.6 App 產品與變現

<!-- @104-directive
{"target_block": "skill", "index": 5, "action": "replace_all", "mode": "plain_text", "name": "App 產品與變現", "tags": ["產品策略", "產品營運", "數據分析", "Electronic Payment", "iOS", "Android"]}
-->

```text
規劃變現時，先把訂閱定價與付款成本放在一起算：比較 App 內購（IAP）及網頁付款的抽成、稅、手續費與撥款週期，試算淨實收後再提出訂閱方案。曾串接本地與海外第三方金流，主導訂閱內容 App Peach 的付款管道轉型，也曾以英文與歐洲金流商視訊洽談合作。定價方面，設計以 Android 為對照組的跨平台定價對照測試。分析交友 App JustDating、Juicy 時，追蹤註冊到首次付費的時間、付費留存率及用戶終身價值（LTV）。分析發現，用戶多在註冊後 7 至 14 天內決定是否購買：這段期間內購買者較可能續訂，未在期間內購買則多半流失；流失後再列為再行銷對象。付費機制的設計也涵蓋 VIP 訂閱、點數付費牆及精選曝光，並熟悉 App Store／Google Play 的審核政策與上架溝通。
```

---

## 4. 自傳

<!-- @104-directive
{"target_block": "bio", "action": "replace_field", "field": "chi", "mode": "quill_html"}
-->

```html
<p>遇到還沒成形的產品想法，我會先弄清楚各個角色想完成什麼、受到哪些限制，再思考彼此該如何互動，逐步形成能運作的產品。向團隊說明方案時，我會把流程和背後的考量一起說清楚，讓大家知道為什麼這樣設計。做過交友與訂閱制 App、網紅媒合平台，也做企業招募系統，我始終在意兩件事：使用者能不能完成想做的事，以及產品能不能支持公司持續經營。</p>
<p><br></p>
<p>規劃 <strong>KOOL</strong> 時沒有直接競品可參考，我便先訪談商家行銷單位，了解他們怎麼找網紅。這段經驗讓我確定，自己喜歡從真實需求出發，先想透商家與網紅各自要完成的事，再把需求轉成產品方案。</p>
<p><br></p>
<p>在尚凡，我負責的 <strong>JustDating</strong> 是公司的主力交友 App，具有高 DAU 與營收規模。主力 App 兩度遭遇下架，當時的壓力是既要延續服務，也要承接營收。我串起各團隊的工作，協調產品交付與行銷承接，讓各方朝共同目標推進，也在過程中熟悉如何與 App Store 溝通、處理上架問題。</p>
<p><br></p>
<p>我加入 <strong>1111</strong>，想參與的是整套招募系統的革新。2024 年底專案重啟後，我接手並主導企業端招募系統全面翻新。面對沒有文件、又必須沿用舊後台與資料庫的限制，我從實際操作歸納規則，再請工程、維運與稽核交叉核對，把散在舊系統與各單位經驗裡的資訊整理成新版流程與規格。我選擇在服務持續運作的情況下改版，與工程團隊一邊調整現行功能，一邊分階段替換。</p>
<p><br></p>
<p>從網紅媒合走到企業招募，我看到兩種產品的共同點：先讓雙方找到彼此，再把雙方各自的操作接起來；企業招募還要進一步想清楚職缺、履歷和搜尋配對之間如何連動。<strong>群組功能</strong>就是這樣想出來的：大型客戶需要按部門或分店共同招募，我從帳號、職缺與履歷的關係切入，規劃出對應的共同招募方式。我喜歡先把關係和例外想透，再向團隊說清楚，讓使用者少花時間停下來摸索。</p>
<p><br></p>
<p>帶團隊使用 <strong>AI Agent</strong>，我不只看工具產出了什麼，也重視同仁是否懂得運用方法、判斷結果。同仁處理大量資料卡住時，我會先了解問題出在哪裡，再提供自己整理的 skill 與作業方法，讓他能用這套方法繼續處理。產出結果仍由同仁自己判斷，少數例外再一起討論，直到完成工作交付。對我來說，AI 換了產出工作的方式，但釐清問題、想出解法、判斷結果，仍然要由人掌握。</p>
<p><br></p>
<p>訂閱變現、新產品規劃與複雜系統翻新，是我能帶進下一個團隊的實務經驗。我能釐清問題與規則，形成產品方案，和工程深入協作，再串起各部門完成交付；也能把 AI 方法帶進團隊的日常工作。在現職，系統如何翻新、需求如何排序，都是我實際做過的判斷；接下來，我希望負責產品線或主要模組，讓產品決策持續回應使用者需求並帶來商業結果。</p>
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
<blockquote><strong>主導兩次 App 下架危機的審核溝通與海外收款串接，守住主力產品營收。</strong>與 <strong>App Store</strong> 溝通，處理兩款產品的上架問題。海外收款方面，負責兩款產品在台灣以外市場的網頁加值頁規劃、商品定價與商務合作洽談，也擔任與收款服務商 <strong>CodaPay</strong> 之間的工程串接溝通窗口。</blockquote>
<p><strong><span style="background-color: #deebf1;">JustDating</span></strong> 遭下架後推出 <strong><span style="background-color: #deebf1;">Juicy</span></strong>，沿用同一套後端導流：男性 DAU 在 6 週內由約 3,200 增至 <span style="background-color: #fbf3db;">1.25 萬</span>（近 4 倍，2020/01–02）。<strong>Juicy</strong> 下架後重推 <strong>JustDating</strong>，男性 DAU 在 12 週內從約 1,500 回升至 <span style="background-color: #fbf3db;">1.2 萬</span>（8 倍，2020/04–06），守住主力營收產品。</p>
```

### 5.2 KOOL 網紅媒合平台 0 到 1 規劃

- 起訖：2018/05 – 2022/03｜isInProgress：否｜url：留空
- 圖片：`images/project2_kool.png`（104「專案素材」選「上傳圖片或影片」，把此檔上傳到「素材檔」；每個專案只放這一張）

<!-- @104-directive
{"target_block": "project", "index": 1, "action": "replace_all", "mode": "quill_html", "name": "KOOL 網紅媒合平台 0 到 1 規劃", "media_type": "上傳圖片或影片", "image": "images/project2_kool.png", "image_action": "upload_replace"}
-->

```html
<blockquote><strong>以「網紅人力銀行」為構想從 0 到 1 規劃，半年 8 萬多次合作報名。</strong>沒有直接競品可參考，先訪談商家行銷單位，了解他們如何在 <strong>Instagram</strong> 尋找網紅，再借鏡 <strong>Airbnb</strong> 房東刊登房源的模式，將 <strong><span style="background-color: #deebf1;">KOOL</span></strong> 設計成雙邊媒合平台：商家刊登合作邀約，網紅可報名，也能接受商家邀請。</blockquote>
<p>從刊登、邀請、報名到聯繫，逐一安排商家與網紅的操作與付費規則，再用 <strong>Miro</strong> 畫出流程圖，搭配規劃簡報向團隊說明；2018/05 啟動後，統籌產品、設計與程式部門完成上線。平台累積約 <span style="background-color: #fbf3db;">1.6 萬份</span>網紅檔案。</p>
<p>付費機制包括 VIP 訂閱、點數付費牆與精選曝光，其他功能則有評價、工作地點地圖、手機認證與網紅作品集；產品涵蓋 iOS、Android 與網頁版本。</p>
```

### 5.3 1111 新版求才系統重整

- 起訖：2024/12 – ｜isInProgress：**是**｜url：留空
- 圖片：`images/project3_1111_recruit.png`（104「專案素材」選「上傳圖片或影片」，把此檔上傳到「素材檔」；每個專案只放這一張）

<!-- @104-directive
{"target_block": "project", "index": 2, "action": "replace_all", "mode": "quill_html", "name": "1111 新版求才系統重整", "media_type": "上傳圖片或影片", "image": "images/project3_1111_recruit.png", "image_action": "upload_replace"}
-->

```html
<blockquote><strong>分階段上線新版求才系統，並規劃下一階段的訊息整合。</strong>2025/10 第一階段上線登入、首頁、帳號、聯絡人、功能選單、公告與通知，2026/01 接續上線公司資料；針對帳號與公司資料的使用痛點，企業累積提出 840 件建議，已完成 <span style="background-color: #fbf3db;">743 件（88%）</span>。</blockquote>
<p>企業多年反映招募溝通不便，自 2021 年起累積提出 199 件要求合併訊息工具的建議。下一階段規劃整合兩套功能重複的工具，統一傳訊息流程，讓企業更方便邀約求職者面試；目前與工程及相關單位協作，仍在開發中。</p>
```

### 5.4 1111 企業群組共同招募

- 起訖：2025/03 – 2025/09｜isInProgress：否（104 只收年月）｜url：留空
- 圖片：`images/project4_1111_recruit.png`（104「專案素材」選「上傳圖片或影片」，把此檔上傳到「素材檔」；每個專案只放這一張）

<!-- @104-directive
{"target_block": "project", "index": 3, "action": "replace_all", "mode": "quill_html", "name": "1111 企業群組共同招募", "media_type": "上傳圖片或影片", "image": "images/project4_1111_recruit.png", "image_action": "upload_replace"}
-->

```html
<blockquote><strong>在「全公司／個人」之間新增部門與分店資料範圍，讓連鎖與大型企業共用職缺與履歷。</strong>規劃<strong><span style="background-color: #deebf1;">群組功能</span></strong>，重新定義帳號、職缺與履歷的權限關聯及舊資料轉換規則，讓既有帳號與職缺可直接加入群組；與工程團隊協作，於 2025/09 上線，回應自 2020/12 起累積的 55 件廠商建議。</blockquote>

```

---

## 6. 求職條件（工作內容，純文字；其餘求職條件欄位不動）

<!-- @104-directive
{"target_block": "jobCondition", "action": "replace_field", "field": "preferJobContent", "mode": "plain_text", "locked_fields": ["preferJobTitle", "salary", "workArea", "onboardDate", "remoteWork"]}
-->

```text
希望以產品經理的角色，負責整個產品、產品線或主要模組；帶人範圍則依團隊規模安排。
從需求取捨與產品方向判斷開始，把構想及需求轉成團隊能討論、執行的規則和流程，並承接規格、驗收、時程與跨部門交付。從規劃到上線持續投入，為產品與商業方向帶來正向影響。
```





