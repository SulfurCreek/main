"""104 中英並列產生器回歸測試（讀 repo 內已定稿檔；缺檔時略過）。"""
import pathlib
import re
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import gen_104_bilingual as gb  # noqa: E402
import line_md  # noqa: E402
import verify_polish as vp  # noqa: E402


@unittest.skipUnless(gb.ZH_MD.exists() and gb.LINE_MD.exists(), "需要 v12.19 公開版與 LINE resume")
class BilingualTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.zh = gb.ZH_MD.read_text(encoding="utf-8")
        line_text = gb.LINE_MD.read_text(encoding="utf-8")
        cls.doc = line_md.parse(line_text)
        cls.eng = gb.english_blocks(cls.doc)
        cls.out = gb.combine(cls.zh, cls.eng)

    def test_chinese_kept_verbatim(self):
        for m in re.finditer(r"### 2\.\d [^\n]*\n.*?```html\n(.*?)```", self.zh, re.S):
            self.assertIn(m.group(1).rstrip("\n"), self.out)
        bio = re.search(r'"mode": "plain_text"\}\n-->\n\n```text\n(近 10 年.*?)```', self.zh, re.S).group(1).strip()
        self.assertIn(bio, self.out)

    def test_english_first_in_every_field(self):
        bio = re.search(r'"mode": "plain_text"\}\n-->\n\n```text\n(.*?)```', self.out, re.S).group(1)
        self.assertTrue(bio.startswith("Product Owner"))
        self.assertLess(bio.index("Product Owner"), bio.index("近 10 年"))
        for m in re.finditer(r"### 2\.\d [^\n]*\n.*?```html\n(.*?)```", self.out, re.S):
            h = m.group(1)
            first_cjk = re.search(r"[一-鿿]", h).start()
            first_en = re.search(r"[A-Za-z]{4}", h).start()
            self.assertLess(first_en, first_cjk)

    def test_other_fields_untouched(self):
        for key in ("把構想變成產品", "AI Agent 協作", "從交友與訂閱制 App、網紅媒合平台到企業招募系統"):
            self.assertEqual(self.zh.count(key), self.out.count(key), key)
        self.assertNotIn("英文自傳", self.out)

    def test_blocks_parse_with_104_html_whitelist(self):
        for m in re.finditer(r"### 2\.\d [^\n]*\n.*?```html\n(.*?)```", self.out, re.S):
            p = vp.FieldHTML()
            p.feed(m.group(1))
            p.close()

    def test_every_english_bullet_comes_from_line_resume(self):
        src = set(sum([x["bullets"] for x in self.doc["directives"] if x["d"]["target_block"] == "work_experience"], []))
        src = {gb.reduce_fix(b) for b in src}
        for idx, (bl, _) in self.eng.items():
            for b in bl:
                self.assertIn(b, src)

    def test_accent_phrase_must_exist(self):
        with self.assertRaises(ValueError):
            gb.accent_html("abc", {"G": ["xyz"]})


if __name__ == "__main__":
    unittest.main()
