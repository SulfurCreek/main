#!/usr/bin/env python3
"""RETIRED 2026-11-03. Original source: career/archive/2026-11-03-fact-validation-retired/."""
RETIRED = True
def __getattr__(name):
    raise AttributeError("fact_lock is retired; automatic fact validation is disabled")
if __name__ == "__main__":
    raise SystemExit("RETIRED: no fact verification was executed (exit 1).")
