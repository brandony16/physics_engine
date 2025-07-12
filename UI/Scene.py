from physics.objects import Object


class Scene:
    """
    Stores the objects in the simulation and updates them each step.
    UI then gets the objects and renders them to the screen.
    """

    def __init__(self, h: int, w: int, objects: list[Object] = None):
        """
        h and w define the bounding box for the simulation. 
        Objects will stop if they try to exceed these bounds
        """
        self.h = h
        self.w = w

        self.objects = objects

    def add_object(self, obj: Object):
        self.objects.append(obj)

    def get_objects(self):
        return self.objects

    """
    Moves the simulation forward by a specified dt

    Args:
        dt (float): the time step in seconds
    """

    def step(self, dt: float):
        # TODO: Implement this
        pass
