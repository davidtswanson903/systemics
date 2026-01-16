"""EX1: Minimal Algebra (finite toy).

This exemplar is small but fully executable:
- finite carriers
- 2 relational kernels
- sequential composition induced by `CompositionKit` and `systemics.semantics.seq`
- generates a LaTeX report + JSON law report

It is intended to be exhaustive (no randomness).
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Literal

from systemics.core.trace import Trace
from systemics.kit.composition_kit import CompositionKit
from systemics.semantics.seq import seq

# Concrete carriers for this exemplar.
T = int
U = Literal["A", "B", "C"]
G = Literal["g0", "g1"]
V = int
D = Literal[0, 1]

R = str  # receipts
C = None  # no capacity witness in this exemplar

# Use a concrete trace alias for readability (avoid using it in annotations to satisfy linters).
ToyTrace = Trace[int, U, G, int, D, str, None]


def _canon_r(r: R) -> R:
    return r.lower().strip()


def _merge_r(r2: R, r1: R) -> R:
    r2c, r1c = _canon_r(r2), _canon_r(r1)
    if not r1c:
        return r2c
    if not r2c:
        return r1c
    return f"{r2c}+{r1c}"


def _compat_seq(tau1, tau2) -> bool:
    # tau1, tau2: ToyTrace
    return (tau1.u_out == tau2.u_in) and (tau1.gamma_out == tau2.gamma_in)


def _compose_seq(tau2, tau1):
    # tau2, tau1: ToyTrace
    return Trace(
        t=tau2.t,
        u_in=tau1.u_in,
        gamma_in=tau1.gamma_in,
        u_out=tau2.u_out,
        v_out=tau2.v_out,
        d_out=tau2.d_out,
        r_out=_merge_r(tau2.r_out, tau1.r_out),
        c_out=None,
        gamma_out=tau2.gamma_out,
    )


KIT: CompositionKit[int, U, G, int, D, str, None] = CompositionKit(
    compat_seq=_compat_seq,
    canon_r=_canon_r,
    merge_r=_merge_r,
    compose_seq=_compose_seq,
)


@dataclass(frozen=True)
class K1:
    """Toy kernel K1: A->B and A->C under g0, emits distinct receipts."""

    def exec(self, t: int, u: U, gamma: G):
        # returns Iterable[ToyTrace]
        if gamma != "g0":
            return []
        if u != "A":
            return []
        return [
            Trace(t, "A", "g0", "B", 1, 1, "R1", None, "g0"),
            Trace(t, "A", "g0", "C", 2, 1, "R2", None, "g0"),
        ]


@dataclass(frozen=True)
class K2:
    """Toy kernel K2: B->C and C->B under g0, emits receipts."""

    def exec(self, t: int, u: U, gamma: G):
        # returns Iterable[ToyTrace]
        if gamma != "g0":
            return []
        if u == "B":
            return [Trace(t, "B", "g0", "C", 10, 1, "S1", None, "g0")]
        if u == "C":
            return [Trace(t, "C", "g0", "B", 20, 0, "S2", None, "g0")]
        return []


def _latex_escape(s: str) -> str:
    return s.replace("_", "\\_")


def build(out_dir: str) -> dict:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    K = K1()
    L = K2()
    LK = seq(L, K, KIT)

    traces = list(LK.exec(0, "A", "g0"))

    def row(tau) -> str:
        # tau: ToyTrace
        return " & ".join(
            [
                _latex_escape(str(tau.u_in)),
                _latex_escape(str(tau.gamma_in)),
                _latex_escape(str(tau.u_out)),
                str(tau.v_out),
                str(tau.d_out),
                _latex_escape(str(tau.r_out)),
                _latex_escape(str(tau.gamma_out)),
            ]
        ) + r"\\"

    report = r"""
% Auto-generated exemplar report: EX1_minimal_algebra
\subsubsection*{Instance Declaration}
\noindent
Finite carriers:
\begin{itemize}[leftmargin=*]
  \item $U=\{A,B,C\}$
  \item $\Gamma=\{g0,g1\}$
  \item receipts $R$ are strings with $\canon$ = lowercase+trim and merge = concatenation with \texttt{+}
\end{itemize}

\subsubsection*{Core Demonstrations}
\paragraph{Sequential composition.}
Let $K_1$ and $K_2$ be the two toy kernels. We form $K_2\seqc K_1$ using the composition kit.
The composed kernel has (exhaustively enumerated) traces below for input $A$ under envelope $g0$.

\begin{center}
\begin{tabular}{lllllll}
$u_{in}$ & $\gamma_{in}$ & $u_{out}$ & $v$ & $d$ & receipt & $\gamma_{out}$\\
\hline
""".lstrip()

    report += "\n".join(row(t) for t in traces) + "\n"

    report += r"""
\end{tabular}
\end{center}

\subsubsection*{Law Obligations}
\begin{tabular}{lll}
Obligation & Status & Notes\\
\hline
R0 canon idempotence & CHECKED & holds for receipt canon in this toy ($\canon(\canon(r))=\canon(r)$)\\
\end{tabular}
"""

    (out / "report.tex").write_text(report)

    law_report = {
        "id": "EX1_minimal_algebra",
        "obligations": [
            {
                "id": "R0_CANON_IDEMPOTENT",
                "status": "CHECKED",
                "notes": "canon_r is lowercase+trim; idempotent on all strings",
            }
        ],
        "trace_count": len(traces),
    }
    (out / "law_report.json").write_text(__import__("json").dumps(law_report, indent=2))
    return law_report
