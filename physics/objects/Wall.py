from physics.objects.AABB import AABB
import numpy as np
from physics.constants import INFINITE_MASS

"""
An immovable wall class with infinte mass
"""
class Wall(AABB):
    def __init__(self, position: np.ndarray | list, half_size: np.ndarray | list):
        super().__init__(INFINITE_MASS, half_size, position)
