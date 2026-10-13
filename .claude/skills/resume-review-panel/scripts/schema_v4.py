#!/usr/bin/env python3
"""規準 v4 的輸出驗證與彙整（career/review-panel/rubric-v4.md §6–7）。

  python3 schema_v4.py validate <A輸出.json>...          # 檢查 enums、必填、null 規則；違規印出並 exit 1
  python3 schema_v4.py aggregate --run <資料夾> [--manifest manifest.json]
      讀 V_*.json（可見性壓力測試）、A_<版本>_r*.json（獨立審查）、B_r*.json（比較），
      先列每輪決定，再列中位數與範圍；比較列甲／乙／平手次數並檢查順序敏感；issue 以 claim 去重。
彙整結果是描述性的，不是招聘勝率；human_calibration: not_performed。
"""
import json, sys, glob, os, re, statistics as S, collections as C, argparse

DIMS = ['positioning', 'role_evidence', 'decision_depth', 'outcome_quality', 'ownership', 'readability']
RATINGS = ['強', '足夠', '待補', '未呈現', '不適用']
REQ = ['supported', 'partial', 'unknown', 'contradicted', 'not_applicable']
SEV = ['blocking', 'interview_follow_up', 'editorial']
REC = ['interview', 'clarify_first', 'not_matched', 'insufficient_info']
KINDS = ['context', 'output', 'outcome', 'decision', 'in_progress']
PREF = ['甲', '乙', '無明確偏好', '兩者均須先修正']
HR = [f'HR{i:02d}' for i in range(1, 13)]
HRS = ['supported', 'partial', 'unknown', 'not_applicable']
SRC = [f'S{i:02d}' for i in range(1, 51)]


def check(o):
    err = []
    ver = str(o.get('rubric_version'))
    if ver not in ('4.0', '4.1'): err.append('rubric_version 不是 4.0／4.1')
    if ver == '4.1':
        hq = o.get('hr_questions', [])
        if not hq: err.append('v4.1 缺 hr_questions')
        for q in hq:
            if q.get('rule_id') not in HR: err.append(f'hr_questions rule_id 非法：{q.get("rule_id")}')
            if q.get('status') not in HRS: err.append(f'{q.get("rule_id")} status 非法：{q.get("status")}')
            if q.get('status') in ('supported', 'partial') and not q.get('resume_evidence'): err.append(f'{q.get("rule_id")} 缺 resume_evidence')
        for i in o.get('issues', []):
            if i.get('rule_id') not in HR: err.append(f'issue {i.get("id")} 缺合法 rule_id')
            bad = [x for x in i.get('source_ids', []) if x not in SRC]
            if bad: err.append(f'issue {i.get("id")} source_ids 不在 registry：{bad}')
    if o.get('human_calibrated') is not False: err.append('human_calibrated 必須為 false')
    ds = {d.get('id'): d for d in o.get('dimensions', [])}
    for d in DIMS:
        if d not in ds: err.append(f'缺維度 {d}')
        elif ds[d].get('rating') not in RATINGS: err.append(f'{d}.rating 非法：{ds[d].get("rating")}')
    for r in o.get('requirements', []):
        if r.get('status') not in REQ: err.append(f'requirement {r.get("id")} status 非法')
        if r.get('blocks_interview') and r.get('status') != 'contradicted':
            err.append(f'requirement {r.get("id")}：只有 contradicted（有證據顯示不符）可阻擋面試')
    for i in o.get('issues', []):
        if i.get('severity') not in SEV: err.append(f'issue {i.get("id")} severity 非法')
    for r in o.get('results', []):
        if not set(r.get('kinds', [])) <= set(KINDS): err.append(f'result kinds 非法：{r.get("kinds")}')
    rec = o.get('decision', {}).get('recommendation')
    if rec not in REC: err.append(f'recommendation 非法：{rec}')
    if len(o.get('interview_questions', [])) > 8: err.append('面試追問超過 8 題')
    t = o.get('tests', {})
    for k in ('pdf_extraction', 'ats_import'):
        if t.get(k) not in ('not_tested', 'tested'): err.append(f'tests.{k} 未標示')
    if t.get('ai_provenance') not in ('indeterminate_from_text_alone', 'known_ai_assisted'): err.append('ai_provenance 未標示')
    lv = o.get('spectrum', {}).get('level')
    if lv is not None and not (isinstance(lv, int) and 1 <= lv <= 10): err.append('level 非 1–10 整數')
    return err


def load(p):
    try:
        return json.load(open(p, encoding='utf8')), None
    except Exception as e:
        return None, f'technical_failure: {e}'


def norm_claim(s):
    return re.sub(r'[\s「」『』"“”，。、；：:,.]', '', s or '')[:18]


