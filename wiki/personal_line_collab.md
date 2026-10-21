# 個人線協作規則：Career Move × 作品集網站助手 × Resume Writer

> 適用兩個 session：**Career Move**（`session_017u5Po6SGpjD3iLBZ2VL2HH`，管內容）與 **作品集網站助手**（`session_01X5B4jtorqQNpioe46ePnFs`，管渲染）。
> 2026-10-20 起新增第三方 **Resume Writer**（OpenAI Codex session，不是 Claude Code，**沒有 session_id**，不受 `guard_career_scope.sh` 約束，只靠指示約束）：文字編輯者，讀 `career/` 的事實把履歷與求職文件寫順。詳見本檔 §7。
> 共用分支 `claude/happy-lamport-ljis8c`（Resume Writer 用自己的分支，見 §7）。本檔只有 Repo Steward 能改。2026-10-05 起生效。

## 1. 目錄所有權（一個目錄只有一個寫入者）

| 路徑 | 唯一寫入者 | 另一方 |
| :--- | :--- | :--- |
| `career/portfolio/*.md`（內部完整版）、`career/wiki/`、`career/letters/`、`career/career-ops/` 等 | Career Move | 作品集助手：**不讀來當網站內容** |
| `career/portfolio/public/*.md`（對外版） | Career Move | 唯讀，網站唯一內容來源 |
| `career/portfolio/public/STATUS.md`（回覆與核可紀錄） | Career Move | 唯讀 |
| `career/site/**`（網站原始碼、`QUESTIONS.md`） | 作品集網站助手 | Career Move 不動 |

`career/` 以外兩邊都唯讀（`scripts/guard_career_scope.sh` 擋），**唯一例外**：個人線自有 skill `resume-craft`／`resume-review-panel`／`portfolio-site`／`104coverletter`／`104resume` 由 **Career Move** 改（2026-10-08 起；作品集助手要改 `portfolio-site` 時寫進 QUESTIONS.md 請 Career Move 改）。Steward 從本分支單向同步到 main，main 不直接改這五個目錄。護欄分不出是哪個 session，目錄分工靠本規則與兩邊遵守，不靠 hook。

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

改上述五個個人線 skill 不需主幹（Career Move 直接改、commit 前綴 `career(skill):`）。其餘兩邊都寫進各自可寫的地方請主幹施作：Career Move 用 `career/_requests-to-main.md`；作品集助手用 `career/site/QUESTIONS.md` 開頭加「請主幹：…」。

## 7. Resume Writer（Codex，2026-10-20 使用者決定納入）

| 項目 | 內容 |
| :--- | :--- |
| 角色 | 文字編輯者。事實唯一來源是 `career/library/`（Career Move 維護）；Resume Writer 只負責把事實寫成通順自然的文字，**不新增事實** |
| 讀取 | 只讀 `career/`；repo 其他目錄一律不碰 |
| 寫入 | 只寫 `career/drafts/codex/`（草稿、產出、`QUESTIONS.md`）。`library/`、`wiki/`、`style/`、`104/` 等一律唯讀 |
| 分支 | 自己的分支（建議 `codex/resume-writer`），**不推 `main`、不推 `claude/happy-lamport-ljis8c`**，不 force push |
| 事實有疑問 | 寫進 `career/drafts/codex/QUESTIONS.md`（編號、問題、出處），由使用者決定；Career Move 查證後更新 library 並答覆 |
| 取用成果 | 由使用者決定採用哪份產出。Career Move 只**讀取**（`git checkout origin/codex/resume-writer -- career/drafts/codex`），採用的內容由 Career Move 納入自己的檔案，不整支合併分支 |
| 約束方式 | 無 hook，只靠環境指示與 `AGENTS.md`；`AGENTS.md` 放 `career/drafts/codex/` 內，不放根目錄或 `career/` 根目錄，**不得在任何 `CLAUDE.md` 用 `@AGENTS.md` 引用**（否則會把 Codex 規則帶進 Claude session） |
| 隱私 | Resume Writer 能讀到的範圍取決於 Codex 環境連的 repo；若連 `SulfurCreek/main` 就讀得到整個 repo。真要隔離需另開只放 `career/` 的私有 repo（使用者尚未決定） |
