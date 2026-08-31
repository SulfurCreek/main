#!/usr/bin/env python3
"""把 report_data.json 注入 report_template.html，輸出最終自包含 HTML。
改樣式改 template，改分析邏輯改 ../scripts/analyze_duty_recommendation_accuracy.py（重跑後也要重跑本檔）。
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
DATA_PATH = HERE / "report_data.json"
TEMPLATE_PATH = HERE / "report_template.html"
OUT_PATH = HERE.parent / "analysis_推薦精準度_報告.html"

data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
template = TEMPLATE_PATH.read_text(encoding="utf-8")
html = template.replace("__DATA__", json.dumps(data, ensure_ascii=False))
OUT_PATH.write_text(html, encoding="utf-8")
print(f"wrote {OUT_PATH} ({len(html):,} bytes)")
