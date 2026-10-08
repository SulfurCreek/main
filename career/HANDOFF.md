<!--markdownlint-disable MD013-->

# 交接 / Session Handoff — career session

> **現役**：`session_017u5Po6SGpjD3iLBZ2VL2HH`，側欄「**Career Move**」（2026-09-29 接手；v1 `session_018VJFZiuZYfnPhMppvaGFcR`、v2 `session_01PKC4scvp58BuQxq5JKMHPw` 皆已 ARCHIVED）。分支 `claude/happy-lamport-ljis8c`。
> **2026-10-08 Repo Steward 健檢重建**：新增 [`library/`](library/README.md)（使用者提供資料庫）、修正矛盾檔、104 舊版歸檔、自有 skill 擁有權移交本 session。
> **開工順序**：[`library/README.md`](library/README.md) → 本檔 → [`CLAUDE.md`](CLAUDE.md)（硬規則一、二）→ [`competency-framework.md`](competency-framework.md)（wiki 入口）。其餘依任務按需讀取。

## 1. 你是誰、邊界在哪

- **角色**：替使用者（聶崑淮，1111 人力銀行求才產品企劃）讀 repo 既有產出 → 萃取成職能框架（F1–F15）、作品集、履歷素材；並操作 career-ops 求職工具。
- **只能寫 `career/` 與自有 skill**（`resume-craft`／`resume-review-panel`／`portfolio-site`，2026-10-08 起自己改自己推，commit 前綴 `career(skill):`）。全 repo 可讀。其餘 → 寫進 [`_requests-to-main.md`](_requests-to-main.md)，由 Repo Steward 施作。
- **使用者給的新事實、更正、決定 → 當下寫進 [`library/`](library/README.md)**（附日期與來源），再改下游檔。這是防止「忘記使用者提供過的資訊」的唯一機制。
- **只能 push `claude/happy-lamport-ljis8c`**。
- **不外流**：`career/` 內容絕不寫進 HackMD；對外版本抽象化 1111 內部名稱（API 名、欄位名、權限代碼、廠商／合作對象名稱）。
- 護欄 `scripts/guard_career_scope.sh` 只在本分支生效。這些規則在 2026-09-16 由使用者下達，前任曾越界（刪 `hackmd-api` 空殼、改根 `CLAUDE.md`），已還原。

## 2. 工作慣例（使用者已確認過的）

| 慣例 | 內容 |
| :--- | :--- |
| 語言與風格 | 繁中回覆、結論先行、簡短；wiki 為中英雙語 |
| 誠實契約 | 沒數字就寫 `〔待補數據〕`，**絕不捏造**；區分相關與因果；統計主張附 n 與顯著性 |
| 規模脈絡 ≠ 個人貢獻 | 公司營收、App 下載量只能當脈絡，不可寫成個人成果（見 `evidence-prior-products.md` 使用邊界表） |
| 數字版本 | 一律取 [`library/facts-1111.md`](library/facts-1111.md)、[`library/facts-prior.md`](library/facts-prior.md)；本頁不重複，避免兩處不同步 |
| 新職能判定 | 先對照 F1–F15，能歸入既有職能就不開新號（例：異業 API 合約 → 併入 F2＋F13，未開 F16） |
| 修改後驗證 | 跑相對連結檢查（見 §6），`git status` 確認只動到 `career/` |
| 使用者更正過的事實 | **全部收在 [`library/`](library/README.md)**（現行版）與 [`library/superseded.md`](library/superseded.md)（防倒退清單），本表不再逐條列 |

## 3. 檔案清單 / File index

### 入口與治理

| 檔案 | 內容 |
| :--- | :--- |
| [`CLAUDE.md`](CLAUDE.md) | 硬規則一（只寫 career/）、硬規則二（不外流）、目錄結構 |
| [`HANDOFF.md`](HANDOFF.md) | 本檔 |
| [`competency-framework.md`](competency-framework.md) | **wiki 入口**：定位、Profile Snapshot、路由表、F1–F15 總覽 |
| [`library/`](library/README.md) | **使用者提供資料庫**：`profile`、`facts-1111`、`facts-prior`、`decisions`、`superseded`、`open-questions` |
| [`_requests-to-main.md`](_requests-to-main.md) | 給主幹的變更請求（自有 skill 不必走這裡） |
| [`wiki/README.md`](wiki/README.md) | wiki 分頁目錄 |

### 職能分頁 `wiki/F01`–`F15`（定義 → 實際展現 → 證據 → 資深度訊號）

