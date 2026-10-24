# 給 Claude Code：履歷評分機制修訂規格 v4.1

日期：2026/10/13  
更新：整合 50 筆去重來源，其中 30 筆沿用已完成的寫作研究，20 筆為本次新增查閱的招聘端／評估資料。新增第 12–15 節；執行時連同原規則採用。
用途：依本文件修改現有履歷審查 skills、提示與腳本。這是待實作規格，不代表改版已完成或經過真人驗證。  
依據：使用者提供的 `validation-methods-complete.md`、本次方法審查及已確認的履歷事實。未檢閱 repo 腳本本體，請先核對實作是否與文件一致。

## 0. 任務與完成條件

請先改進評分器，再用新規準檢查履歷。不要以讓 v9.4 勝過 v8.1 為目標，不預設任何版本必須獲勝，也不要為了得分改寫事實。

完成以下工作：

1. 檢查現有規則與程式，列出實際受影響檔案。
2. 分開「事實核對、內容判斷、可讀性、PDF 解析、搜尋實驗、真人效度」。
3. 修改不合理的扣分與通過規則，加入可重現的迴歸案例。
4. 以同一份最新事實快照整理版本比較的輸入，保留原版，不覆寫歷史。
5. 執行能力範圍內的測試，交付結果、失敗項與未測項。缺真人資料不阻擋程式修訂，但必須標示尚未真人校準。
6. 不把 persona 數、重複輪次或模型一致性，宣稱為真人支持。

目標是改善判斷品質，不是增加流程數量。先完成核心修正與必要迴歸，不自動啟動昂貴的 50 份合成履歷計畫。

## 1. 必須採用的評估原則

- 「未提供證據」「證據顯示不符合」「與事實矛盾」是三種不同狀態。
- 有數字不等於有影響，有影響不必然需要數字。
- 使用者的語氣偏好是編輯規則，不是所有招聘者的通用淘汰條件。
- 結果、決策品質、交付能力分開評估；進行中專案可提供決策證據，但不得獲得尚未實現的結果評價。
- 學歷名氣、公司名氣、管理人數、術語密度不自動加分。
- a 資深交付、b PO／跨部門協調、c 方向與資源決策是能力分布，不是必須逐級晉升的單一路線。
- 同一缺口只在主要維度計入一次；其他維度可交叉引用，不能重複扣分。
- 每個負面判斷必須交代它如何影響「是否值得面試」或「要追問什麼」。
- 允許平手、不確定與不適用。禁止強迫每一組版本分出高下。
- 履歷裡的事實一致不代表外部查證成功，使用者口述也不能冒充監測紀錄。

## 2. 先確認評估的是哪一種工作

不要用 15 筆職缺高頻詞與 20 種公司情境混成一個總分。

每次評估使用一份完整目標 JD，保留擷取日期與版本；若只有摘要，明示摘要限制，不推測缺漏條件。多職缺分開出報告，不默認平均。

使用者有兩個值得分開看的方向：

| 路線 | 主要能力 |
| --- | --- |
| 企業平台／Product Owner | 需求釐清、優先級、系統整合、跨部門協調、交付品質與風險 |
| 偏產品策略的資深 PM | 問題選擇、使用者洞察、商業取捨、方向與資源配置、成果衡量 |

目前使用者希望投入更有影響力的產品、將更多心力放回產品策略。不要把「想接觸更艱深系統」當作其求職動機。

建立 requirement matrix，每項保留：

- JD 原句與 requirement_id。
- 類型：明文必要／加分／工作情境。
- 文字證據與所在位置。
- 狀態：supported／partial／unknown／contradicted／not_applicable。
- 是否足以阻擋面試，以及理由。

只有明確必要條件且有證據顯示不符合時，才可列硬性不符合。必要條件沒有寫在履歷上時，列 unknown；可影響篩選信心，但不能直接認定本人不會。

沒有完整 JD 時，可做一般履歷品質診斷；不可產出特定職缺匹配率、招聘成功率，或宣稱完全符合職缺。

## 3. 拆開現有五類檢查

### 3.1 事實核對：先於比較，但與盲審分開

事實核對者可以讀事實庫；內容審查者不可以。

將每項聲明對應 claim_id，記錄來源類型、期間、單位、母體、責任與狀態。缺資料填 null，不補推測。

| 狀態 | 含義 | 後續 |
| --- | --- | --- |
| supported | 與提供資料一致 | 可進入審查；不等於外部驗證 |
| incomplete | 口徑或來源資訊不完整 | 保留限制，產生追問 |
| unsupported | 目前找不到支持資料 | 不讓它取得已確認成果的優勢，先釐清或移除 |
| contradicted | 與有效事實直接衝突 | 阻擋該聲明進入可信比較，修正後再評 |
| superseded | 已被新資訊取代 | 保留歷史，正文採最新有效口徑 |

比較寫作版本時，要用相同事實快照清理既有聲明，不需強迫兩版包含完全相同的內容；內容取捨本身仍可比較。另存 corrected copy 與修正紀錄。

本案必查：

- v8.1 若仍把職缺匯入列為已上線，必須修正。已上線 AI 功能為公司簡介生成、職缺工作說明生成、推薦人才三項。
- 簽章驗證上線日期已補為 2026/04/17；截至 2026/10 未再出現同類冒用是使用者口述。不能推算至 10 月底，不能補監測來源或宣稱完全杜絕。
- 約 50 項大項功能與 111 項 Roadmap 細項不是同一單位；本人主責規劃並與工程密切協作，每日上版調整。「大項」正式定義仍待補。
- Juicy 的 DAU 是產品上線及行銷導入原 iOS App 下架用戶期間的整體表現。不能歸為個人設計的單一效果，不能推論本人掌控行銷預算。
- 定價實驗只含非續訂營收。約 28% 為 1.05／0.82−1，與 23 個百分點差不同；還原後 −65% 比較的是基準期。
- 全站廠商數是規模；留存差異是觀察，不是因果。
- 信件與即時通整合仍在開發中。可支持優先級判斷，不可作已上線成果。
- 準時率已因定義不明刪除，不得從舊版本補回。

### 3.2 機械檢查：只報檢查結果

保留日期、聯絡資訊、章節、亂碼、讀序與文字遺漏檢查，但作以下修正：

| 舊規則 | 新規則 |
| --- | --- |
| 關鍵字 70–90% 最高分，≥95% 扣分 | 刪除固定甜蜜區間；逐項做能力證據對應，同義詞也可支持。無關重複另列可讀性問題 |
| 經歷與技能重複出現才加分 | 不因重複本身加分；經歷提供證據、技能提供索引即可 |
| 含數字條列 ≥60% 得滿分 | 數字比例只作描述，不轉換成影響力分數 |
| 負責／協助／參與等命中就扣 | 移至語境檢查；誠實協作描述不扣。沒有說明具體貢獻才標缺口 |
| 日期超過 24 字寬就扣內容分 | 只作版面提醒；是否可讀以實際排版另驗 |
| 禁用詞命中即影響 Level | 使用者偏好另列 style_lint；事實禁寫另列 factual_guard，不混入能力判斷 |
| 自傳、照片、英文版一律必要 | 依投遞平台與明確 JD 要求，否則為 N/A 或編輯選項 |
| 雙欄 PDF 一律不適用 ATS | 以實際文字還原、讀序與匯入結果判定，不能由欄數直接推出通用結論 |

