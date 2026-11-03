"""Offline package-version test using an isolated synthetic Git repository."""
import contextlib
import io
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import run_pinned_verifier as runner


class PinnedTests(unittest.TestCase):
    def test_invalid_sha_and_tool_rejected(self):
        for args in ([], ['short', 'verify_polish.py'], ['a'*40, 'fact_lock.py']):
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(runner.run(args), 2)

    def test_batch_and_missing_source_options_rejected(self):
        for args in (['a'*40, 'verify_letter.py', '--all'],
                     ['a'*40, 'verify_104_bilingual.py', 'out.md']):
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(runner.run(args), 2)

    def test_dependencies_from_same_commit_and_original_cwd(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            scripts = root/'career/scripts'
            scripts.mkdir(parents=True)
            (scripts/'helper.py').write_text('VALUE = 7\n')
            (scripts/'verify_polish.py').write_text(
                'import helper, pathlib, sys\n'
                'sys.exit(0 if helper.VALUE == 7 and pathlib.Path("candidate.md").is_file() else 1)\n')
            subprocess.run(['git', 'init', '-q', td], check=True)
            subprocess.run(['git', '-C', td, 'add', '.'], check=True)
            subprocess.run(['git', '-C', td, '-c', 'user.name=Test', '-c', 'user.email=test@example.invalid',
                            'commit', '-qm', 'synthetic tools'], check=True)
            sha = subprocess.check_output(['git', '-C', td, 'rev-parse', 'HEAD'], text=True).strip()
            (scripts/'helper.py').write_text('VALUE = 999\n')
            (root/'candidate.md').write_text('synthetic candidate')
            before = Path.cwd()
            try:
                os.chdir(root)
                with contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(runner.run([sha, 'verify_polish.py']), 0)
                self.assertEqual((scripts/'helper.py').read_text(), 'VALUE = 999\n')
            finally:
                os.chdir(before)
