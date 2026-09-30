"""report_template.html + report_data.json → 未來 user-journey 報告 HTML（自包含）。"""
import json, pathlib
HERE = pathlib.Path(__file__).parent
data = json.loads((HERE / "report_data.json").read_text(encoding="utf-8"))
tpl = (HERE / "report_template.html").read_text(encoding="utf-8")
blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
out = HERE.parent / "recruiter_journey_report.html"
out.write_text(tpl.replace("__DATA__", blob), encoding="utf-8")
print("wrote", out, out.stat().st_size, "bytes")
