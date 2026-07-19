<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

# Session 交接包 — 信件訊息頁（ResumePoolNoticeMail）切版

> 本檔是給**新 session** 接手用的完整交接。讀完這份，新 session 不需要舊對話也能繼續。
> 產生時間：2026-06-23　工作分支：`claude/eloquent-maxwell-j31ot5`（PR #8）

---

## 0. 這個任務在做什麼

1111 求才（recruit）企業端「信件訊息」頁（`ResumePoolNoticeMail.aspx`）的**前端視覺改版**。
PM 給了一份「mock」（已被前一手 AI 調整過的 HTML/CSS）＋兩份對照文件，要把它整理成**給人類前端工程師看的需求文件**，並依設計稿（Figma）持續微調樣式。

**鐵則（整個任務的約束）**

1. **只改 CSS 值**達成視覺；**不改 HTML 的 DOM 結構 / class / tag 名稱**。
2. HTML 即使有明顯 typo 也**不自行修正**（會讓結構對不上正式環境）。
3. **字體一律微軟正黑體**（`"Microsoft JhengHei","微軟正黑體","新微軟正黑體",sans-serif`）；設計稿標 Noto Sans TC 也不採用；FontAwesome 圖示字型不要動。
4. **每次動到畫面（HTML/CSS），完成後一律重生一份自包含預覽 HTML 交付**（見 `CLAUDE.md` 的「UI/UX 工作慣例」）。

---

## 1. 四個檔案 + 兩份修改紀錄的關係（重點）

這個包裡有 **4 個程式檔** + **2 份修改紀錄**。先搞懂它們的關係再動手。

### 1.1 先認識「三個狀態」

| 代號 | 是什麼 | 在哪 |
| :--- | :--- | :--- |
| **P　正式環境原始** | 真正線上 `ResumePoolNoticeMail.aspx` 的 HTML | **未存檔**。使用者曾在對話貼出；其結構特徵記在 `01_…§2.5` |
| **B　before（mock 收到時）** | PM 給的 mock，**前一手已對 P 做過偏離**（搬節點、刪節點、拿掉 `data-*` 等） | `_migration/before/` |
| **A　after（現在）** | 在 B 之上，**我這輪做的視覺調整**後的狀態 | `_migration/after/` |

> ⚠️ 關鍵：`before` **不是**正式環境原始（P）。`before` 已經是被前一手動過的 mock（B）。
> 「mock 與正式環境（P↔B）的偏離」記在 `01_…§2.5`；「我這輪的改動（B↔A）」就是下面四個檔案的 diff。

### 1.2 四個程式檔

| # | 檔案 | 內容 | 行數 |
| :-- | :--- | :--- | :--- |
| 1 | `before/ResumePoolNoticeMail.html` | mock HTML（我動手前，B） | 267 |
| 2 | `after/ResumePoolNoticeMail.html` | mock HTML（現在，A） | 267 |
| 3 | `before/resumePoolNoticeMail.css` | mock CSS（B，原始 bundle） | 1629 |
| 4 | `after/resumePoolNoticeMail.css` | mock CSS（A，bundle＋我加的 override） | 1706 |

* **檔 1 ↔ 檔 2（HTML 的 B↔A）**：我對 HTML 只動過一次有效改動 — 把「有意願/無意願」兩列從 `.mail-type` inline 上色，**改回正式結構** `.td-status > p.wish-content.isWish/.isNoWish`（中間還經歷過 `#BF1212→#FF5D15` 的 inline 階段，最後被這次重構取代）。其餘 HTML 與 B 完全相同。
* **檔 3 ↔ 檔 4（CSS 的 B↔A）**：所有視覺調整都在這。after 比 before 多了檔尾一段 override 區塊（約 +77 行），外加幾處直接改原規則（hover、isNoWish 顏色等）。**逐條清單見 `02_…`**。

### 1.3 兩份修改紀錄

