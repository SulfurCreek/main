import json, random, hashlib
from pathlib import Path

P=Path(__file__).parent
(P/'blind').mkdir(parents=True,exist_ok=True)
(P/'private').mkdir(parents=True,exist_ok=True)

roles=[
{
'code':'PM','title':'資深產品經理','industry':'企業軟體','degree':'資訊管理學士','skills':'產品策略、需求探索、PRD、SQL、事件追蹤、API、UAT',
'jd':'負責B2B SaaS產品策略與Roadmap、使用者研究、需求排序、跨部門交付、數據分析及API整合。需要8年以上產品經驗；能說明取捨、衡量結果及責任邊界。無人員管理硬性要求。',
'scope':'負責企業採購SaaS，服務約180家付費企業；協調6位工程師、2位設計師與客服，無直屬人員。',
'a1':'訪談18家客戶並分析事件資料，將簽核流程拆為狀態與權限規則；2025/01–06，120家既有客戶的流程完成率由61%升至76%。來源為同一事件定義的產品看板；我負責研究、方案與驗收，工程團隊負責開發。',
'a2':'比較強制遷移與漸進遷移後，選擇保留舊API六個月並提供轉換層；兩家ERP夥伴均在期限內完成切換，期間沒有因版本停用造成的已確認重大事故。',
'a3':'與客服重設導入檢核點；2025年第二、三季共40家新客戶的平均啟用時間由21天降至14天。兩季客戶規模不同，因此只作流程改善指標，不宣稱完全由產品變更造成。',
'deliverable':'建立Roadmap評分表、API例外狀態清單及UAT案例庫。',
'early':'產品專員／產品經理｜企業軟體乙公司（虛構）｜2016/10–2022/09｜負責客戶訪談、後台功能與兩項ERP串接。'},
{
'code':'FA','title':'資深財務分析師','industry':'製造','degree':'會計學士','skills':'預算、滾動預測、成本分析、Excel、Power BI、SAP、管理報表',
'jd':'負責事業部預算與滾動預測、成本與差異分析、管理報表及情境模型。需要8年以上財務分析經驗，能說明模型口徑、數據來源及跨部門影響。',
'scope':'負責三個事業部、240個主要料號的預算與月度預測，向財務主管報告；無採購簽核權。',
'a1':'重建材料、工時與匯率成本模型；2025/01–09月度成本預測MAPE由18%降至9%，前後均以月底實際成本及同一240個料號計算。我負責模型與差異分析，會計負責關帳確認。',
'a2':'在年度預算提出基準、原料上漲10%與台幣升值5%三種情境，指出兩個低毛利產品組合的敏感度；事業部採用其中一項調價與一項採購避險方案，最終決策由財務長及營運主管作成。',
'a3':'與會計統一科目映射並自動取數；2025年第二季起，月度管理報表準備由5個工作天降至3天，連續六個月維持。',
'deliverable':'建立版本控管的假設表、差異橋接表與月度覆核清單。',
'early':'財務專員／財務分析師｜製造乙公司（虛構）｜2016/10–2022/09｜負責成本結算、預算彙整及管理報表。'},
{
'code':'HR','title':'資深人才招募夥伴','industry':'零售','degree':'企業管理學士','skills':'招募策略、結構式面試、ATS、人才漏斗、Excel、面試官訓練',
'jd':'負責總部與門市招募、人才漏斗分析、面試流程、用人主管協作及雇主品牌。需要8年以上相關經驗；能以一致口徑衡量招募效率與品質。',
'scope':'負責25家門市及總部職缺，每年約160件招募案；與店長及部門主管合作，無薪酬政策決策權。',
'a1':'依職類拆分漏斗並調整面試排程；2025年職缺核准至報到中位數由35天降至27天，前後各80件已完成案件，以ATS日期欄位計算。我負責流程與追蹤，用人主管負責錄用決策。',
'a2':'為六種門市職務建立結構式題庫及行為錨定評分表；抽查120份評分表，完整填寫率由54%升至91%。沒有資料證明這項變更單獨提高新人績效。',
'a3':'與營運共同改版新人訓練；兩批共90位新人的90天留任率由72%升至81%。兩批跨不同季節，因此在報告中列為觀察結果並保留季節因素。',
'deliverable':'建立每月面試官校準、招募漏斗看板與職缺結案復盤。',
'early':'人資助理／人資專員｜零售乙公司（虛構）｜2016/10–2022/09｜負責招募行政、校園招募與新人報到。'},
{
'code':'MK','title':'資深成長行銷經理','industry':'電子商務','degree':'大眾傳播學士','skills':'GA4、CRM、會員分群、付費媒體、實驗設計、行銷預算',
'jd':'負責會員成長、CRM、付費媒體與實驗規劃，管理預算並與商品、數據團隊協作。需要8年以上經驗；能區分相關與因果、說明歸因口徑。',
'scope':'負責會員回購與每季300萬元媒體預算，管理3位專員；與商品及數據團隊協作。',
'a1':'以8,000位近90天未購會員做隨機分組，實驗組接收分群優惠、對照組維持既有訊息；8週回購率18%對14%，95%信賴區間為1.9–6.1個百分點。我負責假設、預算與分析，數據團隊覆核分組。',
'a2':'統一30天點擊歸因視窗並排除品牌字後，2025/01–06首次購買媒體成本由620元降至510元；同期商品折扣改變，故另以品類分層呈現，未把全部降幅歸因於素材。',
'a3':'將每週預算規則改為依邊際轉換成本加減碼；六個月內有4次停投、7次加碼決策，預算均在季額度內，並建立例外核准紀錄。',
'deliverable':'建立實驗登錄表、歸因口徑文件與每週預算決策紀錄。',
'early':'行銷專員／CRM行銷｜電子商務乙公司（虛構）｜2016/10–2022/09｜負責EDM、會員活動與廣告報表。'},
{
'code':'SC','title':'資深供應鏈規劃師','industry':'消費品','degree':'工業工程學士','skills':'需求預測、SAP、庫存策略、S&OP、Excel、供應商協作',
'jd':'負責需求預測、補貨、庫存策略、S&OP及跨部門供需協調。需要8年以上相關經驗；能說明服務水準、庫存與缺貨之間的取捨。',
'scope':'負責180個SKU、兩座倉庫的需求與補貨規劃；協調業務、採購與倉儲，無供應商合約簽署權。',
'a1':'依需求波動及交期重做ABC與安全庫存規則；2025年平均庫存天數由68降至54，訂單行缺貨率由6.0%降至4.5%，前後均用ERP週報及同一180個SKU。',
'a2':'針對A類品評估較低庫存與服務水準風險，選擇將12個高波動SKU維持較高安全庫存；因此總庫存降幅較小，但促銷週缺貨率未超過既定5%門檻。',
'a3':'與業務建立促銷事件輸入；前三個月與後三個月使用相同SKU集合，促銷品預測MAPE由32%降至23%。我負責模型與補貨建議，業務提供活動假設，採購確認供應。',
'deliverable':'主持月度S&OP，維護假設版本、例外清單及供應商交期偏差表。',
'early':'物料管理專員／供應鏈規劃師｜消費品乙公司（虛構）｜2016/10–2022/09｜負責補貨、庫存報表與供應商交期追蹤。'}]

