# v13 履歷評論索引

更新：2026-11-03（Asia/Taipei）。本目錄供本人、Claude與Codex跨輪接續；使用者已明確同意發布到本公開repository。

## 先讀

- [評論日誌 LOG.md](LOG.md)：每輪結論、有效寫法、缺口、後續修正與最新使用者目標。
- [完整版本快照 SNAPSHOTS.md](SNAPSHOTS.md)：六個指定commit的原文，含上游標記。
- 最新已審草稿：[2a7a8da](https://github.com/SulfurCreek/main/blob/2a7a8da/career/01_claude_stage/v13-pm-draft.md)。
- 最新評論：LOG.md的R05；不要將R01的問題不加核對地重複套到後版。

## 版本 × 回答

| 輪次 | 指定commit | 文件 | 對應分析 | 狀態 |
| --- | --- | --- | --- | --- |
| R00 | 無v13 commit | 原104 PDF與Gemini回饋 | 原始診斷與整合邊界 | 回顧摘要，原附件未複製到本目錄 |
| R01 | 0e3ff1f | 寫作指南第一版 | 六個缺口：決策、翻新成果、篇幅、路由、待決/語言、招聘驗收 | 當輪已讀 |
| R02 | 9fe7b73 | 指南中間版 | 沒有獨立回答，不補造評語 | 建日誌時補存快照 |
| R03 | 28750df | 指南更新 | 結構可動筆，缺人物定位與聘用理由；公式為題目＋作用＋成果 | 當輪已讀 |
| R04 | 7f9a069＋fa3be9f | 更新指南＋PM草稿第一版 | 已可推薦；簡介、推薦細節、AI標題、兩次承接待修 | 當輪已讀 |
| R05 | 2a7a8da | PM草稿第二版 | 補回技術溝通、AI實務、帶人/跨層級溝通；避免精簡掉能力廣度 | 當輪已讀，最新接續點 |

上游路徑：
- 指南：career/drafts/v13/00-writing-guide.md
- 草稿：career/01_claude_stage/v13-pm-draft.md

## 本人最新目標

讓HR看見並記住：
1. 非程式背景仍能與工程深入溝通規格與流程。
2. 英文有高分與跨國實務。
3. AI不只推出功能，也用於本人工作與團隊作業。
4. 能串起產品定位、流程、商業邏輯與交付。
5. 能教導部屬、對齊上級與不熟系統的人。

正向放大有證據的能力與作用，不捏造成效或把團隊工作寫成一人全做。

## 防止跨輪遺忘與搖擺

- 基本功不放摘要，不代表整份刪掉工程規格與交付鏈。
- 簡報不是單獨成就，但可證明讓非技術人員理解方案。
- 不突出上百筆對照，不代表刪除AI方法、可重用流程與團隊導入。
- 支付版聚焦不能犧牲全部個人辨識度；產品定位的宣稱要留案例證據。
- 沒有數據的資料已結案，不反覆追問；歷史評論不是新的事實授權。
- 紀錄是保留關鍵資訊的整理版，不是逐字聊天匯出。
- 本目錄沒有宣稱v13已通過腳本、PDF或完整JD驗收。

## 分支與Claude讀取

文件位於codex/resume-writer分支。Claude如在自己的分支工作，先fetch，再唯讀：
```sh
git show origin/codex/resume-writer:career/drafts/codex/v13-review-journal/INDEX.md
git show origin/codex/resume-writer:career/drafts/codex/v13-review-journal/LOG.md
git show origin/codex/resume-writer:career/drafts/codex/v13-review-journal/SNAPSHOTS.md
```

本次不改Claude維護的career/ROUTER.md。Claude可將本INDEX路徑加入自己的ROUTER入口。

## 後續記錄契約

每次新commit/評論：保存指定版本原文、追加LOG輪次、更新本表與最新接續點。沒有實際比對的採納狀態寫待核對；不覆寫舊結論或以新稿冒充舊稿。
