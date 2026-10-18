<!--markdownlint-disable MD013-->

# v10.4 驗證統整（Opus 58 份＋ChatGPT 49 份）｜2026-10-19

| 來源 | 範圍 | 結果 |
| :-- | :-- | :-- |
| Opus F 層（各自獨立） | 14 | 面試 13、先釐清 1（8kebd）；Level 7×10、8×3、6×1；決策深度 強 10／足夠 4 |
| Opus L 層（5 批） | 44 | fit 高 13／中 22／低 9；面試 27、先釐清 16、不符 1 |
| ChatGPT（同一對話連續審，非獨立） | L 44＋F 錨點 5 | L：fit 高 14／中 24／低 6；面試 24、先釐清 19、不符 1。F 錨點 Level 6/7/7/7/8 |

## 兩模型一致度
- L 層 44 份：fit 一致 33、決定一致 29。
- F 錨點 5 份：Level 差 ≤1；決定有 3 份不同（8ocje、94le0、950oe：ChatGPT 先釐清、Opus 面試），都卡在工具（Jira／Confluence）或近母語英文這類「履歷沒寫」的條件。依路由規則（≥2 份不同）可加跑 Gemini 錨點；差異原因明確，可不跑。

## 投遞優先：兩模型都評 fit 高（9 份）
玩美移動 SaaS PM（95zyw）、玩美移動 App PM（7dijs）、買即可 產品經理（95q7h）、拍付 支付連（8692h）、蝦皮 Seller & Financial（8f25l）、LINE Pay Product Planner（8sxlq）、台灣大哥大 AI 專案 PM（96686）、台灣大哥大 D597 產品專案 PM（7wq7q）、蝦皮 Product Solution（8x7oe）。
加上 F 層 Level 8 的 3 份（見 opus-matrix.md）。

## 任一模型評 fit 低（9 份，優先度最低）
口袋證券 軟體 PM、台哥大 數據服務與金流 PM、台哥大 D637 金流營運、遠傳 行動支付、Taiwan AI Labs FedGPT、台哥大 I110 AI PM、Klook API PM、和泰 去趣、蝦皮店到店。主因：Junior 定位、偏營運／BD、學位或領域硬條件。

## 跨模型重複缺口（改履歷的方向）
1. 工具未寫：Jira／Confluence／敏捷框架（6 份以上）。是否用過由本人確認，用過才補。
2. 垂直領域轉譯：支付／證券／資安等規則面經驗只到 CodaPay、Peach（2016–2021），近年案例集中 B2B 招募。
3. 資料分析深度：只寫 Google Sheets／Excel；SQL 不寫（本人不會）。
4. 英文商務能力：有分數與跨國協作，缺英文會議／簡報的直接證據。
5. 對外客戶責任：直接面對客戶的訪談與決策權較少呈現。

原始資料：`runs/2026-10-19-v10.4-f14-opus/`、`runs/2026-10-19-v10.4-l44-opus/report.md`、`runs/2026-10-19-v10.4-chatgpt/{report-chatgpt.md,light.md}`。
