#!/usr/bin/env python3
"""104 特化版 md 的共用解析契約（2026-11-03）。

文件 = 原文片段 + directive 區塊；directive 區塊為
    <!-- @104-directive\\n{json}\\n-->[\\n\\n```lang\\n<body>```]
body 可有可無（例如 layout）。parse() 後以 assemble() 重組必須與原文逐位元組相同。
"""
import html
import json
import re

DIRECTIVE = re.compile(r"<!-- @104-directive\n(?P<json>\{.*?\})\n-->(?:\n\n```(?P<lang>\w+)\n(?P<body>.*?)```)?", re.S)
CJK = re.compile(r"[一-鿿]")


def parse(text):
    secs, pieces, pos = [], [], 0
    for m in DIRECTIVE.finditer(text):
        pieces.append(text[pos:m.start()])
        d = json.loads(m.group("json"))
        secs.append({"d": d, "raw": m.group("json"), "lang": m.group("lang"), "body": m.group("body"),
                     "key": key(d), "span": (m.start(), m.end())})
        pieces.append(None)
        pos = m.end()
    pieces.append(text[pos:])
    return {"pieces": pieces, "sections": secs}


def key(d):
    b = d.get("target_block")
    return (b, d["field"]) if "field" in d else (b, d.get("index"))


def render(sec, body=None):
    body = sec["body"] if body is None else body
    out = f"<!-- @104-directive\n{sec['raw']}\n-->"
    if sec["lang"] is not None:
        out += f"\n\n```{sec['lang']}\n{body}```"
    return out


def assemble(doc, bodies=None):
    """bodies：{section index: 新 body}；未指定者沿用原 body。"""
    bodies = bodies or {}
    out, i = [], 0
    for p in doc["pieces"]:
        if p is None:
            out.append(render(doc["sections"][i], bodies.get(i)))
            i += 1
        else:
            out.append(p)
    return "".join(out)


def visible_len(body):
    """可見字元數（兩種口徑取大者）：去標籤、entity 解碼；區塊結尾與 <br> 計 1 個換行／不計換行。"""
    t = re.sub(r"<br\s*/?>|</(?:p|li|blockquote|h\d)>", "\n", body)
    t = html.unescape(re.sub(r"<[^>]*>", "", t))
    t = re.sub(r"\n{2,}", "\n", t).strip("\n")
    return max(len(t), len(t.replace("\n", "")))
