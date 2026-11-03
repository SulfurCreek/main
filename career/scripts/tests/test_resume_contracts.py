"""2026-11-02 履歷工具鏈契約回歸測試（合成資料，只寫暫存目錄，不依賴私人事實）。

Run: python3 -m unittest discover -s career/scripts/tests -p "test_*.py"
"""
import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import gen_line_pack  # noqa: E402
import gen_line_pdf  # noqa: E402
import line_md  # noqa: E402
import verify_line_pdf  # noqa: E402
import verify_line_profile  # noqa: E402
import verify_polish as vp  # noqa: E402

# Entire fixture below is invented for parser/format tests; no real applicant data.
A21 = ("- Analyzed example requirements; 123 of 456 sample requests were recorded.\n"
       "- Planned a sample workflow for a fictional team.\n"
       "- Tuned recommendations from actual selections.\n"
       "- Audited sample fields in an example dataset.\n")
A22 = "- Led an example prototype exercise for a fictional organization.\n"


def directive(block, fields, index=None, action=None):
    d = {"target_block": block, "action": action or ("replace_all" if block == "basic" else "replace_row"), "fields": fields}
    if index is not None:
        d["index"] = index
    return "<!-- @line-directive\n" + json.dumps(d, ensure_ascii=False, indent=2) + "\n-->\n"


def work(i, start, end):
    return {"company": f"Co {i}", "position_title": "Product Manager", "employment_type": "1194", "location": "Taipei City",
            "start_date": start, "end_date": end}


def doc(summary=True, basic_email="applicant@example.invalid", action=None, a21=A21, extra=""):
    basic = {"email": basic_email, "mobile_phone": "000-000-000-000", "current_position_title": "Product Owner",
             "current_employer": "Co 0", "country": "215", "address": "Synthetic Address Placeholder", "city": "Taipei"}
    edu = {"degree_name": "International Business", "type_of_degree": "21", "degree_status": "1172", "university": "Example University",
           "start_date": "2010-09", "end_date": "2014-06"}
    lang = {"language": "10", "written": "1174", "spoken": "1174", "reading": "1174", "listening": "1174"}
    s = "# Resume\n\n"
    if summary:
        s += ("## 0. Professional Summary & Skills\n\n- Product Owner with nearly 10 years of experience.\n"
              "- Requirements: PRD, User Story\n- Languages: English\n\n---\n\n")
    s += "## 1. Basic\n\n" + directive("basic", basic, action=action) + "\n## 2. Work\n\n"
    s += "### 2.1 Product Owner｜Co 0｜2022-08 – Present\n\n" + directive("work_experience", work(0, "2022-08", ""), 0) + "\n" + a21
    s += "\n### 2.2 Product Manager｜Co 1｜2018-01 – 2022-03\n\n" + directive("work_experience", work(1, "2018-01", "2022-03"), 1) + "\n" + A22
    s += "\n## 3. Education\n\n### 3.1 Example\n\n" + directive("education", edu, 0)
    s += "\n## 4. Languages\n\n### 4.1 English\n\n" + directive("languages", lang, 0) + extra
    return s


def run_verify(text, purpose="verify", upstream=None):
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "x.md"
        p.write_text(text, encoding="utf-8")
        up = None
        if upstream is not None:
            up = Path(td) / "up.md"
            up.write_text(upstream, encoding="utf-8")
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc = verify_line_profile.main(str(p), purpose, str(up) if up else None)
        return rc, out.getvalue()


class EnglishFormatTests(unittest.TestCase):
    def test_valid_resume_passes_all_purposes(self):
        for purpose in ("verify", "pack", "pdf"):
            rc, out = run_verify(doc(), purpose)
            self.assertEqual(rc, 0, out)

    def test_profile_format_verify_ok_but_pack_rejected_upfront(self):
        self.assertEqual(run_verify(doc(summary=False))[0], 0)
        rc, out = run_verify(doc(summary=False), "pack")
        self.assertEqual(rc, 1)
        self.assertIn("不支援的格式", out)

    def test_summary_heading_without_number_is_supported(self):
        text = doc().replace("## 0. Professional Summary & Skills", "## Professional Summary & Skills")
        self.assertEqual(run_verify(text, "pack")[0], 0)

    def test_empty_required_field_rejected(self):
        rc, out = run_verify(doc(basic_email=""))
        self.assertEqual(rc, 1)
        self.assertIn("不得留空", out)

    def test_illegal_action_rejected(self):
        rc, out = run_verify(doc(action="delete"))
        self.assertEqual(rc, 1)
        self.assertIn("action", out)

    def test_duplicate_key_rejected(self):
        text = doc().replace('"city": "Taipei"', '"city": "Taipei",\n    "city": "Taipei"', 1)
        rc, out = run_verify(text)
        self.assertEqual(rc, 1)
        self.assertIn("重複鍵", out)

    def test_fixed_fact_anchors_no_longer_gate(self):
        a21 = A21.replace("- Tuned recommendations from actual selections.\n", "<!-- actual selections -->\n- Tuned recommendations.\n")
        rc, out = run_verify(doc(a21=a21))
        self.assertEqual(rc, 0, out)
        self.assertIn("已停用", out)

    def test_upstream_fact_checks_are_retired(self):
        up = doc()
        rc, out = run_verify(up.replace("123 of 456", "999 of 850"), upstream=up)
        self.assertEqual(rc, 0, out)
        self.assertIn("已停用", out)
        self.assertNotIn("已與上游", out)

    def test_facts_always_marked_disabled(self):
        self.assertIn("已停用", run_verify(doc())[1])