targets={
1:[3,2,3,3,3,1],2:[5,5,5,5,4,1],3:[7,8,8,7,5,2],4:[8,11,10,9,6,3],5:[10,15,13,11,7,3],
6:[11,18,16,12,8,4],7:[12,21,19,13,8,4],8:[13,24,21,14,9,4],9:[14,27,23,14,9,5],10:[15,30,25,15,10,5]}
keys=['positioning','achievements','fit','structure','wording','differentiation']
labels={1:'不可用',2:'很差',3:'差',4:'低於平均',5:'普通',6:'合格',7:'良好',8:'很強',9:'優秀',10:'近乎完美'}

def resume(r,lvl,idx):
 name=f'合成候選人 {idx:02d}'
 head=f'姓名：{name}（完全虛構）\n聯絡：synthetic{idx:02d}@example.invalid｜台北\n'
 if lvl==1:
  return head+f'''\n個人簡介\n我做過很多辦公室工作，學習快、抗壓性高、善於溝通，希望有發展。\n\n經驗\n某公司｜主管\n- 處理各種事情，帶領團隊完成任務。\n- 大幅提升效率及滿意度，深受主管肯定。\n- 熟悉電腦、AI與跨部門溝通。\n\n技能\nOffice、溝通、管理、解決問題\n'''
 if lvl==2:
  return head+f'''求職目標：{r['title']}\n\n摘要\n約10年{r['industry']}經驗，積極負責，具策略思維與執行力。\n\n工作經歷\n{r['industry']}丙公司（虛構）｜資深專員｜2022–現在\n- 負責相關專案與跨部門溝通。\n- 優化流程並達成目標。\n{r['industry']}乙公司（虛構）｜專員｜2016–2022\n- 協助主管及完成例行工作。\n\n技能\n{r['skills']}\n'''
 if lvl==3:
  return head+f'''求職目標：{r['title']}\n\n專業摘要\n累積約10年{r['industry']}經驗，近四年擔任資深專員。\n\n工作經歷\n{r['industry']}丙公司（虛構）｜資深專員｜2022/10–2026/09\n- 負責{r['skills']}相關工作。\n- 召開會議、整理報表並追蹤專案。\n- 與內外部單位溝通，完成主管交辦事項。\n\n{r['early']}\n- 執行日常作業、資料維護與文件整理。\n\n學歷\n示例大學（虛構）｜{r['degree']}｜2012/09–2016/06\n\n技能\n{r['skills']}\n'''
 common=f'''求職目標：{r['title']}\n\n專業摘要\n累積約10年{r['industry']}經驗；近四年負責核心業務。{r['scope']}\n\n工作經歷\n{r['industry']}丙公司（虛構）｜{r['title']}｜2022/10–2026/09\n'''
 if lvl==4:
  body=f'''- {r['scope']}\n- {r['deliverable']}\n- 參與一項流程改善，整理需求及文件並協助上線；未保留前後成效數據。\n'''
 elif lvl==5:
  # One measurable result, but deliberately incomplete comparison and attribution.
  short=r['a1'].split('；')[0]+'；相關指標後來有所改善，但未在履歷列出完整前後期間與共同貢獻。'
  body=f'''- {short}\n- {r['deliverable']}\n- 協調相關部門執行專案並完成交付。\n'''
 elif lvl==6:
  body=f'''- {r['a1'].split("。來源")[0]}。\n- {r['a2'].split("；")[0]}，完成預定交付。\n- {r['deliverable']}\n'''
 elif lvl==7:
  body=f'''- {r['a1']}\n- {r['a2'].split("；")[0]}；我負責分析與協調，最後決策或實作由相關主管及專業團隊完成。\n- {r['deliverable']}\n'''
 elif lvl==8:
  body=f'''- {r['a1']}\n- {r['a2']}\n- {r['a3'].split("。兩")[0].split("。同期")[0]}。\n- {r['deliverable']}\n'''
 elif lvl==9:
  body=f'''- {r['a1']}\n- 決策取捨：{r['a2']}\n- {r['a3']}\n- {r['deliverable']}\n'''
 else:
  common=f'''求職目標：{r['title']}\n\n專業摘要\n近10年{r['industry']}經驗，能力對應目標職務的核心要求：{r['skills']}。{r['scope']}擅長把模糊問題轉為可追蹤決策，並明確區分自己的責任、團隊共同成果與資料限制。\n\n工作經歷\n{r['industry']}丙公司（虛構）｜{r['title']}｜2022/10–2026/09\n'''
  body=f'''- 核心成果：{r['a1']}\n- 取捨與風險：{r['a2']}\n- 跨部門成果：{r['a3']}\n- 可稽核交付：{r['deliverable']}所有數字均標示期間、對象及資料來源；面試可說明計算方式，履歷不主張未驗證的因果。\n'''
 tail=f'''\n{r['early']}\n- 由執行角色逐步承擔分析、改善與跨部門專案；離職與到職月份無重疊。\n\n學歷\n示例大學（虛構）｜{r['degree']}｜2012/09–2016/06\n\n專業技能\n{r['skills']}\n語言：中文流利；英文可閱讀工作文件。\n'''
 if lvl>=7: tail+=f'''\n目標職務對應\n- 經驗對應：{r['jd']}\n- 責任邊界：成果為履歷自述；未宣稱直屬管理、最終簽核權或單獨造成全部結果。\n'''
 return head+common+body+tail

