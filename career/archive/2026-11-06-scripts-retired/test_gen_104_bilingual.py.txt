"""104 雙語組裝器／驗收器 r2 契約：離線合成資料測試（不依賴任何實際履歷檔，不會 skip）。"""
import hashlib
import json
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import gen_104_bilingual as gb  # noqa: E402
import bilingual_contract as bc  # noqa: E402
import line_md  # noqa: E402
import md104  # noqa: E402
import verify_104_bilingual as vb  # noqa: E402

LINE = """# LINE Resume

## 0. Professional Summary & Skills

<!-- [STATUS: LOCKED] -->
- Product Owner with ten years in product. Manage two product planners as direct reports. Use AI agents for specs.
- Requirements: PRD, User Story
- Tools: Axure RP, Figma
- Methods: Kanban

---

## 2. Work Experience

### 2.1 PO

<!-- @line-directive
{"target_block": "work_experience", "action": "replace_row", "index": 0, "fields": {}}
-->
- Bullet zero.
- Bullet one.
- Messaging flow for 199 requests.
- Bullet three.
- Bullet four.
- Mapped permissions for 743 of 840 requests (88%). Hands-on testing and interviews shaped the plan.
- Planned a shared recruitment feature for 55 requests.

### 2.2 PM

<!-- @line-directive
{"target_block": "work_experience", "action": "replace_row", "index": 1, "fields": {}}
-->
- Managed apps.
- Bullet b1.
- Bullet b2.
- Planned KOOL reaching about 16,000 profiles.
- Led Juicy launch, DAU from about 3,200 to 12,500.
"""


def d(obj):
    return "<!-- @104-directive\n" + json.dumps(obj, ensure_ascii=False) + "\n-->"


def zh_doc():
    p = ["# 104 特化版｜v-test｜**可填表**\n\n", d({"target_block": "layout", "action": "update_theme"}), "\n\n## 1. 個人簡介\n\n",
         d({"target_block": "info", "field": "bio", "mode": "plain_text"}), "\n\n```text\n中文簡介。\n```\n\n",
         d({"target_block": "info", "field": "trait", "mode": "plain_text"}), "\n\n```text\n特色一\n```\n\n## 2. 工作經歷\n\n"]
    for i in range(4):
        p += [f"### 2.{i+1} 職稱{i}\n\n", d({"target_block": "experience", "index": i, "tags": ["標籤"]}),
              f"\n\n```html\n<blockquote>中文經歷{i}</blockquote>\n```\n\n"]
    p.append("## 3. 專長\n\n")
    for i in range(6):
        p += [f"### 3.{i+1} 專長{i}\n\n", d({"target_block": "skill", "index": i, "name": f"專長{i}", "tags": ["AI"]}),
              f"\n\n```text\n中文專長說明{i}。\n```\n\n"]
    p += ["## 4. 自傳\n\n", d({"target_block": "bio", "field": "chi", "mode": "quill_html"}), "\n\n```html\n<p>中文自傳</p>\n```\n\n## 5. 專案\n\n"]
    for i in range(4):
        p += [f"### 5.{i+1} 專案{i}\n\n", d({"target_block": "project", "index": i, "name": f"專案{i}", "image": f"images/p{i}.png"}),
              f"\n\n```html\n<blockquote>中文專案{i}</blockquote>\n```\n\n"]
    p += [d({"target_block": "jobCondition", "field": "preferJobContent"}), "\n\n```text\n求職條件\n```\n"]
    return "".join(p)


