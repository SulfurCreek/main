# HR集合體｜入口與角色索引

建立：2026-11-03（Asia/Taipei）。
**主 HR 的任務：每輪先讓全新陌生讀者通篇理解並轉述，再分開判斷訊息傳達與面談推薦；有指定 JD 時另做適配。**
角色為模擬招聘視角，不宣稱與這些公司HR有真實交情或掌握內部標準。

## 審查責任入口（2026-11-04更新）

- [審查者治理](../REVIEWER_GOVERNANCE.md)：主HR／persona審查與上游訪談分工。
- [交其他AI的訪談指令](UPSTREAM_INTERVIEW_REQUEST.md)：19萬筆、Agent／skill與結案率期間三項待釐清。
- 近期R07–R15沒有實際派persona，屬主審閱讀／版本比較；不能稱已完成集合審查。正式後續審查依治理實際派發並記結果；本次僅治理維護。

## 現行預設：陌生全文理解（2026-11-06）

每輪含新版複審，都新派不繼承對話的讀者（fork_turns=none），先完整逐段白話轉述，主審最後才做歷史比較。派發及報告使用 [READER_PROMPT.md](READER_PROMPT.md)，不以只列缺口、三亮點或整體值得面談代替理解結果。下面 persona 卡與歷史 runs 只供主審準備／追溯，不能整卡或連本 INDEX 交陌生代理；候選專屬推薦／疑慮不派發，只抽中性招聘身分、完整 JD 及必要公開公司背景。歷史紀錄不表示新預設當時已執行。

## 從這裡開始

1. [PROTOCOL.md](PROTOCOL.md)：單人、領域集合、全體、協助式與隔離審讀，以及草稿/PDF規則。
2. [STATUS.md](STATUS.md)：136個來源職缺逐筆納入/排除原因。
3. [COMPANIES.md](COMPANIES.md)：46家公司公開背景原文及職缺關聯。
4. 下方選擇HR-code，開對應領域文件，完整讀該卡與全文JD；各卡均附固定來源commit及公司ID。

有效角色82個、46家公司、10領域。舊63筆清單已由較新137筆同步與投遞/放棄紀錄交叉核對。只在repo快照意義上標記未應徵，不宣稱即時狀態。
初次建置僅建角色；2026-11-03已完成[r6診斷](runs/2026-11-03-585ee01/REPORT.md)，含獨立評閱與主HR閱讀（非正式成品盲審），未驗PDF。

## 使用方式

- 「派HR-8692h看這份草稿」：支付連專屬招聘視角。
- 「派HR-93shv看這份英文履歷」：SHOPLINE Data Product Manager視角，不混用Checkout。
- 「支付組一起看」：PAY領域全部有效角色，逐職缺保留結論。
- 「全部集合看」：82角色逐職缺審視，再由主HR整合共通強項與版本差異；不是用平均分或模擬多數票決定。
- 每輪預設「陌生全文理解」：隔離代理只讀完整對外候選＋必要 JD／公開公司資料，不給整卡、預期優點、過往評論或修改清單；不必等本人另說盲讀。
- 指定PDF時需實際讀檔及看頁面；僅MD不可宣稱版面驗收。

若使用者點名的公司/職缺不在有效池，先查STATUS，說明已投/關閉/放棄/未確認；未經要求不自動復活。
綠界95whq、SHOPLINE Checkout962f7在新快照為apply；Pi錢包91sgi為off，故不在預設集合。這不是忘記原PM線，而是狀態更新。

## 角色分組

| 領域 | 數量 | 文件 |
| --- | ---: | --- |
| PAY 支付、金融與合作串接 | 11 | [PAY.md](personas/PAY.md) |
| COMMERCE 電商、商家與平台產品 | 8 | [COMMERCE.md](personas/COMMERCE.md) |
| ENTERPRISE 企業系統、產品整合與複雜規則 | 8 | [ENTERPRISE.md](personas/ENTERPRISE.md) |
| CONSUMER 消費產品、訂閱與成長 | 11 | [CONSUMER.md](personas/CONSUMER.md) |
| AI AI產品、導入與組織推動 | 7 | [AI.md](personas/AI.md)＋[HR-94wfd](personas/HR-94wfd.md) |
| DATA 數據產品、行為分析與商業洞察 | 3 | [DATA.md](personas/DATA.md) |
| DELIVERY 軟體專案、客戶交付與顧問協作 | 10 | [DELIVERY.md](personas/DELIVERY.md) |
| SOLUTION 雲端、資安、電信與解決方案經營 | 10 | [SOLUTION.md](personas/SOLUTION.md) |
| HARDWARE 硬體、製造與供應鏈 | 12 | [HARDWARE.md](personas/HARDWARE.md) |
| OPERATIONS 營運企劃與商品管理 | 2 | [OPERATIONS.md](personas/OPERATIONS.md) |

