import numpy as np
from typing import Sequence


class Object:
    def __init__(
        self,
        mass: float,
        position: np.ndarray | Sequence[float],
        velocity: np.ndarray | Sequence[float],
    ):
        if mass <= 0:
            raise ValueError("Mass must be a positive, non-zero number")
        if len(position) != 2:
            raise ValueError("Position must be a 2D vector")
        if len(velocity) != 2:
            raise ValueError("Velocity must be a 2D vector")

        self.mass = mass
        self.position = np.asarray(position, dtype=float)
        self.velocity = np.asarray(velocity, dtype=float)


class Circle(Object):
    def __init__(
        self,
        mass: float,
        position: np.ndarray | Sequence[float],
        velocity: np.ndarray | Sequence[float],
        radius: float,
    ):
        super().__init__(mass, position, velocity)
        self.radius = radius
