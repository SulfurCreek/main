# ROUTES：改這個網站，先看這份

成品是單一自包含 HTML（`../recruiter_journey_report.html`），由 `parts/` 分區塊組出來。
**改哪個區塊，就只開那個區塊的檔案**；每個 parts 檔開頭有 `AI-NOTE`（建置時剝除，不進成品），寫了資料來源、依賴、禁忌。

```
grep -rn "@part:persona" parts/        # 一個區塊的全部檔案（css／html／js）
```

## 1. 我想改…（找區塊）

| 我想改… | 素材 md 章節 | 解析（`step1_parse_journey.py`） | 版面檔（`parts/`） | `DATA` key |
| :--- | :--- | :--- | :--- | :--- |
| 標題、lead、素材說明 | 開頭＋「給沒有專案背景的讀者」 | `parse_intro()` | `hero.*` | `title`／`intro`／`head_bullets` |
| 路線圖（階段篩選）、迷你列 | 「階段讀法」表 | `parse_intro()` | `route.*` | `intro.stage_rows` |
| 分頁 Persona／Journey Map | — | — | `tabs.*` | — |
| Persona 總覽矩陣、P1~P7 卡、受限廠商、名詞 | `## 1. Persona` | `parse_persona()`（`stage_states()` 轉可走狀態） | `persona.*` | `persona` |
| 旅程看板（泳道、欄、Touchpoints） | `## 2. The Journey Grid` | `parse_grid()` | `grid.*` | `grid` |
| persona／階段如何連動看板 | — | — | `apply.js` | — |
| Sitemap 樹、對應文件、文件關係表 | HackMD Sitemap＋附錄〈文件關係〉 | `step0_fetch_sitemap.py`＋`parse_appendix()` | `sitemap.*` | `appendix.library` |
| 流程圖 | 〈流程圖索引〉＋各文件 `## 流程圖` | `step0`（渲染 SVG）＋`parse_appendix()` | `flows.*` | `flows` |
| 附錄（共用元件、缺口、待辦） | `## 附錄` | `parse_appendix()` | `appendix.*` | `appendix`／`todo` |
| 顏色、字體、間距 token | — | — | `core.css`（`:root` 三處：亮／系統暗／手動暗） | — |
| 手機版排版 | — | — | `responsive.css`＋各區塊 css | — |
| 標記徽章（US／US*／推論／NULL）、md 轉換 | — | — | `core.js` 的 `md()`／`MK` | — |

## 2. 資料與連動怎麼流

```
素材 md ──step1──▶ report_data.json ─┐
HackMD Sitemap／流程圖 ──step0──▶ sitemap_docs.json、flows/ ─┘
parts/* ──step2（依 MANIFEST 順序串接＋注入 DATA）──▶ ../recruiter_journey_report.html
```

前端狀態只有三個，全部連動走 `apply.js`：

| 狀態 | 宣告 | 改變它 | 影響 |
| :--- | :--- | :--- | :--- |
| `sel` 階段篩選 | `data.js` | `setSel(i)` | 路線圖、看板欄、Touchpoints、流程圖、Sitemap、文件表 |
| `pid` persona | `persona.js` | `setPersona(id)` | persona 卡、看板反灰（`applyPersona()`）、路線圖虛線 |
| 分頁 | `tabs.js` | `setTab(t)` | Persona／Journey Map 兩個 pane 顯示；下方共用區塊不動 |

新增一個「依階段變動」的區塊：寫 `renderX()`，加到 `setSel()` 最後一行。

## 3. 常見改動 SOP

| 情境 | 做法 |
| :--- | :--- |
| md 格式變了（解析壞掉） | 只改 `step1` 對應的 `parse_*()`；跑 `./build.sh`，看自檢輸出（空格應為 0） |
| md 內容更新 | `git fetch origin main && git merge origin/main`（共用檔衝突取 main）→ `./build.sh --test` |
| HackMD Sitemap／流程圖有更新 | `python3 step0_fetch_sitemap.py`（需 `HACKMD_TOKEN`）→ `./build.sh --test` |
| 新增一個區塊 | 在 `parts/` 加 `名稱.html/.css/.js`（開頭放 `AI-NOTE`），把名稱加進 `step2_build_report.py` 的 `CSS`／`HTML`／`JS` 清單；順序即輸出順序 |
| 新增分頁 | `tabs.html` 加按鈕與 pane、`tabs.js` 的 `setTab()` |
| 改 CSS 順序／JS 順序 | 先確認該區塊沒有依賴前面的宣告；改完跑 `--test` |
| 發布 artifact | `FRAGMENT=<路徑> ./build.sh --test`，再用 Artifact 工具發布該檔（同路徑＝同網址） |

## 4. 驗證

```
NODE_PATH=/opt/node22/lib/node_modules node tests/smoke.js        # 互動煙霧測試（失敗 exit 1）
NODE_PATH=/opt/node22/lib/node_modules node tests/shots.js <資料夾> # 1440 亮暗／390 截圖，逐張看
```

## 5. 不要做

- 不改 `../recruiter_journey_map.md`（只有文件助手能改；缺漏回報使用者）。
- 不省略 `NULL`、不替沒資料的格子補推論；`US`／`US*`／`〔推論〕` 與來源連結照原樣。
- 不要手改 `report_data.json`、`sitemap_docs.json`、`flows/`（生成物）。
- 痛點列在旅程看板上隱藏（使用者指示）；persona 卡的 Pain Points 依 md 註解要顯示。
- 不連外部資源（Google Fonts 例外，且必須有系統字體 fallback）。
