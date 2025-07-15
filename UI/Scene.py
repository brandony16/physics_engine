from physics.objects.Object import Object
from physics.constants import GRAVITY_VECTOR
import numpy as np
from physics.vector_utils import add, scale
from physics.objects.Circle import Circle
from physics.objects.Wall import Wall


class Scene:
    """
    Runs the simulation.
    Stores the objects in the simulation and updates them each step.
    """

    def __init__(
        self,
        w: int,
        h: int,
        objects: list[Object] = None,
    ):
        """
        h and w define the bounding box for the simulation.
        Objects will stop if they try to exceed these bounds
        """
        self.w = w
        self.h = h

        circle = Circle(1, 50, [w / 2, h / 2], [0, 0])  # Temp circle

        self.objects = [circle]

        if objects is not None:
            for obj in objects:
                self.objects.append(obj)

        self.gravity = GRAVITY_VECTOR

        # Create walls around sim
        left_wall = Wall([-1, h / 2], [1, h / 2])
        right_wall = Wall([w + 1, h / 2], [1, h / 2])
        top_wall = Wall([w / 2, -1], [w / 2, 1])
        bottom_wall = Wall([w / 2, h + 1], [w / 2, 1])

        self.objects.append(left_wall)
        self.objects.append(right_wall)
        self.objects.append(top_wall)
        self.objects.append(bottom_wall)

    def add_object(self, obj: Object):
        self.objects.append(obj)

    """
    Moves the simulation forward by a specified dt

    Args:
        dt (float): the time step in seconds
    """

    def step(self, dt: float):
        # If no objects, do nothing
        if len(self.objects) == 0:
            return

        for obj in self.objects:
            # Update position
            obj.position += scale(obj.velocity, dt)

            # Clip position so objects dont leave the scene
            obj.position = np.clip(obj.position, [0, 0], [self.w, self.h])

            # Update velocity
            # F/m = a, a*dt = dv
            force_v = np.sum(obj.forces, axis=0)
            acceleration = scale(force_v, 1 / obj.mass)
            obj.velocity += scale(acceleration, dt)

            # Update forces
            obj.forces = []
            obj.forces.append(self.gravity)
