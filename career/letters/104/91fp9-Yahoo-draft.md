<!--
104 自我推薦信上游草稿 r1（2026-10-29，四階段工作流＋verify_letter）｜j-91fp9 Yahoo（香港商雅虎資訊）[R78] (Sr.)Product Manager 產品經理｜分級：一般｜Career Move
給潤飾者（Codex）：
1. 只改語感與節奏；不改公司名、職缺名、數字、日期、條列點數；不新增事實或對公司的觀察。
2. 純文字；條列用「‧」。方案 A：中文破題約 100 字＋英文條列 120–150 words（JD 為英文）；方案 B：全中文 250–350 字。英文依 career/style/voice-en.md。
3. 語氣：破題與條列 pursuing／proactive；結尾謙和（「期待能將…」），不寫「可以直接投入」（decisions §56）。
4. 「主導／led」只能用在 AI 功能（decisions §51）；訊息整合只寫規劃與「開發中」，不寫預計日期、不寫成效。
5. 禁用：AI 套話、乞求句、strategic、passionate、detail-oriented、proactive；不暗示 SQL、Adobe Campaign、LangChain／n8n、MarTech 業界資歷、Machine Learning 經驗；一點只講一件事，不用 Separately／另外 硬湊；產品名第一次出現要交代是什麼；不寫新加坡、國籍。
6. 交件前跑 `python3 career/scripts/verify_letter.py <檔> --job "[R78] (Sr.)Product Manager 產品經理"`，0 違規。
-->

# 正文（方案 A：中文破題＋英文條列，建議採用）

```text
您好：
應徵貴司 [R78] (Sr.)Product Manager 產品經理。我有近 10 年產品經理經驗，現任人力銀行企業端招募系統 Product Owner，並以 AI Agent 協作日常的規格撰寫與資料分析。以下是三項相關經驗：

‧ I work with AI agents such as Antigravity and Claude Code on specs and data analysis. I define the problem, rules and verification requirements, the agent checks the data and flags its confidence, and a person makes the final call. I turned this practice into a reusable skill and taught a colleague to use it on large volumes of data.
‧ I led the launch of AI-generated job descriptions and AI talent recommendations in our recruitment system, working with the data science team on use cases and acceptance criteria. Employers confirm AI content before publishing, and we adjust recommendation rules based on what clients actually select.
‧ Employers and job seekers were messaging through two overlapping tools. I am planning to merge them into one flow, responding to 199 client requests accumulated since 2021; the work is in development.

期待能將 AI Agent 工作流與訊息平台規劃的經驗，運用在貴司的產品團隊。謝謝您的閱讀。

聶崑淮
```

# 正文（方案 B：全中文備選）

```text
您好：
應徵貴司 [R78] (Sr.)Product Manager 產品經理。我有近 10 年產品經理經驗，現任人力銀行企業端招募系統 Product Owner，並以 AI Agent 協作日常的規格撰寫與資料分析。

‧ 以 Antigravity、Claude Code 等 AI Agent 協作：我先定義問題、規則與驗證要求，由 AI 檢查資料並標示把握程度，最後由人判斷；並將做法整理成 skill，教同仁用它處理大量資料。
‧ 主導企業端招募系統的職缺工作說明生成與 AI 推薦人才上線，與資料科學團隊定義使用情境與驗收標準；AI 內容經企業確認才刊登，並依客戶實際選用調整推薦規則。
‧ 企業與求職者的訊息分散在兩套功能重複的工具，我正規劃整合為一條流程，回應 2021 年起累積的 199 件客戶建議；目前開發中。

期待能將 AI Agent 工作流與訊息平台規劃的經驗，運用在貴司的產品團隊。謝謝您的閱讀。

聶崑淮
```

# 對位表

| 點 | JD 需求 | 四大支柱 | library 出處 |
| --- | --- | --- | --- |
| 破題 | 8 年以上；business sense | ③④ | profile；facts-1111 第 270–274 行 |
| 1 | AI agentic tools & automation；內部推廣 | ④ | facts-1111 第 270–274 行；about-me §四〈AI Agent 與 human in the loop〉〈帶人〉；decisions §50 |
| 2 | LLM／AI 應用；跨部門與分析師協作 | ④② | facts-1111〈AI 功能品質把關〉第 338 行；decisions §46、§51 |
| 3 | customer messaging platform；roadmap、優先序 | ③ | facts-1111 第 49、243–244 行（199 件、開發中）；decisions §24（只寫開發中） |

# 刻意不寫

| 缺口或素材 | 處理 |
| --- | --- |
| SQL、資料庫查詢 | 不會（R11），不提；JD 為必要條件，信中不暗示 |
| Adobe Campaign、Salesforce Marketing Cloud、eDM／Push | 無經驗，不提 |
| LangChain、n8n 等 AI 工作流平台 | 無紀錄，不提 |
| Machine Learning | 不寫（FORBIDDEN 標籤） |
| 信件與即時通上線日期、成效 | 披露規則：只寫開發中 |
| 歐洲金流商英文洽談 | 一點一事與字數考量未放；面試可補（JD 有海外電話會議） |
| 優先序取捨與被延後項目 | R01，面試口述 |

# 字數

方案 A 中文約 94 字、英文約 137 words；方案 B 379 字（含標點、不含空白）；verify_letter 0 違規。
