---
name: portfolio-site
description: >
  把使用者的 PM 作品集 case study（career/portfolio/*.md）渲染成可直接部署到 GitHub Pages 或 Cloudflare Pages 的
  靜態網站（純 HTML5＋CSS，不用框架、不需要 JS）。涵蓋語意化結構、WCAG 2.1 AA、Mermaid 預先渲染成 SVG、
  XYZ／HEART 寫法、NDA 去識別化、noindex 隱私開關與部署前驗證。
  觸發詞：作品集網站、portfolio site、靜態網站、個人網站、GitHub Pages、Cloudflare Pages、把 case study 做成網頁。
  只負責「渲染」：內容由 career session 依 resume-craft 寫好；本 skill 不寫新內容、不編數字。
---

<!--markdownlint-disable MD013-->

# portfolio-site — PM 作品集靜態網站

## 0. 分層與邊界（先讀）

| 層 | 誰負責 | 位置 |
| :--- | :--- | :--- |
| 內容（已去識別化的 case study md） | career session，依 `resume-craft` 寫 | `career/portfolio/*.md`（唯一內容來源） |
| 渲染（本 skill） | HTML 助手 session | **使用者自己的作品集 repo**（公開），不是本 repo |
| 部署 | 使用者 | GitHub Pages 或 Cloudflare Pages |

- **不寫新內容、不改數字**。內容缺什麼，回報給使用者轉給 career session，不要自己補。
- **不要把網站原始碼放進本 repo**：本 repo 是私有的，且 `career/` 只有 career session 能寫。
- 不需要問卷式 intake：專案背景、角色、數字都已在 case study md 裡。

## 1. 技術約束

- **只用語意化 HTML5＋一支 CSS**：`<header>` `<nav>` `<main>` `<article>` `<section>` `<aside>` `<footer>`；不用 React／Vue／Tailwind CDN。
- **預設零 JS**。真的需要（例如語言切換）才用少量原生 JS，且關掉 JS 時內容仍完整可讀。
- **漸進揭露**：PRD 細節、API 邏輯、邊界案例放 `<details><summary>`；第一層只放結論與成果。
- **自包含**：不載入外部 CDN、追蹤碼、Google Fonts；字型用系統字體堆疊。理由：部署零依賴、隱私、速度。
- **RWD**：手機優先，最大內文寬約 72ch；支援 `prefers-color-scheme` 深色模式與 `@media print`。
- **效能預算**：每頁 HTML＋CSS＋SVG 合計 < 200 KB（不含照片）；圖片用 WebP／AVIF、指定寬高避免版面位移。

## 2. 無障礙（WCAG 2.1 AA）

- `<html lang="zh-Hant">`（英文頁 `lang="en"`）；每頁一個 `<h1>`，標題層級不跳級。
- 文字對比 ≥ 4.5:1；連結與按鈕有可見的 `:focus-visible` 樣式；提供「跳到主要內容」連結。
- 所有圖片與圖表要有說明：`<img alt>`；內嵌 SVG 要有 `<title>`＋`<desc>`，並用 `role="img"`＋`aria-labelledby`。
- 不能只靠顏色傳達資訊（例如狀態圖要同時有文字標籤）。

## 3. 圖表：Mermaid 預先渲染成 SVG

- **不要在瀏覽器端跑 Mermaid**（不用 `<div class="mermaid">`＋CDN）：需要 JS、會閃爍、拖慢載入、關掉 JS 就看不到。
- 作法：`.mmd` 原始檔留在 `diagrams/` → 用 mermaid-cli 轉 SVG → 內嵌或以 `<img>` 引用。
  ```bash
  npx -y @mermaid-js/mermaid-cli -p puppeteer.json -i diagrams/x.mmd -o assets/x.svg
  # puppeteer.json: {"executablePath":"/opt/pw-browsers/chromium","args":["--no-sandbox"]}
  ```
- 樣式依本 repo `wiki/mermaid_styling_rules.md`（柔色系；循序圖用 §4 的 frontmatter config）。
- 每篇 case study 至少一張圖，挑最能呈現系統複雜度的：狀態機、跨系統循序圖或資料流。
- 圖只畫抽象層級：用「求才端／求職端／訊息服務」這類角色名，**不出現內部 API 名、欄位名、資料表名**。

## 4. 敘事規則

- **XYZ 公式**：「達成 [X]，以 [Y] 衡量，透過 [Z]」。用在**有數據的成果句**，不用硬套每一行。
- **HEART 只用在使用者端產品**（Happiness／Engagement／Adoption／Retention／Task success）。
  B2B 交付、維運類成果用它們自己的指標（準時率、處理週期、付費客群留存），不要硬塞進 HEART。
- 每篇結構沿用 `resume-craft` 範本：台灣版 `portfolio-case-study-tw.md` 或國際版 `portfolio-case-study.md`。
- 首頁：一句定位、3 個成果數字卡、case study 卡片列表、聯絡連結（LinkedIn／Email）。

## 5. 保密與誠實（硬規則）

- 數字只能照抄 case study md；md 沒有的數字一律不寫。
- **不寫營收、分潤的絕對數字**；可以寫倍數與比例（例如 DAU 約 14 倍、網頁付款占比 24%→80%+）。
- Peach 只描述為「訂閱制社交內容 App」，不寫產品細節。
- 不出現 1111 內部 API 名、欄位名、權限代碼、客戶與廠商名稱；不放內部系統截圖，用重畫的圖表代替。
- 不放電話、住址、出生日期。
- 任何 `〔待補〕`／`〔待填〕`／`TODO` 不能出現在網站上：建置前全文 grep，有就停下回報。

## 6. 隱私與 SEO 開關

使用者仍在職時預設「不公開索引」：

```html
<meta name="robots" content="noindex, nofollow">
```

並在根目錄放 `robots.txt`（`User-agent: *` ／ `Disallow: /`）。使用者明確說要公開時才移除。
`<title>`、`<meta name="description">`、Open Graph（`og:title`／`og:description`／`og:image`）仍要寫，貼連結時預覽才好看。

## 7. 網站結構

```text
/index.html            首頁
/cases/<slug>.html     每篇 case study
/en/...                英文版（選配，與中文同結構）
/assets/style.css      唯一的樣式表
/assets/*.svg          預先渲染的圖表
/diagrams/*.mmd        圖表原始檔（可不部署）
/404.html
/robots.txt
```

## 8. 交付前驗證（全過才交付）

| 項目 | 方法 |
| :--- | :--- |
| HTML 合法 | `npx -y html-validate "**/*.html"` 零錯誤 |
| 佔位字 | `grep -rn "〔待\|TODO" --include=*.html .` 零結果 |
| 連結 | 站內連結全部可達（含 404 頁） |
| 數字一致 | 抽查每篇的數字，與 case study md 和 104 履歷一致 |
| 無障礙與效能 | Lighthouse（mobile）Accessibility ≥ 95、Performance ≥ 95 |
| 外觀 | Playwright 截 375px 與 1280px 兩種寬度，淺色與深色都看一次 |
| 外部請求 | 開發者工具 Network 不得有第三方網域 |

## 9. 部署（使用者執行）

- **GitHub Pages**：repo 設定 → Pages → 從 `main` 分支根目錄部署；不需要建置步驟。
- **Cloudflare Pages**：連結 repo，Build command 留空，輸出目錄為 `/`。
- 兩者都不需要伺服器；SVG 已預先渲染，網站上線後不依賴任何外部服務。
