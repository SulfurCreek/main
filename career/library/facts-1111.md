<!--markdownlint-disable MD013-->

# 1111 期間現行事實（2022/08–）

> 格式：`事實｜口徑／使用限制｜來源`。數字只取本頁；本頁沒有的數字不得出現在產出裡。對外版一律抽象化內部名稱（見 [decisions](decisions.md) §3）。

## 1. 角色與組織

| 事實 | 口徑／限制 | 來源 |
| :--- | :--- | :--- |
| 求才（企業端）招募系統的 Product Owner／PM，正式職稱「產品企劃主任」 | 職稱寫法見 [profile](profile.md) §1 | 2026-10-08 使用者確認｜`wiki/prior-roles.md` |
| 直接向副總匯報；經理不在匯報線上 | — | 2026-10-08 使用者確認 |
| 直屬管理 2 名企劃，委派工單給工程 | 對外不寫同事姓名 | `wiki/F08-roadmap-delivery.md` |
| 角色＝**規劃、協作、驗收、時程掌控**；不碰程式實作，但全盤掌握技術專案 | 寫法鐵則，見 [decisions](decisions.md) §1 | 2026-10-06 使用者確認｜`style/resume-voice-zh.md` §7 |
| 需求單一窗口，對接 16 個利害關係單位（高層到第一線客服） | — | `wiki/resume-extract.md`、F09 |
| 每週至少一次以簡報向全國客服、業務、主管說明新功能；簡報固定附 FAQ（借鑑 Amazon PR/FAQ 課程概念） | — | 2026-10-05 使用者補充｜`wiki/evidence-briefings.md`、F09 |
| Kick-off 簡報內嵌 Axure RP 互動原型，先讓客服與工程看過流程再封測 | 嵌入內容讀不到，以口述為準 | 2026-10-05 使用者確認｜F01 |
| 專案管理：Kanban 看板推進瀑布式開發；艾森豪矩陣排先後；主持 Daily Stand-up 與 Retrospective | **不是正式 Scrum**，不寫 Scrum；站會／回顧頻率〔待補〕 | 2026-10-05 使用者確認｜F08、`wiki/pm-vocabulary-map.md` #21 |
| 優先級制度定到 P0–P5，實際只用到 P3 → 履歷寫 P0–P3 | — | 2026-10-05 使用者確認｜F08 |

| 個人標準交付流程：User Journey Map、User Story、Use Case、SA、Flowchart／Sequence Diagram、Wireframe、與 UI/UX 協作、Prototype（Axure RP）、Stakeholder 匯報、Spec 文件、與工程跑專案追時程、與 QA 協作（由規格推導驗收案例）、上線計畫、完整交付 | 產出物可對外寫；份數〔待補〕 | **早已記錄於** `competency-framework.md`（User Story → Wireframe → 規格 → 交接）、F01、F02、F05、`wiki/resume-extract.md`、`104/resume-104.md` 專長；2026-10-08 使用者重申完整順序。library 重建時漏收 |

## 2. 交付與數字

| 事實 | 口徑／限制 | 來源 |
| :--- | :--- | :--- |
| 2023/12–2026/03 主導約 50 項功能上線 | 依上線時間軸截圖 | 2026-10-05 使用者提供｜`wiki/evidence-1111-launches.md` |
| 227 項 roadmap；近半年 111 項上線；有計畫／實際日期的 89 項中 84 項準時或提前（94%） | 「94%」的分母是 89，不是 111 | `wiki/resume-extract.md`、F08 |
| 維運工單：2026 年截至 9/29 累計 **1,857** 張、完成 1,726、處理率約 **93%** | 寫「截至 2026/09」；06/16 舊快照（1,279 張／約 88%）**作廢** | `wiki/evidence-weekly-reports.md`、F11 |
| 處理週期平均 100.4 → 30.9 天（2026 Q1→Q2，約 69%） | 前提：2025/11 一次性清倉積案後的穩態比較 | `wiki/resume-extract.md`、F11 |
| 工單管線覆蓋 **1,279 家**活躍付費廠商；年化留存 81.2% vs 全站 74.2%（+7pt，p=0.011） | ⚠️ 與上方「06/16 的 1,279 張工單」數字巧合、定義不同，**勿混用**；相關性非因果 | `wiki/evidence-paying-customers.md` |
| 全站活躍付費廠商約 **6.6 萬家**（2026/04/30：66,150） | 只當規模脈絡，不是個人成果 | `wiki/evidence-paying-customers.md` |
| 合約價值（NT$3 千萬量級、超額留存約 NT$55 萬） | 只在 wiki 內部分析；對外是否可寫〔待確認〕，目前履歷不用 | `wiki/evidence-paying-customers.md` |

## 3. 專案事實

