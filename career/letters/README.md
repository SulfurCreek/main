<!--markdownlint-disable MD013-->

# 求職信資料庫 / Cover-letter database

中文**自我推薦信**與英文 **cover letter** 的素材與紀錄。寫法規則在 skill（見下方〈工具〉）；這裡只放**資料**。

| 檔案 | 內容 |
| :--- | :--- |
| [`story-bank.md`](story-bank.md) | 可重複使用的段落素材：開場鉤子、成果證據（附來源）、動機、收尾，中英對照 |
| [`log.md`](log.md) | 每封信的投遞紀錄：日期、公司、職缺、語言、檔案、結果 |
| [`archive/`](archive/) | 寫好的信，一封一檔：`YYYY-MM-DD-公司-職稱-zh|en.md` |

## 規則

- **數字只能來自 `story-bank.md`**，story-bank 的數字只能來自 `career/wiki/`；沒有的標 `〔待補數據〕`，不編。
- **不放聯絡資訊**（電話、email、地址），信件標頭用 `[聯絡資訊]` 佔位，輸出時才填。
- 對外版本遵守 `career/CLAUDE.md` 硬規則二：不外露 1111 內部 API 名、欄位名、客戶名。
- 新信寫完：存進 `archive/`、在 `log.md` 加一列；若用到新的成果句，回填 `story-bank.md`。

## 工具

- 英文 cover letter：career-ops 的 `cover` 模式（`/home/user/career-ops/modes/cover.md`），
  讀 `career-ops/cv.md`＋`config/profile.yml`；本資料庫的 story-bank 優先於 cv.md。
- 中文自我推薦信：待主幹納管（見 [`../_requests-to-main.md`](../_requests-to-main.md) 2026-10-04 條目）；
  納管前依 story-bank 與 `resume-craft` 自傳規則手寫。
