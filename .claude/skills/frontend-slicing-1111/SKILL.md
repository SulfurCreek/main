---
name: frontend-slicing-1111
description: >
  1111 求才/求職前端「切版視覺改版 → 工程師需求文件」流程的工作慣例。當任務是：拿到一份被調整過的頁面 mock（HTML/CSS）、
  要逐一盤點視覺/樣式更動、依 Figma 設計稿微調樣式、把改動整理成給人類前端工程師的需求文件、或要比對 mock 與正式環境 HTML 的結構差異時，使用本 skill。
  關鍵字：切版、改版、視覺調整、樣式對照、mock、handoff、CSS 對照表、底線式頁籤、便當卡片、需求文件、設計稿落地、before/after。
  本 skill 封裝的是「只改 CSS 不動結構、mock↔正式偏離稽核、自包含預覽、微軟正黑體字體規則、求才白話需求文件」這套做法。
  （需求文件的 HackMD 排版格式請另搭配 spec-doc-1111 skill。）
---

# 1111 前端切版／需求文件 工作慣例（frontend-slicing-1111）

把「設計稿 + 被改過的 mock」變成「工程師照著做就對的需求文件」。核心是**保守、可追溯、誠實記錄偏離**。

## 何時使用

- 拿到頁面 mock（HTML + 多支 CSS）＋對照文件，要轉成人類工程師可執行的視覺需求清單。
- 依 Figma 設計稿調樣式（顏色、字級、間距、頁籤、卡片…）。
- 要查「mock 跟正式環境差在哪」（結構/class/屬性）。
- 每次改完要給可預覽畫面。

## 鐵則（最常被忽略，先記住）

1. **只改 CSS 值達成視覺**；**不動 HTML 的 DOM 結構 / class / tag 名稱**（可搬位置，但本系列任務通常連搬都不搬）。
2. **HTML 即使有明顯 typo 也不自行修正** —— 會讓結構對不上正式環境、害結構跑掉。
3. **字體一律微軟正黑體**：`"Microsoft JhengHei","微軟正黑體","新微軟正黑體",sans-serif`。設計稿標 `Noto Sans TC` 也**不採用**；`Font Awesome` 是圖示字型、**不要動**。
4. **每次動到畫面（HTML/CSS），完成後一律重生「自包含預覽 HTML」並交付**（把 `<link>` 換成內嵌 `<style>`）。細節見 `reference/preview-and-figma.md`。
5. **mock 可能本來就偏離正式環境**（前一手 AI 動過）。動手前先稽核、據實記錄；別宣稱「結構零改動」未經查證。見 `reference/mock-vs-production-audit.md`。

## 標準流程

1. **盤點輸入**：mock HTML、mock CSS（通常是打包過的大 bundle）、既有對照文件、正式環境 HTML（若有）、Figma 連結。
2. **稽核 mock↔正式**（若有正式 HTML）：用 tag/class skeleton diff 找偏離，據實記錄；偏離若會誤導工程師，**優先把 mock 修正成正式結構**，勝過留「請別學我」警語。→ `reference/mock-vs-production-audit.md`
3. **抓設計 token**：Figma `get_design_context` + `get_variable_defs`，記下精確 hex / 間距 / 字級 token。→ `reference/preview-and-figma.md`
4. **改 CSS**：在 mock CSS 檔尾加 override 區塊（帶 `!important`）或直接改原規則；**排除離線替身**（FontAwesome CDN、inline SVG）。→ `reference/css-conventions.md`
5. **重生自包含預覽**並交付。
6. **更新兩份對照紀錄**：`01_HTML結構調整對照.md`（結構/偏離）、`02_CSS樣式調整對照.md`（逐條 selector｜原值→新值｜行數）。
7. **產需求文件**：求才 template、**白話、逐 HTML 標籤、CSS 標檔名行號**、結構前提用明確指示。→ `reference/requirement-doc-style.md`（HackMD 排版格式搭 `spec-doc-1111`）
8. **commit/push** 到工作分支，更新 PR；每個 commit 對應一個需求。

## 三個狀態別搞混

| 代號 | 是什麼 |
| :-- | :-- |
| P 正式環境原始 | 真正線上的 HTML（常常沒存檔，只能靠對話/紀錄描述） |
| B before | PM 給的 mock（**可能已被前一手偏離 P**） |
| A after | 你改完的 mock |

- `before/after` 的 diff = **你的改動（B↔A）**。
- `mock 與正式的偏離` = **P↔B**，記在 `01_…§2.5`。兩者不要混為一談。

## 參考檔（細節）

- `reference/css-conventions.md` — CSS override 策略、字體規則、離線替身排除、CSS 行號擷取法、常見改法（底線頁籤、便當合併、hover、意願結構）。
- `reference/mock-vs-production-audit.md` — 怎麼用 Python HTMLParser 做 tag/class skeleton diff、怎麼據實記錄偏離、何時該修 mock。
- `reference/requirement-doc-style.md` — 給工程師的需求文件寫法（白話、逐標籤、標記符號、結構前提指示）。
- `reference/preview-and-figma.md` — 自包含預覽產生法、Figma token 擷取、環境限制（無頭瀏覽器/HackMD egress）。

## 環境限制（常見）

- 多半**無頭瀏覽器不可用**（截不了圖）→ 交付自包含預覽 HTML。
- HackMD 常被 **egress 擋**（`hackmd.io`/`api.hackmd.io`）、且**無 `HACKMD_TOKEN`** → 需使用者貼內容/上傳，或開放 egress＋設 token 後重開 session。
- Figma MCP 通常可用。
