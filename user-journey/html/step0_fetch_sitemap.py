"""從 HackMD 讀 [求才系統] Sitemap（shortId rkGFjjlPWe），輸出 sitemap_docs.json。

只保留「文件名稱＋shortId」，不存 Sitemap／文件原文（wiki/hackmd_rules.md 規則 A）。
不輸出頁面 URL／aspx 名稱（使用者要求：只要文件名稱）。
需要環境變數 HACKMD_TOKEN；離線重跑 step1／step2 時不需要本步驟（直接用已 commit 的 JSON）。
"""
import os, re, json, pathlib, subprocess, tempfile, urllib.request

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


def parse_tree(blk):
    """Sitemap 程式碼區塊 → 頁面節點 [{name, depth, group, tag}]。只留頁面名稱，不留 URL／aspx 對照（登入節點本身即以 aspx 命名者除外）"""
    m = re.search(r"```\n(.*?)```", blk, re.S)
    nodes = []
    for i, ln in enumerate(m.group(1).splitlines() if m else []):
        pm = re.match(r"^([│├└─\s]*)(.+)$", ln)
        if not pm or i == 0 or pm.group(2).startswith(("🔧", "🚧")):
            continue
        depth, t = len(pm.group(1)) // 4, pm.group(2)
        t = re.sub(r"^✅\s*開發中新功能：", "", t)
        tag = "new" if "【new】" in t else ""
        t = t.replace("【new】", "")
        name = (t.split("→")[0] if "→" in t else re.split(r"\s*【|（", t)[0]).strip()
        name = re.sub(r"\s*【[^】]*】.*$", "", name)
        if name:
            nodes.append({"name": name.rstrip("/"), "depth": depth, "group": name.endswith("/"), "tag": tag})
    return nodes


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
    modules.append({"no": no, "name": name.strip(), "stage": STAGE.get(no, ""), "docs": docs, "tree": parse_tree(blk)})

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

# ---------- 附錄〈文件關係〉表：shortId → 文件名稱，併入文件庫 ----------
relations, rel_unmatched = [], []
rel = re.search(r"^### 文件關係[^\n]*\n(.*?)(?=^### |^---|\Z)", md, re.M | re.S)
for line in (rel.group(1).splitlines() if rel else []):
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) < 3 or cells[0] in ("階段", "") or cells[0].startswith(":"):
        continue
    docs = []
    for tok, note in re.findall(r"([A-Za-z0-9_-]{9,22})(?:（([^）]*)）)?", cells[2]):
        d = doc_of(tok)
        if d:
            docs.append({**d, "note": note})
        else:
            rel_unmatched.append({"row": cells[1], "ref": tok})
    relations.append({"stage": cells[0], "func": cells[1], "docs": docs})

# ---------- 流程圖：依 journey map〈流程圖索引〉抓文件內 `## 流程圖` 的 mermaid，渲染成 SVG ----------
FLOWS = HERE / "flows"
FLOWS.mkdir(exist_ok=True)
idx = re.search(r"^### 流程圖索引\n(.*?)(?=^#{2,3} |\Z)", md, re.M | re.S)
flow_manifest = []
if idx:
    pp = pathlib.Path(tempfile.gettempdir()) / "mmdc-puppeteer.json"
    pp.write_text(json.dumps({"executablePath": "/opt/pw-browsers/chromium", "args": ["--no-sandbox"]}))
    for line in idx.group(1).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5 or cells[0] in ("階段", ":---") or cells[0].startswith(":"):
            continue
        ids = re.findall(r"`([A-Za-z0-9_-]{9,22})`", cells[3])
        if len(ids) < 2:
            continue
        note_id, short = ids[0], ids[1]
        code = cells[0].split()[0]
        req2 = urllib.request.Request(f"https://api.hackmd.io/v1/teams/1111-jobdocs/notes/{note_id}",
                                      headers={"Authorization": "Bearer " + os.environ["HACKMD_TOKEN"]})
        note = json.load(urllib.request.urlopen(req2, timeout=90))
        body = note["content"]
        i = body.find("## 流程圖")
        sec = body[i:] if i >= 0 else ""
        nxt = re.search(r"\n## ", sec[5:])
        sec = sec[: nxt.start() + 5] if nxt else sec
        svgs = []
        for k, blk in enumerate(re.findall(r"```mermaid\n(.*?)```", sec, re.S), 1):
            stem = f"{code}_{short}_{k}"
            (FLOWS / f"{stem}.mmd").write_text(blk, encoding="utf-8")
            subprocess.run(["npx", "-y", "@mermaid-js/mermaid-cli", "-p", str(pp), "-i", str(FLOWS / f"{stem}.mmd"),
                            "-o", str(FLOWS / f"{stem}.svg"), "-I", f"flow-{stem}".replace("_", "-")], check=True, capture_output=True, timeout=280)
            svgs.append(f"{stem}.svg")
        flow_manifest.append({"stage": code, "noteId": note_id, "shortId": short, "title": " ".join(note["title"].split()), "svgs": svgs})
(FLOWS / "manifest.json").write_text(json.dumps(flow_manifest, ensure_ascii=False, indent=1), encoding="utf-8")
print("flows:", [(f["stage"], f["title"], len(f["svgs"])) for f in flow_manifest])

OUT.write_text(json.dumps({"source": "HackMD [求才系統] Sitemap", "sitemap_shortId": SITEMAP_SHORT,
                           "modules": modules, "shared": shared, "unmatched_refs": unmatched,
                           "relations": relations, "relations_unmatched": rel_unmatched},
                          ensure_ascii=False, indent=1), encoding="utf-8")
print({m["no"] + " " + m["name"]: len(m["docs"]) for m in modules}, "shared:", len(shared), "unmatched:", unmatched, "relations:", len(relations), sum(len(r["docs"]) for r in relations), "rel_unmatched:", rel_unmatched)
