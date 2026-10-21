來源檔：Career Move `7839fd42a75c763ff12e4ee23fc1553ed3fa7ec7` 的 `career/01_claude_stage/causal_draft.md`、新版因果 skill、01 README、原版 verify_polish.py、中文／英文 style 與 About Me；本人本輪指令及長度補充。
〔待補〕：上游六處〔待補數據〕原樣保留，不補數字、不改寫。
事實疑問：無新增；本輪僅下游句法潤飾，未更動上游、library 或驗證程式。

# Stage 02 交付與修改紀錄（2026-10-21）

## 完成範圍

- 成品：[final_resume.md](../../02_codex_stage/final_resume.md)；語氣：[voice_style_guide.md](../../02_codex_stage/voice_style_guide.md)。上游已到位，前次缺稿阻塞解除。
- 掃描 20 點 NEEDS_POLISH、12 處 LOCKED。先複製正文保護鎖定，再依 1111（9 點）→尚凡（7 點）→SweetRing（4 點）逐職位改寫並寫入；每區完成標 POLISHED，全部完成後才移除 32 個狀態註解。過程的唯讀來源、逐區塊進度及帶標記工作快照留在本區 .scratch，不提交。
- 實體字典、拓撲大綱、檢查三節及所有交接標記均未進成品；成品不附來源或修改理由。
- 12 處 LOCKED 包含非條列的簡介、特色、自傳與專案區塊，整段文字均核對原樣保留，不只檢查原程式識別的單行 bullet。上游未標記的標題維持，只有一個標題末尾空格作 Markdown 空白清理，未改標題文字。
- 本人已回覆：**保留完整事實，65–85 字作節奏目標**。14 點超過 85 字，2 點少於 65 字；如實列在下表，不補字、不為行數刪事實，亦不宣稱所有點可排兩行。實際 104／PDF 排版由 Claude 做。
- 本人再次要求 12 處 LOCKED 原樣保留，因此禁詞替換僅適用 20 點 NEEDS_POLISH。鎖定區原有用語照留，沒有為清禁詞而改掉半字。

## 原版驗證：通過

來源草稿 blob：`297529bd56a05a7c70bff0d17f10952c3f9facbb`。
核對程式 blob：`8cdf80bc4d9d2735ce40d3006f0b9c2288f011c8`。

本分支不寫入 Claude 的 01 stage 或共用 scripts。以 git show 取得上述固定提交的原檔唯讀快照，兩檔均用 git hash-object 比對來源 blob 相同，再執行原程式：

```bash
python3 career/drafts/codex/.scratch/pipeline-7839fd4/verify_polish.py career/drafts/codex/.scratch/pipeline-7839fd4/causal_draft.md career/02_codex_stage/final_resume.md
```

結果：`✓ 全部通過`，exit 0。沒有修改核對程式、測試輸入或跳過檢查。

## 補充硬性檢查：通過

- 20 點各自保留原有 LOCK_ENTITIES 的字串及出現次數；不是依賴別點含相同詞來通過。
- 每點與全文正文的數字值及次數一致；全文比對先排除來源註解內重複列出的鎖定值，不把控制標記計作履歷數據。
- 12 處 LOCKED 完整內容相同；六個〔待補數據〕相同。
- 可改點無本輪中文禁詞，也無透過／藉由／利用；逗號、分號、句號與直線切開的子句均不超過 25 字。
- 字面改寫幅度以正規化 Levenshtein 字元編輯距離計：最少插入／刪除／替換次數，除以原／新文較長字數；不含 `- ` 與狀態註解。20 點為 30.0%–55.2%，全數至少 30%；不用它評判文案品質，不以加標點或廢話湊比例。
- 人工核對：未更換首次定義的概念次序，未反轉因果或數據比較，未新增權限、工程責任、效益或完成狀態。短句仍保留上游指定的 Result｜Action／限制關係。
- 格式自檢保留最後一個 LOCKED 區塊的來源末尾空行；Git 僅對 final_resume.md 放行來源繼承的 blank-at-eof，其餘 whitespace 檢查照常執行，不為 Git 格式檢查改動鎖定區塊。

## 逐點修改理由與字數

字數含標點、空格及英文字元，不含 bullet 符號；序號依源稿 32 個狀態區塊排列，因此跳過 1、2 及後續 LOCKED。

