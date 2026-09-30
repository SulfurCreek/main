# user-journey：User Journey × 流程圖 × 文件 專案

專案目標：把求才端（招募人員）的 User Journey Map、各階段流程圖、對應 HackMD 文件串成一套可瀏覽的 HTML。

| 項目 | 內容 |
| :--- | :--- |
| 素材 | [`recruiter_journey_map.md`](recruiter_journey_map.md)（2026-09-30 由 HackMD 文件 session 產出，方法見 `.claude/skills/user-journey-map/SKILL.md`） |
| 接手 session | 規格文件html示意圖助手（`claude/gifted-meitner-6eSoK`）——開工前先 `git fetch origin main && git merge origin/main` |
| 誰能改素材 | 只有 HackMD 文件 session 能改 `recruiter_journey_map.md` 的**內容**（事實來源是 HackMD 規格）；HTML session 發現缺口或錯誤，回報使用者轉給文件 session，不自行改寫 |
| HTML 產出放哪 | 本資料夾下（例如 `html/`），不放 repo 根目錄、不動 `CLAUDE.md`／`wiki/`／`.claude/` 等共用檔 |
| 標記規則 | `US`＝真實 User Story；`US*`＝套版句；`NULL`＝文件未記載，一律照原標記呈現，不推測補齊 |
| 圖片 | 依 `photo` skill：成品圖一律存 R2 |
