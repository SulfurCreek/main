# Figma 規則

## 現況

Figma MCP 伺服器連線時，會自帶它自己的 skill 指示（`figma-use`、`figma-generate-design`、`figma-generate-library`、`figma-code-connect` 等），那些指示由 Figma MCP 原生提供，不需要、也不應該在這裡重複。涉及讀取/產生 Figma 設計、Code Connect 對照時，直接遵循 Figma MCP 自帶的指示即可。

## 截圖存檔與標註 → 改用 `photo` skill

**本專案特有的「Figma 截圖 ↔ 規格書」轉換慣例（截圖存進 repo、badge／紅框標註）已改用獨立 skill 管理，不再寫在本檔：**

👉 `.claude/skills/photo/SKILL.md`（skill 名稱 `photo`）

涵蓋範圍：
- 截圖存檔流程（Figma fetch 或使用者上傳圖片皆適用）：下載 → commit 進 `.claude/assets/` → push → `raw.githubusercontent.com` 網址引用。
- 標註樣式：**一律用 HTML 絕對定位覆蓋**（`position:absolute` 疊 badge／紅框在 `<img>` 上），不再用 Pillow 把 badge 燒進圖片像素。
- 多圖點擊流程（A 圖某按鈕 → B 圖）：HTML flex 並排＋純文字箭頭，取代舊的 Pillow 拼接大圖做法。

若之後這套 photo skill 的規則需要調整，直接修改 `.claude/skills/photo/SKILL.md`，本檔僅維持指標、不重複內容。
