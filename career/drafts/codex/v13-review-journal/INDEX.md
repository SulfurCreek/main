# v13–v14 履歷評論索引

更新：2026-11-04（Asia/Taipei）。本目錄供本人、Claude與Codex跨輪接續；使用者已明確同意發布到本公開repository。

## 先讀

- [評論日誌 LOG.md](LOG.md)：每輪結論、有效寫法、缺口、後續修正與最新使用者目標。
- [完整版本快照 SNAPSHOTS.md](SNAPSHOTS.md)：六個指定commit的原文，含上游標記。
- 最新已審成品：b3b1cfb3 的 career/02_codex_stage/104-v14.md；R12。
- 前輪已審文字：[使用者貼上的 v14 快照](sources/2026-11-04-v14-pasted.md)，無指定 commit；不可當作 585ee01 版本。
- 最新治理校正：[審查者責任與persona調度](../REVIEWER_GOVERNANCE.md)｜[上游訪談指令](../hr-personas/UPSTREAM_INTERVIEW_REQUEST.md)。R07–R15只有主審閱讀，未實際派persona；不可當成完整persona審查。
- 最新歷史評論：[R15｜58dfa89升級與905c743整合審視](reviews/2026-11-04-58dfa89-905c743-upgrade.md)。
- 前輪評論：[R14｜行銷版與潤飾版增量比較](reviews/2026-11-04-c6768415-vs-1372959e.md)，c6768415 → 1372959e。
- 前輪評論：[R13｜實際 PDF 的候選人推廣與推薦效果](reviews/2026-11-04-pdf-promotion-vouch.md)。
- 前輪評論：[R12｜104-v14 審視與 Codex 需求](reviews/2026-11-04-b3b1cfb3-104-v14.md)，底稿 b3b1cfb3。
- 前輪評論：[R07–R11 完整整理](reviews/2026-11-04-pdf-to-v14.md)，以 R11 接續；R08 保留對局部審視的校正。歷史問題不能直接套用後版。

## 版本 × 回答

| 輪次 | 指定commit | 文件 | 對應分析 | 狀態 |
| --- | --- | --- | --- | --- |
| R00 | 無v13 commit | 原104 PDF與Gemini回饋 | 原始診斷與整合邊界 | 回顧摘要，原附件未複製到本目錄 |
| R01 | 0e3ff1f | 寫作指南第一版 | 六個缺口：決策、翻新成果、篇幅、路由、待決/語言、招聘驗收 | 當輪已讀 |
| R02 | 9fe7b73 | 指南中間版 | 沒有獨立回答，不補造評語 | 建日誌時補存快照 |
| R03 | 28750df | 指南更新 | 結構可動筆，缺人物定位與聘用理由；公式為題目＋作用＋成果 | 當輪已讀 |
| R04 | 7f9a069＋fa3be9f | 更新指南＋PM草稿第一版 | 已可推薦；簡介、推薦細節、AI標題、兩次承接待修 | 當輪已讀 |
| R05 | 2a7a8da | PM草稿第二版 | 補回技術溝通、AI實務、帶人/跨層級溝通；避免精簡掉能力廣度 | 當輪已讀，歷史版本 |

| R06 | 585ee01 | r6＋JD責任線分類 | 33筆未投PM、能力組合及三項補答 | 歷史診斷，連結見下方 |
| R07 | 未提供；非 r6 commit | v13 PM PDF | 第一輪 summary／工作經歷閱讀；四項優先修改。 | [連續紀錄](reviews/2026-11-04-pdf-to-v14.md) |
| R08 | 未提供；非 r6 commit | 同一份 v13 PM PDF | 使用者指出局部審視後，補整體定位、職級、近期成果、KOOL、影響力與篇幅權重；修正前輪結論。 | [連續紀錄](reviews/2026-11-04-pdf-to-v14.md) |
| R09 | 未提供；非 r6 commit | 同一份 PDF＋兩份評論 | 整合最終評論，並非履歷定稿或驗收通過。 | [連續紀錄](reviews/2026-11-04-pdf-to-v14.md) |
| R10 | 未提供；非 r6 commit | 聊天室新版 v13，無 commit | 商業首屏改善；七點密度、KOOL位置、比較期、AI覆核與價格解碼尚待修。 | [連續紀錄](reviews/2026-11-04-pdf-to-v14.md) |
| R11 | 未提供；非 r6 commit | 聊天室 v14，無 commit | 最新接續：完整產品能力已可辨識；摘要、提案口徑／留存歸因、AI密度、付款DAU歸因、定價表達優先。 | [連續紀錄](reviews/2026-11-04-pdf-to-v14.md) |

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


## HR集合體（2026-11-03新增）

