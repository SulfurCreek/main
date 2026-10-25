<!--markdownlint-disable MD013-->

# 審查規準 v4.3（rubric_version 4.3，2026-10-25；v4.2 原則全數保留，增補見 §10）

> 依使用者提供的修訂規格 v4（`career/style/scoring-improvement-v4-source.md`）與 v4.1（`career/style/scoring-improvement-v4.1-source.md`，新增 §12–15：人資十二問、50 筆來源、分歧處理）實作。v4.0 的 2026-10-13 結果保留於 `runs/2026-10-13-v4/`。取代 `blind-output-v3.1.md` 的評分與彙整；v3.x 的歷史報告保留，**跨規準分數不可直接比較**。
> 本規準是模型內部檢查工具，**human_calibration: not_performed**。不得宣稱招聘成功率或「真人會更喜歡」。

## 1. 原則（審查者與彙整者都要遵守）

1. 「未提供證據（unknown）」「證據顯示不符合（contradicted）」「部分支持（partial）」三種狀態分開。
2. 有數字 ≠ 有影響；有影響不一定要數字。數字依性質分類：context／output／outcome／decision／in_progress（可並存）。
3. 使用者的語氣偏好是編輯規則（editorial），不是招聘淘汰條件。
4. 結果、決策品質、交付能力分開評；進行中專案可支持決策，不能算已實現結果。
5. 學歷名氣、公司名氣、管理人數、術語密度、強勢動詞不自動加分；「負責／協助／參與」等誠實描述不自動扣分。
6. a 交付／b PO 跨部門協調／c 方向與資源是能力分布，分別評，不是逐級晉升。
7. 同一缺口只在主要維度計一次（issue_id），其他維度交叉引用。
8. 每個負面判斷都要說明它影響「是否值得面試」或「要追問什麼」。
9. 允許平手、不確定、不適用；不強迫分出高下。
10. 履歷內部一致不代表外部查證成功；使用者口述不能冒充監測紀錄。
11. 不推測空窗、離職原因、性格或誠信。

## 2. 目標職缺（每次只用一份）

本次：Gogolook Senior Product Manager（Anti-Scam BU／2B），104 #950oe，擷取 2026-10 的 `104/jd-digest-A.md` §20。**job_input: summary**（英文原文的中文摘要，可能缺條件；不推測缺漏）。
路線：企業平台／PO 與偏產品策略的資深 PM 兩條路線分開看；使用者目前希望把心力放回產品策略。

## 3. 六維度與評等錨點

| 評等 | 定義 |
| :-- | :-- |
| 強 | 有直接相關的具體案例，關鍵動作與責任清楚，足以支持本職缺所需能力 |
| 足夠 | 有相關證據，足以支持面試，仍有可釐清處 |
| 待補 | 有線索但不足；說明缺口與對面試決策的影響 |
| 未呈現 | 文件沒提供；不推論本人沒有能力 |
| 不適用 | 不是本職缺或本文件需判斷的項目 |

維度：`positioning` 定位與職涯脈絡／`role_evidence` 目標職缺能力證據／`decision_depth` 決策、取捨與使用者理解／`outcome_quality` 結果與衡量品質／`ownership` 個人角色、協作與責任邊界／`readability` 可讀性與資訊取捨。不加權、不算總分。

Level（次要概括，±1 級，非信賴區間、非百分位）：6 有相關案例與可信範圍但缺重要角色或判斷依據；7 多案例足以支持面試；8 另有清楚取捨、可比較衡量、限制、一致專業模式；9–10 高度對應具體目標工作、關鍵量測與責任可追溯。

招聘決定（只能四選一）：`interview` 建議面試／`clarify_first` 需先釐清關鍵條件／`not_matched` 本職缺不匹配／`insufficient_info` 資訊不足。

issue severity：`blocking`（事實衝突、關鍵資料不可讀、有證據顯示不符必要條件）／`interview_follow_up`／`editorial`。

requirement 狀態：`supported`／`partial`／`unknown`／`contradicted`／`not_applicable`；只有「明文必要條件＋有證據顯示不符」才可列 blocking。

## 3.1 人資十二問 HR01–HR12（v4.1；對應六維度，**不是另加十二項總分**）

來源與限制：`rule-registry-v4.2.json`（規則；v4.1 的 12 條 HR 已含於內）、`research-registry-v4.1.json`（50 筆來源；S01–S30 沿用筆記未重開網頁，S31–S50 本次查閱）。來源只說明「為什麼問這個問題」，不證明候選人聲明為真，**不能因來源提及就列 blocking**。

