# 工具清單（供核對；副本在本資料夾）

## Claude 端（本分支）
| 類別 | 檔案 | 用途 |
| :-- | :-- | :-- |
| 管線規則 | `claude/career/CLAUDE.md` | 四階段、盲測、終審與收斂停機 |
| Skill | `claude/.claude/skills/104resume/SKILL.md` | 104 特化版 md 產生規則 |
| Skill | `claude/.claude/skills/resume-causal-logic-compiler/` | 上游草稿編譯（禁前向引用、LEAD、LOCK） |
| 盲測 | `claude/.claude/skills/resume-review-panel/kit/credibility-blind-prompt.md` | Stage 2／4 Claude 端盲測 |
| 盲審 | `claude/.claude/skills/resume-review-panel/kit/coach-prompt.md` | 定稿 Coach 盲審 |
| 規格 | `claude/career/104/styling-directive-guide.md`、`fields-spec.md`、`content-spec-quill.md` | 104 欄位、Quill 樣式、directive |
| 規格 | `claude/career/104/antigravity-bilingual-fill-playbook.md` | 填表指令（將依新規格改寫） |
| 語氣 | `claude/career/style/README.md`、`resume-voice-zh.md`、`voice-en.md` | 中英語氣分流 |
| 腳本 | `claude/career/scripts/verify_polish.py` | 中文上下游驗收（含 --verify-104） |
| 腳本 | `claude/career/scripts/gen_104_md.py` | final_resume → 104 md |
| 腳本 | `claude/career/scripts/public_redact.py` | 公開版去識別化 |
| 腳本 | `claude/career/scripts/fact_lock.py` | 數字＋單位、鎖定事實、限定詞比對 |
| 腳本 | `claude/career/scripts/gen_104_bilingual.py`、`verify_104_bilingual.py` | 雙語組合與驗收（將依新規格改寫） |
| 腳本 | `claude/career/scripts/line_md.py`、`verify_line_profile.py` | 英文來源解析與英文語氣驗收 |
| 測試 | `claude/career/scripts/tests/` | 單元測試 |

## Codex 端（`origin/codex/resume-writer`，唯讀複本）
| 檔案 | 用途 |
| :-- | :-- |
| `codex/career/drafts/codex/AGENTS.md` | Codex 角色與邊界 |
| `codex/career/02_codex_stage/voice_style_guide.md` | 潤飾語氣規則 |
| `codex/career/drafts/codex/scripts/check_polish_structure.py` | Codex 自檢腳本 |
| `codex/career/drafts/codex/ROUTER.md`、`INDEX.md` | Codex 檔案路由 |