95% 去空白相似度可保留作內部回歸門檻，不稱業界標準。高相似度仍可能漏掉關鍵數字；須另檢查職稱、日期、Email、重要數字及重複日期出現次數與所屬經歷。區分實質遺漏與換行、標點差異。

BM25 工具改名為「指定語料與查詢下的搜尋實驗」。報告語料、查詢、切詞及參數，不能把 Top-10 解釋為 104 或任何商用 ATS 的真實排名。沒有實際匯入，一律寫 ATS import: not tested。

### 3.3 可見性壓力測試：與全文審查隔離

將「6 秒 F 型初篩」改稱「截斷文字可見性壓力測試」。

- 每行 10 字、抬頭 24 字、1,400 字截斷皆為內部代理規則，不稱為真實視線或第一屏。
- 第一個模型請求只能拿到遮罩後內容與職缺，不能拿到完整履歷、其他版本或詳細審查結果。
- 先保存第一關輸出，第二次獨立請求才提供全文。
- 回答 unknown 不等於履歷不合格。逐項回報職稱、公司、年資及職缺相關證據是否可見，不因一個欄位答錯就淘汰全文。
- PDF 畫面可讀性另測；缺 PDF 時，標示僅驗 Markdown 原始行，不能推論排版後的視覺行。
- 真正限時初篩需由真人看實際版面並記錄結果，不可由模型遮罩測試冒稱。

### 3.4 內容審查：每份獨立，再比較

先以相同規準、相同 JD，逐份在新 context 評估，不提供其他版本或預設排名。所有受測版本接受相同審查深度；取消「只審篇幅最長三份」。

保留兩個角色視角即可：

1. HR：基本條件、職涯脈絡、資訊清楚程度、可信度與是否值得安排面試。
2. 用人主管：目標工作需要的能力、決策與取捨、結果及責任邊界、面試需要釐清的風險。

原 20 persona 可留作選用的特定情境，不平均為 20 人投票。刪除未與職缺連結的普遍淘汰規則，例如每份任職必須滿兩年、只有大公司經驗即扣分、沒有英文版必定淘汰。

有完整履歷與未知背景時，不推測離職原因、性格、能力不足或不誠實。

### 3.5 編輯建議：與能力判斷分開

- 可建議把重要證據移到更容易找到的位置，但不能僅因放在自傳就把決策能力砍半。
- XYZ 是提醒工具，不是每條履歷都必須滿足的公式。
- 只有交付物、只有決策、已有結果的條列分別分類，不用同一套成果門檻處罰。
- 若要求補資料會把履歷寫成面試逐字稿，保留最影響判斷的口徑，其餘列面試追問。
- 本案保留新蛋與兵役是使用者決定，標示版面成本即可，不能每輪反覆扣同一個偏好。
- 自然語氣檢查只談冗詞、抽象程度、句型與場景。無可靠來源紀錄時，AI provenance: indeterminate from text alone；已知 AI 協作歷史可如實標記，不計作者機率，不影響能力分數。

## 4. 新的內容判讀尺度

先找證據，再給判斷。每一維度使用以下共同錨點；未知與不適用都不記為零分，不做加權總分：

| 標記 | 定義 |
| --- | --- |
| 強 | 有直接相關的具體案例，關鍵動作與責任清楚；足以支持本職缺所需能力 |
| 足夠 | 有相關證據，足以支持進一步面試，但仍有可釐清之處 |
| 待補 | 有線索，但不足支持該能力；說明缺口及對面試決策的影響 |
| 未呈現 | 文件沒有提供相關資訊；不推論本人沒有能力 |
| 不適用 | 不是本職缺或本文件需要判斷的項目 |

維度固定為：

1. 定位與職涯脈絡。
2. 目標職缺能力證據。
3. 決策、取捨與使用者理解。
4. 結果與衡量品質。
5. 個人角色、協作及責任邊界。
6. 可讀性與資訊取捨。

六維度必須套用第 12 節的 HR01–HR12 閱讀問題；這些是證據檢查，不是額外十二項加總分數。

對結果再分類為 context（規模背景）、output（交付物）、outcome（使用者／業務結果）、decision（決策）、in_progress（進行中）。多標記可以並存。每個數字按性質判讀，不因出現數字就算 outcome。

例如「50 項功能上線」主要是 output；「因重複信箱而選擇首次登入確認」是 decision；「付款占營收 24% 至 80%」是渠道組成變化，不能直接等同總營收或毛利提升。

Level 可保留作次要概括：

- 6：有相關案例與可信範圍，仍缺重要角色或判斷依據。
- 7：多個案例足以支持面試，行動、結果或交付、責任可辨。
- 8：另呈現清楚取捨、可比較衡量、限制與一致的專業模式。
- 9–10：需高度對應具體目標工作、關鍵量測與責任可追溯，不能只靠數字密度。
- 不符合上述者描述不足，沿用既有低分段完整定義或標待建立，不硬套 6–10。
- 不確定性預設 ±1 級，只是粗略判讀範圍，不是統計信賴區間或同業百分位。
- 未經真人校準，不得寫「已證明優於同級」「真人會更喜歡」。

主要結論使用「建議面試／需先釐清關鍵條件／本職缺不匹配／資訊不足」，後接證據。禁止由總分門檻自動推出邀約決策。

## 5. 可直接採用的審查提示

### A. 獨立內容審查

```text
你要根據一份職缺與一份履歷，判斷履歷是否提供足夠證據支持面試。
你不是在替文字競賽評分，也不能查驗候選人所有經歷的真偽。

只使用本次提供的 JD、履歷和固定規準，不使用版本名稱、過往排名或改稿目的。
把「未寫」「部分支持」「明確不符合」「事實矛盾」分開。
每個判斷引用原句，說明對該職缺的意義。
不要因數字、術語、公司名氣、管理人數或強勢動詞直接加分。
不要因協助／負責／參與等誠實描述直接扣分。
進行中案例可以支持決策能力，但不能算已實現成果。
不要推測空窗或轉職的負面原因。
同一缺口不要重複扣分。
允許資訊不足、未呈現與不適用。
依第 12 節 HR01–HR12 提問，先辨識人資需要解決的招聘問題，再引用履歷證據。
對每個問題標記 supported／partial／unknown／not_applicable，並說明招聘意義。
必要資料是否已在平台欄位、求職信或本次提供的附件呈現，須一併考慮；不要只盯 PDF。
來源中的個人偏好、學生規範、國外情境或產品功能，不得轉成普遍淘汰門檻。
輸出職缺對應、六維度、招聘決定、三個優勢、主要缺口及最多八題面試追問。
本次沒有實際測試的 PDF、ATS 或 AI 作者辨識不得宣稱已完成。

輸入：
{完整 JD 或明示限制的摘要}
{固定規準}
{一份履歷}
```

