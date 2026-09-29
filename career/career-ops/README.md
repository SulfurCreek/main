# career-ops 個人資料層

[career-ops](https://github.com/career-ops-hq/career-ops)（MIT）的使用者資料，從 `career/wiki/` 萃取。
放在 repo 裡是因為雲端 container 會回收，career-ops 本體每次由環境 Setup script 重新 clone。

| 本目錄 | 複製到 career-ops 的 | 來源 |
| :--- | :--- | :--- |
| `cv.md` | `cv.md` | [resume-extract.md](../wiki/resume-extract.md)、[prior-roles.md](../wiki/prior-roles.md)、[學歷證照](../wiki/education-certifications.md) |
| `profile.yml` | `config/profile.yml` | 同上＋F1–F15 |

```bash
cp career/career-ops/cv.md /home/user/career-ops/cv.md
cp career/career-ops/profile.yml /home/user/career-ops/config/profile.yml
```

**同步規則**：`career/wiki/` 是唯一事實來源。wiki 有新成果時，先改 wiki，再同步到本目錄的 `cv.md`，不要反向。

**與 wiki 的刻意差異**：
- 刪掉 wiki 中的 `〔待補數據〕` bullet 尾巴，改寫成不帶數字的定性句（career-ops 的 `cv:verify-facts` 會擋無法查證的數字）。
- 刪掉直屬部屬姓名（第三人個資）。
- 前段雇主城市未經查證，只寫 Taiwan。

**待你決定（TODO）**：LinkedIn／作品集網址、電話、薪資區間與底線、目標職稱確認、輸出語言、預告期、畢業年份（2013 或 2014）。
