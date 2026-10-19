<!--markdownlint-disable MD013-->

# 履歷驗證套件 v10.8｜分流版（63 份職缺）

> 產生日：2026-10-19｜規準：rubric 4.2（F 完整）＋ L1（輕量）｜職缺來源：`career/targets/jobs.md`
> 這個資料夾的每個 `F-*.md`、`L-*.md` 都是**一次呼叫的完整封包**（規則＋履歷＋職缺），整份貼進一個新對話即可，不需要其他檔案。

## 1. 為什麼這樣分（省 token 的設計）

| 手段 | 做法 | 省多少 |
| :-- | :-- | :-- |
| 分流只做一次 | 職缺分層（`jd/routing.tsv`）由 Claude 依職缺內容決定，跟履歷版本無關；之後換版本直接沿用 | 每版省掉 63 次分類 |
| 分三層 | **F 完整審查** 14 份（核心面板＋新類型代表）／**L 輕量對位** 44 份（5 批）／**X 略過** 5 份（非 PM 或明顯不符，只列原因） | 63 次完整審查 → 19 次呼叫 |
| 輕量層批次化 | L 層同類職缺 6–10 份一批，履歷與規則每批只讀一次；只輸出條件對位 JSON | L 層每份約為 F 的 1/10 |
| 輸出去重 | F 層只交 JSON＋審查者質疑＋評語；表格由 Claude 用腳本從 JSON 產生 | F 層輸出約少一半 |
| ATS 移到本機 | PDF 抽字、讀序由 Claude 用 `parse_check.py` 本機跑，不交給外部模型 | 每次呼叫少一段 ATS 規則 |
| 依模型分工 | 見 §3：Opus 跑 F 全部；外部模型只跑 L 與 5 份錨點校準 | 你手動跑的次數由 30 次降到 10 次 |
| 依改動決定重跑範圍 | 見 §4：只改自傳就只跑錨點，不必全跑 | 小改版省 80% 以上 |
| 自動升級 | L 層標 `escalate:true` 的職缺（最多 4 份）才補跑 F 完整審查 | 只把深度花在值得的職缺 |

## 2. 呼叫清單

### 2.1 F 層：完整審查（每份一個新對話）

| 封包 | 職缺 | 公司 | 群組 | 錨點 |
| :-- | :-- | :-- | :-- | :-: |
| `F-8kebd.md` | AI Product Manager / Technical PM 產品經理(電商/餐飲Saas) | 台鋼新零售 | AI | ★ |
| `F-91sgi.md` | 產品經理 (Pi錢包) | 拍付國際資訊 | 支付 |  |
| `F-82slf.md` | 產品經理 Product Manager | 微拓科技 | B2B SaaS |  |
| `F-8o3s3.md` | 【北士科】Product Manager | 沛思坦網路 | B2B SaaS |  |
| `F-94le0.md` | D441 MyVideo影音產品Growth PM(可遠端工作) | 台灣大哥大 | 消費成長 | ★ |
| `F-950oe.md` | Senior Product Manager (Anti-Scam BU/2B) | Gogolook | B2B SaaS | ★ |
| `F-8bymx.md` | 資深產品經理｜Senior Product Manager | 悠勢科技 | B2B SaaS |  |
| `F-92io8.md` | 資深產品經理【擴編】 | 人易科技 | B2B SaaS | ★ |
| `F-94n8b.md` | 產品專案經理(內部系統) ★預計2027年中搬遷至松山站共構大樓★ | 104人力銀行 | B2B SaaS |  |
| `F-8dbp3.md` | ［UPD］SaaS 產品經理 / Product Owner (Commerce Cloud, G11N, OMO) | 91APP | B2B SaaS |  |
| `F-8ocje.md` | 全支付- Product Manager (內部系統、串接) | 全支付電子支付 | 支付 | ★ |
| `F-94fod.md` | 【PMC】軟體產品經理 ( Product Manager / Technical Program Manager) | QuickClick快一點 | B2B SaaS |  |
| `F-95jyg.md` | Product Manager (Messenger & OA Products) | LINE Taiwan | 消費成長 |  |
| `F-93qa8.md` | [Music] Senior Product Planner | 新加坡商科科科技台灣分公司 | 消費成長 |  |

### 2.2 L 層：輕量批次（每批一個新對話）

