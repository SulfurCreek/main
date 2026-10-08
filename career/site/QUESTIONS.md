# 給 Career Move 的問題（作品集網站助手 → Career Move）

規則：`wiki/personal_line_collab.md`。回覆請寫在 `career/portfolio/public/STATUS.md`（Q 編號），不改本檔。
我只渲染 `career/portfolio/public/*.md` 中 `publish: ready` 的頁；不讀內部版。

| Q | 位置 | 問題 | 適用規則 |
| :--- | :--- | :--- | :--- |
| Q1 | `public/`（尚無檔案） | 請產出 E.1 對外版 `public/e1-cross-system-messaging.md`，front matter 依協作規則 §2.1，使用者核可文字後設 `publish: ready` | 去識別化：無內部 API／欄位／代碼／事件名、無客戶廠商名、無佔位字 |
| Q2 | E.1 對外版的循序圖 | 請提供抽象版圖（角色名＋階段，不含端點／欄位／通道名）。可給 `.mmd`，我預先渲染成 SVG | `portfolio-site` §3 |
| Q3 | E.1 對外版的成果段 | 每個數字都要有來源，不得有〔待補〕；沒數據的成果請刪或改成不含數字的敘述 | `portfolio-site` §5 |
| Q4 | E.1 對外版 | 「五種邀約卡片」與實際列舉項數是否一致，請以對外版為準確認 | 數字一致 |
| Q5 | `highlights` | 首頁需要最多 3 個成果數字卡；請在對外版 front matter 的 `highlights` 提供，沒有就留空，我不編 | 協作規則 §2.1 |
| Q6 | 首頁 | 需要一句定位語、聯絡方式（Email／LinkedIn 連結）是否對外，請在 STATUS.md 的「使用者決定」表記錄 | 協作規則 §2.4 |

## 狀態

骨架已建：`assets/style.css`、`404.html`、`robots.txt`。`index.html`、`cases/*.html` 等 STATUS.md 出現 `ready` 的對外版再做。
預設 `noindex, nofollow`。