| ID | 問題 | 主維度 | 不足時怎麼處理 | 來源 |
| :-- | :-- | :-- | :-- | :-- |
| HR01 | 這個人和這份工作有哪些直接關聯？ | role_evidence | 區分必要與加分；未寫列 unknown，不要求字面全命中 | S19、S25、S31、S38、S40、S43、S48、S50 |
| HR02 | 他最近實際在做什麼、工作環境和我們有何異同？ | positioning | 產品名或公司名不清楚可建議一句範圍，不因規模／名氣直接加分 | S07、S16、S32、S37、S44、S47 |
| HR03 | 這些經驗中，他本人做了哪一部分？ | ownership | 「協助」後有清楚動作可成立；整體成長不能全歸本人 | S06、S11、S21、S23、S35、S40、S44 |
| HR04 | 工作留下什麼可確認的改變？ | outcome_quality | 質性結果可支持；未量測不補數字，目的與結果分開 | S01、S04、S08、S09、S13、S29、S32、S35、S40 |
| HR05 | 面對限制，他如何作判斷？ | decision_depth | 對 PM 把結果背後的判斷轉成追問；不強制每點都列被否決方案 | S02、S10、S15、S20、S24、S35、S48 |
| HR06 | 職涯的責任與方向如何演變？ | positioning | 任職短或空窗不直接等於不穩定；升遷不是唯一成長證據 | S17、S31、S33、S36、S39、S40、S44 |
| HR07 | 列出的技能、溝通與協作能力是否用過？ | role_evidence | 工具清單和形容詞只是線索；缺案例列待補，不從英文名稱推測熟練度 | S03、S11、S13、S26、S35、S37、S40、S43、S50 |
| HR08 | 能否容易找到並理解重點？ | readability | 可建議排序與減字；不按固定秒數、十字、頁數或每句字數淘汰 | S05、S12、S18、S22、S27、S28、S37、S44、S48 |
| HR09 | 哪些聲明需要面試核對，而不是現在直接否定？ | outcome_quality | 矛盾才走事實修正；未知列追問。內部資料不公開不等於造假 | S12、S27、S31、S34、S35、S39、S40、S46、S49 |
| HR10 | 他的下一步方向和這個職位是否相容？ | positioning | 沒有動機段不推論沒興趣；有明顯方向落差才列需釐清 | S28、S36、S37、S39 |
| HR11 | 實際工作條件是否有已知衝突？ | role_evidence | 未提供不猜；平台已有欄位不要求 PDF 重複。薪資等可留電話確認 | S38、S39 |
| HR12 | 這份文件足以支持下一步面試嗎？還不能回答什麼？ | decision | 輸出邀約／先釐清／不匹配／資訊不足；不把文件分數當聘用能力或錄取率 | S34、S39、S41、S42、S43、S45、S46、S47、S49、S50 |

- 每題標 supported／partial／unknown／not_applicable，附履歷證據（`resume_evidence`）與招聘意義；只展開與本職缺有關的題目。
- 路線差異：企業平台 PO 在 HR02／03／05／07 優先找系統情境、需求取捨、工程／QA／第一線協作；偏策略的資深 PM 優先找問題選擇、商業模式、定價、優先級與成果衡量。
- 跨國、英文、法遵、人員管理只在 JD 有關時展開；自傳、求職信、平台欄位裡的資料都算證據位置，不只看 PDF。
- 理念句（例如「產品是作品」）是敘事脈絡；能否支持能力要回到具體行動與選擇。

### 3.2 分歧資料的處理（規格 §13）

| 議題 | 採用方式 |
| :-- | :-- |
| 看履歷幾秒 | 保留可掃讀檢查；不把遮罩通過率叫真人初篩率 |
| 空窗／轉職 | 可列追問；不判不穩定、不推論人格或離職原因 |
| 數字 | 能衡量就交代口徑；不能衡量就寫可確認的改變；不以比例湊分 |
| 公司背景、年資、學校 | 只當環境與責任脈絡，不直接加分 |
| 自傳／照片／英文版 | 依投遞平台與 JD 明文要求 |
| 動機位置 | 看整份申請材料；未寫動機≠無意願 |
| ATS 與搜尋 | 解析、可搜尋性、內容判斷分開；本地 BM25≠104 排名 |
| 104 未讀／未回 | 不等於履歷失敗；投遞追蹤要記管道與時間 |
| 新鮮人規範 | 資深 PM 不套一頁、學歷優先 |
| 文字精緻度 | 有助理解，不證明真實；不做 AI 作者機率 |

