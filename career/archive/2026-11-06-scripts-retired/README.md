# 2026-11-06 退役腳本與測試原始碼

僅供追溯，不指定目前底稿。以 `.txt` 保存，不可直接執行；`career/scripts/` 內同名 `.py` 為退役 stub（RETIRED = True，執行 exit 1，未執行任何驗證）。

腳本：verify_polish、verify_letter、verify_104_bilingual、verify_line_profile、verify_line_pdf、run_pinned_verifier、strip_markers。
測試：test_resume_pipeline、test_resume_contracts、test_pinned_verifier、test_verify_letter、test_gen_104_bilingual、test_gen_cover_drafts（後者經 verify_letter 驗證，連帶失效）。
