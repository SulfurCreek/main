import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import verify_letter as vl  # noqa: E402


class LetterTests(unittest.TestCase):
    def test_undefined_product_flagged(self):
        errs = vl.check("Peach's web payment share rose from 24% to 80%.")
        self.assertTrue(any("Peach" in e for e in errs))

    def test_defined_product_passes(self):
        self.assertEqual(vl.check("For Peach, a subscription content app, web payment rose."), [])

    def test_only_first_mention_needs_definition(self):
        body = "For JustDating, our flagship dating app, I led a relaunch. JustDating grew."
        self.assertEqual(vl.check(body), [])

    def test_chinese_definition(self):
        self.assertEqual(vl.check("規劃訂閱制內容 App Peach 從 App 內購轉向網頁付款。"), [])

    def test_overconfident_closing_flagged(self):
        self.assertTrue(any("可以直接投入" in e for e in vl.check("我的經驗可以直接投入這個職位。")))

    def test_job_name_mismatch(self):
        self.assertTrue(vl.check("應徵貴司產品經理。", job="【北士科】Product Manager"))


class LetterTests2(unittest.TestCase):
    def test_separately_flagged(self):
        self.assertTrue(any("Separately" in e for e in vl.check("I set criteria. Separately, I fixed bugs.")))

    def test_unapproved_city_flagged(self):
        self.assertTrue(any("Singapore" in e for e in vl.check("I worked with CodaPay, a payment provider, in Singapore.")))

    def test_old_closing_flagged(self):
        self.assertTrue(any("可用於" in e for e in vl.check("這些經驗可用於貴司產品。")))


if __name__ == "__main__":
    unittest.main()
