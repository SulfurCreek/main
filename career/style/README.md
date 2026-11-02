<!--markdownlint-disable MD013-->

# style/ 語氣與規範路由（中英分流）

> 2026-11-02 本人指定：中英文履歷維度差很多，**語氣規則與工具分流、互不影響**。事實層（`library/`）、編譯核心與 Final Arbiter 兩邊共用。

## 先選語言，再讀對應檔

| 輸出語言 | 語氣規範（唯一） | 編譯護欄 | 驗證與產出工具 |
| :-- | :-- | :-- | :-- |
| **中文**（104 履歷、自傳、中文推薦信） | [`resume-voice-zh.md`](resume-voice-zh.md)（輔：`pm-resume-best-practices-zh.md`、`leaving-reason-source.md`、`autobio-storyteller-source.md`） | `.claude/skills/resume-causal-logic-compiler/references/zh-voice-guardrails.md` | `scripts/verify_polish.py`、`scripts/gen_104_md.py`、`scripts/verify_letter.py`（中文信） |
| **英文**（LINE Resume／LinkedIn／英文 CV／英文條列） | [`voice-en.md`](voice-en.md) | `.claude/skills/resume-causal-logic-compiler/references/en-voice-guardrails.md` | `scripts/verify_line_profile.py`、`scripts/verify_line_pdf.py`、`scripts/build_line_pdf.py`、`scripts/gen_line_pack.py` |

## 不互相套用的例子

- 只屬中文：「建立」「救回」計數、前 20 字張力、`[AMPLIFY: 主導]` 白名單、Quill HTML 與紅字、自傳。
- 只屬英文：全篇第一人稱 `I` ≤3、`direct reports`／`delegated`、日期 `YYYY/MM` 與 `YYYY-MM – YYYY-MM`、禁 `Reverse-engineered`、Title Case Skills、2 頁上限、不放自傳。
- 混合文件（中文推薦信含英文條列）：中文段落走中文規則，英文條列走英文規則。
- **唯一橋接**：英文版要完整保留對應中文版的商業目的、影響範圍與口徑（`voice-en.md` §7、en 護欄〈跨語言一致性〉）。

## 其他檔案（共用參考，不當規則）

`ats-2026-source.md`、`hr-6-second-source.md`（ATS／HR 來源，英文內容為主）、`anti-ai-ats.md`（去 AI 感以中文為主，ATS 部分兩邊可參考）、`scoring-improvement-*.md`、`de-ai-reverse-engineering-source.md`、`external-review-chatgpt-2026-10-12.md`、`postmortem-2026-10-08-deliverables.md`：歷史來源與評分素材；中文為主，英文產出不以它們為規則。

## Codex 端的中英分流（2026-11-02）

Codex 的 `career/02_codex_stage/voice_style_guide.md` 已於 Codex 分支 `codex/resume-writer` @ `3701462` 拆為「中文潤飾」「英文潤飾」兩個互不引用的章節，`drafts/codex/AGENTS.md` 先選語言再選規則與驗證入口。規則內容以本目錄為準；Codex 的檔案只有 Codex 寫，這裡只記版本。若日後 Codex 的指南與本目錄不一致，列為待辦由使用者轉達，不由 Claude 代改。
