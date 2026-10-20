import json, statistics as st, zipfile, hashlib
from pathlib import Path
P=Path(__file__).parent
def read(n): return json.loads((P/n).read_text())
def validate(rows, dims):
 assert len(rows)==50 and {r['id'] for r in rows}=={f'R{i:02}' for i in range(1,51)}
 for r in rows:
  assert set(r['scores'])==set(dims),r['id']
  assert all(isinstance(r['scores'][k],int) and 0<=r['scores'][k]<=m for k,m in dims.items()),r['id']
  assert r['total']==sum(r['scores'].values()),r['id']
design=read('private/design.json'); data=read('blind/resumes.json')
v1=read('secondary_v1.json');v2=read('secondary_v2.json');rep=read('repeat_v1.json');primary=read('private/primary_v1.json')
validate(v1,{d['key']:d['max'] for d in read('blind/rubric_v1.json')['dimensions']})
validate(v2,{d['key']:d['max'] for d in read('blind/rubric_v2.json')['dimensions']})
assert len(rep)==10 and len({r['id'] for r in rep})==10
for r in rep: assert r['total']==sum(r['scores'].values())
m1={r['id']:r for r in v1};m2={r['id']:r for r in v2};mp={r['id']:r for r in primary}
families={}
for d in design:families.setdefault(d['family'],{})[d['variant']]=d['id']
metrics={}; pairrows=[]
for ver,m in [('v1',m1),('v2',m2)]:
 gaps=[];jargon=[];equiv=[];overlap=[]
 for f,ids in families.items():
  a=m[ids['evidence']]['total']-m[ids['vague']]['total']
  b=m[ids['jargon']]['total']-m[ids['vague']]['total']
  c=abs(m[ids['plain']]['total']-m[ids['evidence']]['total'])
  r=m[ids['overlap']]
  # Machine keyword screen plus report explicitly calls for manual check.
  issue_text=' '.join(r.get('issues',[]))+' '+r.get('evidence',{}).get('structure','')
  detected=any(k in issue_text for k in ['重疊','overlap','同時','並行','兼職'])
  gaps.append(a);jargon.append(b);equiv.append(c);overlap.append(detected)
  pairrows.append({'version':ver,'family':f,'role':next(d['role'] for d in design if d['family']==f),'evidence_vague_gap':a,'jargon_gain':b,'equivalent_abs_gap':c,'overlap_flag_keyword':detected})
 metrics[ver]={'evidence_vague_mean_gap':st.mean(gaps),'evidence_vague_pass':sum(x>=12 for x in gaps),'jargon_mean_gain':st.mean(jargon),'jargon_pass':sum(x<=3 for x in jargon),'equivalent_mean_abs_gap':st.mean(equiv),'equivalent_max_abs_gap':max(equiv),'equivalent_pass':sum(x<=3 for x in equiv),'overlap_flag_keyword_count':sum(overlap),'mean_total':st.mean(r['total'] for r in m.values())}