## 82個角色完整索引（最新狀態與職責欄）

新增欄位來源：原jobs.json的`resume_review`，完整137筆見[JOB_TRACKS](JOB_TRACKS.md)。狀態取09a7c235快照；舊角色卡內舊擷取狀態以本表/新清單為準。非PM職缺仍保留角色，未混稱PM。

| HR ID | 公司 | 職缺 | track | pm_line | v13_fit | 卡片 |
| --- | --- | --- | --- | --- | --- | --- |
| HR-96686 | 台灣大哥大股份有限公司 | I210 AI專案PM(可遠端工作) | PM_PO | conditional | partial | [AI](personas/AI.md#hr-96686) |
| HR-5jvck | 三竹資訊股份有限公司 | APP應用事業群 - Project Manager | PROJECT | no | not_target | [DELIVERY](personas/DELIVERY.md#hr-5jvck) |
| HR-5n0va | Inventec_英業達股份有限公司 | 軟體專案經理(SEPM)(士林) | HARDWARE | no | not_target | [HARDWARE](personas/HARDWARE.md#hr-5n0va) |
| HR-5ya5p | 三竹資訊股份有限公司 | 金融服務事業群 - 證券產品經理 | PM_PO | yes | primary | [CONSUMER](personas/CONSUMER.md#hr-5ya5p) |
| HR-6ilwb | 台灣固網股份有限公司 | D50 固網產品PM | PM | no | not_target | [SOLUTION](personas/SOLUTION.md#hr-6ilwb) |
| HR-6k2q4 | 台灣大哥大股份有限公司 | D467 用戶行為分析人員 (可遠端工作) | DATA_ANALYST | no | not_target | [DATA](personas/DATA.md#hr-6k2q4) |
| HR-6ujxk | PressPlay_瑞奧股份有限公司 | 【知識】產品設計部｜產品經理 Product Manager | PM | yes | primary | [CONSUMER](personas/CONSUMER.md#hr-6ujxk) |
| HR-75rkw | 和泰聯網股份有限公司 | 【yoxi】APP產品經理 | PM | yes | primary | [CONSUMER](personas/CONSUMER.md#hr-75rkw) |
| HR-77jpv | 玉山銀行_玉山商業銀行股份有限公司 | 【數位金融】數位平台企劃-Web/APP Product Manager(經驗行員) | PM_PO | yes | primary | [PAY](personas/PAY.md#hr-77jpv) |
| HR-78em2 | 桓竑智聯股份有限公司 | 專案經理（Project Manager） | PROJECT | no | not_target | [DELIVERY](personas/DELIVERY.md#hr-78em2) |
| HR-7996v | 全支付電子支付股份有限公司 | 全支付- Product Manager (專案執行) | PO | conditional | primary | [PAY](personas/PAY.md#hr-7996v) |
| HR-7dijs | 玩美移動股份有限公司 | APP Product Manager 產品經理 | PM | yes | primary | [CONSUMER](personas/CONSUMER.md#hr-7dijs) |
| HR-7ig7x | 新加坡商蝦皮娛樂電商有限公司台灣分公司 | Product Manager 產品經理／蝦皮店到店 | PO | conditional | partial | [COMMERCE](personas/COMMERCE.md#hr-7ig7x) |
| HR-7p3v5 | 宏碁雲架構服務股份有限公司 | 雲端產品經理PM | SOLUTION | conditional | partial | [SOLUTION](personas/SOLUTION.md#hr-7p3v5) |
| HR-7ppuh | 口袋證券股份有限公司 | 軟體產品經理 | PM | yes | primary | [CONSUMER](personas/CONSUMER.md#hr-7ppuh) |
| HR-7rk75 | Inventec_英業達股份有限公司 | 【電競事業部】軟體專案經理(SEPM)(士林) | HARDWARE | no | not_target | [HARDWARE](personas/HARDWARE.md#hr-7rk75) |
| HR-7uqbx | 核果智能科技股份有限公司 | 資深軟體專案經理｜ Senior PM | PROJECT | no | not_target | [DELIVERY](personas/DELIVERY.md#hr-7uqbx) |
| HR-7wq7q | 台灣大哥大股份有限公司 | D597 產品專案PM | PO | conditional | partial | [DELIVERY](personas/DELIVERY.md#hr-7wq7q) |
| HR-81bhg | iRent_和雲行動服務股份有限公司 | iRent營運企劃（產品經理） (企劃部) | OPERATIONS | conditional | partial | [OPERATIONS](personas/OPERATIONS.md#hr-81bhg) |
| HR-81x5r | 台灣大哥大股份有限公司 | D464 行動裝置周邊配件產品PM(可遠端上班) | OPERATIONS | no | not_target | [OPERATIONS](personas/OPERATIONS.md#hr-81x5r) |
| HR-82gqm | 台灣固網股份有限公司 | D53 IDC產品PM (可遠端工作) | PM | conditional | partial | [SOLUTION](personas/SOLUTION.md#hr-82gqm) |
| HR-84s1l | 訊連科技股份有限公司 | SaaS Product Manager | PM | yes | primary | [AI](personas/AI.md#hr-84s1l) |
| HR-8692h | 拍付國際資訊股份有限公司 | 產品經理(支付連) | PM | yes | primary | [PAY](personas/PAY.md#hr-8692h) |
| HR-86svk | 三竹資訊股份有限公司 | 軟體產品經理 - 雲端事業群 \| CoLine | PM | yes | primary | [ENTERPRISE](personas/ENTERPRISE.md#hr-86svk) |
| HR-8bymx | 悠勢科技股份有限公司 | 資深產品經理｜Senior Product Manager | PM_PO | yes | primary | [ENTERPRISE](personas/ENTERPRISE.md#hr-8bymx) |
| HR-8c9o0 | Cooler Master_訊凱國際股份有限公司 | 專案經理 Project Manager | OPERATIONS | no | not_target | [HARDWARE](personas/HARDWARE.md#hr-8c9o0) |
| HR-8cb9c | 台灣理光股份有限公司 | 智能辦公解決方案 產品經理(Jr./Sr.) | SOLUTION | no | not_target | [SOLUTION](personas/SOLUTION.md#hr-8cb9c) |
| HR-8cfb8 | 行動力國際股份有限公司 | 專案經理PM | HARDWARE | no | not_target | [HARDWARE](personas/HARDWARE.md#hr-8cfb8) |
| HR-8dbp3 | 91APP_英屬開曼群島商九一應用軟體股份有限公司台灣分公司 | ［UPD］SaaS 產品經理 / Product Owner (Commerce Cloud, G11N, OMO) | PM_PO | yes | primary | [COMMERCE](personas/COMMERCE.md#hr-8dbp3) |
| HR-8f25l | 新加坡商蝦皮娛樂電商有限公司台灣分公司 | Product Manager 產品管理師  / Product Management 產品管理部 | PO | conditional | partial | [COMMERCE](personas/COMMERCE.md#hr-8f25l) |
| HR-8geon | 三竹資訊股份有限公司 | 金融服務事業群-PM | PROJECT | conditional | partial | [DELIVERY](personas/DELIVERY.md#hr-8geon) |
| HR-8ick4 | 新加坡商蝦皮娛樂電商有限公司台灣分公司 | Shopee - B2C System Product Manager 產品經理 | PO | conditional | partial | [ENTERPRISE](personas/ENTERPRISE.md#hr-8ick4) |
| HR-8mpjw | LINE Pay_連加網路商業股份有限公司 | Technical Product Manager | PO | conditional | partial | [PAY](personas/PAY.md#hr-8mpjw) |
| HR-8n0mx | GARMIN_台灣國際航電股份有限公司 | 【全球智慧製造】智慧製造系統產品經理 Smart Manufacturing System Product Manager_新店 | PO | conditional | not_target | [HARDWARE](personas/HARDWARE.md#hr-8n0mx) |
| HR-8nijy | NVIDIA_新加坡商輝達開發有限公司台灣分公司 | Server Product Program Manager | HARDWARE | no | not_target | [HARDWARE](personas/HARDWARE.md#hr-8nijy) |
| HR-8nuo3 | Eunodata_御諾資訊股份有限公司 | 軟體專案管理師 Software Project Manager (PM) | PROJECT | no | not_target | [DELIVERY](personas/DELIVERY.md#hr-8nuo3) |
| HR-8ocje | 全支付電子支付股份有限公司 | 全支付- Product Manager (內部系統、串接) | PO | conditional | partial | [PAY](personas/PAY.md#hr-8ocje) |
| HR-8olw0 | 統一集團_安源資訊股份有限公司 | 平台應用開發 Team－專案管理師 | PROJECT | no | not_target | [DELIVERY](personas/DELIVERY.md#hr-8olw0) |
| HR-8p4ix | Klook客路_客遊天下旅行社有限公司 | Project Manager (API) | OPERATIONS | no | not_target | [DELIVERY](personas/DELIVERY.md#hr-8p4ix) |
| HR-8ph3b | 台灣固網股份有限公司 | D68 雲端產品PM | SOLUTION | no | not_target | [SOLUTION](personas/SOLUTION.md#hr-8ph3b) |
| HR-8q2st | 光速未來有限公司 | 產品經理 Product Manager | PM_PO | yes | partial | [ENTERPRISE](personas/ENTERPRISE.md#hr-8q2st) |
| HR-8qd7h | 和泰聯網股份有限公司 | 【去趣】旅遊應用程式 產品經理 PM | PO | conditional | partial | [CONSUMER](personas/CONSUMER.md#hr-8qd7h) |
| HR-8rb54 | 台灣固網股份有限公司 | D80 資安產品PM | SOLUTION | conditional | partial | [SOLUTION](personas/SOLUTION.md#hr-8rb54) |
| HR-8rb81 | 台灣固網股份有限公司 | D81 企業AI PM | SOLUTION | conditional | partial | [SOLUTION](personas/SOLUTION.md#hr-8rb81) |
| HR-8rnz1 | 台灣固網股份有限公司 | D82 自研產品PM (可遠端工作) | PM | yes | primary | [SOLUTION](personas/SOLUTION.md#hr-8rnz1) |
| HR-8s2o0 | 台灣大哥大股份有限公司 | D637 金流產品營運PM | OPERATIONS | conditional | partial | [PAY](personas/PAY.md#hr-8s2o0) |
| HR-8v53h | 台灣大哥大股份有限公司 | 虛擬資產交易所產品PM | PM | yes | partial | [PAY](personas/PAY.md#hr-8v53h) |
| HR-8vt92 | ADAM elements International Co., Ltd._亞果元素國際股份有限公司 | 產品專案管理師 Product Project Specialist | HARDWARE | no | not_target | [HARDWARE](personas/HARDWARE.md#hr-8vt92) |
| HR-8vymg | 技嘉科技股份有限公司 | Software PM_3225 | PM_PO | conditional | partial | [HARDWARE](personas/HARDWARE.md#hr-8vymg) |
| HR-8wezw | 104人力銀行_一零四資訊科技股份有限公司 | 資深產品經理 (打工與兼職服務) ★預計2027年中搬遷至松山站共構大樓★ | PM | yes | primary | [CONSUMER](personas/CONSUMER.md#hr-8wezw) |
| HR-8wzup | 刻刻在雲股份有限公司 | 【Going Cloud】Project Manager | PROJECT | no | not_target | [DELIVERY](personas/DELIVERY.md#hr-8wzup) |
| HR-8xcyw | 美商超微半導體股份有限公司台灣分公司 | Production Planner & Controller (Hsinchu) | OPERATIONS | no | not_target | [HARDWARE](personas/HARDWARE.md#hr-8xcyw) |
| HR-8y7n8 | 91APP_英屬開曼群島商九一應用軟體股份有限公司台灣分公司 | ［UPD］金流產品經理 Product Owner - Payment Service | PM_PO | yes | primary | [PAY](personas/PAY.md#hr-8y7n8) |
| HR-8zacy | 台灣大哥大股份有限公司 | I110 AI 產品經理(可遠端工作) | PM | conditional | partial | [AI](personas/AI.md#hr-8zacy) |
| HR-91bo9 | 易遊網旅行社股份有限公司 | F09T-產品經理(Product Manager/PM) | PM | yes | primary | [CONSUMER](personas/CONSUMER.md#hr-91bo9) |
| HR-91ddn | 台灣大哥大股份有限公司 | 數據服務與金流PM | PO | conditional | partial | [PAY](personas/PAY.md#hr-91ddn) |
| HR-923em | 和碩集團_和碩聯合科技股份有限公司 | Product Manager (PM)_15742 | HARDWARE | no | not_target | [HARDWARE](personas/HARDWARE.md#hr-923em) |
| HR-93shv | SHOPLINE Technology Corp., Ltd._商線科技股份有限公司 | 【TPD0603】Data Product Manager 數據產品經理 | PM | yes | primary | [DATA](personas/DATA.md#hr-93shv) |
| HR-93vx9 | 三竹資訊股份有限公司 | 創新產品部-行動廣告系統產品經理（Product Manager） | PM_PO | yes | primary | [DATA](personas/DATA.md#hr-93vx9) |
| HR-943rr | 台灣固網股份有限公司 | D86 國際專案管理師 | SOLUTION | no | not_target | [SOLUTION](personas/SOLUTION.md#hr-943rr) |
| HR-94bt1 | 遠傳電信股份有限公司 | C0631 行動支付產品PM | SOLUTION | conditional | partial | [PAY](personas/PAY.md#hr-94bt1) |
| HR-94fod | QuickClick快一點_點點全球股份有限公司 | 【PMC】軟體產品經理 ( Product Manager / Technical Program Manager) | PM_PO | yes | primary | [ENTERPRISE](personas/ENTERPRISE.md#hr-94fod) |
| HR-94h37 | 口袋證券股份有限公司 | 行銷產品經理（Marketing Product Manager） | PM | yes | primary | [CONSUMER](personas/CONSUMER.md#hr-94h37) |
| HR-94hek | 訊連科技股份有限公司 | AI Product Manager | PM_PO | yes | primary | [AI](personas/AI.md#hr-94hek) |
| HR-94lbz | 台灣大哥大股份有限公司 | D440 MyVideo 影音產品PM(可遠端工作) | PM | yes | primary | [CONSUMER](personas/CONSUMER.md#hr-94lbz) |
| HR-94le0 | 台灣大哥大股份有限公司 | D441 MyVideo影音產品Growth PM(可遠端工作) | PM | yes | primary | [CONSUMER](personas/CONSUMER.md#hr-94le0) |
| HR-94n8b | 104人力銀行_一零四資訊科技股份有限公司 | 產品專案經理(內部系統) ★預計2027年中搬遷至松山站共構大樓★ | PO | conditional | partial | [ENTERPRISE](personas/ENTERPRISE.md#hr-94n8b) |
| HR-94roa | SHOPLINE Technology Corp., Ltd._商線科技股份有限公司 | 【TPD0402】Product Manager | PM | yes | primary | [COMMERCE](personas/COMMERCE.md#hr-94roa) |
| HR-94wfd | 台灣大哥大股份有限公司 | D661 AI產品暨商務發展管理PM | PM | yes | primary | [AI](personas/HR-94wfd.md) |
| HR-94ywa | 富邦媒體科技股份有限公司(富邦momo) | BA1000【多領域招募】產品經理/Product Manager | PM_PO | yes | primary | [COMMERCE](personas/COMMERCE.md#hr-94ywa) |
| HR-94zew | 台灣固網股份有限公司 | D87 ICT產品PM | SOLUTION | conditional | partial | [SOLUTION](personas/SOLUTION.md#hr-94zew) |
| HR-950oe | Gogolook_走著瞧股份有限公司 | Senior Product Manager (Anti-Scam BU/2B) | PM_PO | yes | primary | [DELIVERY](personas/DELIVERY.md#hr-950oe) |
| HR-95aew | 技鋼科技股份有限公司_技嘉集團 | 1086_跨平台產品整合(PM/Solution Owner) | PM_PO | yes | partial | [ENTERPRISE](personas/ENTERPRISE.md#hr-95aew) |
| HR-95mvt | 悠勢科技股份有限公司 | 產品經理｜Product Manager | PM_PO | yes | primary | [ENTERPRISE](personas/ENTERPRISE.md#hr-95mvt) |
| HR-95q16 | 旭隼科技股份有限公司 | 產品管理師 Product Manager | HARDWARE | no | not_target | [HARDWARE](personas/HARDWARE.md#hr-95q16) |
| HR-95q7h | 買即可全球電商有限公司 | 產品經理 | PM_PO | yes | primary | [COMMERCE](personas/COMMERCE.md#hr-95q7h) |
| HR-95te1 | 和碩集團_和碩聯合科技股份有限公司 | 軟體專案管理師_16284 | HARDWARE | no | not_target | [HARDWARE](personas/HARDWARE.md#hr-95te1) |
| HR-95zyw | 玩美移動股份有限公司 | Saas Product Manager | PM | yes | primary | [COMMERCE](personas/COMMERCE.md#hr-95zyw) |
| HR-963h3 | LINE Pay_連加網路商業股份有限公司 | Technical Partner Solution Specialist(EPI) | SOLUTION | no | not_target | [PAY](personas/PAY.md#hr-963h3) |
| HR-9667l | 台灣大哥大股份有限公司 | I210 AI資安PM(可遠端工作) | PM_PO | conditional | partial | [AI](personas/AI.md#hr-9667l) |
| HR-9686i | 十論科技股份有限公司 | B2B PM AI顧問｜ B2B PM, AI Consultant | SOLUTION | conditional | partial | [AI](personas/AI.md#hr-9686i) |
| HR-968yx | Studio Doe_朵墨股份有限公司 | 【Studio Doe】產品經理 Product Manager - Commerce & Operations | PM_PO | yes | primary | [COMMERCE](personas/COMMERCE.md#hr-968yx) |

## 來源固定版本

- JD/公司：automation/104-data，365896782ff60868ec48d974b37a3d555622477e，career/targets/104/jobs.json與companies.json。
- 狀態交叉：Claude分支8e1a40864c42b0ae3064d164bd307bca7bd9bb03的applications及批次紀錄。
- 原稿評論歷史：codex/resume-writer的career/drafts/codex/v13-review-journal/INDEX.md。此角色包不是事實庫或本人履歷來源。

## 持久化與接續

本人已於本聊天室明確同意公開並要求push。repo位置：career/drafts/codex/hr-personas/，分支codex/resume-writer。不修改Claude上游。
Claude可把本INDEX路徑加入其ROUTER；既有日誌索引另設本入口。
每次審稿與狀態變更依PROTOCOL追加紀錄，不只依賴聊天記憶。


## 最新：r6 PM職缺分類與招聘診斷

- [137筆責任線＋33筆未投PM](JOB_TRACKS.md)
- [新增resume_review欄位／housekeeper指令](HOUSEKEEPER.md)
- [585ee01用人主管診斷](runs/2026-11-03-585ee01/REPORT.md)
- [原稿完整快照](runs/2026-11-03-585ee01/SOURCE.md)

新增94wfd後共82有效角色；原81角色歷史、原始STATUS快照保留，不假裝當時就有82個。

## R17｜最新104 Markdown：五位persona完整審查

2026-11-04實際派發與完成，2026-11-05補齊先前GitHub故障未同步的報告。
[完整入口](runs/2026-11-04-216445b9-104/INDEX.md)｜[整合報告](runs/2026-11-04-216445b9-104/REPORT.md)｜[上游需求](runs/2026-11-04-216445b9-104/UPSTREAM.md)。入口含五份原始全文，來源固定216445b97d7aa282c4f4c0b47229c54fe496adb1的career/02_codex_stage/104-v14.md。支付連、91APP與訊連值得邀約；PressPlay先釐清行為分析、SHOPLINE Data先釐清數據產品責任。共通資料處理、Agent術語與統計口徑仍交上游，不等於已核實。協助式、非隔離盲審，未改履歷或驗PDF。

## R18｜2026-11-05 v14.9正式複審（最新）

固定候選d28332e41dbc7fc73ae4408eb651345f950c6e36，career/drafts/v14.9/104-v14.9.md。五位實際子代理完成全文複審：[完整入口](runs/2026-11-05-d28332e-v14.9/INDEX.md)｜[主審報告](runs/2026-11-05-d28332e-v14.9/REPORT.md)｜[Fact Gatherer／Marketer／Writer分工指令](runs/2026-11-05-d28332e-v14.9/UPSTREAM.md)。
結論：仍有可推薦的商業／企業Senior PM能力；P1部分解，P2舊常駐／14／23已解但驗證／團隊範圍未確認，P3新季度與52→79對應未解。首句與2.1順序有效；3.1不因廣度判灌水，但不能以流程清單當成熟導入。本輪不重開職缺專屬缺口，不訪談本人、不改稿、不驗新PDF。協助式非隔離盲審，五份原始報告已保存repo。接續見career/drafts/codex/session-state/hr-subagent.md。

## R19｜2026-11-05 v15 native正式審查（最新）

固定候選d4299ef739b2f60b8efff3a31ae9216e7255810d，career/02_codex_stage/104-v15-native.md；對照e056227fe8c5b8aa86af03052b6f59465ff99eaa的career/drafts/v15/104-v15.md與notes。五位實際子代理均完成全文審查：[完整入口](runs/2026-11-05-d4299ef-v15-native/INDEX.md)｜[報告](runs/2026-11-05-d4299ef-v15-native/REPORT.md)｜[分工交接](runs/2026-11-05-d4299ef-v15-native/UPSTREAM.md)。
結論：保留native候選，自然化有實際增益，Senior與推薦力保住；Writer局部處理迭代變討論及規則設計主體。底稿已補明全量比對／本人把關測試環境／兩名企劃採用，不再沿R18重問。P3季度與52→79仍是既有未決，FG單獨接續，不歸咎本輪Writer擅改，不以無新增疑問宣告舊問題已解。未改履歷、未訪談本人、未跑驗證器／PDF。原JD專屬缺口本輪不重評。

## R20｜2026-11-05完整資訊重寫：共通內容可收斂（最新）

固定候選516842e576467b94fede1be1c31489e646381cb2，career/02_codex_stage/104-v15-native.md；資訊底稿8650da8aeca9acb6e263a1b61e8f7d04a2a19eff的career/drafts/v14.10/104-v14.10.md。五位實際子代理均完成全文審查：[完整入口](runs/2026-11-05-516842e-v15-full/INDEX.md)｜[整合報告](runs/2026-11-05-516842e-v15-full/REPORT.md)｜[上游結案交接](runs/2026-11-05-516842e-v15-full/UPSTREAM.md)。
五項回補均可見；最新FG來源確認月份52.4%／78.9%，候選恢復相同月份52%→79%，舊季度問題結案，不用舊10/04反覆索證。AI修正值／測試環境／兩名企劃範圍及R19規則本人作用、反覆修正均已處理。無新增必訪談或全篇改寫需求，可保留候選。小修僅非阻擋建議，原JD專屬適配不重評。未改履歷、未訪談本人、未跑驗證器／PDF；不冒稱獨立核算原始資料。歷史R18／R19當時未決保留，新來源在R20使其收斂。


## R21｜2026-11-06 完整PM v1.1（最新）

固定候選cf5e43749e0075398d5e72956d5417fed12df8ad，career/02_codex_stage/104-PM-v1.1.md；完整上游ad68d632cc1fc95f449747b72f4d1be7d01302ec，career/drafts/PM-v1.1/104-PM-v1.1.md。五位實際persona完成全文協助式審讀，非隔離盲審：[完整入口](runs/2026-11-06-cf5e437-PM-v1.1/INDEX.md)｜[主審報告](runs/2026-11-06-cf5e437-PM-v1.1/REPORT.md)｜[上游分工](runs/2026-11-06-cf5e437-PM-v1.1/UPSTREAM.md)。
結論：Senior與promote／vouch成立，可推薦商業／訂閱PM、複雜企業PM／PO。支付連、91APP、訊連、PressPlay值得邀約；SHOPLINE Data值得適配初談，未冒稱直接數據產品線經驗。PressPlay已看見首購／續訂／LTV證據，不套舊版缺口。無新增FG必訪談或全篇重寫需求；743件短標權重與AI閱讀節奏為非阻擋。季度依本人11/06裁定保留52→79，不revert、不重算、不冒稱獨立核算。未改履歷、訪談本人、跑驗證器或驗PDF。完整原稿與五份原始報告均已保存。


## R22｜2026-11-06 PM v1.2當事人敘事版（最新）

固定候選a79ca79a9f89152845fa479402b41afa268c7106，career/02_codex_stage/104-PM-v1.2-owner.md；上游9c038f53b5c7607e43ae1a1281c88220a96c48a4，career/drafts/PM-v1.2/104-PM-v1.2.md。[完整入口](runs/2026-11-06-a79ca79-PM-v1.2-owner/INDEX.md)｜[主審全文](runs/2026-11-06-a79ca79-PM-v1.2-owner/REPORT.md)｜[上游結案交接](runs/2026-11-06-a79ca79-PM-v1.2-owner/UPSTREAM.md)。
支付連、91APP、訊連三個實際persona均完成全文、值得邀約；未另派PPA／SHOPLINE，不宣稱五位重跑。R21的743標題權重及AI層次已處理；自然省略主詞未削弱本人判斷／Senior／promote-vouch。無新增FG或寫手必辦，可收斂。季度裁定保留，不revert、不重算；未改履歷、訪談本人、跑驗證器或驗PDF。自動審核拒絕重複上傳完整履歷快照，未重試全文；SOURCE僅連結既有固定原稿，報告與三份原始審讀均已保存。


## 2026-11-06｜fab9bcf v1.6：陌生HR全文理解審讀（最新）

固定fab9bcf8d131a5eda157d5006c7f3596ad4a35d3，career/02_codex_stage/104-PM-v1.6-refined.md。[主審全文](runs/2026-11-06-fab9bcf-v1.6-reader/REPORT.md)｜[三份原始全文與方法](runs/2026-11-06-fab9bcf-v1.6-reader/INDEX.md)。本人要求只懂通用產品/專案/業界詞、沒有個案背景，更嚴格重讀。三個新代理fork_turns=none，只讀完整對外正文，未給歷史評論/修改清單/治理，先獨立完成再整合。
整體自然可讀，不是專案名普遍缺介紹；優先Writer處理AI不同推薦功能關係、非續訂營收稱呼、199件合併建議修飾，另留七市場工作範圍的局部歧義。skill及資料狀態重要性各代理不同，不冒稱全體共識。已修簡介/訊息工具句及自傳末段不重退稿。既有AI/營收/季度已確認事實不因隔離代理未知而重開訪談；不把證據強弱混成生硬。無改稿/本人訪談/數據重算/新PDF驗收。三份原始報告、主審採納及未採理由均保存；完整履歷未重複上傳。


## 2026-11-06｜37f9183 v1.8：陌生HR全文複審（最新）

本人指定37f9183e3219fa1db85a9e7afdb9c7c6445cde9f，career/02_codex_stage/104-PM-v1.8.md；完整讀正文/notes及d7d407cc8a4e6fb7096ce8ecb9326c95f0547d2f上游/填表指令，現行角色治理已讀且blob相同。[主審全文](runs/2026-11-06-37f9183-v1.8-reader/REPORT.md)｜[三份獨立原文入口](runs/2026-11-06-37f9183-v1.8-reader/INDEX.md)｜[上游需求](runs/2026-11-06-37f9183-v1.8-reader/UPSTREAM.md)。
三新代理fork_turns=none，只讀去內部註解完整正文、無個案背景，全部完成；非JD匹配或新PDF驗收。前輪四個優先問題已解：推薦類別/人才分工、非續訂（單次購買）、199件要求合併工具、SweetRing市場範圍；合規限定兩項文字生成。代碼表補維護重整與底層欄位，但三位仍不知對照兩端/產物用途，故僅部分解決，局部中等不阻擋投遞。Writer先用既有資料說清，真的缺再交FG有限釐清，不重問整案。填表指令標題/唯一來源仍v1.7已實讀確認，交Marketer修版本指向。無擅改履歷/訪談本人/驗證器/ATS或填表。


## 2026-11-06｜81cffb2 v1.11：逐句逐段、以實際轉述驗收（最新）

固定81cffb2dcc0400e118a1c9ba0f4bffa726ccb64f，career/02_codex_stage/104-PM-v1.11.md。[主審對照](runs/2026-11-06-81cffb2-v1.11-comprehension/REPORT.md)｜[原始轉述與全篇覆蓋](runs/2026-11-06-81cffb2-v1.11-comprehension/INDEX.md)｜[主審每段紀錄](runs/2026-11-06-81cffb2-v1.11-comprehension/MAIN-COVERAGE.md)｜[上游交接](runs/2026-11-06-81cffb2-v1.11-comprehension/UPSTREAM.md)。三個新代理fork_turns=none、無對話/作者背景，只讀候選正文，先白話介紹/聘用理由再重建各案。本人再強調每句每段後，三位按原順序補全篇各段理解，無問題段也列。主審已讀三份原始全文與三份覆蓋補錄，未只核對問題句。
核心情境/本人判斷/分工/用途實際傳達成立：分類與15表可被解釋成修復刊登、履歷及搜尋配對的共同分類，再以新舊及顯示次序對照供工程更新，不只是資料量。搜尋分析與轉換成立，但正式上線訊息未建立；再行銷增量未建立。句內也保留C對手測範圍詞及API安全細節只理解部分，不以整體可讀抵銷。交Writer有限用途橋梁，無新增FG必訪談、不全篇重寫。
REVIEWER_GOVERNANCE已依本人校正新增全篇覆蓋與實際轉述驗收（3eb422b391325a318fbf07c06f3a0b33b85033a1），無法理解即該訊息傳達失敗；不恢復自動驗證器或分數。不改履歷/不訪談本人/未驗PDF或六秒真人掃讀/未填表，原稿未重複公開。
