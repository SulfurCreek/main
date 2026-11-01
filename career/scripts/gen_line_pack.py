#!/usr/bin/env python3
"""（2026-11-01 本人裁定）LINE profile 表單只填 Summary；列點只屬於 resume（PDF）。
產出兩個檔：<stem>.fill.json（表單：欄位＋summary_text，無列點）與 <stem>.resume.json（PDF 用：含列點與 Skills）。
原說明：由 drafts/line/line-profile.md 產生 Antigravity 填表用的 line-profile.fill.json（內文只取自定稿，填表端不得硬編碼）。
先跑 verify_line_profile.py 0 違規才產出。用法：python3 career/scripts/gen_line_pack.py [md路徑]"""
import hashlib, json, re, subprocess, sys
from pathlib import Path

src = Path(sys.argv[1] if len(sys.argv) > 1 else "career/drafts/line/line-profile.md")
if subprocess.run([sys.executable, "career/scripts/verify_line_profile.py", str(src)]).returncode:
    sys.exit("驗收未通過，不產出")
text = src.read_text(encoding="utf-8")
D = re.compile(r"<!-- @line-directive\s*(\{.*?\})\s*-->", re.S)
sec0 = text[text.index("## 0."):text.index("## 1.")]
sec0_lines = [l[2:].strip() for l in sec0.splitlines() if l.startswith("- ")]
summary, skills = sec0_lines[0], sec0_lines[1:]
steps, pos = [], 0
ms = list(D.finditer(text))
for i, m in enumerate(ms):
    d = json.loads(m.group(1))
    end = ms[i + 1].start() if i + 1 < len(ms) else len(text)
    chunk = text[m.end():end]
    bullets = [l[2:].strip() for l in chunk.splitlines() if l.startswith("- ")]
    st = {"step": i + 1, "target_block": d["target_block"], "action": d["action"],
          "index": d.get("index"), "fields": d["fields"]}
    if bullets:
        st["description_bullets"] = bullets
        st["description_text"] = "\n".join("• " + b for b in bullets)
    steps.append(st)
sha = hashlib.sha256(text.encode()).hexdigest()
resume = {"source": str(src), "source_sha256": sha, "summary": summary, "skills": skills, "steps": steps}
form_steps = [{k: v for k, v in s.items() if k not in ("description_bullets", "description_text")} for s in steps]
form = {"source": str(src), "source_sha256": sha, "summary_text": summary, "steps": form_steps}
dst = src.with_name(src.stem + ".fill.json")
dst.write_text(json.dumps(form, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
src.with_name(src.stem + ".resume.json").write_text(json.dumps(resume, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"✅ {dst}：{len(form_steps)} 步＋summary_text，sha256 {sha[:12]}")
