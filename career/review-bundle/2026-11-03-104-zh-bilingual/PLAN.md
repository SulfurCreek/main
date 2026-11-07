# 計畫 r3：104 最新中文履歷 → 中英雙語履歷（2026-11-03，本人已指示直接推進）

> 個資檔，不外流。r3 依本人最終裁定修訂（見 `library/decisions.md` 2026-11-03 最終裁定）。

## 一、裁定摘要

| 項目 | 裁定 |
| :-- | :-- |
| 中文基底 | **一般版**（保留產品真名；雙語公開版不做，除非本人另行要求） |
| 簡介 `info.bio` | 只放英文：LINE Summary 原文＋空一行＋`An English CV is available on request.`（逐字鎖定） |
| 工作經歷 4 筆 | 只放中文（v12.20 原文，逐字） |
| 專案說明 4 筆 | 英文先行＋空段落＋中文 |
| 專長 6 筆說明 | 英文先行＋空行＋中文；**字數上限未量測（fields-spec 無此欄位上限）→ 驗收 Exit 3「未可填表」，需本人量測或 Antigravity 填表時量**；放不下時改維持原中文 |
| 其餘欄位（個人特色、經歷標籤、可自選技能、證照、語文、求職條件、自傳、專案名稱／起訖／圖片／網址） | 全部維持原設定 |
| 驗證契約 | `final_resume.md` 保留標記，`verify_polish.py` 為唯一權威 Gatekeeper；104 檔由 `gen_104_md.py` 產、`--verify-104` 驗。**不用** `check_polish_structure.py` 與 `.clean.md` |
| 英文 | 只擷取 LINE 原文（SHA＋映射雜湊鎖定），零改寫；Claude／Codex 皆不得新寫（CV 句為唯一核可例外） |

## 二、流程

### Step 1｜最新中文履歷 v12.20
1. Claude Stage 1–2：`library/`（含 11-03 九句）→ `01_claude_stage/causal_draft.md`；`verify_polish.py` 上游 0 違規。
2. Claude 端盲測（credibility-blind-prompt）→ A/B/C 分流。
3. Codex Stage 3：潤飾 → `final_resume.md`（自跑 `verify_polish.py`）。
4. Claude Stage 4：唯讀拉取 → `verify_polish.py` → `gen_104_md.py` 產一般版 104 md → `--verify-104`。
5. 定稿盲審（coach-prompt）→ 終審，收斂停機。

### Step 2｜雙語確定性組裝（無 Codex 看稿、無舊版比對、無重複盲審）
`python3 career/scripts/gen_104_bilingual.py --zh <v12.20 一般版> --out <雙語 md> [--limit bio=N --limit skill=N]`
→ 內建 strict 驗收（白名單逐位元組、SHA／映射雜湊、字數）通過才原子寫出 → 直接成品。

## 三、工具狀態
`md104.py`、`gen_104_bilingual.py`、`verify_104_bilingual.py` 完成，離線合成測試通過（全套 120 測試）。細節見 `career/scripts/README.md`。
