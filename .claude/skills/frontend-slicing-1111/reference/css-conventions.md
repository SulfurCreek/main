<!--markdownlint-disable MD013-->

# CSS 改法慣例

## override 策略

- mock CSS 通常是打包過的大 bundle（normalize + FontAwesome + 原站 CSS）。**不要去翻原規則硬改**，在**檔尾加一段 override 區塊**，用 `!important` 蓋過。
- 每段 override 前面寫註解：依據（Figma node / 設計 token）、取代了哪些舊規則行號、正式整併時可刪什麼。
- 交付正式環境時：override 可整併進對應原 selector、拿掉 `!important`。
- 只有「直接改原規則最乾淨」的情況（如移除某個 `:hover` 效果）才動原規則行。

## 字體規則（硬規定）

- 內文字體一律：`font-family:"Microsoft JhengHei","微軟正黑體","新微軟正黑體",sans-serif;`
- 設計稿標 `Noto Sans TC` **不要照用**，改微軟正黑體。
- `Font Awesome 5 Free`（`.fa/@font-face`）是**圖示字型**，動了 icon 會壞 —— 不要碰。
- `monospace`（normalize 對 `code/pre`）通常頁面沒用到，視為惰性、不用動。
- 改之前先 `grep -n font-family` 全盤掃一次，確認只剩微軟正黑體 + FontAwesome。

## 離線替身（C 區）—— 正式環境務必排除

mock 為了單檔可預覽，常把缺的資產換成替身，**這些不可進正式環境**：

- FontAwesome `@font-face` 指 CDN woff2
- 按鈕/星號/清除/箭頭/燈泡等用 inline SVG `data-uri` 取代（原站走 `../../images`）
- `body` 底色、欄寬 `.w2/.w5/...`（原站在沒打包的 `boxPage.css`/外層 layout）

需求文件要明確把這些列在「不需處理 / 排除」。

## 擷取 CSS 行號（給需求文件引用）

需求文件要標「改哪個檔、第幾行」。用 Python regex 抓當前行號（檔案一改就會位移，要重抓）：

```python
import re
lines=open('resumePoolNoticeMail.css',encoding='utf-8').read().split('\n')
def find(p): return [i+1 for i,l in enumerate(lines) if re.search(p,l)]
print(find(r'^\.headingBar \.Title\{'))
```

提醒需求文件讀者：行號是「隨附 mock 檔」的，正式 codebase 要用 selector 自己對。

## 本頁已落地的常見改法（可複用範式）

- **底線式頁籤**：容器 `.tabs` flex+gap32+底部 `#e9ecef` 細線；未選文字 `#212529`、hover `#1a66ff`、選中 `#1a66ff`+`::after` 4px 藍底線（圓角 80px）。底線用偽元素，**不加節點**。
- **頁籤+篩選「便當合併」**：兩個相鄰 sibling，上塊 `border-radius:10px 10px 0 0`+陰影、下塊 `0 0 10px 10px`+`z-index` 高一階蓋住接縫陰影。**前提是兩塊相鄰**（正式環境若不相鄰，要先搬 HTML —— 這是唯一要動 HTML 位置的需求，需在文件明講搬移）。
- **列 hover**：直接改原 `:hover`，`box-shadow:none; background:#FFF7F7`。
- **意願狀態**：正式結構是 `.td-status > p.reply-content.isReply/.isNotReply` ＋ `p.wish-content.isWish/.isNoWish`（`&nbsp;•&nbsp;` 分隔），`.mail-type` 只放類別。顏色：有意願 `#1D880D`、無意願 `#FF5D15`。**別把意願塞進 `.mail-type` 用 inline 上色**（那是前一手 mock 的偏離）。