### B. 版本比較

```text
以下兩份履歷來自同一候選人，版本名稱已隱藏。
它們的既有聲明已按同一事實快照核對；不要假定任一版本較新或較好。
比較的是資訊選擇與表達如何影響本職缺的面試判斷。

先指出差異，再說明差異的招聘意義。
允許 A、B、無明確偏好、兩者均須先修正。
每個偏好必須引用不同的證據；事實相同的同義改寫不應改變能力評價。
不要以篇幅、數字個數、關鍵字個數或與範本一致程度直接決定輸贏。
若優勢只是排版、語氣或資訊可見性，明確標示，不升格成能力差異。
```

此比較階段不取代逐份獨立判讀；每次呈現順序應記錄，可交換 A/B 位置檢查順序敏感性。

## 6. 建議輸出資料結構

下列為欄位範例，不是已完成的 JSON Schema。實作時定義 enums、必填欄位及 null 規則，並驗證輸出。

```json
{
  "rubric_version": "4.1",
  "resume_id": "anonymous_01",
  "job_id": "job_01",
  "job_input": "full",
  "model_id": "actual_runtime_model",
  "run_id": "run_01",
  "human_calibrated": false,
  "requirements": [
    {
      "id": "R01",
      "status": "partial",
      "evidence": ["履歷原句"],
      "impact": "follow_up",
      "reason": "具體說明"
    }
  ],
  "dimensions": [
    {
      "id": "decision_depth",
      "rating": "足夠",
      "evidence": ["履歷原句"],
      "missing": ["仍需釐清"],
      "issue_ids": ["I01"]
    }
  ],
  "issues": [
    {
      "id": "I01",
      "category": "measurement",
      "severity": "interview_follow_up",
      "claim": "受檢查原句",
      "reason": "缺什麼，為何影響判斷",
      "suggestion": "可執行的補充或改寫方向"
    }
  ],
  "decision": {
    "recommendation": "interview",
    "evidence": ["支持邀約的證據"],
    "blocking_unknowns": []
  },
  "seniority": {
    "delivery": "強",
    "po_coordination": "強",
    "direction_resources": "待補"
  },
  "spectrum": {
    "level": 7,
    "uncertainty_levels": 1,
    "basis": "符合哪些錨點"
  },
  "tests": {
    "pdf_extraction": "not_tested",
    "ats_import": "not_tested",
    "ai_provenance": "indeterminate_from_text_alone"
  }
}
```

至少區分三種 issue severity：

- blocking：明確事實衝突、不可讀的關鍵資料，或有證據顯示不符合職缺必要條件。
- interview_follow_up：需要面試釐清的口徑、角色或能力證據。
- editorial：篇幅、位置、語氣與使用者偏好。

範例中的分數與結論均為結構示意，不得拿來當候選人標準答案。事實核對結果另存，不把事實庫傳給盲審模型。

## 7. 多輪判讀與對照組修正

- 保留五輪可作模型輸出的重複性檢查，但五輪不是五位真人；20 persona × 5 輪也不是 100 個獨立觀測。
- 每輪使用同一模型版本與固定規準，記錄實際模型、參數、輸入 hash、執行時間、位置與失敗狀態；模型無法鎖版時明示。
- 先報每輪決定，再報中位數、範圍，以及 A／B／平手次數。這些是描述性結果，不是招聘勝率。
- 不用「兩版平均差小於波動」當正式統計檢定；若保留，只能作保守提示。不要把五輪樣本做出過度精確的信賴主張。
- 單一重大事實矛盾，即使只被發現一次，也要查證；不能等三輪都指出才修。
- 三輪重複出現可提高「值得檢視」的優先度，但重複不代表正確。
- 同儕 C 沒墊底、對照組超前時保留該輪。回查角色適配、資料完整度、預設標籤與評分器，不按預期名次刪資料。
- 若發生工具失敗、缺頁或錯誤輸入，標 technical_failure 並另行重跑；保留原失敗紀錄與原因。
- 比較版本需相同事實基準與相同審查深度；完整履歷和短摘要不可不加說明地當成等價候選人對照。
- 原始版本結果保留為歷史，修訂後評分不得覆蓋舊結果，不宣稱跨規準分數可直接比較。

## 8. 最少要做的迴歸案例

以下是評分規則的測試，不是人類招聘效度證明。測試答案應在執行前固定。

| 控制變動 | 預期 |
| --- | --- |
| 同一事實把「主責規劃」改為「負責規劃」 | 角色證據相同，不應只因動詞改變能力評價 |
| 把「協作」改成證據不支持的「獨力主導」 | 事實核對應擋住，而不是因語氣強獲得優勢 |
| 加入與能力無關的日期或計數 | 不應提高影響力評價 |
| 加入缺失的分母及比較期間 | 衡量清晰度改善，不把能力與所有維度一同加分 |
| 相關觀察改成因果宣稱 | 應標超出證據 |
| 未上線案例明示狀態及取捨 | 可得決策證據，不得得已實現成果 |
| 將相同取捨由條列移到自傳 | 能力證據不變，可讀性可分別討論 |
| 先給遮罩，再加入全文到另一個請求 | 已保存的初篩結果不可被後來全文改寫 |
| 兩版交換呈現順序 | 記錄偏好是否翻轉；若翻轉，標順序敏感，不隱藏 |
| 英文關鍵字替換成意思清楚的中文 | 不應只因字面未命中就判能力消失 |
| JD 未要求人員管理／英文版／照片 | 不得自動列為缺失 |
| 大項功能與細項不同期間並列 | 提醒口徑及不可相加，不自動判矛盾或當兩組等價成果 |
| 對照組未按預期排名 | 該輪仍保存，觸發方法診斷 |
| 同一缺口被 HR 與主管指出 | 用 issue_id 去重，保留兩種影響說明，不當兩次獨立缺陷 |
| 簽章補入 2026/04/17 | 解除起點缺失，保留監測來源未知；不得聲稱所有可信度問題已解決 |

確定性規則做自動測試；語義判斷用多次結果與證據檢視，不以單次模型輸出完全相同為驗收要求。

若後續另行執行 50 份合成校準：生成者與評分者分開、按獨立特徵設計等級、含單變因控制對、評分前保留未碰過的測試集。修規則用校準集，最終驗證用保留集；同一批反覆重評只能叫迴歸。合成標籤仍不是真人標準。

## 9. 真人校準與真實投遞

不需要先微調模型才開始改善。先找出模型與真人在哪些具體判斷上有系統性差異。

可先做小規模試行：使用取得授權並去識別的履歷與完整目標 JD，請至少兩名熟悉該角色的真人獨立判讀；可行時包含 HR 與用人主管。此人數只是起點，不代表統計上已充分驗證。

真人也使用相同任務：

- 是否值得面試、引用何種證據。
- 哪些是阻擋條件，哪些只是追問。
- 兩版有無明確偏好，為什麼。
- 哪些數字或細節對判斷完全沒有幫助。