| 原區塊 | 職位 | 原字數 | 新字數 | 編輯距離比例 | 修改理由 |
| --- | --- | ---: | ---: | ---: | --- |
| 3 | Product Owner／PM | 135 | 122 | 31.1% | 精煉職位範疇，分開產品用途、規模、角色與協調責任；不放大主導權。 |
| 4 | Product Owner／PM | 80 | 92 | 34.8% | 以短句分開需求、設計、規格、驗收與協作上線，保留交付鏈。 |
| 5 | Product Owner／PM | 106 | 104 | 43.4% | 將沿用限制、無文件規則、還原方法及分階段改版切句；不變更因果。 |
| 6 | Product Owner／PM | 99 | 112 | 32.1% | 釐清使用對象、群組存取規則及資料範圍限制，保留轉換與上線。 |
| 7 | Product Owner／PM | 77 | 83 | 45.8% | 將回報來源寫清楚，保留「未再收到回報」範圍，不改成零事件。 |
| 8 | Product Owner／PM | 77 | 90 | 47.8% | 保留三項 AI 名稱與團隊分工，改為短句列舉及驗收／回饋動作。 |
| 9 | Product Owner／PM | 77 | 76 | 50.6% | 交付結果在前，整理同仁卡關、指導工具、同仁判斷及共同討論的句法；不加新的帶人事實。 |
| 10 | Product Owner／PM | 79 | 81 | 43.2% | 保留待補、進行中及長期需求，拆開分散情境、整合規劃與推進責任。 |
| 11 | Product Owner／PM | 118 | 136 | 33.1% | 保留兩期統計與滿期口徑，將客戶問題、排序及追蹤動作寫清楚；未改上游既定指標因果。 |
| 12 | Product Manager | 145 | 153 | 43.8% | 拆開產品類型、公開榜單、職責及英文洽談，不暗示成交。 |
| 13 | Product Manager | 170 | 174 | 32.2% | 保留規模、平台定義、訪談與三項方法；拆句保住 0 到 1 的完整原意。 |
| 14 | Product Manager | 88 | 95 | 42.1% | 釐清簡報、身分規則、甘特圖與測試／確認範圍；不增加工程實作。 |
| 15 | Product Manager | 193 | 219 | 39.7% | 兩段 DAU 分別帶回所屬期間，保留兩次下架承接及行銷／團隊歸因。 |
| 16 | Product Manager | 136 | 143 | 49.0% | 改用增減語句交代三階段觀察；對照組、期間、非續訂口徑及團隊採低價決策保留。 |
| 17 | Product Manager | 83 | 98 | 31.6% | 將付款占比、期間與付款轉向規劃拆開；保留 Peach 及智冠歸屬。 |
| 18 | Product Manager | 57 | 63 | 36.5% | 精煉 KOOL 付費功能的規劃與上線，不為 65 字填充內容。 |
| 19 | Associate PM | 87 | 85 | 55.2% | 移除可改點的禁詞，保留維運優化、完整國家名與非主導性的在地化／支付投入。 |
| 20 | Associate PM | 84 | 90 | 32.2% | 移除可改點的禁詞，保留題庫、發問、問答與操作銜接及團隊上線。 |
| 21 | Associate PM | 49 | 55 | 43.6% | 重組在地化結果、外籍實習生協作及全英文會議；不升級成直屬管理。 |
| 22 | Associate PM | 130 | 140 | 30.0% | 分開加值頁、CodaPay 可用付款管道及實收試算／訂閱方案；不新增金流商或成效。 |

## 來源、採用與同步狀態

- 新管線與語氣參數已寫入 Codex AGENTS／ROUTER／索引／wiki；舊 resume-editor 標為歷史，原健診 patch 明示不能整包套用回退新版因果 skill。
- 已讀回 About Me：既有職涯事實及偏好無需另建副本。本輪語氣參數與本人長度補充，交 Claude 按下段同步，**尚未讀回共同寫入，不說 About Me 已更新**。
- 此為 stage 02 已通過本地核對的交付稿，不等於本人最終定版。Claude 仍需讀回原稿重跑 verify_polish.py，之後才產 104／雙欄 PDF；本輪 PDF 未更新。

## 給 Claude 的接續指令

請 fetch `codex/resume-writer` 並固定提交，以 git show 讀 `career/02_codex_stage/final_resume.md`、`voice_style_guide.md` 與本交接；不要 checkout 或改寫 Codex 區。

用 `7839fd4` 的 causal_draft.md 對照 20 點改寫、12 處 LOCKED 與六處待補，再用原版 `career/scripts/verify_polish.py` 重跑。保留本人最新決定：65–85 字只是節奏目標，完整事實優先；不要重新要求將長點壓入兩行。

請在共同 About Me〈九〉同步本輪本人明確的協作要求：採 library→Claude 因果草稿→Codex 下游潤飾→Claude 核對／成品管線，Codex 只修 NEEDS_POLISH、LOCKED 與待補原樣保留；本人已選定 65–85 字作節奏目標，完整事實及因果優先。這是協作／文字偏好，不推論人格、能力或新增履歷事實。再依本人採用狀態產 104／PDF，不自行刪除待補或更新數字。
