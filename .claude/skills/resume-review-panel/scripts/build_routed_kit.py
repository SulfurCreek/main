#!/usr/bin/env python3
"""分流版驗證套件產生器：依 jd/routing.tsv 把「規則＋履歷＋職缺」組成一次呼叫一個的封包。

用法：python3 build_routed_kit.py --version v10.4 --resume career/drafts/v10.4/resume-v10.4.txt
輸出：career/review-panel/handoff/<version>/{00-start-here.md, F-<code>.md, L-<batch>.md}
分流表、F 層職缺摘要、L 層職缺卡分別在 career/review-panel/jd/{routing.tsv, full/, light-cards.md}。
"""
import argparse, csv, datetime, os, re, shutil

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), *[".."] * 4))
KIT = os.path.join(os.path.dirname(__file__), "..", "kit")
JD = os.path.join(ROOT, "career/review-panel/jd")
ANCHORS = ["8ocje", "92io8", "94le0", "950oe", "8kebd"]
BATCH_NAME = {"LA": "支付與金流", "LB": "B2B SaaS 與系統平台", "LC": "消費型 App、內容與成長",
              "LD": "專案型與垂直產業", "LE": "AI 與數位轉型"}

ap = argparse.ArgumentParser()
ap.add_argument("--version", required=True)
ap.add_argument("--resume", required=True)
a = ap.parse_args()

rd = lambda p: open(p, encoding="utf8").read().strip()
rows = list(csv.DictReader(open(os.path.join(JD, "routing.tsv"), encoding="utf8"), delimiter="\t"))
F = [r for r in rows if r["tier"] == "F"]
L = [r for r in rows if r["tier"] == "L"]
X = [r for r in rows if r["tier"] == "X"]
batches = {}
for r in L:
    batches.setdefault(r["batch"], []).append(r)

resume = f"# 履歷 {a.version}（完整；以下是唯一的候選人資料）\n\n```text\n{rd(os.path.join(ROOT, a.resume))}\n```"
cards = rd(os.path.join(JD, "light-cards.md"))
card = {m.group(1): m.group(0).strip() for m in re.finditer(r"^### j-(\w+)｜.*?(?=^### |^## |\Z)", cards, re.M | re.S)}

out = os.path.join(ROOT, "career/review-panel/handoff", a.version)
shutil.rmtree(out, ignore_errors=True)
os.makedirs(out)
w = lambda name, s: open(os.path.join(out, name), "w", encoding="utf8").write(s.strip() + "\n")
sep = "\n\n---\n\n"

rules_f, rules_l = rd(os.path.join(KIT, "rules-full.md")), rd(os.path.join(KIT, "rules-light.md"))
for r in F:
    jd = rd(os.path.join(JD, "full", r["code"] + ".md"))
    jd = re.sub(r"^## ", f"## j-{r['code']}｜", jd, count=1)
    w(f"F-{r['code']}.md", f"<!-- 封包 F-{r['code']}｜{a.version}｜整份貼進新對話 -->" + sep + rules_f + sep + resume
      + sep + "# 本次審查的職缺（只有這一份）\n\n" + jd + sep + "請依規則 F4 輸出：JSON（單行）→ 審查者的質疑 → 評語。")
for b, rs in sorted(batches.items()):
    missing = [r["code"] for r in rs if r["code"] not in card]
    assert not missing, f"light-cards.md 缺卡：{missing}"
    body = "\n\n".join(card[r["code"]] for r in rs)
    w(f"L-{b}.md", f"<!-- 封包 L-{b}｜{a.version}｜整份貼進新對話 -->" + sep + rules_l + sep + resume
      + sep + f"# 本批職缺（{b}｜{BATCH_NAME.get(b, '')}｜{len(rs)} 份；逐份獨立判斷）\n\n" + body
      + sep + f"請依規則 L2 輸出 {len(rs)} 行 JSON（batch 填 {b}）＋3 行批次摘要。")

n_lb, n_anchor = len(batches), len([r for r in F if r["code"] in ANCHORS])
fill = {
    "VERSION": a.version, "DATE": datetime.date.today().isoformat(), "N_TOTAL": len(rows),
    "N_F": len(F), "N_L": len(L), "N_LB": n_lb, "N_X": len(X), "N_CALLS": len(F) + n_lb,
    "N_ANCHOR": n_anchor, "N_MANUAL": n_lb + n_anchor,
    "F_TABLE": "\n".join(f"| `F-{r['code']}.md` | {r['title']} | {r['company']} | {r['cluster']} | {'★' if r['code'] in ANCHORS else ''} |" for r in F),
    "L_TABLE": "\n".join(f"| `L-{b}.md` | {BATCH_NAME.get(b, '')} | {len(rs)} | {'、'.join(r['code'] for r in rs)} |" for b, rs in sorted(batches.items())),
    "X_TABLE": "\n".join(f"| {r['title']}（{r['code']}） | {r['company']} | {r['note']} |" for r in X),
}
s = rd(os.path.join(KIT, "start-here.md"))
for k, v in fill.items():
    s = s.replace("{" + k + "}", str(v))
w("00-start-here.md", s)
sizes = {f: os.path.getsize(os.path.join(out, f)) for f in os.listdir(out)}
print(f"{out}: {len(sizes)} 檔；F 封包約 {max(v for k, v in sizes.items() if k.startswith('F-')) // 1024} KB，"
      f"L 封包約 {max(v for k, v in sizes.items() if k.startswith('L-')) // 1024} KB")
