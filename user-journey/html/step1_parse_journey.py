"""解析 ../recruiter_journey_map.md → report_data.json（只搬運、不改寫、不補齊）。"""
import re, json, pathlib

HERE = pathlib.Path(__file__).parent
SRC = HERE.parent / "recruiter_journey_map.md"
OUT = HERE / "report_data.json"
text = SRC.read_text(encoding="utf-8")


def section(title_prefix, level="## "):
    m = re.search(rf"^{re.escape(level)}{re.escape(title_prefix)}.*?$(.*?)(?=^{re.escape(level)}\S|\Z)", text, re.M | re.S)
    return m.group(1) if m else ""


def table_rows(block):
    rows = []
    for ln in block.splitlines():
        ln = ln.strip()
        if not ln.startswith("|") or re.match(r"^\|\s*:?-{2,}", ln):
            continue
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", ln.strip("|"))]
        rows.append(cells)
    return rows


# --- 頭部說明 ---
head = text.split("\n---", 1)[0]
title = re.search(r"^# (.+)$", head, re.M).group(1)
head_bullets = [re.sub(r"^- ", "", l) for l in head.splitlines() if l.startswith("- ")]

# --- 1. Persona ---
persona = [r for r in table_rows(section("1. Persona")) if r[0] != "項目"]

# --- 2. 總覽 journey ---
ov = section("2. 總覽")
mer = re.search(r"```mermaid\n(.*?)```", ov, re.S).group(1)
journey_title = re.search(r"title (.+)", mer).group(1).strip()
sections_, cur = [], None
for ln in mer.splitlines():
    m = re.match(r"\s+section (.+)", ln)
    if m:
        cur = {"name": m.group(1).strip(), "tasks": []}
        sections_.append(cur)
        continue
    m = re.match(r"\s+(.+?): (\d+): (.+)", ln)
    if m and cur is not None:
        cur["tasks"].append({"name": m.group(1).strip(), "score": int(m.group(2)), "actor": m.group(3).strip()})
score_note = re.search(r"^> (.+)$", ov, re.M).group(1)

# --- 3. 各階段 ---
stages = []
s3 = section("3. 各階段")
for m in re.finditer(r"^### (3\.\d) (.+?)$(.*?)(?=^### |\Z)", s3, re.M | re.S):
    num, name, body = m.groups()
    lanes = []
    for r in table_rows(body):
        if r[0] == "泳道":
            continue
        lanes.append({"lane": r[0], "content": r[1], "source": r[2] if len(r) > 2 else ""})
    stages.append({"num": num, "name": name.strip(), "lanes": lanes})

# --- 4. 文件關係 ---
docmap = [{"stage": r[0], "func": r[1], "docs": [d.strip() for d in re.split(r"、", r[2]) if d.strip()]}
          for r in table_rows(section("4. 文件關係")) if r[0] != "階段"]
shared = re.search(r"\*\*跨階段共用元件\*\*[^：]*：(.+)", section("4. 文件關係")).group(1).strip().rstrip("。")

# --- 5. 缺口 ---
gaps = [l[2:] for l in section("5. 缺口").splitlines() if l.startswith("- ")]

checks = []

data = {"title": title, "head_bullets": head_bullets, "persona": persona,
        "journey": {"title": journey_title, "sections": sections_, "note": score_note},
        "stages": stages, "docmap": docmap, "shared": shared, "gaps": gaps, "checks": checks}
ids3_l = {}
for m in re.finditer(r"\[([^\]]+)\]\(https://hackmd\.io/@1111-jobdocs/([A-Za-z0-9_-]+)\)", s3):
    ids3_l.setdefault(m.group(2), m.group(1))
ids4_all = set(d.split("（")[0] for x in docmap for d in x["docs"]) | set(re.findall(r"[A-Za-z0-9_-]{9,10}", shared))
missing = [(i, ids3_l[i]) for i in ids3_l if i not in ids4_all]
if missing:
    checks.append("§3 各階段內文引用、但 §4 文件關係表（含跨階段共用元件）沒列出的文件共 %d 份：" % len(missing)
                  + "、".join("[%s](https://hackmd.io/@1111-jobdocs/%s)" % (t, i) for i, t in missing) + "——請文件 session 確認是否補進 §4。")
OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")

# --- 自檢（只回報，不修正素材）---
ids3 = set(re.findall(r"hackmd\.io/@1111-jobdocs/([A-Za-z0-9_-]+)", s3))
ids4 = set(d.split("（")[0] for x in docmap for d in x["docs"])
ids4 |= set(re.findall(r"[A-Za-z0-9_-]{9,10}", shared))
print(f"stages={len(stages)} lanes={sum(len(s['lanes']) for s in stages)} docmap_rows={len(docmap)}")
print("§3 有連結但 §4 沒列:", sorted(ids3 - ids4))
print("§4 有列但 §3 沒連結:", sorted(ids4 - ids3))
print("journey tasks:", sum(len(s['tasks']) for s in sections_), "sections:", len(sections_))
