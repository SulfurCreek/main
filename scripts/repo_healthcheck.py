#!/usr/bin/env python3
"""Repo 健檢：分支耦合、skill 重複、索引完整性。輸出 Markdown 報告到 stdout。

用法：
    python3 scripts/repo_healthcheck.py            # 全部檢查
    python3 scripts/repo_healthcheck.py --section branches
"""

import argparse
import hashlib
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TRUNK = "origin/main"

# 只有主幹管理 session 可以改的共用資產（見 CLAUDE.md 多 session 治理規則 #2）
SHARED_PATHS = (
    "CLAUDE.md",
    ".claude/skills/",
    ".claude/settings.json",
    ".claude_index.md",
    "wiki/",
    "scripts/",
)

STALE_DAYS = 60


def git(*args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(REPO), *args], capture_output=True, text=True, check=False
    ).stdout.strip()


def remote_branches() -> list[str]:
    out = git("for-each-ref", "--sort=-committerdate", "--format=%(refname:short)", "refs/remotes/origin")
    return [b for b in out.splitlines() if b != "origin/HEAD"]


def check_branches() -> list[str]:
    lines = ["## 1. 分支耦合與漂移", ""]
    lines += ["| 分支 | 最後更新 | 落後 main | 超前 main | 動到的共用資產 |", "| :--- | :--- | ---: | ---: | :--- |"]
    coupled = []
    for br in remote_branches():
        if br == TRUNK:
            continue
        date = git("log", "-1", "--format=%cs", br)
        counts = git("rev-list", "--left-right", "--count", f"{TRUNK}...{br}")
        behind, ahead = (counts.split() + ["?", "?"])[:2]
        changed = git("diff", "--name-only", f"{TRUNK}...{br}")
        hits = sorted({p for p in SHARED_PATHS for f in changed.splitlines() if f.startswith(p)})
        if hits:
            coupled.append((br, hits))
        lines.append(f"| `{br.removeprefix('origin/')}` | {date} | {behind} | {ahead} | {'／'.join(hits) if hits else '—'} |")
    lines.append("")
    if coupled:
        lines.append(f"⚠️ **{len(coupled)} 支分支改到共用資產**，合併時必然衝突。處理原則：共用檔一律以 main 為準，分支只保留自己的 deliverable。")
        for br, hits in coupled:
            lines.append(f"* `{br.removeprefix('origin/')}` → {'、'.join(hits)}")
    else:
        lines.append("✅ 沒有分支改到共用資產。")
    return lines


def skill_digest(ref: str, name: str) -> str | None:
    """該分支上某個 skill 目錄的內容雜湊；不存在回 None。"""
    tree = git("ls-tree", "-r", f"{ref}:.claude/skills/{name}")
    return hashlib.sha1(tree.encode()).hexdigest()[:8] if tree else None


def check_skills() -> list[str]:
    lines = ["## 2. Skill 盤點與重複造輪", ""]
    trunk_skills = sorted(p.name for p in (REPO / ".claude/skills").iterdir() if p.is_dir())
    lines.append(f"主幹收錄 **{len(trunk_skills)}** 個 skill：{'、'.join(f'`{s}`' for s in trunk_skills)}")
    lines.append("")

    # 各分支上有、但主幹沒有的 skill；以及同名但內容不同的
    extra: dict[str, list[str]] = {}
    diverged: dict[str, list[str]] = {}
    for br in remote_branches():
        if br == TRUNK:
            continue
        names = [ln.split("/")[0] for ln in git("ls-tree", "--name-only", f"{br}:.claude/skills").splitlines()]
        for name in names:
            if name not in trunk_skills:
                extra.setdefault(name, []).append(br.removeprefix("origin/"))
            elif skill_digest(br, name) != skill_digest(TRUNK, name):
                diverged.setdefault(name, []).append(br.removeprefix("origin/"))

    if extra:
        lines += ["### 分支有、主幹沒有（評估是否納管）", ""]
        for name, brs in sorted(extra.items()):
            lines.append(f"* `{name}` — 出現在 {'、'.join(brs)}" + ("　⚠️ 多支重複造輪" if len(brs) > 1 else ""))
        lines.append("")
    if diverged:
        lines += [
            "### 同名但內容已分歧",
            "",
            "「分支較舊」＝分支拿的是主幹的舊版，不用管；**「分支較新」才需要人工比對**，可能有主幹沒吸收的東西。",
            "",
        ]
        for name, brs in sorted(diverged.items()):
            trunk_date = git("log", "-1", "--format=%cs", TRUNK, "--", f".claude/skills/{name}")
            marks = []
            for b in brs:
                b_date = git("log", "-1", "--format=%cs", f"origin/{b}", "--", f".claude/skills/{name}")
                newer = "🔺分支較新" if b_date > trunk_date else "分支較舊"
                marks.append(f"{b}（{b_date}，{newer}）")
            lines.append(f"* `{name}` — 主幹版 {trunk_date}；{'、'.join(marks)}")
        lines.append("")
    if not extra and not diverged:
        lines.append("✅ 所有分支的 skill 都已被主幹涵蓋且無分歧。")

    # SKILL.md 基本體檢
    broken = []
    for name in trunk_skills:
        f = REPO / ".claude/skills" / name / "SKILL.md"
        if not f.exists():
            broken.append(f"`{name}` 缺 SKILL.md")
            continue
        head = f.read_text(encoding="utf-8")[:400]
        if not head.startswith("---") or "description:" not in head:
            broken.append(f"`{name}` 的 SKILL.md 缺 frontmatter name/description（不會被自動載入）")
    if broken:
        lines += ["", "### SKILL.md 格式問題", ""] + [f"* {b}" for b in broken]
    return lines