## 4. 四個獨立請求（每個都是新 context，互不可見）

| 階段 | 拿到什麼 | 不給什麼 | 產出 |
| :-- | :-- | :-- | :-- |
| V 截斷文字可見性壓力測試 | 職缺＋遮罩後文字（`f_scan.py --view-only`：前 3 行全句、抬頭 24 字寬、其他行 10 字寬、約 1,400 字截斷；**內部代理規則，不是真實視線**） | 全文、其他版本 | 職稱／公司／年資／職缺相關證據是否可見；unknown 允許；**結果先存檔，之後不得被全文改寫** |
| A 獨立內容審查 | 職缺＋本規準＋**一份**全文 | 事實庫、版本名稱、其他版本、過往排名、改稿目的 | §6 JSON |
| B 版本比較 | 職缺＋兩份全文（甲、乙；順序每輪交換並記錄） | 版本名稱、A 的結果 | 偏好甲／乙／無明確偏好／兩者均須先修正＋差異的招聘意義 |
| F 事實核對 | 履歷＋事實庫（**不給 A、B 審查者**） | — | claim 表：supported／incomplete／unsupported／contradicted／superseded |

PDF 畫面可讀性、ATS 匯入、真人限時初篩：沒做就標 `not_tested`，不可由模型遮罩測試冒稱。

## 5. 提示原文

### V
```text
你在做「截斷文字可見性壓力測試」。下面是一份履歷經過遮罩後還看得到的字（上方幾行全句，其餘每行只剩開頭，…代表被遮住）。
這是內部代理規則，不是真實招募者視線。只能根據看得到的字回答；看不到就寫 unknown，unknown 不代表履歷不合格。
目標職缺：{JD}
{遮罩文字}
只輸出 JSON：{"title":{"value":"","visible":true},"company":{"value":"","visible":true},"years":{"value":"","visible":true},
"job_evidence_visible":[{"requirement":"","quote":""}],"unknown":["看不到、無法判斷的項目"],"note":"一句話"}
```

### A（規格 §5.A，原文照用）
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
依 HR01–HR12 提問，先辨識人資需要解決的招聘問題，再引用履歷證據。
對每個問題標記 supported／partial／unknown／not_applicable，並說明招聘意義。
必要資料是否已在平台欄位、求職信或本次提供的附件呈現，須一併考慮；不要只盯 PDF。
來源中的個人偏好、學生規範、國外情境或產品功能，不得轉成普遍淘汰門檻。
輸出職缺對應、六維度、招聘決定、三個優勢、主要缺口及最多八題面試追問。
本次沒有實際測試的 PDF、ATS 或 AI 作者辨識不得宣稱已完成。
```

### B（規格 §5.B，原文照用）
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

## 6. A 的輸出 JSON（驗證：`scripts/schema_v4.py validate`）

```json
{"rubric_version":"4.1","resume_id":"anonymous_01","job_id":"gogolook_950oe","job_input":"summary",
 "model_id":"","run_id":"","human_calibrated":false,
 "requirements":[{"id":"R01","text":"JD 原句","type":"required|preferred|context","status":"supported|partial|unknown|contradicted|not_applicable","evidence":["履歷原句"],"blocks_interview":false,"reason":""}],
 "dimensions":[{"id":"positioning|role_evidence|decision_depth|outcome_quality|ownership|readability","rating":"強|足夠|待補|未呈現|不適用","evidence":[""],"missing":[""],"issue_ids":[""]}],
 "results":[{"quote":"","kinds":["context|output|outcome|decision|in_progress"]}],
 "hr_questions":[{"rule_id":"HR01","status":"supported|partial|unknown|not_applicable","resume_evidence":["履歷原句"],"application_note":"招聘意義"}],
 "issues":[{"id":"I01","rule_id":"HR01–HR12","source_ids":["S..."],"application_note":"","context_limit":"來源適用限制","category":"measurement|ownership|fact|readability|requirement|style","severity":"blocking|interview_follow_up|editorial","claim":"原句","reason":"","suggestion":""}],
 "decision":{"recommendation":"interview|clarify_first|not_matched|insufficient_info","evidence":[""],"blocking_unknowns":[]},
 "seniority":{"delivery":"強|足夠|待補|未呈現","po_coordination":"…","direction_resources":"…"},
 "strengths":["三個"],"interview_questions":["最多八題"],
 "spectrum":{"level":7,"uncertainty_levels":1,"basis":""},
 "tests":{"pdf_extraction":"not_tested","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"}}