| # | 檔案 | 職能 | 期間 |
| :--- | :--- | :--- | :--- |
| F1 | [`F01-product-definition.md`](wiki/F01-product-definition.md) | 產品定義全鏈路 | 1111 |
| F2 | [`F02-spec-systems-thinking.md`](wiki/F02-spec-systems-thinking.md) | 功能規格與系統思維（含 2026/09 異業 API 契約、HMAC／重放／限流） | 1111 |
| F3 | [`F03-employer-platform.md`](wiki/F03-employer-platform.md) | 廠商端平台深度＋公司頁 | 1111 |
| F4 | [`F04-ai-product.md`](wiki/F04-ai-product.md) | AI 產品企劃（對客戶交付的 AI 功能） | 1111 |
| F5 | [`F05-delivery-quality.md`](wiki/F05-delivery-quality.md) | 交付流程與品質 | 1111 |
| F6 | [`F06-collaboration-handoff.md`](wiki/F06-collaboration-handoff.md) | 跨職能協作與知識交接 | 1111 |
| F7 | [`F07-process-tooling.md`](wiki/F07-process-tooling.md) | 流程標準化與工具化 | 1111 |
| F8 | [`F08-roadmap-delivery.md`](wiki/F08-roadmap-delivery.md) | 優先級、路線圖與交付節奏 | 1111 |
| F9 | [`F09-stakeholder-influence.md`](wiki/F09-stakeholder-influence.md) | 利害關係人管理與向上影響 | 1111 |
| F10 | [`F10-business-logic.md`](wiki/F10-business-logic.md) | 業務邏輯梳理 | 1111 |
| F11 | [`F11-problem-solving-ops.md`](wiki/F11-problem-solving-ops.md) | 問題解決與維運交付（工單週期治理） | 1111 |
| F12 | [`F12-consumer-mobile.md`](wiki/F12-consumer-mobile.md) | C 端行動產品與 0→1 | 2016–2022 |
| F13 | [`F13-monetization-pricing.md`](wiki/F13-monetization-pricing.md) | 變現、定價與金流（含異業 API 合約議定） | 2018–至今 |
| F14 | [`F14-localization-intl.md`](wiki/F14-localization-intl.md) | 國際化與在地化 | 2016–2018 |
| F15 | [`F15-ai-workflow-governance.md`](wiki/F15-ai-workflow-governance.md) | AI 協作系統設計與治理（分身工作制） | 1111 |

### 證據、履歷素材、作品集

| 檔案 | 內容 |
| :--- | :--- |
| [`wiki/flagship-e1.md`](wiki/flagship-e1.md) | 旗艦專案 E.1 跨系統聯絡人才（摘要） |
| [`portfolio/e1-cross-system-messaging.md`](portfolio/e1-cross-system-messaging.md) | E.1 完整 case study |
| [`wiki/evidence-paying-customers.md`](wiki/evidence-paying-customers.md) | 工單 × 付費客戶交叉分析、雙快照留存（+7pt、p=0.011）、年約當合約價值、定價 benchmark |
| [`wiki/evidence-prior-products.md`](wiki/evidence-prior-products.md) | 尚凡（TPEx 5278）財報、SweetRing／JustDating／KOOL／Juicy 上架資料、榜單成績（部落格來源，已標查證邊界）、拿不到的資料 |
| [`wiki/resume-extract.md`](wiki/resume-extract.md) | **履歷 bullet 草稿基底**（中英對照） |
| [`wiki/prior-roles.md`](wiki/prior-roles.md) | 2013–2022 職涯時間軸、下架產品寫法、兩處待釐清不一致 |
| [`wiki/education-certifications.md`](wiki/education-certifications.md) | 淡江國企、CSUS 交換、TOEIC 980、AWS CCP、TOEFL 93、GEPT |
| [`wiki/pm-vocabulary-map.md`](wiki/pm-vocabulary-map.md) | 50 個 PM／AI 語彙 → 證據對照（✅25 🟡15 ⚠️10）、LTV 推導 |
| [`wiki/growth-edges.md`](wiki/growth-edges.md) | 下一步補強建議與證據缺口 |

### 104 求職 `104/`

| 檔案 | 內容 |
| :--- | :--- |
| [`104/README.md`](104/README.md) | 104 工作區入口：職缺分析、職缺分級、履歷逐欄內容、Claude in Chrome 操作手冊 |
| [`104/resume-104-v5.2.txt`](104/resume-104-v5.2.txt) | **現行版**（2026-10-08）；改版另存新版號，舊版移入 `104/archive/` |

### 求職信 `letters/`

| 檔案 | 內容 |
| :--- | :--- |
| [`letters/README.md`](letters/README.md) | 求職信資料庫入口與規則 |
| [`letters/story-bank.md`](letters/story-bank.md) | 定位句／成果證據／動機鉤子／收尾素材（中英，附來源） |
| [`letters/log.md`](letters/log.md) | 投遞紀錄 |
| `letters/archive/` | 寫好的信（含 2022 Positive Grid 舊信＋檢討） |