diffs=[abs(r['total']-m1[r['id']]['total']) for r in rep]
metrics['repeat_v1']={'n':len(diffs),'median_abs_difference':st.median(diffs),'mean_abs_difference':st.mean(diffs),'max_abs_difference':max(diffs)}
metrics['primary_secondary']={'mean_absolute_total_difference':st.mean(abs(mp[i]['total']-r['total']) for i,r in m1.items()),'note':'主模型為按設計版本預先給定的簡化估計，不是50份獨立盲評，也不是正確答案。'}
(P/'metrics.json').write_text(json.dumps({'metrics':metrics,'pairs':pairrows},ensure_ascii=False,indent=2))
lines=['# 50 份合成白領履歷：評分方法校準','', '日期：2026-10-12。全數虛構，約10年資歷；沒有使用真實候選人個資。','', '## 先說結論','', '這是兩個模型的規則一致性與受控擾動測試。第二評分模型為 gpt-6-astra；它實際讀取50份履歷並輸出分項分數與依據。主模型產生資料、事先記錄簡化預估及設計檢核規則。另一個模型的分數不構成招募真值。','', '原版最確定需要修改的是：僅有配分、缺少評分錨點；文字履歷無法驗證ATS卻占10分；職缺匹配度在缺完整JD時容易被過度解讀；成果、差異化與語氣可能重複獎勵同一證據。','', '## 實驗設計與防止誤導','', '- 10個職類各5份版本，合計50份完整文字履歷；它們是10組受控案例，不是50名統計獨立的求職者。每份包含目標、摘要、三段工作、學歷、技能與語言。','- 每組：成果有依據、成果模糊、模糊內容堆疊術語、相同事實以較平實文字重寫、未解釋的任職重疊。各職類目標職責不要求管理人員。','- 設計答案與主模型估分藏在private目錄，第二模型收到隨機排序的履歷及規則；未取得版本答案；同一上下文仍可能從相似文字推知配對，隱藏標籤不等於完全盲測。模型看到的是合成職務摘要，非正式完整JD。','- 在第二模型交付前，發現並修正10份平實版本的自動同義替換語病，要求重新讀取；正式結果均採最新資料。此為資料品質修正，並非依得分改寫答案。','- v2候選規則與通過門檻在v1結果交付前固定；在同一批資料再評，只能看描述性差異，不能稱為樣本外驗證或由結果證明全面改善。','- 同一第二模型複評10份v1履歷，順序改變且不讀先前結果，但共享上下文，不是獨立會話的重測；v2未另做複評，因此不能推論新版重測穩定性。','', '## 可重現的測試結果','', '| 測試 | 事先指定工程門檻 | 原版v1 | 候選v2 |','|---|---|---|---|']
tests=[('有證據優於模糊','每組至少高12分','evidence_vague_pass'),('術語不應被過度獎勵','術語版最多高3分','jargon_pass'),('相同事實應近似評分','分差絕對值不超過3分','equivalent_pass'),('任職重疊應列待核對','10組都辨識','overlap_flag_keyword_count')]
for title,threshold,key in tests:lines.append(f'| {title} | {threshold} | {metrics["v1"][key]}/10 | {metrics["v2"][key]}/10 |')
improved=[title for title,_,key in tests if metrics['v2'][key]>metrics['v1'][key]]
worse=[title for title,_,key in tests if metrics['v2'][key]<metrics['v1'][key]]
lines+=['', '候選新版在通過組數上改善的項目：'+('、'.join(improved) if improved else '無；本次未觀察到通過組數增加')+'。退步項目：'+('、'.join(worse) if worse else '無')+'。這不能證明一般履歷評分能力改善；明確的收益是規則與未檢測狀態變得可審核。']
for ver in ['v1','v2']:
 fails=[]
 for r in pairrows:
  if r['version']!=ver: continue
  names=[]
  if r['evidence_vague_gap']<12:names.append('證據差距不足12')
  if r['jargon_gain']>3:names.append('術語增分超過3')
  if r['equivalent_abs_gap']>3:names.append('等義分差超過3')
  if not r['overlap_flag_keyword']:names.append('重疊未列明')
  if names:fails.append(r['role']+'（'+ '、'.join(names)+'）')
 lines+=['',ver+'未達預設門檻的職類：'+('；'.join(fails) if fails else '無')+'。']
lines+=['','重疊檢測以issues及structure依據中的明確描述計數，再人工核對全部10份。v2有兩份僅在structure依據明言重疊，issues改寫為兩職關係；不能只憑issues關鍵字漏計。逐案原文保留於評分JSON；辨識問題不等於已查證造假。所有通過門檻都是工程驗收設定，非經研究驗證的招聘分數線。','',f'v1等義版本平均絕對分差：{metrics["v1"]["equivalent_mean_abs_gap"]:.1f}，最大{metrics["v1"]["equivalent_max_abs_gap"]}；v2為{metrics["v2"]["equivalent_mean_abs_gap"]:.1f}，最大{metrics["v2"]["equivalent_max_abs_gap"]}。',f'v1十份複評的絕對分差中位數{st.median(diffs):.1f}、平均{st.mean(diffs):.1f}、最大{max(diffs)}。預設門檻為中位數≤3、最大≤7；同上下文的結果可能低估獨立會話波動。',f'主模型簡化預估對第二模型v1的平均絕對分差為{metrics["primary_secondary"]["mean_absolute_total_difference"]:.1f}分。這是估分差異，不是准确率，兩模型一致也不能證明正確。','', 'v1與v2的總分不可直接作為進步幅度：v2移除ATS並重新分配權重。應比較上述成對行為與問題辨識，而非平均分高低。','', '## 候選評分規則','', '| 維度 | v1 | v2 |','|---|---:|---:|','| 專業定位 | 15 | 15 |','| 經歷與成果證據 | 25 | 30 |','| 目標職責匹配 | 20 | 25 |','| 結構與閱讀效率 | 15 | 15 |','| 文字精確度 | 10 | 10 |','| 差異化方法與範圍 | 5 | 5 |','| ATS | 10 | 不計分，另列檢測狀態 |','', '- 每個分項附履歷證據；技能列表與工作案例分開，數字需看口徑、期間、樣本與責任歸屬。','- 相同問題只在最直接的維度扣分；重疊先列待核對，不能推定造假。共同成果、沒有直屬部屬或沒有量化的舊職務不自動扣分。','- 中文白話與英文術語不應影響相同事實的評價；差異化看方法及範圍，不重複獎勵成果數字。','- 匹配度標示provisional；成果標示self_report_only；ATS標示not_tested。實際PDF、視覺布局、抽取順序與ATS匯入另行檢查。','', '## 逐組對照','', '| 職類 | v1證據−模糊 | v2證據−模糊 | v1術語−模糊 | v2術語−模糊 | v1等義差 | v2等義差 |','|---|---:|---:|---:|---:|---:|---:|']
ats_dist={}
for r in v1:ats_dist[str(r['scores']['ats'])]=ats_dist.get(str(r['scores']['ats']),0)+1
ats_note='原版ATS分項實際分布：'+json.dumps(ats_dist,ensure_ascii=False)+'（分數：份數）。這些分數全部來自純文字暫估，沒有解析測試；因此移出100分是修正證據與標籤的錯位，而非聲稱新版招聘預測較準。'
ix=lines.index('## 候選評分規則');lines[ix:ix]=[ats_note,'']
for f in sorted(families):
 a=next(r for r in pairrows if r['version']=='v1' and r['family']==f);b=next(r for r in pairrows if r['version']=='v2' and r['family']==f)
 lines.append(f'| {a["role"]} | {a["evidence_vague_gap"]} | {b["evidence_vague_gap"]} | {a["jargon_gain"]} | {b["jargon_gain"]} | {a["equivalent_abs_gap"]} | {b["equivalent_abs_gap"]} |')
