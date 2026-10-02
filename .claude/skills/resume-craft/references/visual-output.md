<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

# 視覺化／可列印輸出（HTML / LaTeX）

> 回 [`../SKILL.md`](../SKILL.md)。

當使用者要的是**人看的、可匯出 PDF 的高顏值版本**（非 ATS 上傳版）時，切換到資深前端設計師＋排版師模式。

> ⚠️ **與 ATS 不衝突的前提**：視覺版**僅供人看／面試攜帶／作品集**；**ATS 上傳一律用單欄純文字版**。
> 一份內容、兩種包裝——**動手前先確認這份是「視覺版」還是「ATS 版」**。

## 模式一：列印優化單檔 HTML

產出**單一檔案**的 HTML/CSS：

1. **排版框架**：Tailwind CSS（CDN 引入），現代極簡。
2. **列印優化（關鍵）**：`<style>` 內加 `@media print`——隱藏滾動條與非必要元素、
   `print-color-adjust: exact;`（強制背景色列印）、`page-break-inside: avoid;`（避免內容被切斷）。
3. **視覺風格**：專業 PM 質感；字體 Inter／Roboto；主色沉穩**深藍或碳灰**；高對比可讀。
4. **輸出與指示**：以 Artifacts 原生渲染供預覽，並提示使用者「**在瀏覽器列印 → 另存為 PDF**」。

## 模式二：科技業 LaTeX

使用者明確要求最頂級、嚴謹的 PDF 排版時切 LaTeX：

1. **套件**：基於 `Awesome-CV` 或標準 `article` 類別；含中文時用 `xeCJK`（須 XeLaTeX 編譯）。
2. **結構**：嚴格用 `\section`／`\subsection`，讓學歷、核心職能、專案經歷有完美對齊與間隔。
3. **純代碼輸出**：產出完整 `.tex` 代碼區塊，附一句「**將此代碼貼至 Overleaf 即可匯出 PDF**」。

> 內容來源仍是 `career/competency-framework.md` 與 `career/wiki/` 分頁；視覺版只換**包裝**、
> 不改成就與數字，「不捏造」契約照舊。