class Synthetic(unittest.TestCase):
    def setUp(self):
        self.saved = {k: getattr(bc, k) for k in ("LINE_SHA", "SUMMARY_SHA", "SKILL_SRC", "PROJECT_SRC")}
        doc = line_md.parse(LINE)
        w = [x["bullets"] for x in doc["directives"]]
        h = gb.sha16
        s = gb.sentences(doc["summary"])
        bc.LINE_SHA = hashlib.sha256(LINE.encode()).hexdigest()
        bc.SUMMARY_SHA = h(doc["summary"])
        bc.SKILL_SRC = [("summary_sentence", 2, h(s[2])), ("skills_line", 0, h(doc["skills"][0])),
                        ("bullet_sentence", (0, 5, 1), h(gb.sentences(w[0][5])[1])), ("skills_line", 1, h(doc["skills"][1])),
                        ("summary_sentence", 1, h(s[1])), ("skills_line", 2, h(doc["skills"][2]))]
        bc.PROJECT_SRC = {0: [(1, 4, h(w[1][4]))], 1: [(1, 3, h(w[1][3]))], 2: [(0, 5, h(w[0][5])), (0, 2, h(w[0][2]))], 3: [(0, 6, h(w[0][6]))]}
        self.saved_accents = gb.PROJECT_ACCENT
        gb.PROJECT_ACCENT = {1: {"B": ["KOOL"], "G": ["about 16,000 profiles"]}}
        self.zh = zh_doc()
        self.out = gb.build(self.zh, LINE)
        self.lim = {"project": 2000, "bio": 2000, "skill": 2000}

    def tearDown(self):
        for k, v in self.saved.items():
            setattr(bc, k, v)
        gb.PROJECT_ACCENT = self.saved_accents

    def check(self, text, line=LINE, lim=None):
        return vb.verify(text, self.zh, line, bc.LINE_SHA, self.lim if lim is None else lim)

    def sec(self, text, key):
        return next(s for s in md104.parse(text)["sections"] if s["key"] == key)

    def test_roundtrip_and_pass(self):
        self.assertEqual(md104.assemble(md104.parse(self.zh)), self.zh)
        self.assertEqual(self.check(self.out), ([], []))

    def test_experience_chinese_verbatim_no_english(self):
        for i in range(4):
            b = self.sec(self.out, ("experience", i))["body"]
            self.assertEqual(b, f"<blockquote>中文經歷{i}</blockquote>\n")

    def test_bio_english_only_with_cv(self):
        b = self.sec(self.out, ("info", "bio"))["body"]
        self.assertFalse(md104.CJK.search(b))
        self.assertTrue(b.rstrip().endswith(gb.CV_SENTENCE))

    def test_skill_and_project_english_first_chinese_kept(self):
        b = self.sec(self.out, ("skill", 0))["body"]
        self.assertTrue(b.startswith("Use AI agents for specs.\n\n") and b.endswith("中文專長說明0。\n"))
        p = self.sec(self.out, ("project", 2))["body"]
        self.assertLess(p.index("Mapped permissions"), p.index("中文專案2"))
        self.assertIn("<p><br></p>\n<blockquote>中文專案2", p)

    def test_non_whitelisted_changes_fail(self):
        for old, new in (("中文經歷1", "中文經歷X"), ('"images/p0.png"', '"images/px.png"'), ('"tags": ["AI"]', '"tags": ["BI"]'),
                         ("中文自傳", "中文自傳改"), ("特色一", "特色二"), ("求職條件", "求職條件改")):
            errs, _ = self.check(self.out.replace(old, new, 1))
            self.assertTrue(errs, old)

    def test_missing_duplicate_reordered_fields_fail(self):
        s = md104.parse(self.out)["sections"]
        a, b = s[7]["span"], s[8]["span"]
        dropped = self.out[:a[0]] + self.out[a[1]:]
        self.assertTrue(self.check(dropped)[0])
        dup = self.out[:b[1]] + "\n\n" + self.out[a[0]:a[1]] + self.out[b[1]:]
        self.assertTrue(self.check(dup)[0])
        swapped = self.out[:a[0]] + self.out[b[0]:b[1]] + self.out[a[1]:b[0]] + self.out[a[0]:a[1]] + self.out[b[1]:]
        self.assertTrue(self.check(swapped)[0])

    def test_out_of_source_english_fails(self):
        for old, new in (("Use AI agents for specs.", "Use AI agents for all specs."),
                         ("Mapped permissions", "Analyzed permissions"), (gb.CV_SENTENCE, "English CV available.")):
            self.assertTrue(self.check(self.out.replace(old, new, 1))[0], old)

    def test_chinese_added_to_bio_fails(self):
        self.assertTrue(self.check(self.out.replace(gb.CV_SENTENCE, gb.CV_SENTENCE + "\n\n中文", 1))[0])

    def test_line_changed_or_mapping_mismatch_fails(self):
        changed = LINE.replace("Bullet b1.", "Bullet b1 new.")
        self.assertTrue(self.check(self.out, line=changed)[0])
        with self.assertRaises(ValueError):
            gb.build(self.zh, changed)
        bc.LINE_SHA = hashlib.sha256(changed.encode()).hexdigest()
        moved = LINE.replace("- Bullet four.\n", "- Bullet four.\n- Inserted.\n").replace("Bullet b1.", "Bullet b1 new.")
        bc.LINE_SHA = hashlib.sha256(moved.encode()).hexdigest()
        with self.assertRaises(ValueError):  # 插入列點導致索引位移 → 映射原文雜湊不符
            gb.build(self.zh, moved)

    def test_first_sentence_must_be_complete(self):
        import verify_104_bilingual as v
        out = self.out
        sec = self.sec(out, ("skill", 0))
        bad_body = "Used hands-on testing, then shipped.\n\n" + sec["body"].split("\n\n", 1)[1]
        mutated = out[: sec["span"][0]] + md104.render(sec, bad_body) + out[sec["span"][1]:]
        errs, _ = self.check(mutated)
        self.assertTrue(any("英文首句不完整" in e for e in errs), errs)

    def test_verb_highlight_rejected(self):
        i = self.out.index("<blockquote>", self.out.index("### 5.3"))
        bad = self.out[:i] + '<blockquote><strong><span style="background-color: #deebf1;">Analyzed and mapped</span></strong>' + self.out[i + len("<blockquote>"):]
        errs, _ = self.check(bad)
        self.assertTrue(errs)

    def test_limits(self):
        errs, _ = self.check(self.out, lim={"project": 10, "bio": 2000, "skill": 2000})
        self.assertTrue(any("字數超標" in e for e in errs))
        errs, pending = self.check(self.out, lim={"project": 2000})
        self.assertEqual(errs, [])
        self.assertEqual(pending, ["bio", "skill"])
        self.assertEqual(vb.parse_limits([]), {"project": 2000, "skill": 1000, "bio": 1000})  # 三類上限皆已知

    def test_pending_limits_do_not_replace_output(self):
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as td:
            zp, lp, op = (pathlib.Path(td, n) for n in ("zh.md", "line.md", "out.md"))
            zp.write_text(self.zh, encoding="utf-8")
            lp.write_text(LINE, encoding="utf-8")
            op.write_text("previous approved output", encoding="utf-8")
            with patch.object(vb, "parse_limits", return_value={"project": 2000}):
                self.assertEqual(gb.main(["--zh", str(zp), "--line", str(lp), "--out", str(op)]), 3)
            self.assertEqual(op.read_text(encoding="utf-8"), "previous approved output")

    def test_validator_does_not_use_generator_to_build_expectations(self):
        from unittest.mock import patch
        with patch.object(gb, "english_units", return_value=("Wrong summary.", [], {})):
            self.assertEqual(self.check(self.out), ([], []))

    def test_main_writes_nothing_on_failure(self):
        with tempfile.TemporaryDirectory() as t:
            zp, lp, op = pathlib.Path(t, "zh.md"), pathlib.Path(t, "line.md"), pathlib.Path(t, "out.md")
            zp.write_text(self.zh, encoding="utf-8")
            lp.write_text(LINE.replace("Bullet b1.", "x"), encoding="utf-8")
            self.assertEqual(gb.main(["--zh", str(zp), "--out", str(op), "--line", str(lp)]), 1)
            self.assertFalse(op.exists())
            lp.write_text(LINE, encoding="utf-8")
            self.assertEqual(gb.main(["--zh", str(zp), "--out", str(op), "--line", str(lp)]), 0)  # 三類上限皆已知，預設即可填表
            self.assertTrue(op.exists())
            self.assertEqual(gb.main(["--zh", str(zp), "--out", str(op), "--line", str(lp), "--limit", "bio=2000", "--limit", "skill=2000"]), 0)


if __name__ == "__main__":
    unittest.main()
