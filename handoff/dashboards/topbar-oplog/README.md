# Topbar 動線數據後台

- 檔案：`index.html`（自包含、無外部資源；示意資料，固定 seed）。分支 `claude/extract-job-duty-markdown-4avmd6`，承接 `claude/topbar-oplog-dashboard` 的第一版。
- 依據：HackMD〈求才埋點需求統整〉v0.0.3。以 Session ID 串 `recruit:login:success` 與 `recruit:topbar:view`。
- 篩選：日期、VIP 狀態（oStatus 0–6）、網段（全部／外網／內網）、功能分區、抵達頁面、廠商名稱／OrganNo、Session ID。
- v2 增補：內外網並列比較卡（不受網段篩選影響）、埋點覆蓋表。
- 驗證：色盲驗證（dataviz `validate_palette.js`）外網 #2a78d6／內網 #eb6834 亮色、#3987e5／#d95926 暗色全 PASS；Playwright 截圖 1440 亮／暗、390 無橫向捲動、無 console 錯誤。
- 接真實資料時：替換 `index.html` 內「示意資料產生」區塊，其餘不變。
