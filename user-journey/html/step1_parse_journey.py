"""解析 ../recruiter_journey_map.md → report_data.json（只搬運，不改寫、不補齊、不自編編號）。

各階段泳道（目標／行動／…）依文件助手指示改按「各頁面 sub user flow」繪製，
待補 md，故本腳本不解析、HTML 不呈現泳道內容。
"""
import re, json, pathlib

HERE = pathlib.Path(__file__).parent
SRC = HERE.parent / "recruiter_journey_map.md"
OUT = HERE / "report_data.json"
text = SRC.read_text(encoding="utf-8")


def section(prefix):
    m = re.search(rf"^## {re.escape(prefix)}[^\n]*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not m:
        raise SystemExit(f"找不到章節：{prefix}")
    return m.group(1)


def heading(prefix):
    return re.search(rf"^## ({re.escape(prefix)}[^\n]*)$", text, re.M).group(1).strip()


def table_rows(block):
    rows = []
    for ln in block.splitlines():
        ln = ln.strip()
        if not ln.startswith("|") or re.match(r"^\|\s*:?-{2,}", ln):
            continue
        rows.append([c.strip() for c in re.split(r"(?<!\\)\|", ln.strip("|"))])
    return rows


head = text.split("\n---", 1)[0]
title = re.search(r"^# (.+)$", head, re.M).group(1)
head_bullets = [l[2:] for l in head.splitlines() if l.startswith("- ")]

persona = [r for r in table_rows(section("Persona")) if r[0] != "項目"]
route = table_rows(section("路由"))
route_head, route_rows = route[0], route[1:]

ov = section("總覽")
mer = re.search(r"```mermaid\n(.*?)```", ov, re.S).group(1)
journey_title = re.search(r"title (.+)", mer).group(1).strip()
sections_, cur = [], None
for ln in mer.splitlines():
    m = re.match(r"\s+section (.+)", ln)
    if m:
        cur = {"name": m.group(1).strip(), "tasks": []}; sections_.append(cur); continue
    m = re.match(r"\s+(.+?): (\d+): (.+)", ln)
    if m and cur is not None:
        cur["tasks"].append({"name": m.group(1).strip(), "score": int(m.group(2)), "actor": m.group(3).strip()})
score_note = re.search(r"^> (.+)$", ov, re.M).group(1)

stage_names = re.findall(r"^### (.+)$", section("各階段"), re.M)

doc_block = section("文件關係")
docmap = [{"stage": r[0], "func": r[1], "docs": [d.strip() for d in r[2].split("、") if d.strip()]}
          for r in table_rows(doc_block) if r[0] != "階段"]
shared = re.search(r"\*\*跨階段共用元件\*\*[^：]*：(.+)", doc_block).group(1).strip().rstrip("。")
gaps = [l[2:] for l in section("缺口").splitlines() if l.startswith("- ")]

data = {"title": title, "head_bullets": head_bullets,
        "headings": {k: heading(k) for k in ["Persona", "路由", "總覽", "各階段", "文件關係", "缺口"]},
        "persona": persona, "route": {"head": route_head, "rows": route_rows},
        "journey": {"title": journey_title, "sections": sections_, "note": score_note},
        "stage_names": stage_names, "docmap": docmap, "shared": shared, "gaps": gaps}
OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"sections={len(sections_)} tasks={sum(len(s['tasks']) for s in sections_)} stages={len(stage_names)} route={len(route_rows)} docmap={len(docmap)} gaps={len(gaps)}")
print("stage_names:", stage_names)