def aggregate(run, manifest):
    man = json.load(open(manifest, encoding='utf8')) if manifest and os.path.exists(manifest) else {}
    out = ['# 規準 v4 彙整（描述性；human_calibration: not_performed）\n']
    # V
    out.append('## V 截斷文字可見性壓力測試（遮罩請求，未見全文）\n\n| 版本 | 輪 | 職稱 | 公司 | 年資 | 可見的職缺證據數 | unknown |\n| :-- | :-: | :-- | :-- | :-- | :-: | :-- |')
    for p in sorted(glob.glob(f'{run}/V_*.json')):
        o, e = load(p); name = os.path.basename(p)[2:-5]; ver, r = name.rsplit('_', 1)
        if e: out.append(f'| {ver} | {r} | {e} | | | | |'); continue
        f = lambda k: f'{o[k]["value"]}{"" if o[k].get("visible") else "（不可見）"}'
        out.append(f'| {ver} | {r} | {f("title")} | {f("company")} | {f("years")} | {len(o.get("job_evidence_visible", []))} | {"、".join(o.get("unknown", []))[:60]} |')
    # A
    vers = sorted({re.match(r'A_(.+)_r\d+\.json', os.path.basename(p)).group(1) for p in glob.glob(f'{run}/A_*_r*.json')})
    out.append('\n## A 獨立內容審查（每份單獨、新 context）\n')
    summary = {}
    for v in vers:
        rows, lv, recs, dimc, sen, issues, errs = [], [], [], C.defaultdict(C.Counter), C.defaultdict(C.Counter), C.Counter(), []
        for p in sorted(glob.glob(f'{run}/A_{v}_r*.json')):
            o, e = load(p); rid = os.path.basename(p)[:-5].rsplit('_', 1)[1]
            if e: rows.append(f'| {rid} | {e} | | |'); continue
            bad = check(o)
            if bad: errs.append(f'{rid}: ' + '；'.join(bad))
            rec = o['decision']['recommendation']; recs.append(rec)
            l = o.get('spectrum', {}).get('level'); lv.append(l)
            for d in o['dimensions']: dimc[d['id']][d['rating']] += 1
            for k, x in o.get('seniority', {}).items(): sen[k][x] += 1
            seen = set()
            for i in o.get('issues', []):
                key = (i['severity'], norm_claim(i.get('claim')))
                if key in seen: continue  # 同一缺口在同一輪只計一次
                seen.add(key); issues[key] += 1
            rows.append(f'| {rid} | {rec} | {l} | {sum(1 for r in o.get("requirements", []) if r["status"]=="supported")}/{len(o.get("requirements", []))} |')
        lvv = [x for x in lv if isinstance(x, int)]
        summary[v] = dict(recs=C.Counter(recs), lv=lvv)
        out.append(f'### {v}\n\n| 輪 | 招聘決定 | Level | requirements supported |\n| :-: | :-- | :-: | :-: |\n' + '\n'.join(rows))
        if lvv: out.append(f'\nLevel 中位數 {S.median(lvv)}、範圍 {min(lvv)}–{max(lvv)}（±1 級為粗略範圍）；決定：{dict(C.Counter(recs))}')
        out.append('\n維度評等分布：\n\n| 維度 | ' + ' | '.join(RATINGS) + ' |\n| :-- |' + ' :-: |' * len(RATINGS))
        for d in DIMS: out.append(f'| {d} | ' + ' | '.join(str(dimc[d][r]) for r in RATINGS) + ' |')
        hqc = C.defaultdict(C.Counter)
        for p in sorted(glob.glob(f'{run}/A_{v}_r*.json')):
            o, e = load(p)
            for q in (o or {}).get('hr_questions', []): hqc[q.get('rule_id')][q.get('status')] += 1
        if hqc:
            out.append('\n人資十二問（每題各輪狀態）：\n\n| 題 | ' + ' | '.join(HRS) + ' |\n| :-- |' + ' :-: |' * len(HRS))
            for r in HR: out.append(f'| {r} | ' + ' | '.join(str(hqc[r][x]) for x in HRS) + ' |')
        out.append('\n資深能力分布（分別評，不是逐級）：' + '；'.join(f'{k} {dict(c)}' for k, c in sen.items()))
        top = [(k, n) for k, n in issues.most_common() if n >= 2 or k[0] == 'blocking']
        out.append('\n重複出現或 blocking 的 issue（同輪去重；重複≠正確）：')
        out += [f'- [{k[0]}] ×{n}：{k[1]}…' for k, n in top[:15]] or ['- 無']
        if errs: out.append('\n⚠️ schema 違規（保留該輪，標示）：\n' + '\n'.join('- ' + x for x in errs))
    # B
    out.append('\n## B 版本比較（甲乙順序每輪交換）\n\n| 輪 | 順序 | 偏好 | 偏好的版本 | 理由 |\n| :-: | :-- | :-- | :-- | :-- |')
    tally = C.Counter(); byorder = C.defaultdict(list)
    for p in sorted(glob.glob(f'{run}/B_r*.json')):
        o, e = load(p); rid = os.path.basename(p)[:-5]; order = man.get(rid + '_order', '?')
        if e: out.append(f'| {rid} | {order} | {e} | | |'); continue
        pref = o.get('preference'); m = dict(x.split('=') for x in order.split('/')) if '=' in order else {}
        winner = m.get(pref, pref); tally[winner] += 1; byorder[order].append(winner)
        out.append(f'| {rid} | {order} | {pref} | {winner} | {str(o.get("reason", ""))[:80]} |')
    out.append(f'\n合計：{dict(tally)}（描述性，不是勝率）')
    vers_pref = [{w for w in v if w not in ('無明確偏好', '兩者均須先修正')} for v in byorder.values()]
    flip = len(byorder) > 1 and len(set().union(*vers_pref)) > 1
    mixed = len({tuple(sorted(set(v))) for v in byorder.values()}) > 1
    out.append('順序敏感：' + ('⚠️ 交換順序後偏好的版本翻轉，標示為順序敏感' if flip else
               ('未翻轉成另一版本；但兩種順序下的判定類別不完全相同（照實列出）' if mixed else '交換順序後偏好一致')))
    return '\n'.join(out), summary


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', choices=['validate', 'aggregate'])
    ap.add_argument('files', nargs='*')
    ap.add_argument('--run'); ap.add_argument('--manifest')
    a = ap.parse_args()
    if a.mode == 'validate':
        bad = 0
        for f in a.files:
            o, e = load(f); errs = [e] if e else check(o)
            print(f, '✅' if not errs else '❌ ' + '；'.join(errs)); bad += bool(errs)
        sys.exit(1 if bad else 0)
    print(aggregate(a.run, a.manifest)[0])
