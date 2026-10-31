"""Regression tests for acceptance boundaries; no private career facts required.

Run: python3 -m unittest discover -s career/scripts/tests -v
"""
import contextlib
import io
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import gen_104_md as gen
import verify_polish as vp


def block(text, status="LOCKED"):
    return f"<!-- [STATUS: {status}] -->\n{text}\n"


def resume():
    parts = ["### 個人簡介\n" + block("產品規劃與交付。"),
             "### 個人特色\n" + block("重視使用者\n重視合作\n重視品質\n重視資料\n重視交付"),
             "### 工作經歷\n"]
    for i in range(4):
        parts.append(f"#### 公司{i}｜2020/01–2021/01\n" + block(f"- 職責{i}。"))
        if i < 3:
            parts.append(block(f"- 案例{i}。"))
    parts.append("### 專長\n")
    for i in range(6):
        parts.append(block(f"技能{i}：能力說明{i}。"))
    parts.append("### 自傳\n" + block("第一段。\n第二段。"))
    parts.append("### 專案成就\n")
    for i in range(4):
        parts.append(f"#### 專案{i}｜2020/01\n" + block(f"專案摘要{i}。\n專案細節{i}。"))
    parts.append("### 求職條件（工作內容）\n" + block("期待產品規劃工作。"))
    return "\n".join(parts)


