# career-ops 個人資料層

[career-ops](https://github.com/career-ops-hq/career-ops)（MIT）的使用者資料，從 `career/wiki/` 萃取。
career-ops 本體（程式碼）由環境 Setup script clone 到 repo 外的 `/home/user/career-ops`；
**使用者資料與產出**透過環境變數 `CAREER_OPS_ROOT` 直接指向本目錄，不再複製。

## 環境設定（一次性）

在雲端環境的**環境變數**加入：

```bash
CAREER_OPS_ROOT=/home/user/main/career/career-ops
```

驗證：

```bash
cd /home/user/career-ops && npm run doctor   # 應顯示 cv.md found、config/profile.yml found
```

## 目錄結構

| 路徑 | 內容 | 版控 |
| :--- | :--- | :--- |
| `cv.md` | 英文 CV | ✅ |
| `config/profile.yml` | 設定檔（含 TODO） | ✅ |
| `reports/` | 職缺評估報告 | ✅ 有價值的才 commit |
| `output/` | 客製 CV／求職信 PDF | ✅ **單檔 ≤ 1MB** 才 commit；超過的不進版控 |
| `data/` | 投遞追蹤（`applications.md`、`pipeline.md`）| ✅ |

## 規則

- **同步方向**：`career/wiki/` 是唯一事實來源。wiki 有新成果時，先改 wiki，再同步到 `cv.md`，不要反向。
- **產出 commit 前**：確認不含第三人個資（同事姓名）與 1111 內部名稱（API 名、欄位名、權限代碼、廠商名稱）——
  見 [`../CLAUDE.md`](../CLAUDE.md) 硬規則二。
- **PDF 體積**：commit 前 `find career/career-ops/output -name '*.pdf' -size +1M`，有結果的不加入。

## 與 wiki 的刻意差異

- 刪掉 wiki 中的 `〔待補數據〕` bullet 尾巴，改寫成不帶數字的定性句（career-ops 的 `cv:verify-facts` 會擋無法查證的數字）。
- 刪掉直屬部屬姓名（第三人個資）。
- 前段雇主城市未經查證，只寫 Taiwan。

**待你決定（TODO）**：LinkedIn／作品集網址、電話、薪資區間與底線、目標職稱確認、輸出語言、預告期、兵役起訖月份（畢業年份已確認 2014）。