class PackAndPdfTests(unittest.TestCase):
    def setUp(self):
        self.td = tempfile.TemporaryDirectory()
        self.dir = Path(self.td.name)
        self.md = self.dir / "r.md"
        self.md.write_text(doc(), encoding="utf-8")

    def tearDown(self):
        self.td.cleanup()

    def pack(self, path=None):
        with contextlib.redirect_stdout(io.StringIO()):
            return gen_line_pack.main([str(path or self.md)])

    def test_pack_and_hash_chain(self):
        self.assertEqual(self.pack(), 0)
        d = json.loads((self.dir / "r.resume.json").read_text(encoding="utf-8"))
        self.assertEqual(gen_line_pdf.check_source(d), [])
        html = gen_line_pdf.render(d)
        self.assertIn(d["payload_sha256"], html)

    def test_tampered_json_and_wrong_source_hash_rejected(self):
        self.pack()
        d = json.loads((self.dir / "r.resume.json").read_text(encoding="utf-8"))
        bad = dict(d, summary=d["summary"] + " Extra.")
        self.assertTrue(any("payload" in e for e in gen_line_pdf.check_source(bad)))
        bad2 = dict(d, source_sha256="0" * 64)
        self.assertTrue(any("source_sha256" in e for e in gen_line_pdf.check_source(bad2)))

    def test_failed_pack_keeps_existing_outputs(self):
        self.pack()
        before = (self.dir / "r.resume.json").read_bytes()
        self.md.write_text(doc(basic_email=""), encoding="utf-8")
        self.assertEqual(self.pack(), 1)
        self.assertEqual((self.dir / "r.resume.json").read_bytes(), before)

    def test_profile_format_pack_fails_before_conversion(self):
        p = self.dir / "p.md"
        p.write_text(doc(summary=False), encoding="utf-8")
        self.assertEqual(self.pack(p), 1)
        self.assertFalse((self.dir / "p.resume.json").exists())

    def reconcile(self, mutate):
        self.pack()
        d = json.loads((self.dir / "r.resume.json").read_text(encoding="utf-8"))
        items = verify_line_pdf.expected_items(d)
        lines = ["Synthetic Applicant"]
        for kind, val in items:
            lines.append(("• " if kind in ("Skill", "Bullet") else "") + val)
        lines = mutate(lines)
        return verify_line_pdf.content_errors("\n".join(lines), d)

    def test_complete_text_reconciles(self):
        self.assertEqual(self.reconcile(lambda x: x), [])

    def test_missing_duplicate_reordered_detected(self):
        self.assertTrue(self.reconcile(lambda x: x[:-3] + x[-2:]))           # 遺失
        self.assertTrue(self.reconcile(lambda x: x + [next(v for v in x if v.startswith('• Planned'))]))  # 列點重複
        def swap(x):
            i = next(k for k, v in enumerate(x) if v.startswith("• Planned"))
            j = next(k for k, v in enumerate(x) if v.startswith("• Tuned"))
            x = list(x); x[i], x[j] = x[j], x[i]
            return x
        self.assertTrue(self.reconcile(swap))  # 換序

    def test_name_plus_ten_placeholder_bullets_not_complete(self):
        self.pack()
        d = json.loads((self.dir / "r.resume.json").read_text(encoding="utf-8"))
        fake = "Synthetic Applicant\n" + "\n".join("• placeholder" for _ in range(10))
        self.assertTrue(verify_line_pdf.content_errors(fake, d))


def zh(text, status="NEEDS_POLISH", attrs=""):
    return f"### 段落\n<!-- [STATUS: {status}]{attrs} -->\n{text}\n"


class RetiredFactPolicyTests(unittest.TestCase):
    def test_numbers_units_and_locks_no_longer_gate(self):
        cases = [
            ("- 完成率 88%。", "- 完成 99 件。", ""),
            ("- 訊息整合目前開發中。", "- 訊息整合已正式上線。", ""),
            ("- 服務約 6 萬家企業，團隊完成 123 件。", "- 服務 8 萬家企業，完成 900 件。", ""),
            ("- 甲產品 10 件，乙產品 20 件。", "- 乙產品 10 件，甲產品 20 件。", " [LOCK_FACTS: 甲產品=10 件; 乙產品=20 件]"),
            ("- 原本名稱。", "- 更換表達。", " [LOCK_ENTITIES: 原本名稱]"),
        ]
        for up, down, attrs in cases:
            self.assertEqual(vp.run_verification(zh(up, attrs=attrs), zh(down, "POLISHED"))[0], [])

    def test_locked_content_no_longer_gates(self):
        self.assertEqual(vp.run_verification(zh("- 原本 10 件。", "LOCKED"), zh("- 重新表達 20 件。", "LOCKED"))[0], [])

    def test_retired_module_exposes_no_validation_api(self):
        import fact_lock
        self.assertTrue(fact_lock.RETIRED)
        self.assertFalse(hasattr(fact_lock, "compare_block"))

    def test_retired_upstream_arg_does_not_read_source(self):
        rc, out = run_verify(doc(), upstream=None)
        self.assertEqual(rc, 0, out)
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as td:
            p = Path(td, "r.md")
            p.write_text(doc(), encoding="utf-8")
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(verify_line_profile.main(str(p), upstream="/missing-source"), 0)

    def test_prepare_validates_once(self):
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as td:
            p = Path(td, "r.md")
            p.write_text(doc(), encoding="utf-8")
            with patch.object(verify_line_profile, "validate_text", wraps=verify_line_profile.validate_text) as check, contextlib.redirect_stdout(io.StringIO()):
                form, resume = gen_line_pack.prepare(p, purpose="pdf")
            self.assertEqual(check.call_count, 1)
            self.assertEqual(form["source_sha256"], resume["source_sha256"])


if __name__ == "__main__":
    unittest.main()