保留真人間分歧，不硬湊成單一真理。檢查模型相對於人的誤拒、誤推與理由差異，再調規則；使用未參與調整的案例檢驗。

104 與投遞資料分開追蹤：被搜尋、被閱讀、投遞量、邀約量及後續進展，保留版本、職缺、日期、管道和觀察窗口。不把不同時期或不同職缺造成的差異全算到履歷頭上。沒有可比設計時只能作觀察，不能聲稱因果改善。

缺真人或投遞樣本時，報告 human_calibration: not_performed，不用模型扮演補成真人結果，也不為此停止已授權的規則與腳本修訂。

## 10. Repo 修改與交付清單

先讀實際檔案，不假定本文件列出的腳本一定存在或與說明相同：

- `resume-review-panel`：改提示、persona 角色、輸出 schema、彙整與結果說明。
- `resume-craft`：分離編輯偏好、事實限制與能力評分；刪除迎合分數的迴圈。
- `resume_score.py`：移除關鍵字甜蜜區間及數字比例影響力分數；保留描述性統計。
- `f_scan.py`：更名或明示壓力測試用途，確保初篩請求不含全文。
- `parse_check.py`：保留還原檢查，補關鍵欄位、數值及讀序檢查。
- `ats_search.py`：保留為本地搜尋基準，不冒稱真實 ATS 表現。
- 相關 skill 與說明文件：同步規則、欄位、限制及改版紀錄。

驗收時交付：

1. 哪些檔案改了、舊規則如何被替換。
2. 規準與輸出 schema 的版本。
3. 迴歸案例及實際結果；未通過不得隱藏。
4. 最新事實快照與版本修正清單。
5. 如執行 v8.1／v9.4 比較，交付各版獨立報告及比較結果，允許平手。
6. 未測的 PDF、ATS 匯入、真人校準與資料缺口。
7. 明確寫出：本次是評分器改進與模型內部檢查，尚不能證明招聘成功率提升。

先完成規則與必要測試，再決定是否有證據支持下一版履歷改寫。不要因新規準沒有讓 v9.4 勝出就再調權重；也不要因 v8.1 勝出就還原已知錯誤。

## 11. 參考與適用邊界

- 使用者提供：`validation-methods-complete.md`（2026/10/13）。本規格針對該文件的流程；實際程式仍須核對。
- Zheng et al., Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena：位置、篇幅與自我偏好等模型評審限制。這是一般 LLM 評審研究，不是台灣 PM 招聘效度研究。https://arxiv.org/abs/2306.05685
- U.S. OPM, Structured Interviews：以工作相關能力及一致尺度評估的原則。可借用評估設計，不可把結構化面試效度直接移植成履歷模型效度。https://www.opm.gov/policy-data-oversight/assessment-and-selection/other-assessment-methods/structured-interviews/
- U.S. OPM, How do I score a structured interview?：權重需有理由。https://www.opm.gov/frequently-asked-questions/assessment-policy-faq/structured-interviews/how-do-i-score-a-structured-interview-how-do-i-assign-points-to-the-content-areas-and-rating-scale/

本規格所提角色拆分、輸出欄位與迴歸案例是針對本案的工程與編輯建議，不是已獲真人驗證的通用招聘標準。


## 12. 研究補強：人資實際需要回答的十二個問題

### 12.1 本次研究範圍與沿用方式

使用者要求「至少 50 個來源，之前做過就不用重做」。本次先檢查既有檔案：

- 找到並完整讀取 `resume-bullets-research-50.md`：已整理 50 筆履歷寫作來源，但包含商業 PM 範本，不能直接稱作 50 項人資審閱研究。
- 沿用其中 30 筆較相關的大學職涯中心、人資指南、台灣平台與招聘顧問資料，重新映射到本次規則。這 30 筆本次讀取既有研究筆記，未逐一重開網站；先前查閱日為 2026/10/13。
- 本次另外上網查閱 20 筆招聘端、雇主調查、招聘系統與評估方法資料，開啟相關頁面核對採用內容。查閱日為 2026/10/13。
- 合計 50 個去重頁面；不是 50 個獨立機構、不是 50 位受訪者，也不是 50 項實驗。相同機構的文章及相同理念不能當作多個獨立研究投票。
- 原方法文件提到 `research-hr-hm-2026-10-08.md`，但本次未取得其原始內容，不宣稱已核驗它的 100 條引文。
- Hays 一個搜尋結果開啟後只有導覽頁，未取得文章正文，已排除，不計入 50 筆。相同文章的地區鏡像、104 學習轉貼與搜尋摘要未另行充數。

來源分類只標示能回答哪種問題，不作統一權重：

- A：有調查背景或評估研究依據。仍需考慮年份、地區、對象、自陳偏好與實際預測的差異。
- B：招聘者、招聘公司或平台的實務建議。可支持審閱問題，不是通用淘汰門檻。
- C：職涯中心或寫作指南。主要支持表達與可讀性，不直接證明真人邀約行為。
- D：系統原始操作文件。只支持該系統的功能、解析或流程；不能用來證明候選人能力。
- 同一來源可能混合不同證據；按實際採用段落判定，而非只看品牌。

### 12.2 審閱問題與落地規則

| ID | 人資需要回答的問題 | 在履歷中看什麼 | 如何處理不足 | 來源 |
| --- | --- | --- | --- | --- |
| HR01 | 這個人和這份工作有哪些直接關聯？ | 經驗、技能與明文必要條件的證據對位，包含可轉移經驗 | 區分必要與加分；未寫列 unknown，不要求字面全命中 | S19、S25、S31、S38、S40、S43、S48、S50 |
| HR02 | 他最近實際在做什麼、工作環境和我們有何異同？ | 近期產品、客群、本人範圍及協作環境；資深者的近期代表作 | 產品名或公司名不清楚可建議一句範圍，不因規模／名氣直接加分 | S07、S16、S32、S37、S44、S47 |
| HR03 | 這些經驗中，他本人做了哪一部分？ | 規劃、決策、協作、驗收的具體動作及邊界 | 「協助」後有清楚動作可成立；整體成長不能全歸本人 | S06、S11、S21、S23、S35、S40、S44 |
| HR04 | 工作留下什麼可確認的改變？ | 使用者或業務結果、交付物、流程改變；有數字時辨識期間與母體 | 質性結果可支持；未量測不補數字，目的與結果分開 | S01、S04、S08、S09、S13、S29、S32、S35、S40 |
| HR05 | 面對限制，他如何作判斷？ | 問題、選項、優先級、採取行動與考量 | 對 PM 把結果背後的判斷轉成追問；不強制每點都列被否決方案 | S02、S10、S15、S20、S24、S35、S48 |
| HR06 | 職涯的責任與方向如何演變？ | 工作時間、責任變化、領域轉換；需要釐清的時序 | 任職短或空窗不直接等於不穩定；升遷不是唯一成長證據 | S17、S31、S33、S36、S39、S40、S44 |
| HR07 | 列出的技能、溝通與協作能力是否用過？ | 真實情境、協作對象、如何說清需求／解決分歧／交付 | 工具清單和形容詞只是線索；缺案例列待補，不從英文名稱推測熟練度 | S03、S11、S13、S26、S35、S37、S40、S43、S50 |
| HR08 | 能否容易找到並理解重點？ | 結構、相關性、必要背景、錯誤是否影響理解 | 可建議排序與減字；不按固定秒數、十字、頁數或每句字數淘汰 | S05、S12、S18、S22、S27、S28、S37、S44、S48 |
| HR09 | 哪些聲明需要面試核對，而不是現在直接否定？ | 摘要、經歷與附件的一致性，數字口徑、角色與來源 | 矛盾才走事實修正；未知列追問。內部資料不公開不等於造假 | S12、S27、S31、S34、S35、S39、S40、S46、S49 |
| HR10 | 他的下一步方向和這個職位是否相容？ | 可從經驗選擇、自傳、求職信或已提供答案辨認的職涯方向 | 沒有動機段不推論沒興趣；有明顯方向落差才列需釐清 | S28、S36、S37、S39 |
| HR11 | 實際工作條件是否有已知衝突？ | JD 的地點／語言／到職等要求與提供的求職條件 | 未提供不猜；平台已有欄位不要求 PDF 重複。薪資等可留電話確認 | S38、S39 |
| HR12 | 這份文件足以支持下一步面試嗎？還不能回答什麼？ | 以上證據的整體組合、少數關鍵未知、後續驗證方式 | 輸出邀約／先釐清／不匹配／資訊不足；不把文件分數當聘用能力或錄取率 | S34、S39、S41、S42、S43、S45、S46、S47、S49、S50 |

