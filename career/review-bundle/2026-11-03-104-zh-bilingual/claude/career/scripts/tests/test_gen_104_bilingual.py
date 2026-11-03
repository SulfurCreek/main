"""104 中英並列產生器與驗收回歸測試（讀 repo 內已定稿檔；缺檔時略過）。"""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import gen_104_bilingual as gb  # noqa: E402
import verify_104_bilingual as vb  # noqa: E402

OUT = gb.ZH_MD.parent.parent / "v12.19-bilingual" / "104-v12.19-bilingual.md"


@unittest.skipUnless(gb.ZH_MD.exists() and gb.LINE_MD.exists() and OUT.exists(), "需要公開版、LINE resume 與並列檔")
class BilingualTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.zh = gb.ZH_MD.read_text(encoding="utf-8")
        cls.line = gb.LINE_MD.read_text(encoding="utf-8")
        cls.out = OUT.read_text(encoding="utf-8")

    def test_strict_pass(self):
        errs, manual = vb.verify(self.out, self.zh, self.line, strict=True)
        self.assertEqual(errs, [])
        self.assertEqual(manual, [])

    def test_fifteen_fields_including_skills(self):
        keys = [k for k, _ in vb.fields(self.out)]
        self.assertEqual(len(keys), 15)
        self.assertEqual(sum(k.startswith("skill") for k in keys), 6)

    def test_changed_english_sentence_is_flagged_not_failed(self):
        en, _ = vb.split_lang(vb.fields(self.out)[0][1])
        first = gb.sentences(vb.norm(en))[0]
        mutated = self.out.replace(first, first + " Extra clause added.", 1)
        errs, manual = vb.verify(mutated, self.zh, self.line, strict=False)
        self.assertEqual(errs, [])
        self.assertTrue(manual)
        errs, _ = vb.verify(mutated, self.zh, self.line, strict=True)
        self.assertTrue(errs)

    def test_altered_chinese_is_rejected(self):
        mutated = self.out.replace("近 10 年", "近 11 年", 1)
        errs, _ = vb.verify(mutated, self.zh, self.line)
        self.assertTrue(any("中文被改動" in e for e in errs))

    def test_experience_english_only_and_within_104_limit(self):
        for k, block in vb.fields(self.out):
            if k.startswith("exp"):
                self.assertFalse(vb.CJK.search(block), k)
                import re as _re
                self.assertLessEqual(len(_re.sub(r"<[^>]*>", "", block).strip()), vb.EXP_LIMIT, k)

    def test_over_limit_experience_is_rejected(self):
        pad = "<p>" + "Extra sentence here. " * 120 + "</p>\n"
        mutated = self.out.replace("### 2.4", "### 2.4", 1)
        i = mutated.index("```html\n", mutated.index("### 2.4")) + len("```html\n")
        mutated = mutated[:i] + pad + mutated[i:]
        errs, _ = vb.verify(mutated, self.zh, self.line)
        self.assertTrue(any("104 字數超標" in e for e in errs))

    def test_accent_phrase_must_exist(self):
        with self.assertRaises(ValueError):
            gb.accent_html("abc", {"G": ["xyz"]})


if __name__ == "__main__":
    unittest.main()
