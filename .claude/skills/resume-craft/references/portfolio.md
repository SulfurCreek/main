<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

# 作品集 / Portfolio ・ 大企業訊號

> 回 [`../SKILL.md`](../SKILL.md)。範本：國際／英文版 [`../assets/portfolio-case-study.md`](../assets/portfolio-case-study.md)、台灣版 [`../assets/portfolio-case-study-tw.md`](../assets/portfolio-case-study-tw.md)（選法見下方〈市場路由〉）。
> 已完成的實例：`career/portfolio/e1-cross-system-messaging.md`。

## 作品集

**何時放連結**：資深 PM（5+ 年）**預期要有**；轉職進 PM、成長型角色也建議放。
放在 **header**（與 LinkedIn 並列），勿塞進工作經歷 bullet。

**Case study 結構（problem → research → approach → results）**，每篇 400–800 字：

1. **問題／背景**：使用者痛點 + 量化現況（含 benchmark）。
2. **研究與洞察**：怎麼理解問題（訪談片段、漏斗、競品）——展示思路，不只結論。
3. **方法與取捨**：為何選這個解（wireframe、PRD 摘錄、假設、實驗設計、取捨）。
4. **結果與學習**：量化成果 + 學到什麼，**至少放一個誠實的失敗實驗**（比「完美」更可信）。

**履歷 ↔ 作品集分工：**

| 元素 | 履歷 | 作品集 |
| :--- | :--- | :--- |
| 內容 | 一行 + 量化結果 | 完整 problem→思路→結果 |
| 深度 | 只給結果 | 過程、取捨、迭代 |
| 素材 | 無 | wireframe／PRD／圖表／回饋 |
| 失敗／迭代 | 不提 | 核心，要展示 |
| 閱讀 | 6 秒掃 | 有興趣才細讀 5–15 分 |

**3–5 篇即可**（深度 > 數量）；用真實素材但**勿放機密 1111 資料**（去識別化或用個人專案）。

## 市場路由：用哪份範本

| 投遞對象 | 範本 | 重點 |
| :--- | :--- | :--- |
| 外商／英文／策略型角色 | [`portfolio-case-study.md`](../assets/portfolio-case-study.md)（國際版） | Executive Summary、Hypothesis、策略重要性、RICE 式優先級 |
| 台灣本土企業／新創／執行導向 | [`portfolio-case-study-tw.md`](../assets/portfolio-case-study-tw.md)（台灣版） | 系統分析與規格定義、跨部門交付、上線同步 |

**同一個專案可以出兩版，但兩份共用同一批事實與數字**：先定稿事實與去識別化後的數字，再分別套版；不可為了迎合市場讓兩版的數字、角色或時程不一致。

## 對外版（供作品集網站）

作品集內部版（`career/portfolio/*.md`）可含內部細節；**要上網站的篇章另產對外版**：`career/portfolio/public/<slug>.md`，
由 Career Move 依下方 NDA 規則去識別化後撰寫，front matter 含 `publish: draft|ready`（使用者核可才設 `ready`）、`source`、`highlights`（首頁數字卡，最多 3 條）。
欄位與交接流程見 `wiki/personal_line_collab.md`。對外版與內部版共用同一批事實與數字，只是抽象化，不新增、不改寫成果。
預設保守：不寫公司名、不寫 HackMD／內部 wiki／RAG 索引、時間線只寫年資級距；使用者明說才放寬。

## NDA 去識別化規則

1. **數字**：絕對值改成 % 或相對值（如「流失 60% → 38%」、「縮短一半」）；營收、人數四捨五入成級距（如「數百人」「千萬級」）。
2. **名稱**：去掉內部 API 名、欄位名、系統代碼，以及客戶與廠商名稱，用通用說法（「後台審核流程」「某類企業客戶」）。
3. **圖**：截圖與流程圖也要去識別化；Mermaid 節點用通用名稱，不放真實欄位。
4. **禁止編造或使用假資料**：沒有數據就標 `〔待補數據〕` 或只寫質化描述。誠實契約優先於美觀，寧可版面空一格，也不放編出來的數字。
5. 來源是 1111 內部資料（工單、客戶名冊、Roadmap）者，對外版本一律先抽象化，見 `career/CLAUDE.md` 硬規則二。

## Mermaid 圖

作品集裡的 Mermaid 一律照 [`wiki/mermaid_styling_rules.md`](../../../../wiki/mermaid_styling_rules.md)（柔和色系、`classDef`、長文字用 `<br>`），並用 mermaid-cli 渲染驗證後才放進文件。每篇最多 1 張，圖要能幫讀者理解狀態、權限或互斥規則，不當裝飾。

## 大企業訊號

**Amazon Leadership Principles**（每關都考；讓 bullet 對映 4–5 條）：

| 原則 | 履歷訊號 | 範例 |
| :--- | :--- | :--- |
| Customer Obsession | 以用戶為中心、影響客戶指標 | 50+ 訪談洞察驅動功能，NPS +12、流失 -15% |
| Ownership | 端到端當責（owned 不是 supported）| 主導 onboarding，留存 +22pt |
| Invent and Simplify | 創新 + 化繁為簡 | 7 步簡化為 3 步，完成率 +60% |
| Dive Deep | 細節分析、非表面 | 分析 500K cohort + session 找出流失主因 |
| Bias for Action | 速度與決斷 | 驗證迴圈 2 週 vs 6 週 |
| Deliver Results | 量化成果、達標 | 12 功能準時、$3M ARR、零重大上線 bug |
| Earn Trust | 跨團隊信任 | C-suite 三項策略決策的信任顧問 |

**Google**：系統／規模思維、清楚的數據敘事、成長指標。
**Meta**：快速實驗、成長／互動、加速工程速度、排序／推薦系統。
**McKinsey（策略職）**：清楚商業影響、建議 > 執行、市場洞察、影響範圍（C-suite／跨組採用）。
