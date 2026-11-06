# 04 — 已知事實總表

> 格式：事實｜來源（檔名或對話日期）｜狀態（現行／已被推翻／待確認）。本檔只收「本 KB 分支」範圍內可追溯的事實，Perry／主要專案端的實際落地狀態以官方匯出檔為準，本 KB 只能回報「KB 這邊觀察到的結果」。

## tCode 總表現況（15 張表）

| 事實 | 來源 | 狀態 |
|---|---|---|
| `TCode_Export.xlsx` 共 15 張工作表，schema 共用（見 `01-schema.md`） | `00-tcode-index.md` | 現行 |
| tCodeBenefit／Certify／CompSkill／DutyHL／DutyNM／DutyPT／DutyST／Major 八表已於 20261102 依官方最新匯出更新 | `00-tcode-index.md`、commit `79ab04f`（2026-11-02） | 現行 |
| City／College／DutyTU／MRT／Nation／Trade／WorkAbility 七表未收錄於 20261102 這批，維持原狀未變動（即該批匯出沒有重新整批匯出這 7 表，但 WorkAbility 的 310000 新增大類是另一條獨立確認路徑，見下方「2026-11-06 批」） | `00-tcode-index.md` | 現行 |
| tCodeDutyNM：644 列／567 葉／58 中類（20 大類） | `00-tcode-index.md`（20261102 更新後數字） | 現行 |
| tCodeDutyHL：136 列／78 葉／42 中類（18 大類） | 同上 | 現行 |
| tCodeDutyPT：576 列／499 葉／59 中類（20 大類） | 同上 | 現行 |
| tCodeDutyST：273 列／206 葉／48 中類（20 大類） | 同上 | 現行 |
| tCodeCertify：2,621 列／2,451 葉／149 中類（index 標示數字，**未反映 2026-11-06 批新增的 12 筆**，見下方「資料層副本落後現況」） | `00-tcode-index.md`；`data_tCodeCertify_summary.md` 標頭核對一致（2451 葉） | **待確認／可能過期**：index 數字與 data 檔案一致，但兩者都可能落後於已確認套用的最新批次 |
| tCodeWorkAbility：1,207 列／1,092 葉／94 中類（index 數字） vs `data_tCodeWorkAbility_summary.md` 標頭寫 1093 葉／21 大類 | `00-tcode-index.md` vs `data_tCodeWorkAbility_summary.md`——**兩個數字本身就對不上（1092 vs 1093）**，且都不包含 2026-11-06 新增的 310000（14 筆） | **待確認**：兩份文件彼此矛盾，且均未反映最新批次 |
| tCodeBenefit：95 列／85 葉／10 中類／CodeType 只有 1/2（無第 3 層） | `00-tcode-index.md` | 現行 |

## 資料層副本落後現況（重要，影響所有查詢）

| 事實 | 來源 | 狀態 |
|---|---|---|
| `data_tCodeCertify_summary.md` 查不到 2026-11-06 批新增的代碼（如 `185912`、`183101`） | 本次打包時實測 `grep`（2026-11-06） | **現行**（這是本次打包新發現，過去的文件沒有記錄這個落後） |
| `data_tCodeWorkAbility_summary.md` 查不到「310000」「310101」等新代碼 | 同上 | **現行**（同上） |
| tCodeDutyHL 的「160203 製程主管 → 160206 生產技術／製程工程師」整併（2026-11-06 批提出）是否已反映進 `data_tCodeDutyHL.md`——**未核對，待確認** | 無 | **待確認** |
| 一般性鐵則：KB 的資料層副本更新時機落後於官方流程，要等 Perry 排程、主要專案套用後才重建，不是異動一提出就同步 | `04-change-workflow-sop.md`〈二、本 KB 在這個流程裡的角色〉 | 現行（設計如此，非 bug） |

## 已執行過的異動輪次（依時間序，僅列本 KB 分支內可追溯者）

