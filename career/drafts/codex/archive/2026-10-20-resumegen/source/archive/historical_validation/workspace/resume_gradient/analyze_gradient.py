import json, math, statistics as st, csv
from pathlib import Path
P=Path(__file__).parent
key=json.loads((P/'private/answer_key.json').read_text())
scores=json.loads((P/'independent_scores.json').read_text())
dims={'positioning':15,'achievements':30,'fit':25,'structure':15,'wording':10,'differentiation':5}
assert len(scores)==50 and len({r['id'] for r in scores})==50
assert {r['id'] for r in scores}=={r['id'] for r in key}
for r in scores:
 assert set(r['scores'])==set(dims),r['id']
 assert all(isinstance(r['scores'][d],int) and 0<=r['scores'][d]<=m for d,m in dims.items()),r['id']
 assert r['total']==sum(r['scores'].values()),r['id']
 assert set(r['evidence'])==set(dims),r['id']

def rankdata(vals):
 order=sorted(range(len(vals)),key=lambda i:vals[i]); ranks=[0.0]*len(vals);i=0
 while i<len(vals):
  j=i+1
  while j<len(vals) and vals[order[j]]==vals[order[i]]:j+=1
  rank=(i+j-1)/2+1
  for k in range(i,j):ranks[order[k]]=rank
  i=j
 return ranks
def pearson(a,b):
 ma,mb=st.mean(a),st.mean(b);num=sum((x-ma)*(y-mb) for x,y in zip(a,b));den=math.sqrt(sum((x-ma)**2 for x in a)*sum((y-mb)**2 for y in b));return num/den
def spearman(a,b):return pearson(rankdata(a),rankdata(b))
def kendall_tau_b(a,b):
 c=d=tx=ty=0
 for i in range(len(a)):
  for j in range(i+1,len(a)):
   dx=(a[i]>a[j])-(a[i]<a[j]);dy=(b[i]>b[j])-(b[i]<b[j])
   if dx==0 and dy==0:continue
   if dx==0:tx+=1
   elif dy==0:ty+=1
   elif dx==dy:c+=1
   else:d+=1
 return (c-d)/math.sqrt((c+d+tx)*(c+d+ty))

M={r['id']:r for r in scores}; rows=[]
for k in key:
 r=M[k['id']]; rows.append({**k,'actual_total':r['total'],'error':r['total']-k['target_total'],'abs_error':abs(r['total']-k['target_total']),'in_band':k['acceptable_total_min']<=r['total']<=k['acceptable_total_max']})
targets=[r['target_total'] for r in rows];actual=[r['actual_total'] for r in rows];levels=[r['level'] for r in rows]
level_stats=[]
for lvl in range(1,11):
 rr=[r for r in rows if r['level']==lvl]; vals=[r['actual_total'] for r in rr]
 level_stats.append({'level':lvl,'label':rr[0]['label'],'target':rr[0]['target_total'],'mean':st.mean(vals),'min':min(vals),'max':max(vals),'spread':max(vals)-min(vals),'scores':vals})
strict_inv=ties=eligible=0
for a in rows:
 for b in rows:
  if b['level']>=a['level']+2:
   eligible+=1
   if a['actual_total']>b['actual_total']:strict_inv+=1
   elif a['actual_total']==b['actual_total']:ties+=1
dim_metrics={}
for d in dims:
 errs=[M[k['id']]['scores'][d]-k['target_scores'][d] for k in key]
 dim_metrics[d]={'mae':st.mean(abs(x) for x in errs),'bias':st.mean(errs),'max_abs_error':max(abs(x) for x in errs)}
