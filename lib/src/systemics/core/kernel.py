from __future__ import annotations

from typing import Generic, Iterable, Protocol, TypeVar

from .trace import Trace

T = TypeVar("T")
U = TypeVar("U")
G = TypeVar("G")
V = TypeVar("V")
D = TypeVar("D")
R = TypeVar("R")
C = TypeVar("C")


class Kernel(Protocol, Generic[T, U, G, V, D, R, C]):
    """Relational kernel semantics.

    Deterministic kernels are a special case that return 0/1 traces.
    """

    def exec(self, t: T, u: U, gamma: G) -> Iterable[Trace[T, U, G, V, D, R, C]]:
        ...
