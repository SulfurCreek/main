"""Versioned bilingual assembly contract, not factual validation.
Human approval owns semantic suitability. Producer and checker import this contract independently.
"""
import hashlib
from pathlib import Path
import line_md

ROOT = Path(__file__).resolve().parents[1]
LINE_MD = ROOT / "drafts/line/line-resume.md"
LINE_SHA = "078b42cba4e3502d0d5865521a29e5ce5d5d83f585561c761155d2c0b09535f8"
CV_SENTENCE = "An English CV is available on request."  # D2：本人 2026-11-03 最終裁定，逐字鎖定（104 表單未必讓 HR 下載附件，此句最通用）
SUMMARY_SHA = "a9418b838075fd98"
# 專長英文：(種類, 位置, 預期原文 sha256 前 16 碼)
SKILL_SRC = [("summary_sentence", 2, "88609a28444bdcfd"), ("skills_line", 0, "e8d1c92fc48cb0c6"),
             ("bullet_sentences", (0, 5, 0, 2), "9782d3e847e2c137"), ("skills_line", 2, "6b3d3dc7522ac7c5"),
             ("summary_sentence", 1, "c3d377ee955aa3bd"), ("skills_line", 3, "99f07c0574a25381")]
# 專案英文：project index → [(經歷 index, 列點 index, 預期 sha)]；第一則 blockquote
PROJECT_SRC = {0: [(1, 4, "6379a38b331090dc")], 1: [(1, 3, "67181f7755f6d6de")],
               2: [(0, 5, "9782d3e847e2c137"), (0, 2, "c0455a0881b9340a")], 3: [(0, 6, "2602e84d5e02b777")]}
LIMITS_KNOWN = {"project": 2000, "skill": 1000, "bio": 1000}  # project：fields-spec；skill、bio：本人 2026-11-03 回報 104 頁面上限各 1000 字

def sha16(s):
    return hashlib.sha256(s.encode()).hexdigest()[:16]


def sentences(text):
    import re
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z(])", text.strip()) if s.strip()]


def english_units(line_text, line_sha=None):
    """依鎖定映射取英文：回傳 (summary, skills[6], projects{idx: [列點原文]})；任何來源不符即 ValueError。"""
    line_sha = line_sha or LINE_SHA
    got = hashlib.sha256(line_text.encode()).hexdigest()
    if got != line_sha:
        raise ValueError(f"LINE 來源 SHA 不符：預期 {line_sha[:12]}…，實際 {got[:12]}…（LINE 已變動，需本人重新核可映射）")
    try:
        return _units(line_md.parse(line_text))
    except (IndexError, KeyError, TypeError) as e:
        raise ValueError(f"LINE 結構與映射不符（列點或句子位置不存在）：{e}")


def _units(doc):
    works = [x for x in doc["directives"] if x["d"]["target_block"] == "work_experience"]
    summ = doc["summary"]
    if sha16(summ) != SUMMARY_SHA:
        raise ValueError("Summary 原文雜湊不符")
    skills = []
    for kind, ref, want in SKILL_SRC:
        if kind == "summary_sentence":
            s = sentences(summ)[ref]
        elif kind == "skills_line":
            s = doc["skills"][ref]
        elif kind == "bullet_sentences":  # 連續整句，以單一空白相接（不改字）
            wi, bi, a, b = ref
            s = " ".join(sentences(works[wi]["bullets"][bi])[a:b])
        else:
            wi, bi, si = ref
            s = sentences(works[wi]["bullets"][bi])[si]
        if sha16(s) != want:
            raise ValueError(f"專長映射 {kind} {ref} 原文雜湊不符")
        skills.append(s)
    projects = {}
    for pi, srcs in PROJECT_SRC.items():
        items = []
        for wi, bi, want in srcs:
            b = works[wi]["bullets"][bi]
            if sha16(b) != want:
                raise ValueError(f"專案 {pi} 映射（經歷 {wi} 列點 {bi}）原文雜湊不符")
            items.append(b)
        projects[pi] = items
    return summ, skills, projects


