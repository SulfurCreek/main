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


class LetterTests4(unittest.TestCase):
    def test_wrong_honorific_flagged(self):
        for w in ("貴司", "我司", "敝司"):
            self.assertTrue(any(w in e for e in vl.check(f"應徵{w}職缺。")))

    def test_hollow_hook_flagged(self):
        self.assertTrue(any("工作方向相近" in e for e in vl.check("貴公司的工作，與我目前的工作方向相近。")))

    def test_backed_by_and_trailing_which_flagged(self):
        self.assertTrue(any("Backed by" in e for e in vl.check("Backed by 199 client requests, I planned a flow.")))
        self.assertTrue(any("which leave" in e for e in vl.check("I merged tools, which leave invitations scattered.")))

    def test_good_english_passes(self):
        ok = "Because employers and job seekers message across two overlapping tools, interview invitations get scattered."
        self.assertFalse(any("Backed" in e or "which" in e for e in vl.check(ok)))


if __name__ == "__main__":
    unittest.main()


class ContractTests(unittest.TestCase):
    """2026-11-02 P0／P1：正文抽取、結構與長度契約、英文禁詞大小寫。"""

    @staticmethod
    def zh_letter(n):
        head = "您好：\n應徵貴公司產品經理。我有近 10 年產品經理經驗。\n\n"
        bullets = "‧ 規劃功能甲。\n\n‧ 規劃功能乙。\n\n‧ 規劃功能丙。\n\n"
        tail = "跨部門專案推進，正是我持續處理的課題。期待有機會與貴公司團隊進一步交流。\n\n聶崑淮\n"
        base = vl.char_count(head + bullets + tail)
        return head + bullets.replace("甲", "甲" + "字" * (n - base)) + tail

    def test_empty_fence_fails(self):
        self.assertEqual(vl.verify_text("```text\n```\n")[0], 0)
        self.assertTrue(vl.verify_text("```text\n```\n")[1])

    def test_greeting_only_fails(self):
        self.assertTrue(vl.verify_text("```text\n您好：\n\n聶崑淮\n```\n")[1])

    def test_unclosed_fence_fails(self):
        self.assertTrue(any("未閉合" in e for e in vl.verify_text("```text\n您好：\n內容")[1]))

    def test_missing_fence_fails(self):
        self.assertTrue(any("缺正文" in e for e in vl.verify_text("沒有區塊")[1]))

    def test_length_boundaries(self):
        for n, err, wrn in ((249, True, False), (250, False, False), (350, False, False), (351, False, True)):
            b = self.zh_letter(n)
            self.assertEqual(vl.char_count(b), n)
            e, w = vl.check_structure(b)
            self.assertEqual(bool(e), err, (n, e))
            self.assertEqual(bool(w), wrn, (n, w))

    def test_bullet_count(self):
        b = self.zh_letter(300).replace("‧ 規劃功能丙。\n\n", "")
        self.assertTrue(any("條列數" in e for e in vl.check_structure(b)[0]))

    def test_spearheaded_case_insensitive(self):
        for w in ("Spearheaded", "spearheaded", "SPEARHEADED"):
            self.assertTrue(any("Spearheaded" in e for e in vl.check(f"I {w} the launch.")), w)
        self.assertFalse(vl.check("I spearhead nothing here."))

    def test_english_letter_skips_zh_closing(self):
        body = "Dear team,\n\nI led a launch.\n\nI look forward to talking.\n\nKun Huai Nieh"
        self.assertFalse(any("結尾" in e for e in vl.check(body)))

    def test_cli_bad_args(self):
        self.assertEqual(vl.main([]), 2)
