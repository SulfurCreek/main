#!/usr/bin/env python3
"""Run a verifier with all scripts dependencies from one Git commit.

Usage: python career/scripts/run_pinned_verifier.py <40-hex-SHA> <verifier.py> [args...]
Only reads Git and creates a temporary tool package outside the repo.
Candidate inputs are resolved against the caller's original working directory.
"""
import hashlib
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import tempfile

ALLOWED = {'verify_polish.py', 'verify_letter.py', 'verify_line_profile.py',
           'verify_line_pdf.py', 'verify_104_bilingual.py'}


def run(argv):
    if len(argv) < 2 or not re.fullmatch(r'[0-9a-f]{40}', argv[0]) or argv[1] not in ALLOWED:
        print(__doc__, file=sys.stderr)
        return 2
    sha, tool, *args = argv
    if '--all' in args:
        print('--all requires a complete pinned checkout; supply explicit candidates here.', file=sys.stderr)
        return 2
    if tool == 'verify_104_bilingual.py' and not all(k in args for k in ('--zh', '--line')):
        print('Explicit --zh and --line paths are required.', file=sys.stderr)
        return 2
    cwd = Path.cwd()
    try:
        subprocess.run(['git', 'cat-file', '-e', sha + '^{commit}'], check=True)
        listing = subprocess.check_output(['git', 'ls-tree', '-rz', sha, 'career/scripts/'])
        with tempfile.TemporaryDirectory(prefix='career-tools-') as td:
            base = Path(td)
            count = 0
            for row in listing.split(b'\0'):
                if not row:
                    continue
                meta, raw_path = row.split(b'\t', 1)
                mode, kind, blob = meta.decode().split()
                name = raw_path.decode('utf-8')
                rel = PurePosixPath(name)
                if rel.is_absolute() or '..' in rel.parts or not name.startswith('career/scripts/'):
                    raise ValueError('Unsafe path')
                if mode not in ('100644', '100755') or kind != 'blob':
                    raise ValueError('Only regular tool files are allowed: ' + name)
                data = subprocess.check_output(['git', 'cat-file', 'blob', blob])
                got = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
                if got != blob:
                    raise ValueError('Git object mismatch: ' + name)
                target = base.joinpath(*rel.parts)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
                count += 1
            entry = base/'career/scripts'/tool
            if not entry.is_file():
                raise ValueError('Verifier absent at pinned commit')
            env = dict(os.environ)
            env.pop('PYTHONPATH', None)
            env['PYTHONNOUSERSITE'] = '1'
            print(f'Tool commit: {sha}; package files: {count}; cwd: {cwd}', flush=True)
            return subprocess.run([sys.executable, str(entry), *args], cwd=cwd, env=env).returncode
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f'Pinned verifier failed: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(run(sys.argv[1:]))