```

B 的輸出：`{"order":"甲=…/乙=…","differences":[{"what":"","hiring_meaning":"","type":"capability|measurement|readability|tone"}],"preference":"甲|乙|無明確偏好|兩者均須先修正","reason":"","evidence_甲":[""],"evidence_乙":[""]}`。

## 7. 彙整（`schema_v4.py aggregate`）

- 先列每輪決定，再列中位數、範圍；比較列甲／乙／平手次數，並檢查**交換順序後偏好是否翻轉**（翻轉＝順序敏感，照實標示）。
- 這些是描述性結果，不是招聘勝率；不用「差距小於波動」當統計檢定。
- 單一重大事實矛盾只出現一次也要查證；≥ 3 輪重複只提高檢視優先度，不代表正確。
- 對照組或同儕沒排在預期位置：保留該輪，做方法診斷，不刪資料。工具失敗標 `technical_failure`，保留紀錄另重跑。
- 修訂後結果不覆蓋舊報告。

## 8. 機械檢查（只報結果，不轉能力分）

| 工具 | v4 行為 |
| :-- | :-- |
| `resume_score.py stats` | 描述性統計（關鍵詞證據對應、含數字比例、左緣訊號比例、抬頭位置）＋`style_lint`（使用者偏好）＋`factual_guard`（事實禁寫）；**不產生 B／C／D 分數** |
| `parse_check.py` | 95% 為**內部回歸門檻**（非業界標準）＋關鍵欄位（職稱、Email、各段日期歸屬）＋重要數字遺漏＋章節讀序 |
| `f_scan.py` | 改名「截斷文字可見性壓力測試」；結構提醒只作版面提醒 |
| `ats_search.py` | 改名「指定語料與查詢下的搜尋實驗」；印出語料、查詢、切詞、參數；**ATS import: not tested** |
| 自傳、照片、英文版 | 依平台與 JD 明文要求，否則 N/A |
| 雙欄 PDF | 以實際還原、讀序、匯入結果判定，不由欄數推論 |


## 9. v4.2 增補（規格 `career/style/scoring-improvement-v4.2-source.md` §16–22，2026-10-14）

| 項目 | 實作 |
| :-- | :-- |
| 來源 | `research-registry-v4.2.json`：A01–A50（ATS 官方文件）、M01–M50（用人主管與選才方法；2026-10-25 追加 M51–M54），規格作者 2026-10-13 查閱；本 session 未重開網頁。與 S01–S50 有重疊，不可相加稱 150 個獨立來源；篇數不是投票權重 |
| 規則 | `rule-registry-v4.2.json`：保留 HR01–HR12，新增 ATS01–ATS14、HM01–HM13（各帶反向 source_ids） |
| ATS 檢查 | `scripts/ats_check.py`：五塊（檔案接受／欄位解析／搜尋可見性／資格流程／匹配與未知設定），pass／risk／fail／unknown／not_applicable，不加總；職稱→公司→日期逐段檢查，總還原率不能掩蓋錯配；test_level 固定 local_extraction |
| A 審查 | 提示加 §19.3 原文與 HM01–HM13 表；JSON 新增 content_questions、interview_reasons（≤3）、key_gaps（≤3）、editorial_appendix、ai_authorship（不給機率）、blocking issue 的 block_target |
| B 比較 | 加一句「依 HM 角度看哪版更能回答值得面試驗證什麼」 |
| 驗證 | `schema_v4.py` 接受 4.2 並檢查上列欄位；`tests/test_v4_rules.py` 新增 7 個確定性案例（R42-03／11／12／14、SCHEMA-42a–c） |
| 未做 | 真實 ATS 匯入、跨模型（本次全為同一模型的新 context，不稱「另一模型」）、真人校準 |

ATS 檢查狀態、事實狀態、六維度評等是三套不同 enum，不混用。

## 10. v4.3 增補（使用者 2026-10-25 指定）

保留 v4.2 全部原則：不造假、不給通用 ATS 分數、區分 context／output／outcome／decision／in_progress、盲審不讀事實庫。規則檔改用 `rule-registry-v4.3.json`（v4.2 檔保留供歷史 run 重現）。

| 規則 | 變更 | 不足時如何回饋 |
| :-- | :-- | :-- |
| **HM14（新增）AI 產品判斷與人機協作邊界**（D2／D3） | 不只看列出模型／工具或 AI 功能上線；檢查 (A) AI 解決了什麼規則引擎做不到的痛點 (B) 面對輸出不確定性如何定驗收標準、回饋修正迴路、人工判斷邊界 | 只有時程或工具名 → 標「有交付但缺產品判斷」，建議補使用情境痛點或品質把關機制 |
| **HM03（強化）策略張力與限制下的取捨**（D3） | 主動逐條掃描核心經歷有無張力：既有系統限制 vs. 翻新、雙線資源競爭、變現 vs. 體驗、降價轉化 vs. 營收 | 寫得像順風順水的任務清單 → 明確指出缺張力，提示可從哪個業務限制、優先序取捨或破局難度切入；**不替候選人編張力** |
| **HM10／HR08（強化）版面投資報酬率與訊號雜訊比**（D6） | 仍不以字數淘汰；檢查 (A) 黃金版面是否用來羅列工具／文件通稱而無商業目的 (B) 統計期間或免責說明是否切斷「行動↔成果」 (C) 模組排序、求職條件措辭與目標路線是否訊號衝突 | 指出原句與衝突的目標路線，給收納口徑或調整排序的方向 |

HM14 來源：S35（Robert Half，工具曝光≠應用能力）、M12（SVPG，將技術用於解決問題）、M51–M54（2026 AI PM 評估，查閱日 2026-10-25，登錄於 `research-registry-v4.2.json`）。依各來源 context_limit：非 AI 職缺僅在履歷列出 AI 功能或 Agent 工作流時才檢查，不作普遍淘汰門檻；不要求寫程式、個人 GitHub 或 Token 成本。

### 10.1 Coach 模式（深度讀後感與優化教練，`--mode coach`）

**觸發**：使用者要「讀後感」「優化建議」「盲審給 Feedback」，或 `career/CLAUDE.md` Stage 3 定稿後自動盲審。

**隔離**：派新子代理（`model: opus`、`effort: low`），**只讀**目標檔（最新 `final_resume.md` 或 `104-<版本>.md`）與本節；**不讀** `career/library/`、`causal_draft.md`、`facts-*`、`decisions.md`、歷史 runs。子代理不得聲稱查證事實；所有「追問」都是對履歷文字的疑問。

**視角**：未指定職缺時，以「策略型資深 PM」與「B2B 平台 PO」雙路線各給判讀，指出同一句在兩條路線的訊號差異。

**底層判讀**：ATS01–14、HR01–12、HM01–14 照常使用，但**禁止只輸出單行 JSON 缺口表**；unknown 只能當註腳，主體必須是讀後心得與改寫洞見。

**輸出（Markdown，四段固定）**：

1. **第一眼 15 秒真實 OS**：第一人稱寫 HR 與用人主管的整體人設印象：最強亮點、整份文件散發的職涯定位訊號，與目標職位的落差。
2. **ATS 檢索與概念對位診斷（ATS03–06）**：已有的真實經驗是否因字眼太內部或太樸素，錯失目標領域的標準概念詞（例：異常登入攔截 → 帳號安全／防詐風控）。只升級概念錨點，不造事實。
3. **逐段訊號雜訊比與策略張力體檢（HM02／03／04／10／14，核心）**：挑 3–5 句「有實績但寫法把功勞變小、像日常交辦或藏住商業判斷」的原句，每句給：
   - **讀者心裡的疑問**：主管會打什麼問號、哪幾個字拉低高度或打斷節奏。
   - **改寫方向**：`原句 → 建議改寫方向`；只調語序、收納括號口徑，或列出要向候選人追問的 Why；**不得新增數字或未寫出的事實**，需要新事實時寫成追問。
4. **面試必考 5 個深水區追問**：其中標出 1–2 題「履歷多補半句（≤15 字）就能提前解除疑慮」。

**收尾**：註明 `human_calibration: not_performed`、審查者為同一模型家族的新 context、未讀事實庫。報告存 `career/review-panel/runs/<日期>-coach-<版本>/report.md`。改寫交 Codex（經 `causal_draft.md` 註解）或 `resume-craft`，coach 不改履歷。
