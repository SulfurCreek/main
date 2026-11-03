#!/usr/bin/env python3
"""Read-only supplement for the upstream polish verifier.

Checks source/final bullet indentation and parent relationships, raw locked
entities, numeric occurrences and all LOCKED blocks including non-bullet text.
Does not grade style, verify facts independently or change either input.
Both inputs must be inside career/ (remote snapshots may live in .scratch).
"""
import argparse
from collections import Counter
import json
from pathlib import Path
import re

CAREER = Path(__file__).resolve().parents[3]
TAGS = re.compile(
    r"<!--\s*\[STATUS:\s*(LOCKED|NEEDS_POLISH)\]"
    r"(?:\s*\[LOCK_ENTITIES:\s*([^\]]*)\])?\s*-->\n"
)
BULLETS = re.compile(r"^( *)[-*] +(.+)$", re.M)


def read(path):
    resolved = Path(path).resolve()
    if not resolved.is_relative_to(CAREER):
        raise ValueError("Input must stay inside career/")
    return resolved.read_text(encoding="utf-8")


def structure(text):
    result, stack = [], []
    for i, match in enumerate(BULLETS.finditer(text)):
        indent = len(match.group(1))
        while stack and indent <= stack[-1][0]:
            stack.pop()
        result.append((indent, stack[-1][1] if stack else None))
        stack.append((indent, i))
    return result


def numbers(text):
    return Counter(re.findall(r"\d+(?:[.,]\d+)?", text))


def check(draft, final):
    match = re.search(r"^## 草稿\s*\n(.*?)(?=^## 檢查|\Z)", draft, re.M | re.S)
    if not match:
        raise ValueError("Required source body section is missing")
    body = match.group(1).lstrip("\n")
    tags = list(TAGS.finditer(body))
    if not tags:
        raise ValueError("Required source status blocks are missing")
    clean = TAGS.sub("", body)
    errors = []
    if structure(clean) != structure(final):
        errors.append("Bullet count, indentation or parent relationship changed")
    if numbers(clean) != numbers(final):
        errors.append("Full-body numeric values or occurrences changed")
    if re.search(r"\[STATUS:|\[LOCK_ENTITIES:|NEEDS_POLISH", final):
        errors.append("Control markers remain in final")
    final_bullets = [m.group(2) for m in BULLETS.finditer(final)]
    bullet_index, locked = 0, 0
    for i, tag in enumerate(tags):
        end = tags[i + 1].start() if i + 1 < len(tags) else len(body)
        heading = re.search(r"^#{1,6} ", body[tag.end():end], re.M)
        if heading:
            end = tag.end() + heading.start()
        original = body[tag.end():end]
        if tag.group(1) == "LOCKED":
            locked += 1
            if final.count(original) != 1:
                errors.append(f"LOCKED block {i + 1} is missing, changed or duplicated")
        bullet = BULLETS.match(original)
        if not bullet:
            continue
        if bullet_index < len(final_bullets):
            actual = final_bullets[bullet_index]
            for entity in (x.strip() for x in (tag.group(2) or "").split(", ")):
                if entity and entity not in actual:
                    errors.append(f"Bullet {bullet_index + 1}: raw entity missing: {entity}")
            if numbers(bullet.group(2)) != numbers(actual):
                errors.append(f"Bullet {bullet_index + 1}: numeric values or occurrences changed")
        bullet_index += 1
    return {"errors": errors, "source_status_blocks": len(tags),
            "locked_blocks": locked, "source_bullets": bullet_index,
            "final_bullets": len(final_bullets),
            "nested_bullets": sum(indent > 0 for indent, _ in structure(final)),
            "limits": "Structural checks only; semantic and stylistic review still required."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("draft")
    parser.add_argument("final")
    args = parser.parse_args()
    try:
        result = check(read(args.draft), read(args.final))
    except (OSError, ValueError) as exc:
        result = {"errors": [str(exc)]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
