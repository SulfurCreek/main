<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

# 給主幹（Repo Steward）的變更請求 / Requests to main

本檔由 `claude/happy-lamport-ljis8c`（career session）依硬規則一寫入，**不自行修改** `career/` 以外的檔案。
請主幹判斷後統一施作，施作後可清空對應條目。

---

## 2026-09-16：`resume-craft` skill 的職能編號已過期（F1–F11 → 應為 F1–F15）

**想改什麼**：
1. `description` frontmatter：「把 F1–F11 職能或專案變成履歷條目」→ 改為 F1–F15。
2. `SKILL.md:145`：`取 \`wiki/F01…F11-*.md\`` → 改為 `F01…F15-*.md`。
3. 核心職能叢集表（若有）：補上 F12（0→1 & Consumer Mobile）、F13（Monetization & Pricing）、
   F14（Internationalization）、F15（AI Workflow & Agent Governance）三筆叢集對映——這三個叢集在合併前
   本分支曾經加過，但合併後 skill 內容以主幹版本為準，故目前遺失。

**為什麼**：`career/wiki/` 這邊在本分支已擴充到 F15（見 `career/competency-framework.md` 的核心職能總覽），
skill 若停在 F1–F11，會在「依框架產出履歷」時漏掉四個職能（含最新的 F15 AI 協作系統設計與治理）。
這不影響 career/ 內容本身的正確性，只影響 `resume-craft` 讀取 wiki 時的覆蓋範圍。

**參考**：合併前本分支版本的叢集表（供對照，非要求照抄）：

```
| 0→1 & Consumer Mobile | **F12** | 3 個 0→1 ＋ 4 個既有產品；iOS／Android／RWD 三端；MVP 交付 |
| Monetization & Pricing | **F13** | IAP 模型與價格點、第三方金流串接、配額計價、牌價結構分析 |
| Internationalization | **F14** | 7 市場在地化、跨文化團隊、TOEIC 980 |
| AI Workflow & Agent Governance | **F15** | 12 條分身／23 skill 的多代理系統；SSOT、重複偵測、事故後機制修復 |
```

---
