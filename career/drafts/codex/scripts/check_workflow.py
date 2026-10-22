#!/usr/bin/env python3
"""Read-only checks for Resume Writer navigation and write boundaries.

No fetch, checkout, writes, commit, push, content grading, or read-completion claims.
Run after the explicit source fetch described in ROUTER.md.
"""
from pathlib import Path
import argparse
import json
import re
import subprocess
from urllib.parse import unquote

OWN = Path(__file__).resolve().parents[1]
CAREER = OWN.parents[1]
REPO = CAREER.parent
DEFAULT_REF = "origin/claude/happy-lamport-ljis8c"
DOCS = (
    "AGENTS.md", "ROUTER.md", "INDEX.md", "ROUTER-INTEGRATION.md",
    "skills/resume-editor/SKILL.md", "wiki/README.md", "wiki/skills.md",
    "wiki/editorial-regressions.md", "wiki/handoff-status.md",
    "wiki/versions.md", "wiki/collaboration.md", "wiki/research-and-tools.md",
    "wiki/validation-history.md", "2026-10-21-skills-healthcheck-and-claude-handoff.md",
    "2026-10-21-stage-pipeline-handoff.md", "../../02_codex_stage/voice_style_guide.md",
    "2026-10-21-stage-active-voice-handoff.md",
    "2026-10-22-r2-polish-handoff.md",
    "../../02_codex_stage/final_resume.md",
)


def git(*args):
    return subprocess.check_output(
        ["git", *args], cwd=REPO, text=True, stderr=subprocess.PIPE, timeout=20
    ).strip()


def run(source_ref):
    failures, warnings = [], []
    checked_links = 0
    if source_ref.startswith("-") or not re.fullmatch(r"[A-Za-z0-9_./-]+", source_ref):
        raise ValueError("Invalid source ref")
    branch = git("branch", "--show-current")
    if branch != "codex/resume-writer":
        failures.append("Working branch is not codex/resume-writer")
    sha = git("rev-parse", "--verify", source_ref + "^{commit}")
    for name in DOCS:
        path = OWN / name
        if not path.is_file():
            failures.append("Missing workflow document: " + name)
            continue
        text = path.read_text(encoding="utf-8")
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        text = re.sub(r"`[^`\n]*`", "", text)
        for raw in re.findall(r"\]\(([^\n)]+)\)", text):
            target = raw.strip().strip("<>")
            if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target) or target.startswith("#"):
                continue
            relative = unquote(target.split("#", 1)[0])
            resolved = (path.parent / relative).resolve()
            if not resolved.is_relative_to(CAREER):
                failures.append(name + ": link leaves career/: " + relative)
            elif not resolved.exists():
                failures.append(name + ": missing link target: " + relative)
            checked_links += 1
    registry = (OWN / "wiki/skills.md").read_text(encoding="utf-8")
    remote_paths = git("ls-tree", "-r", "--name-only", sha, "--", "career").splitlines()
    remote_skills = [p for p in remote_paths if p.endswith("/SKILL.md")
                     and "/drafts/codex/" not in p]
    for path in remote_skills:
        if path not in registry:
            failures.append("Shared skill is not indexed: " + path)
    local_skills = [p for p in OWN.rglob("SKILL.md")
                    if "archive" not in p.relative_to(OWN).parts
                    and ".scratch" not in p.relative_to(OWN).parts]
    for path in local_skills:
        relative = path.relative_to(OWN).as_posix()
        if relative not in registry:
            failures.append("Local skill is not indexed: " + relative)
    staged = git("diff", "--cached", "--name-only", "-z").split("\0")
    for path in filter(None, staged):
        if not path.startswith(("career/drafts/codex/", "career/02_codex_stage/")):
            failures.append("Staged path leaves Codex write scope: " + path)
    status = (OWN / "wiki/handoff-status.md").read_text(encoding="utf-8")
    recorded = re.search(r"Career Move `([0-9a-f]{40})`", status)
    if not recorded or recorded.group(1) != sha:
        warnings.append("Source changed since recorded handoff; read relevant changes before editing.")
    upstream_exists = "career/01_claude_stage/causal_draft.md" in remote_paths
    final_exists = (CAREER / "02_codex_stage/final_resume.md").is_file()
    if not upstream_exists:
        warnings.append("Pipeline input causal_draft.md is missing; final verification has not run. Do not push.")
        if final_exists:
            failures.append("Final resume exists without the required upstream input")
    historical_local = [p for p in local_skills if "status: historical" in p.read_text(encoding="utf-8")]
    result = {
        "source_commit": sha,
        "workflow_documents": len(DOCS),
        "relative_links_checked": checked_links,
        "shared_skills_indexed": len(remote_skills),
        "local_active_skills_indexed": len(local_skills) - len(historical_local),
        "local_historical_skills_indexed": len(historical_local),
        "pipeline_input_present": upstream_exists,
        "pipeline_final_present": final_exists,
        "pipeline_verify_polish": "not executed by this structural checker",
        "failures": failures,
        "warnings": warnings,
        "limits": "Checks structure only; does not prove reading, semantic quality, adoption, or settings installation.",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-ref", default=DEFAULT_REF)
    args = parser.parse_args()
    try:
        raise SystemExit(run(args.source_ref))
    except (ValueError, OSError, subprocess.SubprocessError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))
        raise SystemExit(2)
