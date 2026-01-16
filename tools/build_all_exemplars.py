#!/usr/bin/env python3
"""Build all exemplars under exemplars/.

Usage:
  python tools/build_all_exemplars.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    exemplars_root = repo_root / "exemplars"

    if not exemplars_root.exists():
        print("No exemplars/ folder.", file=sys.stderr)
        return 2

    for ex_dir in sorted(exemplars_root.iterdir()):
        if not ex_dir.is_dir():
            continue
        if ex_dir.name.startswith("_"):
            continue

        subprocess.check_call([sys.executable, str(repo_root / "tools" / "build_exemplar.py"), str(ex_dir)])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
