import numpy as np
from physics.objects.Object import Object


class Circle(Object):
    """
    A circle object
    """

    def __init__(
        self,
        mass: float,
        radius: float,
        position: np.ndarray | list,
        velocity: np.ndarray | list = None,
        forces: list[np.ndarray] | None = None,
    ):
        """
        Position is [x, y], Velocity is [vx, vy], and forces are [fx, fy]
        """
        super().__init__(mass, position, velocity, forces)

        self._validate_radius(radius)
        self.radius = radius

    def _validate_radius(self, r):
        if not isinstance(r, (int, float)):
            raise TypeError("Radius must be a number")
        if r < 0:  # Allow r=0 for point masses
            raise ValueError("Radius must be positive")
