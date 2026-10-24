# 步驟 1｜調用職能＋職缺（v7.1）

- 職能清單沿用 `../v7/01-competencies.md`（F1–F15、交付鏈 14 項皆有落點）。
- **新增：職缺需求對照**。來源 `104/analysis.md`（46 份完整 JD 的需求頻率）、`104/jobs-2026-10.md`（A 級 15 筆已進 `career-ops/data/pipeline.md`）。
- 版本決定：**主版**（對應 A 級多數：人資科技／B2B SaaS、支付、AI、0→1）。各類職缺版留待使用者挑選投遞對象後再做。
- career-ops：`npm run doctor` 通過（3 個 warning 為 portals.yml 等非必要設定）。

## JD 需求 → 履歷落點
| JD 需求（筆數／46） | v7 狀態 | v7.1 處理 | 對應 essay |
| :--- | :--- | :--- | :--- |
| 跨部門協作（36） | ✅ | 保留；摘要點名 16 個單位 | P1、P10 |
| PRD／規格（32） | ✅ | 保留；用「規格書（PRD）」讓 ATS 認得 | P1 |
| 數據分析（~30） | ⚠️ 工具只在技能欄 | 留存分析寫明「兩份名冊快照比對」 | P6 |
| 測試／UAT／驗收（28） | ✅ 驗收案例 | 用 JD 的說法「UAT 驗收案例」 | P2 |
| API／系統串接（21） | ⚠️ 只在技能欄 | 舊系統相容、金流串接條目點出「系統串接」 | P3、Q4、S2 |
| AI／LLM（~20；Gogolook、USPACE 要 Claude） | ⚠️ 只在技能欄末 | **摘要加入 Claude Code AI 協作**；AI 功能條目保留 | P8、P9 |
| Figma／Axure／Wireframe（16） | ✅ | 保留 | P1、Q2 |
| Roadmap（13） | ⚠️ 只有 P0–P3 | 寫出 227 項 roadmap | P2 |
| 使用者訪談（13） | ⚠️ 技能欄 | 保留技能欄（無具體場景，Q 待補） | — |
| B2B／SaaS（12） | ✅ | 摘要用「B2B SaaS」說法 | P1 |
| 支付／金流（14 產業） | ✅ | 摘要點名 | Q4、S2 |
| 0→1（7，USPACE 必備） | ✅ | 保留 | Q1、Q2、Q5 |
| A/B 測試（5） | ✅ | 用「A/B 對照實驗」 | Q3 |
| 英文（9） | ✅ | 保留 | — |
| Jira（10）、SQL（8） | ❌ 未確認 | **不寫**（profile：未確認不得寫） | — |
| Agile／Scrum（10） | 裁定為 Kanban | 寫 Kanban、站會、回顧，不寫 Scrum | P2 |

## career-ops 驗證用關鍵字（步驟 8）
`產品經理,規格書,PRD,跨部門,驗收,UAT,API,AI,Claude,Figma,Axure,Wireframe,Roadmap,數據分析,使用者訪談,B2B,SaaS,金流,0 到 1,A/B,Kanban`

## 補充（2026-10-09）：改用 A 級 15 筆 JD 全文驗證
JD 全文來自使用者上傳檔（原先誤以為只有索引）；摘要 `104/jd-digest-A.md`。A 級 15 筆需求頻率：

| 需求 | 筆數／15 | v7.1 狀態 |
| :--- | :-: | :--- |
| PRD／規格 | 14 | ✅ |
| UAT／測試／驗收 | 12 | ✅ |
| 數據／SQL／BI | 12 | ⚠️ 有分析，**SQL 未確認，不寫** |
| 跨部門 | 10 | ✅ |
| AI／Claude／LLM | 8 | ✅（摘要） |
| Roadmap | 7 | ✅ |
| API／串接 | 7 | ✅ |
| Figma／Wireframe／Prototype | 7 | ✅ |
| 金流／支付 | 7 | ✅ |
| Jira／Confluence | 5 | ❌ 未確認，不寫 |
| 英文 | 5 | ✅（但全中文履歷，需英文版） |
| B2B／SaaS | 5 | ✅ |
| 0→1 | 5 | ✅ |
| 使用者訪談 | 5 | ⚠️ 只有技能欄 |
| Agile／Scrum | 4 | 寫 Kanban，不寫 Scrum |
| 定價／變現 | 2 | ✅ |
