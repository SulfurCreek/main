# 履歷工具入口｜2026-11-03

政策唯一依 [../PIPELINE_POLICY.md](../PIPELINE_POLICY.md)。自動事實驗證全部停用；格式、文體與轉換通過不證明事實正確。

| 任務 | 入口 |
| --- | --- |
| 中文帶標記來源／候選格式與文體 | verify_polish.py；不驗數字、限定或LOCK內容 |
| 中文104產生／驗證 | gen_104_md.py；verify_polish.py --verify-104 |
| 公開處理 | gen_104_md.py --public；public_redact.py只處理支援格式 |
| 英文LINE格式／文體 | verify_line_profile.py --for verify／pack／pdf |
| 英文解析 | line_md.py |
| 英文JSON | gen_line_pack.py，prepare讀取及驗證同一快照 |
| HTML／PDF／內容對帳 | gen_line_pdf.py、build_line_pdf.py、verify_line_pdf.py |
| 104解析 | md104.py |
| 雙語核可映射 | bilingual_contract.py；生成與驗證共用契約，不判定事實真假 |
| 雙語組裝與驗證 | gen_104_bilingual.py、verify_104_bilingual.py |
| 推薦信 | gen_cover_drafts.py、verify_letter.py、gen_cover_index.py；既有介面 |
| 固定完整工具包 | run_pinned_verifier.py |

```bash
python3 career/scripts/run_pinned_verifier.py <完整工具SHA> verify_polish.py --local-codex
python3 career/scripts/verify_line_profile.py <英文md> --for pack
python3 career/scripts/build_line_pdf.py <英文md> <PDF>
python3 career/scripts/gen_104_bilingual.py --zh <中文一般版104.md> --line <核可LINE.md> --out <雙語.md>
python3 -m unittest discover -s career/scripts/tests -p 'test_*.py' -v
```

runner本身亦須來自指定完整checkout；禁止單檔git show串流。--all使用完整固定checkout。
--upstream僅保留參數相容性，不讀取或比對事實來源。
雙語 pending 回傳3且不覆蓋正式檔；失敗不得留下本輪通過標示。
PDF仍需人工視覺驗收。
fact_lock.py只保留退役標示、不提供驗證API；舊碼與測試在archive，不得重新接回流程。
