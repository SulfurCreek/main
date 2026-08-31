# html-anything 版型參考庫（外部匯入）

> 來源：[`nexu-io/html-anything`](https://github.com/nexu-io/html-anything)
> （Apache-2.0，commit `c312045`，2026-08-23 匯入；授權全文見同目錄 `html-templates-LICENSE`）
> 匯入範圍：`next/src/lib/templates/skills/` 下全部 81 個版型，**排除 4 個小紅書（xhs／xiaohongshu）相關版型**
> （`card-xiaohongshu`、`deck-xhs-pastel`、`deck-xhs-post`、`deck-xhs-white`），共 77 個。

## ⚠️ 這是版面參考庫，不能直接拿來用

原始版型是給另一個產品（本地 agentic HTML 編輯器）用的，每個都依賴外部 CDN：

- 圖表：Chart.js / ECharts（jsdelivr CDN）
- 字體：Google Fonts CDN（通常 3 個字族：英數/中文/等寬）
- 樣式：Tailwind CSS CDN

這**違反我們 `report-generator` skill §B 的自包含鐵律**（CSP 情境下無法載外部 CDN/字型/圖片；
報告要能離線開啟、pipeline 要能重跑出 byte-identical 結果）。

**用法**：只借版面結構（區塊怎麼分、grid/flex 怎麼排、KPI 卡片長怎樣），
**改寫時要把三個外部依賴全部拔掉**：
- Chart.js/ECharts → 換成純 SVG + vanilla JS
- Google Fonts → 換成系統字體堆疊
- Tailwind CDN → 換成內嵌 `<style>`，並補上 `prefers-color-scheme` + `:root[data-theme]` 雙主題

## 每個版型資料夾內容

`<name>/SKILL.md`（原產品的版型說明，含 frontmatter：`mode/scenario/surface/preview/design_system`
等，是那個產品自己的 schema，不是 Claude Code skill 格式）＋ `<name>/example.html`（可直接在瀏覽器
打開看版面長怎樣，注意需要網路才能載入 CDN 資源）。部分資料夾另有 `assets/`、`references/`。

## 跟本專案報告最相關的版型（挑選建議）

| 版型 | 適合場景 |
|---|---|
| `data-report` | 數據可視化週報：KPI卡+雙欄圖表+資料表+洞察卡片+方法論折疊區——跟我們現有的 `analysis_推薦精準度_報告.html` 骨架最接近 |
| `dashboard` / `live-dashboard` | 純指標儀表板 |
| `finance-report` | 財務／營運數字報告 |
| `eng-runbook` | 工程操作手冊 |
| `exec-briefing-memo` | 主管簡報摘要 |
| `experiment-readout` | A/B 測試或實驗結果報告 |
| `weekly-update` / `team-okrs` | 週報／OKR追蹤 |
| `competitive-teardown` | 競品分析 |

其餘多數是行銷向版型（landing page、pitch deck、social card、poster 等），本專案目前用不到，
但保留供未來需要視覺化交付物時參考。

## 授權

Apache License 2.0，允許修改與再散布，需保留版權與授權聲明（見 `html-templates-LICENSE`）。
