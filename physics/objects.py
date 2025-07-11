import numpy as np
from typing import Sequence


class Object:
    def __init__(
        self,
        mass: float,
        position: np.ndarray | list,
        velocity: np.ndarray | list,
    ):
        self._validate_mass(mass)
        self._validate_vector(position, name="Position")
        self._validate_vector(velocity, name="Velocity")

        self.mass = mass
        self.position = np.asarray(position, dtype=float)
        self.velocity = np.asarray(velocity, dtype=float)

    def _validate_mass(self, m):
        if not isinstance(m, (int, float)):
            raise TypeError("Mass must be a number")
        if m <= 0:
            raise ValueError("Mass must be positive and non-zero")

    def _validate_vector(self, v, name=None):
        if name is None:
            name = "Vector"

        if not isinstance(v, (list, np.ndarray)):
            raise TypeError(f"{name} must be a list or numpy array")

        if len(v) != 2:
            raise ValueError(f"{name} must have exactly two elements")

        if not all(isinstance(coord, (int, float)) for coord in v):
            raise TypeError(f"{name} must contain only numbers")


class Circle(Object):
    def __init__(
        self,
        mass: float,
        position: np.ndarray | Sequence[float],
        velocity: np.ndarray | Sequence[float],
        radius: float,
    ):
        super().__init__(mass, position, velocity)

        self._validate_radius(radius)
        self.radius = radius

    def _validate_radius(self, r):
        if not isinstance(r, (int, float)):
            raise TypeError("Radius must be a number")
        if r < 0:  # Allow r=0 for point masses
            raise ValueError("Radius must be positive")
