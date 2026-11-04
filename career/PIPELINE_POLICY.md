# 履歷與求職管線政策（2026-11-04 全面革新版）

## 1. 全面停用所有事實驗證與鎖定限制（Full Decommissioning of Verification & Locks）
- **徹底停用所有驗證器做事實或詞彙把關**：不再執行 `verify_polish.py`、`verify_line_profile.py`、`verify_letter.py`、`verify_104_bilingual.py` 中的任何事實比對、禁用詞掃描、相似度檢查、區塊數檢查或 `LOCK_ENTITIES` 核對。
- **廢除所有內部控制標籤與出處註解**：草稿與定稿中**不再標註** `[LOCK_ENTITIES: ...]`、`[STATUS: LOCKED]`、`[LEAD: ...]`、`[AMPLIFY: ...]` 或 `> 出處：...` 註解。
- **不再將修改決定回寫為腳本規則**：任何文字調整均以「能否在 6 秒內驚艷 HR 與 Hiring Manager」為唯一標準，嚴禁將編輯偏好轉寫成正規表達式斷言或硬性禁令。

## 2. 僅保留之純技術輔助（Optional Formatting Only）
- 腳本僅用於「純排版與檔案轉換」（如 Markdown 轉 PDF、104 JSON directive 結構組裝或純字元長度統計），絕不介入文字內容、選材與語氣判斷。