| 輪次 | 內容摘要 | 來源 | 狀態 |
|---|---|---|---|
| 20260622／20260707 | 各表 ChangeType 全為 `UnChange`（該欄位不會自己標記異動） | `00-tcode-index.md`〈注意〉 | 現行（歷史紀錄） |
| 20260701（Google Sheet 即時匯出） | tCodeDutyNM 38 筆、DutyPT 38 筆、DutyST 24 筆、DutyHL 7 筆的 ADD/EDIT 清單 | `change_request_tCodeDuty_engineering.md` | 現行（已於 20260707 確認套用，見下一列） |
| 20260707 | 官方匯出 `TCode_Export_20260707T090934846Z.xlsx` 到貨，逐筆以 `Old_CodeNo` 核對確認 20260701 批已正式套用；同時發現 2 項資料問題（見下方「尚未結案的待辦」） | `change_request_tCodeDuty_engineering.md`〈✅ 20260707 更新〉 | 現行 |
| 20260821 | tCodeDuty 系列大量 move／move_edit／add／edit 驗收檔（HL 2 筆、NM 多達 45 筆 move 等），排除 5 筆延後項目（170204→160213、190205→190206、190207→190201、230110→230111、270202→270201） | `20260821_change_summary.md` | 現行（歷史驗收紀錄） |
| 20261013 | 上述延後的 5 筆整併案 + DutyHL 的 190201→工地監工／主任、270201→餐飲主管／領班 改名，當時只在工程師「異動申請」預覽畫面看過，尚未送審 | `change_request_tCodeDuty_engineering.md`〈✅ 20261102 複查〉提及 | 已套用（見下一列） |
| 20261102 | 官方最新匯出（8 表）到貨，複查確認 20261013 批已正式套用：DutyHL 2 筆改名已套用；DutyNM/PT/ST 五組整併（170204→160213、190207→190201、190205→190206、230110→230111、270202→270201）消失代碼確認正確歸位、無遺漏；tCodeBenefit 95 筆中類全數改為新名，cascade 問題已解決 | `change_request_tCodeDuty_engineering.md`〈✅ 20261102 複查〉、commit `79ab04f` | 現行 |
| 2026-11（AI 證照調查） | 使用者提供 15 項 AI 相關證照名稱清單，要求逐一上網 survey 並核對 `tCodeCertify` 是否已有或已改名；本 KB 一度誤判「AI+行銷科技專業人員」不存在，經使用者提供來源 URL（`https://www.iiiedu.org.tw/certifications/exam/4`）後確認為真（資策會/III，6 domains，50Q/60min/70pass/NT$1,300） | 對話紀錄，無獨立檔案留存（原本建立的 `change_request_tCodeCertify_AI_certs.md` 已依使用者指示刪除，見 `03-document-map.md`） | 已被部分推翻：本 KB 最初對這張證照「不存在」的結論**已被推翻**，正確結論是「存在」 |
| 2026-11-06 批（Certify） | 新增 10 項 AI 相關證照（TQC 拆 3 級共 12 筆代碼）＋ 2 筆 Microsoft 證照改名（180519／180538），使用者確認「工程師端已套用」 | scratchpad `tcode_change_request_20261106.md`（**不在 repo 內**，見 `03-document-map.md`） | 使用者口頭確認已套用，但 KB 資料層副本（`data_tCodeCertify_summary.md`）尚未反映，見上方「資料層副本落後現況」 |
| 2026-11-06 批（DutyHL） | 「160203 製程主管」整併入「160206 生產技術／製程工程師」，**待工程師套用**（NM/PT/ST 這輪沒有對應異動，僅 HL 這一筆） | 同上 scratchpad | **待確認是否已套用**（上一批狀態是「待套用」，之後是否已確認未知，見 `07-open-questions.md`） |
| 2026-11-06 批（WorkAbility） | 新增「310000 AI 能力」大類共 14 項（310101~310503），使用者確認「工程師端已套用」；原規劃與 9 筆既有代碼（140212/140213/140214/140215/140216/140218/140219/140222/140226）合併，**後來裁定改為不合併、兩邊並存**，9 筆舊代碼維持原樣不動 | 同上 scratchpad；裁決過程見對話紀錄（「再檢查一次 不合併了 只新增」） | **已被推翻一次**：最初規劃是「搬移/合併」，後改為「純新增、不合併」。目前的正確狀態是**不合併**，不要誤用較早的合併對照表 |
| 2026-10-21（主幹） | main 把 `tcode-bulletinboard` skill 併入 `tcode-excel-ops`（main commit `6777841`），完整規則轉移到 `.claude/skills/tcode-excel-ops/references/bulletinboard-rules.md` | `.claude/skills/tcode-excel-ops/SKILL.md` 歷史、本分支 commit `d633f3a` | 現行 |