[HR角色與使用入口](../hr-personas/INDEX.md)：81個未應徵快照職缺、46家公司、10領域；含完整JD、職缺專屬判讀、推薦與審視協議、136筆狀態處置。本人已明確同意公開並要求push。本次僅建置角色，未實際審新草稿/PDF或派子代理。後續審視以角色包PROTOCOL與最新指定候選為準，不遺忘本日誌的五項能力定位。


## R06｜585ee01 r6（歷史）

[完整PM招聘診斷](../hr-personas/runs/2026-11-03-585ee01/REPORT.md)｜[原稿完整快照](../hr-personas/runs/2026-11-03-585ee01/SOURCE.md)｜[137職缺分類](../hr-personas/JOB_TRACKS.md)｜[新欄位housekeeper交接](../hr-personas/HOUSEKEEPER.md)。三項本人補答已納入；33筆未投PM線，診斷有獨立評閱與主HR閱讀之別；未改稿/未驗PDF/未正式gate。

## R11｜v14（歷史文字版）

[評論與五項待修](reviews/2026-11-04-pdf-to-v14.md)｜[v14 文字快照](sources/2026-11-04-v14-pasted.md)。R07–R09 是先前 PDF 審視；R10 是新版 v13 貼文，保存來源要點而非完整原文；R11 是 v14 貼文，沒有新 PDF。這次只補記，未修改上游草稿。

## R12｜104-v14（歷史文字版）

[招聘閱讀與 Codex 交接需求](reviews/2026-11-04-b3b1cfb3-104-v14.md)。指定 commit b3b1cfb3ddc2d538ff313404c4fe8d4260b04518，career/02_codex_stage/104-v14.md。與68cdfa3 PDF文字底稿比較；未改成品、未實際傳訊給另一個 agent。

## R13｜實際104 PDF：promote／vouch（歷史）

2026-11-04，[完整檢視及給 Claude／Codex 的需求](reviews/2026-11-04-pdf-promotion-vouch.md)。附件 media_1793781379334_cad82100.pdf，未提供對應 commit；全文文字閱讀與第1、2、4頁影像。promote 已有效，vouch 證據已具備但聘用主張仍需串起。優先定位句、代表作落點、自傳結尾與AI跨欄分工。已改問題不重複追打。未改稿、未跑腳本或派代理。

## R14｜c6768415 行銷版 → 1372959e 潤飾版（歷史）

2026-11-04，[全文比較與實際增益](reviews/2026-11-04-c6768415-vs-1372959e.md)。兩份完整閱讀、九處文字差異。結論：有正向且有限的語句編輯價值；行銷定位與推薦主張主要已存在底稿。潤飾未破壞既有賣點，未完成AI跨欄分工，提案段出現數字重複。保留潤飾版接續，不再全面翻修。未改履歷、未驗新PDF。

## R15｜58dfa89 → 905c743（最新）

2026-11-04，[完整閱讀及比較](reviews/2026-11-04-58dfa89-905c743-upgrade.md)。相對1372959e，Codex已改善代表作短標、產品理由、AI數字與方法分工、提案主訊息，從語句編輯進入說服力編輯。905c743後補口徑括號與專長19萬可保留；提案短標加回留存使訊息過滿，建議沿用58dfa89短標、留存留正文。不否定本人已核可資料。未改履歷或驗新PDF。

## R16｜2026-11-04 審查角色與責任校正

本人明訂此代理負責審查與派HR persona；事實疑問交上游訪談，不直接訪談本人或改稿。已建立 [審查者治理](../REVIEWER_GOVERNANCE.md)、[上游訪談指令](../hr-personas/UPSTREAM_INTERVIEW_REQUEST.md)，並更新AGENTS角色路由與persona協議。R07–R15沒有實際persona派發，屬主審閱讀／比較；先前正向結論不代表19萬筆、常駐Agent及季度期間已完成可信度核對。三項交上游，待回覆後再審。本輪只改治理與交接，沒有派新代理或執行新履歷審查。

## R17｜最新104 Markdown：五位persona完整審查

2026-11-04實際派發與完成，2026-11-05補齊先前GitHub故障未同步的報告。
[完整入口](../hr-personas/runs/2026-11-04-216445b9-104/INDEX.md)｜[整合報告](../hr-personas/runs/2026-11-04-216445b9-104/REPORT.md)｜[上游需求](../hr-personas/runs/2026-11-04-216445b9-104/UPSTREAM.md)。入口含五份原始全文，來源固定216445b97d7aa282c4f4c0b47229c54fe496adb1的career/02_codex_stage/104-v14.md。支付連、91APP與訊連值得邀約；PressPlay先釐清行為分析、SHOPLINE Data先釐清數據產品責任。共通資料處理、Agent術語與統計口徑仍交上游，不等於已核實。協助式、非隔離盲審，未改履歷或驗PDF。
