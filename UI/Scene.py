from physics.objects import Object
from physics.constants import GRAVITY_VECTOR
import numpy as np
from physics.vector_utils import add, scale


class Scene:
    """
    Runs the simulation.
    Stores the objects in the simulation and updates them each step.
    """

    def __init__(
        self,
        h: int,
        w: int,
        objects: list[Object] = None,
    ):
        """
        h and w define the bounding box for the simulation.
        Objects will stop if they try to exceed these bounds
        """
        self.h = h
        self.w = w

        self.objects = []

        if objects is not None:
            for obj in objects:
                self.objects.append(obj)

        self.gravity = GRAVITY_VECTOR

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