metrics={
'spearman_total_vs_target':spearman(targets,actual),
'kendall_total_vs_level':kendall_tau_b(levels,actual),
'mae_total':st.mean(r['abs_error'] for r in rows),
'bias_total':st.mean(r['error'] for r in rows),
'max_abs_error':max(r['abs_error'] for r in rows),
'within_expected_band_count':sum(r['in_band'] for r in rows),
'adjacent_level_means_strictly_increasing':all(level_stats[i]['mean']<level_stats[i+1]['mean'] for i in range(9)),
'cross_level_pairs_2plus':eligible,'strict_inversions':strict_inv,'ties':ties,'strict_inversion_rate':strict_inv/eligible,
'median_within_level_role_spread':st.median(x['spread'] for x in level_stats),'max_within_level_role_spread':max(x['spread'] for x in level_stats),
'dimension_metrics':dim_metrics}
thresholds={
'spearman_total_vs_target':metrics['spearman_total_vs_target']>=.95,
'kendall_total_vs_level':metrics['kendall_total_vs_level']>=.85,
'adjacent_level_mean_monotonic':metrics['adjacent_level_means_strictly_increasing'],
'cross_level_inversions':metrics['strict_inversion_rate']<=.05,
'within_expected_band':metrics['within_expected_band_count']>=40,
'mae_total':metrics['mae_total']<=4,
'role_bias_median_spread':metrics['median_within_level_role_spread']<=5,
'role_bias_max_spread':metrics['max_within_level_role_spread']<=10}
out={'metrics':metrics,'threshold_results':thresholds,'level_stats':level_stats,'rows':rows}
(P/'gradient_metrics.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
with open(P/'score_comparison.csv','w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['id','role','level','label','target_total','acceptable_total_min','acceptable_total_max','actual_total','error','abs_error','in_band']);w.writeheader();w.writerows([{k:r[k] for k in w.fieldnames} for r in rows])

failed=[k for k,v in thresholds.items() if not v]
lines=['# 50份品質梯度履歷：盲評校準報告','', '## 結論','']
if failed: lines.append('這套評分機制**未完全通過**事先鎖定的內部校準門檻。未通過：'+ '、'.join(failed)+'。')
else: lines.append('這套評分機制通過全部事先鎖定的內部校準門檻，能在本批合成資料中復原由差到近乎完美的設計梯度。')
lines+=['', '這次方法符合指定的模型隔離：主模型產生50份履歷、隱藏10級答案與預期分數；另一個全新gpt-6-astra代理只讀打散後的履歷與固定規則，逐份評分，不讀答案。','', '這仍是內部校準，不是招聘效度驗證。履歷由評分規則反向建構，通過代表規則可辨識自己定義的品質，不代表可預測真人面試、錄取或工作表現。','', '## 核心指標','', '| 指標 | 預設門檻 | 結果 | 通過 |','|---|---:|---:|:---:|',
f'| Spearman：目標分與盲評分排序 | ≥0.95 | {metrics["spearman_total_vs_target"]:.3f} | {"是" if thresholds["spearman_total_vs_target"] else "否"} |',
f'| Kendall：等級與盲評分排序 | ≥0.85 | {metrics["kendall_total_vs_level"]:.3f} | {"是" if thresholds["kendall_total_vs_level"] else "否"} |',
f'| 相鄰等級平均分 | 嚴格遞增 | {"遞增" if metrics["adjacent_level_means_strictly_increasing"] else "有倒置"} | {"是" if thresholds["adjacent_level_mean_monotonic"] else "否"} |',
f'| 相差≥2級的嚴格倒置率 | ≤5% | {metrics["strict_inversion_rate"]:.2%}（{strict_inv}/{eligible}；另有{ties}組同分） | {"是" if thresholds["cross_level_inversions"] else "否"} |',
f'| 落在預設±4分區間 | ≥40/50 | {metrics["within_expected_band_count"]}/50 | {"是" if thresholds["within_expected_band"] else "否"} |',
f'| 總分平均絕對誤差 | ≤4.0 | {metrics["mae_total"]:.2f} | {"是" if thresholds["mae_total"] else "否"} |',
f'| 同級跨職類分差中位數 | ≤5 | {metrics["median_within_level_role_spread"]:.1f} | {"是" if thresholds["role_bias_median_spread"] else "否"} |',
f'| 任一級跨職類最大分差 | ≤10 | {metrics["max_within_level_role_spread"]} | {"是" if thresholds["role_bias_max_spread"] else "否"} |','',
f'盲評整體偏差為 {metrics["bias_total"]:+.2f} 分，單份最大絕對誤差為 {metrics["max_abs_error"]} 分。正值代表相對設計答案偏高。','', '## 十級結果','', '| 等級 | 設計標籤 | 目標分 | 盲評平均 | 最低–最高 | 跨職類分差 |','|---:|---|---:|---:|---:|---:|']
for x in level_stats:lines.append(f'| {x["level"]} | {x["label"]} | {x["target"]} | {x["mean"]:.1f} | {x["min"]}–{x["max"]} | {x["spread"]} |')
lines+=['','## 各分項誤差','', '| 分項 | MAE | 平均偏差 | 最大絕對誤差 |','|---|---:|---:|---:|']
labels={'positioning':'專業定位','achievements':'成果證據','fit':'職務匹配','structure':'結構','wording':'用字','differentiation':'差異化'}
for d,m in dim_metrics.items():lines.append(f'| {labels[d]} | {m["mae"]:.2f} | {m["bias"]:+.2f} | {m["max_abs_error"]} |')
lines+=['','## 方法檢查','', '- 50份不是同質複製：5個職類各有10個品質等級；每級各含5個職類。','- 等級答案、預期分項與接受區間在盲評前寫入private，並保存輸入SHA-256。','- 盲評模型只取得履歷、完整合成JD與v3規則；輸入順序已打散。','- 分析同時計算精確分數誤差與排序；高排序相關不能掩蓋分數校準偏差。','- 同級跨職類分差用來找出評分器是否偏好某類職務或某種量化方式。','', '## 方法論下一步','', '若精確分數門檻失敗但排序通過，應把分數解讀為相對品質訊號，收寬或重設錨點，不能宣稱「81分比80分實質更好」。若職類分差超標，需查看每級五職類的具體扣分，調整對非營收成果、定性成果及責任邊界的規則。','', '要驗證真實招聘效度，下一階段必須固定規則後使用未參與建構的匿名真人履歷與完整JD，由至少兩名HR／用人主管獨立評分；先測人類彼此一致性，再比較模型。PDF解析、ATS匯入與AI來源判定要各自使用專門資料集，不能混入文字品質總分。','', '## 產物','', '- `blind/gradient_resumes.json`：另一模型看到的50份打散履歷。','- `blind/rubric_v3.json`：評分規則。','- `private/answer_key.json`：10級答案與預期分項。','- `independent_scores.json`：另一模型逐份盲評、證據與問題。','- `score_comparison.csv`、`gradient_metrics.json`：逐份誤差與統計。']
(P/'品質梯度履歷驗證報告.md').write_text('\n'.join(lines))
print(json.dumps({'metrics':{k:v for k,v in metrics.items() if k!='dimension_metrics'},'thresholds':thresholds},ensure_ascii=False,indent=2))
