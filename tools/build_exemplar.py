#!/usr/bin/env python3
"""Build a single exemplar.

Usage:
  python tools/build_exemplar.py exemplars/EX1_minimal_algebra

Contract:
- exemplar_dir/theory.py must define `build(out_dir: str) -> dict`.
- outputs are written to exemplar_dir/build/.

This script adds `lib/src` to sys.path so exemplars can import `systemics` without
requiring installation.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path


def _load_module(module_path: Path):
    spec = importlib.util.spec_from_file_location("exemplar_theory", module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load module at {module_path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python tools/build_exemplar.py <exemplar_dir>", file=sys.stderr)
        return 2

    repo_root = Path(__file__).resolve().parents[1]
    exemplar_dir = (repo_root / sys.argv[1]).resolve()
    if not exemplar_dir.exists():
        print(f"Exemplar folder not found: {exemplar_dir}", file=sys.stderr)
        return 2

    # Make `import systemics` work from lib/src without installation.
    sys.path.insert(0, str(repo_root / "lib" / "src"))

    theory_path = exemplar_dir / "theory.py"
    if not theory_path.exists():
        print(f"Missing theory.py: {theory_path}", file=sys.stderr)
        return 2

    out_dir = exemplar_dir / "build"
    out_dir.mkdir(parents=True, exist_ok=True)

    mod = _load_module(theory_path)
    if not hasattr(mod, "build"):
        print("theory.py must define build(out_dir: str) -> dict", file=sys.stderr)
        return 2

    result = mod.build(str(out_dir))

    # Ensure a JSON artifact exists even if exemplar forgot.
    lr_path = out_dir / "law_report.json"
    if not lr_path.exists():
        lr_path.write_text(json.dumps(result, indent=2))

    print(f"Built exemplar: {exemplar_dir.name} -> {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
