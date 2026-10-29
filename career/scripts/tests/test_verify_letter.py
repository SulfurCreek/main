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


class LetterTests3(unittest.TestCase):
    def test_label_bullet_flagged(self):
        self.assertTrue(any("冒號小標" in e for e in vl.check("‧ 多方需求取捨：我先取得背書。\n\n期待交流。\n\n聶崑淮")))

    def test_headless_bullet_flagged(self):
        self.assertTrue(any("無頭斷句" in e for e in vl.check("‧ 截至 2026/Q3，約 70 項功能上線。")))
        self.assertTrue(any("無頭斷句" in e for e in vl.check("‧ 帳號權限缺乏文件。")))

    def test_verbose_list_flagged(self):
        self.assertTrue(any("帳號、登入" in e for e in vl.check("840 件帳號、登入、公司資料與聯絡人相關建議")))

    def test_arrogant_closing_flagged(self):
        self.assertTrue(any("直接解決" in e for e in vl.check("我能直接解決貴司問題。")))

    def test_closing_must_be_humble(self):
        body = "您好：\n應徵。\n\n貴司做支付，我有經驗。謝謝。\n\n聶崑淮"
        self.assertTrue(any("結尾不謙和" in e for e in vl.check(body)))
        ok = "您好：\n應徵。\n\n期待能與團隊進一步交流。謝謝。\n\n聶崑淮"
        self.assertFalse(any("結尾不謙和" in e for e in vl.check(ok)))

    def test_names_warn_not_fail(self):
        self.assertTrue(vl.warn("For Peach, a subscription content app, web payments rose."))
        self.assertFalse(vl.warn("CodaPay, a payment provider", payment=True))


if __name__ == "__main__":
    unittest.main()