| 封包 | 群組 | 份數 | 職缺代碼 |
| :-- | :-- | :-: | :-- |
| `L-LA.md` | 支付與金流 | 9 | 8692h、95whq、8enwh、91ddn、8s2o0、7996v、94bt1、8f25l、8sxlq |
| `L-LB.md` | B2B SaaS 與系統平台 | 9 | 96qu1、91fp9、86svk、948j4、7ig7x、8ick4、8x7oe、95mvt、94roa |
| `L-LC.md` | 消費型 App、內容與成長 | 10 | 8bt4g、8qxbv、95zyw、7dijs、94h37、94lbz、95q7h、7ppuh、95asb、75rkw |
| `L-LD.md` | 專案型與垂直產業 | 10 | 6i88h、844j7、8p4ix、5ya5p、8geon、5jvck、8v53h、7wq7q、91bo9、8qd7h |
| `L-LE.md` | AI 與數位轉型 | 6 | 8yxgd、8n92e、96686、9667l、8zacy、94j0t |

### 2.3 X 層：不送審（理由）

| 職缺 | 公司 | 理由 |
| :-- | :-- | :-- |
| 專案管理_26072（8qos1） | 遊戲橘子數位科技 | 專案助理型行政＋需熱愛遊戲 |
| 【OwlPay】營運管理師 Sales & Operations Executive（92d3h） | 奧丁丁集團英屬開曼群島商台灣子公 | 客服與對帳營運 |
| D464 行動裝置周邊配件產品PM(可遠端上班)（81x5r） | 台灣大哥大 | 配件採購與進銷存 |
| D467 用戶行為分析人員 (可遠端工作)（6k2q4） | 台灣大哥大 | 資料分析師 |
| iRent營運企劃（產品經理） (企劃部)（81bhg） | iRent | 營運企劃，薪資帶 40–55k 與年資差距大 |

> 你覺得 X 層哪份其實想投，告訴 Claude 改成 L 或 F，`routing.tsv` 改一行即可。

## 3. 誰跑什麼（模型分工）

| 執行者 | 跑什麼 | 次數 | 備註 |
| :-- | :-- | :-: | :-- |
| Claude（Opus 子代理） | F 層全部 | 14 | 每份獨立 context；Claude 自己跑，你不用動手 |
| ChatGPT（你手動） | L 層全部批次＋F 層錨點 | 5＋5 | 錨點用來校準：和 Opus 的決定比對 |
| Gemini（選做） | 只在錨點有 ≥2 份決定與 Opus 不同時，跑同樣的錨點 | 0 或 5 | 用來判斷是哪一方偏離 |
| Claude | 升級補跑、彙整、本機 ATS 抽字 | — | 用 `multi_report.py`、`parse_check.py` |

**手動操作方式**：每個封包開一個新對話 → 整份貼上（或附加檔案）→ 送出 → 把回覆整段複製存成一個 md（例：`chatgpt-v10.4-raw.md`，多個回覆直接接在一起即可）→ 上傳給 Claude。**不需要請外部模型寫總報告**，彙整由 Claude 用腳本做。

## 4. 下一版要重跑多少（版本路由）

| 這版改了哪裡 | F 層 | L 層 | 外部錨點 |
| :-- | :-- | :-- | :-- |
| 經歷條列或摘要（事實、數字、論述） | 全跑 | 全跑 | 跑 |
| 只改技能欄、求職條件 | 只跑錨點 | 全跑 | 不跑 |
| 只改自傳 | 只跑錨點 | 不跑 | 不跑 |
| 只改排版／PDF | 不跑 | 不跑 | 不跑；只跑本機 ATS 抽字 |
| 職缺清單更新 | 新職缺先分流，只跑新增的 | 同左 | — |

## 5. 回傳後 Claude 會做什麼

1. 用 `schema_v4.py` 檢查 F 層 JSON、補跑格式失敗的份數（標 `technical_failure`，不刪）。
2. 錨點比對：外部模型與 Opus 的決定是否一致。
3. 處理 `escalate:true`：最多 4 份補跑 F。
4. 產出彙整報告：投遞優先清單（依 fit 與決定排序）、跨職缺重複缺口、共同質疑、錨點校準結果；寫入 `review-panel/HISTORY.md` 與 `opus-matrix.md`。
