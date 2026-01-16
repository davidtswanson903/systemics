from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")
U = TypeVar("U")
G = TypeVar("G")
V = TypeVar("V")
D = TypeVar("D")
R = TypeVar("R")
C = TypeVar("C")


@dataclass(frozen=True)
class Trace(Generic[T, U, G, V, D, R, C]):
    """First-class witness object for Systemics.

    The library treats kernel semantics relationally: a kernel defines a set of traces.
    """

    t: T
    u_in: U
    gamma_in: G

    u_out: U
    v_out: V
    d_out: D

    r_out: R
    c_out: Optional[C]

    gamma_out: G