class PolishTests(unittest.TestCase):
    def reject(self, draft, final, needle):
        errors, _ = vp.run_verification(draft, final)
        self.assertTrue(any(needle in e for e in errors), errors)

    def test_valid_locked(self):
        self.assertEqual(vp.run_verification("### 段落\n" + block("原文"), "### 段落\n" + block("原文"))[0], [])

    def test_empty(self):
        self.reject("", "", "空輸入")

    def test_zero_blocks(self):
        self.reject("### 段落\n原文", "### 段落\n原文", "零區塊")

    def test_empty_block(self):
        self.reject(block(""), block(""), "空區塊")

    def test_illegal_status(self):
        self.reject(block("原文"), block("原文", "UNKNOWN"), "非法狀態")

    def test_malformed_status(self):
        self.reject(block("原文"), block("原文").replace("STATUS:", "STATUS :"), "非法狀態")

    def test_locked_state_cannot_be_relabelled(self):
        self.reject(block("原文"), block("原文", "POLISHED"), "狀態轉換")

    def test_unmarked_addition(self):
        self.reject("### 段落\n" + block("原文"), "### 段落\n營收 999 億。\n" + block("原文"), "未標記正文")

    def test_heading_change(self):
        self.reject("### 公司A\n" + block("原文"), "### 公司B\n" + block("原文"), "章節異動")

    def test_heading_order(self):
        self.reject("### A\n" + block("甲") + "### B\n" + block("乙"), "### B\n" + block("乙") + "### A\n" + block("甲"), "章節異動")

    def test_locked_indent(self):
        self.reject(block("    - 原文"), block("- 原文"), "越權修改")

    def test_locked_whitespace(self):
        self.reject(block("原文"), block("原文 "), "越權修改")

    def test_locked_internal_blank_line(self):
        self.reject(block("第一行\n\n第二行"), block("第一行\n第二行"), "越權修改")

    def test_final_cannot_hide_text_in_draft_wrapper(self):
        self.reject(block("原文"), "不應忽略的正文\n## 草稿\n" + block("原文"), "成品結構")

    def test_flatten_child(self):
        draft = block("- 父項", "NEEDS_POLISH") + block("  - 子項", "NEEDS_POLISH")
        final = block("- 上層", "POLISHED") + block("- 下層", "POLISHED")
        self.reject(draft, final, "父子結構")

    def test_reparent_child(self):
        draft = block("- 父項\n  - 子項\n    - 孫項", "NEEDS_POLISH")
        final = block("- 上層\n  - 下層\n  - 同層", "POLISHED")
        self.reject(draft, final, "父子結構")

    def test_equivalent_child_indent(self):
        a = block("- 父項", "NEEDS_POLISH") + block("  - 子項", "NEEDS_POLISH")
        b = block("- 上層", "POLISHED") + block("    - 下層", "POLISHED")
        self.assertEqual(vp.run_verification(a, b)[0], [])

    def test_unlocked_numeric_change(self):
        self.reject(block("- 完成 10 件。", "NEEDS_POLISH"), block("- 已完成 90 件。", "POLISHED"), "數字異動")

    def test_numeric_occurrences(self):
        self.reject(block("- 完成 10 件。", "NEEDS_POLISH"), block("- 已完成 10 件、另完成 10 件。", "POLISHED"), "數字異動")

    def test_concurrent_word_frequency_rule_is_preserved(self):
        self.assertEqual(vp.WORD_FREQ_CAPS["推進"][0], 8)
        self.reject(block("推進" * 9), block("推進" * 9), "推進")

    def test_draft_preamble_excluded(self):
        final = "### 段落\n" + block("原文")
        draft = "# 草稿說明\n不交付\n## 草稿\n" + final + "## 檢查\n附錄"
        self.assertEqual(vp.run_verification(draft, final)[0], [])

    def test_remote_failure_does_not_use_local(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "old.md"
            p.write_text("舊稿")
            with patch.object(vp.subprocess, "run", return_value=subprocess.CompletedProcess([], 1, "", "missing")):
                with self.assertRaises(ValueError):
                    vp.load_file_content(str(p), "origin/missing")

    def test_explicit_local_missing_does_not_use_remote(self):
        with patch.object(vp, "read_from_git") as remote:
            with self.assertRaises(OSError):
                vp.load_file_content("/missing-resume-file", "origin/branch", prefer_local=True)
            remote.assert_not_called()


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.src = self.root / "final.md"
        self.draft = self.root / "draft.md"
        self.out = self.root / "104.md"
        self.src.write_text(resume())
        self.draft.write_text(resume())
        self.generate()
        self.good = self.out.read_text()

    def generate(self, extra=()):
        argv = ["gen_104_md.py", str(self.src), str(self.out), "test", "fixture", "--draft", str(self.draft)]
        argv += list(extra)
        with patch.object(sys, "argv", argv), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return gen.main()

    def check(self, text):
        self.out.write_text(text)
        return vp.verify_104_markdown(str(self.out), self.src.read_text())

    def mutate_directive(self, target, mutation):
        def change(match):
            value = json.loads(match.group(1))
            if target(value):
                mutation(value)
            return "<!-- @104-directive\n" + json.dumps(value, ensure_ascii=False) + "\n-->"
        return re.sub(r"<!-- @104-directive\n(.*?)\n-->", change, self.good, flags=re.S)

    def test_valid_generated(self):
        self.assertEqual(self.check(self.good), [])
        self.assertIn("可填表", self.good)

    def test_extra_fabricated_result(self):
        self.assertTrue(self.check(self.good.replace("產品規劃與交付。", "產品規劃與交付。\n虛構營收 999 億。", 1)))

    def test_duplicate_sentence(self):
        self.assertTrue(self.check(self.good.replace("第一段。", "第一段。第一段。", 1)))

    def test_reordered_biography(self):
        self.assertTrue(self.check(self.good.replace("<p>第一段。</p>\n<p><br></p>\n<p>第二段。</p>", "<p>第二段。</p>\n<p><br></p>\n<p>第一段。</p>")))

    def test_move_sentence_to_another_field(self):
        changed = self.good.replace("產品規劃與交付。", "", 1).replace("期待產品規劃工作。", "期待產品規劃工作。\n產品規劃與交付。", 1)
        self.assertTrue(self.check(changed))

    def test_wrong_skill_name(self):
        self.assertTrue(self.check(self.mutate_directive(lambda d: d.get("target_block") == "skill", lambda d: d.update(name="虛構技能"))))

    def test_wrong_project_name(self):
        self.assertTrue(self.check(self.mutate_directive(lambda d: d.get("target_block") == "project", lambda d: d.update(name="虛構專案"))))

    def test_wrong_company_heading(self):
        self.assertTrue(self.check(self.good.replace("### 2.1 公司0", "### 2.1 虛構公司", 1)))

    def test_unsupported_tag(self):
        self.assertTrue(self.check(self.mutate_directive(lambda d: d.get("target_block") == "skill", lambda d: d.update(tags=["不存在的標籤"])) ))

    def test_known_but_wrong_field_tag(self):
        self.assertTrue(self.check(self.mutate_directive(lambda d: d.get("target_block") == "skill" and d["index"] == 0, lambda d: d.update(tags=vp.ST[1]))))

    def test_wrong_index(self):
        self.assertTrue(self.check(self.mutate_directive(lambda d: d.get("target_block") == "skill", lambda d: d.update(index=99))))

    def test_boolean_index(self):
        self.assertTrue(self.check(self.mutate_directive(lambda d: d.get("target_block") == "skill" and d["index"] == 0, lambda d: d.update(index=False))))

    def test_duplicate_directive(self):
        match = re.search(r"<!-- @104-directive\n.*?\n-->", self.good, re.S)
        self.assertTrue(self.check(self.good + match.group(0)))

    def test_duplicate_json_key(self):
        self.assertTrue(self.check(self.good.replace('"target_block": "layout"', '"target_block": "skill", "target_block": "layout"', 1)))

    def test_extra_code_block(self):
        self.assertTrue(self.check(self.good + "\n```text\n虛構內容\n```\n"))

    def test_unsupported_html(self):
        self.assertTrue(self.check(self.good.replace("<p>第一段。</p>", "<script>第一段。</script>")))

    def test_inline_space_preserved(self):
        parser = vp.FieldHTML();parser.feed("<p><strong>A</strong> <span>B</span></p>")
        self.assertEqual(parser.chunks, ["A B"])

    def test_scrum_requires_card_evidence(self):
        self.assertNotIn("Scrum", vp.skill_tags(4, "以甘特圖與 Trello 管理時程"))
        self.assertIn("Scrum", vp.skill_tags(4, "2022–2023 跑過完整 Scrum"))

    def test_uml_is_retained(self):
        self.assertIn("UML", vp.skill_tags(2, "以循序圖說明系統互動"))

    def test_failed_source_keeps_previous_output(self):
        self.src.write_text(self.src.read_text().replace("產品規劃與交付。", "已被竄改。"))
        with self.assertRaises(ValueError):
            self.generate()
        self.assertEqual(self.out.read_text(), self.good)

    def test_failed_source_creates_no_output(self):
        self.out.unlink()
        self.src.write_text("")
        with self.assertRaises(ValueError):
            self.generate()
        self.assertFalse(self.out.exists())

    def test_failed_output_validation_is_not_published(self):
        self.out.unlink()
        with patch.object(vp, "verify_104_markdown", return_value=["forced regression failure"]):
            with self.assertRaises(ValueError):
                self.generate()
        self.assertFalse(self.out.exists())
        self.assertEqual(list(self.root.glob(".104-*.md")), [])

    def test_failed_output_keeps_previous_good_file(self):
        with patch.object(vp, "verify_104_markdown", return_value=["forced regression failure"]):
            with self.assertRaises(ValueError):
                self.generate()
        self.assertEqual(self.out.read_text(), self.good)

    def test_source_cannot_be_overwritten(self):
        self.out = self.src
        with self.assertRaises(ValueError):
            self.generate()

    def public_fixture(self):
        source = resume().replace("#### 公司0｜", "#### PM｜1111 全球華人｜")
        source = source.replace("#### 公司1｜", block("- 帳號冒用處理。") + "\n#### 公司1｜", 1)
        self.src.write_text(source)
        self.draft.write_text(source)
        return source

    def test_public_is_verified_before_redaction(self):
        from public_redact import redact
        source = self.public_fixture()
        self.generate(["--public"])
        self.assertEqual(vp.verify_104_markdown(str(self.out), redact(source), public=True), [])
        self.assertIn('"image_action": "remove"', self.out.read_text())
        self.assertNotIn("帳號冒用處理", self.out.read_text())

    def test_public_does_not_hide_source_violation(self):
        self.public_fixture()
        self.src.write_text(self.src.read_text().replace("帳號冒用處理", "冒用虛構成果"))
        with self.assertRaises(ValueError):
            self.generate(["--public"])
        self.assertEqual(self.out.read_text(), self.good)

    def test_legacy_public_input_requires_exact_remote_derivative(self):
        from public_redact import redact
        source = self.public_fixture()
        self.src.write_text(redact(source))
        with patch.object(vp, "load_file_content", return_value=source):
            self.generate(["--public"])
        self.src.write_text(self.src.read_text().replace("產品規劃與交付", "偷偷改寫"))
        with patch.object(vp, "load_file_content", return_value=source):
            with self.assertRaises(ValueError):
                self.generate(["--public"])


if __name__ == "__main__":
    unittest.main()
