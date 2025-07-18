from physics.objects.Object import Object
import numpy as np
import physics.vector_utils as v


def get_distance(obj1: Object, obj2: Object) -> float:
    """
    Gets the Euclidean distance between two objects positions.
    """
    pos1 = obj1.position
    pos2 = obj2.position

    # dist = sqrt(dx^2 + dy^2)
    distance = np.sqrt(np.sum((pos1 - pos2) ** 2))

    return distance


def get_normal(obj1: Object, obj2: Object) -> np.ndarray:
    """
    Gets the unit normal vector between two objects using the formula:

    n = (pos2 - pos1) / ||pos2 - pos1||
    """
    pos_diff = v.subtract(obj2.position, obj1.position)

    return pos_diff / np.linalg.norm(pos_diff)
