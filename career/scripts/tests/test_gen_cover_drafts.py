"""gen_cover_drafts 離線回歸測試（合成資料，不依賴 automation/104-data）。"""
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import gen_cover_drafts as g  # noqa: E402

JD = ("【工作內容】負責產品規格撰寫、需求訪談與跨部門溝通，追蹤專案進度與交付，"
      "與業務、客服協作，分析數據指標並提出優化方案。" * 3)


def setup_data(extra=None):
    jobs = {"aaaaa": {"title": "產品經理 <需兩年以上經驗>", "description": JD, "company_id": "c1"},
            "bbbbb": {"title": "智慧製造系統產品經理_新店", "description": JD + "定價 訂閱 A/B", "company_id": "c2"},
            "ccccc": {"title": "產品經理", "description": "", "company_id": "c1"}}
    jobs.update(extra or {})
    comps = {"c1": {"name": "測試軟體股份有限公司", "industry": "電腦軟體服務業"},
             "c2": {"name": "測試航電股份有限公司", "industry": "電子零組件製造業"}}
    g.load({"jobs": jobs}, comps)


class TitleTests(unittest.TestCase):
    def test_clean_title(self):
        cases = {"裕隆集團關係企業-產品經理(Product Manager)": "產品經理(Product Manager)",
                 "產品經理 <需兩年以上經驗>": "產品經理", "資深產品經理【擴編】": "資深產品經理",
                 "專案管理_26072": "專案管理", "PM_JR202609021": "PM",
                 "B2B PM AI顧問｜ B2B PM, AI Consultant": "B2B PM AI顧問",
                 "專案管理【產品經理／專案管理師／專案助理】（台北）": "專案管理",
                 "資深AI/Data專案管理師PJM [7-1]": "資深AI/Data專案管理師PJM"}
        for raw, want in cases.items():
            self.assertEqual(g.clean_title(raw), want, raw)


class GenerateTests(unittest.TestCase):
    def setUp(self):
        setup_data()
        self.tmp = tempfile.TemporaryDirectory()
        self.out = pathlib.Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_missing_jd_fails_and_writes_nothing(self):
        res = g.generate(["ccccc", "zzzzz"], self.out)
        self.assertEqual([r[1] for r in res], ["失敗", "失敗"])
        self.assertEqual(list(self.out.iterdir()), [])

    def test_existing_file_not_overwritten(self):
        first = g.generate(["aaaaa"], self.out)[0]
        self.assertEqual(first[1], "成功")
        path = first[3]
        path.write_bytes("人工修改".encode())
        again = g.generate(["aaaaa"], self.out)[0]
        self.assertEqual(again[1], "略過")
        self.assertEqual(path.read_bytes(), "人工修改".encode())
        self.assertEqual(g.generate(["aaaaa"], self.out, overwrite=True)[0][1], "成功")

    def test_written_draft_passes_verifier_and_has_clean_title(self):
        path = g.generate(["aaaaa"], self.out)[0][3]
        text = path.read_text(encoding="utf-8")
        self.assertIn("應徵貴公司產品經理。", text)
        self.assertIn("職缺原名：產品經理 <需兩年以上經驗>", text)
        n, errs, _ = g.vl.verify_text(text, "產品經理", "測試軟體")
        self.assertEqual((n, errs), (1, []))

    def test_hardware_excludes_consumer_cases(self):
        chosen = g.build("bbbbb")[2]
        self.assertFalse(set(chosen) & set("PJKL"), chosen)

    def test_three_distinct_points(self):
        chosen = g.build("aaaaa")[2]
        self.assertEqual(len(chosen), 3)
        self.assertEqual(len(set(chosen)), 3)


if __name__ == "__main__":
    unittest.main()