| 檔案 | 記什麼 |
| :--- | :--- |
| `01_HTML結構調整對照.md` | HTML 面：差異點（mock data、移除 icon、互動 JS、意願結構），以及 **§2.5 與正式環境（P）的結構偏離清單**（刪節點 / 移除 `data-*`·`onclick` / 位置搬移 / 意願改寫 / 新增節點）。註：意願偏離已於 2026-06-23 修正（見 §2.5 D）。 |
| `02_CSS樣式調整對照.md` | CSS 面：逐條 `selector ｜ 原值 → 新值 ｜ 來源檔 ｜ 性質 ｜ 原因`，A 區（直接改原規則）、B 區（override）、C 區（離線替身，**正式環境排除**）、D 區（轉譯指引、顏色清單）。 |

### 1.4 還有這些（在 `handoff/`，非本包但相關）

* `需求文件-ResumePoolNoticeMail.md` — **給工程師的最終需求文件**（求才 template、白話、逐標籤、附 CSS 檔名行號）。目前 v0.2.2，已發佈到 HackMD（`@1111-jobdocs/S1cYFSFfzx`）。
* `preview-tab-underline.html` — 自包含預覽（把 after CSS 內嵌進 after HTML）。每次改動都要重生。

---

## 2. 改動時間軸（每個 commit = 一個需求）

| commit | 做了什麼 |
| :--- | :--- |
| `65c2850` | 頁籤改**底線式 Tab**（依設計系統，CSS-only；底線用 `li.active::after`） |
| `f894345` | 頁籤**併入篩選便當**（CSS 合併成一張卡）＋表頭列 `.th` 上下 padding 12px |
| `b34608a` | 無意願文字色 `#BF1212 → #FF5D15`（當時是 `.mail-type` inline） |
| `269002e` | CLAUDE.md 新增「每次改動都要產生自包含預覽 HTML」慣例 |
| `b9b4d8e` | 標題「信件訊息」28px/Medium #212529；「共127筆」16px #495057 |
| `f9dbc6d` | 資料列 hover：**移除邊框/陰影**，改純底色 `#FFF7F7` |
| `1fc9921` | **更正紀錄**：據實記錄與正式環境的結構偏離（不動 HTML） |
| `70680f2` | 新增**需求文件**（求才 template，逐標籤＋CSS 檔名行數） |
| `d373fa4` | 字體統一**微軟正黑體**（移除 Noto Sans TC） |
| `1e0a63d` | 需求文件**改寫白話** + §3 改為明確「HTML 搬移」指示 |
| `76efa55` | §11 意願標籤改為明確結構指示（白話＋HTML 範例） |
| `81a0248` | **mock 意願改用正式結構** `.td-status > wish-content`（消除偏離）→ 需求文件 v0.2.2 |

---

## 3. 目前每個區塊的最終狀態（after）

對應 `需求文件` 的章節（CSS 行號為 after 檔 1706 行版）：

| 區塊 | 最終樣式 | CSS 行 |
| :--- | :--- | :--- |
| 標題 `.headingBar .Title` | 微軟正黑體 28px/500 #212529 | 1686–1693 |
| 頁籤 `.tabs/.tab` 底線式 | default #212529 / hover #1a66ff / active #1a66ff+4px 底線 | 1634–1678 |
| 頁籤+篩選便當合併 | titleBar 上圓角10px+陰影 / filter 下圓角10px | 1640 / 1647 |
| 筆數 `.msgRecord` | 微軟正黑體 16px/400 #495057 | 1696–1705 |
| 批次按鈕 | 移除 icon（HTML）、自然寬置中、勾選才顯示 | 1619 / 1628 / 1631 |
| 篩選輸入框群 | 邊框/hover/focus 統一 | 1442 / 1467 / 1477 |
| 卡片留白 | `.whiteBg.list` padding `0 0 20px 0`、`.whiteBg` margin 0 | 1428 / 1565 |
| 表頭 | 底 #E3ECFD 字 #0D2760、`.th` 上下 padding 12px | 1388 / 1682–1683 |
| 列 hover | box-shadow:none、bg #FFF7F7 | 921–927 |
| 訊息欄 | p margin 0、bdi padding 2px、紅點 10px | 1596 / 1386 / 1496 |
| 意願 | `.td-status > p.wish-content.isWish #1D880D / .isNoWish #FF5D15` | 980 / 983 |
| 內文 16px 群 | 多 selector | 1529 起 |

