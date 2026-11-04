#!/usr/bin/env python3
"""Markdown → <stem>.fill.json（表單：欄位＋summary_text，無列點）＋ <stem>.resume.json（PDF：列點、Skills、Languages）。

2026-11-02 契約：
- 解析與格式判定共用 line_md.py；只接受 resume 格式（含 Professional Summary）。profile 格式在前置驗證即拒絕。
- 先跑 verify_line_profile（--for pack），未通過不產出。
- 兩個 JSON 都帶 source_sha256（md 原文）與 payload_sha256（正文內容的標準化雜湊），下游 renderer 會重算比對。
- 原子寫入：先寫暫存檔，兩檔都成功才替換；失敗時既有成品不動。
用法：python3 career/scripts/gen_line_pack.py <md>
"""
import hashlib
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import line_md  # noqa: E402
import verify_line_profile  # noqa: E402


def canonical(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def payload_hash(data):
    keys = ("summary", "skills", "personal_statement", "steps")
    return hashlib.sha256(canonical({k: data.get(k) for k in keys}).encode()).hexdigest()


def build(src):
    text = Path(src).read_text(encoding="utf-8")
    doc = line_md.parse(text)
    errs = line_md.validate(doc, "pack")
    if errs:
        raise ValueError("；".join(errs))
    steps = line_md.payload(doc)
    sha = hashlib.sha256(text.encode()).hexdigest()
    resume = {"source": str(src), "source_sha256": sha, "summary": doc["summary"], "skills": doc["skills"],
              "personal_statement": doc["statement"], "steps": steps}
    resume["payload_sha256"] = payload_hash(resume)
    form_steps = [{k: v for k, v in s.items() if k not in ("description_bullets", "description_text")} for s in steps]
    form = {"source": str(src), "source_sha256": sha, "summary_text": doc["summary"], "steps": form_steps}
    return form, resume


def atomic_write(pairs):
    tmps = []
    try:
        for path, data in pairs:
            tmp = Path(str(path) + ".tmp")
            tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            tmps.append((tmp, path))
        for tmp, path in tmps:
            os.replace(tmp, path)
    finally:
        for tmp, _ in tmps:
            if tmp.exists():
                tmp.unlink()


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 1:
        print(__doc__)
        return 2
    src = Path(argv[0])
    if verify_line_profile.main(str(src), "pack"):
        print("❌ 驗收未通過，不產出（既有成品不動）")
        return 1
    try:
        form, resume = build(src)
    except (OSError, ValueError) as e:
        print(f"❌ 無法產出：{e}")
        return 1
    fill, rj = src.with_name(src.stem + ".fill.json"), src.with_name(src.stem + ".resume.json")
    atomic_write([(fill, form), (rj, resume)])
    print(f"✅ {fill}、{rj}：{len(form['steps'])} 步，source {resume['source_sha256'][:12]}，payload {resume['payload_sha256'][:12]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
