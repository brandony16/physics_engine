class Object:
    def __init__(self, mass: float, position: tuple, velocity: float):
        self.mass = mass
        self.position = position
        self.velocity = velocity


class Circle(Object):
    def __init__(self, radius: int):
        super.__init__()
        self.radius = radius