HR05 是由問題—行動—結果與技能深度建議，轉成 PM 判斷的本案操作化；不是宣稱列出的來源都實證證明「PM 必須寫取捨」。其餘表格也屬跨來源整合，非原文固定量表。

### 12.3 對兩類 PM 職缺的使用方式

不要額外加一個「人資喜好分」。

- 企業平台 PO：HR02、HR03、HR05、HR07 中，優先尋找系統情境、需求取捨、工程／QA／第一線協作的證據。
- 偏策略的資深 PM：同樣的問題，優先找使用者問題選擇、商業模式、定價、優先級與成果衡量。
- HR04 的成果意義依工作判讀；營收不是唯一價值，交付數也不是商業成功。
- 跨國、英文、法遵或人員管理僅在 JD 有關時展開；不因某個 persona 想看就普遍要求。
- 自傳與求職信可以支援動機、判斷與共事方式，但不得拿掉實際經歷證據後以理念替代。
- 把「對我而言產品是作品」這類理念視為敘事脈絡；能否支持能力，要回到具體行動與選擇。

## 13. 分歧資料如何使用，避免重新製造硬規則

| 議題 | 來源顯示的差異 | 本規則採用方式 |
| --- | --- | --- |
| 看履歷到底幾秒 | S48 強調六秒及關鍵字；S44 提醒完整認知需交互比對，不能簡化成秒數 | 保留可掃讀檢查，取消把遮罩通過率叫真人初篩率 |
| 空窗／轉職頻繁 | S33 顯示會引起部分主管疑慮；S39、S40 要求給解釋機會；S44 提醒年資非穩定保證 | 可列追問，不自動判不穩定，更不推論人格、被解僱或留任機率 |
| 數字與成果 | 部分指南鼓勵量化；S09、S29 允許非量化成果 | 能衡量就交代口徑，不能衡量就呈現可確認改變，不以比例湊分 |
| 公司背景與年資 | S44 說明 HR 會用作工作歷練線索；S49 提醒經驗評等不等同未來表現 | 描述環境與責任，不因大公司、名校或待得久直接獎勵 |
| 自傳／照片／英文版 | 台灣平台、學生及國際指南的格式要求不同 | 依明確投遞要求與平台欄位，不普遍加設必填 |
| 動機應放哪裡 | S36 可談興趣與未來潛力；S37 強調短摘要優先回答雇主需要 | 看整份申請材料是否支持方向；不要求摘要硬塞目標，也不推測未寫動機＝無意願 |
| ATS 與搜尋 | S41 說明解析失敗仍可保留附件；S45 說明條件、排序與搜尋路徑 | 分開解析、可搜尋性與內容判斷；本地 BM25 不代表 104 真實排名 |
| 未讀與沒回覆 | S46 提到其他閱讀管道、多人流程與招募情境 | 不把未讀或未回直接標記為履歷失敗，真實投遞評估須保留管道與時間 |
| 新鮮人與資深者 | S47 是無經驗人群，S32 區分不同資歷，學生指南偏早期求職 | 資深 PM 以近期責任、相關案例與影響為重點，不搬學生成績／學校版面權重 |
| 文字精緻與實際能力 | S34、S35、S49 都提醒需進一步核對或評估 | 自然文體有助理解，但不能當真實性證明；不做 AI 作者機率 |

以上取捨不是由文章票數決定。來源描述某種實務偏好，不代表應把該偏好自動化成招聘門檻。

## 14. 50 筆來源清單與規則對照

S01–S30 是沿用既有研究；原序號可回查 `resume-bullets-research-50.md`。本次沒有宣稱重新瀏覽這 30 個網頁。
S31–S50 為本次新增開啟查閱。所有摘要均為閱讀筆記或本案取捨，不是逐字引用。

### 14.1 沿用的 30 筆

