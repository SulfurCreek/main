# 個人線協作規則：Career Move × 作品集網站助手

> 適用兩個 session：**Career Move**（`session_017u5Po6SGpjD3iLBZ2VL2HH`，管內容）與 **作品集網站助手**（`session_01X5B4jtorqQNpioe46ePnFs`，管渲染）。
> 共用分支 `claude/happy-lamport-ljis8c`。本檔只有 Repo Steward 能改。2026-10-05 起生效。

## 1. 目錄所有權（一個目錄只有一個寫入者）

| 路徑 | 唯一寫入者 | 另一方 |
| :--- | :--- | :--- |
| `career/portfolio/*.md`（內部完整版）、`career/wiki/`、`career/letters/`、`career/career-ops/` 等 | Career Move | 作品集助手：**不讀來當網站內容** |
| `career/portfolio/public/*.md`（對外版） | Career Move | 唯讀，網站唯一內容來源 |
| `career/portfolio/public/STATUS.md`（回覆與核可紀錄） | Career Move | 唯讀 |
| `career/site/**`（網站原始碼、`QUESTIONS.md`） | 作品集網站助手 | Career Move 不動 |

`career/` 以外兩邊都唯讀（`scripts/guard_career_scope.sh` 擋）。護欄分不出是哪個 session，目錄分工靠本規則與兩邊遵守，不靠 hook。

## 2. 交接流程

```text
作品集助手 ──QUESTIONS.md──▶ Career Move ──STATUS.md＋public/*.md──▶ 作品集助手
   （缺什麼、哪裡不能公開）      （回覆、產對外版、使用者核可後標 ready）     （只渲染 ready 的頁）
```

1. **對外版**：Career Move 從內部版產出 `career/portfolio/public/<slug>.md`，依 `resume-craft/references/portfolio.md` 的 NDA 去識別化規則。檔頭 front matter：
   ```yaml
   ---
   publish: draft        # draft | ready；ready 只能在使用者於 Career Move 對話明確核可該頁文字後才設
   source: ../<內部版檔名>
   highlights:           # 首頁成果數字卡，最多 3 條；沒有就留空，不編
     - label: ...
       value: ...
   ---
   ```
2. **作品集助手只渲染 `publish: ready` 的對外版**。內部版不當網站內容來源，缺內容一律寫進 `career/site/QUESTIONS.md`（編號 Q1、Q2…，每題一個位置與規則），不自己補、不編數字。
3. **Career Move 回覆**寫在 `STATUS.md`（Q 編號、答覆、日期），不改 `QUESTIONS.md`。
4. 公開與否的**預設值（保守）**：不寫公司名、不寫 HackMD／內部 wiki／RAG 索引、時間線只寫年資級距。使用者在 Career Move 明說放寬，才記進 `STATUS.md` 的「使用者決定」表，作品集助手以該表為準。

## 3. Git 規則

- 兩個 session 都在同一分支：每次推送前 `git pull --rebase origin claude/happy-lamport-ljis8c`；**禁止 force push**；只 commit 自己的目錄。
- commit 訊息前綴：Career Move 用 `career:`，作品集助手用 `site:`。
- 目錄不重疊，所以不會有檔案衝突；真的衝突就停下來回報使用者。

## 4. 沒有直接對話：由使用者轉達

雲端 session 之間 `SendMessage` 送不到（2026-09-29 實測）。每次交接，推完後在回報最後一行寫「請到〈另一個 session〉說：請看 <檔案路徑>」，由使用者貼過去。

## 5. 發布閘門

- `career/site/` 是**暫存區**（本 repo 私有、不從這裡部署）。要上線時，由使用者決定目標 repo（GitHub／Cloudflare Pages），作品集助手把 `career/site/` 的成品複製過去。
- 預設 `noindex, nofollow`＋`robots.txt`，使用者明說公開才移除。
- 網站上不得出現：`〔待補…〕`／`TODO`、內部 API 名／欄位名／權限代碼、客戶與廠商名、電話住址生日。

## 6. 需要改規則時

兩邊都寫進各自可寫的地方請主幹施作：Career Move 用 `career/_requests-to-main.md`；作品集助手用 `career/site/QUESTIONS.md` 開頭加「請主幹：…」。
