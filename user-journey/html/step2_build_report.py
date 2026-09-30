"""report_template.html + report_data.json → ../recruiter_journey_report.html（自包含、離線可開）。

模板本身不含 <html>/<head>/<body>（可直接發布成 artifact，平台會補外框）；
repo 成品另加外框與 UTF-8 charset，讓 GitHub Pages／本機開啟不亂碼。
加 --fragment <路徑> 可另外輸出不含外框的版本（給 artifact 用）。
"""
import json, pathlib, sys
HERE = pathlib.Path(__file__).parent
data = json.loads((HERE / "report_data.json").read_text(encoding="utf-8"))
tpl = (HERE / "report_template.html").read_text(encoding="utf-8")
body = tpl.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
full = ('<!DOCTYPE html>\n<html lang="zh-Hant">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n</head>\n<body>\n'
        + body + '\n</body>\n</html>\n')
out = HERE.parent / "recruiter_journey_report.html"
out.write_text(full, encoding="utf-8")
print("wrote", out, out.stat().st_size, "bytes")
if "--fragment" in sys.argv:
    frag = pathlib.Path(sys.argv[sys.argv.index("--fragment") + 1])
    frag.write_text(body, encoding="utf-8")
    print("wrote", frag, frag.stat().st_size, "bytes")
