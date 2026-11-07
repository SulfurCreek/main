#!/usr/bin/env python3
"""由 raw/*.json 自動產生報告草稿（數字與表格全由腳本算，主代理只補 3 行結論）。

  python3 run_report.py --run <runs/日期-名稱> [--ats ats_a.json ats_b.json ...]

輸出 <run>/report-draft.md：決定／Level／六維度（每版一列）、HR／HM 兩版有差的題（只列有差的）、B 比較與順序敏感、
共同缺口（≥ 一半輪次出現的 issue claim 前綴）、blocking／schema 違規計數。ATS 五塊由 ats_check.py 自己印，這裡只放連結。
全部是描述性結果；human_calibration: not_performed。
"""
import argparse, glob, json, os, re, collections as C, statistics as S, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import schema_v4 as sv


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--run', required=True); a = ap.parse_args()
    raw = f'{a.run}/raw'; man = json.load(open(f'{raw}/manifest.json', encoding='utf8'))
    vers = sorted({re.match(r'A_(.+)_r\d+\.json', os.path.basename(p)).group(1) for p in glob.glob(f'{raw}/A_*_r*.json')})
    D = {}
    for v in vers:
        rs = []
        for p in sorted(glob.glob(f'{raw}/A_{v}_r*.json')):
            try: o = json.load(open(p, encoding='utf8'))
            except Exception as e: rs.append(dict(_err=f'technical_failure {os.path.basename(p)}: {e}')); continue
            o['_errs'] = sv.check(o); rs.append(o)
        D[v] = rs
    out = [f'# 報告草稿（自動產生，{os.path.basename(a.run)}；human_calibration: not_performed）\n', '## 1. 決定與六維度\n',
           '| 版本 | 輪數 | 決定 | Level | ' + ' | '.join(sv.DIMS) + ' | schema 違規 | blocking |', '| :-- | :-: | :-- | :-: | ' + ' | '.join([':-:'] * 6) + ' | :-: | :-: |']
    for v, rs in D.items():
        ok = [r for r in rs if '_err' not in r]
        dec = dict(C.Counter(r['decision']['recommendation'] for r in ok)); lv = [r['spectrum']['level'] for r in ok if isinstance(r.get('spectrum', {}).get('level'), int)]
        dm = {d: dict(C.Counter(x['rating'] for r in ok for x in r['dimensions'] if x['id'] == d)) for d in sv.DIMS}
        bl = sum(1 for r in ok for i in r.get('issues', []) if i.get('severity') == 'blocking')
        out.append(f'| {v} | {len(rs)}（失敗 {len(rs) - len(ok)}） | {dec} | {S.median(lv) if lv else "-"}（{min(lv) if lv else "-"}–{max(lv) if lv else "-"}） | ' +
                   ' | '.join(' '.join(f'{k}×{n}' for k, n in dm[d].items()) for d in sv.DIMS) + f' | {sum(1 for r in ok if r["_errs"])} | {bl} |')
    base = [v for v in vers if not v.endswith('anon')]
    for key, ids, title in (('hr_questions', sv.HR, 'HR'), ('content_questions', sv.HM, 'HM')):
        cnt = {v: {i: C.Counter(q.get('status') for r in D[v] if '_err' not in r for q in r.get(key, []) if q.get('rule_id') == i) for i in ids} for v in vers}
        rows = [f'| {i} | ' + ' | '.join(f'{dict(cnt[v][i])}' for v in base) + ' |' for i in ids if len({tuple(sorted(cnt[v][i].items())) for v in base}) > 1]
        out += [f'\n## {title} 兩版判定有差的題（沒列的題兩版相同）\n', '| 題 | ' + ' | '.join(base) + ' |', '| :-- | ' + ' | '.join([':--'] * len(base)) + ' |'] + (rows or ['| （無） |'])
    out.append('\n## 共同缺口（≥ 一半輪次出現；claim 前 14 字合併）\n')
    for v in base:
        n = len([r for r in D[v] if '_err' not in r]); c = C.Counter()
        for r in D[v]:
            if '_err' in r: continue
            for k in {sv.norm_claim(g)[:14] for g in r.get('key_gaps', [])}: c[k] += 1
        out.append(f'- {v}：' + ('；'.join(f'{k}…×{m}' for k, m in c.most_common(6) if m * 2 >= n) or '無'))
    bs = sorted(glob.glob(f'{raw}/B_r*.json'))
    if bs:
        t = C.Counter(); by = C.defaultdict(list)
        for p in bs:
            rid = os.path.basename(p)[:-5]; o = json.load(open(p, encoding='utf8')); order = man.get(rid + '_order', '?')
            m = dict(x.split('=') for x in order.split('/')) if '=' in order else {}
            w = m.get(o.get('preference'), o.get('preference')); t[w] += 1; by[order].append(w)
        vs = [{w for w in v if w in base} for v in by.values()]
        flip = len(by) > 1 and len(set().union(*vs)) > 1
        out += ['\n## 兩版直接比較（甲乙順序逐輪交換）\n', f'合計：{dict(t)}；順序敏感：{"⚠️ 是（交換順序後偏好的版本不同）" if flip else "否"}']
    open(f'{a.run}/report-draft.md', 'w', encoding='utf8').write('\n'.join(out) + '\n'); print('\n'.join(out))


if __name__ == '__main__':
    main()
