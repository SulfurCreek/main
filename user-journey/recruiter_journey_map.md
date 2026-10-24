# 求才端 User Journey Map（招募人員）

- 來源：反向工程自 [求才系統 Sitemap](https://hackmd.io/@1111-jobdocs/rkGFjjlPWe) 的 module 順序＋團隊 HackMD 規格內的 User Story／Use Case／需求背景（2026-09-30 擷取，377 份中求才端約 120 份）。
- 方法與格式規則：`.claude/skills/user-journey-map/SKILL.md`。
- 標記：`US` = 文件內真實 User Story；`US*` = 套版句「以便提高求才效率」（只證明功能存在，不證明動機）；`NULL` = 文件未記載，不推測。
- 連結前綴：`https://hackmd.io/@1111-jobdocs/<shortId>`，下表只寫 shortId 文字。

---

## 給沒有專案背景的讀者（先看這裡）

**這是什麼**：1111 人力銀行的「求才系統」（recruit.1111.com.tw）是企業 HR／招募人員用的後台，用來建立公司頁、刊登職缺、看應徵履歷或搜尋人才、聯繫求職者並約面試。本文件把這套後台的 HackMD 規格文件（約 137 份）反向整理成一條招募人員的使用旅程，每格都附來源文件連結。

**新版／現版**：頁面編號英文字母開頭（`A.1`、`E.1`）＝新版求才；純數字（`2.2`、`3.1.1`）＝現版求才，兩者架構不同。

**階段讀法**（階段碼沿用 HackMD 資料夾編碼，所以字母數字混排；表內順序＝招募流程由左到右）：

| 階段 | 白話名稱 | 版本 | 這一階段在做什麼 |
| :--- | :--- | :--- | :--- |
| J | 登入 | 新版 | 登入、雙重驗證、忘記帳號密碼；登入前可試搜人才 |
| A | 首頁 | 新版 | 一進來看刊登狀態、近期修改職缺、今日面試、快速搜人 |
| B | 公司 | 新版為主 | 建立公司頁（門面）；開副帳號、設權限與刊登設定 |
| C | 職缺 | 現版 | 新增／複製／匯入職缺、多筆管理、排序、移轉、廣告排程 |
| D | 人才 | 現版 | 收主動應徵履歷、看來訪名單、搜尋人才、追蹤／備註／封鎖 |
| E | 聯繫 | 現版＋新版 | 發詢問意願／面試邀約、聊天室對話、面試行事曆、錄取通知 |
| 5 | 紀錄 | 現版 | 回看邀約、瀏覽、使用、購買紀錄與數據統計 |
| 6／7 | 服務／購買（支援） | 現版為主 | 續約、購買曝光、簡訊加值、下載文件；任何階段都可能插入 |

**Opportunities 狀態標籤**：`【提案】`＝提案文件、`【草稿】`＝文件狀態草稿、`【規劃】`＝已排入第三階段但尚未完成；未標＝文件未載開發狀態。

<!--
[SYSTEM: UI/UX RENDERING INSTRUCTIONS FOR HTML AI AGENT]
Context: Section "1. Persona" holds 7 Roman Pichler style persona canvases (no personal names) plus shared terms, a persona comparison matrix and restricted-vendor modifiers. It replaces the former Context block (Persona / Scenario & Goal / Journey Type / variants / glossary are all merged here).
Action: When rendering this section into HTML:
1. Layout: modern SaaS dashboard, CSS Grid/Flexbox; multi-column on desktop, stacked on mobile.
2. Typography: clean sans-serif (Inter, Roboto, PingFang TC, Microsoft JhengHei).
3. "Persona 總覽" table: render as a comparison matrix on top; each row links (anchor) to its persona card. Use chips for 廠商狀態 (oStatus) and 帳號類型; color-code by status group: VIP=primary, 普通/過期=neutral, 關權=warning.
4. Persona cards (each "### P1…P7"): one card per persona, switchable by tabs or a card grid. Inside: quote as hero (large italic, thick brand-color left border, muted text; keep 〔推論〕 visible), "Details" as profile panel, "Goals" with success token (mint background, dark green text, check icon), "Pain Points" with danger token (light rose background, dark red text, warning icon), "可走的旅程" as stage chips J/A/B/C/D/E/5/6/7 (unavailable stages greyed out).
5. "受限廠商類型": render as filterable modifier cards (one per flag) that can be overlaid on any persona; keep code values (oStatus, confirmed&N, 代碼N) in monospace.
6. "名詞": render as a compact glossary (definition list or 2-column table), collapsible.
7. Evidence markers (US / US* / 〔推論〕 / NULL) and source links must stay visible; do not drop NULL cells.
-->

## 1. Persona

求才系統的使用者差異來自兩個維度：**公司的會員狀態**（`oStatus`）與**登入帳號的角色**（主帳號或副帳號＋權限）。以下 7 個 persona 由使用者定義（2026-10-05），內容依規格文件整理；文件沒寫的標 `NULL`，依文件事實推出的標 `〔推論〕`。下方 Journey Grid 以 **P3 VIP 主帳號** 的完整旅程為主線，其他 persona 的差異寫在各自的「可走的旅程」。

**旅程範圍：** Current State 現狀（由既有規格反向工程；第三階段規劃項目只出現在 Opportunities）。

### Persona 總覽

| Persona | 廠商狀態 | 帳號類型 | 可走的旅程 | 主要限制 |
| :--- | :--- | :--- | :--- | :--- |
| P1 普通廠商 | `oStatus:0` | NULL | J、A；C 不可刊登 | 無合約不可刊登，進職缺總覽提示洽客服 |
| P2 過期廠商 | `oStatus:2` | NULL | J、A、6／7 續約；C 不可刊登 | 合約到期，提示洽客服 |
| P3 VIP 主帳號（人資窗口） | `oStatus:1` | 主帳號 | 全部階段 | 無（權限最大、不可被限制） |
| P4 VIP 副帳號（人資） | `oStatus:1` | 副帳號 | 依權限代碼 | 每項功能由主帳號勾選權限 |
| P5 VIP 副帳號（用人主管／分店店長） | `oStatus:1` | 副帳號 | 依權限代碼，職缺限個人或所屬群組 | 只管自己或群組的職缺 |
| P6 VIP 人事助理 | `oStatus:1` | NULL（待確認是否為副帳號） | 依權限代碼 | NULL |
| P7 關權廠商 | `oStatus:3` | NULL | J、A、B.4 刊登設定；C 刊登暫停 | 會員暫停中，依條件可自行開啟刊登或需洽客服 |

* 其他會員狀態：`oStatus:4` 免費 VIP 同 VIP；`oStatus:5` 免費曝光會提示曝光期限；`oStatus:6` 準 VIP 提示會員未啟用與啟用日期（[2.1 職缺總覽](https://hackmd.io/@1111-jobdocs/HJvxSmNMWe)）。代碼定義見 [[REF] 系統代碼表 §1](https://hackmd.io/@1111-jobdocs/B1j3sN-bzx)。
* 權限模型：每間公司有一個主帳號與若干副帳號；主帳號權限最大、不可被限制，副帳號的權限於 [B.2.3 權限設定](https://hackmd.io/@1111-jobdocs/SyKtjeP8We) 逐項勾選（[[REF] 系統代碼表 §5.0](https://hackmd.io/@1111-jobdocs/B1j3sN-bzx)）。權限產生順序：稽核賦予廠商權限 → 客服設定廠商權限 → 主帳號設定帳號權限（[2.1 職缺總覽](https://hackmd.io/@1111-jobdocs/HJvxSmNMWe)）。

### P1 普通廠商

> 「我想刊職缺，但系統一直叫我去找客服。」〔推論〕依據：普通會員進職缺總覽會跳出「貴公司目前非VIP會員，若要刊登徵才職缺請洽客服」（[2.1 職缺總覽](https://hackmd.io/@1111-jobdocs/HJvxSmNMWe)）

* **Details：** 無合約，不可刊登（[[REF] 系統代碼表 §1](https://hackmd.io/@1111-jobdocs/B1j3sN-bzx)）；有 `confirmed&8192`（可聯絡求職者）時，收到主投信仍看得到聯絡方式，但不能使用招募功能
* **Goals：** 〔推論〕成為 VIP 以刊登職缺；依據：同上 alert 引導洽客服
* **Pain Points：** 進職缺總覽每天都會跳提示，可選「今日不再顯示」（[2.1 職缺總覽](https://hackmd.io/@1111-jobdocs/HJvxSmNMWe)）
* **可走的旅程：** J 登入、A 首頁；C 職缺不可刊登；其他階段 NULL（文件未載）

### P2 過期廠商

> 「合約到期了，我得先續約才能繼續刊登。」〔推論〕依據：到期會員進職缺總覽提示「非VIP會員，若要刊登請洽客服」（[2.1 職缺總覽](https://hackmd.io/@1111-jobdocs/HJvxSmNMWe)）

* **Details：** 合約已到期（`oStatus:2`）；有 `confirmed&8192` 時同 P1 可看主投者聯絡方式
* **Goals：** 續約恢復刊登（[7.1 線上續約](https://hackmd.io/@1111-jobdocs/ByKdpLaWZe)；續約入口顯示規則見 [(現版)1.2.3 開關天數設定](https://hackmd.io/@1111-jobdocs/Bkw7pIVLbx)）
* **Pain Points：** 同 P1 的每日提示
* **可走的旅程：** J、A、6／7 購買（續約）；C 不可刊登；其他 NULL

### P3 VIP 主帳號（人資窗口）

> 「我只想在同一個地方回覆求職者，回了就該算數。」〔推論〕依據：廠商因即時通與信件分開計算限時回應而抱怨（[即時通、信件通知合併](https://hackmd.io/@1111-jobdocs/SJJY3isYZe)）

* **Details：** 公司唯一主帳號，權限最大、不可被限制（[[REF] 系統代碼表 §5.0](https://hackmd.io/@1111-jobdocs/B1j3sN-bzx)）；負責開副帳號、設權限、群組與通知（[B.2 帳號設定](https://hackmd.io/@1111-jobdocs/SkfafU2WZg)、[新增帳號Modal](https://hackmd.io/@1111-jobdocs/rkciNnFHMg)）；固定收新增帳號信、帳號登入通知、續約感謝信（[新增／修改帳號信](https://hackmd.io/@1111-jobdocs/Bkw6AsHwMg)、[登入系統通知信](https://hackmd.io/@1111-jobdocs/HkZrBvaubg)、[VIP 續約感謝信](https://hackmd.io/@1111-jobdocs/Syo5pb-sbl)）
* **Goals：** 從開通帳號到把人招進來：建立公司門面 → 刊登職缺 → 收履歷／找人 → 聯繫邀約面試 → 錄取 → 回看成效；並管理團隊帳號
* **Pain Points：**
  * 面試邀約與即時通兩套工具，副帳號通知兩組設定，限時回應被分開計算（[即時通、信件通知合併](https://hackmd.io/@1111-jobdocs/SJJY3isYZe)）
  * 在其他人力銀行已刊登的職缺要手動重建（US [職缺匯入提案](https://hackmd.io/@1111-jobdocs/BJATOLPwbx)）
  * 來訪名單無法過濾、看不到誰關注公司或職缺（US [現版人才來訪拉皮更新](https://hackmd.io/@1111-jobdocs/SJ5oUbXv-g)、US [關注名單](https://hackmd.io/@1111-jobdocs/B1jNIrMBZl)）
  * 部分廠商沒有信箱，新驗證機制造成登入困難（[同步會議 2026.04.08](https://hackmd.io/@1111-jobdocs/Sk8KaX73Wl)）
* **可走的旅程：** 全部階段（下方 Journey Grid 主線）

### P4 VIP 副帳號（人資）

> 「我是人資，但有些功能要等主帳號幫我開權限才看得到。」〔推論〕依據：副帳號的功能入口依權限代碼顯示（[B.2.3 權限設定](https://hackmd.io/@1111-jobdocs/SyKtjeP8We)）

* **Details：** 權限由主帳號逐項勾選；例：通知設定需 `代碼66`（[B.2.2 通知設定](https://hackmd.io/@1111-jobdocs/BJGdoePUWl)），管理全部帳號需 `7+23`（[B.2 帳號設定](https://hackmd.io/@1111-jobdocs/SkfafU2WZg)），新增／修改職缺需 `代碼53`（[職缺匯入提案](https://hackmd.io/@1111-jobdocs/BJATOLPwbx)），帳號邀約紀錄需 `代碼55`（[5.1 帳號邀約紀錄](https://hackmd.io/@1111-jobdocs/rJ5Bp4RE-g)）
* **Goals：** 同 P3 的招募主線，範圍以被授權的功能為限
* **Pain Points：** NULL（文件未載）
* **可走的旅程：** 依權限代碼；未授權的功能不顯示入口

### P5 VIP 副帳號（用人主管／分店店長）

> 「我只管我這間店的職缺和應徵者。」〔推論〕依據：副帳號設了所屬群組後，管理職缺權限會改為「個人或群組職缺」（[B.2.3 權限設定 §6.2](https://hackmd.io/@1111-jobdocs/SyKtjeP8We)）

* **Details：** 由主帳號或有群組管理權限（`代碼65`）的帳號指定所屬群組；自己無法修改群組（[B.2.3 權限設定](https://hackmd.io/@1111-jobdocs/SyKtjeP8We)）；群組設定見 [1.2.4 群組設定](https://hackmd.io/@1111-jobdocs/S1G_8GQbZe)、[群組選擇Modal](https://hackmd.io/@1111-jobdocs/ByhoS3trGg)
* **Goals：** 〔推論〕處理自己或群組職缺的應徵者與面試；依據：管理職缺權限限個人或群組
* **Pain Points：** NULL（文件未載）
* **可走的旅程：** 〔推論〕以 C 職缺（限個人／群組）、D 人才、E 聯繫為主；依權限代碼而定

### P6 VIP 人事助理

> NULL（文件未載此角色的需求或抱怨）

* **Details：** 角色由使用者定義，規格文件沒有「人事助理」的描述；帳號類型與權限組合待確認。B.2.3 權限設定的「快速帶入」有依身分帶入的權限預設組合，各預設內容見 Figma，文件未列出（[B.2.3 權限設定 §6.1](https://hackmd.io/@1111-jobdocs/SyKtjeP8We)）
* **Goals：** NULL
* **Pain Points：** NULL
* **可走的旅程：** 依權限代碼；NULL（待確認）

### P7 關權廠商

> 「會員暫停中，我得先開啟刊登，或請客服幫忙。」〔推論〕依據：關權會員進職缺總覽的提示（[2.1 職缺總覽](https://hackmd.io/@1111-jobdocs/HJvxSmNMWe)）

* **Details：** `oStatus:3`，刊登暫停中。提示依條件分流（[2.1 職缺總覽](https://hackmd.io/@1111-jobdocs/HJvxSmNMWe)）：
  * 有刊登限制（`showfield` 非 4096）：提示洽客服
  * 無刊登限制且廠商可自行開啟、帳號有購買權限：提示「請開啟刊登」，按鈕導向開啟刊登畫面，需使用者手動開啟
  * 帳號無購買權限：提示洽客服
* **Goals：** 恢復刊登（[B.4 刊登設定](https://hackmd.io/@1111-jobdocs/ryEY3vBZbl)、[2.2.1 排程開關權Modal](https://hackmd.io/@1111-jobdocs/By5Eo8NvZx)）
* **Pain Points：** NULL（文件未載）；關權時系統會調查關權原因（[2.2.2 暫停刊登Modal](https://hackmd.io/@1111-jobdocs/SJ0mjWHvZx)）
* **可走的旅程：** J、A、B.4 刊登設定；C 職缺刊登暫停

### 受限廠商類型（廠商屬性旗標 `organs.confirmed`）

另一層差異來自廠商屬性旗標，會讓整段旅程少掉某些階段（[[REF] 系統代碼表 §2](https://hackmd.io/@1111-jobdocs/B1j3sN-bzx)）。

| 類型 | 旗標 | 限制 | 影響的旅程階段 |
| :--- | :--- | :--- | :--- |
| Cake 特殊廠商 | `confirmed&64` | 僅可使用主投與刊登職缺；不可用追蹤名單、追蹤資料夾、備註名單、匯入名單、全部搜尋、人才點數查詢、線上續約、購買優先排序（[A.1 Topbar Cake 功能清單](https://hackmd.io/@1111-jobdocs/Hym116n3-x)） | D 人才、5 紀錄、7 購買 |
| 保險業 | `confirmed&512` | 2011/3/15 起僅能主投，無配對名單與查詢名單功能 | D 人才 |
| 不公布廠商 | `confirmed&128` | 沒有主投、沒有配對，且不能查詢名單 | D 人才 |
| 八大行業 | `confirmed&4096` | 特種行業（八大）；列入黑名單組合 | D 人才 |
| 酒店／特種行業 | `confirmed&524288` | 酒店類廠商；列入黑名單組合 | D 人才 |
| 殯葬禮儀 | `confirmed&8` | 不可刊登業務職缺，並同時鎖定「需審核」 | C 職缺 |
| 直銷 | `confirmed&256` | 2014/12/2 起不再提供刊登 | C 職缺 |
| 需審核 | `confirmed&16384` | 職缺異動須經客服審核通過才對外顯示 | C 職缺 |
| 投審會已核準 | `confirmed&8388608` | 才能刊登工作地為中國（不含港澳）的職缺，送出後需審核 | C 職缺 |
| 高風險國家已核準 | `confirmed&1073741824` | 9 個海外高風險國家職缺原則不可刊登，核准者例外 | C 職缺 |
| 派遣單購點數 | `confirmed&1024` | 需購買點數才能查看名單與刊登職缺 | C 職缺、D 人才 |
| 不可修改（外網限制） | `confirmed&131072` | 外網時無法編輯公司資料、帳號權限、開關天數、職缺等 | B 公司、C 職缺 |
| 不可登入 | `confirmed&262144` | 廠商無法登入求才，內部同仁只能透過客服系統登入 | J 登入（整段旅程中斷） |
| 可聯絡求職者 | `confirmed&8192` | 普通／過期廠商仍看得到主投者聯絡方式，但不能使用招募功能 | D 人才、E 聯繫 |

* **黑名單組合**：`confirmed&128`、`&512`、`&4096`、`&524288`、`&64` 一併用於隱藏配對、AI 推薦等功能。
* 人派／勞務外包、經紀、保全清潔、房仲等旗標主要影響計價或業績歸屬，不改變旅程功能，未列入上表（見 REF §2）。

### 名詞

| 詞 | 意思 | 出處 |
| :--- | :--- | :--- |
| 主投 | 求職者主動應徵某職缺 | [主動應徵](https://hackmd.io/@1111-jobdocs/ry9S7kjuWe) |
| 副帳號 | 主帳號底下再開的其他招募人員帳號，有各自權限與群組 | [B.2 帳號設定](https://hackmd.io/@1111-jobdocs/SkfafU2WZg) |
| `oStatus` | 廠商會員狀態：0 普通、1 VIP、2 過期、3 關權、4 免費VIP、5 免費曝光、6 準VIP | [REF 系統代碼表](https://hackmd.io/@1111-jobdocs/B1j3sN-bzx) |
| 關權 | `oStatus:3`，刊登暫停中 | 同上 |
| 需審核 | 廠商旗標 `confirmed&16384`，職缺異動要客服審核後才對外顯示 | 同上 |
| 職缺審核 | 命中風險字或廠商需審核時，職缺進「審核中」，由客服通過／不通過 | [職缺審核信](https://hackmd.io/@1111-jobdocs/Hyj6_7X8fl) |
| 限時回應 | 職缺設定 1～7 天內回應求職者，達成可得「快速回覆標章」 | [職缺設定](https://hackmd.io/@1111-jobdocs/SJEiSjRzbl) |
| 立即上工 | 職缺屬性之一（`role` 32），工作時間用指定日期／期間 | [職缺內容](https://hackmd.io/@1111-jobdocs/BJ7Yob8W-g) |
| 承攬制 | 職缺特殊性質之一，工作時間固定「與公司議定」 | 同上 |
| 詢問意願／面試邀約 | 聯繫階段兩種通知；整併專案要把兩者拆開（詢問意願改 `mailType:2`） | [第三階段](https://hackmd.io/@1111-jobdocs/Hk3SOQrFfg) |
| 錄取通知 | 到職確認通知（`mailType:6`），未來用來追蹤招募成效 | [整併專案](https://hackmd.io/@1111-jobdocs/SJJY3isYZe) |
| Modal／Lightbox | 頁面上彈出的視窗，文件另有「M. Modal&Lightbox」資料夾 | — |
| `.aspx` | 現版頁面的檔名，Touchpoints 用它標示頁面 | Sitemap |
| `US`／`US*`／`〔推論〕`／`NULL` | 證據標記，見下方標記說明 | — |

> 標記：無標記＝文件明載（附連結）；`〔推論〕`＝依同格所寫文件事實推出；`NULL`＝文件未載也無可推論。`US`＝真實 User Story，`US*`＝套版句「以便提高求才效率」（只證明功能存在）。連結前綴 `https://hackmd.io/@1111-jobdocs/<shortId>`。

## 路由（找資料先看這裡）

> 🤖 **本節是給 AI 讀取用的索引，不是給人閱讀的內容。** AI 要找某階段的資料時，先查此表定位（HackMD 資料夾、本檔章節、起手文件），再去讀對應章節或原文；人類讀者可直接跳到〈總覽〉。

階段編碼**沿用 HackMD 資料夾編碼**（`求才系統/` 下的 A.～E.、5.～7.，登入為 `J.`），不自編；Sitemap 的 1～9 是另一套 module 序號，僅在「Sitemap 第N節」引用。

**版本判定**：頁面／文件編號英文字母開頭＝新版求才；純數字＝現版求才（兩者架構不同）。資料夾字母不代表版本，例如 `C. 職缺` 內的 `2.x` 文件都是現版。IA 異動時本檔與 [Sitemap](https://hackmd.io/@1111-jobdocs/rkGFjjlPWe) 要一起更新。

**前端架構**：新版求才＝Nuxt 3（Vue 3）為主、仍載入 jQuery 舊外掛；現版求才＝ASP.NET WebForms＋jQuery＋Bootstrap（`.aspx`，伺服器 postback）；兩者共用 `components.1111.com.tw` 的獨立元件（IIFE 打包）。埋點、共用元件等前端工作，新版可用 Nuxt composable，現版需另寫 jQuery 版。

| 編碼 | HackMD 資料夾 | 版本 | 文件數 | 本檔章節 | Sitemap | 起手文件 |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| J | `求才系統/J. 登入流程與登入前` | 新版 | 9 | 表 A | 第1節 | r11ad8Okfe（登入前頁） |
| A | `求才系統/A. 首頁` | 新版 | 12 | 表 A | 第2節 | Hym116n3-x（A.1 topbar） |
| B | `B. 公司`＋`B.2 帳號設定`＋`B.4 刊登設定` | 新版（例外：`1.2.3` 開關天數、`1.2.4` 群組設定為現版） | 23 | 表 A | 第3節 | S1jhD6RRbe（B.1） |
| C | `C. 職缺` | 現版（`2.x`） | 13 | 表 B | 第4節 | S1SfBeXxfe（2.2 新增職缺） |
| D | `求才系統/D. 人才` | 現版（`3.x`） | 21 | 表 B | 第5節 | HyYq_GgXWl（履歷詳細頁） |
| E | `E. 聯繫`＋`信件即時通合併專案` | 混合：`4.x` 現版；`E.1`／`E.2.x` 新版 | 9＋12 | 表 B | 第6節 | BJ0R8ocgGl（E.1 聯絡人才） |
| 5 | `求才系統/5. 紀錄` | 現版 | 4 | 表 C | 第7節 | S13Zy8rKze（5.5 人才點數） |
| 6／7 | `求才系統/6. 服務`、`求才系統/7. 購買` | 現版（例外：`A.7.1` 文件下載、`H.3` 合約上傳為新版） | 2＋3 | 表 C | 第8、9節 | ByKdpLaWZe（7.1 線上續約） |
| 共用 | `M. Modal&Lightbox`、`[REF]` 代碼表 | 依各文件編號 | 15＋ | 附錄〈文件關係〉末段 | — | B1j3sN-bzx（REF 系統代碼表） |

### 流程圖索引

各階段已繪製的流程圖位置（前端助手等 session 抓圖用）。連結是使用者從 HackMD 複製的精準定位連結（`stext`），文件被增刪內容後偏移量會失準，失準時改用 note ID 讀全文、找 `## 流程圖` 標題下的 mermaid 區塊。

| 階段 | 流程 | 圖類型 | 文件（note ID／shortId） | 精準位置 |
| :--- | :--- | :--- | :--- | :--- |
| C 職缺 | 求才廠商新增職缺完整流程（新增方式 → 屬性切換 → AI 功能 → 風險字檢查 → 送審 → 曝光） | Mermaid 循序圖 | 2.2 新增職缺（`nztEtyKMQYioP0uQ_BajBA`／`S1SfBeXxfe`），`## 流程圖` | [連結](https://hackmd.io/nztEtyKMQYioP0uQ_BajBA?both=&stext=3055%3A3%3A0%3A1790736378%3A-TdkQO) |

編輯流程：改事實 → 先到上表「HackMD 資料夾」找原文件修 → 再改對應章節的表格與〈文件關係〉。完整目錄見 repo 根目錄 `tree.md`。

## 2. The Journey Grid (旅程矩陣)

階段編碼沿用 HackMD 資料夾編碼；每表最多 4 個階段欄，共 3 張表（表 A：J、A、B；表 B：C、D、E；表 C：5、6／7 支援）。

### 表 A｜階段 J、A、B

| 階段 (Phases) | J 登入 | A 首頁 | B 公司 |
| :--- | :--- | :--- | :--- |
| **User Actions**<br>(用戶行為) | 登入前試搜人才 → 登入 → 雙重驗證（Email 連結）→ 忘記帳號／密碼時重設<br>[試搜](https://hackmd.io/@1111-jobdocs/Sk4CnTjgMg)、[登入](https://hackmd.io/@1111-jobdocs/rych3fo0bl)、[雙重驗證](https://hackmd.io/@1111-jobdocs/ryqrsG2lWg)、[忘記密碼](https://hackmd.io/@1111-jobdocs/HJT3dH_vWg)、[登入前頁](https://hackmd.io/@1111-jobdocs/r11ad8Okfe)、[聯絡我們](https://hackmd.io/@1111-jobdocs/HJqwacQNGl)、[傳真刊登](https://hackmd.io/@1111-jobdocs/SkpgK_GYWl) | 看快訊與刊登狀態 → 點近期修改職缺 → 看今日面試／匯出行事曆 → 人才秒搜<br>[A.2&A.3](https://hackmd.io/@1111-jobdocs/Bye3E5tl-g)、[A.4](https://hackmd.io/@1111-jobdocs/HJIK-sUGbe)、[A.5](https://hackmd.io/@1111-jobdocs/B1MejWhvGl)、[A.10](https://hackmd.io/@1111-jobdocs/BkIIbQYfWe) | 填基本資料 → 形象／工作環境／產品服務／福利／更多介紹 → 上傳面試須知 → 選版型 → 預覽送審；取公司頁 QR Code；開副帳號、設通知與權限、群組、聯絡人、刊登設定<br>[B.1](https://hackmd.io/@1111-jobdocs/S1jhD6RRbe)、[B.1.3](https://hackmd.io/@1111-jobdocs/SkztPlKsbx)、[B.2](https://hackmd.io/@1111-jobdocs/SkfafU2WZg)、[B.4](https://hackmd.io/@1111-jobdocs/ryEY3vBZbl) |
| **Touchpoints**<br>(接觸點) | login.aspx、AgentVerify.aspx、AgentVerifyCheck.aspx（Sitemap 第1節）<br>Email：[裝置驗證信](https://hackmd.io/@1111-jobdocs/B1fzI8G2We)、[登入系統通知信](https://hackmd.io/@1111-jobdocs/HkZrBvaubg) | 首頁；Topbar（公告、通知、帳號選單、異常狀態列）（Sitemap 第2節）<br>[A.1](https://hackmd.io/@1111-jobdocs/Hym116n3-x)、[A.1.7](https://hackmd.io/@1111-jobdocs/SkJEsXNWMx) | /company/\*、/settings/\*、VipSchedule.aspx、PublishEmpGroup.aspx（Sitemap 第3節）<br>Email：[新增／修改帳號信](https://hackmd.io/@1111-jobdocs/Bkw6AsHwMg) |
| **Thoughts**<br>(內心 OS) | 〔推論〕「我沒有信箱，怎麼驗證？」依據：客服反映部分廠商沒有信箱，無法通過現行驗證 [同步會議 2026.04.08](https://hackmd.io/@1111-jobdocs/Sk8KaX73Wl) | NULL | NULL |
| **Emotions**<br>(情緒感受) | 🤔 困惑〔推論〕依據同上 | NULL | NULL |
| **Pain Points**<br>(痛點/摩擦力) | 部分廠商沒有信箱，新驗證機制造成登入困難（客服反映）[來源](https://hackmd.io/@1111-jobdocs/Sk8KaX73Wl) | 會員／刊登異常不易察覺（異常狀態列存在的理由）US [A.1.7](https://hackmd.io/@1111-jobdocs/SkJEsXNWMx) | 內部 IP 上傳的圖片有侵權風險，需對外下架 [B.1.4](https://hackmd.io/@1111-jobdocs/Sy6vKV4FZx) |
| **Opportunities**<br>(產品機會點) | 登入異常統一 Alert；登入前智能客服（每日 3 次）<br>[特殊狀態與Alert](https://hackmd.io/@1111-jobdocs/HJb5FnCGZg)、[智能客服](https://hackmd.io/@1111-jobdocs/Hy95Qz7g-e) | `【規劃】`Topbar 通知收斂為只剩來訪人才（第三階段）[來源](https://hackmd.io/@1111-jobdocs/Hk3SOQrFfg) | 三種新增帳號方式（含複製帳號）；刊登設定取代開關天數設定<br>[功能說明頁](https://hackmd.io/@1111-jobdocs/rynOybVWZx)、[新增帳號Modal](https://hackmd.io/@1111-jobdocs/rkciNnFHMg) |
| **Metrics**<br>(衡量指標) | 〔推論〕登入成功率（含雙重驗證完成率）；依據：雙重驗證為登入必經步驟 | 〔推論〕首頁區塊點擊率（職缺、面試行事曆）；依據：首頁以入口導流為主 | 〔推論〕公司資料完成度；依據：B.1 設有填寫進度條 |

### 表 B｜階段 C、D、E

| 階段 (Phases) | C 職缺 | D 人才 | E 聯繫 |
| :--- | :--- | :--- | :--- |
| **User Actions**<br>(用戶行為) | 快速新增／複製／全新／匯入職缺 → 設應徵過濾 → 總覽多筆操作（更新日期、開關、改工作時間）→ 排序、移轉、排廣告<br>完整流程（循序圖）：[2.2 新增職缺＞流程圖](https://hackmd.io/nztEtyKMQYioP0uQ_BajBA?both=&stext=3055%3A3%3A0%3A1790736378%3A-TdkQO)<br>[2.2](https://hackmd.io/@1111-jobdocs/S1SfBeXxfe)、[複製](https://hackmd.io/@1111-jobdocs/HJW-MWp4Wg)、[匯入](https://hackmd.io/@1111-jobdocs/Bk854rrtGe)、[應徵過濾](https://hackmd.io/@1111-jobdocs/r1AirkvF-x)、[2.1 總覽](https://hackmd.io/@1111-jobdocs/HJvxSmNMWe)、[多筆修改](https://hackmd.io/@1111-jobdocs/HkHIwU8Y-x)、[2.3](https://hackmd.io/@1111-jobdocs/B1Srfpi7bg)、[2.4](https://hackmd.io/@1111-jobdocs/rJ5KsWEG-e)、[2.7](https://hackmd.io/@1111-jobdocs/Sy7bgNuzZg)<br>職缺內頁（新增／修改職缺欄位）：[2.0 總覽](https://hackmd.io/@1111-jobdocs/B1p54YozMe)、[職缺內容](https://hackmd.io/@1111-jobdocs/BJ7Yob8W-g)、[職缺設定](https://hackmd.io/@1111-jobdocs/SJEiSjRzbl)、[應徵方式](https://hackmd.io/@1111-jobdocs/Sy_fXBBfWx)、[送出彈窗與審核](https://hackmd.io/@1111-jobdocs/rJhe4yBNWe)、[職缺預覽頁](https://hackmd.io/@1111-jobdocs/S1OfrDqiWl)、[職缺健檢提案](https://hackmd.io/@1111-jobdocs/Hk_KPwz3Zl)、[工作時間提案](https://hackmd.io/@1111-jobdocs/S1xTdMKV-l) | 看主動應徵 → 開履歷詳細頁 → 追蹤／備註／封鎖／轉寄／列印 → 看來訪名單 → AI 推薦／配對／簡易／進階／大專搜尋<br>[3.1.1](https://hackmd.io/@1111-jobdocs/ry9S7kjuWe)、[履歷詳細頁](https://hackmd.io/@1111-jobdocs/HyYq_GgXWl)、[追蹤人才](https://hackmd.io/@1111-jobdocs/r1V8b3ZDWg)、[備註](https://hackmd.io/@1111-jobdocs/rkX_P2qqZl)、[轉寄](https://hackmd.io/@1111-jobdocs/ByoEYp2a-g)、[列印](https://hackmd.io/@1111-jobdocs/SJMq3nfkGe)、[3.2.6](https://hackmd.io/@1111-jobdocs/r1TBqJjeGx)、[3.2.1](https://hackmd.io/@1111-jobdocs/Bk06kDtf-l)、[3.2.3](https://hackmd.io/@1111-jobdocs/Syn7AN87Wl) | 開通知 Lightbox → 選範本 → 發詢問意願／面試邀約 → 聊天室對話 → 建立／改期／取消面試 → 錄取通知；求職者失約時回報<br>[4.0](https://hackmd.io/@1111-jobdocs/r1qJb-uXbx)、[範本](https://hackmd.io/@1111-jobdocs/SJ8KDMo8fl)、[4.1](https://hackmd.io/@1111-jobdocs/rJkyKgeGWl)、[信件對話](https://hackmd.io/@1111-jobdocs/r1ghrPxP-x)、[第二階段](https://hackmd.io/@1111-jobdocs/ry_GPNuZze)、[4.3](https://hackmd.io/@1111-jobdocs/HydajKbPfl)、[失約回報](https://hackmd.io/@1111-jobdocs/Sy70gCPKGe) |
| **Touchpoints**<br>(接觸點) | PublishList／PublishOpening／PublishEmpSort／PublishEmpTrans／BuyScheduleBooking.aspx（Sitemap 第4節）<br>Email：[職缺確認信](https://hackmd.io/@1111-jobdocs/BktAq_Szbl)、[職缺審核信](https://hackmd.io/@1111-jobdocs/Hyj6_7X8fl) | ResumePool\*.aspx、ResumeSearch\*.aspx、ResumeDetailShow.aspx（Sitemap 第5節）<br>Email：[人才配對信](https://hackmd.io/@1111-jobdocs/Hka1IFeUfx)、[凌晨配對信](https://hackmd.io/@1111-jobdocs/ryisuzlZzg) | ResumePoolNoticeMail(Detail).aspx、Exemplar.aspx、oInterView.aspx、SMS.aspx、右下角即時通面板（Sitemap 第6節）<br>Email：[企業通知信件](https://hackmd.io/@1111-jobdocs/HkKTVkw_fl)[即時通面板](https://hackmd.io/@1111-jobdocs/SJsYLtmr-g) |
| **Thoughts**<br>(內心 OS) | 〔推論〕「別家已經刊過了，為什麼要重打？」依據：匯入提案 User Story 要把其他人力銀行職缺直接匯入 [來源](https://hackmd.io/@1111-jobdocs/BJATOLPwbx) | 〔推論〕「誰關注了我？數字怎麼對不上？」依據：關注名單設計理念要避免廠商抱怨數字不一致 [來源](https://hackmd.io/@1111-jobdocs/B1jNIrMBZl) | 〔推論〕「回了怎麼還算沒回應？」依據：即時通與信件分開判斷，廠商抱怨限時回應 [來源](https://hackmd.io/@1111-jobdocs/SJJY3isYZe) |
| **Emotions**<br>(情緒感受) | 😤 挫折〔推論〕依據同上 | 😤 挫折〔推論〕依據同上 | 😤 挫折〔推論〕依據同上 |
| **Pain Points**<br>(痛點/摩擦力) | 在其他人力銀行已刊登的職缺要手動重建 US [來源](https://hackmd.io/@1111-jobdocs/BJATOLPwbx) | 來訪名單無法過濾（狀態、日期、性別、年齡）；追蹤名單不能直接刪除；看不到誰關注公司／職缺<br>US [來訪拉皮](https://hackmd.io/@1111-jobdocs/SJ5oUbXv-g)、[追蹤人才](https://hackmd.io/@1111-jobdocs/r1V8b3ZDWg)、[關注名單](https://hackmd.io/@1111-jobdocs/B1jNIrMBZl) | 兩套工具各自溝通、副帳號通知兩組設定；勾「希望 N 天內回覆」後訊息未顯示期限；範本不能排序置頂；求職者失約<br>[SJJY3isYZe](https://hackmd.io/@1111-jobdocs/SJJY3isYZe)、[信件對話](https://hackmd.io/@1111-jobdocs/r1ghrPxP-x)、US [E.2.1](https://hackmd.io/@1111-jobdocs/HyDIQwJUWg)、US [失約回報](https://hackmd.io/@1111-jobdocs/Sy70gCPKGe) |
| **Opportunities**<br>(產品機會點) | `【提案】`職缺匯入；`【草稿】`AI 職缺審核<br>[匯入提案](https://hackmd.io/@1111-jobdocs/BJATOLPwbx)、[AI審核提案](https://hackmd.io/@1111-jobdocs/B1bkIvMhZx) | `【提案】`關注名單（數字與名單一致）；來訪名單過濾<br>[關注名單](https://hackmd.io/@1111-jobdocs/B1jNIrMBZl)、[來訪拉皮](https://hackmd.io/@1111-jobdocs/SJ5oUbXv-g) | 整併專案（分三階段，第三階段`【規劃】`）：信件＋即時通整併、訊息收回、已讀、附檔；詢問意願與面試邀約拆開；同意面試後自動建立行事曆<br>[SJJY3isYZe](https://hackmd.io/@1111-jobdocs/SJJY3isYZe)、[各階段內容](https://hackmd.io/@1111-jobdocs/r1eNVEfmMx)、[第三階段](https://hackmd.io/@1111-jobdocs/Hk3SOQrFfg) |
| **Metrics**<br>(衡量指標) | 〔推論〕職缺建立完成率、匯入使用率；依據：提案以「不需手動建職缺」為價值 | 〔推論〕來訪名單→聯絡轉換率；依據：來訪名單 User Story 目的是「主動接觸有意願的人才」 | 面試邀約使用率（文件預期會增加）、限時回應達成率〔推論〕；依據：[SJJY3isYZe](https://hackmd.io/@1111-jobdocs/SJJY3isYZe) 載明預期面試邀約使用率增加、回覆主投者皆計入限時回應 |

### 表 C｜階段 5、6／7（支援）

| 階段 (Phases) | 5 紀錄 | 6 服務／7 購買（支援，任何階段可插入） |
| :--- | :--- | :--- |
| **User Actions**<br>(用戶行為) | 看帳號邀約紀錄 → 履歷瀏覽紀錄 → 帳號使用／購買紀錄 → 數據統計 → 人才點數<br>[5.1](https://hackmd.io/@1111-jobdocs/rJ5Bp4RE-g)、[5.3](https://hackmd.io/@1111-jobdocs/S1-Wt68M-e)、[5.6](https://hackmd.io/@1111-jobdocs/SJeZiGSMbx)、[5.5](https://hackmd.io/@1111-jobdocs/S13Zy8rKze)、[記錄管理](https://hackmd.io/@1111-jobdocs/Sk4AvcZ-We) | 續約 → 購買優先排序／簡訊加值 → 上傳合約；下載文件、填滿意度、問智能客服<br>[7.1](https://hackmd.io/@1111-jobdocs/ByKdpLaWZe)、[7.2](https://hackmd.io/@1111-jobdocs/HJzsieKfWe)、[H.3](https://hackmd.io/@1111-jobdocs/HJD1Eu0c-e)、[A.7.1](https://hackmd.io/@1111-jobdocs/Sk5kyX6ubx)、[6.8](https://hackmd.io/@1111-jobdocs/S1fR49Fg-l) |
| **Touchpoints**<br>(接觸點) | Log\*.aspx（Sitemap 第7節） | vipContract.aspx、BuyExposure.aspx、SMSorder.aspx、/download、外部連結（Sitemap 第8、9節）<br>Email：[VIP 續約感謝信](https://hackmd.io/@1111-jobdocs/Syo5pb-sbl)、[信用卡繳款通知信](https://hackmd.io/@1111-jobdocs/BJ2GChM1Mx) |
| **Thoughts**<br>(內心 OS) | NULL | NULL |
| **Emotions**<br>(情緒感受) | NULL | NULL |
| **Pain Points**<br>(痛點/摩擦力) | NULL | 合約要另外用 E-mail 寄給客服 US [H.3](https://hackmd.io/@1111-jobdocs/HJD1Eu0c-e)；薪資行情與法規疑問、新廠商學習成本 US [智能客服](https://hackmd.io/@1111-jobdocs/Hy95Qz7g-e) |
| **Opportunities**<br>(產品機會點) | 錄取通知作為招募成效數據，與 E 聯繫連動 [來源](https://hackmd.io/@1111-jobdocs/SJJY3isYZe) | 線上合約上傳；智能客服 |
| **Metrics**<br>(衡量指標) | 〔推論〕數據統計查詢造訪率；依據：5.6 為成效回看入口（US*，未載動機） | 〔推論〕線上續約完成率；依據：7.1 為續約入口 |

## 3. Key Takeaways & PM Action Items

* **🤩 Aha Moment (頓悟時刻):** E 聯繫：求職者同意面試後，系統自動建立面試行事曆，廠商不必再手動排程。選它的證據：整併專案文件明載此為預期價值 [SJJY3isYZe](https://hackmd.io/@1111-jobdocs/SJJY3isYZe)（屬「預期」，文件無實測資料）。
* **⚠️ Biggest Drop-off Risk (最大流失風險):** E 聯繫：溝通被拆在兩套工具，限時回應被分開計算。選它的證據：文件載有廠商抱怨與副帳號雙組通知設定 [SJJY3isYZe](https://hackmd.io/@1111-jobdocs/SJJY3isYZe)；聯繫階段記載的痛點最多。
* **🚀 Next Steps (下一步行動):**
  1. **E 聯繫**：第三階段「面試提醒系統訊息」的觸發時機、文案、收件對象目前皆 `待補` [來源](https://hackmd.io/@1111-jobdocs/Hk3SOQrFfg)，需先定義才能取代舊提醒（對應痛點：兩套工具、面試管理分散）。
  2. **D 人才**：來訪名單過濾與關注名單併入同一名單，避免人數與名單不一致（對應痛點：來訪名單無法過濾、看不到關注者）。
  3. **5 紀錄**：補上真實 User Story 與痛點（目前為套版句），否則無法設計成效回看（對應缺口）。
  4. **全站**：Sitemap 上約 11 個頁面（職缺同步、自動更新、即時通記錄等）沒有規格文件，列入補文件清單。

---

## 附錄｜文件關係與缺口

### 文件關係（階段 → 功能 → 文件）

| 階段 | 功能 | 文件 |
| :--- | :--- | :--- |
| J 登入 | 登入前頁／試搜 | r11ad8Okfe、Sk4CnTjgMg、Hyt5LqcyMl |
| J 登入 | 登入／驗證／找回 | rych3fo0bl、HJb5FnCGZg、rk0aZy0aZg、ryqrsG2lWg、HJT3dH_vWg、SJNKOS_D-g |
| A 首頁 | Topbar | Hym116n3-x、HkTiVy7Z-e、SJsQkWsWbg、ryik5PAZWl、SkJEsXNWMx |
| A 首頁 | 首頁區塊 | Bye3E5tl-g、HJIK-sUGbe、B1MejWhvGl、BkIIbQYfWe |
| B 公司 | 公司資料 | S1jhD6RRbe、ryUoKHCG-e、SJhAVOy8Wg、SkztPlKsbx、Sy6vKV4FZx、Hk7HExLUWx、HJvhE8BFWe、BJEWK648bx、S1HPE5EU-e、ByA4t_-cZg、H1ZbConBbl、HkSJkuy8bx |
| B 公司 | 設定 | SkfafU2WZg、BytSsxD8be、Bk1uH5fXbx、BJGdoePUWl、SyKtjeP8We、rkciNnFHMg、SkdiYvsnZe、S1G_8GQbZe、ryEY3vBZbl、Bkw7pIVLbx、By5Eo8NvZx、SJ0mjWHvZx |
| C 職缺 | 建立 | S1SfBeXxfe、HJW-MWp4Wg、Bk854rrtGe、BJATOLPwbx、B1bkIvMhZx、BJ7Yob8W-g（職缺內容欄位） |
| C 職缺 | 管理 | HJvxSmNMWe、B1pOwHZQ-e、rJvOFkwFbl、HkHIwU8Y-x、r1AirkvF-x、B1Srfpi7bg、rJ5KsWEG-e、Sy7bgNuzZg |
| D 人才 | 履歷 | ry9S7kjuWe、S1I24H-lzl、Byy7rOTM-x、B19dalQ-Zx、rkMnZsqu-g、SJ5oUbXv-g、rk8RQxMXzg、rkkn5BZQ-g、B1jNIrMBZl、HyYq_GgXWl、H18Vo3zyMx |
| D 人才 | 搜尋 | r1TBqJjeGx、Bk06kDtf-l、BkMNTH_Pfe、Syn7AN87Wl、SJleDiy9bl、SkyLndUmWe、BkCVW1nXbg、SyvesCVEbg、rygtdmRNZl |
| E 聯繫 | 發通知 | r1qJb-uXbx、S1XwSUPBZg、H1OpoEs7fe、SJ8KDMo8fl、HyDIQwJUWg、BJt1Rj59Ze、BkXGV4BW-e |
| E 聯繫 | 對話（整併專案） | BJ0R8ocgGl、ry_GPNuZze、Hk3SOQrFfg、rJkyKgeGWl、r1ghrPxP-x、BJmM2cDGfl、SJJY3isYZe、r1eNVEfmMx、Hk87bluGMg、SkKwqvUFfg、SJsYLtmr-g |
| E 聯繫 | 面試 | HydajKbPfl、Sy70gCPKGe |
| 5 紀錄 | 紀錄 | rJ5Bp4RE-g、S1-Wt68M-e、SJeZiGSMbx、S13Zy8rKze、Sk4AvcZ-We |
| C 職缺 | 職缺內頁（2.0） | B1p54YozMe、BJ7Yob8W-g、SJEiSjRzbl、Sy_fXBBfWx、rJhe4yBNWe、S1OfrDqiWl、Hk_KPwz3Zl、S1xTdMKV-l |
| J 登入 | 登入前補充 | r11ad8Okfe、HJqwacQNGl、SkpgK_GYWl |
| 各階段 | 系統 Mail（廠商收到的信） | B1fzI8G2We、HkZrBvaubg、Bkw6AsHwMg、BktAq_Szbl、Hyj6_7X8fl、Hka1IFeUfx、ryisuzlZzg、HkKTVkw_fl、Syo5pb-sbl、BJ2GChM1Mx、SystNGUZWx（廠商回流 E-mail 短解，用途待確認） |
| E 聯繫 | 整併專案參考 | HyEvtWMLGe（Phase 1 測試文件）、SknUQhPfGx（求職端交付內容）、rk-QWt0Yfg（mailNotice SQL 筆記）、S1cYFSFfzx（信件訊息頁前端視覺調整） |
| 6／7 服務購買 | 服務／購買 | Sk5kyX6ubx、S1fR49Fg-l、ByKdpLaWZe、HJzsieKfWe、HJD1Eu0c-e、Hy95Qz7g-e、SJtErv_lZl、rynOybVWZx |

**跨階段共用元件**（不屬單一階段）：無權限Alert ryACpaCAWe、帳號選擇 S13ZYP9jbg、群組選擇 ByhoS3trGg、職缺選單 r1jXRIzqGg、現版職缺選擇 BkxSWZuGWx、通訊錄 B1iOzIB9-e、新增封鎖 H1guSxywZe、代碼參考 B1j3sN-bzx／ryjSpM-tzg。

---

### 缺口（寫 journey 時發現）

- 約 30 份文件的 User Story 是套版句「以便提高求才效率」，沒有寫出真正動機（如 A.2、A.4、5.x、3.2.x、7.x）——這些階段的「目標」只能標 US*。
- 全部文件都**沒有情緒／想法**的記載（沒有訪談或可用性測試資料），情緒曲線只能從「抱怨」「客服反映」推。
- `紀錄` 階段沒有任何痛點或動機記載。
- Sitemap 上沒掛文件連結、這次也沒找到對應規格的頁面：公司相關訊息、上傳檔案、職缺同步、自動更新、職缺所屬群組、匯入名單、還原刪除履歷、問題履歷回報、即時通記錄、簡訊通知紀錄、帳號使用紀錄（除購買紀錄外）。

- **範圍外（使用者 2026-09-30 指示暫不納入）**：客服系統資料夾（人才推薦、客服後台上傳文件、廠商瀏覽器驗證、顯示控制代碼表、不顯示外籍人士、聯絡我們清單）；因此 Grid 不加「後台／客服」泳道，審核流程只在 2.2 流程圖裡以客服參與者呈現。
- **已修正**：Sitemap「公司頁進度條」斷連結 `/HJe0Qv5pLWg` 已改指 B.1（`S1jhD6RRbe`）。
- **已排除**：`七言絕句`、Archived 忘記帳號／密碼、重複的 3.1.1 卡片 `rJPXuwBxzg`。

### 待辦（補證據計畫）

* 流程圖：目前只有 C 職缺一張（見〈流程圖索引〉）；優先補 E 聯繫（詢問意願／面試邀約到錄取）> B 公司（開通到開副帳號）> D 人才（收履歷到聯絡）。每畫一張就在〈流程圖索引〉加一列。
* 套版 User Story（"以便提高求才效率"）共 35 份，請文件作者補上真實動機，補完後這些階段的 Thoughts／Emotions 才能脫離 `NULL`：
  * [人才試搜列表](https://hackmd.io/@1111-jobdocs/Sk4CnTjgMg)
  * [3.2.6 AI推薦人才名單](https://hackmd.io/@1111-jobdocs/r1TBqJjeGx)
  * [人才試搜履歷資料](https://hackmd.io/@1111-jobdocs/Hyt5LqcyMl)
  * [登入功能](https://hackmd.io/@1111-jobdocs/rych3fo0bl)
  * [toast](https://hackmd.io/@1111-jobdocs/rk0aZy0aZg)
  * [廠商瀏覽器驗證](https://hackmd.io/@1111-jobdocs/ryugZ32nWe)
  * [3.2.4 大專人才搜尋](https://hackmd.io/@1111-jobdocs/SJleDiy9bl)
  * [A.7.1 文件下載](https://hackmd.io/@1111-jobdocs/Sk5kyX6ubx)
  * [3.1.1 主動應徵履歷列表](https://hackmd.io/@1111-jobdocs/ry9S7kjuWe)
  * [J.1.9 忘記密碼規格文件](https://hackmd.io/@1111-jobdocs/HJT3dH_vWg)
  * [J.1.9 忘記帳號規格文件](https://hackmd.io/@1111-jobdocs/SJNKOS_D-g)
  * [即時通面板](https://hackmd.io/@1111-jobdocs/SJsYLtmr-g)
  * [5.1 帳號邀約紀錄](https://hackmd.io/@1111-jobdocs/rJ5Bp4RE-g)
  * [搜尋人才卡片（改版畫面）](https://hackmd.io/@1111-jobdocs/SyvesCVEbg)
  * [3.2 搜尋結果頁（現版）](https://hackmd.io/@1111-jobdocs/SkyLndUmWe)
  * [3.2.3 進階搜尋](https://hackmd.io/@1111-jobdocs/Syn7AN87Wl)
  * [3.1.8 封鎖名單](https://hackmd.io/@1111-jobdocs/rkkn5BZQ-g)
  * [登入特殊狀態與Alert](https://hackmd.io/@1111-jobdocs/HJb5FnCGZg)
  * [3.1.1 主動應徵履歷卡片](https://hackmd.io/@1111-jobdocs/Byy7rOTM-x)
  * [3.2.1 配對條件設定](https://hackmd.io/@1111-jobdocs/Bk06kDtf-l)
  * [A.10 人才秒搜](https://hackmd.io/@1111-jobdocs/BkIIbQYfWe)
  * [7.2 購買優先排序](https://hackmd.io/@1111-jobdocs/HJzsieKfWe)
  * [5.3 帳號使用紀錄＞購買紀錄](https://hackmd.io/@1111-jobdocs/S1-Wt68M-e)
  * [A.4 近期修改職缺](https://hackmd.io/@1111-jobdocs/HJIK-sUGbe)
  * [5.6 數據統計查詢](https://hackmd.io/@1111-jobdocs/SJeZiGSMbx)
  * [不顯示：外籍人士需求](https://hackmd.io/@1111-jobdocs/S1ZG37NG-x)
  * [A.1.6 帳號資訊選單](https://hackmd.io/@1111-jobdocs/ryik5PAZWl)
  * [7.1 線上續約](https://hackmd.io/@1111-jobdocs/ByKdpLaWZe)
  * [A.1.4&A.1.5 公告&通知](https://hackmd.io/@1111-jobdocs/SJsQkWsWbg)
  * [追蹤名單權限](https://hackmd.io/@1111-jobdocs/B19dalQ-Zx)
  * [A.1.3 公告](https://hackmd.io/@1111-jobdocs/HkTiVy7Z-e)
  * [J.1.7 雙重驗證 規格文件](https://hackmd.io/@1111-jobdocs/ryqrsG2lWg)
  * [6.8 滿意度調查](https://hackmd.io/@1111-jobdocs/S1fR49Fg-l)
  * [A.2 首頁快訊 & A.3刊登狀態](https://hackmd.io/@1111-jobdocs/Bye3E5tl-g)
  * [求才智能客服](https://hackmd.io/@1111-jobdocs/Hy95Qz7g-e)
