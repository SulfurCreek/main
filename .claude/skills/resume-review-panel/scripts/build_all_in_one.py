#!/usr/bin/env python3
"""一次對話版驗證封包：L 五批＋F 錨點五份合成一檔，給 ChatGPT／Gemini。
用法：python3 build_all_in_one.py --version v10.8（需先跑 build_routed_kit.py）"""
import argparse, os, re
ap = argparse.ArgumentParser(); ap.add_argument("--version", required=True); a = ap.parse_args()
K = os.path.join(os.path.dirname(__file__), "..", "kit")
H = "career/review-panel/handoff/" + a.version
r = lambda p: open(p, encoding="utf8").read().strip()
res = re.search(r"# 履歷 .*?```\n", r(f"{H}/F-8ocje.md"), re.S).group(0)
part = lambda f, s: (lambda t: t[t.index(s):].rsplit("\n---\n", 1)[0].strip())(r(f))
o = [r(os.path.join(K, "all-in-one-head.md")).replace("{VERSION}", a.version), r(os.path.join(K, "rules-light.md")), "---",
     r(os.path.join(K, "rules-full.md")), "---", res, "---", "# 第一部分：輕量批次"]
for b in ["LA", "LB", "LC", "LD", "LE"]:
    o += [f"## === L-{b} ===", part(f"{H}/L-{b}.md", "# 本批職缺").replace("# 本批", "### 本批", 1)]
o += ["---", "# 第二部分：完整審查（5 份）"]
for c in ["8ocje", "92io8", "94le0", "950oe", "8kebd"]:
    o += [f"## === F-{c} ===", part(f"{H}/F-{c}.md", "## j-")]
o += ["---", r(os.path.join(K, "all-in-one-report.md")).replace("{VERSION}", a.version)]
open(f"{H}/ALL-IN-ONE-chatgpt.md", "w", encoding="utf8").write("\n\n".join(o) + "\n")
print(f"{H}/ALL-IN-ONE-chatgpt.md")
