from physics.objects.Object import Object
import numpy as np


def get_distance(obj1: Object, obj2: Object) -> float:
    """
    Gets the Euclidean distance between two objects positions.
    """
    pos1 = obj1.position
    pos2 = obj2.position

    # dist = sqrt(dx^2 + dy^2)
    distance = np.sqrt(np.sum((pos1 - pos2) ** 2))

    return distance
