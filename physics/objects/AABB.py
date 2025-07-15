from physics.objects.Object import Object
import numpy as np


class AABB(Object):
    def __init__(
        self,
        mass: float,
        half_size: np.ndarray | list,
        position: np.ndarray | list,
        velocity: np.ndarray | list = None,
        forces: list[np.ndarray | list] = None,
    ):
        super().__init__(mass, position, velocity, forces)

        self._validate_half_size(half_size)

        self.half_size = half_size

    def _validate_half_size(self, half_size):
        if not isinstance(half_size, (list, np.ndarray)):
            raise TypeError(f"Half-size must be a list or numpy array")

        if len(half_size) != 2:
            raise ValueError(f"Half-size must have exactly two elements")

        if not all(isinstance(size, (int, float)) for size in half_size):
            raise TypeError(f"Half-size must contain only numbers")

        if not all(size >= 0 for size in half_size):
            raise ValueError(f"Half-sizes must be positive")
