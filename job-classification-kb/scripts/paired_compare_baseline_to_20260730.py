"""基準版（7/9）→ 20260730 同批配對比較，跳過 20260720 中間版本。

沿用 paired_compare_20260720_to_20260730.py 的標題 join 做法：
把新模型（20260730）對同一標題的推薦，接到基準版每一列原有的廠商 duty 選擇上重新分類，
比較「同一組廠商選擇」在「最初模型 vs 20260730 模型」下的判定。
"""
import pandas as pd

old = pd.read_pickle('/tmp/baseline_0709.pkl')
new = pd.read_pickle('/tmp/new_20260730.pkl')

rec_cols = [f'職類推薦{i}' for i in range(1, 11)]
duty_cols = [f'duty{i}' for i in range(5)]

new_recs_by_title = new.drop_duplicates('職缺名稱').set_index('職缺名稱')[rec_cols]

old = old.copy()
old['duties'] = old[duty_cols].apply(lambda r: [d for d in r if pd.notna(d)], axis=1)

joined = old.join(new_recs_by_title, on='職缺名稱', rsuffix='_new')
new_rec_cols = [c + '_new' for c in rec_cols]

n_old = len(old)
covered = joined[new_rec_cols[0]].notna().sum()
print(f"基準版 {n_old:,} 筆，標題可對到 20260730 推薦的有 {covered:,} 筆（{covered/n_old:.1%}）")


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
old_rec_cols = rec_cols
sub['old_scenario'] = sub.apply(lambda r: classify_from(r['duties'], [r[c] for c in old_rec_cols]), axis=1)
sub['new_scenario'] = sub.apply(lambda r: classify_from(r['duties'], [r[c] for c in new_rec_cols]), axis=1)

print(f"\n可配對職缺（同一批廠商 duty 選擇，基準版 vs 20260730）: {len(sub):,} 筆\n")

for label, col in [('基準版(7/9)', 'old_scenario'), ('20260730', 'new_scenario')]:
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
print(f"真命中率（前5名內）  基準: {sub['old_hit5'].mean():.1%}  20260730: {sub['new_hit5'].mean():.1%}  "
      f"變化: {(sub['new_hit5'].mean()-sub['old_hit5'].mean())*100:+.1f}pp")


def first_hit(duties, recs):
    recs = [r for r in recs if pd.notna(r)]
    return bool(recs) and recs[0] in duties


sub['old_first'] = sub.apply(lambda r: first_hit(r['duties'], [r[c] for c in old_rec_cols]), axis=1)
sub['new_first'] = sub.apply(lambda r: first_hit(r['duties'], [r[c] for c in new_rec_cols]), axis=1)
print(f"第1名就命中  基準: {sub['old_first'].mean():.1%}  20260730: {sub['new_first'].mean():.1%}")


def coverage(duties, recs):
    recs = [r for r in recs if pd.notna(r)]
    if not duties:
        return None
    return len(set(recs[:5]) & set(duties)) / len(duties)


sub['old_cov'] = sub.apply(lambda r: coverage(r['duties'], [r[c] for c in old_rec_cols]), axis=1)
sub['new_cov'] = sub.apply(lambda r: coverage(r['duties'], [r[c] for c in new_rec_cols]), axis=1)
print(f"前5名平均覆蓋率  基準: {sub['old_cov'].mean():.1%}  20260730: {sub['new_cov'].mean():.1%}")

print("\n=== 轉移矩陣（基準情境 \\ 20260730情境） ===")
mat = pd.crosstab(sub['old_scenario'], sub['new_scenario'])
mat = mat.reindex(index=['best', 'enhancement', 'worst', 'other'],
                   columns=['best', 'enhancement', 'worst', 'other'], fill_value=0)
print(mat)

rescued = mat.loc['worst', ['best', 'enhancement', 'other']].sum()
worst_total = mat.loc['worst'].sum()
regressed = mat.loc[['best', 'enhancement', 'other'], 'worst'].sum()
print(f"\n救回（基準worst→20260730非worst）: {rescued:,} / 基準worst {worst_total:,} = {rescued/worst_total:.1%}")
print(f"退步（基準非worst→20260730worst）: {regressed:,}")
print(f"淨值: {rescued - regressed:+,}")

sub.to_pickle('/tmp/paired_baseline_to_20260730.pkl')
print("\n已存 /tmp/paired_baseline_to_20260730.pkl")
