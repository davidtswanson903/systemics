from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Iterable, TypeVar

from ..core.kernel import Kernel
from ..core.trace import Trace
from ..kit.composition_kit import CompositionKit

T = TypeVar("T")
U = TypeVar("U")
G = TypeVar("G")
V = TypeVar("V")
D = TypeVar("D")
R = TypeVar("R")
C = TypeVar("C")


@dataclass(frozen=True)
class SeqKernel(Generic[T, U, G, V, D, R, C]):
    K2: Kernel[T, U, G, V, D, R, C]
    K1: Kernel[T, U, G, V, D, R, C]
    kit: CompositionKit[T, U, G, V, D, R, C]

    def exec(self, t: T, u: U, gamma: G) -> Iterable[Trace[T, U, G, V, D, R, C]]:
        for tau1 in self.K1.exec(t, u, gamma):
            for tau2 in self.K2.exec(t, tau1.u_out, tau1.gamma_out):
                if self.kit.compat_seq(tau1, tau2):
                    yield self.kit.compose_seq(tau2, tau1)


def seq(
    K2: Kernel[T, U, G, V, D, R, C],
    K1: Kernel[T, U, G, V, D, R, C],
    kit: CompositionKit[T, U, G, V, D, R, C],
) -> Kernel[T, U, G, V, D, R, C]:
    """Sequential kernel composition induced by a `CompositionKit`."""

    return SeqKernel(K2=K2, K1=K1, kit=kit)
