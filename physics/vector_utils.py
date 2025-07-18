import numpy as np
from typing import Sequence

# Basic bector ops. Provides flexibility for future changes,
# making all logic centralized if it is changed(to a vector class or something)


def to_vec(v: np.ndarray | Sequence[float]) -> np.ndarray:
    return np.asarray(v, dtype=float)


def add(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a + b


def subtract(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a - b


def scale(v: np.ndarray, scalar: float) -> np.ndarray:
    return v * scalar


def dot(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b))


def norm(v: np.ndarray) -> float:
    return float(np.linalg.norm(v))