### career-ops（求職工具）

| 檔案 | 內容 |
| :--- | :--- |
| [`career-ops/README.md`](career-ops/README.md) | 資料層說明、`CAREER_OPS_ROOT` 設定、版控規則（PDF ≤ 1MB）、同步規則（wiki → 這裡，單向） |
| [`career-ops/cv.md`](career-ops/cv.md) | 英文 CV |
| [`career-ops/config/profile.yml`](career-ops/config/profile.yml) | 設定檔，含 TODO |
| `career-ops/reports/`、`output/`、`data/` | career-ops 產出（評估報告、PDF、投遞追蹤），經 `CAREER_OPS_ROOT` 直接寫在這裡 |

## 4. 工作歷程摘要

1. 建立 F1–F11 框架 → wiki 化（入口＋分頁）。
2. E.1 旗艦專案寫成 case study。
3. 工單 × 付費客戶交叉分析、公開牌價 benchmark、工單週期治理（–69%）。
4. 雙快照留存分析：原始檔 `UA_6349.xlsx`（2026/04/30）、`UA_7017.xlsx`（2026/07/07）是使用者上傳檔，**不在 repo**，結果已寫入 `evidence-paying-customers.md`；要重算需請使用者重新上傳。
5. 前段職涯公開數據調查 → F12–F14、`evidence-prior-products.md`。
6. F15 AI 協作治理（來源：使用者的分身工作制 artifact）。
7. 2026-09-16 同步主幹、接受唯讀邊界、還原越界檔案。
8. 異業 API 合約（2026/09 起，進行中）→ 併入 F2、F13；pm-vocabulary-map #32、#35 升 ✅。
9. 2026-09-29 建立 career-ops 資料層；career-ops 本體由環境 setup script clone 到 `/home/user/career-ops`。
10. 2026-09-29 換手；主幹施作兩條請求（`7a0dbee`）；改用 `CAREER_OPS_ROOT` 讓產出直接落在 `career/career-ops/`。

## 5. 未完成事項

| 項目 | 狀態 | 位置 |
| :--- | :--- | :--- |
| **`CAREER_OPS_ROOT` 環境變數**：已改為直接讀寫 repo（不再 cp）；需使用者在環境設定加入 | 等使用者設定 | `career-ops/README.md` |
| 所有待使用者回答的事實題 | 集中在 [`library/open-questions.md`](library/open-questions.md)，問之前先查，答完寫回 library | `library/` |
| growth-edges 缺口：AI 功能採用、續約因果歸因、A/B 實驗主導 | 長期 | `wiki/growth-edges.md` |

### v2 session 未結案項目（2026-09-29）

| 項目 | 狀態 |
| :--- | :--- |
| 104 職缺無法直接抓：2026-09-29 v3 已把代理 CA 匯入 `~/.pki/nssdb`，Chromium 可正常開 HTTPS；但 104 首頁回 502、搜尋頁卡 Cloudflare「Just a moment」驗證（403） | 請使用者貼 JD 全文 |
| 已評估：和泰聯網「去趣」旅遊 App PM（3.4/5，職級偏低、Test Plan／親自執行測試待確認、無旅遊產業經驗）；評估結果只在對話中，**未寫成 report** | 使用者尚未決定是否投遞 |
| F5 已補測試案例設計＋QA 協作證據（`9512810`）；待確認：Test Plan 產出、是否親自執行測試與工具 | 等使用者回答 |
| T11669 在留言紀錄中看不到使用者名字：面試只能講「單據 owner、追蹤測試與範圍異動、必要時介入」 | 使用者可補具體介入內容 |

## 6. 常用指令

```bash
# 相對連結檢查（改完 wiki 必跑）
python3 - <<'EOF'
import re, pathlib
bad = []
for p in pathlib.Path('career').rglob('*.md'):
    for m in re.finditer(r'\]\(([^)#\s]+)', p.read_text()):
        t = m.group(1)
        if t.startswith(('http', 'mailto')): continue
        if not (p.parent / t).resolve().exists(): bad.append(f'{p}: {t}')
print('\n'.join(bad) or '✅ links OK')
EOF

# 同步主幹（career/ 以外衝突一律取 main）
git fetch origin main && git merge origin/main
```

- 履歷產出：`Skill` 載入 `resume-craft`（已涵蓋 F1–F15；這個 skill 現在歸你維護）。

## 待辦（2026-10-08 健檢後）

- 健檢報告：Repo Steward 在 main 的對話中產出（見使用者轉達）。重點：事實改以 `library/` 為準；`wiki/evidence-prior-products.md` 前段舊層未刪，只加了指向 library 的橫幅。
- `library/open-questions.md` Q1（Juicy 角色）會影響前段職涯 bullet，下次與使用者對話時優先確認。