| ID／原序號 | 來源連結 | 類型與取得方式 | 採用與限制 | 規則 |
| --- | --- | --- | --- | --- |
| S01／原 1 | [Accomplishment Statements ／ Career Center](https://careercenter.ucdavis.edu/resumes-and-materials/resumes/accomplishment-statements) | C 職涯／寫作指南；沿用筆記 | 以行動、情境、結果交代貢獻；本研究另區分設計目的與實際結果。 | HR04 |
| S02／原 2 | [Action-Oriented Accomplishment Statements ／ Center for Career Development](https://careerdevelopment.princeton.edu/resume-guide/action-oriented-accomplishment-statements) | C 職涯／寫作指南；沿用筆記 | ACE 結構提醒補上工作情境及成果證據，不只列動詞。 | HR05 |
| S03／原 3 | [Accomplishment Statements / Bullet Points - Career Services ／ myUSF](https://myusf.usfca.edu/career-services/career-resources/resumes-cover-letters/resumes/bullet-points) | C 職涯／寫作指南；沿用筆記 | 動作、對象、背景、結果可作為原始材料檢查表。 | HR07 |
| S04／原 4 | [Accomplishment Statements - Career Center - Santa Clara University](https://www.scu.edu/careercenter/toolkit/resumes/accomplishment-statements/) | C 職涯／寫作指南；沿用筆記 | 成果不必是大型商業成功，具體交付也能說明貢獻。 | HR04 |
| S05／原 5 | [Sample Resumes - Career Center](https://career.sa.ua.edu/develop/resumes/sample-resumes/) | C 職涯／寫作指南；沿用筆記 | 以具體工作及結果取代職責清單；學生範本篇幅不直接套用。 | HR08 |
| S06／原 6 | [How to Create Strong Resume Bullet Points ／ University of Michigan-Dearborn](https://umdearborn.edu/career-services/job-and-internship-prep/resumes-and-cover-letters/how-create-strong-resume-bullet) | C 職涯／寫作指南；沿用筆記 | STAR 適合先整理事件，再濃縮；補上本人角色與規模。 | HR03 |
| S07／原 7 | [Resumes and Curriculum Vitae ／ Career Center](https://miamioh.edu/centers-institutes/career-center/professional-development/resumes.html) | C 職涯／寫作指南；沿用筆記 | 優先排列相關且重要的貢獻，保留必要情境。 | HR02 |
| S08／原 8 | [Guidelines for Accomplishment Statements ／ Human Resources](https://hr.ucdavis.edu/departments/learning/toolkits/career-dev/action/accomplish-guidelines) | C 職涯／寫作指南；沿用筆記 | APR 強調問題、行動、結果，以短句表達。 | HR04 |
| S09／原 9 | [Resumes ／ Career Development Center ／ Student Affairs ／ Oregon State University](https://career.oregonstate.edu/resumes-cvs-cover-letters/resumes) | C 職涯／寫作指南；沿用筆記 | 明確提醒適度量化，避免每一點都硬塞數字。 | HR04 |
| S10／原 10 | [Career toolkit: Crafting an effective resume – Career Advising & Professional Development ／ MIT](https://capd.mit.edu/resources/career-toolkit-crafting-an-effective-resume/) | C 職涯／寫作指南；沿用筆記 | PAR、精準動詞及非專業讀者可理解的表達；AI 草稿需核對。 | HR05 |
| S11／原 11 | [CV/Resume : Broad Institute of MIT and Harvard](https://mitcommlab.mit.edu/broad/commkit/cvresume/) | C 職涯／寫作指南；沿用筆記 | 挑選相關內容，說清個人貢獻，降低專業術語閱讀門檻。 | HR03、HR07 |
| S12／原 12 | [Harvard College Guide to Creating a Strong Resume – Harvard FAS ／ Mignone Center for Career Success](https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/) | C 職涯／寫作指南；沿用筆記 | 具體、主動、以事實為本；重點是清楚表達而非華麗修飾。 | HR08、HR09 |
| S13／原 13 | [How to Write Effective Resume Bullets ／ Wellesley Career Education](https://careereducation.wellesley.edu/resources/how-write-effective-resume-bullets) | C 職涯／寫作指南；沿用筆記 | 補上做法、原因、受益者，使工作內容成為具體貢獻。 | HR04、HR07 |
| S14／原 14 | [Resume & CV: Career Process & Resources: Career Services: Student Portal: Luddy School of Informatics, Computing, and Engineering: Indiana University Indianapolis](https://luddy.indianapolis.iu.edu/student-portal/career-services/career-prep/resume.html) | C 職涯／寫作指南；沿用筆記 | 從解決問題、責任範圍及實際工作量找證據。 | HR02、HR04 |
| S15／原 15 | [Elevating Bullet Points ／ Ohio University](https://www.ohio.edu/business/about/centers-institutes/academic-advising-career-services/enhance-resumes-cover-letters/elevating-bullet-points) | C 職涯／寫作指南；沿用筆記 | 用 what/how/why 辨識工作價值，避免只有任務名稱。 | HR05 |
| S16／原 16 | [UVA Darden Career Corner : Pro Tips: How to Write a Great Resume Bullet –](https://blogs.darden.virginia.edu/careercorner/2023/11/28/pro-tips-how-to-write-a-great-resume-bullet/) | C 職涯／寫作指南；沿用筆記 | 具體專案與影響優於泛稱跨部門合作；可採成果先行。 | HR02、HR04 |
| S17／原 17 | [Resumes – Center for Career and Professional Development ／ Kalamazoo College](https://career.kzoo.edu/navigating-the-application-process/resumes/) | C 職涯／寫作指南；沿用筆記 | 選擇最相關成果；大型專案可依不同貢獻拆點。 | HR06 |
| S18／原 18 | [Writing Bullet Points – Graduate Students and Postdocs   – UConn Center for Career Readiness and Life Skills](https://career.uconn.edu/writing-bullet-points-grad-students-postdocs/) | C 職涯／寫作指南；沿用筆記 | 先列做過什麼，再補如何、為何；最後排序與縮寫。 | HR08 |
| S19／原 19 | [台灣就業通 - 找工作-- 一定要會的學經歷、工作經驗簡述 3 技巧！ - 履歷攻略](https://job.taiwanjobs.gov.tw/internet/index/DocDetail.aspx?docid=41540&uk=2747) | B/C 台灣平台指南；沿用筆記 | 工作經歷需有具體細節並對應職缺；Cake 授權轉載僅計一次。 | HR01 |
| S20／原 20 | [履歷怎麼寫？履歷 STAR 原則，讓你的工作經歷 / 學歷更耀眼！｜Yourator 職涯平台專欄｜找工作、求職、徵才](https://www.yourator.co/articles/177) | B/C 台灣平台指南；沿用筆記 | STAR 作為整理背景與行動的框架，非逐句硬套模板。 | HR05 |
| S21／原 21 | [104履歷「個人特色標籤」怎麼寫？3招學會名片簡介、專案成果厲害寫法 ／ 履歷範本篇｜104職場力](https://blog.104.com.tw/resume_teach_2022/) | B/C 台灣平台指南；沿用筆記 | 專案成果應交代自己負責的部分與問題處理。 | HR03 |
| S22／原 22 | [2026履歷表範本免費下載│格式、寫作技巧、自傳密技一次搞定！｜104職場力](https://blog.104.com.tw/resume-download/) | B/C 台灣平台指南；沿用筆記 | 一般履歷架構與重點篩選參考，不作為 PM 專屬實證。 | HR08 |
| S23／原 23 | [〖最新履歷教學〗新鮮人就靠這篇搞定（附範本）｜104職場力](https://blog.104.com.tw/2020-resume-all-in-one/) | B/C 台灣平台指南；沿用筆記 | 團隊成果與個人角色應分清；新鮮人案例僅取通用原則。 | HR03 |
| S24／原 24 | [履歷定生死，編輯教你怎麼寫！內容篇（附104履歷範本）｜104職場力](https://blog.104.com.tw/how-to-write-a-resume/) | B/C 台灣平台指南；沿用筆記 | 具體期間、內容、成果比抽象能力標籤有辨識度。 | HR05 |
| S25／原 25 | [一份好履歷怎麼寫？10 分鐘完成人資最愛履歷表〖附履歷範本、履歷健檢表〗｜Yourator 職涯平台專欄｜找工作、求職、徵才](https://www.yourator.co/articles/152) | B/C 台灣平台指南；沿用筆記 | 職務、角色與成果需清楚；不採用保證通過 ATS 的推論。 | HR01 |
| S26／原 26 | [〖PM 產品經理履歷範本〗掌握 5 點寫出優質 PM 履歷！｜Yourator 職涯平台專欄｜找工作、求職、徵才](https://s.yourator.co/articles/814) | B/C 台灣平台指南；沿用筆記 | PM 成效指標可參考；示例中的留存與營收因果不可套到本人。 | HR07 |
| S27／原 44 | [8 Tips for Writing a Resume](https://www.roberthalf.com/us/en/insights/landing-job/8-tips-for-writing-a-resume) | B/C 招聘／職涯指南；沿用筆記 | 條列易讀、解釋縮寫、保持真實，不堆砌專業術語。 | HR08、HR09 |
| S28／原 45 | [How to write a resume](https://www.roberthalf.com/au/en/insights/landing-job/resume) | B/C 招聘／職涯指南；沿用筆記 | 保留與職務相關內容，刪泛泛敘述，維持本人專業語氣。 | HR08、HR10 |
| S29／原 46 | [How to talk about achievements in your resume - SEEK](https://au.seek.com/career-advice/article/how-to-talk-about-achievements-in-your-resume) | B/C 招聘／職涯指南；沿用筆記 | CAR 加上非量化成果，工作職責與貢獻分開理解。 | HR04 |
| S30／原 50 | [7 Resume Writing Tips to Get You to the Finance Interview](https://www.roberthalf.com/us/en/insights/landing-job/7-resume-writing-tips-to-get-you-to-the-finance-interview) | B/C 招聘／職涯指南；沿用筆記 | 招聘顧問建議具體工作範圍與小型案例；財會要求不直接套用 PM。 | HR02、HR04 |

### 14.2 本次新增查閱的 20 筆

| ID | 來源連結 | 類型與取得方式 | 採用與限制 | 規則 |
| --- | --- | --- | --- | --- |
| S31 | [Robert Half｜How to Master the Art of Reviewing Resumes](https://www.roberthalf.com/us/en/insights/hiring-help/reviewing-resumes-heres-what-you-need-to-know) | B 招聘實務；本次查閱 | 先依工作必要條件分類，再看職涯與適配；保留 maybe。 文章的紅旗是經驗建議；不採空窗、未升遷直接推論性格。 | HR01、HR06、HR09 |
| S32 | [Robert Half｜Recent Work History Top Factor…（2019）](https://press.roberthalf.com/2019-09-19-Survey-Recent-Work-History-Top-Factor-For-Hiring-Managers-When-Evaluating-Tech-Candidates) | A 雇主問卷；本次查閱 | 逾 2,800 名美國 IT 決策者調查，近期經驗及過往專案對中高階候選人重要。 2019 美國 IT 招聘、自陳偏好；不是台灣 PM 預測效度，不能由此固定權重。 | HR02、HR04 |
| S33 | [Robert Half｜5 Considerations to Improve Your Job Search（2022）](https://press.roberthalf.com/2022-10-25-Robert-Half-Shares-5-Considerations-to-Improve-Your-Job-Search) | A 雇主問卷；本次查閱 | 逾 2,300 名美國資深主管調查，模糊工作描述與技能不符會引起疑慮，轉職頻繁也常被注意。 關注比例不是淘汰率；不導出任職必須滿兩年或推斷離職原因。 | HR01、HR06、HR08 |
| S34 | [Robert Half｜Promising Resumes Often Don't Equal Promising Hires（2018）](https://press.roberthalf.com/2018-03-20-Promising-Resumes-Often-Dont-Equal-Promising-Hires) | A 雇主問卷；本次查閱 | 主管回報漂亮履歷與面試表現可能不同；書面篩選只是一個環節。 舊年度調查且屬自陳；不以此估計本人的錄取機率。 | HR09、HR12 |
| S35 | [Robert Half｜AI in the hiring process: … recruit tech talent with more confidence](https://www.roberthalf.com/us/en/insights/management-tips/ai-in-the-hiring-process-and-recruiting-strategies-for-tech-talent) | B 招聘實務；本次查閱 | 以理解深度、本人工作範圍及改變結果追問經驗，工具曝光不等於應用能力。 採框架，不採 AI 作者推測；技術職案例不要求 PM 親自寫程式。 | HR03、HR04、HR07 |
| S36 | [Hays｜Three Burning Questions Your CV Must Answer](https://www.hays.ae/career-advice/article/questions-cv-must-answer-1) | B 招聘實務；本次查閱 | 職缺興趣、可帶來的價值與未來潛力，是閱讀履歷的三種問題。 不把所有動機塞進摘要；不因未寫雄心、空窗未學習或單一錯字推論能力。 | HR01、HR06、HR10 |
| S37 | [Hays｜How to make your CV stand out?](https://www.hays.nl/en/web/hays-netherlands/career-coach/how-to-make-your-cv-stand-out) | B 招聘實務；本次查閱 | 能力摘要之後須在經歷找到證據；近期相關工作優先，舊經歷可簡述。 兩頁是該文建議，不是全球硬門檻；不強制技能重複列兩次。 | HR02、HR07、HR08 |
| S38 | [Workable｜Best practices: Candidate Screening](https://help.workable.com/hc/en-us/articles/23365968258711-Best-practices-Candidate-Screening) | D 系統操作／B 實務；本次查閱 | 先定必要條件，可用申請問題確認技能、年資、地點與薪資。 明確回答 No 不等於履歷沒寫；產品的自動淘汰功能不是普遍適當門檻。 | HR01、HR11 |
| S39 | [Workable｜Screening applicants: best methods and handy tips](https://resources.workable.com/tutorial/screening-applicants) | B 招聘實務；本次查閱 | 履歷、求職信及電話篩選各有用途；未說明空窗值得追問，不是直接淘汰理由。 不從錯字推斷人格；語氣、溝通與能力仍需其他評估。 | HR06、HR09、HR10、HR11 |
| S40 | [Indeed Employer Guide｜How to Read an Applicant Resume](https://www.indeed.com/hire/c/info/how-to-read-a-resume?co=US) | B 雇主指南；本次查閱 | 以一致規準看工作範圍、影響、技能、責任成長與協作；給候選人解釋疑慮的機會。 不採空窗暗示被解僱或難相處的推測，也不依 mentoring 等字詞自動判協作能力。 | HR01、HR03、HR04、HR06、HR07 |
| S41 | [Greenhouse｜Unsuccessful resume parse](https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse) | D 產品原始文件；本次查閱 | 解析失敗可能仍保留附件；姓名聯絡資料置於頁首頁尾或文字框等格式可能造成問題。 僅說明此產品行為；不等於所有 ATS 自動淘汰，不把格式問題當能力不足。 | HR08、HR12 |
| S42 | [Greenhouse｜Scorecard overview](https://support.greenhouse.io/hc/en-us/articles/4414777492891-Scorecard-overview) | D 產品原始文件；本次查閱 | 先設定職缺相關準則，各面試官記錄回饋後再討論。 是結構化招聘流程，不是模型 persona 已具有真人獨立性的證據。 | HR01、HR12 |
| S43 | [Greenhouse｜Structured hiring: Scorecard definitions](https://support.greenhouse.io/hc/en-us/articles/360007247412-Structured-hiring-Scorecard-definitions) | D 產品原始文件；本次查閱 | 把職務成功所需的能力明確化，並用後續面試驗證。 能力項目仍須依職缺設定，不直接搬 traits 作人格評分。 | HR01、HR07、HR12 |
| S44 | [104／楊琮熙｜人資只花XX秒看履歷？重點不在秒數，而是三個關鍵內容](https://blog.104.com.tw/3-key-resume-points-to-catch-the-hr-attention/) | B 台灣招聘者經驗；本次查閱 | 科技業有經驗者會被看工作環境、專業年資、成就及角色；不把審閱簡化成固定秒數。 作者自述適用情境有限；公司規模只作脈絡，不因公司名氣加分，也不採自傳普遍必備。 | HR02、HR03、HR06、HR08 |
| S45 | [104｜用對方法找人才快！5 大查詢履歷技巧](https://blog.104.com.tw/5-important-ways-to-find-talents/) | D 平台操作文件；本次查閱 | 招聘者可透過條件、關鍵字及不同排序查找履歷；搜尋與內容判斷是不同環節。 文章為歷史操作說明，不保證現行全部功能；不採年齡條件作評分，也不採宣傳成效推論本人曝光。 | HR01、HR12 |
| S46 | [104｜人資老實說：投履歷無回的可能原因](https://blog.104.com.tw/why-hr-no-reply/) | B 台灣招聘者訪談彙整；本次查閱 | 可能由多人、Email 或其他系統閱讀，平台未讀不能直接等同未被評估。 非代表性樣本；不採七天無邀請必定失敗等時間推論。 | HR09、HR12 |
| S47 | [104｜人資該怎麼挑新鮮人履歷、如何有效面談？](https://blog.104.com.tw/best-ways-to-attract-gen-z-talent/) | A 平台調查轉述／B 實務；本次查閱 | 提供無工作經驗者的欄位關注資料及人資經驗，顯示審閱重點有職涯階段差異。 對象是新鮮人，不能把比例或科系權重套用近 10 年 PM；本條主要作適用邊界。 | HR02、HR12 |
| S48 | [104／王語逢｜30 年人資主管教你用關鍵字掌握黃金 6 秒](https://blog.104.com.tw/write-your-resume-as-a-marketing-plan/) | B 台灣招聘者經驗；本次查閱 | 主張扣緊工作內容，從關鍵字延伸到曾解決的問題與價值。 其六秒說法與 S44 觀點不同；保留內容對位，不轉成十字遮罩或一律限時。 | HR01、HR07、HR08 |
| S49 | [U.S. OPM｜Training and Experience Evaluations](https://www.opm.gov/policy-data-oversight/assessment-and-selection/other-assessment-methods/training-and-experience-evaluations/) | A 評估研究綜述；本次查閱 | 以工作需求設定經驗評估；傳統經驗評等與工作表現的關係有侷限，自陳需要驗證。 多為美國公部門及早期篩選脈絡；不能把所有履歷模型或台灣 PM 的效度一概定量。 | HR09、HR12 |
| S50 | [U.S. OPM｜Structured Interviews](https://www.opm.gov/policy-data-oversight/assessment-and-selection/other-assessment-methods/structured-interviews/) | A 評估方法指南；本次查閱 | 問題與評分尺度依工作相關能力設計，保持候選人間的一致性。 結構化面試的證據不能直接當履歷文字評分的效度。 | HR01、HR07、HR12 |

## 15. Claude Code 需要追加的實作與驗收

本節與第 0–10 節一起執行。研究清單已完成，不需再為湊 50 筆重搜；若某規則需要引用來源未支持的具體結論，才補查原文。

### 15.1 資料與提示

1. 新增 research registry，保留 source_id、標題、URL、來源類型、取得方式、查閱日、適用地區／職涯階段、採用內容、限制及 mapped_rule_ids。
2. 明確保留 30 筆沿用與 20 筆本次查閱的差別。無法取得原頁時不可偽稱剛核對全文。
3. 為 HR01–HR12 建立 rule registry，記錄問題、適用條件、對應六維度及 source_ids。維度不增加，避免雙重計分。
4. 在獨立評估提示加入十二個招聘問題，但只展開與職缺有關的項目。不強迫每個候選人都寫滿十二種內容。
5. 每項 issue 增加 rule_id、source_ids 與 application_note。source_ids 用來追溯「為什麼要問這個問題」，不是證明候選人的聲明為真。
6. 候選人的履歷證據另存 resume_evidence；研究依據不可混入候選人的事實庫。
7. 凡需要比對其他資料，限本次合法取得並提供的履歷、JD、附件或平台欄位，不默認搜尋候選人私人社群。
8. 採用來源中的經驗建議前，輸出 context_limit；不能因來源有提及就列 blocking。
9. 若 JD 本身含與工作無關的人口特徵偏好，不把它當候選人能力門檻；標示為需人工檢視的條件，不自動執行。

建議增加的欄位示例：

```json
{
  "rule_id": "HR03",
  "source_ids": ["S21", "S35", "S44"],
  "resume_evidence": ["本人規劃產品上線，行銷導入既有用戶"],
  "status": "supported",
  "application_note": "已辨識本人與行銷的不同作用，不把共同 DAU 成長歸為個人單獨效果",
  "context_limit": "招聘實務框架；不據此認證實際因果",
  "severity": null
}
```

### 15.2 追加六個迴歸案例

| 案例 | 驗收要求 |
| --- | --- |
| 兩年內有契約職結束或一段空窗，其他證據相同 | 不直接判低穩定度；有必要時才追問時序，不猜離職原因 |
| 相同工作證據，替換雇主名氣或候選人姓名 | 內容能力評價不應因名氣或人口特徵推測而改變；保留真實工作情境資訊 |
| 移除每點硬塞的頻率數字，但保留決策與交付 | 不應因數字比例下降，自動把策略或影響力判斷降級 |
| 自傳／求職信與平台欄位已包含必要資料，PDF 未重複 | 不自動列缺漏；記錄證據所在位置 |
| 104 顯示未讀，但已知公司透過 Email 閱讀 | 不把未讀當成未通過初篩，不計為履歷內容失敗 |
| 新鮮人指南要求一頁、學歷優先；目標為資深 PM | 不機械套用版面及學歷權重；近期相關經驗與職缺證據優先 |

追加案例與第 8 節原有 15 項合計 21 項。規則改動只做必要回歸；沒有要求此次再跑 50 份合成履歷。

### 15.3 交付結果應回答的問題

- 哪些既有扣分取消了？哪些改為面試追問？
- 每個新規則對應哪些來源，來源的適用限制是什麼？
- 能否指出候選人值得面試的具體理由，而非只報關鍵字、數字比例或 Level？
- 能否辨認重要缺口，同時避免把履歷變成含所有細節的查核報告？
- 是否把可讀性、事實一致性、能力證據及真人招聘效度分開報告？
- 哪些結論因沒有完整 JD、沒有原始資料或沒有真人評分仍然未知？

這次新增的是「有來源的審閱問題與適用邊界」，不是「經過訓練的人資模型」。原有真人校準要求仍然成立，不因湊足 50 筆來源而解除。

