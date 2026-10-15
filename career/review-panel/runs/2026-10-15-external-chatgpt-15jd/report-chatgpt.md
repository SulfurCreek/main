# 履歷驗證報告：K vs M × 15 職缺｜2026-10-15｜model_id: unknown｜human_calibration: not_run

## 1. 結論
K：interview 15、clarify_first 0、not_matched 0、insufficient_info 0；M：interview 14、clarify_first 1、not_matched 0、insufficient_info 0。
B揭盲：K勝 0、M勝 15、無明確偏好0、兩者均須先修正0。
位置：K當甲8職缺（M勝8）、當乙7職缺（M勝7）。
整體判定：M略佔上風，限文件比較；B一致偏好具體取數分工及配對規則，但A未顯示能力全面較高，且K邀約較多。
兩版均interview且最高Level 8，按JD代號展示前5：jd03、jd09、jd11、jd26、jd30；全部同分候選：jd03、jd09、jd11、jd26、jd30、jd31、jd32、jd34、jd36、jd40、jd43、jd44、jd47。
Level僅在單一職缺內比較；差≤1視同級，不跨職缺計平均或中位數。

## 2. 職缺×版本矩陣

|職缺|K決定/Level|M決定/Level|B偏好揭盲|決定性條件≤20字|
|---|---|---|---|---|
|jd03|interview/8|interview/8|M|支付整合深度待問|
|jd09|interview/8|interview/8|M|訪談與SaaS模式待核|
|jd11|interview/8|interview/8|M|敏捷及英文文件待核|
|jd14|interview/8|interview/7|M|Growth年限與工具待核|
|jd20|interview/8|clarify_first/7|M|B2B年資及近母語英語|
|jd26|interview/8|interview/8|M|法遵及協作工具待核|
|jd30|interview/8|interview/8|M|完整0到1與技術素養|
|jd31|interview/8|interview/8|M|直接訪談及Scrum待核|
|jd32|interview/8|interview/8|M|AI營運分析案例待補|
|jd34|interview/8|interview/8|M|零售流程與Scrum待核|
|jd36|interview/8|interview/8|M|API法遵與工具待核|
|jd40|interview/8|interview/8|M|API與客戶合約待核|
|jd43|interview/8|interview/8|M|總部路線圖及研究待核|
|jd44|interview/8|interview/8|M|長期策略及實驗設計|
|jd47|interview/8|interview/8|M|0到1與技術文件待核|

## 3. 職缺分群

|群組|職缺代號|共同卡關或優勢|
|---|---|---|
|支付／系統整合交付|jd03、jd26、jd36、jd40|規格驗收與串接支持面試；API深度、法遵或客戶責任依各JD追問|
|探索與產品策略|jd09、jd43、jd44|取捨與協作可見；直接研究、長期策略或海外路線圖責任未完整|
|敏捷PO與內部營運|jd11、jd31、jd32、jd34|需求到交付完整；敏捷方法、營運AI或角色期待各有待核|
|新產品與AI技術素養|jd30、jd47|上線經驗可見；同一產品探索至迭代鏈條及技術文件待核|
|特定門檻角色|jd14、jd20|前者全漏斗Growth年限工具待核；後者B2B年資與近母語英語是必要條件|

## 4. 跨職缺重複缺口

下表僅計issues明確指出的缺口，未因某工具出現在履歷就擴張至所有職缺。原句、run_id、issue ID與嚴重度見gap_coding.json；本表未把追問、加分未知或partial一律當淘汰。

|缺口|出現職缺數K/M|影響哪類職缺|需補什麼事實|
|---|---|---|---|
|留存年化方法與群體可比性|9/6|使用留存觀察的產品／成長職缺|年化公式、群體定義、選樣與可比性|
|安全事件觀測來源與覆蓋|13/13|引用登入安全成果的職缺|事件來源、定義、涵蓋期間、漏報限制|
|API規格與異常流程深度|3/3|支付／整合／TPM|本人設計的規則、狀態流與失敗驗收|
|直接訪談的執行與洞察|3/3|需求探索／客戶導向產品|受訪者、本人角色、洞察如何改變需求|
|Jira等指定工具經驗|3/2|指定協作工具的交付職缺|真實使用經驗；未使用則說明可轉移流程|

指定工具缺口可與英文等問題同列於一個issue；此處只編碼該句明說的Jira經驗。Scrum在issues.reason中明文出現於jd31、jd34，未達3個職缺，故不列；一般敏捷問題不併入。SQL實作、Sheet分析、GA4/Firebase等異質條件未合成通用數據缺口。

## 5. 評語合併

### 5.1 K

做得好（每項至少兩個不同職缺原審查支持）：

|位置|原句≤40字|對本職缺用途／來源|
|---|---|---|
|1111／登入改版|選擇首次登入引導確認、不強迫修改|顯示風險與流程取捨；jd03、jd09 decision_depth|
|規格與驗收|與 QA 制定 UAT 驗收案例、排定上線計畫|支持需求到交付鏈條；jd09、jd32 role_evidence|
|主責交付|由我主責規劃，與工程團隊密切協作|本人規劃責任明確；jd09、jd11 ownership|

可改進（只合併跨職缺明確重複項；以下皆非自動淘汰）：

|位置|原句≤40字|問題類型|嚴重度|面試影響|建議方向／來源|
|---|---|---|---|---|---|
|1111／留存條目|該群年化留存 81.2%，同期全站 74.2%|measurement|interview_follow_up|留存觀察不能視為因果；核對年化與群體可比性以確認分析判讀|年化公式、群體定義、選樣與可比性；來源jd03、jd09、jd11、jd14、jd31、jd34、jd40、jd44、jd47|
|1111／帳號安全條目|依目前掌握的情況|measurement|interview_follow_up|未再得知冒用不等於完整監測；核對事件來源與安全驗收界線|事件來源、定義、涵蓋期間、漏報限制；來源jd03、jd09、jd11、jd20、jd26、jd30、jd31、jd34、jd36、jd40、jd43、jd44、jd47|
|尚凡／CodaPay付款條目|並與 CodaPay 新加坡技術團隊協調串接|requirement|interview_follow_up|需看交易異常處理與驗收案例，以確認整合規格深度|本人設計的規則、狀態流與失敗驗收；來源jd03、jd36、jd40|
|專業技能／研究與數據|使用者訪談與問卷、競品實測|requirement|interview_follow_up|需確認本人如何取得第一手需求，並將洞察轉成規格或產品選擇|受訪者、本人角色、洞察如何改變需求；來源jd09、jd11、jd31|
|專業技能／工具|Figma、Axure RP、Notion、Trello、Markdown|requirement|interview_follow_up|僅待確認指定工具經驗與既有流程可轉移性；未列工具不判不符|真實使用經驗；未使用則說明可轉移流程；來源jd11、jd26、jd36|

### 5.2 M

做得好（每項至少兩個不同職缺原審查支持）：

|位置|原句≤40字|對本職缺用途／來源|
|---|---|---|
|1111／登入改版|選擇首次登入引導確認、不強迫修改|顯示風險與流程取捨；jd03、jd09 decision_depth|
|規格與驗收|與 QA 制定 UAT 驗收案例、排定上線計畫|支持需求到交付鏈條；jd09、jd32 role_evidence|
|留存分析分工|由我擬定取數的資料表與欄位|區分本人定義與DBA執行；jd03、jd11 ownership|

可改進（只合併跨職缺明確重複項；以下皆非自動淘汰）：

|位置|原句≤40字|問題類型|嚴重度|面試影響|建議方向／來源|
|---|---|---|---|---|---|
|1111／留存條目|該群年化留存 81.2%，同期全站 74.2%|measurement|interview_follow_up|留存觀察不能視為因果；核對年化與群體可比性以確認分析判讀|年化公式、群體定義、選樣與可比性；來源jd03、jd09、jd11、jd14、jd31、jd40|
|1111／帳號安全條目|上線後至 2026/10 未再出現同類帳號冒用|measurement|interview_follow_up|未再得知冒用不等於完整監測；核對事件來源與安全驗收界線|事件來源、定義、涵蓋期間、漏報限制；來源jd03、jd11、jd20、jd26、jd30、jd31、jd32、jd34、jd36、jd40、jd43、jd44、jd47|
|尚凡／CodaPay付款條目|並與 CodaPay 新加坡技術團隊協調串接|requirement|interview_follow_up|需看交易異常處理與驗收案例，以確認整合規格深度|本人設計的規則、狀態流與失敗驗收；來源jd03、jd36、jd40|
|專業技能／研究與數據|使用者訪談與問卷|requirement|interview_follow_up|需確認本人如何取得第一手需求，並將洞察轉成規格或產品選擇|受訪者、本人角色、洞察如何改變需求；來源jd09、jd31、jd43|
|專業技能／工具|Figma、Axure RP、Notion、Trello|requirement|interview_follow_up|僅待確認指定工具經驗與既有流程可轉移性；未列工具不判不符|真實使用經驗；未使用則說明可轉移流程；來源jd26、jd36|

### 5.3 兩版差異造成的判定不同

只列原決定或Level不同的JD；下述是單輪評語與引用對照，未以控制實驗證明某一句造成分數變化。

|職缺|原判定差異|原輪理由與引用的解讀|
|---|---|---|
|jd14|K interview/8；M interview/7|兩版六維度評等相同；均引用「KOOL 訂閱與付費牆規劃上線」與定價對照，也都要求核對Growth年限、完整漏斗及工具。K basis較強調多案例及衡量限制；M basis強調工具與Growth責任未核。差1視同級，A具體維度不足支持能力差；B偏M僅是文件具體度優勢。|
|jd20|K interview/8；M clarify_first/7|K I01/I02把B2B年資、英語列面試確認；M I01/I02把「近10年PM」不能直接支持5年B2B/B2G，以及「TOEIC 980、TOEFL iBT 93」不能確認近母語，列為先澄清。這是相同必要資格的單次門檻解讀差異，不能歸因M更差。M role_evidence為待補、K為足夠；B仍偏M，理由是取數分工與配對案例較可驗證，不能改寫A決定。|

## 6. ATS五塊不加總

本次M為實際PDF，主流程已用pdftotext 24.02.0抽字並核對3頁；PDF未加密、159,799 bytes，主要欄位與成果數值已視覺交叉核對，與閱讀文字在空白及Markdown項目正規化後一致（3,487字元）。K僅純文字，未提供送出檔。這是本機閱讀證據，不宣稱真實ATS通過。actual_ats_import_performed: false。

|真實ATS五塊|K|M|
|---|---|---|
|檔案接受|unknown/not_tested|unknown/not_tested|
|欄位解析|unknown/not_tested|unknown/not_tested|
|搜尋可見性|unknown/not_tested|unknown/not_tested|
|資格與流程條件|unknown/not_tested|unknown/not_tested|
|匹配功能與未知設定|unknown/not_tested|unknown/not_tested|

A中pdf_extraction: not_tested只表示該獨立審查僅看文字；主流程另做的M本機PDF檢查並不矛盾。完整ATS01–14與本機證據另附，未產生總分。

## 7. 方法限制與未做

共45個新context（A30、B15），共享檔案環境並非OS強隔離。45份輸出均通過結構驗證；原評等及決定不更改。執行期間系統明確提示切換模型，各部署精確model_id未暴露，因此不能確認全程同一模型，也未完成可識別的跨模型驗證；未設計跨模型校準。

每職缺僅一輪A及一輪B，無重測。跨職缺交替甲乙位置與職缺內容混雜；K當甲8職缺、當乙7職缺均偏M，只是描述，不能識別順序因果效應或證明不受位置影響。B的同事實快照核對是使用者前提，本次未外部查證。

JD為摘要，未補全文；jd34年資欄5年與內文2年、jd36年資欄2年與內文3年的矛盾保留，不自行裁決。沒有真人校準、真實ATS測試或真實招聘效度驗證，不判作者是否AI。沒有加入其他對話的新個人背景。

technical_failure依執行紀錄保留：A-jd03-K usage_limit後已有輸出恢復並驗證；A-jd30-K usage_limit及A-jd34-K interruption續做同輪；A-jd32-M Markdown產生器tuple index錯誤經格式修復。均不增加獨立輪次，格式修復不重評。

原始規準逐字凍結，補充執行說明分檔。完整45份JSON及MD另作附錄；盲B原order文字保留為甲輸入／乙輸入，最終附錄提供揭盲映射，不更動投票。


---

# 附錄 A：30 份獨立審查與15份比較完整輸出

以下按職缺排列，逐份提供單行JSON與完整評語。單份審查者只讀一份職缺及一份履歷；比較者只讀該份職缺與甲乙兩份文字。內容審查均採全新、不繼承主對話的context；不向審查者提供過往排名、其他職缺的結果或附件檔名。K／M映射於彙整時揭示。

B輸出的order與揭盲欄位在下方由固定映射填入，其餘偏好、理由、證據均未改。盲審當時原始JSON另保留於附錄B。A中pdf_extraction: not_tested指獨立審查者未測檔案；主流程M本機抽字另見附錄C。



# jd03｜逐次輸出


## A-jd03-K｜履歷K

```json
{"rubric_version": "4.2", "resume_id": "K", "job_id": "jd03", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd03-K", "human_calibrated": false, "requirements": [{"id": "R01", "text": "2年以上獨立PM經驗", "type": "required", "status": "supported", "evidence": ["由我主責規劃"], "blocks_interview": false, "reason": "2018起PM、近期主責規劃及交付，可支持獨立PM要求。"}, {"id": "R02", "text": "能撰寫PRD／User Story／Wireframe", "type": "required", "status": "supported", "evidence": ["從 User Story、Wireframe 到 Figma／Axure 原型"], "blocks_interview": false, "reason": "文件有實際訂閱與招募產品用途。"}, {"id": "R03", "text": "理解API串接與系統運作邏輯", "type": "required", "status": "partial", "evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "blocks_interview": false, "reason": "有串接與系統分析經驗，交易失敗、回調與對帳等技術細節待面試。"}, {"id": "R04", "text": "金融科技／支付／點數／電子票證／電商經驗", "type": "preferred", "status": "supported", "evidence": ["導入 CodaPay"], "blocks_interview": false, "reason": "網頁支付、電信帳單、超商付款與點數設計直接相關。"}, {"id": "R05", "text": "政府機關或銀行產品串接經驗", "type": "preferred", "status": "unknown", "evidence": [], "blocks_interview": false, "reason": "未呈現銀行或政府串接；加分未知不阻擋面試。"}, {"id": "R06", "text": "會員經營／用戶留存經驗", "type": "preferred", "status": "partial", "evidence": ["該群年化留存 81.2%，同期全站 74.2%"], "blocks_interview": false, "reason": "有留存分析與訂閱設計；會員經營策略及成效歸因仍待確認。"}, {"id": "R07", "text": "數據觀測分析經驗", "type": "preferred", "status": "supported", "evidence": ["以 Android 售價不變作對照"], "blocks_interview": false, "reason": "定價實驗與留存觀察提供相關證據，衡量限制另追問。"}, {"id": "R08", "text": "UI／UX規劃經驗", "type": "preferred", "status": "supported", "evidence": ["設定檔案完成、社群認證及照片門檻"], "blocks_interview": false, "reason": "有原型、付費牆與登入流程規劃。"}], "dimensions": [{"id": "positioning", "rating": "強", "evidence": ["訂閱制 B2C App 與雙邊媒合平台。"], "missing": ["近期為招募系統；需確認轉入高頻支付的情境理解。"], "issue_ids": []}, {"id": "role_evidence", "rating": "足夠", "evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "missing": ["API深度與銀行政府經驗待追問。"], "issue_ids": ["I01"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": ["可進一步討論支付情境風險取捨。"], "issue_ids": []}, {"id": "outcome_quality", "rating": "足夠", "evidence": ["為觀察差異，非因果。"], "missing": ["年化方法、付款占比及實驗限制仍需核對。"], "issue_ids": ["I02", "I03"]}, {"id": "ownership", "rating": "強", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫。"], "missing": ["合作方責任及支付決策權限可面試補充。"], "issue_ids": []}, {"id": "readability", "rating": "足夠", "evidence": ["曾設計定價實驗、規劃網頁付款"], "missing": ["可提前支付案例提升本職缺對位速度。"], "issue_ids": []}], "results": [{"quote": "約 50 項大項功能上線", "kinds": ["output"]}, {"quote": "需求平均處理週期由 100.4 天降至 30.9 天", "kinds": ["outcome"]}, {"quote": "該群年化留存 81.2%，同期全站 74.2%", "kinds": ["outcome"]}, {"quote": "依結果全面調降售價", "kinds": ["decision"]}, {"quote": "Peach 網頁付款占營收由 24% 至 80% 以上", "kinds": ["outcome"]}, {"quote": "目前專案仍在開發中", "kinds": ["decision", "in_progress"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["曾設計定價實驗、規劃網頁付款"], "application_note": "支付及產品交付可支持面試"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "近期B2B情境清楚"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我主責規劃"], "application_note": "個人規劃與工程協作有區分"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "有流程結果，核對樣本與口徑"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "有使用者與資料限制取捨"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["近 10 年 PM 經驗，經手 6 款產品"], "application_note": "職涯領域與範圍可追溯"}, {"rule_id": "HR07", "status": "supported", "resume_evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "application_note": "協作有具體產品案例"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["曾設計定價實驗、規劃網頁付款"], "application_note": "摘要可找到支付相關經驗"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["依目前掌握的情況"], "application_note": "安全結果屬自述，需確認監測"}, {"rule_id": "HR10", "status": "supported", "resume_evidence": ["我希望將更多心力放回產品策略"], "application_note": "方向與產品規劃相容"}, {"rule_id": "HR11", "status": "not_applicable", "resume_evidence": [], "application_note": "JD未提供可比對工作條件"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫。"], "application_note": "可約談並驗證支付技術深度"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["訂閱制 B2C App 與雙邊媒合平台。"], "evidence_type": "context", "source_ids": [], "interview_question": "如何從訂閱支付轉入高頻交易場景？"}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["最大宗是溝通管道中斷"], "evidence_type": "decision", "source_ids": [], "interview_question": "如何把工單訊號轉成優先順序？"}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "evidence_type": "decision", "source_ids": [], "interview_question": "比較過哪些登入方案與風險？"}, {"rule_id": "HM04", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "evidence_type": "decision", "source_ids": [], "interview_question": "支付成本如何影響方案選擇？"}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "partial", "resume_evidence": ["為觀察差異，非因果。"], "evidence_type": "outcome", "source_ids": [], "interview_question": "年化留存如何算，付款占比變化代表何種價值？"}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["與資料科學團隊合作，定義使用情境與驗收標準"], "evidence_type": "output", "source_ids": [], "interview_question": "你與工程及合作方的決策邊界為何？"}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫。"], "evidence_type": "output", "source_ids": [], "interview_question": "如何定義支付錯誤與恢復流程的驗收？"}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "partial", "resume_evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "evidence_type": "output", "source_ids": [], "interview_question": "請畫一個付款API成功、逾時及重複通知流程。"}, {"rule_id": "HM09", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "evidence_type": "output", "source_ids": [], "interview_question": "哪些範圍與風險由你獨立決定？"}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["曾設計定價實驗、規劃網頁付款"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則"], "evidence_type": "decision", "source_ids": [], "interview_question": "哪項回饋改變規則，後續如何驗證？"}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["導入 CodaPay"], "evidence_type": "output", "source_ids": [], "interview_question": "以去識別化支付PRD說明規則及驗收。"}, {"rule_id": "HM13", "primary_dimension": "", "status": "not_applicable", "resume_evidence": [], "evidence_type": null, "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HM08", "source_ids": [], "application_note": "面試追問，不阻擋邀約", "context_limit": "僅履歷文字自述，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "並與 CodaPay 新加坡技術團隊協調串接", "reason": "有串接案例但未呈現API錯誤處理與交易狀態設計；影響技術深度驗證。", "suggestion": "補一例負責的API規則、異常情境與驗收邊界；面試看去識別化規格。"}, {"id": "I02", "rule_id": "HM05", "source_ids": [], "application_note": "面試追問，不阻擋邀約", "context_limit": "僅履歷文字自述，未外部查證", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "該群年化留存 81.2%，同期全站 74.2%", "reason": "短期快照年化與選樣可能影響解讀；已註明非因果，不否定觀察。", "suggestion": "交代留存定義、快照轉年化方法與兩群可比性。"}, {"id": "I03", "rule_id": "HR09", "source_ids": [], "application_note": "面試追問，不阻擋邀約", "context_limit": "僅履歷文字自述，未外部查證", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "依目前掌握的情況", "reason": "未再冒用屬掌握範圍自述，並非監測證明；需確認安全成效口徑。", "suggestion": "補充通報或監測來源、覆蓋範圍；無紀錄則保留限定語。"}], "decision": {"recommendation": "interview", "evidence": ["曾設計定價實驗、規劃網頁付款", "選擇首次登入引導確認、不強迫修改"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["「導入 CodaPay」提供支付與合作方串接經驗。", "「與 QA 制定 UAT 驗收案例、排定上線計畫。」支持交付。", "「選擇首次登入引導確認、不強迫修改」呈現取捨。"], "key_gaps": ["支付API與交易異常處理深度尚未完整呈現。", "銀行政府串接未呈現；會員經營策略僅部分支持。", "留存年化與安全結果的衡量來源待核對。"], "strengths": ["支付串接與實收試算直接關聯職缺。", "規格、協作、驗收到上線責任清楚。", "登入方案取捨與進行中專案區分清楚。"], "interview_questions": ["請用CodaPay案例畫出API、交易狀態、異常處理與驗收。", "與銀行或政府機關有無串接經驗？責任為何？", "年化留存的定義、方法與群體選擇為何？", "付款占比提升時，實收及總營收如何變化？", "定價實驗的分群、同期干擾與還原期異常如何解釋？", "會員留存策略中，你做了哪些選擇？", "安全事件有何監測與通報範圍？"], "editorial_appendix": ["可將支付串接與實收試算案例提前，不改變能力判斷。"], "spectrum": {"level": 8, "uncertainty_levels": 1, "basis": "多案例、責任與取捨清楚，衡量有期間及限制；支付技術深度仍待驗證。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷K｜第 1 輪｜model_id: unknown

### 1. 結論

- 招聘決定：interview

- Level：8（±1）

- 一句話理由：「導入 CodaPay」加上具體規格交付與取捨，足以面試確認支付深度。

### 2. 六維度

| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |

| :-- | :-- | :-- | :-- |

| positioning | 強 | 訂閱制 B2C App 與雙邊媒合平台。 | 近期為招募系統；需確認轉入高頻支付的情境理解。 |

| role_evidence | 足夠 | 並與 CodaPay 新加坡技術團隊協調串接 | API深度與銀行政府經驗待追問。 |

| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 可進一步討論支付情境風險取捨。 |

| outcome_quality | 足夠 | 為觀察差異，非因果。 | 年化方法、付款占比及實驗限制仍需核對。 |

| ownership | 強 | 與 QA 制定 UAT 驗收案例、排定上線計畫。 | 合作方責任及支付決策權限可面試補充。 |

| readability | 足夠 | 曾設計定價實驗、規劃網頁付款 | 可提前支付案例提升本職缺對位速度。 |

### 3. JD 條件對照

| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |

| :-- | :-- | :-- | :-- | :-- |

| 2年以上獨立PM經驗 | 必要 | supported | 由我主責規劃 | 2018起PM、近期主責規劃及交付，可支持獨立PM要求。 |

| 能撰寫PRD／User Story／Wireframe | 必要 | supported | 從 User Story、Wireframe 到 Figma／Axure 原型 | 文件有實際訂閱與招募產品用途。 |

| 理解API串接與系統運作邏輯 | 必要 | partial | 並與 CodaPay 新加坡技術團隊協調串接 | 有串接與系統分析經驗，交易失敗、回調與對帳等技術細節待面試。 |

| 金融科技／支付／點數／電子票證／電商經驗 | 加分 | supported | 導入 CodaPay | 網頁支付、電信帳單、超商付款與點數設計直接相關。 |

| 政府機關或銀行產品串接經驗 | 加分 | unknown | 未呈現 | 未呈現銀行或政府串接；加分未知不阻擋面試。 |

| 會員經營／用戶留存經驗 | 加分 | partial | 該群年化留存 81.2%，同期全站 74.2% | 有留存分析與訂閱設計；會員經營策略及成效歸因仍待確認。 |

| 數據觀測分析經驗 | 加分 | supported | 以 Android 售價不變作對照 | 定價實驗與留存觀察提供相關證據，衡量限制另追問。 |

| UI／UX規劃經驗 | 加分 | supported | 設定檔案完成、社群認證及照片門檻 | 有原型、付費牆與登入流程規劃。 |

### 4. HR 十二問 ／ HM 十三問

| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |

| :-- | :-- | :-- | :-- |

| HR01 | supported | 曾設計定價實驗、規劃網頁付款 | 支付及產品交付可支持面試 |

| HR02 | supported | 企業端招募系統全模組與求職端公司頁 | 近期B2B情境清楚 |

| HR03 | supported | 由我主責規劃 | 個人規劃與工程協作有區分 |

| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 有流程結果，核對樣本與口徑 |

| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 有使用者與資料限制取捨 |

| HR06 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 職涯領域與範圍可追溯 |

| HR07 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 協作有具體產品案例 |

| HR08 | supported | 曾設計定價實驗、規劃網頁付款 | 摘要可找到支付相關經驗 |

| HR09 | partial | 依目前掌握的情況 | 安全結果屬自述，需確認監測 |

| HR10 | supported | 我希望將更多心力放回產品策略 | 方向與產品規劃相容 |

| HR11 | not_applicable | 未呈現 | JD未提供可比對工作條件 |

| HR12 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫。 | 可約談並驗證支付技術深度 |

| HM01 | supported | 訂閱制 B2C App 與雙邊媒合平台。 | 具體案例支持邀約 |

| HM02 | supported | 最大宗是溝通管道中斷 | 具體案例支持邀約 |

| HM03 | supported | 選擇首次登入引導確認、不強迫修改 | 具體案例支持邀約 |

| HM04 | supported | 依抽成、稅、手續費及撥款週期做實收試算 | 具體案例支持邀約 |

| HM05 | partial | 為觀察差異，非因果。 | 面試核對技術或衡量限制 |

| HM06 | supported | 與資料科學團隊合作，定義使用情境與驗收標準 | 具體案例支持邀約 |

| HM07 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫。 | 具體案例支持邀約 |

| HM08 | partial | 並與 CodaPay 新加坡技術團隊協調串接 | 面試核對技術或衡量限制 |

| HM09 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 具體案例支持邀約 |

| HM10 | supported | 曾設計定價實驗、規劃網頁付款 | 具體案例支持邀約 |

| HM11 | supported | 依客服測試回饋調整推薦規則 | 具體案例支持邀約 |

| HM12 | supported | 導入 CodaPay | 具體案例支持邀約 |

| HM13 | not_applicable | 方法層，非履歷能力項 | 方法規範不加分 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）

| # | 約談理由（引原句） |

| :-- | :-- |

| 1 | 「導入 CodaPay」提供支付與合作方串接經驗。 |

| 2 | 「與 QA 制定 UAT 驗收案例、排定上線計畫。」支持交付。 |

| 3 | 「選擇首次登入引導確認、不強迫修改」呈現取捨。 |



| # | 關鍵缺口 | 面試追問 |

| :-- | :-- | :-- |

| 1 | 支付API與交易異常處理深度尚未完整呈現。 | 請用CodaPay案例畫出API、交易狀態、異常處理與驗收。 |

| 2 | 銀行政府串接未呈現；會員經營策略僅部分支持。 | 與銀行或政府機關有無串接經驗？責任為何？ |

| 3 | 留存年化與安全結果的衡量來源待核對。 | 年化留存的定義、方法與群體選擇為何？ |

### 6. 評語（給寫稿者的具體回饋）

**做得好（3 點）**：

- 思維特支付｜「依抽成、稅、手續費及撥款週期做實收試算」｜連結支付產品選擇與商業成本。

- 1111交付｜「與 QA 制定 UAT 驗收案例、排定上線計畫。」｜對應規格、跨部門協作及進度責任。

- 登入改版｜「選擇首次登入引導確認、不強迫修改」｜顯示資料限制與使用者體驗取捨。

**可改進（3 點）**：

- 位置：尚凡付款串接
  - 原句：並與 CodaPay 新加坡技術團隊協調串接
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：有串接案例但未呈現API錯誤處理與交易狀態設計；影響技術深度驗證。
  - 建議方向：補一例負責的API規則、異常情境與驗收邊界；面試看去識別化規格。

- 位置：1111留存
  - 原句：該群年化留存 81.2%，同期全站 74.2%
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：短期快照年化與選樣可能影響解讀；已註明非因果，不否定觀察。
  - 建議方向：交代留存定義、快照轉年化方法與兩群可比性。

- 位置：1111登入安全
  - 原句：依目前掌握的情況
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：未再冒用屬掌握範圍自述，並非監測證明；需確認安全成效口徑。
  - 建議方向：補充通報或監測來源、覆蓋範圍；無紀錄則保留限定語。

**編輯附件**（不影響判斷）：可提前支付案例。

### 7. 資深能力分布

delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

方向選擇已有定價、優先級與成本試算證據；組織資源配置未完整呈現，非本職缺阻擋條件。

### 8. 未測試聲明

PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

所有證據為履歷自述，內部一致不等於外部查證。未加權或計算總分。

### 成果分類補表

| 原句／原文片段 | 分類 | 解讀限制 |

| :-- | :-- | :-- |

| 約 50 項大項功能上線 | output | 依正文限制解讀 |

| 需求平均處理週期由 100.4 天降至 30.9 天 | outcome | 依正文限制解讀 |

| 該群年化留存 81.2%，同期全站 74.2% | outcome | 依正文限制解讀 |

| 依結果全面調降售價 | decision | 依正文限制解讀 |

| Peach 網頁付款占營收由 24% 至 80% 以上 | outcome | 依正文限制解讀 |

| 目前專案仍在開發中 | decision／in_progress | 依正文限制解讀 |

| 全站活躍付費廠商約 6.6 萬家 | context | 系統規模非個人創造成果 |

| 另於 2026/01–06 上線 111 項 Roadmap 細項。 | output | 與50項口徑不同，不相加 |

| 停機約 1.5 小時 | output | 切換作業時間，非使用者價值證明 |

| 未再出現同類帳號冒用 | outcome | 依掌握情況，非監測證據 |

| 完成 1,726／1,857 張需求與問題單，約 93%。 | output | 處理量與完成率 |

| 需求管線觸及 1,279 家活躍付費廠商 | context | 觸及群體規模 |

| AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。 | output | 已交付，不等於採用改善 |

| 依客服測試回饋調整推薦規則 | decision | 回饋促成調整 |

| 降價期 iOS 非續訂營收較基準期增 5% | outcome | 非全部營收，需確認同期干擾 |

| Android 減 18%，相對變化約多 28% | outcome | 對照相對變化，非絕對淨成長 |

| 還原原價後 iOS 較基準期減 65% | outcome | 基準與異常原因待追問 |

| KOOL 訂閱與付費牆規劃上線 | output | 跨平台交付 |

| 設定檔案完成、社群認證及照片門檻 | decision | 資格規則選擇 |

| 主導 Juicy 上線 | output | 配合行銷導流 |

| 上線後 6 週男性 DAU 約 3,200 至 1.25 萬 | outcome | 團隊及行銷期間整體表現 |

| SweetRing 在地化涵蓋美國、墨西哥、巴西、印尼、馬來西亞、日本、韓國 7 個市場 | output | 在地化範圍非成長率 |

| 與最多約 10 位外國實習生協作 | context | 非直屬管理人數 |

| 導入 CodaPay | output | 付款方式交付 |

| 提出 7／30／90 天訂閱方案與加贈內容 | decision/output | 成本試算後方案，不推論業績 |

| Newegg.com 商品資訊英翻中與校對。 | output | 翻譯交付 |

| 我便將信件與即時通整合排在其他新功能之前 | decision/in_progress | 優先級已決定，專案未完成 |


## A-jd03-M｜履歷M

```json
{"rubric_version": "4.2", "resume_id": "M", "job_id": "jd03", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd03-M", "human_calibrated": false, "requirements": [{"id": "R01", "text": "2年以上獨立PM經驗", "type": "required", "status": "supported", "evidence": ["由我主責規劃"], "blocks_interview": false, "reason": "任期與主責規劃、優先級案例支持獨立PM經驗。"}, {"id": "R02", "text": "能撰寫PRD", "type": "required", "status": "supported", "evidence": ["整理為 PRD 與 Axure Prototype"], "blocks_interview": false, "reason": "文件連結業務流程與交付。"}, {"id": "R03", "text": "能撰寫User Story", "type": "required", "status": "supported", "evidence": ["從 User Story、Wireframe 到 Figma／Axure 原型"], "blocks_interview": false, "reason": "KOOL有實際應用。"}, {"id": "R04", "text": "能撰寫Wireframe", "type": "required", "status": "supported", "evidence": ["以 Use Case、Wireframe 定義業務流程與畫面"], "blocks_interview": false, "reason": "直接證據。"}, {"id": "R05", "text": "理解API串接與系統運作邏輯", "type": "required", "status": "partial", "evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "blocks_interview": false, "reason": "串接協作與系統分析相關，介面規則及異常處理深度待面試確認。"}, {"id": "R06", "text": "金融科技／支付／點數／電子票證／電商經驗", "type": "preferred", "status": "supported", "evidence": ["規劃 VIP 訂閱、點數付費牆與精選置頂曝光"], "blocks_interview": false, "reason": "付款與點數經驗命中加分領域，不推定電子票證經驗。"}, {"id": "R07", "text": "政府機關或銀行產品串接經驗", "type": "preferred", "status": "unknown", "evidence": [], "blocks_interview": false, "reason": "CodaPay合作不等於銀行或政府串接；非阻擋條件。"}, {"id": "R08", "text": "會員經營／用戶留存經驗", "type": "preferred", "status": "supported", "evidence": ["該群年化留存 81.2%，同期全站 74.2%"], "blocks_interview": false, "reason": "訂閱、會員資格及留存分析具相關性，非因果提升。"}, {"id": "R09", "text": "數據觀測分析經驗", "type": "preferred", "status": "supported", "evidence": ["以 Android 售價不變作對照"], "blocks_interview": false, "reason": "定價實驗與留存觀察有具體方法。"}, {"id": "R10", "text": "UI/UX規劃經驗", "type": "preferred", "status": "supported", "evidence": ["選擇首次登入引導確認、不強迫修改"], "blocks_interview": false, "reason": "登入流程取捨及原型支持。"}], "dimensions": [{"id": "positioning", "rating": "強", "evidence": ["涵蓋訂閱制社交 App、網紅媒合及企業招募系統"], "missing": ["近期為企業招募；高頻支付運作情境可在面試確認。"], "issue_ids": []}, {"id": "role_evidence", "rating": "足夠", "evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "missing": ["API錯誤、對帳與狀態流轉深度待核對。"], "issue_ids": ["I01"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": ["決策理由清楚，可追問風險評估與替代方案。"], "issue_ids": []}, {"id": "outcome_quality", "rating": "強", "evidence": ["為觀察差異，非因果"], "missing": ["留存年化算法與安全觀測來源仍待釐清。"], "issue_ids": ["I02", "I03"]}, {"id": "ownership", "rating": "強", "evidence": ["由我擬定取數的資料表與欄位"], "missing": ["本人定義與DBA執行分開；付款成果分工可追問。"], "issue_ids": []}, {"id": "readability", "rating": "足夠", "evidence": ["資深產品經理｜Senior Product Manager"], "missing": ["可前置支付案例，協助辨識與Pi職缺關聯。"], "issue_ids": ["I04"]}], "results": [{"quote": "約 50 項大項功能上線", "kinds": ["output"]}, {"quote": "選擇首次登入引導確認、不強迫修改", "kinds": ["decision"]}, {"quote": "需求平均處理週期由 100.4 天降至 30.9 天", "kinds": ["outcome"]}, {"quote": "該群年化留存 81.2%，同期全站 74.2%", "kinds": ["outcome"]}, {"quote": "兩案皆開發中", "kinds": ["decision", "in_progress"]}, {"quote": "Peach 網頁付款占營收由 24% 至 80% 以上", "kinds": ["outcome"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "application_note": "支付經驗與規格交付支持約談"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "近期環境清楚，可轉移至平台產品"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我擬定取數的資料表與欄位"], "application_note": "規劃與執行邊界具體"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "有流程改變，定義可面試確認"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "兼顧資料與客戶登入風險"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["近 10 年 PM 經驗，經手 6 款產品"], "application_note": "責任演變有案例支持"}, {"rule_id": "HR07", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "application_note": "跨職能協作連結實際交付"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["曾設計定價實驗、規劃網頁付款"], "application_note": "相關案例可找到，支付可前置"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["依目前掌握的情況"], "application_note": "安全與留存口徑需核對來源"}, {"rule_id": "HR10", "status": "supported", "resume_evidence": ["接下來，我希望將更多心力放回產品策略"], "application_note": "方向與產品規劃相容"}, {"rule_id": "HR11", "status": "not_applicable", "resume_evidence": ["錄取後三週可上班"], "application_note": "JD未列工作條件，無已知衝突"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["從需求釐清、系統分析到 PRD、原型、UAT 與上線計畫"], "application_note": "足以面試，API深度留案例驗證"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["訂閱制 B2C App 與雙邊媒合平台"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["客服反映配對名單「少又舊」"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["改版排在新功能職缺健檢之前"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM04", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "supported", "resume_evidence": ["為觀察差異，非因果"], "evidence_type": "outcome", "source_ids": [], "interview_question": null}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["與資料科學團隊合作，定義使用情境與驗收標準"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["第一階段於 2025/10 離峰切換上線"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "partial", "resume_evidence": ["API 串接規劃、舊系統資料盤點"], "evidence_type": "context", "source_ids": [], "interview_question": "請用付款串接案例說明交易狀態、失敗重試與驗收責任。"}, {"rule_id": "HM09", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["曾設計定價實驗、規劃網頁付款"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["規劃由 App 內購轉向網頁付款"], "evidence_type": "decision", "source_ids": [], "interview_question": "請用付款串接案例說明交易狀態、失敗重試與驗收責任。"}, {"rule_id": "HM13", "primary_dimension": "", "status": "not_applicable", "resume_evidence": [], "evidence_type": null, "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HM08", "source_ids": [], "application_note": "不阻擋面試；需確認API理解達必備深度。", "context_limit": "付款串接段", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "並與 CodaPay 新加坡技術團隊協調串接", "reason": "尚未呈現API業務規則與失敗處理細節。", "suggestion": "補一個規則或異常流程的規劃與驗收例，不要求寫程式。"}, {"id": "I02", "rule_id": "HM05", "source_ids": [], "application_note": "影響衡量可信範圍，不否定已呈現分析能力。", "context_limit": "留存分析段", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "該群年化留存 81.2%，同期全站 74.2%", "reason": "兩次快照如何年化、同群口徑與觀察偏差仍待確認。", "suggestion": "說明年化公式、群體定義與非隨機選樣限制。"}, {"id": "I03", "rule_id": "HR09", "source_ids": [], "application_note": "面試追問事件資料來源及覆蓋範圍。", "context_limit": "登入安全段", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "上線後至 2026/10 未再出現同類帳號冒用", "reason": "目前掌握情況不等於完整安全監控。", "suggestion": "保留保守措辭，註明依客服回報或監測何種訊號。"}, {"id": "I04", "rule_id": "HR08", "source_ids": [], "application_note": "只影響相關證據可見性，不改變能力判定。", "context_limit": "專業摘要", "category": "readability", "severity": "editorial", "block_target": null, "claim": "曾設計定價實驗、規劃網頁付款", "reason": "支付證據分布於較早經歷，讀者需串接。", "suggestion": "在摘要前置支付合作、點數及API規劃的現有證據。"}], "decision": {"recommendation": "interview", "evidence": ["並與 CodaPay 新加坡技術團隊協調串接", "以 Use Case、Wireframe 定義業務流程與畫面", "選擇首次登入引導確認、不強迫修改"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["「並與 CodaPay 新加坡技術團隊協調串接」對應支付合作。", "「整理為 PRD 與 Axure Prototype」支持規格交付。", "「選擇首次登入引導確認、不強迫修改」呈現取捨。"], "key_gaps": ["API交易狀態與異常處理深度", "留存年化算法與選樣限制", "安全事件觀測來源與覆蓋"], "strengths": ["付款與點數產品經驗，並有合作技術團隊對接。", "需求至規格、驗收及分期上線有完整責任線索。", "取捨與衡量限制清楚，觀察差異不冒充因果。"], "interview_questions": ["請以CodaPay串接說明交易狀態、回呼失敗、重試與驗收責任。", "留存快照如何年化？群體如何選取，可能有哪些偏差？", "未再出現冒用依據哪些事件來源，覆蓋範圍如何？", "網頁付款占比變動中你的決策與行銷、工程貢獻如何區分？", "定價實驗如何處理時間差、匯率及客群差異？", "曾如何與銀行或政府合作？若未曾，如何理解串接限制？"], "editorial_appendix": ["可將既有支付與點數案例前置；不需要增加術語。"], "spectrum": {"level": 8, "uncertainty_levels": 1, "basis": "多案例具清楚取捨、衡量期間與限制，支付及會員可轉移；核心API深度尚待面試驗證。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷｜第 1 輪｜model_id: unknown

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「並與 CodaPay 新加坡技術團隊協調串接」及規格、取捨案例支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 涵蓋訂閱制社交 App、網紅媒合及企業招募系統 | 近期為企業招募；高頻支付運作情境可在面試確認。 |
| role_evidence | 足夠 | 並與 CodaPay 新加坡技術團隊協調串接 | API錯誤、對帳與狀態流轉深度待核對。 |
| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 決策理由清楚，可追問風險評估與替代方案。 |
| outcome_quality | 強 | 為觀察差異，非因果 | 留存年化算法與安全觀測來源仍待釐清。 |
| ownership | 強 | 由我擬定取數的資料表與欄位 | 本人定義與DBA執行分開；付款成果分工可追問。 |
| readability | 足夠 | 資深產品經理｜Senior Product Manager | 可前置支付案例，協助辨識與Pi職缺關聯。 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 2年以上獨立PM經驗 | 必要 | supported | 由我主責規劃 | 任期與主責規劃、優先級案例支持獨立PM經驗。 |
| 能撰寫PRD | 必要 | supported | 整理為 PRD 與 Axure Prototype | 文件連結業務流程與交付。 |
| 能撰寫User Story | 必要 | supported | 從 User Story、Wireframe 到 Figma／Axure 原型 | KOOL有實際應用。 |
| 能撰寫Wireframe | 必要 | supported | 以 Use Case、Wireframe 定義業務流程與畫面 | 直接證據。 |
| 理解API串接與系統運作邏輯 | 必要 | partial | 並與 CodaPay 新加坡技術團隊協調串接 | 串接協作與系統分析相關，介面規則及異常處理深度待面試確認。 |
| 金融科技／支付／點數／電子票證／電商經驗 | 加分 | supported | 規劃 VIP 訂閱、點數付費牆與精選置頂曝光 | 付款與點數經驗命中加分領域，不推定電子票證經驗。 |
| 政府機關或銀行產品串接經驗 | 加分 | unknown | 未呈現 | CodaPay合作不等於銀行或政府串接；非阻擋條件。 |
| 會員經營／用戶留存經驗 | 加分 | supported | 該群年化留存 81.2%，同期全站 74.2% | 訂閱、會員資格及留存分析具相關性，非因果提升。 |
| 數據觀測分析經驗 | 加分 | supported | 以 Android 售價不變作對照 | 定價實驗與留存觀察有具體方法。 |
| UI/UX規劃經驗 | 加分 | supported | 選擇首次登入引導確認、不強迫修改 | 登入流程取捨及原型支持。 |

職責適配：付款合作、PRD／Wireframe與交付可對應支付生態規劃；定價和留存分析支持優化；工單週報與UAT支持流程協作。未推定已有銀行、政府或高頻交易核心平台經驗。

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 支付經驗與規格交付支持約談 |
| HR02 | supported | 企業端招募系統全模組與求職端公司頁 | 近期環境清楚，可轉移至平台產品 |
| HR03 | supported | 由我擬定取數的資料表與欄位 | 規劃與執行邊界具體 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 有流程改變，定義可面試確認 |
| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 兼顧資料與客戶登入風險 |
| HR06 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 責任演變有案例支持 |
| HR07 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 跨職能協作連結實際交付 |
| HR08 | supported | 曾設計定價實驗、規劃網頁付款 | 相關案例可找到，支付可前置 |
| HR09 | partial | 依目前掌握的情況 | 安全與留存口徑需核對來源 |
| HR10 | supported | 接下來，我希望將更多心力放回產品策略 | 方向與產品規劃相容 |
| HR11 | not_applicable | 錄取後三週可上班 | JD未列工作條件，無已知衝突 |
| HR12 | supported | 從需求釐清、系統分析到 PRD、原型、UAT 與上線計畫 | 足以面試，API深度留案例驗證 |
| HM01 | supported | 訂閱制 B2C App 與雙邊媒合平台 | 支付與會員經驗可轉移 |
| HM02 | supported | 客服反映配對名單「少又舊」 | 問題定位連結規則修改 |
| HM03 | supported | 改版排在新功能職缺健檢之前 | 進行中專案已有優先級判斷 |
| HM04 | supported | 依抽成、稅、手續費及撥款週期做實收試算 | 理解付款成本與商業選擇 |
| HM05 | supported | 為觀察差異，非因果 | 有衡量限制，算法需釐清 |
| HM06 | supported | 與資料科學團隊合作，定義使用情境與驗收標準 | 本人與協作者範圍清楚 |
| HM07 | supported | 第一階段於 2025/10 離峰切換上線 | 分期交付兼顧客戶風險 |
| HM08 | partial | API 串接規劃、舊系統資料盤點 | 需驗證串接規則及異常處理 |
| HM09 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 自主範圍足以支持本職缺 |
| HM10 | supported | 曾設計定價實驗、規劃網頁付款 | 主線可辨，支付案例可前置 |
| HM11 | supported | 依客服測試回饋調整推薦規則 | 有回饋修正，追問前後差異 |
| HM12 | supported | 規劃由 App 內購轉向網頁付款 | 串接案例值得深入驗證 |
| HM13 | not_applicable | 方法層：獨立依指定JD判讀 | 方法規則，不是候選人能力分數 |

HM13執行說明：本輪只對指定JD與履歷取證，未使用名氣、年資數量或語氣作能力代理；缺口分別歸入主要維度，不重複計分。

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「並與 CodaPay 新加坡技術團隊協調串接」對應支付合作。 |
| 2 | 「整理為 PRD 與 Axure Prototype」支持規格交付。 |
| 3 | 「選擇首次登入引導確認、不強迫修改」呈現取捨。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | API交易狀態與異常處理深度 | 請以CodaPay串接說明交易狀態、回呼失敗、重試與驗收責任。 |
| 2 | 留存年化算法與選樣限制 | 留存快照如何年化？群體如何選取，可能有哪些偏差？ |
| 3 | 安全事件觀測來源與覆蓋 | 未再出現冒用依據哪些事件來源，覆蓋範圍如何？ |

補充追問：
- 網頁付款占比變動中你的決策與行銷、工程貢獻如何區分？
- 定價實驗如何處理時間差、匯率及客群差異？
- 曾如何與銀行或政府合作？若未曾，如何理解串接限制？

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 尚凡付款段｜「並與 CodaPay 新加坡技術團隊協調串接」｜直接對應支付合作與跨團隊整合。
- 1111交付段｜「與 QA 制定 UAT 驗收案例、排定上線計畫」｜規格後的責任清楚，對應專案追蹤。
- 留存段｜「為觀察差異，非因果」｜限制明確，有助評估數據分析能力。

**可改進（4 點）**：

- 位置：付款串接段
- 原句：並與 CodaPay 新加坡技術團隊協調串接
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：尚未呈現API業務規則與失敗處理細節。不阻擋面試；需確認API理解達必備深度。
- 建議方向：補一個規則或異常流程的規劃與驗收例，不要求寫程式。

- 位置：留存分析段
- 原句：該群年化留存 81.2%，同期全站 74.2%
- 問題類型：measurement
- 嚴重度：interview_follow_up
- 影響：兩次快照如何年化、同群口徑與觀察偏差仍待確認。影響衡量可信範圍，不否定已呈現分析能力。
- 建議方向：說明年化公式、群體定義與非隨機選樣限制。

- 位置：登入安全段
- 原句：上線後至 2026/10 未再出現同類帳號冒用
- 問題類型：measurement
- 嚴重度：interview_follow_up
- 影響：目前掌握情況不等於完整安全監控。面試追問事件資料來源及覆蓋範圍。
- 建議方向：保留保守措辭，註明依客服回報或監測何種訊號。

- 位置：專業摘要
- 原句：曾設計定價實驗、規劃網頁付款
- 問題類型：readability
- 嚴重度：editorial
- 影響：支付證據分布於較早經歷，讀者需串接。只影響相關證據可見性，不改變能力判定。
- 建議方向：在摘要前置支付合作、點數及API規劃的現有證據。

**編輯附件**（不影響判斷）：可前置現有支付證據；自傳的使用者情境提供決策增量，不因篇幅扣分。

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠
交付與無直屬跨團隊協作有多例；優先級與定價支持方向判斷，組織資源配置未完整呈現，但JD未要求管理或P&L。

### 8. 未測試聲明
PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run
所有證據均為履歷自述，未做外部查證，不將安全口述當監測紀錄。

### 成果分類補表
| 位置／成果原句 | 分類 | 解讀限制 |
| :-- | :-- | :-- |
| 對接 16 個需求單位 | context | 協作範圍，不是影響成果 |
| 近 10 年 PM 經驗，經手 6 款產品 | context | 經驗背景，不直接推Level |
| 全站活躍付費廠商約 6.6 萬家 | context | 系統規模，非本人取得客戶 |
| 團隊 3 名企劃 | context | 不等於直屬管理人數 |
| 約 50 項大項功能上線 | output | 交付數，不等於使用者改善 |
| 另於 2026/01–06 上線 111 項 Roadmap 細項 | output | 細項口徑不同，不與大項相加 |
| 盤點出上千組重複 E-mail | output, context | 資料盤點及既有問題規模 |
| 選擇首次登入引導確認、不強迫修改 | decision | 有客戶中斷風險考量 |
| 停機約 1.5 小時 | output | 切換紀錄，無目標或基準不判成效 |
| 十多家廠商帳號遭冒用 | context | 事件觸發，非改善結果 |
| 上線簽章驗證 | output | 工程協作交付 |
| 上線後至 2026/10 未再出現同類帳號冒用 | outcome | 僅目前掌握，非完整監測證明 |
| 需求平均處理週期由 100.4 天降至 30.9 天 | outcome | 穩態期間比較，工單類別待核對 |
| 完成 1,726／1,857 張需求與問題單，約 93% | output | 處理完成率，不等於需求效益 |
| 每週發布處理週報 | output | 流程交付 |
| 兩案皆開發中 | decision, in_progress | 排序已發生，成果未實現 |
| 20 天內不重複推薦 | decision, output | 規則設計，無採用成效 |
| 需求管線觸及 1,279 家活躍付費廠商 | context | 選取群體，不當全站影響 |
| 該群年化留存 81.2%，同期全站 74.2% | outcome | 觀察差異，不宣稱因果 |
| AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才 | output | 功能交付，無品質成效數字 |
| 依客服測試回饋調整推薦規則 | decision, output | 有迭代，不推定結果提升 |
| 各期 21 天 | context | 定價觀察窗口 |
| 降價期 iOS 非續訂營收較基準期增 5% | outcome | 非隨機實驗仍有混淆 |
| Android 減 18%，相對變化約多 28% | outcome | 相對比較非增加28個百分點 |
| 還原原價後 iOS 較基準期減 65% | outcome | 時間比較未證明單因果 |
| 依結果全面調降售價 | decision | 決策，非調價後成效 |
| Peach 網頁付款占營收由 24% 至 80% 以上 | outcome | 通路組成，不等於總營收成長 |
| KOOL 訂閱與付費牆規劃上線 | output | 多平台交付 |
| 設定檔案完成、社群認證及照片門檻 | decision, output | 資格規則，無留存結果 |
| 主導 Juicy 上線 | output | 延續營收為目的 |
| 上線後 6 週男性 DAU 約 3,200 至 1.25 萬 | outcome | 團隊與行銷整體結果 |
| 7 個市場 | context | 在地化範圍 |
| 與最多約 10 位外國實習生協作 | context, output | 無直屬關係，不寫帶人 |
| 導入 CodaPay | output | 支付方式交付 |
| 提出 7／30／90 天訂閱方案與加贈內容 | decision, output | 實收試算支持方案，非已實現收入 |
| Newegg.com 商品資訊英翻中與英文校對 | output | 翻譯交付 |
| 12 條分支、23 個共用 skill | output | 協作流程產物，不代表效率提升 |
| 英文 TOEIC 980、TOEFL iBT 93 | context | 資格背景，非JD必要條件 |
| AWS Certified Cloud Practitioner（2023/12） | context | 證照，不替代API案例 |


## B-jd03｜揭盲：甲=K、乙=M；偏好=M

```json
{"job_id":"jd03","order":"甲=K/乙=M","differences":[{"what":"乙補出留存分析的取數分工與工具；甲呈現相同觀察結果。","hiring_meaning":"對數據觀測及會員留存要求，乙讓主管可追問資料表選擇、群組定義與年化方法；相同留存數值不構成成效差異，也不推定自行寫 SQL。","type":"measurement"},{"what":"乙新增配對問題的根因、競品實測與具體規則；甲僅概述依回饋調整推薦。","hiring_meaning":"對產品優化及競品分析，乙提供可驗證的診斷到規則設計案例，可追問排序依據、限制取捨與上線後成效；不將規則調整視為已證明成效。","type":"capability"},{"what":"乙說明帳號冒用涉及個資外洩風險；甲已有相同安全處置與結果。","hiring_meaning":"支付與會員平台面試更容易定位風險判斷的追問，但這是風險脈絡可見性，不能推論新增資安能力或銀行串接經驗。","type":"readability"}],"preference":"乙","reason":"乙的取數分工與配對規則案例，讓主管能具體驗證留存分析、競品研究與產品取捨。共同付款串接與文件經驗不分高下；銀行對接及高頻交易系統理解仍須面試確認。","evidence_甲":["比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。","與資料科學團隊合作，定義使用情境與驗收標準，依客服測試回饋調整推薦規則。","登入安全盤點源於 2026/04 十多家廠商帳號遭冒用。"],"evidence_乙":["由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。","客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。","登入安全盤點源於 2026/04 十多家廠商帳號遭冒用；求才端可存取大量求職者個資，冒用登入即有外洩風險。"]}
```

## 版本比較｜jd03｜順序 甲=K 乙=M｜model_id: unknown
- 偏好：乙（揭盲：M）
| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 乙補出留存分析的取數分工與工具；甲呈現相同觀察結果。 | 對數據觀測及會員留存要求，乙讓主管可追問資料表選擇、群組定義與年化方法；相同留存數值不構成成效差異，也不推定自行寫 SQL。 | measurement | 比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |
| 2 | 乙新增配對問題的根因、競品實測與具體規則；甲僅概述依回饋調整推薦。 | 對產品優化及競品分析，乙提供可驗證的診斷到規則設計案例，可追問排序依據、限制取捨與上線後成效；不將規則調整視為已證明成效。 | capability | 與資料科學團隊合作，定義使用情境與驗收標準，依客服測試回饋調整推薦規則。 | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 |
| 3 | 乙說明帳號冒用涉及個資外洩風險；甲已有相同安全處置與結果。 | 支付與會員平台面試更容易定位風險判斷的追問，但這是風險脈絡可見性，不能推論新增資安能力或銀行串接經驗。 | readability | 登入安全盤點源於 2026/04 十多家廠商帳號遭冒用。 | 登入安全盤點源於 2026/04 十多家廠商帳號遭冒用；求才端可存取大量求職者個資，冒用登入即有外洩風險。 |
- 理由（≤120 字）：乙的取數分工與配對規則案例，讓主管能具體驗證留存分析、競品研究與產品取捨。共同付款串接與文件經驗不分高下；銀行對接及高頻交易系統理解仍須面試確認。

兩份履歷共同呈現 PRD、User Story、Wireframe、UAT、CodaPay 技術協調與訂閱點數規劃，足以形成基本面試切入點，未因乙重述或增加數字而提高能力評價。甲自傳已有溝通整合優先級案例，乙移入經歷不另算能力差異；新增英文情境與 AI 工具規模不作本職缺決勝依據。以上僅依指定文本比較，未宣稱外部核實事實快照。


# jd09｜逐次輸出


## A-jd09-K｜履歷K

```json
{"rubric_version": "4.2", "resume_id": "K", "job_id": "jd09", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd09-K", "human_calibrated": false, "requirements": [{"id": "R01", "text": "3年以上軟體產品或專案管理經驗", "type": "required", "status": "supported", "evidence": ["近 10 年 PM 經驗"], "blocks_interview": false, "reason": "職涯時間及多項軟體交付支持。"}, {"id": "R02", "text": "B2B SaaS經驗尤佳", "type": "preferred", "status": "partial", "evidence": ["企業端招募系統全模組與求職端公司頁"], "blocks_interview": false, "reason": "企業產品相關；未明示SaaS服務模式。"}, {"id": "R03", "text": "熟悉UI/UX概念方法論", "type": "required", "status": "supported", "evidence": ["以 Use Case、Wireframe 定義業務流程與畫面"], "blocks_interview": false, "reason": "有原型及登入流程取捨案例。"}, {"id": "R04", "text": "批判性思維", "type": "required", "status": "supported", "evidence": ["選擇首次登入引導確認、不強迫修改"], "blocks_interview": false, "reason": "依既有使用風險調整方案。"}, {"id": "R05", "text": "數據驅動思維", "type": "required", "status": "supported", "evidence": ["以 Android 售價不變作對照"], "blocks_interview": false, "reason": "實驗及觀察資料均有使用，因果限制另追問。"}, {"id": "R06", "text": "獨立作業善跨部門溝通", "type": "required", "status": "supported", "evidence": ["由我主責規劃，與工程團隊密切協作"], "blocks_interview": false, "reason": "有本人責任及QA、客服、資料科學協作。"}, {"id": "R07", "text": "需求搜集、客服業務合作、市場競品與需求訪談", "type": "required", "status": "partial", "evidence": ["依使用者旅程與工單問題排定優先級"], "blocks_interview": false, "reason": "客服訊號直接；市場競品與主導訪談僅技能線索。"}, {"id": "R08", "text": "產品路線規劃、創新方案、優先序與PRD", "type": "required", "status": "supported", "evidence": ["將信件與即時通整合排在其他新功能之前"], "blocks_interview": false, "reason": "有優先級理由及PRD交付；整合仍開發中。"}, {"id": "R09", "text": "規格討論、進度追蹤與測試驗收", "type": "required", "status": "supported", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "blocks_interview": false, "reason": "完整規格到驗收鏈條。"}, {"id": "R10", "text": "說明文件、使用分析與迭代建議", "type": "required", "status": "supported", "evidence": ["依客服測試回饋調整推薦規則"], "blocks_interview": false, "reason": "有客服說明、規則調整及流程分析。"}], "dimensions": [{"id": "positioning", "rating": "強", "evidence": ["現任 1111 招募系統 Product Owner"], "missing": ["MarTech領域未直接呈現，可於面試了解轉移方式。"], "issue_ids": []}, {"id": "role_evidence", "rating": "足夠", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "missing": ["主導訪談、競品到路線圖的實例待補。"], "issue_ids": ["I01"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": ["優先級與風險有直接證據；資源配置權限可追問。"], "issue_ids": []}, {"id": "outcome_quality", "rating": "足夠", "evidence": ["為觀察差異，非因果"], "missing": ["實驗時間混淆、留存年化算法及安全監測來源待核對。"], "issue_ids": ["I02", "I03"]}, {"id": "ownership", "rating": "強", "evidence": ["由我主責規劃，與工程團隊密切協作"], "missing": ["功能規劃與工程交付邊界清楚；方向決策權可追問。"], "issue_ids": []}, {"id": "readability", "rating": "足夠", "evidence": ["正式職稱產品企劃主任"], "missing": ["主線清楚；大項與細項計數關係可加註。"], "issue_ids": ["I04"]}], "results": [{"quote": "約 50 項大項功能上線", "kinds": ["output"]}, {"quote": "需求平均處理週期由 100.4 天降至 30.9 天", "kinds": ["outcome"]}, {"quote": "該群年化留存 81.2%，同期全站 74.2%", "kinds": ["outcome"]}, {"quote": "選擇首次登入引導確認、不強迫修改", "kinds": ["decision"]}, {"quote": "Peach 網頁付款占營收由 24% 至 80% 以上", "kinds": ["outcome"]}, {"quote": "目前專案仍在開發中", "kinds": ["in_progress"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["近 10 年 PM 經驗"], "application_note": "交付與企業產品經驗支持面試"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "客群相關，需了解MarTech轉移"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "application_note": "本人規劃與協作範圍明確"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "有可比較流程結果，口徑待核"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "能權衡資料與既有客戶風險"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["從交友與訂閱制 App 到企業招募系統"], "application_note": "產品類型及責任脈絡可辨"}, {"rule_id": "HR07", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則"], "application_note": "有實際跨團隊迭代證據"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["正式職稱產品企劃主任"], "application_note": "職稱與實際產品範圍可理解"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["依目前掌握的情況"], "application_note": "安全成效須核對觀測來源"}, {"rule_id": "HR10", "status": "supported", "resume_evidence": ["我希望將更多心力放回產品策略"], "application_note": "方向與路線規劃相容"}, {"rule_id": "HR11", "status": "not_applicable", "resume_evidence": ["錄取後三週可上班"], "application_note": "JD未列地點語言到職硬條件"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "application_note": "足以面試，補核需求探索與衡量"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "evidence_type": "context", "source_ids": [], "interview_question": "如何將企業招募經驗轉移到CDP、MA與BI產品？"}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["廠商抱怨工單中，最大宗是溝通管道中斷"], "evidence_type": "decision", "source_ids": [], "interview_question": "如何由工單追溯問題，並以訪談驗證？"}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["將信件與即時通整合排在其他新功能之前"], "evidence_type": "decision", "source_ids": [], "interview_question": "當時比較哪些方案與資源限制？"}, {"rule_id": "HM04", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "evidence_type": "decision", "source_ids": [], "interview_question": "如何把商業判斷用於B2B產品路線？"}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "partial", "resume_evidence": ["為觀察差異，非因果"], "evidence_type": "outcome", "source_ids": [], "interview_question": "留存年化公式、分母及選樣差異是什麼？"}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["與資料科學團隊合作，定義使用情境與驗收標準"], "evidence_type": "output", "source_ids": [], "interview_question": "需求方與工程意見衝突時如何決策？"}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["以 Use Case、Wireframe 定義業務流程與畫面"], "evidence_type": "output", "source_ids": [], "interview_question": "選擇登入方案時討論過哪些技術限制？"}, {"rule_id": "HM09", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "evidence_type": "output", "source_ids": [], "interview_question": "哪些路線決策可獨立決定，哪些須核准？"}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["正式職稱產品企劃主任"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則"], "evidence_type": "decision", "source_ids": [], "interview_question": "哪個回饋使規則改變，後續如何驗證？"}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "evidence_type": "decision", "source_ids": [], "interview_question": "請以去識別化PRD說明需求到驗收完整案例。"}, {"rule_id": "HM13", "primary_dimension": "", "status": "supported", "resume_evidence": [], "evidence_type": null, "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HR07", "source_ids": [], "application_note": "核對需求探索深度", "context_limit": "技能列示不等同已主導案例", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "使用者訪談與問卷、競品實測", "reason": "JD要求需求訪談與市場競品分析，尚未見如何改變產品選擇；可面試核對而非否定能力。", "suggestion": "補一例訪談或競品訊號如何改變PRD或優先級。"}, {"id": "I02", "rule_id": "HM05", "source_ids": [], "application_note": "核對衡量與因果限制", "context_limit": "相對比較有用但不等同因果識別", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "該群年化留存 81.2%，同期全站 74.2%", "reason": "年化方法與群體差異未展開；定價實驗亦需核對時間及平台混淆，不阻擋面試。", "suggestion": "說明留存算法、母體與選樣，定價實驗同期活動及續訂排除方式。"}, {"id": "I03", "rule_id": "HR09", "source_ids": [], "application_note": "核對安全結果觀測來源", "context_limit": "履歷已限縮為目前掌握情況", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "上線後至 2026/10 未再出現同類帳號冒用", "reason": "未提供監測或通報來源，不能認定安全問題已消除；面試追問觀察涵蓋範圍。", "suggestion": "標示觀測來源及盲區，保留自述限制。"}, {"id": "I04", "rule_id": "HR08", "source_ids": [], "application_note": "讓交付範圍更易讀", "context_limit": "不是互相矛盾的證據", "category": "readability", "severity": "editorial", "block_target": null, "claim": "另於 2026/01–06 上線 111 項 Roadmap 細項", "reason": "與50項大項時間重疊且粒度不同，讀者需自行辨認；不影響面試判斷。", "suggestion": "補註兩種計數是否包含及用途，不相加。"}], "decision": {"recommendation": "interview", "evidence": ["近 10 年 PM 經驗", "選擇首次登入引導確認、不強迫修改", "與 QA 制定 UAT 驗收案例、排定上線計畫"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["「近 10 年 PM 經驗」及企業產品經驗直接相關。", "「選擇首次登入引導確認、不強迫修改」呈現風險取捨。", "「與 QA 制定 UAT 驗收案例、排定上線計畫」支持交付。"], "key_gaps": ["主導需求訪談及競品分析的決策案例。", "留存年化、實驗比較及安全觀測的口徑。", "B2B SaaS模式與MarTech轉移、方向資源權限。"], "strengths": ["企業端產品範圍與本人規劃責任清楚。", "登入改版有選項、風險與採取方案。", "量測提供期間、比較基準並主動限制因果。"], "interview_questions": ["請以需求訪談或競品實測案例說明如何改變產品規劃。", "企業招募系統的交付與收費模式為何，如何轉移至MarTech？", "登入改版有哪些替代方案、風險與核准角色？", "留存年化公式、群體母體與選樣差異為何？", "定價各階段如何排除同期活動及平台用戶差異？", "帳號冒用觀測來自監測、通報或客服？有何盲區？", "請以去識別化PRD展示規格、優先級與驗收。", "路線與資源配置哪些由你決定、哪些需上級批准？"], "editorial_appendix": ["50項大項與111項細項宜加計數關係註解，不相加。"], "spectrum": {"level": 8, "uncertainty_levels": 1, "basis": "多個相關案例有清楚取捨、比較基準與限制，支持面試；需求探索及MarTech適配仍待核實。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷 K｜第 1 輪｜model_id: unknown

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「選擇首次登入引導確認、不強迫修改」呈現取捨，企業產品與交付足以支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 現任 1111 招募系統 Product Owner | MarTech領域未直接呈現，可於面試了解轉移方式。 |
| role_evidence | 足夠 | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 主導訪談、競品到路線圖的實例待補。 |
| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 優先級與風險有直接證據；資源配置權限可追問。 |
| outcome_quality | 足夠 | 為觀察差異，非因果 | 實驗時間混淆、留存年化算法及安全監測來源待核對。 |
| ownership | 強 | 由我主責規劃，與工程團隊密切協作 | 功能規劃與工程交付邊界清楚；方向決策權可追問。 |
| readability | 足夠 | 正式職稱產品企劃主任 | 主線清楚；大項與細項計數關係可加註。 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 3年以上軟體產品或專案管理經驗 | 必要 | supported | 近 10 年 PM 經驗 | 職涯時間及多項軟體交付支持。 |
| B2B SaaS經驗尤佳 | 加分 | partial | 企業端招募系統全模組與求職端公司頁 | 企業產品相關；未明示SaaS服務模式。 |
| 熟悉UI/UX概念方法論 | 必要 | supported | 以 Use Case、Wireframe 定義業務流程與畫面 | 有原型及登入流程取捨案例。 |
| 批判性思維 | 必要 | supported | 選擇首次登入引導確認、不強迫修改 | 依既有使用風險調整方案。 |
| 數據驅動思維 | 必要 | supported | 以 Android 售價不變作對照 | 實驗及觀察資料均有使用，因果限制另追問。 |
| 獨立作業善跨部門溝通 | 必要 | supported | 由我主責規劃，與工程團隊密切協作 | 有本人責任及QA、客服、資料科學協作。 |
| 需求搜集、客服業務合作、市場競品與需求訪談 | 必要 | partial | 依使用者旅程與工單問題排定優先級 | 客服訊號直接；市場競品與主導訪談僅技能線索。 |
| 產品路線規劃、創新方案、優先序與PRD | 必要 | supported | 將信件與即時通整合排在其他新功能之前 | 有優先級理由及PRD交付；整合仍開發中。 |
| 規格討論、進度追蹤與測試驗收 | 必要 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 完整規格到驗收鏈條。 |
| 說明文件、使用分析與迭代建議 | 必要 | supported | 依客服測試回饋調整推薦規則 | 有客服說明、規則調整及流程分析。 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗 | 交付與企業產品經驗支持面試 |
| HR02 | supported | 企業端招募系統全模組與求職端公司頁 | 客群相關，需了解MarTech轉移 |
| HR03 | supported | 由我主責規劃，與工程團隊密切協作 | 本人規劃與協作範圍明確 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 有可比較流程結果，口徑待核 |
| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 能權衡資料與既有客戶風險 |
| HR06 | supported | 從交友與訂閱制 App 到企業招募系統 | 產品類型及責任脈絡可辨 |
| HR07 | supported | 依客服測試回饋調整推薦規則 | 有實際跨團隊迭代證據 |
| HR08 | supported | 正式職稱產品企劃主任 | 職稱與實際產品範圍可理解 |
| HR09 | partial | 依目前掌握的情況 | 安全成效須核對觀測來源 |
| HR10 | supported | 我希望將更多心力放回產品策略 | 方向與路線規劃相容 |
| HR11 | not_applicable | 錄取後三週可上班 | JD未列地點語言到職硬條件 |
| HR12 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 足以面試，補核需求探索與衡量 |
| HM01 | supported | 企業端招募系統全模組與求職端公司頁 | 企業產品可轉移，領域需核對 |
| HM02 | supported | 廠商抱怨工單中，最大宗是溝通管道中斷 | 工單具體，主導訪談仍待補 |
| HM03 | supported | 將信件與即時通整合排在其他新功能之前 | 有取捨，整合未完成 |
| HM04 | supported | 依抽成、稅、手續費及撥款週期做實收試算 | 商業分析相關，需轉移B2B |
| HM05 | partial | 為觀察差異，非因果 | 核對算法與比較限制 |
| HM06 | supported | 與資料科學團隊合作，定義使用情境與驗收標準 | 本人與團隊分工清楚 |
| HM07 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 規格驗收到上線鏈條完整 |
| HM08 | supported | 以 Use Case、Wireframe 定義業務流程與畫面 | 業務規則與工程協作有證據 |
| HM09 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 自主範圍可約談確認 |
| HM10 | supported | 正式職稱產品企劃主任 | 職責及脈絡容易理解 |
| HM11 | supported | 依客服測試回饋調整推薦規則 | 回饋確實改變推薦規則 |
| HM12 | supported | 選擇首次登入引導確認、不強迫修改 | 案例足夠，作品尚未查核 |
| HM13 | supported | —（評估方法，非履歷能力） | 依本JD獨立審查，無真人校準 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「近 10 年 PM 經驗」及企業產品經驗直接相關。 |
| 2 | 「選擇首次登入引導確認、不強迫修改」呈現風險取捨。 |
| 3 | 「與 QA 制定 UAT 驗收案例、排定上線計畫」支持交付。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 主導需求訪談及競品分析的決策案例。 | 訪談或競品訊號如何改變優先級？ |
| 2 | 留存年化、實驗比較及安全觀測的口徑。 | 年化公式、實驗同期差異及安全觀測來源？ |
| 3 | B2B SaaS模式與MarTech轉移、方向資源權限。 | SaaS服務模式與路線資源決策權為何？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
1. 1111交付｜「由我主責規劃，與工程團隊密切協作」｜辨識本人規劃責任，符合跨部門交付需求。
2. 改版／自傳｜「選擇首次登入引導確認、不強迫修改」｜風險與方案連結清楚，支持批判性思維。
3. 留存比較｜「為觀察差異，非因果」｜明示衡量限制，支持數據思維而不誇大效果。

**可改進（4 點）**：

- 位置：專業技能／研究與數據
- 原句：使用者訪談與問卷、競品實測
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：JD要求需求訪談與市場競品分析，尚未見如何改變產品選擇；可面試核對而非否定能力。
- 建議方向：補一例訪談或競品訊號如何改變PRD或優先級。

- 位置：1111留存與尚凡定價實驗
- 原句：該群年化留存 81.2%，同期全站 74.2%
- 問題類型：measurement
- 嚴重度：interview_follow_up
- 影響：年化方法與群體差異未展開；定價實驗亦需核對時間及平台混淆，不阻擋面試。
- 建議方向：說明留存算法、母體與選樣，定價實驗同期活動及續訂排除方式。

- 位置：1111登入安全
- 原句：上線後至 2026/10 未再出現同類帳號冒用
- 問題類型：measurement
- 嚴重度：interview_follow_up
- 影響：未提供監測或通報來源，不能認定安全問題已消除；面試追問觀察涵蓋範圍。
- 建議方向：標示觀測來源及盲區，保留自述限制。

- 位置：1111交付統計
- 原句：另於 2026/01–06 上線 111 項 Roadmap 細項
- 問題類型：readability
- 嚴重度：editorial
- 影響：與50項大項時間重疊且粒度不同，讀者需自行辨認；不影響面試判斷。
- 建議方向：補註兩種計數是否包含及用途，不相加。

**編輯附件**（語氣、用詞微調；不影響判斷）：
- 保留目前角色邊界與非因果限定語；大項、細項註明關係即可。

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

本審查僅依提供文字，無外部查證。結構驗證另由指定validator執行，不代表招聘效度、ATS或事實驗證。

### 成果分類補表
| 原句／成果 | 分類 | 限制 |
| :-- | :-- | :-- |
| 對接 16 個需求單位 | context | 需求協作範圍，非管理人數 |
| 經手 6 款產品 | context | 產品經歷範圍 |
| 全站活躍付費廠商約 6.6 萬家 | context | 系統規模非個人成果 |
| 約 50 項大項功能上線 | output | 規劃與工程協作交付 |
| 上線 111 項 Roadmap 細項 | output | 不同粒度期間，不與50項相加 |
| 盤點出上千組重複 E-mail | output / context | 資料盤點及風險背景 |
| 選擇首次登入引導確認、不強迫修改 | decision | 保護既有登入流程 |
| 第一階段於 2025/10 離峰切換上線 | output | 停機約1.5小時是交付觀測 |
| 十多家廠商帳號遭冒用 | context | 問題規模 |
| 於 2026/04/17 上線簽章驗證 | output | 與工程協作 |
| 未再出現同類帳號冒用 | outcome | 目前掌握情況，非全面監測證明 |
| 需求平均處理週期由 100.4 天降至 30.9 天 | outcome | Q1至Q2穩態比較；案件組成需核 |
| 完成 1,726／1,857 張需求與問題單 | output | 截至09/29約93%，非客戶價值本身 |
| 需求管線觸及 1,279 家活躍付費廠商 | context | 約1.9%服務母體 |
| 該群年化留存 81.2%，同期全站 74.2% | outcome | 觀察差異非因果 |
| AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才 | output | 未提供採用成效 |
| 依客服測試回饋調整推薦規則 | decision / output | 有修正，未提供成效 |
| 降價期 iOS 非續訂營收較基準期增 5% | outcome | Android減18%，時間平台混淆待核 |
| 還原原價後 iOS 較基準期減 65% | outcome | 非隨機實驗 |
| 依結果全面調降售價 | decision | 不等同後續營收已驗證 |
| Peach 網頁付款占營收由 24% 至 80% 以上 | outcome | 支付占比，非總營收或利潤成長 |
| KOOL 訂閱與付費牆規劃上線 | output | 跨平台交付，未報使用效果 |
| 才開放精選網紅資格 | decision | 資格門檻產品規則 |
| 主導 Juicy 上線 | output | 延續營收為目的 |
| 男性 DAU 約 3,200 至 1.25 萬 | outcome | 產品與行銷整體表現 |
| SweetRing 在地化涵蓋 | output / context | 7市場，協作最多10人非直屬管理 |
| 導入 CodaPay | output | 支付通道交付 |
| 提出 7／30／90 天訂閱方案與加贈內容 | decision / output | 實收試算支持，未報結果 |
| Newegg.com 商品資訊英翻中與校對 | output | 歷史工作產出 |
| 將信件與即時通整合排在其他新功能之前 | decision / in_progress | 已發生優先級決策，專案仍開發 |


## A-jd09-M｜履歷M

```json
{"rubric_version": "4.2", "resume_id": "M", "job_id": "jd09", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd09-M", "human_calibrated": false, "requirements": [{"id": "R01", "text": "3年以上軟體產品或專案管理經驗", "type": "required", "status": "supported", "evidence": ["近 10 年 PM 經驗，經手 6 款產品"], "blocks_interview": false, "reason": "任職時序與多個軟體產品案例相互支持。"}, {"id": "R02", "text": "B2B SaaS經驗", "type": "preferred", "status": "partial", "evidence": ["企業端招募系統全模組與求職端公司頁"], "blocks_interview": false, "reason": "企業端產品直接相關，但SaaS服務及商業模式細節未呈現。"}, {"id": "R03", "text": "熟悉UI/UX概念方法論", "type": "required", "status": "supported", "evidence": ["以 Use Case、Wireframe 定義業務流程與畫面"], "blocks_interview": false, "reason": "原型與流程設計有實際用途。"}, {"id": "R04", "text": "批判性思維", "type": "required", "status": "supported", "evidence": ["查出根因是名單依履歷修改日排序"], "blocks_interview": false, "reason": "由問題追根因後調整規則。"}, {"id": "R05", "text": "數據驅動思維", "type": "required", "status": "supported", "evidence": ["為觀察差異，非因果"], "blocks_interview": false, "reason": "有取數、比較、定價實驗及限制辨識。"}, {"id": "R06", "text": "獨立作業且善跨部門溝通", "type": "required", "status": "supported", "evidence": ["由我主責規劃，與工程團隊密切協作"], "blocks_interview": false, "reason": "具自主規劃、QA及客服協作案例。"}, {"id": "R07", "text": "需求搜集、客服業務合作、競品市場分析及主導訪談", "type": "required", "status": "partial", "evidence": ["實測主要競品反推規則後"], "blocks_interview": false, "reason": "客服與競品證據具體；主導訪談與市場趨勢分析僅有線索。"}, {"id": "R08", "text": "路線規劃、方案、跨部門優先序與PRD", "type": "required", "status": "supported", "evidence": ["信件與即時通整合排在其他新功能之前"], "blocks_interview": false, "reason": "有選擇依據與規格產出；中長期路線可面試追問。"}, {"id": "R09", "text": "功能規格、進度控管、測試驗收", "type": "required", "status": "supported", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "blocks_interview": false, "reason": "具完整交付流程與風險分階段處理。"}, {"id": "R10", "text": "說明文件、使用分析及迭代優化", "type": "required", "status": "partial", "evidence": ["依客服測試回饋調整推薦規則"], "blocks_interview": false, "reason": "回饋迭代與客服說明明確，使用漏斗及對外文件細節待核對。"}], "dimensions": [{"id": "positioning", "rating": "強", "evidence": ["現任 1111 招募系統 Product Owner"], "missing": ["MarTech領域可轉移性於面試確認。"], "issue_ids": []}, {"id": "role_evidence", "rating": "足夠", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "missing": ["主導需求訪談及市場趨勢分析待補。"], "issue_ids": ["I01"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": ["可追問中長期路線圖與資源配置。"], "issue_ids": ["I03"]}, {"id": "outcome_quality", "rating": "足夠", "evidence": ["為觀察差異，非因果"], "missing": ["留存年化算法、處理週期母體與安全觀察來源需核對。"], "issue_ids": ["I02"]}, {"id": "ownership", "rating": "強", "evidence": ["由我主責規劃，與工程團隊密切協作"], "missing": ["策略權責及資源決定邊界可追問。"], "issue_ids": []}, {"id": "readability", "rating": "足夠", "evidence": ["兩案皆開發中"], "missing": ["代表案例可優先聚焦企業產品與需求分析。"], "issue_ids": []}], "results": [{"quote": "約 50 項大項功能上線", "kinds": ["output"]}, {"quote": "需求平均處理週期由 100.4 天降至 30.9 天", "kinds": ["outcome"]}, {"quote": "兩案皆開發中", "kinds": ["decision", "in_progress"]}, {"quote": "該群年化留存 81.2%，同期全站 74.2%", "kinds": ["outcome"]}, {"quote": "相對變化約多 28%", "kinds": ["outcome"]}, {"quote": "Peach 網頁付款占營收由 24% 至 80% 以上", "kinds": ["outcome"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "application_note": "產品規劃交付直接相關"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "企業端流程可轉移"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "application_note": "個人規劃與工程分工清楚"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "有流程結果但需核對口徑"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "能處理既有客戶限制"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["從交友與訂閱制 App 到企業招募系統"], "application_note": "跨產品方向演進清楚"}, {"rule_id": "HR07", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "application_note": "技能有交付案例支持"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["兩案皆開發中"], "application_note": "完成與進行中可分辨"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["為觀察差異，非因果"], "application_note": "數字口徑留面試查核"}, {"rule_id": "HR10", "status": "supported", "resume_evidence": ["我希望將更多心力放回產品策略"], "application_note": "與路線規劃方向相容"}, {"rule_id": "HR11", "status": "unknown", "resume_evidence": ["錄取後三週可上班"], "application_note": "JD未列地點或到職限制"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["信件與即時通整合排在其他新功能之前"], "application_note": "足以面試驗證需求與策略能力"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "evidence_type": "context", "source_ids": [], "interview_question": "企業產品經驗如何轉用到CDP與行銷自動化？"}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["客服反映配對名單「少又舊」"], "evidence_type": "decision", "source_ids": [], "interview_question": "請示範一次由你主導的訪談如何改變需求。"}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "evidence_type": "decision", "source_ids": [], "interview_question": "如何比較強制修改與引導確認的風險？"}, {"rule_id": "HM04", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "evidence_type": "decision", "source_ids": [], "interview_question": "企業產品的商業目標如何進入路線規劃？"}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "partial", "resume_evidence": ["為觀察差異，非因果"], "evidence_type": "outcome", "source_ids": [], "interview_question": "留存年化公式、期間與比較群如何定義？"}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "evidence_type": "output", "source_ids": [], "interview_question": "請說明一次優先序分歧及最後決策者。"}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "evidence_type": "output", "source_ids": [], "interview_question": "如何訂驗收門檻與處理未達標項目？"}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["改依職缺上線日排序、20 天內不重複推薦"], "evidence_type": "decision", "source_ids": [], "interview_question": "規則如何拆成規格與驗收案例？"}, {"rule_id": "HM09", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "evidence_type": "output", "source_ids": [], "interview_question": "路線圖與資源預算由你決定到哪一層？"}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["兩案皆開發中"], "evidence_type": "in_progress", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則"], "evidence_type": "decision", "source_ids": [], "interview_question": "何種回饋推翻最初假設？"}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["以 Use Case、Wireframe 定義業務流程與畫面"], "evidence_type": "output", "source_ids": [], "interview_question": "可否用去識別PRD演示需求到驗收？"}, {"rule_id": "HM13", "primary_dimension": "method", "status": "not_applicable", "resume_evidence": [], "evidence_type": null, "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HR01", "source_ids": [], "application_note": "面試追問，不阻擋邀約", "context_limit": "僅據履歷文字，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "使用者訪談與問卷", "reason": "JD要求主導訪談與分析市場；技能列舉不足呈現執行品質，但不構成不符。", "suggestion": "補一個訪談對象、問題與如何改變方案的真實案例，市場趨勢亦同。"}, {"id": "I02", "rule_id": "HM05", "source_ids": [], "application_note": "面試追問，不阻擋邀約", "context_limit": "僅據履歷文字，未外部查證", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "該群年化留存 81.2%，同期全站 74.2%", "reason": "已有期間與非因果限制，年化算法及兩群可比性仍待面試確認。", "suggestion": "說明年化公式、觀察窗、樣本定義；另核對週期及安全觀察來源。"}, {"id": "I03", "rule_id": "HM03", "source_ids": [], "application_note": "面試追問，不阻擋邀約", "context_limit": "僅據履歷文字，未外部查證", "category": "ownership", "severity": "interview_follow_up", "block_target": null, "claim": "信件與即時通整合排在其他新功能之前", "reason": "優先序有依據，但中長期路線及資源決策權限尚不完整，留作策略深度追問。", "suggestion": "以一個路線圖案例交代目標、替代選項、資源限制與核定者。"}], "decision": {"recommendation": "interview", "evidence": ["選擇首次登入引導確認、不強迫修改", "與 QA 制定 UAT 驗收案例、排定上線計畫"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["「企業端招募系統全模組與求職端公司頁」支持企業工具經驗。", "「選擇首次登入引導確認、不強迫修改」支持用戶限制下的判斷。", "「與 QA 制定 UAT 驗收案例、排定上線計畫」支持交付能力。"], "key_gaps": ["主導訪談與市場趨勢研究的具體案例", "年化留存與流程結果的量測口徑", "中長期路線及資源決策邊界"], "strengths": ["企業端經驗｜「企業端招募系統全模組與求職端公司頁」｜可轉移到B2B工具的流程與需求管理。", "取捨案例｜「選擇首次登入引導確認、不強迫修改」｜把既有客戶限制轉為方案選擇。", "交付分工｜「與 QA 制定 UAT 驗收案例、排定上線計畫」｜直接支持JD規格、驗收與時程責任。"], "interview_questions": ["請展示一次主導需求訪談及其改變的產品決策。", "如何分析市場趨勢並轉為MarTech產品機會？", "請用一份去識別路線圖說明目標、優先序、資源與核定權責。", "年化留存如何計算，樣本選擇與比較限制是什麼？", "處理週期母體與起訖定義為何，是否含未完成單？", "未再發生帳號冒用的觀察來源與涵蓋範圍為何？", "如何從功能使用數據推動迭代，並撰寫客戶說明？"], "editorial_appendix": ["可將企業需求、競品研究與迭代案例排在變現案例之前；僅為可讀性調整。"], "spectrum": {"level": 8, "uncertainty_levels": 1, "basis": "多個相關企業產品案例、清楚取捨、比較數據與限制足以面試；MarTech專門經驗非明文必要，訪談及策略權責待核對。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷 M｜第 1 輪｜model_id: unknown

### 1. 結論

- 招聘決定：interview

- Level：8（±1）

- 一句話理由：「選擇首次登入引導確認、不強迫修改」呈現取捨，企業產品交付與數據案例足以面試。

### 2. 六維度

| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 現任 1111 招募系統 Product Owner | MarTech領域可轉移性於面試確認。 |
| role_evidence | 足夠 | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 主導需求訪談及市場趨勢分析待補。 |
| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 可追問中長期路線圖與資源配置。 |
| outcome_quality | 足夠 | 為觀察差異，非因果 | 留存年化算法、處理週期母體與安全觀察來源需核對。 |
| ownership | 強 | 由我主責規劃，與工程團隊密切協作 | 策略權責及資源決定邊界可追問。 |
| readability | 足夠 | 兩案皆開發中 | 代表案例可優先聚焦企業產品與需求分析。 |

### 3. JD 條件對照

下列工作內容按職責對照，非額外資格門檻。未有明文必要條件的反證。

| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 3年以上軟體產品或專案管理經驗 | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 任職時序與多個軟體產品案例相互支持。 |
| B2B SaaS經驗 | 加分 | partial | 企業端招募系統全模組與求職端公司頁 | 企業端產品直接相關，但SaaS服務及商業模式細節未呈現。 |
| 熟悉UI/UX概念方法論 | 必要 | supported | 以 Use Case、Wireframe 定義業務流程與畫面 | 原型與流程設計有實際用途。 |
| 批判性思維 | 必要 | supported | 查出根因是名單依履歷修改日排序 | 由問題追根因後調整規則。 |
| 數據驅動思維 | 必要 | supported | 為觀察差異，非因果 | 有取數、比較、定價實驗及限制辨識。 |
| 獨立作業且善跨部門溝通 | 必要 | supported | 由我主責規劃，與工程團隊密切協作 | 具自主規劃、QA及客服協作案例。 |
| 需求搜集、客服業務合作、競品市場分析及主導訪談 | 必要 | partial | 實測主要競品反推規則後 | 客服與競品證據具體；主導訪談與市場趨勢分析僅有線索。 |
| 路線規劃、方案、跨部門優先序與PRD | 必要 | supported | 信件與即時通整合排在其他新功能之前 | 有選擇依據與規格產出；中長期路線可面試追問。 |
| 功能規格、進度控管、測試驗收 | 必要 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 具完整交付流程與風險分階段處理。 |
| 說明文件、使用分析及迭代優化 | 必要 | partial | 依客服測試回饋調整推薦規則 | 回饋迭代與客服說明明確，使用漏斗及對外文件細節待核對。 |

### 4. HR 十二問 ／ HM 十三問

| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 產品規劃交付直接相關 |
| HR02 | supported | 企業端招募系統全模組與求職端公司頁 | 企業端流程可轉移 |
| HR03 | supported | 由我主責規劃，與工程團隊密切協作 | 個人規劃與工程分工清楚 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 有流程結果但需核對口徑 |
| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 能處理既有客戶限制 |
| HR06 | supported | 從交友與訂閱制 App 到企業招募系統 | 跨產品方向演進清楚 |
| HR07 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 技能有交付案例支持 |
| HR08 | supported | 兩案皆開發中 | 完成與進行中可分辨 |
| HR09 | partial | 為觀察差異，非因果 | 數字口徑留面試查核 |
| HR10 | supported | 我希望將更多心力放回產品策略 | 與路線規劃方向相容 |
| HR11 | unknown | 錄取後三週可上班 | JD未列地點或到職限制 |
| HR12 | supported | 信件與即時通整合排在其他新功能之前 | 足以面試驗證需求與策略能力 |
| HM01 | supported | 企業端招募系統全模組與求職端公司頁 | 企業工具經驗可轉移 |
| HM02 | supported | 客服反映配對名單「少又舊」 | 客服問題分析具體，訪談待核對 |
| HM03 | supported | 選擇首次登入引導確認、不強迫修改 | 有明確替代方案與限制 |
| HM04 | supported | 依抽成、稅、手續費及撥款週期做實收試算 | 有定價與成本選擇證據 |
| HM05 | partial | 為觀察差異，非因果 | 量測口徑需追問 |
| HM06 | supported | 由我主責規劃，與工程團隊密切協作 | 本人與工程分工清楚 |
| HM07 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 具分階段交付與風險管理 |
| HM08 | supported | 改依職缺上線日排序、20 天內不重複推薦 | 業務規則可連到技術驗收 |
| HM09 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 符合自主產品負責範圍 |
| HM10 | supported | 兩案皆開發中 | 狀態與角色可辨識 |
| HM11 | supported | 依客服測試回饋調整推薦規則 | 客服回饋能改變規則 |
| HM12 | supported | 以 Use Case、Wireframe 定義業務流程與畫面 | 可用PRD工作樣本核對 |
| HM13 | not_applicable | — | 方法層不作候選人能力加分 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）

| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「企業端招募系統全模組與求職端公司頁」支持企業工具經驗。 |
| 2 | 「選擇首次登入引導確認、不強迫修改」支持用戶限制下的判斷。 |
| 3 | 「與 QA 制定 UAT 驗收案例、排定上線計畫」支持交付能力。 |



| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 主導訪談與市場趨勢研究的具體案例 | 請展示一次主導需求訪談及其改變的產品決策。 |
| 2 | 年化留存與流程結果的量測口徑 | 年化留存如何計算，樣本選擇與比較限制是什麼？ |
| 3 | 中長期路線及資源決策邊界 | 請用一份去識別路線圖說明目標、優先序、資源與核定權責。 |

完整追問清單：

1. 請展示一次主導需求訪談及其改變的產品決策。

2. 如何分析市場趨勢並轉為MarTech產品機會？

3. 請用一份去識別路線圖說明目標、優先序、資源與核定權責。

4. 年化留存如何計算，樣本選擇與比較限制是什麼？

5. 處理週期母體與起訖定義為何，是否含未完成單？

6. 未再發生帳號冒用的觀察來源與涵蓋範圍為何？

7. 如何從功能使用數據推動迭代，並撰寫客戶說明？

### 6. 評語（給寫稿者的具體回饋）

**做得好（3 點）**：

- 企業端經驗｜「企業端招募系統全模組與求職端公司頁」｜可轉移到B2B工具的流程與需求管理。

- 取捨案例｜「選擇首次登入引導確認、不強迫修改」｜把既有客戶限制轉為方案選擇。

- 交付分工｜「與 QA 制定 UAT 驗收案例、排定上線計畫」｜直接支持JD規格、驗收與時程責任。



**可改進（3 點）**：

- 位置：專業技能／研究與數據

- 原句：使用者訪談與問卷

- 問題類型：requirement

- 嚴重度：interview_follow_up

- 影響：JD要求主導訪談與分析市場；技能列舉不足呈現執行品質，但不構成不符。

- 建議方向：補一個訪談對象、問題與如何改變方案的真實案例，市場趨勢亦同。



- 位置：1111／需求管線留存

- 原句：該群年化留存 81.2%，同期全站 74.2%

- 問題類型：measurement

- 嚴重度：interview_follow_up

- 影響：已有期間與非因果限制，年化算法及兩群可比性仍待面試確認。

- 建議方向：說明年化公式、觀察窗、樣本定義；另核對週期及安全觀察來源。



- 位置：1111／使用者旅程優先序

- 原句：信件與即時通整合排在其他新功能之前

- 問題類型：ownership

- 嚴重度：interview_follow_up

- 影響：優先序有依據，但中長期路線及資源決策權限尚不完整，留作策略深度追問。

- 建議方向：以一個路線圖案例交代目標、替代選項、資源限制與核定者。



**編輯附件**（不影響判斷）：

可將企業需求、競品研究與迭代案例排在變現案例之前；僅為可讀性調整。

### 7. 資深能力分布

delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

交付與PO協調證據完整；方向選擇有案例，較長期資源配置權責仍待追問。

### 8. 未測試聲明

PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

本次僅評履歷自述，未外部查證。HM13為方法層，不計分；沒有總分或跨職缺平均。

### 成果分類補表

| 原句片段 | 分類 | 說明 |
| :-- | :-- | :-- |
| 約 50 項大項功能上線 | output | 主表成果；仍為履歷自述 |
| 需求平均處理週期由 100.4 天降至 30.9 天 | outcome | 主表成果；仍為履歷自述 |
| 兩案皆開發中 | decision / in_progress | 主表成果；仍為履歷自述 |
| 該群年化留存 81.2%，同期全站 74.2% | outcome | 主表成果；仍為履歷自述 |
| 相對變化約多 28% | outcome | 主表成果；仍為履歷自述 |
| Peach 網頁付款占營收由 24% 至 80% 以上 | outcome | 主表成果；仍為履歷自述 |
| 全站活躍付費廠商約 6.6 萬家 | context | 產品規模，非個人成果 |
| 另於 2026/01–06 上線 111 項 Roadmap 細項 | output | 與50項口徑不同，不加總 |
| 盤點出上千組重複 E-mail | output / context | 資料盤點與問題規模 |
| 選擇首次登入引導確認、不強迫修改 | decision | 保留登入可用性的選擇 |
| 停機約 1.5 小時 | output | 改版切換交付條件 |
| 十多家廠商帳號遭冒用 | context | 安全問題規模 |
| 於 2026/04/17 上線簽章驗證 | output | 安全交付 |
| 上線後至 2026/10 未再出現同類帳號冒用 | outcome | 限定目前掌握情況，非監測查證 |
| 完成 1,726／1,857 張需求與問題單，約 93% | output | 工單完成量與比例 |
| 信件與即時通整合排在其他新功能之前 | decision / in_progress | 不可視為已實現影響 |
| 改版排在新功能職缺健檢之前 | decision / in_progress | 搜尋改版尚開發中 |
| 改依職缺上線日排序、20 天內不重複推薦 | decision / output | 規則修改，使用改善尚無量測 |
| 需求管線觸及 1,279 家活躍付費廠商 | context | 分析樣本與涵蓋範圍 |
| AI 功能已上線公司簡介生成 | output | 含工作說明生成及推薦人才，無成效數字 |
| 依客服測試回饋調整推薦規則 | decision / output | 回饋導向修正 |
| 依結果全面調降售價 | decision | 定價實驗後選擇，非全部因果證明 |
| KOOL 訂閱與付費牆規劃上線 | output | 跨平台付費功能交付 |
| 主導 Juicy 上線 | output | 上線責任 |
| 男性 DAU 約 3,200 至 1.25 萬 | outcome | 六週團隊上線與行銷整體表現 |
| 涵蓋美國、墨西哥、巴西、印尼、馬來西亞、日本、韓國 | output / context | 在地化涵蓋市場 |
| 與最多約 10 位外國實習生協作 | context | 協作範圍非直屬管理 |
| 開放印尼、泰國等市場的電信帳單與超商付款 | output | 付款整合交付 |
| 提出 7／30／90 天訂閱方案與加贈內容 | decision / output | 以成本試算支持方案 |
| 商品資訊英翻中與英文校對 | output | 翻譯交付 |
| 12 條分支、23 個共用 skill | output | 協作流程產物數非業務成效 |


## B-jd09｜揭盲：甲=M、乙=K；偏好=M

```json
{"job_id":"jd09","order":"甲=M/乙=K","differences":[{"what":"甲補充客服問題、競品實測到推薦規則調整的完整案例；乙僅列競品實測技能。","hiring_meaning":"對應需求搜集、競品分析與迭代優化，可追問根因驗證、規則取捨與調整後成效；是證據具體程度差異，不推斷乙缺乏能力。","type":"capability"},{"what":"同一留存觀察，甲交代本人定義取數欄位、DBA執行與試算表比對；乙只呈現比對結果。","hiring_meaning":"更清楚界定數據工作分工，可驗證群體定義、年化算法與選擇偏差；兩版皆註明非因果，不提高結果可信度。","type":"measurement"}],"preference":"甲","reason":"甲提供從客服痛點、競品實測到規則調整的可追問案例，並交代留存分析的本人分工，更利於驗證本職缺的需求判斷與數據思維；共同交付成果不重複加分。","evidence_甲":["客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。","由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。"],"evidence_乙":["研究與數據：使用者訪談與問卷、競品實測、GA4、世代分析、對照組實驗、Excel","比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。"]}
```

## 版本比較｜jd09｜順序 甲=M 乙=K｜model_id: unknown
- 偏好：甲（揭盲：M）

| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 甲補充客服問題、競品實測到推薦規則調整的完整案例；乙僅列競品實測技能。 | 對應需求搜集、競品分析與迭代優化，可追問根因驗證、規則取捨與調整後成效；是證據具體程度差異，不推斷乙缺乏能力。 | capability | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 | 研究與數據：使用者訪談與問卷、競品實測、GA4、世代分析、對照組實驗、Excel |
| 2 | 同一留存觀察，甲交代本人定義取數欄位、DBA執行與試算表比對；乙只呈現比對結果。 | 更清楚界定數據工作分工，可驗證群體定義、年化算法與選擇偏差；兩版皆註明非因果，不提高結果可信度。 | measurement | 由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |

- 理由（≤120 字）：甲提供從客服痛點、競品實測到規則調整的可追問案例，並交代留存分析的本人分工，更利於驗證本職缺的需求判斷與數據思維；共同交付成果不重複加分。

共同證據包含 PRD、原型、UAT、分階段上線與定價對照實驗，兩版均足以支持進一步面試。B2B 招募系統經驗與目標 MarTech SaaS 的轉移性，仍需面試確認；此處未作外部核實。


# jd11｜逐次輸出


## A-jd11-K｜履歷K

```json
{"rubric_version": "4.2", "resume_id": "K", "job_id": "jd11", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd11-K", "human_calibrated": false, "requirements": [{"id": "R01", "text": "規劃CMS或HRIS產品、持續優化流程", "type": "required", "status": "supported", "evidence": ["企業端招募系統全模組與求職端公司頁"], "blocks_interview": false, "reason": "招募系統經驗直接相關；可追問客戶管理流程差異。"}, {"id": "R02", "text": "使用者訪談與需求挖掘", "type": "required", "status": "partial", "evidence": ["使用者訪談與問卷"], "blocks_interview": false, "reason": "工單驅動需求有案例，直接訪談如何改變需求仍待確認。"}, {"id": "R03", "text": "PRD、流程圖、使用者故事", "type": "required", "status": "supported", "evidence": ["從 User Story、Wireframe 到 Figma／Axure 原型"], "blocks_interview": false, "reason": "有文件與實際交付案例。"}, {"id": "R04", "text": "協同UI/UX工程與roadmap規劃", "type": "required", "status": "supported", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "blocks_interview": false, "reason": "跨職能交付及優先順序有實例。"}, {"id": "R05", "text": "追蹤KPI與用戶反饋", "type": "required", "status": "supported", "evidence": ["依客服測試回饋調整推薦規則"], "blocks_interview": false, "reason": "有週期、留存及客服回饋證據。"}, {"id": "R06", "text": "5年以上PM經驗", "type": "required", "status": "supported", "evidence": ["近 10 年 PM 經驗"], "blocks_interview": false, "reason": "2016年起PM任職時序支持。"}, {"id": "R07", "text": "熟悉敏捷開發與跨部門專案管理", "type": "required", "status": "partial", "evidence": ["Kanban 搭配瀑布式開發"], "blocks_interview": false, "reason": "跨部門交付明確；敏捷迭代運作深度需追問。"}, {"id": "R08", "text": "邏輯溝通與專案範圍資源協商能力", "type": "required", "status": "supported", "evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "blocks_interview": false, "reason": "有風險取捨與協作範圍；資源協商可於面試確認。"}, {"id": "R09", "text": "Jira、Notion等工具及中英文文件撰寫", "type": "required", "status": "partial", "evidence": ["Figma、Axure RP、Notion、Trello、Markdown"], "blocks_interview": false, "reason": "Notion與中文規格有證據；Jira及英文撰寫樣本未呈現。"}, {"id": "R10", "text": "HR Tech/LegalTech/生成式AI產品經驗", "type": "preferred", "status": "supported", "evidence": ["AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。"], "blocks_interview": false, "reason": "HR Tech與生成式AI經驗相符。"}, {"id": "R11", "text": "LLM prompt或自動化內容編排", "type": "preferred", "status": "partial", "evidence": ["Claude Code 多分支流程與共用 skill 庫"], "blocks_interview": false, "reason": "有AI協作，prompt或內容編排責任不明。"}, {"id": "R12", "text": "資料思維、AB測試與前後端背景", "type": "preferred", "status": "partial", "evidence": ["以 Android 售價不變作對照"], "blocks_interview": false, "reason": "資料實驗支持；非隨機AB證據，基本HTML/CSS不等於工程背景。"}], "dimensions": [{"id": "positioning", "rating": "強", "evidence": ["現任 1111 招募系統 Product Owner"], "missing": ["無關鍵定位缺口"], "issue_ids": []}, {"id": "role_evidence", "rating": "足夠", "evidence": ["從需求釐清、系統分析到 PRD、原型、UAT 與上線計畫"], "missing": ["確認敏捷實務、訪談與英文文件；見I01–I03"], "issue_ids": ["I01", "I02", "I03"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": ["面試確認工單訊號到roadmap的取捨過程"], "issue_ids": []}, {"id": "outcome_quality", "rating": "足夠", "evidence": ["為觀察差異，非因果"], "missing": ["留存年化方法與安全監測來源待核對"], "issue_ids": ["I04"]}, {"id": "ownership", "rating": "強", "evidence": ["由我主責規劃，與工程團隊密切協作"], "missing": ["面試確認AI功能的產品與技術責任邊界"], "issue_ids": []}, {"id": "readability", "rating": "足夠", "evidence": ["資深產品經理｜Senior Product Manager"], "missing": ["可將最貼近HR Tech的案例提前；非面試障礙"], "issue_ids": []}], "results": [{"quote": "約 50 項大項功能上線", "kinds": ["output"]}, {"quote": "需求平均處理週期由 100.4 天降至 30.9 天", "kinds": ["outcome"]}, {"quote": "該群年化留存 81.2%，同期全站 74.2%", "kinds": ["outcome"]}, {"quote": "選擇首次登入引導確認、不強迫修改", "kinds": ["decision"]}, {"quote": "依結果全面調降售價", "kinds": ["decision"]}, {"quote": "目前專案仍在開發中", "kinds": ["in_progress"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "招募流程與職缺直接相關"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["對接 16 個需求單位"], "application_note": "近期角色及協作環境清楚"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "application_note": "能區分規劃與工程交付"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "流程改變有期間可追問"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "限制下有明確取捨"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["Associate PM｜思維特網路資訊｜2016/06 - 2018/01"], "application_note": "時序支持跨產品責任演變"}, {"rule_id": "HR07", "status": "partial", "resume_evidence": ["與 CodaPay 新加坡技術團隊協調串接"], "application_note": "實際協作明確，英文文件待核對"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "背景與代表案例易定位"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["為觀察差異，非因果"], "application_note": "查量測來源，不推定失實"}, {"rule_id": "HR10", "status": "supported", "resume_evidence": ["參與問題定義、方向選擇與成效判斷"], "application_note": "策略方向與roadmap職責相容"}, {"rule_id": "HR11", "status": "supported", "resume_evidence": ["台北市、新北市，可接受遠端或混合辦公"], "application_note": "所列地點未見已知衝突"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["與資料科學團隊合作，定義使用情境與驗收標準"], "application_note": "案例足以邀約，缺口可面試核對"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["廠商抱怨工單中，最大宗是溝通管道中斷"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM04", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "partial", "resume_evidence": ["該群年化留存 81.2%，同期全站 74.2%"], "evidence_type": "outcome", "source_ids": [], "interview_question": null}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["釐清需求與系統分析後"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM09", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["現任 1111 招募系統 Product Owner"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM13", "primary_dimension": "method", "status": "supported", "resume_evidence": [], "evidence_type": null, "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HR07", "source_ids": [], "application_note": "熟悉敏捷流程的程度", "context_limit": "僅依文字履歷，未外部查核", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "Kanban 搭配瀑布式開發", "reason": "混合流程不是不符合；需確認實際迭代、回顧及優先級調整是否支持JD敏捷要求。", "suggestion": "補一個回顧或回饋改變開發範圍的案例。"}, {"id": "I02", "rule_id": "HR07", "source_ids": [], "application_note": "工具與英文文件需核對", "context_limit": "僅依文字履歷，未外部查核", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "Figma、Axure RP、Notion、Trello、Markdown", "reason": "Notion有列；Jira未寫，英文翻譯與成績不直接證明英文PRD撰寫。缺口可於面試驗證。", "suggestion": "提供可分享的英文文件片段並確認工具使用；無經驗勿補寫。"}, {"id": "I03", "rule_id": "HM02", "source_ids": [], "application_note": "直接訪談證據待補", "context_limit": "僅依文字履歷，未外部查核", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "使用者訪談與問卷", "reason": "工單與客服訊號已支持問題理解，但直接訪談的角色與洞察尚未呈現；追問方法及如何改變需求。", "suggestion": "補一個訪談對象、問題、洞察與需求改動的實例。"}, {"id": "I04", "rule_id": "HM05", "source_ids": [], "application_note": "成果口徑需確認", "context_limit": "僅依文字履歷，未外部查核", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "該群年化留存 81.2%，同期全站 74.2%", "reason": "已明示非因果；年化方式、群體選擇與安全事件偵測來源仍須核對，不否定結果。", "suggestion": "說明計算窗口、年化公式及可分享的來源摘要；安全觀察維持自述限制。"}], "decision": {"recommendation": "interview", "evidence": ["企業端招募系統全模組與求職端公司頁", "選擇首次登入引導確認、不強迫修改"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["招募系統與生成式AI產品案例直接相關", "規格、驗收、風險及跨職能交付清楚", "能從使用者限制與數據作產品取捨"], "key_gaps": ["敏捷迭代與直接使用者訪談細節", "Jira熟悉程度與英文產品文件樣本", "成果計算與監測來源"], "strengths": ["HR Tech經驗與產品開發流程直接對位", "登入改版提供具體限制與選擇理由", "成果標示期間、整體表現與非因果限制"], "interview_questions": ["請說明一次迭代或回顧如何改變需求範圍。", "使用者訪談由誰進行？哪個洞察改變了PRD？", "可展示去識別的英文產品文件並說明Jira或相似工具實務嗎？", "年化留存如何計算，如何處理客群選擇差異？", "帳號冒用改善的事件偵測與資料來源是什麼？", "AI生成產品中你負責哪些prompt、驗收與編排決策？", "多需求單位衝突時，如何協商人力與roadmap順序？"], "editorial_appendix": ["可把AI產品案例提前，方便快速辨識與本職缺的關聯。"], "spectrum": {"level": 8, "uncertainty_levels": 1, "basis": "多個直接相關案例，有清楚取捨、期間比較與限制；工具、英文文件及量測來源仍待面試確認。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷K｜第 1 輪｜model_id: unknown

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「企業端招募系統全模組與求職端公司頁」直接相關，取捨及交付案例足以支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 現任 1111 招募系統 Product Owner | 無關鍵定位缺口 |
| role_evidence | 足夠 | 從需求釐清、系統分析到 PRD、原型、UAT 與上線計畫 | 確認敏捷實務、訪談與英文文件；見I01–I03 |
| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 面試確認工單訊號到roadmap的取捨過程 |
| outcome_quality | 足夠 | 為觀察差異，非因果 | 留存年化方法與安全監測來源待核對 |
| ownership | 強 | 由我主責規劃，與工程團隊密切協作 | 面試確認AI功能的產品與技術責任邊界 |
| readability | 足夠 | 資深產品經理｜Senior Product Manager | 可將最貼近HR Tech的案例提前；非面試障礙 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 規劃CMS或HRIS產品、持續優化流程 | 必要 | supported | 企業端招募系統全模組與求職端公司頁 | 招募系統經驗直接相關；可追問客戶管理流程差異。 |
| 使用者訪談與需求挖掘 | 必要 | partial | 使用者訪談與問卷 | 工單驅動需求有案例，直接訪談如何改變需求仍待確認。 |
| PRD、流程圖、使用者故事 | 必要 | supported | 從 User Story、Wireframe 到 Figma／Axure 原型 | 有文件與實際交付案例。 |
| 協同UI/UX工程與roadmap規劃 | 必要 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 跨職能交付及優先順序有實例。 |
| 追蹤KPI與用戶反饋 | 必要 | supported | 依客服測試回饋調整推薦規則 | 有週期、留存及客服回饋證據。 |
| 5年以上PM經驗 | 必要 | supported | 近 10 年 PM 經驗 | 2016年起PM任職時序支持。 |
| 熟悉敏捷開發與跨部門專案管理 | 必要 | partial | Kanban 搭配瀑布式開發 | 跨部門交付明確；敏捷迭代運作深度需追問。 |
| 邏輯溝通與專案範圍資源協商能力 | 必要 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 有風險取捨與協作範圍；資源協商可於面試確認。 |
| Jira、Notion等工具及中英文文件撰寫 | 必要 | partial | Figma、Axure RP、Notion、Trello、Markdown | Notion與中文規格有證據；Jira及英文撰寫樣本未呈現。 |
| HR Tech/LegalTech/生成式AI產品經驗 | 加分 | supported | AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。 | HR Tech與生成式AI經驗相符。 |
| LLM prompt或自動化內容編排 | 加分 | partial | Claude Code 多分支流程與共用 skill 庫 | 有AI協作，prompt或內容編排責任不明。 |
| 資料思維、AB測試與前後端背景 | 加分 | partial | 以 Android 售價不變作對照 | 資料實驗支持；非隨機AB證據，基本HTML/CSS不等於工程背景。 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 企業端招募系統全模組與求職端公司頁 | 招募流程與職缺直接相關 |
| HR02 | supported | 對接 16 個需求單位 | 近期角色及協作環境清楚 |
| HR03 | supported | 由我主責規劃，與工程團隊密切協作 | 能區分規劃與工程交付 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 流程改變有期間可追問 |
| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 限制下有明確取捨 |
| HR06 | supported | Associate PM｜思維特網路資訊｜2016/06 - 2018/01 | 時序支持跨產品責任演變 |
| HR07 | partial | 與 CodaPay 新加坡技術團隊協調串接 | 實際協作明確，英文文件待核對 |
| HR08 | supported | 企業端招募系統全模組與求職端公司頁 | 背景與代表案例易定位 |
| HR09 | partial | 為觀察差異，非因果 | 查量測來源，不推定失實 |
| HR10 | supported | 參與問題定義、方向選擇與成效判斷 | 策略方向與roadmap職責相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公 | 所列地點未見已知衝突 |
| HR12 | supported | 與資料科學團隊合作，定義使用情境與驗收標準 | 案例足以邀約，缺口可面試核對 |
| HM01 | supported | 企業端招募系統全模組與求職端公司頁 | 招募流程能力可轉移 |
| HM02 | supported | 廠商抱怨工單中，最大宗是溝通管道中斷 | 有問題訊號，訪談過程可追問 |
| HM03 | supported | 選擇首次登入引導確認、不強迫修改 | 風險與使用者取捨清楚 |
| HM04 | supported | 依抽成、稅、手續費及撥款週期做實收試算 | 能連結商業條件與方案 |
| HM05 | partial | 該群年化留存 81.2%，同期全站 74.2% | 需核對年化算法與群體差異 |
| HM06 | supported | 由我主責規劃，與工程團隊密切協作 | 本人與工程邊界可辨 |
| HM07 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 有範圍驗收及上線證據 |
| HM08 | supported | 釐清需求與系統分析後 | 符合一般PM技術協作需求 |
| HM09 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 有自主範圍及風險管理 |
| HM10 | supported | 現任 1111 招募系統 Product Owner | 產品及角色資訊清楚 |
| HM11 | supported | 依客服測試回饋調整推薦規則 | 回饋曾導致修改 |
| HM12 | supported | AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。 | 有HR Tech及AI案例可深挖 |
| HM13 | supported | 不適用：方法層 | 依此JD獨立判讀，未作外部查證 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「企業端招募系統全模組與求職端公司頁」：直接領域關聯。 |
| 2 | 「與 QA 制定 UAT 驗收案例、排定上線計畫」：交付責任明確。 |
| 3 | 「選擇首次登入引導確認、不強迫修改」：具體風險取捨。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 敏捷迭代與直接使用者訪談細節 | 敏捷回顧與訪談如何改變需求？ |
| 2 | Jira熟悉程度與英文產品文件樣本 | 能否提供英文產品文件及工具使用案例？ |
| 3 | 成果計算與監測來源 | 留存如何年化，安全事件如何追蹤？ |

其他面試追問：
- AI生成產品中你負責哪些prompt、驗收與編排決策？
- 多需求單位衝突時，如何協商人力與roadmap順序？

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
1. 1111經歷｜「企業端招募系統全模組與求職端公司頁」｜能直接判斷與HR流程產品的相關性。
2. 改版案例｜「選擇首次登入引導確認、不強迫修改」｜呈現資料限制、使用者風險與可交付取捨。
3. 留存案例｜「為觀察差異，非因果」｜界定成果主張範圍，有助討論KPI而不誤認因果。

**可改進（4 點）**：

- 位置：熟悉敏捷流程的程度
- 原句：Kanban 搭配瀑布式開發
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：混合流程不是不符合；需確認實際迭代、回顧及優先級調整是否支持JD敏捷要求。
- 建議方向：補一個回顧或回饋改變開發範圍的案例。

- 位置：工具與英文文件需核對
- 原句：Figma、Axure RP、Notion、Trello、Markdown
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：Notion有列；Jira未寫，英文翻譯與成績不直接證明英文PRD撰寫。缺口可於面試驗證。
- 建議方向：提供可分享的英文文件片段並確認工具使用；無經驗勿補寫。

- 位置：直接訪談證據待補
- 原句：使用者訪談與問卷
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：工單與客服訊號已支持問題理解，但直接訪談的角色與洞察尚未呈現；追問方法及如何改變需求。
- 建議方向：補一個訪談對象、問題、洞察與需求改動的實例。

- 位置：成果口徑需確認
- 原句：該群年化留存 81.2%，同期全站 74.2%
- 問題類型：measurement
- 嚴重度：interview_follow_up
- 影響：已明示非因果；年化方式、群體選擇與安全事件偵測來源仍須核對，不否定結果。
- 建議方向：說明計算窗口、年化公式及可分享的來源摘要；安全觀察維持自述限制。

**編輯附件**（不影響判斷）：
- 可將AI產品案例提前；無需新增未發生的經驗。

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

交付與跨部門協作有直接案例；方向選擇有優先級及商業方案依據，完整人力配置與策略成效責任可留面試確認。三者獨立判定。

### 8. 未測試聲明
PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

所有結果均為履歷自述，沒有外部查證；不計總分，不推論作者身分。

### 成果分類補表
| 原句片段 | 分類 | 解讀限制 |
| :-- | :-- | :-- |
| 全站活躍付費廠商約 6.6 萬家 | context | 系統規模，非個人成果 |
| 另於 2026/01–06 上線 111 項 Roadmap 細項 | output | 細項交付；不與50項相加 |
| 盤點出上千組重複 E-mail | output、context | 資料盤點與問題範圍 |
| 停機約 1.5 小時 | output | 上線執行記錄，非採用結果 |
| 2026/04 十多家廠商帳號遭冒用 | context | 事件背景 |
| 於 2026/04/17 上線簽章驗證 | output | 與工程合作上線 |
| 上線後至 2026/10 未再出現同類帳號冒用 | outcome | 目前掌握情況；非獨立監測查證 |
| 完成 1,726／1,857 張需求與問題單，約 93% | output | 截至09/29的處理量與分母 |
| 需求管線觸及 1,279 家活躍付費廠商 | context | 觸及範圍，約1.9%非影響率 |
| AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。 | output | 功能交付，未提供採用成效 |
| 依客服測試回饋調整推薦規則 | decision | 回饋促成調整 |
| 降價期 iOS 非續訂營收較基準期增 5% | outcome | 三階段各21天，非隨機實驗 |
| Android 減 18%，相對變化約多 28% | outcome | 平台對照與相對差異，因果需追問 |
| 還原原價後 iOS 較基準期減 65% | outcome | 支持後續定價決策，仍有時間效應 |
| Peach 網頁付款占營收由 24% 至 80% 以上 | outcome | 渠道占比，非總營收成長 |
| KOOL 訂閱與付費牆規劃上線 | output | 跨平台交付 |
| 設定檔案完成、社群認證及照片門檻 | decision | 資格規則設計 |
| 主導 Juicy 上線 | output | 上線交付 |
| 上線後 6 週男性 DAU 約 3,200 至 1.25 萬 | outcome | 產品與行銷整體表現 |
| SweetRing 在地化涵蓋美國、墨西哥、巴西、印尼、馬來西亞、日本、韓國 7 個市場 | output、context | 在地化交付範圍，不作市場成功推論 |
| 與最多約 10 位外國實習生協作 | context | 無直屬管理關係 |
| 導入 CodaPay | output | 付款選項交付 |
| 提出 7／30／90 天訂閱方案與加贈內容 | decision、output | 實收試算支持方案，未宣稱成效 |
| Newegg.com 商品資訊英翻中與校對。 | output | 翻譯工作，非英文產品文件證明 |
| 將信件與即時通整合排在其他新功能之前 | decision、in_progress | 已決策但仍開發，不計已實現結果 |


## A-jd11-M｜履歷M

```json
{"rubric_version": "4.2", "resume_id": "M", "job_id": "jd11", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd11-M", "human_calibrated": false, "requirements": [{"id": "R01", "text": "5年以上PM經驗", "type": "required", "status": "supported", "evidence": ["近 10 年 PM 經驗"], "blocks_interview": false, "reason": "2016年至今的PM職務時間支持。"}, {"id": "R02", "text": "熟悉敏捷開發與跨部門專案管理", "type": "required", "status": "partial", "evidence": ["以 Kanban 推進瀑布式開發"], "blocks_interview": false, "reason": "跨部門交付充分；混合流程支持部分敏捷實務，需確認迭代及回顧如何運作。"}, {"id": "R03", "text": "優秀邏輯與溝通能力", "type": "required", "status": "supported", "evidence": ["選擇首次登入引導確認、不強迫修改"], "blocks_interview": false, "reason": "有資料風險取捨及客服、工程協作案例。"}, {"id": "R04", "text": "熟悉Jira、Notion等工具", "type": "required", "status": "partial", "evidence": ["Notion、Trello"], "blocks_interview": false, "reason": "Notion有列示，Jira未呈現；不推論不會使用。"}, {"id": "R05", "text": "中英文文件撰寫能力", "type": "required", "status": "partial", "evidence": ["Newegg.com 商品資訊英翻中與英文校對"], "blocks_interview": false, "reason": "中文產品規格及英文校對有線索；英文產品文件需樣本確認。"}, {"id": "R06", "text": "規劃CMS或HRIS、訪談挖掘需求並優化流程", "type": "required", "status": "partial", "evidence": ["現任 1111 招募系統 Product Owner"], "blocks_interview": false, "reason": "招募系統可轉移；直接CMS／內部HRIS範圍及訪談如何改變決策待問。"}, {"id": "R07", "text": "撰寫PRD、流程圖、使用者故事並協同設計工程交付", "type": "required", "status": "supported", "evidence": ["整理為 PRD 與 Axure Prototype"], "blocks_interview": false, "reason": "文件、UAT及跨職能上線實例可支持。"}, {"id": "R08", "text": "追蹤KPI、用戶反饋並參與roadmap", "type": "required", "status": "supported", "evidence": ["依使用者旅程排優先級"], "blocks_interview": false, "reason": "工單回饋、週期與留存觀察支持；可追問指標治理。"}, {"id": "R09", "text": "HR Tech／LegalTech／生成式AI產品經驗", "type": "preferred", "status": "supported", "evidence": ["AI 功能已上線公司簡介生成"], "blocks_interview": false, "reason": "招募產品與生成式AI情境直接相關，未宣稱具LegalTech。"}, {"id": "R10", "text": "LLM prompt設計或自動化內容編排", "type": "preferred", "status": "partial", "evidence": ["自建 Claude Code 協作流程"], "blocks_interview": false, "reason": "有AI工作流程線索，未呈現prompt版本或內容編排設計細節。"}, {"id": "R11", "text": "資料導向思維、AB測試經驗", "type": "preferred", "status": "partial", "evidence": ["以 Android 售價不變作對照"], "blocks_interview": false, "reason": "有對照實驗與資料判讀，非隨機A/B的證據，需問偏差處理。"}, {"id": "R12", "text": "前端或後端技術背景", "type": "preferred", "status": "partial", "evidence": ["基本 HTML／CSS、資料庫知識"], "blocks_interview": false, "reason": "呈現技術素養但未呈現前後端開發經歷；非必要條件。"}], "dimensions": [{"id": "positioning", "rating": "強", "evidence": ["現任 1111 招募系統 Product Owner"], "missing": ["招募外部產品與內部CMS／HRIS差異可面試釐清"], "issue_ids": []}, {"id": "role_evidence", "rating": "足夠", "evidence": ["整理為 PRD 與 Axure Prototype"], "missing": ["敏捷實務、工具及英文產品文件待核對"], "issue_ids": ["I01", "I02"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": ["可追問訪談如何修正優先級"], "issue_ids": []}, {"id": "outcome_quality", "rating": "足夠", "evidence": ["為觀察差異，非因果"], "missing": ["留存年化、週期母體與安全觀察來源待核對"], "issue_ids": ["I03"]}, {"id": "ownership", "rating": "強", "evidence": ["由我擬定取數的資料表與欄位"], "missing": ["AI功能中的模型與產品責任邊界可深化"], "issue_ids": ["I04"]}, {"id": "readability", "rating": "足夠", "evidence": ["企業端招募系統全模組與求職端公司頁"], "missing": ["成果計數單位與重複敘事可精簡"], "issue_ids": ["I05"]}], "results": [{"quote": "全站活躍付費廠商約 6.6 萬家", "kinds": ["context"]}, {"quote": "約 50 項大項功能上線", "kinds": ["output"]}, {"quote": "選擇首次登入引導確認、不強迫修改", "kinds": ["decision"]}, {"quote": "需求平均處理週期由 100.4 天降至 30.9 天", "kinds": ["outcome"]}, {"quote": "為觀察差異，非因果", "kinds": ["outcome"]}, {"quote": "兩案皆開發中", "kinds": ["in_progress"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["整理為 PRD 與 Axure Prototype"], "application_note": "文件與交付直接對應職務"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "招募流程經驗可轉移"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我擬定取數的資料表與欄位"], "application_note": "個人與DBA分工清楚"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "有改變，需核對衡量口徑"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "能具體說明風險取捨"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["從交友與訂閱制 App 到企業招募系統"], "application_note": "職涯領域演變清楚"}, {"rule_id": "HR07", "status": "partial", "resume_evidence": ["以 Kanban 推進瀑布式開發"], "application_note": "敏捷深度及英文文件待核對"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["依使用者旅程排優先級"], "application_note": "代表判斷可快速辨認"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["依目前掌握的情況"], "application_note": "安全觀察與年化方式需核對"}, {"rule_id": "HR10", "status": "supported", "resume_evidence": ["參與問題定義、方向選擇與成效判斷"], "application_note": "方向與roadmap工作相容"}, {"rule_id": "HR11", "status": "supported", "resume_evidence": ["台北市、新北市，可接受遠端或混合辦公"], "application_note": "北士科地點未見已知衝突"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["AI 功能已上線公司簡介生成"], "application_note": "相關案例充分，適合面試驗證"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["現任 1111 招募系統 Product Owner"], "evidence_type": "context", "source_ids": [], "interview_question": "招募系統與CMS／HRIS的資料流程有哪些異同？"}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["客服反映配對名單「少又舊」"], "evidence_type": "decision", "source_ids": [], "interview_question": "哪次訪談或客服回饋改變你原本的問題定義？"}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["信件與即時通整合排在其他新功能之前"], "evidence_type": "decision", "source_ids": [], "interview_question": "如何比較整合與新功能價值，誰有最終決策權？"}, {"rule_id": "HM04", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "evidence_type": "decision", "source_ids": [], "interview_question": "如何把商業衡量轉用企業內部流程產品？"}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "partial", "resume_evidence": ["為觀察差異，非因果"], "evidence_type": "outcome", "source_ids": [], "interview_question": "留存年化與週期計算的母體、排除條件為何？"}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "evidence_type": "output", "source_ids": [], "interview_question": "你與工程、設計在範圍分歧時如何決策？"}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["第一階段於 2025/10 離峰切換上線"], "evidence_type": "output", "source_ids": [], "interview_question": "切換驗收、回滾及客戶告知如何安排？"}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["改依職缺上線日排序、20 天內不重複推薦"], "evidence_type": "decision", "source_ids": [], "interview_question": "規則如何落成資料欄位、例外情境與驗收？"}, {"rule_id": "HM09", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "evidence_type": "output", "source_ids": [], "interview_question": "自主決策範圍與資源授權為何？"}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則"], "evidence_type": "decision", "source_ids": [], "interview_question": "請說明一次反證、具體調整與後續驗證。"}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["AI 功能已上線公司簡介生成"], "evidence_type": "output", "source_ids": [], "interview_question": "可否展示匿名中英文PRD及AI驗收範例？"}, {"rule_id": "HM13", "primary_dimension": "", "status": "supported", "resume_evidence": ["以 Android 售價不變作對照"], "evidence_type": "context", "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HR07", "source_ids": [], "application_note": "專業摘要／交付技能", "context_limit": "僅依履歷文字，未外部驗證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "以 Kanban 推進瀑布式開發", "reason": "混合流程不等於不符敏捷；需確認JD要求的迭代能力，不阻擋面試。", "suggestion": "補一例迭代、回顧改變與工具使用。"}, {"id": "I02", "rule_id": "HR01", "source_ids": [], "application_note": "翻譯工讀生／語言", "context_limit": "僅依履歷文字，未外部驗證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "Newegg.com 商品資訊英翻中與英文校對", "reason": "英文使用有證據，英文產品文件撰寫尚未直接呈現；留面試核對。", "suggestion": "準備匿名中英文規格片段，說明本人撰寫範圍。"}, {"id": "I03", "rule_id": "HM05", "source_ids": [], "application_note": "1111數據與安全成果", "context_limit": "僅依履歷文字，未外部驗證", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "該群年化留存 81.2%，同期全站 74.2%", "reason": "已有非因果限制，但年化與群組定義待問；安全觀察亦非監測證明。", "suggestion": "補留存年化公式、週期母體及安全訊號來源，保留觀察限制。"}, {"id": "I04", "rule_id": "HM06", "source_ids": [], "application_note": "1111 AI功能", "context_limit": "僅依履歷文字，未外部驗證", "category": "ownership", "severity": "interview_follow_up", "block_target": null, "claim": "定義使用情境與驗收標準", "reason": "生成式AI產品相關，但prompt、評估與資料科學責任邊界待問。", "suggestion": "補一個生成品質驗收與回饋修正案例。"}, {"id": "I05", "rule_id": "HR08", "source_ids": [], "application_note": "1111交付成果", "context_limit": "僅依履歷文字，未外部驗證", "category": "readability", "severity": "editorial", "block_target": null, "claim": "另於 2026/01–06 上線 111 項 Roadmap 細項。", "reason": "大項、細項及工單不同口徑容易被混讀；僅影響資訊理解。", "suggestion": "簡短註明各層級關係，減少摘要與自傳重複。"}], "decision": {"recommendation": "interview", "evidence": ["現任 1111 招募系統 Product Owner", "整理為 PRD 與 Axure Prototype", "AI 功能已上線公司簡介生成"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["「現任 1111 招募系統 Product Owner」直接鄰近HR Tech流程。", "「整理為 PRD 與 Axure Prototype」配合驗收與交付責任。", "「選擇首次登入引導確認、不強迫修改」呈現風險取捨。"], "key_gaps": ["敏捷實務、Jira熟悉程度及英文產品文件需核對。", "衡量母體、年化方式及安全觀察來源需核對。", "AI驗收與prompt責任邊界需釐清。"], "strengths": ["招募流程與生成式AI產品經驗對應職缺。", "個人規劃、QA驗收及DBA分工可辨識。", "取捨與觀察限制有明確敘述。"], "interview_questions": ["如何實際迭代、回顧並使用Notion／Jira管理跨部門需求？", "請展示匿名中英文PRD及本人撰寫範圍。", "招募系統經驗如何轉移CMS／HRIS，哪次使用者訪談改變了需求？", "請解釋留存年化、週期母體與安全觀察的資料來源。", "AI生成品質如何驗收，prompt與資料科學團隊如何分工？", "定價實驗如何排除平台差異及時間偏差？", "三階段上線如何安排驗收、回滾與客服溝通？", "roadmap取捨與資源調整的最終決策權在哪裡？"], "editorial_appendix": ["可將招募系統與AI產品案例前置；不因措辭或篇幅改判。"], "spectrum": {"level": 8, "uncertainty_levels": 1, "basis": "多個相關交付案例、清楚取捨及有比較與限制的衡量支持面試；英文產品文件與AI細節尚待驗證。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷｜第 1 輪｜model_id: unknown

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「現任 1111 招募系統 Product Owner」具相關流程、交付與取捨，支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 現任 1111 招募系統 Product Owner | 招募外部產品與內部CMS／HRIS差異可面試釐清 |
| role_evidence | 足夠 | 整理為 PRD 與 Axure Prototype | 敏捷實務、工具及英文產品文件待核對 |
| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 可追問訪談如何修正優先級 |
| outcome_quality | 足夠 | 為觀察差異，非因果 | 留存年化、週期母體與安全觀察來源待核對 |
| ownership | 強 | 由我擬定取數的資料表與欄位 | AI功能中的模型與產品責任邊界可深化 |
| readability | 足夠 | 企業端招募系統全模組與求職端公司頁 | 成果計數單位與重複敘事可精簡 |

### 3. JD 條件對照
摘要中的工作職責也逐條對照；未把工具未寫推定成不符合。
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 5年以上PM經驗 | 必要 | supported | 近 10 年 PM 經驗 | 2016年至今的PM職務時間支持。 |
| 熟悉敏捷開發與跨部門專案管理 | 必要 | partial | 以 Kanban 推進瀑布式開發 | 跨部門交付充分；混合流程支持部分敏捷實務，需確認迭代及回顧如何運作。 |
| 優秀邏輯與溝通能力 | 必要 | supported | 選擇首次登入引導確認、不強迫修改 | 有資料風險取捨及客服、工程協作案例。 |
| 熟悉Jira、Notion等工具 | 必要 | partial | Notion、Trello | Notion有列示，Jira未呈現；不推論不會使用。 |
| 中英文文件撰寫能力 | 必要 | partial | Newegg.com 商品資訊英翻中與英文校對 | 中文產品規格及英文校對有線索；英文產品文件需樣本確認。 |
| 規劃CMS或HRIS、訪談挖掘需求並優化流程 | 必要 | partial | 現任 1111 招募系統 Product Owner | 招募系統可轉移；直接CMS／內部HRIS範圍及訪談如何改變決策待問。 |
| 撰寫PRD、流程圖、使用者故事並協同設計工程交付 | 必要 | supported | 整理為 PRD 與 Axure Prototype | 文件、UAT及跨職能上線實例可支持。 |
| 追蹤KPI、用戶反饋並參與roadmap | 必要 | supported | 依使用者旅程排優先級 | 工單回饋、週期與留存觀察支持；可追問指標治理。 |
| HR Tech／LegalTech／生成式AI產品經驗 | 加分 | supported | AI 功能已上線公司簡介生成 | 招募產品與生成式AI情境直接相關，未宣稱具LegalTech。 |
| LLM prompt設計或自動化內容編排 | 加分 | partial | 自建 Claude Code 協作流程 | 有AI工作流程線索，未呈現prompt版本或內容編排設計細節。 |
| 資料導向思維、AB測試經驗 | 加分 | partial | 以 Android 售價不變作對照 | 有對照實驗與資料判讀，非隨機A/B的證據，需問偏差處理。 |
| 前端或後端技術背景 | 加分 | partial | 基本 HTML／CSS、資料庫知識 | 呈現技術素養但未呈現前後端開發經歷；非必要條件。 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 整理為 PRD 與 Axure Prototype | 文件與交付直接對應職務 |
| HR02 | supported | 企業端招募系統全模組與求職端公司頁 | 招募流程經驗可轉移 |
| HR03 | supported | 由我擬定取數的資料表與欄位 | 個人與DBA分工清楚 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 有改變，需核對衡量口徑 |
| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 能具體說明風險取捨 |
| HR06 | supported | 從交友與訂閱制 App 到企業招募系統 | 職涯領域演變清楚 |
| HR07 | partial | 以 Kanban 推進瀑布式開發 | 敏捷深度及英文文件待核對 |
| HR08 | supported | 依使用者旅程排優先級 | 代表判斷可快速辨認 |
| HR09 | partial | 依目前掌握的情況 | 安全觀察與年化方式需核對 |
| HR10 | supported | 參與問題定義、方向選擇與成效判斷 | 方向與roadmap工作相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公 | 北士科地點未見已知衝突 |
| HR12 | supported | AI 功能已上線公司簡介生成 | 相關案例充分，適合面試驗證 |
| HM01 | supported | 現任 1111 招募系統 Product Owner | HR Tech流程經驗可轉移 |
| HM02 | supported | 客服反映配對名單「少又舊」 | 有客服訊號與根因判讀 |
| HM03 | supported | 信件與即時通整合排在其他新功能之前 | 優先級與登入風險取捨清楚 |
| HM04 | supported | 依抽成、稅、手續費及撥款週期做實收試算 | 有商業方案評估能力 |
| HM05 | partial | 為觀察差異，非因果 | 衡量口徑留面試釐清 |
| HM06 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 個人與協作者角色可辨 |
| HM07 | supported | 第一階段於 2025/10 離峰切換上線 | 可追問上線回滾細節 |
| HM08 | supported | 改依職缺上線日排序、20 天內不重複推薦 | 業務規則可與工程協作 |
| HM09 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 自主範圍支持資深IC面試 |
| HM10 | supported | 由我主責規劃，與工程團隊密切協作 | 重點清楚，計數可再註解 |
| HM11 | supported | 依客服測試回饋調整推薦規則 | 具回饋修正線索 |
| HM12 | supported | AI 功能已上線公司簡介生成 | 樣本驗證英文與AI細節 |
| HM13 | supported | 以 Android 售價不變作對照 | 獨立對照JD，未作真人校準 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「現任 1111 招募系統 Product Owner」直接鄰近HR Tech流程。 |
| 2 | 「整理為 PRD 與 Axure Prototype」配合驗收與交付責任。 |
| 3 | 「選擇首次登入引導確認、不強迫修改」呈現風險取捨。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 敏捷實務、Jira熟悉程度及英文產品文件需核對。 | 如何實際迭代、回顧並使用Notion／Jira管理跨部門需求？ 請展示匿名中英文PRD及本人撰寫範圍。 |
| 2 | 衡量母體、年化方式及安全觀察來源需核對。 | 請解釋留存年化、週期母體與安全觀察的資料來源。 |
| 3 | AI驗收與prompt責任邊界需釐清。 | AI生成品質如何驗收，prompt與資料科學團隊如何分工？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 摘要｜「現任 1111 招募系統 Product Owner」｜直接對應企業流程與HR Tech產品。
- 1111交付｜「與 QA 制定 UAT 驗收案例、排定上線計畫」｜顯示規格到交付的責任。
- 1111改版｜「選擇首次登入引導確認、不強迫修改」｜有使用者風險與可執行取捨。

**可改進（5 點）**：

- 位置：專業摘要／交付技能
- 原句：以 Kanban 推進瀑布式開發
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：混合流程不等於不符敏捷；需確認JD要求的迭代能力，不阻擋面試。
- 建議方向：補一例迭代、回顧改變與工具使用。

- 位置：翻譯工讀生／語言
- 原句：Newegg.com 商品資訊英翻中與英文校對
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：英文使用有證據，英文產品文件撰寫尚未直接呈現；留面試核對。
- 建議方向：準備匿名中英文規格片段，說明本人撰寫範圍。

- 位置：1111數據與安全成果
- 原句：該群年化留存 81.2%，同期全站 74.2%
- 問題類型：measurement
- 嚴重度：interview_follow_up
- 影響：已有非因果限制，但年化與群組定義待問；安全觀察亦非監測證明。
- 建議方向：補留存年化公式、週期母體及安全訊號來源，保留觀察限制。

- 位置：1111 AI功能
- 原句：定義使用情境與驗收標準
- 問題類型：ownership
- 嚴重度：interview_follow_up
- 影響：生成式AI產品相關，但prompt、評估與資料科學責任邊界待問。
- 建議方向：補一個生成品質驗收與回饋修正案例。

- 位置：1111交付成果
- 原句：另於 2026/01–06 上線 111 項 Roadmap 細項。
- 問題類型：readability
- 嚴重度：editorial
- 影響：大項、細項及工單不同口徑容易被混讀；僅影響資訊理解。
- 建議方向：簡短註明各層級關係，減少摘要與自傳重複。

**編輯附件**（不影響判斷）：可將招募系統與AI產品案例前置；不因措辭或篇幅改判。

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠
方向取捨有證據，資源授權與長期roadmap權責仍可追問；三者分別判定。

### 8. 未測試聲明
PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run
本審查僅依指定履歷與JD摘要；所有成果均屬履歷自述，未外部驗證。

### 成果分類補表
| 原文片段 | 分類 | 解讀限制 |
| :-- | :-- | :-- |
| 全站活躍付費廠商約 6.6 萬家 | context | 見主評語 |
| 約 50 項大項功能上線 | output | 見主評語 |
| 選擇首次登入引導確認、不強迫修改 | decision | 見主評語 |
| 需求平均處理週期由 100.4 天降至 30.9 天 | outcome | 見主評語 |
| 為觀察差異，非因果 | outcome | 見主評語 |
| 兩案皆開發中 | in_progress | 見主評語 |
| 另於 2026/01–06 上線 111 項 Roadmap 細項。 | output | 與50大項口徑不同，不相加 |
| 停機約 1.5 小時 | output | 切換紀錄，非使用者效益 |
| 於 2026/04/17 上線簽章驗證 | output | 工程協作交付 |
| 上線後至 2026/10 未再出現同類帳號冒用 | outcome | 目前掌握情況，不冒充監測紀錄 |
| 完成 1,726／1,857 張需求與問題單，約 93%。 | output | 處理量與完成比例，非客戶價值本身 |
| 改依職缺上線日排序、20 天內不重複推薦 | decision | 規則調整，未提供採用結果 |
| 需求管線觸及 1,279 家活躍付費廠商 | context | 接觸母體，非成效 |
| 該群年化留存 81.2%，同期全站 74.2% | outcome | 觀察差異而非因果 |
| AI 功能已上線公司簡介生成 | output | 生成與推薦功能交付，未呈現採用率 |
| 依客服測試回饋調整推薦規則 | decision | 回饋修正，非已證實成效 |
| 相對變化約多 28% | outcome | 平台及時間差異待核對 |
| 依結果全面調降售價 | decision | 價格決策，非後續成效 |
| Peach 網頁付款占營收由 24% 至 80% 以上 | outcome | 付款組合變化，不等同總營收成長 |
| KOOL 訂閱與付費牆規劃上線 | output | 跨平台方案交付 |
| 才開放精選網紅資格 | decision | 品質門檻設計 |
| 主導 Juicy 上線 | output | 產品交付 |
| 男性 DAU 約 3,200 至 1.25 萬 | outcome | 產品及行銷共同期間表現 |
| SweetRing 在地化涵蓋美國、墨西哥、巴西 | output | 多市場在地化範圍 |
| 與最多約 10 位外國實習生協作 | context | 無直屬管理關係 |
| 導入 CodaPay | output | 支付方式交付 |
| 提出 7／30／90 天訂閱方案與加贈內容 | decision | 實收試算支持方案選擇 |
| Newegg.com 商品資訊英翻中與英文校對 | output | 文件工作線索 |
| 12 條分支、23 個共用 skill | output | 自建協作流程規模，非生產力成效 |


## B-jd11｜揭盲：甲=K、乙=M；偏好=M

```json
{"job_id":"jd11","order":"甲=K/乙=M","differences":[{"what":"乙補充配對名單問題的根因、競品實測與排序規則；甲僅概述依客服回饋調整推薦規則。","hiring_meaning":"乙讓主管可追問如何驗證根因、選擇規則及衡量改善，對招募流程優化更具體；不據此認定甲欠缺能力。","type":"capability"},{"what":"兩版留存數值與非因果限定相同；乙另交代本人擬定資料表欄位、DBA取數與試算表比對。","hiring_meaning":"乙更清楚界定分析分工，可驗證資料口徑、年化方法與選樣偏差；相同留存結果不提高能力評價。","type":"measurement"}],"preference":"乙","reason":"偏好乙，因配對規則改善提供可追問的問題診斷鏈，取數分工也使資料導向能力更易驗證；不是因數字較多。兩版仍須面試確認敏捷實務、中英文PRD與HRIS經驗範圍。","evidence_甲":["AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。與資料科學團隊合作，定義使用情境與驗收標準，依客服測試回饋調整推薦規則。","需求管線觸及 1,279 家活躍付費廠商，約占全站 66,150 家的 1.9%（全站基準日 2026/04/30）。比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。"],"evidence_乙":["客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。","需求管線觸及 1,279 家活躍付費廠商，約占全站 66,150 家的 1.9%（全站基準日 2026/04/30）。由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。"]}
```

## 版本比較｜jd11｜順序 甲=K 乙=M｜model_id: unknown
- 偏好：乙（揭盲：M）
| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 乙補充配對名單問題的根因、競品實測與排序規則；甲僅概述依客服回饋調整推薦規則。 | 乙讓主管可追問如何驗證根因、選擇規則及衡量改善，對招募流程優化更具體；不據此認定甲欠缺能力。 | capability | AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。與資料科學團隊合作，定義使用情境與驗收標準，依客服測試回饋調整推薦規則。 | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 |
| 2 | 兩版留存數值與非因果限定相同；乙另交代本人擬定資料表欄位、DBA取數與試算表比對。 | 乙更清楚界定分析分工，可驗證資料口徑、年化方法與選樣偏差；相同留存結果不提高能力評價。 | measurement | 需求管線觸及 1,279 家活躍付費廠商，約占全站 66,150 家的 1.9%（全站基準日 2026/04/30）。比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 需求管線觸及 1,279 家活躍付費廠商，約占全站 66,150 家的 1.9%（全站基準日 2026/04/30）。由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |
- 理由（≤120 字）：偏好乙，因配對規則改善提供可追問的問題診斷鏈，取數分工也使資料導向能力更易驗證；不是因數字較多。兩版仍須面試確認敏捷實務、中英文PRD與HRIS經驗範圍。


# jd14｜逐次輸出


## A-jd14-K｜履歷K

```json
{"rubric_version": "4.2", "resume_id": "K", "job_id": "jd14", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd14-K", "human_calibrated": false, "requirements": [{"id": "R01", "text": "3年以上Growth PM經驗", "type": "required", "status": "partial", "evidence": ["訂閱制 B2C App 與雙邊媒合平台。"], "blocks_interview": false, "reason": "2018–2022有成長相關案例，需確認成長職責持續範圍。"}, {"id": "R02", "text": "獨立撰寫PRD／User Flow／Wireframe", "type": "required", "status": "supported", "evidence": ["以 Use Case、Wireframe 定義業務流程與畫面"], "blocks_interview": false, "reason": "主責規劃並整理PRD，足以支持面試。"}, {"id": "R03", "text": "熟悉GA4", "type": "required", "status": "partial", "evidence": ["GA4"], "blocks_interview": false, "reason": "技能清單列出，需實際分析案例。"}, {"id": "R04", "text": "熟悉Firebase", "type": "required", "status": "unknown", "evidence": [], "blocks_interview": false, "reason": "未提供，不推論不會；面試確認即可。"}, {"id": "R05", "text": "數據分析能力", "type": "required", "status": "supported", "evidence": ["以 Android 售價不變作對照"], "blocks_interview": false, "reason": "實驗及留存分析支持。"}, {"id": "R06", "text": "跨部門溝通能力", "type": "required", "status": "supported", "evidence": ["與 CodaPay 新加坡技術團隊協調串接"], "blocks_interview": false, "reason": "另有工程、QA、客服協作。"}, {"id": "R07", "text": "全生命週期成長策略與Growth Funnel", "type": "required", "status": "partial", "evidence": ["配合行銷導入原 iOS App 下架後的用戶"], "blocks_interview": false, "reason": "有導流、付費與留存線索，缺完整漏斗策略案例。"}, {"id": "R08", "text": "訂閱與會員轉換優化", "type": "required", "status": "supported", "evidence": ["規劃 VIP 訂閱、點數付費牆與精選置頂曝光"], "blocks_interview": false, "reason": "訂閱付費牆、定價及付款渠道直接相關。"}, {"id": "R09", "text": "識別成長機會與探索商業模式", "type": "required", "status": "supported", "evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "blocks_interview": false, "reason": "付款與訂閱方案能支持商業判斷面試。"}, {"id": "R10", "text": "A/B Test與產品實驗", "type": "required", "status": "supported", "evidence": ["定價實驗採原價、iOS 降價、還原原價三階段"], "blocks_interview": false, "reason": "準實驗設計可轉移，隨機化A/B方法待核對。"}], "dimensions": [{"id": "positioning", "rating": "足夠", "evidence": ["涵蓋訂閱制社交 App、網紅媒合及企業招募系統。"], "missing": ["近期為B2B招募，需釐清轉用影音訂閱的想法。"], "issue_ids": []}, {"id": "role_evidence", "rating": "足夠", "evidence": ["KOOL 訂閱與付費牆規劃上線"], "missing": ["成長職責年資、全漏斗策略及工具實用待確認。"], "issue_ids": ["I01", "I02"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": ["定價實驗干擾因素在衡量維度追問。"], "issue_ids": []}, {"id": "outcome_quality", "rating": "足夠", "evidence": ["為觀察差異，非因果。"], "missing": ["付款占比不代表增量營收；實驗因果與留存口徑待核。"], "issue_ids": ["I03", "I04"]}, {"id": "ownership", "rating": "強", "evidence": ["由我主責規劃，與工程團隊密切協作"], "missing": ["成長策略中的最終決策權可面試確認。"], "issue_ids": []}, {"id": "readability", "rating": "足夠", "evidence": ["曾設計定價實驗、規劃網頁付款"], "missing": ["可將訂閱代表案例提前，屬編輯建議。"], "issue_ids": []}], "results": [{"quote": "定價實驗採原價、iOS 降價、還原原價三階段", "kinds": ["decision", "output"]}, {"quote": "相對變化約多 28%", "kinds": ["outcome"]}, {"quote": "Peach 網頁付款占營收由 24% 至 80% 以上", "kinds": ["outcome"]}, {"quote": "KOOL 訂閱與付費牆規劃上線", "kinds": ["output"]}, {"quote": "為觀察差異，非因果。", "kinds": ["outcome"]}, {"quote": "目前專案仍在開發中", "kinds": ["decision", "in_progress"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["KOOL 訂閱與付費牆規劃上線"], "application_note": "訂閱與實驗經驗可轉移"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "近期B2B與影音客群有差異"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "application_note": "本人規劃及協作邊界清楚"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "流程改變可辨識，仍需核口徑"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "有具體風險取捨"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["近 10 年 PM 經驗，經手 6 款產品"], "application_note": "可見產品領域與責任變化"}, {"rule_id": "HR07", "status": "partial", "resume_evidence": ["GA4"], "application_note": "協作用過，分析工具實用待核"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["曾設計定價實驗、規劃網頁付款"], "application_note": "摘要可快速找到成長相關性"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["為觀察差異，非因果。"], "application_note": "已限制歸因，仍需核量測方法"}, {"rule_id": "HR10", "status": "supported", "resume_evidence": ["我希望將更多心力放回產品策略"], "application_note": "方向與策略型成長職位相容"}, {"rule_id": "HR11", "status": "not_applicable", "resume_evidence": [], "application_note": "摘要無地點語言等硬性限制"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["以 Android 售價不變作對照"], "application_note": "值得面試，驗證漏斗與工具深度"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["訂閱制 B2C App 與雙邊媒合平台。"], "evidence_type": "context", "source_ids": [], "interview_question": "如何把訂閱社交經驗轉用影音？"}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["最大宗是溝通管道中斷"], "evidence_type": "decision", "source_ids": [], "interview_question": "工單分群如何影響優先順序？"}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "evidence_type": "decision", "source_ids": [], "interview_question": "比較過哪些替代方案？"}, {"rule_id": "HM04", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "evidence_type": "decision", "source_ids": [], "interview_question": "怎麼衡量付款渠道淨收益？"}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "partial", "resume_evidence": ["為觀察差異，非因果。"], "evidence_type": "outcome", "source_ids": [], "interview_question": "留存年化口徑與樣本差異為何？"}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["與資料科學團隊合作，定義使用情境與驗收標準"], "evidence_type": "output", "source_ids": [], "interview_question": "推薦規則分歧如何解決？"}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "evidence_type": "output", "source_ids": [], "interview_question": "如何驗收成長實驗事件？"}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["與 CodaPay 新加坡技術團隊協調串接"], "evidence_type": "output", "source_ids": [], "interview_question": "付款例外與失敗流程如何定義？"}, {"rule_id": "HM09", "primary_dimension": "ownership", "status": "partial", "resume_evidence": ["對接 16 個需求單位"], "evidence_type": "context", "source_ids": [], "interview_question": "成長目標與預算的自主權多大？"}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["曾設計定價實驗、規劃網頁付款"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則"], "evidence_type": "decision", "source_ids": [], "interview_question": "哪個回饋改變了原本假設？"}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["定價實驗採原價、iOS 降價、還原原價三階段"], "evidence_type": "decision", "source_ids": [], "interview_question": "請帶去識別化實驗設計與分析。"}, {"rule_id": "HM13", "primary_dimension": "method", "status": "not_applicable", "resume_evidence": [], "evidence_type": null, "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HR01", "source_ids": [], "application_note": "面試追問，不阻擋邀約", "context_limit": "僅履歷文字自述，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "訂閱制 B2C App 與雙邊媒合平台。", "reason": "相關任期超過三年，但Growth專責跨度及全漏斗目標未交代；面試核對，非阻擋。", "suggestion": "補實際成長職責期間、漏斗階段、目標與本人範圍。"}, {"id": "I02", "rule_id": "HR07", "source_ids": [], "application_note": "面試追問，不阻擋邀約", "context_limit": "僅履歷文字自述，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "GA4", "reason": "僅工具列名，Firebase未呈現；追問事件、分析及實驗實用。", "suggestion": "若曾使用，補一例GA4或Firebase事件與決策用途；未用則誠實說明。"}, {"id": "I03", "rule_id": "HM05", "source_ids": [], "application_note": "面試追問，不阻擋邀約", "context_limit": "僅履歷文字自述，未外部查證", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "相對變化約多 28%", "reason": "跨平台時序比較可能受族群與時期干擾；需追問能支持何種定價結論。", "suggestion": "交代樣本、口徑、季節或行銷變化及隨機化限制。"}, {"id": "I04", "rule_id": "HR09", "source_ids": [], "application_note": "面試追問，不阻擋邀約", "context_limit": "僅履歷文字自述，未外部查證", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "Peach 網頁付款占營收由 24% 至 80% 以上", "reason": "占比改變不能單獨證明營收增量；留存年化亦需核對，影響成效解讀。", "suggestion": "補可公開的總營收或淨收益方向與限制，並說明留存年化方法。"}], "decision": {"recommendation": "interview", "evidence": ["KOOL 訂閱與付費牆規劃上線", "以 Android 售價不變作對照", "以 Use Case、Wireframe 定義業務流程與畫面"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["訂閱付費牆與定價實驗直接相關", "具業務流程、規格及跨部門交付證據", "決策取捨及量測限制清楚"], "key_gaps": ["Growth職責跨度與完整漏斗策略", "GA4實用及Firebase經驗", "實驗干擾與商業增量衡量"], "strengths": ["訂閱付費牆具體而直接相關", "風險與使用者流程取捨清楚", "本人規劃與跨部門責任邊界明確"], "interview_questions": ["哪些期間以Growth為主要職責？請以一個完整漏斗說明目標與責任。", "GA4和Firebase實際用於哪些事件、受眾及決策？", "如何設計影音會員從啟用到續訂的實驗？", "定價實驗如何排除平台族群、季節與行銷變化？", "網頁付款占比提高時，總營收及實收成本有何變化？", "留存如何年化，樣本選擇與重複廠商如何處理？"], "editorial_appendix": ["可提前訂閱與定價案例，便於影音Growth職缺閱讀；不改變能力判斷。"], "spectrum": {"level": 8, "uncertainty_levels": 1, "basis": "多個相關案例、明確取捨與有期間及限制的衡量；影音全漏斗及工具深度留面試驗證。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷K｜第 1 輪｜model_id: unknown

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「KOOL 訂閱與付費牆規劃上線」與定價實驗直接相關，足以約談。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 涵蓋訂閱制社交 App、網紅媒合及企業招募系統。 | 近期為B2B招募，需釐清轉用影音訂閱的想法。 |
| role_evidence | 足夠 | KOOL 訂閱與付費牆規劃上線 | 成長職責年資、全漏斗策略及工具實用待確認。 |
| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 定價實驗干擾因素在衡量維度追問。 |
| outcome_quality | 足夠 | 為觀察差異，非因果。 | 付款占比不代表增量營收；實驗因果與留存口徑待核。 |
| ownership | 強 | 由我主責規劃，與工程團隊密切協作 | 成長策略中的最終決策權可面試確認。 |
| readability | 足夠 | 曾設計定價實驗、規劃網頁付款 | 可將訂閱代表案例提前，屬編輯建議。 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 3年以上Growth PM經驗 | 必要 | partial | 訂閱制 B2C App 與雙邊媒合平台。 | 2018–2022有成長相關案例，需確認成長職責持續範圍。 |
| 獨立撰寫PRD／User Flow／Wireframe | 必要 | supported | 以 Use Case、Wireframe 定義業務流程與畫面 | 主責規劃並整理PRD，足以支持面試。 |
| 熟悉GA4 | 必要 | partial | GA4 | 技能清單列出，需實際分析案例。 |
| 熟悉Firebase | 必要 | unknown | 未呈現 | 未提供，不推論不會；面試確認即可。 |
| 數據分析能力 | 必要 | supported | 以 Android 售價不變作對照 | 實驗及留存分析支持。 |
| 跨部門溝通能力 | 必要 | supported | 與 CodaPay 新加坡技術團隊協調串接 | 另有工程、QA、客服協作。 |
| 全生命週期成長策略與Growth Funnel | 必要 | partial | 配合行銷導入原 iOS App 下架後的用戶 | 有導流、付費與留存線索，缺完整漏斗策略案例。 |
| 訂閱與會員轉換優化 | 必要 | supported | 規劃 VIP 訂閱、點數付費牆與精選置頂曝光 | 訂閱付費牆、定價及付款渠道直接相關。 |
| 識別成長機會與探索商業模式 | 必要 | supported | 依抽成、稅、手續費及撥款週期做實收試算 | 付款與訂閱方案能支持商業判斷面試。 |
| A/B Test與產品實驗 | 必要 | supported | 定價實驗採原價、iOS 降價、還原原價三階段 | 準實驗設計可轉移，隨機化A/B方法待核對。 |

JD未列加分項；責任項按工作要求對照。無明文必要條件被證據否定。Firebase未知與年資部分支持可在面試確認，不構成先行阻擋。

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | KOOL 訂閱與付費牆規劃上線 | 訂閱與實驗經驗可轉移 |
| HR02 | supported | 企業端招募系統全模組與求職端公司頁 | 近期B2B與影音客群有差異 |
| HR03 | supported | 由我主責規劃，與工程團隊密切協作 | 本人規劃及協作邊界清楚 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 流程改變可辨識，仍需核口徑 |
| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 有具體風險取捨 |
| HR06 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 可見產品領域與責任變化 |
| HR07 | partial | GA4 | 協作用過，分析工具實用待核 |
| HR08 | supported | 曾設計定價實驗、規劃網頁付款 | 摘要可快速找到成長相關性 |
| HR09 | partial | 為觀察差異，非因果。 | 已限制歸因，仍需核量測方法 |
| HR10 | supported | 我希望將更多心力放回產品策略 | 方向與策略型成長職位相容 |
| HR11 | not_applicable | 未提供／不適用 | 摘要無地點語言等硬性限制 |
| HR12 | supported | 以 Android 售價不變作對照 | 值得面試，驗證漏斗與工具深度 |
| HM01 | supported | 訂閱制 B2C App 與雙邊媒合平台。 | 訂閱商模可轉移，影音經驗待核 |
| HM02 | supported | 最大宗是溝通管道中斷 | 使用者訊號影響優先順序 |
| HM03 | supported | 選擇首次登入引導確認、不強迫修改 | 有具體替代方案與風險考量 |
| HM04 | supported | 依抽成、稅、手續費及撥款週期做實收試算 | 具成本與付費方案判斷 |
| HM05 | partial | 為觀察差異，非因果。 | 驗證因果及年化口徑 |
| HM06 | supported | 與資料科學團隊合作，定義使用情境與驗收標準 | 責任邊界清楚 |
| HM07 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 交付驗收證據充分 |
| HM08 | supported | 與 CodaPay 新加坡技術團隊協調串接 | 符合一般PM技術協作要求 |
| HM09 | partial | 對接 16 個需求單位 | 核對成長目標自主權 |
| HM10 | supported | 曾設計定價實驗、規劃網頁付款 | 能辨識相關代表作 |
| HM11 | supported | 依客服測試回饋調整推薦規則 | 回饋有轉成產品調整 |
| HM12 | supported | 定價實驗採原價、iOS 降價、還原原價三階段 | 相關案例足以支持約談 |
| HM13 | not_applicable | 不適用 | 方法項，不評候選人能力 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「KOOL 訂閱與付費牆規劃上線」對應訂閱轉換。 |
| 2 | 「以 Android 售價不變作對照」提供產品實驗討論基礎。 |
| 3 | 「與 QA 制定 UAT 驗收案例、排定上線計畫」支持交付。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | Growth職責跨度與完整漏斗 | 哪些期間主責Growth？如何訂定各階段指標？ |
| 2 | GA4實用與Firebase | 實作過哪些事件及分析，如何影響決策？ |
| 3 | 成效歸因與增量 | 定價干擾如何控制？付款占比與淨收益、留存年化如何解讀？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 尚凡KOOL條列｜「KOOL 訂閱與付費牆規劃上線」｜訂閱與付費牆範圍對應會員變現。
- 1111改版條列｜「選擇首次登入引導確認、不強迫修改」｜顯示降低登入阻力的風險取捨。
- 1111功能交付條列｜「由我主責規劃，與工程團隊密切協作」｜區分本人規劃與團隊實作，利於核對權責。

**可改進（4 點）**：

- 位置：尚凡任期與產品說明
- 原句：訂閱制 B2C App 與雙邊媒合平台。
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：相關任期超過三年，但Growth專責跨度及全漏斗目標未交代；面試核對，非阻擋。
- 建議方向：補實際成長職責期間、漏斗階段、目標與本人範圍。

- 位置：研究與數據技能
- 原句：GA4
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：僅工具列名，Firebase未呈現；追問事件、分析及實驗實用。
- 建議方向：若曾使用，補一例GA4或Firebase事件與決策用途；未用則誠實說明。

- 位置：尚凡定價實驗
- 原句：相對變化約多 28%
- 問題類型：measurement
- 嚴重度：interview_follow_up
- 影響：跨平台時序比較可能受族群與時期干擾；需追問能支持何種定價結論。
- 建議方向：交代樣本、口徑、季節或行銷變化及隨機化限制。

- 位置：尚凡付款／1111留存
- 原句：Peach 網頁付款占營收由 24% 至 80% 以上
- 問題類型：measurement
- 嚴重度：interview_follow_up
- 影響：占比改變不能單獨證明營收增量；留存年化亦需核對，影響成效解讀。
- 建議方向：補可公開的總營收或淨收益方向與限制，並說明留存年化方法。

**編輯附件**（不影響判斷）：可提前訂閱、定價與付款代表作。

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠
有分階段交付與跨單位規劃；定價及優先級可支持方向判斷，未推定具P&L或預算控制權。

### 8. 未測試聲明
PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run
以上均為履歷自述，非外部查證。

### 成果分類補表
| 原句／成果 | 分類 | 解讀限制 |
| :-- | :-- | :-- |
| 近 10 年 PM 經驗，經手 6 款產品 | context | 年資與產品範圍，不直接等於能力 |
| 全站活躍付費廠商約 6.6 萬家 | context | 系統規模，不是個人成效 |
| 約 50 項大項功能上線 | output | 交付數，非使用者結果 |
| 上線 111 項 Roadmap 細項 | output | 不同粒度，不與大項累加 |
| 第一階段於 2025/10 離峰切換上線 | output | 第一階段完成，不代表全改版完成 |
| 停機約 1.5 小時 | outcome | 切換結果，無比較基準 |
| 十多家廠商帳號遭冒用 | context | 問題規模 |
| 上線簽章驗證 | output | 與工程協作，非本人實作 |
| 未再出現同類帳號冒用 | outcome | 目前掌握情況，非完整監測證據 |
| 需求平均處理週期由 100.4 天降至 30.9 天 | outcome | Q1/Q2穩態比較，追問案件組成 |
| 完成 1,726／1,857 張需求與問題單 | output | 截至09/29處理量 |
| 需求管線觸及 1,279 家活躍付費廠商 | context | 接觸樣本，非全站成長 |
| 該群年化留存 81.2%，同期全站 74.2% | outcome | 名冊快照觀察差異，非因果 |
| AI 功能已上線公司簡介生成 | output | 另含工作說明及推薦人才，無成效量測 |
| 依客服測試回饋調整推薦規則 | decision | 回饋改變規則 |
| 降價期 iOS 非續訂營收較基準期增 5% | outcome | Android減18%，跨平台相對變化非隨機A/B |
| 還原原價後 iOS 較基準期減 65% | outcome | 時序干擾待核 |
| 依結果全面調降售價 | decision | 策略行動，非調價後成果 |
| Peach 網頁付款占營收由 24% 至 80% 以上 | outcome | 渠道占比，不等於總營收成長 |
| 規劃由 App 內購轉向網頁付款 | decision/output | 與CodaPay串接 |
| KOOL 訂閱與付費牆規劃上線 | output | 多平台訂閱交付，未量測轉換 |
| 設定檔案完成、社群認證及照片門檻 | decision/output | 資格規則，不視為啟用率提升 |
| 主導 Juicy 上線 | output | 配合行銷導流 |
| 上線後 6 週男性 DAU 約 3,200 至 1.25 萬 | outcome | 產品與行銷整體表現，非個人歸因 |
| SweetRing 在地化涵蓋 | output/context | 七市場；協作人數非管理能力代理 |
| 導入 CodaPay | output | 開放多市場付款渠道 |
| 提出 7／30／90 天訂閱方案與加贈內容 | decision/output | 實收試算支持方案，不推論上線收益 |
| Newegg.com 商品資訊英翻中與校對。 | output | 與Growth關聯有限，不扣分 |
| 將信件與即時通整合排在其他新功能之前 | decision/in_progress | 仍開發中，不算已實現成效 |


## A-jd14-M｜履歷M

```json
{"rubric_version": "4.2", "resume_id": "M", "job_id": "jd14", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd14-M", "human_calibrated": false, "requirements": [{"id": "R01", "text": "3年以上Growth PM經驗", "type": "required", "status": "partial", "evidence": ["訂閱制 B2C App 與雙邊媒合平台。"], "blocks_interview": false, "reason": "2018–2022有訂閱、定價與導流案例，但專責Growth職能的年限及持續投入範圍需核對。"}, {"id": "R02", "text": "獨立撰寫PRD/User Flow/Wireframe", "type": "required", "status": "supported", "evidence": ["以 Use Case、Wireframe 定義業務流程與畫面"], "blocks_interview": false, "reason": "主責規劃並整理PRD及原型，支持流程與文件能力。"}, {"id": "R03", "text": "熟悉GA4", "type": "required", "status": "partial", "evidence": ["競品實測、GA4、世代分析、對照組實驗"], "blocks_interview": false, "reason": "列出工具但未呈現GA4事件、漏斗或決策案例。"}, {"id": "R04", "text": "熟悉Firebase", "type": "required", "status": "unknown", "evidence": [], "blocks_interview": false, "reason": "履歷未提供Firebase證據，未知不等於不符。"}, {"id": "R05", "text": "數據分析能力", "type": "required", "status": "supported", "evidence": ["為觀察差異，非因果。"], "blocks_interview": false, "reason": "提供定價對照及留存比較，能區別觀察與因果。"}, {"id": "R06", "text": "跨部門溝通能力", "type": "required", "status": "supported", "evidence": ["並與 CodaPay 新加坡技術團隊協調串接。"], "blocks_interview": false, "reason": "有工程、QA、客服與支付整合合作。"}, {"id": "R07", "text": "全生命週期成長策略與Growth Funnel", "type": "required", "status": "partial", "evidence": ["配合行銷導入原 iOS App 下架後的用戶"], "blocks_interview": false, "reason": "有導流、付費及留存個別案例，未見整體漏斗策略。"}, {"id": "R08", "text": "訂閱與會員轉換優化", "type": "required", "status": "supported", "evidence": ["KOOL 訂閱與付費牆規劃上線"], "blocks_interview": false, "reason": "具訂閱付費牆、付款路徑與價格調整實作。"}, {"id": "R09", "text": "識別成長機會與探索新商業模式", "type": "required", "status": "partial", "evidence": ["提出 7／30／90 天訂閱方案與加贈內容。"], "blocks_interview": false, "reason": "能連結成本與方案，尚需驗證新模式機會判斷。"}, {"id": "R10", "text": "A/B Test與產品實驗", "type": "required", "status": "partial", "evidence": ["以 Android 售價不變作對照"], "blocks_interview": false, "reason": "有準實驗與價格決策，未見隨機分流A/B設計。"}], "dimensions": [{"id": "positioning", "rating": "足夠", "evidence": ["涵蓋訂閱制社交 App、網紅媒合及企業招募系統。"], "missing": ["影音訂閱領域的轉移假設待面試確認。"], "issue_ids": []}, {"id": "role_evidence", "rating": "足夠", "evidence": ["KOOL 訂閱與付費牆規劃上線"], "missing": ["Growth職能年限、完整漏斗及GA4/Firebase實用深度待核對。"], "issue_ids": ["I01", "I02"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": ["價格實驗對跨平台差異的控制待追問。"], "issue_ids": ["I03"]}, {"id": "outcome_quality", "rating": "足夠", "evidence": ["為觀察差異，非因果。"], "missing": ["付款占比不是整體營收增長；留存年化算法及實驗干擾待查。"], "issue_ids": ["I03", "I04"]}, {"id": "ownership", "rating": "強", "evidence": ["由我主責規劃，與工程團隊密切協作"], "missing": ["行銷導流與產品對增長的貢獻可再拆分。"], "issue_ids": []}, {"id": "readability", "rating": "足夠", "evidence": ["曾設計定價實驗、規劃網頁付款；"], "missing": ["可提前呈現與Growth直接相關的訂閱案例。"], "issue_ids": []}], "results": [{"quote": "約 50 項大項功能上線", "kinds": ["output"]}, {"quote": "需求平均處理週期由 100.4 天降至 30.9 天", "kinds": ["outcome"]}, {"quote": "該群年化留存 81.2%，同期全站 74.2%", "kinds": ["outcome"]}, {"quote": "降價期 iOS 非續訂營收較基準期增 5%", "kinds": ["outcome"]}, {"quote": "Peach 網頁付款占營收由 24% 至 80% 以上", "kinds": ["outcome"]}, {"quote": "上線後 6 週男性 DAU 約 3,200 至 1.25 萬", "kinds": ["outcome"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["KOOL 訂閱與付費牆規劃上線"], "application_note": "訂閱與變現經驗可轉移"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁；"], "application_note": "近期B2B與影音B2C環境不同"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "application_note": "本人規劃與工程邊界清楚"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "有流程改變及比較期間"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "可見風險與使用情境取捨"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["從交友與訂閱制 App 到企業招募系統"], "application_note": "領域轉換有可辨識脈絡"}, {"rule_id": "HR07", "status": "partial", "resume_evidence": ["競品實測、GA4、世代分析、對照組實驗"], "application_note": "分析有案例，工具熟練度待核對"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["曾設計定價實驗、規劃網頁付款；"], "application_note": "摘要可找到成長相關代表作"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["為觀察差異，非因果。"], "application_note": "量測限制清楚但算法待核對"}, {"rule_id": "HR10", "status": "supported", "resume_evidence": ["接下來，我希望將更多心力放回產品策略"], "application_note": "方向與產品成長相容"}, {"rule_id": "HR11", "status": "supported", "resume_evidence": ["台北市、新北市，可接受遠端或混合辦公"], "application_note": "未見工作條件明確衝突"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["KOOL 訂閱與付費牆規劃上線"], "application_note": "案例足以約談，工具於面試核對"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["訂閱制 B2C App 與雙邊媒合平台。"], "evidence_type": "context", "source_ids": [], "interview_question": "如何把訂閱社交經驗轉移到影音會員？"}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["客服反映配對名單「少又舊」"], "evidence_type": "decision", "source_ids": [], "interview_question": "哪些用戶訊號改變你的成長假設？"}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "evidence_type": "decision", "source_ids": [], "interview_question": "定價實驗還考慮了哪些替代方案？"}, {"rule_id": "HM04", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "evidence_type": "decision", "source_ids": [], "interview_question": "如何選擇可持續的訂閱成長機會？"}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "partial", "resume_evidence": ["為觀察差異，非因果。"], "evidence_type": "outcome", "source_ids": [], "interview_question": "年化留存如何計算及控制群體差異？"}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "evidence_type": "output", "source_ids": [], "interview_question": "產品與行銷如何分工及解決優先級分歧？"}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫。"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["由我擬定取數的資料表與欄位"], "evidence_type": "output", "source_ids": [], "interview_question": "請展示GA4/Firebase事件設計與驗收案例。"}, {"rule_id": "HM09", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "evidence_type": "decision", "source_ids": [], "interview_question": "哪些成長方向與資源配置由你自主決定？"}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["曾設計定價實驗、規劃網頁付款；"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則。"], "evidence_type": "decision", "source_ids": [], "interview_question": "回饋如何轉化成規則及下一輪驗證？"}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["KOOL 訂閱與付費牆規劃上線"], "evidence_type": "output", "source_ids": [], "interview_question": "請以一個案例展示完整成長漏斗與實驗迭代。"}, {"rule_id": "HM13", "primary_dimension": "", "status": "supported", "resume_evidence": ["為觀察差異，非因果。"], "evidence_type": null, "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HR01", "source_ids": [], "application_note": "面試核對，不視為已證實不符", "context_limit": "僅依履歷文字與職缺摘要", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "訂閱制 B2C App 與雙邊媒合平台。", "reason": "三年以上Growth職能與全漏斗責任未直接界定，影響角色契合程度。", "suggestion": "補充實際承擔Growth的期間、漏斗範圍與決策責任。"}, {"id": "I02", "rule_id": "HR07", "source_ids": [], "application_note": "面試核對，不視為已證實不符", "context_limit": "僅依履歷文字與職缺摘要", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "競品實測、GA4、世代分析、對照組實驗", "reason": "GA4只列技能，Firebase未呈現，需確認能否執行本職資料分析。", "suggestion": "若確有經驗，補充事件、漏斗與Firebase應用；沒有就如實說明。"}, {"id": "I03", "rule_id": "HM05", "source_ids": [], "application_note": "面試核對，不視為已證實不符", "context_limit": "僅依履歷文字與職缺摘要", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "以 Android 售價不變作對照", "reason": "跨平台與不同期間可能有干擾，不能直接當隨機A/B因果效果。", "suggestion": "說明樣本、同期間行銷與季節變化、決策門檻及檢核。"}, {"id": "I04", "rule_id": "HR09", "source_ids": [], "application_note": "面試核對，不視為已證實不符", "context_limit": "僅依履歷文字與職缺摘要", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "該群年化留存 81.2%，同期全站 74.2%", "reason": "年化算法及選樣尚不明，付款占比也無法證明總營收提升；追問成效口徑。", "suggestion": "補充留存定義與年化方法，並區分支付結構及淨收入影響。"}], "decision": {"recommendation": "interview", "evidence": ["KOOL 訂閱與付費牆規劃上線", "以 Android 售價不變作對照"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["「KOOL 訂閱與付費牆規劃上線」支持訂閱變現實作。", "「以 Android 售價不變作對照」支持實驗及數據決策。", "「由我主責規劃，與工程團隊密切協作」支持跨部門交付。"], "key_gaps": ["Growth專責年限與全生命週期漏斗責任", "GA4及Firebase具體操作深度", "實驗控制、留存年化與收入影響口徑"], "strengths": ["尚凡｜「KOOL 訂閱與付費牆規劃上線」｜直接對應會員轉換產品。", "尚凡｜「以 Android 售價不變作對照」｜展示定價決策的比較依據。", "1111｜「為觀察差異，非因果。」｜尊重留存分析的推論限制。"], "interview_questions": ["請界定至少三年的Growth工作期間、投入比例與漏斗責任。", "請展示GA4事件及漏斗報表；Firebase用過哪些功能？", "如何為MyVideo設計Activation、付費及留存指標？", "價格實驗如何處理平台差異、樣本量與行銷干擾？", "年化留存的分母、算法及觀察期間是什麼？", "網頁付款占比提升對淨收入、轉換及會員留存有何影響？", "請展示一份由你獨立定義的流程、PRD與驗收依據。"], "editorial_appendix": ["可將訂閱、實驗、付款案例前移，減少讀者定位Growth證據的成本。"], "spectrum": {"level": 7, "uncertainty_levels": 1, "basis": "多個訂閱、變現與交付案例支持面試；工具深度與完整Growth責任尚待驗證。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷 M｜第 1 輪｜model_id: unknown

### 1. 結論
- 招聘決定：interview
- Level：7（±1）
- 一句話理由：「KOOL 訂閱與付費牆規劃上線」支持成長產品面試，工具深度待核對。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 涵蓋訂閱制社交 App、網紅媒合及企業招募系統。 | 影音訂閱領域的轉移假設待面試確認。 |
| role_evidence | 足夠 | KOOL 訂閱與付費牆規劃上線 | Growth職能年限、完整漏斗及GA4/Firebase實用深度待核對。 |
| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 價格實驗對跨平台差異的控制待追問。 |
| outcome_quality | 足夠 | 為觀察差異，非因果。 | 付款占比不是整體營收增長；留存年化算法及實驗干擾待查。 |
| ownership | 強 | 由我主責規劃，與工程團隊密切協作 | 行銷導流與產品對增長的貢獻可再拆分。 |
| readability | 足夠 | 曾設計定價實驗、規劃網頁付款； | 可提前呈現與Growth直接相關的訂閱案例。 |

### 3. JD 條件對照
職責亦依工作需求列入；只有明文必要且有反證才阻擋，本文無反證。
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 3年以上Growth PM經驗 | 必要 | partial | 訂閱制 B2C App 與雙邊媒合平台。 | 2018–2022有訂閱、定價與導流案例，但專責Growth職能的年限及持續投入範圍需核對。 |
| 獨立撰寫PRD/User Flow/Wireframe | 必要 | supported | 以 Use Case、Wireframe 定義業務流程與畫面 | 主責規劃並整理PRD及原型，支持流程與文件能力。 |
| 熟悉GA4 | 必要 | partial | 競品實測、GA4、世代分析、對照組實驗 | 列出工具但未呈現GA4事件、漏斗或決策案例。 |
| 熟悉Firebase | 必要 | unknown | 未呈現 | 履歷未提供Firebase證據，未知不等於不符。 |
| 數據分析能力 | 必要 | supported | 為觀察差異，非因果。 | 提供定價對照及留存比較，能區別觀察與因果。 |
| 跨部門溝通能力 | 必要 | supported | 並與 CodaPay 新加坡技術團隊協調串接。 | 有工程、QA、客服與支付整合合作。 |
| 全生命週期成長策略與Growth Funnel | 必要 | partial | 配合行銷導入原 iOS App 下架後的用戶 | 有導流、付費及留存個別案例，未見整體漏斗策略。 |
| 訂閱與會員轉換優化 | 必要 | supported | KOOL 訂閱與付費牆規劃上線 | 具訂閱付費牆、付款路徑與價格調整實作。 |
| 識別成長機會與探索新商業模式 | 必要 | partial | 提出 7／30／90 天訂閱方案與加贈內容。 | 能連結成本與方案，尚需驗證新模式機會判斷。 |
| A/B Test與產品實驗 | 必要 | partial | 以 Android 售價不變作對照 | 有準實驗與價格決策，未見隨機分流A/B設計。 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | KOOL 訂閱與付費牆規劃上線 | 訂閱與變現經驗可轉移 |
| HR02 | supported | 企業端招募系統全模組與求職端公司頁； | 近期B2B與影音B2C環境不同 |
| HR03 | supported | 由我主責規劃，與工程團隊密切協作 | 本人規劃與工程邊界清楚 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 有流程改變及比較期間 |
| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 可見風險與使用情境取捨 |
| HR06 | supported | 從交友與訂閱制 App 到企業招募系統 | 領域轉換有可辨識脈絡 |
| HR07 | partial | 競品實測、GA4、世代分析、對照組實驗 | 分析有案例，工具熟練度待核對 |
| HR08 | supported | 曾設計定價實驗、規劃網頁付款； | 摘要可找到成長相關代表作 |
| HR09 | partial | 為觀察差異，非因果。 | 量測限制清楚但算法待核對 |
| HR10 | supported | 接下來，我希望將更多心力放回產品策略 | 方向與產品成長相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公 | 未見工作條件明確衝突 |
| HR12 | supported | KOOL 訂閱與付費牆規劃上線 | 案例足以約談，工具於面試核對 |
| HM01 | supported | 訂閱制 B2C App 與雙邊媒合平台。 | 訂閱產品經驗可轉移 |
| HM02 | supported | 客服反映配對名單「少又舊」 | 客服痛點連到規則調整 |
| HM03 | supported | 選擇首次登入引導確認、不強迫修改 | 有替代方案與風險取捨 |
| HM04 | supported | 依抽成、稅、手續費及撥款週期做實收試算 | 成本與方案有連結 |
| HM05 | partial | 為觀察差異，非因果。 | 量測限制需面試確認 |
| HM06 | supported | 由我主責規劃，與工程團隊密切協作 | 本人與協作者邊界清楚 |
| HM07 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫。 | 規格連到驗收上線 |
| HM08 | supported | 由我擬定取數的資料表與欄位 | 一般PM技術協作足夠 |
| HM09 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 自主統籌範圍支持資深IC |
| HM10 | supported | 曾設計定價實驗、規劃網頁付款； | 可找到成長代表案例 |
| HM11 | supported | 依客服測試回饋調整推薦規則。 | 有依回饋修正案例 |
| HM12 | supported | KOOL 訂閱與付費牆規劃上線 | 具約談價值，核對完整漏斗 |
| HM13 | supported | 為觀察差異，非因果。 | 按JD取證，不作作者或人格推論 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「KOOL 訂閱與付費牆規劃上線」支持訂閱變現實作。 |
| 2 | 「以 Android 售價不變作對照」支持實驗及數據決策。 |
| 3 | 「由我主責規劃，與工程團隊密切協作」支持跨部門交付。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | Growth專責年限與全生命週期漏斗責任 | 請界定至少三年的Growth工作期間、投入比例與漏斗責任。 |
| 2 | GA4及Firebase具體操作深度 | 請展示GA4事件及漏斗報表；Firebase用過哪些功能？ |
| 3 | 實驗控制、留存年化與收入影響口徑 | 請解釋實驗干擾、留存算法與付款的淨收入影響。 |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 尚凡｜「KOOL 訂閱與付費牆規劃上線」｜直接對應會員轉換產品。
- 尚凡｜「以 Android 售價不變作對照」｜展示定價決策的比較依據。
- 1111｜「為觀察差異，非因果。」｜尊重留存分析的推論限制。

**可改進（4 點）**：

- 位置：尚凡經歷
- 原句：訂閱制 B2C App 與雙邊媒合平台。
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：三年以上Growth職能與全漏斗責任未直接界定，影響角色契合程度。
- 建議方向：補充實際承擔Growth的期間、漏斗範圍與決策責任。

- 位置：專業技能
- 原句：競品實測、GA4、世代分析、對照組實驗
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：GA4只列技能，Firebase未呈現，需確認能否執行本職資料分析。
- 建議方向：若確有經驗，補充事件、漏斗與Firebase應用；沒有就如實說明。

- 位置：尚凡定價實驗
- 原句：以 Android 售價不變作對照
- 問題類型：measurement
- 嚴重度：interview_follow_up
- 影響：跨平台與不同期間可能有干擾，不能直接當隨機A/B因果效果。
- 建議方向：說明樣本、同期間行銷與季節變化、決策門檻及檢核。

- 位置：1111留存分析／尚凡網頁付款
- 原句：該群年化留存 81.2%，同期全站 74.2%
- 問題類型：measurement
- 嚴重度：interview_follow_up
- 影響：年化算法及選樣尚不明，付款占比也無法證明總營收提升；追問成效口徑。
- 建議方向：補充留存定義與年化方法，並區分支付結構及淨收入影響。

**編輯附件**（不影響判斷）：
- 可將訂閱、實驗、付款案例前移，減少讀者定位Growth證據的成本。

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠
有明確優先級、定價與風險取捨；未憑職稱或年資認定資源管理權限。

### 8. 未測試聲明
PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run
履歷自述不是外部查證。缺口僅在主要維度登記，其他題交叉引用，不重複扣分。

### 成果分類補表
| 原句 | 分類 | 限制 |
| :-- | :-- | :-- |
| 全站活躍付費廠商約 6.6 萬家 | context | 系統規模，不是個人成果 |
| 另於 2026/01–06 上線 111 項 Roadmap 細項。 | output | 與50大項不同口徑，不相加 |
| 第一階段於 2025/10 離峰切換上線 | output | 階段交付 |
| 停機約 1.5 小時。 | outcome | 切換時間，未推論改善幅度 |
| 與工程協作於 2026/04/17 上線簽章驗證。 | output | 工程共同交付 |
| 上線後至 2026/10 未再出現同類帳號冒用。 | outcome | 依目前掌握情況，不是完整監測紀錄 |
| 完成 1,726／1,857 張需求與問題單，約 93%。 | output | 工單完成率不是使用者成效 |
| 兩案皆開發中 | decision / in_progress | 優先級已決，結果未實現 |
| 改依職缺上線日排序、20 天內不重複推薦 | decision / output | 未呈現採用或滿意度結果 |
| 需求管線觸及 1,279 家活躍付費廠商 | context | 分析群體與覆蓋率 |
| AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。 | output | 未提供使用成效 |
| 依客服測試回饋調整推薦規則。 | decision | 回饋修正 |
| 還原原價後 iOS 較基準期減 65% | outcome | 期間比較，非隨機因果 |
| 依結果全面調降售價。 | decision | 價格選擇 |
| KOOL 訂閱與付費牆規劃上線 | output | 不等於轉換提升 |
| 主導 Juicy 上線 | output | DAU為產品與行銷共同期間表現 |
| 與最多約 10 位外國實習生協作 | context / output | 無直屬管理，不當帶人 |
| 開放印尼、泰國等市場的電信帳單與超商付款。 | output | 支付方式交付 |
| 提出 7／30／90 天訂閱方案與加贈內容。 | decision / output | 方案及實收試算，未報收入結果 |
| Newegg.com 商品資訊英翻中與英文校對 | output | 非Growth直接證據 |
| 12 條分支、23 個共用 skill | output | AI工作流程規模，不是效率成效 |


## B-jd14｜揭盲：甲=M、乙=K；偏好=M

```json
{"job_id":"jd14","order":"甲=M/乙=K","differences":[{"what":"甲交代留存分析的取數需求、DBA分工及比對工具，乙僅交代快照與結果。","hiring_meaning":"可針對指標定義、年化方式與取數正確性追問，較能界定候選人的分析責任；兩版均聲明非因果，不據此認定留存提升。","type":"measurement"},{"what":"甲另有從配對名單問題追查排序根因並調整規則的案例；乙的問題排序案例主要在自傳呈現。","hiring_meaning":"甲增加可驗證的問題診斷與產品規則決策素材，可追問如何衡量推薦品質及留存；尚不能推論已有成長成效。","type":"capability"}],"preference":"甲","reason":"甲更清楚交代留存分析的本人角色與取數分工，另提供配對規則調整案例，讓主管能追問分析設計與產品決策；兩版相同的訂閱、定價實驗不重複加分，GA4實作與Firebase仍待驗證。","evidence_甲":["由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。","客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。"],"evidence_乙":["比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。","例如廠商抱怨工單中，最大宗是溝通管道中斷，我便將信件與即時通整合排在其他新功能之前，目前專案仍在開發中。"]}
```

## 版本比較｜jd14｜順序 甲=M 乙=K｜model_id: unknown
- 偏好：甲（揭盲：M）

| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 甲交代留存分析的取數需求、DBA分工及比對工具，乙僅交代快照與結果。 | 可針對指標定義、年化方式與取數正確性追問，較能界定候選人的分析責任；兩版均聲明非因果，不據此認定留存提升。 | measurement | 由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |
| 2 | 甲另有從配對名單問題追查排序根因並調整規則的案例；乙的問題排序案例主要在自傳呈現。 | 甲增加可驗證的問題診斷與產品規則決策素材，可追問如何衡量推薦品質及留存；尚不能推論已有成長成效。 | capability | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 | 例如廠商抱怨工單中，最大宗是溝通管道中斷，我便將信件與即時通整合排在其他新功能之前，目前專案仍在開發中。 |

- 理由（≤120 字）：甲更清楚交代留存分析的本人角色與取數分工，另提供配對規則調整案例，讓主管能追問分析設計與產品決策；兩版相同的訂閱、定價實驗不重複加分，GA4實作與Firebase仍待驗證。


# jd20｜逐次輸出


## A-jd20-K｜履歷K

```json
{"rubric_version": "4.2", "resume_id": "K", "job_id": "jd20", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd20-K", "human_calibrated": false, "requirements": [{"id": "R01", "text": "5–8年以上B2B/B2G產品或專案管理", "type": "required", "status": "partial", "evidence": ["近 10 年 PM 經驗，經手 6 款產品"], "blocks_interview": false, "reason": "企業招募系統自2022/08起；早期雙邊平台企業側責任與年資待核對，非已證不符。"}, {"id": "R02", "text": "接近母語英語口說及書寫", "type": "required", "status": "partial", "evidence": ["英文 TOEIC 980、TOEFL iBT 93"], "blocks_interview": false, "reason": "有測驗與海外協作線索，不能替代近母語工作表現驗證。"}, {"id": "R03", "text": "溝通及關係人管理", "type": "required", "status": "supported", "evidence": ["對接 16 個需求單位"], "blocks_interview": false, "reason": "需求、工程、QA、客服與海外技術團隊協作具體。"}, {"id": "R04", "text": "需求、PRD、路線圖、待辦、時程與風險管理", "type": "required", "status": "supported", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "blocks_interview": false, "reason": "改版、登入安全與交付流程直接相關。"}, {"id": "R05", "text": "獨立使用SQL/BI/試算表查詢分析", "type": "required", "status": "partial", "evidence": ["比對 2026/04/30、07/07 名冊快照"], "blocks_interview": false, "reason": "有分析與Excel線索，獨立取數操作及來源仍需工作樣本。"}, {"id": "R06", "text": "AI工具與工作流整合", "type": "required", "status": "supported", "evidence": ["Claude Code 多分支流程與共用 skill 庫"], "blocks_interview": false, "reason": "規格、資料整理分析應用明確；外部工具自動串接深度待問。"}, {"id": "R07", "text": "對防詐及風險偵測的熱情", "type": "required", "status": "unknown", "evidence": [], "blocks_interview": false, "reason": "安全事件有實務，未直接表達防詐職涯動機；面試確認。"}, {"id": "R08", "text": "防詐、資安、風險或信任產品", "type": "preferred", "status": "supported", "evidence": ["與工程協作於 2026/04/17 上線簽章驗證"], "blocks_interview": false, "reason": "登入帳號冒用案例相關，尚非專職防詐產品。"}, {"id": "R09", "text": "企業或政府客戶，尤其海外市場", "type": "preferred", "status": "partial", "evidence": ["企業端招募系統全模組與求職端公司頁"], "blocks_interview": false, "reason": "企業端直接相關；海外經驗多為B2C，無政府案例。"}, {"id": "R10", "text": "技術背景或密切合作RD/AI團隊", "type": "preferred", "status": "supported", "evidence": ["與資料科學團隊合作，定義使用情境與驗收標準"], "blocks_interview": false, "reason": "工程協作與AI功能驗收具體。"}, {"id": "R11", "text": "Agile/Scrum與Jira專案管理", "type": "preferred", "status": "partial", "evidence": ["以 Kanban 推進瀑布式開發"], "blocks_interview": false, "reason": "有Kanban，未呈現Scrum及Jira實作。"}, {"id": "R12", "text": "定價、報價或成本利潤分析", "type": "preferred", "status": "supported", "evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "blocks_interview": false, "reason": "定價實驗與付款成本分析具體。"}], "dimensions": [{"id": "positioning", "rating": "足夠", "evidence": ["現任 1111 招募系統 Product Owner"], "missing": ["B2B年資適用範圍與防詐動機待確認"], "issue_ids": ["I01"]}, {"id": "role_evidence", "rating": "足夠", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "missing": ["英語、獨立查詢分析、工作流串接待驗證"], "issue_ids": ["I02", "I03"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": ["可追問選項權重及最終決策權"], "issue_ids": []}, {"id": "outcome_quality", "rating": "足夠", "evidence": ["為觀察差異，非因果"], "missing": ["安全事件監測口徑及週期資料定義待確認"], "issue_ids": ["I04"]}, {"id": "ownership", "rating": "強", "evidence": ["由我主責規劃，與工程團隊密切協作"], "missing": ["不把工程實作及行銷效果全歸本人"], "issue_ids": []}, {"id": "readability", "rating": "強", "evidence": ["企業端招募系統全模組與求職端公司頁"], "missing": ["職缺關聯可再前置；非面試障礙"], "issue_ids": []}], "results": [{"quote": "約 50 項大項功能上線", "kinds": ["output"]}, {"quote": "需求平均處理週期由 100.4 天降至 30.9 天", "kinds": ["outcome"]}, {"quote": "該群年化留存 81.2%，同期全站 74.2%", "kinds": ["outcome"]}, {"quote": "選擇首次登入引導確認、不強迫修改", "kinds": ["decision"]}, {"quote": "相對變化約多 28%", "kinds": ["outcome"]}, {"quote": "目前專案仍在開發中", "kinds": ["decision", "in_progress"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "application_note": "交付證據足以約談"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "近期企業產品範圍清楚"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "application_note": "規劃與工程分工明確"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "流程改變可追問口徑"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "具體處理既有客戶風險"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["從交友與訂閱制 App 到企業招募系統"], "application_note": "責任轉移脈絡可理解"}, {"rule_id": "HR07", "status": "partial", "resume_evidence": ["Claude Code 多分支流程與共用 skill 庫"], "application_note": "分析與英文實作待驗證"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["現任 1111 招募系統 Product Owner"], "application_note": "近期代表案例易定位"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["依目前掌握的情況"], "application_note": "安全結果需查監測定義"}, {"rule_id": "HR10", "status": "partial", "resume_evidence": ["我希望將更多心力放回產品策略"], "application_note": "確認接受一半專案管理"}, {"rule_id": "HR11", "status": "partial", "resume_evidence": ["英文 TOEIC 980、TOEFL iBT 93"], "application_note": "近母語程度需工作樣本"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["與資料科學團隊合作，定義使用情境與驗收標準"], "application_note": "相關案例支持進入面試"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "evidence_type": "context", "source_ids": [], "interview_question": "企業側服務與早期B2B年資如何界定？"}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["廠商抱怨工單中，最大宗是溝通管道中斷"], "evidence_type": "decision", "source_ids": [], "interview_question": "工單如何改變原本的優先順序？"}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "evidence_type": "decision", "source_ids": [], "interview_question": "強制修改與引導確認的風險如何比較？"}, {"rule_id": "HM04", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "evidence_type": "decision", "source_ids": [], "interview_question": "成本模型如何影響定價？"}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "partial", "resume_evidence": ["為觀察差異，非因果"], "evidence_type": "outcome", "source_ids": [], "interview_question": "年化留存如何計算，是否存在選擇偏差？"}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "evidence_type": "output", "source_ids": [], "interview_question": "需求衝突時最終由誰拍板？"}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "evidence_type": "output", "source_ids": [], "interview_question": "簽章驗證的風險與回滾條件是什麼？"}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則"], "evidence_type": "decision", "source_ids": [], "interview_question": "如何把測試回饋轉成規則與驗收？"}, {"rule_id": "HM09", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "evidence_type": "output", "source_ids": [], "interview_question": "安全事件中有哪些自主決策權？"}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["現任 1111 招募系統 Product Owner"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則"], "evidence_type": "decision", "source_ids": [], "interview_question": "哪個反例使推薦規則改變？"}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["與工程協作於 2026/04/17 上線簽章驗證"], "evidence_type": "output", "source_ids": [], "interview_question": "用英語介紹安全事件，並展示匿名分析工作樣本。"}, {"rule_id": "HM13", "primary_dimension": "", "status": "not_applicable", "resume_evidence": [], "evidence_type": null, "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HR01", "source_ids": [], "application_note": "面試驗證，非已證不符合", "context_limit": "僅履歷自述，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "近 10 年 PM 經驗，經手 6 款產品", "reason": "總PM年資不能直接當B2B/B2G年資；需確認但非已證不符。", "suggestion": "補企業側服務範圍及起訖，並面試確認防詐動機與50%專案管理意願。"}, {"id": "I02", "rule_id": "HR11", "source_ids": [], "application_note": "面試驗證，非已證不符合", "context_limit": "僅履歷自述，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "英文 TOEIC 980、TOEFL iBT 93", "reason": "測驗與協作經驗不能證明接近母語；影響客戶及BD溝通驗證。", "suggestion": "以英語需求澄清與PRD寫作樣本確認。"}, {"id": "I03", "rule_id": "HR07", "source_ids": [], "application_note": "面試驗證，非已證不符合", "context_limit": "僅履歷自述，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "Claude Code 多分支流程與共用 skill 庫", "reason": "工具使用有線索，獨立查詢與跨工具自動化深度仍待面試驗證。", "suggestion": "展示匿名試算表查詢分析及AI工作流，說明本人操作。"}, {"id": "I04", "rule_id": "HR09", "source_ids": [], "application_note": "面試驗證，非已證不符合", "context_limit": "僅履歷自述，未外部查證", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "依目前掌握的情況", "reason": "沒有再得知事件不能直接等同監測零事件；需追問來源及覆蓋率。", "suggestion": "說明事件判定、回報來源、觀察期間與限制。"}], "decision": {"recommendation": "interview", "evidence": ["與工程協作於 2026/04/17 上線簽章驗證", "與 QA 制定 UAT 驗收案例、排定上線計畫"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["「上線簽章驗證」提供風險處理相關案例", "「與 QA 制定 UAT 驗收案例」支持交付協作", "「依抽成、稅、手續費及撥款週期做實收試算」支持商業判斷"], "key_gaps": ["B2B年資範圍、防詐動機與職務比例", "近母語英語實務表現", "獨立查詢分析及AI自動化深度"], "strengths": ["近期企業產品與安全事件直接相關", "需求、PRD、UAT及交付責任具體", "取捨與結果限制明確，避免把相關當因果"], "interview_questions": ["請界定各段B2B/B2G產品或專案年資及企業客戶責任。", "為何希望投入防詐，如何看待50%專案管理？", "請以英語澄清一項企業客戶需求並寫簡短PRD。", "請展示獨立查詢試算表或BI並解讀結果的工作樣本。", "Claude Code流程如何與追蹤工具串接，如何驗證品質？", "簽章驗證後無同類事件的資訊來源、覆蓋範圍為何？", "請比較改版選項、決策權及回滾條件。", "定價實驗如何處理平台差異、季節性及樣本量？"], "editorial_appendix": ["可前置登入安全與AI協作案例，提升對位可見性，不影響能力判定。"], "spectrum": {"level": 8, "uncertainty_levels": 1, "basis": "多個相關案例、取捨與量測限制支持約談；英語及B2B年資仍需驗證，非高度全對位。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷K｜第 1 輪｜model_id: unknown

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「上線簽章驗證」與企業交付案例支持約談，英語與B2B年資待驗證。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 現任 1111 招募系統 Product Owner | B2B年資適用範圍與防詐動機待確認 |
| role_evidence | 足夠 | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 英語、獨立查詢分析、工作流串接待驗證 |
| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 可追問選項權重及最終決策權 |
| outcome_quality | 足夠 | 為觀察差異，非因果 | 安全事件監測口徑及週期資料定義待確認 |
| ownership | 強 | 由我主責規劃，與工程團隊密切協作 | 不把工程實作及行銷效果全歸本人 |
| readability | 強 | 企業端招募系統全模組與求職端公司頁 | 職缺關聯可再前置；非面試障礙 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 5–8年以上B2B/B2G產品或專案管理 | required | partial | 近 10 年 PM 經驗，經手 6 款產品 | 企業招募系統自2022/08起；早期雙邊平台企業側責任與年資待核對，非已證不符。 |
| 接近母語英語口說及書寫 | required | partial | 英文 TOEIC 980、TOEFL iBT 93 | 有測驗與海外協作線索，不能替代近母語工作表現驗證。 |
| 溝通及關係人管理 | required | supported | 對接 16 個需求單位 | 需求、工程、QA、客服與海外技術團隊協作具體。 |
| 需求、PRD、路線圖、待辦、時程與風險管理 | required | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 改版、登入安全與交付流程直接相關。 |
| 獨立使用SQL/BI/試算表查詢分析 | required | partial | 比對 2026/04/30、07/07 名冊快照 | 有分析與Excel線索，獨立取數操作及來源仍需工作樣本。 |
| AI工具與工作流整合 | required | supported | Claude Code 多分支流程與共用 skill 庫 | 規格、資料整理分析應用明確；外部工具自動串接深度待問。 |
| 對防詐及風險偵測的熱情 | required | unknown | 未呈現 | 安全事件有實務，未直接表達防詐職涯動機；面試確認。 |
| 防詐、資安、風險或信任產品 | preferred | supported | 與工程協作於 2026/04/17 上線簽章驗證 | 登入帳號冒用案例相關，尚非專職防詐產品。 |
| 企業或政府客戶，尤其海外市場 | preferred | partial | 企業端招募系統全模組與求職端公司頁 | 企業端直接相關；海外經驗多為B2C，無政府案例。 |
| 技術背景或密切合作RD/AI團隊 | preferred | supported | 與資料科學團隊合作，定義使用情境與驗收標準 | 工程協作與AI功能驗收具體。 |
| Agile/Scrum與Jira專案管理 | preferred | partial | 以 Kanban 推進瀑布式開發 | 有Kanban，未呈現Scrum及Jira實作。 |
| 定價、報價或成本利潤分析 | preferred | supported | 依抽成、稅、手續費及撥款週期做實收試算 | 定價實驗與付款成本分析具體。 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 交付證據足以約談 |
| HR02 | supported | 企業端招募系統全模組與求職端公司頁 | 近期企業產品範圍清楚 |
| HR03 | supported | 由我主責規劃，與工程團隊密切協作 | 規劃與工程分工明確 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 流程改變可追問口徑 |
| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 具體處理既有客戶風險 |
| HR06 | supported | 從交友與訂閱制 App 到企業招募系統 | 責任轉移脈絡可理解 |
| HR07 | partial | Claude Code 多分支流程與共用 skill 庫 | 分析與英文實作待驗證 |
| HR08 | supported | 現任 1111 招募系統 Product Owner | 近期代表案例易定位 |
| HR09 | partial | 依目前掌握的情況 | 安全結果需查監測定義 |
| HR10 | partial | 我希望將更多心力放回產品策略 | 確認接受一半專案管理 |
| HR11 | partial | 英文 TOEIC 980、TOEFL iBT 93 | 近母語程度需工作樣本 |
| HR12 | supported | 與資料科學團隊合作，定義使用情境與驗收標準 | 相關案例支持進入面試 |
| HM01 | supported | 企業端招募系統全模組與求職端公司頁 | 支持相關案例約談；細節面試核對 |
| HM02 | supported | 廠商抱怨工單中，最大宗是溝通管道中斷 | 支持相關案例約談；細節面試核對 |
| HM03 | supported | 選擇首次登入引導確認、不強迫修改 | 支持相關案例約談；細節面試核對 |
| HM04 | supported | 依抽成、稅、手續費及撥款週期做實收試算 | 支持相關案例約談；細節面試核對 |
| HM05 | partial | 為觀察差異，非因果 | 支持相關案例約談；細節面試核對 |
| HM06 | supported | 由我主責規劃，與工程團隊密切協作 | 支持相關案例約談；細節面試核對 |
| HM07 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 支持相關案例約談；細節面試核對 |
| HM08 | supported | 依客服測試回饋調整推薦規則 | 支持相關案例約談；細節面試核對 |
| HM09 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 支持相關案例約談；細節面試核對 |
| HM10 | supported | 現任 1111 招募系統 Product Owner | 支持相關案例約談；細節面試核對 |
| HM11 | supported | 依客服測試回饋調整推薦規則 | 支持相關案例約談；細節面試核對 |
| HM12 | supported | 與工程協作於 2026/04/17 上線簽章驗證 | 支持相關案例約談；細節面試核對 |
| HM13 | not_applicable | 不適用：評估方法由審查者負責 | 方法層，不對候選人加分 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「上線簽章驗證」提供風險處理相關案例 |
| 2 | 「與 QA 制定 UAT 驗收案例」支持交付協作 |
| 3 | 「依抽成、稅、手續費及撥款週期做實收試算」支持商業判斷 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | B2B年資範圍、防詐動機與職務比例 | 企業側年資、防詐動機及專案管理比例？ |
| 2 | 近母語英語實務表現 | 英語需求澄清與規格寫作樣本？ |
| 3 | 獨立查詢分析及AI自動化深度 | 匿名取數分析與AI工作流演示？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111安全案例｜「上線簽章驗證」｜與防詐及風險處理有直接可轉移性。
- 1111交付案例｜「與 QA 制定 UAT 驗收案例、排定上線計畫」｜支持此職一半專案交付責任。
- 1111改版案例｜「選擇首次登入引導確認、不強迫修改」｜呈現既有客戶風險與取捨。

**可改進（4 點）**：

- 位置：摘要／專業技能
- 原句：近 10 年 PM 經驗，經手 6 款產品
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：總PM年資不能直接當B2B/B2G年資；需確認但非已證不符。
- 建議方向：補企業側服務範圍及起訖，並面試確認防詐動機與50%專案管理意願。

- 位置：摘要／專業技能
- 原句：英文 TOEIC 980、TOEFL iBT 93
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：測驗與協作經驗不能證明接近母語；影響客戶及BD溝通驗證。
- 建議方向：以英語需求澄清與PRD寫作樣本確認。

- 位置：摘要／專業技能
- 原句：Claude Code 多分支流程與共用 skill 庫
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：工具使用有線索，獨立查詢與跨工具自動化深度仍待面試驗證。
- 建議方向：展示匿名試算表查詢分析及AI工作流，說明本人操作。

- 位置：1111登入安全案例
- 原句：依目前掌握的情況
- 問題類型：measurement
- 嚴重度：interview_follow_up
- 影響：沒有再得知事件不能直接等同監測零事件；需追問來源及覆蓋率。
- 建議方向：說明事件判定、回報來源、觀察期間與限制。

**編輯附件**（不影響判斷）：
- 可前置登入安全與AI協作案例，提升對位可見性，不影響能力判定。

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

### 成果分類補表
全部均為履歷自述；內部一致不代表外部查證。重複摘要及自傳案例合併列示。
| 原句／成果片段 | 分類 | 限制 |
| :-- | :-- | :-- |
| 全站活躍付費廠商約 6.6 萬家 | context | 系統規模，不是個人業績 |
| 約 50 項大項功能上線 | output | 2023/12–2026/03；不是成效 |
| 另於 2026/01–06 上線 111 項 Roadmap 細項 | output | 細項與大項不可相加 |
| 盤點出上千組重複 E-mail | context/output | 問題盤點 |
| 選擇首次登入引導確認、不強迫修改 | decision | 兼顧既有登入風險 |
| 停機約 1.5 小時 | output | 切換交付資訊，未證明最佳化 |
| 十多家廠商帳號遭冒用 | context | 事件規模 |
| 上線簽章驗證 | output | 工程協作完成 |
| 未再出現同類帳號冒用 | outcome | 依目前掌握，非完整監測證據 |
| 需求平均處理週期由 100.4 天降至 30.9 天 | outcome | Q1/Q2穩態比較；需核口徑 |
| 完成 1,726／1,857 張需求與問題單 | output | 截至09/29；完成率非使用者成效 |
| 需求管線觸及 1,279 家活躍付費廠商 | context | 覆蓋群體與分母日期不同需確認 |
| 該群年化留存 81.2%，同期全站 74.2% | outcome | 觀察差異，非因果；需核年化方法 |
| AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才 | output | 未提供採用及模型品質成效 |
| 依客服測試回饋調整推薦規則 | decision | 反饋導致修正 |
| 相對變化約多 28% | outcome | 平台對照非隨機實驗 |
| 依結果全面調降售價 | decision | 非調價後長期成果 |
| Peach 網頁付款占營收由 24% 至 80% 以上 | outcome | 付款占比，不是總營收成長 |
| KOOL 訂閱與付費牆規劃上線 | output | 多平台交付 |
| 才開放精選網紅資格 | decision | 資格門檻設計 |
| 主導 Juicy 上線 | output | 含用戶遷移配合 |
| 上線後 6 週男性 DAU 約 3,200 至 1.25 萬 | outcome | 產品及行銷整體表現 |
| 與最多約 10 位外國實習生協作 | context | 無直屬管理 |
| SweetRing 在地化涵蓋美國、墨西哥、巴西、印尼、馬來西亞、日本、韓國 7 個市場 | output/context | 市場覆蓋非商業成效 |
| 導入 CodaPay | output | 支付管道交付 |
| 提出 7／30／90 天訂閱方案與加贈內容 | output/decision | 實收試算支持，無採用結果 |
| Newegg.com 商品資訊英翻中與校對 | output | 翻譯職責，非近母語口說證明 |
| 目前專案仍在開發中 | decision/in_progress | 信件與即時通優先排序，不算已實現結果 |


## A-jd20-M｜履歷M

```json
{"rubric_version": "4.2", "resume_id": "M", "job_id": "jd20", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd20-M", "human_calibrated": false, "requirements": [{"id": "R01", "text": "5–8年以上B2B/B2G產品或專案管理", "type": "required", "status": "partial", "evidence": ["企業端招募系統全模組與求職端公司頁"], "blocks_interview": false, "reason": "明確企業端任期約4年2月；早期雙邊平台是否含企業客戶責任待確認，不能由總PM年資代替。"}, {"id": "R02", "text": "接近母語英語口說與書寫", "type": "required", "status": "partial", "evidence": ["英文 TOEIC 980、TOEFL iBT 93"], "blocks_interview": false, "reason": "有英文工作與測驗證據，但未呈現近母語客戶需求及規格溝通。"}, {"id": "R03", "text": "溝通與關係人管理", "type": "required", "status": "supported", "evidence": ["對接 16 個需求單位"], "blocks_interview": false, "reason": "需求排序、客服及工程協作有實例。"}, {"id": "R04", "text": "產品基礎、PRD、路線圖與交付風險管理", "type": "required", "status": "supported", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "blocks_interview": false, "reason": "產品規格、分階段切換及優先級證據直接。"}, {"id": "R05", "text": "獨立SQL/BI/試算表查詢分析", "type": "required", "status": "partial", "evidence": ["再以 Google Sheet 比對"], "blocks_interview": false, "reason": "可自行分析試算表；取數委託DBA，需確認能否自行查詢產品資料。"}, {"id": "R06", "text": "AI工具與工作流整合", "type": "required", "status": "supported", "evidence": ["自建 Claude Code 協作流程"], "blocks_interview": false, "reason": "規格、整理分析有用途；Jira/Confluence整合未述，屬待驗證工具遷移。"}, {"id": "R07", "text": "對防詐與風險偵測的熱情", "type": "required", "status": "partial", "evidence": ["對產品負責也包括保護使用它的人"], "blocks_interview": false, "reason": "有主動安全事件處理；防詐領域投入動機可面談。"}, {"id": "R08", "text": "防詐、資安、風險或信任產品經驗", "type": "preferred", "status": "supported", "evidence": ["與工程協作於 2026/04/17 上線簽章驗證"], "blocks_interview": false, "reason": "支持帳號安全場景，不外推完整防詐產品經驗。"}, {"id": "R09", "text": "企業或政府客戶，尤其海外市場", "type": "preferred", "status": "partial", "evidence": ["與 CodaPay 新加坡技術團隊協調串接"], "blocks_interview": false, "reason": "國內企業系統明確；海外合作是供應商串接，未證明海外企業客戶服務。"}, {"id": "R10", "text": "技術背景或與RD/AI密切協作", "type": "preferred", "status": "supported", "evidence": ["與資料科學團隊合作，定義使用情境與驗收標準"], "blocks_interview": false, "reason": "AI功能與工程協作具體。"}, {"id": "R11", "text": "Agile/Scrum與Jira經驗", "type": "preferred", "status": "partial", "evidence": ["Kanban 搭配瀑布式開發"], "blocks_interview": false, "reason": "有迭代協作，未呈現Scrum/Jira實際使用。"}, {"id": "R12", "text": "定價、報價或成本利潤分析", "type": "preferred", "status": "supported", "evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "blocks_interview": false, "reason": "定價實驗與實收試算直接相關。"}], "dimensions": [{"id": "positioning", "rating": "足夠", "evidence": ["近 10 年 PM 經驗，經手 6 款產品"], "missing": ["B2C轉企業系統脈絡清楚；B2B年資另見I01。"], "issue_ids": []}, {"id": "role_evidence", "rating": "待補", "evidence": ["自建 Claude Code 協作流程"], "missing": ["企業端年資、近母語英語及獨立查詢範圍待核對。"], "issue_ids": ["I01", "I02", "I03"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": ["可追問安全風險與登入便利的界線。"], "issue_ids": []}, {"id": "outcome_quality", "rating": "足夠", "evidence": ["為觀察差異，非因果"], "missing": ["安全事件觀察來源與期間覆蓋需核對。"], "issue_ids": ["I04"]}, {"id": "ownership", "rating": "強", "evidence": ["由我擬定取數的資料表與欄位"], "missing": ["工程、DBA與本人角色清楚；不推論本人實作。"], "issue_ids": []}, {"id": "readability", "rating": "足夠", "evidence": ["現任 1111 招募系統 Product Owner"], "missing": ["安全案例可前移以加快本職缺對位。"], "issue_ids": []}], "results": [{"quote": "約 50 項大項功能上線", "kinds": ["output"]}, {"quote": "停機約 1.5 小時", "kinds": ["output"]}, {"quote": "上線後至 2026/10 未再出現同類帳號冒用", "kinds": ["outcome"]}, {"quote": "需求平均處理週期由 100.4 天降至 30.9 天", "kinds": ["outcome"]}, {"quote": "該群年化留存 81.2%，同期全站 74.2%", "kinds": ["outcome"]}, {"quote": "依使用者旅程排優先級", "kinds": ["decision", "in_progress"]}], "hr_questions": [{"rule_id": "HR01", "status": "partial", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "核心可轉移，先核必要資格"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["正式職稱產品企劃主任"], "application_note": "近期企業系統與責任清楚"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "application_note": "可辨識規劃與工程邊界"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "有流程結果及比較期間"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["改版排在新功能職缺健檢之前"], "application_note": "有具體排序依據"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["從交友與訂閱制 App 到企業招募系統"], "application_note": "職涯轉換及方向可理解"}, {"rule_id": "HR07", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "application_note": "工具連結實際交付"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["資深產品經理｜Senior Product Manager"], "application_note": "結構可讀且案例可定位"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["依目前掌握的情況"], "application_note": "觀察不等於監測查證"}, {"rule_id": "HR10", "status": "supported", "resume_evidence": ["我希望將更多心力放回產品策略"], "application_note": "方向相容，確認50%交付期待"}, {"rule_id": "HR11", "status": "partial", "resume_evidence": ["英文 TOEIC 980、TOEFL iBT 93"], "application_note": "近母語要求仍待工作樣本"}, {"rule_id": "HR12", "status": "partial", "resume_evidence": ["與工程協作於 2026/04/17 上線簽章驗證"], "application_note": "有約談價值，先核必要條件"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["客服反映配對名單「少又舊」"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM04", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依結果全面調降售價"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "partial", "resume_evidence": ["為觀察差異，非因果"], "evidence_type": "outcome", "source_ids": [], "interview_question": null}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["交 DBA 撈取"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["第一階段於 2025/10 離峰切換上線"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["與資料科學團隊合作，定義使用情境與驗收標準"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM09", "primary_dimension": "role_evidence", "status": "partial", "resume_evidence": ["對接 16 個需求單位"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["現任 1111 招募系統 Product Owner"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "partial", "resume_evidence": ["自建 Claude Code 協作流程"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM13", "primary_dimension": "role_evidence", "status": "not_applicable", "resume_evidence": [], "evidence_type": null, "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HR01", "source_ids": [], "application_note": "先釐清企業端年資", "context_limit": "總PM年資不能直接視為B2B年資", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "近 10 年 PM 經驗，經手 6 款產品", "reason": "明確企業端任期未達5年；早期平台企業客群責任未知，影響必要資格判斷，非已證實不符。", "suggestion": "列明早期企業客戶產品的任期與責任，確認可計入的B2B經驗。"}, {"id": "I02", "rule_id": "HR11", "source_ids": [], "application_note": "先確認英語工作水準", "context_limit": "考試分數與協作不等同近母語", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "英文 TOEIC 980、TOEFL iBT 93", "reason": "近母語為明文必要條件，現有證據不足確認客戶澄清與英文PRD能力。", "suggestion": "用短段英文需求會議與英文規格樣本核對，不由測驗分數推定不符。"}, {"id": "I03", "rule_id": "HR07", "source_ids": [], "application_note": "面試核對獨立查詢", "context_limit": "JD允許試算表，不必強制SQL", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "交 DBA 撈取", "reason": "已具資料設計與分析證據，但獨立查詢範圍不明；需核對日常產品洞察的自主度。", "suggestion": "提供去識別試算表或工作樣本，說明自行篩選、查詢及解讀步驟。"}, {"id": "I04", "rule_id": "HM05", "source_ids": [], "application_note": "追問安全事件監測口徑", "context_limit": "自述未再發生不等於持續監測", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "依目前掌握的情況", "reason": "防詐產品重視漏報與風險偵測；尚不能判斷未再出現是客服回報或完整監測。", "suggestion": "補充觀察來源、涵蓋帳號與漏報限制，保留現有限定語。"}], "decision": {"recommendation": "clarify_first", "evidence": ["企業端招募系統全模組與求職端公司頁", "英文 TOEIC 980、TOEFL iBT 93"], "blocking_unknowns": ["可計入的B2B/B2G經驗是否達5年以上", "英文客戶溝通與書寫是否接近母語"]}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["「與工程協作於 2026/04/17 上線簽章驗證」支持安全交付", "「選擇首次登入引導確認、不強迫修改」有風險取捨", "「依抽成、稅、手續費及撥款週期做實收試算」支持商業理解"], "key_gaps": ["B2B/B2G必要年資未充分確認", "接近母語英語未充分確認", "獨立查詢範圍與安全監測口徑待面試驗證"], "strengths": ["安全事件有影響評估、驗證流程及上線責任。", "使用者旅程與既有資料限制轉化為明確優先級。", "定價與實收試算可轉移到企業產品商業判斷。"], "interview_questions": ["早期雙邊平台有哪些企業客戶責任、任期，可否補足五年以上B2B經驗？", "請以英文澄清一個海外客戶需求並口述PRD取捨。", "如何自行用試算表查詢產品資料，哪些步驟必須交給DBA？", "簽章驗證上線後的未再冒用，來自哪些監測或回報，漏報限制是什麼？", "請展示Claude Code流程，如何串接團隊任務或知識工具？", "為何希望投入防詐？如何看待本職缺一半產品、一半專案交付？", "定價實驗各期外部干擾與還原後跌幅，如何影響決策可信度？"], "editorial_appendix": ["可把登入安全案例前移；只改善資訊可見性，不改變能力判定。"], "spectrum": {"level": 7, "uncertainty_levels": 1, "basis": "多個交付、決策與商業案例支持約談價值；職缺必要年資及英文仍須先確認。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷 M｜第 1 輪｜model_id: unknown

### 1. 結論
- 招聘決定：clarify_first
- Level：7（±1）
- 一句話理由：「企業端招募系統全模組與求職端公司頁」有相關案例，先核企業端年資與近母語英文。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 近 10 年 PM 經驗，經手 6 款產品 | B2C轉企業系統脈絡清楚；B2B年資另見I01。 |
| role_evidence | 待補 | 自建 Claude Code 協作流程 | 企業端年資、近母語英語及獨立查詢範圍待核對。 |
| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 可追問安全風險與登入便利的界線。 |
| outcome_quality | 足夠 | 為觀察差異，非因果 | 安全事件觀察來源與期間覆蓋需核對。 |
| ownership | 強 | 由我擬定取數的資料表與欄位 | 工程、DBA與本人角色清楚；不推論本人實作。 |
| readability | 足夠 | 現任 1111 招募系統 Product Owner | 安全案例可前移以加快本職缺對位。 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 5–8年以上B2B/B2G產品或專案管理 | 必要 | partial | 企業端招募系統全模組與求職端公司頁 | 明確企業端任期約4年2月；早期雙邊平台是否含企業客戶責任待確認，不能由總PM年資代替。 |
| 接近母語英語口說與書寫 | 必要 | partial | 英文 TOEIC 980、TOEFL iBT 93 | 有英文工作與測驗證據，但未呈現近母語客戶需求及規格溝通。 |
| 溝通與關係人管理 | 必要 | supported | 對接 16 個需求單位 | 需求排序、客服及工程協作有實例。 |
| 產品基礎、PRD、路線圖與交付風險管理 | 必要 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 產品規格、分階段切換及優先級證據直接。 |
| 獨立SQL/BI/試算表查詢分析 | 必要 | partial | 再以 Google Sheet 比對 | 可自行分析試算表；取數委託DBA，需確認能否自行查詢產品資料。 |
| AI工具與工作流整合 | 必要 | supported | 自建 Claude Code 協作流程 | 規格、整理分析有用途；Jira/Confluence整合未述，屬待驗證工具遷移。 |
| 對防詐與風險偵測的熱情 | 必要 | partial | 對產品負責也包括保護使用它的人 | 有主動安全事件處理；防詐領域投入動機可面談。 |
| 防詐、資安、風險或信任產品經驗 | 加分 | supported | 與工程協作於 2026/04/17 上線簽章驗證 | 支持帳號安全場景，不外推完整防詐產品經驗。 |
| 企業或政府客戶，尤其海外市場 | 加分 | partial | 與 CodaPay 新加坡技術團隊協調串接 | 國內企業系統明確；海外合作是供應商串接，未證明海外企業客戶服務。 |
| 技術背景或與RD/AI密切協作 | 加分 | supported | 與資料科學團隊合作，定義使用情境與驗收標準 | AI功能與工程協作具體。 |
| Agile/Scrum與Jira經驗 | 加分 | partial | Kanban 搭配瀑布式開發 | 有迭代協作，未呈現Scrum/Jira實際使用。 |
| 定價、報價或成本利潤分析 | 加分 | supported | 依抽成、稅、手續費及撥款週期做實收試算 | 定價實驗與實收試算直接相關。 |

沒有已證實不符的必要條件；所有 blocks_interview=false。先釐清為資格證據不足，不是淘汰。

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | partial | 企業端招募系統全模組與求職端公司頁 | 核心可轉移，先核必要資格 |
| HR02 | supported | 正式職稱產品企劃主任 | 近期企業系統與責任清楚 |
| HR03 | supported | 由我主責規劃，與工程團隊密切協作 | 可辨識規劃與工程邊界 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 有流程結果及比較期間 |
| HR05 | supported | 改版排在新功能職缺健檢之前 | 有具體排序依據 |
| HR06 | supported | 從交友與訂閱制 App 到企業招募系統 | 職涯轉換及方向可理解 |
| HR07 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 工具連結實際交付 |
| HR08 | supported | 資深產品經理｜Senior Product Manager | 結構可讀且案例可定位 |
| HR09 | partial | 依目前掌握的情況 | 觀察不等於監測查證 |
| HR10 | supported | 我希望將更多心力放回產品策略 | 方向相容，確認50%交付期待 |
| HR11 | partial | 英文 TOEIC 980、TOEFL iBT 93 | 近母語要求仍待工作樣本 |
| HR12 | partial | 與工程協作於 2026/04/17 上線簽章驗證 | 有約談價值，先核必要條件 |
| HM01 | supported | 企業端招募系統全模組與求職端公司頁 | 企業流程與安全情境可轉移 |
| HM02 | supported | 客服反映配對名單「少又舊」 | 能由問題訊號定位規則 |
| HM03 | supported | 選擇首次登入引導確認、不強迫修改 | 有替代選項及使用風險 |
| HM04 | supported | 依結果全面調降售價 | 實驗連到商業選擇 |
| HM05 | partial | 為觀察差異，非因果 | 衡量有限制，安全觀察待核 |
| HM06 | supported | 交 DBA 撈取 | 取數責任邊界明確 |
| HM07 | supported | 第一階段於 2025/10 離峰切換上線 | 能推進分期與風險控制 |
| HM08 | supported | 與資料科學團隊合作，定義使用情境與驗收標準 | 具技術協作與驗收案例 |
| HM09 | partial | 對接 16 個需求單位 | 複雜協作成立，B2B任期待核 |
| HM10 | supported | 現任 1111 招募系統 Product Owner | 代表作與責任容易辨認 |
| HM11 | supported | 依客服測試回饋調整推薦規則 | 有回饋導致修正 |
| HM12 | partial | 自建 Claude Code 協作流程 | 可用英文工作樣本補關鍵資格 |
| HM13 | not_applicable | — | 方法檢核，不作候選人加分 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「與工程協作於 2026/04/17 上線簽章驗證」支持安全交付 |
| 2 | 「選擇首次登入引導確認、不強迫修改」有風險取捨 |
| 3 | 「依抽成、稅、手續費及撥款週期做實收試算」支持商業理解 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | B2B/B2G必要年資未充分確認 | 早期雙邊平台有哪些企業客戶責任、任期，可否補足五年以上B2B經驗？ |
| 2 | 接近母語英語未充分確認 | 請以英文澄清一個海外客戶需求並口述PRD取捨。 |
| 3 | 獨立查詢範圍與安全監測口徑待面試驗證 | 如何自行用試算表查詢產品資料，哪些步驟必須交給DBA？ 簽章驗證上線後的未再冒用，來自哪些監測或回報，漏報限制是什麼？ |

其他面試追問：
- 請展示Claude Code流程，如何串接團隊任務或知識工具？
- 為何希望投入防詐？如何看待本職缺一半產品、一半專案交付？
- 定價實驗各期外部干擾與還原後跌幅，如何影響決策可信度？

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111安全案例｜「與工程協作於 2026/04/17 上線簽章驗證」｜與風險產品交付直接相關。
- 1111改版案例｜「選擇首次登入引導確認、不強迫修改」｜把既有客戶使用限制納入決策。
- 思維特付款案例｜「依抽成、稅、手續費及撥款週期做實收試算」｜可支持企業產品成本與定價討論。

**可改進（4 點）**：

- 位置：專業摘要／企業端任期
- 原句：近 10 年 PM 經驗，經手 6 款產品
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：明確企業端任期未達5年；早期平台企業客群責任未知，影響必要資格判斷，非已證實不符。
- 建議方向：列明早期企業客戶產品的任期與責任，確認可計入的B2B經驗。

- 位置：專業技能／語言
- 原句：英文 TOEIC 980、TOEFL iBT 93
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：近母語為明文必要條件，現有證據不足確認客戶澄清與英文PRD能力。
- 建議方向：用短段英文需求會議與英文規格樣本核對，不由測驗分數推定不符。

- 位置：1111留存分析案例
- 原句：交 DBA 撈取
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：已具資料設計與分析證據，但獨立查詢範圍不明；需核對日常產品洞察的自主度。
- 建議方向：提供去識別試算表或工作樣本，說明自行篩選、查詢及解讀步驟。

- 位置：1111登入安全案例
- 原句：依目前掌握的情況
- 問題類型：measurement
- 嚴重度：interview_follow_up
- 影響：防詐產品重視漏報與風險偵測；尚不能判斷未再出現是客服回報或完整監測。
- 建議方向：補充觀察來源、涵蓋帳號與漏報限制，保留現有限定語。

**編輯附件**（不影響判斷）：
- 可把登入安全案例前移；只改善資訊可見性，不改變能力判定。

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

交付有規格、UAT與分期切換；協調有工程、客服及資料科學合作；方向選擇有排序與定價，但未呈現完整資源配置責任。

### 8. 未測試聲明
PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

履歷自述未經外部查證。未以公司、學校名氣、語氣或數字多寡評分；未將進行中項目當成果。

### 成果分類補表
| 原句或原文片段 | 分類 | 判讀限制 |
| :-- | :-- | :-- |
| 全站活躍付費廠商約 6.6 萬家 | context | 系統規模，不是個人獲客成果 |
| 約 50 項大項功能上線 | output | 有時間窗；非使用者影響 |
| 另於 2026/01–06 上線 111 項 Roadmap 細項 | output | 不可與大項功能相加 |
| 盤點出上千組重複 E-mail | context/output | 資料問題與盤點產出 |
| 選擇首次登入引導確認、不強迫修改 | decision | 兼顧既有客戶可用性 |
| 停機約 1.5 小時 | output | 切換事實，無基準不能稱改善 |
| 2026/04 十多家廠商帳號遭冒用 | context | 觸發安全盤點的事件 |
| 與工程協作於 2026/04/17 上線簽章驗證 | output | 共同交付 |
| 上線後至 2026/10 未再出現同類帳號冒用 | outcome | 有限觀察，不當完整監測證明 |
| 需求平均處理週期由 100.4 天降至 30.9 天 | outcome | Q1至Q2穩態比較，仍可追問案件組成 |
| 完成 1,726／1,857 張需求與問題單，約 93% | output | 完成率，不等於品質或產品成效 |
| 信件與即時通整合排在其他新功能之前 | decision/in_progress | 兩案仍開發中 |
| 改版排在新功能職缺健檢之前 | decision/in_progress | 排序已發生，結果尚無 |
| 改依職缺上線日排序、20 天內不重複推薦 | decision/output | 規則調整，未量測配對品質 |
| 需求管線觸及 1,279 家活躍付費廠商 | context | 管線覆蓋群體 |
| 該群年化留存 81.2%，同期全站 74.2% | outcome | 觀察差異，非因果 |
| AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才 | output | 交付，不代替採用結果 |
| 依客服測試回饋調整推薦規則 | decision | 回饋改變做法 |
| 降價期 iOS 非續訂營收較基準期增 5% | outcome | Android減18%，非隨機實驗 |
| 還原原價後 iOS 較基準期減 65% | outcome | 各期21天，時間干擾待核 |
| 依結果全面調降售價 | decision | 實驗導向決策 |
| Peach 網頁付款占營收由 24% 至 80% 以上 | outcome | 支付通路結構，不等於營收成長 |
| KOOL 訂閱與付費牆規劃上線 | output | 跨平台交付 |
| 才開放精選網紅資格 | decision/output | 資格門檻設計 |
| 主導 Juicy 上線 | output | 產品交付 |
| 上線後 6 週男性 DAU 約 3,200 至 1.25 萬 | outcome | 上線及行銷整體表現 |
| 與最多約 10 位外國實習生協作 | context | 無直屬關係，不換算管理幅度 |
| 導入 CodaPay | output | 拓展付款方式 |
| 提出 7／30／90 天訂閱方案與加贈內容 | output/decision | 實收試算支持方案 |
| Newegg.com 商品資訊英翻中與英文校對 | output | 工作英語證據，非近母語認證 |
| 自建 Claude Code 協作流程 | output | 12分支、23skill為範圍，不是效率結果 |


## B-jd20｜揭盲：甲=K、乙=M；偏好=M

```json
{"job_id":"jd20","order":"甲=K/乙=M","differences":[{"what":"乙交代取數與分析分工；甲僅呈現快照比較結果。","hiring_meaning":"可直接追問資料表、欄位、試算表分析與DBA依賴程度，核對本職缺獨立查詢分析的必備條件；不因結果相同提高分析能力評價。","type":"measurement"},{"what":"乙增加搜尋改版優先序與推薦名單根因、規則調整；甲已有溝通整合優先序，但未提供這兩個案例。","hiring_meaning":"新增可驗證的需求取捨及問題診斷案例，能追問排序依據、競品推論與推薦品質驗收；開發中案例不能當交付成效。","type":"capability"},{"what":"乙明示帳號冒用涉及求職者個資外洩風險；甲呈現同一安全事件與處置。","hiring_meaning":"讓防詐職缺的風險判斷訪談切入點更清楚，可問威脅評估與簽章驗證範圍；同一事件不代表乙多一段資安實績或已證明防詐熱情。","type":"readability"}],"preference":"乙","reason":"乙補足取數分工與需求診斷案例，較能界定面試驗證內容；仍須確認獨立數據分析、近母語英文、海外企業客戶及AI工作流整合深度，安全事件不等於完整防詐經驗。","evidence_甲":["比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。","例如廠商抱怨工單中，最大宗是溝通管道中斷，我便將信件與即時通整合排在其他新功能之前，目前專案仍在開發中。","登入安全盤點源於 2026/04 十多家廠商帳號遭冒用。"],"evidence_乙":["由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。","客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。","登入安全盤點源於 2026/04 十多家廠商帳號遭冒用；求才端可存取大量求職者個資，冒用登入即有外洩風險。"]}
```

## 版本比較｜jd20｜順序 甲=K 乙=M｜model_id: unknown
- 偏好：乙（揭盲：M）
| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 乙交代取數與分析分工；甲僅呈現快照比較結果。 | 可直接追問資料表、欄位、試算表分析與DBA依賴程度，核對本職缺獨立查詢分析的必備條件；不因結果相同提高分析能力評價。 | measurement | 比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |
| 2 | 乙增加搜尋改版優先序與推薦名單根因、規則調整；甲已有溝通整合優先序，但未提供這兩個案例。 | 新增可驗證的需求取捨及問題診斷案例，能追問排序依據、競品推論與推薦品質驗收；開發中案例不能當交付成效。 | capability | 例如廠商抱怨工單中，最大宗是溝通管道中斷，我便將信件與即時通整合排在其他新功能之前，目前專案仍在開發中。 | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 |
| 3 | 乙明示帳號冒用涉及求職者個資外洩風險；甲呈現同一安全事件與處置。 | 讓防詐職缺的風險判斷訪談切入點更清楚，可問威脅評估與簽章驗證範圍；同一事件不代表乙多一段資安實績或已證明防詐熱情。 | readability | 登入安全盤點源於 2026/04 十多家廠商帳號遭冒用。 | 登入安全盤點源於 2026/04 十多家廠商帳號遭冒用；求才端可存取大量求職者個資，冒用登入即有外洩風險。 |
- 理由（≤120 字）：乙補足取數分工與需求診斷案例，較能界定面試驗證內容；仍須確認獨立數據分析、近母語英文、海外企業客戶及AI工作流整合深度，安全事件不等於完整防詐經驗。

兩版核心PRD、交付、AI功能與定價案例相同。乙英文協作及Claude Code流程補述可用來追問實際工作情境，但不能以考試分數、分支或skill數量判定近母語英文與整合能力；兩版也未明示Jira／Confluence整合。以上僅依提供文本比較，未外部核實事實。


# jd26｜逐次輸出


## A-jd26-K｜履歷K

```json
{"rubric_version": "4.2", "resume_id": "K", "job_id": "jd26", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd26-K", "human_calibrated": false, "requirements": [{"id": "R01", "text": "2年以上相關工作經驗", "type": "required", "status": "supported", "evidence": ["近 10 年 PM 經驗"], "blocks_interview": false, "reason": "相關PM任職時序支持年資。"}, {"id": "R02", "text": "Axure規劃及Jira、Confluence專案管理", "type": "required", "status": "partial", "evidence": ["整理為 PRD 與 Axure Prototype"], "blocks_interview": false, "reason": "Axure有實際交付；Jira、Confluence未呈現，面試確認使用能力。"}, {"id": "R03", "text": "考量技術可行性與系統架構關連", "type": "required", "status": "supported", "evidence": ["釐清需求與系統分析後"], "blocks_interview": false, "reason": "舊系統資料、登入改版與串接提供具體案例。"}, {"id": "R04", "text": "預期及識別專案風險", "type": "required", "status": "supported", "evidence": ["選擇首次登入引導確認、不強迫修改"], "blocks_interview": false, "reason": "辨識重複信箱與登入中斷風險並分階段上線。"}, {"id": "R05", "text": "跨部門溝通與同理心", "type": "required", "status": "supported", "evidence": ["與 QA 制定 UAT 驗收案例"], "blocks_interview": false, "reason": "工程、客服、QA及使用者限制有實際協作證據。"}, {"id": "R06", "text": "喜愛或熟悉數位金融、支付產品", "type": "required", "status": "supported", "evidence": ["導入 CodaPay"], "blocks_interview": false, "reason": "有網頁付款與替代支付規劃，支持支付熟悉度；不等同本地電支專業。"}, {"id": "R07", "text": "需求分析、設計規格及兼顧合作方公司用戶", "type": "required", "status": "supported", "evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "blocks_interview": false, "reason": "PRD、原型、實收試算及外部串接支持；Hybrid App細節待追問。"}, {"id": "R08", "text": "確認合作需求與法遵適法性", "type": "required", "status": "partial", "evidence": ["法務與稽核協作"], "blocks_interview": false, "reason": "合作方串接有案例，適法性確認僅見技能層級。"}, {"id": "R09", "text": "時程、溝通、測試驗收上線與教育訓練", "type": "required", "status": "partial", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "blocks_interview": false, "reason": "交付明確，客服說明可轉移，正式內外部訓練未具體呈現。"}, {"id": "R10", "text": "線上問題排除、迭代及分析工具應用", "type": "required", "status": "partial", "evidence": ["依客服測試回饋調整推薦規則"], "blocks_interview": false, "reason": "問題排除與迭代有例；加分的分析工具實際應用未連結明確。"}, {"id": "R11", "text": "熟悉代理收付、電子支付及行動支付", "type": "preferred", "status": "partial", "evidence": ["電信帳單與超商付款"], "blocks_interview": false, "reason": "跨境替代支付可轉移，台灣電子支付與代理收付規則未呈現。"}, {"id": "R12", "text": "精通英文", "type": "preferred", "status": "supported", "evidence": ["英文 TOEIC 980、TOEFL iBT 93"], "blocks_interview": false, "reason": "分數、翻譯及跨國協作共同支持，口語可面試核對。"}], "dimensions": [{"id": "positioning", "rating": "足夠", "evidence": ["現任 1111 招募系統 Product Owner"], "missing": ["策略志向與本職專案執行比重需對齊。"], "issue_ids": ["I03"]}, {"id": "role_evidence", "rating": "足夠", "evidence": ["整理為 PRD 與 Axure Prototype"], "missing": ["Jira、Confluence、適法性確認及教育訓練案例。"], "issue_ids": ["I01", "I02"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": [], "issue_ids": []}, {"id": "outcome_quality", "rating": "足夠", "evidence": ["為觀察差異，非因果"], "missing": ["安全事件觀察來源及實驗歸因限制。"], "issue_ids": ["I04"]}, {"id": "ownership", "rating": "強", "evidence": ["由我主責規劃，與工程團隊密切協作"], "missing": [], "issue_ids": []}, {"id": "readability", "rating": "足夠", "evidence": ["從需求釐清、系統分析到 PRD、原型、UAT 與上線計畫"], "missing": ["可把支付案例前移以增加職缺對應可見性。"], "issue_ids": []}], "results": [{"quote": "約 50 項大項功能上線", "kinds": ["output"]}, {"quote": "需求平均處理週期由 100.4 天降至 30.9 天", "kinds": ["outcome"]}, {"quote": "該群年化留存 81.2%，同期全站 74.2%", "kinds": ["outcome"]}, {"quote": "選擇首次登入引導確認、不強迫修改", "kinds": ["decision"]}, {"quote": "Peach 網頁付款占營收由 24% 至 80% 以上", "kinds": ["outcome"]}, {"quote": "目前專案仍在開發中", "kinds": ["in_progress"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["整理為 PRD 與 Axure Prototype"], "application_note": "規格與交付直接相關"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "B2B環境與支付差異可釐清"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "application_note": "責任與工程分工清楚"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "流程結果有期間仍需核對口徑"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "限制下的具體取捨"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["近 10 年 PM 經驗"], "application_note": "產品與責任變化可辨識"}, {"rule_id": "HR07", "status": "supported", "resume_evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "application_note": "有跨團隊實際運用"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["曾設計定價實驗、規劃網頁付款"], "application_note": "摘要易找到支付經驗"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["依目前掌握的情況"], "application_note": "安全觀察來源留面試核對"}, {"rule_id": "HR10", "status": "partial", "resume_evidence": ["希望將更多心力放回產品策略"], "application_note": "確認能接受專案執行比重"}, {"rule_id": "HR11", "status": "unknown", "resume_evidence": ["錄取後三週可上班"], "application_note": "JD未載足以比對的工作條件"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "application_note": "交付證據足以支持面試"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["訂閱制 B2C App 與雙邊媒合平台"], "evidence_type": "context", "source_ids": [], "interview_question": "支付合作專案與目前B2B工作有何異同？"}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["最大宗是溝通管道中斷"], "evidence_type": "decision", "source_ids": [], "interview_question": "工單分類如何影響優先級？"}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "evidence_type": "decision", "source_ids": [], "interview_question": "如何比較替代遷移方案與風險？"}, {"rule_id": "HM04", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "evidence_type": "decision", "source_ids": [], "interview_question": "試算如何影響合作條件與訂閱方案？"}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "partial", "resume_evidence": ["為觀察差異，非因果"], "evidence_type": "outcome", "source_ids": [], "interview_question": "週期、留存與安全事件的資料來源為何？"}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "evidence_type": "output", "source_ids": [], "interview_question": "規格決定與技術決定如何分工？"}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "evidence_type": "output", "source_ids": [], "interview_question": "如何設計切換、回退及驗收門檻？"}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "evidence_type": "output", "source_ids": [], "interview_question": "簽章驗證涉及哪些系統關連與限制？"}, {"rule_id": "HM09", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["對接 16 個需求單位"], "evidence_type": "context", "source_ids": [], "interview_question": "多方需求衝突時如何取得決定？"}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["曾設計定價實驗、規劃網頁付款"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則"], "evidence_type": "decision", "source_ids": [], "interview_question": "哪些反例促成推薦規則修改？"}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "evidence_type": "output", "source_ids": [], "interview_question": "請以支付專案展示規格至上線的完整流程。"}, {"rule_id": "HM13", "primary_dimension": "method", "status": "supported", "resume_evidence": ["為觀察差異，非因果"], "evidence_type": null, "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HR01", "source_ids": [], "application_note": "留面試釐清，不據此淘汰", "context_limit": "僅依指定履歷與JD摘要", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "Figma、Axure RP、Notion、Trello", "reason": "Jira、Confluence未呈現；Axure及交付實例支持進入面試確認工具適應。", "suggestion": "如有實際使用，補充專案與用途；否則如實說明可轉移流程。"}, {"id": "I02", "rule_id": "HM07", "source_ids": [], "application_note": "留面試釐清，不據此淘汰", "context_limit": "僅依指定履歷與JD摘要", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "法務與稽核協作", "reason": "未見適法性確認與正式教育訓練案例，面試需驗證支付協作全流程。", "suggestion": "補一個法務審查或教育訓練的責任、對象與交付物。"}, {"id": "I03", "rule_id": "HR10", "source_ids": [], "application_note": "留面試釐清，不據此淘汰", "context_limit": "僅依指定履歷與JD摘要", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "希望將更多心力放回產品策略", "reason": "本職以合作專案執行為主，需確認工作比重期待；不推論不願執行。", "suggestion": "面試說明對執行及策略責任配比的期待。"}, {"id": "I04", "rule_id": "HM05", "source_ids": [], "application_note": "留面試釐清，不據此淘汰", "context_limit": "僅依指定履歷與JD摘要", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "依目前掌握的情況", "reason": "未再發生事件屬有限觀察，不能當完整監控或因果證明；追問來源即可。", "suggestion": "補觀察管道、範圍與未覆蓋限制，保留現有審慎限定。"}], "decision": {"recommendation": "interview", "evidence": ["整理為 PRD 與 Axure Prototype", "並與 CodaPay 新加坡技術團隊協調串接"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["規格、驗收與上線有完整交付案例。", "支付串接與實收試算可轉移至合作專案。", "風險辨識及分階段切換有具體決策。"], "key_gaps": ["Jira、Confluence及分析工具實際運用待確認。", "本地電支付法遵與教育訓練案例不足。", "策略志向與執行職務比重待對齊。"], "strengths": ["規格到上線的本人責任清楚。", "支付實收與跨國串接經驗直接相關。", "取捨及量測限制明示，便於面試追溯。"], "interview_questions": ["Jira、Confluence是否實際用過？如何管理規格與追蹤？", "請展示支付串接的規格、系統關連與驗收案例。", "如何與法遵確認適法性並處理意見衝突？", "如何設計內外部教育訓練及上線問題處理？", "哪個分析工具的結果曾改變上線功能？", "安全事件與處理週期的來源、分母及限制為何？", "你期待策略與合作專案執行的工作比例為何？"], "editorial_appendix": ["可將支付串接案例前移；屬可見性調整，不代表能力改變。"], "spectrum": {"level": 8, "uncertainty_levels": 1, "basis": "多個規格、交付與支付案例，且具明確取捨、比較期間及限制；工具與法遵細節可面試釐清。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷K｜第 1 輪｜model_id: unknown

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「整理為 PRD 與 Axure Prototype」及支付串接支持面試，工具與法遵待核對。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 現任 1111 招募系統 Product Owner | 策略志向與本職專案執行比重需對齊。 |
| role_evidence | 足夠 | 整理為 PRD 與 Axure Prototype | Jira、Confluence、適法性確認及教育訓練案例。 |
| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 足以支持面試；細節可案例追問。 |
| outcome_quality | 足夠 | 為觀察差異，非因果 | 安全事件觀察來源及實驗歸因限制。 |
| ownership | 強 | 由我主責規劃，與工程團隊密切協作 | 足以支持面試；細節可案例追問。 |
| readability | 足夠 | 從需求釐清、系統分析到 PRD、原型、UAT 與上線計畫 | 可把支付案例前移以增加職缺對應可見性。 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 2年以上相關工作經驗 | 必要 | supported | 近 10 年 PM 經驗 | 相關PM任職時序支持年資。 |
| Axure規劃及Jira、Confluence專案管理 | 必要 | partial | 整理為 PRD 與 Axure Prototype | Axure有實際交付；Jira、Confluence未呈現，面試確認使用能力。 |
| 考量技術可行性與系統架構關連 | 必要 | supported | 釐清需求與系統分析後 | 舊系統資料、登入改版與串接提供具體案例。 |
| 預期及識別專案風險 | 必要 | supported | 選擇首次登入引導確認、不強迫修改 | 辨識重複信箱與登入中斷風險並分階段上線。 |
| 跨部門溝通與同理心 | 必要 | supported | 與 QA 制定 UAT 驗收案例 | 工程、客服、QA及使用者限制有實際協作證據。 |
| 喜愛或熟悉數位金融、支付產品 | 必要 | supported | 導入 CodaPay | 有網頁付款與替代支付規劃，支持支付熟悉度；不等同本地電支專業。 |
| 需求分析、設計規格及兼顧合作方公司用戶 | 必要 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | PRD、原型、實收試算及外部串接支持；Hybrid App細節待追問。 |
| 確認合作需求與法遵適法性 | 必要 | partial | 法務與稽核協作 | 合作方串接有案例，適法性確認僅見技能層級。 |
| 時程、溝通、測試驗收上線與教育訓練 | 必要 | partial | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 交付明確，客服說明可轉移，正式內外部訓練未具體呈現。 |
| 線上問題排除、迭代及分析工具應用 | 必要 | partial | 依客服測試回饋調整推薦規則 | 問題排除與迭代有例；加分的分析工具實際應用未連結明確。 |
| 熟悉代理收付、電子支付及行動支付 | 加分 | partial | 電信帳單與超商付款 | 跨境替代支付可轉移，台灣電子支付與代理收付規則未呈現。 |
| 精通英文 | 加分 | supported | 英文 TOEIC 980、TOEFL iBT 93 | 分數、翻譯及跨國協作共同支持，口語可面試核對。 |
分析工具實際運用屬JD加分項，R10合併呈現但不升格為必要條件；沒有明文必要條件遭證據否定。

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 整理為 PRD 與 Axure Prototype | 規格與交付直接相關 |
| HR02 | supported | 企業端招募系統全模組與求職端公司頁 | B2B環境與支付差異可釐清 |
| HR03 | supported | 由我主責規劃，與工程團隊密切協作 | 責任與工程分工清楚 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 流程結果有期間仍需核對口徑 |
| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 限制下的具體取捨 |
| HR06 | supported | 近 10 年 PM 經驗 | 產品與責任變化可辨識 |
| HR07 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 有跨團隊實際運用 |
| HR08 | supported | 曾設計定價實驗、規劃網頁付款 | 摘要易找到支付經驗 |
| HR09 | partial | 依目前掌握的情況 | 安全觀察來源留面試核對 |
| HR10 | partial | 希望將更多心力放回產品策略 | 確認能接受專案執行比重 |
| HR11 | unknown | 錄取後三週可上班 | JD未載足以比對的工作條件 |
| HR12 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 交付證據足以支持面試 |
| HM01 | supported | 訂閱制 B2C App 與雙邊媒合平台 | 產品情境可轉移，支付領域再確認 |
| HM02 | supported | 最大宗是溝通管道中斷 | 有使用者訊號驅動優先級 |
| HM03 | supported | 選擇首次登入引導確認、不強迫修改 | 已發生取捨支持決策能力 |
| HM04 | supported | 依抽成、稅、手續費及撥款週期做實收試算 | 支付商業條件有具體考量 |
| HM05 | partial | 為觀察差異，非因果 | 量測口徑及觀察來源需追問 |
| HM06 | supported | 由我主責規劃，與工程團隊密切協作 | 本人規劃與工程協作邊界清楚 |
| HM07 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 測試上線直接支持職務 |
| HM08 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 系統影響有案例可深入驗證 |
| HM09 | supported | 對接 16 個需求單位 | 有跨單位自主規劃證據 |
| HM10 | supported | 曾設計定價實驗、規劃網頁付款 | 摘要與經歷重點容易辨識 |
| HM11 | supported | 依客服測試回饋調整推薦規則 | 回饋有轉為規則修改 |
| HM12 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 已有案例支持面試驗證 |
| HM13 | supported | 為觀察差異，非因果 | 依本JD獨立判讀；非外部驗證 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「與 QA 制定 UAT 驗收案例、排定上線計畫」支持交付。 |
| 2 | 「並與 CodaPay 新加坡技術團隊協調串接」支持合作方溝通。 |
| 3 | 「選擇首次登入引導確認、不強迫修改」支持風險取捨。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | Jira、Confluence及分析工具實際運用待確認。 | Jira、Confluence是否實際用過？如何管理規格與追蹤？ |
| 2 | 本地電支付法遵與教育訓練案例不足。 | 如何與法遵確認適法性並處理意見衝突？ |
| 3 | 策略志向與執行職務比重待對齊。 | 你期待策略與合作專案執行的工作比例為何？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
1. 1111交付｜「由我主責規劃，與工程團隊密切協作」｜清楚交代本人與工程的責任。
2. 思維特付款｜「依抽成、稅、手續費及撥款週期做實收試算」｜連結支付合作與公司需求。
3. 1111改版｜「選擇首次登入引導確認、不強迫修改」｜呈現用戶體驗及上線風險的取捨。

**可改進（4 點）**：

- 位置：專業技能
- 原句：Figma、Axure RP、Notion、Trello
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：Jira、Confluence未呈現；Axure及交付實例支持進入面試確認工具適應。
- 建議方向：如有實際使用，補充專案與用途；否則如實說明可轉移流程。

- 位置：專業技能／上線經歷
- 原句：法務與稽核協作
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：未見適法性確認與正式教育訓練案例，面試需驗證支付協作全流程。
- 建議方向：補一個法務審查或教育訓練的責任、對象與交付物。

- 位置：自傳末段
- 原句：希望將更多心力放回產品策略
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：本職以合作專案執行為主，需確認工作比重期待；不推論不願執行。
- 建議方向：面試說明對執行及策略責任配比的期待。

- 位置：1111登入安全
- 原句：依目前掌握的情況
- 問題類型：measurement
- 嚴重度：interview_follow_up
- 影響：未再發生事件屬有限觀察，不能當完整監控或因果證明；追問來源即可。
- 建議方向：補觀察管道、範圍與未覆蓋限制，保留現有審慎限定。

**編輯附件**（不影響判斷）：支付案例可前移。

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠
方向能力有定價與優先級證據；不將年資、單位數或功能數直接當成資深程度。

### 8. 未測試聲明
PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run
全部為履歷自述，未作外部查證；本次不推估錄取率。

### 成果分類補表
| 原句片段 | 分類 | 解讀及限制 |
| :-- | :-- | :-- |
| 全站活躍付費廠商約 6.6 萬家 | context | 系統規模，非本人新增客戶 |
| 上線 111 項 Roadmap 細項 | output | 與大項功能口徑不同，不相加 |
| 盤點出上千組重複 E-mail | output | 資料盤點發現，不是用戶成效 |
| 停機約 1.5 小時 | outcome | 切換運作觀察，未有原定目標比較 |
| 於 2026/04/17 上線簽章驗證 | output | 安全交付 |
| 上線後至 2026/10 未再出現同類帳號冒用 | outcome | 限目前掌握情況，非完整監測證明 |
| 完成 1,726／1,857 張需求與問題單 | output | 截至09/29的工單完成量 |
| 需求管線觸及 1,279 家活躍付費廠商 | context | 觸及母體，非新增營收 |
| 已上線公司簡介生成、職缺工作說明生成及推薦人才 | output | AI功能交付 |
| 依客服測試回饋調整推薦規則 | decision | 回饋改變規則，無已證明成效 |
| 降價期 iOS 非續訂營收較基準期增 5% | outcome | 各期21天，Android對照仍有平台差異 |
| Android 減 18%，相對變化約多 28% | outcome | 相對比例變化，不等於28個百分點 |
| 還原原價後 iOS 較基準期減 65% | outcome | 時序觀察，需核對其他變動因素 |
| 依結果全面調降售價 | decision | 由實驗結果形成價格決策 |
| KOOL 訂閱與付費牆規劃上線 | output | 付費功能交付 |
| 才開放精選網紅資格 | decision | 資格門檻設計，非成效 |
| 主導 Juicy 上線 | output | 上線交付 |
| 男性 DAU 約 3,200 至 1.25 萬 | outcome | 六週，包含行銷導流的整體表現 |
| SweetRing 在地化涵蓋 | output | 七市場在地化，未提供採用成效 |
| 與最多約 10 位外國實習生協作 | context | 協作範圍，非直屬管理 |
| 導入 CodaPay | output | 付款方式交付 |
| 提出 7／30／90 天訂閱方案與加贈內容 | output | 方案產出，不是收入提升 |
| Newegg.com 商品資訊英翻中與校對 | output | 翻譯工作產出 |
| 將信件與即時通整合排在其他新功能之前 | decision / in_progress | 優先級已決定，專案仍開發，不能算實現成效 |


## A-jd26-M｜履歷M

```json
{"rubric_version": "4.2", "resume_id": "M", "job_id": "jd26", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd26-M", "human_calibrated": false, "requirements": [{"id": "R01", "text": "2年以上相關工作經驗", "type": "required", "status": "supported", "evidence": ["近 10 年 PM 經驗"], "blocks_interview": false, "reason": "有連續產品規劃與交付案例。"}, {"id": "R02", "text": "Axure規劃及Jira、Confluence專案管理", "type": "required", "status": "partial", "evidence": ["整理為 PRD 與 Axure Prototype"], "blocks_interview": false, "reason": "Axure有實作；Jira、Confluence未呈現，面試確認可轉移工具能力。"}, {"id": "R03", "text": "技術可行性及系統架構關連影響", "type": "required", "status": "supported", "evidence": ["盤點出上千組重複 E-mail"], "blocks_interview": false, "reason": "既有資料、登入流程與分階段切換有具體考量。"}, {"id": "R04", "text": "預期與識別執行風險", "type": "required", "status": "supported", "evidence": ["選擇首次登入引導確認、不強迫修改"], "blocks_interview": false, "reason": "具既有客戶登入與個資風險案例。"}, {"id": "R05", "text": "跨部門溝通及同理心", "type": "required", "status": "supported", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "blocks_interview": false, "reason": "協作角色明確，兼顧廠商與第一線說明。"}, {"id": "R06", "text": "喜愛或熟悉數位金融、支付產品", "type": "required", "status": "supported", "evidence": ["與 CodaPay 新加坡技術團隊協調串接"], "blocks_interview": false, "reason": "具付款整合及實收試算經驗。"}, {"id": "R07", "text": "需求規劃、設計規格並兼顧合作方與用戶", "type": "required", "status": "supported", "evidence": ["以 Use Case、Wireframe 定義業務流程與畫面"], "blocks_interview": false, "reason": "有規格、原型與付款合作方協作案例。"}, {"id": "R08", "text": "合作單位需求確認及法遵適法性確認", "type": "required", "status": "partial", "evidence": ["法務與稽核協作"], "blocks_interview": false, "reason": "協作僅技能列示，支付法遵審查案例未知。"}, {"id": "R09", "text": "時程、測試驗收、上線、訓練、問題處理與迭代", "type": "required", "status": "partial", "evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "blocks_interview": false, "reason": "交付及問題處理明確，正式教育訓練未呈現。"}, {"id": "R10", "text": "代理收付、電子支付及行動支付知識應用", "type": "preferred", "status": "partial", "evidence": ["開放印尼、泰國等市場的電信帳單與超商付款"], "blocks_interview": false, "reason": "相鄰支付經驗支持，臺灣電子支付業務規則仍須驗證。"}, {"id": "R11", "text": "精通英文", "type": "preferred", "status": "supported", "evidence": ["英文 TOEIC 980、TOEFL iBT 93"], "blocks_interview": false, "reason": "有英文實際工作；精通程度可由面試核對。"}, {"id": "R12", "text": "實際使用數據分析工具迭代功能", "type": "preferred", "status": "partial", "evidence": ["再以 Google Sheet 比對"], "blocks_interview": false, "reason": "工具分析有證據，功能迭代前後成效連結待補。"}], "dimensions": [{"id": "positioning", "rating": "足夠", "evidence": ["現任 1111 招募系統 Product Owner"], "missing": ["策略方向與執行型職位偏好需確認"], "issue_ids": []}, {"id": "role_evidence", "rating": "足夠", "evidence": ["整理為 PRD 與 Axure Prototype"], "missing": ["Jira／Confluence、支付法遵與教育訓練需追問"], "issue_ids": ["I01", "I02"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": ["支付領域限制的取捨可面試延伸"], "issue_ids": []}, {"id": "outcome_quality", "rating": "足夠", "evidence": ["為觀察差異，非因果"], "missing": ["安全觀察來源及數據驅動迭代閉環待核對"], "issue_ids": ["I03", "I04"]}, {"id": "ownership", "rating": "強", "evidence": ["由我擬定取數的資料表與欄位"], "missing": ["合作方、工程與法遵的責任界線可再核對"], "issue_ids": []}, {"id": "readability", "rating": "足夠", "evidence": ["從需求釐清、系統分析到 PRD、原型、UAT 與上線計畫"], "missing": ["可將支付整合案例提前；不影響面試"], "issue_ids": []}], "results": [{"quote": "全站活躍付費廠商約 6.6 萬家", "kinds": ["context"]}, {"quote": "另於 2026/01–06 上線 111 項 Roadmap 細項", "kinds": ["output"]}, {"quote": "需求平均處理週期由 100.4 天降至 30.9 天", "kinds": ["outcome"]}, {"quote": "為觀察差異，非因果", "kinds": ["outcome"]}, {"quote": "信件與即時通整合排在其他新功能之前", "kinds": ["decision", "in_progress"]}, {"quote": "Peach 網頁付款占營收由 24% 至 80% 以上", "kinds": ["outcome"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["與 CodaPay 新加坡技術團隊協調串接"], "application_note": "付款整合與專案執行直接相關"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "近期為企業產品，可轉移交付能力"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "application_note": "規劃責任與工程交付有區分"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "有期間與處理成果，仍需核對口徑"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "有既有客戶風險下的取捨"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["從交友與訂閱制 App 到企業招募系統"], "application_note": "可看出領域與責任演進"}, {"rule_id": "HR07", "status": "partial", "resume_evidence": ["整理為 PRD 與 Axure Prototype"], "application_note": "Axure已用，另兩項工具待核對"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "application_note": "可辨識交付流程與本人工作"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["依目前掌握的情況"], "application_note": "安全效果屬自述觀察，追問來源"}, {"rule_id": "HR10", "status": "partial", "resume_evidence": ["我希望將更多心力放回產品策略"], "application_note": "確認對專案執行占比的期待"}, {"rule_id": "HR11", "status": "unknown", "resume_evidence": [], "application_note": "未提供衝突證據，薪資等可面談"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["規劃由 App 內購轉向網頁付款"], "application_note": "足以約談，驗證支付規則與工具"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["訂閱制 B2C App 與雙邊媒合平台"], "evidence_type": "context", "source_ids": [], "interview_question": "如何轉移到電子支付合作專案？"}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["客服反映配對名單「少又舊」"], "evidence_type": "decision", "source_ids": [], "interview_question": "哪些客服訊號改變原本方案？"}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "evidence_type": "decision", "source_ids": [], "interview_question": "當時有哪些替代方案與風險？"}, {"rule_id": "HM04", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "evidence_type": "decision", "source_ids": [], "interview_question": "試算如何影響支付商與方案選擇？"}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "partial", "resume_evidence": ["為觀察差異，非因果"], "evidence_type": "outcome", "source_ids": [], "interview_question": "如何確認迭代成效與樣本限制？"}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["與資料科學團隊合作，定義使用情境與驗收標準"], "evidence_type": "output", "source_ids": [], "interview_question": "你與工程、合作方各自決定什麼？"}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "evidence_type": "output", "source_ids": [], "interview_question": "如何處理上線風險及回復方案？"}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["盤點出上千組重複 E-mail"], "evidence_type": "decision", "source_ids": [], "interview_question": "付款串接有哪些系統狀態與例外？"}, {"rule_id": "HM09", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "evidence_type": "output", "source_ids": [], "interview_question": "哪些風險決策由你獨立承擔？"}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["規劃由 App 內購轉向網頁付款"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則"], "evidence_type": "decision", "source_ids": [], "interview_question": "回饋如何轉成規則與後續驗證？"}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["整理為 PRD 與 Axure Prototype"], "evidence_type": "output", "source_ids": [], "interview_question": "可否以去識別規格演示交付過程？"}, {"rule_id": "HM13", "primary_dimension": "role_evidence", "status": "not_applicable", "resume_evidence": [], "evidence_type": null, "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HR07", "source_ids": [], "application_note": "Jira與Confluence未呈現；已有交付能力，於面試驗", "context_limit": "只讀履歷文字與JD摘要，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "Figma、Axure RP、Notion、Trello", "reason": "Jira與Confluence未呈現；已有交付能力，於面試驗證工具經驗。", "suggestion": "如實補充使用情境；無經驗則說明可轉移方法。"}, {"id": "I02", "rule_id": "HM07", "source_ids": [], "application_note": "支付法遵與正式教育訓練缺具體案例，追問流程與責任。", "context_limit": "只讀履歷文字與JD摘要，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "法務與稽核協作", "reason": "支付法遵與正式教育訓練缺具體案例，追問流程與責任。", "suggestion": "選一個合作專案補充法遵確認、訓練對象與本人範圍。"}, {"id": "I03", "rule_id": "HM05", "source_ids": [], "application_note": "安全效果的觀察管道不明，不能當成完整監測證明。", "context_limit": "只讀履歷文字與JD摘要，未外部查證", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "依目前掌握的情況", "reason": "安全效果的觀察管道不明，不能當成完整監測證明。", "suggestion": "說明觀察來源、涵蓋範圍與無法觀察的限制。"}, {"id": "I04", "rule_id": "HM05", "source_ids": [], "application_note": "有分析工具使用，但分析如何促成迭代及驗證尚未連結。", "context_limit": "只讀履歷文字與JD摘要，未外部查證", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "再以 Google Sheet 比對", "reason": "有分析工具使用，但分析如何促成迭代及驗證尚未連結。", "suggestion": "補一個資料、改動、上線觀察連續案例，不新增假數字。"}, {"id": "I05", "rule_id": "HR10", "source_ids": [], "application_note": "職涯期待偏策略，需確認是否接受此職以合作專案執行為主。", "context_limit": "只讀履歷文字與JD摘要，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "我希望將更多心力放回產品策略", "reason": "職涯期待偏策略，需確認是否接受此職以合作專案執行為主。", "suggestion": "面試釐清對執行占比與策略參與空間的期待。"}], "decision": {"recommendation": "interview", "evidence": ["整理為 PRD 與 Axure Prototype", "與 CodaPay 新加坡技術團隊協調串接"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["「整理為 PRD 與 Axure Prototype」支持需求到驗收交付。", "「與 CodaPay 新加坡技術團隊協調串接」有支付合作經驗。", "「選擇首次登入引導確認、不強迫修改」呈現風險取捨。"], "key_gaps": ["Jira／Confluence、支付法遵與訓練案例待核對。", "分析到功能迭代成效的連結及安全觀察來源待驗證。", "策略方向與專案執行職位期待需確認。"], "strengths": ["規格與驗收交付鏈清楚", "支付合作與商業試算可轉移", "使用者與既有資料風險取捨具體"], "interview_questions": ["曾如何使用Jira與Confluence管理需求及版本？", "付款串接如何確認法遵、例外與責任邊界？", "如何安排教育訓練與線上問題交接？", "請用一個分析工具驅動功能迭代的案例說明前後成效。", "未再冒用的觀察來自何種管道，涵蓋哪些情況？", "此職以合作專案執行為主，與你的下一步期待如何相容？"], "editorial_appendix": ["可提前支付整合案例，讓職缺關聯更快被看見；不改變能力判斷。"], "spectrum": {"level": 8, "uncertainty_levels": 1, "basis": "多個交付與支付案例、具體取捨及量測限制支持面試；臺灣電子支付法遵與工具仍須核對。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷 M｜第 1 輪｜model_id: unknown


### 1. 結論

- 招聘決定：interview

- Level：8（±1）

- 一句話理由：「整理為 PRD 與 Axure Prototype」及支付串接支持面試。


### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 現任 1111 招募系統 Product Owner | 策略方向與執行型職位偏好需確認 |
| role_evidence | 足夠 | 整理為 PRD 與 Axure Prototype | Jira／Confluence、支付法遵與教育訓練需追問 |
| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 支付領域限制的取捨可面試延伸 |
| outcome_quality | 足夠 | 為觀察差異，非因果 | 安全觀察來源及數據驅動迭代閉環待核對 |
| ownership | 強 | 由我擬定取數的資料表與欄位 | 合作方、工程與法遵的責任界線可再核對 |
| readability | 足夠 | 從需求釐清、系統分析到 PRD、原型、UAT 與上線計畫 | 可將支付整合案例提前；不影響面試 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 2年以上相關工作經驗 | 必要 | supported | 近 10 年 PM 經驗 | 有連續產品規劃與交付案例。 |
| Axure規劃及Jira、Confluence專案管理 | 必要 | partial | 整理為 PRD 與 Axure Prototype | Axure有實作；Jira、Confluence未呈現，面試確認可轉移工具能力。 |
| 技術可行性及系統架構關連影響 | 必要 | supported | 盤點出上千組重複 E-mail | 既有資料、登入流程與分階段切換有具體考量。 |
| 預期與識別執行風險 | 必要 | supported | 選擇首次登入引導確認、不強迫修改 | 具既有客戶登入與個資風險案例。 |
| 跨部門溝通及同理心 | 必要 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 協作角色明確，兼顧廠商與第一線說明。 |
| 喜愛或熟悉數位金融、支付產品 | 必要 | supported | 與 CodaPay 新加坡技術團隊協調串接 | 具付款整合及實收試算經驗。 |
| 需求規劃、設計規格並兼顧合作方與用戶 | 必要 | supported | 以 Use Case、Wireframe 定義業務流程與畫面 | 有規格、原型與付款合作方協作案例。 |
| 合作單位需求確認及法遵適法性確認 | 必要 | partial | 法務與稽核協作 | 協作僅技能列示，支付法遵審查案例未知。 |
| 時程、測試驗收、上線、訓練、問題處理與迭代 | 必要 | partial | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 交付及問題處理明確，正式教育訓練未呈現。 |
| 代理收付、電子支付及行動支付知識應用 | 加分 | partial | 開放印尼、泰國等市場的電信帳單與超商付款 | 相鄰支付經驗支持，臺灣電子支付業務規則仍須驗證。 |
| 精通英文 | 加分 | supported | 英文 TOEIC 980、TOEFL iBT 93 | 有英文實際工作；精通程度可由面試核對。 |
| 實際使用數據分析工具迭代功能 | 加分 | partial | 再以 Google Sheet 比對 | 工具分析有證據，功能迭代前後成效連結待補。 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 與 CodaPay 新加坡技術團隊協調串接 | 付款整合與專案執行直接相關 |
| HR02 | supported | 企業端招募系統全模組與求職端公司頁 | 近期為企業產品，可轉移交付能力 |
| HR03 | supported | 由我主責規劃，與工程團隊密切協作 | 規劃責任與工程交付有區分 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 有期間與處理成果，仍需核對口徑 |
| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 有既有客戶風險下的取捨 |
| HR06 | supported | 從交友與訂閱制 App 到企業招募系統 | 可看出領域與責任演進 |
| HR07 | partial | 整理為 PRD 與 Axure Prototype | Axure已用，另兩項工具待核對 |
| HR08 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 可辨識交付流程與本人工作 |
| HR09 | partial | 依目前掌握的情況 | 安全效果屬自述觀察，追問來源 |
| HR10 | partial | 我希望將更多心力放回產品策略 | 確認對專案執行占比的期待 |
| HR11 | unknown | 未呈現 | 未提供衝突證據，薪資等可面談 |
| HR12 | supported | 規劃由 App 內購轉向網頁付款 | 足以約談，驗證支付規則與工具 |
| HM01 | supported | 訂閱制 B2C App 與雙邊媒合平台 | 產品類型可轉移至合作專案 |
| HM02 | supported | 客服反映配對名單「少又舊」 | 有客服訊號到規則的案例 |
| HM03 | supported | 選擇首次登入引導確認、不強迫修改 | 有具體替代方案與風險取捨 |
| HM04 | supported | 依抽成、稅、手續費及撥款週期做實收試算 | 實收試算連結方案選擇 |
| HM05 | partial | 為觀察差異，非因果 | 驗證分析到迭代的衡量閉環 |
| HM06 | supported | 與資料科學團隊合作，定義使用情境與驗收標準 | 本人規劃與技術團隊分工明確 |
| HM07 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 驗收上線足以支持面試 |
| HM08 | supported | 盤點出上千組重複 E-mail | 可面試驗證支付架構與例外 |
| HM09 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 具跨單位自主統籌案例 |
| HM10 | supported | 規劃由 App 內購轉向網頁付款 | 付款工作與交付內容易辨識 |
| HM11 | supported | 依客服測試回饋調整推薦規則 | 回饋會改變規則 |
| HM12 | supported | 整理為 PRD 與 Axure Prototype | 已有足夠約談證據 |
| HM13 | not_applicable | 不適用 | 方法層，不當候選人能力加分 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「整理為 PRD 與 Axure Prototype」支持需求到驗收交付。 |
| 2 | 「與 CodaPay 新加坡技術團隊協調串接」有支付合作經驗。 |
| 3 | 「選擇首次登入引導確認、不強迫修改」呈現風險取捨。 |
| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | Jira／Confluence、支付法遵與訓練案例待核對。 | 曾如何使用Jira與Confluence管理需求及版本？ |
| 2 | 分析到功能迭代成效的連結及安全觀察來源待驗證。 | 請用一個分析工具驅動功能迭代的案例說明前後成效。 |
| 3 | 策略方向與專案執行職位期待需確認。 | 此職以合作專案執行為主，與你的下一步期待如何相容？ |

### 6. 評語（給寫稿者的具體回饋）

**做得好（3 點）**

- 1111 交付｜「與 QA 制定 UAT 驗收案例、排定上線計畫」｜直接支持驗收上線責任。

- 尚凡付款｜「與 CodaPay 新加坡技術團隊協調串接」｜與外部合作專案直接相關。

- 1111 改版｜「選擇首次登入引導確認、不強迫修改」｜具體呈現用戶體驗與風險考量。

**可改進（5 點）**

- 位置：專業技能
  - 原句：Figma、Axure RP、Notion、Trello
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：Jira與Confluence未呈現；已有交付能力，於面試驗證工具經驗。
  - 建議方向：如實補充使用情境；無經驗則說明可轉移方法。

- 位置：跨部門與整合
  - 原句：法務與稽核協作
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：支付法遵與正式教育訓練缺具體案例，追問流程與責任。
  - 建議方向：選一個合作專案補充法遵確認、訓練對象與本人範圍。

- 位置：登入安全
  - 原句：依目前掌握的情況
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：安全效果的觀察管道不明，不能當成完整監測證明。
  - 建議方向：說明觀察來源、涵蓋範圍與無法觀察的限制。

- 位置：需求管線分析
  - 原句：再以 Google Sheet 比對
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：有分析工具使用，但分析如何促成迭代及驗證尚未連結。
  - 建議方向：補一個資料、改動、上線觀察連續案例，不新增假數字。

- 位置：自傳末段
  - 原句：我希望將更多心力放回產品策略
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：職涯期待偏策略，需確認是否接受此職以合作專案執行為主。
  - 建議方向：面試釐清對執行占比與策略參與空間的期待。

**編輯附件**（不影響判斷）：可提前支付整合案例，讓職缺關聯更快被看見；不改變能力判斷。


### 7. 資深能力分布

delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

方向取捨有具體證據；資源配置範圍仍可追問，不以年資或團隊人數推斷。


### 8. 未測試聲明

PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run


### 成果分類補表

以下均為履歷自述，未外部查證；重複摘要合併列示。
| 原句片段 | 分類 | 解讀與限制 |
| :-- | :-- | :-- |
| 經手 6 款產品 | context | 產品範圍，不等於成果品質 |
| 對接 16 個需求單位 | context | 協作範圍 |
| 約 50 項大項功能上線 | output | 功能交付量，非使用者結果 |
| 另於 2026/01–06 上線 111 項 Roadmap 細項 | output | 不同粒度，不與大項相加 |
| 第一階段於 2025/10 離峰切換上線 | output | 已完成第一階段 |
| 停機約 1.5 小時 | outcome | 切換運作觀察，非改善幅度 |
| 於 2026/04/17 上線簽章驗證 | output | 工程協作交付 |
| 上線後至 2026/10 未再出現同類帳號冒用 | outcome | 有限觀察，不等同完整監測 |
| 完成 1,726／1,857 張需求與問題單，約 93% | output | 截至指定日期處理量 |
| 需求平均處理週期由 100.4 天降至 30.9 天 | outcome | 流程期間比較，非全歸本人 |
| 信件與即時通整合排在其他新功能之前 | decision / in_progress | 優先級已定，開發中 |
| 改版排在新功能職缺健檢之前 | decision / in_progress | 進行中不列實現結果 |
| 改依職缺上線日排序、20 天內不重複推薦 | decision / output | 規則調整，未列成效 |
| 需求管線觸及 1,279 家活躍付費廠商 | context | 樣本範圍非因果 |
| 該群年化留存 81.2%，同期全站 74.2% | outcome | 觀察差異，樣本選擇需核對 |
| AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才 | output | 功能交付，未列採用成效 |
| 依客服測試回饋調整推薦規則 | decision / output | 回饋修正，成效未知 |
| 降價期 iOS 非續訂營收較基準期增 5% | outcome | 有同期Android對照，非隨機證明 |
| 還原原價後 iOS 較基準期減 65% | outcome | 期間結果，受其他變因限制 |
| 依結果全面調降售價 | decision | 實驗後決策 |
| Peach 網頁付款占營收由 24% 至 80% 以上 | outcome | 付款渠道占比，非總營收成長 |
| KOOL 訂閱與付費牆規劃上線 | output | 跨平台交付 |
| 上線後 6 週男性 DAU 約 3,200 至 1.25 萬 | outcome | 產品與行銷整體結果 |
| 與最多約 10 位外國實習生協作 | context / output | 市場範圍，非管理人數加分 |
| 開放印尼、泰國等市場的電信帳單與超商付款 | output | 支付渠道交付 |
| 提出 7／30／90 天訂閱方案與加贈內容 | decision / output | 方案產出，未列已實現商業成效 |
| Newegg.com 商品資訊英翻中與英文校對 | output | 英語工作產出 |
| 12 條分支、23 個共用 skill | output | 個人工具流程，非產品成效 |


## B-jd26｜揭盲：甲=M、乙=K；偏好=M

```json
{"job_id":"jd26","order":"甲=M/乙=K","differences":[{"what":"甲交代取數分工與分析工具，乙僅列快照比對及留存結果。","hiring_meaning":"甲讓主管可直接驗證資料表與欄位定義、DBA協作及分析方法，較能釐清數據迭代的實際參與程度；不表示結果較佳。","type":"measurement"},{"what":"甲提供配對名單問題的根因、競品實測及規則調整；乙主要以AI推薦的回饋調整描述迭代。","hiring_meaning":"甲提供另一個可追問的線上問題排查案例，可驗證排序與推薦限制的設計理由、技術影響及上線成效；尚無此案成效數據。","type":"capability"},{"what":"甲明示帳號冒用與求職者個資外洩風險的關聯，乙保留事件及處置流程。","hiring_meaning":"甲較快呈現風險判斷脈絡，便於追問支付專案所需的風險辨識與法遵協作；相同處置成果不構成能力高低證據。","type":"readability"}],"preference":"甲","reason":"甲的取數分工及配對問題排查案例，讓主管更能驗證數據分析、線上問題處理與迭代決策。兩者共同的付款串接、Axure與驗收經驗相當；Jira／Confluence、支付法遵及教育訓練仍需確認。","evidence_甲":["由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。","客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。","求才端可存取大量求職者個資，冒用登入即有外洩風險。"],"evidence_乙":["比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。","AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。與資料科學團隊合作，定義使用情境與驗收標準，依客服測試回饋調整推薦規則。","登入安全盤點源於 2026/04 十多家廠商帳號遭冒用。"]}
```

## 版本比較｜jd26｜順序 甲=M 乙=K｜model_id: unknown
- 偏好：甲（揭盲：M）
| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 甲交代取數分工與分析工具，乙僅列快照比對及留存結果。 | 甲讓主管可直接驗證資料表與欄位定義、DBA協作及分析方法，較能釐清數據迭代的實際參與程度；不表示結果較佳。 | measurement | 由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |
| 2 | 甲提供配對名單問題的根因、競品實測及規則調整；乙主要以AI推薦的回饋調整描述迭代。 | 甲提供另一個可追問的線上問題排查案例，可驗證排序與推薦限制的設計理由、技術影響及上線成效；尚無此案成效數據。 | capability | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 | AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。與資料科學團隊合作，定義使用情境與驗收標準，依客服測試回饋調整推薦規則。 |
| 3 | 甲明示帳號冒用與求職者個資外洩風險的關聯，乙保留事件及處置流程。 | 甲較快呈現風險判斷脈絡，便於追問支付專案所需的風險辨識與法遵協作；相同處置成果不構成能力高低證據。 | readability | 求才端可存取大量求職者個資，冒用登入即有外洩風險。 | 登入安全盤點源於 2026/04 十多家廠商帳號遭冒用。 |
- 理由（≤120 字）：甲的取數分工及配對問題排查案例，讓主管更能驗證數據分析、線上問題處理與迭代決策。兩者共同的付款串接、Axure與驗收經驗相當；Jira／Confluence、支付法遵及教育訓練仍需確認。

本比較依提供的同一事實快照前提判讀資訊選擇，不代表外部核實；偏好反映可追問的證據較具體，不推定候選人實際能力隨版本改變。


# jd30｜逐次輸出


## A-jd30-K｜履歷K

```json
{"rubric_version": "4.2", "resume_id": "K", "job_id": "jd30", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd30-K", "human_calibrated": false, "requirements": [{"id": "R01", "text": "3年以上Software Product Manager經驗", "type": "required", "status": "supported", "evidence": ["Product Manager｜尚凡國際創新科技"], "blocks_interview": false, "reason": "有多年軟體產品管理經歷。"}, {"id": "R02", "text": "直接負責完整0到1探索、驗證、設計、開發、上線與迭代", "type": "required", "status": "partial", "evidence": ["主導 Juicy 上線"], "blocks_interview": false, "reason": "有新產品上線及設計交付；同一案例探索驗證與後續迭代待核對。"}, {"id": "R03", "text": "清楚的PRD、流程圖與資料結構規格", "type": "required", "status": "partial", "evidence": ["整理為 PRD 與 Axure Prototype"], "blocks_interview": false, "reason": "PRD與流程有案例；資料結構規格未呈現。"}, {"id": "R04", "text": "理解API、JSON與基本SQL", "type": "required", "status": "partial", "evidence": ["API 串接規劃、舊系統資料盤點"], "blocks_interview": false, "reason": "API有整合線索；JSON及SQL未呈現，面試以工作樣本確認。"}, {"id": "R05", "text": "智慧停車或MaaS產品完整週期推進", "type": "required", "status": "partial", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "blocks_interview": false, "reason": "完整交付可轉移；特定場域經驗未呈現，不當必要產業門檻。"}, {"id": "R06", "text": "跨業務、客服、財務釐清情境與優先序", "type": "required", "status": "partial", "evidence": ["對接 16 個需求單位"], "blocks_interview": false, "reason": "客服與業務有依據；財務對齊及分歧處理待問。"}, {"id": "R07", "text": "AI原型、產品AI機會與PM流程化", "type": "required", "status": "partial", "evidence": ["用於規格撰寫、資料整理與分析"], "blocks_interview": false, "reason": "AI協作及產品應用有證據；快速原型與流程化成效待問。"}, {"id": "R08", "text": "測試驗收、數據成長及PoC到Pilot到Scale", "type": "required", "status": "partial", "evidence": ["與 QA 制定 UAT 驗收案例"], "blocks_interview": false, "reason": "驗收與成長實驗具體；PoC至規模化轉換未完整交代。"}, {"id": "R09", "text": "與工程設計技術方案及跨部門外部協作", "type": "required", "status": "supported", "evidence": ["與 CodaPay 新加坡技術團隊協調串接"], "blocks_interview": false, "reason": "支付整合及工程協作可支持面試。"}, {"id": "R10", "text": "停車、交通、MaaS、保險、支付或FinTech經驗", "type": "preferred", "status": "supported", "evidence": ["導入 CodaPay"], "blocks_interview": false, "reason": "具支付經驗，無須同時符合各產業。"}, {"id": "R11", "text": "Prompt engineering、RAG或Agent實作", "type": "preferred", "status": "unknown", "evidence": ["Claude Code 多分支流程與共用 skill 庫"], "blocks_interview": false, "reason": "工具使用不等同特定RAG或Agent實作。"}, {"id": "R12", "text": "Growth、數據分析及AI／LLM實際工作應用", "type": "preferred", "status": "supported", "evidence": ["以 Android 售價不變作對照"], "blocks_interview": false, "reason": "定價實驗及AI規格、資料處理均有線索。"}], "dimensions": [{"id": "positioning", "rating": "強", "evidence": ["近 10 年 PM 經驗，經手 6 款產品"], "missing": ["智慧停車情境的轉移方式可於面試確認"], "issue_ids": []}, {"id": "role_evidence", "rating": "足夠", "evidence": ["整理為 PRD 與 Axure Prototype"], "missing": ["完整0到1、JSON／SQL、資料結構與AI原型待核對"], "issue_ids": ["I01", "I02", "I03"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": ["可追問新產品探索的替代方案"], "issue_ids": []}, {"id": "outcome_quality", "rating": "強", "evidence": ["為觀察差異，非因果"], "missing": ["年化留存算法及安全監測來源待核對"], "issue_ids": ["I04"]}, {"id": "ownership", "rating": "足夠", "evidence": ["由我主責規劃，與工程團隊密切協作"], "missing": ["財務對齊及工程方案決策分工待問"], "issue_ids": ["I05"]}, {"id": "readability", "rating": "足夠", "evidence": ["資深產品經理｜Senior Product Manager"], "missing": ["代表作與詳細方法較分散，可集中對應JD"], "issue_ids": []}], "results": [{"quote": "約 50 項大項功能上線", "kinds": ["output"]}, {"quote": "停機約 1.5 小時", "kinds": ["output"]}, {"quote": "需求平均處理週期由 100.4 天降至 30.9 天", "kinds": ["outcome"]}, {"quote": "該群年化留存 81.2%，同期全站 74.2%", "kinds": ["outcome"]}, {"quote": "選擇首次登入引導確認、不強迫修改", "kinds": ["decision"]}, {"quote": "目前專案仍在開發中", "kinds": ["in_progress"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["曾設計定價實驗、規劃網頁付款"], "application_note": "支付、成長與軟體交付直接相關"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["現任 1111 招募系統 Product Owner"], "application_note": "企業流程經驗可轉移至營運產品"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "application_note": "規劃責任清楚；技術分工可追問"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "呈現流程改變與比較期間"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "有使用者風險與交付取捨"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["從交友與訂閱制 App 到企業招募系統"], "application_note": "職涯跨客群且方向連貫"}, {"rule_id": "HR07", "status": "supported", "resume_evidence": ["與 CodaPay 新加坡技術團隊協調串接"], "application_note": "協作有真實應用情境"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["資深產品經理｜Senior Product Manager"], "application_note": "定位與代表案例可辨識"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["依目前掌握的情況"], "application_note": "安全結果需核對觀察來源"}, {"rule_id": "HR10", "status": "supported", "resume_evidence": ["接下來，我希望將更多心力放回產品策略"], "application_note": "與策略及完整週期責任相容"}, {"rule_id": "HR11", "status": "unknown", "resume_evidence": ["台北市、新北市，可接受遠端或混合辦公"], "application_note": "JD未明列地點，未見已知衝突"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["主導 Juicy 上線"], "application_note": "相關案例足以約談，核心細節待驗證"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["訂閱制 B2C App 與雙邊媒合平台"], "evidence_type": "context", "source_ids": [], "interview_question": "如何將支付與平台經驗轉移到停車產品？"}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["最大宗是溝通管道中斷"], "evidence_type": "decision", "source_ids": [], "interview_question": "客服訊號如何改變原本排序？"}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "evidence_type": "decision", "source_ids": [], "interview_question": "比較過哪些資料遷移方案？"}, {"rule_id": "HM04", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "evidence_type": "decision", "source_ids": [], "interview_question": "實收模型如何改變方案選擇？"}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "supported", "resume_evidence": ["為觀察差異，非因果"], "evidence_type": "outcome", "source_ids": [], "interview_question": "年化留存使用何種公式與母體？"}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "partial", "resume_evidence": ["與資料科學團隊合作"], "evidence_type": "output", "source_ids": [], "interview_question": "技術方案與財務優先序由誰拍板？"}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "evidence_type": "output", "source_ids": [], "interview_question": "請展示驗收標準與上線風險處理。"}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "partial", "resume_evidence": ["API 串接規劃、舊系統資料盤點"], "evidence_type": "context", "source_ids": [], "interview_question": "能否以支付案例解說JSON、資料結構及基本SQL？"}, {"rule_id": "HM09", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "evidence_type": "output", "source_ids": [], "interview_question": "請說明自主決策範圍與資源協調。"}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則"], "evidence_type": "decision", "source_ids": [], "interview_question": "哪次測試反證改變了驗收標準？"}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["主導 Juicy 上線"], "evidence_type": "output", "source_ids": [], "interview_question": "請用同一產品串起探索至上線後迭代。"}, {"rule_id": "HM13", "primary_dimension": "", "status": "supported", "resume_evidence": [], "evidence_type": null, "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HM12", "source_ids": [], "application_note": "完整0到1鏈路未在同一案例呈現", "context_limit": "僅依履歷文字，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "主導 Juicy 上線", "reason": "相關上線足以面試；需確認是否直接負責探索驗證及迭代。", "suggestion": "補同一案例的探索依據、驗證與迭代責任。"}, {"id": "I02", "rule_id": "HM08", "source_ids": [], "application_note": "JSON、基本SQL與資料結構規格未呈現", "context_limit": "僅依履歷文字，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "API 串接規劃、舊系統資料盤點", "reason": "列為面試技能驗證，不推論不會。", "suggestion": "若有實作，補非機密資料結構與查詢用途。"}, {"id": "I03", "rule_id": "HR07", "source_ids": [], "application_note": "AI原型與流程化案例仍缺範圍", "context_limit": "僅依履歷文字，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "Claude Code 多分支流程與共用 skill 庫", "reason": "追問能否用AI快速驗證產品假設。", "suggestion": "補一次AI原型或自動化的輸入、產物與驗證。"}, {"id": "I04", "rule_id": "HM05", "source_ids": [], "application_note": "安全觀察與年化留存方法尚待確認", "context_limit": "僅依履歷文字，未外部查證", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "依目前掌握的情況", "reason": "可保留成果，但面試需區分監測紀錄與口述。", "suggestion": "交代事件來源、觀察覆蓋與留存年化公式。"}, {"id": "I05", "rule_id": "HM06", "source_ids": [], "application_note": "技術方案與財務優先序責任不夠具體", "context_limit": "僅依履歷文字，未外部查證", "category": "ownership", "severity": "interview_follow_up", "block_target": null, "claim": "與資料科學團隊合作", "reason": "面試需確認方案討論及跨財務協作深度。", "suggestion": "補本人與工程、財務各自的決策與協商範圍。"}], "decision": {"recommendation": "interview", "evidence": ["主導 Juicy 上線", "與 QA 制定 UAT 驗收案例、排定上線計畫", "以 Android 售價不變作對照"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["「主導 Juicy 上線」及支付整合提供新產品交付線索。", "「以 Android 售價不變作對照」支持成長驗證能力。", "「選擇首次登入引導確認、不強迫修改」呈現使用者與風險取捨。"], "key_gaps": ["同一產品完整0到1探索驗證與迭代責任。", "JSON、基本SQL及資料結構規格。", "AI原型流程化及跨財務技術方案決策深度。"], "strengths": ["改版案例｜「選擇首次登入引導確認、不強迫修改」｜能處理既有使用者風險。", "定價案例｜「以 Android 售價不變作對照」｜支持成長實驗判斷。", "交付案例｜「與 QA 制定 UAT 驗收案例、排定上線計畫」｜完整落地動作具體。"], "interview_questions": ["請以Juicy串起探索、驗證、設計、開發、上線及迭代，說明直接責任。", "請以API整合範例說明JSON資料結構與基本SQL用途。", "展示一次Claude Code原型或自動化及驗證方式。", "PoC如何設成功門檻並轉入Pilot與規模化？", "留存如何年化，安全事件由哪些紀錄追蹤？", "工程與財務優先序分歧時如何取捨及拍板？"], "editorial_appendix": ["可集中一個完整0到1代表作，降低跨段拼接成本；不影響現有能力判斷。"], "spectrum": {"level": 8, "uncertainty_levels": 1, "basis": "多案例支持交付、支付與成長；清楚取捨及可比較衡量，且主動標示觀察限制。必要技術及完整0到1細節仍需面試核對，未達高度可追溯。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷K｜第 1 輪｜model_id: unknown

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「主導 Juicy 上線」及支付、驗收、成長案例足以約談，技術與完整探索鏈路待驗證。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 近 10 年 PM 經驗，經手 6 款產品 | 智慧停車情境的轉移方式可於面試確認 |
| role_evidence | 足夠 | 整理為 PRD 與 Axure Prototype | 完整0到1、JSON／SQL、資料結構與AI原型待核對 |
| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 可追問新產品探索的替代方案 |
| outcome_quality | 強 | 為觀察差異，非因果 | 年化留存算法及安全監測來源待核對 |
| ownership | 足夠 | 由我主責規劃，與工程團隊密切協作 | 財務對齊及工程方案決策分工待問 |
| readability | 足夠 | 資深產品經理｜Senior Product Manager | 代表作與詳細方法較分散，可集中對應JD |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 3年以上Software Product Manager經驗 | 必要 | supported | Product Manager｜尚凡國際創新科技 | 有多年軟體產品管理經歷。 |
| 直接負責完整0到1探索、驗證、設計、開發、上線與迭代 | 必要 | partial | 主導 Juicy 上線 | 有新產品上線及設計交付；同一案例探索驗證與後續迭代待核對。 |
| 清楚的PRD、流程圖與資料結構規格 | 必要 | partial | 整理為 PRD 與 Axure Prototype | PRD與流程有案例；資料結構規格未呈現。 |
| 理解API、JSON與基本SQL | 必要 | partial | API 串接規劃、舊系統資料盤點 | API有整合線索；JSON及SQL未呈現，面試以工作樣本確認。 |
| 智慧停車或MaaS產品完整週期推進 | 必要 | partial | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 完整交付可轉移；特定場域經驗未呈現，不當必要產業門檻。 |
| 跨業務、客服、財務釐清情境與優先序 | 必要 | partial | 對接 16 個需求單位 | 客服與業務有依據；財務對齊及分歧處理待問。 |
| AI原型、產品AI機會與PM流程化 | 必要 | partial | 用於規格撰寫、資料整理與分析 | AI協作及產品應用有證據；快速原型與流程化成效待問。 |
| 測試驗收、數據成長及PoC到Pilot到Scale | 必要 | partial | 與 QA 制定 UAT 驗收案例 | 驗收與成長實驗具體；PoC至規模化轉換未完整交代。 |
| 與工程設計技術方案及跨部門外部協作 | 必要 | supported | 與 CodaPay 新加坡技術團隊協調串接 | 支付整合及工程協作可支持面試。 |
| 停車、交通、MaaS、保險、支付或FinTech經驗 | 加分 | supported | 導入 CodaPay | 具支付經驗，無須同時符合各產業。 |
| Prompt engineering、RAG或Agent實作 | 加分 | unknown | Claude Code 多分支流程與共用 skill 庫 | 工具使用不等同特定RAG或Agent實作。 |
| Growth、數據分析及AI／LLM實際工作應用 | 加分 | supported | 以 Android 售價不變作對照 | 定價實驗及AI規格、資料處理均有線索。 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 曾設計定價實驗、規劃網頁付款 | 支付、成長與軟體交付直接相關 |
| HR02 | supported | 現任 1111 招募系統 Product Owner | 企業流程經驗可轉移至營運產品 |
| HR03 | supported | 由我主責規劃，與工程團隊密切協作 | 規劃責任清楚；技術分工可追問 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 呈現流程改變與比較期間 |
| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 有使用者風險與交付取捨 |
| HR06 | supported | 從交友與訂閱制 App 到企業招募系統 | 職涯跨客群且方向連貫 |
| HR07 | supported | 與 CodaPay 新加坡技術團隊協調串接 | 協作有真實應用情境 |
| HR08 | supported | 資深產品經理｜Senior Product Manager | 定位與代表案例可辨識 |
| HR09 | partial | 依目前掌握的情況 | 安全結果需核對觀察來源 |
| HR10 | supported | 接下來，我希望將更多心力放回產品策略 | 與策略及完整週期責任相容 |
| HR11 | unknown | 台北市、新北市，可接受遠端或混合辦公 | JD未明列地點，未見已知衝突 |
| HR12 | supported | 主導 Juicy 上線 | 相關案例足以約談，核心細節待驗證 |
| HM01 | supported | 訂閱制 B2C App 與雙邊媒合平台 | 平台與支付能力可轉移 |
| HM02 | supported | 最大宗是溝通管道中斷 | 客服訊號改變排序 |
| HM03 | supported | 選擇首次登入引導確認、不強迫修改 | 風險取捨清楚 |
| HM04 | supported | 依抽成、稅、手續費及撥款週期做實收試算 | 商業成本連到產品選擇 |
| HM05 | supported | 為觀察差異，非因果 | 衡量限制明示，算法待核對 |
| HM06 | partial | 與資料科學團隊合作 | 需確認財務及技術決策分工 |
| HM07 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 驗收與分階段交付具體 |
| HM08 | partial | API 串接規劃、舊系統資料盤點 | JSON、SQL及結構待驗證 |
| HM09 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 責任複雜度足以約談 |
| HM10 | supported | 由我主責規劃，與工程團隊密切協作 | 代表證據可辨識 |
| HM11 | supported | 依客服測試回饋調整推薦規則 | 已有回饋修正行動 |
| HM12 | supported | 主導 Juicy 上線 | 0到1鏈路值得面試核對 |
| HM13 | supported | —（方法層） | 按JD獨立取證，無真人校準 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「主導 Juicy 上線」及支付整合提供新產品交付線索。 |
| 2 | 「以 Android 售價不變作對照」支持成長驗證能力。 |
| 3 | 「選擇首次登入引導確認、不強迫修改」呈現使用者與風險取捨。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 同一產品完整0到1探索驗證與迭代責任。 | 請以Juicy串起探索、驗證、設計、開發、上線及迭代，說明直接責任。 |
| 2 | JSON、基本SQL及資料結構規格。 | 請以API整合範例說明JSON資料結構與基本SQL用途。 |
| 3 | AI原型流程化及跨財務技術方案決策深度。 | 展示一次Claude Code原型或自動化及驗證方式。 |

其餘追問：
- PoC如何設成功門檻並轉入Pilot與規模化？
- 留存如何年化，安全事件由哪些紀錄追蹤？
- 工程與財務優先序分歧時如何取捨及拍板？

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：

- 改版案例｜「選擇首次登入引導確認、不強迫修改」｜能處理既有使用者風險。
- 定價案例｜「以 Android 售價不變作對照」｜支持成長實驗判斷。
- 交付案例｜「與 QA 制定 UAT 驗收案例、排定上線計畫」｜完整落地動作具體。

**可改進（5 點）**：

- 位置：尚凡／Juicy
- 原句：主導 Juicy 上線
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：相關上線足以面試；需確認是否直接負責探索驗證及迭代。
- 建議方向：補同一案例的探索依據、驗證與迭代責任。

- 位置：專業技能／跨部門與整合
- 原句：API 串接規劃、舊系統資料盤點
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：列為面試技能驗證，不推論不會。
- 建議方向：若有實作，補非機密資料結構與查詢用途。

- 位置：專業技能／AI協作
- 原句：Claude Code 多分支流程與共用 skill 庫
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：追問能否用AI快速驗證產品假設。
- 建議方向：補一次AI原型或自動化的輸入、產物與驗證。

- 位置：1111／登入安全與留存
- 原句：依目前掌握的情況
- 問題類型：measurement
- 嚴重度：interview_follow_up
- 影響：可保留成果，但面試需區分監測紀錄與口述。
- 建議方向：交代事件來源、觀察覆蓋與留存年化公式。

- 位置：1111／AI功能
- 原句：與資料科學團隊合作
- 問題類型：ownership
- 嚴重度：interview_follow_up
- 影響：面試需確認方案討論及跨財務協作深度。
- 建議方向：補本人與工程、財務各自的決策與協商範圍。

**編輯附件**（不影響判斷）：
- 可集中一個完整0到1代表作，降低跨段拼接成本；不影響現有能力判斷。

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠
方向與資源以定價、成本及優先序支持；未將團隊人數視為能力加分。

### 8. 未測試聲明
PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run
所有成果均為履歷自述，非外部驗證；各缺口只在主要維度記一次。

### 成果分類補表
| 原句片段 | 分類 | 限制 |
| :-- | :-- | :-- |
| 約 50 項大項功能上線 | output | 主表分類，非外部驗證 |
| 停機約 1.5 小時 | output | 主表分類，非外部驗證 |
| 需求平均處理週期由 100.4 天降至 30.9 天 | outcome | 主表分類，非外部驗證 |
| 該群年化留存 81.2%，同期全站 74.2% | outcome | 主表分類，非外部驗證 |
| 選擇首次登入引導確認、不強迫修改 | decision | 主表分類，非外部驗證 |
| 目前專案仍在開發中 | in_progress | 主表分類，非外部驗證 |
| 全站活躍付費廠商約 6.6 萬家 | context | 系統規模，非個人成果 |
| 另於 2026/01–06 上線 111 項 Roadmap 細項 | output | 細項交付，不與50項直接相加 |
| 第一階段於 2025/10 離峰切換上線 | output | 改版階段交付 |
| 於 2026/04/17 上線簽章驗證 | output | 工程協作產出 |
| 上線後至 2026/10 未再出現同類帳號冒用 | outcome | 依目前掌握情況，非完整監測證明 |
| 完成 1,726／1,857 張需求與問題單，約 93% | output | 工單處理量及比例 |
| 需求管線觸及 1,279 家活躍付費廠商 | context | 觸及群組，非因果成效 |
| AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才 | output | 未提供採用與品質結果 |
| 依客服測試回饋調整推薦規則 | decision | 回饋後修正 |
| 降價期 iOS 非續訂營收較基準期增 5% | outcome | 同時參照Android及期間 |
| Android 減 18%，相對變化約多 28% | outcome | 平台非隨機對照，仍有干擾 |
| 還原原價後 iOS 較基準期減 65% | outcome | 階段性觀察 |
| 依結果全面調降售價 | decision | 產品定價選擇 |
| Peach 網頁付款占營收由 24% 至 80% 以上 | outcome | 通路占比，非總營收成長 |
| 與 CodaPay 新加坡技術團隊協調串接 | output | 跨團隊整合 |
| KOOL 訂閱與付費牆規劃上線 | output | 付費設計已交付 |
| 才開放精選網紅資格 | decision | 資格門檻設計 |
| 上線後 6 週男性 DAU 約 3,200 至 1.25 萬 | outcome | 產品上線與行銷導流整體表現 |
| 與最多約 10 位外國實習生協作 | context | 協作範圍，不等於直屬管理 |
| 美國、墨西哥、巴西、印尼、馬來西亞、日本、韓國 7 個市場 | output | 市場在地化交付，非業務增長 |
| 導入 CodaPay | output | 支付渠道交付 |
| 提出 7／30／90 天訂閱方案與加贈內容 | decision | 實收試算後提案，不等於已實現結果 |
| Newegg.com 商品資訊英翻中與校對 | output | 工作產出 |
| 將信件與即時通整合排在其他新功能之前 | decision / in_progress | 已發生排序，專案仍開發中 |

### 執行紀錄
technical_failure：前次因usage_limit中斷；本次續行同一輪，未新增審查輪數。


## A-jd30-M｜履歷M

```json
{"rubric_version":"4.2","resume_id":"M","job_id":"jd30","job_input":"summary","model_id":"unknown","run_id":"A-jd30-M","human_calibrated":false,"requirements":[{"id":"R01","text":"3年以上Software Product Manager經驗","type":"required","status":"supported","evidence":["近 10 年 PM 經驗，經手 6 款產品"],"blocks_interview":false,"reason":"軟體產品經歷跨App與企業系統。"},{"id":"R02","text":"至少一次完整0到1探索、驗證、設計、開發、上線與迭代直接負責","type":"required","status":"partial","evidence":["主導 Juicy 上線"],"blocks_interview":false,"reason":"上線與設計交付充分，但同一產品探索驗證及迭代鏈待核對。"},{"id":"R03","text":"清楚規格文件：PRD、流程圖、資料結構","type":"required","status":"partial","evidence":["整理為 PRD 與 Axure Prototype"],"blocks_interview":false,"reason":"PRD與流程有案例，資料結構深度待確認。"},{"id":"R04","text":"理解API、JSON與基本SQL","type":"required","status":"partial","evidence":["API 串接規劃、舊系統資料盤點"],"blocks_interview":false,"reason":"API有串接案例，JSON與SQL未呈現；交DBA不等於不會SQL。"},{"id":"R05","text":"跨部門痛點整理、優先序與技術方案協作","type":"required","status":"supported","evidence":["依使用者旅程排優先級"],"blocks_interview":false,"reason":"客服訊號、工程協作與驗收有直接例證。"},{"id":"R06","text":"AI原型、AI產品機會與PM流程化","type":"required","status":"partial","evidence":["自建 Claude Code 協作流程"],"blocks_interview":false,"reason":"規格與分析流程及AI功能有實作，快速原型未呈現。"},{"id":"R07","text":"上線驗收、成熟產品成長與新產品PoC→Pilot→Scale","type":"required","status":"partial","evidence":["與 QA 制定 UAT 驗收案例"],"blocks_interview":false,"reason":"驗收與成長分析有案例，新產品階段轉換仍待驗證。"},{"id":"R08","text":"停車、交通、MaaS、保險、支付或FinTech經驗","type":"preferred","status":"supported","evidence":["並與 CodaPay 新加坡技術團隊協調串接"],"blocks_interview":false,"reason":"符合支付分支；無須同時具備所有產業。"},{"id":"R09","text":"Prompt engineering、RAG或Agent實作","type":"preferred","status":"partial","evidence":["自建 Claude Code 協作流程"],"blocks_interview":false,"reason":"流程與skill是線索，未明示具體技術實作。"},{"id":"R10","text":"Growth或數據分析經驗","type":"preferred","status":"supported","evidence":["以 Android 售價不變作對照"],"blocks_interview":false,"reason":"定價實驗與留存分析可轉移。"},{"id":"R11","text":"AI／LLM用於規格、資料處理、自動化或原型","type":"preferred","status":"supported","evidence":["用於規格撰寫、資料整理與分析"],"blocks_interview":false,"reason":"至少規格與資料處理已有使用情境。"}],"dimensions":[{"id":"positioning","rating":"強","evidence":["訂閱制 B2C App 與雙邊媒合平台。"],"missing":["智慧停車領域需到職學習，不阻擋約談。"],"issue_ids":[]},{"id":"role_evidence","rating":"足夠","evidence":["整理為 PRD 與 Axure Prototype"],"missing":["同一0到1完整週期、JSON／SQL與AI原型待追問。"],"issue_ids":["I01","I02","I03"]},{"id":"decision_depth","rating":"強","evidence":["選擇首次登入引導確認、不強迫修改"],"missing":[],"issue_ids":[]},{"id":"outcome_quality","rating":"強","evidence":["為觀察差異，非因果。"],"missing":["安全成果是目前掌握情況，非監測查證。"],"issue_ids":["I04"]},{"id":"ownership","rating":"強","evidence":["由我擬定取數的資料表與欄位"],"missing":["0到1角色核對見I01，不另扣分。"],"issue_ids":[]},{"id":"readability","rating":"足夠","evidence":["全站活躍付費廠商約 6.6 萬家"],"missing":["摘要與自傳重複可壓縮，不影響面試。"],"issue_ids":[]}],"results":[{"quote":"全站活躍付費廠商約 6.6 萬家","kinds":["context"]},{"quote":"約 50 項大項功能上線","kinds":["output"]},{"quote":"選擇首次登入引導確認、不強迫修改","kinds":["decision"]},{"quote":"需求平均處理週期由 100.4 天降至 30.9 天","kinds":["outcome"]},{"quote":"為觀察差異，非因果。","kinds":["outcome"]},{"quote":"兩案皆開發中","kinds":["decision","in_progress"]}],"hr_questions":[{"rule_id":"HR01","status":"supported","resume_evidence":["近 10 年 PM 經驗，經手 6 款產品"],"application_note":"軟體產品與支付經驗可轉移"},{"rule_id":"HR02","status":"supported","resume_evidence":["企業端招募系統全模組與求職端公司頁"],"application_note":"近期責任範圍清楚"},{"rule_id":"HR03","status":"supported","resume_evidence":["由我擬定取數的資料表與欄位"],"application_note":"區分本人分析與DBA取數"},{"rule_id":"HR04","status":"supported","resume_evidence":["需求平均處理週期由 100.4 天降至 30.9 天"],"application_note":"流程改善有期間與基準"},{"rule_id":"HR05","status":"supported","resume_evidence":["選擇首次登入引導確認、不強迫修改"],"application_note":"具風險與體驗取捨"},{"rule_id":"HR06","status":"supported","resume_evidence":["從交友與訂閱制 App 到企業招募系統"],"application_note":"跨客群責任脈絡清楚"},{"rule_id":"HR07","status":"supported","resume_evidence":["與 QA 制定 UAT 驗收案例"],"application_note":"技能有交付情境"},{"rule_id":"HR08","status":"supported","resume_evidence":["資深產品經理｜Senior Product Manager"],"application_note":"定位與經驗易辨識"},{"rule_id":"HR09","status":"partial","resume_evidence":["依目前掌握的情況"],"application_note":"安全觀察來源須核對"},{"rule_id":"HR10","status":"supported","resume_evidence":["我希望將更多心力放回產品策略"],"application_note":"與方向選擇責任相容"},{"rule_id":"HR11","status":"unknown","resume_evidence":["錄取後三週可上班"],"application_note":"JD未列地點等條件，無已知衝突"},{"rule_id":"HR12","status":"supported","resume_evidence":["主導 Juicy 上線"],"application_note":"已有約談價值，補驗完整週期"}],"content_questions":[{"rule_id":"HM01","primary_dimension":"positioning","status":"supported","resume_evidence":["訂閱制 B2C App 與雙邊媒合平台。"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM02","primary_dimension":"decision_depth","status":"supported","resume_evidence":["客服反映配對名單「少又舊」"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM03","primary_dimension":"decision_depth","status":"supported","resume_evidence":["選擇首次登入引導確認、不強迫修改"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM04","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依結果全面調降售價"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM05","primary_dimension":"outcome_quality","status":"supported","resume_evidence":["為觀察差異，非因果。"],"evidence_type":"outcome","source_ids":[],"interview_question":"留存年化方式及樣本可比性為何？"},{"rule_id":"HM06","primary_dimension":"ownership","status":"supported","resume_evidence":["與資料科學團隊合作"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM07","primary_dimension":"role_evidence","status":"supported","resume_evidence":["與 QA 制定 UAT 驗收案例"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM08","primary_dimension":"role_evidence","status":"partial","resume_evidence":["API 串接規劃、舊系統資料盤點"],"evidence_type":"output","source_ids":[],"interview_question":"請用API payload與SQL範例說明技術協作。"},{"rule_id":"HM09","primary_dimension":"ownership","status":"supported","resume_evidence":["統籌影響評估、範圍與時程"],"evidence_type":"output","source_ids":[],"interview_question":null},{"rule_id":"HM10","primary_dimension":"readability","status":"supported","resume_evidence":["企業端招募系統全模組與求職端公司頁"],"evidence_type":"context","source_ids":[],"interview_question":null},{"rule_id":"HM11","primary_dimension":"decision_depth","status":"supported","resume_evidence":["依客服測試回饋調整推薦規則"],"evidence_type":"decision","source_ids":[],"interview_question":null},{"rule_id":"HM12","primary_dimension":"role_evidence","status":"supported","resume_evidence":["主導 Juicy 上線"],"evidence_type":"output","source_ids":[],"interview_question":"請走讀同一0到1產品從探索到迭代。"},{"rule_id":"HM13","primary_dimension":"","status":"not_applicable","resume_evidence":[],"evidence_type":null,"source_ids":[],"interview_question":null}],"issues":[{"id":"I01","rule_id":"HM12","source_ids":[],"application_note":"面試核對，不作淘汰條件","context_limit":"僅履歷自述，未外部驗證","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"主導 Juicy 上線","reason":"完整0到1直接負責是核心必要條件，履歷未串連探索驗證與後續迭代；已有上線及多產品證據，值得面試核對。","suggestion":"選同一產品補充問題假設、驗證、設計、上線與迭代責任。"},{"id":"I02","rule_id":"HM08","source_ids":[],"application_note":"面試核對，不作淘汰條件","context_limit":"僅履歷自述，未外部驗證","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"API 串接規劃、舊系統資料盤點","reason":"JSON與SQL未呈現，需確認明文技術素養；不把交DBA視為能力不足。","suggestion":"準備資料結構、JSON payload與基本SQL工作樣本。"},{"id":"I03","rule_id":"HR07","source_ids":[],"application_note":"面試核對，不作淘汰條件","context_limit":"僅履歷自述，未外部驗證","category":"requirement","severity":"interview_follow_up","block_target":null,"claim":"自建 Claude Code 協作流程","reason":"AI規格與分析有證據，但JD快速原型及PoC至Scale的驗證流程未清楚呈現，留面試核對。","suggestion":"展示一次AI原型及驗證交付流程，區分已做與未做。"},{"id":"I04","rule_id":"HR09","source_ids":[],"application_note":"面試核對，不作淘汰條件","context_limit":"僅履歷自述，未外部驗證","category":"measurement","severity":"interview_follow_up","block_target":null,"claim":"依目前掌握的情況","reason":"未再出現冒用是有限觀察，不能當已證實安全成效；面試追問資訊來源與涵蓋範圍。","suggestion":"維持限制語，說明通報或監測來源、分類與觀察期間。"}],"decision":{"recommendation":"interview","evidence":["主導 Juicy 上線","選擇首次登入引導確認、不強迫修改","自建 Claude Code 協作流程"],"blocking_unknowns":[]},"seniority":{"delivery":"強","po_coordination":"強","direction_resources":"足夠"},"interview_reasons":["「主導 Juicy 上線」支持產品交付經驗。","「選擇首次登入引導確認、不強迫修改」呈現取捨。","「自建 Claude Code 協作流程」契合AI工作方式。"],"key_gaps":["同一0到1產品完整探索至迭代責任待核對。","JSON、基本SQL與資料結構工作深度未明。","AI快速原型與PoC→Pilot→Scale案例待補。"],"strengths":["近期系統交付及驗收責任具體。","使用者痛點能轉成優先序與風險取捨。","實驗、留存與團隊成果有衡量限制。"],"interview_questions":["請選同一0到1產品說明探索、驗證、設計、開發、上線與迭代，以及你的權責。","請展示PRD資料結構、JSON payload及基本SQL範例。","Claude Code如何產出可測試原型？如何從PoC轉Pilot再Scale？","AI推薦的驗收規則與資料科學團隊如何分工？","留存年化公式、分母及群體可比性為何？","安全未再發生的資訊來源與監測範圍為何？"],"editorial_appendix":["可壓縮摘要與自傳重複內容，將支付與AI案例前移；不影響能力判斷。"],"spectrum":{"level":8,"uncertainty_levels":1,"basis":"多個直接案例、清楚取捨與比較衡量支持面試；完整0到1及技術素養仍需核對。"},"ai_authorship":{"determination":"not_determinable_from_style","probability":null,"editorial_observations":[]},"tests":{"pdf_extraction":"not_tested","ats_import":"not_tested","ai_provenance":"indeterminate_from_text_alone"},"validation":{"structural_checks":"not_run","behavioral_regressions":"not_run","real_ats_test":"not_run","human_calibration":"not_run"}}
```

## 單份審查｜履歷M｜第 1 輪｜model_id: unknown

### 1. 結論

- 招聘決定：interview

- Level：8（±1）

- 一句話理由：「主導 Juicy 上線」加上具體取捨、支付與AI流程案例，支持約談驗證完整週期。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 訂閱制 B2C App 與雙邊媒合平台。 | 智慧停車領域需到職學習，不阻擋約談。 |
| role_evidence | 足夠 | 整理為 PRD 與 Axure Prototype | 同一0到1完整週期、JSON／SQL與AI原型待追問。 |
| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 無關鍵缺口；履歷自述仍待面試驗證 |
| outcome_quality | 強 | 為觀察差異，非因果。 | 安全成果是目前掌握情況，非監測查證。 |
| ownership | 強 | 由我擬定取數的資料表與欄位 | 0到1角色核對見I01，不另扣分。 |
| readability | 足夠 | 全站活躍付費廠商約 6.6 萬家 | 摘要與自傳重複可壓縮，不影響面試。 |
### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 3年以上Software Product Manager經驗 | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 軟體產品經歷跨App與企業系統。 |
| 至少一次完整0到1探索、驗證、設計、開發、上線與迭代直接負責 | 必要 | partial | 主導 Juicy 上線 | 上線與設計交付充分，但同一產品探索驗證及迭代鏈待核對。 |
| 清楚規格文件：PRD、流程圖、資料結構 | 必要 | partial | 整理為 PRD 與 Axure Prototype | PRD與流程有案例，資料結構深度待確認。 |
| 理解API、JSON與基本SQL | 必要 | partial | API 串接規劃、舊系統資料盤點 | API有串接案例，JSON與SQL未呈現；交DBA不等於不會SQL。 |
| 跨部門痛點整理、優先序與技術方案協作 | 必要 | supported | 依使用者旅程排優先級 | 客服訊號、工程協作與驗收有直接例證。 |
| AI原型、AI產品機會與PM流程化 | 必要 | partial | 自建 Claude Code 協作流程 | 規格與分析流程及AI功能有實作，快速原型未呈現。 |
| 上線驗收、成熟產品成長與新產品PoC→Pilot→Scale | 必要 | partial | 與 QA 制定 UAT 驗收案例 | 驗收與成長分析有案例，新產品階段轉換仍待驗證。 |
| 停車、交通、MaaS、保險、支付或FinTech經驗 | 加分 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 符合支付分支；無須同時具備所有產業。 |
| Prompt engineering、RAG或Agent實作 | 加分 | partial | 自建 Claude Code 協作流程 | 流程與skill是線索，未明示具體技術實作。 |
| Growth或數據分析經驗 | 加分 | supported | 以 Android 售價不變作對照 | 定價實驗與留存分析可轉移。 |
| AI／LLM用於規格、資料處理、自動化或原型 | 加分 | supported | 用於規格撰寫、資料整理與分析 | 至少規格與資料處理已有使用情境。 |
JD工作職責以必要工作能力對照；partial均不是已證實不符，不列blocking。

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 軟體產品與支付經驗可轉移 |
| HR02 | supported | 企業端招募系統全模組與求職端公司頁 | 近期責任範圍清楚 |
| HR03 | supported | 由我擬定取數的資料表與欄位 | 區分本人分析與DBA取數 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 流程改善有期間與基準 |
| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 具風險與體驗取捨 |
| HR06 | supported | 從交友與訂閱制 App 到企業招募系統 | 跨客群責任脈絡清楚 |
| HR07 | supported | 與 QA 制定 UAT 驗收案例 | 技能有交付情境 |
| HR08 | supported | 資深產品經理｜Senior Product Manager | 定位與經驗易辨識 |
| HR09 | partial | 依目前掌握的情況 | 安全觀察來源須核對 |
| HR10 | supported | 我希望將更多心力放回產品策略 | 與方向選擇責任相容 |
| HR11 | unknown | 錄取後三週可上班 | JD未列地點等條件，無已知衝突 |
| HR12 | supported | 主導 Juicy 上線 | 已有約談價值，補驗完整週期 |
| HM01 | supported | 訂閱制 B2C App 與雙邊媒合平台。 | 可轉移B2C與企業產品能力 |
| HM02 | supported | 客服反映配對名單「少又舊」 | 客服痛點連結規則修正 |
| HM03 | supported | 選擇首次登入引導確認、不強迫修改 | 有風險與體驗取捨 |
| HM04 | supported | 依結果全面調降售價 | 定價與支付具商業理解 |
| HM05 | supported | 為觀察差異，非因果。 | 有比較與限制，仍須核對方法 |
| HM06 | supported | 與資料科學團隊合作 | 跨部門責任有界線 |
| HM07 | supported | 與 QA 制定 UAT 驗收案例 | 有規格驗收到分階段交付 |
| HM08 | partial | API 串接規劃、舊系統資料盤點 | JSON與SQL須工作樣本驗證 |
| HM09 | supported | 統籌影響評估、範圍與時程 | 具資深IC自主範圍 |
| HM10 | supported | 企業端招募系統全模組與求職端公司頁 | 資訊足以定位代表作 |
| HM11 | supported | 依客服測試回饋調整推薦規則 | 回饋確有改變產品規則 |
| HM12 | supported | 主導 Juicy 上線 | 已有約談基礎，補驗完整週期 |
| HM13 | not_applicable | — | 方法規則，不是候選人能力項 |
本審查先依JD獨立判讀，不以姓名、公司或學歷作能力代理；HM13不加分。

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「主導 Juicy 上線」支持產品交付經驗。 |
| 2 | 「選擇首次登入引導確認、不強迫修改」呈現取捨。 |
| 3 | 「自建 Claude Code 協作流程」契合AI工作方式。 |
| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 同一0到1產品完整探索至迭代責任待核對。 | 請選同一0到1產品說明探索、驗證、設計、開發、上線與迭代，以及你的權責。 |
| 2 | JSON、基本SQL與資料結構工作深度未明。 | 請展示PRD資料結構、JSON payload及基本SQL範例。 |
| 3 | AI快速原型與PoC→Pilot→Scale案例待補。 | Claude Code如何產出可測試原型？如何從PoC轉Pilot再Scale？ |
### 6. 評語（給寫稿者的具體回饋）

**做得好（3 點）**

- 1111交付｜「與 QA 制定 UAT 驗收案例」｜對應上線前測試驗收與工程協作。

- 1111改版｜「選擇首次登入引導確認、不強迫修改」｜呈現既有客戶風險與體驗取捨。

- 數據分析｜「為觀察差異，非因果。」｜保留衡量限制，利於成長分析面試。

**可改進（4 點）**

- 位置：Juicy上線

  - 原句：主導 Juicy 上線

  - 問題類型：requirement

  - 嚴重度：interview_follow_up

  - 影響：完整0到1直接負責是核心必要條件，履歷未串連探索驗證與後續迭代；已有上線及多產品證據，值得面試核對。

  - 建議方向：選同一產品補充問題假設、驗證、設計、上線與迭代責任。

- 位置：專業技能

  - 原句：API 串接規劃、舊系統資料盤點

  - 問題類型：requirement

  - 嚴重度：interview_follow_up

  - 影響：JSON與SQL未呈現，需確認明文技術素養；不把交DBA視為能力不足。

  - 建議方向：準備資料結構、JSON payload與基本SQL工作樣本。

- 位置：專業技能

  - 原句：自建 Claude Code 協作流程

  - 問題類型：requirement

  - 嚴重度：interview_follow_up

  - 影響：AI規格與分析有證據，但JD快速原型及PoC至Scale的驗證流程未清楚呈現，留面試核對。

  - 建議方向：展示一次AI原型及驗證交付流程，區分已做與未做。

- 位置：登入安全盤點

  - 原句：依目前掌握的情況

  - 問題類型：measurement

  - 嚴重度：interview_follow_up

  - 影響：未再出現冒用是有限觀察，不能當已證實安全成效；面試追問資訊來源與涵蓋範圍。

  - 建議方向：維持限制語，說明通報或監測來源、分類與觀察期間。

**編輯附件**（不影響判斷）：可壓縮摘要與自傳重複內容，將支付與AI案例前移；不影響能力判斷。

### 7. 資深能力分布

delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

方向有優先序與定價決策支持；組織資源配置證據有限，不要求未列於JD的P&L或管理人數。

### 8. 未測試聲明

PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

履歷內部敘述並非外部查證。未執行真實ATS、行為回歸或錄取效度校準。

### 成果分類補表
| 成果／聲明 | 分類 | 限制 |
| :-- | :-- | :-- |
| 近10年、6款產品；16個需求單位；團隊3名企劃 | context | 規模與年資不自動代表能力 |
| 50項大項及111項Roadmap細項 | output | 不同粒度，不加總 |
| 三階段改版、重複信箱、首次登入引導 | context／decision／output | 第一階段已上線，整體三階段不當全完成 |
| 離峰切換、停機約1.5小時 | output | 交付及停機資訊，非成長結果 |
| 十多家帳號遭冒用、簽章驗證上線 | context／output | 安全事件背景與交付 |
| 上線後至2026/10未再出現同類冒用 | outcome | 目前掌握的觀察，非監測紀錄 |
| 處理週期100.4至30.9天；完成1726/1857約93% | outcome／output | 前者流程成效，後者工單完成量 |
| 信件即時通整合、搜尋改版優先 | decision／in_progress | 未當已實現結果 |
| 排序、20天不重複推薦及首次配對上限 | decision／output | 規則調整，採用成效未提供 |
| 1279家、1.9%；留存81.2%對74.2% | context／outcome | 觀察差異，非因果 |
| AI公司簡介、職缺說明、推薦人才 | output／decision | 已上線；未提供使用者成效 |
| 三階段定價；iOS增5%、Android減18%、相對多28% | outcome／decision | 各期21天；相對變化不當百分點 |
| 還原原價後iOS減65%、全面降價 | outcome／decision | 時期因素及樣本待核對 |
| Peach網頁付款營收占比24%至80%以上 | outcome／output | 支付組成變化，不等於總營收成長 |
| KOOL訂閱、付費牆及精選資格 | output／decision | 規劃上線，不補收入成果 |
| Juicy上線及男性DAU3200至1.25萬 | output／outcome | 6週產品與行銷整體表現 |
| SweetRing七市場、最多約十位實習生 | context／output | 協作規模，非直屬管理 |
| CodaPay電信帳單與超商付款、7/30/90天方案 | output／decision | 實收試算支持方案，未提供收入結果 |
| 英翻中與英文校對 | output | 工作產出，非PM結果 |
| Claude Code十二分支、二十三共用skill | output | 流程建置，不把數量當成效率成效 |


## B-jd30｜揭盲：甲=K、乙=M；偏好=M

```json
{"job_id":"jd30","order":"甲=K/乙=M","differences":[{"what":"甲呈現由工單痛點排優先序；乙另提供配對規則的根因診斷與具體調整。","hiring_meaning":"乙讓主管可追問從客服問題、競品驗證到規則設計及驗收的鏈路，貼近需求定義與迭代；不把甲乙共有的優先序例子當能力差距。","type":"capability"},{"what":"相同留存觀察，乙補明本人定義取數欄位、DBA取數及試算表分析的分工。","hiring_meaning":"乙更清楚界定數據分析的直接責任；可驗證欄位選擇與留存算法，並另測職缺必備的基本SQL、JSON，不能把委託取數視為SQL能力證明。","type":"measurement"}],"preference":"乙","reason":"乙新增配對規則診斷的具體鏈路，並界定留存分析的取數分工，更能形成需求驗證與技術素養的面試問題；共同的AI協作與交付經驗不重複加分，SQL、JSON及完整0到1責任仍須核問。","evidence_甲":["例如廠商抱怨工單中，最大宗是溝通管道中斷，我便將信件與即時通整合排在其他新功能之前，目前專案仍在開發中。","比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。"],"evidence_乙":["客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。","由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。"]}
```

## 版本比較｜jd30｜順序 甲=K 乙=M｜model_id: unknown
- 偏好：乙（揭盲：M）

| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 甲呈現由工單痛點排優先序；乙另提供配對規則的根因診斷與具體調整。 | 乙讓主管可追問從客服問題、競品驗證到規則設計及驗收的鏈路，貼近需求定義與迭代；不把甲乙共有的優先序例子當能力差距。 | capability | 例如廠商抱怨工單中，最大宗是溝通管道中斷，我便將信件與即時通整合排在其他新功能之前，目前專案仍在開發中。 | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 |
| 2 | 相同留存觀察，乙補明本人定義取數欄位、DBA取數及試算表分析的分工。 | 乙更清楚界定數據分析的直接責任；可驗證欄位選擇與留存算法，並另測職缺必備的基本SQL、JSON，不能把委託取數視為SQL能力證明。 | measurement | 比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |

- 理由（≤120 字）：乙新增配對規則診斷的具體鏈路，並界定留存分析的取數分工，更能形成需求驗證與技術素養的面試問題；共同的AI協作與交付經驗不重複加分，SQL、JSON及完整0到1責任仍須核問。


# jd31｜逐次輸出


## A-jd31-K｜履歷K

```json
{"rubric_version": "4.2", "resume_id": "K", "job_id": "jd31", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd31-K", "human_calibrated": false, "requirements": [{"id": "R01", "text": "3年以上產品規劃與需求訪談經驗", "type": "required", "status": "partial", "evidence": ["近 10 年 PM 經驗，經手 6 款產品"], "blocks_interview": false, "reason": "產品規劃年資充分；直接客戶訪談的年資與案例待釐清。"}, {"id": "R02", "text": "熟悉0到1或迭代優化流程", "type": "required", "status": "supported", "evidence": ["主導 Juicy 上線"], "blocks_interview": false, "reason": "另有企業招募系統分階段改版。"}, {"id": "R03", "text": "具備專案管理經驗與時程風險追蹤", "type": "required", "status": "supported", "evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "blocks_interview": false, "reason": "具體涵蓋範圍、時程與切換風險。"}, {"id": "R04", "text": "有多系統整合或API串接經驗", "type": "required", "status": "supported", "evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "blocks_interview": false, "reason": "支付串接直接相關；介面與資料交換細節可面試追問。"}, {"id": "R05", "text": "熟悉PRD、功能規格與流程圖設計", "type": "required", "status": "supported", "evidence": ["以 Use Case、Wireframe 定義業務流程與畫面"], "blocks_interview": false, "reason": "文件與驗收用途具體，技能另列流程圖。"}, {"id": "R06", "text": "熟悉敏捷開發流程（Scrum）", "type": "required", "status": "partial", "evidence": ["Daily stand-up 與回顧"], "blocks_interview": false, "reason": "有儀式線索；明述Kanban搭配瀑布不能直接證明完整Scrum熟悉度，也不構成不符。"}, {"id": "R07", "text": "客戶需求訪談、問題分析及方案轉規格", "type": "required", "status": "partial", "evidence": ["依使用者旅程與工單問題排定優先級"], "blocks_interview": false, "reason": "工單分析與轉規格有證據；直接客戶會談尚無具體案例。"}, {"id": "R08", "text": "業務支援、售前會議與產品展示", "type": "required", "status": "partial", "evidence": ["與工程、設計及業務端一起推進產品"], "blocks_interview": false, "reason": "業務合作有線索；售前與展示角色待面試驗證。"}, {"id": "R09", "text": "Roadmap、需求管理與功能設計", "type": "required", "status": "supported", "evidence": ["我便將信件與即時通整合排在其他新功能之前"], "blocks_interview": false, "reason": "有優先順序理由與需求管線成果。"}, {"id": "R10", "text": "企業級ERP/HRM/SaaS/平台產品規劃", "type": "preferred", "status": "supported", "evidence": ["企業端招募系統全模組與求職端公司頁"], "blocks_interview": false, "reason": "企業招募系統與平台型產品直接可轉移。"}, {"id": "R11", "text": "資料分析能力（SQL/BI工具）", "type": "preferred", "status": "partial", "evidence": ["GA4、世代分析、對照組實驗、Excel"], "blocks_interview": false, "reason": "有分析案例；SQL與BI實際使用未呈現，不阻擋面試。"}, {"id": "R12", "text": "技術背景（API、資料庫、系統架構）", "type": "preferred", "status": "partial", "evidence": ["API 串接規劃、舊系統資料盤點"], "blocks_interview": false, "reason": "API與資料庫線索充分，架構設計深度未呈現。"}], "dimensions": [{"id": "positioning", "rating": "強", "evidence": ["企業端招募系統全模組與求職端公司頁"], "missing": [], "issue_ids": []}, {"id": "role_evidence", "rating": "足夠", "evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "missing": ["直接訪談、售前與Scrum實務待核對。"], "issue_ids": ["I01", "I02"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": [], "issue_ids": []}, {"id": "outcome_quality", "rating": "足夠", "evidence": ["為觀察差異，非因果。"], "missing": ["留存年化方法及安全事件監測範圍待核對。"], "issue_ids": ["I03"]}, {"id": "ownership", "rating": "強", "evidence": ["由我主責規劃，與工程團隊密切協作"], "missing": [], "issue_ids": []}, {"id": "readability", "rating": "足夠", "evidence": ["正式職稱產品企劃主任"], "missing": ["可將客戶訪談與售前代表案例前置。"], "issue_ids": []}], "results": [{"quote": "約 50 項大項功能上線", "kinds": ["output"]}, {"quote": "停機約 1.5 小時。", "kinds": ["output"]}, {"quote": "需求平均處理週期由 100.4 天降至 30.9 天", "kinds": ["outcome"]}, {"quote": "該群年化留存 81.2%，同期全站 74.2%", "kinds": ["outcome"]}, {"quote": "依結果全面調降售價", "kinds": ["decision"]}, {"quote": "目前專案仍在開發中", "kinds": ["in_progress"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "application_note": "系統整合與產品規劃支持面試"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "近期企業產品背景直接相關"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "application_note": "規劃與工程責任有區隔"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "流程改變具期間及基準"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "有資料與客戶風險取捨"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["從交友與訂閱制 App 到企業招募系統"], "application_note": "可見產品領域與責任演進"}, {"rule_id": "HR07", "status": "partial", "resume_evidence": ["Daily stand-up 與回顧"], "application_note": "Scrum及售前應追問案例"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["正式職稱產品企劃主任"], "application_note": "職稱與實際責任容易定位"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["依目前掌握的情況"], "application_note": "需確認事件監測與數字口徑"}, {"rule_id": "HR10", "status": "supported", "resume_evidence": ["我希望將更多心力放回產品策略"], "application_note": "方向與Roadmap責任相容"}, {"rule_id": "HR11", "status": "supported", "resume_evidence": ["台北市、新北市，可接受遠端或混合辦公"], "application_note": "未見與摘要工作條件衝突"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["主導 Juicy 上線"], "application_note": "多個案例值得面試驗證"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["廠商抱怨工單中，最大宗是溝通管道中斷"], "evidence_type": "decision", "source_ids": [], "interview_question": "請說明直接客戶訪談如何改變需求與規格。"}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM04", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依結果全面調降售價"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "partial", "resume_evidence": ["該群年化留存 81.2%，同期全站 74.2%"], "evidence_type": "outcome", "source_ids": [], "interview_question": "留存年化公式、群組定義與觀察窗口為何？"}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["與資料科學團隊合作，定義使用情境與驗收標準"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "partial", "resume_evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "evidence_type": "output", "source_ids": [], "interview_question": "請用支付案例說明API、異常處理與資料交換設計。"}, {"rule_id": "HM09", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["主導 Juicy 上線"], "evidence_type": "output", "source_ids": [], "interview_question": "請帶一份去識別規格說明需求到交付流程。"}, {"rule_id": "HM13", "primary_dimension": "", "status": "not_applicable", "resume_evidence": [], "evidence_type": null, "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HR01", "source_ids": [], "application_note": "直接訪談與售前角色待核對", "context_limit": "只讀履歷及職缺摘要", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "使用者訪談與問卷", "reason": "方法列舉未呈現直接客戶訪談年資與售前實作；影響面試驗證重點，不推定不具備。", "suggestion": "補一則親自訪談或售前會議案例，說明對象、問題與規格如何改變。"}, {"id": "I02", "rule_id": "HR07", "source_ids": [], "application_note": "Scrum實務待驗證", "context_limit": "現行流程不等於全部經驗", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "Kanban 搭配瀑布式開發", "reason": "Scrum是明文條件，現有儀式線索不夠證明熟悉程度，但不構成能力矛盾。", "suggestion": "據實說明使用Scrum的經驗或對角色、Sprint與檢視機制的掌握。"}, {"id": "I03", "rule_id": "HM05", "source_ids": [], "application_note": "量測口徑待面試確認", "context_limit": "自述未作外部查證", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "該群年化留存 81.2%，同期全站 74.2%", "reason": "已註明非因果，但年化公式與事件監測覆蓋仍不明；影響衡量可信範圍，不阻擋面試。", "suggestion": "交代留存窗口與年化公式；安全成果保留掌握範圍，說明紀錄來源。"}], "decision": {"recommendation": "interview", "evidence": ["企業端招募系統全模組與求職端公司頁", "並與 CodaPay 新加坡技術團隊協調串接", "選擇首次登入引導確認、不強迫修改"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["「企業端招募系統全模組與求職端公司頁」直接對應企業產品。", "「並與 CodaPay 新加坡技術團隊協調串接」支持整合經驗。", "「選擇首次登入引導確認、不強迫修改」呈現風險取捨。"], "key_gaps": ["直接客戶訪談年資與售前展示經驗。", "Scrum實務熟悉程度。", "留存年化口徑及安全事件觀察來源。"], "strengths": ["企業招募產品經驗與本職缺場景相關。", "規劃、驗收與跨團隊交付責任具體。", "取捨理由及成果歸因限制清楚。"], "interview_questions": ["請說明直接客戶訪談年資與一則由訪談改變規格的案例。", "請描述與業務共同售前、產品展示及方案討論的角色。", "請說明Scrum經驗與Kanban、瀑布流程的選用理由。", "支付整合中，你如何規劃API、資料交換、異常處理與驗收？", "留存年化公式、群組分母與安全事件監測來源為何？", "請分享Roadmap跨部門資源衝突及最終決策權。"], "editorial_appendix": ["可前置與客戶會議及需求訪談直接相關的代表案例。"], "spectrum": {"level": 8, "uncertainty_levels": 1, "basis": "企業產品與支付整合有多個案例，具明確取捨、衡量基準與歸因限制；訪談、售前與Scrum仍需核對。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷K｜第 1 輪｜model_id: unknown

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「企業端招募系統全模組與求職端公司頁」及支付整合案例支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 企業端招募系統全模組與求職端公司頁 | 證據足以支持面試，外部未查證。 |
| role_evidence | 足夠 | 並與 CodaPay 新加坡技術團隊協調串接 | 直接訪談、售前與Scrum實務待核對。 |
| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 證據足以支持面試，外部未查證。 |
| outcome_quality | 足夠 | 為觀察差異，非因果。 | 留存年化方法及安全事件監測範圍待核對。 |
| ownership | 強 | 由我主責規劃，與工程團隊密切協作 | 證據足以支持面試，外部未查證。 |
| readability | 足夠 | 正式職稱產品企劃主任 | 可將客戶訪談與售前代表案例前置。 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 3年以上產品規劃與需求訪談經驗 | 必要 | partial | 近 10 年 PM 經驗，經手 6 款產品 | 產品規劃年資充分；直接客戶訪談的年資與案例待釐清。 |
| 熟悉0到1或迭代優化流程 | 必要 | supported | 主導 Juicy 上線 | 另有企業招募系統分階段改版。 |
| 具備專案管理經驗與時程風險追蹤 | 必要 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 具體涵蓋範圍、時程與切換風險。 |
| 有多系統整合或API串接經驗 | 必要 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 支付串接直接相關；介面與資料交換細節可面試追問。 |
| 熟悉PRD、功能規格與流程圖設計 | 必要 | supported | 以 Use Case、Wireframe 定義業務流程與畫面 | 文件與驗收用途具體，技能另列流程圖。 |
| 熟悉敏捷開發流程（Scrum） | 必要 | partial | Daily stand-up 與回顧 | 有儀式線索；明述Kanban搭配瀑布不能直接證明完整Scrum熟悉度，也不構成不符。 |
| 客戶需求訪談、問題分析及方案轉規格 | 必要 | partial | 依使用者旅程與工單問題排定優先級 | 工單分析與轉規格有證據；直接客戶會談尚無具體案例。 |
| 業務支援、售前會議與產品展示 | 必要 | partial | 與工程、設計及業務端一起推進產品 | 業務合作有線索；售前與展示角色待面試驗證。 |
| Roadmap、需求管理與功能設計 | 必要 | supported | 我便將信件與即時通整合排在其他新功能之前 | 有優先順序理由與需求管線成果。 |
| 企業級ERP/HRM/SaaS/平台產品規劃 | 加分 | supported | 企業端招募系統全模組與求職端公司頁 | 企業招募系統與平台型產品直接可轉移。 |
| 資料分析能力（SQL/BI工具） | 加分 | partial | GA4、世代分析、對照組實驗、Excel | 有分析案例；SQL與BI實際使用未呈現，不阻擋面試。 |
| 技術背景（API、資料庫、系統架構） | 加分 | partial | API 串接規劃、舊系統資料盤點 | API與資料庫線索充分，架構設計深度未呈現。 |
工作職責列作工作需求對照；未將部分支持升格為明文資格不符。

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 系統整合與產品規劃支持面試 |
| HR02 | supported | 企業端招募系統全模組與求職端公司頁 | 近期企業產品背景直接相關 |
| HR03 | supported | 由我主責規劃，與工程團隊密切協作 | 規劃與工程責任有區隔 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 流程改變具期間及基準 |
| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 有資料與客戶風險取捨 |
| HR06 | supported | 從交友與訂閱制 App 到企業招募系統 | 可見產品領域與責任演進 |
| HR07 | partial | Daily stand-up 與回顧 | Scrum及售前應追問案例 |
| HR08 | supported | 正式職稱產品企劃主任 | 職稱與實際責任容易定位 |
| HR09 | partial | 依目前掌握的情況 | 需確認事件監測與數字口徑 |
| HR10 | supported | 我希望將更多心力放回產品策略 | 方向與Roadmap責任相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公 | 未見與摘要工作條件衝突 |
| HR12 | supported | 主導 Juicy 上線 | 多個案例值得面試驗證 |
| HM01 | supported | 企業端招募系統全模組與求職端公司頁 | 企業產品背景可轉移 |
| HM02 | supported | 廠商抱怨工單中，最大宗是溝通管道中斷 | 客戶訪談細節應追問 |
| HM03 | supported | 選擇首次登入引導確認、不強迫修改 | 可辨識風險與取捨 |
| HM04 | supported | 依結果全面調降售價 | 定價與收入模式有案例 |
| HM05 | partial | 該群年化留存 81.2%，同期全站 74.2% | 確認量測口徑，不作因果推定 |
| HM06 | supported | 與資料科學團隊合作，定義使用情境與驗收標準 | 個人與團隊責任可區別 |
| HM07 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 範圍、驗收與切換風險具體 |
| HM08 | partial | 並與 CodaPay 新加坡技術團隊協調串接 | 整合有案例，技術細節待驗證 |
| HM09 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 支持資深IC面試 |
| HM10 | supported | 由我主責規劃，與工程團隊密切協作 | 脈絡與本人動作易辨識 |
| HM11 | supported | 依客服測試回饋調整推薦規則 | 回饋有改變推薦規則 |
| HM12 | supported | 主導 Juicy 上線 | 可用去識別工作樣本追問 |
| HM13 | not_applicable | — | 方法層不對候選人加分 |
HM13：本輪依指定職缺獨立審查，未以名校、名企或人格代理能力；未經真人校準。

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「企業端招募系統全模組與求職端公司頁」直接對應企業產品。 |
| 2 | 「並與 CodaPay 新加坡技術團隊協調串接」支持整合經驗。 |
| 3 | 「選擇首次登入引導確認、不強迫修改」呈現風險取捨。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 直接客戶訪談年資與售前展示經驗。 | 請說明直接客戶訪談年資與一則由訪談改變規格的案例。 請描述與業務共同售前、產品展示及方案討論的角色。 |
| 2 | Scrum實務熟悉程度。 | 請說明Scrum經驗與Kanban、瀑布流程的選用理由。 |
| 3 | 留存年化口徑及安全事件觀察來源。 | 留存年化公式、群組分母與安全事件監測來源為何？ |
補充追問：支付整合中，你如何規劃API、資料交換、異常處理與驗收？
補充追問：請分享Roadmap跨部門資源衝突及最終決策權。

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
1. 1111背景｜「企業端招募系統全模組與求職端公司頁」｜直接呈現企業級產品情境。
2. 1111交付｜「與 QA 制定 UAT 驗收案例、排定上線計畫」｜規格到驗收可對應專案交付。
3. 改版案例｜「選擇首次登入引導確認、不強迫修改」｜解釋資料風險與使用者影響的取捨。

**可改進（3 點）**：

- 位置：專業技能
- 原句：使用者訪談與問卷
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：方法列舉未呈現直接客戶訪談年資與售前實作；影響面試驗證重點，不推定不具備。
- 建議方向：補一則親自訪談或售前會議案例，說明對象、問題與規格如何改變。

- 位置：專業技能
- 原句：Kanban 搭配瀑布式開發
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：Scrum是明文條件，現有儀式線索不夠證明熟悉程度，但不構成能力矛盾。
- 建議方向：據實說明使用Scrum的經驗或對角色、Sprint與檢視機制的掌握。

- 位置：1111留存與安全成果
- 原句：該群年化留存 81.2%，同期全站 74.2%
- 問題類型：measurement
- 嚴重度：interview_follow_up
- 影響：已註明非因果，但年化公式與事件監測覆蓋仍不明；影響衡量可信範圍，不阻擋面試。
- 建議方向：交代留存窗口與年化公式；安全成果保留掌握範圍，說明紀錄來源。

**編輯附件**（不影響判斷）：可前置與客戶會議及需求訪談直接相關的代表案例。

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠
有排優先順序與定價決策；長期資源配置權限尚待面試核對，不以團隊人數推論主管能力。

### 8. 未測試聲明
PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run
本輪只讀文字；履歷自述與內部一致不等於外部驗證。

### 成果分類補表
| 原文片段 | 分類 | 限制 |
| :-- | :-- | :-- |
| 約 50 項大項功能上線 | output | 履歷自述；依段落所列期間與口徑 |
| 停機約 1.5 小時。 | output | 履歷自述；依段落所列期間與口徑 |
| 需求平均處理週期由 100.4 天降至 30.9 天 | outcome | 履歷自述；依段落所列期間與口徑 |
| 該群年化留存 81.2%，同期全站 74.2% | outcome | 履歷自述；依段落所列期間與口徑 |
| 依結果全面調降售價 | decision | 履歷自述；依段落所列期間與口徑 |
| 目前專案仍在開發中 | in_progress | 履歷自述；依段落所列期間與口徑 |
| 全站活躍付費廠商約 6.6 萬家 | context | 系統規模，非個人創造成果 |
| 另於 2026/01–06 上線 111 項 Roadmap 細項。 | output | 與50項大項不同口徑，不相加 |
| 停機約 1.5 小時。 | output | 切換交付紀錄，非使用者改善幅度 |
| 上線後至 2026/10 未再出現同類帳號冒用。 | outcome | 依掌握情況自述，非已驗監測 |
| 完成 1,726／1,857 張需求與問題單，約 93%。 | output | 需求與問題單交付量 |
| 需求管線觸及 1,279 家活躍付費廠商 | context | 觸及母體，非留存因果 |
| AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。 | output | 功能上線不等於採用成效 |
| 依客服測試回饋調整推薦規則 | decision | 調整行為，不補成效 |
| 降價期 iOS 非續訂營收較基準期增 5% | outcome | 有平台對照；非隨機實驗 |
| 還原原價後 iOS 較基準期減 65% | outcome | 期間觀察支持決策，仍有混雜 |
| Peach 網頁付款占營收由 24% 至 80% 以上 | outcome | 營收通路占比，不是總營收成長 |
| KOOL 訂閱與付費牆規劃上線 | output | 跨平台交付 |
| 才開放精選網紅資格 | decision | 門檻設計 |
| 上線後 6 週男性 DAU 約 3,200 至 1.25 萬 | outcome | 產品與行銷整體表現 |
| 7 個市場 | context | 在地化範圍 |
| 在無直屬管理關係下分派翻譯與粉專經營任務 | output | 協作，非直屬管理 |
| 開放印尼、泰國等市場的電信帳單與超商付款 | output | 支付方式交付 |
| 提出 7／30／90 天訂閱方案與加贈內容 | output, decision | 基於實收試算提出方案 |
| Newegg.com 商品資訊英翻中與校對。 | output | 翻譯交付 |
| 我便將信件與即時通整合排在其他新功能之前 | decision, in_progress | 已作排序，整合仍開發中 |


## A-jd31-M｜履歷M

```json
{"rubric_version": "4.2", "resume_id": "M", "job_id": "jd31", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd31-M", "human_calibrated": false, "requirements": [{"id": "R01", "text": "3年以上產品規劃與需求訪談經驗", "type": "required", "status": "partial", "evidence": ["近 10 年 PM 經驗"], "blocks_interview": false, "reason": "規劃年資充分；直接客戶訪談的期間與案例待確認。"}, {"id": "R02", "text": "熟悉0到1或迭代優化流程", "type": "required", "status": "supported", "evidence": ["主導 Juicy 上線"], "blocks_interview": false, "reason": "有上線與既有系統改版案例。"}, {"id": "R03", "text": "專案管理與進度風險管理", "type": "required", "status": "supported", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "blocks_interview": false, "reason": "有驗收、時程與分階段風險處理。"}, {"id": "R04", "text": "多系統整合或API串接經驗", "type": "required", "status": "supported", "evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "blocks_interview": false, "reason": "付款第三方整合支持，技術細節面試確認。"}, {"id": "R05", "text": "PRD、功能規格與流程圖設計", "type": "required", "status": "supported", "evidence": ["整理為 PRD 與 Axure Prototype"], "blocks_interview": false, "reason": "流程與規格產物明確。"}, {"id": "R06", "text": "熟悉敏捷開發流程（Scrum）", "type": "required", "status": "partial", "evidence": ["Daily stand-up 與回顧"], "blocks_interview": false, "reason": "有相關實務線索；Kanban瀑布經驗不等於Scrum熟悉度。"}, {"id": "R07", "text": "客戶訪談、問題分析與方案轉換", "type": "required", "status": "partial", "evidence": ["使用者訪談與問卷"], "blocks_interview": false, "reason": "有問題分析與規格實績；直接訪談僅技能列示。"}, {"id": "R08", "text": "業務支援、售前會議與產品展示", "type": "required", "status": "partial", "evidence": ["工程、設計、QA、資料科學、客服、業務、法務與稽核協作"], "blocks_interview": false, "reason": "業務協作有線索，未呈現售前展示責任。"}, {"id": "R09", "text": "Roadmap與功能設計、產品迭代", "type": "required", "status": "supported", "evidence": ["依使用者旅程排優先級"], "blocks_interview": false, "reason": "以工單痛點排序並有功能規則設計。"}, {"id": "R10", "text": "企業級ERP/HRM/SaaS/平台規劃", "type": "preferred", "status": "supported", "evidence": ["企業端招募系統全模組與求職端公司頁"], "blocks_interview": false, "reason": "企業招募平台直接相關，不推定HRM全模組經驗。"}, {"id": "R11", "text": "資料分析能力（SQL/BI工具）", "type": "preferred", "status": "partial", "evidence": ["以 Google Sheet、Excel 分析"], "blocks_interview": false, "reason": "分析有案例；SQL/BI操作未呈現。"}, {"id": "R12", "text": "技術背景：API、資料庫、架構", "type": "preferred", "status": "partial", "evidence": ["API 串接規劃、舊系統資料盤點"], "blocks_interview": false, "reason": "有整合與資料協作，系統架構深度待驗證。"}], "dimensions": [{"id": "positioning", "rating": "強", "evidence": ["現任 1111 招募系統 Product Owner"], "missing": ["企業招募平台與本職相關，非完整HRM經驗。"], "issue_ids": []}, {"id": "role_evidence", "rating": "足夠", "evidence": ["整理為 PRD 與 Axure Prototype"], "missing": ["直接客戶訪談、Scrum與售前深度待追問。"], "issue_ids": ["I01", "I02", "I03"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": ["可追問替代方案及排序成功條件。"], "issue_ids": []}, {"id": "outcome_quality", "rating": "足夠", "evidence": ["為觀察差異，非因果"], "missing": ["安全事件掌握來源及處理週期母體待確認。"], "issue_ids": ["I04"]}, {"id": "ownership", "rating": "強", "evidence": ["由我擬定取數的資料表與欄位"], "missing": ["可進一步驗證整合規格與工程責任界線。"], "issue_ids": []}, {"id": "readability", "rating": "足夠", "evidence": ["兩案皆開發中"], "missing": ["輸出、觀察與進行中已有區分；可優先露出售前例證。"], "issue_ids": []}], "results": [{"quote": "約 50 項大項功能上線", "kinds": ["output"]}, {"quote": "停機約 1.5 小時", "kinds": ["outcome"]}, {"quote": "需求平均處理週期由 100.4 天降至 30.9 天", "kinds": ["outcome"]}, {"quote": "該群年化留存 81.2%，同期全站 74.2%", "kinds": ["outcome"]}, {"quote": "兩案皆開發中", "kinds": ["decision", "in_progress"]}, {"quote": "Peach 網頁付款占營收由 24% 至 80% 以上", "kinds": ["outcome"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "企業平台與規格交付對位。"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["對接 16 個需求單位"], "application_note": "近期跨單位PO情境清楚。"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "application_note": "規劃與工程交付界線可辨。"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "流程改變有比較基準，待核口徑。"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "既有客戶登入風險的取捨清楚。"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["從交友與訂閱制 App 到企業招募系統"], "application_note": "責任脈絡與領域轉換可辨。"}, {"rule_id": "HR07", "status": "partial", "resume_evidence": ["Daily stand-up 與回顧"], "application_note": "Scrum完整實務仍須追問。"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["為觀察差異，非因果"], "application_note": "資訊限制清楚利於閱讀。"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["依目前掌握的情況"], "application_note": "需核對安全事件與量測來源。"}, {"rule_id": "HR10", "status": "supported", "resume_evidence": ["接下來，我希望將更多心力放回產品策略"], "application_note": "方向與Roadmap責任相容。"}, {"rule_id": "HR11", "status": "unknown", "resume_evidence": ["台北市、新北市，可接受遠端或混合辦公"], "application_note": "JD無具體地點，未見已知衝突。"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "application_note": "已有面試價值，缺口可約談驗證。"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "evidence_type": "context", "source_ids": [], "interview_question": "如何把招募平台經驗轉用企業人資系統？"}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["查出根因是名單依履歷修改日排序"], "evidence_type": "decision", "source_ids": [], "interview_question": "請補一個直接客戶訪談改變方案的例子。"}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["改版排在新功能職缺健檢之前"], "evidence_type": "decision", "source_ids": [], "interview_question": "如何比較兩案價值與成本？"}, {"rule_id": "HM04", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "evidence_type": "decision", "source_ids": [], "interview_question": "成本試算如何改變付款方案？"}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "partial", "resume_evidence": ["為觀察差異，非因果"], "evidence_type": "outcome", "source_ids": [], "interview_question": "週期母體、年化留存算法及安全事件來源是什麼？"}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["與資料科學團隊合作，定義使用情境與驗收標準"], "evidence_type": "output", "source_ids": [], "interview_question": "規則分歧如何定案？"}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "evidence_type": "output", "source_ids": [], "interview_question": "請用改版說明里程碑與回退計畫。"}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "partial", "resume_evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "evidence_type": "output", "source_ids": [], "interview_question": "請說明付款資料流、例外與驗收責任。"}, {"rule_id": "HM09", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "evidence_type": "output", "source_ids": [], "interview_question": "哪些範圍可自主決定，哪些須向上協商？"}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["兩案皆開發中"], "evidence_type": "in_progress", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則"], "evidence_type": "decision", "source_ids": [], "interview_question": "哪個回饋推翻原先規則？"}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["整理為 PRD 與 Axure Prototype"], "evidence_type": "output", "source_ids": [], "interview_question": "可用去識別PRD與流程圖驗證規格深度嗎？"}, {"rule_id": "HM13", "primary_dimension": "method", "status": "supported", "resume_evidence": ["為觀察差異，非因果"], "evidence_type": null, "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HR01", "source_ids": [], "application_note": "直接客戶訪談證據不足", "context_limit": "僅文字自述，未外部查證。", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "使用者訪談與問卷", "reason": "JD重視直接需求訪談，技能列示未呈現受訪者、期間及轉規格過程；已有需求分析，故留面試追問。", "suggestion": "補充實際客戶訪談案例、本人動作與規格轉換。"}, {"id": "I02", "rule_id": "HR07", "source_ids": [], "application_note": "Scrum熟悉度待核對", "context_limit": "僅文字自述，未外部查證。", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "Daily stand-up 與回顧", "reason": "相關儀式不能等同完整Scrum；Kanban瀑布也不證明不熟悉，面試驗證即可。", "suggestion": "說明是否用過Sprint、角色協作與回顧改善，不虛補。"}, {"id": "I03", "rule_id": "HM06", "source_ids": [], "application_note": "售前責任未清楚", "context_limit": "僅文字自述，未外部查證。", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "工程、設計、QA、資料科學、客服、業務、法務與稽核協作", "reason": "職缺包含業務支援與展示，跨部門名單未顯示售前方案責任，需追問而非否定。", "suggestion": "若有實例，補客戶會議、展示或方案承諾邊界。"}, {"id": "I04", "rule_id": "HM05", "source_ids": [], "application_note": "成果追溯口徑待核", "context_limit": "僅文字自述，未外部查證。", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "依目前掌握的情況", "reason": "未再冒用是掌握範圍的觀察，非已驗證監測結果；週期與留存算法也需面試核對。", "suggestion": "說明事件來源、觀察範圍、週期母體與年化方法。"}], "decision": {"recommendation": "interview", "evidence": ["企業端招募系統全模組與求職端公司頁", "並與 CodaPay 新加坡技術團隊協調串接", "選擇首次登入引導確認、不強迫修改"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["企業平台與PRD、驗收及改版經驗直接相關。", "第三方付款整合具備可驗證案例。", "登入風險與痛點排序呈現具體取捨。"], "key_gaps": ["直接客戶訪談與售前方案責任。", "Scrum完整流程的熟悉度。", "成果監測與比較母體的追溯方式。"], "strengths": ["企業招募平台的交付流程完整且責任明確。", "既有資料與客戶登入風險取捨具體。", "觀察差異、團隊表現與進行中狀態標示清楚。"], "interview_questions": ["請舉直接客戶訪談轉成PRD的案例，說明期間、本人工作與需求衝突。", "曾如何支援業務展示及售前方案？如何避免承諾超過可交付範圍？", "請說明Scrum角色、Sprint規劃與回顧經驗，與現行Kanban瀑布有何不同？", "用CodaPay說明API資料流、異常處理、驗收與本人責任。", "需求處理週期的母體、計算方式與前後組合是否一致？", "年化留存如何從快照計算？未再冒用由哪些紀錄支持？", "請展示去識別的PRD與流程圖，解釋里程碑及改版回退方案。", "信件整合優先級如何決定？何時驗證使用者價值？"], "editorial_appendix": ["可將直接客戶訪談與售前案例放在相關經歷前段；無實例則不補寫。"], "spectrum": {"level": 8, "uncertainty_levels": 1, "basis": "多個相關企業平台與整合案例，具取捨、比較基準及限制；Scrum、客戶訪談及量測追溯仍需核對。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷 M｜第 1 輪｜model_id: unknown

### 1. 結論

- 招聘決定：interview

- Level：8（±1）

- 一句話理由：「企業端招募系統全模組與求職端公司頁」及整合案例支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 現任 1111 招募系統 Product Owner | 企業招募平台與本職相關，非完整HRM經驗。 |
| role_evidence | 足夠 | 整理為 PRD 與 Axure Prototype | 直接客戶訪談、Scrum與售前深度待追問。 |
| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 可追問替代方案及排序成功條件。 |
| outcome_quality | 足夠 | 為觀察差異，非因果 | 安全事件掌握來源及處理週期母體待確認。 |
| ownership | 強 | 由我擬定取數的資料表與欄位 | 可進一步驗證整合規格與工程責任界線。 |
| readability | 足夠 | 兩案皆開發中 | 輸出、觀察與進行中已有區分；可優先露出售前例證。 |
### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 3年以上產品規劃與需求訪談經驗 | 必要 | partial | 近 10 年 PM 經驗 | 規劃年資充分；直接客戶訪談的期間與案例待確認。 |
| 熟悉0到1或迭代優化流程 | 必要 | supported | 主導 Juicy 上線 | 有上線與既有系統改版案例。 |
| 專案管理與進度風險管理 | 必要 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 有驗收、時程與分階段風險處理。 |
| 多系統整合或API串接經驗 | 必要 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 付款第三方整合支持，技術細節面試確認。 |
| PRD、功能規格與流程圖設計 | 必要 | supported | 整理為 PRD 與 Axure Prototype | 流程與規格產物明確。 |
| 熟悉敏捷開發流程（Scrum） | 必要 | partial | Daily stand-up 與回顧 | 有相關實務線索；Kanban瀑布經驗不等於Scrum熟悉度。 |
| 客戶訪談、問題分析與方案轉換 | 必要 | partial | 使用者訪談與問卷 | 有問題分析與規格實績；直接訪談僅技能列示。 |
| 業務支援、售前會議與產品展示 | 必要 | partial | 工程、設計、QA、資料科學、客服、業務、法務與稽核協作 | 業務協作有線索，未呈現售前展示責任。 |
| Roadmap與功能設計、產品迭代 | 必要 | supported | 依使用者旅程排優先級 | 以工單痛點排序並有功能規則設計。 |
| 企業級ERP/HRM/SaaS/平台規劃 | 加分 | supported | 企業端招募系統全模組與求職端公司頁 | 企業招募平台直接相關，不推定HRM全模組經驗。 |
| 資料分析能力（SQL/BI工具） | 加分 | partial | 以 Google Sheet、Excel 分析 | 分析有案例；SQL/BI操作未呈現。 |
| 技術背景：API、資料庫、架構 | 加分 | partial | API 串接規劃、舊系統資料盤點 | 有整合與資料協作，系統架構深度待驗證。 |
### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 企業端招募系統全模組與求職端公司頁 | 企業平台與規格交付對位。 |
| HR02 | supported | 對接 16 個需求單位 | 近期跨單位PO情境清楚。 |
| HR03 | supported | 由我主責規劃，與工程團隊密切協作 | 規劃與工程交付界線可辨。 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 流程改變有比較基準，待核口徑。 |
| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 既有客戶登入風險的取捨清楚。 |
| HR06 | supported | 從交友與訂閱制 App 到企業招募系統 | 責任脈絡與領域轉換可辨。 |
| HR07 | partial | Daily stand-up 與回顧 | Scrum完整實務仍須追問。 |
| HR08 | supported | 為觀察差異，非因果 | 資訊限制清楚利於閱讀。 |
| HR09 | partial | 依目前掌握的情況 | 需核對安全事件與量測來源。 |
| HR10 | supported | 接下來，我希望將更多心力放回產品策略 | 方向與Roadmap責任相容。 |
| HR11 | unknown | 台北市、新北市，可接受遠端或混合辦公 | JD無具體地點，未見已知衝突。 |
| HR12 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 已有面試價值，缺口可約談驗證。 |
| HM01 | supported | 企業端招募系統全模組與求職端公司頁 | 企業平台經驗可轉移。 |
| HM02 | supported | 查出根因是名單依履歷修改日排序 | 問題理解具體，補直接訪談。 |
| HM03 | supported | 改版排在新功能職缺健檢之前 | 已有排序依據。 |
| HM04 | supported | 依抽成、稅、手續費及撥款週期做實收試算 | 具商業成本與方案連結。 |
| HM05 | partial | 為觀察差異，非因果 | 核對量測口徑與資料來源。 |
| HM06 | supported | 與資料科學團隊合作，定義使用情境與驗收標準 | 規劃與合作角色明確。 |
| HM07 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 具交付與風險管理證據。 |
| HM08 | partial | 並與 CodaPay 新加坡技術團隊協調串接 | 驗證API例外與資料流深度。 |
| HM09 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 範圍支持資深IC面試。 |
| HM10 | supported | 兩案皆開發中 | 進行中狀態清楚。 |
| HM11 | supported | 依客服測試回饋調整推薦規則 | 有回饋改變規則的線索。 |
| HM12 | supported | 整理為 PRD 與 Axure Prototype | 工作樣本可驗證規格深度。 |
| HM13 | supported | 為觀察差異，非因果 | 依JD獨立取證，未真人校準。 |
### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「企業端招募系統全模組與求職端公司頁」直接對應企業平台。 |
| 2 | 「並與 CodaPay 新加坡技術團隊協調串接」支持整合經驗。 |
| 3 | 「選擇首次登入引導確認、不強迫修改」呈現風險取捨。 |
| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 客戶訪談與售前 | 請用一次客戶會議說明需求轉規格與展示責任。 |
| 2 | Scrum熟悉度 | 如何進行Sprint規劃與回顧改善？ |
| 3 | 量測追溯 | 週期母體、留存算法與安全觀察來源為何？ |
### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111首條｜「整理為 PRD 與 Axure Prototype」｜規格、驗收與上線流程對應職缺。
- 1111改版｜「選擇首次登入引導確認、不強迫修改」｜顯示既有資料與客戶使用風險的取捨。
- 1111留存分析｜「為觀察差異，非因果」｜區分觀察與因果，利於面試核對分析品質。
**可改進（4 點）**：
- 位置：專業技能
- 原句：使用者訪談與問卷
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：JD重視直接需求訪談，技能列示未呈現受訪者、期間及轉規格過程；已有需求分析，故留面試追問。
- 建議方向：補充實際客戶訪談案例、本人動作與規格轉換。
- 位置：專業技能
- 原句：Daily stand-up 與回顧
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：相關儀式不能等同完整Scrum；Kanban瀑布也不證明不熟悉，面試驗證即可。
- 建議方向：說明是否用過Sprint、角色協作與回顧改善，不虛補。
- 位置：專業技能
- 原句：工程、設計、QA、資料科學、客服、業務、法務與稽核協作
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：職缺包含業務支援與展示，跨部門名單未顯示售前方案責任，需追問而非否定。
- 建議方向：若有實例，補客戶會議、展示或方案承諾邊界。
- 位置：1111安全與量測條列
- 原句：依目前掌握的情況
- 問題類型：measurement
- 嚴重度：interview_follow_up
- 影響：未再冒用是掌握範圍的觀察，非已驗證監測結果；週期與留存算法也需面試核對。
- 建議方向：說明事件來源、觀察範圍、週期母體與年化方法。
**編輯附件**（不影響判斷）：可將直接客戶訪談與售前案例放在相關經歷前段；無實例則不補寫。
### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠
方向與資源有優先級及定價依據；不推論預算、人員配置權或管理職能力。
### 8. 未測試聲明
PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run
本次僅單一JD、單份履歷的文字盲審。所有結果均為履歷自述，未外部查證；無必要條件的明確矛盾，未設阻擋。
### 成果分類補表
| 原句片段 | 分類 | 解讀限制 |
| :-- | :-- | :-- |
| 對接 16 個需求單位 | context | 協作範圍，不自動代表績效。 |
| 全站活躍付費廠商約 6.6 萬家 | context | 系統規模，非本人獲客成果。 |
| 團隊 3 名企劃 | context | 不推定管理能力。 |
| 另於 2026/01–06 上線 111 項 Roadmap 細項 | output | 不同粒度，不與50項相加。 |
| 盤點出上千組重複 E-mail | output/context | 資料問題規模。 |
| 選擇首次登入引導確認、不強迫修改 | decision | 保留既有客戶登入。 |
| 第一階段於 2025/10 離峰切換上線 | output | 分期交付。 |
| 十多家廠商帳號遭冒用 | context | 事件背景。 |
| 與工程協作於 2026/04/17 上線簽章驗證 | output | 不推論本人實作。 |
| 上線後至 2026/10 未再出現同類帳號冒用 | outcome | 掌握情況的觀察，非監測驗證。 |
| 完成 1,726／1,857 張需求與問題單，約 93% | output | 2026截至09/29；不等於價值。 |
| 改依職缺上線日排序、20 天內不重複推薦 | decision/output | 規則調整，未載成效。 |
| 需求管線觸及 1,279 家活躍付費廠商 | context | 選取群體非隨機。 |
| AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才 | output | 未載採用與效果。 |
| 依客服測試回饋調整推薦規則 | decision | 回饋修正。 |
| 相對變化約多 28% | outcome | 馬來西亞分期平台比較，非隨機因果。 |
| 依結果全面調降售價 | decision | 定價判斷，長期結果未載。 |
| KOOL 訂閱與付費牆規劃上線 | output | 交付非收入成果。 |
| 設定檔案完成、社群認證及照片門檻 | decision/output | 資格規則。 |
| 主導 Juicy 上線 | output | 與行銷配合。 |
| 上線後 6 週男性 DAU 約 3,200 至 1.25 萬 | outcome | 產品與行銷整體表現。 |
| 與最多約 10 位外國實習生協作 | context/output | 非直屬管理。 |
| 開放印尼、泰國等市場的電信帳單與超商付款 | output | 付款管道交付。 |
| 提出 7／30／90 天訂閱方案與加贈內容 | decision/output | 依實收試算，未載結果。 |
| Newegg.com 商品資訊英翻中與英文校對 | output | 早期工作產出。 |
| 自建 Claude Code 協作流程（12 條分支、23 個共用 skill） | output | 工具流程數量非成效。 |


## B-jd31｜揭盲：甲=M、乙=K；偏好=M

```json
{"job_id":"jd31","order":"甲=M/乙=K","differences":[{"what":"甲增加配對名單問題的根因分析與規則設計，乙以AI功能及客服回饋概述優化。","hiring_meaning":"甲可讓面試追查如何由客戶抱怨形成需求、驗證競品推論與設定規則；屬新增能力證據，並非已證明優化成效。","type":"capability"},{"what":"甲說明取數規格、DBA分工與試算工具；乙只保留快照比較結果。","hiring_meaning":"甲較清楚界定資料分析實作邊界，可追問欄位、群組與年化方法；不因此認定會SQL或BI。","type":"measurement"},{"what":"甲補明帳號冒用涉及個資風險，乙保留同一安全事件與處理成果。","hiring_meaning":"補充風險脈絡方便追問影響評估；同一事件不增加交付能力評價，兩版仍須驗證API整合深度、Scrum及售前經驗。","type":"readability"}],"preference":"甲","reason":"甲提供配對規則的問題拆解及取數分工，較能形成需求規劃與分析能力的具體追問；共同的PRD、付款串接與交付證據相同，仍需確認Scrum、客戶訪談及售前參與。","evidence_甲":["客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。","由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。","求才端可存取大量求職者個資，冒用登入即有外洩風險。"],"evidence_乙":["AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。與資料科學團隊合作，定義使用情境與驗收標準，依客服測試回饋調整推薦規則。","比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。","登入安全盤點源於 2026/04 十多家廠商帳號遭冒用。"]}
```

## 版本比較｜jd31｜順序 甲=M 乙=K｜model_id: unknown
- 偏好：甲（揭盲：M）
| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 甲增加配對名單問題的根因分析與規則設計，乙以AI功能及客服回饋概述優化。 | 甲可讓面試追查如何由客戶抱怨形成需求、驗證競品推論與設定規則；屬新增能力證據，並非已證明優化成效。 | capability | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 | AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。與資料科學團隊合作，定義使用情境與驗收標準，依客服測試回饋調整推薦規則。 |
| 2 | 甲說明取數規格、DBA分工與試算工具；乙只保留快照比較結果。 | 甲較清楚界定資料分析實作邊界，可追問欄位、群組與年化方法；不因此認定會SQL或BI。 | measurement | 由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |
| 3 | 甲補明帳號冒用涉及個資風險，乙保留同一安全事件與處理成果。 | 補充風險脈絡方便追問影響評估；同一事件不增加交付能力評價，兩版仍須驗證API整合深度、Scrum及售前經驗。 | readability | 求才端可存取大量求職者個資，冒用登入即有外洩風險。 | 登入安全盤點源於 2026/04 十多家廠商帳號遭冒用。 |
- 理由（≤120 字）：甲提供配對規則的問題拆解及取數分工，較能形成需求規劃與分析能力的具體追問；共同的PRD、付款串接與交付證據相同，仍需確認Scrum、客戶訪談及售前參與。


# jd32｜逐次輸出


## A-jd32-K｜履歷K

```json
{"rubric_version": "4.2", "resume_id": "K", "job_id": "jd32", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd32-K", "human_calibrated": false, "requirements": [{"id": "R01", "text": "3年以上經歷", "type": "required", "status": "supported", "evidence": ["近 10 年 PM 經驗"], "blocks_interview": false, "reason": "履歷時序支持所需年資。"}, {"id": "R02", "text": "內部營運網站功能設計、規格與驗收", "type": "required", "status": "supported", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "blocks_interview": false, "reason": "企業網站規格與驗收直接可轉移；內部營運範圍可於面試核對。"}, {"id": "R03", "text": "接手內部使用者及外部客戶議題並優化修正", "type": "required", "status": "supported", "evidence": ["對接 16 個需求單位"], "blocks_interview": false, "reason": "需求管線與客服問題處理有具體交付案例。"}, {"id": "R04", "text": "彙整需求、跨單位產品協作與優化提案", "type": "required", "status": "supported", "evidence": ["依使用者旅程與工單問題排定優先級"], "blocks_interview": false, "reason": "有需求彙整及跨工程、客服、資料科學協作。"}, {"id": "R05", "text": "與團隊評估方案可行性與時程", "type": "required", "status": "supported", "evidence": ["統籌影響評估、範圍與時程"], "blocks_interview": false, "reason": "安全驗證及分階段改版有實例。"}, {"id": "R06", "text": "資訊或網站開發經驗或SA經驗", "type": "required", "status": "supported", "evidence": ["釐清需求與系統分析後"], "blocks_interview": false, "reason": "網站產品與系統分析符合替代條件，不要求本人寫程式。"}, {"id": "R07", "text": "AI工具營運分析或提案", "type": "required", "status": "partial", "evidence": ["用於規格撰寫、資料整理與分析"], "blocks_interview": false, "reason": "已述AI使用目的，但未連結特定營運分析或提案決策。"}, {"id": "R08", "text": "熟悉規格撰寫及跨單位溝通", "type": "required", "status": "supported", "evidence": ["整理為 PRD 與 Axure Prototype"], "blocks_interview": false, "reason": "文件用途與QA、工程協作明確。"}, {"id": "R09", "text": "細心耐心、團隊導向", "type": "required", "status": "partial", "evidence": ["依客服測試回饋調整推薦規則"], "blocks_interview": false, "reason": "有協作行為，不由文風推定人格；以工作情境面試核對。"}], "dimensions": [{"id": "positioning", "rating": "足夠", "evidence": ["現任 1111 招募系統 Product Owner"], "missing": ["策略方向與內部系統日常工作的期待需核對"], "issue_ids": ["I03"]}, {"id": "role_evidence", "rating": "強", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "missing": ["AI分析的具體輸入、檢核及產出待問"], "issue_ids": ["I01"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": [], "issue_ids": []}, {"id": "outcome_quality", "rating": "足夠", "evidence": ["為觀察差異，非因果。"], "missing": ["需求週期口徑及安全事件監測範圍可釐清"], "issue_ids": ["I02"]}, {"id": "ownership", "rating": "強", "evidence": ["由我主責規劃，與工程團隊密切協作"], "missing": [], "issue_ids": []}, {"id": "readability", "rating": "足夠", "evidence": ["企業端招募系統全模組與求職端公司頁"], "missing": ["可將內部需求與AI工具案例提前呈現"], "issue_ids": []}], "results": [{"quote": "約 50 項大項功能上線", "kinds": ["output"]}, {"quote": "需求平均處理週期由 100.4 天降至 30.9 天", "kinds": ["outcome"]}, {"quote": "該群年化留存 81.2%，同期全站 74.2%", "kinds": ["outcome"]}, {"quote": "選擇首次登入引導確認、不強迫修改", "kinds": ["decision"]}, {"quote": "目前專案仍在開發中", "kinds": ["in_progress"]}, {"quote": "用於規格撰寫、資料整理與分析", "kinds": ["output"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["對接 16 個需求單位"], "application_note": "網站規格及需求協作直接相關"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "外部網站經驗可轉移至內部系統"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "application_note": "本人規劃與工程交付邊界可辨"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "有流程改善；面試確認口徑"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "有考慮既有使用者的取捨"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["近 10 年 PM 經驗"], "application_note": "時序呈現跨產品至系統責任"}, {"rule_id": "HR07", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "application_note": "技能連結交付情境"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "背景及代表作容易辨識"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["依目前掌握的情況"], "application_note": "需核對事件監測及成效資料"}, {"rule_id": "HR10", "status": "partial", "resume_evidence": ["我希望將更多心力放回產品策略"], "application_note": "確認內部營運職位與期待相容"}, {"rule_id": "HR11", "status": "supported", "resume_evidence": ["台北市、新北市，可接受遠端或混合辦公"], "application_note": "地點無已知衝突，待遇可電話確認"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["釐清需求與系統分析後"], "application_note": "足以約談，AI案例可於面試補問"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "evidence_type": "context", "source_ids": [], "interview_question": "說明內部使用者需求與外部廠商需求如何分流？"}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["最大宗是溝通管道中斷"], "evidence_type": "decision", "source_ids": [], "interview_question": "工單訊號如何影響優先級？"}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "evidence_type": "decision", "source_ids": [], "interview_question": "當時比較過哪些方案及風險？"}, {"rule_id": "HM04", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "partial", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "evidence_type": "outcome", "source_ids": [], "interview_question": "兩季需求類型及週期起迄點是否一致？"}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["與資料科學團隊合作，定義使用情境與驗收標準"], "evidence_type": "output", "source_ids": [], "interview_question": "如何處理跨單位需求衝突？"}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["釐清需求與系統分析後"], "evidence_type": "output", "source_ids": [], "interview_question": "請展示業務規則到驗收案例的範例。"}, {"rule_id": "HM09", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["統籌影響評估、範圍與時程"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則"], "evidence_type": "decision", "source_ids": [], "interview_question": "哪項回饋改變原規則，如何驗證？"}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["用於規格撰寫、資料整理與分析"], "evidence_type": "output", "source_ids": [], "interview_question": "AI工具分析如何形成營運建議並檢核？"}, {"rule_id": "HM13", "primary_dimension": "role_evidence", "status": "not_applicable", "resume_evidence": [], "evidence_type": null, "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HR07", "source_ids": [], "application_note": "可於面試核對，不阻擋邀約", "context_limit": "僅履歷自述，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "用於規格撰寫、資料整理與分析", "reason": "JD明列AI營運分析或提案，工具用途尚未形成可檢視的案例。", "suggestion": "補一個AI分析或提案案例，交代輸入、人工核對與採用決策。"}, {"id": "I02", "rule_id": "HM05", "source_ids": [], "application_note": "可於面試核對，不阻擋邀約", "context_limit": "僅履歷自述，未外部查證", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "需求平均處理週期由 100.4 天降至 30.9 天", "reason": "有期間及穩態說明，但需求組成、起迄定義未列，需確認改善可比性。", "suggestion": "面試說明週期定義、樣本納入規則與事件監測限制。"}, {"id": "I03", "rule_id": "HR10", "source_ids": [], "application_note": "可於面試核對，不阻擋邀約", "context_limit": "僅履歷自述，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "我希望將更多心力放回產品策略", "reason": "本職偏內部營運系統交付，需確認策略期待與日常需求修正工作的相容性。", "suggestion": "面試確認願意承擔的內部系統工作比例，不推定缺乏興趣。"}], "decision": {"recommendation": "interview", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫", "對接 16 個需求單位"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["「釐清需求與系統分析後」連結網站規格與驗收。", "「對接 16 個需求單位」支持內部需求協調。", "「選擇首次登入引導確認、不強迫修改」呈現使用者與風險取捨。"], "key_gaps": ["AI營運分析或提案的具體案例", "需求改善的口徑與監測範圍", "策略期待與內部營運工作的相容性"], "strengths": ["網站規格、驗收與上線責任清楚", "跨單位議題處理與優先級有實例", "能區分觀察差異、團隊成果與進行中工作"], "interview_questions": ["請展示一個內部需求從規格到UAT的案例。", "AI工具如何分析營運資料、檢核錯誤並形成提案？", "兩季處理週期如何定義與比較，案件組成有何差異？", "安全事件未再發生的資訊來源與涵蓋範圍是什麼？", "重複信箱方案如何評估風險與替代路徑？", "內部系統修正交付與策略工作各占多少符合期待？"], "editorial_appendix": ["可將AI工具的實際應用案例放在近期經歷；不需新增未有事實。"], "spectrum": {"level": 8, "uncertainty_levels": 1, "basis": "多個直接相關交付案例，具取捨、比較期間及限制；AI分析細節與工作期待仍待面試核對。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷K｜第 1 輪｜model_id: unknown

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「與 QA 制定 UAT 驗收案例、排定上線計畫」對應規格交付，足以約談。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 現任 1111 招募系統 Product Owner | 策略方向與內部系統日常工作的期待需核對 |
| role_evidence | 強 | 與 QA 制定 UAT 驗收案例、排定上線計畫 | AI分析的具體輸入、檢核及產出待問 |
| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 足以支持面試；以實際案例確認 |
| outcome_quality | 足夠 | 為觀察差異，非因果。 | 需求週期口徑及安全事件監測範圍可釐清 |
| ownership | 強 | 由我主責規劃，與工程團隊密切協作 | 足以支持面試；以實際案例確認 |
| readability | 足夠 | 企業端招募系統全模組與求職端公司頁 | 可將內部需求與AI工具案例提前呈現 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 3年以上經歷 | 必要 | supported | 近 10 年 PM 經驗 | 履歷時序支持所需年資。 |
| 內部營運網站功能設計、規格與驗收 | 必要 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 企業網站規格與驗收直接可轉移；內部營運範圍可於面試核對。 |
| 接手內部使用者及外部客戶議題並優化修正 | 必要 | supported | 對接 16 個需求單位 | 需求管線與客服問題處理有具體交付案例。 |
| 彙整需求、跨單位產品協作與優化提案 | 必要 | supported | 依使用者旅程與工單問題排定優先級 | 有需求彙整及跨工程、客服、資料科學協作。 |
| 與團隊評估方案可行性與時程 | 必要 | supported | 統籌影響評估、範圍與時程 | 安全驗證及分階段改版有實例。 |
| 資訊或網站開發經驗或SA經驗 | 必要 | supported | 釐清需求與系統分析後 | 網站產品與系統分析符合替代條件，不要求本人寫程式。 |
| AI工具營運分析或提案 | 必要 | partial | 用於規格撰寫、資料整理與分析 | 已述AI使用目的，但未連結特定營運分析或提案決策。 |
| 熟悉規格撰寫及跨單位溝通 | 必要 | supported | 整理為 PRD 與 Axure Prototype | 文件用途與QA、工程協作明確。 |
| 細心耐心、團隊導向 | 必要 | partial | 依客服測試回饋調整推薦規則 | 有協作行為，不由文風推定人格；以工作情境面試核對。 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 對接 16 個需求單位 | 網站規格及需求協作直接相關 |
| HR02 | supported | 企業端招募系統全模組與求職端公司頁 | 外部網站經驗可轉移至內部系統 |
| HR03 | supported | 由我主責規劃，與工程團隊密切協作 | 本人規劃與工程交付邊界可辨 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 有流程改善；面試確認口徑 |
| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 有考慮既有使用者的取捨 |
| HR06 | supported | 近 10 年 PM 經驗 | 時序呈現跨產品至系統責任 |
| HR07 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 技能連結交付情境 |
| HR08 | supported | 企業端招募系統全模組與求職端公司頁 | 背景及代表作容易辨識 |
| HR09 | partial | 依目前掌握的情況 | 需核對事件監測及成效資料 |
| HR10 | partial | 我希望將更多心力放回產品策略 | 確認內部營運職位與期待相容 |
| HR11 | supported | 台北市、新北市，可接受遠端或混合辦公 | 地點無已知衝突，待遇可電話確認 |
| HR12 | supported | 釐清需求與系統分析後 | 足以約談，AI案例可於面試補問 |
| HM01 | supported | 企業端招募系統全模組與求職端公司頁 | 情境可轉移，核對內部營運範圍 |
| HM02 | supported | 最大宗是溝通管道中斷 | 有工單訊號支持問題理解 |
| HM03 | supported | 選擇首次登入引導確認、不強迫修改 | 有資料與使用者風險取捨 |
| HM04 | supported | 依抽成、稅、手續費及撥款週期做實收試算 | 商業試算支持提案思考 |
| HM05 | partial | 需求平均處理週期由 100.4 天降至 30.9 天 | 可比性與監測口徑留面試核對 |
| HM06 | supported | 與資料科學團隊合作，定義使用情境與驗收標準 | 本人定義與合作責任明確 |
| HM07 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 具規格、驗收與分階段交付 |
| HM08 | supported | 釐清需求與系統分析後 | 系統分析案例支持技術協作 |
| HM09 | supported | 統籌影響評估、範圍與時程 | 責任範圍符合本職需求 |
| HM10 | supported | 由我主責規劃，與工程團隊密切協作 | 背景與個人動作容易辨識 |
| HM11 | supported | 依客服測試回饋調整推薦規則 | 有回饋調整，追問驗證方法 |
| HM12 | supported | 用於規格撰寫、資料整理與分析 | 交付足以約談，補問AI分析 |
| HM13 | not_applicable | — | 方法層不作候選人能力評分 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「釐清需求與系統分析後」連結網站規格與驗收。 |
| 2 | 「對接 16 個需求單位」支持內部需求協調。 |
| 3 | 「選擇首次登入引導確認、不強迫修改」呈現使用者與風險取捨。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | AI營運分析或提案的具體案例 | AI工具如何分析營運資料、檢核錯誤並形成提案？ |
| 2 | 需求改善的口徑與監測範圍 | 兩季處理週期如何定義與比較，案件組成有何差異？ |
| 3 | 策略期待與內部營運工作的相容性 | 內部系統修正交付與策略工作各占多少符合期待？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
1. 1111交付｜「與 QA 制定 UAT 驗收案例、排定上線計畫」｜直接支持本職規格與驗收。
2. 專業摘要｜「對接 16 個需求單位」｜與需求優化、跨單位協作相關。
3. 1111留存｜「為觀察差異，非因果。」｜清楚限制歸因，有助核對衡量品質。

**可改進（3 點）**：

- 位置：專業技能AI協作
- 原句：用於規格撰寫、資料整理與分析
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：JD明列AI營運分析或提案，工具用途尚未形成可檢視的案例。
- 建議方向：補一個AI分析或提案案例，交代輸入、人工核對與採用決策。

- 位置：1111需求週期
- 原句：需求平均處理週期由 100.4 天降至 30.9 天
- 問題類型：measurement
- 嚴重度：interview_follow_up
- 影響：有期間及穩態說明，但需求組成、起迄定義未列，需確認改善可比性。
- 建議方向：面試說明週期定義、樣本納入規則與事件監測限制。

- 位置：自傳職涯方向
- 原句：我希望將更多心力放回產品策略
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：本職偏內部營運系統交付，需確認策略期待與日常需求修正工作的相容性。
- 建議方向：面試確認願意承擔的內部系統工作比例，不推定缺乏興趣。

**編輯附件**（不影響判斷）：可將AI工具的實際應用案例放在近期經歷；不需新增未有事實。

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠
交付及跨單位整合證據直接；方向選擇有依據，未聲稱具有完整預算或人事權。

### 8. 未測試聲明
PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run
履歷內部敘述不等於外部查證；不從文風判斷作者。

### 成果分類補表
| 原句片段 | 分類 | 限制 |
| :-- | :-- | :-- |
| 約 50 項大項功能上線 | output | 依正文限制解讀 |
| 需求平均處理週期由 100.4 天降至 30.9 天 | outcome | 依正文限制解讀 |
| 該群年化留存 81.2%，同期全站 74.2% | outcome | 依正文限制解讀 |
| 選擇首次登入引導確認、不強迫修改 | decision | 依正文限制解讀 |
| 目前專案仍在開發中 | in_progress | 依正文限制解讀 |
| 用於規格撰寫、資料整理與分析 | output | 依正文限制解讀 |
| 全站活躍付費廠商約 6.6 萬家 | context | 系統規模，不是個人新增成果 |
| 另於 2026/01–06 上線 111 項 Roadmap 細項 | output | 不同粒度，不與50項相加 |
| 停機約 1.5 小時 | output | 切換交付資訊，不視為使用者改善 |
| 2026/04 十多家廠商帳號遭冒用 | context | 事件背景 |
| 與工程協作於 2026/04/17 上線簽章驗證 | output | 合作交付 |
| 上線後至 2026/10 未再出現同類帳號冒用 | outcome | 掌握範圍內未見，不等於全面監測 |
| 完成 1,726／1,857 張需求與問題單，約 93% | output | 處理量，非直接業務成果 |
| 需求管線觸及 1,279 家活躍付費廠商 | context | 接觸群體非新增付費 |
| AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才 | output | 功能交付非效益證明 |
| 依客服測試回饋調整推薦規則 | decision | 回饋影響規則 |
| 相對變化約多 28% | outcome | 定價實驗相對變化，仍須核對組成 |
| 依結果全面調降售價 | decision | 決策不等於全面降價後成果 |
| Peach 網頁付款占營收由 24% 至 80% 以上 | outcome | 通路占比非總營收增長 |
| KOOL 訂閱與付費牆規劃上線 | output | 未提供採用或營收增量 |
| 設定檔案完成、社群認證及照片門檻 | decision | 資格規則 |
| 主導 Juicy 上線 | output | 上線交付 |
| 男性 DAU 約 3,200 至 1.25 萬 | outcome | 與行銷導流的整體表現 |
| 與最多約 10 位外國實習生協作 | context | 非直屬管理 |
| SweetRing 在地化涵蓋 | output | 7市場在地化範圍 |
| 導入 CodaPay | output | 支付整合 |
| 提出 7／30／90 天訂閱方案與加贈內容 | decision, output | 試算提案非已驗證收入 |
| Newegg.com 商品資訊英翻中與校對。 | output | 翻譯交付 |
| 將信件與即時通整合排在其他新功能之前 | decision, in_progress | 已發生排序，尚在開發 |


## A-jd32-M｜履歷M

```json
{"rubric_version": "4.2", "resume_id": "M", "job_id": "jd32", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd32-M", "human_calibrated": false, "requirements": [{"id": "R01", "text": "3年以上經歷", "type": "required", "status": "supported", "evidence": ["近 10 年 PM 經驗"], "blocks_interview": false, "reason": "任職時序及產品規劃案例支持。"}, {"id": "R02", "text": "內部營運網站功能設計、規格撰寫與驗收", "type": "required", "status": "supported", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "blocks_interview": false, "reason": "企業系統與內部需求協作可轉移，內部營運網站範圍可面試核對。"}, {"id": "R03", "text": "處理內部使用者與外部客戶議題並優化或修正", "type": "required", "status": "supported", "evidence": ["每週發布處理週報"], "blocks_interview": false, "reason": "工單處理及客服配對名單案例具體。"}, {"id": "R04", "text": "彙整內部需求、跨單位產品協作及優化提案", "type": "required", "status": "supported", "evidence": ["對接 16 個需求單位"], "blocks_interview": false, "reason": "有需求整合、旅程排序與規則優化案例。"}, {"id": "R05", "text": "與團隊評估可行性及時程", "type": "required", "status": "supported", "evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "blocks_interview": false, "reason": "登入安全及分階段改版支持。"}, {"id": "R06", "text": "資訊或網站開發經驗或SA經驗", "type": "required", "status": "supported", "evidence": ["釐清需求與系統分析後"], "blocks_interview": false, "reason": "SA及業務流程拆解支持；不推論親自開發。"}, {"id": "R07", "text": "運用AI工具進行營運分析或提案", "type": "required", "status": "partial", "evidence": ["用於規格撰寫、資料整理與分析"], "blocks_interview": false, "reason": "工具用途有自述，缺單一營運分析或提案的輸入、判讀與採用案例。"}, {"id": "R08", "text": "熟悉規格撰寫與跨單位溝通", "type": "required", "status": "supported", "evidence": ["整理為 PRD 與 Axure Prototype"], "blocks_interview": false, "reason": "具規格、QA驗收、工程及客服協作。"}, {"id": "R09", "text": "細心耐心、團隊導向", "type": "required", "status": "partial", "evidence": ["選擇首次登入引導確認、不強迫修改"], "blocks_interview": false, "reason": "資料風險與協作行為有線索，不從履歷判定人格。"}], "dimensions": [{"id": "positioning", "rating": "足夠", "evidence": ["現任 1111 招募系統 Product Owner"], "missing": ["策略方向與內部營運系統日常工作的期待可釐清。"], "issue_ids": ["I03"]}, {"id": "role_evidence", "rating": "強", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "missing": ["AI營運分析實際案例待核對。"], "issue_ids": ["I01"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": [], "issue_ids": []}, {"id": "outcome_quality", "rating": "足夠", "evidence": ["為觀察差異，非因果"], "missing": ["週期統計口徑與安全事件觀察來源可補。"], "issue_ids": ["I02"]}, {"id": "ownership", "rating": "強", "evidence": ["由我擬定取數的資料表與欄位"], "missing": ["可面試細問跨產品團隊分歧處理。"], "issue_ids": []}, {"id": "readability", "rating": "足夠", "evidence": ["企業端招募系統全模組與求職端公司頁"], "missing": ["可優先呈現內部營運及AI分析案例。"], "issue_ids": []}], "results": [{"quote": "約 50 項大項功能上線", "kinds": ["output"]}, {"quote": "第一階段於 2025/10 離峰切換上線", "kinds": ["output"]}, {"quote": "上線後至 2026/10 未再出現同類帳號冒用", "kinds": ["outcome"]}, {"quote": "需求平均處理週期由 100.4 天降至 30.9 天", "kinds": ["outcome"]}, {"quote": "兩案皆開發中", "kinds": ["in_progress"]}, {"quote": "該群年化留存 81.2%，同期全站 74.2%", "kinds": ["outcome"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "application_note": "規格、驗收與系統經驗直接相關"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "近期系統場景及內外部對象清楚"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我擬定取數的資料表與欄位"], "application_note": "規劃與DBA執行邊界明確"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "有流程結果，核對統計口徑"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "以登入風險說明取捨"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["近 10 年 PM 經驗"], "application_note": "時序與領域轉換可辨識"}, {"rule_id": "HR07", "status": "supported", "resume_evidence": ["與資料科學團隊合作，定義使用情境與驗收標準"], "application_note": "跨職能合作有實際情境"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["現任 1111 招募系統 Product Owner"], "application_note": "摘要可快速定位"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["依目前掌握的情況"], "application_note": "安全結果須追問觀察來源"}, {"rule_id": "HR10", "status": "partial", "resume_evidence": ["接下來，我希望將更多心力放回產品策略"], "application_note": "釐清營運系統職務期待"}, {"rule_id": "HR11", "status": "unknown", "resume_evidence": ["台北市、新北市，可接受遠端或混合辦公"], "application_note": "搬遷與薪資接受度可電話核對"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["釐清需求與系統分析後"], "application_note": "足以面試；缺口可用案例確認"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["客服反映配對名單「少又舊」"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM04", "primary_dimension": "role_evidence", "status": "not_applicable", "resume_evidence": [], "evidence_type": null, "source_ids": [], "interview_question": null}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "partial", "resume_evidence": ["為觀察差異，非因果"], "evidence_type": "outcome", "source_ids": [], "interview_question": "處理週期的起訖、母體與排除規則是什麼？"}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["改依職缺上線日排序、20 天內不重複推薦"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM09", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["現任 1111 招募系統 Product Owner"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["用於規格撰寫、資料整理與分析"], "evidence_type": "output", "source_ids": [], "interview_question": "請展示AI營運分析或提案案例及人工查核方式。"}, {"rule_id": "HM13", "primary_dimension": "", "status": "not_applicable", "resume_evidence": [], "evidence_type": null, "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HR07", "source_ids": [], "application_note": "追問AI實際工作樣本", "context_limit": "僅依履歷文字，未外部查證。", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "用於規格撰寫、資料整理與分析", "reason": "AI工具用途有線索，但未連結一個營運分析或提案決策；可面試補證。", "suggestion": "補一個可匿名化的輸入、人工驗證與採用結果案例。"}, {"id": "I02", "rule_id": "HM05", "source_ids": [], "application_note": "核對流程指標與安全觀察", "context_limit": "僅依履歷文字，未外部查證。", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "需求平均處理週期由 100.4 天降至 30.9 天", "reason": "有期間及穩態說明，仍缺母體與起訖；安全未再發生也屬掌握範圍，面試查核，不視為矛盾。", "suggestion": "說明處理週期的納入規則、起訖及安全觀察資料來源。"}, {"id": "I03", "rule_id": "HR10", "source_ids": [], "application_note": "確認職務內容期待", "context_limit": "僅依履歷文字，未外部查證。", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "接下來，我希望將更多心力放回產品策略", "reason": "策略方向可能相容，但內部營運系統改善比例與本人期待尚未知，不阻擋面試。", "suggestion": "面試確認對內部需求、維運修正與功能規劃工作的期待。"}], "decision": {"recommendation": "interview", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫", "選擇首次登入引導確認、不強迫修改"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["「與 QA 制定 UAT 驗收案例、排定上線計畫」支持規格到交付。", "「對接 16 個需求單位」且有工單排序案例。", "「選擇首次登入引導確認、不強迫修改」呈現風險取捨。"], "key_gaps": ["AI營運分析或提案工作樣本。", "週期計算與安全觀察資料來源。", "內部營運系統工作內容的職涯期待。"], "strengths": ["規格與交付｜「與 QA 制定 UAT 驗收案例、排定上線計畫」｜符合內部系統驗收交付需求。", "決策｜「選擇首次登入引導確認、不強迫修改」｜展示既有使用者風險與實際取捨。", "協作｜「由我擬定取數的資料表與欄位」｜交代本人分析規劃與DBA合作邊界。"], "interview_questions": ["請展示AI營運分析或提案案例及人工查核方式。", "需求平均處理週期如何定義起訖、母體及排除規則？", "未再出現同類帳號冒用的觀察來源及涵蓋範圍是什麼？", "跨單位需求衝突時如何與產品團隊決定範圍和時程？", "內部營運改善與產品策略的工作比例，何種安排符合期待？", "如何確認配對規則修改確實改善名單少又舊的問題？"], "editorial_appendix": ["可將AI分析實例與內部需求改善放在較前位置；不影響能力評定。"], "spectrum": {"level": 8, "uncertainty_levels": 1, "basis": "多個系統分析、規格及交付案例對應JD；有清楚取捨、可比較流程指標與觀察限制。AI應用仍待實例核對。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷｜第 1 輪｜model_id: unknown

### 1. 結論

- 招聘決定：interview

- Level：8（±1）

- 一句話理由：「與 QA 制定 UAT 驗收案例、排定上線計畫」及系統取捨案例足以支持面試。

### 2. 六維度

| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 現任 1111 招募系統 Product Owner | 策略方向與內部營運系統日常工作的期待可釐清。 |
| role_evidence | 強 | 與 QA 制定 UAT 驗收案例、排定上線計畫 | AI營運分析實際案例待核對。 |
| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 證據足以支持面試，細節可用工作樣本確認。 |
| outcome_quality | 足夠 | 為觀察差異，非因果 | 週期統計口徑與安全事件觀察來源可補。 |
| ownership | 強 | 由我擬定取數的資料表與欄位 | 可面試細問跨產品團隊分歧處理。 |
| readability | 足夠 | 企業端招募系統全模組與求職端公司頁 | 可優先呈現內部營運及AI分析案例。 |
### 3. JD 條件對照
本摘要將希望具備條件納入職務期待；部分支持不等同明文不符合。
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 3年以上經歷 | 必要／職務期待 | supported | 近 10 年 PM 經驗 | 任職時序及產品規劃案例支持。 |
| 內部營運網站功能設計、規格撰寫與驗收 | 必要／職務期待 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 企業系統與內部需求協作可轉移，內部營運網站範圍可面試核對。 |
| 處理內部使用者與外部客戶議題並優化或修正 | 必要／職務期待 | supported | 每週發布處理週報 | 工單處理及客服配對名單案例具體。 |
| 彙整內部需求、跨單位產品協作及優化提案 | 必要／職務期待 | supported | 對接 16 個需求單位 | 有需求整合、旅程排序與規則優化案例。 |
| 與團隊評估可行性及時程 | 必要／職務期待 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 登入安全及分階段改版支持。 |
| 資訊或網站開發經驗或SA經驗 | 必要／職務期待 | supported | 釐清需求與系統分析後 | SA及業務流程拆解支持；不推論親自開發。 |
| 運用AI工具進行營運分析或提案 | 必要／職務期待 | partial | 用於規格撰寫、資料整理與分析 | 工具用途有自述，缺單一營運分析或提案的輸入、判讀與採用案例。 |
| 熟悉規格撰寫與跨單位溝通 | 必要／職務期待 | supported | 整理為 PRD 與 Axure Prototype | 具規格、QA驗收、工程及客服協作。 |
| 細心耐心、團隊導向 | 必要／職務期待 | partial | 選擇首次登入引導確認、不強迫修改 | 資料風險與協作行為有線索，不從履歷判定人格。 |
### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 規格、驗收與系統經驗直接相關 |
| HR02 | supported | 企業端招募系統全模組與求職端公司頁 | 近期系統場景及內外部對象清楚 |
| HR03 | supported | 由我擬定取數的資料表與欄位 | 規劃與DBA執行邊界明確 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 有流程結果，核對統計口徑 |
| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 以登入風險說明取捨 |
| HR06 | supported | 近 10 年 PM 經驗 | 時序與領域轉換可辨識 |
| HR07 | supported | 與資料科學團隊合作，定義使用情境與驗收標準 | 跨職能合作有實際情境 |
| HR08 | supported | 現任 1111 招募系統 Product Owner | 摘要可快速定位 |
| HR09 | partial | 依目前掌握的情況 | 安全結果須追問觀察來源 |
| HR10 | partial | 接下來，我希望將更多心力放回產品策略 | 釐清營運系統職務期待 |
| HR11 | unknown | 台北市、新北市，可接受遠端或混合辦公 | 搬遷與薪資接受度可電話核對 |
| HR12 | supported | 釐清需求與系統分析後 | 足以面試；缺口可用案例確認 |
| HM01 | supported | 企業端招募系統全模組與求職端公司頁 | 企業流程經驗可轉移 |
| HM02 | supported | 客服反映配對名單「少又舊」 | 客服訊號連到問題根因 |
| HM03 | supported | 選擇首次登入引導確認、不強迫修改 | 取捨及使用者風險清楚 |
| HM04 | not_applicable | — | JD未要求商業策略或損益責任 |
| HM05 | partial | 為觀察差異，非因果 | 有衡量限制，仍須核對口徑 |
| HM06 | supported | 由我主責規劃，與工程團隊密切協作 | 本人規劃及工程合作清楚 |
| HM07 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 規格至驗收與交付具體 |
| HM08 | supported | 改依職缺上線日排序、20 天內不重複推薦 | 可拆解系統業務規則 |
| HM09 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 責任範圍符合專案協作職務 |
| HM10 | supported | 現任 1111 招募系統 Product Owner | 近期工作及代表案例容易辨識 |
| HM11 | supported | 依客服測試回饋調整推薦規則 | 有依回饋修正行為 |
| HM12 | supported | 用於規格撰寫、資料整理與分析 | 值得約談並驗證AI實際應用 |
| HM13 | not_applicable | — | 方法檢查不作候選人能力加分 |
HM13 方法說明：獨立依本JD判讀；未使用其他履歷或結果，無真人校準。
### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「與 QA 制定 UAT 驗收案例、排定上線計畫」支持規格到交付。 |
| 2 | 「對接 16 個需求單位」且有工單排序案例。 |
| 3 | 「選擇首次登入引導確認、不強迫修改」呈現風險取捨。 |
| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | AI營運分析或提案工作樣本。 | 請展示AI營運分析或提案案例及人工查核方式。 |
| 2 | 週期計算與安全觀察資料來源。 | 需求平均處理週期如何定義起訖、母體及排除規則？ 未再出現同類帳號冒用的觀察來源及涵蓋範圍是什麼？ |
| 3 | 內部營運系統工作內容的職涯期待。 | 內部營運改善與產品策略的工作比例，何種安排符合期待？ |
補充追問：跨單位需求衝突時如何與產品團隊決定範圍和時程？ 如何確認配對規則修改確實改善名單少又舊的問題？
### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 規格與交付｜「與 QA 制定 UAT 驗收案例、排定上線計畫」｜符合內部系統驗收交付需求。
- 決策｜「選擇首次登入引導確認、不強迫修改」｜展示既有使用者風險與實際取捨。
- 協作｜「由我擬定取數的資料表與欄位」｜交代本人分析規劃與DBA合作邊界。
**可改進（3 點）**：
- 位置：專業技能／AI協作
  - 原句：用於規格撰寫、資料整理與分析
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：AI工具用途有線索，但未連結一個營運分析或提案決策；可面試補證。
  - 建議方向：補一個可匿名化的輸入、人工驗證與採用結果案例。
- 位置：1111需求處理週期與安全盤點
  - 原句：需求平均處理週期由 100.4 天降至 30.9 天
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：有期間及穩態說明，仍缺母體與起訖；安全未再發生也屬掌握範圍，面試查核，不視為矛盾。
  - 建議方向：說明處理週期的納入規則、起訖及安全觀察資料來源。
- 位置：自傳末段
  - 原句：接下來，我希望將更多心力放回產品策略
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：策略方向可能相容，但內部營運系統改善比例與本人期待尚未知，不阻擋面試。
  - 建議方向：面試確認對內部需求、維運修正與功能規劃工作的期待。
**編輯附件**（不影響判斷）：可將AI分析實例與內部需求改善放在較前位置；不影響能力評定。
### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠
方向取捨有具體案例；不推論預算或人員管理責任。
### 8. 未測試聲明
PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run
### 成果分類補表
數字為履歷自述；分類不代表外部查證。重複摘要不重算。
| 原句或原句片段 | 分類 | 解讀限制 |
| :-- | :-- | :-- |
| 約 50 項大項功能上線 | output | 履歷自述，未外部查證。 |
| 第一階段於 2025/10 離峰切換上線 | output | 履歷自述，未外部查證。 |
| 上線後至 2026/10 未再出現同類帳號冒用 | outcome | 目前掌握情況，不等於完整監測紀錄。 |
| 需求平均處理週期由 100.4 天降至 30.9 天 | outcome | 履歷自述，未外部查證。 |
| 兩案皆開發中 | in_progress | 僅支持已發生的排序決策，不算已實現結果。 |
| 該群年化留存 81.2%，同期全站 74.2% | outcome | 觀察差異，非因果。 |
| 全站活躍付費廠商約 6.6 萬家 | context | 履歷自述，未外部查證。 |
| 團隊 3 名企劃 | context | 履歷自述，未外部查證。 |
| 上線 111 項 Roadmap 細項 | output | 履歷自述，未外部查證。 |
| 盤點出上千組重複 E-mail | output／context | 履歷自述，未外部查證。 |
| 停機約 1.5 小時 | output | 履歷自述，未外部查證。 |
| 2026/04 十多家廠商帳號遭冒用 | context | 履歷自述，未外部查證。 |
| 於 2026/04/17 上線簽章驗證 | output | 履歷自述，未外部查證。 |
| 完成 1,726／1,857 張需求與問題單，約 93% | output | 履歷自述，未外部查證。 |
| 改依職缺上線日排序、20 天內不重複推薦 | decision／output | 履歷自述，未外部查證。 |
| 需求管線觸及 1,279 家活躍付費廠商 | context | 履歷自述，未外部查證。 |
| 約占全站 66,150 家的 1.9% | context | 履歷自述，未外部查證。 |
| AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才 | output | 履歷自述，未外部查證。 |
| 依客服測試回饋調整推薦規則 | decision | 履歷自述，未外部查證。 |
| 降價期 iOS 非續訂營收較基準期增 5% | outcome | 履歷自述，未外部查證。 |
| Android 減 18%，相對變化約多 28% | outcome | 履歷自述，未外部查證。 |
| 還原原價後 iOS 較基準期減 65% | outcome | 履歷自述，未外部查證。 |
| 依結果全面調降售價 | decision | 履歷自述，未外部查證。 |
| Peach 網頁付款占營收由 24% 至 80% 以上 | outcome | 收入渠道占比，不等於總營收增長。 |
| KOOL 訂閱與付費牆規劃上線 | output | 履歷自述，未外部查證。 |
| 設定檔案完成、社群認證及照片門檻 | decision | 履歷自述，未外部查證。 |
| 主導 Juicy 上線 | output | 履歷自述，未外部查證。 |
| 上線後 6 週男性 DAU 約 3,200 至 1.25 萬 | outcome | 產品上線與行銷導流的整體表現。 |
| 7 個市場 | context | 履歷自述，未外部查證。 |
| 與最多約 10 位外國實習生協作 | context | 履歷自述，未外部查證。 |
| 導入 CodaPay | output | 履歷自述，未外部查證。 |
| 提出 7／30／90 天訂閱方案與加贈內容 | output／decision | 履歷自述，未外部查證。 |
| Newegg.com 商品資訊英翻中與英文校對 | output | 履歷自述，未外部查證。 |
| 12 條分支、23 個共用 skill | output | 履歷自述，未外部查證。 |
| 近 10 年 PM 經驗，經手 6 款產品 | context | 履歷自述，未外部查證。 |


## B-jd32｜揭盲：甲=K、乙=M；偏好=M

```json
{"job_id":"jd32","order":"甲=K/乙=M","differences":[{"what":"乙補充客服問題的根因與推薦規則設計；甲僅概述依回饋調整。","hiring_meaning":"更能針對問題分析、規格取捨及規則驗收追問，貼合內部系統議題處理；仍需驗證改善成效。","type":"capability"},{"what":"乙交代留存分析中本人、DBA與試算表的分工，兩版結果與非因果限制相同。","hiring_meaning":"更易驗證取數規格與分析責任；不把相同留存差異升格為乙的成果優勢。","type":"measurement"},{"what":"乙新增搜尋改版優先於新功能的案例；信件與即時通案例兩版皆有。","hiring_meaning":"增加可追問的需求排序取捨，適合驗證跨單位優化提案；兩案開發中，不能視為交付成效。","type":"capability"}],"preference":"乙","reason":"乙補充配對問題的根因與規則、分析取數分工及搜尋改版取捨，讓主管更明確驗證問題處理與需求排序。共同規格、驗收及AI協作經驗不重複加分，新增數字本身不構成優勢。","evidence_甲":["AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。與資料科學團隊合作，定義使用情境與驗收標準，依客服測試回饋調整推薦規則。","比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。","例如廠商抱怨工單中，最大宗是溝通管道中斷，我便將信件與即時通整合排在其他新功能之前，目前專案仍在開發中。"],"evidence_乙":["客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。","由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。","依使用者旅程排優先級：廠商抱怨工單最大宗是溝通管道中斷，信件與即時通整合排在其他新功能之前；搜尋結果頁的現有功能卡在痛點上，改版排在新功能職缺健檢之前（兩案皆開發中）。"]}
```

## 版本比較｜jd32｜順序 甲=K 乙=M｜model_id: unknown
- 偏好：乙（揭盲：M）
| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 乙補充客服問題的根因與推薦規則設計；甲僅概述依回饋調整。 | 更能針對問題分析、規格取捨及規則驗收追問，貼合內部系統議題處理；仍需驗證改善成效。 | capability | AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。與資料科學團隊合作，定義使用情境與驗收標準，依客服測試回饋調整推薦規則。 | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 |
| 2 | 乙交代留存分析中本人、DBA與試算表的分工，兩版結果與非因果限制相同。 | 更易驗證取數規格與分析責任；不把相同留存差異升格為乙的成果優勢。 | measurement | 比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |
| 3 | 乙新增搜尋改版優先於新功能的案例；信件與即時通案例兩版皆有。 | 增加可追問的需求排序取捨，適合驗證跨單位優化提案；兩案開發中，不能視為交付成效。 | capability | 例如廠商抱怨工單中，最大宗是溝通管道中斷，我便將信件與即時通整合排在其他新功能之前，目前專案仍在開發中。 | 依使用者旅程排優先級：廠商抱怨工單最大宗是溝通管道中斷，信件與即時通整合排在其他新功能之前；搜尋結果頁的現有功能卡在痛點上，改版排在新功能職缺健檢之前（兩案皆開發中）。 |
- 理由（≤120 字）：乙補充配對問題的根因與規則、分析取數分工及搜尋改版取捨，讓主管更明確驗證問題處理與需求排序。共同規格、驗收及AI協作經驗不重複加分，新增數字本身不構成優勢。


# jd34｜逐次輸出


## A-jd34-K｜履歷K

```json
{"rubric_version": "4.2", "resume_id": "K", "job_id": "jd34", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd34-K", "human_calibrated": false, "requirements": [{"id": "R01", "text": "經歷5年以上；產品管理2年以上", "type": "required", "status": "supported", "evidence": ["近 10 年 PM 經驗"], "blocks_interview": false, "reason": "工作時序支持兩項年資門檻"}, {"id": "R02", "text": "完整產品循環，與UX、RD、QA合作交付上市", "type": "required", "status": "supported", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "blocks_interview": false, "reason": "具規格、原型、工程協作及驗收上線案例"}, {"id": "R03", "text": "理解商業模式、利害關係人需求及具體規格", "type": "required", "status": "supported", "evidence": ["對接 16 個需求單位"], "blocks_interview": false, "reason": "訂閱定價、實收試算及需求轉PRD直接相關"}, {"id": "R04", "text": "定義目標及衡量標準，分析效益", "type": "required", "status": "supported", "evidence": ["定義使用情境與驗收標準"], "blocks_interview": false, "reason": "具實驗對照與留存觀察，成效歸因仍需追問"}, {"id": "R05", "text": "維運需求及產品指標、工作效率優化", "type": "required", "status": "supported", "evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "blocks_interview": false, "reason": "工單、週報與安全修復具體"}, {"id": "R06", "text": "金流、物流、會員、促購、優惠券、購買流程、訂單功能經驗", "type": "required", "status": "partial", "evidence": ["規劃由 App 內購轉向網頁付款"], "blocks_interview": false, "reason": "支付、訂閱、資格門檻可轉移；物流、優惠券、訂單未呈現"}, {"id": "R07", "text": "產品設計、RD合作與製作使用者介面", "type": "required", "status": "supported", "evidence": ["以 Use Case、Wireframe 定義業務流程與畫面"], "blocks_interview": false, "reason": "介面原型與工程交付有案例"}, {"id": "R08", "text": "參與和運作Scrum團隊", "type": "required", "status": "partial", "evidence": ["Kanban 搭配瀑布式開發"], "blocks_interview": false, "reason": "有站會回顧線索；未證實Scrum實際運作，不等於不會"}, {"id": "R09", "text": "從0到1產品開發", "type": "preferred", "status": "partial", "evidence": ["主導 Juicy 上線"], "blocks_interview": false, "reason": "有上市證據，從探索至首次推出的完整邊界待問"}, {"id": "R10", "text": "熟悉支付產業生態及趨勢", "type": "preferred", "status": "partial", "evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "blocks_interview": false, "reason": "支付實務直接相關；近期生態趨勢未呈現"}, {"id": "R11", "text": "簡報募資、提案；200人以上軟體團隊工作2年以上", "type": "preferred", "status": "unknown", "evidence": [], "blocks_interview": false, "reason": "兩項加分均未明示，不以公司名或企劃人數推論"}, {"id": "R12", "text": "Gen AI加入產品具體案例", "type": "preferred", "status": "supported", "evidence": ["AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。"], "blocks_interview": false, "reason": "文字生成情境及資料科學協作支持；不將個人工具當產品案例"}], "dimensions": [{"id": "positioning", "rating": "強", "evidence": ["訂閱制 B2C App 與雙邊媒合平台。"], "missing": ["零售全通路領域需到職銜接"], "issue_ids": ["I01"]}, {"id": "role_evidence", "rating": "足夠", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "missing": ["商務模組廣度及Scrum運作需面試釐清"], "issue_ids": ["I01", "I02"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": ["可追問替代方案與成功標準"], "issue_ids": []}, {"id": "outcome_quality", "rating": "足夠", "evidence": ["為觀察差異，非因果。"], "missing": ["留存年化、營收占比與安全觀察的量測限制"], "issue_ids": ["I03", "I04", "I05"]}, {"id": "ownership", "rating": "強", "evidence": ["由我主責規劃，與工程團隊密切協作"], "missing": ["產品方向與資源配置的最終決策權待確認"], "issue_ids": []}, {"id": "readability", "rating": "足夠", "evidence": ["近 10 年 PM 經驗，經手 6 款產品"], "missing": ["可將支付與AI產品案例前移；不影響面試"], "issue_ids": []}], "results": [{"quote": "約 50 項大項功能上線", "kinds": ["output"]}, {"quote": "需求平均處理週期由 100.4 天降至 30.9 天", "kinds": ["outcome"]}, {"quote": "該群年化留存 81.2%，同期全站 74.2%", "kinds": ["outcome"]}, {"quote": "選擇首次登入引導確認、不強迫修改", "kinds": ["decision"]}, {"quote": "Peach 網頁付款占營收由 24% 至 80% 以上", "kinds": ["outcome"]}, {"quote": "目前專案仍在開發中", "kinds": ["in_progress"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["規劃由 App 內購轉向網頁付款"], "application_note": "支付與PO交付直接相關"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "企業流程可轉移至SaaS"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "application_note": "個人規劃與工程邊界清楚"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "效率改變可追問口徑"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "有既有客戶風險取捨"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["從交友與訂閱制 App 到企業招募系統"], "application_note": "領域與責任變化清楚"}, {"rule_id": "HR07", "status": "supported", "resume_evidence": ["與資料科學團隊合作"], "application_note": "協作有產品應用案例"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["資深產品經理｜Senior Product Manager"], "application_note": "結構能定位近期責任"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["上線後至 2026/10 未再出現同類帳號冒用"], "application_note": "需核對通報涵蓋與觀察口徑"}, {"rule_id": "HR10", "status": "supported", "resume_evidence": ["我希望將更多心力放回產品策略"], "application_note": "方向與產品價值判斷相容"}, {"rule_id": "HR11", "status": "unknown", "resume_evidence": ["台北市、新北市，可接受遠端或混合辦公"], "application_note": "JD未列完整條件，無已知衝突"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "application_note": "交付與商業案例足以約談"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["訂閱制 B2C App 與雙邊媒合平台。"], "evidence_type": "context", "source_ids": [], "interview_question": "如何將訂閱與企業流程經驗轉到零售全通路？"}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["最大宗是溝通管道中斷"], "evidence_type": "decision", "source_ids": [], "interview_question": "工單問題如何排序，還考慮哪些使用者訊號？"}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "evidence_type": "decision", "source_ids": [], "interview_question": "登入改版還評估哪些方案？"}, {"rule_id": "HM04", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "evidence_type": "decision", "source_ids": [], "interview_question": "付款成本及風險如何影響方案選擇？"}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "partial", "resume_evidence": ["為觀察差異，非因果。"], "evidence_type": "outcome", "source_ids": [], "interview_question": "年化留存如何計算？樣本有何選擇偏差？"}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "evidence_type": "output", "source_ids": [], "interview_question": "產品排序與工程時程分歧如何解決？"}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "evidence_type": "output", "source_ids": [], "interview_question": "驗收、回滾和既有客戶風險如何處理？"}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["並與 CodaPay 新加坡技術團隊協調串接。"], "evidence_type": "output", "source_ids": [], "interview_question": "串接限制及失敗付款如何拆成規格與驗收？"}, {"rule_id": "HM09", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "evidence_type": "output", "source_ids": [], "interview_question": "哪些方向與資源決定需要副總核定？"}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["近 10 年 PM 經驗，經手 6 款產品"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則。"], "evidence_type": "decision", "source_ids": [], "interview_question": "測試回饋改變了哪些規則？"}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["規劃由 App 內購轉向網頁付款"], "evidence_type": "output", "source_ids": [], "interview_question": "用一個付款案例展示規格、驗收與效益。"}, {"rule_id": "HM13", "primary_dimension": "", "status": "not_applicable", "resume_evidence": [], "evidence_type": null, "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HR01", "source_ids": [], "application_note": "付款與訂閱經驗可轉移", "context_limit": "僅依履歷文字與本職缺摘要，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "規劃由 App 內購轉向網頁付款", "reason": "物流、優惠券及訂單等零售流程未呈現；影響上手範圍而非證實不符", "suggestion": "面試用購買流程拆解確認能力與待學範圍"}, {"id": "I02", "rule_id": "HR07", "source_ids": [], "application_note": "不把非Scrum經驗當矛盾", "context_limit": "僅依履歷文字與本職缺摘要，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "Kanban 搭配瀑布式開發", "reason": "站會與回顧不能單獨證實運作Scrum；需確認PO角色適配", "suggestion": "追問Sprint、Backlog及Review實作，沒有就誠實說明"}, {"id": "I03", "rule_id": "HM05", "source_ids": [], "application_note": "觀察差異非因果", "context_limit": "僅依履歷文字與本職缺摘要，未外部查證", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "該群年化留存 81.2%，同期全站 74.2%", "reason": "短期快照年化公式與群組選擇影響可比性；面試核對", "suggestion": "補年化公式、觀察窗及樣本納入規則"}, {"id": "I04", "rule_id": "HR09", "source_ids": [], "application_note": "履歷未聲稱監測查證", "context_limit": "僅依履歷文字與本職缺摘要，未外部查證", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "上線後至 2026/10 未再出現同類帳號冒用", "reason": "目前掌握的情況不等同全面監測；需問來源及漏報限制", "suggestion": "維持觀察措辭，說明客服通報或其他紀錄範圍"}, {"id": "I05", "rule_id": "HM05", "source_ids": [], "application_note": "占比不是總收入增長", "context_limit": "僅依履歷文字與本職缺摘要，未外部查證", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "Peach 網頁付款占營收由 24% 至 80% 以上", "reason": "通路占比無法獨立證明淨收益或付款轉換提升；面試核對", "suggestion": "補可公開的淨收入或轉換口徑，無資料不補數字"}], "decision": {"recommendation": "interview", "evidence": ["規劃由 App 內購轉向網頁付款", "與 QA 制定 UAT 驗收案例、排定上線計畫", "選擇首次登入引導確認、不強迫修改"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["付款與訂閱商業經驗可轉移到商務SaaS", "規格、驗收與維運串成完整交付案例", "既有客戶風險取捨與Gen AI產品應用具體"], "key_gaps": ["零售商務模組經驗廣度", "Scrum實際運作與PO責任", "留存、付款與安全觀察的衡量口徑"], "strengths": ["完整規格驗收交付責任清楚", "支付成本與定價決策直接相關", "產品AI生成案例已上線"], "interview_questions": ["請以付款案例展示需求、規格、驗收與商業取捨。", "做過哪些物流、優惠券、會員及訂單流程？", "曾如何運作Scrum？若未做過，如何銜接？", "留存年化公式、母體與選擇偏差為何？", "付款占比變化對淨收益和轉換有何影響？", "帳號冒用觀察來源及涵蓋範圍為何？", "AI生成如何定義品質、風險與使用成效？", "方向與資源配置哪些由本人決定？"], "editorial_appendix": ["支付與Gen AI產品案例可前移，以提高職缺相關證據可見性。"], "spectrum": {"level": 8, "uncertainty_levels": 1, "basis": "多個交付與商業案例，具明確取捨、比較基準及歸因限制；商務廣度與Scrum仍待面試核對"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷 K｜第 1 輪｜model_id: unknown

### 1. 結論

- 招聘決定：interview

- Level：8（±1）

- 一句話理由：「規劃由 App 內購轉向網頁付款」，兼具交付與取捨，足以面試。

### 2. 六維度

| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 訂閱制 B2C App 與雙邊媒合平台。 | 零售全通路領域需到職銜接 |
| role_evidence | 足夠 | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 商務模組廣度及Scrum運作需面試釐清 |
| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 可追問替代方案與成功標準 |
| outcome_quality | 足夠 | 為觀察差異，非因果。 | 留存年化、營收占比與安全觀察的量測限制 |
| ownership | 強 | 由我主責規劃，與工程團隊密切協作 | 產品方向與資源配置的最終決策權待確認 |
| readability | 足夠 | 近 10 年 PM 經驗，經手 6 款產品 | 可將支付與AI產品案例前移；不影響面試 |

### 3. JD 條件對照

| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 經歷5年以上；產品管理2年以上 | 必要 | supported | 近 10 年 PM 經驗 | 工作時序支持兩項年資門檻 |
| 完整產品循環，與UX、RD、QA合作交付上市 | 必要 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 具規格、原型、工程協作及驗收上線案例 |
| 理解商業模式、利害關係人需求及具體規格 | 必要 | supported | 對接 16 個需求單位 | 訂閱定價、實收試算及需求轉PRD直接相關 |
| 定義目標及衡量標準，分析效益 | 必要 | supported | 定義使用情境與驗收標準 | 具實驗對照與留存觀察，成效歸因仍需追問 |
| 維運需求及產品指標、工作效率優化 | 必要 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 工單、週報與安全修復具體 |
| 金流、物流、會員、促購、優惠券、購買流程、訂單功能經驗 | 必要 | partial | 規劃由 App 內購轉向網頁付款 | 支付、訂閱、資格門檻可轉移；物流、優惠券、訂單未呈現 |
| 產品設計、RD合作與製作使用者介面 | 必要 | supported | 以 Use Case、Wireframe 定義業務流程與畫面 | 介面原型與工程交付有案例 |
| 參與和運作Scrum團隊 | 必要 | partial | Kanban 搭配瀑布式開發 | 有站會回顧線索；未證實Scrum實際運作，不等於不會 |
| 從0到1產品開發 | 加分 | partial | 主導 Juicy 上線 | 有上市證據，從探索至首次推出的完整邊界待問 |
| 熟悉支付產業生態及趨勢 | 加分 | partial | 依抽成、稅、手續費及撥款週期做實收試算 | 支付實務直接相關；近期生態趨勢未呈現 |
| 簡報募資、提案；200人以上軟體團隊工作2年以上 | 加分 | unknown | 未提供 | 兩項加分均未明示，不以公司名或企劃人數推論 |
| Gen AI加入產品具體案例 | 加分 | supported | AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。 | 文字生成情境及資料科學協作支持；不將個人工具當產品案例 |

JD的經歷欄與內文門檻分別核對，均有支持；商務模組列為部分支持，不將未寫事項判為矛盾。R11合併兩項各自unknown的加分項以符合列數上限。

### 4. HR 十二問 ／ HM 十三問

| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 規劃由 App 內購轉向網頁付款 | 支付與PO交付直接相關 |
| HR02 | supported | 企業端招募系統全模組與求職端公司頁 | 企業流程可轉移至SaaS |
| HR03 | supported | 由我主責規劃，與工程團隊密切協作 | 個人規劃與工程邊界清楚 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 效率改變可追問口徑 |
| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 有既有客戶風險取捨 |
| HR06 | supported | 從交友與訂閱制 App 到企業招募系統 | 領域與責任變化清楚 |
| HR07 | supported | 與資料科學團隊合作 | 協作有產品應用案例 |
| HR08 | supported | 資深產品經理｜Senior Product Manager | 結構能定位近期責任 |
| HR09 | partial | 上線後至 2026/10 未再出現同類帳號冒用 | 需核對通報涵蓋與觀察口徑 |
| HR10 | supported | 我希望將更多心力放回產品策略 | 方向與產品價值判斷相容 |
| HR11 | unknown | 台北市、新北市，可接受遠端或混合辦公 | JD未列完整條件，無已知衝突 |
| HR12 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 交付與商業案例足以約談 |
| HM01 | supported | 訂閱制 B2C App 與雙邊媒合平台。 | 企業流程及訂閱經驗可轉移 |
| HM02 | supported | 最大宗是溝通管道中斷 | 使用者困難改變優先級 |
| HM03 | supported | 選擇首次登入引導確認、不強迫修改 | 具保護既有客戶的取捨 |
| HM04 | supported | 依抽成、稅、手續費及撥款週期做實收試算 | 成本及定價有商業判斷 |
| HM05 | partial | 為觀察差異，非因果。 | 衡量有基準但需核對口徑 |
| HM06 | supported | 由我主責規劃，與工程團隊密切協作 | 規劃與工程責任有區分 |
| HM07 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 交付與風險處理具體 |
| HM08 | supported | 並與 CodaPay 新加坡技術團隊協調串接。 | 可追問支付整合技術限制 |
| HM09 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 自主範圍支持資深IC面試 |
| HM10 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 重點易找到，可調整排序 |
| HM11 | supported | 依客服測試回饋調整推薦規則。 | 回饋確實改變推薦規則 |
| HM12 | supported | 規劃由 App 內購轉向網頁付款 | 面試用付款案例驗證能力 |
| HM13 | not_applicable | 不適用 | 方法層；獨立按JD審查，不計分 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）

| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「規劃由 App 內購轉向網頁付款」：直接連到支付與購買流程。 |
| 2 | 「與 QA 制定 UAT 驗收案例、排定上線計畫」：支持完整循環。 |
| 3 | 「選擇首次登入引導確認、不強迫修改」：支持使用者與風險取捨。 |
| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 商務模組廣度 | 實際做過哪些物流、訂單與優惠流程？ |
| 2 | Scrum運作 | 如何管理Sprint與Backlog？ |
| 3 | 衡量口徑 | 留存年化、付款價值及安全觀察來源為何？ |

### 6. 評語（給寫稿者的具體回饋）

**做得好（3 點）**：

1. 1111交付｜「與 QA 制定 UAT 驗收案例、排定上線計畫」｜規格到上市的責任有直接證據。

2. 思維特支付｜「依抽成、稅、手續費及撥款週期做實收試算」｜連結商業模式與支付選擇。

3. 1111 AI｜「AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。」｜對應Gen AI產品加分項。

**可改進（5 點）**：



- 位置：尚凡付款與商務經驗

- 原句：規劃由 App 內購轉向網頁付款

- 問題類型：requirement

- 嚴重度：interview_follow_up

- 影響：物流、優惠券及訂單等零售流程未呈現；影響上手範圍而非證實不符

- 建議方向：面試用購買流程拆解確認能力與待學範圍



- 位置：專業技能／交付

- 原句：Kanban 搭配瀑布式開發

- 問題類型：requirement

- 嚴重度：interview_follow_up

- 影響：站會與回顧不能單獨證實運作Scrum；需確認PO角色適配

- 建議方向：追問Sprint、Backlog及Review實作，沒有就誠實說明



- 位置：1111留存觀察

- 原句：該群年化留存 81.2%，同期全站 74.2%

- 問題類型：measurement

- 嚴重度：interview_follow_up

- 影響：短期快照年化公式與群組選擇影響可比性；面試核對

- 建議方向：補年化公式、觀察窗及樣本納入規則



- 位置：1111登入安全

- 原句：上線後至 2026/10 未再出現同類帳號冒用

- 問題類型：measurement

- 嚴重度：interview_follow_up

- 影響：目前掌握的情況不等同全面監測；需問來源及漏報限制

- 建議方向：維持觀察措辭，說明客服通報或其他紀錄範圍



- 位置：尚凡Peach付款

- 原句：Peach 網頁付款占營收由 24% 至 80% 以上

- 問題類型：measurement

- 嚴重度：interview_follow_up

- 影響：通路占比無法獨立證明淨收益或付款轉換提升；面試核對

- 建議方向：補可公開的淨收入或轉換口徑，無資料不補數字



**編輯附件**（不影響判斷）：支付與AI產品案例可前移；不需要增加術語或編造量測。

### 7. 資深能力分布

delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

有自主排序與商業判斷；未明示整體資源預算權，不推論管理職能力。

### 8. 未測試聲明

PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

本輪僅讀文字；履歷自述與內部一致性不代表外部查證。

### 成果分類補表

| 原文片段 | 分類 | 解讀限制 |
| :-- | :-- | :-- |
| 約 50 項大項功能上線 | output | 依正文限制解讀 |
| 需求平均處理週期由 100.4 天降至 30.9 天 | outcome | 依正文限制解讀 |
| 該群年化留存 81.2%，同期全站 74.2% | outcome | 依正文限制解讀 |
| 選擇首次登入引導確認、不強迫修改 | decision | 依正文限制解讀 |
| Peach 網頁付款占營收由 24% 至 80% 以上 | outcome | 依正文限制解讀 |
| 目前專案仍在開發中 | in_progress | 依正文限制解讀 |
| 全站活躍付費廠商約 6.6 萬家 | context | 系統規模非本人業績 |
| 另於 2026/01–06 上線 111 項 Roadmap 細項 | output | 與50項粒度不同，不相加 |
| 第一階段於 2025/10 離峰切換上線 | output | 僅第一階段完成 |
| 停機約 1.5 小時 | context | 上線操作限制非效益 |
| 於 2026/04/17 上線簽章驗證 | output | 工程實作不歸本人 |
| 上線後至 2026/10 未再出現同類帳號冒用 | outcome | 目前掌握範圍非全面監測 |
| 完成 1,726／1,857 張需求與問題單，約 93% | output | 工單完成非客戶結果 |
| 需求管線觸及 1,279 家活躍付費廠商 | context | 觸及母體非全站成效 |
| AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。 | output | 採用及業務結果未列 |
| 依客服測試回饋調整推薦規則。 | decision | 已發生修正 |
| 降價期 iOS 非續訂營收較基準期增 5% | outcome | 各期21天，跨平台差異不能獨立證因果 |
| Android 減 18%，相對變化約多 28% | outcome | 相對變化非28個百分點 |
| 還原原價後 iOS 較基準期減 65% | outcome | 回復期差異仍需檢查干擾 |
| 依結果全面調降售價 | decision | 不視為後續成效 |
| KOOL 訂閱與付費牆規劃上線 | output | 功能上線非營收提升 |
| 才開放精選網紅資格 | decision | 資格門檻設計 |
| 主導 Juicy 上線 | output | 0到1探索範圍尚待核對 |
| 上線後 6 週男性 DAU 約 3,200 至 1.25 萬 | outcome | 產品與行銷共同期間表現 |
| 與最多約 10 位外國實習生協作 | context | 無直屬管理，不以人數加分 |
| 美國、墨西哥、巴西、印尼、馬來西亞、日本、韓國 7 個市場 | output | 市場範圍非採用成效 |
| 開放印尼、泰國等市場的電信帳單與超商付款 | output | 支付選項交付 |
| 提出 7／30／90 天訂閱方案與加贈內容 | output | 方案提出非已實現收益 |
| Newegg.com 商品資訊英翻中與校對。 | output | 翻譯交付非產品結果 |
| 將信件與即時通整合排在其他新功能之前 | decision、in_progress | 已排序；開發中不算成果 |
| 用於規格撰寫、資料整理與分析 | output | AI工作協作非AI產品成果 |

### 執行紀錄

續行同一A審查，輪數仍為1。先前中斷記為technical_failure；續行時未發現既有JSON或Markdown，無失敗原稿可保留。未新增評分輪次。

結構驗證：validate_run.py A-jd34-K 回傳 pass，errors=[]。本輪未發生格式驗證失敗或判定修復。


## A-jd34-M｜履歷M

```json
{"rubric_version": "4.2", "resume_id": "M", "job_id": "jd34", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd34-M", "human_calibrated": false, "requirements": [{"id": "R01", "text": "年資：欄位5年以上、內文2年以上產品管理", "type": "required", "status": "supported", "evidence": ["近 10 年 PM 經驗"], "blocks_interview": false, "reason": "兩種年資門檻均有支持"}, {"id": "R02", "text": "完整產品循環及UX、RD、QA協作上市", "type": "required", "status": "supported", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "blocks_interview": false, "reason": "需求至驗收與上市皆有案例"}, {"id": "R03", "text": "理解商業模式、蒐集需求及具體規格", "type": "required", "status": "supported", "evidence": ["以 Use Case、Wireframe 定義業務流程與畫面"], "blocks_interview": false, "reason": "訂閱及企業流程經驗可轉移"}, {"id": "R04", "text": "定義目標衡量標準並分析效益", "type": "required", "status": "supported", "evidence": ["為觀察差異，非因果"], "blocks_interview": false, "reason": "比較期間及限制有交代"}, {"id": "R05", "text": "日常維運及指標效率優化", "type": "required", "status": "supported", "evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "blocks_interview": false, "reason": "工單與安全上線具直接案例"}, {"id": "R06", "text": "金流等交易相關功能開發", "type": "required", "status": "supported", "evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "blocks_interview": false, "reason": "金流及付費牆支持；物流訂單未呈現"}, {"id": "R07", "text": "產品設計、RD合作及使用者介面", "type": "required", "status": "supported", "evidence": ["從 User Story、Wireframe 到 Figma／Axure 原型"], "blocks_interview": false, "reason": "原型及規格有實作情境"}, {"id": "R08", "text": "參與和運作Scrum團隊", "type": "required", "status": "unknown", "evidence": ["以 Kanban 推進瀑布式開發"], "blocks_interview": false, "reason": "未寫Scrum不代表未做過；面試確認"}, {"id": "R09", "text": "從0到1產品開發", "type": "preferred", "status": "partial", "evidence": ["主導 Juicy 上線"], "blocks_interview": false, "reason": "有新產品上線，初始探索與範圍待核對"}, {"id": "R10", "text": "熟悉支付生態趨勢及簡報募資提案", "type": "preferred", "status": "partial", "evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "blocks_interview": false, "reason": "支付實務有支持；趨勢及提案場合待問"}, {"id": "R11", "text": "200人以上軟體開發團隊工作2年以上", "type": "preferred", "status": "unknown", "evidence": [], "blocks_interview": false, "reason": "未提供團隊規模與任期對應"}, {"id": "R12", "text": "Gen AI加入產品具體案例", "type": "preferred", "status": "supported", "evidence": ["AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。"], "blocks_interview": false, "reason": "有生成情境、驗收及回饋"}], "dimensions": [{"id": "positioning", "rating": "強", "evidence": ["訂閱制 B2C App 與雙邊媒合平台。"], "missing": ["零售OMO領域轉移需面試核對"], "issue_ids": []}, {"id": "role_evidence", "rating": "足夠", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "missing": ["Scrum運作及零售交易情境待問"], "issue_ids": ["I01"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": ["產品組合與資源配置深度待核對"], "issue_ids": ["I03"]}, {"id": "outcome_quality", "rating": "強", "evidence": ["為觀察差異，非因果"], "missing": ["安全觀察來源及定價干擾因素待問"], "issue_ids": ["I02"]}, {"id": "ownership", "rating": "強", "evidence": ["由我擬定取數的資料表與欄位"], "missing": ["方向及資源最終決策權待問"], "issue_ids": ["I03"]}, {"id": "readability", "rating": "足夠", "evidence": ["曾設計定價實驗、規劃網頁付款"], "missing": ["可前置交易與支付案例"], "issue_ids": []}], "results": [{"quote": "約 50 項大項功能上線", "kinds": ["output"]}, {"quote": "需求平均處理週期由 100.4 天降至 30.9 天", "kinds": ["outcome"]}, {"quote": "該群年化留存 81.2%，同期全站 74.2%", "kinds": ["outcome"]}, {"quote": "改版排在新功能職缺健檢之前（兩案皆開發中）", "kinds": ["decision", "in_progress"]}, {"quote": "Peach 網頁付款占營收由 24% 至 80% 以上", "kinds": ["outcome"]}, {"quote": "上線後 6 週男性 DAU 約 3,200 至 1.25 萬", "kinds": ["outcome"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["曾設計定價實驗、規劃網頁付款"], "application_note": "支付與產品交付可轉移"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "企業流程相關，非零售同域"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "application_note": "規劃與工程責任可區分"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "效率變化具比較期"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "有使用者風險取捨"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["從交友與訂閱制 App 到企業招募系統"], "application_note": "職涯領域與責任連貫"}, {"rule_id": "HR07", "status": "supported", "resume_evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "application_note": "技能連結實際協作"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["曾設計定價實驗、規劃網頁付款"], "application_note": "摘要能辨識相關性"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["依目前掌握的情況"], "application_note": "安全結果需確認監測來源"}, {"rule_id": "HR10", "status": "supported", "resume_evidence": ["我希望將更多心力放回產品策略"], "application_note": "方向與職缺相容"}, {"rule_id": "HR11", "status": "unknown", "resume_evidence": [], "application_note": "摘要未列明工作條件衝突"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "application_note": "足以面試，Scrum留待核對"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["訂閱制 B2C App 與雙邊媒合平台。"], "evidence_type": "context", "source_ids": [], "interview_question": "如何轉移到零售OMO情境？"}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["客服反映配對名單「少又舊」"], "evidence_type": "decision", "source_ids": [], "interview_question": "如何驗證排序調整改善使用者問題？"}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["改版排在新功能職缺健檢之前（兩案皆開發中）"], "evidence_type": "decision", "source_ids": [], "interview_question": "如何比較價值與成本？"}, {"rule_id": "HM04", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "evidence_type": "decision", "source_ids": [], "interview_question": "支付方案的成本和採用取捨為何？"}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "supported", "resume_evidence": ["為觀察差異，非因果"], "evidence_type": "outcome", "source_ids": [], "interview_question": "定價實驗如何控制平台差異與促銷因素？"}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["與資料科學團隊合作，定義使用情境與驗收標準"], "evidence_type": "output", "source_ids": [], "interview_question": "與資料科學及工程的決策邊界為何？"}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["第一階段於 2025/10 離峰切換上線"], "evidence_type": "output", "source_ids": [], "interview_question": "上線驗收與回復機制如何設定？"}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["整理為 PRD 與 Axure Prototype"], "evidence_type": "output", "source_ids": [], "interview_question": "如何拆解付款失敗與退款規則？"}, {"rule_id": "HM09", "primary_dimension": "ownership", "status": "partial", "resume_evidence": ["對接 16 個需求單位"], "evidence_type": "context", "source_ids": [], "interview_question": "如何取得跨部門資源與方向決策權？"}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["曾設計定價實驗、規劃網頁付款"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則"], "evidence_type": "decision", "source_ids": [], "interview_question": "哪一個回饋具體改變驗收標準？"}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "evidence_type": "output", "source_ids": [], "interview_question": "請用付款案例展示規格與上線決策。"}, {"rule_id": "HM13", "primary_dimension": "method", "status": "supported", "resume_evidence": [], "evidence_type": "context", "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HR07", "source_ids": [], "application_note": "Scrum運作經驗留待面試確認", "context_limit": "Kanban與瀑布不證明未有Scrum經驗", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "以 Kanban 推進瀑布式開發", "reason": "JD希望參與及運作Scrum；文件未提供直接案例，現有交付經驗仍支持面試。", "suggestion": "若有實際經驗補充團隊運作與本人角色，否則說明可轉移做法。"}, {"id": "I02", "rule_id": "HM05", "source_ids": [], "application_note": "核對成果的觀察範圍", "context_limit": "自述不是監測紀錄；不推論數據不實", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "依目前掌握的情況", "reason": "未再冒用的資訊來源不明；定價亦需控制因素，影響成效追問而非面試資格。", "suggestion": "交代安全觀察管道與覆蓋範圍；面試確認定價各期可比性。"}, {"id": "I03", "rule_id": "HM09", "source_ids": [], "application_note": "核對產品方向與資源權責", "context_limit": "協調範圍不等於最終決策權", "category": "ownership", "severity": "interview_follow_up", "block_target": null, "claim": "對接 16 個需求單位", "reason": "主導方向所需的資源配置與最終拍板邊界較少，應用代表案確認。", "suggestion": "補充一項方向決策的授權、資源衝突與核定方式。"}], "decision": {"recommendation": "interview", "evidence": ["曾設計定價實驗、規劃網頁付款", "與 QA 制定 UAT 驗收案例、排定上線計畫"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["支付及訂閱設計可轉移到交易產品", "完整交付與跨部門協調有具體責任", "決策、衡量及限制可供深入驗證"], "key_gaps": ["Scrum實際運作案例", "成果觀察來源與比較限制", "產品方向及資源最終權責"], "strengths": ["付款及訂閱商業理解有案例", "從規格至驗收交付責任清楚", "能區分觀察差異與因果"], "interview_questions": ["曾如何參與或運作Scrum團隊？", "如何將支付經驗轉移到零售交易和OMO？", "定價比較如何排除平台及同期活動影響？", "安全事件由何管道監測，有哪些未涵蓋情境？", "如何決定資源配置，最終拍板者是誰？", "請展示付款規格、異常處理及驗收範例。", "生成式AI功能如何定義品質與驗收？"], "editorial_appendix": ["可將支付、訂閱及AI產品案例前置，以利辨識JD關聯。"], "spectrum": {"level": 8, "uncertainty_levels": 1, "basis": "多個交付、付款與決策案例，衡量具期間及限制；Scrum與零售情境待核對。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷｜第 1 輪｜model_id: unknown

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「曾設計定價實驗、規劃網頁付款」搭配完整交付，足以面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 訂閱制 B2C App 與雙邊媒合平台。 | 零售OMO領域轉移需面試核對 |
| role_evidence | 足夠 | 與 QA 制定 UAT 驗收案例、排定上線計畫 | Scrum運作及零售交易情境待問 |
| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 產品組合與資源配置深度待核對 |
| outcome_quality | 強 | 為觀察差異，非因果 | 安全觀察來源及定價干擾因素待問 |
| ownership | 強 | 由我擬定取數的資料表與欄位 | 方向及資源最終決策權待問 |
| readability | 足夠 | 曾設計定價實驗、規劃網頁付款 | 可前置交易與支付案例 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 年資：欄位5年以上、內文2年以上產品管理 | required | supported | 近 10 年 PM 經驗 | 兩種年資門檻均有支持 |
| 完整產品循環及UX、RD、QA協作上市 | required | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 需求至驗收與上市皆有案例 |
| 理解商業模式、蒐集需求及具體規格 | required | supported | 以 Use Case、Wireframe 定義業務流程與畫面 | 訂閱及企業流程經驗可轉移 |
| 定義目標衡量標準並分析效益 | required | supported | 為觀察差異，非因果 | 比較期間及限制有交代 |
| 日常維運及指標效率優化 | required | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 工單與安全上線具直接案例 |
| 金流等交易相關功能開發 | required | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 金流及付費牆支持；物流訂單未呈現 |
| 產品設計、RD合作及使用者介面 | required | supported | 從 User Story、Wireframe 到 Figma／Axure 原型 | 原型及規格有實作情境 |
| 參與和運作Scrum團隊 | required | unknown | 以 Kanban 推進瀑布式開發 | 未寫Scrum不代表未做過；面試確認 |
| 從0到1產品開發 | preferred | partial | 主導 Juicy 上線 | 有新產品上線，初始探索與範圍待核對 |
| 熟悉支付生態趨勢及簡報募資提案 | preferred | partial | 依抽成、稅、手續費及撥款週期做實收試算 | 支付實務有支持；趨勢及提案場合待問 |
| 200人以上軟體開發團隊工作2年以上 | preferred | unknown | 未呈現 | 未提供團隊規模與任期對應 |
| Gen AI加入產品具體案例 | preferred | supported | AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。 | 有生成情境、驗收及回饋 |
支付趨勢與募資提案因列數上限合列，分開判讀：支付實務有支持；最新趨勢與提案場合未知。職缺沒有要求所有交易模組均有經驗。Scrum未知不作矛盾或阻擋；以已有交付基礎安排面試驗證。

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 曾設計定價實驗、規劃網頁付款 | 支付與產品交付可轉移 |
| HR02 | supported | 企業端招募系統全模組與求職端公司頁 | 企業流程相關，非零售同域 |
| HR03 | supported | 由我主責規劃，與工程團隊密切協作 | 規劃與工程責任可區分 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 效率變化具比較期 |
| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 有使用者風險取捨 |
| HR06 | supported | 從交友與訂閱制 App 到企業招募系統 | 職涯領域與責任連貫 |
| HR07 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 技能連結實際協作 |
| HR08 | supported | 曾設計定價實驗、規劃網頁付款 | 摘要能辨識相關性 |
| HR09 | partial | 依目前掌握的情況 | 安全結果需確認監測來源 |
| HR10 | supported | 我希望將更多心力放回產品策略 | 方向與職缺相容 |
| HR11 | unknown | 未呈現 | 摘要未列明工作條件衝突 |
| HR12 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 足以面試，Scrum留待核對 |
| HM01 | supported | 訂閱制 B2C App 與雙邊媒合平台。 | 企業流程及訂閱可轉移 |
| HM02 | supported | 客服反映配對名單「少又舊」 | 客服問題連結調整方案 |
| HM03 | supported | 改版排在新功能職缺健檢之前（兩案皆開發中） | 進行中可支持取捨 |
| HM04 | supported | 依抽成、稅、手續費及撥款週期做實收試算 | 具成本及變現判斷 |
| HM05 | supported | 為觀察差異，非因果 | 有比較與限制，需核口徑 |
| HM06 | supported | 與資料科學團隊合作，定義使用情境與驗收標準 | 具角色邊界，仍可追問 |
| HM07 | supported | 第一階段於 2025/10 離峰切換上線 | 規格驗收到上線具案例 |
| HM08 | supported | 整理為 PRD 與 Axure Prototype | 技術規則可用付款案驗證 |
| HM09 | partial | 對接 16 個需求單位 | 方向資源權限需確認 |
| HM10 | supported | 曾設計定價實驗、規劃網頁付款 | 相關證據可迅速辨識 |
| HM11 | supported | 依客服測試回饋調整推薦規則 | 有依回饋修正案例 |
| HM12 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 可用工作樣本驗證 |
| HM13 | supported | 方法層：無履歷引句 | 依本JD獨立判讀，未作真人校準 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「曾設計定價實驗、規劃網頁付款」支持交易產品理解。 |
| 2 | 「與 QA 制定 UAT 驗收案例、排定上線計畫」支持交付。 |
| 3 | 「為觀察差異，非因果」保留衡量限制。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | Scrum案例 | 曾如何運作Scrum，如何處理阻塞？ |
| 2 | 衡量觀察範圍 | 安全監測來源及定價比較干擾為何？ |
| 3 | 方向資源權責 | 何種決策可自行拍板，如何取得資源？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
1. 尚凡付款｜「並與 CodaPay 新加坡技術團隊協調串接」｜支持支付整合及跨團隊協作。
2. 1111交付｜「與 QA 制定 UAT 驗收案例、排定上線計畫」｜連結規格與上市責任。
3. 1111留存｜「為觀察差異，非因果」｜保留成效解讀限制，利於效益分析追問。

**可改進（3 點）**：
- 位置：專業摘要與交付技能
- 原句：以 Kanban 推進瀑布式開發
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：JD希望參與及運作Scrum；文件未提供直接案例，現有交付經驗仍支持面試。
- 建議方向：若有實際經驗補充團隊運作與本人角色，否則說明可轉移做法。

- 位置：1111成果與責任段
- 原句：依目前掌握的情況
- 問題類型：measurement
- 嚴重度：interview_follow_up
- 影響：未再冒用的資訊來源不明；定價亦需控制因素，影響成效追問而非面試資格。
- 建議方向：交代安全觀察管道與覆蓋範圍；面試確認定價各期可比性。

- 位置：1111成果與責任段
- 原句：對接 16 個需求單位
- 問題類型：ownership
- 嚴重度：interview_follow_up
- 影響：主導方向所需的資源配置與最終拍板邊界較少，應用代表案確認。
- 建議方向：補充一項方向決策的授權、資源衝突與核定方式。

**編輯附件**（不影響判斷）：可前置支付、訂閱及AI產品案例。

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run
履歷自述尚未外部查證。本輪只依指定JD摘要與文字履歷，沒有補充查詢。

### 成果分類補表
| 原句片段 | 分類 | 解讀限制 |
| :-- | :-- | :-- |
| 約 50 項大項功能上線 | output | 依履歷自述；數字非外部查證 |
| 需求平均處理週期由 100.4 天降至 30.9 天 | outcome | 依履歷自述；數字非外部查證 |
| 該群年化留存 81.2%，同期全站 74.2% | outcome | 依履歷自述；數字非外部查證 |
| 改版排在新功能職缺健檢之前（兩案皆開發中） | decision、in_progress | 進行中非已實現成果 |
| Peach 網頁付款占營收由 24% 至 80% 以上 | outcome | 依履歷自述；數字非外部查證 |
| 上線後 6 週男性 DAU 約 3,200 至 1.25 萬 | outcome | 依履歷自述；數字非外部查證 |
| 全站活躍付費廠商約 6.6 萬家 | context | 產品規模，非個人成果 |
| 另於 2026/01–06 上線 111 項 Roadmap 細項 | output | 與大項粒度不同，不加總 |
| 上千組重複 E-mail | context | 資料風險規模 |
| 選擇首次登入引導確認、不強迫修改 | decision | 登入風險取捨 |
| 停機約 1.5 小時 | output | 切換觀察，不等於客戶效益 |
| 十多家廠商帳號遭冒用 | context | 事件起因 |
| 於 2026/04/17 上線簽章驗證 | output | 已交付安全措施 |
| 上線後至 2026/10 未再出現同類帳號冒用 | outcome | 掌握範圍內觀察，未等同監測查證 |
| 完成 1,726／1,857 張需求與問題單，約 93% | output | 截至09/29工單完成率 |
| 信件與即時通整合排在其他新功能之前 | decision、in_progress | 未完成，不當成果 |
| 改依職缺上線日排序、20 天內不重複推薦 | decision、output | 規則變更，改善成效未列 |
| 需求管線觸及 1,279 家活躍付費廠商 | context | 觀察群體 |
| 約占全站 66,150 家的 1.9% | context | 母體占比 |
| AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。 | output | 功能交付非採用成效 |
| 依客服測試回饋調整推薦規則 | decision | 回饋促成修正 |
| 降價期 iOS 非續訂營收較基準期增 5% | outcome | 各期21天平台比較 |
| Android 減 18%，相對變化約多 28% | outcome | 相對變化非因果證明 |
| 還原原價後 iOS 較基準期減 65% | outcome | 尚待排除時序干擾 |
| 依結果全面調降售價 | decision | 實驗後決策 |
| KOOL 訂閱與付費牆規劃上線 | output | 功能交付 |
| 主導 Juicy 上線 | output | 0到1範圍待核對 |
| 涵蓋美國、墨西哥、巴西、印尼、馬來西亞、日本、韓國 7 個市場 | output、context | 在地化範圍 |
| 與最多約 10 位外國實習生協作 | context | 無直屬管理關係 |
| 導入 CodaPay | output | 支付整合 |
| 提出 7／30／90 天訂閱方案與加贈內容 | decision、output | 方案設計非收益 |
| Newegg.com 商品資訊英翻中與英文校對 | output | 早期工作產出 |
| 12 條分支、23 個共用 skill | output | 個人工具流程非產品AI成果 |


## B-jd34｜揭盲：甲=M、乙=K；偏好=M

```json
{"job_id":"jd34","order":"甲=M/乙=K","differences":[{"what":"甲補出搜尋改版優先級與配對規則根因，乙僅於自傳保留溝通管道排序案例。","hiring_meaning":"甲讓主管可追問如何從抱怨定位根因、取捨新功能與維運改善；並不能據此認定乙缺乏該能力。","type":"capability"},{"what":"甲交代留存分析由本人擬定資料表欄位、交DBA取數及試算表比對，乙只列快照與結果。","hiring_meaning":"甲更能界定數據分析分工，面試可驗證指標定義、樣本選擇及分析深度；兩者皆明示非因果。","type":"measurement"}],"preference":"甲","reason":"兩版付款、定價、交付與AI產品證據相同；甲另提供優先級與根因分析案例，且交代取數分工，更能設計產品判斷與指標分析追問。Scrum及零售OMO經驗仍須查證。","evidence_甲":["客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。","由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。"],"evidence_乙":["例如廠商抱怨工單中，最大宗是溝通管道中斷，我便將信件與即時通整合排在其他新功能之前，目前專案仍在開發中。","比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。"]}
```

## 版本比較｜jd34｜順序 甲=M 乙=K｜model_id: unknown
- 偏好：甲（揭盲：M）

| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 甲補出搜尋改版優先級與配對規則根因，乙僅於自傳保留溝通管道排序案例。 | 甲讓主管可追問如何從抱怨定位根因、取捨新功能與維運改善；並不能據此認定乙缺乏該能力。 | capability | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 | 例如廠商抱怨工單中，最大宗是溝通管道中斷，我便將信件與即時通整合排在其他新功能之前，目前專案仍在開發中。 |
| 2 | 甲交代留存分析由本人擬定資料表欄位、交DBA取數及試算表比對，乙只列快照與結果。 | 甲更能界定數據分析分工，面試可驗證指標定義、樣本選擇及分析深度；兩者皆明示非因果。 | measurement | 由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |

- 理由（≤120 字）：兩版付款、定價、交付與AI產品證據相同；甲另提供優先級與根因分析案例，且交代取數分工，更能設計產品判斷與指標分析追問。Scrum及零售OMO經驗仍須查證。

比較依指定輸入的共同事實快照前提，未宣稱外部核實。甲的增補用於形成面試驗證題目，不將乙省略的內容解讀為能力不足。兩版既有金流串接、UI原型、QA驗收及Gen AI上市案例相同，不因同義表達改變評價。


# jd36｜逐次輸出


## A-jd36-K｜履歷K

```json
{"rubric_version": "4.2", "resume_id": "K", "job_id": "jd36", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd36-K", "human_calibrated": false, "requirements": [{"id": "R01", "text": "3年以上相關工作經驗", "type": "required", "status": "supported", "evidence": ["近 10 年 PM 經驗"], "blocks_interview": false, "reason": "採正文必要條件3年；經歷時序足以支持。"}, {"id": "R02", "text": "Axure規劃及Jira、Confluence專案管理", "type": "required", "status": "partial", "evidence": ["整理為 PRD 與 Axure Prototype"], "blocks_interview": false, "reason": "Axure有案例；Jira、Confluence未呈現，非證據顯示不會。"}, {"id": "R03", "text": "需求分析、資料架構、原型流程及規格設計", "type": "required", "status": "supported", "evidence": ["以 Use Case、Wireframe 定義業務流程與畫面"], "blocks_interview": false, "reason": "系統分析、舊資料盤點與PRD有具體交付。"}, {"id": "R04", "text": "技術可行性、系統架構關連影響及API規格", "type": "required", "status": "partial", "evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "blocks_interview": false, "reason": "有串接及系統風險案例，API欄位、錯誤處理與架構影響分析深度須追問。"}, {"id": "R05", "text": "合作方需求確認、法遵適法性確認", "type": "required", "status": "partial", "evidence": ["法務與稽核協作"], "blocks_interview": false, "reason": "合作方串接明確；法務僅技能描述，未呈現支付適法性確認案例。"}, {"id": "R06", "text": "時程安排、測試驗收及上線準備", "type": "required", "status": "supported", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "blocks_interview": false, "reason": "本人規劃及QA協作清楚。"}, {"id": "R07", "text": "團隊協作、跨部門及對外溝通與同理心", "type": "required", "status": "supported", "evidence": ["選擇首次登入引導確認、不強迫修改"], "blocks_interview": false, "reason": "顧及客戶登入與客服說明，並有跨部門及外部技術團隊協作。"}, {"id": "R08", "text": "上線功能內部教育訓練", "type": "required", "status": "partial", "evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "blocks_interview": false, "reason": "客服說明有線索，正式教育訓練設計與執行未呈現。"}, {"id": "R09", "text": "線上問題釐清排除", "type": "required", "status": "supported", "evidence": ["與工程協作於 2026/04/17 上線簽章驗證"], "blocks_interview": false, "reason": "帳號冒用事件具問題、處置與上線紀錄自述。"}, {"id": "R10", "text": "依回饋與使用狀況迭代優化", "type": "required", "status": "supported", "evidence": ["依客服測試回饋調整推薦規則"], "blocks_interview": false, "reason": "有使用回饋影響功能規則的案例。"}, {"id": "R11", "text": "代理收付、電子支付與行動支付知識應用", "type": "preferred", "status": "partial", "evidence": ["開放印尼、泰國等市場的電信帳單與超商付款"], "blocks_interview": false, "reason": "具有支付應用與實收試算，台灣電子支付及代理收付細節未呈現。"}, {"id": "R12", "text": "資管資工學系或相關工作經驗", "type": "preferred", "status": "supported", "evidence": ["釐清需求與系統分析後"], "blocks_interview": false, "reason": "以系統分析、串接工作支持相關工作經驗路徑，不以科系否定。"}], "dimensions": [{"id": "positioning", "rating": "足夠", "evidence": ["企業端招募系統全模組與求職端公司頁"], "missing": ["轉入電子支付內部系統的動機可面試確認。"], "issue_ids": []}, {"id": "role_evidence", "rating": "足夠", "evidence": ["整理為 PRD 與 Axure Prototype"], "missing": ["Jira／Confluence及支付API規格深度須追問。", "法遵與內訓案例尚不完整。"], "issue_ids": ["I01", "I02", "I03"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": [], "issue_ids": []}, {"id": "outcome_quality", "rating": "足夠", "evidence": ["為觀察差異，非因果"], "missing": ["安全事件追蹤的監測範圍未交代。"], "issue_ids": ["I04"]}, {"id": "ownership", "rating": "強", "evidence": ["由我主責規劃，與工程團隊密切協作"], "missing": [], "issue_ids": []}, {"id": "readability", "rating": "足夠", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "missing": ["可優先凸顯內部系統與串接案例。"], "issue_ids": []}], "results": [{"quote": "全站活躍付費廠商約 6.6 萬家", "kinds": ["context"]}, {"quote": "約 50 項大項功能上線", "kinds": ["output"]}, {"quote": "需求平均處理週期由 100.4 天降至 30.9 天", "kinds": ["outcome"]}, {"quote": "為觀察差異，非因果", "kinds": ["outcome"]}, {"quote": "選擇首次登入引導確認、不強迫修改", "kinds": ["decision"]}, {"quote": "目前專案仍在開發中", "kinds": ["in_progress"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "application_note": "系統交付與支付串接具直接關聯"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "近期企業系統經驗可轉移"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "application_note": "規劃與工程實作邊界清楚"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "流程結果有比較期，需確認計算口徑"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "展現既有客戶與遷移風險取捨"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["從交友與訂閱制 App 到企業招募系統"], "application_note": "職涯領域與責任演進清楚"}, {"rule_id": "HR07", "status": "partial", "resume_evidence": ["整理為 PRD 與 Axure Prototype"], "application_note": "Axure有應用，Jira等未呈現"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["產品文件：User Journey Map"], "application_note": "分區明確，可調整串接案例排序"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["依目前掌握的情況"], "application_note": "安全結果需確認監測與事件定義"}, {"rule_id": "HR10", "status": "partial", "resume_evidence": ["我希望將更多心力放回產品策略"], "application_note": "策略期待與作業系統職責可面談"}, {"rule_id": "HR11", "status": "unknown", "resume_evidence": [], "application_note": "未提供完整工作條件，無已知衝突"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "application_note": "已有約談價值，缺口可於面試驗證"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["訂閱制 B2C App 與雙邊媒合平台"], "evidence_type": "context", "source_ids": [], "interview_question": "如何將企業系統與付款經驗轉用至內部支付作業？"}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["最大宗是溝通管道中斷"], "evidence_type": "decision", "source_ids": [], "interview_question": "如何從工單判斷問題優先級？"}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "evidence_type": "decision", "source_ids": [], "interview_question": "比較過哪些登入遷移方案？"}, {"rule_id": "HM04", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "partial", "resume_evidence": ["為觀察差異，非因果"], "evidence_type": "outcome", "source_ids": [], "interview_question": "安全事件及週期改善的觀測口徑為何？"}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "evidence_type": "output", "source_ids": [], "interview_question": "串接中本人與工程、合作方各負責什麼？"}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "partial", "resume_evidence": ["API 串接規劃、舊系統資料盤點"], "evidence_type": "context", "source_ids": [], "interview_question": "請說明API欄位、異常回應及架構依賴的規格案例。"}, {"rule_id": "HM09", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則"], "evidence_type": "decision", "source_ids": [], "interview_question": "哪項回饋改變了原規則？"}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "evidence_type": "output", "source_ids": [], "interview_question": "可否以去識別規格展示串接與驗收流程？"}, {"rule_id": "HM13", "primary_dimension": "", "status": "not_applicable", "resume_evidence": [], "evidence_type": null, "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HR07", "source_ids": [], "application_note": "確認指定專案工具經驗", "context_limit": "僅依本履歷與職缺摘要判讀；未外部查證。", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "Figma、Axure RP、Notion、Trello", "reason": "JD指定Jira、Confluence；未列出不等於不具備，面試確認工具經驗與可轉移流程。", "suggestion": "若實際使用過補充用途；否則如實說明可轉移做法。"}, {"id": "I02", "rule_id": "HM08", "source_ids": [], "application_note": "確認API與架構判斷深度", "context_limit": "僅依本履歷與職缺摘要判讀；未外部查證。", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "API 串接規劃、舊系統資料盤點", "reason": "串接經歷支持相關性，但尚不足判斷API規格與架構依賴的技術深度；以案例追問。", "suggestion": "補充一個本人拆解介面規格、錯誤處理與驗收的真實片段。"}, {"id": "I03", "rule_id": "HR01", "source_ids": [], "application_note": "確認法遵協作與教育訓練", "context_limit": "僅依本履歷與職缺摘要判讀；未外部查證。", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "法務與稽核協作", "reason": "未呈現適法性確認的步驟及內訓執行；影響到職後責任範圍確認，不構成不符。", "suggestion": "面試說明法遵合作及內訓的實際角色，未做過則說明。"}, {"id": "I04", "rule_id": "HM05", "source_ids": [], "application_note": "核對安全結果觀測範圍", "context_limit": "僅依本履歷與職缺摘要判讀；未外部查證。", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "上線後至 2026/10 未再出現同類帳號冒用", "reason": "附有掌握範圍的保留語，但未明示監測來源；不能視為完整安全效果驗證。", "suggestion": "補充通報或監測來源及同類事件定義，不新增未驗證結論。"}], "decision": {"recommendation": "interview", "evidence": ["並與 CodaPay 新加坡技術團隊協調串接", "與 QA 制定 UAT 驗收案例、排定上線計畫"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["「整理為 PRD 與 Axure Prototype」支持規格交付。", "「並與 CodaPay 新加坡技術團隊協調串接」具支付整合關聯。", "「選擇首次登入引導確認、不強迫修改」呈現遷移取捨。"], "key_gaps": ["Jira、Confluence使用未呈現。", "API與架構技術深度及支付法遵、內訓須核對。", "安全結果的監測來源與定義未呈現。"], "strengths": ["企業系統從需求到驗收交付具體。", "付款串接與實收試算可轉移至支付職缺。", "遷移取捨、個人責任與結果限制表達清楚。"], "interview_questions": ["曾如何使用Jira與Confluence？若未用過，既有專案流程如何轉移？", "請以一項支付串接說明API欄位、異常回應、重複交易及系統依賴。", "法遵確認和內部教育訓練中，你實際負責什麼？", "登入安全的事件定義、監測來源與觀測涵蓋範圍為何？", "需求週期的起訖點、樣本和案件複雜度如何比較？", "偏向產品策略的下一步，如何看待本職內部作業優化責任？"], "editorial_appendix": ["可將CodaPay串接案例前置，幫助辨識本職缺相關性；不影響能力判斷。"], "spectrum": {"level": 8, "uncertainty_levels": 1, "basis": "多個系統交付與支付串接案例，加上清楚遷移取捨、比較期及觀察限制；特定工具與API深度留待面試。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷 K｜第 1 輪｜model_id: unknown

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「與 QA 制定 UAT 驗收案例、排定上線計畫」及付款串接支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 企業端招募系統全模組與求職端公司頁 | 轉入電子支付內部系統的動機可面試確認。 |
| role_evidence | 足夠 | 整理為 PRD 與 Axure Prototype | Jira／Confluence及支付API規格深度須追問。；法遵與內訓案例尚不完整。 |
| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 足以支持面試，實作細節留待驗證。 |
| outcome_quality | 足夠 | 為觀察差異，非因果 | 安全事件追蹤的監測範圍未交代。 |
| ownership | 強 | 由我主責規劃，與工程團隊密切協作 | 足以支持面試，實作細節留待驗證。 |
| readability | 足夠 | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 可優先凸顯內部系統與串接案例。 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 3年以上相關工作經驗 | 必要 | supported | 近 10 年 PM 經驗 | 採正文必要條件3年；經歷時序足以支持。 |
| Axure規劃及Jira、Confluence專案管理 | 必要 | partial | 整理為 PRD 與 Axure Prototype | Axure有案例；Jira、Confluence未呈現，非證據顯示不會。 |
| 需求分析、資料架構、原型流程及規格設計 | 必要 | supported | 以 Use Case、Wireframe 定義業務流程與畫面 | 系統分析、舊資料盤點與PRD有具體交付。 |
| 技術可行性、系統架構關連影響及API規格 | 必要 | partial | 並與 CodaPay 新加坡技術團隊協調串接 | 有串接及系統風險案例，API欄位、錯誤處理與架構影響分析深度須追問。 |
| 合作方需求確認、法遵適法性確認 | 必要 | partial | 法務與稽核協作 | 合作方串接明確；法務僅技能描述，未呈現支付適法性確認案例。 |
| 時程安排、測試驗收及上線準備 | 必要 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 本人規劃及QA協作清楚。 |
| 團隊協作、跨部門及對外溝通與同理心 | 必要 | supported | 選擇首次登入引導確認、不強迫修改 | 顧及客戶登入與客服說明，並有跨部門及外部技術團隊協作。 |
| 上線功能內部教育訓練 | 必要 | partial | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 客服說明有線索，正式教育訓練設計與執行未呈現。 |
| 線上問題釐清排除 | 必要 | supported | 與工程協作於 2026/04/17 上線簽章驗證 | 帳號冒用事件具問題、處置與上線紀錄自述。 |
| 依回饋與使用狀況迭代優化 | 必要 | supported | 依客服測試回饋調整推薦規則 | 有使用回饋影響功能規則的案例。 |
| 代理收付、電子支付與行動支付知識應用 | 加分 | partial | 開放印尼、泰國等市場的電信帳單與超商付款 | 具有支付應用與實收試算，台灣電子支付及代理收付細節未呈現。 |
| 資管資工學系或相關工作經驗 | 加分 | supported | 釐清需求與系統分析後 | 以系統分析、串接工作支持相關工作經驗路徑，不以科系否定。 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 系統交付與支付串接具直接關聯 |
| HR02 | supported | 企業端招募系統全模組與求職端公司頁 | 近期企業系統經驗可轉移 |
| HR03 | supported | 由我主責規劃，與工程團隊密切協作 | 規劃與工程實作邊界清楚 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 流程結果有比較期，需確認計算口徑 |
| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 展現既有客戶與遷移風險取捨 |
| HR06 | supported | 從交友與訂閱制 App 到企業招募系統 | 職涯領域與責任演進清楚 |
| HR07 | partial | 整理為 PRD 與 Axure Prototype | Axure有應用，Jira等未呈現 |
| HR08 | supported | 產品文件：User Journey Map | 分區明確，可調整串接案例排序 |
| HR09 | partial | 依目前掌握的情況 | 安全結果需確認監測與事件定義 |
| HR10 | partial | 我希望將更多心力放回產品策略 | 策略期待與作業系統職責可面談 |
| HR11 | unknown | 未呈現 | 未提供完整工作條件，無已知衝突 |
| HR12 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 已有約談價值，缺口可於面試驗證 |
| HM01 | supported | 訂閱制 B2C App 與雙邊媒合平台 | 系統與支付經驗可轉移 |
| HM02 | supported | 最大宗是溝通管道中斷 | 工單訊號支持問題辨識 |
| HM03 | supported | 選擇首次登入引導確認、不強迫修改 | 登入遷移有明確取捨 |
| HM04 | supported | 依抽成、稅、手續費及撥款週期做實收試算 | 實收試算支持商業理解 |
| HM05 | partial | 為觀察差異，非因果 | 衡量限制清楚，監測來源待核 |
| HM06 | supported | 由我主責規劃，與工程團隊密切協作 | 個人規劃與工程分工清楚 |
| HM07 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 有驗收與分階段上線證據 |
| HM08 | partial | API 串接規劃、舊系統資料盤點 | 追問API規格及架構依賴 |
| HM09 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 責任範圍支持獨立承擔 |
| HM10 | supported | 企業端招募系統全模組與求職端公司頁 | 重點可辨識，可前置串接案例 |
| HM11 | supported | 依客服測試回饋調整推薦規則 | 回饋有改變規則的證據 |
| HM12 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 以去識別規格驗證技術深度 |
| HM13 | not_applicable | 不適用（方法層） | 方法層不加分；已依JD獨立判讀 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「整理為 PRD 與 Axure Prototype」支持規格交付。 |
| 2 | 「並與 CodaPay 新加坡技術團隊協調串接」具支付整合關聯。 |
| 3 | 「選擇首次登入引導確認、不強迫修改」呈現遷移取捨。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | Jira、Confluence使用未呈現。 | 曾如何使用Jira與Confluence？若未用過，既有專案流程如何轉移？ |
| 2 | API與架構技術深度及支付法遵、內訓須核對。 | 以串接規格、法遵確認與內訓案例說明本人責任。 |
| 3 | 安全結果的監測來源與定義未呈現。 | 登入安全的事件定義、監測來源與觀測涵蓋範圍為何？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
1. 1111交付｜「與 QA 制定 UAT 驗收案例、排定上線計畫」｜對應本職驗收與交付責任。
2. 尚凡付款｜「並與 CodaPay 新加坡技術團隊協調串接」｜能對應外部合作方串接。
3. 1111改版｜「選擇首次登入引導確認、不強迫修改」｜展示既有客戶資料遷移的判斷。

**可改進（4 點）**：

- 位置：專業技能／工具
- 原句：Figma、Axure RP、Notion、Trello
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：JD指定Jira、Confluence；未列出不等於不具備，面試確認工具經驗與可轉移流程。
- 建議方向：若實際使用過補充用途；否則如實說明可轉移做法。

- 位置：專業技能／跨部門與整合
- 原句：API 串接規劃、舊系統資料盤點
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：串接經歷支持相關性，但尚不足判斷API規格與架構依賴的技術深度；以案例追問。
- 建議方向：補充一個本人拆解介面規格、錯誤處理與驗收的真實片段。

- 位置：專業技能／跨部門與整合
- 原句：法務與稽核協作
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：未呈現適法性確認的步驟及內訓執行；影響到職後責任範圍確認，不構成不符。
- 建議方向：面試說明法遵合作及內訓的實際角色，未做過則說明。

- 位置：1111／登入安全
- 原句：上線後至 2026/10 未再出現同類帳號冒用
- 問題類型：measurement
- 嚴重度：interview_follow_up
- 影響：附有掌握範圍的保留語，但未明示監測來源；不能視為完整安全效果驗證。
- 建議方向：補充通報或監測來源及同類事件定義，不新增未驗證結論。

**編輯附件**（不影響判斷）：
- 可將CodaPay串接案例前置，幫助辨識本職缺相關性；不影響能力判斷。

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠
交付與跨部門有完整案例；方向選擇及實收試算支持資源判斷，但未假設具預算或組織管理權。

### 8. 未測試聲明
PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run
僅有履歷自述，非外部查證；本次為單次職缺審查，未跨職缺加總或平均。

### 成果分類補表
| 原句片段 | 分類 | 限制 |
| :-- | :-- | :-- |
| 全站活躍付費廠商約 6.6 萬家 | context | 依正文範圍判讀。 |
| 約 50 項大項功能上線 | output | 依正文範圍判讀。 |
| 需求平均處理週期由 100.4 天降至 30.9 天 | outcome | 依正文範圍判讀。 |
| 為觀察差異，非因果 | outcome | 依正文範圍判讀。 |
| 選擇首次登入引導確認、不強迫修改 | decision | 依正文範圍判讀。 |
| 目前專案仍在開發中 | in_progress | 依正文範圍判讀。 |
| 另於 2026/01–06 上線 111 項 Roadmap 細項 | output | 與50大項不同粒度，不相加。 |
| 停機約 1.5 小時 | output | 切換執行耗時，非使用者成效。 |
| 十多家廠商帳號遭冒用 | context | 事件背景。 |
| 上線後至 2026/10 未再出現同類帳號冒用 | outcome | 限定目前掌握範圍，非完整監測證明。 |
| 完成 1,726／1,857 張需求與問題單，約 93% | output | 需求處理交付量。 |
| 需求管線觸及 1,279 家活躍付費廠商 | context | 樣本範圍，不是新增客戶。 |
| 該群年化留存 81.2%，同期全站 74.2% | outcome | 快照年化觀察差異，非因果。 |
| AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才 | output | 上線不等同使用成效。 |
| 依客服測試回饋調整推薦規則 | decision | 未提供調整後成效。 |
| 相對變化約多 28% | outcome | 定價實驗相對變化，非淨增因果證明。 |
| 依結果全面調降售價 | decision | 方案決策。 |
| Peach 網頁付款占營收由 24% 至 80% 以上 | outcome | 付款管道占比，不等於總營收成長。 |
| KOOL 訂閱與付費牆規劃上線 | output | 交付範圍。 |
| 才開放精選網紅資格 | decision | 門檻規則。 |
| 主導 Juicy 上線 | output | 產品交付。 |
| 男性 DAU 約 3,200 至 1.25 萬 | outcome | 產品與行銷導流整體表現。 |
| 7 個市場 | context | 在地化範圍。 |
| 在無直屬管理關係下分派翻譯與粉專經營任務 | output | 協作交付，非直屬管理。 |
| 開放印尼、泰國等市場的電信帳單與超商付款 | output | 支付串接交付。 |
| 提出 7／30／90 天訂閱方案與加贈內容 | decision | 實收試算支持的方案。 |
| Newegg.com 商品資訊英翻中與校對 | output | 翻譯交付。 |
| 將信件與即時通整合排在其他新功能之前 | decision / in_progress | 排序已決定；仍開發中。 |


## A-jd36-M｜履歷M

```json
{"rubric_version": "4.2", "resume_id": "M", "job_id": "jd36", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd36-M", "human_calibrated": false, "requirements": [{"id": "R01", "text": "3年以上相關工作經驗", "type": "required", "status": "supported", "evidence": ["近 10 年 PM 經驗"], "blocks_interview": false, "reason": "年表支持超過三年；摘要經歷2年以上與必要條件3年以後者判讀。"}, {"id": "R02", "text": "Axure產品規劃及Jira、Confluence專案管理", "type": "required", "status": "partial", "evidence": ["整理為 PRD 與 Axure Prototype"], "blocks_interview": false, "reason": "Axure有實作；Jira、Confluence未呈現，須問工具轉換能力。"}, {"id": "R03", "text": "兼顧技術可行性及系統架構關連影響", "type": "required", "status": "supported", "evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "blocks_interview": false, "reason": "登入改版、舊資料與簽章驗證支持影響評估；架構細節面試確認。"}, {"id": "R04", "text": "熟悉API規格", "type": "required", "status": "partial", "evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "blocks_interview": false, "reason": "具串接案例，規格欄位、錯誤碼及驗收深度未呈現。"}, {"id": "R05", "text": "有效團隊協作、跨部門溝通及同理心", "type": "required", "status": "supported", "evidence": ["選擇首次登入引導確認、不強迫修改"], "blocks_interview": false, "reason": "工程QA客服合作及既有用戶登入限制具體。"}, {"id": "R06", "text": "需求分析、資料架構、畫面流程及規格文件", "type": "required", "status": "supported", "evidence": ["以 Use Case、Wireframe 定義業務流程與畫面"], "blocks_interview": false, "reason": "系統分析、取數表欄位與PRD提供相關證據。"}, {"id": "R07", "text": "確認合作方需求與法遵適法性", "type": "required", "status": "partial", "evidence": ["工程、設計、QA、資料科學、客服、業務、法務與稽核協作"], "blocks_interview": false, "reason": "合作方有案例；法務僅技能敘述，適法性確認過程未呈現。"}, {"id": "R08", "text": "時程、溝通、測試驗收及上線協調", "type": "required", "status": "supported", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "blocks_interview": false, "reason": "上線交付具體。"}, {"id": "R09", "text": "上線內部教育訓練", "type": "required", "status": "partial", "evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "blocks_interview": false, "reason": "客服說明相關但未呈現完整教育訓練。"}, {"id": "R10", "text": "線上問題排除與依反饋持續迭代", "type": "required", "status": "supported", "evidence": ["依客服測試回饋調整推薦規則"], "blocks_interview": false, "reason": "名單根因追查及安全事件處置支持。"}, {"id": "R11", "text": "代理收付、電子支付與行動支付領域", "type": "preferred", "status": "partial", "evidence": ["導入 CodaPay，開放印尼、泰國等市場的電信帳單與超商付款"], "blocks_interview": false, "reason": "有支付經驗；台灣電子支付法規與銀行串接未呈現。"}, {"id": "R12", "text": "資管資工學歷或相關工作經驗", "type": "preferred", "status": "supported", "evidence": ["釐清需求與系統分析後"], "blocks_interview": false, "reason": "國企學歷不符學科分支，但系統分析及串接支持替代工作經驗。"}], "dimensions": [{"id": "positioning", "rating": "足夠", "evidence": ["現任 1111 招募系統 Product Owner"], "missing": ["內部流程與付款串接可轉移；策略期待與職務日常需確認"], "issue_ids": []}, {"id": "role_evidence", "rating": "足夠", "evidence": ["整理為 PRD 與 Axure Prototype"], "missing": ["API規格、Jira／Confluence與法遵細節需追問"], "issue_ids": ["I01", "I02", "I03"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": ["能辨識資料風險及使用者中斷成本"], "issue_ids": []}, {"id": "outcome_quality", "rating": "足夠", "evidence": ["為觀察差異，非因果"], "missing": ["帳號冒用未再發生的監測來源待核對"], "issue_ids": ["I04"]}, {"id": "ownership", "rating": "強", "evidence": ["由我主責規劃，與工程團隊密切協作"], "missing": ["規劃、工程、QA與DBA責任邊界具體"], "issue_ids": []}, {"id": "readability", "rating": "足夠", "evidence": ["企業端招募系統全模組與求職端公司頁"], "missing": ["可優先呈現付款串接案例；不影響面試"], "issue_ids": []}], "results": [{"quote": "約 50 項大項功能上線", "kinds": ["output"]}, {"quote": "需求平均處理週期由 100.4 天降至 30.9 天", "kinds": ["outcome"]}, {"quote": "為觀察差異，非因果", "kinds": ["outcome"]}, {"quote": "選擇首次登入引導確認、不強迫修改", "kinds": ["decision"]}, {"quote": "兩案皆開發中", "kinds": ["in_progress"]}, {"quote": "Peach 網頁付款占營收由 24% 至 80% 以上", "kinds": ["outcome"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "application_note": "交付與串接相關，支持約談"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "企業流程可轉移，電支情境需適應"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我擬定取數的資料表與欄位"], "application_note": "本人與DBA分工具體"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "有流程結果，應追問口徑"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "有既有客戶風險取捨"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["從交友與訂閱制 App 到企業招募系統"], "application_note": "產品領域及責任變化清楚"}, {"rule_id": "HR07", "status": "supported", "resume_evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "application_note": "跨方合作有案例"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["從需求釐清、系統分析到 PRD、原型、UAT 與上線計畫"], "application_note": "主軸可辨識"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["依目前掌握的情況"], "application_note": "安全結果來源需核對"}, {"rule_id": "HR10", "status": "partial", "resume_evidence": ["接下來，我希望將更多心力放回產品策略"], "application_note": "確認對內部系統維運範圍的期待"}, {"rule_id": "HR11", "status": "unknown", "resume_evidence": ["錄取後三週可上班"], "application_note": "JD未列到職地點等細節，不猜衝突"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["整理為 PRD 與 Axure Prototype"], "application_note": "已有核心案例，未知可於面試核對"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "evidence_type": "context", "source_ids": [], "interview_question": "如何將招募系統經驗轉用於電支內部系統？"}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["客服反映配對名單「少又舊」"], "evidence_type": "decision", "source_ids": [], "interview_question": "如何確認排序規則是主要根因？"}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "evidence_type": "decision", "source_ids": [], "interview_question": "比較過哪些登入遷移方案？"}, {"rule_id": "HM04", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "evidence_type": "decision", "source_ids": [], "interview_question": "試算如何改變付款方案？"}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "partial", "resume_evidence": ["為觀察差異，非因果"], "evidence_type": "outcome", "source_ids": [], "interview_question": "安全事件未再發生依據哪些紀錄？"}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "evidence_type": "output", "source_ids": [], "interview_question": "串接時你與工程及合作方各決定什麼？"}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["第一階段於 2025/10 離峰切換上線"], "evidence_type": "output", "source_ids": [], "interview_question": "上線有哪些回滾與風險控制？"}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "partial", "resume_evidence": ["API 串接規劃、舊系統資料盤點"], "evidence_type": "context", "source_ids": [], "interview_question": "以實例說明API規格、重試、對帳及錯誤驗收。"}, {"rule_id": "HM09", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "evidence_type": "output", "source_ids": [], "interview_question": "自主決策邊界為何？"}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["近 10 年 PM 經驗，經手 6 款產品"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則"], "evidence_type": "decision", "source_ids": [], "interview_question": "哪個回饋使你改變原規則？"}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "evidence_type": "output", "source_ids": [], "interview_question": "可否用去識別規格展示串接深度？"}, {"rule_id": "HM13", "primary_dimension": "method", "status": "supported", "resume_evidence": ["為觀察差異，非因果"], "evidence_type": null, "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HR07", "source_ids": [], "application_note": "保留面試，以具體案例核對", "context_limit": "僅履歷文字自述，未外部驗證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "整理為 PRD 與 Axure Prototype", "reason": "Jira與Confluence沒有使用證據", "suggestion": "面試確認工具經驗與工作流轉換；未寫不等於不能。"}, {"id": "I02", "rule_id": "HM08", "source_ids": [], "application_note": "保留面試，以具體案例核對", "context_limit": "僅履歷文字自述，未外部驗證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "API 串接規劃、舊系統資料盤點", "reason": "串接經驗未展開到熟悉API規格的深度", "suggestion": "以付款串接的欄位、驗證、例外及驗收案例核對。"}, {"id": "I03", "rule_id": "HR01", "source_ids": [], "application_note": "保留面試，以具體案例核對", "context_limit": "僅履歷文字自述，未外部驗證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "工程、設計、QA、資料科學、客服、業務、法務與稽核協作", "reason": "法遵確認與內部訓練僅有協作或客服說明線索", "suggestion": "追問適法性如何落成規格，以及上線教育訓練範圍。"}, {"id": "I04", "rule_id": "HM05", "source_ids": [], "application_note": "保留面試，以具體案例核對", "context_limit": "僅履歷文字自述，未外部驗證", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "依目前掌握的情況", "reason": "未再冒用是有保留的自述，監測範圍未交代", "suggestion": "補已知資訊來源、覆蓋範圍與漏報限制，不改成零事故保證。"}], "decision": {"recommendation": "interview", "evidence": ["整理為 PRD 與 Axure Prototype", "並與 CodaPay 新加坡技術團隊協調串接"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["「整理為 PRD 與 Axure Prototype」支持需求至交付能力", "「並與 CodaPay 新加坡技術團隊協調串接」支持跨方整合", "「選擇首次登入引導確認、不強迫修改」具使用者與資料風險取捨"], "key_gaps": ["API規格深度與例外處理", "Jira／Confluence實務經驗", "法遵確認與內部教育訓練實例"], "strengths": ["1111交付｜「與 QA 制定 UAT 驗收案例、排定上線計畫」｜符合測試上線職責", "付款串接｜「並與 CodaPay 新加坡技術團隊協調串接」｜具合作方整合經驗", "改版決策｜「選擇首次登入引導確認、不強迫修改」｜顧及既有客戶與資料風險"], "interview_questions": ["請以CodaPay說明API欄位、驗證、重試、錯誤回應與對帳驗收。", "是否用過Jira及Confluence？如何對應現有工作流？", "如何與法遵確認適法性並轉成驗收條件？", "上線教育訓練由誰執行，你交付哪些材料？", "帳號冒用未再發生依據哪些通報或監測紀錄？", "登入改版如何比較替代方案、規劃回滾？", "對內部系統維運與策略工作的比例期待為何？"], "editorial_appendix": ["可將付款串接與內部流程案例提前，提高職缺關聯的可見性。"], "spectrum": {"level": 8, "uncertainty_levels": 1, "basis": "多個交付與付款串接案例，有清楚取捨、衡量限制及責任邊界；API規格與電支法遵仍需核對。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷 M｜第 1 輪｜model_id: unknown

### 1. 結論

- 招聘決定：interview

- Level：8（±1）

- 一句話理由：「整理為 PRD 與 Axure Prototype」及付款串接案例支持面試。

### 2. 六維度

| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |

| :-- | :-- | :-- | :-- |

| positioning | 足夠 | 現任 1111 招募系統 Product Owner | 內部流程與付款串接可轉移；策略期待與職務日常需確認 |

| role_evidence | 足夠 | 整理為 PRD 與 Axure Prototype | API規格、Jira／Confluence與法遵細節需追問 |

| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 能辨識資料風險及使用者中斷成本 |

| outcome_quality | 足夠 | 為觀察差異，非因果 | 帳號冒用未再發生的監測來源待核對 |

| ownership | 強 | 由我主責規劃，與工程團隊密切協作 | 規劃、工程、QA與DBA責任邊界具體 |

| readability | 足夠 | 企業端招募系統全模組與求職端公司頁 | 可優先呈現付款串接案例；不影響面試 |

### 3. JD 條件對照

| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |

| :-- | :-- | :-- | :-- | :-- |

| 3年以上相關工作經驗 | required | supported | 近 10 年 PM 經驗 | 年表支持超過三年；摘要經歷2年以上與必要條件3年以後者判讀。 |

| Axure產品規劃及Jira、Confluence專案管理 | required | partial | 整理為 PRD 與 Axure Prototype | Axure有實作；Jira、Confluence未呈現，須問工具轉換能力。 |

| 兼顧技術可行性及系統架構關連影響 | required | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 登入改版、舊資料與簽章驗證支持影響評估；架構細節面試確認。 |

| 熟悉API規格 | required | partial | 並與 CodaPay 新加坡技術團隊協調串接 | 具串接案例，規格欄位、錯誤碼及驗收深度未呈現。 |

| 有效團隊協作、跨部門溝通及同理心 | required | supported | 選擇首次登入引導確認、不強迫修改 | 工程QA客服合作及既有用戶登入限制具體。 |

| 需求分析、資料架構、畫面流程及規格文件 | required | supported | 以 Use Case、Wireframe 定義業務流程與畫面 | 系統分析、取數表欄位與PRD提供相關證據。 |

| 確認合作方需求與法遵適法性 | required | partial | 工程、設計、QA、資料科學、客服、業務、法務與稽核協作 | 合作方有案例；法務僅技能敘述，適法性確認過程未呈現。 |

| 時程、溝通、測試驗收及上線協調 | required | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 上線交付具體。 |

| 上線內部教育訓練 | required | partial | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 客服說明相關但未呈現完整教育訓練。 |

| 線上問題排除與依反饋持續迭代 | required | supported | 依客服測試回饋調整推薦規則 | 名單根因追查及安全事件處置支持。 |

| 代理收付、電子支付與行動支付領域 | preferred | partial | 導入 CodaPay，開放印尼、泰國等市場的電信帳單與超商付款 | 有支付經驗；台灣電子支付法規與銀行串接未呈現。 |

| 資管資工學歷或相關工作經驗 | preferred | supported | 釐清需求與系統分析後 | 國企學歷不符學科分支，但系統分析及串接支持替代工作經驗。 |

所有條件均未出現 contradicted；缺少工具名稱與規格細節不足以阻擋面試。

### 4. HR 十二問 ／ HM 十三問

| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |

| :-- | :-- | :-- | :-- |

| HR01 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 交付與串接相關，支持約談 |

| HR02 | supported | 企業端招募系統全模組與求職端公司頁 | 企業流程可轉移，電支情境需適應 |

| HR03 | supported | 由我擬定取數的資料表與欄位 | 本人與DBA分工具體 |

| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 有流程結果，應追問口徑 |

| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 有既有客戶風險取捨 |

| HR06 | supported | 從交友與訂閱制 App 到企業招募系統 | 產品領域及責任變化清楚 |

| HR07 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 跨方合作有案例 |

| HR08 | supported | 從需求釐清、系統分析到 PRD、原型、UAT 與上線計畫 | 主軸可辨識 |

| HR09 | partial | 依目前掌握的情況 | 安全結果來源需核對 |

| HR10 | partial | 接下來，我希望將更多心力放回產品策略 | 確認對內部系統維運範圍的期待 |

| HR11 | unknown | 錄取後三週可上班 | JD未列到職地點等細節，不猜衝突 |

| HR12 | supported | 整理為 PRD 與 Axure Prototype | 已有核心案例，未知可於面試核對 |

| HM01 | supported | 企業端招募系統全模組與求職端公司頁 | 企業流程及串接經驗可轉移 |

| HM02 | supported | 客服反映配對名單「少又舊」 | 有客服訊號與根因分析 |

| HM03 | supported | 選擇首次登入引導確認、不強迫修改 | 既有用戶風險取捨明確 |

| HM04 | supported | 依抽成、稅、手續費及撥款週期做實收試算 | 付款成本連結方案選擇 |

| HM05 | partial | 為觀察差異，非因果 | 監測來源仍待核對 |

| HM06 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 本人與協作對象界線清楚 |

| HM07 | supported | 第一階段於 2025/10 離峰切換上線 | 有規格驗收及分段交付 |

| HM08 | partial | API 串接規劃、舊系統資料盤點 | API規格深度留待面試 |

| HM09 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 支持自主協調交付範圍 |

| HM10 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 重點可辨識 |

| HM11 | supported | 依客服測試回饋調整推薦規則 | 回饋能帶動規則調整 |

| HM12 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 值得以串接樣本驗證 |

| HM13 | supported | 為觀察差異，非因果 | 獨立依本JD判讀，未作外部查證 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）

| # | 約談理由（引原句） |

| :-- | :-- |

| 1 | 「整理為 PRD 與 Axure Prototype」支持需求至交付能力 |

| 2 | 「並與 CodaPay 新加坡技術團隊協調串接」支持跨方整合 |

| 3 | 「選擇首次登入引導確認、不強迫修改」具使用者與資料風險取捨 |

| # | 關鍵缺口 | 面試追問 |

| :-- | :-- | :-- |

| 1 | API規格深度與例外處理 | 請以CodaPay說明API欄位、驗證、重試、錯誤回應與對帳驗收。 |

| 2 | Jira／Confluence實務經驗 | 是否用過Jira及Confluence？如何對應現有工作流？ |

| 3 | 法遵確認與內部教育訓練實例 | 如何與法遵確認適法性並轉成驗收條件？ |

其他追問：上線教育訓練由誰執行，你交付哪些材料？；帳號冒用未再發生依據哪些通報或監測紀錄？；登入改版如何比較替代方案、規劃回滾？；對內部系統維運與策略工作的比例期待為何？

### 6. 評語（給寫稿者的具體回饋）

**做得好（3 點）**：

- 1111交付｜「與 QA 制定 UAT 驗收案例、排定上線計畫」｜符合測試上線職責

- 付款串接｜「並與 CodaPay 新加坡技術團隊協調串接」｜具合作方整合經驗

- 改版決策｜「選擇首次登入引導確認、不強迫修改」｜顧及既有客戶與資料風險

**可改進（4 點）**：

- 位置：1111首項交付與技能工具

  - 原句：整理為 PRD 與 Axure Prototype

  - 問題類型：requirement

  - 嚴重度：interview_follow_up

  - 影響：Jira與Confluence沒有使用證據；不阻擋面試，需案例核對。

  - 建議方向：面試確認工具經驗與工作流轉換；未寫不等於不能。

- 位置：跨部門與整合技能／付款串接

  - 原句：API 串接規劃、舊系統資料盤點

  - 問題類型：requirement

  - 嚴重度：interview_follow_up

  - 影響：串接經驗未展開到熟悉API規格的深度；不阻擋面試，需案例核對。

  - 建議方向：以付款串接的欄位、驗證、例外及驗收案例核對。

- 位置：跨部門與整合技能／安全上線

  - 原句：工程、設計、QA、資料科學、客服、業務、法務與稽核協作

  - 問題類型：requirement

  - 嚴重度：interview_follow_up

  - 影響：法遵確認與內部訓練僅有協作或客服說明線索；不阻擋面試，需案例核對。

  - 建議方向：追問適法性如何落成規格，以及上線教育訓練範圍。

- 位置：1111登入安全條列

  - 原句：依目前掌握的情況

  - 問題類型：measurement

  - 嚴重度：interview_follow_up

  - 影響：未再冒用是有保留的自述，監測範圍未交代；不阻擋面試，需案例核對。

  - 建議方向：補已知資訊來源、覆蓋範圍與漏報限制，不改成零事故保證。

**編輯附件**（不影響判斷）：可將付款串接與內部流程案例提前，提高職缺關聯的可見性。

### 7. 資深能力分布

delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

具優先序與定價方向證據；不因近十年年資或團隊人數自動升等。

### 8. 未測試聲明

PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

履歷自述未經外部查證；同一缺口僅於主要維度計入。

### 成果分類補表

| 原句片段 | 分類 | 說明 |

| :-- | :-- | :-- |

| 全站活躍付費廠商約 6.6 萬家 | context | 系統規模，非個人績效 |

| 另於 2026/01–06 上線 111 項 Roadmap 細項 | output | 與50項不同粒度，不相加 |

| 盤點出上千組重複 E-mail | context | 資料遷移問題規模 |

| 停機約 1.5 小時 | output | 切換交付窗口，非用戶收益 |

| 與工程協作於 2026/04/17 上線簽章驗證 | output | 安全交付 |

| 上線後至 2026/10 未再出現同類帳號冒用 | outcome | 有保留自述，監測未查證 |

| 完成 1,726／1,857 張需求與問題單，約 93% | output | 工單完成量與比例 |

| 改依職缺上線日排序、20 天內不重複推薦 | decision / output | 規則調整，未給成效 |

| 需求管線觸及 1,279 家活躍付費廠商 | context | 觀察母體 |

| 該群年化留存 81.2%，同期全站 74.2% | outcome | 觀察差異，非因果 |

| AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才 | output | 功能交付 |

| 依客服測試回饋調整推薦規則 | decision | 回饋修正 |

| 降價期 iOS 非續訂營收較基準期增 5% | outcome | 有對照及期間，仍須核對其他干擾 |

| Android 減 18%，相對變化約多 28% | outcome | 同一實驗比較，非新增獨立成果 |

| 依結果全面調降售價 | decision | 採用實驗判斷 |

| KOOL 訂閱與付費牆規劃上線 | output | 跨端交付 |

| 上線後 6 週男性 DAU 約 3,200 至 1.25 萬 | outcome | 產品與行銷整體表現 |

| SweetRing 在地化涵蓋美國、墨西哥、巴西、印尼、馬來西亞、日本、韓國 | output | 七市場在地化 |

| 與最多約 10 位外國實習生協作 | context | 協作範圍非直屬帶人 |

| 導入 CodaPay | output | 支付方式整合 |

| 提出 7／30／90 天訂閱方案與加贈內容 | decision / output | 成本試算支持方案，未給結果 |

| Newegg.com 商品資訊英翻中與英文校對 | output | 翻譯交付 |

| 12 條分支、23 個共用 skill | output | 工具流程規模非效益 |

| TOEIC 980、TOEFL iBT 93 | context | 語言資格自述 |


## B-jd36｜揭盲：甲=K、乙=M；偏好=M

```json
{"job_id":"jd36","order":"甲=K/乙=M","differences":[{"what":"甲概述推薦功能與回饋調整；乙補充配對名單問題的根因、規則與限制。","hiring_meaning":"乙讓主管可驗證如何從客服問題定位排序根因、制定規則及衡量改善，對應線上問題排除與迭代；未提供改善成效，不視為已證明有效。","type":"capability"},{"what":"同一留存數據，甲呈現快照比較，乙交代欄位需求、DBA取數與試算表分析分工。","hiring_meaning":"乙更能界定候選人的資料工作責任，可追問表欄位選擇、口徑與年化算法；不推定自行寫SQL，也不將觀察差異當成因果。","type":"measurement"}],"preference":"乙","reason":"乙提供配對問題的根因與規則調整，以及取數分工，讓主管能追問線上問題診斷、迭代依據與資料架構理解；共同的串接、驗收經驗不重複加分，Jira／Confluence、API規格及法遵實作仍待驗證。","evidence_甲":["AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。與資料科學團隊合作，定義使用情境與驗收標準，依客服測試回饋調整推薦規則。","比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。"],"evidence_乙":["客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。","由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。"]}
```

## 版本比較｜jd36｜順序 甲=K 乙=M｜model_id: unknown
- 偏好：乙（揭盲：M）
| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 甲概述推薦功能與回饋調整；乙補充配對名單問題的根因、規則與限制。 | 乙讓主管可驗證如何從客服問題定位排序根因、制定規則及衡量改善，對應線上問題排除與迭代；未提供改善成效，不視為已證明有效。 | capability | AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。與資料科學團隊合作，定義使用情境與驗收標準，依客服測試回饋調整推薦規則。 | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 |
| 2 | 同一留存數據，甲呈現快照比較，乙交代欄位需求、DBA取數與試算表分析分工。 | 乙更能界定候選人的資料工作責任，可追問表欄位選擇、口徑與年化算法；不推定自行寫SQL，也不將觀察差異當成因果。 | measurement | 比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |
- 理由（≤120 字）：乙提供配對問題的根因與規則調整，以及取數分工，讓主管能追問線上問題診斷、迭代依據與資料架構理解；共同的串接、驗收經驗不重複加分，Jira／Confluence、API規格及法遵實作仍待驗證。


# jd40｜逐次輸出


## A-jd40-K｜履歷K

```json
{"rubric_version": "4.2", "resume_id": "K", "job_id": "jd40", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd40-K", "human_calibrated": false, "requirements": [{"id": "R01", "text": "5年以上軟體產品或技術專案管理經驗", "type": "required", "status": "supported", "evidence": ["近 10 年 PM 經驗，經手 6 款產品"], "blocks_interview": false, "reason": "任職時間與軟體產品案例支持。"}, {"id": "R02", "text": "需求探索、策略與Roadmap規劃", "type": "required", "status": "supported", "evidence": ["依使用者旅程與工單問題排定優先級"], "blocks_interview": false, "reason": "有需求訊號、排序與商業決策案例。"}, {"id": "R03", "text": "完整需求規劃至上線交付", "type": "required", "status": "supported", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "blocks_interview": false, "reason": "規格、驗收與上線鏈條清楚。"}, {"id": "R04", "text": "需求拆解、流程、PRD與驗收標準", "type": "required", "status": "supported", "evidence": ["以 Use Case、Wireframe 定義業務流程與畫面"], "blocks_interview": false, "reason": "文件連結具體交付用途。"}, {"id": "R05", "text": "理解API、資料流程、架構及系統串接", "type": "required", "status": "partial", "evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "blocks_interview": false, "reason": "有串接實務；API資料契約與架構取捨需追問。"}, {"id": "R06", "text": "優先順序、跨團隊溝通與風險管理", "type": "required", "status": "supported", "evidence": ["選擇首次登入引導確認、不強迫修改"], "blocks_interview": false, "reason": "有既有客戶登入風險與分階段上線案例。"}, {"id": "R07", "text": "專案範圍、里程碑、時程與需求變更管理", "type": "required", "status": "partial", "evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "blocks_interview": false, "reason": "範圍與時程明確；商業客戶變更及成本控制待問。"}, {"id": "R08", "text": "測試、驗收、上線後追蹤及產品迭代", "type": "required", "status": "supported", "evidence": ["依客服測試回饋調整推薦規則"], "blocks_interview": false, "reason": "有UAT、上線計畫與回饋迭代。"}, {"id": "R09", "text": "KA、客製化或NRE專案經驗", "type": "preferred", "status": "unknown", "evidence": [], "blocks_interview": false, "reason": "未見明確付費客製化或NRE範圍與驗收責任。"}, {"id": "R10", "text": "支付、餐飲、零售、SaaS或跨系統整合經驗", "type": "preferred", "status": "supported", "evidence": ["導入 CodaPay"], "blocks_interview": false, "reason": "支付與整合經驗符合列舉之一，餐飲不另設門檻。"}, {"id": "R11", "text": "基本SQL查詢或資料分析能力", "type": "preferred", "status": "supported", "evidence": ["以 Android 售價不變作對照"], "blocks_interview": false, "reason": "定價實驗與留存分析支持資料分析，未宣稱SQL。"}, {"id": "R12", "text": "客戶提案、需求協商或高階利害關係人溝通", "type": "preferred", "status": "partial", "evidence": ["直接向組織副總匯報"], "blocks_interview": false, "reason": "有高階匯報線索，協商與提案實例未詳。"}], "dimensions": [{"id": "positioning", "rating": "強", "evidence": ["現任 1111 招募系統 Product Owner"], "missing": ["餐飲及KA環境差異於面試確認。"], "issue_ids": []}, {"id": "role_evidence", "rating": "足夠", "evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "missing": ["API資料流程與客製交付深度待確認。"], "issue_ids": ["I01", "I02"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": ["定價替代方案與成本假設可追問。"], "issue_ids": []}, {"id": "outcome_quality", "rating": "足夠", "evidence": ["為觀察差異，非因果"], "missing": ["安全事件監測來源及年化留存口徑待核對。"], "issue_ids": ["I03", "I04"]}, {"id": "ownership", "rating": "強", "evidence": ["由我主責規劃，與工程團隊密切協作"], "missing": ["資源承諾與最終技術決策權可追問。"], "issue_ids": []}, {"id": "readability", "rating": "足夠", "evidence": ["2023/12–2026/03 主責約 50 項大項功能規劃"], "missing": ["大項與Roadmap細項口徑可更快辨識。"], "issue_ids": []}], "results": [{"quote": "約 50 項大項功能上線", "kinds": ["output"]}, {"quote": "停機約 1.5 小時", "kinds": ["output"]}, {"quote": "需求平均處理週期由 100.4 天降至 30.9 天", "kinds": ["outcome"]}, {"quote": "該群年化留存 81.2%，同期全站 74.2%", "kinds": ["outcome"]}, {"quote": "Peach 網頁付款占營收由 24% 至 80% 以上", "kinds": ["outcome"]}, {"quote": "我便將信件與即時通整合排在其他新功能之前", "kinds": ["decision", "in_progress"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "application_note": "支付與產品交付直接相關"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "企業系統經驗可轉移"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "application_note": "規劃與工程責任有區分"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "流程結果可支持約談"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "有客戶風險取捨"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["從交友與訂閱制 App 到企業招募系統"], "application_note": "脈絡與責任演變可辨"}, {"rule_id": "HR07", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "application_note": "文件技能有實務用途"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["近 10 年 PM 經驗，經手 6 款產品"], "application_note": "近期與相關案例易定位"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["依目前掌握的情況"], "application_note": "需確認監測與數據來源"}, {"rule_id": "HR10", "status": "supported", "resume_evidence": ["參與問題定義、方向選擇與成效判斷"], "application_note": "方向相容，確認交付投入意願"}, {"rule_id": "HR11", "status": "unknown", "resume_evidence": [], "application_note": "摘要未提供明確地點等限制"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "案例足以約談，技術深度留待驗證"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["訂閱制 B2C App 與雙邊媒合平台"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["廠商抱怨工單中，最大宗是溝通管道中斷"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM04", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "partial", "resume_evidence": ["該群年化留存 81.2%，同期全站 74.2%"], "evidence_type": "outcome", "source_ids": [], "interview_question": "如何年化、處理群體差異與追蹤期間？"}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "partial", "resume_evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "evidence_type": "output", "source_ids": [], "interview_question": "請說明支付API資料流、失敗重試及驗收責任。"}, {"rule_id": "HM09", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["近 10 年 PM 經驗，經手 6 款產品"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "evidence_type": "output", "source_ids": [], "interview_question": "請以一次串接專案走讀規格、決策與上線。"}, {"rule_id": "HM13", "primary_dimension": "method", "status": "supported", "resume_evidence": [], "evidence_type": null, "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HM08", "source_ids": [], "application_note": "技術深度留待面試核對", "context_limit": "僅依履歷文字，未外部查證。", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "並與 CodaPay 新加坡技術團隊協調串接", "reason": "有實務但尚不足辨識API及架構協作深度。", "suggestion": "補一個資料流、錯誤處理或技術替代方案案例。"}, {"id": "I02", "rule_id": "HM07", "source_ids": [], "application_note": "不阻擋，追問客製交付經驗", "context_limit": "僅依履歷文字，未外部查證。", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "統籌影響評估、範圍與時程、驗證流程及客服說明", "reason": "未呈現KA或NRE合約範圍、成本與變更協商；屬加分未知。", "suggestion": "如曾處理客製專案，補範圍變更與驗收界線。"}, {"id": "I03", "rule_id": "HM05", "source_ids": [], "application_note": "追問年化口徑，不當因果成效", "context_limit": "僅依履歷文字，未外部查證。", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "該群年化留存 81.2%，同期全站 74.2%", "reason": "短期快照如何年化、群體差異及樣本界定尚待釐清。", "suggestion": "保留非因果限制，補年化公式及納入條件。"}, {"id": "I04", "rule_id": "HR09", "source_ids": [], "application_note": "追問安全成效觀察來源", "context_limit": "僅依履歷文字，未外部查證。", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "依目前掌握的情況", "reason": "未再出現同類事件的觀察來源與涵蓋範圍不明。", "suggestion": "區分客服回報、事件紀錄與監測範圍。"}], "decision": {"recommendation": "interview", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫", "選擇首次登入引導確認、不強迫修改", "並與 CodaPay 新加坡技術團隊協調串接"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["「與 QA 制定 UAT 驗收案例、排定上線計畫」支持完整交付。", "「選擇首次登入引導確認、不強迫修改」呈現既有客戶風險判斷。", "「並與 CodaPay 新加坡技術團隊協調串接」對應支付整合。"], "key_gaps": ["API資料流程及架構方案協作深度。", "KA、NRE或客製變更、成本與驗收管理經驗。", "年化留存與安全事件追蹤口徑。"], "strengths": ["1111改版｜選擇首次登入引導確認、不強迫修改｜可轉移至既有商戶上線風險管理。", "1111交付｜與 QA 制定 UAT 驗收案例、排定上線計畫｜對應規格到驗收上線。", "尚凡付款｜並與 CodaPay 新加坡技術團隊協調串接｜直接關聯支付與跨系統協作。"], "interview_questions": ["請走讀支付API、資料流、異常處理與本人驗收範圍。", "有無KA或NRE客製專案？如何處理變更、成本及客戶承諾？", "年化留存的計算、群體定義與期間限制是什麼？", "安全事件未再發生的依據是客服回報或監測？", "如何配置工程資源、處理技術替代方案與時程衝突？", "如何平衡策略探索與持續交付責任？"], "editorial_appendix": ["可用一句註解區分50項大項與111項細項，不影響能力評價。"], "spectrum": {"level": 8, "uncertainty_levels": 1, "basis": "多個完整交付、支付整合與風險取捨案例，具期間與限制說明；API深度及KA客製交付仍待面試驗證。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷 K｜第 1 輪｜model_id: unknown

### 1. 結論

- 招聘決定：interview

- Level：8（±1）

- 一句話理由：「選擇首次登入引導確認、不強迫修改」呈現風險判斷，支付與交付案例支持面試。

### 2. 六維度

| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 現任 1111 招募系統 Product Owner | 餐飲及KA環境差異於面試確認。 |
| role_evidence | 足夠 | 並與 CodaPay 新加坡技術團隊協調串接 | API資料流程與客製交付深度待確認。 |
| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 定價替代方案與成本假設可追問。 |
| outcome_quality | 足夠 | 為觀察差異，非因果 | 安全事件監測來源及年化留存口徑待核對。 |
| ownership | 強 | 由我主責規劃，與工程團隊密切協作 | 資源承諾與最終技術決策權可追問。 |
| readability | 足夠 | 2023/12–2026/03 主責約 50 項大項功能規劃 | 大項與Roadmap細項口徑可更快辨識。 |
### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 5年以上軟體產品或技術專案管理經驗 | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 任職時間與軟體產品案例支持。 |
| 需求探索、策略與Roadmap規劃 | 必要 | supported | 依使用者旅程與工單問題排定優先級 | 有需求訊號、排序與商業決策案例。 |
| 完整需求規劃至上線交付 | 必要 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 規格、驗收與上線鏈條清楚。 |
| 需求拆解、流程、PRD與驗收標準 | 必要 | supported | 以 Use Case、Wireframe 定義業務流程與畫面 | 文件連結具體交付用途。 |
| 理解API、資料流程、架構及系統串接 | 必要 | partial | 並與 CodaPay 新加坡技術團隊協調串接 | 有串接實務；API資料契約與架構取捨需追問。 |
| 優先順序、跨團隊溝通與風險管理 | 必要 | supported | 選擇首次登入引導確認、不強迫修改 | 有既有客戶登入風險與分階段上線案例。 |
| 專案範圍、里程碑、時程與需求變更管理 | 必要 | partial | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 範圍與時程明確；商業客戶變更及成本控制待問。 |
| 測試、驗收、上線後追蹤及產品迭代 | 必要 | supported | 依客服測試回饋調整推薦規則 | 有UAT、上線計畫與回饋迭代。 |
| KA、客製化或NRE專案經驗 | 加分 | unknown | 未呈現 | 未見明確付費客製化或NRE範圍與驗收責任。 |
| 支付、餐飲、零售、SaaS或跨系統整合經驗 | 加分 | supported | 導入 CodaPay | 支付與整合經驗符合列舉之一，餐飲不另設門檻。 |
| 基本SQL查詢或資料分析能力 | 加分 | supported | 以 Android 售價不變作對照 | 定價實驗與留存分析支持資料分析，未宣稱SQL。 |
| 客戶提案、需求協商或高階利害關係人溝通 | 加分 | partial | 直接向組織副總匯報 | 有高階匯報線索，協商與提案實例未詳。 |
### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 支付與產品交付直接相關 |
| HR02 | supported | 企業端招募系統全模組與求職端公司頁 | 企業系統經驗可轉移 |
| HR03 | supported | 由我主責規劃，與工程團隊密切協作 | 規劃與工程責任有區分 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 流程結果可支持約談 |
| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 有客戶風險取捨 |
| HR06 | supported | 從交友與訂閱制 App 到企業招募系統 | 脈絡與責任演變可辨 |
| HR07 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 文件技能有實務用途 |
| HR08 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 近期與相關案例易定位 |
| HR09 | partial | 依目前掌握的情況 | 需確認監測與數據來源 |
| HR10 | supported | 參與問題定義、方向選擇與成效判斷 | 方向相容，確認交付投入意願 |
| HR11 | unknown | 未呈現 | 摘要未提供明確地點等限制 |
| HR12 | supported | 選擇首次登入引導確認、不強迫修改 | 案例足以約談，技術深度留待驗證 |
| HM01 | supported | 訂閱制 B2C App 與雙邊媒合平台 | 情境可轉移至產品兼技術專案 |
| HM02 | supported | 廠商抱怨工單中，最大宗是溝通管道中斷 | 工單訊號連到優先級 |
| HM03 | supported | 選擇首次登入引導確認、不強迫修改 | 顧及既有使用者風險 |
| HM04 | supported | 依抽成、稅、手續費及撥款週期做實收試算 | 支付實收試算支援商業判斷 |
| HM05 | partial | 該群年化留存 81.2%，同期全站 74.2% | 量測可追問，勿當因果 |
| HM06 | supported | 由我主責規劃，與工程團隊密切協作 | 本人與團隊分工可辨 |
| HM07 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 具備驗收與上線鏈條 |
| HM08 | partial | 並與 CodaPay 新加坡技術團隊協調串接 | 面試確認API與架構深度 |
| HM09 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 複雜系統協作支持資深範圍 |
| HM10 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 重點可辨，不按篇幅扣分 |
| HM11 | supported | 依客服測試回饋調整推薦規則 | 回饋確有改變規則 |
| HM12 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 約談可驗證技術與客製交付 |
| HM13 | supported | 方法層，不以履歷評分 | 依本JD獨立取證，未真人校準 |
### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「與 QA 制定 UAT 驗收案例、排定上線計畫」支持完整交付。 |
| 2 | 「選擇首次登入引導確認、不強迫修改」呈現既有客戶風險判斷。 |
| 3 | 「並與 CodaPay 新加坡技術團隊協調串接」對應支付整合。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | API資料流程及架構方案協作深度。 | 請走讀支付API、資料流、異常處理與本人驗收範圍。 |
| 2 | KA、NRE或客製變更、成本與驗收管理經驗。 | 有無KA或NRE客製專案？如何處理變更、成本及客戶承諾？ |
| 3 | 年化留存與安全事件追蹤口徑。 | 年化留存的計算、群體定義與期間限制是什麼？ |
### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**
- 1111改版｜選擇首次登入引導確認、不強迫修改｜可轉移至既有商戶上線風險管理。
- 1111交付｜與 QA 制定 UAT 驗收案例、排定上線計畫｜對應規格到驗收上線。
- 尚凡付款｜並與 CodaPay 新加坡技術團隊協調串接｜直接關聯支付與跨系統協作。

**可改進（4 點）**
- 位置：尚凡付款串接
  - 原句：並與 CodaPay 新加坡技術團隊協調串接
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：有實務但尚不足辨識API及架構協作深度。 技術深度留待面試核對
  - 建議方向：補一個資料流、錯誤處理或技術替代方案案例。
- 位置：1111登入安全交付
  - 原句：統籌影響評估、範圍與時程、驗證流程及客服說明
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：未呈現KA或NRE合約範圍、成本與變更協商；屬加分未知。 不阻擋，追問客製交付經驗
  - 建議方向：如曾處理客製專案，補範圍變更與驗收界線。
- 位置：1111留存比較
  - 原句：該群年化留存 81.2%，同期全站 74.2%
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：短期快照如何年化、群體差異及樣本界定尚待釐清。 追問年化口徑，不當因果成效
  - 建議方向：保留非因果限制，補年化公式及納入條件。
- 位置：1111安全成效
  - 原句：依目前掌握的情況
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：未再出現同類事件的觀察來源與涵蓋範圍不明。 追問安全成效觀察來源
  - 建議方向：區分客服回報、事件紀錄與監測範圍。

**編輯附件**（不影響判斷）
- 可用一句註解區分50項大項與111項細項，不影響能力評價。
### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠
方向與資源有優先級及商業決策支持；未將直屬匯報、團隊人數或年資當作自主資源配置證據。
### 8. 未測試聲明
PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run
本次僅依指定職缺摘要及履歷文字，未做外部查證；模型一致性不代表真人效度。
### 成果分類補表
| 原句／片段 | 分類 | 判讀限制 |
| :-- | :-- | :-- |
| 約 50 項大項功能上線 | output | JSON已列，依本文限制解讀 |
| 停機約 1.5 小時 | output | JSON已列，依本文限制解讀 |
| 需求平均處理週期由 100.4 天降至 30.9 天 | outcome | JSON已列，依本文限制解讀 |
| 該群年化留存 81.2%，同期全站 74.2% | outcome | JSON已列，依本文限制解讀 |
| Peach 網頁付款占營收由 24% 至 80% 以上 | outcome | JSON已列，依本文限制解讀 |
| 我便將信件與即時通整合排在其他新功能之前 | decision／in_progress | JSON已列，依本文限制解讀 |
| 全站活躍付費廠商約 6.6 萬家 | context | 系統規模非個人成果 |
| 對接 16 個需求單位 | context | 協作範圍 |
| 另於 2026/01–06 上線 111 項 Roadmap 細項 | output | 與50大項分開口徑 |
| 盤點出上千組重複 E-mail | output | 盤點產物與風險情境 |
| 選擇首次登入引導確認、不強迫修改 | decision | 已發生取捨 |
| 第一階段於 2025/10 離峰切換上線 | output | 已交付階段 |
| 與工程協作於 2026/04/17 上線簽章驗證 | output | 與工程協作非本人實作 |
| 上線後至 2026/10 未再出現同類帳號冒用 | outcome | 有限掌握情況，非監測證明 |
| 完成 1,726／1,857 張需求與問題單，約 93% | output | 結單量非使用者成果 |
| 需求管線觸及 1,279 家活躍付費廠商 | context | 群體涵蓋度非因果 |
| AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才 | output | 未呈現採用與品質結果 |
| 依客服測試回饋調整推薦規則 | decision | 回饋改變規則 |
| 降價期 iOS 非續訂營收較基準期增 5% | outcome | Android對照及期間具備，仍需確認可比性 |
| Android 減 18%，相對變化約多 28% | outcome | 相對變化非百分點 |
| 還原原價後 iOS 較基準期減 65% | outcome | 階段比較非隨機因果 |
| 依結果全面調降售價 | decision | 定價決策 |
| KOOL 訂閱與付費牆規劃上線 | output | 訂閱規則交付 |
| 才開放精選網紅資格 | decision | 設計資格門檻 |
| 主導 Juicy 上線 | output | 產品交付 |
| 男性 DAU 約 3,200 至 1.25 萬 | outcome | 產品與行銷期間整體表現 |
| SweetRing 在地化涵蓋美國、墨西哥、巴西、印尼、馬來西亞、日本、韓國 | output | 市場覆蓋非業績 |
| 與最多約 10 位外國實習生協作 | context | 無直屬管理關係 |
| 導入 CodaPay | output | 新增付款方式 |
| 依抽成、稅、手續費及撥款週期做實收試算 | decision | 商業方案依據 |
| 提出 7／30／90 天訂閱方案與加贈內容 | output | 提案非已實現營收 |
| Newegg.com 商品資訊英翻中與校對 | output | 較早期交付，非本職核心 |
| 目前專案仍在開發中 | in_progress | 溝通管道整合未視為已實現結果 |


## A-jd40-M｜履歷M

```json
{"rubric_version": "4.2", "resume_id": "M", "job_id": "jd40", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd40-M", "human_calibrated": false, "requirements": [{"id": "R01", "text": "5年以上軟體產品、技術產品或技術專案管理經驗", "type": "required", "status": "supported", "evidence": ["近 10 年 PM 經驗，經手 6 款產品"], "blocks_interview": false, "reason": "任職時間與軟體產品案例相互支持。"}, {"id": "R02", "text": "參與需求規劃至上線交付完整流程", "type": "required", "status": "supported", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "blocks_interview": false, "reason": "功能規劃、規格、測試與上線皆有案例。"}, {"id": "R03", "text": "理解API、資料流程與系統串接邏輯", "type": "required", "status": "partial", "evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "blocks_interview": false, "reason": "串接與資料欄位案例支持相關經驗；架構、API異常與資料一致性深度待驗證。"}, {"id": "R04", "text": "需求拆解、優先判斷、跨團隊溝通及風險管理", "type": "required", "status": "supported", "evidence": ["選擇首次登入引導確認、不強迫修改"], "blocks_interview": false, "reason": "改版風險、工單排序與跨職能交付均有明確動作。"}, {"id": "R05", "text": "探索需求、規劃維護Roadmap及產品策略", "type": "required", "status": "supported", "evidence": ["依使用者旅程排優先級"], "blocks_interview": false, "reason": "客服訊號、競品實測與取捨支撐；長期策略可面談。"}, {"id": "R06", "text": "產品需求、流程、驗收標準與PRD等文件", "type": "required", "status": "supported", "evidence": ["整理為 PRD 與 Axure Prototype"], "blocks_interview": false, "reason": "有連到業務流程、QA驗收及上線用途。"}, {"id": "R07", "text": "專案範圍、里程碑、時程及客戶期待與變更管理", "type": "required", "status": "partial", "evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "blocks_interview": false, "reason": "內部交付清楚；客戶變更與NRE合約範圍待問。"}, {"id": "R08", "text": "測試驗收、上線追蹤及成效迭代", "type": "required", "status": "supported", "evidence": ["依客服測試回饋調整推薦規則"], "blocks_interview": false, "reason": "UAT、分階段切換及後續數據比較均有線索。"}, {"id": "R09", "text": "KA客戶、客製化需求或NRE管理", "type": "preferred", "status": "unknown", "evidence": [], "blocks_interview": false, "reason": "未明示KA或NRE案例，屬加分條件，不阻擋面試。"}, {"id": "R10", "text": "支付、餐飲、零售、SaaS或跨系統整合經驗", "type": "preferred", "status": "supported", "evidence": ["導入 CodaPay"], "blocks_interview": false, "reason": "支付及第三方整合符合其中選項，不要求餐飲全命中。"}, {"id": "R11", "text": "基本SQL查詢或資料分析能力", "type": "preferred", "status": "supported", "evidence": ["再以 Google Sheet 比對"], "blocks_interview": false, "reason": "具資料分析與對照實驗；未聲稱SQL實作。"}, {"id": "R12", "text": "客戶提案、需求協商或高階利害關係人溝通", "type": "preferred", "status": "partial", "evidence": ["直接向組織副總匯報"], "blocks_interview": false, "reason": "具高階匯報情境，但具體協商決策案例仍待問。"}], "dimensions": [{"id": "positioning", "rating": "強", "evidence": ["現任 1111 招募系統 Product Owner"], "missing": ["餐飲情境可到職學習；確認策略與交付期待。"], "issue_ids": []}, {"id": "role_evidence", "rating": "足夠", "evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "missing": ["API架構及KA/NRE交付深度待驗證。"], "issue_ids": ["I01", "I02"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": ["長期Roadmap資源配置可面談補充。"], "issue_ids": []}, {"id": "outcome_quality", "rating": "足夠", "evidence": ["為觀察差異，非因果"], "missing": ["安全監測口徑、留存年化與實驗偏差待核對。"], "issue_ids": ["I03"]}, {"id": "ownership", "rating": "強", "evidence": ["由我主責規劃，與工程團隊密切協作"], "missing": ["高階協商與客戶變更的授權邊界可追問。"], "issue_ids": []}, {"id": "readability", "rating": "足夠", "evidence": ["訂閱制 B2C App 與雙邊媒合平台。"], "missing": ["摘要及自傳有重複，宜優先突出支付整合。"], "issue_ids": []}], "results": [{"quote": "約 50 項大項功能上線", "kinds": ["output"]}, {"quote": "停機約 1.5 小時", "kinds": ["output"]}, {"quote": "需求平均處理週期由 100.4 天降至 30.9 天", "kinds": ["outcome"]}, {"quote": "兩案皆開發中", "kinds": ["in_progress"]}, {"quote": "該群年化留存 81.2%，同期全站 74.2%", "kinds": ["outcome"]}, {"quote": "降價期 iOS 非續訂營收較基準期增 5%", "kinds": ["outcome"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "application_note": "支付整合與全流程經驗支持約談"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "近期企業流程經驗可轉移"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "application_note": "規劃與工程責任分開"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "有流程改變；核對統計口徑"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "能以既有客戶風險做取捨"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["從交友與訂閱制 App 到企業招募系統"], "application_note": "職涯領域及責任演變可辨識"}, {"rule_id": "HR07", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "application_note": "協作技能有實際用途"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["資深產品經理｜Senior Product Manager"], "application_note": "定位及案例容易定位"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["依目前掌握的情況"], "application_note": "安全結果仍需查監測範圍"}, {"rule_id": "HR10", "status": "supported", "resume_evidence": ["我希望將更多心力放回產品策略"], "application_note": "方向相容；核對交付工作比重"}, {"rule_id": "HR11", "status": "unknown", "resume_evidence": ["錄取後三週可上班"], "application_note": "JD未列工作地點等衝突條件"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["導入 CodaPay"], "application_note": "建議以技術整合案例面試"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["訂閱制 B2C App 與雙邊媒合平台。"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["客服反映配對名單「少又舊」"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["改版排在新功能職缺健檢之前"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM04", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "partial", "resume_evidence": ["為觀察差異，非因果"], "evidence_type": "outcome", "source_ids": [], "interview_question": null}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["與資料科學團隊合作，定義使用情境與驗收標準"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["第一階段於 2025/10 離峰切換上線"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "partial", "resume_evidence": ["API 串接規劃、舊系統資料盤點"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM09", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["現任 1111 招募系統 Product Owner"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["導入 CodaPay"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM13", "primary_dimension": "", "status": "not_applicable", "resume_evidence": [], "evidence_type": null, "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HM08", "source_ids": [], "application_note": "保留約談；以具體案例核對", "context_limit": "僅履歷文字自述，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "API 串接規劃、舊系統資料盤點", "reason": "整合經驗有線索，但TPM需要的API失敗處理與資料流細節未展開；面試驗證而非否定。", "suggestion": "以CodaPay案例補充資料流、異常重試、驗收與本人權責。"}, {"id": "I02", "rule_id": "HM07", "source_ids": [], "application_note": "保留約談；以具體案例核對", "context_limit": "僅履歷文字自述，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "掌握驗收與交付時程。", "reason": "內部交付證據充分，KA/NRE的客戶承諾與需求變更經驗未知，屬面試追問。", "suggestion": "如確有案例，說明客戶範圍協商、變更及時程管理；沒有則保留未知。"}, {"id": "I03", "rule_id": "HM05", "source_ids": [], "application_note": "保留約談；以具體案例核對", "context_limit": "僅履歷文字自述，未外部查證", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "依目前掌握的情況", "reason": "未再冒用屬有限觀察；年化留存及實驗差異也需核對方法，不能直接推為因果。", "suggestion": "面試核對安全監測來源、留存年化算法、付款營收分母及實驗干擾。"}], "decision": {"recommendation": "interview", "evidence": ["導入 CodaPay", "選擇首次登入引導確認、不強迫修改", "與 QA 制定 UAT 驗收案例、排定上線計畫"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["「導入 CodaPay」直接相關支付與第三方整合。", "「選擇首次登入引導確認、不強迫修改」呈現交付風險取捨。", "「與 QA 制定 UAT 驗收案例、排定上線計畫」支持完整交付。"], "key_gaps": ["API架構與異常處理細節", "KA/NRE客戶變更與商務承諾", "安全監測與數據口徑"], "strengths": ["支付經歷｜「導入 CodaPay」｜直接對應支付服務與整合。", "招募改版｜「選擇首次登入引導確認、不強迫修改」｜具既有客戶風險取捨。", "招募交付｜「與 QA 制定 UAT 驗收案例、排定上線計畫」｜具測試到上線責任。"], "interview_questions": ["請用CodaPay畫出API與資料流，說明失敗重試、對帳、驗收及本人決策。", "是否做過KA或NRE？如何處理客戶需求變更、成本與時程衝突？", "安全事件的監測來源、涵蓋範圍與未再發生的判定方式為何？", "留存年化如何計算？兩個群體的差異與選樣偏差如何處理？", "定價實驗有何季節、平台及同期行銷干擾？付款占比提升是否伴隨總營收變化？", "Roadmap如何在商務、客戶與技術債間配置資源，高階分歧如何解決？"], "editorial_appendix": ["可將付款整合案例前移，自傳重複的改版敘事適度縮短；不影響能力判斷。"], "spectrum": {"level": 8, "uncertainty_levels": 1, "basis": "多個相關交付與支付案例，有明確取捨及比較口徑限制；技術架構和KA/NRE仍待面試。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷 M｜第 1 輪｜model_id: unknown

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「導入 CodaPay」與完整上線、風險取捨案例支持面試，技術深度待驗證。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 現任 1111 招募系統 Product Owner | 餐飲情境可到職學習；確認策略與交付期待。 |
| role_evidence | 足夠 | 並與 CodaPay 新加坡技術團隊協調串接 | API架構及KA/NRE交付深度待驗證。 |
| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 長期Roadmap資源配置可面談補充。 |
| outcome_quality | 足夠 | 為觀察差異，非因果 | 安全監測口徑、留存年化與實驗偏差待核對。 |
| ownership | 強 | 由我主責規劃，與工程團隊密切協作 | 高階協商與客戶變更的授權邊界可追問。 |
| readability | 足夠 | 訂閱制 B2C App 與雙邊媒合平台。 | 摘要及自傳有重複，宜優先突出支付整合。 |

### 3. JD 條件對照
必要標籤包含主要職責，並非每項皆為招聘硬門檻；無已證實不符的必要條件。
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 5年以上軟體產品、技術產品或技術專案管理經驗 | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 任職時間與軟體產品案例相互支持。 |
| 參與需求規劃至上線交付完整流程 | 必要 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 功能規劃、規格、測試與上線皆有案例。 |
| 理解API、資料流程與系統串接邏輯 | 必要 | partial | 並與 CodaPay 新加坡技術團隊協調串接 | 串接與資料欄位案例支持相關經驗；架構、API異常與資料一致性深度待驗證。 |
| 需求拆解、優先判斷、跨團隊溝通及風險管理 | 必要 | supported | 選擇首次登入引導確認、不強迫修改 | 改版風險、工單排序與跨職能交付均有明確動作。 |
| 探索需求、規劃維護Roadmap及產品策略 | 必要 | supported | 依使用者旅程排優先級 | 客服訊號、競品實測與取捨支撐；長期策略可面談。 |
| 產品需求、流程、驗收標準與PRD等文件 | 必要 | supported | 整理為 PRD 與 Axure Prototype | 有連到業務流程、QA驗收及上線用途。 |
| 專案範圍、里程碑、時程及客戶期待與變更管理 | 必要 | partial | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 內部交付清楚；客戶變更與NRE合約範圍待問。 |
| 測試驗收、上線追蹤及成效迭代 | 必要 | supported | 依客服測試回饋調整推薦規則 | UAT、分階段切換及後續數據比較均有線索。 |
| KA客戶、客製化需求或NRE管理 | 加分 | unknown | 未呈現 | 未明示KA或NRE案例，屬加分條件，不阻擋面試。 |
| 支付、餐飲、零售、SaaS或跨系統整合經驗 | 加分 | supported | 導入 CodaPay | 支付及第三方整合符合其中選項，不要求餐飲全命中。 |
| 基本SQL查詢或資料分析能力 | 加分 | supported | 再以 Google Sheet 比對 | 具資料分析與對照實驗；未聲稱SQL實作。 |
| 客戶提案、需求協商或高階利害關係人溝通 | 加分 | partial | 直接向組織副總匯報 | 具高階匯報情境，但具體協商決策案例仍待問。 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 支付整合與全流程經驗支持約談 |
| HR02 | supported | 企業端招募系統全模組與求職端公司頁 | 近期企業流程經驗可轉移 |
| HR03 | supported | 由我主責規劃，與工程團隊密切協作 | 規劃與工程責任分開 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 有流程改變；核對統計口徑 |
| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 能以既有客戶風險做取捨 |
| HR06 | supported | 從交友與訂閱制 App 到企業招募系統 | 職涯領域及責任演變可辨識 |
| HR07 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 協作技能有實際用途 |
| HR08 | supported | 資深產品經理｜Senior Product Manager | 定位及案例容易定位 |
| HR09 | partial | 依目前掌握的情況 | 安全結果仍需查監測範圍 |
| HR10 | supported | 我希望將更多心力放回產品策略 | 方向相容；核對交付工作比重 |
| HR11 | unknown | 錄取後三週可上班 | JD未列工作地點等衝突條件 |
| HR12 | supported | 導入 CodaPay | 建議以技術整合案例面試 |
| HM01 | supported | 訂閱制 B2C App 與雙邊媒合平台。 | 支付與企業產品可轉移 |
| HM02 | supported | 客服反映配對名單「少又舊」 | 問題根因改變設計 |
| HM03 | supported | 改版排在新功能職缺健檢之前 | 已做排序；專案仍開發中 |
| HM04 | supported | 依抽成、稅、手續費及撥款週期做實收試算 | 商業成本支持方案選擇 |
| HM05 | partial | 為觀察差異，非因果 | 限制清楚；口徑待核對 |
| HM06 | supported | 與資料科學團隊合作，定義使用情境與驗收標準 | 本人定義與團隊合作可辨識 |
| HM07 | supported | 第一階段於 2025/10 離峰切換上線 | 既有客戶及上線風險具案例 |
| HM08 | partial | API 串接規劃、舊系統資料盤點 | 需用整合案例確認技術深度 |
| HM09 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 支持資深IC與跨團隊責任 |
| HM10 | supported | 現任 1111 招募系統 Product Owner | 代表經驗與本人動作可辨識 |
| HM11 | supported | 依客服測試回饋調整推薦規則 | 具依回饋修正做法證據 |
| HM12 | supported | 導入 CodaPay | 值得透過技術工作樣本驗證 |
| HM13 | not_applicable | 不適用 | 方法檢核；不當成候選人能力 |
HM13：本次先依本JD獨立審查；未用姓名、公司名氣、學歷或文風作能力代理。未做真人校準。

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「導入 CodaPay」直接相關支付與第三方整合。 |
| 2 | 「選擇首次登入引導確認、不強迫修改」呈現交付風險取捨。 |
| 3 | 「與 QA 制定 UAT 驗收案例、排定上線計畫」支持完整交付。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | API架構與異常處理細節 | 請用CodaPay畫出API與資料流，說明失敗重試、對帳、驗收及本人決策。 |
| 2 | KA/NRE客戶變更與商務承諾 | 是否做過KA或NRE？如何處理客戶需求變更、成本與時程衝突？ |
| 3 | 安全監測與數據口徑 | 安全事件的監測來源、涵蓋範圍與未再發生的判定方式為何？ |

其餘面試追問：
- 留存年化如何計算？兩個群體的差異與選樣偏差如何處理？
- 定價實驗有何季節、平台及同期行銷干擾？付款占比提升是否伴隨總營收變化？
- Roadmap如何在商務、客戶與技術債間配置資源，高階分歧如何解決？

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 支付經歷｜「導入 CodaPay」｜直接對應支付服務與整合。
- 招募改版｜「選擇首次登入引導確認、不強迫修改」｜具既有客戶風險取捨。
- 招募交付｜「與 QA 制定 UAT 驗收案例、排定上線計畫」｜具測試到上線責任。

**可改進（3 點）**：

- 位置：專業技能／跨部門與整合
- 原句：API 串接規劃、舊系統資料盤點
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：整合經驗有線索，但TPM需要的API失敗處理與資料流細節未展開；面試驗證而非否定。
- 建議方向：以CodaPay案例補充資料流、異常重試、驗收與本人權責。

- 位置：專業摘要／交付時程
- 原句：掌握驗收與交付時程。
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：內部交付證據充分，KA/NRE的客戶承諾與需求變更經驗未知，屬面試追問。
- 建議方向：如確有案例，說明客戶範圍協商、變更及時程管理；沒有則保留未知。

- 位置：登入安全與數據成果
- 原句：依目前掌握的情況
- 問題類型：measurement
- 嚴重度：interview_follow_up
- 影響：未再冒用屬有限觀察；年化留存及實驗差異也需核對方法，不能直接推為因果。
- 建議方向：面試核對安全監測來源、留存年化算法、付款營收分母及實驗干擾。

**編輯附件**（不影響判斷）：
- 可將付款整合案例前移，自傳重複的改版敘事適度縮短；不影響能力判斷。

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠
方向與資源評等依優先排序、定價及分階段決策；未推定預算或人事管理能力。

### 8. 未測試聲明
PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run
所有成果為履歷自述，非外部查證；本次只有一次獨立審查，不跨職缺平均。

### 成果分類補表
| 原句片段 | 分類 | 解讀與限制 |
| :-- | :-- | :-- |
| 全站活躍付費廠商約 6.6 萬家 | context | 系統規模，非個人新增客戶 |
| 對接 16 個需求單位 | context | 協作範圍，非成效 |
| 近 10 年 PM 經驗，經手 6 款產品 | context | 職涯背景 |
| 約 50 項大項功能上線 | output | 交付數量，非使用者成效 |
| 另於 2026/01–06 上線 111 項 Roadmap 細項 | output | 不同粒度與期間，不與50直接相加 |
| 上千組重複 E-mail | context | 資料風險範圍 |
| 選擇首次登入引導確認、不強迫修改 | decision | 降低既有客戶登入阻力 |
| 停機約 1.5 小時 | output | 切換紀錄，未提供目標比較 |
| 十多家廠商帳號遭冒用 | context | 安全事件背景 |
| 於 2026/04/17 上線簽章驗證 | output | 安全交付 |
| 上線後至 2026/10 未再出現同類帳號冒用 | outcome | 有限觀察，監測完整性待核對 |
| 需求平均處理週期由 100.4 天降至 30.9 天 | outcome | Q1/Q2流程結果，案件組成待核對 |
| 完成 1,726／1,857 張需求與問題單 | output | 有分母與截止日，非業務成果 |
| 兩案皆開發中 | decision、in_progress | 排序已決定，未計已完成成效 |
| 改依職缺上線日排序、20 天內不重複推薦 | decision、output | 規則調整，成效未呈現 |
| 需求管線觸及 1,279 家活躍付費廠商 | context | 分析群體範圍 |
| 該群年化留存 81.2%，同期全站 74.2% | outcome | 觀察差異非因果，年化公式待問 |
| AI 功能已上線公司簡介生成 | output | 另含職缺說明與推薦人才上線，未報採用成效 |
| 依客服測試回饋調整推薦規則 | decision | 依回饋修正 |
| 降價期 iOS 非續訂營收較基準期增 5% | outcome | Android減18%、相對約多28%；非隨機因果結論 |
| 還原原價後 iOS 較基準期減 65% | outcome | 實驗第三階段結果 |
| 依結果全面調降售價 | decision | 商業選擇 |
| Peach 網頁付款占營收由 24% 至 80% 以上 | outcome | 付款渠道占比，非總營收成長 |
| 並與 CodaPay 新加坡技術團隊協調串接 | output | 整合交付，架構深度待驗證 |
| KOOL 訂閱與付費牆規劃上線 | output | 跨平台變現功能 |
| 才開放精選網紅資格 | decision | 資格門檻規則 |
| 上線後 6 週男性 DAU 約 3,200 至 1.25 萬 | outcome | Juicy產品與行銷整體表現 |
| SweetRing 在地化涵蓋 | output | 七市場在地化範圍 |
| 與最多約 10 位外國實習生協作 | context | 非直屬管理人數 |
| 導入 CodaPay | output | 新增支付途徑 |
| 提出 7／30／90 天訂閱方案與加贈內容 | decision、output | 實收試算支持方案，未列業績 |
| 商品資訊英翻中與英文校對 | output | 翻譯工作產出 |
| 12 條分支、23 個共用 skill | output | 協作流程產物，未量測效率 |


## B-jd40｜揭盲：甲=M、乙=K；偏好=M

```json
{"job_id":"jd40","order":"甲=M/乙=K","differences":[{"what":"甲補出配對排序根因、競品反推與規則調整；乙僅列競品實測技能。","hiring_meaning":"可追問甲如何由客服問題轉成規則、如何驗收成效，對應需求探索與產品迭代；仍須驗證實際效果。","type":"capability"},{"what":"甲交代取數資料表、欄位、DBA及Google Sheet分工；乙只呈現快照比較結果。","hiring_meaning":"甲使資料分析參與範圍更可驗證，可追問資料定義與比較方法；不能據此認定具備SQL實作。","type":"measurement"},{"what":"甲補充安全事件的個資風險脈絡，乙已有相同協調與上線事實。","hiring_meaning":"甲更易定位風險判斷追問，但不增加已證明的交付能力；兩者皆須追問API架構、KA與NRE經驗。","type":"readability"}],"preference":"甲","reason":"甲提供配對規則決策與取數分工的具體證據，較能安排需求拆解、競品分析及成效追蹤的面試驗證；安全脈絡僅提升可讀性。共同交付與支付經驗不重複加分，API深度及KA／NRE仍待確認。","evidence_甲":["客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。","由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。","求才端可存取大量求職者個資，冒用登入即有外洩風險。"],"evidence_乙":["研究與數據：使用者訪談與問卷、競品實測、GA4、世代分析、對照組實驗、Excel","比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。","登入安全盤點源於 2026/04 十多家廠商帳號遭冒用。"]}
```

## 版本比較｜jd40｜順序 甲=M 乙=K｜model_id: unknown
- 偏好：甲（揭盲：M）
| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 甲補出配對排序根因、競品反推與規則調整；乙僅列競品實測技能。 | 可追問甲如何由客服問題轉成規則、如何驗收成效，對應需求探索與產品迭代；仍須驗證實際效果。 | capability | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 | 研究與數據：使用者訪談與問卷、競品實測、GA4、世代分析、對照組實驗、Excel |
| 2 | 甲交代取數資料表、欄位、DBA及Google Sheet分工；乙只呈現快照比較結果。 | 甲使資料分析參與範圍更可驗證，可追問資料定義與比較方法；不能據此認定具備SQL實作。 | measurement | 由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |
| 3 | 甲補充安全事件的個資風險脈絡，乙已有相同協調與上線事實。 | 甲更易定位風險判斷追問，但不增加已證明的交付能力；兩者皆須追問API架構、KA與NRE經驗。 | readability | 求才端可存取大量求職者個資，冒用登入即有外洩風險。 | 登入安全盤點源於 2026/04 十多家廠商帳號遭冒用。 |
- 理由（≤120 字）：甲提供配對規則決策與取數分工的具體證據，較能安排需求拆解、競品分析及成效追蹤的面試驗證；安全脈絡僅提升可讀性。共同交付與支付經驗不重複加分，API深度及KA／NRE仍待確認。


# jd43｜逐次輸出


## A-jd43-K｜履歷K

```json
{"rubric_version": "4.2", "resume_id": "K", "job_id": "jd43", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd43-K", "human_calibrated": false, "requirements": [{"id": "R01", "text": "5年以上網路或科技產業產品管理或相關經驗", "type": "required", "status": "supported", "evidence": ["近 10 年 PM 經驗，經手 6 款產品"], "blocks_interview": false, "reason": "2016年至今的產品工作具體列示。"}, {"id": "R02", "text": "產品策略、PRD、與總部共同規劃路線圖及優先級", "type": "required", "status": "partial", "evidence": ["依使用者旅程與工單問題排定優先級"], "blocks_interview": false, "reason": "有在地化與PRD案例，總部共同決策及策略權責待問。"}, {"id": "R03", "text": "使用者研究、競品分析與假設驗證", "type": "required", "status": "partial", "evidence": ["研究與數據：使用者訪談與問卷、競品實測"], "blocks_interview": false, "reason": "有工單訊號及定價實驗；訪談與競品如何改變方案未展開。"}, {"id": "R04", "text": "跨職能、跨國團隊協作與利害關係人管理", "type": "required", "status": "supported", "evidence": ["並與 CodaPay 新加坡技術團隊協調串接。"], "blocks_interview": false, "reason": "工程、QA、客服及海外串接均有具體情境。"}, {"id": "R05", "text": "數位產品從概念、需求至上線及後續優化", "type": "required", "status": "supported", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫。"], "blocks_interview": false, "reason": "功能、分階段切換與回饋調整均有案例。"}, {"id": "R06", "text": "分析、解決問題、溝通能力", "type": "required", "status": "supported", "evidence": ["選擇首次登入引導確認、不強迫修改"], "blocks_interview": false, "reason": "將資料風險轉為分階段流程選擇，並協調交付。"}, {"id": "R07", "text": "定義監控KPI、行為分析及A/B測試等量化決策", "type": "required", "status": "partial", "evidence": ["以 Android 售價不變作對照"], "blocks_interview": false, "reason": "有對照與期間，但非隨機A/B；核心安全指標監測待驗證。"}, {"id": "R08", "text": "熟悉Confluence、Jira、Figma、Codex等工具", "type": "required", "status": "partial", "evidence": ["從 User Story、Wireframe 到 Figma／Axure 原型"], "blocks_interview": false, "reason": "Figma有案例，其他列名工具未呈現；Claude Code不等同Codex。"}, {"id": "R09", "text": "英文流利", "type": "required", "status": "partial", "evidence": ["英文 TOEIC 980、TOEFL iBT 93"], "blocks_interview": false, "reason": "分數與跨國協作支持英文基礎，流利商務討論待面試驗證。"}, {"id": "R10", "text": "帳號安全、防詐與訊息體驗相關專案職責", "type": "required", "status": "partial", "evidence": ["與工程協作於 2026/04/17 上線簽章驗證。"], "blocks_interview": false, "reason": "帳號安全直接相關；防詐與OA未見，訊息整合仍開發中。"}, {"id": "R11", "text": "AI產品開發或AI整合經驗", "type": "preferred", "status": "supported", "evidence": ["AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。"], "blocks_interview": false, "reason": "有使用情境、驗收及資料科學協作。"}, {"id": "R12", "text": "日文或韓文能力", "type": "preferred", "status": "unknown", "evidence": [], "blocks_interview": false, "reason": "未提供日韓語能力，非必要條件。"}], "dimensions": [{"id": "positioning", "rating": "強", "evidence": ["涵蓋訂閱制社交 App、網紅媒合及企業招募系統。"], "missing": ["區域總部產品共決範圍待問"], "issue_ids": []}, {"id": "role_evidence", "rating": "足夠", "evidence": ["與工程協作於 2026/04/17 上線簽章驗證。"], "missing": ["總部合作、指定工具及英文流利度待驗證"], "issue_ids": ["I01", "I02"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": ["使用者研究如何改變策略待追問"], "issue_ids": ["I03"]}, {"id": "outcome_quality", "rating": "足夠", "evidence": ["為觀察差異，非因果。"], "missing": ["安全事件監測與實驗可比性仍待核對"], "issue_ids": ["I04", "I05"]}, {"id": "ownership", "rating": "強", "evidence": ["由我主責規劃，與工程團隊密切協作"], "missing": ["最終核准與資源調配權責待問"], "issue_ids": []}, {"id": "readability", "rating": "足夠", "evidence": ["正式職稱產品企劃主任"], "missing": ["可將安全與訊息案例提前，屬編輯建議"], "issue_ids": []}], "results": [{"quote": "約 50 項大項功能上線", "kinds": ["output"]}, {"quote": "上線後至 2026/10 未再出現同類帳號冒用。", "kinds": ["outcome"]}, {"quote": "需求平均處理週期由 100.4 天降至 30.9 天", "kinds": ["outcome"]}, {"quote": "該群年化留存 81.2%，同期全站 74.2%", "kinds": ["outcome"]}, {"quote": "相對變化約多 28%", "kinds": ["outcome"]}, {"quote": "目前專案仍在開發中。", "kinds": ["in_progress"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["與工程協作於 2026/04/17 上線簽章驗證。"], "application_note": "帳號安全與交付直接相關"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "近期範圍明確，客群差異可轉移"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "application_note": "規劃與工程責任有區分"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "有流程改變，口徑需核對"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "呈現風險與使用者取捨"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["從交友與訂閱制 App 到企業招募系統"], "application_note": "領域與責任演變清楚"}, {"rule_id": "HR07", "status": "supported", "resume_evidence": ["並與 CodaPay 新加坡技術團隊協調串接。"], "application_note": "技能連結實際跨國情境"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["現任 1111 招募系統 Product Owner"], "application_note": "主要定位容易辨識"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["依目前掌握的情況"], "application_note": "安全觀察來源須面試核對"}, {"rule_id": "HR10", "status": "supported", "resume_evidence": ["我希望將更多心力放回產品策略"], "application_note": "與策略及規劃方向相容"}, {"rule_id": "HR11", "status": "unknown", "resume_evidence": [], "application_note": "JD未列完整工作條件，無已知衝突"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "application_note": "多個相關案例足以面試"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["涵蓋訂閱制社交 App、網紅媒合及企業招募系統。"], "evidence_type": "context", "source_ids": [], "interview_question": "如何將B2B安全經驗轉移至Messenger與OA？"}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["最大宗是溝通管道中斷"], "evidence_type": "decision", "source_ids": [], "interview_question": "哪些工單或研究改變了原先方案？"}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "evidence_type": "decision", "source_ids": [], "interview_question": "考慮過哪些替代方案與安全風險？"}, {"rule_id": "HM04", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "evidence_type": "decision", "source_ids": [], "interview_question": "如何把市場商業機會變成路線圖？"}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "partial", "resume_evidence": ["為觀察差異，非因果。"], "evidence_type": "outcome", "source_ids": [], "interview_question": "安全事件如何偵測，定價實驗如何排除混淆？"}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫。"], "evidence_type": "output", "source_ids": [], "interview_question": "對總部或跨部門分歧如何形成決議？"}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["第一階段於 2025/10 離峰切換上線"], "evidence_type": "output", "source_ids": [], "interview_question": "上線回復方案與驗收門檻是什麼？"}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["釐清需求與系統分析後"], "evidence_type": "output", "source_ids": [], "interview_question": "簽章驗證的限制、替代方案與驗收如何討論？"}, {"rule_id": "HM09", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "evidence_type": "context", "source_ids": [], "interview_question": "哪些方向與資源決策由你最終負責？"}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["正式職稱產品企劃主任"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則。"], "evidence_type": "decision", "source_ids": [], "interview_question": "哪次回饋改變規則，如何確認改善？"}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。"], "evidence_type": "output", "source_ids": [], "interview_question": "可否用安全專案工作樣本核對規劃與驗收？"}, {"rule_id": "HM13", "primary_dimension": "", "status": "supported", "resume_evidence": ["為觀察差異，非因果。"], "evidence_type": null, "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HM06", "source_ids": [], "application_note": "總部共決能力待核對", "context_limit": "僅依履歷文字，未外部查證。", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "並與 CodaPay 新加坡技術團隊協調串接。", "reason": "有跨國合作，但不足確認與總部產品團隊共同排定路線圖的能力；值得面試追問。", "suggestion": "補一個跨國產品優先級分歧、本人權責及決議過程。"}, {"id": "I02", "rule_id": "HR07", "source_ids": [], "application_note": "英文與工具可在面試驗證", "context_limit": "僅依履歷文字，未外部查證。", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "英文 TOEIC 980、TOEFL iBT 93", "reason": "語言分數及海外合作有支持，但流利度與指定工具熟悉度仍不完整；不阻擋面試。", "suggestion": "面試用英文討論案例，核對Jira、Confluence與Codex實際使用。"}, {"id": "I03", "rule_id": "HM02", "source_ids": [], "application_note": "研究如何改變決策待補", "context_limit": "僅依履歷文字，未外部查證。", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "研究與數據：使用者訪談與問卷、競品實測", "reason": "方法清單未顯示研究樣本、洞察及改變的方案；追問研究對產品策略的影響。", "suggestion": "選一個研究案例說明對象、洞察與決策改變。"}, {"id": "I04", "rule_id": "HM05", "source_ids": [], "application_note": "安全成效需核對監測範圍", "context_limit": "僅依履歷文字，未外部查證。", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "依目前掌握的情況", "reason": "未再出現冒用屬有限觀察，未載偵測覆蓋與事件定義；需追問不能視為零事故證明。", "suggestion": "說明客服回報或監測來源、期間、同類事件定義及盲區。"}, {"id": "I05", "rule_id": "HM05", "source_ids": [], "application_note": "定價結果不直接等同因果", "context_limit": "僅依履歷文字，未外部查證。", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "以 Android 售價不變作對照", "reason": "跨平台、先後時段實驗仍可能受流量與促銷混淆；追問可比性而非否定決策。", "suggestion": "說明樣本、非續訂口徑、同期活動及採用決策限制。"}], "decision": {"recommendation": "interview", "evidence": ["與工程協作於 2026/04/17 上線簽章驗證。", "選擇首次登入引導確認、不強迫修改"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["帳號安全案例直接對應本職責", "跨國整合及社交App經驗可轉移", "具體取捨與上線交付支持面試"], "key_gaps": ["總部路線圖共決、工具及英文實務待核對", "研究洞察如何改變策略待展開", "安全監測與定價實驗可比性待驗證"], "strengths": ["安全專案範圍與跨部門責任清楚", "既有使用者登入風險與取捨具體", "衡量期間與觀察限制明確標示"], "interview_questions": ["總部產品團隊與在地需求衝突時，你如何共同排定優先級？", "請用英文說明安全專案，並介紹指定工具的使用情境。", "哪個訪談或競品發現改變了方案？", "未再冒用的偵測來源、覆蓋、事件定義為何？", "定價實驗各期流量、活動與樣本是否可比？", "簽章驗證有哪些替代方案與上線風險？", "工單週期如何計算，案件難度與結案標準是否一致？", "哪些資源與方向由你決定，哪些需主管或合作團隊核准？"], "editorial_appendix": ["可將帳號安全與訊息整合案例提前；後者保留開發中狀態。"], "spectrum": {"level": 8, "uncertainty_levels": 1, "basis": "多案例支持面試，具明確取捨、期間、比較與限制；安全監測及總部協作尚待驗證，非聘用能力保證。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷K｜第 1 輪｜model_id: unknown

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「選擇首次登入引導確認、不強迫修改」呈現安全與使用者取捨，多個交付案例支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 涵蓋訂閱制社交 App、網紅媒合及企業招募系統。 | 區域總部產品共決範圍待問；面試核對，不推論沒有能力 |
| role_evidence | 足夠 | 與工程協作於 2026/04/17 上線簽章驗證。 | 總部合作、指定工具及英文流利度待驗證；面試核對，不推論沒有能力 |
| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 使用者研究如何改變策略待追問；面試核對，不推論沒有能力 |
| outcome_quality | 足夠 | 為觀察差異，非因果。 | 安全事件監測與實驗可比性仍待核對；面試核對，不推論沒有能力 |
| ownership | 強 | 由我主責規劃，與工程團隊密切協作 | 最終核准與資源調配權責待問；面試核對，不推論沒有能力 |
| readability | 足夠 | 正式職稱產品企劃主任 | 可將安全與訊息案例提前，屬編輯建議；面試核對，不推論沒有能力 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| R01 5年以上網路或科技產業產品管理或相關經驗 | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 2016年至今的產品工作具體列示。 不阻擋面試。 |
| R02 產品策略、PRD、與總部共同規劃路線圖及優先級 | 必要 | partial | 依使用者旅程與工單問題排定優先級 | 有在地化與PRD案例，總部共同決策及策略權責待問。 不阻擋面試。 |
| R03 使用者研究、競品分析與假設驗證 | 必要 | partial | 研究與數據：使用者訪談與問卷、競品實測 | 有工單訊號及定價實驗；訪談與競品如何改變方案未展開。 不阻擋面試。 |
| R04 跨職能、跨國團隊協作與利害關係人管理 | 必要 | supported | 並與 CodaPay 新加坡技術團隊協調串接。 | 工程、QA、客服及海外串接均有具體情境。 不阻擋面試。 |
| R05 數位產品從概念、需求至上線及後續優化 | 必要 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫。 | 功能、分階段切換與回饋調整均有案例。 不阻擋面試。 |
| R06 分析、解決問題、溝通能力 | 必要 | supported | 選擇首次登入引導確認、不強迫修改 | 將資料風險轉為分階段流程選擇，並協調交付。 不阻擋面試。 |
| R07 定義監控KPI、行為分析及A/B測試等量化決策 | 必要 | partial | 以 Android 售價不變作對照 | 有對照與期間，但非隨機A/B；核心安全指標監測待驗證。 不阻擋面試。 |
| R08 熟悉Confluence、Jira、Figma、Codex等工具 | 必要 | partial | 從 User Story、Wireframe 到 Figma／Axure 原型 | Figma有案例，其他列名工具未呈現；Claude Code不等同Codex。 不阻擋面試。 |
| R09 英文流利 | 必要 | partial | 英文 TOEIC 980、TOEFL iBT 93 | 分數與跨國協作支持英文基礎，流利商務討論待面試驗證。 不阻擋面試。 |
| R10 帳號安全、防詐與訊息體驗相關專案職責 | 必要 | partial | 與工程協作於 2026/04/17 上線簽章驗證。 | 帳號安全直接相關；防詐與OA未見，訊息整合仍開發中。 不阻擋面試。 |
| R11 AI產品開發或AI整合經驗 | 加分 | supported | AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。 | 有使用情境、驗收及資料科學協作。 不阻擋面試。 |
| R12 日文或韓文能力 | 加分 | unknown | 未呈現 | 未提供日韓語能力，非必要條件。 不阻擋面試。 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 與工程協作於 2026/04/17 上線簽章驗證。 | 帳號安全與交付直接相關 |
| HR02 | supported | 企業端招募系統全模組與求職端公司頁 | 近期範圍明確，客群差異可轉移 |
| HR03 | supported | 由我主責規劃，與工程團隊密切協作 | 規劃與工程責任有區分 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 有流程改變，口徑需核對 |
| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 呈現風險與使用者取捨 |
| HR06 | supported | 從交友與訂閱制 App 到企業招募系統 | 領域與責任演變清楚 |
| HR07 | supported | 並與 CodaPay 新加坡技術團隊協調串接。 | 技能連結實際跨國情境 |
| HR08 | supported | 現任 1111 招募系統 Product Owner | 主要定位容易辨識 |
| HR09 | partial | 依目前掌握的情況 | 安全觀察來源須面試核對 |
| HR10 | supported | 我希望將更多心力放回產品策略 | 與策略及規劃方向相容 |
| HR11 | unknown | 未呈現 | JD未列完整工作條件，無已知衝突 |
| HR12 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 多個相關案例足以面試 |
| HM01 | supported | 涵蓋訂閱制社交 App、網紅媒合及企業招募系統。 | 情境可轉移，OA直接經驗待問 |
| HM02 | supported | 最大宗是溝通管道中斷 | 工單提供具體問題訊號 |
| HM03 | supported | 選擇首次登入引導確認、不強迫修改 | 取捨清楚，可驗證替代方案 |
| HM04 | supported | 依抽成、稅、手續費及撥款週期做實收試算 | 商業計算連結產品選擇 |
| HM05 | partial | 為觀察差異，非因果。 | 量測限制列入面試核對 |
| HM06 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫。 | 個人責任與協作清楚 |
| HM07 | supported | 第一階段於 2025/10 離峰切換上線 | 規格驗收與切換支持交付 |
| HM08 | supported | 釐清需求與系統分析後 | 可驗證技術方案討論深度 |
| HM09 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 符合資深IC線索，非管理職推定 |
| HM10 | supported | 正式職稱產品企劃主任 | 資訊可辨識，編排可微調 |
| HM11 | supported | 依客服測試回饋調整推薦規則。 | 回饋改變推薦規則 |
| HM12 | supported | AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。 | 安全與AI案例值得約談 |
| HM13 | supported | 為觀察差異，非因果。 | 依本JD獨立判讀，未真人校準 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「統籌影響評估、範圍與時程、驗證流程及客服說明」直接對應安全專案 |
| 2 | 「並與 CodaPay 新加坡技術團隊協調串接。」支持跨國合作 |
| 3 | 「選擇首次登入引導確認、不強迫修改」呈現產品取捨 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 總部路線圖共決、工具及英文實務待核對 | 如何與總部共決路線圖？可用英文演示工具與案例？ |
| 2 | 研究洞察如何改變策略待展開 | 哪次研究改變了原定方案？ |
| 3 | 安全監測與定價實驗可比性待驗證 | 安全監測覆蓋及定價對照可比性為何？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111安全專案｜「統籌影響評估、範圍與時程、驗證流程及客服說明」｜責任範圍對應安全產品的跨職能推動。
- 1111改版｜「選擇首次登入引導確認、不強迫修改」｜說清楚限制下的選擇，可驗證使用者理解。
- 1111留存｜「為觀察差異，非因果。」｜避免把相關性當產品影響，支持審慎判讀。

**可改進（5 點）**：

- 位置：尚凡網頁付款
- 原句：並與 CodaPay 新加坡技術團隊協調串接。
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：有跨國合作，但不足確認與總部產品團隊共同排定路線圖的能力；值得面試追問。
- 建議方向：補一個跨國產品優先級分歧、本人權責及決議過程。

- 位置：專業技能語言與工具
- 原句：英文 TOEIC 980、TOEFL iBT 93
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：語言分數及海外合作有支持，但流利度與指定工具熟悉度仍不完整；不阻擋面試。
- 建議方向：面試用英文討論案例，核對Jira、Confluence與Codex實際使用。

- 位置：專業技能研究與數據
- 原句：研究與數據：使用者訪談與問卷、競品實測
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：方法清單未顯示研究樣本、洞察及改變的方案；追問研究對產品策略的影響。
- 建議方向：選一個研究案例說明對象、洞察與決策改變。

- 位置：1111登入安全
- 原句：依目前掌握的情況
- 問題類型：measurement
- 嚴重度：interview_follow_up
- 影響：未再出現冒用屬有限觀察，未載偵測覆蓋與事件定義；需追問不能視為零事故證明。
- 建議方向：說明客服回報或監測來源、期間、同類事件定義及盲區。

- 位置：尚凡定價實驗
- 原句：以 Android 售價不變作對照
- 問題類型：measurement
- 嚴重度：interview_follow_up
- 影響：跨平台、先後時段實驗仍可能受流量與促銷混淆；追問可比性而非否定決策。
- 建議方向：說明樣本、非續訂口徑、同期活動及採用決策限制。

**編輯附件**（不影響判斷）：安全案例可提前；訊息整合保留開發中狀態。

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠
方向能力由優先級與定價決策支持；資源最終核准權限仍待問，不推定有完整P&L或直屬管理權。

### 8. 未測試聲明
PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run
僅依指定JD摘要與履歷自述，未外部查證；Level不加總、不加權，不是錄取率或百分位。

### 成果分類補表
| 成果或數字原句 | 分類 | 限制 |
| :-- | :-- | :-- |
| 對接 16 個需求單位 | context | 協作範圍，非影響 |
| 近 10 年 PM 經驗，經手 6 款產品 | context | 年資及範圍，非直接加分 |
| 全站活躍付費廠商約 6.6 萬家 | context | 系統規模，非本人獲客 |
| 團隊 3 名企劃 | context | 不推定直屬管理 |
| 約 50 項大項功能上線 | output | 交付數量 |
| 上線 111 項 Roadmap 細項 | output | 不同粒度，不與50項相加 |
| 盤點出上千組重複 E-mail | output / context | 資料發現 |
| 選擇首次登入引導確認、不強迫修改 | decision | 已發生取捨 |
| 停機約 1.5 小時 | output | 上線運作紀錄自述 |
| 十多家廠商帳號遭冒用 | context | 安全事件背景 |
| 上線簽章驗證 | output | 功能交付 |
| 上線後至 2026/10 未再出現同類帳號冒用。 | outcome | 有限掌握情況，非零事故證明 |
| 需求平均處理週期由 100.4 天降至 30.9 天 | outcome | 流程結果，需核對案件組成 |
| 完成 1,726／1,857 張需求與問題單，約 93% | output | 截至09/29結案 |
| 需求管線觸及 1,279 家活躍付費廠商 | context | 接觸母體 |
| 約占全站 66,150 家的 1.9% | context | 基準日04/30 |
| 該群年化留存 81.2%，同期全站 74.2% | outcome | 觀察差異，非因果 |
| AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。 | output | 未提供採用或品質結果 |
| 依客服測試回饋調整推薦規則。 | decision / output | 回饋調整，未提供改善量 |
| 降價期 iOS 非續訂營收較基準期增 5% | outcome | 跨期對照非隨機實驗 |
| Android 減 18%，相對變化約多 28% | outcome | 相對比值變化非百分點 |
| 還原原價後 iOS 較基準期減 65% | outcome | 跨期比較 |
| 依結果全面調降售價 | decision | 已採取產品決定 |
| Peach 網頁付款占營收由 24% 至 80% 以上 | outcome | 收入組成，不代表總收入增加 |
| KOOL 訂閱與付費牆規劃上線 | output | 跨平台交付 |
| 才開放精選網紅資格 | decision | 資格門檻設計 |
| 主導 Juicy 上線 | output | 交付 |
| 上線後 6 週男性 DAU 約 3,200 至 1.25 萬 | outcome | 產品及行銷整體表現 |
| 日本、韓國 7 個市場 | context | 在地化範圍 |
| 與最多約 10 位外國實習生協作 | context | 無直屬管理 |
| 導入 CodaPay | output | 支付整合 |
| 提出 7／30／90 天訂閱方案與加贈內容。 | output / decision | 實收試算後提案，未載收入成效 |
| Newegg.com 商品資訊英翻中與校對。 | output | 語言工作線索 |
| 將信件與即時通整合排在其他新功能之前 | decision | 工單訊號形成優先級 |
| 目前專案仍在開發中。 | in_progress | 不能列已交付結果 |


## A-jd43-M｜履歷M

```json
{"rubric_version": "4.2", "resume_id": "M", "job_id": "jd43", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd43-M", "human_calibrated": false, "requirements": [{"id": "R01", "text": "5年以上網路或科技業產品或相關經驗", "type": "required", "status": "supported", "evidence": ["近 10 年 PM 經驗，經手 6 款產品"], "blocks_interview": false, "reason": "2016年至今產品相關任職可支持年資。"}, {"id": "R02", "text": "數位產品從概念到上線及優化", "type": "required", "status": "supported", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "blocks_interview": false, "reason": "規格、驗收、分階段切換與上線後調整均有案例。"}, {"id": "R03", "text": "產品策略、PRD與總部共塑路線圖", "type": "required", "status": "partial", "evidence": ["信件與即時通整合排在其他新功能之前"], "blocks_interview": false, "reason": "有PRD與取捨；總部共同制定區域路線圖及權責尚待確認。"}, {"id": "R04", "text": "使用者研究、競品分析與假設驗證", "type": "required", "status": "partial", "evidence": ["實測主要競品反推規則後"], "blocks_interview": false, "reason": "客服訊號、競品實測、對照實驗具體；訪談問卷僅技能自述。"}, {"id": "R05", "text": "跨職能及跨國團隊合作", "type": "required", "status": "supported", "evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "blocks_interview": false, "reason": "有工程、QA、客服、資料科學與海外技術團隊合作。"}, {"id": "R06", "text": "分析、解題、溝通及利害關係人管理", "type": "required", "status": "supported", "evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "blocks_interview": false, "reason": "帳號冒用處理、需求優先級及實驗分析有具體行動。"}, {"id": "R07", "text": "定義監控KPI與數據驅動決策", "type": "required", "status": "partial", "evidence": ["以 Android 售價不變作對照"], "blocks_interview": false, "reason": "定價實驗支持分析；產品KPI持續監控與警戒規則不清。"}, {"id": "R08", "text": "熟悉Confluence、Jira、Figma、Codex", "type": "required", "status": "partial", "evidence": ["工具與技術素養：Figma、Axure RP"], "blocks_interview": false, "reason": "Figma有案例；Confluence、Jira、Codex未呈現，Claude Code非同一工具。"}, {"id": "R09", "text": "英文流利", "type": "required", "status": "supported", "evidence": ["以英文分派 UI/UX 翻譯與多國粉專經營任務"], "blocks_interview": false, "reason": "實際工作英文與檢定提供面試支持；可用英文驗證協商能力。"}, {"id": "R10", "text": "AI產品開發或整合", "type": "preferred", "status": "supported", "evidence": ["與資料科學團隊合作，定義使用情境與驗收標準"], "blocks_interview": false, "reason": "生成與推薦功能已上線，角色清楚。"}, {"id": "R11", "text": "日文或韓文能力", "type": "preferred", "status": "unknown", "evidence": [], "blocks_interview": false, "reason": "多國在地化不等於本人具日韓語能力；加分未知不阻擋。"}], "dimensions": [{"id": "positioning", "rating": "強", "evidence": ["涵蓋訂閱制社交 App、網紅媒合及企業招募系統"], "missing": [], "issue_ids": []}, {"id": "role_evidence", "rating": "足夠", "evidence": ["與工程協作於 2026/04/17 上線簽章驗證"], "missing": ["總部協作權責、指定工具與研究方法深度待確認"], "issue_ids": ["I01", "I03"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": [], "issue_ids": []}, {"id": "outcome_quality", "rating": "足夠", "evidence": ["為觀察差異，非因果"], "missing": ["安全結果監測口徑、定價對照可比性需確認"], "issue_ids": ["I02"]}, {"id": "ownership", "rating": "強", "evidence": ["由我主責規劃，與工程團隊密切協作"], "missing": [], "issue_ids": []}, {"id": "readability", "rating": "足夠", "evidence": ["現任 1111 招募系統 Product Owner"], "missing": ["安全案例可提前，摘要與自傳可去重"], "issue_ids": ["I04"]}], "results": [{"quote": "全站活躍付費廠商約 6.6 萬家", "kinds": ["context"]}, {"quote": "約 50 項大項功能上線", "kinds": ["output"]}, {"quote": "選擇首次登入引導確認、不強迫修改", "kinds": ["decision"]}, {"quote": "上線後至 2026/10 未再出現同類帳號冒用", "kinds": ["outcome"]}, {"quote": "為觀察差異，非因果", "kinds": ["outcome"]}, {"quote": "信件與即時通整合排在其他新功能之前", "kinds": ["decision", "in_progress"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["與工程協作於 2026/04/17 上線簽章驗證"], "application_note": "安全與社交產品案例對應職務"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "近期B2B系統經驗可轉用帳號安全"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "application_note": "規劃驗收與工程實作邊界清楚"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "流程改變可追問口徑"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "有使用者風險與切換取捨"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["從交友與訂閱制 App 到企業招募系統"], "application_note": "領域轉換與責任脈絡清楚"}, {"rule_id": "HR07", "status": "supported", "resume_evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "application_note": "有跨國合作實例"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["現任 1111 招募系統 Product Owner"], "application_note": "定位與代表案例可找到"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["依目前掌握的情況"], "application_note": "安全觀察不等同完整監測"}, {"rule_id": "HR10", "status": "supported", "resume_evidence": ["接下來，我希望將更多心力放回產品策略"], "application_note": "方向與策略規劃職責相容"}, {"rule_id": "HR11", "status": "partial", "resume_evidence": ["台北市、新北市，可接受遠端或混合辦公"], "application_note": "未見已知衝突；實際條件待確認"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["定義使用情境與驗收標準"], "application_note": "多個案例支持邀約並追問缺口"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["訂閱制 B2C App 與雙邊媒合平台"], "evidence_type": "context", "source_ids": [], "interview_question": "如何把社交App與企業安全經驗轉用Messenger與OA？"}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["客服反映配對名單「少又舊」"], "evidence_type": "decision", "source_ids": [], "interview_question": "客服訊號如何經研究驗證為主要痛點？"}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "evidence_type": "decision", "source_ids": [], "interview_question": "比較過哪些登入改版方案與風險？"}, {"rule_id": "HM04", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "evidence_type": "decision", "source_ids": [], "interview_question": "商業收益如何與安全摩擦及使用者體驗取捨？"}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "partial", "resume_evidence": ["為觀察差異，非因果"], "evidence_type": "outcome", "source_ids": [], "interview_question": "如何監測冒用事件與控制定價實驗混淆？"}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["與資料科學團隊合作，定義使用情境與驗收標準"], "evidence_type": "output", "source_ids": [], "interview_question": "與資安法務或海外團隊有分歧時如何決策？"}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "evidence_type": "output", "source_ids": [], "interview_question": "安全上線的驗收、回退及客服準備如何安排？"}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["改依職缺上線日排序、20 天內不重複推薦"], "evidence_type": "decision", "source_ids": [], "interview_question": "簽章驗證有哪些限制與工程替代方案？"}, {"rule_id": "HM09", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "evidence_type": "output", "source_ids": [], "interview_question": "區域產品方向決策與資源協調的自主範圍？"}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["現任 1111 招募系統 Product Owner"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則"], "evidence_type": "decision", "source_ids": [], "interview_question": "哪次反證改變方案，後來如何沿用？"}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["與工程協作於 2026/04/17 上線簽章驗證"], "evidence_type": "output", "source_ids": [], "interview_question": "以安全專案及跨國協作工作樣本確認能力。"}, {"rule_id": "HM13", "primary_dimension": "method", "status": "supported", "resume_evidence": ["為觀察差異，非因果"], "evidence_type": null, "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HM06", "source_ids": [], "application_note": "總部協作權責待確認", "context_limit": "僅依履歷文字，未外部查證", "category": "ownership", "severity": "interview_follow_up", "block_target": null, "claim": "並與 CodaPay 新加坡技術團隊協調串接", "reason": "海外串接不完全等同與總部共同塑造路線圖；不阻擋面試，需核對協商範圍。", "suggestion": "補一例跨國優先級分歧、本人決策權與解法。"}, {"id": "I02", "rule_id": "HM05", "source_ids": [], "application_note": "安全結果口徑待核對", "context_limit": "僅依履歷文字，未外部查證", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "依目前掌握的情況", "reason": "未再冒用是有限觀察；缺事件定義、覆蓋率與監測來源，需面試核對而非否定。", "suggestion": "說明監測來源與盲區；定價實驗另確認樣本及同期混淆。"}, {"id": "I03", "rule_id": "HR07", "source_ids": [], "application_note": "工具與研究方法需驗證", "context_limit": "僅依履歷文字，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "研究與數據：使用者訪談與問卷", "reason": "訪談問卷缺具體應用；指定工具部分未呈現，屬可於面試釐清之缺口。", "suggestion": "有實際經驗才補研究如何改變決策及指定工具用途。"}, {"id": "I04", "rule_id": "HR08", "source_ids": [], "application_note": "安全案例可更早呈現", "context_limit": "僅依履歷文字，未外部查證", "category": "readability", "severity": "editorial", "block_target": null, "claim": "近 10 年 PM 經驗，經手 6 款產品", "reason": "摘要未優先呈現最相關安全專案，自傳部分重複；僅影響資訊可見性。", "suggestion": "提前安全案例並縮減重複敘述，不升格為能力差異。"}], "decision": {"recommendation": "interview", "evidence": ["與工程協作於 2026/04/17 上線簽章驗證", "並與 CodaPay 新加坡技術團隊協調串接"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["安全與登入專案直接相關：「上線簽章驗證」。", "跨國協作具體：「與 CodaPay 新加坡技術團隊協調串接」。", "有取捨：「選擇首次登入引導確認、不強迫修改」。"], "key_gaps": ["總部共同規劃路線圖與決策權責", "安全監測與實驗可比性口徑", "指定工具與訪談問卷實際運用"], "strengths": ["安全專案｜「上線簽章驗證」｜與職缺帳號安全主題直接相關。", "改版｜「選擇首次登入引導確認、不強迫修改」｜呈現使用者摩擦與切換風險取捨。", "跨國付款｜「與 CodaPay 新加坡技術團隊協調串接」｜支持跨國技術溝通。"], "interview_questions": ["請拆解安全專案的決策權責、資安法務協作、驗收與回退。", "未再冒用的資料來源、事件定義、監測覆蓋與盲區是什麼？", "跨國合作如何處理優先級分歧？與總部共塑路線圖的經驗？", "請說明定價實驗的樣本、季節因素及對照可比性。", "哪次訪談或問卷改變產品決策？", "Confluence、Jira、Codex的實際使用情況？", "用英文說明一次跨國技術協商與取捨。"], "editorial_appendix": ["依本職缺將安全專案提前；自傳保留新增判斷，刪減重複。"], "spectrum": {"level": 8, "uncertainty_levels": 1, "basis": "多個相關案例含安全交付、使用者風險取捨及比較衡量限制；總部權責與監控仍須面試驗證。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷 M｜第 1 輪｜model_id: unknown

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「上線簽章驗證」與跨國協作、使用者取捨支持面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 涵蓋訂閱制社交 App、網紅媒合及企業招募系統 | 證據足以支持面試；細節面試核對 |
| role_evidence | 足夠 | 與工程協作於 2026/04/17 上線簽章驗證 | 總部協作權責、指定工具與研究方法深度待確認 |
| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 證據足以支持面試；細節面試核對 |
| outcome_quality | 足夠 | 為觀察差異，非因果 | 安全結果監測口徑、定價對照可比性需確認 |
| ownership | 強 | 由我主責規劃，與工程團隊密切協作 | 證據足以支持面試；細節面試核對 |
| readability | 足夠 | 現任 1111 招募系統 Product Owner | 安全案例可提前，摘要與自傳可去重 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 5年以上網路或科技業產品或相關經驗 | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 2016年至今產品相關任職可支持年資。 |
| 數位產品從概念到上線及優化 | 必要 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 規格、驗收、分階段切換與上線後調整均有案例。 |
| 產品策略、PRD與總部共塑路線圖 | 必要 | partial | 信件與即時通整合排在其他新功能之前 | 有PRD與取捨；總部共同制定區域路線圖及權責尚待確認。 |
| 使用者研究、競品分析與假設驗證 | 必要 | partial | 實測主要競品反推規則後 | 客服訊號、競品實測、對照實驗具體；訪談問卷僅技能自述。 |
| 跨職能及跨國團隊合作 | 必要 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 有工程、QA、客服、資料科學與海外技術團隊合作。 |
| 分析、解題、溝通及利害關係人管理 | 必要 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 帳號冒用處理、需求優先級及實驗分析有具體行動。 |
| 定義監控KPI與數據驅動決策 | 必要 | partial | 以 Android 售價不變作對照 | 定價實驗支持分析；產品KPI持續監控與警戒規則不清。 |
| 熟悉Confluence、Jira、Figma、Codex | 必要 | partial | 工具與技術素養：Figma、Axure RP | Figma有案例；Confluence、Jira、Codex未呈現，Claude Code非同一工具。 |
| 英文流利 | 必要 | supported | 以英文分派 UI/UX 翻譯與多國粉專經營任務 | 實際工作英文與檢定提供面試支持；可用英文驗證協商能力。 |
| AI產品開發或整合 | 加分 | supported | 與資料科學團隊合作，定義使用情境與驗收標準 | 生成與推薦功能已上線，角色清楚。 |
| 日文或韓文能力 | 加分 | unknown | 未呈現 | 多國在地化不等於本人具日韓語能力；加分未知不阻擋。 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 與工程協作於 2026/04/17 上線簽章驗證 | 安全與社交產品案例對應職務 |
| HR02 | supported | 企業端招募系統全模組與求職端公司頁 | 近期B2B系統經驗可轉用帳號安全 |
| HR03 | supported | 由我主責規劃，與工程團隊密切協作 | 規劃驗收與工程實作邊界清楚 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 流程改變可追問口徑 |
| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 有使用者風險與切換取捨 |
| HR06 | supported | 從交友與訂閱制 App 到企業招募系統 | 領域轉換與責任脈絡清楚 |
| HR07 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 有跨國合作實例 |
| HR08 | supported | 現任 1111 招募系統 Product Owner | 定位與代表案例可找到 |
| HR09 | partial | 依目前掌握的情況 | 安全觀察不等同完整監測 |
| HR10 | supported | 接下來，我希望將更多心力放回產品策略 | 方向與策略規劃職責相容 |
| HR11 | partial | 台北市、新北市，可接受遠端或混合辦公 | 未見已知衝突；實際條件待確認 |
| HR12 | supported | 定義使用情境與驗收標準 | 多個案例支持邀約並追問缺口 |
| HM01 | supported | 訂閱制 B2C App 與雙邊媒合平台 | 社交與安全經驗具轉移性 |
| HM02 | supported | 客服反映配對名單「少又舊」 | 客服與競品訊號已改變規則 |
| HM03 | supported | 選擇首次登入引導確認、不強迫修改 | 可追問選項及決策權 |
| HM04 | supported | 依抽成、稅、手續費及撥款週期做實收試算 | 有商業試算與產品選擇 |
| HM05 | partial | 為觀察差異，非因果 | 有衡量限制但監控口徑待補 |
| HM06 | supported | 與資料科學團隊合作，定義使用情境與驗收標準 | 角色清楚；總部權責需核對 |
| HM07 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫 | 端到端交付具體 |
| HM08 | supported | 改依職缺上線日排序、20 天內不重複推薦 | 業務規則拆解有證據 |
| HM09 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 符合資深IC協作範圍 |
| HM10 | supported | 現任 1111 招募系統 Product Owner | 重點明確但有重複 |
| HM11 | supported | 依客服測試回饋調整推薦規則 | 有修正訊號可深化 |
| HM12 | supported | 與工程協作於 2026/04/17 上線簽章驗證 | 直接相關案例值得約談 |
| HM13 | supported | 為觀察差異，非因果 | 依本JD獨立取證；尚無真人校準 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 安全與登入專案直接相關：「上線簽章驗證」。 |
| 2 | 跨國協作具體：「與 CodaPay 新加坡技術團隊協調串接」。 |
| 3 | 有取捨：「選擇首次登入引導確認、不強迫修改」。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 總部共同規劃路線圖與決策權責 | 跨國合作如何處理優先級分歧？與總部共塑路線圖的經驗？ |
| 2 | 安全監測與實驗可比性口徑 | 未再冒用的資料來源、事件定義、監測覆蓋與盲區是什麼？ |
| 3 | 指定工具與訪談問卷實際運用 | 哪次訪談或問卷改變產品決策？ Confluence、Jira、Codex的實際使用情況？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 安全專案｜「上線簽章驗證」｜與職缺帳號安全主題直接相關。
- 改版｜「選擇首次登入引導確認、不強迫修改」｜呈現使用者摩擦與切換風險取捨。
- 跨國付款｜「與 CodaPay 新加坡技術團隊協調串接」｜支持跨國技術溝通。

**可改進（4 點）**：

- 位置：尚凡／Peach付款
- 原句：並與 CodaPay 新加坡技術團隊協調串接
- 問題類型：ownership
- 嚴重度：interview_follow_up
- 影響：海外串接不完全等同與總部共同塑造路線圖；不阻擋面試，需核對協商範圍。
- 建議方向：補一例跨國優先級分歧、本人決策權與解法。

- 位置：1111／登入安全
- 原句：依目前掌握的情況
- 問題類型：measurement
- 嚴重度：interview_follow_up
- 影響：未再冒用是有限觀察；缺事件定義、覆蓋率與監測來源，需面試核對而非否定。
- 建議方向：說明監測來源與盲區；定價實驗另確認樣本及同期混淆。

- 位置：專業技能
- 原句：研究與數據：使用者訪談與問卷
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：訪談問卷缺具體應用；指定工具部分未呈現，屬可於面試釐清之缺口。
- 建議方向：有實際經驗才補研究如何改變決策及指定工具用途。

- 位置：專業摘要及自傳
- 原句：近 10 年 PM 經驗，經手 6 款產品
- 問題類型：readability
- 嚴重度：editorial
- 影響：摘要未優先呈現最相關安全專案，自傳部分重複；僅影響資訊可見性。
- 建議方向：提前安全案例並縮減重複敘述，不升格為能力差異。

**編輯附件**（不影響判斷）：依本職缺將安全專案提前；自傳保留新增判斷，刪減重複。

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

### 成果分類補表
重複摘要與自傳依同一案例分類；下列數字不視為獨立加分。
| 成果或敘述原句 | 分類 | 解讀限制 |
| :-- | :-- | :-- |
| 近 10 年 PM 經驗，經手 6 款產品 | context | 經歷範圍 |
| 對接 16 個需求單位 | context | 協作範圍非成果 |
| 全站活躍付費廠商約 6.6 萬家 | context | 系統規模非個人成果 |
| 約 50 項大項功能上線 | output | 規劃與工程共同交付 |
| 上線 111 項 Roadmap 細項 | output | 與大項口徑不同不相加 |
| 盤點出上千組重複 E-mail | output / context | 問題盤點 |
| 選擇首次登入引導確認、不強迫修改 | decision | 降低既有使用者切換風險 |
| 停機約 1.5 小時 | output | 切換交付紀錄非使用者成效 |
| 十多家廠商帳號遭冒用 | context | 安全事件背景 |
| 上線簽章驗證 | output | 安全功能交付 |
| 未再出現同類帳號冒用 | outcome | 有限掌握情況非監測證明 |
| 需求平均處理週期由 100.4 天降至 30.9 天 | outcome | 有期間與穩態限制；口徑待核對 |
| 完成 1,726／1,857 張需求與問題單 | output | 處理量與完成率 |
| 信件與即時通整合排在其他新功能之前 | decision / in_progress | 尚未完成不算結果 |
| 改版排在新功能職缺健檢之前 | decision / in_progress | 尚未完成不算結果 |
| 改依職缺上線日排序、20 天內不重複推薦 | decision / output | 規則改變未提供效果量測 |
| 需求管線觸及 1,279 家活躍付費廠商 | context | 分析母體非全站代表 |
| 該群年化留存 81.2%，同期全站 74.2% | outcome | 觀察差異非因果 |
| 公司簡介生成、職缺工作說明生成及推薦人才 | output | 已上線未提供採用成效 |
| 依客服測試回饋調整推薦規則 | decision | 回饋改變方案 |
| 相對變化約多 28% | outcome | 跨平台及時間對照，非隨機因果 |
| 依結果全面調降售價 | decision | 以實驗結果改變定價 |
| Peach 網頁付款占營收由 24% 至 80% 以上 | outcome | 渠道占比非總營收提升 |
| KOOL 訂閱與付費牆規劃上線 | output | 三端產品交付 |
| 設定檔案完成、社群認證及照片門檻 | decision | 資格與付費牆規則 |
| 主導 Juicy 上線 | output | 上線交付 |
| 男性 DAU 約 3,200 至 1.25 萬 | outcome | 產品與行銷導流整體表現 |
| SweetRing 在地化涵蓋 | output | 七市場在地化交付 |
| 與最多約 10 位外國實習生協作 | context | 無直屬權限協作非管理規模加分 |
| 導入 CodaPay | output | 支付整合 |
| 提出 7／30／90 天訂閱方案與加贈內容 | decision / output | 實收試算支持方案 |
| 商品資訊英翻中與英文校對 | output | 英文應用 |
| 自建 Claude Code 協作流程 | output | 流程建立非AI產品成效 |
| 12 條分支、23 個共用 skill | context | 流程規模不等於效能 |


## B-jd43｜揭盲：甲=K、乙=M；偏好=M

```json
{"job_id":"jd43","order":"甲=K/乙=M","differences":[{"what":"乙補出帳號冒用對個資的風險，甲已交代相同安全事件與交付。","hiring_meaning":"更容易定位安全風險判斷的追問；不因此提高安全交付能力評價，仍須驗證威脅模型與監測範圍。","type":"readability"},{"what":"乙補出配對痛點、排序根因與競品實測到規則調整的鏈條；甲僅概述推薦驗收與回饋。","hiring_meaning":"對使用者理解與競品分析提供具體面試切入點，可驗證如何排除其他根因、規則效果及驗證方法。","type":"capability"},{"what":"乙明確區分自己定義取數需求、DBA撈取與試算表分析；甲呈現快照比較結果。","hiring_meaning":"可釐清分析職責邊界，追問留存年化方法與樣本選擇；兩者均註明非因果，不能視為留存提升功績。","type":"measurement"}],"preference":"乙","reason":"乙補出競品實測與排序診斷的決策鏈，也交代留存分析分工，讓主管更能設計研究與數據追問；安全風險說明僅增可讀性，相同交付與成效不重複加分。","evidence_甲":["登入安全盤點源於 2026/04 十多家廠商帳號遭冒用。","AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。與資料科學團隊合作，定義使用情境與驗收標準，依客服測試回饋調整推薦規則。","比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。"],"evidence_乙":["登入安全盤點源於 2026/04 十多家廠商帳號遭冒用；求才端可存取大量求職者個資，冒用登入即有外洩風險。","客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。","由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。"]}
```

## 版本比較｜jd43｜順序 甲=K 乙=M｜model_id: unknown
- 偏好：乙（揭盲：M）
| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 乙補出帳號冒用對個資的風險，甲已交代相同安全事件與交付。 | 更容易定位安全風險判斷的追問；不因此提高安全交付能力評價，仍須驗證威脅模型與監測範圍。 | readability | 登入安全盤點源於 2026/04 十多家廠商帳號遭冒用。 | 登入安全盤點源於 2026/04 十多家廠商帳號遭冒用；求才端可存取大量求職者個資，冒用登入即有外洩風險。 |
| 2 | 乙補出配對痛點、排序根因與競品實測到規則調整的鏈條；甲僅概述推薦驗收與回饋。 | 對使用者理解與競品分析提供具體面試切入點，可驗證如何排除其他根因、規則效果及驗證方法。 | capability | AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。與資料科學團隊合作，定義使用情境與驗收標準，依客服測試回饋調整推薦規則。 | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 |
| 3 | 乙明確區分自己定義取數需求、DBA撈取與試算表分析；甲呈現快照比較結果。 | 可釐清分析職責邊界，追問留存年化方法與樣本選擇；兩者均註明非因果，不能視為留存提升功績。 | measurement | 比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |
- 理由（≤120 字）：乙補出競品實測與排序診斷的決策鏈，也交代留存分析分工，讓主管更能設計研究與數據追問；安全風險說明僅增可讀性，相同交付與成效不重複加分。


# jd44｜逐次輸出


## A-jd44-K｜履歷K

```json
{"rubric_version": "4.2", "resume_id": "K", "job_id": "jd44", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd44-K", "human_calibrated": false, "requirements": [{"id": "R01", "text": "3年以上網路產品管理經驗", "type": "required", "status": "supported", "evidence": ["近 10 年 PM 經驗"], "blocks_interview": false, "reason": "網路產品經驗直接對應"}, {"id": "R02", "text": "以使用者為中心", "type": "required", "status": "supported", "evidence": ["選擇首次登入引導確認、不強迫修改"], "blocks_interview": false, "reason": "具體使用情境影響方案"}, {"id": "R03", "text": "策略思考與執行能力", "type": "required", "status": "partial", "evidence": ["依結果全面調降售價"], "blocks_interview": false, "reason": "可見決策與交付；長期願景推導待問"}, {"id": "R04", "text": "數據驅動、行為分析、A/B測試與指標", "type": "required", "status": "partial", "evidence": ["以 Android 售價不變作對照"], "blocks_interview": false, "reason": "具準實驗與指標；隨機A/B設計待驗證"}, {"id": "R05", "text": "溝通協作能力，含跨國外部合作", "type": "required", "status": "supported", "evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "blocks_interview": false, "reason": "內外部協作有案例"}, {"id": "R06", "text": "市場與競品分析能力", "type": "required", "status": "partial", "evidence": ["競品實測"], "blocks_interview": false, "reason": "僅技能線索；未展示如何影響方向"}, {"id": "R07", "text": "優異英文溝通及寫作能力", "type": "required", "status": "partial", "evidence": ["英文 TOEIC 980、TOEFL iBT 93"], "blocks_interview": false, "reason": "測驗及跨國合作支持基礎；專業寫作待驗證"}, {"id": "R08", "text": "音樂、內容、社群、娛樂或AI產品經驗", "type": "preferred", "status": "supported", "evidence": ["訂閱制 B2C App 與雙邊媒合平台"], "blocks_interview": false, "reason": "社交與AI產品可轉移，不要求音樂全命中"}, {"id": "R09", "text": "日文能力", "type": "preferred", "status": "unknown", "evidence": [], "blocks_interview": false, "reason": "未提供；不阻擋面試"}, {"id": "R10", "text": "AI熱忱或AI功能上線實務", "type": "preferred", "status": "supported", "evidence": ["AI 功能已上線公司簡介生成"], "blocks_interview": false, "reason": "具AI上線及資料科學協作"}, {"id": "R11", "text": "成功從0到1推動新產品或核心功能上線", "type": "preferred", "status": "supported", "evidence": ["主導 Juicy 上線"], "blocks_interview": false, "reason": "新產品交付成立；構思與定位可追問"}], "dimensions": [{"id": "positioning", "rating": "足夠", "evidence": ["涵蓋訂閱制社交 App、網紅媒合及企業招募系統"], "missing": ["音樂場景需轉移驗證"], "issue_ids": []}, {"id": "role_evidence", "rating": "足夠", "evidence": ["以 Android 售價不變作對照"], "missing": ["市場分析、正式A/B及英文寫作待驗證"], "issue_ids": ["I01", "I02", "I03"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": ["長期願景與路線圖推導待問"], "issue_ids": ["I04"]}, {"id": "outcome_quality", "rating": "足夠", "evidence": ["為觀察差異，非因果"], "missing": ["年化留存算法及安全監測範圍待核"], "issue_ids": ["I05"]}, {"id": "ownership", "rating": "強", "evidence": ["由我主責規劃，與工程團隊密切協作"], "missing": ["外部共創決策邊界可面試確認"], "issue_ids": []}, {"id": "readability", "rating": "足夠", "evidence": ["現任 1111 招募系統 Product Owner"], "missing": ["音樂職缺可前置B2C與AI代表案例"], "issue_ids": []}], "results": [{"quote": "全站活躍付費廠商約 6.6 萬家", "kinds": ["context"]}, {"quote": "約 50 項大項功能上線", "kinds": ["output"]}, {"quote": "需求平均處理週期由 100.4 天降至 30.9 天", "kinds": ["outcome"]}, {"quote": "該群年化留存 81.2%，同期全站 74.2%", "kinds": ["outcome"]}, {"quote": "相對變化約多 28%", "kinds": ["outcome"]}, {"quote": "目前專案仍在開發中", "kinds": ["in_progress"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["近 10 年 PM 經驗"], "application_note": "具產品、訂閱與AI可轉移案例"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "近期B2B與音樂B2C情境不同"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "application_note": "規劃、驗收與工程邊界明確"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "具流程改變，口徑面試核對"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "依使用者風險選擇方案"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["從交友與訂閱制 App 到企業招募系統"], "application_note": "責任演變與跨產品經驗清楚"}, {"rule_id": "HR07", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例"], "application_note": "工具與協作連到實際交付"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["曾設計定價實驗、規劃網頁付款"], "application_note": "可快速找到相關代表案例"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["依目前掌握的情況"], "application_note": "需區分口述與監測紀錄"}, {"rule_id": "HR10", "status": "supported", "resume_evidence": ["我希望將更多心力放回產品策略"], "application_note": "方向與策略職責相容"}, {"rule_id": "HR11", "status": "unknown", "resume_evidence": [], "application_note": "JD未列地點語言外條件衝突"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["主導 Juicy 上線"], "application_note": "足以面試，缺口可用工作樣本核對"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["訂閱制 B2C App 與雙邊媒合平台"], "evidence_type": "context", "source_ids": [], "interview_question": "如何轉用到音樂訂閱？"}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["最大宗是溝通管道中斷"], "evidence_type": "decision", "source_ids": [], "interview_question": "工單分析如何改變優先級？"}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "evidence_type": "decision", "source_ids": [], "interview_question": "比較過哪些方案及風險？"}, {"rule_id": "HM04", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "evidence_type": "decision", "source_ids": [], "interview_question": "實收試算如何影響產品選擇？"}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "partial", "resume_evidence": ["為觀察差異，非因果"], "evidence_type": "outcome", "source_ids": [], "interview_question": "年化留存計算及選樣限制為何？"}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["與資料科學團隊合作，定義使用情境與驗收標準"], "evidence_type": "output", "source_ids": [], "interview_question": "AI專案的決策權責如何分配？"}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例"], "evidence_type": "output", "source_ids": [], "interview_question": "切換時如何決定回滾條件？"}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["與工程協作於 2026/04/17 上線簽章驗證"], "evidence_type": "output", "source_ids": [], "interview_question": "驗證規則與替代方案如何討論？"}, {"rule_id": "HM09", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "evidence_type": "output", "source_ids": [], "interview_question": "跨產品方向與資源如何協商？"}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["曾設計定價實驗、規劃網頁付款"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則"], "evidence_type": "decision", "source_ids": [], "interview_question": "哪一項反例導致推薦規則改動？"}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["主導 Juicy 上線"], "evidence_type": "output", "source_ids": [], "interview_question": "可否提供去識別化策略與實驗案例？"}, {"rule_id": "HM13", "primary_dimension": "", "status": "not_applicable", "resume_evidence": [], "evidence_type": null, "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HM08", "source_ids": [], "application_note": "可面試釐清，不阻擋邀約", "context_limit": "僅依履歷文字，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "以 Android 售價不變作對照", "reason": "跨平台前後比較不能直接證明隨機A/B熟練度", "suggestion": "追問分組、樣本、干擾與判讀；不否定準實驗價值"}, {"id": "I02", "rule_id": "HR07", "source_ids": [], "application_note": "可面試釐清，不阻擋邀約", "context_limit": "僅依履歷文字，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "競品實測", "reason": "缺市場與競品分析如何改變產品選擇的案例", "suggestion": "補一個分析依據及採取行動的案例"}, {"id": "I03", "rule_id": "HR11", "source_ids": [], "application_note": "可面試釐清，不阻擋邀約", "context_limit": "僅依履歷文字，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "英文 TOEIC 980、TOEFL iBT 93", "reason": "考試與跨國串接未完整證明優異商務寫作", "suggestion": "面試以英文討論規格並檢視去識別寫作樣本"}, {"id": "I04", "rule_id": "HM03", "source_ids": [], "application_note": "可面試釐清，不阻擋邀約", "context_limit": "僅依履歷文字，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "我希望將更多心力放回產品策略", "reason": "具優先級與商業決策，但長期願景和市場路線圖證據待補", "suggestion": "追問市場、使用者、資源如何形成長期路線圖"}, {"id": "I05", "rule_id": "HM05", "source_ids": [], "application_note": "可面試釐清，不阻擋邀約", "context_limit": "僅依履歷文字，未外部查證", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "該群年化留存 81.2%，同期全站 74.2%", "reason": "短期快照年化算法與選樣差異需核對；安全改善亦非監測證明", "suggestion": "說明年化公式、母體及限制，另確認安全觀察來源"}], "decision": {"recommendation": "interview", "evidence": ["主導 Juicy 上線", "依結果全面調降售價", "依客服測試回饋調整推薦規則"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["「主導 Juicy 上線」支持0到1交付", "「依結果全面調降售價」呈現數據與商業決策", "「依客服測試回饋調整推薦規則」支持AI迭代"], "key_gaps": ["市場競品與長期策略的完整案例", "正式A/B設計與留存量測口徑", "優異英文溝通及寫作的工作樣本"], "strengths": ["定價實驗｜「依結果全面調降售價」｜連接分析與商業選擇", "招募改版｜「選擇首次登入引導確認、不強迫修改」｜具使用者風險取捨", "AI功能｜「依客服測試回饋調整推薦規則」｜具AI產品迭代實務"], "interview_questions": ["請說明一份市場與競品分析如何改變長期路線圖。", "定價準實驗的干擾、樣本與隨機A/B如何處理？", "請說明年化留存公式、名冊母體與選樣限制。", "請以英文討論跨國串接需求並提供去識別寫作樣本。", "Juicy從問題定義到上線的本人責任與行銷貢獻各為何？", "AI推薦調整的具體反例、驗收門檻和成效為何？", "安全改善的觀察來源與監測範圍為何？"], "editorial_appendix": ["可將訂閱、0到1與AI案例前置；僅屬資訊排序。"], "spectrum": {"level": 8, "uncertainty_levels": 1, "basis": "多個相關案例、具體取捨與比較衡量支持面試；長期策略、A/B與英文深度仍須驗證。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷K｜第 1 輪｜model_id: unknown

### 1. 結論

- 招聘決定：interview

- Level：8（±1）

- 一句話理由：「主導 Juicy 上線」並具定價與AI迭代案例，足以面試驗證策略深度。

### 2. 六維度

| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 足夠 | 涵蓋訂閱制社交 App、網紅媒合及企業招募系統 | 音樂場景需轉移驗證 |
| role_evidence | 足夠 | 以 Android 售價不變作對照 | 市場分析、正式A/B及英文寫作待驗證 |
| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 長期願景與路線圖推導待問 |
| outcome_quality | 足夠 | 為觀察差異，非因果 | 年化留存算法及安全監測範圍待核 |
| ownership | 強 | 由我主責規劃，與工程團隊密切協作 | 外部共創決策邊界可面試確認 |
| readability | 足夠 | 現任 1111 招募系統 Product Owner | 音樂職缺可前置B2C與AI代表案例 |

### 3. JD 條件對照

| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 3年以上網路產品管理經驗 | 必要 | supported | 近 10 年 PM 經驗 | 網路產品經驗直接對應 |
| 以使用者為中心 | 必要 | supported | 選擇首次登入引導確認、不強迫修改 | 具體使用情境影響方案 |
| 策略思考與執行能力 | 必要 | partial | 依結果全面調降售價 | 可見決策與交付；長期願景推導待問 |
| 數據驅動、行為分析、A/B測試與指標 | 必要 | partial | 以 Android 售價不變作對照 | 具準實驗與指標；隨機A/B設計待驗證 |
| 溝通協作能力，含跨國外部合作 | 必要 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 內外部協作有案例 |
| 市場與競品分析能力 | 必要 | partial | 競品實測 | 僅技能線索；未展示如何影響方向 |
| 優異英文溝通及寫作能力 | 必要 | partial | 英文 TOEIC 980、TOEFL iBT 93 | 測驗及跨國合作支持基礎；專業寫作待驗證 |
| 音樂、內容、社群、娛樂或AI產品經驗 | 加分 | supported | 訂閱制 B2C App 與雙邊媒合平台 | 社交與AI產品可轉移，不要求音樂全命中 |
| 日文能力 | 加分 | unknown | 未呈現 | 未提供；不阻擋面試 |
| AI熱忱或AI功能上線實務 | 加分 | supported | AI 功能已上線公司簡介生成 | 具AI上線及資料科學協作 |
| 成功從0到1推動新產品或核心功能上線 | 加分 | supported | 主導 Juicy 上線 | 新產品交付成立；構思與定位可追問 |

### 4. HR 十二問 ／ HM 十三問

| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗 | 具產品、訂閱與AI可轉移案例 |
| HR02 | supported | 企業端招募系統全模組與求職端公司頁 | 近期B2B與音樂B2C情境不同 |
| HR03 | supported | 由我主責規劃，與工程團隊密切協作 | 規劃、驗收與工程邊界明確 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 具流程改變，口徑面試核對 |
| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 依使用者風險選擇方案 |
| HR06 | supported | 從交友與訂閱制 App 到企業招募系統 | 責任演變與跨產品經驗清楚 |
| HR07 | supported | 與 QA 制定 UAT 驗收案例 | 工具與協作連到實際交付 |
| HR08 | supported | 曾設計定價實驗、規劃網頁付款 | 可快速找到相關代表案例 |
| HR09 | partial | 依目前掌握的情況 | 需區分口述與監測紀錄 |
| HR10 | supported | 我希望將更多心力放回產品策略 | 方向與策略職責相容 |
| HR11 | unknown | 未呈現 | JD未列地點語言外條件衝突 |
| HR12 | supported | 主導 Juicy 上線 | 足以面試，缺口可用工作樣本核對 |
| HM01 | supported | 訂閱制 B2C App 與雙邊媒合平台 | B2C訂閱可轉移，音樂場景待問 |
| HM02 | supported | 最大宗是溝通管道中斷 | 使用者訊號實際影響優先級 |
| HM03 | supported | 選擇首次登入引導確認、不強迫修改 | 限制與選擇清楚 |
| HM04 | supported | 依抽成、稅、手續費及撥款週期做實收試算 | 具變現與成本思考 |
| HM05 | partial | 為觀察差異，非因果 | 量測算法及限制仍需核對 |
| HM06 | supported | 與資料科學團隊合作，定義使用情境與驗收標準 | AI與跨部門責任可追問 |
| HM07 | supported | 與 QA 制定 UAT 驗收案例 | 交付與風險控制有案例 |
| HM08 | supported | 與工程協作於 2026/04/17 上線簽章驗證 | 具規則拆解及工程協作 |
| HM09 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 資深交付成立，長期方向待問 |
| HM10 | supported | 曾設計定價實驗、規劃網頁付款 | 摘要與案例可快速辨認 |
| HM11 | supported | 依客服測試回饋調整推薦規則 | 回饋能改變產品規則 |
| HM12 | supported | 主導 Juicy 上線 | 值得用策略與實驗工作樣本驗證 |
| HM13 | not_applicable | 不適用 | 方法層不評候選人；本次獨立對照JD |

### 5. 約談理由（≤3）與關鍵缺口（≤3）

| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「主導 Juicy 上線」支持0到1交付 |
| 2 | 「依結果全面調降售價」呈現數據與商業決策 |
| 3 | 「依客服測試回饋調整推薦規則」支持AI迭代 |
| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 市場競品與長期策略的完整案例 | 請說明一份市場與競品分析如何改變長期路線圖。 |
| 2 | 正式A/B設計與留存量測口徑 | 定價準實驗的干擾、樣本與隨機A/B如何處理？ |
| 3 | 優異英文溝通及寫作的工作樣本 | 請以英文討論跨國串接需求並提供去識別寫作樣本。 |

補充追問：

- 請說明年化留存公式、名冊母體與選樣限制。

- Juicy從問題定義到上線的本人責任與行銷貢獻各為何？

- AI推薦調整的具體反例、驗收門檻和成效為何？

- 安全改善的觀察來源與監測範圍為何？

### 6. 評語（給寫稿者的具體回饋）

**做得好（3 點）**：

- 定價實驗｜「依結果全面調降售價」｜連接分析與商業選擇

- 招募改版｜「選擇首次登入引導確認、不強迫修改」｜具使用者風險取捨

- AI功能｜「依客服測試回饋調整推薦規則」｜具AI產品迭代實務

**可改進（≤5 點）**：

- 位置：尚凡定價實驗

  - 原句：以 Android 售價不變作對照

  - 問題類型：requirement

  - 嚴重度：interview_follow_up

  - 影響：跨平台前後比較不能直接證明隨機A/B熟練度；需面試追問，不阻擋邀約。

  - 建議方向：追問分組、樣本、干擾與判讀；不否定準實驗價值

- 位置：專業技能／研究與數據

  - 原句：競品實測

  - 問題類型：requirement

  - 嚴重度：interview_follow_up

  - 影響：缺市場與競品分析如何改變產品選擇的案例；需面試追問，不阻擋邀約。

  - 建議方向：補一個分析依據及採取行動的案例

- 位置：語言與跨國合作

  - 原句：英文 TOEIC 980、TOEFL iBT 93

  - 問題類型：requirement

  - 嚴重度：interview_follow_up

  - 影響：考試與跨國串接未完整證明優異商務寫作；需面試追問，不阻擋邀約。

  - 建議方向：面試以英文討論規格並檢視去識別寫作樣本

- 位置：自傳／策略方向

  - 原句：我希望將更多心力放回產品策略

  - 問題類型：requirement

  - 嚴重度：interview_follow_up

  - 影響：具優先級與商業決策，但長期願景和市場路線圖證據待補；需面試追問，不阻擋邀約。

  - 建議方向：追問市場、使用者、資源如何形成長期路線圖

- 位置：1111／留存與安全成果

  - 原句：該群年化留存 81.2%，同期全站 74.2%

  - 問題類型：measurement

  - 嚴重度：interview_follow_up

  - 影響：短期快照年化算法與選樣差異需核對；安全改善亦非監測證明；需面試追問，不阻擋邀約。

  - 建議方向：說明年化公式、母體及限制，另確認安全觀察來源

**編輯附件**（語氣、用詞微調；不影響判斷）：

可將訂閱、0到1與AI案例前置；僅屬資訊排序。

### 7. 資深能力分布

delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明

PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

本審查未外部查證；履歷內部可讀與一致不等於成效已驗證。

### 成果分類補表

| 原句 | 分類 | 解讀 |
| :-- | :-- | :-- |
| 全站活躍付費廠商約 6.6 萬家 | context | JSON已列，非外部查證 |
| 約 50 項大項功能上線 | output | JSON已列，非外部查證 |
| 需求平均處理週期由 100.4 天降至 30.9 天 | outcome | JSON已列，非外部查證 |
| 該群年化留存 81.2%，同期全站 74.2% | outcome | JSON已列，非外部查證 |
| 相對變化約多 28% | outcome | JSON已列，非外部查證 |
| 目前專案仍在開發中 | in_progress | JSON已列，非外部查證 |
| 對接 16 個需求單位 | context | 協作範圍 |
| 經手 6 款產品 | context | 產品經驗範圍 |
| 團隊 3 名企劃 | context | 不直接代表管理能力 |
| 另於 2026/01–06 上線 111 項 Roadmap 細項 | output | 與50項不同粒度，不加總 |
| 盤點出上千組重複 E-mail | output | 盤點發現 |
| 選擇首次登入引導確認、不強迫修改 | decision | 降低改版登入風險 |
| 第一階段於 2025/10 離峰切換上線 | output | 分階段交付 |
| 停機約 1.5 小時 | outcome | 切換運作結果 |
| 2026/04 十多家廠商帳號遭冒用 | context | 問題背景 |
| 與工程協作於 2026/04/17 上線簽章驗證 | output | 協作交付 |
| 上線後至 2026/10 未再出現同類帳號冒用 | outcome | 依目前掌握，非獨立監測證明 |
| 完成 1,726／1,857 張需求與問題單，約 93% | output | 工單完成量 |
| 需求管線觸及 1,279 家活躍付費廠商 | context | 觸及母體 |
| 約占全站 66,150 家的 1.9% | context | 群體覆蓋範圍 |
| AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才 | output | 已交付AI功能 |
| 依客服測試回饋調整推薦規則 | decision | 依回饋修正 |
| 降價期 iOS 非續訂營收較基準期增 5% | outcome | 平台與期間限定 |
| Android 減 18% | outcome | 對照平台表現 |
| 還原原價後 iOS 較基準期減 65% | outcome | 還原階段觀察 |
| 依結果全面調降售價 | decision | 商業決策 |
| Peach 網頁付款占營收由 24% 至 80% 以上 | outcome | 通路占比非總營收增幅 |
| KOOL 訂閱與付費牆規劃上線 | output | 核心付費功能交付 |
| 設定檔案完成、社群認證及照片門檻 | decision | 精選網紅資格規則 |
| 主導 Juicy 上線 | output | 新產品交付 |
| 上線後 6 週男性 DAU 約 3,200 至 1.25 萬 | outcome | 產品與行銷導流共同表現 |
| 與最多約 10 位外國實習生協作 | context | 無直屬管理關係 |
| 日本、韓國 7 個市場 | context | 在地化市場範圍 |
| 導入 CodaPay | output | 支付整合 |
| 提出 7／30／90 天訂閱方案與加贈內容 | output | 提案非已實現成效 |
| 將信件與即時通整合排在其他新功能之前 | decision / in_progress | 優先級已決定，成效未實現 |


## A-jd44-M｜履歷M

```json
{"rubric_version": "4.2", "resume_id": "M", "job_id": "jd44", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd44-M", "human_calibrated": false, "requirements": [{"id": "R01", "text": "3年以上網路產品管理經驗", "type": "required", "status": "supported", "evidence": ["近 10 年 PM 經驗，經手 6 款產品"], "blocks_interview": false, "reason": "具連續網路產品經驗。"}, {"id": "R02", "text": "使用者為中心與核心需求理解", "type": "required", "status": "supported", "evidence": ["客服反映配對名單「少又舊」"], "blocks_interview": false, "reason": "客服訊號、規則根因與改動相連。"}, {"id": "R03", "text": "策略、長期路線圖與執行", "type": "required", "status": "partial", "evidence": ["信件與即時通整合排在其他新功能之前"], "blocks_interview": false, "reason": "有優先級取捨，長期市場願景與資源配置待核對。"}, {"id": "R04", "text": "跨國跨職能及外部廠商共創", "type": "required", "status": "partial", "evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "blocks_interview": false, "reason": "跨國整合成立，外部產品概念共創深度待核對。"}, {"id": "R05", "text": "全生命週期、0到1及持續優化", "type": "required", "status": "supported", "evidence": ["主導 Juicy 上線"], "blocks_interview": false, "reason": "另有規格、驗收與持續迭代案例。"}, {"id": "R06", "text": "數據、行為分析、A/B測試與關鍵指標", "type": "required", "status": "partial", "evidence": ["以 Android 售價不變作對照"], "blocks_interview": false, "reason": "有對照定價實驗與留存分析；隨機A/B與行為漏斗待核對。"}, {"id": "R07", "text": "市場與競品分析", "type": "required", "status": "partial", "evidence": ["實測主要競品反推規則後"], "blocks_interview": false, "reason": "競品實測具體，市場趨勢如何改變方向待核對。"}, {"id": "R08", "text": "優異英文溝通與寫作", "type": "required", "status": "supported", "evidence": ["以英文分派 UI/UX 翻譯與多國粉專經營任務"], "blocks_interview": false, "reason": "具實際英文協作與校對證據，面試驗證程度。"}, {"id": "R09", "text": "使用者參與、留存與AI個人化探索", "type": "required", "status": "partial", "evidence": ["依客服測試回饋調整推薦規則"], "blocks_interview": false, "reason": "有AI推薦與留存觀察，音樂粉絲情境可轉移性待談。"}, {"id": "R10", "text": "音樂、內容、社群、娛樂或AI產品經驗", "type": "preferred", "status": "supported", "evidence": ["AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。"], "blocks_interview": false, "reason": "已有社交訂閱與AI產品經驗，音樂經驗未呈現。"}, {"id": "R11", "text": "日文能力", "type": "preferred", "status": "unknown", "evidence": [], "blocks_interview": false, "reason": "未提供日文能力，不阻擋面試。"}, {"id": "R12", "text": "AI熱忱或上線實務；成功0到1上線", "type": "preferred", "status": "supported", "evidence": ["KOOL 訂閱與付費牆規劃上線"], "blocks_interview": false, "reason": "AI功能及新產品上線支持加分，具體起點待面試核對。"}], "dimensions": [{"id": "positioning", "rating": "強", "evidence": ["涵蓋訂閱制社交 App、網紅媒合及企業招募系統。"], "missing": ["音樂串流的遷移判斷留面試確認"], "issue_ids": []}, {"id": "role_evidence", "rating": "足夠", "evidence": ["以 Android 售價不變作對照"], "missing": ["隨機A/B、跨國共創的責任深度待核對"], "issue_ids": ["I02", "I03"]}, {"id": "decision_depth", "rating": "足夠", "evidence": ["信件與即時通整合排在其他新功能之前"], "missing": ["長期市場願景與資源選擇未充分呈現"], "issue_ids": ["I01"]}, {"id": "outcome_quality", "rating": "強", "evidence": ["為觀察差異，非因果。"], "missing": ["安全效果的監測依據仍有限"], "issue_ids": ["I04"]}, {"id": "ownership", "rating": "強", "evidence": ["由我擬定取數的資料表與欄位"], "missing": ["跨國共創權責見I03，不重複扣列"], "issue_ids": []}, {"id": "readability", "rating": "足夠", "evidence": ["資深產品經理｜Senior Product Manager"], "missing": ["代表作可優先呈現訂閱與AI經驗"], "issue_ids": []}], "results": [{"quote": "全站活躍付費廠商約 6.6 萬家", "kinds": ["context"]}, {"quote": "約 50 項大項功能上線", "kinds": ["output"]}, {"quote": "兩案皆開發中", "kinds": ["decision", "in_progress"]}, {"quote": "為觀察差異，非因果。", "kinds": ["outcome"]}, {"quote": "以 Android 售價不變作對照", "kinds": ["decision"]}, {"quote": "上線後 6 週男性 DAU 約 3,200 至 1.25 萬", "kinds": ["outcome"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["近 10 年 PM 經驗，經手 6 款產品"], "application_note": "產品年資與可轉移領域支持面試"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "近期企業端；既往消費訂閱可轉移"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我擬定取數的資料表與欄位"], "application_note": "本人與DBA分工清楚"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["為觀察差異，非因果。"], "application_note": "明示限制，結果仍需核對口徑"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "有風險與體驗取捨"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["接下來，我希望將更多心力放回產品策略"], "application_note": "方向從交付走向策略，與職缺相容"}, {"rule_id": "HR07", "status": "supported", "resume_evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "application_note": "技能具有實際協作情境"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["訂閱制 B2C App 與雙邊媒合平台。"], "application_note": "結構清楚，可調整相關案例排序"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["依目前掌握的情況"], "application_note": "安全效果不是已核實監測結論"}, {"rule_id": "HR10", "status": "supported", "resume_evidence": ["接下來，我希望將更多心力放回產品策略"], "application_note": "方向相容，不推測音樂動機"}, {"rule_id": "HR11", "status": "unknown", "resume_evidence": ["錄取後三週可上班"], "application_note": "JD未明列地點到職條件，無已知衝突"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["主導 Juicy 上線"], "application_note": "多個相關案例足以約談"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["訂閱制 B2C App 與雙邊媒合平台。"], "evidence_type": "context", "source_ids": [], "interview_question": "如何將訂閱社交產品經驗轉用音樂串流？"}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["客服反映配對名單「少又舊」"], "evidence_type": "decision", "source_ids": [], "interview_question": "什麼證據使你改變推薦規則？"}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["信件與即時通整合排在其他新功能之前"], "evidence_type": "decision", "source_ids": [], "interview_question": "如何衡量延後新功能的機會成本？"}, {"rule_id": "HM04", "primary_dimension": "decision_depth", "status": "partial", "resume_evidence": ["依結果全面調降售價。"], "evidence_type": "decision", "source_ids": [], "interview_question": "如何由市場與單位經濟推導長期路線圖？"}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "supported", "resume_evidence": ["為觀察差異，非因果。"], "evidence_type": "outcome", "source_ids": [], "interview_question": "如何計算年化留存及控制選樣差異？"}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["與資料科學團隊合作，定義使用情境與驗收標準"], "evidence_type": "output", "source_ids": [], "interview_question": "推薦功能的決策權與分歧如何處理？"}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫。"], "evidence_type": "output", "source_ids": [], "interview_question": "如何設定上線品質門檻？"}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["改依職缺上線日排序、20 天內不重複推薦"], "evidence_type": "decision", "source_ids": [], "interview_question": "如何與工程評估替代推薦規則？"}, {"rule_id": "HM09", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["對接 16 個需求單位"], "evidence_type": "context", "source_ids": [], "interview_question": "跨多產品領域如何分配策略投入？"}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["資深產品經理｜Senior Product Manager"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則。"], "evidence_type": "decision", "source_ids": [], "interview_question": "哪次測試反證改變原本設計？"}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["KOOL 訂閱與付費牆規劃上線"], "evidence_type": "output", "source_ids": [], "interview_question": "請以一項功能說明0到1及後續學習。"}, {"rule_id": "HM13", "primary_dimension": "method", "status": "not_applicable", "resume_evidence": [], "evidence_type": null, "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HM04", "source_ids": [], "application_note": "策略路線圖", "context_limit": "僅據履歷文字，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "信件與即時通整合排在其他新功能之前", "reason": "已有局部取捨，尚無長期願景、市場趨勢與資源配置鏈條；面試追問策略跨度。", "suggestion": "選一例補方向假設、替代方向及投入依據。"}, {"id": "I02", "rule_id": "HR07", "source_ids": [], "application_note": "實驗能力", "context_limit": "僅據履歷文字，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "以 Android 售價不變作對照", "reason": "跨平台分期對照不等同隨機A/B；面試確認分流、樣本與偏差處理。", "suggestion": "說明實驗設計與限制；有隨機A/B案例才補入。"}, {"id": "I03", "rule_id": "HM06", "source_ids": [], "application_note": "跨國共創", "context_limit": "僅據履歷文字，未外部查證", "category": "ownership", "severity": "interview_follow_up", "block_target": null, "claim": "並與 CodaPay 新加坡技術團隊協調串接", "reason": "整合協作可見，廠商共同構思新產品的範圍不明；留面試確認。", "suggestion": "補外部夥伴討論的方案、本人決策與英文文件用途。"}, {"id": "I04", "rule_id": "HR09", "source_ids": [], "application_note": "安全效果", "context_limit": "僅據履歷文字，未外部查證", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "依目前掌握的情況", "reason": "未再冒用的掌握渠道與觀測覆蓋不明；只追問，不能當監測證實。", "suggestion": "維持限制語，補實際回報或監測來源與觀察期間。"}], "decision": {"recommendation": "interview", "evidence": ["主導 Juicy 上線", "以 Android 售價不變作對照", "依客服測試回饋調整推薦規則。"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["訂閱與新產品案例可轉移至音樂產品", "數據實驗與留存限制寫得清楚", "AI上線與跨國協作提供實際追問基礎"], "key_gaps": ["長期市場策略與資源配置", "隨機A/B及行為分析深度", "外部廠商共創範圍與英文商務寫作程度"], "strengths": ["訂閱定價與付款經驗直接相關", "清楚標示觀察差異及團隊表現限制", "AI情境、驗收與客服回饋形成迭代鏈"], "interview_questions": ["請用市場趨勢、使用者需求與數據推導一份長期產品路線圖。", "定價實驗如何處理跨平台、時間及樣本差異？另有隨機A/B案例嗎？", "與外部廠商從概念到方案的共創案例中，你負責哪些決定？", "請用英文說明一次產品提案與決策文件的寫作過程。", "年化留存如何計算，需求群與全站的選樣差異有哪些？", "AI推薦的驗收指標、失敗案例與使用者參與效果為何？", "Juicy上線前的產品起點、本人範圍及行銷貢獻如何區分？", "安全事件未再發生的觀測渠道與覆蓋範圍為何？"], "editorial_appendix": ["針對本職缺，可把訂閱、實驗、AI與跨國協作移到摘要前段。"], "spectrum": {"level": 8, "uncertainty_levels": 1, "basis": "多個相關案例、清楚取捨及衡量限制支持面試；長期策略、隨機A/B與廠商共創仍待核對。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷｜第 1 輪｜model_id: unknown

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「主導 Juicy 上線」及訂閱、AI與實驗案例可轉移，足以面試。

### 2. 六維度
| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 涵蓋訂閱制社交 App、網紅媒合及企業招募系統。 | 音樂串流的遷移判斷留面試確認 |
| role_evidence | 足夠 | 以 Android 售價不變作對照 | 隨機A/B、跨國共創的責任深度待核對 |
| decision_depth | 足夠 | 信件與即時通整合排在其他新功能之前 | 長期市場願景與資源選擇未充分呈現 |
| outcome_quality | 強 | 為觀察差異，非因果。 | 安全效果的監測依據仍有限 |
| ownership | 強 | 由我擬定取數的資料表與欄位 | 跨國共創權責見I03，不重複扣列 |
| readability | 足夠 | 資深產品經理｜Senior Product Manager | 代表作可優先呈現訂閱與AI經驗 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 3年以上網路產品管理經驗 | 必要 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 具連續網路產品經驗。 |
| 使用者為中心與核心需求理解 | 必要 | supported | 客服反映配對名單「少又舊」 | 客服訊號、規則根因與改動相連。 |
| 策略、長期路線圖與執行 | 必要 | partial | 信件與即時通整合排在其他新功能之前 | 有優先級取捨，長期市場願景與資源配置待核對。 |
| 跨國跨職能及外部廠商共創 | 必要 | partial | 並與 CodaPay 新加坡技術團隊協調串接 | 跨國整合成立，外部產品概念共創深度待核對。 |
| 全生命週期、0到1及持續優化 | 必要 | supported | 主導 Juicy 上線 | 另有規格、驗收與持續迭代案例。 |
| 數據、行為分析、A/B測試與關鍵指標 | 必要 | partial | 以 Android 售價不變作對照 | 有對照定價實驗與留存分析；隨機A/B與行為漏斗待核對。 |
| 市場與競品分析 | 必要 | partial | 實測主要競品反推規則後 | 競品實測具體，市場趨勢如何改變方向待核對。 |
| 優異英文溝通與寫作 | 必要 | supported | 以英文分派 UI/UX 翻譯與多國粉專經營任務 | 具實際英文協作與校對證據，面試驗證程度。 |
| 使用者參與、留存與AI個人化探索 | 必要 | partial | 依客服測試回饋調整推薦規則 | 有AI推薦與留存觀察，音樂粉絲情境可轉移性待談。 |
| 音樂、內容、社群、娛樂或AI產品經驗 | 加分 | supported | AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。 | 已有社交訂閱與AI產品經驗，音樂經驗未呈現。 |
| 日文能力 | 加分 | unknown | 未提供 | 未提供日文能力，不阻擋面試。 |
| AI熱忱或上線實務；成功0到1上線 | 加分 | supported | KOOL 訂閱與付費牆規劃上線 | AI功能及新產品上線支持加分，具體起點待面試核對。 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 產品年資與可轉移領域支持面試 |
| HR02 | supported | 企業端招募系統全模組與求職端公司頁 | 近期企業端；既往消費訂閱可轉移 |
| HR03 | supported | 由我擬定取數的資料表與欄位 | 本人與DBA分工清楚 |
| HR04 | supported | 為觀察差異，非因果。 | 明示限制，結果仍需核對口徑 |
| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 有風險與體驗取捨 |
| HR06 | supported | 接下來，我希望將更多心力放回產品策略 | 方向從交付走向策略，與職缺相容 |
| HR07 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 技能具有實際協作情境 |
| HR08 | supported | 訂閱制 B2C App 與雙邊媒合平台。 | 結構清楚，可調整相關案例排序 |
| HR09 | partial | 依目前掌握的情況 | 安全效果不是已核實監測結論 |
| HR10 | supported | 接下來，我希望將更多心力放回產品策略 | 方向相容，不推測音樂動機 |
| HR11 | unknown | 錄取後三週可上班 | JD未明列地點到職條件，無已知衝突 |
| HR12 | supported | 主導 Juicy 上線 | 多個相關案例足以約談 |
| HM01 | supported | 訂閱制 B2C App 與雙邊媒合平台。 | 消費訂閱可轉移，音樂情境待談 |
| HM02 | supported | 客服反映配對名單「少又舊」 | 使用者訊號連至規則改動 |
| HM03 | supported | 信件與即時通整合排在其他新功能之前 | 取捨已發生，開發中不算結果 |
| HM04 | partial | 依結果全面調降售價。 | 長期市場策略與資源跨度待核對 |
| HM05 | supported | 為觀察差異，非因果。 | 口徑與限制清楚，仍需查證 |
| HM06 | supported | 與資料科學團隊合作，定義使用情境與驗收標準 | 本人與技術夥伴分工清楚 |
| HM07 | supported | 與 QA 制定 UAT 驗收案例、排定上線計畫。 | 規格、驗收與上線有實例 |
| HM08 | supported | 改依職缺上線日排序、20 天內不重複推薦 | 業務規則與工程協作具體 |
| HM09 | supported | 對接 16 個需求單位 | 範圍支持資深IC面試 |
| HM10 | supported | 資深產品經理｜Senior Product Manager | 結構足以辨識主要證據 |
| HM11 | supported | 依客服測試回饋調整推薦規則。 | 回饋能改變規則 |
| HM12 | supported | KOOL 訂閱與付費牆規劃上線 | 相關作品足以支持工作樣本面試 |
| HM13 | not_applicable | 不適用 | 方法層，不作候選人能力加分 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「KOOL 訂閱與付費牆規劃上線」支持訂閱產品能力。 |
| 2 | 「以 Android 售價不變作對照」支持實驗思考。 |
| 3 | 「依客服測試回饋調整推薦規則。」支持AI迭代。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 長期市場策略與資源配置 | 如何由市場資料選方向並配置資源？ |
| 2 | 隨機A/B與行為分析 | 實驗偏差如何處理，另有隨機分流案例嗎？ |
| 3 | 跨國共創與英文寫作深度 | 請以英文說明一次廠商產品提案與本人決策。 |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
1. 尚凡｜「KOOL 訂閱與付費牆規劃上線」｜訂閱與付費體驗與音樂產品有相關性。
2. 1111留存｜「為觀察差異，非因果。」｜主動區分關聯與歸因，利於數據判斷。
3. 1111 AI｜「依客服測試回饋調整推薦規則。」｜使用者回饋連至AI功能迭代。

**可改進（4 點）**：

- 位置：策略路線圖
- 原句：信件與即時通整合排在其他新功能之前
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：已有局部取捨，尚無長期願景、市場趨勢與資源配置鏈條；面試追問策略跨度。
- 建議方向：選一例補方向假設、替代方向及投入依據。

- 位置：實驗能力
- 原句：以 Android 售價不變作對照
- 問題類型：requirement
- 嚴重度：interview_follow_up
- 影響：跨平台分期對照不等同隨機A/B；面試確認分流、樣本與偏差處理。
- 建議方向：說明實驗設計與限制；有隨機A/B案例才補入。

- 位置：跨國共創
- 原句：並與 CodaPay 新加坡技術團隊協調串接
- 問題類型：ownership
- 嚴重度：interview_follow_up
- 影響：整合協作可見，廠商共同構思新產品的範圍不明；留面試確認。
- 建議方向：補外部夥伴討論的方案、本人決策與英文文件用途。

- 位置：安全效果
- 原句：依目前掌握的情況
- 問題類型：measurement
- 嚴重度：interview_follow_up
- 影響：未再冒用的掌握渠道與觀測覆蓋不明；只追問，不能當監測證實。
- 建議方向：維持限制語，補實際回報或監測來源與觀察期間。

**編輯附件**（不影響判斷）：
- 針對本職缺，可把訂閱、實驗、AI與跨國協作移到摘要前段。

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

### 8. 未測試聲明
PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

### 成果分類補表
以下涵蓋各條成果與摘要重述；所有結果均為履歷自述，未外部查證。
| 成果／原句片段 | 分類 | 限制 |
| :-- | :-- | :-- |
| 對接 16 個需求單位 | context | 協作範圍非成效 |
| 近 10 年 PM 經驗，經手 6 款產品 | context | 年資與產品數不自動加分 |
| 約 50 項大項功能上線 | output | 摘要與經歷重述，不重計 |
| 上線 111 項 Roadmap 細項 | output | 粒度不同不與50項直接合計 |
| 全站活躍付費廠商約 6.6 萬家 | context | 系統規模非本人成果 |
| 三階段推進招募系統改版 | decision, output | 首階段已完成，其餘未明 |
| 停機約 1.5 小時 | output | 切換限制，非成長成效 |
| 上線簽章驗證 | output | 與工程協作 |
| 上線後至 2026/10 未再出現同類帳號冒用 | outcome | 依掌握情況，非外部監測驗證 |
| 需求平均處理週期由 100.4 天降至 30.9 天 | outcome | Q1至Q2穩態比較，組成待核對 |
| 完成 1,726／1,857 張需求與問題單 | output | 截至09/29之交付量 |
| 信件與即時通整合排在其他新功能之前 | decision, in_progress | 不當已實現結果 |
| 改版排在新功能職缺健檢之前 | decision, in_progress | 不當已實現結果 |
| 20 天內不重複推薦 | decision, output | 規則，未呈現採用成效 |
| 需求管線觸及 1,279 家活躍付費廠商 | context | 1.9%為涵蓋母體 |
| 該群年化留存 81.2%，同期全站 74.2% | outcome | 非因果；年化算法待核對 |
| AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。 | output | 未宣稱使用者成效 |
| 依客服測試回饋調整推薦規則。 | decision | 回饋帶來調整 |
| 以 Android 售價不變作對照 | decision | 跨平台分期設計非隨機A/B |
| 相對變化約多 28% | outcome | 相對比率，非28百分點 |
| 還原原價後 iOS 較基準期減 65% | outcome | 時間與平台混雜待核對 |
| 依結果全面調降售價。 | decision | 決策，不等於後續收益 |
| Peach 網頁付款占營收由 24% 至 80% 以上 | outcome | 渠道占比，不等於總營收成長 |
| KOOL 訂閱與付費牆規劃上線 | output | 含付費牆與資格門檻決策 |
| 主導 Juicy 上線 | output | 本人產品範圍待核對 |
| 上線後 6 週男性 DAU 約 3,200 至 1.25 萬 | outcome | 產品與行銷整體表現 |
| SweetRing 在地化涵蓋美國、墨西哥、巴西 | output, context | 七市場範圍，不自動加分 |
| 與最多約 10 位外國實習生協作 | context | 無直屬權限，不等於管理 |
| 導入 CodaPay | output | 付款整合 |
| 提出 7／30／90 天訂閱方案與加贈內容 | decision, output | 實收試算連結方案 |
| Newegg.com 商品資訊英翻中與英文校對 | output | 英文實際使用 |
| 12 條分支、23 個共用 skill | output | 工具流程非產品業務成效 |


## B-jd44｜揭盲：甲=M、乙=K；偏好=M

```json
{"job_id":"jd44","order":"甲=M/乙=K","differences":[{"what":"甲增加配對排序根因與競品實測案例；乙僅列競品實測技能。","hiring_meaning":"可追問如何辨識使用者痛點、推導推薦規則與驗證參與成效；不是新增已證明的成效。","type":"capability"},{"what":"甲交代留存分析的取數分工與工具；乙僅述快照比對。","hiring_meaning":"更易確認候選人的分析責任與資料能力邊界；兩版留存數字及非因果限制相同，不提高效果評價。","type":"measurement"},{"what":"甲明列英文分派任務及英文校對；乙保留跨國協作與語言成績但未明示工作語言。","hiring_meaning":"提高英文工作情境的可見性，方便面試驗證跨國溝通及寫作；不能據此判定英文能力較強。","type":"readability"}],"preference":"甲","reason":"甲提供推薦規則診斷與分析分工的不同證據，更能聚焦驗證產品洞察、數據判斷及英文協作；共有的AI上線、定價實驗與0到1經歷不重複加分，音樂應用仍須面試驗證。","evidence_甲":["客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。","由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。","SweetRing 在地化涵蓋美國、墨西哥、巴西、印尼、馬來西亞、日本、韓國 7 個市場；與最多約 10 位外國實習生協作，在無直屬管理關係下以英文分派 UI/UX 翻譯與多國粉專經營任務。"],"evidence_乙":["研究與數據：使用者訪談與問卷、競品實測、GA4、世代分析、對照組實驗、Excel","比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。","SweetRing 在地化涵蓋美國、墨西哥、巴西、印尼、馬來西亞、日本、韓國 7 個市場；與最多約 10 位外國實習生協作，在無直屬管理關係下分派翻譯與粉專經營任務。"]}
```

## 版本比較｜jd44｜順序 甲=M 乙=K｜model_id: unknown
- 偏好：甲（揭盲：M）
| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 甲增加配對排序根因與競品實測案例；乙僅列競品實測技能。 | 可追問如何辨識使用者痛點、推導推薦規則與驗證參與成效；不是新增已證明的成效。 | capability | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 | 研究與數據：使用者訪談與問卷、競品實測、GA4、世代分析、對照組實驗、Excel |
| 2 | 甲交代留存分析的取數分工與工具；乙僅述快照比對。 | 更易確認候選人的分析責任與資料能力邊界；兩版留存數字及非因果限制相同，不提高效果評價。 | measurement | 由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |
| 3 | 甲明列英文分派任務及英文校對；乙保留跨國協作與語言成績但未明示工作語言。 | 提高英文工作情境的可見性，方便面試驗證跨國溝通及寫作；不能據此判定英文能力較強。 | readability | SweetRing 在地化涵蓋美國、墨西哥、巴西、印尼、馬來西亞、日本、韓國 7 個市場；與最多約 10 位外國實習生協作，在無直屬管理關係下以英文分派 UI/UX 翻譯與多國粉專經營任務。 | SweetRing 在地化涵蓋美國、墨西哥、巴西、印尼、馬來西亞、日本、韓國 7 個市場；與最多約 10 位外國實習生協作，在無直屬管理關係下分派翻譯與粉專經營任務。 |
- 理由（≤120 字）：甲提供推薦規則診斷與分析分工的不同證據，更能聚焦驗證產品洞察、數據判斷及英文協作；共有的AI上線、定價實驗與0到1經歷不重複加分，音樂應用仍須面試驗證。


# jd47｜逐次輸出


## A-jd47-K｜履歷K

```json
{"rubric_version": "4.2", "resume_id": "K", "job_id": "jd47", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd47-K", "human_calibrated": false, "requirements": [{"id": "R01", "text": "3年以上Software Product Manager經驗", "type": "required", "status": "supported", "evidence": ["Product Manager｜尚凡國際創新科技"], "blocks_interview": false, "reason": "2018–2022 軟體產品經驗及現職足以支持年資。"}, {"id": "R02", "text": "完整0到1探索、驗證、設計、開發、上線與迭代直接負責", "type": "required", "status": "partial", "evidence": ["主導 Juicy 上線"], "blocks_interview": false, "reason": "有主導上線與付費牆設計；同一產品完整探索及驗證鏈需面試確認。"}, {"id": "R03", "text": "清楚規格文件：PRD、流程圖、資料結構", "type": "required", "status": "partial", "evidence": ["整理為 PRD 與 Axure Prototype"], "blocks_interview": false, "reason": "PRD與流程有實例，資料結構文件未呈現。"}, {"id": "R04", "text": "理解API、JSON與基本SQL", "type": "required", "status": "partial", "evidence": ["API 串接規劃、舊系統資料盤點"], "blocks_interview": false, "reason": "API有規劃與付款串接線索；JSON與基本SQL未知，宜用工作樣本核對。"}, {"id": "R05", "text": "多元專案、成熟產品迭代及時程範圍管理", "type": "required", "status": "supported", "evidence": ["另於 2026/01–06 上線 111 項 Roadmap 細項"], "blocks_interview": false, "reason": "既有系統改版、優先序與上線驗收直接相關。"}, {"id": "R06", "text": "商業模式、產業競品分析與產品策略、GTM及Growth", "type": "required", "status": "partial", "evidence": ["依結果全面調降售價"], "blocks_interview": false, "reason": "定價與導流有案例；產業趨勢研究及完整GTM規劃責任待問。"}, {"id": "R07", "text": "內外部產品教育訓練與上線測試驗收", "type": "required", "status": "partial", "evidence": ["與 QA 制定 UAT 驗收案例"], "blocks_interview": false, "reason": "驗收具體，客服說明可轉移；完整內外部訓練規劃未呈現。"}, {"id": "R08", "text": "跨部門資源優先序與協作溝通", "type": "required", "status": "supported", "evidence": ["對接 16 個需求單位"], "blocks_interview": false, "reason": "有工程、QA、客服協作與需求排序。"}, {"id": "R09", "text": "停車、交通、MaaS、保險、支付或FinTech經驗", "type": "preferred", "status": "supported", "evidence": ["並與 CodaPay 新加坡技術團隊協調串接"], "blocks_interview": false, "reason": "支付整合符合列舉之一，非停車領域證據。"}, {"id": "R10", "text": "Prompt engineering、RAG或Agent實作", "type": "preferred", "status": "unknown", "evidence": [], "blocks_interview": false, "reason": "AI功能協作不能直接證明上述個人實作。"}, {"id": "R11", "text": "Growth或數據分析經驗", "type": "preferred", "status": "supported", "evidence": ["以 Android 售價不變作對照"], "blocks_interview": false, "reason": "定價實驗與留存分析支持。"}, {"id": "R12", "text": "AI/LLM工具用於規格、資料、自動化或原型", "type": "preferred", "status": "supported", "evidence": ["用於規格撰寫、資料整理與分析"], "blocks_interview": false, "reason": "Claude Code具體用途對應。"}], "dimensions": [{"id": "positioning", "rating": "強", "evidence": ["近 10 年 PM 經驗，經手 6 款產品"], "missing": ["停車場景可到職學習；以支付、B2B流程經驗轉移。"], "issue_ids": []}, {"id": "role_evidence", "rating": "足夠", "evidence": ["整理為 PRD 與 Axure Prototype"], "missing": ["完整0到1鏈、JSON/SQL、資料結構與訓練需驗證。"], "issue_ids": ["I01", "I02", "I03"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": ["可追問產業研究如何形成策略。"], "issue_ids": ["I04"]}, {"id": "outcome_quality", "rating": "足夠", "evidence": ["為觀察差異，非因果"], "missing": ["年化留存估算、實驗可比性與安全監測範圍需核對。"], "issue_ids": ["I05"]}, {"id": "ownership", "rating": "強", "evidence": ["由我主責規劃，與工程團隊密切協作"], "missing": ["GTM與方向決策的最終權責待問。"], "issue_ids": []}, {"id": "readability", "rating": "足夠", "evidence": ["為產品上線與行銷導流期間的整體表現"], "missing": ["摘要與自傳略重複，可精簡提升檢索效率。"], "issue_ids": []}], "results": [{"quote": "全站活躍付費廠商約 6.6 萬家", "kinds": ["context"]}, {"quote": "約 50 項大項功能上線", "kinds": ["output"]}, {"quote": "需求平均處理週期由 100.4 天降至 30.9 天", "kinds": ["outcome"]}, {"quote": "該群年化留存 81.2%，同期全站 74.2%", "kinds": ["outcome"]}, {"quote": "依結果全面調降售價", "kinds": ["decision"]}, {"quote": "目前專案仍在開發中", "kinds": ["in_progress"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["近 10 年 PM 經驗，經手 6 款產品"], "application_note": "軟體PM、支付與交付支持面試"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "近期B2B流程經驗可轉移"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "application_note": "規劃與工程責任有區分"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "有流程成果，需核對統計口徑"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "兼顧既有用戶與資料限制"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["從交友與訂閱制 App 到企業招募系統"], "application_note": "責任跨變現與企業流程"}, {"rule_id": "HR07", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例"], "application_note": "工具與協作連到交付情境"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["現任 1111 招募系統 Product Owner"], "application_note": "定位與近期範圍易辨識"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["該群年化留存 81.2%，同期全站 74.2%"], "application_note": "年化方式與監測來源待核對"}, {"rule_id": "HR10", "status": "supported", "resume_evidence": ["接下來，我希望將更多心力放回產品策略"], "application_note": "方向與策略職責相容"}, {"rule_id": "HR11", "status": "unknown", "resume_evidence": ["錄取後三週可上班"], "application_note": "JD未列到職及地點，無已知衝突"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["主導 Juicy 上線"], "application_note": "可約談驗證完整0到1及技術理解"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["訂閱制 B2C App 與雙邊媒合平台"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["最大宗是溝通管道中斷"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM04", "primary_dimension": "decision_depth", "status": "partial", "resume_evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "partial", "resume_evidence": ["為觀察差異，非因果"], "evidence_type": "outcome", "source_ids": [], "interview_question": null}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["與資料科學團隊合作，定義使用情境與驗收標準"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["第一階段於 2025/10 離峰切換上線"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "partial", "resume_evidence": ["API 串接規劃、舊系統資料盤點"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM09", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["為產品上線與行銷導流期間的整體表現"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["規劃由 App 內購轉向網頁付款"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM13", "primary_dimension": "role_evidence", "status": "not_applicable", "resume_evidence": [], "evidence_type": null, "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HM07", "source_ids": [], "application_note": "面試追問，不據缺漏否定能力", "context_limit": "僅文字履歷自述，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "主導 Juicy 上線", "reason": "同一產品完整0到1探索驗證至迭代未完整呈現", "suggestion": "選Juicy說明探索假設、驗證與上線後迭代。"}, {"id": "I02", "rule_id": "HM08", "source_ids": [], "application_note": "面試追問，不據缺漏否定能力", "context_limit": "僅文字履歷自述，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "API 串接規劃、舊系統資料盤點", "reason": "JSON、基本SQL與資料結構文件未呈現", "suggestion": "用去識別API payload、資料模型與SQL工作樣本驗證。"}, {"id": "I03", "rule_id": "HR07", "source_ids": [], "application_note": "面試追問，不據缺漏否定能力", "context_limit": "僅文字履歷自述，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "與 QA 制定 UAT 驗收案例", "reason": "驗收明確但內外部教育訓練規劃未知", "suggestion": "追問訓練對象、材料、安排與理解度確認。"}, {"id": "I04", "rule_id": "HM04", "source_ids": [], "application_note": "面試追問，不據缺漏否定能力", "context_limit": "僅文字履歷自述，未外部查證", "category": "ownership", "severity": "interview_follow_up", "block_target": null, "claim": "配合行銷導入原 iOS App 下架後的用戶", "reason": "GTM及產業研究責任界線未完全呈現", "suggestion": "說明產業競品資訊如何影響產品與資源選擇。"}, {"id": "I05", "rule_id": "HM05", "source_ids": [], "application_note": "面試追問，不據缺漏否定能力", "context_limit": "僅文字履歷自述，未外部查證", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "該群年化留存 81.2%，同期全站 74.2%", "reason": "短期快照年化方法、實驗可比性及安全監測口徑待核對", "suggestion": "交代計算方式、樣本限制及資料來源；不補造因果。"}], "decision": {"recommendation": "interview", "evidence": ["主導 Juicy 上線", "與 QA 制定 UAT 驗收案例", "並與 CodaPay 新加坡技術團隊協調串接"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["主導上線與成熟產品迭代直接相關", "支付串接與定價分析對應商業需求", "跨部門驗收交付與明確取捨具面試價值"], "key_gaps": ["完整0到1探索驗證鏈", "JSON、SQL及資料結構實務", "教育訓練與GTM策略責任"], "strengths": ["交付與跨部門權責具體", "支付與定價案例對應商業分析", "量測承認非因果與團隊成果邊界"], "interview_questions": ["請選一款0到1產品，串起探索、驗證、設計、開發、上線及迭代，指出你的直接責任。", "請用去識別例子說明API JSON資料結構，並寫出基本SQL查詢。", "內外部產品訓練如何規劃、驗證理解並支援上線？", "產業競品研究如何影響GTM、優先序及資源配置，誰決定？", "留存年化公式、快照樣本與工單處理週期分母為何？", "定價實驗各平台同期有何干擾，如何支持全面調價？", "未再遭冒用依何種監測或回報來源，觀察範圍為何？"], "editorial_appendix": ["可精簡摘要與自傳重複資訊；不影響招聘決定。"], "spectrum": {"level": 8, "uncertainty_levels": 1, "basis": "多個交付、商業與取捨案例，提供比較期間與限制；技術必備細項及完整0到1鏈仍需面試驗證。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷 K｜第 1 輪｜model_id: unknown

### 1. 結論

- 招聘決定：interview

- Level：8（±1）

- 一句話理由：「主導 Juicy 上線」及支付、迭代案例支持面試，完整探索鏈與技術細項待驗證。

### 2. 六維度

| 維度 | 評等 | 證據原句（≤40 字） | 缺什麼／對面試的影響 |

| :-- | :-- | :-- | :-- |

| positioning | 強 | 近 10 年 PM 經驗，經手 6 款產品 | 停車場景可到職學習；以支付、B2B流程經驗轉移。 |

| role_evidence | 足夠 | 整理為 PRD 與 Axure Prototype | 完整0到1鏈、JSON/SQL、資料結構與訓練需驗證。 |

| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 可追問產業研究如何形成策略。 |

| outcome_quality | 足夠 | 為觀察差異，非因果 | 年化留存估算、實驗可比性與安全監測範圍需核對。 |

| ownership | 強 | 由我主責規劃，與工程團隊密切協作 | GTM與方向決策的最終權責待問。 |

| readability | 足夠 | 為產品上線與行銷導流期間的整體表現 | 摘要與自傳略重複，可精簡提升檢索效率。 |

### 3. JD 條件對照

| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |

| :-- | :-- | :-- | :-- | :-- |

| 3年以上Software Product Manager經驗 | 必要 | supported | Product Manager｜尚凡國際創新科技 | 2018–2022 軟體產品經驗及現職足以支持年資。 |

| 完整0到1探索、驗證、設計、開發、上線與迭代直接負責 | 必要 | partial | 主導 Juicy 上線 | 有主導上線與付費牆設計；同一產品完整探索及驗證鏈需面試確認。 |

| 清楚規格文件：PRD、流程圖、資料結構 | 必要 | partial | 整理為 PRD 與 Axure Prototype | PRD與流程有實例，資料結構文件未呈現。 |

| 理解API、JSON與基本SQL | 必要 | partial | API 串接規劃、舊系統資料盤點 | API有規劃與付款串接線索；JSON與基本SQL未知，宜用工作樣本核對。 |

| 多元專案、成熟產品迭代及時程範圍管理 | 必要 | supported | 另於 2026/01–06 上線 111 項 Roadmap 細項 | 既有系統改版、優先序與上線驗收直接相關。 |

| 商業模式、產業競品分析與產品策略、GTM及Growth | 必要 | partial | 依結果全面調降售價 | 定價與導流有案例；產業趨勢研究及完整GTM規劃責任待問。 |

| 內外部產品教育訓練與上線測試驗收 | 必要 | partial | 與 QA 制定 UAT 驗收案例 | 驗收具體，客服說明可轉移；完整內外部訓練規劃未呈現。 |

| 跨部門資源優先序與協作溝通 | 必要 | supported | 對接 16 個需求單位 | 有工程、QA、客服協作與需求排序。 |

| 停車、交通、MaaS、保險、支付或FinTech經驗 | 加分 | supported | 並與 CodaPay 新加坡技術團隊協調串接 | 支付整合符合列舉之一，非停車領域證據。 |

| Prompt engineering、RAG或Agent實作 | 加分 | unknown | 未呈現 | AI功能協作不能直接證明上述個人實作。 |

| Growth或數據分析經驗 | 加分 | supported | 以 Android 售價不變作對照 | 定價實驗與留存分析支持。 |

| AI/LLM工具用於規格、資料、自動化或原型 | 加分 | supported | 用於規格撰寫、資料整理與分析 | Claude Code具體用途對應。 |

工作職責列以必要工作內容對照，不將未呈現誤列為不符合。無明文必要條件之 contradicted。

### 4. HR 十二問 ／ HM 十三問

| 題 | 狀態 | 證據（1 句） | 招聘意義（≤30 字） |

| :-- | :-- | :-- | :-- |

| HR01 | supported | 近 10 年 PM 經驗，經手 6 款產品 | 軟體PM、支付與交付支持面試 |

| HR02 | supported | 企業端招募系統全模組與求職端公司頁 | 近期B2B流程經驗可轉移 |

| HR03 | supported | 由我主責規劃，與工程團隊密切協作 | 規劃與工程責任有區分 |

| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 有流程成果，需核對統計口徑 |

| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 兼顧既有用戶與資料限制 |

| HR06 | supported | 從交友與訂閱制 App 到企業招募系統 | 責任跨變現與企業流程 |

| HR07 | supported | 與 QA 制定 UAT 驗收案例 | 工具與協作連到交付情境 |

| HR08 | supported | 現任 1111 招募系統 Product Owner | 定位與近期範圍易辨識 |

| HR09 | partial | 該群年化留存 81.2%，同期全站 74.2% | 年化方式與監測來源待核對 |

| HR10 | supported | 接下來，我希望將更多心力放回產品策略 | 方向與策略職責相容 |

| HR11 | unknown | 錄取後三週可上班 | JD未列到職及地點，無已知衝突 |

| HR12 | supported | 主導 Juicy 上線 | 可約談驗證完整0到1及技術理解 |

| HM01 | supported | 訂閱制 B2C App 與雙邊媒合平台 | 支付與成熟迭代有轉移性 |

| HM02 | supported | 最大宗是溝通管道中斷 | 客服訊號改變優先序 |

| HM03 | supported | 選擇首次登入引導確認、不強迫修改 | 具體限制與方案取捨 |

| HM04 | partial | 依抽成、稅、手續費及撥款週期做實收試算 | 商業分析具體，產業策略待問 |

| HM05 | partial | 為觀察差異，非因果 | 限制有交代，量測仍需核對 |

| HM06 | supported | 與資料科學團隊合作，定義使用情境與驗收標準 | 個人與技術團隊分工可辨 |

| HM07 | supported | 第一階段於 2025/10 離峰切換上線 | 分階段上線與品質風險具體 |

| HM08 | partial | API 串接規劃、舊系統資料盤點 | JSON與SQL能力待樣本驗證 |

| HM09 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 跨部門複雜交付有依據 |

| HM10 | supported | 為產品上線與行銷導流期間的整體表現 | 結果邊界清楚可理解 |

| HM11 | supported | 依客服測試回饋調整推薦規則 | 回饋形成修正行為 |

| HM12 | supported | 規劃由 App 內購轉向網頁付款 | 約談可驗證支付與完整產品鏈 |

| HM13 | not_applicable | 方法層，非履歷能力證據 | 方法題，依本JD獨立評估不加分 |

### 5. 約談理由（≤3）與關鍵缺口（≤3）

| # | 約談理由（引原句） |

| :-- | :-- |

| 1 | 「主導 Juicy 上線」與成熟迭代符合交付需求 |

| 2 | 「並與 CodaPay 新加坡技術團隊協調串接」具支付實務 |

| 3 | 「選擇首次登入引導確認、不強迫修改」呈現取捨 |

| # | 關鍵缺口 | 面試追問 |

| :-- | :-- | :-- |

| 1 | 完整0到1探索驗證鏈 | 請選一款0到1產品，串起探索、驗證、設計、開發、上線及迭代，指出你的直接責任。 |

| 2 | JSON、SQL及資料結構實務 | 請用去識別例子說明API JSON資料結構，並寫出基本SQL查詢。 |

| 3 | 教育訓練與GTM策略責任 | 內外部產品訓練如何規劃、驗證理解並支援上線？ |

其他追問：

- 產業競品研究如何影響GTM、優先序及資源配置，誰決定？

- 留存年化公式、快照樣本與工單處理週期分母為何？

- 定價實驗各平台同期有何干擾，如何支持全面調價？

- 未再遭冒用依何種監測或回報來源，觀察範圍為何？

### 6. 評語（給寫稿者的具體回饋）

**做得好（3 點）**

- 1111交付｜「由我主責規劃，與工程團隊密切協作」｜清楚區分規劃與工程協作，符合專案橋樑責任。

- 尚凡定價｜「以 Android 售價不變作對照」｜商業選擇有比較依據，支持策略約談。

- 1111留存｜「為觀察差異，非因果」｜主動界定衡量限制，避免把觀察當產品歸因。

**可改進（5 點）**

- 位置：尚凡Juicy

  - 原句：主導 Juicy 上線

  - 問題類型：requirement

  - 嚴重度：interview_follow_up

  - 影響：同一產品完整0到1探索驗證至迭代未完整呈現；保留面試，釐清相關能力與口徑。

  - 建議方向：選Juicy說明探索假設、驗證與上線後迭代。

- 位置：專業技能與相關經歷

  - 原句：API 串接規劃、舊系統資料盤點

  - 問題類型：requirement

  - 嚴重度：interview_follow_up

  - 影響：JSON、基本SQL與資料結構文件未呈現；保留面試，釐清相關能力與口徑。

  - 建議方向：用去識別API payload、資料模型與SQL工作樣本驗證。

- 位置：1111驗收

  - 原句：與 QA 制定 UAT 驗收案例

  - 問題類型：requirement

  - 嚴重度：interview_follow_up

  - 影響：驗收明確但內外部教育訓練規劃未知；保留面試，釐清相關能力與口徑。

  - 建議方向：追問訓練對象、材料、安排與理解度確認。

- 位置：尚凡Juicy與策略經歷

  - 原句：配合行銷導入原 iOS App 下架後的用戶

  - 問題類型：ownership

  - 嚴重度：interview_follow_up

  - 影響：GTM及產業研究責任界線未完全呈現；保留面試，釐清相關能力與口徑。

  - 建議方向：說明產業競品資訊如何影響產品與資源選擇。

- 位置：1111留存與成果衡量

  - 原句：該群年化留存 81.2%，同期全站 74.2%

  - 問題類型：measurement

  - 嚴重度：interview_follow_up

  - 影響：短期快照年化方法、實驗可比性及安全監測口徑待核對；保留面試，釐清相關能力與口徑。

  - 建議方向：交代計算方式、樣本限制及資料來源；不補造因果。

**編輯附件**（不影響判斷）：可精簡摘要與自傳重複敘述。

### 7. 資深能力分布

delivery：強 ／ po_coordination：強 ／ direction_resources：足夠

方向與資源有優先序及定價決策線索，但未完整呈現產業策略與跨部門資源決策權；不以團隊人數推論管理能力。

### 8. 未測試聲明

PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run

所有成果均為履歷自述，內部一致性不等於外部查證。此為單輪獨立審查，不跨JD平均Level。

### 成果分類補表

| 成果或數字原句 | 分類 | 解讀限制 |

| :-- | :-- | :-- |

| 全站活躍付費廠商約 6.6 萬家 | context | 依正文口徑，非外部查核 |

| 約 50 項大項功能上線 | output | 依正文口徑，非外部查核 |

| 需求平均處理週期由 100.4 天降至 30.9 天 | outcome | 依正文口徑，非外部查核 |

| 該群年化留存 81.2%，同期全站 74.2% | outcome | 依正文口徑，非外部查核 |

| 依結果全面調降售價 | decision | 依正文口徑，非外部查核 |

| 目前專案仍在開發中 | in_progress | 依正文口徑，非外部查核 |

| 對接 16 個需求單位 | context | 協作範圍，不是影響 |

| 近 10 年 PM 經驗，經手 6 款產品 | context | 經驗範圍，不自動加分 |

| 團隊 3 名企劃 | context | 不推論帶人能力 |

| 另於 2026/01–06 上線 111 項 Roadmap 細項 | output | 細項與50大項不可相加 |

| 盤點出上千組重複 E-mail | context | 問題規模 |

| 選擇首次登入引導確認、不強迫修改 | decision | 既有用戶限制下取捨 |

| 停機約 1.5 小時 | output | 切換運作紀錄，非改善幅度 |

| 2026/04 十多家廠商帳號遭冒用 | context | 事件背景 |

| 與工程協作於 2026/04/17 上線簽章驗證 | output | 交付成果 |

| 上線後至 2026/10 未再出現同類帳號冒用 | outcome | 目前掌握情況，非證明零事件 |

| 完成 1,726／1,857 張需求與問題單，約 93% | output | 至09/29處理量，不等於使用者結果 |

| 需求管線觸及 1,279 家活躍付費廠商 | context | 觸及母體，非歸因 |

| 約占全站 66,150 家的 1.9% | context | 基準日與觸及範圍 |

| AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才 | output | 功能交付非個人RAG實作 |

| 依客服測試回饋調整推薦規則 | decision | 回饋驅動修正 |

| 各期 21 天 | context | 實驗時窗 |

| 降價期 iOS 非續訂營收較基準期增 5% | outcome | 同期對照仍待混淆因素確認 |

| Android 減 18%，相對變化約多 28% | outcome | 相對變化，非單純百分點 |

| 還原原價後 iOS 較基準期減 65% | outcome | 期間比較非直接因果 |

| Peach 網頁付款占營收由 24% 至 80% 以上 | outcome | 付款占比改變非營收成長 |

| KOOL 訂閱與付費牆規劃上線 | output | 功能設計交付 |

| 設定檔案完成、社群認證及照片門檻 | decision | 供給資格規則 |

| 主導 Juicy 上線 | output | 非完整探索驗證證據 |

| 上線後 6 週男性 DAU 約 3,200 至 1.25 萬 | outcome | 產品與行銷共同期間成果 |

| 7 個市場 | context | 在地化範圍 |

| 最多約 10 位外國實習生協作 | context | 無直屬關係 |

| 導入 CodaPay | output | 付款選項交付 |

| 提出 7／30／90 天訂閱方案與加贈內容 | output/decision | 試算後方案，未呈現轉換收益 |

| Newegg.com 商品資訊英翻中與校對 | output | 早期工作交付 |

| 將信件與即時通整合排在其他新功能之前 | decision/in_progress | 已排序但開發中，不列實現成效 |


## A-jd47-M｜履歷M

```json
{"rubric_version": "4.2", "resume_id": "M", "job_id": "jd47", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd47-M", "human_calibrated": false, "requirements": [{"id": "R01", "text": "3年以上 Software Product Manager 經驗", "type": "required", "status": "supported", "evidence": ["近 10 年 PM 經驗"], "blocks_interview": false, "reason": "具連續軟體產品規劃與交付經歷。"}, {"id": "R02", "text": "完整0到1探索、驗證、設計、開發、上線與迭代直接負責", "type": "required", "status": "partial", "evidence": ["主導 Juicy 上線"], "blocks_interview": false, "reason": "有新產品上線與設計案例；單一產品完整探索驗證及迭代責任待確認。"}, {"id": "R03", "text": "清楚規格文件：PRD、流程圖、資料結構", "type": "required", "status": "partial", "evidence": ["整理為 PRD 與 Axure Prototype"], "blocks_interview": false, "reason": "PRD與流程有案例，資料結構文件深度需看樣本。"}, {"id": "R04", "text": "理解API、JSON與基本SQL", "type": "required", "status": "partial", "evidence": ["API 串接規劃、舊系統資料盤點"], "blocks_interview": false, "reason": "API有線索；JSON及基本SQL未呈現，不推論不會。"}, {"id": "R05", "text": "多元專案管理、MVP與成熟產品迭代", "type": "required", "status": "supported", "evidence": ["三階段推進招募系統改版"], "blocks_interview": false, "reason": "產品上線、改版、範圍及驗收可支持約談。"}, {"id": "R06", "text": "商業模式、產業趨勢、競品與用戶需求分析", "type": "required", "status": "partial", "evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "blocks_interview": false, "reason": "商業與競品案例具體，產業趨勢研究及策略方法需釐清。"}, {"id": "R07", "text": "內外部產品教育訓練與上線測試驗收", "type": "required", "status": "partial", "evidence": ["與 QA 制定 UAT 驗收案例"], "blocks_interview": false, "reason": "驗收充分；客服說明有線索，完整內外部教育訓練未呈現。"}, {"id": "R08", "text": "跨部門資源優先序、溝通與整合", "type": "required", "status": "supported", "evidence": ["對接 16 個需求單位"], "blocks_interview": false, "reason": "具排優先級及工程、客服協作案例。"}, {"id": "R09", "text": "停車、交通、MaaS、保險、支付或FinTech經驗", "type": "preferred", "status": "supported", "evidence": ["與 CodaPay 新加坡技術團隊協調串接"], "blocks_interview": false, "reason": "支付串接相關，不延伸認定具停車或交通經驗。"}, {"id": "R10", "text": "Prompt engineering、RAG或Agent實作", "type": "preferred", "status": "partial", "evidence": ["自建 Claude Code 協作流程"], "blocks_interview": false, "reason": "工具流程實作有線索，未說明提示工程或Agent架構。"}, {"id": "R11", "text": "Growth或數據分析經驗", "type": "preferred", "status": "supported", "evidence": ["以 Android 售價不變作對照"], "blocks_interview": false, "reason": "定價實驗與留存比較直接相關。"}, {"id": "R12", "text": "AI/LLM用於規格、資料、自動化或原型", "type": "preferred", "status": "supported", "evidence": ["用於規格撰寫、資料整理與分析"], "blocks_interview": false, "reason": "有自建AI協作流程自述，可驗證實際工作樣本。"}], "dimensions": [{"id": "positioning", "rating": "強", "evidence": ["訂閱制 B2C App 與雙邊媒合平台。"], "missing": ["交通場景可轉移程度於面試釐清"], "issue_ids": []}, {"id": "role_evidence", "rating": "足夠", "evidence": ["與 QA 制定 UAT 驗收案例"], "missing": ["完整0到1及JSON、SQL和訓練經驗待核對"], "issue_ids": ["I01", "I02", "I03"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": ["可追問替代方案與決策權限"], "issue_ids": []}, {"id": "outcome_quality", "rating": "強", "evidence": ["為觀察差異，非因果。"], "missing": ["安全事件與年化留存口徑待追問"], "issue_ids": ["I04"]}, {"id": "ownership", "rating": "強", "evidence": ["由我主責規劃，與工程團隊密切協作"], "missing": ["整體成長需維持團隊歸因"], "issue_ids": []}, {"id": "readability", "rating": "足夠", "evidence": ["近 10 年 PM 經驗"], "missing": ["可將0到1及技術案例前置"], "issue_ids": ["I05"]}], "results": [{"quote": "約 50 項大項功能上線", "kinds": ["output"]}, {"quote": "需求平均處理週期由 100.4 天降至 30.9 天", "kinds": ["outcome"]}, {"quote": "該群年化留存 81.2%，同期全站 74.2%", "kinds": ["outcome"]}, {"quote": "相對變化約多 28%", "kinds": ["outcome"]}, {"quote": "Peach 網頁付款占營收由 24% 至 80% 以上", "kinds": ["outcome"]}, {"quote": "兩案皆開發中", "kinds": ["in_progress"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["近 10 年 PM 經驗"], "application_note": "交付、支付與數據經驗相關"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "近期產品範圍清楚"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "application_note": "個人與工程責任可辨識"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "有交付與流程變化"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "具既有客戶風險取捨"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["從交友與訂閱制 App 到企業招募系統"], "application_note": "責任與領域轉移可辨識"}, {"rule_id": "HR07", "status": "supported", "resume_evidence": ["與 CodaPay 新加坡技術團隊協調串接"], "application_note": "協作技能有實務情境"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["現任 1111 招募系統 Product Owner"], "application_note": "摘要與案例可快速定位"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["上線後至 2026/10 未再出現同類帳號冒用"], "application_note": "追問觀測來源與範圍"}, {"rule_id": "HR10", "status": "supported", "resume_evidence": ["我希望將更多心力放回產品策略"], "application_note": "方向與策略職責相容"}, {"rule_id": "HR11", "status": "unknown", "resume_evidence": ["錄取後三週可上班"], "application_note": "JD未列地點到職限制，無已知衝突"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["主導 Juicy 上線"], "application_note": "具約談價值，驗證完整生命週期"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["訂閱制 B2C App 與雙邊媒合平台。"], "evidence_type": "context", "source_ids": [], "interview_question": "如何將訂閱與企業產品經驗轉用到交通產品？"}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["查出根因是名單依履歷修改日排序"], "evidence_type": "decision", "source_ids": [], "interview_question": "客服訊號如何驗證為排序問題？"}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["改版排在新功能職缺健檢之前"], "evidence_type": "decision", "source_ids": [], "interview_question": "如何比較價值、成本及不同部門優先序？"}, {"rule_id": "HM04", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依抽成、稅、手續費及撥款週期做實收試算"], "evidence_type": "decision", "source_ids": [], "interview_question": "實收試算如何影響支付及訂閱選擇？"}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "supported", "resume_evidence": ["為觀察差異，非因果。"], "evidence_type": "outcome", "source_ids": [], "interview_question": "年化留存如何計算，如何處理選樣差異？"}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["與資料科學團隊合作，定義使用情境與驗收標準"], "evidence_type": "output", "source_ids": [], "interview_question": "你與資料科學團隊的驗收責任如何切分？"}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例"], "evidence_type": "output", "source_ids": [], "interview_question": "請示範上線驗收、回滾及風險管理。"}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "partial", "resume_evidence": ["API 串接規劃、舊系統資料盤點"], "evidence_type": "context", "source_ids": [], "interview_question": "請以API案例說明JSON欄位並寫基本SQL。"}, {"rule_id": "HM09", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "evidence_type": "output", "source_ids": [], "interview_question": "跨部門衝突如何決策、誰批准資源？"}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["從需求釐清、系統分析到 PRD、原型、UAT 與上線計畫"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則"], "evidence_type": "decision", "source_ids": [], "interview_question": "回饋改變了哪些規則，如何判斷改善？"}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["主導 Juicy 上線"], "evidence_type": "output", "source_ids": [], "interview_question": "請用單一案例串起0到1探索至上線後迭代。"}, {"rule_id": "HM13", "primary_dimension": "role_evidence", "status": "not_applicable", "resume_evidence": [], "evidence_type": null, "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HM12", "source_ids": [], "application_note": "面試核對完整0到1責任；不是已證明不符。", "context_limit": "僅依履歷文字，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "主導 Juicy 上線", "reason": "新產品交付清楚，但未完整連結探索、驗證及迭代。", "suggestion": "補一個單一產品生命週期與本人責任。"}, {"id": "I02", "rule_id": "HM08", "source_ids": [], "application_note": "面試用小型工作樣本確認明文技術條件。", "context_limit": "僅依履歷文字，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "API 串接規劃、舊系統資料盤點", "reason": "JSON、SQL及資料結構設計深度未直接呈現。", "suggestion": "僅補實際使用過的JSON、SQL及資料模型案例。"}, {"id": "I03", "rule_id": "HR07", "source_ids": [], "application_note": "追問業務、財務與合作夥伴教育經驗。", "context_limit": "僅依履歷文字，未外部查證", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "驗證流程及客服說明", "reason": "客服說明不能完整替代內外部產品訓練證據。", "suggestion": "若有實例，交代對象、教材與操作驗證。"}, {"id": "I04", "rule_id": "HM05", "source_ids": [], "application_note": "核對資訊來源；不直接否定安全改善。", "context_limit": "僅依履歷文字，未外部查證", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "上線後至 2026/10 未再出現同類帳號冒用", "reason": "這是目前掌握情況，非完整監控已證明零事件。", "suggestion": "保留限制並說明觀測來源、涵蓋範圍。"}, {"id": "I05", "rule_id": "HM10", "source_ids": [], "application_note": "編輯可提升辨識效率，不改變能力判斷。", "context_limit": "僅依履歷文字，未外部查證", "category": "readability", "severity": "editorial", "block_target": null, "claim": "近 10 年 PM 經驗", "reason": "直接對應完整0到1與技術條件的資訊較分散。", "suggestion": "前置單一0到1案例及已具備的技術證據。"}], "decision": {"recommendation": "interview", "evidence": ["主導 Juicy 上線", "與 CodaPay 新加坡技術團隊協調串接", "選擇首次登入引導確認、不強迫修改"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["新產品上線與成熟系統改版皆有實例", "支付與定價分析直接對應加分能力", "有具體使用者問題、取捨及跨部門交付"], "key_gaps": ["完整0到1探索驗證至迭代的直接責任鏈", "JSON、基本SQL與資料結構實作深度", "內外部教育訓練及產業策略研究範圍"], "strengths": ["責任邊界與交付動作清楚", "取捨連結既有客戶風險", "數據區分觀察差異與因果"], "interview_questions": ["請用單一產品說明0到1探索、驗證、設計、開發、上線與迭代責任。", "請用支付API案例解釋JSON資料結構及錯誤處理，示範基本SQL。", "如何規劃內部業務、客服、財務及外部夥伴的教育訓練？", "定價實驗如何處理期間差異、樣本與外部干擾？", "年化留存如何計算，如何處理兩組客戶的選樣差異？", "登入安全改善的觀測範圍、來源及通報機制為何？", "市場與競品研究如何轉為策略及跨部門資源配置？", "Claude Code流程由你實作哪些部分，有何可展示的成果？"], "editorial_appendix": [], "spectrum": {"level": 8, "uncertainty_levels": 1, "basis": "多個相關案例具取捨、比較基準及限制；完整0到1和部分技術資格仍需面試驗證。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```

## 單份審查｜履歷｜第 1 輪｜model_id: unknown

### 1. 結論
- 招聘決定：interview
- Level：8（±1）
- 一句話理由：「主導 Juicy 上線」及支付、改版案例支持面試，完整生命週期與技術細節待核對。

### 2. 六維度
| 維度 | 評等 | 證據原句 | 缺什麼／對面試的影響 |
| :-- | :-- | :-- | :-- |
| positioning | 強 | 訂閱制 B2C App 與雙邊媒合平台。 | 交通場景可轉移程度於面試釐清 |
| role_evidence | 足夠 | 與 QA 制定 UAT 驗收案例 | 完整0到1及JSON、SQL和訓練經驗待核對 |
| decision_depth | 強 | 選擇首次登入引導確認、不強迫修改 | 可追問替代方案與決策權限 |
| outcome_quality | 強 | 為觀察差異，非因果。 | 安全事件與年化留存口徑待追問 |
| ownership | 強 | 由我主責規劃，與工程團隊密切協作 | 整體成長需維持團隊歸因 |
| readability | 足夠 | 近 10 年 PM 經驗 | 可將0到1及技術案例前置 |

### 3. JD 條件對照
| 條件 | 必要/加分 | 狀態 | 履歷證據 | 備註 |
| :-- | :-- | :-- | :-- | :-- |
| 3年以上 Software Product Manager 經驗 | 必要 | supported | 近 10 年 PM 經驗 | 具連續軟體產品規劃與交付經歷。 |
| 完整0到1探索、驗證、設計、開發、上線與迭代直接負責 | 必要 | partial | 主導 Juicy 上線 | 有新產品上線與設計案例；單一產品完整探索驗證及迭代責任待確認。 |
| 清楚規格文件：PRD、流程圖、資料結構 | 必要 | partial | 整理為 PRD 與 Axure Prototype | PRD與流程有案例，資料結構文件深度需看樣本。 |
| 理解API、JSON與基本SQL | 必要 | partial | API 串接規劃、舊系統資料盤點 | API有線索；JSON及基本SQL未呈現，不推論不會。 |
| 多元專案管理、MVP與成熟產品迭代 | 必要 | supported | 三階段推進招募系統改版 | 產品上線、改版、範圍及驗收可支持約談。 |
| 商業模式、產業趨勢、競品與用戶需求分析 | 必要 | partial | 依抽成、稅、手續費及撥款週期做實收試算 | 商業與競品案例具體，產業趨勢研究及策略方法需釐清。 |
| 內外部產品教育訓練與上線測試驗收 | 必要 | partial | 與 QA 制定 UAT 驗收案例 | 驗收充分；客服說明有線索，完整內外部教育訓練未呈現。 |
| 跨部門資源優先序、溝通與整合 | 必要 | supported | 對接 16 個需求單位 | 具排優先級及工程、客服協作案例。 |
| 停車、交通、MaaS、保險、支付或FinTech經驗 | 加分 | supported | 與 CodaPay 新加坡技術團隊協調串接 | 支付串接相關，不延伸認定具停車或交通經驗。 |
| Prompt engineering、RAG或Agent實作 | 加分 | partial | 自建 Claude Code 協作流程 | 工具流程實作有線索，未說明提示工程或Agent架構。 |
| Growth或數據分析經驗 | 加分 | supported | 以 Android 售價不變作對照 | 定價實驗與留存比較直接相關。 |
| AI/LLM用於規格、資料、自動化或原型 | 加分 | supported | 用於規格撰寫、資料整理與分析 | 有自建AI協作流程自述，可驗證實際工作樣本。 |

### 4. HR 十二問 ／ HM 十三問
| 題 | 狀態 | 證據（1句） | 招聘意義 |
| :-- | :-- | :-- | :-- |
| HR01 | supported | 近 10 年 PM 經驗 | 交付、支付與數據經驗相關 |
| HR02 | supported | 企業端招募系統全模組與求職端公司頁 | 近期產品範圍清楚 |
| HR03 | supported | 由我主責規劃，與工程團隊密切協作 | 個人與工程責任可辨識 |
| HR04 | supported | 需求平均處理週期由 100.4 天降至 30.9 天 | 有交付與流程變化 |
| HR05 | supported | 選擇首次登入引導確認、不強迫修改 | 具既有客戶風險取捨 |
| HR06 | supported | 從交友與訂閱制 App 到企業招募系統 | 責任與領域轉移可辨識 |
| HR07 | supported | 與 CodaPay 新加坡技術團隊協調串接 | 協作技能有實務情境 |
| HR08 | supported | 現任 1111 招募系統 Product Owner | 摘要與案例可快速定位 |
| HR09 | partial | 上線後至 2026/10 未再出現同類帳號冒用 | 追問觀測來源與範圍 |
| HR10 | supported | 我希望將更多心力放回產品策略 | 方向與策略職責相容 |
| HR11 | unknown | 錄取後三週可上班 | JD未列地點到職限制，無已知衝突 |
| HR12 | supported | 主導 Juicy 上線 | 具約談價值，驗證完整生命週期 |
| HM01 | supported | 訂閱制 B2C App 與雙邊媒合平台。 | 跨場景經驗可轉移 |
| HM02 | supported | 查出根因是名單依履歷修改日排序 | 具體理解使用者問題 |
| HM03 | supported | 改版排在新功能職缺健檢之前 | 取捨已發生，未當完成結果 |
| HM04 | supported | 依抽成、稅、手續費及撥款週期做實收試算 | 商業分析連結選擇 |
| HM05 | supported | 為觀察差異，非因果。 | 比較與限制清楚，仍需核對 |
| HM06 | supported | 與資料科學團隊合作，定義使用情境與驗收標準 | 協作邊界可辨識 |
| HM07 | supported | 與 QA 制定 UAT 驗收案例 | 驗收及分階段交付具體 |
| HM08 | partial | API 串接規劃、舊系統資料盤點 | 明文技術深度需驗證 |
| HM09 | supported | 統籌影響評估、範圍與時程、驗證流程及客服說明 | 具自主統籌責任 |
| HM10 | supported | 從需求釐清、系統分析到 PRD、原型、UAT 與上線計畫 | 資訊結構足以約談 |
| HM11 | supported | 依客服測試回饋調整推薦規則 | 有回饋修正行動 |
| HM12 | supported | 主導 Juicy 上線 | 約談驗證生命週期 |
| HM13 | not_applicable | — | 方法層不計分；本輪獨立對照JD |

### 5. 約談理由（≤3）與關鍵缺口（≤3）
| # | 約談理由（引原句） |
| :-- | :-- |
| 1 | 「主導 Juicy 上線」與「三階段推進招募系統改版」涵蓋新舊產品。 |
| 2 | 「與 CodaPay 新加坡技術團隊協調串接」支持支付協作。 |
| 3 | 「選擇首次登入引導確認、不強迫修改」具體反映風險取捨。 |

| # | 關鍵缺口 | 面試追問 |
| :-- | :-- | :-- |
| 1 | 完整0到1探索驗證至迭代的直接責任鏈 | 請用單一產品說明0到1探索、驗證、設計、開發、上線與迭代責任。 |
| 2 | JSON、基本SQL與資料結構實作深度 | 請用支付API案例解釋JSON資料結構及錯誤處理，示範基本SQL。 |
| 3 | 內外部教育訓練及產業策略研究範圍 | 如何規劃內部業務、客服、財務及外部夥伴的教育訓練？ |

### 6. 評語（給寫稿者的具體回饋）
**做得好（3 點）**：
- 1111交付｜「由我主責規劃，與工程團隊密切協作」｜區分本人規劃與工程交付。
- 1111改版｜「選擇首次登入引導確認、不強迫修改」｜呈現成熟產品切換與客戶風險取捨。
- 留存分析｜「為觀察差異，非因果。」｜對成效解讀有清楚限制，符合數據分析需求。

**可改進（5 點）**：

- 位置：I01｜Juicy
  - 原句：主導 Juicy 上線
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：新產品交付清楚，但未完整連結探索、驗證及迭代。面試核對完整0到1責任；不是已證明不符。
  - 建議方向：補一個單一產品生命週期與本人責任。

- 位置：I02｜技能／技術協作
  - 原句：API 串接規劃、舊系統資料盤點
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：JSON、SQL及資料結構設計深度未直接呈現。面試用小型工作樣本確認明文技術條件。
  - 建議方向：僅補實際使用過的JSON、SQL及資料模型案例。

- 位置：I03｜登入安全與客服說明
  - 原句：驗證流程及客服說明
  - 問題類型：requirement
  - 嚴重度：interview_follow_up
  - 影響：客服說明不能完整替代內外部產品訓練證據。追問業務、財務與合作夥伴教育經驗。
  - 建議方向：若有實例，交代對象、教材與操作驗證。

- 位置：I04｜登入安全
  - 原句：上線後至 2026/10 未再出現同類帳號冒用
  - 問題類型：measurement
  - 嚴重度：interview_follow_up
  - 影響：這是目前掌握情況，非完整監控已證明零事件。核對資訊來源；不直接否定安全改善。
  - 建議方向：保留限制並說明觀測來源、涵蓋範圍。

- 位置：I05｜專業摘要
  - 原句：近 10 年 PM 經驗
  - 問題類型：readability
  - 嚴重度：editorial
  - 影響：直接對應完整0到1與技術條件的資訊較分散。編輯可提升辨識效率，不改變能力判斷。
  - 建議方向：前置單一0到1案例及已具備的技術證據。

**編輯附件**：無額外語氣要求；不以文風判斷能力或作者。

### 7. 資深能力分布
delivery：強 ／ po_coordination：強 ／ direction_resources：足夠
具優先級與定價方向案例，資源配置及更完整產業策略範圍留面試核對，三項不視為升遷階梯。

### 8. 未測試聲明
PDF 抽字：not_tested ／ ATS 匯入：not_tested ／ AI 作者判讀：不可由文字判定 ／ 真人校準：not_run
僅看指定文字摘要，未外部查證履歷聲明。結構validator另行執行，不代表真人效度或ATS通過。

### 成果分類補表
| 履歷聲明／原句 | 分類 | 解讀限制 |
| :-- | :-- | :-- |
| 對接 16 個需求單位 | context | 協作規模非能力分數 |
| 經手 6 款產品 | context | 經驗範圍 |
| 全站活躍付費廠商約 6.6 萬家 | context | 系統規模非個人帶來客戶數 |
| 團隊 3 名企劃 | context | 不推定管理能力 |
| 約 50 項大項功能上線 | output | 大項交付非業務影響 |
| 上線 111 項 Roadmap 細項 | output | 與大項口徑不同不加總 |
| 盤點出上千組重複 E-mail | output | 資料盤點發現 |
| 選擇首次登入引導確認、不強迫修改 | decision | 既有使用風險取捨 |
| 停機約 1.5 小時 | output | 切換作業觀測，無目標比較 |
| 十多家廠商帳號遭冒用 | context | 問題背景 |
| 2026/04/17 上線簽章驗證 | output | 安全功能交付 |
| 上線後至 2026/10 未再出現同類帳號冒用 | outcome | 目前掌握情況，非獨立監控證明 |
| 需求平均處理週期由 100.4 天降至 30.9 天 | outcome | 穩態Q1/Q2比較，需核對案件組成 |
| 完成 1,726／1,857 張需求與問題單 | output | 處理量及完成比例 |
| 信件與即時通整合排在其他新功能之前 | decision / in_progress | 排序已發生，效益未完成 |
| 改版排在新功能職缺健檢之前 | decision / in_progress | 不可認定已產生搜尋改善 |
| 改依職缺上線日排序、20 天內不重複推薦 | decision / output | 規則修改，未給成效數據 |
| 需求管線觸及 1,279 家活躍付費廠商 | context | 樣本涵蓋率非影響率 |
| 該群年化留存 81.2%，同期全站 74.2% | outcome | 觀察差異非因果 |
| AI 功能已上線公司簡介生成 | output | 另含職缺生成及推薦人才，不代表採用成效 |
| 依客服測試回饋調整推薦規則 | decision / output | 修正行動 |
| 相對變化約多 28% | outcome | 定價實驗相對變化需確認算法與樣本 |
| 還原原價後 iOS 較基準期減 65% | outcome | 期別比較不自動排除干擾 |
| 依結果全面調降售價 | decision | 商業決策 |
| Peach 網頁付款占營收由 24% 至 80% 以上 | outcome | 支付組成變化非總營收成長 |
| KOOL 訂閱與付費牆規劃上線 | output | 多端功能交付 |
| 主導 Juicy 上線 | output | 新產品上線 |
| 男性 DAU 約 3,200 至 1.25 萬 | outcome | 產品上線及行銷導流整體表現 |
| SweetRing 在地化涵蓋 | output | 7市場在地化範圍 |
| 最多約 10 位外國實習生協作 | context | 無直屬管理關係 |
| 導入 CodaPay | output | 付款方式拓展 |
| 提出 7／30／90 天訂閱方案與加贈內容 | decision / output | 商業方案非收入結果 |
| Newegg.com 商品資訊英翻中與英文校對 | output | 翻譯產出 |
| 12 條分支、23 個共用 skill | output | AI工作流程規模非生產力結果 |


## B-jd47｜揭盲：甲=K、乙=M；偏好=M

```json
{"job_id":"jd47","order":"甲=K/乙=M","differences":[{"what":"乙增加配對名單的根因、競品實測與規則調整案例；甲僅概述以使用者困難作產品判斷。","hiring_meaning":"對應成熟產品迭代、競品研究與需求洞察，可追問反推規則的證據、替代方案及調整後成效；尚不證明成長結果。","type":"capability"},{"what":"留存數值相同，乙補出本人定義資料表欄位、DBA取數與試算表比對的分工。","hiring_meaning":"更易驗證資料分析方法及技術邊界；不能因此推論會寫SQL。兩版仍需驗證JSON、基本SQL及完整0到1責任。","type":"measurement"}],"preference":"乙","reason":"乙補出競品實測到規則調整的決策鏈，以及取數分析的本人分工，讓成熟產品迭代與數據能力的面試追問更具體；共同成果不重複加分，SQL、JSON及完整0到1仍須查證。","evidence_甲":["從使用者的困難出發，再考慮商業需求與交付條件，是我希望持續深化的產品判斷。","比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。"],"evidence_乙":["客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。","由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。"]}
```

## 版本比較｜jd47｜順序 甲=K 乙=M｜model_id: unknown
- 偏好：乙（揭盲：M）
| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 乙增加配對名單的根因、競品實測與規則調整案例；甲僅概述以使用者困難作產品判斷。 | 對應成熟產品迭代、競品研究與需求洞察，可追問反推規則的證據、替代方案及調整後成效；尚不證明成長結果。 | capability | 從使用者的困難出發，再考慮商業需求與交付條件，是我希望持續深化的產品判斷。 | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 |
| 2 | 留存數值相同，乙補出本人定義資料表欄位、DBA取數與試算表比對的分工。 | 更易驗證資料分析方法及技術邊界；不能因此推論會寫SQL。兩版仍需驗證JSON、基本SQL及完整0到1責任。 | measurement | 比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |
- 理由（≤120 字）：乙補出競品實測到規則調整的決策鏈，以及取數分析的本人分工，讓成熟產品迭代與數據能力的面試追問更具體；共同成果不重複加分，SQL、JSON及完整0到1仍須查證。


---

# 附錄 B：比較盲審原始JSON與技術失敗

比較者原先只見甲乙，order以盲標籤輸出。以下保留原始輸出；此揭盲作業是預定欄位處理，不是重新投票或新增輪次。



## B-jd03｜原始盲標籤

```json
{"job_id": "jd03", "order": "甲=甲輸入/乙=乙輸入", "differences": [{"what": "乙補出留存分析的取數分工與工具；甲呈現相同觀察結果。", "hiring_meaning": "對數據觀測及會員留存要求，乙讓主管可追問資料表選擇、群組定義與年化方法；相同留存數值不構成成效差異，也不推定自行寫 SQL。", "type": "measurement"}, {"what": "乙新增配對問題的根因、競品實測與具體規則；甲僅概述依回饋調整推薦。", "hiring_meaning": "對產品優化及競品分析，乙提供可驗證的診斷到規則設計案例，可追問排序依據、限制取捨與上線後成效；不將規則調整視為已證明成效。", "type": "capability"}, {"what": "乙說明帳號冒用涉及個資外洩風險；甲已有相同安全處置與結果。", "hiring_meaning": "支付與會員平台面試更容易定位風險判斷的追問，但這是風險脈絡可見性，不能推論新增資安能力或銀行串接經驗。", "type": "readability"}], "preference": "乙", "reason": "乙的取數分工與配對規則案例，讓主管能具體驗證留存分析、競品研究與產品取捨。共同付款串接與文件經驗不分高下；銀行對接及高頻交易系統理解仍須面試確認。", "evidence_甲": ["比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。", "與資料科學團隊合作，定義使用情境與驗收標準，依客服測試回饋調整推薦規則。", "登入安全盤點源於 2026/04 十多家廠商帳號遭冒用。"], "evidence_乙": ["由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。", "客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。", "登入安全盤點源於 2026/04 十多家廠商帳號遭冒用；求才端可存取大量求職者個資，冒用登入即有外洩風險。"]}
```

## 版本比較｜jd03｜順序 甲=甲輸入 乙=乙輸入｜model_id: unknown
- 偏好：乙（揭盲：由彙整階段填寫）
| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 乙補出留存分析的取數分工與工具；甲呈現相同觀察結果。 | 對數據觀測及會員留存要求，乙讓主管可追問資料表選擇、群組定義與年化方法；相同留存數值不構成成效差異，也不推定自行寫 SQL。 | measurement | 比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |
| 2 | 乙新增配對問題的根因、競品實測與具體規則；甲僅概述依回饋調整推薦。 | 對產品優化及競品分析，乙提供可驗證的診斷到規則設計案例，可追問排序依據、限制取捨與上線後成效；不將規則調整視為已證明成效。 | capability | 與資料科學團隊合作，定義使用情境與驗收標準，依客服測試回饋調整推薦規則。 | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 |
| 3 | 乙說明帳號冒用涉及個資外洩風險；甲已有相同安全處置與結果。 | 支付與會員平台面試更容易定位風險判斷的追問，但這是風險脈絡可見性，不能推論新增資安能力或銀行串接經驗。 | readability | 登入安全盤點源於 2026/04 十多家廠商帳號遭冒用。 | 登入安全盤點源於 2026/04 十多家廠商帳號遭冒用；求才端可存取大量求職者個資，冒用登入即有外洩風險。 |
- 理由（≤120 字）：乙的取數分工與配對規則案例，讓主管能具體驗證留存分析、競品研究與產品取捨。共同付款串接與文件經驗不分高下；銀行對接及高頻交易系統理解仍須面試確認。

兩份履歷共同呈現 PRD、User Story、Wireframe、UAT、CodaPay 技術協調與訂閱點數規劃，足以形成基本面試切入點，未因乙重述或增加數字而提高能力評價。甲自傳已有溝通整合優先級案例，乙移入經歷不另算能力差異；新增英文情境與 AI 工具規模不作本職缺決勝依據。以上僅依指定文本比較，未宣稱外部核實事實快照。


## B-jd09｜原始盲標籤

```json
{"job_id": "jd09", "order": "甲=甲輸入/乙=乙輸入", "differences": [{"what": "甲補充客服問題、競品實測到推薦規則調整的完整案例；乙僅列競品實測技能。", "hiring_meaning": "對應需求搜集、競品分析與迭代優化，可追問根因驗證、規則取捨與調整後成效；是證據具體程度差異，不推斷乙缺乏能力。", "type": "capability"}, {"what": "同一留存觀察，甲交代本人定義取數欄位、DBA執行與試算表比對；乙只呈現比對結果。", "hiring_meaning": "更清楚界定數據工作分工，可驗證群體定義、年化算法與選擇偏差；兩版皆註明非因果，不提高結果可信度。", "type": "measurement"}], "preference": "甲", "reason": "甲提供從客服痛點、競品實測到規則調整的可追問案例，並交代留存分析的本人分工，更利於驗證本職缺的需求判斷與數據思維；共同交付成果不重複加分。", "evidence_甲": ["客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。", "由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。"], "evidence_乙": ["研究與數據：使用者訪談與問卷、競品實測、GA4、世代分析、對照組實驗、Excel", "比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。"]}
```

## 版本比較｜jd09｜順序 甲=甲輸入 乙=乙輸入｜model_id: unknown
- 偏好：甲（揭盲：由彙整階段填寫）

| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 甲補充客服問題、競品實測到推薦規則調整的完整案例；乙僅列競品實測技能。 | 對應需求搜集、競品分析與迭代優化，可追問根因驗證、規則取捨與調整後成效；是證據具體程度差異，不推斷乙缺乏能力。 | capability | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 | 研究與數據：使用者訪談與問卷、競品實測、GA4、世代分析、對照組實驗、Excel |
| 2 | 同一留存觀察，甲交代本人定義取數欄位、DBA執行與試算表比對；乙只呈現比對結果。 | 更清楚界定數據工作分工，可驗證群體定義、年化算法與選擇偏差；兩版皆註明非因果，不提高結果可信度。 | measurement | 由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |

- 理由（≤120 字）：甲提供從客服痛點、競品實測到規則調整的可追問案例，並交代留存分析的本人分工，更利於驗證本職缺的需求判斷與數據思維；共同交付成果不重複加分。

共同證據包含 PRD、原型、UAT、分階段上線與定價對照實驗，兩版均足以支持進一步面試。B2B 招募系統經驗與目標 MarTech SaaS 的轉移性，仍需面試確認；此處未作外部核實。


## B-jd11｜原始盲標籤

```json
{"job_id": "jd11", "order": "甲=甲輸入/乙=乙輸入", "differences": [{"what": "乙補充配對名單問題的根因、競品實測與排序規則；甲僅概述依客服回饋調整推薦規則。", "hiring_meaning": "乙讓主管可追問如何驗證根因、選擇規則及衡量改善，對招募流程優化更具體；不據此認定甲欠缺能力。", "type": "capability"}, {"what": "兩版留存數值與非因果限定相同；乙另交代本人擬定資料表欄位、DBA取數與試算表比對。", "hiring_meaning": "乙更清楚界定分析分工，可驗證資料口徑、年化方法與選樣偏差；相同留存結果不提高能力評價。", "type": "measurement"}], "preference": "乙", "reason": "偏好乙，因配對規則改善提供可追問的問題診斷鏈，取數分工也使資料導向能力更易驗證；不是因數字較多。兩版仍須面試確認敏捷實務、中英文PRD與HRIS經驗範圍。", "evidence_甲": ["AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。與資料科學團隊合作，定義使用情境與驗收標準，依客服測試回饋調整推薦規則。", "需求管線觸及 1,279 家活躍付費廠商，約占全站 66,150 家的 1.9%（全站基準日 2026/04/30）。比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。"], "evidence_乙": ["客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。", "需求管線觸及 1,279 家活躍付費廠商，約占全站 66,150 家的 1.9%（全站基準日 2026/04/30）。由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。"]}
```

## 版本比較｜jd11｜順序 甲=甲輸入 乙=乙輸入｜model_id: unknown
- 偏好：乙（揭盲：由彙整階段填寫）
| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 乙補充配對名單問題的根因、競品實測與排序規則；甲僅概述依客服回饋調整推薦規則。 | 乙讓主管可追問如何驗證根因、選擇規則及衡量改善，對招募流程優化更具體；不據此認定甲欠缺能力。 | capability | AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。與資料科學團隊合作，定義使用情境與驗收標準，依客服測試回饋調整推薦規則。 | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 |
| 2 | 兩版留存數值與非因果限定相同；乙另交代本人擬定資料表欄位、DBA取數與試算表比對。 | 乙更清楚界定分析分工，可驗證資料口徑、年化方法與選樣偏差；相同留存結果不提高能力評價。 | measurement | 需求管線觸及 1,279 家活躍付費廠商，約占全站 66,150 家的 1.9%（全站基準日 2026/04/30）。比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 需求管線觸及 1,279 家活躍付費廠商，約占全站 66,150 家的 1.9%（全站基準日 2026/04/30）。由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |
- 理由（≤120 字）：偏好乙，因配對規則改善提供可追問的問題診斷鏈，取數分工也使資料導向能力更易驗證；不是因數字較多。兩版仍須面試確認敏捷實務、中英文PRD與HRIS經驗範圍。


## B-jd14｜原始盲標籤

```json
{"job_id": "jd14", "order": "甲=甲輸入/乙=乙輸入", "differences": [{"what": "甲交代留存分析的取數需求、DBA分工及比對工具，乙僅交代快照與結果。", "hiring_meaning": "可針對指標定義、年化方式與取數正確性追問，較能界定候選人的分析責任；兩版均聲明非因果，不據此認定留存提升。", "type": "measurement"}, {"what": "甲另有從配對名單問題追查排序根因並調整規則的案例；乙的問題排序案例主要在自傳呈現。", "hiring_meaning": "甲增加可驗證的問題診斷與產品規則決策素材，可追問如何衡量推薦品質及留存；尚不能推論已有成長成效。", "type": "capability"}], "preference": "甲", "reason": "甲更清楚交代留存分析的本人角色與取數分工，另提供配對規則調整案例，讓主管能追問分析設計與產品決策；兩版相同的訂閱、定價實驗不重複加分，GA4實作與Firebase仍待驗證。", "evidence_甲": ["由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。", "客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。"], "evidence_乙": ["比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。", "例如廠商抱怨工單中，最大宗是溝通管道中斷，我便將信件與即時通整合排在其他新功能之前，目前專案仍在開發中。"]}
```

## 版本比較｜jd14｜順序 甲=甲輸入 乙=乙輸入｜model_id: unknown
- 偏好：甲（揭盲：由彙整階段填寫）

| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 甲交代留存分析的取數需求、DBA分工及比對工具，乙僅交代快照與結果。 | 可針對指標定義、年化方式與取數正確性追問，較能界定候選人的分析責任；兩版均聲明非因果，不據此認定留存提升。 | measurement | 由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |
| 2 | 甲另有從配對名單問題追查排序根因並調整規則的案例；乙的問題排序案例主要在自傳呈現。 | 甲增加可驗證的問題診斷與產品規則決策素材，可追問如何衡量推薦品質及留存；尚不能推論已有成長成效。 | capability | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 | 例如廠商抱怨工單中，最大宗是溝通管道中斷，我便將信件與即時通整合排在其他新功能之前，目前專案仍在開發中。 |

- 理由（≤120 字）：甲更清楚交代留存分析的本人角色與取數分工，另提供配對規則調整案例，讓主管能追問分析設計與產品決策；兩版相同的訂閱、定價實驗不重複加分，GA4實作與Firebase仍待驗證。


## B-jd20｜原始盲標籤

```json
{"job_id": "jd20", "order": "甲=甲輸入/乙=乙輸入", "differences": [{"what": "乙交代取數與分析分工；甲僅呈現快照比較結果。", "hiring_meaning": "可直接追問資料表、欄位、試算表分析與DBA依賴程度，核對本職缺獨立查詢分析的必備條件；不因結果相同提高分析能力評價。", "type": "measurement"}, {"what": "乙增加搜尋改版優先序與推薦名單根因、規則調整；甲已有溝通整合優先序，但未提供這兩個案例。", "hiring_meaning": "新增可驗證的需求取捨及問題診斷案例，能追問排序依據、競品推論與推薦品質驗收；開發中案例不能當交付成效。", "type": "capability"}, {"what": "乙明示帳號冒用涉及求職者個資外洩風險；甲呈現同一安全事件與處置。", "hiring_meaning": "讓防詐職缺的風險判斷訪談切入點更清楚，可問威脅評估與簽章驗證範圍；同一事件不代表乙多一段資安實績或已證明防詐熱情。", "type": "readability"}], "preference": "乙", "reason": "乙補足取數分工與需求診斷案例，較能界定面試驗證內容；仍須確認獨立數據分析、近母語英文、海外企業客戶及AI工作流整合深度，安全事件不等於完整防詐經驗。", "evidence_甲": ["比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。", "例如廠商抱怨工單中，最大宗是溝通管道中斷，我便將信件與即時通整合排在其他新功能之前，目前專案仍在開發中。", "登入安全盤點源於 2026/04 十多家廠商帳號遭冒用。"], "evidence_乙": ["由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。", "客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。", "登入安全盤點源於 2026/04 十多家廠商帳號遭冒用；求才端可存取大量求職者個資，冒用登入即有外洩風險。"]}
```

## 版本比較｜jd20｜順序 甲=甲輸入 乙=乙輸入｜model_id: unknown
- 偏好：乙（揭盲：由彙整階段填寫）
| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 乙交代取數與分析分工；甲僅呈現快照比較結果。 | 可直接追問資料表、欄位、試算表分析與DBA依賴程度，核對本職缺獨立查詢分析的必備條件；不因結果相同提高分析能力評價。 | measurement | 比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |
| 2 | 乙增加搜尋改版優先序與推薦名單根因、規則調整；甲已有溝通整合優先序，但未提供這兩個案例。 | 新增可驗證的需求取捨及問題診斷案例，能追問排序依據、競品推論與推薦品質驗收；開發中案例不能當交付成效。 | capability | 例如廠商抱怨工單中，最大宗是溝通管道中斷，我便將信件與即時通整合排在其他新功能之前，目前專案仍在開發中。 | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 |
| 3 | 乙明示帳號冒用涉及求職者個資外洩風險；甲呈現同一安全事件與處置。 | 讓防詐職缺的風險判斷訪談切入點更清楚，可問威脅評估與簽章驗證範圍；同一事件不代表乙多一段資安實績或已證明防詐熱情。 | readability | 登入安全盤點源於 2026/04 十多家廠商帳號遭冒用。 | 登入安全盤點源於 2026/04 十多家廠商帳號遭冒用；求才端可存取大量求職者個資，冒用登入即有外洩風險。 |
- 理由（≤120 字）：乙補足取數分工與需求診斷案例，較能界定面試驗證內容；仍須確認獨立數據分析、近母語英文、海外企業客戶及AI工作流整合深度，安全事件不等於完整防詐經驗。

兩版核心PRD、交付、AI功能與定價案例相同。乙英文協作及Claude Code流程補述可用來追問實際工作情境，但不能以考試分數、分支或skill數量判定近母語英文與整合能力；兩版也未明示Jira／Confluence整合。以上僅依提供文本比較，未外部核實事實。


## B-jd26｜原始盲標籤

```json
{"job_id": "jd26", "order": "甲=甲輸入/乙=乙輸入", "differences": [{"what": "甲交代取數分工與分析工具，乙僅列快照比對及留存結果。", "hiring_meaning": "甲讓主管可直接驗證資料表與欄位定義、DBA協作及分析方法，較能釐清數據迭代的實際參與程度；不表示結果較佳。", "type": "measurement"}, {"what": "甲提供配對名單問題的根因、競品實測及規則調整；乙主要以AI推薦的回饋調整描述迭代。", "hiring_meaning": "甲提供另一個可追問的線上問題排查案例，可驗證排序與推薦限制的設計理由、技術影響及上線成效；尚無此案成效數據。", "type": "capability"}, {"what": "甲明示帳號冒用與求職者個資外洩風險的關聯，乙保留事件及處置流程。", "hiring_meaning": "甲較快呈現風險判斷脈絡，便於追問支付專案所需的風險辨識與法遵協作；相同處置成果不構成能力高低證據。", "type": "readability"}], "preference": "甲", "reason": "甲的取數分工及配對問題排查案例，讓主管更能驗證數據分析、線上問題處理與迭代決策。兩者共同的付款串接、Axure與驗收經驗相當；Jira／Confluence、支付法遵及教育訓練仍需確認。", "evidence_甲": ["由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。", "客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。", "求才端可存取大量求職者個資，冒用登入即有外洩風險。"], "evidence_乙": ["比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。", "AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。與資料科學團隊合作，定義使用情境與驗收標準，依客服測試回饋調整推薦規則。", "登入安全盤點源於 2026/04 十多家廠商帳號遭冒用。"]}
```

## 版本比較｜jd26｜順序 甲=甲輸入 乙=乙輸入｜model_id: unknown
- 偏好：甲（揭盲：由彙整階段填寫）
| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 甲交代取數分工與分析工具，乙僅列快照比對及留存結果。 | 甲讓主管可直接驗證資料表與欄位定義、DBA協作及分析方法，較能釐清數據迭代的實際參與程度；不表示結果較佳。 | measurement | 由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |
| 2 | 甲提供配對名單問題的根因、競品實測及規則調整；乙主要以AI推薦的回饋調整描述迭代。 | 甲提供另一個可追問的線上問題排查案例，可驗證排序與推薦限制的設計理由、技術影響及上線成效；尚無此案成效數據。 | capability | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 | AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。與資料科學團隊合作，定義使用情境與驗收標準，依客服測試回饋調整推薦規則。 |
| 3 | 甲明示帳號冒用與求職者個資外洩風險的關聯，乙保留事件及處置流程。 | 甲較快呈現風險判斷脈絡，便於追問支付專案所需的風險辨識與法遵協作；相同處置成果不構成能力高低證據。 | readability | 求才端可存取大量求職者個資，冒用登入即有外洩風險。 | 登入安全盤點源於 2026/04 十多家廠商帳號遭冒用。 |
- 理由（≤120 字）：甲的取數分工及配對問題排查案例，讓主管更能驗證數據分析、線上問題處理與迭代決策。兩者共同的付款串接、Axure與驗收經驗相當；Jira／Confluence、支付法遵及教育訓練仍需確認。

本比較依提供的同一事實快照前提判讀資訊選擇，不代表外部核實；偏好反映可追問的證據較具體，不推定候選人實際能力隨版本改變。


## B-jd30｜原始盲標籤

```json
{"job_id": "jd30", "order": "甲=甲輸入/乙=乙輸入", "differences": [{"what": "甲呈現由工單痛點排優先序；乙另提供配對規則的根因診斷與具體調整。", "hiring_meaning": "乙讓主管可追問從客服問題、競品驗證到規則設計及驗收的鏈路，貼近需求定義與迭代；不把甲乙共有的優先序例子當能力差距。", "type": "capability"}, {"what": "相同留存觀察，乙補明本人定義取數欄位、DBA取數及試算表分析的分工。", "hiring_meaning": "乙更清楚界定數據分析的直接責任；可驗證欄位選擇與留存算法，並另測職缺必備的基本SQL、JSON，不能把委託取數視為SQL能力證明。", "type": "measurement"}], "preference": "乙", "reason": "乙新增配對規則診斷的具體鏈路，並界定留存分析的取數分工，更能形成需求驗證與技術素養的面試問題；共同的AI協作與交付經驗不重複加分，SQL、JSON及完整0到1責任仍須核問。", "evidence_甲": ["例如廠商抱怨工單中，最大宗是溝通管道中斷，我便將信件與即時通整合排在其他新功能之前，目前專案仍在開發中。", "比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。"], "evidence_乙": ["客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。", "由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。"]}
```

## 版本比較｜jd30｜順序 甲=甲輸入 乙=乙輸入｜model_id: unknown
- 偏好：乙（揭盲：由彙整階段填寫）

| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 甲呈現由工單痛點排優先序；乙另提供配對規則的根因診斷與具體調整。 | 乙讓主管可追問從客服問題、競品驗證到規則設計及驗收的鏈路，貼近需求定義與迭代；不把甲乙共有的優先序例子當能力差距。 | capability | 例如廠商抱怨工單中，最大宗是溝通管道中斷，我便將信件與即時通整合排在其他新功能之前，目前專案仍在開發中。 | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 |
| 2 | 相同留存觀察，乙補明本人定義取數欄位、DBA取數及試算表分析的分工。 | 乙更清楚界定數據分析的直接責任；可驗證欄位選擇與留存算法，並另測職缺必備的基本SQL、JSON，不能把委託取數視為SQL能力證明。 | measurement | 比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |

- 理由（≤120 字）：乙新增配對規則診斷的具體鏈路，並界定留存分析的取數分工，更能形成需求驗證與技術素養的面試問題；共同的AI協作與交付經驗不重複加分，SQL、JSON及完整0到1責任仍須核問。


## B-jd31｜原始盲標籤

```json
{"job_id": "jd31", "order": "甲=甲輸入/乙=乙輸入", "differences": [{"what": "甲增加配對名單問題的根因分析與規則設計，乙以AI功能及客服回饋概述優化。", "hiring_meaning": "甲可讓面試追查如何由客戶抱怨形成需求、驗證競品推論與設定規則；屬新增能力證據，並非已證明優化成效。", "type": "capability"}, {"what": "甲說明取數規格、DBA分工與試算工具；乙只保留快照比較結果。", "hiring_meaning": "甲較清楚界定資料分析實作邊界，可追問欄位、群組與年化方法；不因此認定會SQL或BI。", "type": "measurement"}, {"what": "甲補明帳號冒用涉及個資風險，乙保留同一安全事件與處理成果。", "hiring_meaning": "補充風險脈絡方便追問影響評估；同一事件不增加交付能力評價，兩版仍須驗證API整合深度、Scrum及售前經驗。", "type": "readability"}], "preference": "甲", "reason": "甲提供配對規則的問題拆解及取數分工，較能形成需求規劃與分析能力的具體追問；共同的PRD、付款串接與交付證據相同，仍需確認Scrum、客戶訪談及售前參與。", "evidence_甲": ["客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。", "由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。", "求才端可存取大量求職者個資，冒用登入即有外洩風險。"], "evidence_乙": ["AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。與資料科學團隊合作，定義使用情境與驗收標準，依客服測試回饋調整推薦規則。", "比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。", "登入安全盤點源於 2026/04 十多家廠商帳號遭冒用。"]}
```

## 版本比較｜jd31｜順序 甲=甲輸入 乙=乙輸入｜model_id: unknown
- 偏好：甲（揭盲：由彙整階段填寫）
| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 甲增加配對名單問題的根因分析與規則設計，乙以AI功能及客服回饋概述優化。 | 甲可讓面試追查如何由客戶抱怨形成需求、驗證競品推論與設定規則；屬新增能力證據，並非已證明優化成效。 | capability | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 | AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。與資料科學團隊合作，定義使用情境與驗收標準，依客服測試回饋調整推薦規則。 |
| 2 | 甲說明取數規格、DBA分工與試算工具；乙只保留快照比較結果。 | 甲較清楚界定資料分析實作邊界，可追問欄位、群組與年化方法；不因此認定會SQL或BI。 | measurement | 由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |
| 3 | 甲補明帳號冒用涉及個資風險，乙保留同一安全事件與處理成果。 | 補充風險脈絡方便追問影響評估；同一事件不增加交付能力評價，兩版仍須驗證API整合深度、Scrum及售前經驗。 | readability | 求才端可存取大量求職者個資，冒用登入即有外洩風險。 | 登入安全盤點源於 2026/04 十多家廠商帳號遭冒用。 |
- 理由（≤120 字）：甲提供配對規則的問題拆解及取數分工，較能形成需求規劃與分析能力的具體追問；共同的PRD、付款串接與交付證據相同，仍需確認Scrum、客戶訪談及售前參與。


## B-jd32｜原始盲標籤

```json
{"job_id": "jd32", "order": "甲=甲輸入/乙=乙輸入", "differences": [{"what": "乙補充客服問題的根因與推薦規則設計；甲僅概述依回饋調整。", "hiring_meaning": "更能針對問題分析、規格取捨及規則驗收追問，貼合內部系統議題處理；仍需驗證改善成效。", "type": "capability"}, {"what": "乙交代留存分析中本人、DBA與試算表的分工，兩版結果與非因果限制相同。", "hiring_meaning": "更易驗證取數規格與分析責任；不把相同留存差異升格為乙的成果優勢。", "type": "measurement"}, {"what": "乙新增搜尋改版優先於新功能的案例；信件與即時通案例兩版皆有。", "hiring_meaning": "增加可追問的需求排序取捨，適合驗證跨單位優化提案；兩案開發中，不能視為交付成效。", "type": "capability"}], "preference": "乙", "reason": "乙補充配對問題的根因與規則、分析取數分工及搜尋改版取捨，讓主管更明確驗證問題處理與需求排序。共同規格、驗收及AI協作經驗不重複加分，新增數字本身不構成優勢。", "evidence_甲": ["AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。與資料科學團隊合作，定義使用情境與驗收標準，依客服測試回饋調整推薦規則。", "比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。", "例如廠商抱怨工單中，最大宗是溝通管道中斷，我便將信件與即時通整合排在其他新功能之前，目前專案仍在開發中。"], "evidence_乙": ["客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。", "由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。", "依使用者旅程排優先級：廠商抱怨工單最大宗是溝通管道中斷，信件與即時通整合排在其他新功能之前；搜尋結果頁的現有功能卡在痛點上，改版排在新功能職缺健檢之前（兩案皆開發中）。"]}
```

## 版本比較｜jd32｜順序 甲=甲輸入 乙=乙輸入｜model_id: unknown
- 偏好：乙（揭盲：由彙整階段填寫）
| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 乙補充客服問題的根因與推薦規則設計；甲僅概述依回饋調整。 | 更能針對問題分析、規格取捨及規則驗收追問，貼合內部系統議題處理；仍需驗證改善成效。 | capability | AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。與資料科學團隊合作，定義使用情境與驗收標準，依客服測試回饋調整推薦規則。 | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 |
| 2 | 乙交代留存分析中本人、DBA與試算表的分工，兩版結果與非因果限制相同。 | 更易驗證取數規格與分析責任；不把相同留存差異升格為乙的成果優勢。 | measurement | 比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |
| 3 | 乙新增搜尋改版優先於新功能的案例；信件與即時通案例兩版皆有。 | 增加可追問的需求排序取捨，適合驗證跨單位優化提案；兩案開發中，不能視為交付成效。 | capability | 例如廠商抱怨工單中，最大宗是溝通管道中斷，我便將信件與即時通整合排在其他新功能之前，目前專案仍在開發中。 | 依使用者旅程排優先級：廠商抱怨工單最大宗是溝通管道中斷，信件與即時通整合排在其他新功能之前；搜尋結果頁的現有功能卡在痛點上，改版排在新功能職缺健檢之前（兩案皆開發中）。 |
- 理由（≤120 字）：乙補充配對問題的根因與規則、分析取數分工及搜尋改版取捨，讓主管更明確驗證問題處理與需求排序。共同規格、驗收及AI協作經驗不重複加分，新增數字本身不構成優勢。


## B-jd34｜原始盲標籤

```json
{"job_id": "jd34", "order": "甲=甲輸入/乙=乙輸入", "differences": [{"what": "甲補出搜尋改版優先級與配對規則根因，乙僅於自傳保留溝通管道排序案例。", "hiring_meaning": "甲讓主管可追問如何從抱怨定位根因、取捨新功能與維運改善；並不能據此認定乙缺乏該能力。", "type": "capability"}, {"what": "甲交代留存分析由本人擬定資料表欄位、交DBA取數及試算表比對，乙只列快照與結果。", "hiring_meaning": "甲更能界定數據分析分工，面試可驗證指標定義、樣本選擇及分析深度；兩者皆明示非因果。", "type": "measurement"}], "preference": "甲", "reason": "兩版付款、定價、交付與AI產品證據相同；甲另提供優先級與根因分析案例，且交代取數分工，更能設計產品判斷與指標分析追問。Scrum及零售OMO經驗仍須查證。", "evidence_甲": ["客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。", "由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。"], "evidence_乙": ["例如廠商抱怨工單中，最大宗是溝通管道中斷，我便將信件與即時通整合排在其他新功能之前，目前專案仍在開發中。", "比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。"]}
```

## 版本比較｜jd34｜順序 甲=甲輸入 乙=乙輸入｜model_id: unknown
- 偏好：甲（揭盲：由彙整階段填寫）

| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 甲補出搜尋改版優先級與配對規則根因，乙僅於自傳保留溝通管道排序案例。 | 甲讓主管可追問如何從抱怨定位根因、取捨新功能與維運改善；並不能據此認定乙缺乏該能力。 | capability | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 | 例如廠商抱怨工單中，最大宗是溝通管道中斷，我便將信件與即時通整合排在其他新功能之前，目前專案仍在開發中。 |
| 2 | 甲交代留存分析由本人擬定資料表欄位、交DBA取數及試算表比對，乙只列快照與結果。 | 甲更能界定數據分析分工，面試可驗證指標定義、樣本選擇及分析深度；兩者皆明示非因果。 | measurement | 由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |

- 理由（≤120 字）：兩版付款、定價、交付與AI產品證據相同；甲另提供優先級與根因分析案例，且交代取數分工，更能設計產品判斷與指標分析追問。Scrum及零售OMO經驗仍須查證。

比較依指定輸入的共同事實快照前提，未宣稱外部核實。甲的增補用於形成面試驗證題目，不將乙省略的內容解讀為能力不足。兩版既有金流串接、UI原型、QA驗收及Gen AI上市案例相同，不因同義表達改變評價。


## B-jd36｜原始盲標籤

```json
{"job_id": "jd36", "order": "甲=甲輸入/乙=乙輸入", "differences": [{"what": "甲概述推薦功能與回饋調整；乙補充配對名單問題的根因、規則與限制。", "hiring_meaning": "乙讓主管可驗證如何從客服問題定位排序根因、制定規則及衡量改善，對應線上問題排除與迭代；未提供改善成效，不視為已證明有效。", "type": "capability"}, {"what": "同一留存數據，甲呈現快照比較，乙交代欄位需求、DBA取數與試算表分析分工。", "hiring_meaning": "乙更能界定候選人的資料工作責任，可追問表欄位選擇、口徑與年化算法；不推定自行寫SQL，也不將觀察差異當成因果。", "type": "measurement"}], "preference": "乙", "reason": "乙提供配對問題的根因與規則調整，以及取數分工，讓主管能追問線上問題診斷、迭代依據與資料架構理解；共同的串接、驗收經驗不重複加分，Jira／Confluence、API規格及法遵實作仍待驗證。", "evidence_甲": ["AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。與資料科學團隊合作，定義使用情境與驗收標準，依客服測試回饋調整推薦規則。", "比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。"], "evidence_乙": ["客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。", "由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。"]}
```

## 版本比較｜jd36｜順序 甲=甲輸入 乙=乙輸入｜model_id: unknown
- 偏好：乙（揭盲：由彙整階段填寫）
| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 甲概述推薦功能與回饋調整；乙補充配對名單問題的根因、規則與限制。 | 乙讓主管可驗證如何從客服問題定位排序根因、制定規則及衡量改善，對應線上問題排除與迭代；未提供改善成效，不視為已證明有效。 | capability | AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。與資料科學團隊合作，定義使用情境與驗收標準，依客服測試回饋調整推薦規則。 | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 |
| 2 | 同一留存數據，甲呈現快照比較，乙交代欄位需求、DBA取數與試算表分析分工。 | 乙更能界定候選人的資料工作責任，可追問表欄位選擇、口徑與年化算法；不推定自行寫SQL，也不將觀察差異當成因果。 | measurement | 比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |
- 理由（≤120 字）：乙提供配對問題的根因與規則調整，以及取數分工，讓主管能追問線上問題診斷、迭代依據與資料架構理解；共同的串接、驗收經驗不重複加分，Jira／Confluence、API規格及法遵實作仍待驗證。


## B-jd40｜原始盲標籤

```json
{"job_id": "jd40", "order": "甲=甲輸入/乙=乙輸入", "differences": [{"what": "甲補出配對排序根因、競品反推與規則調整；乙僅列競品實測技能。", "hiring_meaning": "可追問甲如何由客服問題轉成規則、如何驗收成效，對應需求探索與產品迭代；仍須驗證實際效果。", "type": "capability"}, {"what": "甲交代取數資料表、欄位、DBA及Google Sheet分工；乙只呈現快照比較結果。", "hiring_meaning": "甲使資料分析參與範圍更可驗證，可追問資料定義與比較方法；不能據此認定具備SQL實作。", "type": "measurement"}, {"what": "甲補充安全事件的個資風險脈絡，乙已有相同協調與上線事實。", "hiring_meaning": "甲更易定位風險判斷追問，但不增加已證明的交付能力；兩者皆須追問API架構、KA與NRE經驗。", "type": "readability"}], "preference": "甲", "reason": "甲提供配對規則決策與取數分工的具體證據，較能安排需求拆解、競品分析及成效追蹤的面試驗證；安全脈絡僅提升可讀性。共同交付與支付經驗不重複加分，API深度及KA／NRE仍待確認。", "evidence_甲": ["客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。", "由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。", "求才端可存取大量求職者個資，冒用登入即有外洩風險。"], "evidence_乙": ["研究與數據：使用者訪談與問卷、競品實測、GA4、世代分析、對照組實驗、Excel", "比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。", "登入安全盤點源於 2026/04 十多家廠商帳號遭冒用。"]}
```

## 版本比較｜jd40｜順序 甲=甲輸入 乙=乙輸入｜model_id: unknown
- 偏好：甲（揭盲：由彙整階段填寫）
| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 甲補出配對排序根因、競品反推與規則調整；乙僅列競品實測技能。 | 可追問甲如何由客服問題轉成規則、如何驗收成效，對應需求探索與產品迭代；仍須驗證實際效果。 | capability | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 | 研究與數據：使用者訪談與問卷、競品實測、GA4、世代分析、對照組實驗、Excel |
| 2 | 甲交代取數資料表、欄位、DBA及Google Sheet分工；乙只呈現快照比較結果。 | 甲使資料分析參與範圍更可驗證，可追問資料定義與比較方法；不能據此認定具備SQL實作。 | measurement | 由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |
| 3 | 甲補充安全事件的個資風險脈絡，乙已有相同協調與上線事實。 | 甲更易定位風險判斷追問，但不增加已證明的交付能力；兩者皆須追問API架構、KA與NRE經驗。 | readability | 求才端可存取大量求職者個資，冒用登入即有外洩風險。 | 登入安全盤點源於 2026/04 十多家廠商帳號遭冒用。 |
- 理由（≤120 字）：甲提供配對規則決策與取數分工的具體證據，較能安排需求拆解、競品分析及成效追蹤的面試驗證；安全脈絡僅提升可讀性。共同交付與支付經驗不重複加分，API深度及KA／NRE仍待確認。


## B-jd43｜原始盲標籤

```json
{"job_id": "jd43", "order": "甲=甲輸入/乙=乙輸入", "differences": [{"what": "乙補出帳號冒用對個資的風險，甲已交代相同安全事件與交付。", "hiring_meaning": "更容易定位安全風險判斷的追問；不因此提高安全交付能力評價，仍須驗證威脅模型與監測範圍。", "type": "readability"}, {"what": "乙補出配對痛點、排序根因與競品實測到規則調整的鏈條；甲僅概述推薦驗收與回饋。", "hiring_meaning": "對使用者理解與競品分析提供具體面試切入點，可驗證如何排除其他根因、規則效果及驗證方法。", "type": "capability"}, {"what": "乙明確區分自己定義取數需求、DBA撈取與試算表分析；甲呈現快照比較結果。", "hiring_meaning": "可釐清分析職責邊界，追問留存年化方法與樣本選擇；兩者均註明非因果，不能視為留存提升功績。", "type": "measurement"}], "preference": "乙", "reason": "乙補出競品實測與排序診斷的決策鏈，也交代留存分析分工，讓主管更能設計研究與數據追問；安全風險說明僅增可讀性，相同交付與成效不重複加分。", "evidence_甲": ["登入安全盤點源於 2026/04 十多家廠商帳號遭冒用。", "AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。與資料科學團隊合作，定義使用情境與驗收標準，依客服測試回饋調整推薦規則。", "比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。"], "evidence_乙": ["登入安全盤點源於 2026/04 十多家廠商帳號遭冒用；求才端可存取大量求職者個資，冒用登入即有外洩風險。", "客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。", "由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。"]}
```

## 版本比較｜jd43｜順序 甲=甲輸入 乙=乙輸入｜model_id: unknown
- 偏好：乙（揭盲：由彙整階段填寫）
| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 乙補出帳號冒用對個資的風險，甲已交代相同安全事件與交付。 | 更容易定位安全風險判斷的追問；不因此提高安全交付能力評價，仍須驗證威脅模型與監測範圍。 | readability | 登入安全盤點源於 2026/04 十多家廠商帳號遭冒用。 | 登入安全盤點源於 2026/04 十多家廠商帳號遭冒用；求才端可存取大量求職者個資，冒用登入即有外洩風險。 |
| 2 | 乙補出配對痛點、排序根因與競品實測到規則調整的鏈條；甲僅概述推薦驗收與回饋。 | 對使用者理解與競品分析提供具體面試切入點，可驗證如何排除其他根因、規則效果及驗證方法。 | capability | AI 功能已上線公司簡介生成、職缺工作說明生成及推薦人才。與資料科學團隊合作，定義使用情境與驗收標準，依客服測試回饋調整推薦規則。 | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 |
| 3 | 乙明確區分自己定義取數需求、DBA撈取與試算表分析；甲呈現快照比較結果。 | 可釐清分析職責邊界，追問留存年化方法與樣本選擇；兩者均註明非因果，不能視為留存提升功績。 | measurement | 比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |
- 理由（≤120 字）：乙補出競品實測與排序診斷的決策鏈，也交代留存分析分工，讓主管更能設計研究與數據追問；安全風險說明僅增可讀性，相同交付與成效不重複加分。


## B-jd44｜原始盲標籤

```json
{"job_id": "jd44", "order": "甲=甲輸入/乙=乙輸入", "differences": [{"what": "甲增加配對排序根因與競品實測案例；乙僅列競品實測技能。", "hiring_meaning": "可追問如何辨識使用者痛點、推導推薦規則與驗證參與成效；不是新增已證明的成效。", "type": "capability"}, {"what": "甲交代留存分析的取數分工與工具；乙僅述快照比對。", "hiring_meaning": "更易確認候選人的分析責任與資料能力邊界；兩版留存數字及非因果限制相同，不提高效果評價。", "type": "measurement"}, {"what": "甲明列英文分派任務及英文校對；乙保留跨國協作與語言成績但未明示工作語言。", "hiring_meaning": "提高英文工作情境的可見性，方便面試驗證跨國溝通及寫作；不能據此判定英文能力較強。", "type": "readability"}], "preference": "甲", "reason": "甲提供推薦規則診斷與分析分工的不同證據，更能聚焦驗證產品洞察、數據判斷及英文協作；共有的AI上線、定價實驗與0到1經歷不重複加分，音樂應用仍須面試驗證。", "evidence_甲": ["客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。", "由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。", "SweetRing 在地化涵蓋美國、墨西哥、巴西、印尼、馬來西亞、日本、韓國 7 個市場；與最多約 10 位外國實習生協作，在無直屬管理關係下以英文分派 UI/UX 翻譯與多國粉專經營任務。"], "evidence_乙": ["研究與數據：使用者訪談與問卷、競品實測、GA4、世代分析、對照組實驗、Excel", "比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。", "SweetRing 在地化涵蓋美國、墨西哥、巴西、印尼、馬來西亞、日本、韓國 7 個市場；與最多約 10 位外國實習生協作，在無直屬管理關係下分派翻譯與粉專經營任務。"]}
```

## 版本比較｜jd44｜順序 甲=甲輸入 乙=乙輸入｜model_id: unknown
- 偏好：甲（揭盲：由彙整階段填寫）
| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 甲增加配對排序根因與競品實測案例；乙僅列競品實測技能。 | 可追問如何辨識使用者痛點、推導推薦規則與驗證參與成效；不是新增已證明的成效。 | capability | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 | 研究與數據：使用者訪談與問卷、競品實測、GA4、世代分析、對照組實驗、Excel |
| 2 | 甲交代留存分析的取數分工與工具；乙僅述快照比對。 | 更易確認候選人的分析責任與資料能力邊界；兩版留存數字及非因果限制相同，不提高效果評價。 | measurement | 由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |
| 3 | 甲明列英文分派任務及英文校對；乙保留跨國協作與語言成績但未明示工作語言。 | 提高英文工作情境的可見性，方便面試驗證跨國溝通及寫作；不能據此判定英文能力較強。 | readability | SweetRing 在地化涵蓋美國、墨西哥、巴西、印尼、馬來西亞、日本、韓國 7 個市場；與最多約 10 位外國實習生協作，在無直屬管理關係下以英文分派 UI/UX 翻譯與多國粉專經營任務。 | SweetRing 在地化涵蓋美國、墨西哥、巴西、印尼、馬來西亞、日本、韓國 7 個市場；與最多約 10 位外國實習生協作，在無直屬管理關係下分派翻譯與粉專經營任務。 |
- 理由（≤120 字）：甲提供推薦規則診斷與分析分工的不同證據，更能聚焦驗證產品洞察、數據判斷及英文協作；共有的AI上線、定價實驗與0到1經歷不重複加分，音樂應用仍須面試驗證。


## B-jd47｜原始盲標籤

```json
{"job_id": "jd47", "order": "甲=甲輸入/乙=乙輸入", "differences": [{"what": "乙增加配對名單的根因、競品實測與規則調整案例；甲僅概述以使用者困難作產品判斷。", "hiring_meaning": "對應成熟產品迭代、競品研究與需求洞察，可追問反推規則的證據、替代方案及調整後成效；尚不證明成長結果。", "type": "capability"}, {"what": "留存數值相同，乙補出本人定義資料表欄位、DBA取數與試算表比對的分工。", "hiring_meaning": "更易驗證資料分析方法及技術邊界；不能因此推論會寫SQL。兩版仍需驗證JSON、基本SQL及完整0到1責任。", "type": "measurement"}], "preference": "乙", "reason": "乙補出競品實測到規則調整的決策鏈，以及取數分析的本人分工，讓成熟產品迭代與數據能力的面試追問更具體；共同成果不重複加分，SQL、JSON及完整0到1仍須查證。", "evidence_甲": ["從使用者的困難出發，再考慮商業需求與交付條件，是我希望持續深化的產品判斷。", "比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。"], "evidence_乙": ["客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。", "由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。"]}
```

## 版本比較｜jd47｜順序 甲=甲輸入 乙=乙輸入｜model_id: unknown
- 偏好：乙（揭盲：由彙整階段填寫）
| # | 差異 | 招聘意義 | 類型 | 甲的證據 | 乙的證據 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 乙增加配對名單的根因、競品實測與規則調整案例；甲僅概述以使用者困難作產品判斷。 | 對應成熟產品迭代、競品研究與需求洞察，可追問反推規則的證據、替代方案及調整後成效；尚不證明成長結果。 | capability | 從使用者的困難出發，再考慮商業需求與交付條件，是我希望持續深化的產品判斷。 | 客服反映配對名單「少又舊」，查出根因是名單依履歷修改日排序；實測主要競品反推規則後，改依職缺上線日排序、20 天內不重複推薦，並設新職缺首次配對每日上限。 |
| 2 | 留存數值相同，乙補出本人定義資料表欄位、DBA取數與試算表比對的分工。 | 更易驗證資料分析方法及技術邊界；不能因此推論會寫SQL。兩版仍需驗證JSON、基本SQL及完整0到1責任。 | measurement | 比對 2026/04/30、07/07 名冊快照，該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 | 由我擬定取數的資料表與欄位，交 DBA 撈取 2026/04/30、07/07 名冊快照，再以 Google Sheet 比對：該群年化留存 81.2%，同期全站 74.2%；為觀察差異，非因果。 |
- 理由（≤120 字）：乙補出競品實測到規則調整的決策鏈，以及取數分析的本人分工，讓成熟產品迭代與數據能力的面試追問更具體；共同成果不重複加分，SQL、JSON及完整0到1仍須查證。


執行中斷紀錄：

```json
{"date":"2026-10-15","planned_A":30,"planned_B":15,"completed_validated":["A-jd03-K","A-jd03-M","A-jd09-K","A-jd09-M","A-jd11-K","A-jd11-M","A-jd14-K","A-jd14-M","A-jd20-K","A-jd20-M","A-jd26-K","A-jd26-M","A-jd30-K","A-jd30-M","A-jd31-K","A-jd31-M","A-jd32-K","A-jd32-M","A-jd34-K","A-jd34-M","A-jd36-K","A-jd36-M","A-jd40-K","A-jd40-M","A-jd43-K","A-jd43-M","A-jd44-K","A-jd44-M","A-jd47-K","A-jd47-M","B-jd03","B-jd09","B-jd11","B-jd14","B-jd20","B-jd26","B-jd30","B-jd31","B-jd32","B-jd34","B-jd36","B-jd40","B-jd43","B-jd44","B-jd47"],"technical_failures":[{"run_id":"A-jd03-K","kind":"usage_limit","status":"output_recovered_and_validated","note":"工具回報中斷，恢復時JSON及MD均存在且validator為pass；未額外計一輪"},{"run_id":"A-jd30-K","kind":"usage_limit","status":"resumed_same_review_and_validated","note":"無新增獨立輪數"},{"run_id":"A-jd34-K","kind":"interruption","status":"resumed_same_review_and_validated","note":"無新增獨立輪數"},{"run_id":"A-jd32-M","kind":"markdown_generator_tuple_index","status":"repaired_without_regrading","original":"A-jd32-M.failed-1.jsonl","repair_record":"A-jd32-M.repair.md"}],"protocol":"Each review/comparison starts with fork_turns none; no old results supplied.","model_runtime_notice":"執行中系統提示切換模型；精確model_id仍未暴露，無法確認全程同模型，也不視為已識別的跨模型驗證。","completed_A":30,"completed_B":15,"context_count":45}
```


## A-jd32-M.failed-1.jsonl

```text
{"rubric_version": "4.2", "resume_id": "M", "job_id": "jd32", "job_input": "summary", "model_id": "unknown", "run_id": "A-jd32-M", "human_calibrated": false, "requirements": [{"id": "R01", "text": "3年以上經歷", "type": "required", "status": "supported", "evidence": ["近 10 年 PM 經驗"], "blocks_interview": false, "reason": "任職時序及產品規劃案例支持。"}, {"id": "R02", "text": "內部營運網站功能設計、規格撰寫與驗收", "type": "required", "status": "supported", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "blocks_interview": false, "reason": "企業系統與內部需求協作可轉移，內部營運網站範圍可面試核對。"}, {"id": "R03", "text": "處理內部使用者與外部客戶議題並優化或修正", "type": "required", "status": "supported", "evidence": ["每週發布處理週報"], "blocks_interview": false, "reason": "工單處理及客服配對名單案例具體。"}, {"id": "R04", "text": "彙整內部需求、跨單位產品協作及優化提案", "type": "required", "status": "supported", "evidence": ["對接 16 個需求單位"], "blocks_interview": false, "reason": "有需求整合、旅程排序與規則優化案例。"}, {"id": "R05", "text": "與團隊評估可行性及時程", "type": "required", "status": "supported", "evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "blocks_interview": false, "reason": "登入安全及分階段改版支持。"}, {"id": "R06", "text": "資訊或網站開發經驗或SA經驗", "type": "required", "status": "supported", "evidence": ["釐清需求與系統分析後"], "blocks_interview": false, "reason": "SA及業務流程拆解支持；不推論親自開發。"}, {"id": "R07", "text": "運用AI工具進行營運分析或提案", "type": "required", "status": "partial", "evidence": ["用於規格撰寫、資料整理與分析"], "blocks_interview": false, "reason": "工具用途有自述，缺單一營運分析或提案的輸入、判讀與採用案例。"}, {"id": "R08", "text": "熟悉規格撰寫與跨單位溝通", "type": "required", "status": "supported", "evidence": ["整理為 PRD 與 Axure Prototype"], "blocks_interview": false, "reason": "具規格、QA驗收、工程及客服協作。"}, {"id": "R09", "text": "細心耐心、團隊導向", "type": "required", "status": "partial", "evidence": ["選擇首次登入引導確認、不強迫修改"], "blocks_interview": false, "reason": "資料風險與協作行為有線索，不從履歷判定人格。"}], "dimensions": [{"id": "positioning", "rating": "足夠", "evidence": ["現任 1111 招募系統 Product Owner"], "missing": ["策略方向與內部營運系統日常工作的期待可釐清。"], "issue_ids": ["I03"]}, {"id": "role_evidence", "rating": "強", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "missing": ["AI營運分析實際案例待核對。"], "issue_ids": ["I01"]}, {"id": "decision_depth", "rating": "強", "evidence": ["選擇首次登入引導確認、不強迫修改"], "missing": [], "issue_ids": []}, {"id": "outcome_quality", "rating": "足夠", "evidence": ["為觀察差異，非因果"], "missing": ["週期統計口徑與安全事件觀察來源可補。"], "issue_ids": ["I02"]}, {"id": "ownership", "rating": "強", "evidence": ["由我擬定取數的資料表與欄位"], "missing": ["可面試細問跨產品團隊分歧處理。"], "issue_ids": []}, {"id": "readability", "rating": "足夠", "evidence": ["企業端招募系統全模組與求職端公司頁"], "missing": ["可優先呈現內部營運及AI分析案例。"], "issue_ids": []}], "results": [{"quote": "約 50 項大項功能上線", "kinds": ["output"]}, {"quote": "第一階段於 2025/10 離峰切換上線", "kinds": ["output"]}, {"quote": "上線後至 2026/10 未再出現同類帳號冒用", "kinds": ["outcome"]}, {"quote": "需求平均處理週期由 100.4 天降至 30.9 天", "kinds": ["outcome"]}, {"quote": "兩案皆開發中", "kinds": ["in_progress"]}, {"quote": "該群年化留存 81.2%，同期全站 74.2%", "kinds": ["outcome"]}], "hr_questions": [{"rule_id": "HR01", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "application_note": "規格、驗收與系統經驗直接相關"}, {"rule_id": "HR02", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "application_note": "近期系統場景及內外部對象清楚"}, {"rule_id": "HR03", "status": "supported", "resume_evidence": ["由我擬定取數的資料表與欄位"], "application_note": "規劃與DBA執行邊界明確"}, {"rule_id": "HR04", "status": "supported", "resume_evidence": ["需求平均處理週期由 100.4 天降至 30.9 天"], "application_note": "有流程結果，核對統計口徑"}, {"rule_id": "HR05", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "application_note": "以登入風險說明取捨"}, {"rule_id": "HR06", "status": "supported", "resume_evidence": ["近 10 年 PM 經驗"], "application_note": "時序與領域轉換可辨識"}, {"rule_id": "HR07", "status": "supported", "resume_evidence": ["與資料科學團隊合作，定義使用情境與驗收標準"], "application_note": "跨職能合作有實際情境"}, {"rule_id": "HR08", "status": "supported", "resume_evidence": ["現任 1111 招募系統 Product Owner"], "application_note": "摘要可快速定位"}, {"rule_id": "HR09", "status": "partial", "resume_evidence": ["依目前掌握的情況"], "application_note": "安全結果須追問觀察來源"}, {"rule_id": "HR10", "status": "partial", "resume_evidence": ["接下來，我希望將更多心力放回產品策略"], "application_note": "釐清營運系統職務期待"}, {"rule_id": "HR11", "status": "unknown", "resume_evidence": ["台北市、新北市，可接受遠端或混合辦公"], "application_note": "搬遷與薪資接受度可電話核對"}, {"rule_id": "HR12", "status": "supported", "resume_evidence": ["釐清需求與系統分析後"], "application_note": "足以面試；缺口可用案例確認"}], "content_questions": [{"rule_id": "HM01", "primary_dimension": "positioning", "status": "supported", "resume_evidence": ["企業端招募系統全模組與求職端公司頁"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM02", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["客服反映配對名單「少又舊」"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM03", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["選擇首次登入引導確認、不強迫修改"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM04", "primary_dimension": "role_evidence", "status": "not_applicable", "resume_evidence": [], "evidence_type": null, "source_ids": [], "interview_question": null}, {"rule_id": "HM05", "primary_dimension": "outcome_quality", "status": "partial", "resume_evidence": ["為觀察差異，非因果"], "evidence_type": "outcome", "source_ids": [], "interview_question": "處理週期的起訖、母體與排除規則是什麼？"}, {"rule_id": "HM06", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["由我主責規劃，與工程團隊密切協作"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM07", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM08", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["改依職缺上線日排序、20 天內不重複推薦"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM09", "primary_dimension": "ownership", "status": "supported", "resume_evidence": ["統籌影響評估、範圍與時程、驗證流程及客服說明"], "evidence_type": "output", "source_ids": [], "interview_question": null}, {"rule_id": "HM10", "primary_dimension": "readability", "status": "supported", "resume_evidence": ["現任 1111 招募系統 Product Owner"], "evidence_type": "context", "source_ids": [], "interview_question": null}, {"rule_id": "HM11", "primary_dimension": "decision_depth", "status": "supported", "resume_evidence": ["依客服測試回饋調整推薦規則"], "evidence_type": "decision", "source_ids": [], "interview_question": null}, {"rule_id": "HM12", "primary_dimension": "role_evidence", "status": "supported", "resume_evidence": ["用於規格撰寫、資料整理與分析"], "evidence_type": "output", "source_ids": [], "interview_question": "請展示AI營運分析或提案案例及人工查核方式。"}, {"rule_id": "HM13", "primary_dimension": "", "status": "not_applicable", "resume_evidence": [], "evidence_type": null, "source_ids": [], "interview_question": null}], "issues": [{"id": "I01", "rule_id": "HR07", "source_ids": [], "application_note": "追問AI實際工作樣本", "context_limit": "僅依履歷文字，未外部查證。", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "用於規格撰寫、資料整理與分析", "reason": "AI工具用途有線索，但未連結一個營運分析或提案決策；可面試補證。", "suggestion": "補一個可匿名化的輸入、人工驗證與採用結果案例。"}, {"id": "I02", "rule_id": "HM05", "source_ids": [], "application_note": "核對流程指標與安全觀察", "context_limit": "僅依履歷文字，未外部查證。", "category": "measurement", "severity": "interview_follow_up", "block_target": null, "claim": "需求平均處理週期由 100.4 天降至 30.9 天", "reason": "有期間及穩態說明，仍缺母體與起訖；安全未再發生也屬掌握範圍，面試查核，不視為矛盾。", "suggestion": "說明處理週期的納入規則、起訖及安全觀察資料來源。"}, {"id": "I03", "rule_id": "HR10", "source_ids": [], "application_note": "確認職務內容期待", "context_limit": "僅依履歷文字，未外部查證。", "category": "requirement", "severity": "interview_follow_up", "block_target": null, "claim": "接下來，我希望將更多心力放回產品策略", "reason": "策略方向可能相容，但內部營運系統改善比例與本人期待尚未知，不阻擋面試。", "suggestion": "面試確認對內部需求、維運修正與功能規劃工作的期待。"}], "decision": {"recommendation": "interview", "evidence": ["與 QA 制定 UAT 驗收案例、排定上線計畫", "選擇首次登入引導確認、不強迫修改"], "blocking_unknowns": []}, "seniority": {"delivery": "強", "po_coordination": "強", "direction_resources": "足夠"}, "interview_reasons": ["「與 QA 制定 UAT 驗收案例、排定上線計畫」支持規格到交付。", "「對接 16 個需求單位」且有工單排序案例。", "「選擇首次登入引導確認、不強迫修改」呈現風險取捨。"], "key_gaps": ["AI營運分析或提案工作樣本。", "週期計算與安全觀察資料來源。", "內部營運系統工作內容的職涯期待。"], "strengths": ["規格與交付｜「與 QA 制定 UAT 驗收案例、排定上線計畫」｜符合內部系統驗收交付需求。", "決策｜「選擇首次登入引導確認、不強迫修改」｜展示既有使用者風險與實際取捨。", "協作｜「由我擬定取數的資料表與欄位」｜交代本人分析規劃與DBA合作邊界。"], "interview_questions": ["請展示AI營運分析或提案案例及人工查核方式。", "需求平均處理週期如何定義起訖、母體及排除規則？", "未再出現同類帳號冒用的觀察來源及涵蓋範圍是什麼？", "跨單位需求衝突時如何與產品團隊決定範圍和時程？", "內部營運改善與產品策略的工作比例，何種安排符合期待？", "如何確認配對規則修改確實改善名單少又舊的問題？"], "editorial_appendix": ["可將AI分析實例與內部需求改善放在較前位置；不影響能力評定。"], "spectrum": {"level": 8, "uncertainty_levels": 1, "basis": "多個系統分析、規格及交付案例對應JD；有清楚取捨、可比較流程指標與觀察限制。AI應用仍待實例核對。"}, "ai_authorship": {"determination": "not_determinable_from_style", "probability": null, "editorial_observations": []}, "tests": {"pdf_extraction": "not_tested", "ats_import": "not_tested", "ai_provenance": "indeterminate_from_text_alone"}, "validation": {"structural_checks": "not_run", "behavioral_regressions": "not_run", "real_ats_test": "not_run", "human_calibration": "not_run"}}
```


## A-jd32-M.repair.md

```text
technical_failure：初次Markdown產生器以錯誤tuple索引讀取HM意義欄，導致MD缺失，validator未完成。已保留failed-1.jsonl；修正索引後重建同一輪，不更改判定。
```


## 彙整初稿修正｜非審查重評

以下為未採用的彙整初稿，曾使用規準外的決定名稱、缺口名稱代替段落位置及過於概括的影響文字，已在正文修正。原A/B決定、Level及偏好均未改；此初稿不列為有效報告。

```text
# 履歷驗證報告：K vs M × 15 職缺｜2026-10-15｜model_id: unknown｜human_calibration: not_run

## 1. 結論
K：interview 15、clarify_first 0、revise_first 0、reject 0；M：interview 14、clarify_first 1、revise_first 0、reject 0。
B揭盲：K勝 0、M勝 15、無明確偏好0、兩者均須先修正0。
位置：K當甲8職缺（M勝8）、當乙7職缺（M勝7）。
整體判定：M略佔上風，限文件比較；B一致偏好具體取數分工及配對規則，但A未顯示能力全面較高，且K邀約較多。
兩版均interview且最高Level 8，按JD代號展示前5：jd03、jd09、jd11、jd26、jd30；全部同分候選：jd03、jd09、jd11、jd26、jd30、jd31、jd32、jd34、jd36、jd40、jd43、jd44、jd47。
Level僅在單一職缺內比較；差≤1視同級，不跨職缺計平均或中位數。

## 2. 職缺×版本矩陣

|職缺|K決定/Level|M決定/Level|B偏好揭盲|決定性條件≤20字|
|---|---|---|---|---|
|jd03|interview/8|interview/8|M|支付整合深度待問|
|jd09|interview/8|interview/8|M|訪談與SaaS模式待核|
|jd11|interview/8|interview/8|M|敏捷及英文文件待核|
|jd14|interview/8|interview/7|M|Growth年限與工具待核|
|jd20|interview/8|clarify_first/7|M|B2B年資及近母語英語|
|jd26|interview/8|interview/8|M|法遵及協作工具待核|
|jd30|interview/8|interview/8|M|完整0到1與技術素養|
|jd31|interview/8|interview/8|M|直接訪談及Scrum待核|
|jd32|interview/8|interview/8|M|AI營運分析案例待補|
|jd34|interview/8|interview/8|M|零售流程與Scrum待核|
|jd36|interview/8|interview/8|M|API法遵與工具待核|
|jd40|interview/8|interview/8|M|API與客戶合約待核|
|jd43|interview/8|interview/8|M|總部路線圖及研究待核|
|jd44|interview/8|interview/8|M|長期策略及實驗設計|
|jd47|interview/8|interview/8|M|0到1與技術文件待核|

## 3. 職缺分群

|群組|職缺代號|共同卡關或優勢|
|---|---|---|
|支付／系統整合交付|jd03、jd26、jd36、jd40|規格驗收與串接支持面試；API深度、法遵或客戶責任依各JD追問|
|探索與產品策略|jd09、jd43、jd44|取捨與協作可見；直接研究、長期策略或海外路線圖責任未完整|
|敏捷PO與內部營運|jd11、jd31、jd32、jd34|需求到交付完整；敏捷方法、營運AI或角色期待各有待核|
|新產品與AI技術素養|jd30、jd47|上線經驗可見；同一產品探索至迭代鏈條及技術文件待核|
|特定門檻角色|jd14、jd20|前者全漏斗Growth年限工具待核；後者B2B年資與近母語英語是必要條件|

## 4. 跨職缺重複缺口

下表僅計issues明確指出的缺口，未因某工具出現在履歷就擴張至所有職缺。原句、run_id、issue ID與嚴重度見gap_coding.json；本表未把追問、加分未知或partial一律當淘汰。

|缺口|出現職缺數K/M|影響哪類職缺|需補什麼事實|
|---|---|---|---|
|留存年化方法與群體可比性|9/6|使用留存觀察的產品／成長職缺|年化公式、群體定義、選樣與可比性|
|安全事件觀測來源與覆蓋|13/13|引用登入安全成果的職缺|事件來源、定義、涵蓋期間、漏報限制|
|API規格與異常流程深度|3/3|支付／整合／TPM|本人設計的規則、狀態流與失敗驗收|
|直接訪談的執行與洞察|3/3|需求探索／客戶導向產品|受訪者、本人角色、洞察如何改變需求|
|Jira等指定工具經驗|3/2|指定協作工具的交付職缺|真實使用經驗；未使用則說明可轉移流程|

指定工具缺口可與英文等問題同列於一個issue；此處只編碼該句明說的Jira經驗。Scrum在issues.reason中明文出現於jd31、jd34，未達3個職缺，故不列；一般敏捷問題不併入。SQL實作、Sheet分析、GA4/Firebase等異質條件未合成通用數據缺口。

## 5. 評語合併

### 5.1 K

做得好（每項至少兩個不同職缺原審查支持）：

|位置|原句≤40字|對本職缺用途／來源|
|---|---|---|
|登入安全方案|選擇首次登入引導確認、不強迫修改|顯示風險與流程取捨；jd03、jd09 decision_depth|
|規格與驗收|與 QA 制定 UAT 驗收案例、排定上線計畫|支持需求到交付鏈條；jd09、jd32 role_evidence|
|主責交付|由我主責規劃，與工程團隊密切協作|本人規劃責任明確；jd09、jd11 ownership|

可改進（只合併跨職缺明確重複項；以下皆非自動淘汰）：

|位置|原句≤40字|問題類型|嚴重度|面試影響|建議方向／來源|
|---|---|---|---|---|---|
|留存年化方法與群體可比性|該群年化留存 81.2%，同期全站 74.2%|measurement|interview_follow_up|限縮證據可驗證範圍，須追問|年化公式、群體定義、選樣與可比性；來源jd03、jd09、jd11、jd14、jd31、jd34、jd40、jd44、jd47|
|安全事件觀測來源與覆蓋|依目前掌握的情況|measurement|interview_follow_up|限縮證據可驗證範圍，須追問|事件來源、定義、涵蓋期間、漏報限制；來源jd03、jd09、jd11、jd20、jd26、jd30、jd31、jd34、jd36、jd40、jd43、jd44、jd47|
|API規格與異常流程深度|並與 CodaPay 新加坡技術團隊協調串接|requirement|interview_follow_up|限縮證據可驗證範圍，須追問|本人設計的規則、狀態流與失敗驗收；來源jd03、jd36、jd40|
|直接訪談的執行與洞察|使用者訪談與問卷、競品實測|requirement|interview_follow_up|限縮證據可驗證範圍，須追問|受訪者、本人角色、洞察如何改變需求；來源jd09、jd11、jd31|
|Jira等指定工具經驗|Figma、Axure RP、Notion、Trello、Markdown|requirement|interview_follow_up|限縮證據可驗證範圍，須追問|真實使用經驗；未使用則說明可轉移流程；來源jd11、jd26、jd36|

### 5.2 M

做得好（每項至少兩個不同職缺原審查支持）：

|位置|原句≤40字|對本職缺用途／來源|
|---|---|---|
|登入安全方案|選擇首次登入引導確認、不強迫修改|顯示風險與流程取捨；jd03、jd09 decision_depth|
|規格與驗收|與 QA 制定 UAT 驗收案例、排定上線計畫|支持需求到交付鏈條；jd09、jd32 role_evidence|
|留存分析分工|由我擬定取數的資料表與欄位|區分本人定義與DBA執行；jd03、jd11 ownership|

可改進（只合併跨職缺明確重複項；以下皆非自動淘汰）：

|位置|原句≤40字|問題類型|嚴重度|面試影響|建議方向／來源|
|---|---|---|---|---|---|
|留存年化方法與群體可比性|該群年化留存 81.2%，同期全站 74.2%|measurement|interview_follow_up|限縮證據可驗證範圍，須追問|年化公式、群體定義、選樣與可比性；來源jd03、jd09、jd11、jd14、jd31、jd40|
|安全事件觀測來源與覆蓋|上線後至 2026/10 未再出現同類帳號冒用|measurement|interview_follow_up|限縮證據可驗證範圍，須追問|事件來源、定義、涵蓋期間、漏報限制；來源jd03、jd11、jd20、jd26、jd30、jd31、jd32、jd34、jd36、jd40、jd43、jd44、jd47|
|API規格與異常流程深度|並與 CodaPay 新加坡技術團隊協調串接|requirement|interview_follow_up|限縮證據可驗證範圍，須追問|本人設計的規則、狀態流與失敗驗收；來源jd03、jd36、jd40|
|直接訪談的執行與洞察|使用者訪談與問卷|requirement|interview_follow_up|限縮證據可驗證範圍，須追問|受訪者、本人角色、洞察如何改變需求；來源jd09、jd31、jd43|
|Jira等指定工具經驗|Figma、Axure RP、Notion、Trello|requirement|interview_follow_up|限縮證據可驗證範圍，須追問|真實使用經驗；未使用則說明可轉移流程；來源jd26、jd36|

### 5.3 兩版差異造成的判定不同

只列原決定或Level不同的JD；下述是單輪評語與引用對照，未以控制實驗證明某一句造成分數變化。

|職缺|原判定差異|原輪理由與引用的解讀|
|---|---|---|
|jd14|K interview/8；M interview/7|兩版六維度評等相同；均引用「KOOL 訂閱與付費牆規劃上線」與定價對照，也都要求核對Growth年限、完整漏斗及工具。K basis較強調多案例及衡量限制；M basis強調工具與Growth責任未核。差1視同級，A具體維度不足支持能力差；B偏M僅是文件具體度優勢。|
|jd20|K interview/8；M clarify_first/7|K I01/I02把B2B年資、英語列面試確認；M I01/I02把「近10年PM」不能直接支持5年B2B/B2G，以及「TOEIC 980、TOEFL iBT 93」不能確認近母語，列為先澄清。這是相同必要資格的單次門檻解讀差異，不能歸因M更差。M role_evidence為待補、K為足夠；B仍偏M，理由是取數分工與配對案例較可驗證，不能改寫A決定。|

## 6. ATS五塊不加總

本次M為實際PDF，主流程已用pdftotext 24.02.0抽字並核對3頁；PDF未加密、159,799 bytes，主要欄位與成果數值已視覺交叉核對，與閱讀文字在空白及Markdown項目正規化後一致（3,487字元）。K僅純文字，未提供送出檔。這是本機閱讀證據，不宣稱真實ATS通過。actual_ats_import_performed: false。

|真實ATS五塊|K|M|
|---|---|---|
|檔案接受|unknown/not_tested|unknown/not_tested|
|欄位解析|unknown/not_tested|unknown/not_tested|
|搜尋可見性|unknown/not_tested|unknown/not_tested|
|資格與流程條件|unknown/not_tested|unknown/not_tested|
|匹配功能與未知設定|unknown/not_tested|unknown/not_tested|

A中pdf_extraction: not_tested只表示該獨立審查僅看文字；主流程另做的M本機PDF檢查並不矛盾。完整ATS01–14與本機證據另附，未產生總分。

## 7. 方法限制與未做

共45個新context（A30、B15），共享檔案環境並非OS強隔離。45份輸出均通過結構驗證；原評等及決定不更改。執行期間系統明確提示切換模型，各部署精確model_id未暴露，因此不能確認全程同一模型，也未完成可識別的跨模型驗證；未設計跨模型校準。

每職缺僅一輪A及一輪B，無重測。跨職缺交替甲乙位置與職缺內容混雜；K當甲8職缺、當乙7職缺均偏M，只是描述，不能識別順序因果效應或證明不受位置影響。B的同事實快照核對是使用者前提，本次未外部查證。

JD為摘要，未補全文；jd34年資欄5年與內文2年、jd36年資欄2年與內文3年的矛盾保留，不自行裁決。沒有真人校準、真實ATS測試或真實招聘效度驗證，不判作者是否AI。沒有加入其他對話的新個人背景。

technical_failure依執行紀錄保留：A-jd03-K usage_limit後已有輸出恢復並驗證；A-jd30-K usage_limit及A-jd34-K interruption續做同輪；A-jd32-M Markdown產生器tuple index錯誤經格式修復。均不增加獨立輪次，格式修復不重評。

原始規準逐字凍結，補充執行說明分檔。完整45份JSON及MD另作附錄；盲B原order文字保留為甲輸入／乙輸入，最終附錄提供揭盲映射，不更動投票。
```


---

# 附錄 C：檔案與ATS獨立紀錄

# ATS準備檢查｜K／M｜2026-10-15

使用者本次明確指定K取自貼上的Markdown、M取自附件PDF，因此套件「只有文字、沒有實際檔案」的前提不適用於M。已為閱讀來源完成M本機抽字與三頁視覺核對；這不改變內容評等，也不代表任何雇主ATS實測。兩版均未實際投遞或匯入ATS。

`actual_ats_import_performed: false`。真實ATS測試`not_run`。K檔案抽字`not_tested`；M本機文字擷取`completed`，層級`local_text_extraction`。各A審查者只讀純文字，故其原始JSON中的`pdf_extraction: not_tested`表示該獨立審查未執行PDF檢查；主流程另於本節記錄已做的本機操作。

| 塊 | K | M | 說明 |
| :-- | :-- | :-- | :-- |
| 檔案接受 | unknown／not_tested | unknown／not_tested | 沒有15個實際申請流程的格式、大小或密碼限制。M為可開啟的PDF且未加密，不等於雇主系統接受。 |
| 欄位解析 | unknown／not_tested | unknown／not_tested（真實ATS） | M本機可抽字且已逐頁核對姓名、聯絡、職稱公司任期與主要數值；真實平台欄位映射與解析器皆未知。K只有貼文。 |
| 搜尋可見性 | unknown／not_tested | unknown／not_tested | 沒有招聘者實際查詢、全文與欄位搜尋設定；不以字詞多寡推論命中或資格。 |
| 資格與流程條件 | unknown／not_tested | unknown／not_tested | 沒有申請表題目、答案及自動拒絕／推進規則，不能由未寫技能推測必遭淘汰。 |
| 匹配功能與未知設定 | unknown／not_tested | unknown／not_tested | 各公司的vendor/module/版本/權重/人工覆核途徑皆unknown；104只是提供的職缺來源。 |

## ATS01–14

| ID | 狀態（K／M） | 已知、影響及補證 |
| :-- | :-- | :-- |
| ATS01 | unknown／unknown | vendor、module、設定及版本未知；繁中履歷夾英語術語；日期2026-10-15。招聘方提供設定才可判讀。 |
| ATS02 | unknown／unknown | K送出檔案未知；M本機PDF可開且未加密，但接受限制與解析限制均未知。候選人及招聘方提供實際流程。 |
| ATS03 | unknown／unknown（真實ATS） | M本機抽字與畫面核對已做；未觀察到主要欄位錯序。這不是特定ATS成功。候選人提供K送出檔，招聘方提供授權欄位測試。 |
| ATS04 | unknown／unknown | 未知解析器的繁中支援；不得用UI語言推論。招聘方補公開支援文件與實際欄位。 |
| ATS05 | unknown／unknown | 未測全文、欄位、備註、答案、歷史池或AND/OR/NOT。招聘方提供完整查詢與授權搜尋路徑。 |
| ATS06 | unknown／unknown | 逐JD語意對位列於30份內容審查requirements；沒有通用關鍵字覆蓋門檻或搜尋測試。候選人僅補真實使用過的術語與案例。 |
| ATS07 | unknown／unknown | 無申請題與答案；空白不是No，unknown不是不符。候選人提供真實答案，招聘方說明條件組合。 |
| ATS08 | unknown／unknown | 表單規則、AI評估、人工決定與發信排程未知。招聘方提供流程，不依拒信速度猜原因。 |
| ATS09 | unknown／unknown | 未知匹配輸入、準則權重、尺度與覆核機制；不產生ATS總分。招聘方補實際設定。 |
| ATS10 | unknown／unknown | 無合併、重投與來源狀態；不建議多帳號或反覆投遞。招聘方查流程紀錄。 |
| ATS11 | unknown／unknown | 無平台申請模式或身分查核訊號；不由文風或PDF生成軟體判定AI作者或詐騙。 |
| ATS12 | unknown／unknown | 未提供平台摘要。審查引用回查輸入，但不是外部事實查證；若有平台摘要，招聘方逐項對照原文來源。 |
| ATS13 | unknown／unknown（真實ATS） | M已做本機抽字，工具版本與輸入hash另附；K無PDF。搜尋模擬、真實匯入均not_run。招聘方授權後才可升級測試層級。 |
| ATS14 | unknown／unknown | 實際人工覆核未知；本表逐項保留未知及補證責任，不將缺分或技術錯誤當低能力。 |

本機閱讀檢查未發現需要改寫履歷才能抽字的問題；不以頁數、第三頁留白或版型直接加扣內容分。V階段未執行。


本機PDF核對：

```json
{"test_level":"local_text_extraction","actual_ats_import_performed":false,"pdf":{"source":"uploaded PDF designated M by user","sha256":"034c8cc4a426b912c942bfeef157d7e4f67a5a474bf804133166d65755a96c2a","size_bytes":159799,"pages":3,"encrypted":false,"tool":"pdftotext 24.02.0","visual_pages_checked":[1,2,3],"local_extraction":"completed","fields_visually_cross_checked":["姓名","聯絡方式","職稱—公司—任期","章節","成果數值與比較基準"],"actual_vendor_parsing":"not_tested"},"K":{"source":"user supplied Markdown text","submitted_file":"not_provided","pdf_extraction":"not_tested"},"transcript_match":{"status":"exact_after_whitespace_and_markdown_bullet_normalization","characters":3487,"pdf_text_source":"pdftotext 24.02.0"}}
```


---

# 附錄 D：彙整與完整性核對

本節只確認輸出格式、題目覆蓋、原文引句及統計計算，不是招聘效度、真人校準或真實ATS測試。


```json
{"runs":45,"pass":45,"checks":[{"run_id":"A-jd03-K","status":"pass","errors":[]},{"run_id":"A-jd03-M","status":"pass","errors":[]},{"run_id":"B-jd03","status":"pass","errors":[]},{"run_id":"A-jd09-K","status":"pass","errors":[]},{"run_id":"A-jd09-M","status":"pass","errors":[]},{"run_id":"B-jd09","status":"pass","errors":[]},{"run_id":"A-jd11-K","status":"pass","errors":[]},{"run_id":"A-jd11-M","status":"pass","errors":[]},{"run_id":"B-jd11","status":"pass","errors":[]},{"run_id":"A-jd14-K","status":"pass","errors":[]},{"run_id":"A-jd14-M","status":"pass","errors":[]},{"run_id":"B-jd14","status":"pass","errors":[]},{"run_id":"A-jd20-K","status":"pass","errors":[]},{"run_id":"A-jd20-M","status":"pass","errors":[]},{"run_id":"B-jd20","status":"pass","errors":[]},{"run_id":"A-jd26-K","status":"pass","errors":[]},{"run_id":"A-jd26-M","status":"pass","errors":[]},{"run_id":"B-jd26","status":"pass","errors":[]},{"run_id":"A-jd30-K","status":"pass","errors":[]},{"run_id":"A-jd30-M","status":"pass","errors":[]},{"run_id":"B-jd30","status":"pass","errors":[]},{"run_id":"A-jd31-K","status":"pass","errors":[]},{"run_id":"A-jd31-M","status":"pass","errors":[]},{"run_id":"B-jd31","status":"pass","errors":[]},{"run_id":"A-jd32-K","status":"pass","errors":[]},{"run_id":"A-jd32-M","status":"pass","errors":[]},{"run_id":"B-jd32","status":"pass","errors":[]},{"run_id":"A-jd34-K","status":"pass","errors":[]},{"run_id":"A-jd34-M","status":"pass","errors":[]},{"run_id":"B-jd34","status":"pass","errors":[]},{"run_id":"A-jd36-K","status":"pass","errors":[]},{"run_id":"A-jd36-M","status":"pass","errors":[]},{"run_id":"B-jd36","status":"pass","errors":[]},{"run_id":"A-jd40-K","status":"pass","errors":[]},{"run_id":"A-jd40-M","status":"pass","errors":[]},{"run_id":"B-jd40","status":"pass","errors":[]},{"run_id":"A-jd43-K","status":"pass","errors":[]},{"run_id":"A-jd43-M","status":"pass","errors":[]},{"run_id":"B-jd43","status":"pass","errors":[]},{"run_id":"A-jd44-K","status":"pass","errors":[]},{"run_id":"A-jd44-M","status":"pass","errors":[]},{"run_id":"B-jd44","status":"pass","errors":[]},{"run_id":"A-jd47-K","status":"pass","errors":[]},{"run_id":"A-jd47-M","status":"pass","errors":[]},{"run_id":"B-jd47","status":"pass","errors":[]}]}
```


輸入凍結、巢狀欄位、成果分類補表與盲標籤核對：

```json
{"status":"pass","scope":"nested_schema_result_supplements_frozen_inputs_and_blind_mapping","errors":[],"A_contexts":30,"B_contexts":15,"K_as_甲":8,"K_as_乙":7}
```


跨職缺缺口編碼（每個職缺同一缺口去重，僅採原審查輸出）：

```json
{"method":"只依A輸出issues.reason明確提及編碼；同職缺同缺口每版去重；不把必要／加分或unknown／partial變成淘汰判斷。Scrum不與Jira合併；SQL不與Sheet合併。","gaps":[{"gap":"留存年化方法與群體可比性","counts":{"K":9,"M":6},"unique_jobs":["jd03","jd09","jd11","jd14","jd31","jd34","jd40","jd44","jd47"],"affected_roles":"使用留存觀察的產品／成長職缺","facts_to_supply":"年化公式、群體定義、選樣與可比性","sources":[{"job_id":"jd03","version":"K","run_id":"A-jd03-K","source_type":"issue","source_id":"I02","original_sentence":"短期快照年化與選樣可能影響解讀；已註明非因果，不否定觀察。","claim":"該群年化留存 81.2%，同期全站 74.2%","status":"interview_follow_up","category":"measurement","application_note":"面試追問，不阻擋邀約"},{"job_id":"jd03","version":"M","run_id":"A-jd03-M","source_type":"issue","source_id":"I02","original_sentence":"兩次快照如何年化、同群口徑與觀察偏差仍待確認。","claim":"該群年化留存 81.2%，同期全站 74.2%","status":"interview_follow_up","category":"measurement","application_note":"影響衡量可信範圍，不否定已呈現分析能力。"},{"job_id":"jd09","version":"K","run_id":"A-jd09-K","source_type":"issue","source_id":"I02","original_sentence":"年化方法與群體差異未展開；定價實驗亦需核對時間及平台混淆，不阻擋面試。","claim":"該群年化留存 81.2%，同期全站 74.2%","status":"interview_follow_up","category":"measurement","application_note":"核對衡量與因果限制"},{"job_id":"jd09","version":"M","run_id":"A-jd09-M","source_type":"issue","source_id":"I02","original_sentence":"已有期間與非因果限制，年化算法及兩群可比性仍待面試確認。","claim":"該群年化留存 81.2%，同期全站 74.2%","status":"interview_follow_up","category":"measurement","application_note":"面試追問，不阻擋邀約"},{"job_id":"jd11","version":"K","run_id":"A-jd11-K","source_type":"issue","source_id":"I04","original_sentence":"已明示非因果；年化方式、群體選擇與安全事件偵測來源仍須核對，不否定結果。","claim":"該群年化留存 81.2%，同期全站 74.2%","status":"interview_follow_up","category":"measurement","application_note":"成果口徑需確認"},{"job_id":"jd11","version":"M","run_id":"A-jd11-M","source_type":"issue","source_id":"I03","original_sentence":"已有非因果限制，但年化與群組定義待問；安全觀察亦非監測證明。","claim":"該群年化留存 81.2%，同期全站 74.2%","status":"interview_follow_up","category":"measurement","application_note":"1111數據與安全成果"},{"job_id":"jd14","version":"K","run_id":"A-jd14-K","source_type":"issue","source_id":"I04","original_sentence":"占比改變不能單獨證明營收增量；留存年化亦需核對，影響成效解讀。","claim":"Peach 網頁付款占營收由 24% 至 80% 以上","status":"interview_follow_up","category":"measurement","application_note":"面試追問，不阻擋邀約"},{"job_id":"jd14","version":"M","run_id":"A-jd14-M","source_type":"issue","source_id":"I04","original_sentence":"年化算法及選樣尚不明，付款占比也無法證明總營收提升；追問成效口徑。","claim":"該群年化留存 81.2%，同期全站 74.2%","status":"interview_follow_up","category":"measurement","application_note":"面試核對，不視為已證實不符"},{"job_id":"jd31","version":"K","run_id":"A-jd31-K","source_type":"issue","source_id":"I03","original_sentence":"已註明非因果，但年化公式與事件監測覆蓋仍不明；影響衡量可信範圍，不阻擋面試。","claim":"該群年化留存 81.2%，同期全站 74.2%","status":"interview_follow_up","category":"measurement","application_note":"量測口徑待面試確認"},{"job_id":"jd31","version":"M","run_id":"A-jd31-M","source_type":"issue","source_id":"I04","original_sentence":"未再冒用是掌握範圍的觀察，非已驗證監測結果；週期與留存算法也需面試核對。","claim":"依目前掌握的情況","status":"interview_follow_up","category":"measurement","application_note":"成果追溯口徑待核"},{"job_id":"jd34","version":"K","run_id":"A-jd34-K","source_type":"issue","source_id":"I03","original_sentence":"短期快照年化公式與群組選擇影響可比性；面試核對","claim":"該群年化留存 81.2%，同期全站 74.2%","status":"interview_follow_up","category":"measurement","application_note":"觀察差異非因果"},{"job_id":"jd40","version":"K","run_id":"A-jd40-K","source_type":"issue","source_id":"I03","original_sentence":"短期快照如何年化、群體差異及樣本界定尚待釐清。","claim":"該群年化留存 81.2%，同期全站 74.2%","status":"interview_follow_up","category":"measurement","application_note":"追問年化口徑，不當因果成效"},{"job_id":"jd40","version":"M","run_id":"A-jd40-M","source_type":"issue","source_id":"I03","original_sentence":"未再冒用屬有限觀察；年化留存及實驗差異也需核對方法，不能直接推為因果。","claim":"依目前掌握的情況","status":"interview_follow_up","category":"measurement","application_note":"保留約談；以具體案例核對"},{"job_id":"jd44","version":"K","run_id":"A-jd44-K","source_type":"issue","source_id":"I05","original_sentence":"短期快照年化算法與選樣差異需核對；安全改善亦非監測證明","claim":"該群年化留存 81.2%，同期全站 74.2%","status":"interview_follow_up","category":"measurement","application_note":"可面試釐清，不阻擋邀約"},{"job_id":"jd47","version":"K","run_id":"A-jd47-K","source_type":"issue","source_id":"I05","original_sentence":"短期快照年化方法、實驗可比性及安全監測口徑待核對","claim":"該群年化留存 81.2%，同期全站 74.2%","status":"interview_follow_up","category":"measurement","application_note":"面試追問，不據缺漏否定能力"}]},{"gap":"安全事件觀測來源與覆蓋","counts":{"K":13,"M":13},"unique_jobs":["jd03","jd09","jd11","jd20","jd26","jd30","jd31","jd32","jd34","jd36","jd40","jd43","jd44","jd47"],"affected_roles":"引用登入安全成果的職缺","facts_to_supply":"事件來源、定義、涵蓋期間、漏報限制","sources":[{"job_id":"jd03","version":"K","run_id":"A-jd03-K","source_type":"issue","source_id":"I03","original_sentence":"未再冒用屬掌握範圍自述，並非監測證明；需確認安全成效口徑。","claim":"依目前掌握的情況","status":"interview_follow_up","category":"measurement","application_note":"面試追問，不阻擋邀約"},{"job_id":"jd03","version":"M","run_id":"A-jd03-M","source_type":"issue","source_id":"I03","original_sentence":"目前掌握情況不等於完整安全監控。","claim":"上線後至 2026/10 未再出現同類帳號冒用","status":"interview_follow_up","category":"measurement","application_note":"面試追問事件資料來源及覆蓋範圍。"},{"job_id":"jd09","version":"K","run_id":"A-jd09-K","source_type":"issue","source_id":"I03","original_sentence":"未提供監測或通報來源，不能認定安全問題已消除；面試追問觀察涵蓋範圍。","claim":"上線後至 2026/10 未再出現同類帳號冒用","status":"interview_follow_up","category":"measurement","application_note":"核對安全結果觀測來源"},{"job_id":"jd11","version":"K","run_id":"A-jd11-K","source_type":"issue","source_id":"I04","original_sentence":"已明示非因果；年化方式、群體選擇與安全事件偵測來源仍須核對，不否定結果。","claim":"該群年化留存 81.2%，同期全站 74.2%","status":"interview_follow_up","category":"measurement","application_note":"成果口徑需確認"},{"job_id":"jd11","version":"M","run_id":"A-jd11-M","source_type":"issue","source_id":"I03","original_sentence":"已有非因果限制，但年化與群組定義待問；安全觀察亦非監測證明。","claim":"該群年化留存 81.2%，同期全站 74.2%","status":"interview_follow_up","category":"measurement","application_note":"1111數據與安全成果"},{"job_id":"jd20","version":"K","run_id":"A-jd20-K","source_type":"issue","source_id":"I04","original_sentence":"沒有再得知事件不能直接等同監測零事件；需追問來源及覆蓋率。","claim":"依目前掌握的情況","status":"interview_follow_up","category":"measurement","application_note":"面試驗證，非已證不符合"},{"job_id":"jd20","version":"M","run_id":"A-jd20-M","source_type":"issue","source_id":"I04","original_sentence":"防詐產品重視漏報與風險偵測；尚不能判斷未再出現是客服回報或完整監測。","claim":"依目前掌握的情況","status":"interview_follow_up","category":"measurement","application_note":"追問安全事件監測口徑"},{"job_id":"jd26","version":"K","run_id":"A-jd26-K","source_type":"issue","source_id":"I04","original_sentence":"未再發生事件屬有限觀察，不能當完整監控或因果證明；追問來源即可。","claim":"依目前掌握的情況","status":"interview_follow_up","category":"measurement","application_note":"留面試釐清，不據此淘汰"},{"job_id":"jd26","version":"M","run_id":"A-jd26-M","source_type":"issue","source_id":"I03","original_sentence":"安全效果的觀察管道不明，不能當成完整監測證明。","claim":"依目前掌握的情況","status":"interview_follow_up","category":"measurement","application_note":"安全效果的觀察管道不明，不能當成完整監測證明。"},{"job_id":"jd30","version":"K","run_id":"A-jd30-K","source_type":"issue","source_id":"I04","original_sentence":"可保留成果，但面試需區分監測紀錄與口述。","claim":"依目前掌握的情況","status":"interview_follow_up","category":"measurement","application_note":"安全觀察與年化留存方法尚待確認"},{"job_id":"jd30","version":"M","run_id":"A-jd30-M","source_type":"issue","source_id":"I04","original_sentence":"未再出現冒用是有限觀察，不能當已證實安全成效；面試追問資訊來源與涵蓋範圍。","claim":"依目前掌握的情況","status":"interview_follow_up","category":"measurement","application_note":"面試核對，不作淘汰條件"},{"job_id":"jd31","version":"K","run_id":"A-jd31-K","source_type":"issue","source_id":"I03","original_sentence":"已註明非因果，但年化公式與事件監測覆蓋仍不明；影響衡量可信範圍，不阻擋面試。","claim":"該群年化留存 81.2%，同期全站 74.2%","status":"interview_follow_up","category":"measurement","application_note":"量測口徑待面試確認"},{"job_id":"jd31","version":"M","run_id":"A-jd31-M","source_type":"issue","source_id":"I04","original_sentence":"未再冒用是掌握範圍的觀察，非已驗證監測結果；週期與留存算法也需面試核對。","claim":"依目前掌握的情況","status":"interview_follow_up","category":"measurement","application_note":"成果追溯口徑待核"},{"job_id":"jd32","version":"M","run_id":"A-jd32-M","source_type":"issue","source_id":"I02","original_sentence":"有期間及穩態說明，仍缺母體與起訖；安全未再發生也屬掌握範圍，面試查核，不視為矛盾。","claim":"需求平均處理週期由 100.4 天降至 30.9 天","status":"interview_follow_up","category":"measurement","application_note":"核對流程指標與安全觀察"},{"job_id":"jd34","version":"K","run_id":"A-jd34-K","source_type":"issue","source_id":"I04","original_sentence":"目前掌握的情況不等同全面監測；需問來源及漏報限制","claim":"上線後至 2026/10 未再出現同類帳號冒用","status":"interview_follow_up","category":"measurement","application_note":"履歷未聲稱監測查證"},{"job_id":"jd34","version":"M","run_id":"A-jd34-M","source_type":"issue","source_id":"I02","original_sentence":"未再冒用的資訊來源不明；定價亦需控制因素，影響成效追問而非面試資格。","claim":"依目前掌握的情況","status":"interview_follow_up","category":"measurement","application_note":"核對成果的觀察範圍"},{"job_id":"jd36","version":"K","run_id":"A-jd36-K","source_type":"issue","source_id":"I04","original_sentence":"附有掌握範圍的保留語，但未明示監測來源；不能視為完整安全效果驗證。","claim":"上線後至 2026/10 未再出現同類帳號冒用","status":"interview_follow_up","category":"measurement","application_note":"核對安全結果觀測範圍"},{"job_id":"jd36","version":"M","run_id":"A-jd36-M","source_type":"issue","source_id":"I04","original_sentence":"未再冒用是有保留的自述，監測範圍未交代","claim":"依目前掌握的情況","status":"interview_follow_up","category":"measurement","application_note":"保留面試，以具體案例核對"},{"job_id":"jd40","version":"K","run_id":"A-jd40-K","source_type":"issue","source_id":"I04","original_sentence":"未再出現同類事件的觀察來源與涵蓋範圍不明。","claim":"依目前掌握的情況","status":"interview_follow_up","category":"measurement","application_note":"追問安全成效觀察來源"},{"job_id":"jd40","version":"M","run_id":"A-jd40-M","source_type":"issue","source_id":"I03","original_sentence":"未再冒用屬有限觀察；年化留存及實驗差異也需核對方法，不能直接推為因果。","claim":"依目前掌握的情況","status":"interview_follow_up","category":"measurement","application_note":"保留約談；以具體案例核對"},{"job_id":"jd43","version":"K","run_id":"A-jd43-K","source_type":"issue","source_id":"I04","original_sentence":"未再出現冒用屬有限觀察，未載偵測覆蓋與事件定義；需追問不能視為零事故證明。","claim":"依目前掌握的情況","status":"interview_follow_up","category":"measurement","application_note":"安全成效需核對監測範圍"},{"job_id":"jd43","version":"M","run_id":"A-jd43-M","source_type":"issue","source_id":"I02","original_sentence":"未再冒用是有限觀察；缺事件定義、覆蓋率與監測來源，需面試核對而非否定。","claim":"依目前掌握的情況","status":"interview_follow_up","category":"measurement","application_note":"安全結果口徑待核對"},{"job_id":"jd44","version":"K","run_id":"A-jd44-K","source_type":"issue","source_id":"I05","original_sentence":"短期快照年化算法與選樣差異需核對；安全改善亦非監測證明","claim":"該群年化留存 81.2%，同期全站 74.2%","status":"interview_follow_up","category":"measurement","application_note":"可面試釐清，不阻擋邀約"},{"job_id":"jd44","version":"M","run_id":"A-jd44-M","source_type":"issue","source_id":"I04","original_sentence":"未再冒用的掌握渠道與觀測覆蓋不明；只追問，不能當監測證實。","claim":"依目前掌握的情況","status":"interview_follow_up","category":"measurement","application_note":"安全效果"},{"job_id":"jd47","version":"K","run_id":"A-jd47-K","source_type":"issue","source_id":"I05","original_sentence":"短期快照年化方法、實驗可比性及安全監測口徑待核對","claim":"該群年化留存 81.2%，同期全站 74.2%","status":"interview_follow_up","category":"measurement","application_note":"面試追問，不據缺漏否定能力"},{"job_id":"jd47","version":"M","run_id":"A-jd47-M","source_type":"issue","source_id":"I04","original_sentence":"這是目前掌握情況，非完整監控已證明零事件。","claim":"上線後至 2026/10 未再出現同類帳號冒用","status":"interview_follow_up","category":"measurement","application_note":"核對資訊來源；不直接否定安全改善。"}]},{"gap":"API規格與異常流程深度","counts":{"K":3,"M":3},"unique_jobs":["jd03","jd36","jd40"],"affected_roles":"支付／整合／TPM","facts_to_supply":"本人設計的規則、狀態流與失敗驗收","sources":[{"job_id":"jd03","version":"K","run_id":"A-jd03-K","source_type":"issue","source_id":"I01","original_sentence":"有串接案例但未呈現API錯誤處理與交易狀態設計；影響技術深度驗證。","claim":"並與 CodaPay 新加坡技術團隊協調串接","status":"interview_follow_up","category":"requirement","application_note":"面試追問，不阻擋邀約"},{"job_id":"jd03","version":"M","run_id":"A-jd03-M","source_type":"issue","source_id":"I01","original_sentence":"尚未呈現API業務規則與失敗處理細節。","claim":"並與 CodaPay 新加坡技術團隊協調串接","status":"interview_follow_up","category":"requirement","application_note":"不阻擋面試；需確認API理解達必備深度。"},{"job_id":"jd36","version":"K","run_id":"A-jd36-K","source_type":"issue","source_id":"I02","original_sentence":"串接經歷支持相關性，但尚不足判斷API規格與架構依賴的技術深度；以案例追問。","claim":"API 串接規劃、舊系統資料盤點","status":"interview_follow_up","category":"requirement","application_note":"確認API與架構判斷深度"},{"job_id":"jd36","version":"M","run_id":"A-jd36-M","source_type":"issue","source_id":"I02","original_sentence":"串接經驗未展開到熟悉API規格的深度","claim":"API 串接規劃、舊系統資料盤點","status":"interview_follow_up","category":"requirement","application_note":"保留面試，以具體案例核對"},{"job_id":"jd40","version":"K","run_id":"A-jd40-K","source_type":"issue","source_id":"I01","original_sentence":"有實務但尚不足辨識API及架構協作深度。","claim":"並與 CodaPay 新加坡技術團隊協調串接","status":"interview_follow_up","category":"requirement","application_note":"技術深度留待面試核對"},{"job_id":"jd40","version":"M","run_id":"A-jd40-M","source_type":"issue","source_id":"I01","original_sentence":"整合經驗有線索，但TPM需要的API失敗處理與資料流細節未展開；面試驗證而非否定。","claim":"API 串接規劃、舊系統資料盤點","status":"interview_follow_up","category":"requirement","application_note":"保留約談；以具體案例核對"}]},{"gap":"直接訪談的執行與洞察","counts":{"K":3,"M":3},"unique_jobs":["jd09","jd11","jd31","jd43"],"affected_roles":"需求探索／客戶導向產品","facts_to_supply":"受訪者、本人角色、洞察如何改變需求","sources":[{"job_id":"jd09","version":"K","run_id":"A-jd09-K","source_type":"issue","source_id":"I01","original_sentence":"JD要求需求訪談與市場競品分析，尚未見如何改變產品選擇；可面試核對而非否定能力。","claim":"使用者訪談與問卷、競品實測","status":"interview_follow_up","category":"requirement","application_note":"核對需求探索深度"},{"job_id":"jd09","version":"M","run_id":"A-jd09-M","source_type":"issue","source_id":"I01","original_sentence":"JD要求主導訪談與分析市場；技能列舉不足呈現執行品質，但不構成不符。","claim":"使用者訪談與問卷","status":"interview_follow_up","category":"requirement","application_note":"面試追問，不阻擋邀約"},{"job_id":"jd11","version":"K","run_id":"A-jd11-K","source_type":"issue","source_id":"I03","original_sentence":"工單與客服訊號已支持問題理解，但直接訪談的角色與洞察尚未呈現；追問方法及如何改變需求。","claim":"使用者訪談與問卷","status":"interview_follow_up","category":"requirement","application_note":"直接訪談證據待補"},{"job_id":"jd31","version":"K","run_id":"A-jd31-K","source_type":"issue","source_id":"I01","original_sentence":"方法列舉未呈現直接客戶訪談年資與售前實作；影響面試驗證重點，不推定不具備。","claim":"使用者訪談與問卷","status":"interview_follow_up","category":"requirement","application_note":"直接訪談與售前角色待核對"},{"job_id":"jd31","version":"M","run_id":"A-jd31-M","source_type":"issue","source_id":"I01","original_sentence":"JD重視直接需求訪談，技能列示未呈現受訪者、期間及轉規格過程；已有需求分析，故留面試追問。","claim":"使用者訪談與問卷","status":"interview_follow_up","category":"requirement","application_note":"直接客戶訪談證據不足"},{"job_id":"jd43","version":"M","run_id":"A-jd43-M","source_type":"issue","source_id":"I03","original_sentence":"訪談問卷缺具體應用；指定工具部分未呈現，屬可於面試釐清之缺口。","claim":"研究與數據：使用者訪談與問卷","status":"interview_follow_up","category":"requirement","application_note":"工具與研究方法需驗證"}]},{"gap":"Jira等指定工具經驗","counts":{"K":3,"M":2},"unique_jobs":["jd11","jd26","jd36"],"affected_roles":"指定協作工具的交付職缺","facts_to_supply":"真實使用經驗；未使用則說明可轉移流程","sources":[{"job_id":"jd11","version":"K","run_id":"A-jd11-K","source_type":"issue","source_id":"I02","original_sentence":"Notion有列；Jira未寫，英文翻譯與成績不直接證明英文PRD撰寫。缺口可於面試驗證。","claim":"Figma、Axure RP、Notion、Trello、Markdown","status":"interview_follow_up","category":"requirement","application_note":"工具與英文文件需核對"},{"job_id":"jd26","version":"K","run_id":"A-jd26-K","source_type":"issue","source_id":"I01","original_sentence":"Jira、Confluence未呈現；Axure及交付實例支持進入面試確認工具適應。","claim":"Figma、Axure RP、Notion、Trello","status":"interview_follow_up","category":"requirement","application_note":"留面試釐清，不據此淘汰"},{"job_id":"jd26","version":"M","run_id":"A-jd26-M","source_type":"issue","source_id":"I01","original_sentence":"Jira與Confluence未呈現；已有交付能力，於面試驗證工具經驗。","claim":"Figma、Axure RP、Notion、Trello","status":"interview_follow_up","category":"requirement","application_note":"Jira與Confluence未呈現；已有交付能力，於面試驗"},{"job_id":"jd36","version":"K","run_id":"A-jd36-K","source_type":"issue","source_id":"I01","original_sentence":"JD指定Jira、Confluence；未列出不等於不具備，面試確認工具經驗與可轉移流程。","claim":"Figma、Axure RP、Notion、Trello","status":"interview_follow_up","category":"requirement","application_note":"確認指定專案工具經驗"},{"job_id":"jd36","version":"M","run_id":"A-jd36-M","source_type":"issue","source_id":"I01","original_sentence":"Jira與Confluence沒有使用證據","claim":"整理為 PRD 與 Axure Prototype","status":"interview_follow_up","category":"requirement","application_note":"保留面試，以具體案例核對"}]}]}
```


缺口編碼引用及次數核對：

```json
{"status":"pass","errors":[],"checked_gaps":[{"gap":"留存年化方法與群體可比性","counts":{"K":9,"M":6},"unique_jobs":["jd03","jd09","jd11","jd14","jd31","jd34","jd40","jd44","jd47"]},{"gap":"安全事件觀測來源與覆蓋","counts":{"K":13,"M":13},"unique_jobs":["jd03","jd09","jd11","jd20","jd26","jd30","jd31","jd32","jd34","jd36","jd40","jd43","jd44","jd47"]},{"gap":"API規格與異常流程深度","counts":{"K":3,"M":3},"unique_jobs":["jd03","jd36","jd40"]},{"gap":"直接訪談的執行與洞察","counts":{"K":3,"M":3},"unique_jobs":["jd09","jd11","jd31","jd43"]},{"gap":"Jira等指定工具經驗","counts":{"K":3,"M":2},"unique_jobs":["jd11","jd26","jd36"]}]}
```


```json
{"counts":{"K":{"interview":15},"M":{"interview":14,"clarify_first":1}},"preferences":{"M":15},"raw_label_preferences":{"乙":8,"甲":7},"position_groups":{"甲":{"jobs":["jd03","jd11","jd20","jd30","jd32","jd36","jd43","jd47"],"preferences":{"M":8}},"乙":{"jobs":["jd09","jd14","jd26","jd31","jd34","jd40","jd44"],"preferences":{"M":7}}},"order_effect_identifiable":false,"order_limitation":"不同職缺交替位置，未在同一JD重做反向比較；職缺與位置混雜，不能判定順序效應存在或不存在。"}
```


輸入SHA-256（不含審查者從未讀取的PDF檔名；PDF hash另見附錄C）：

```json
{"inputs/comparison_blind.md":"e98f82a4c4a35fd4ae9dcc95ed3e071fb2f5f78c1522a5d9328fbf7e5b008602","inputs/comparison.md":"a24bf0e02a6718cc6582f6666129cf27bf28694f3c6734974544551eba95c521","inputs/jd34.md":"27ad597055ee4d9c67463cbb704c1e3d1652de34cfafee1f3cef703286a8de55","inputs/jd43.md":"f47e046783c4beb069c21b2adb36399d71cd33fb8bbe542e9308b36330bdb7bf","inputs/resume_k.txt":"355f14df248d225044a9f3f026d70d0a0bcdede1024a0184fd5abede4ad56837","inputs/jd47.md":"8b80fed023b669d59eb970a7ed001842be3d0842db6bd4c03ac6315533e16d20","inputs/jd26.md":"3482a9baa7b183872a429a15ffd1637ce36c548cc29e3bea2b005c81146164db","inputs/jd14.md":"228903748401777baebdffc7efb4b5842510e7d07bb4fc6af80a276919618124","inputs/review_instructions.md":"281ea7e263097d7a80eb961a90f9389498429eda2cc16dd761ccc345815e2b61","inputs/transcribe_m.py":"d5ddb018ad19ac730361941b6e5c68885e3a30fecaef1387364e75e74bcff57e","inputs/jd03.md":"6f5e0ab6afb390035a8ec8f9cc3acb8641498305937d7763564059c4560dd8ba","inputs/rubric.md":"fc4f94845e8c890db6705f607951e2f939f40f560ca3953f7eac0a850339ea88","inputs/jd40.md":"1a4f457b781f02b708d6bf86cf9501ef0378b3f0f8bc8c72516efbfb58595137","inputs/jd44.md":"87eced6ca3080e7f04a95c34683ec3243138f5eab0478da78f614483c7e4a224","inputs/transcript_m.txt":"ca998c3afba84bef50ea778ccf570af4c9e6fbc634fb0b0c181c23d2971fa3a2","inputs/jd32.md":"8401e08f1a0c82b6f89a47377fe4cb2f485960e16f69e4a1f0e13b8be83c5e42","inputs/jd31.md":"64e6c4ceced737ba77834339da03d86826c3b384351141740f2a4a75ef60dfda","inputs/jd09.md":"261bc17d90e355b9872f34698d6151307d619b0527a6f751962fc139f0246f84","inputs/jd30.md":"4376a7f98ccfdeb59572760c605cb5131e989fa9c6f2328c3c100cdf38e24a8d","inputs/jd36.md":"fd9cf6c22fccf6226bdbadf2a5d5e58f339f2535df345f886a2e5c84f7149df8","inputs/jd20.md":"9a7d0581e8905330d4ee987aabddae77f98b13c115e0ba5bf1748ad2c54465ef","inputs/comparison_order.md":"57bc2fa5ff349394c2efc509ed464217c5372189c51ed525f71d8adcb38bc8be","inputs/jd11.md":"82296497cbd6d43e0b318bdcda4e1a522d58242a70bd3083dc6027bb2c846b52","inputs/resume_m.txt":"ca998c3afba84bef50ea778ccf570af4c9e6fbc634fb0b0c181c23d2971fa3a2","inputs/pair14/alpha.txt":"ca998c3afba84bef50ea778ccf570af4c9e6fbc634fb0b0c181c23d2971fa3a2","inputs/pair14/beta.txt":"355f14df248d225044a9f3f026d70d0a0bcdede1024a0184fd5abede4ad56837","inputs/pair09/alpha.txt":"355f14df248d225044a9f3f026d70d0a0bcdede1024a0184fd5abede4ad56837","inputs/pair09/beta.txt":"ca998c3afba84bef50ea778ccf570af4c9e6fbc634fb0b0c181c23d2971fa3a2","inputs/pair15/alpha.txt":"355f14df248d225044a9f3f026d70d0a0bcdede1024a0184fd5abede4ad56837","inputs/pair15/beta.txt":"ca998c3afba84bef50ea778ccf570af4c9e6fbc634fb0b0c181c23d2971fa3a2","inputs/pair06/alpha.txt":"ca998c3afba84bef50ea778ccf570af4c9e6fbc634fb0b0c181c23d2971fa3a2","inputs/pair06/beta.txt":"355f14df248d225044a9f3f026d70d0a0bcdede1024a0184fd5abede4ad56837","inputs/pair02/alpha.txt":"ca998c3afba84bef50ea778ccf570af4c9e6fbc634fb0b0c181c23d2971fa3a2","inputs/pair02/beta.txt":"355f14df248d225044a9f3f026d70d0a0bcdede1024a0184fd5abede4ad56837","inputs/pair12/alpha.txt":"ca998c3afba84bef50ea778ccf570af4c9e6fbc634fb0b0c181c23d2971fa3a2","inputs/pair12/beta.txt":"355f14df248d225044a9f3f026d70d0a0bcdede1024a0184fd5abede4ad56837","inputs/pair08/alpha.txt":"ca998c3afba84bef50ea778ccf570af4c9e6fbc634fb0b0c181c23d2971fa3a2","inputs/pair08/beta.txt":"355f14df248d225044a9f3f026d70d0a0bcdede1024a0184fd5abede4ad56837","inputs/pair05/alpha.txt":"355f14df248d225044a9f3f026d70d0a0bcdede1024a0184fd5abede4ad56837","inputs/pair05/beta.txt":"ca998c3afba84bef50ea778ccf570af4c9e6fbc634fb0b0c181c23d2971fa3a2","inputs/pair10/alpha.txt":"ca998c3afba84bef50ea778ccf570af4c9e6fbc634fb0b0c181c23d2971fa3a2","inputs/pair10/beta.txt":"355f14df248d225044a9f3f026d70d0a0bcdede1024a0184fd5abede4ad56837","inputs/pair03/alpha.txt":"355f14df248d225044a9f3f026d70d0a0bcdede1024a0184fd5abede4ad56837","inputs/pair03/beta.txt":"ca998c3afba84bef50ea778ccf570af4c9e6fbc634fb0b0c181c23d2971fa3a2","inputs/pair01/alpha.txt":"355f14df248d225044a9f3f026d70d0a0bcdede1024a0184fd5abede4ad56837","inputs/pair01/beta.txt":"ca998c3afba84bef50ea778ccf570af4c9e6fbc634fb0b0c181c23d2971fa3a2","inputs/pair07/alpha.txt":"355f14df248d225044a9f3f026d70d0a0bcdede1024a0184fd5abede4ad56837","inputs/pair07/beta.txt":"ca998c3afba84bef50ea778ccf570af4c9e6fbc634fb0b0c181c23d2971fa3a2","inputs/pair04/alpha.txt":"ca998c3afba84bef50ea778ccf570af4c9e6fbc634fb0b0c181c23d2971fa3a2","inputs/pair04/beta.txt":"355f14df248d225044a9f3f026d70d0a0bcdede1024a0184fd5abede4ad56837","inputs/pair13/alpha.txt":"355f14df248d225044a9f3f026d70d0a0bcdede1024a0184fd5abede4ad56837","inputs/pair13/beta.txt":"ca998c3afba84bef50ea778ccf570af4c9e6fbc634fb0b0c181c23d2971fa3a2","inputs/pair11/alpha.txt":"355f14df248d225044a9f3f026d70d0a0bcdede1024a0184fd5abede4ad56837","inputs/pair11/beta.txt":"ca998c3afba84bef50ea778ccf570af4c9e6fbc634fb0b0c181c23d2971fa3a2"}
```


---

# 附錄 E：方法與執行檢查清單

- [x] A共30次；15職缺各K、M一次，每次新context。
- [x] B共15次；按JD由小到大，奇數位置甲K乙M、偶數位置甲M乙K。
- [x] 每次記錄model_id；不可取得者為unknown，不猜部署ID或宣稱不同模型。
- [x] JSON單行、HR12及HM13全列，約談理由及關鍵缺口各≤3。
- [x] 未平均跨職缺Level、未建立加權總分或ATS分數。
- [x] 未將未呈現技能、學歷名氣、頁數、空窗或語氣直接當淘汰條件。
- [x] M本機抽字與內容評等分開；真實ATS匯入及真人校準未做。
- [x] 30份A與15份B的原始判定均保留；格式失敗另列，不藉修復改分。
- [ ] 同一職缺反向順序重測：本次未要求亦未執行，因此無法識別順序因果效應。
- [ ] 跨模型與真人招聘效度驗證：未執行。