rubric={
'version':'v3-gradient-frozen-before-independent-scoring',
'total':100,
'scope':'只評履歷呈現品質與對所附完整合成JD的匹配，不評真人能力、背景聲望或成果真偽。合成資料的真偽不可外部查證，不因此扣分；看是否清楚標示口徑與責任。',
'dimensions':[
{'key':'positioning','label':'專業定位與職涯敘事','max':15,'anchor':'0–4無目標且歷程不明；5–8有目標但定位模糊；9–12目標及相關歷程清楚；13–14責任範圍與轉變清楚；15高度聚焦且無明顯缺口。'},
{'key':'achievements','label':'成果證據','max':30,'anchor':'0–5只有形容與交辦；6–11有行動或交付但無結果；12–17有一項結果但口徑或歸屬不全；18–23有兩項具體成果並交代部分期間/責任；24–27多項成果含行動、結果、期間、對象及責任；28–30多項可檢核成果並主動標示資料來源、可比性、因果限制。'},
{'key':'fit','label':'職務匹配','max':25,'anchor':'0–5無相關證據；6–10主要靠技能表；11–15部分核心職責有案例；16–20多數核心職責有案例；21–23涵蓋大多數JD且範圍相符；24–25逐項對應核心要求且有工作證據。'},
{'key':'structure','label':'結構與閱讀效率','max':15,'anchor':'0–4無法重建歷程；5–8缺基本資訊或順序混亂；9–11基本完整但證據難找；12–13清楚易掃讀；14–15完整一致且關鍵證據優先。純文字測試不評字型與PDF。'},
{'key':'wording','label':'用字精準度','max':10,'anchor':'0–3大量空泛、誇大或難解；4–5多數抽象；6–7大致清楚但有模糊歸功；8–9清楚並區分責任；10簡潔精確、主動處理限制。'},
{'key':'differentiation','label':'差異化','max':5,'anchor':'0無辨識點；1只有通用特質；2有特定範圍或工具；3有具體方法或場景；4有方法、範圍或取捨的組合；5有清楚且可信的專業模式，不重複以成果數字大小加分。'}],
'scoring_rules':['逐項引用本份履歷證據後給整數分；不可先猜總級別再倒推。','同一缺陷只在最直接維度扣分；如影響另一維度，需引用不同證據。','不能因英文術語、公司/學校聲望、管理人數或數字大而自動加分。','缺人員管理不扣分，除非JD要求；本測試JD均已說明。','輸出總分、六分項、逐項證據、最多三個主要問題、信心。']}
(P/'blind'/'rubric_v3.json').write_text(json.dumps(rubric,ensure_ascii=False,indent=2))

