# 提醒信成效分析 — 重跑流程

產出物：`../提醒信成效分析報告.html`（自包含、無外部資源，離線可開）。

## 資料來源

「各廠商所有帳號都未讀的職缺履歷統計」Google Sheets 發布 CSV（base URL 見 `../00-總覽-寄送廠商數.md` 頂部）。
依分頁 gid 下載至工作目錄，命名為 `寄送廠商數.csv` 與 `尾數{0-9}.csv`（gid 對照見各明細 MD 檔頂部）：

```bash
curl -sSL -f -o 尾數0.csv "<base>/pub?gid=0&single=true&output=csv"
```

## 執行

```bash
pip install pandas
python3 step1_analyze.py <資料目錄>        # 產出 summary.json（回流率/改善度/持續性等聚合統計）
python3 step2_build_report.py <資料目錄>   # 補算回鍋率/慢性占比 → report_data.json → 注入模板產出 HTML
```

## 檔案

| 檔案 | 說明 |
| :--- | :--- |
| `step1_analyze.py` | 逐批計算：疑似回流率、連續出現改善度、出現輪數分佈、慢性族群量級、與總覽表核對 |
| `step2_build_report.py` | 補算消失後回鍋率、慢性族群未讀占比，彙總成圖表用 JSON 並注入模板 |
| `report_template.html` | 報告模板（`__DATA__` 佔位符由 step2 注入），圖表為 inline SVG＋vanilla JS，深/淺色自適應 |

## 已知資料落差

總覽表「寄送廠商數」固定比明細表廠商數多約 6%（39 天皆如此），原因不明（推測總覽含明細未列出的廠商）；
分析一律以明細表為基礎，報告 §1 限制聲明第 ④ 點已載明。
