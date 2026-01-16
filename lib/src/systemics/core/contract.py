from __future__ import annotations

from typing import Callable, TypeVar

from .trace import Trace

T = TypeVar("T")
U = TypeVar("U")
G = TypeVar("G")
V = TypeVar("V")
D = TypeVar("D")
R = TypeVar("R")
C = TypeVar("C")

Contract = Callable[[Trace[T, U, G, V, D, R, C]], bool]
