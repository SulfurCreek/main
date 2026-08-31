#!/usr/bin/env python3
"""
hackmd_safe_patch.py — 安全回寫 HackMD note（防覆蓋 / anti-clobber）。

實作 wiki/hackmd_rules.md「規則 D — 安全回寫契約」：回寫前先重新抓一次遠端內容，
和落地時的 baseline 比對；唯有「遠端未在編輯期間被別人（如小聶）改動」時才 PATCH，
否則中止並印出 diff 摘要，交由人判斷如何合併——絕不盲蓋。

改寫自 hackmd-skills/shared/scripts/safe-sync.sh，改用本 repo 慣例：
  * 直接打 REST API（api.hackmd.io/v1），不依賴 hackmd-cli
  * 認證用環境變數 HACKMD_TOKEN（見 CLAUDE.md 速查 / wiki/hackmd_rules.md）

用法：
    python3 scripts/hackmd_safe_patch.py \
        --note-id <noteId> \
        --baseline <落地當下存的 .md> \
        --working  <本地改完待回寫的 .md> \
        [--team-path 1111-jobdocs]

流程：
    1. GET 目前遠端 content → recheck
    2. diff(baseline, recheck)
         有差異 → 遠端在你編輯期間被改過 → exit 1（印 diff 摘要，不 PATCH）
         無差異 → PATCH working 內容
Exit code：0 已更新 / 1 衝突（遠端已變）/ 2 參數或 API 錯誤。
"""

from __future__ import annotations

import argparse
import difflib
import os
import sys
import urllib.error
import urllib.request

BASE = "https://api.hackmd.io/v1"


def _fail(msg: str, code: int = 2) -> "NoReturn":  # type: ignore[name-defined]
    print(msg, file=sys.stderr)
    sys.exit(code)


def _token() -> str:
    tok = os.environ.get("HACKMD_TOKEN")
    if not tok:
        _fail("ERROR: 環境變數 HACKMD_TOKEN 未設定（見 wiki/hackmd_rules.md）")
    return tok


def _note_path(note_id: str, team_path: str | None) -> str:
    if team_path:
        return f"/teams/{team_path}/notes/{note_id}"
    return f"/notes/{note_id}"


def _get_content(note_id: str, team_path: str | None, token: str) -> str:
    req = urllib.request.Request(
        BASE + _note_path(note_id, team_path),
        headers={"Authorization": f"Bearer {token}"},
    )
    try:
        with urllib.request.urlopen(req) as resp:
            import json

            return json.load(resp).get("content", "")
    except urllib.error.HTTPError as e:
        _fail(f"ERROR: GET {note_id} 失敗：HTTP {e.code} {e.reason}")
    except urllib.error.URLError as e:
        _fail(f"ERROR: GET {note_id} 連線失敗：{e.reason}")


def _patch_content(note_id: str, team_path: str | None, token: str, content: str) -> None:
    import json

    body = json.dumps({"content": content}).encode("utf-8")
    req = urllib.request.Request(
        BASE + _note_path(note_id, team_path),
        data=body,
        method="PATCH",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req) as resp:
            # PATCH 成功回 202 Accepted（body 為字面 "Accepted"）
            if resp.status not in (200, 202):
                _fail(f"ERROR: PATCH 非預期狀態碼 {resp.status}")
    except urllib.error.HTTPError as e:
        _fail(f"ERROR: PATCH {note_id} 失敗：HTTP {e.code} {e.reason}")
    except urllib.error.URLError as e:
        _fail(f"ERROR: PATCH {note_id} 連線失敗：{e.reason}")


def main() -> int:
    ap = argparse.ArgumentParser(description="安全回寫 HackMD note（防覆蓋）")
    ap.add_argument("--note-id", required=True, help="內部 note id（長 id，非 short slug）")
    ap.add_argument("--baseline", required=True, help="落地當下存的基準檔（.md）")
    ap.add_argument("--working", required=True, help="本地改完待回寫的檔（.md）")
    ap.add_argument("--team-path", default=None, help="團隊 path，如 1111-jobdocs（個人 note 免填）")
    args = ap.parse_args()

    for f in (args.baseline, args.working):
        if not os.path.isfile(f):
            _fail(f"ERROR: 找不到檔案：{f}")

    token = _token()

    with open(args.baseline, encoding="utf-8") as f:
        baseline = f.read()
    with open(args.working, encoding="utf-8") as f:
        working = f.read()

    recheck = _get_content(args.note_id, args.team_path, token)

    if recheck != baseline:
        print(
            "CONFLICT: 遠端 note 自 baseline 落地後已被改動，中止回寫（未 PATCH）。",
            file=sys.stderr,
        )
        diff = difflib.unified_diff(
            baseline.splitlines(),
            recheck.splitlines(),
            fromfile="baseline",
            tofile="remote(recheck)",
            lineterm="",
        )
        for i, line in enumerate(diff):
            if i >= 100:
                print("… (diff 過長，已截斷前 100 行)", file=sys.stderr)
                break
            print(line, file=sys.stderr)
        print(
            "\n請重新 fetch 最新遠端內容、把本地修改重套上去後再跑一次；勿盲蓋。",
            file=sys.stderr,
        )
        return 1

    _patch_content(args.note_id, args.team_path, token, working)
    print(f"OK: 已更新 {args.note_id}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
