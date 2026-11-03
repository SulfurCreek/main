# Codex Resume Writer 路由

操作入口AGENTS.md；自動檢查與流程唯一政策為Claude分支career/PIPELINE_POLICY.md。
Codex獲准唯讀該政策與CAREER_START_HERE.md，其他存取邊界不變；main嚴格唯讀。

| 任務 | 路由 |
| --- | --- |
| 中文／英文語氣 | voice_style_guide.md各自語言章 |
| 上游／候選 | 本人指定完整SHA與路徑，完整閱讀，不自行跨受限目錄補事實 |
| 格式／文體 | 固定完整工具包的對應verify；不判事實 |
| 自動事實、數字、LOCK比對 | 全部停用，改主代理人工判斷 |
| check_polish_structure.py | 退役；原碼封存，不重新啟用 |
| FINAL-LOCKED雙語 | 核可英文只擷取與排列，不改寫 |
| PDF／轉換／填表 | Claude執行與驗收，未實做標未驗證 |

完整閱讀／改稿→格式文體Exit 0→隔離盲審→三分類→修改後重驗及全文閱讀→Claude終審。
歷史INDEX／archive／交接只供追溯。規則維護不虛報成品盲審。

## 本輪部署狀態
Claude 工具／政策版本：d969f97589d7a73113b7c40e49840dc9d165d069。
voice_style_guide.md 與 AGENTS.md 已依本人明確授權部署，兩份原版均已封存。
兩檔舊的自動事實比對、數字及 LOCK gate 指令依本人最新裁定失效；不重新執行退役工具。
其他人工閱讀、存取邊界及語言規則仍適用。正式使用以本人裁定與上述政策為準。