rows=[]; hidden=[]; idx=0
for lvl in range(1,11):
 for r in roles:
  idx+=1
  total=sum(targets[lvl]); rid=f'G{idx:02d}'
  txt=resume(r,lvl,idx)
  rows.append({'id':rid,'target_job':r['jd'],'resume':txt})
  hidden.append({'id':rid,'role_code':r['code'],'role':r['title'],'level':lvl,'label':labels[lvl],
                 'target_scores':dict(zip(keys,targets[lvl])),'target_total':total,
                 'acceptable_total_min':max(0,total-4),'acceptable_total_max':min(100,total+4)})
random.Random(20261012).shuffle(rows)
(P/'blind'/'gradient_resumes.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
(P/'private'/'answer_key.json').write_text(json.dumps(hidden,ensure_ascii=False,indent=2))
(P/'private'/'preregistration.json').write_text(json.dumps({
'frozen_before_independent_scoring':True,
'design':'5職類 × 10品質等級 = 50份；每個等級都有5個不同職類。主模型產生，獨立模型不可讀private。',
'primary_metrics':{
'spearman_total_vs_target':'>=0.95',
'kendall_total_vs_level':'>=0.85',
'adjacent_level_mean_monotonic':'10級平均分嚴格遞增',
'cross_level_inversions':'相差2級以上的成對倒置率<=5%',
'within_expected_band':'>=40/50位於預設±4分區間',
'mae_total':'<=4.0',
'role_bias_within_level':'同級五職類最大分差中位數<=5，任一級最大分差<=10'},
'secondary_checks':['最低與最高級不可顛倒','檢查低級術語或自我形容是否被錯誤加分','檢查頂級因主動寫限制而被不當扣分','逐維MAE與系統性高估/低估'],
'interpretation':'這是由同一規則建構的內部校準集，答案是設計目標而非真人真值。通過代表評分器能復原設計梯度，不代表可預測面試或工作表現。'
},ensure_ascii=False,indent=2))
manifest={'rubric_sha256':hashlib.sha256((P/'blind'/'rubric_v3.json').read_bytes()).hexdigest(),
          'resumes_sha256':hashlib.sha256((P/'blind'/'gradient_resumes.json').read_bytes()).hexdigest()}
(P/'private'/'frozen_hashes.json').write_text(json.dumps(manifest,indent=2))
print('generated',len(rows),'blind resumes; target totals:',[sum(targets[i]) for i in range(1,11)])