| 專案 | 現行事實 | 來源 |
| :--- | :--- | :--- |
| 求才新版改版 | 前任主管規劃未落地，使用者**接手**並拆三階段；第一階段 2025/10 上線（登入、首頁、帳號、聯絡人、選單、公告、通知）；上線前請全國客服封測 | `wiki/evidence-1111-launches.md`、`wiki/evidence-briefings.md` |
| 求才新版上線方式 | **離峰切換、停機約 1.5 小時**（晚間停連線 → 內網測 → 20:00 開放）。**不可寫零停機** | 2026-10-05 使用者確認｜`wiki/evidence-briefings.md` |
| 舊系統相容 | 先盤點流程與髒資料；E-mail 登入時發現上千組重複 E-mail，決定首次登入引導確認、不強迫修改 | 2026-10-08 使用者口述｜`wiki/evidence-briefings.md`、v5.1 審查 |
| 第二階段：公司資料改版 | 2025/12 封測 | `wiki/evidence-briefings.md` |
| 信件即時通合併（E.1） | 第一階段 2026/08、第二階段 2026/10 測試；**對外寫「開發中」** | `wiki/evidence-briefings.md`、`style/resume-voice-zh.md` |
| 即時通事故（2026/05） | 合併前置優化造成部分廠商無法使用 → 週報公開說明、致歉、新增檢查機制 | `wiki/evidence-weekly-reports.md` |
| 配對名單「少又舊」 | 根因：依履歷修改日排序；實測主要競品反推規則，改上線日排序、20 天內不重複、新職缺首次配對每日上限 | `wiki/evidence-briefings.md` |
| 帳號安全升級（2026/04） | 十多家廠商遭冒用 → 新裝置驗證等；使用者負責影響評估、範圍與時程、驗證解鎖流程、客服說明與回饋收斂，**不參與技術實作**；一週內依客服回饋調整 | `wiki/evidence-weekly-reports.md`、`wiki/soft-skills.md` |
| 承攬制職缺 | 需求來自業務；先研究法規，與法務、稽核對齊後才進系統設計 | F09、F10 |
| AI 功能 | 已上線：公司簡介生成、職缺工作說明生成、職缺匯入、AI 推薦人才等；**職缺健檢尚未上線** | 2026-10-05 使用者確認｜F04 |

## 4. 方法與產出（2026-10-08 library 稽核補收；皆為既有 wiki 記錄）

| 事實 | 口徑／限制 | 來源 |
| :--- | :--- | :--- |
| 狀態驅動的規格方法：MECE 四狀態、權限代碼建模、條件邏輯，降低 RD／QA 反工 | 一般職缺寫白話「狀態與例外寫清楚」 | F02、`wiki/resume-extract.md` |
| UML／BPMN 建模：循序圖、活動圖、使用案例圖、BPMN | 產出物名稱可寫 | F02、`competency-framework.md` |
| 由規格推導驗收測試案例（跨系統即時訊息第二階段 11 條，逐條回連規格章節），與 QA 共寫並管理範圍異動 | 2026/09 起 | F05、`wiki/resume-extract.md` |
| PM／RD／QA／設計之間的樞紐；產出交接文件、功能說明頁、競品分析、跨組會議紀錄 | — | F06 |
| 流程工具化：把規格撰寫、驗收案例寫法沉澱成可重用 skill | — | F07、F05 |
| AI 協作系統：12 條分支、14 個常駐 session、23 個共用 skill、1 份共用規則書；SSOT、重複造輪偵測（攔截 2 次） | 對外寫「AI 協作流程」 | F15 |
| 227 項 roadmap、P0–P3 分級、時間盒交付 | — | F08、`competency-framework.md` |
| 負責範圍：求才（企業端）系統全模組（內部 A–M）＋求職端公司頁；HackMD 工作區 307 份文件為多人共用，只能說本人負責的範圍 | 對外不寫模組代號；撰寫份數〔待補〕 | `competency-framework.md` Profile Snapshot |
| AI 產品線：職缺匯入、公司簡介生成、職缺工作說明生成、AI 推薦人才（職缺健檢未上線） | — | F04、Profile Snapshot |
| 與第一線 tech support（同部門平行單位）協作 | — | Profile Snapshot |
| 每週發布需求處理週報（30 份以上） | — | `wiki/evidence-weekly-reports.md`、`wiki/soft-skills.md` |

## 5. 軟實力行為證據

完整表在 `wiki/soft-skills.md`（傾聽第一線、讓同仁參與決策、預先回答 FAQ、透明認錯、跨部門說服、接手困局、帶人與委派、跨文化協作、對外夥伴、平台政策、用證據說服、持續回報），皆有對應證據，**library 視為現行可用**；與 library 其他條衝突時以 library 為準（例：CodaPay 國家寫「印尼、泰國等」）。
