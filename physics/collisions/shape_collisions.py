from physics.objects.Circle import Circle
from physics.utils import getDistance


def circle_circle_collision(c1: Circle, c2: Circle) -> bool:
    """
    Determines if two circles are colliding.
    """
    if not isinstance(c1, Circle) or not isinstance(c2, Circle):
        raise TypeError("Both inputs must be circles")

    distance = getDistance(c1, c2)

    # Due to radial symmetry, if the centers of the circles are closer than 
    # the sum of the two radii, they are colliding
    return distance < (c1.radius + c2.radius)
