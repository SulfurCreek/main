# 求才端 User Journey Map（招募人員）

- 來源：反向工程自 [求才系統 Sitemap](https://hackmd.io/@1111-jobdocs/rkGFjjlPWe) 的 module 順序＋團隊 HackMD 規格內的 User Story／Use Case／需求背景（2026-09-30 擷取，377 份中求才端約 120 份）。
- 方法與格式規則：`.claude/skills/user-journey-map/SKILL.md`。
- 標記：`US` = 文件內真實 User Story；`US*` = 套版句「以便提高求才效率」（只證明功能存在，不證明動機）；`NULL` = 文件未記載，不推測。
- 連結前綴：`https://hackmd.io/@1111-jobdocs/<shortId>`，下表只寫 shortId 文字。

---

## 1. Context (情境設定)

* **Persona (目標用戶):** 企業 HR／招募人員（主帳號可開副帳號、分群組與權限）。
  * 核心痛點（文件有載）：面試邀約與即時通兩套工具各自溝通、副帳號通知有兩組設定、限時回應被分開計算而抱怨 [來源](https://hackmd.io/@1111-jobdocs/SJJY3isYZe)；新廠商學習成本高、薪資行情與法規疑問需問客服 [來源](https://hackmd.io/@1111-jobdocs/Hy95Qz7g-e)。
  * 變體：VIP／免費VIP／關權／到期（刊登與權限不同，見 [B.4 刊登設定](https://hackmd.io/@1111-jobdocs/ryEY3vBZbl)、[REF 系統代碼表](https://hackmd.io/@1111-jobdocs/B1j3sN-bzx)）；Cake 特殊廠商部分人才功能不可用。
* **Scenario & Goal (場景與目標):** 從開通帳號到把人招進來——建立公司門面 → 刊登職缺 → 收履歷／找人 → 聯繫邀約面試 → 錄取 → 回看成效。`服務`、`購買`不在主線，於任何階段都可能插入（見支援格組）。
* **Journey Type:** Current State 現狀（由既有規格反向工程；第三階段規劃項目只出現在 Opportunities）。

> 標記：無標記＝文件明載（附連結）；`〔推論〕`＝依同格所寫文件事實推出；`NULL`＝文件未載也無可推論。`US`＝真實 User Story，`US*`＝套版句「以便提高求才效率」（只證明功能存在）。連結前綴 `https://hackmd.io/@1111-jobdocs/<shortId>`。

## 路由（找資料先看這裡）

> 🤖 **本節是給 AI 讀取用的索引，不是給人閱讀的內容。** AI 要找某階段的資料時，先查此表定位（HackMD 資料夾、本檔章節、起手文件），再去讀對應章節或原文；人類讀者可直接跳到〈總覽〉。

階段編碼**沿用 HackMD 資料夾編碼**（`求才系統/` 下的 A.～E.、5.～7.，登入為 `J.`），不自編；Sitemap 的 1～9 是另一套 module 序號，僅在「Sitemap 第N節」引用。

**版本判定**：頁面／文件編號英文字母開頭＝新版求才；純數字＝現版求才（兩者架構不同）。資料夾字母不代表版本，例如 `C. 職缺` 內的 `2.x` 文件都是現版。IA 異動時本檔與 [Sitemap](https://hackmd.io/@1111-jobdocs/rkGFjjlPWe) 要一起更新。

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

編輯流程：改事實 → 先到上表「HackMD 資料夾」找原文件修 → 再改對應章節的表格與〈文件關係〉。完整目錄見 repo 根目錄 `tree.md`。

## 2. The Journey Grid (旅程矩陣)

階段編碼沿用 HackMD 資料夾編碼；每表最多 4 個階段欄，共 3 張表（表 A：J、A、B；表 B：C、D、E；表 C：5、6／7 支援）。

### 表 A｜階段 J、A、B

| 階段 (Phases) | J 登入 | A 首頁 | B 公司 |
| :--- | :--- | :--- | :--- |
| **User Actions**<br>(用戶行為) | 登入前試搜人才 → 登入 → 雙重驗證（Email 連結）→ 忘記帳號／密碼時重設<br>[試搜](https://hackmd.io/@1111-jobdocs/Sk4CnTjgMg)、[登入](https://hackmd.io/@1111-jobdocs/rych3fo0bl)、[雙重驗證](https://hackmd.io/@1111-jobdocs/ryqrsG2lWg)、[忘記密碼](https://hackmd.io/@1111-jobdocs/HJT3dH_vWg) | 看快訊與刊登狀態 → 點近期修改職缺 → 看今日面試／匯出行事曆 → 人才秒搜<br>[A.2&A.3](https://hackmd.io/@1111-jobdocs/Bye3E5tl-g)、[A.4](https://hackmd.io/@1111-jobdocs/HJIK-sUGbe)、[A.5](https://hackmd.io/@1111-jobdocs/B1MejWhvGl)、[A.10](https://hackmd.io/@1111-jobdocs/BkIIbQYfWe) | 填基本資料 → 形象／工作環境／產品服務／福利／更多介紹 → 上傳面試須知 → 選版型 → 預覽送審；取公司頁 QR Code；開副帳號、設通知與權限、群組、聯絡人、刊登設定<br>[B.1](https://hackmd.io/@1111-jobdocs/S1jhD6RRbe)、[B.1.3](https://hackmd.io/@1111-jobdocs/SkztPlKsbx)、[B.2](https://hackmd.io/@1111-jobdocs/SkfafU2WZg)、[B.4](https://hackmd.io/@1111-jobdocs/ryEY3vBZbl) |
| **Touchpoints**<br>(接觸點) | login.aspx、AgentVerify.aspx、AgentVerifyCheck.aspx（Sitemap 第1節） | 首頁；Topbar（公告、通知、帳號選單、異常狀態列）（Sitemap 第2節）<br>[A.1](https://hackmd.io/@1111-jobdocs/Hym116n3-x)、[A.1.7](https://hackmd.io/@1111-jobdocs/SkJEsXNWMx) | /company/\*、/settings/\*、VipSchedule.aspx、PublishEmpGroup.aspx（Sitemap 第3節） |
| **Thoughts**<br>(內心 OS) | 〔推論〕「我沒有信箱，怎麼驗證？」依據：客服反映部分廠商沒有信箱，無法通過現行驗證 [同步會議 2026.04.08](https://hackmd.io/@1111-jobdocs/Sk8KaX73Wl) | NULL | NULL |
| **Emotions**<br>(情緒感受) | 🤔 困惑〔推論〕依據同上 | NULL | NULL |
| **Pain Points**<br>(痛點/摩擦力) | 部分廠商沒有信箱，新驗證機制造成登入困難（客服反映）[來源](https://hackmd.io/@1111-jobdocs/Sk8KaX73Wl) | 會員／刊登異常不易察覺（異常狀態列存在的理由）US [A.1.7](https://hackmd.io/@1111-jobdocs/SkJEsXNWMx) | 內部 IP 上傳的圖片有侵權風險，需對外下架 [B.1.4](https://hackmd.io/@1111-jobdocs/Sy6vKV4FZx) |
| **Opportunities**<br>(產品機會點) | 登入異常統一 Alert；登入前智能客服（每日 3 次）<br>[特殊狀態與Alert](https://hackmd.io/@1111-jobdocs/HJb5FnCGZg)、[智能客服](https://hackmd.io/@1111-jobdocs/Hy95Qz7g-e) | Topbar 通知收斂為只剩來訪人才（第三階段）[來源](https://hackmd.io/@1111-jobdocs/Hk3SOQrFfg) | 三種新增帳號方式（含複製帳號）；刊登設定取代開關天數設定<br>[功能說明頁](https://hackmd.io/@1111-jobdocs/rynOybVWZx)、[新增帳號Modal](https://hackmd.io/@1111-jobdocs/rkciNnFHMg) |
| **Metrics**<br>(衡量指標) | 〔推論〕登入成功率（含雙重驗證完成率）；依據：雙重驗證為登入必經步驟 | 〔推論〕首頁區塊點擊率（職缺、面試行事曆）；依據：首頁以入口導流為主 | 〔推論〕公司資料完成度；依據：B.1 設有填寫進度條 |

### 表 B｜階段 C、D、E

| 階段 (Phases) | C 職缺 | D 人才 | E 聯繫 |
| :--- | :--- | :--- | :--- |
| **User Actions**<br>(用戶行為) | 快速新增／複製／全新／匯入職缺 → 設應徵過濾 → 總覽多筆操作（更新日期、開關、改工作時間）→ 排序、移轉、排廣告<br>完整流程（循序圖）：[2.2 新增職缺＞流程圖](https://hackmd.io/@1111-jobdocs/S1SfBeXxfe#流程圖)<br>[2.2](https://hackmd.io/@1111-jobdocs/S1SfBeXxfe)、[複製](https://hackmd.io/@1111-jobdocs/HJW-MWp4Wg)、[匯入](https://hackmd.io/@1111-jobdocs/Bk854rrtGe)、[應徵過濾](https://hackmd.io/@1111-jobdocs/r1AirkvF-x)、[2.1 總覽](https://hackmd.io/@1111-jobdocs/HJvxSmNMWe)、[多筆修改](https://hackmd.io/@1111-jobdocs/HkHIwU8Y-x)、[2.3](https://hackmd.io/@1111-jobdocs/B1Srfpi7bg)、[2.4](https://hackmd.io/@1111-jobdocs/rJ5KsWEG-e)、[2.7](https://hackmd.io/@1111-jobdocs/Sy7bgNuzZg) | 看主動應徵 → 開履歷詳細頁 → 追蹤／備註／封鎖／轉寄／列印 → 看來訪名單 → AI 推薦／配對／簡易／進階／大專搜尋<br>[3.1.1](https://hackmd.io/@1111-jobdocs/ry9S7kjuWe)、[履歷詳細頁](https://hackmd.io/@1111-jobdocs/HyYq_GgXWl)、[追蹤人才](https://hackmd.io/@1111-jobdocs/r1V8b3ZDWg)、[備註](https://hackmd.io/@1111-jobdocs/rkX_P2qqZl)、[轉寄](https://hackmd.io/@1111-jobdocs/ByoEYp2a-g)、[列印](https://hackmd.io/@1111-jobdocs/SJMq3nfkGe)、[3.2.6](https://hackmd.io/@1111-jobdocs/r1TBqJjeGx)、[3.2.1](https://hackmd.io/@1111-jobdocs/Bk06kDtf-l)、[3.2.3](https://hackmd.io/@1111-jobdocs/Syn7AN87Wl) | 開通知 Lightbox → 選範本 → 發詢問意願／面試邀約 → 聊天室對話 → 建立／改期／取消面試 → 錄取通知；求職者失約時回報<br>[4.0](https://hackmd.io/@1111-jobdocs/r1qJb-uXbx)、[範本](https://hackmd.io/@1111-jobdocs/SJ8KDMo8fl)、[4.1](https://hackmd.io/@1111-jobdocs/rJkyKgeGWl)、[信件對話](https://hackmd.io/@1111-jobdocs/r1ghrPxP-x)、[第二階段](https://hackmd.io/@1111-jobdocs/ry_GPNuZze)、[4.3](https://hackmd.io/@1111-jobdocs/HydajKbPfl)、[失約回報](https://hackmd.io/@1111-jobdocs/Sy70gCPKGe) |
| **Touchpoints**<br>(接觸點) | PublishList／PublishOpening／PublishEmpSort／PublishEmpTrans／BuyScheduleBooking.aspx（Sitemap 第4節） | ResumePool\*.aspx、ResumeSearch\*.aspx、ResumeDetailShow.aspx（Sitemap 第5節） | ResumePoolNoticeMail(Detail).aspx、Exemplar.aspx、oInterView.aspx、SMS.aspx、右下角即時通面板（Sitemap 第6節）[即時通面板](https://hackmd.io/@1111-jobdocs/SJsYLtmr-g) |
| **Thoughts**<br>(內心 OS) | 〔推論〕「別家已經刊過了，為什麼要重打？」依據：匯入提案 User Story 要把其他人力銀行職缺直接匯入 [來源](https://hackmd.io/@1111-jobdocs/BJATOLPwbx) | 〔推論〕「誰關注了我？數字怎麼對不上？」依據：關注名單設計理念要避免廠商抱怨數字不一致 [來源](https://hackmd.io/@1111-jobdocs/B1jNIrMBZl) | 〔推論〕「回了怎麼還算沒回應？」依據：即時通與信件分開判斷，廠商抱怨限時回應 [來源](https://hackmd.io/@1111-jobdocs/SJJY3isYZe) |
| **Emotions**<br>(情緒感受) | 😤 挫折〔推論〕依據同上 | 😤 挫折〔推論〕依據同上 | 😤 挫折〔推論〕依據同上 |
| **Pain Points**<br>(痛點/摩擦力) | 在其他人力銀行已刊登的職缺要手動重建 US [來源](https://hackmd.io/@1111-jobdocs/BJATOLPwbx) | 來訪名單無法過濾（狀態、日期、性別、年齡）；追蹤名單不能直接刪除；看不到誰關注公司／職缺<br>US [來訪拉皮](https://hackmd.io/@1111-jobdocs/SJ5oUbXv-g)、[追蹤人才](https://hackmd.io/@1111-jobdocs/r1V8b3ZDWg)、[關注名單](https://hackmd.io/@1111-jobdocs/B1jNIrMBZl) | 兩套工具各自溝通、副帳號通知兩組設定；勾「希望 N 天內回覆」後訊息未顯示期限；範本不能排序置頂；求職者失約<br>[SJJY3isYZe](https://hackmd.io/@1111-jobdocs/SJJY3isYZe)、[信件對話](https://hackmd.io/@1111-jobdocs/r1ghrPxP-x)、US [E.2.1](https://hackmd.io/@1111-jobdocs/HyDIQwJUWg)、US [失約回報](https://hackmd.io/@1111-jobdocs/Sy70gCPKGe) |
| **Opportunities**<br>(產品機會點) | 職缺匯入；AI 職缺審核<br>[匯入提案](https://hackmd.io/@1111-jobdocs/BJATOLPwbx)、[AI審核提案](https://hackmd.io/@1111-jobdocs/B1bkIvMhZx) | 關注名單（數字與名單一致）；來訪名單過濾<br>[關注名單](https://hackmd.io/@1111-jobdocs/B1jNIrMBZl)、[來訪拉皮](https://hackmd.io/@1111-jobdocs/SJ5oUbXv-g) | 信件＋即時通整併、訊息收回、已讀、附檔；詢問意願與面試邀約拆開；同意面試後自動建立行事曆<br>[SJJY3isYZe](https://hackmd.io/@1111-jobdocs/SJJY3isYZe)、[各階段內容](https://hackmd.io/@1111-jobdocs/r1eNVEfmMx)、[第三階段](https://hackmd.io/@1111-jobdocs/Hk3SOQrFfg) |
| **Metrics**<br>(衡量指標) | 〔推論〕職缺建立完成率、匯入使用率；依據：提案以「不需手動建職缺」為價值 | 〔推論〕來訪名單→聯絡轉換率；依據：來訪名單 User Story 目的是「主動接觸有意願的人才」 | 面試邀約使用率（文件預期會增加）、限時回應達成率〔推論〕；依據：[SJJY3isYZe](https://hackmd.io/@1111-jobdocs/SJJY3isYZe) 載明預期面試邀約使用率增加、回覆主投者皆計入限時回應 |

### 表 C｜階段 5、6／7（支援）

| 階段 (Phases) | 5 紀錄 | 6 服務／7 購買（支援，任何階段可插入） |
| :--- | :--- | :--- |
| **User Actions**<br>(用戶行為) | 看帳號邀約紀錄 → 履歷瀏覽紀錄 → 帳號使用／購買紀錄 → 數據統計 → 人才點數<br>[5.1](https://hackmd.io/@1111-jobdocs/rJ5Bp4RE-g)、[5.3](https://hackmd.io/@1111-jobdocs/S1-Wt68M-e)、[5.6](https://hackmd.io/@1111-jobdocs/SJeZiGSMbx)、[5.5](https://hackmd.io/@1111-jobdocs/S13Zy8rKze)、[記錄管理](https://hackmd.io/@1111-jobdocs/Sk4AvcZ-We) | 續約 → 購買優先排序／簡訊加值 → 上傳合約；下載文件、填滿意度、問智能客服<br>[7.1](https://hackmd.io/@1111-jobdocs/ByKdpLaWZe)、[7.2](https://hackmd.io/@1111-jobdocs/HJzsieKfWe)、[H.3](https://hackmd.io/@1111-jobdocs/HJD1Eu0c-e)、[A.7.1](https://hackmd.io/@1111-jobdocs/Sk5kyX6ubx)、[6.8](https://hackmd.io/@1111-jobdocs/S1fR49Fg-l) |
| **Touchpoints**<br>(接觸點) | Log\*.aspx（Sitemap 第7節） | vipContract.aspx、BuyExposure.aspx、SMSorder.aspx、/download、外部連結（Sitemap 第8、9節） |
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
| 6／7 服務購買 | 服務／購買 | Sk5kyX6ubx、S1fR49Fg-l、ByKdpLaWZe、HJzsieKfWe、HJD1Eu0c-e、Hy95Qz7g-e、SJtErv_lZl、rynOybVWZx |

**跨階段共用元件**（不屬單一階段）：無權限Alert ryACpaCAWe、帳號選擇 S13ZYP9jbg、群組選擇 ByhoS3trGg、職缺選單 r1jXRIzqGg、現版職缺選擇 BkxSWZuGWx、通訊錄 B1iOzIB9-e、新增封鎖 H1guSxywZe、代碼參考 B1j3sN-bzx／ryjSpM-tzg。

---

### 缺口（寫 journey 時發現）

- 約 30 份文件的 User Story 是套版句「以便提高求才效率」，沒有寫出真正動機（如 A.2、A.4、5.x、3.2.x、7.x）——這些階段的「目標」只能標 US*。
- 全部文件都**沒有情緒／想法**的記載（沒有訪談或可用性測試資料），情緒曲線只能從「抱怨」「客服反映」推。
- `紀錄` 階段沒有任何痛點或動機記載。
- Sitemap 上沒掛文件連結、這次也沒找到對應規格的頁面：公司相關訊息、上傳檔案、職缺同步、自動更新、職缺所屬群組、匯入名單、還原刪除履歷、問題履歷回報、即時通記錄、簡訊通知紀錄、帳號使用紀錄（除購買紀錄外）。