---

## 4. 待辦 / 卡住的事（交給新 session）

1. **HackMD 區塊對應任務（進行中、卡住）**
   * 使用者要把 `需求文件` 改成符合一份**已標好區塊編號的參考文件**的分區方式：
     * 參考文件（區塊編號）：`https://hackmd.io/@1111-jobdocs/rJkyKgeGWl`
     * 我方需求文件（要被改）：`https://hackmd.io/@1111-jobdocs/S1cYFSFfzx`（＝本地 `需求文件-ResumePoolNoticeMail.md`）
   * **卡點**：本環境 **egress 擋掉 `hackmd.io`**（連線失敗），讀不到 `rJkyKgeGWl`。需使用者把該文件內容貼上/上傳，或開放 egress。
   * 對應後要**列出對不到的項目**。
2. **before/after 截圖編號**：使用者稍後會給「修改前 / 修改後」兩張畫面截圖，要直接在圖上**標上區塊編號**（before/after 各一），編號需與參考文件 `rJkyKgeGWl` 一致。
3. （可選）把其他仍存在的「mock↔正式」偏離也比照意願那樣**修正 mock**（清單見 `01_…§2.5`：`h1.titleFont`、被拿掉的 `data-*`/`onclick`、頁籤位置搬移等）。

---

## 5. 重要慣例與約束（務必沿用）

* **只改 CSS、不改 HTML 結構/class/tag**；HTML typo 不自行修。
* **字體微軟正黑體**（見 §0.3）。
* **每次動畫面就重生自包含預覽**（把 `<link>` 換成內嵌 `<style>`，輸出預覽檔，SendUserFile 交付）。
* **mock 偏離要據實記錄**，別宣稱「結構零改動」未經查證；偏離若會誤導工程師，優先**把 mock 修正成正式結構**（像意願那次），勝過留「請別學我」警語。
* **需求文件給人看不是給 AI 看**：白話、逐標籤、CSS 標檔名行號、結構前提用明確指示（🔧）而非開放式提問。
* CSS 整併：override 區塊在 after 檔尾、帶 `!important`；**正式環境**可整併進原 selector 並拿掉 `!important`，且**排除 C 區離線替身**（FontAwesome CDN、inline SVG）。

---

## 6. 環境限制（新 session 同樣會遇到）

| 限制 | 影響 | 對策 |
| :--- | :--- | :--- |
| 無 `HACKMD_TOKEN`、egress 擋 `hackmd.io`/`api.hackmd.io` | 無法讀寫 HackMD | 請使用者貼內容/上傳；或開放 egress + 設 token 後重開 session |
| 無無頭瀏覽器（playwright 下載被擋） | 無法自動截圖 | 改交付**自包含預覽 HTML**，請使用者自行開啟 |
| Figma MCP 可用 | 讀設計稿正常 | `get_design_context` + `get_variable_defs` 抓 token |

---

## 7. 新 session 怎麼接手

1. 讀本檔 → 讀 `01_`、`02_` 兩份紀錄 → 讀 `需求文件-ResumePoolNoticeMail.md`。
2. 要改樣式：改 `handoff/_files/resumePoolNoticeMail.css` → 重生 `preview-tab-underline.html` → 更新 `02_`／需求文件 → commit/push。
3. 要對 HackMD 區塊：先請使用者提供 `rJkyKgeGWl` 內容（egress 擋著）。
4. 經驗法則都封裝在 skill：`.claude/skills/frontend-slicing-1111/`（見其 `SKILL.md`）。
