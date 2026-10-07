# 交接：E320 未讀篩選線框圖 PNG 上傳 R2

## 目標
把 `handoff/wireframes/E320_unread/E320_unread_s1.png` ～ `s7.png` 上傳到 R2，驗證每個網址回 200，回報七個網址。

## 範圍（只做這件事）
- 只上傳與驗證，不改 `index.html`、PNG、HackMD 文件，也不動 `CLAUDE.md`、`.claude/`、`wiki/`、`scripts/`。
- 分支：`claude/lofi-wireframer-skill-0u25rk`（PNG 已在上面）。開工前 `git fetch origin claude/lofi-wireframer-skill-0u25rk` 並確認在這條分支。

## 前置檢查
1. 四個環境變數必須有值，缺任一個就停下來告訴使用者，不要硬編：
   `R2_ENDPOINT_URL`、`R2_ACCESS_KEY_ID`、`R2_SECRET_ACCESS_KEY`、`R2_PUBLIC_URL_BASE`（`R2_BUCKET` 可選，預設 `agent-image-dump`）。
   ```bash
   for v in R2_ENDPOINT_URL R2_ACCESS_KEY_ID R2_SECRET_ACCESS_KEY R2_PUBLIC_URL_BASE; do [ -n "${!v}" ] && echo "$v set" || echo "$v MISSING"; done
   ```
2. 這個環境沒有 `boto3`，先 `pip install boto3`。
3. 規則來源：`.claude/skills/photo/SKILL.md` 的 R2 段落（key 前綴 `photo-skill/`、憑證只讀環境變數、不把任何金鑰寫進檔案或 commit）。

## 檔名對照（key = `photo-skill/<檔名>`）
| 狀態 | 檔名 | 內容 | 預期尺寸 |
| :--- | :--- | :--- | :--- |
| S1 | `E320_unread_s1.png` | 預設：tag＝不拘，3.3~3.7 disabled | 2364×2174 |
| S2 | `E320_unread_s2.png` | 選「未讀」：3.1a，3.2 與操作項右移 | 2364×2174 |
| S3 | `E320_unread_s3.png` | S2＋勾選履歷，3.3~3.7 enabled | 2364×2174 |
| S4 | `E320_unread_s4.png` | 已排除 0 筆已讀 | 2364×2174 |
| S5 | `E320_unread_s5.png` | 空畫面 b | 2364×1712 |
| S6 | `E320_unread_s6.png` | 點「查看＞」後還原 | 2364×2374 |
| S7 | `E320_unread_s7.png` | 空畫面 a／b 並排對照 | 2364×1388 |

## 上傳與驗證
```python
import os, boto3
s3 = boto3.client('s3',
    endpoint_url=os.environ['R2_ENDPOINT_URL'],
    aws_access_key_id=os.environ['R2_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['R2_SECRET_ACCESS_KEY'],
    region_name='auto')
bucket = os.environ.get('R2_BUCKET', 'agent-image-dump')
for i in range(1, 8):
    name = f'E320_unread_s{i}.png'
    s3.upload_file(f'handoff/wireframes/E320_unread/{name}', bucket, f'photo-skill/{name}',
                   ExtraArgs={'ContentType': 'image/png'})
    print(f"{os.environ['R2_PUBLIC_URL_BASE']}/photo-skill/{name}")
```
上傳後對**印出的每個最終網址**（不是腳本內的檔名變數）逐一驗證：
```bash
curl -sI "<網址>" | head -1    # 必須 HTTP/2 200
```
有任何一個不是 200 就回報該網址與狀態碼，不要隱瞞。

## 回報格式
1. 七個 R2 網址（S1～S7 對照表）。
2. 七個 `curl -sI` 結果。
3. 提醒使用者：之後交給文件助手——S1～S4、S6 嵌進 §3，S5 嵌進空畫面 b，S7 作對照用。

## 同時帶給使用者的「文件待確認」清單（原樣轉述，不要自行決定）
1. 空畫面 b 時，3.2 全選與 3.3~3.7 是否顯示（文件只說 3.1a 仍顯示；S5 以虛線框標出）。
2. 空畫面 b 的垂直間距（3.1a→標題、標題→5），文件沒定義，圖中為估值。
3. 最末頁整頁皆已讀時，敘述「請點擊下一頁繼續查看」但 5 的「下一頁」按鈕已隱藏，文案是否沿用。
4. 「不設獨立下一頁按鈕」是只指空畫面內不放按鈕，還是連 5 的「下一頁」也不顯示？圖中先依前者畫。
5. 3.1a 的字重與「查看＞」樣式（Figma 未授權，依相鄰元件推估）。
6. 選「未讀」以外的 tag（已讀／追蹤中…）時，3.1 是否有對應變化。
7. 「查看＞」還原後停在第幾頁、其他篩選條件是否保留。
8. 換頁時勾選狀態與全選是否保留。
9. 權限隱藏（廠商 showfield 33554432、帳號權限 51）是任一缺少即隱藏，還是兩者皆缺才隱藏。
10. 真實 UI 的 3.4 文字是「追蹤」，文件標題寫「3.4 加入追蹤」，兩者不一致。
