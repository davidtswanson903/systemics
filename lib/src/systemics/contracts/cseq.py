from __future__ import annotations

from typing import TypeVar

from ..core.contract import Contract
from ..core.trace import Trace
from ..kit.composition_kit import CompositionKit

T = TypeVar("T")
U = TypeVar("U")
G = TypeVar("G")
V = TypeVar("V")
D = TypeVar("D")
R = TypeVar("R")
C = TypeVar("C")


def cseq(
    C2: Contract[T, U, G, V, D, R, C],
    C1: Contract[T, U, G, V, D, R, C],
    kit: CompositionKit[T, U, G, V, D, R, C],
) -> Contract[T, U, G, V, D, R, C]:
    """Sequential contract composition induced by the same kit.

    This is a minimal (Milestone 0) version: a composed trace satisfies `cseq(C2,C1)`
    iff it can be exhibited as a kit-composition of compatible subtraces that satisfy
    `C1` and `C2` respectively.

    In general, this is easiest to use in settings where `compose_seq` is injective or
    traces carry explicit subtrace structure.
    """

    def _composed(tau: Trace[T, U, G, V, D, R, C]) -> bool:
        # By default we cannot decompose an arbitrary composed trace.
        # Users can either (a) use traces that are explicitly structured, or
        # (b) provide bespoke contract operators for their theory.
        _ = tau
        raise NotImplementedError(
            "cseq requires a decomposition strategy or structured traces; provide a theory-specific implementation."
        )

    return _composed
