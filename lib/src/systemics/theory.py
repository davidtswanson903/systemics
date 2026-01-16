from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

from .kit.composition_kit import CompositionKit

T = TypeVar("T")  # execution index / time / run id
U = TypeVar("U")  # artifact
G = TypeVar("G")  # envelope / regime
V = TypeVar("V")  # valuation
D = TypeVar("D")  # decision
R = TypeVar("R")  # receipt
C = TypeVar("C")  # capacity witness


@dataclass(frozen=True)
class SystemicsTheory(Generic[T, U, G, V, D, R, C]):
    """A Systemics theory instance packaged as a single record.

    This is the library's central object: the universe carriers are implicit in the
    parametric types, and all composition/equivalence/rewrite operators are induced
    from the provided `CompositionKit` plus optional enrichments.
    """

    kit: CompositionKit[T, U, G, V, D, R, C]

    # Optional enrichments (kept intentionally untyped in milestone 0).
    stability: Optional[object] = None
    capacity: Optional[object] = None
    evidence: Optional[object] = None