lines+=['', '## 全部50份分數','', '| ID | 職類 | 設計版本（評分時隱藏） | 主模型預估v1 | 第二模型v1 | 第二模型v2 |','|---|---|---|---:|---:|---:|']
labels={'evidence':'有證據','vague':'模糊','jargon':'术語','plain':'平實等義','overlap':'日期重疊'}
for d in design:
 i=d['id'];lines.append(f'| {i} | {d["role"]} | {labels[d["variant"]]} | {mp[i]["total"]} | {m1[i]["total"]} | {m2[i]["total"]} |')
lines+=['', '## 能下與不能下的結論','', '可以確認：這套規則對本批受控文字的可區分性、術語敏感度、等義穩定性、時間線問題辨識，以及一次共享上下文複評的波動。不能確認：真實候選人能力、可信度、各產業公平性、PDF/ATS相容性、面試率或聘用後表現。資料作者與檢核設計者是同一模型，合成偏差仍在；沒有第三方真人標註。','', '後續若要證明招聘效度，應固定v2，另取未見過的匿名真實履歷及完整JD，由至少兩名HR／用人主管獨立評分，先分析人類一致性，再比較模型；另以真正的PDF及目標ATS做解析測試。現在的分數適合指導文字優化，不宜當錄取門檻。','', '完整规则、履歷、每份評分依據、重測、預先註冊與計算程式均隨測試包提供。']
lines+=['', '## 新增：AI生成痕跡檢查','', '此模組在原來两輪評分完成後，依使用者補充要求新增；不是原先預先註冊的AI來源判定實驗。50份來源均已知是本任務模型生成，來源證據是生成流程，而非偵測器。沒有真人對照，不能計算誤報率或AI偵測準確率。','', '對只有成品文字的個人履歷，來源先標示「無法判定」。另外列出模板句、抽象術語、重複結構及過度歸功等可觀察的編輯風險；風險低／中／高不等於AI生成機率。AI使用本身不扣分，模糊或誇大只在既有對應維度處理。沒有使用商業AI檢測器或把履歷交給第三方。','', '2026年的一篇預印本指出，文字特徵偵測器可能依賴資料集特有文風，跨領域與跨生成器測試會退步；2023年的已發表研究也發現所測工具有可靠性限制。這些研究支持保留來源不確定性，不能直接當作繁體中文履歷的偵測成效證據。','', '- [2026研究預印本](https://arxiv.org/abs/2603.23146)','- [2023研究](https://arxiv.org/abs/2306.15666)','', '完整方法在ai_review_protocol.json。若要真正驗證來源判定，需要可驗證來源的真人、純AI及混合編修履歷，配對語言、職類與長度，使用未參與調整的持出資料測試。']
(P/'履歷評分校準報告.md').write_text('\n'.join(lines))
collection=['# 50份虛構履歷測試集','', '這是10組職類各5種受控版本；全數虛構，不代表真實候選人。']
for r in data:collection+=['',f'## {r["id"]}','',r['target'],'',r['resume']]
(P/'50份虛構履歷.md').write_text('\n'.join(collection))
manifest={str(f.relative_to(P)):hashlib.sha256(f.read_bytes()).hexdigest() for f in P.rglob('*') if f.is_file() and 'helper' not in f.parts and '__pycache__' not in f.parts and f.suffix!='.zip' and f.name!='manifest.json'}
(P/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
with zipfile.ZipFile(P/'履歷評分測試包.zip','w',zipfile.ZIP_DEFLATED) as z:
 for f in sorted(P.rglob('*')):
  if f.is_file() and 'helper' not in f.parts and '__pycache__' not in f.parts and f.suffix!='.zip':z.write(f,f.relative_to(P))
print(json.dumps(metrics,ensure_ascii=False,indent=2))
