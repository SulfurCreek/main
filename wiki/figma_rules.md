# Figma 規則

## 現況

Figma MCP 伺服器連線時，會自帶它自己的 skill 指示（`figma-use`、`figma-generate-design`、`figma-generate-library`、`figma-code-connect` 等），那些指示由 Figma MCP 原生提供，不需要、也不應該在這裡重複。涉及讀取/產生 Figma 設計、Code Connect 對照時，直接遵循 Figma MCP 自帶的指示即可。

## 截圖存檔與標註 → 改用 `photo` skill

**本專案特有的「Figma 截圖 ↔ 規格書」轉換慣例（截圖存進 repo、badge／紅框標註）已改用獨立 skill 管理，不再寫在本檔：**

👉 `.claude/skills/photo/SKILL.md`（skill 名稱 `photo`）

涵蓋範圍：
- 截圖存檔流程（Figma fetch 或使用者上傳圖片皆適用）：下載 → 上傳 Cloudflare R2 圖床（boto3，憑證讀環境變數）→ 用回傳的 `public_url` 引用。舊版 `commit` 進 `.claude/assets/`／`raw.githubusercontent.com` 做法已棄用。
- 標註樣式：**一律用 HTML 絕對定位覆蓋**（`position:absolute` 疊 badge／紅框在 `<img>` 上），不再用 Pillow 把 badge 燒進圖片像素。
- 多圖點擊流程（A 圖某按鈕 → B 圖）：HTML flex 並排＋純文字箭頭，取代舊的 Pillow 拼接大圖做法。
- **所有 HTML 標註區塊最外層一律加白色背景**（`background:#fff`）：避免 HackMD 深色模式下截圖文字/淺色 UI 看不清楚。

若之後這套 photo skill 的規則需要調整，直接修改 `.claude/skills/photo/SKILL.md`，本檔僅維持指標、不重複內容。

## 舊版 Pillow 燒像素做法 → 改用 `png` skill（棄用中，僅特殊情境備用）

CLAUDE.md 原本收錄的「規格書 UI 截圖標號慣例」＋「以 Pillow 在截圖上標注／覆蓋文字」整套舊做法（直接把編號徽章／覆蓋文字燒進截圖像素），已搬遷並改用獨立 skill 管理：

👉 `.claude/skills/png/SKILL.md`（skill 名稱 `png`）

**預設一律用 `photo` skill**（HTML 覆蓋，不燒像素）；只有 `photo` 做不到的情況——最主要是**需要覆蓋改寫截圖裡既有的文字內容**（HTML 疊圖只能疊加、換不掉圖片本身的文字），或維護既有「截圖標號＝章節編號」舊格式規格書時——才用 `png` skill。
