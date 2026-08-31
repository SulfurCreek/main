"""20260720 → 20260730 同批配對比較（rawdata skill Step 2）。

這次新檔沒有 employeeNo 重疊（0%），但職缺名稱有 87.1% 重疊，且已驗證
「模型輸出 100% 由標題決定」，所以改用「標題 join」做同一批職缺的配對：

對舊檔每一列（職缺、廠商實際送出的 duty，不變），把「新模型對同一個標題的推薦」
接上去重新分類——這樣比較的是「同一組廠商選擇 duty」在「舊模型 vs 新模型」下的判定，
排除了新檔案樣本組成（新增大量新職缺）的干擾。
"""
import pandas as pd, numpy as np

old = pd.read_pickle('/tmp/old_20260720.pkl')
new = pd.read_pickle('/tmp/new_20260730.pkl')

rec_cols = [f'職類推薦{i}' for i in range(1, 11)]
duty_cols = [f'duty{i}' for i in range(5)]

# 標題 -> 新模型推薦（每個標題理論上唯一，取第一筆；已知內部一致率 99.8%）
new_recs_by_title = new.drop_duplicates('職缺名稱').set_index('職缺名稱')[rec_cols]

old = old.copy()
old['duties'] = old[duty_cols].apply(lambda r: [d for d in r if pd.notna(d)], axis=1)

joined = old.join(new_recs_by_title, on='職缺名稱', rsuffix='_new')
matched = joined[joined[rec_cols[0] + '_new'].notna()] if (rec_cols[0] + '_new') in joined.columns else joined
# 若標題本身在新舊欄位重名，需重新對齊：新推薦欄位用 _new 後綴
new_rec_cols = [c + '_new' if c + '_new' in joined.columns else c for c in rec_cols]

n_old = len(old)
covered = joined[new_rec_cols[0]].notna().sum()
print(f"舊檔 {n_old:,} 筆，標題可對到新模型推薦的有 {covered:,} 筆（{covered/n_old:.1%}）")

def classify_from(duties, recs):
    if not duties or not recs or all(pd.isna(x) for x in recs):
        return None
    recs = [r for r in recs if pd.notna(r)]
    top5, rank6_10 = recs[:5], recs[5:10]
    hit5 = set(top5) & set(duties)
    hit10_extra = set(rank6_10) & set(duties)
    n_duty = len(duties)
    if recs and recs[0] in duties and len(hit5) == n_duty:
        return 'best'
    if not hit5 and hit10_extra:
        return 'enhancement'
    if not hit5 and not hit10_extra:
        return 'worst'
    return 'other'

sub = joined[joined[new_rec_cols[0]].notna()].copy()
old_rec_cols = [f'職類推薦{i}' for i in range(1, 11)]
sub['old_scenario'] = sub.apply(lambda r: classify_from(r['duties'], [r[c] for c in old_rec_cols]), axis=1)
sub['new_scenario'] = sub.apply(lambda r: classify_from(r['duties'], [r[c] for c in new_rec_cols]), axis=1)

print(f"\n可配對職缺（同一批廠商 duty 選擇，舊模型 vs 新模型）: {len(sub):,} 筆\n")

for label, col in [('舊模型(20260720)', 'old_scenario'), ('新模型(20260730)', 'new_scenario')]:
    dist = sub[col].value_counts()
    tot = len(sub)
    print(f"[{label}]")
    for k in ['best', 'enhancement', 'worst', 'other']:
        v = dist.get(k, 0)
        print(f"  {k:<12}{v:>10,}  {v/tot:>7.1%}")
    print()

def hit5(duties, recs):
    recs = [r for r in recs if pd.notna(r)]
    return bool(set(recs[:5]) & set(duties))

sub['old_hit5'] = sub.apply(lambda r: hit5(r['duties'], [r[c] for c in old_rec_cols]), axis=1)
sub['new_hit5'] = sub.apply(lambda r: hit5(r['duties'], [r[c] for c in new_rec_cols]), axis=1)
print(f"真命中率（前5名內）  舊: {sub['old_hit5'].mean():.1%}  新: {sub['new_hit5'].mean():.1%}  "
      f"變化: {(sub['new_hit5'].mean()-sub['old_hit5'].mean())*100:+.1f}pp")

print("\n=== 轉移矩陣（舊情境 \\ 新情境） ===")
mat = pd.crosstab(sub['old_scenario'], sub['new_scenario'])
mat = mat.reindex(index=['best', 'enhancement', 'worst', 'other'],
                   columns=['best', 'enhancement', 'worst', 'other'], fill_value=0)
print(mat)

rescued = mat.loc['worst', ['best', 'enhancement', 'other']].sum()
worst_total = mat.loc['worst'].sum()
regressed = mat.loc[['best', 'enhancement', 'other'], 'worst'].sum()
print(f"\n救回（舊worst→新非worst）: {rescued:,} / 舊worst {worst_total:,} = {rescued/worst_total:.1%}")
print(f"退步（舊非worst→新worst）: {regressed:,}")

sub.to_pickle('/tmp/paired_20260720_to_20260730.pkl')
print("\n已存 /tmp/paired_20260720_to_20260730.pkl")
