from physics.objects import Object
from physics.constants import GRAVITY_VECTOR
import numpy as np


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

        self.objects = objects

        self.gravity = GRAVITY_VECTOR

    def add_object(self, obj: Object):
        self.objects.append(obj)

    """
    Moves the simulation forward by a specified dt

    Args:
        dt (float): the time step in seconds
    """

    def step(self, dt: float):
        # TODO: Implement this
        pass