## 使用者做過的裁決（會影響後續判斷邏輯，容易被誤用舊版）

| 裁決 | 來源 | 狀態 |
|---|---|---|
| 核對異動時不信任單一文件的 ChangeType 欄位，要用「修改前 vs 修改後」兩份獨立檔案逐列比對 | 對話紀錄，已寫入 `bulletinboard-rules.md`〈資料來源鐵則〉 | 現行，已成為鐵則 |
| 一對多合併，每個被合併的舊代碼各自一筆 `move`，不可合併成一筆 | 對話紀錄（WorkAbility 案例時重申） | 現行，已寫入 `02-iron-rules.md` |
| WorkAbility「310000 AI 能力」大類最終裁定：**不與既有 9 筆代碼合併，純新增、兩邊並存** | 對話紀錄「再檢查一次 不合併了 只新增」 | 現行，**取代了更早的「9 筆合併進 4 個新代碼」規劃**——若看到任何文件還在講這 9 筆要合併，那是舊版，以本條為準 |
| 刪除的代碼要在公告裡交代被併入哪一個項目（刪除／合併對照要合併成同一張表，不要拆成分開的表） | 對話紀錄 | 現行，已反映在 `tcode-excel-ops` 公告格式裡 |
| 一次性輸出（調查結果、給工程師的需求表）預設不進 repo，只用 scratchpad + 直接貼在對話裡，除非使用者明確要留存 | 對話紀錄（「刪掉這個檔案這個output不需要在repo 你直接秀給我就好」） | 現行，已是本 KB 的輸出慣例 |

## 公告已發／未發的狀態

| 批次 | 公告狀態 | 來源 | 狀態 |
|---|---|---|---|
| 20260707／20260821／20261013／20261102 各批 | 本 KB 只確認「工程端已套用」，**沒有**記錄對應的對外公告是否已發布（公告發布由企劃／維運負責，不在 KB 追蹤範圍內） | 無 | **未知**，見 `07-open-questions.md` |
| 2026-11-06 批（Certify／WorkAbility） | 使用者標記「已確認工程師端已套用，供留存紀錄」，公告狀態未知 | scratchpad `tcode_change_request_20261106.md` | **未知** |
| 2026-11-06 批（DutyHL 160203→160206） | 標記「待工程師套用」，顯然尚未發公告 | 同上 | 待套用，未發公告 |

## 尚未結案的待辦

| 待辦 | 來源 | 狀態 |
|---|---|---|
| tCodeDutyPT 250513「其他語系教師」的 `New_CodeNo`／`CodeNo` 欄位被錯誤改成「麵點／港點師傅」／「餐飲烘焙」，但同列 `CodeNameA`／`CodeNameC` 仍是語言教學相關文字——欄位互相矛盾，疑似批次編輯複製貼上錯位 | `change_request_tCodeDuty_engineering.md`〈⚠️ 20260707 複查發現〉 | **待確認是否已修正**——20261102 複查只提到 Benefit 的 cascade 問題已解決，沒提到這個欄位矛盾問題是否已修正，見 `07-open-questions.md` |
| tCodeDutyNM／PT／ST 的 250500（教育師資→國教師資）、260300（補習進修→補教師資）中類改名，底下葉節點 `CodeNo` 參照未同步更新（cascade 未落地） | 同上 | **待確認是否已修正**，同上 |
| 140224、200307、200308 只在 tCodeDutyNM 出現 `EDIT`，看不出具體改了哪個欄位，異動內容待查 | `change_request_tCodeDuty_engineering.md`〈備註〉 | 待查，未結案 |
| tCodeDutyPT 250513（其他語系教師）已標記 `EDIT`，但 tCodeDutyNM 當時尚未套用（名稱本身一致，只是跨表沒同步） | 同上 | 狀態未知是否已跨表同步，見 `07-open-questions.md` |
