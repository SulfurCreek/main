# 給 Career Move 的問題（作品集網站助手 → career session）

作品集網站助手（render session）已獲使用者核准把網站原始碼放在 `career/site/`。我只渲染、不改內容；
`career/site/` 請 Career Move 不要動。下列問題請回覆在本檔下方或直接更新 `career/portfolio/*.md`，我再渲染。

## Q1　E.1 目前不能渲染成公開頁（阻擋項）

`career/portfolio/e1-cross-system-messaging.md` 檔頭自己註明「對外引用務必抽象化」，但正文尚未去識別化。
請產出**對外版**（建議新檔 `e1-cross-system-messaging.public.md`，保留現檔當內部版）：

| # | 問題 | 位置 | 規則 |
| :--- | :--- | :--- | :--- |
| 1 | 內部 API 名：`get-echat-mail-logs`／`get-detail/{infoNo}`／`get-by-condition`／`update-chatlog` | §3、循序圖 | 不得出現 |
| 2 | 欄位／代碼名：`mailType`／`interViewKind`／`revokeFlag`／`sendKind`／`readflag`／`oViewDate`／`tViewDate`／`sendType`／`Type:8`；前端函式 `chatMessageMapper`／`toMailType`／`toInterviewStatus` | §2、§3 | 不得出現 |
| 3 | 推播通道／事件名：`echathub`／`ReceiveMessage`／`UpdateMessageStatus` | 循序圖 | 不得出現 |
| 4 | 〔待補數據〕 | §4 量化成果 | 網站不得有佔位字；請補真實數據或刪掉該條 |
| 5 | 「1111 人力銀行」、HackMD、GitHub、內部 wiki 路由表／RAG 索引 | §1、§4 | 請確認是否可公開；未確認前我一律不放 |
| 6 | 循序圖含「廠商編號／履歷編號／職缺編號」等欄位級描述、點數／權限檢查細節 | 循序圖 | 請改畫抽象版（角色名＋階段），我預先渲染成 SVG |
| 7 | §1 寫「五種邀約卡片」卻列六項 | §1 | 數字請你確認 |
| 8 | 「2022/08 到職」「仍在職」類時間線 | §1 | 請確認是否對外 |

## Q2　其他案例

目前 `career/portfolio/` 只有 E.1 一篇。首頁需要「一句定位＋3 個成果數字卡」，數字請由你在 md 提供，我不編。
Peach 案例尚未寫。

## 狀態

網站骨架（`assets/style.css`、`404.html`、`robots.txt`）已建。`index.html`、`cases/*.html` 等 E.1 對外版 md 到手再做。
預設 `noindex, nofollow`。
