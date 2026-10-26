#!/usr/bin/env python3
"""多職缺驗證（v4.2 規準）：每份 JD × 每個版本 A 審查 1 輪＋每份 JD 一輪 B（甲乙順序依 JD 序號交替）。

  python3 build_multi.py --run <runs/日期-名稱> --digest career/104/jd-digest-A.md \
      --resume v9.4=path.txt --resume v9.5=path.txt

會先把 digest 依 `## <編號>.` 拆成 career/review-panel/jd/a/<編號>.md（已存在則覆寫），再寫：
  <run>/raw/prompt_A_<jd>_<標籤>.md、prompt_B_<jd>.md、manifest.json、<run>/RUN.md
彙整：python3 multi_report.py --run <run>
"""
import argparse, hashlib, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_run import prefix, b_prompt, HERE, RP


def split(digest):
    txt = open(digest, encoding='utf8').read()
    parts = re.split(r'^## (\d+)\. ', txt, flags=re.M)
    out = {}
    os.makedirs(f'{RP}/jd/a', exist_ok=True)
    for i in range(1, len(parts), 2):
        jid = f'jd{int(parts[i]):02d}'
        body = '## ' + parts[i + 1].strip()
        open(f'{RP}/jd/a/{jid}.md', 'w', encoding='utf8').write(body + '\n')
        out[jid] = body
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--run', required=True); ap.add_argument('--digest', required=True)
    ap.add_argument('--resume', action='append', required=True)
    a = ap.parse_args()
    raw = f'{a.run}/raw'; os.makedirs(raw, exist_ok=True)
    jds = split(a.digest)
    res = {k: open(v, encoding='utf8').read() for k, v in (x.split('=', 1) for x in a.resume)}
    ks = list(res); man = {'jds': list(jds), 'resumes': {k: hashlib.sha256(t.encode()).hexdigest()[:16] for k, t in res.items()}}
    jobs = []
    for n, (jid, jd) in enumerate(jds.items()):
        pre = prefix(jd)
        for k in ks:
            rid = f'A_{jid}_{k}'
            open(f'{raw}/prompt_{rid}.md', 'w', encoding='utf8').write(pre + res[k]); jobs.append(rid)
        if len(ks) == 2:
            x, y = (ks[0], ks[1]) if n % 2 == 0 else (ks[1], ks[0])
            open(f'{raw}/prompt_B_{jid}.md', 'w', encoding='utf8').write(b_prompt(jd, res[x], res[y]))
            man[f'B_{jid}_order'] = f'甲={x}/乙={y}'; jobs.append(f'B_{jid}')
    json.dump(man, open(f'{raw}/manifest.json', 'w'), ensure_ascii=False, indent=1)
    open(f'{a.run}/RUN.md', 'w', encoding='utf8').write(
        f'# 執行單（多職缺）\n子代理指令（一句話）：\n\n```\n讀 {raw}/prompt_<ID>.md 並照做；用「一次」Bash 指令把單行 JSON 寫到 {raw}/<ID>.json；'
        f'A 類接著執行 python3 {HERE}/schema_v4.py validate {raw}/<ID>.json；不要讀其他檔案；回覆只寫 done＋decision。\n```\n\n'
        f'工作清單（{len(jobs)}）：' + '、'.join(jobs) + f'\n\n完成後：python3 {HERE}/multi_report.py --run {a.run}\n')
    print(f'{len(jds)} 份 JD；{len(jobs)} 個請求；{a.run}/RUN.md')


if __name__ == '__main__':
    main()
