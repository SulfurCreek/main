<!--markdownlint-disable MD013-->

# mock ↔ 正式環境 結構稽核

mock（PM 給的）常常已被前一手 AI 動過：搬節點、刪節點、拿掉 `data-*`/`onclick`、改寫呈現方式。**動手前先查清楚**，否則會把偏離當成原樣、誤導工程師。

## 不要憑印象，做程式化 skeleton diff

把正式環境 HTML 存成檔，用 stdlib `html.parser` 抽出 tag/class 骨架，比對「class/tag 集合」：

```python
from html.parser import HTMLParser
from collections import Counter
class Skel(HTMLParser):
    def __init__(s): super().__init__(); s.inscript=False; s.tags=Counter(); s.cls=Counter()
    def handle_starttag(s,t,a):
        if t in('script','style'): s.inscript=True; return
        d=dict(a)
        for c in (d.get('class') or '').split(): s.cls[c]+=1
        s.tags[t]+=1
    def handle_endtag(s,t):
        if t in('script','style'): s.inscript=False
def parse(fn): k=Skel(); k.feed(open(fn,encoding='utf-8').read()); return k
P=parse('production.html'); M=parse('mock.html')
print('class 只在正式:', sorted(set(P.cls)-set(M.cls)))
print('class 只在 mock:', sorted(set(M.cls)-set(P.cls)))   # 空=沒改名/沒新增亂 class
print('tag 只在正式:', sorted(set(P.tags)-set(M.tags)))
```

- **「class 只在 mock」= 空** → 代表沒有任何 class 被改名/拼錯/亂加（重要結論，常被誤會）。
- **「class 只在正式」** → mock 刪掉的節點（如 `titleFont`、`wish-content`、`isWish`、`isNoWish`），或整塊沒納入的區（如 guidedTour 浮層）。
- 屬性層級（`data-starno`、`data-mailno`、`onclick`…）另外用 grep 數：`grep -o 'data-starno' x.html | wc -l`。

## 偏離分類（記到 `01_…§2.5`）

A. 刪除的節點（連 class）　B. 移除的屬性（`data-*`/`onclick`）　C. 位置搬移（class 不變）　D. 呈現方式改寫（如意願移到 `.mail-type` inline）　E. mock 新增（空 div、standalone `html/head/body`）。

## 誠實原則

- 別宣稱「結構零改動 / 完全沿用」未經查證 —— 本任務踩過這個雷（原紀錄誤寫「皆沿用原檔」，實為偏離）。發現紀錄寫錯要**據實更正**。
- class token 順序（`active tab` vs `tab active`）= 同樣 class、無影響，不算改名。

## 偏離怎麼處理：優先「修 mock」而非「留警語」

當 mock 的偏離會讓工程師照錯（例：意願塞在 `.mail-type` inline，但正式是 `.td-status > wish-content`）：

- **首選**：把 mock 改回正式結構（動 mock HTML/CSS），讓 mock = 正式、預覽即正解，紀錄標「已修正」。
- 次選（不便動 mock 時）：需求文件用明確指示講正式結構，並標「🔧 別照 mock 寫法」。
- 動 mock 前先跟使用者確認（本任務使用者明確選了「修 mock」）。
