<!--markdownlint-disable MD013-->

# LINE Career Profile 填表指令（給 Antigravity）｜版本 r4 FINAL LOCKED

> 打包內容（同一資料夾）：**LINE 申請一律用 LINE Resume 版**：`line-resume.md`（定稿，人讀）、`line-resume.fill.json`（機器讀，**填表唯一內文來源**：表單欄位＋`summary_text`，**不含工作列點**）、`line-resume.pdf`（ATS 上傳用，含 Summary、Skills 與所有工作列點）、本檔。通用版 `line-profile.*` 只在使用者明說時才用。（操作規則）。
> 產生方式：`python3 career/scripts/gen_line_pack.py career/drafts/line/line-resume.md`（先跑 `verify_line_profile.py` 0 違規才會產出）。內文改動一律回上游重走管線，**不在填表端改**。
> 個資檔，不外流：不得貼到任何公開位置、不得上傳 HackMD。

## 一、最高鐵律（違反即中止）

1. **Zero Text Mutation**：所有欄位內文只取自 `line-resume.fill.json`，逐字填入。**禁止**在腳本內硬編碼任何履歷文字、改寫、摘要、補字、翻譯、調整標點或換行。
2. **寫入前後純文字斷言**：每個文字欄位寫入後，讀回 DOM 的純文字，必須等於 JSON 對應字串（去除首尾空白後逐字相同）。不相等就停止、不要儲存，回報步驟編號、欄位與差異。
3. **不碰送出**：絕對不按「Submit／送出／投遞／Apply／Finish」。每個區塊填完只按該區塊的「Save／儲存」，且按下前先停下來列出填了什麼，等使用者說「OK 儲存」。最後一步「整份送出」由使用者自己按。
4. **不碰登入與帳號**：不改密碼、通知、帳號設定，不上傳履歷檔或附件，不填 JSON 以外的任何欄位（例如薪資期望、國籍、性別、身分證、生日、社群連結、推薦人）——表單要求必填但 JSON 沒有時，**停下來問使用者**，不要猜。
5. **下拉選項用 value 比對，不用顯示文字**：JSON 的 `"1194"`、`"2559"`、`"215"` 等是表單選項的 value 代碼。找不到該 value 的選項、或選到後顯示的標籤與預期不符（例如 `country: 215` 應該是 Taiwan），停下來回報，不要選最接近的。
6. **不確定就停**：頁面與本檔描述不符（找不到欄位、跳驗證碼、版面不同、需要手機驗證），停下來描述畫面，不要自行變通。
7. **日期格式**：JSON 為 `YYYY-MM`。若表單要分開的年／月欄位，依 `-` 拆開；若表單要求日，**停下來問**，不要自己補 `01`。在職（`end_date` 為空字串）要勾「目前在職／Present」，且結束日期欄位留空。

## 二、開工前檢查（步驟 0）

1. 使用者提供：LINE 表單網址、是否已登入。**沒有網址就不要自己搜尋或猜網址**。
2. 讀 `line-resume.fill.json`，確認 `steps` 共 9 步，記下 `source_sha256`（回報時附上）。
3. 開啟表單，確認頁面有這幾個區塊：Basic & Contact Information、Work Experience（Dataset 155）、Education History（Dataset 157）、Languages（Dataset 257）。缺任何區塊就停下來回報。
4. 列出表單上每個必填欄位，與 JSON 欄位對照；有對不上的，統一列給使用者，**不要邊填邊問**。

## 二之一、內容限制（2026-11-01 英文母語審視補充）

- 表單內文必須是純文字：`summary_text` 內的英文月份、`–`（en dash）可原樣貼入；若表單欄位拒收或亂碼，**停下來回報字元與欄位**，不要自行換成 `-` 或其他符號（Zero Text Mutation）。
- 由上游維持 ASCII 友善：避免 `→` 這類箭頭符號；若 JSON 出現，回報給 Claude 轉 Codex 改寫。
- **Profile 表單只填 Summary（`summary_text`）；工作列點只在 resume（PDF）**（本人 2026-11-01 裁定）。表單的工作經歷只填公司、職稱、聘僱型態、地點、起訖日；描述欄位**留空**，不要貼列點。Skills 只在 PDF。表單若有 Summary／About 欄位才填 `summary_text`；找不到對應欄位就停下來回報，不要塞進其他欄位。
- 英文內容一律保持英文，不自動翻譯、不改標點、不改大小寫。

## 三、步驟（依 `steps[].step` 順序，一次一步）

| step | target_block | 動作 | 欄位來源 | 注意 |
| :-- | :-- | :-- | :-- | :-- |
| 0 | Summary | 填 `summary_text` | 頂層 `summary_text` | 只填 Summary／About 欄位；無此欄位就回報 |
| 1 | `basic` | `replace_all` | `fields`：email、mobile_phone、current_position_title、current_employer、country、address、city | `country`＝選項 value `215`；`address` 逐字，結尾不補句點 |
| 2 | `work_experience` index 0 | `replace_row` | `fields` | 在職：`end_date` 空，勾 Present |
| 3 | `work_experience` index 1 | `replace_row` | 同上 | |
| 4 | `work_experience` index 2 | `replace_row` | 同上 | |
| 5 | `work_experience` index 3 | `replace_row` | 同上 | `employment_type` 是 `1195`，與前三筆 `1194` 不同 |
| 6 | `education` index 0 | `replace_row` | `fields` | 淡江 |
| 7 | `education` index 1 | `replace_row` | `fields` | CSU Sacramento；`degree_status` `2559`、`type_of_degree` `21` 依本人口徑 |
| 8 | `languages` index 0 | `replace_row` | `fields` | English，四項能力皆 `1174` |
| 9 | `languages` index 1 | `replace_row` | `fields` | Mandarin，四項能力皆 `33` |

- `replace_row` 的意思：第 `index` 筆已有資料就覆蓋；沒有就新增一筆，順序要與 `index` 一致（0,1,2…）。表單原本有多餘舊筆時，**不要刪除**，停下來問使用者。
- **工作經歷描述欄位**：留空（列點只在 PDF resume）。若表單把描述設為必填，停下來回報，不要自行填入。
- 所有英文內容保持原樣，**不要自動翻成中文、不要拼字修正**；表單若觸發自動校正，把校正結果還原。

## 四、儲存與回報流程

1. 每完成一個 step：讀回該區塊所有欄位，做純文字斷言。
2. 斷言通過 → 在對話中列出「step N：欄位＝填入值（前 40 字）」，**等使用者說 OK**，再按該區塊的 Save。
3. 全部 9 步完成後，回報：
   - 完成的 step 清單與 `source_sha256`。
   - 跳過、停下來或需要使用者補的欄位清單。
   - 表單上有但 JSON 沒有、而你沒有填的欄位清單。
4. **不要按最後送出**；請使用者人工檢查整份預覽後自己送出。

## 五、停止條件（立刻停下並回報）

- 任一斷言不相等。
- 要求手機／Email 驗證碼、CAPTCHA、同意條款勾選。
- 表單欄位的選項 value 與 JSON 對不上。
- 字數超限。
- 需要刪除表單上既有資料。
- 看到與本檔不符的畫面或錯誤訊息。

## 六、給使用者的啟動指令（貼給 Antigravity）

```text
請先讀同資料夾的 line-fill-playbook.md 與 line-resume.fill.json，照 playbook 填 LINE Career Profile。
表單網址：<貼上網址>
我已登入。每個區塊填完先讓我確認再按 Save，全程不要按最後送出。
遇到 playbook 第五節任何停止條件，立刻停下來回報。
```
