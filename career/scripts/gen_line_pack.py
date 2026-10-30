#!/usr/bin/env python3
"""由 drafts/line/line-profile.md 產生 Antigravity 填表用的 line-profile.fill.json（內文只取自定稿，填表端不得硬編碼）。
先跑 verify_line_profile.py 0 違規才產出。用法：python3 career/scripts/gen_line_pack.py [md路徑]"""
import hashlib, json, re, subprocess, sys
from pathlib import Path

src = Path(sys.argv[1] if len(sys.argv) > 1 else "career/drafts/line/line-profile.md")
if subprocess.run([sys.executable, "career/scripts/verify_line_profile.py", str(src)]).returncode:
    sys.exit("驗收未通過，不產出")
text = src.read_text(encoding="utf-8")
D = re.compile(r"<!-- @line-directive\s*(\{.*?\})\s*-->", re.S)
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
out = {"source": str(src), "source_sha256": hashlib.sha256(text.encode()).hexdigest(), "steps": steps}
dst = src.with_name("line-profile.fill.json")
dst.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"✅ {dst}：{len(steps)} 步，sha256 {out['source_sha256'][:12]}")