def check_index() -> list[str]:
    lines = ["## 3. 索引與路由完整性", ""]
    index = (REPO / ".claude_index.md").read_text(encoding="utf-8")
    claude_md = (REPO / "CLAUDE.md").read_text(encoding="utf-8")

    tracked = git("ls-files").splitlines()
    watched = [f for f in tracked if f.startswith(("wiki/", "scripts/", "notes/")) or f in ("CLAUDE.md", "tree.md")]
    missing = [f for f in watched if Path(f).name not in index]
    if missing:
        lines.append(f"⚠️ **{len(missing)} 個檔案不在 `.claude_index.md`**（新 session 查不到就會重造）：")
        lines += [f"* `{f}`" for f in missing[:25]]
        if len(missing) > 25:
            lines.append(f"* …另外 {len(missing) - 25} 個")
    else:
        lines.append("✅ 受管目錄的檔案都有進索引。")
    lines.append("")

    unrouted = [
        p.name
        for p in (REPO / ".claude/skills").iterdir()
        if p.is_dir() and p.name not in claude_md
    ]
    if unrouted:
        lines.append(f"⚠️ **{len(unrouted)} 個 skill 沒出現在 CLAUDE.md 路由表**（等於沒人知道它存在）：{'、'.join(f'`{s}`' for s in unrouted)}")
    else:
        lines.append("✅ 所有 skill 都在 CLAUDE.md 路由表裡有對應任務類型。")
    lines.append("")

    orphan = [str(p.relative_to(REPO)) for p in (REPO / "wiki").rglob("*.md") if p.name not in claude_md and p.name not in index]
    if orphan:
        lines.append(f"⚠️ wiki 孤兒檔（CLAUDE.md 與索引都沒提到）：{'、'.join(f'`{o}`' for o in orphan)}")
    return lines


def check_bulk() -> list[str]:
    lines = ["## 4. 體積與雜物", ""]
    big = []
    for f in git("ls-files").splitlines():
        p = REPO / f
        if p.is_file() and p.stat().st_size > 1_000_000:
            big.append((f, p.stat().st_size // 1024))
    if big:
        lines.append("⚠️ 進版控的大檔（>1MB，考慮移出或改放分支）：")
        lines += [f"* `{f}` — {kb} KB" for f, kb in sorted(big, key=lambda x: -x[1])[:10]]
    else:
        lines.append("✅ 沒有超過 1MB 的版控檔案。")
    return lines


SECTIONS = {"branches": check_branches, "skills": check_skills, "index": check_index, "bulk": check_bulk}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--section", choices=list(SECTIONS), action="append")
    args = ap.parse_args()
    chosen = args.section or list(SECTIONS)

    print(f"# Repo 健檢報告\n\n> 產生時間：{git('log', '-1', '--format=%cs', 'HEAD')} 之後執行；主幹基準 `{TRUNK}` = `{git('rev-parse', '--short', TRUNK)}`\n")
    for key in chosen:
        print("\n".join(SECTIONS[key]()))
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
