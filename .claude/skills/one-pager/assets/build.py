#!/usr/bin/env python3
"""把 one-pager 內容 JSON 注入 template.html，輸出可渲染的 HTML（中間鷹架）。
用法：python3 build.py <content.json> [out.html]
最終交付是 PNG，本檔只產生給 render_png.js 截圖用的 HTML。
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
TEMPLATE = HERE / "template.html"

content_path = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "example_decision_matrix.json"
out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else content_path.with_suffix(".html")

data = json.loads(content_path.read_text(encoding="utf-8"))
html = TEMPLATE.read_text(encoding="utf-8").replace("__DATA__", json.dumps(data, ensure_ascii=False))
out_path.write_text(html, encoding="utf-8")
print(f"wrote {out_path}")
