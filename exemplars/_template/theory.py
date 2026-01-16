"""Template exemplar.

This file is executed by tools/build_exemplar.py.

Contract: define a `build(out_dir: str) -> dict` function.
It should write `report.tex` and `law_report.json` into out_dir.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any


def build(out_dir: str) -> dict[str, Any]:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    report_tex = out / "report.tex"
    report_tex.write_text(
        r"""
% Auto-generated exemplar report (template)
\subsubsection*{Instance Declaration}
Template.

\subsubsection*{Law Obligations}
\begin{tabular}{lll}
Obligation & Status & Notes \\
\hline
R0 & AXIOM & (template) \\
\end{tabular}
""".lstrip()
    )

    law_report = {
        "obligations": [
            {"id": "R0_CANON_IDEMPOTENT", "status": "AXIOM", "notes": "template"}
        ]
    }
    (out / "law_report.json").write_text(__import__("json").dumps(law_report, indent=2))
    return law_report
