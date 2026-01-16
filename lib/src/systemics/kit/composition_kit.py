from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Generic, Optional, TypeVar

from ..core.trace import Trace

T = TypeVar("T")
U = TypeVar("U")
G = TypeVar("G")
V = TypeVar("V")
D = TypeVar("D")
R = TypeVar("R")
C = TypeVar("C")
O = TypeVar("O")


@dataclass(frozen=True)
class CompositionKit(Generic[T, U, G, V, D, R, C]):
    """Constructor kit aligning process, contract, capacity, and evidence composition.

    In the book, this is the composition alignment principle made concrete.
    """

    # compatibility predicates
    compat_seq: Callable[[Trace[T, U, G, V, D, R, C], Trace[T, U, G, V, D, R, C]], bool]
    compat_par: Optional[
        Callable[[Trace[T, U, G, V, D, R, C], Trace[T, U, G, V, D, R, C]], bool]
    ] = None

    # receipt canonicalization/merge
    canon_r: Callable[[R], R] = lambda r: r
    merge_r: Callable[[R, R], R] = lambda r2, r1: r2

    # capacity merge (optional)
    merge_c: Optional[Callable[[C, C], C]] = None

    # trace constructors
    compose_seq: Callable[[Trace[T, U, G, V, D, R, C], Trace[T, U, G, V, D, R, C]], Trace[T, U, G, V, D, R, C]] = (
        lambda t2, t1: t2
    )
    compose_par: Optional[
        Callable[[Trace[T, U, G, V, D, R, C], Trace[T, U, G, V, D, R, C]], Trace[T, U, G, V, D, R, C]]
    ] = None
