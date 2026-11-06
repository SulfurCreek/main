# Career 工具入口

角色與管線依 `../ROLE_CONTRACT.md`、`../PIPELINE_POLICY.md`。工具不是第五個履歷角色。

- 不跑 verify、fact_lock、相似度、黑名單、LOCK／數字來源比對、ATS 分數或以 Exit 0 定稿的歷史路線。
- Writer／Marketer 不使用控制標記或解鎖流程，Fact Gatherer 訪談不是程式化 fact gate。
- 現有歷史腳本保留作追溯；含內建驗證的 gen/build/pack 不因此變成獲准純格式工具，不照抄歷史整串命令執行。
- 只在當輪有需求時使用已支援的純排版、字元統計、JSON／Quill 組裝或轉檔路徑；先了解實際介面與副作用，不為文字任務重建驗證器。
- 本人指定來源與輸出、格式生成、人工閱讀、HR 結果、PDF 視覺分別回報；沒有實際產物不宣稱通過。

舊指令原文由 Git 與 archive 保存。104 格式參數依 ../104/fields-spec.md 及 ../104/content-spec-quill.md；範例不提供履歷事實或 LOCK 規則。

## 逐檔清單（2026-11-06）

| 現行純格式／輔助工具（先確認介面與副作用） | 已退役（stub，原始碼在 `../archive/2026-11-06-scripts-retired/*.txt`） |
| --- | --- |
| md104.py、line_md.py、bilingual_contract.py、public_redact.py、build_zh_pdf.py、gen_cover_index.py | verify_polish.py、verify_letter.py、verify_104_bilingual.py、verify_line_profile.py、verify_line_pdf.py、run_pinned_verifier.py、strip_markers.py、fact_lock.py（2026-11-03） |

含已停用驗證、勿照歷史命令執行（檔頭已標註；匯入或呼叫上列退役腳本，現在會失敗）：gen_104_md.py、gen_cover_drafts.py、gen_line_pack.py、gen_104_bilingual.py、gen_line_pdf.py、build_line_pdf.py。

`tests/` 內全部測試已隨被測腳本移入 archive，目前無測試。
