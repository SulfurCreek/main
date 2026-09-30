"""從 HackMD 讀 [求才系統] Sitemap（shortId rkGFjjlPWe），輸出 sitemap_docs.json。

只保留「文件名稱＋shortId」，不存 Sitemap／文件原文（wiki/hackmd_rules.md 規則 A）。
不輸出頁面 URL／aspx 名稱（使用者要求：只要文件名稱）。
需要環境變數 HACKMD_TOKEN；離線重跑 step1／step2 時不需要本步驟（直接用已 commit 的 JSON）。
"""
import os, re, json, pathlib, urllib.request

HERE = pathlib.Path(__file__).parent
OUT = HERE / "sitemap_docs.json"
SITEMAP_SHORT = "rkGFjjlPWe"

req = urllib.request.Request("https://api.hackmd.io/v1/teams/1111-jobdocs/notes",
                             headers={"Authorization": "Bearer " + os.environ["HACKMD_TOKEN"]})
notes = json.load(urllib.request.urlopen(req, timeout=90))
by_id = {n["id"]: n for n in notes}
by_sid = {n["shortId"]: n for n in notes}
sm = by_sid[SITEMAP_SHORT]["content"]

# Sitemap module 序號 → 旅程階段編碼（journey map 路由表：Sitemap 第N節）
STAGE = {"1": "J", "2": "A", "3": "B", "4": "C", "5": "D", "6": "E", "7": "5", "8": "6／7", "9": "6／7"}
REF = re.compile(r"/([A-Za-z0-9_-]{9,22})(?![A-Za-z0-9_/.-])")


def doc_of(token):
    n = by_id.get(token) or by_sid.get(token)
    return None if not n else {"shortId": n["shortId"], "title": " ".join(n["title"].split())}


modules, unmatched, used = [], [], set()   # used：文件只歸第一個出現的 Module（例：聯繫節點內對 A.5 的交叉提示不重複列）
body = sm.split("## 🚧 待確認差異總覽")[0]
for m in re.finditer(r"^### (\d+)\. (.+?)$(.*?)(?=^### \d+\. |\Z)", body, re.M | re.S):
    no, name, blk = m.groups()
    docs, seen = [], set()
    for tok in REF.findall(blk):
        d = doc_of(tok)
        if d is None:
            if re.search(r"[A-Z]", tok) and len(tok) >= 9:   # 排除 /company/... 這類路由
                unmatched.append({"module": f"{no} {name.strip()}", "ref": tok})
            continue
        if d["shortId"] not in seen and d["shortId"] not in used:
            seen.add(d["shortId"]); used.add(d["shortId"]); docs.append(d)
    modules.append({"no": no, "name": name.strip(), "stage": STAGE.get(no, ""), "docs": docs})

# 「待確認差異總覽」內以文件連結列出的聯繫新版文件，歸入該 Module
tail = sm.split("## 🚧 待確認差異總覽")[1] if "## 🚧 待確認差異總覽" in sm else ""
for row in tail.splitlines():
    cells = [c.strip() for c in row.strip().strip("|").split("|")]
    if len(cells) >= 2 and cells[1] in {mm["name"] for mm in modules}:
        mod = next(mm for mm in modules if mm["name"] == cells[1])
        for tok in REF.findall(cells[0]):
            d = doc_of(tok)
            if d and d["shortId"] not in used:
                used.add(d["shortId"]); mod["docs"].append(d)

# journey map 附錄「跨階段共用元件」的 shortId → 文件名稱
md = (HERE.parent / "recruiter_journey_map.md").read_text(encoding="utf-8")
sh = re.search(r"\*\*跨階段共用元件\*\*[^：]*：(.+)", md).group(1)
shared = []
for tok in re.findall(r"[A-Za-z0-9_-]{9,11}", sh):
    d = doc_of(tok)
    if d:
        shared.append(d)

OUT.write_text(json.dumps({"source": "HackMD [求才系統] Sitemap", "sitemap_shortId": SITEMAP_SHORT,
                           "modules": modules, "shared": shared, "unmatched_refs": unmatched},
                          ensure_ascii=False, indent=1), encoding="utf-8")
print({m["no"] + " " + m["name"]: len(m["docs"]) for m in modules}, "shared:", len(shared), "unmatched:", unmatched)
