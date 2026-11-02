# 英文履歷語氣與編譯護欄（en）

> 適用：LINE Resume／通用版、LinkedIn、英文 CV、推薦信英文條列。**不適用於中文輸出**（中文見 `zh-voice-guardrails.md`）。英文語氣規範：`career/style/voice-en.md`；驗證：`scripts/verify_line_profile.py`、`scripts/verify_line_pdf.py`。

## 跨語言一致性護欄（2026-10-29，本人：LINE profile 英文稿被降維）

編譯任何英文版履歷（LINE、LinkedIn、英文 CV、推薦信英文條列）時，**必須 100% 保留中文版 Stage 2 的四大支柱商業目的（Why）、系統影響範圍（Stakes）與統計分母口徑**，嚴禁因語言轉換或壓縮字數刪除。逐點對照中文版：句首目的、句尾客戶回饋調整、共同基礎定位、分母口徑、時序（啟動≠上線）缺一不可。另避免中文直譯撞上工程術語（merge request 等），細則見 `style/voice-en.md` §7；驗證層：`scripts/verify_line_profile.py` 的黑名單與必備錨點。



## 英文履歷職級感與反贅字護欄（2026-11-01，本人：LINE Resume 審核）

編譯任何英文履歷（LINE、LinkedIn、英文 CV）時，另須遵守 `style/voice-en.md` §9：直屬部屬一律 `direct reports`／`delegated … to direct reports`；代碼表類首句須定義對象，不得裸寫 `categories`；`human-in-the-loop` 不與 `human review` 疊用；Skills 用 Title Case 與 `&`；`Claude Code`、`Antigravity` 前須帶 `AI agents`／`Agentic AI Tools`；同一數字只留在一處。驗證層：`scripts/verify_line_profile.py`。



## 英文履歷結構、日期與 PDF 護欄（2026-11-02，本人第二次抓出同類問題）

編譯任何外商英文履歷時（見 `style/voice-en.md` §11–§12）：不放 Personal Statement，PDF ≤2 頁；姓名 `Kun Huai Nieh`；禁 `Reverse-engineer(ed)`；起訖日期 `YYYY-MM – YYYY-MM`，內文日期用 `YYYY/MM`，不以日期開頭。驗證層：`scripts/verify_line_profile.py`（原稿）與 `scripts/verify_line_pdf.py`（PDF 成品）。
