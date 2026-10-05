"""parts/*（分區塊的 CSS／HTML／JS）＋ report_data.json → ../recruiter_journey_report.html（自包含、離線可開）。

先讀 ROUTES.md 找要改哪個 parts 檔。組裝順序＝下方 MANIFEST，與舊版單檔模板逐位元組相同。
parts 檔開頭的 AI-NOTE 註解只給維護者看，建置時剝除，不進成品。
模板不含 <html>/<head>/<body>（可直接發布成 artifact）；repo 成品另加外框與 UTF-8 charset。
加 --fragment <路徑> 可另外輸出不含外框的版本（給 artifact 用）。
"""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).parent
PARTS = HERE / "parts"

# 順序即輸出順序（CSS 的層疊與 JS 的函式宣告順序都依賴它，改順序要重新跑 tests）
CSS = ["core", "hero", "route", "tabs", "sections", "persona", "grid", "sitemap", "flows", "appendix", "responsive"]
HTML = ["shell_top", "hero", "tabs", "persona", "route", "grid", "sitemap", "flows", "appendix", "shell_bottom"]
JS = ["core", "hero", "data", "route", "persona", "grid", "apply", "flows", "sitemap", "appendix", "tabs"]

NOTE = re.compile(r"(?:<!--AI-NOTE.*?-->|/\*AI-NOTE.*?\*/)\n", re.S)


def part(name, ext):
    return NOTE.sub("", (PARTS / f"{name}.{ext}").read_text(encoding="utf-8"))


def template():
    return (part("head", "html") + "<style>\n" + "".join(part(n, "css") for n in CSS) + "</style>\n" +
            "".join(part(n, "html") for n in HTML) + "<script>\n" + "".join(part(n, "js") for n in JS) + part("tail", "html"))


if __name__ == "__main__":
    data = json.loads((HERE / "report_data.json").read_text(encoding="utf-8"))
    body = template().replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
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
