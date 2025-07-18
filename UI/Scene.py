from physics.objects.Object import Object
from physics.constants import GRAVITY_VECTOR
import numpy as np
from physics.vector_utils import scale
from physics.objects.Circle import Circle
from physics.objects.Wall import Wall
from physics.collisions.shape_collisions import circle_circle_collision
from physics.utils import get_normal
import copy


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

        self.objects = []

        if objects is not None:
            for obj in objects:
                self.objects.append(obj)

        self.saved_objects = copy.deepcopy(self.objects)

        self.gravity = GRAVITY_VECTOR

        # How elastic collisions are. 1.0 for fully elastic, 0 for inelastic
        self.restitution = 0.1

        # # Create walls around sim
        # left_wall = Wall([-1, h / 2], [1, h / 2])
        # right_wall = Wall([w + 1, h / 2], [1, h / 2])
        # top_wall = Wall([w / 2, -1], [w / 2, 1])
        # bottom_wall = Wall([w / 2, h + 1], [w / 2, 1])

        # self.objects.append(left_wall)
        # self.objects.append(right_wall)
        # self.objects.append(top_wall)
        # self.objects.append(bottom_wall)

    def add_object(self, obj: Object):
        self.objects.append(obj)
        self.save_objects()

    def save_objects(self):
        self.saved_objects = copy.deepcopy(self.objects)

    def load_objects(self):
        self.objects = copy.deepcopy(self.saved_objects)

    def reset(self):
        self.objects = []
        self.saved_objects = []

    """
    Moves the simulation forward by a specified dt

    Args:
        dt (float): the time step in seconds
    """

    def step(self, dt: float):
        # If no objects, do nothing
        if len(self.objects) == 0:
            return

        collided = set()

        for i, obj in enumerate(self.objects):
            # Update position
            obj.position += scale(obj.velocity, dt)

            for j in range(i + 1, len(self.objects)):
                obj2 = self.objects[j]
                if circle_circle_collision(obj, obj2):
                    collided.add(obj)
                    collided.add(obj2)
                    self.handle_collision(obj, obj2)

            # Clip position so objects dont leave the scene
            # TEMP SOLUTION, add actual collision logic
            obj.position = np.clip(obj.position, [0, 0], [self.w, self.h])

            # Update velocity
            # F/m = a, a*dt = dv
            if obj not in collided:
                force_v = np.sum(obj.forces, axis=0)
                acceleration = scale(force_v, 1 / obj.mass)
                obj.velocity += scale(acceleration, dt)

            # Update forces
            obj.forces = []
            # obj.forces.append(self.gravity)

    def handle_collision(self, obj1: Object, obj2: Object):
        percent = 0.8
        slop = 0.01  # Allows for small overlap so floating point error doesnt cause jitters

        dist = np.linalg.norm(obj1.position - obj2.position)
        penetration = (obj1.radius + obj2.radius) - dist

        # Only update velos and positions if penetration is significant
        if penetration > slop:
            norm = get_normal(obj1, obj2)
            tangent = np.array([-norm[1], norm[0]])

            # Get velocities in normal and tangent directions
            v1, v2 = obj1.velocity, obj2.velocity
            v1n = np.dot(v1, norm)
            v1t = np.dot(v1, tangent)
            v2n = np.dot(v2, norm)
            v2t = np.dot(v2, tangent)

            # Calculate final v's in the direction of the norm
            m1, m2, e = obj1.mass, obj2.mass, self.restitution
            total_m = m1 + m2
            vf1n = ((m1 - e * m2) * v1n / total_m) + (((1 + e) * m2) * v2n / total_m)
            vf2n = (((1 + e) * m1) * v1n / total_m) + ((m2 - e * m1) * v2n / total_m)

            # Tangent stays the same
            vf1t = v1t
            vf2t = v2t

            # Reconstruct complete velocities
            vf1 = vf1n * norm + vf1t * tangent
            vf2 = vf2n * norm + vf2t * tangent

            obj1.velocity = vf1
            obj2.velocity = vf2

            # Positional correction so objects are no longer clipping
            # Calculate inverse masses
            inv_m1 = 0.0 if obj1.mass == float("inf") else 1.0 / obj1.mass
            inv_m2 = 0.0 if obj2.mass == float("inf") else 1.0 / obj2.mass
            inv_mass_sum = inv_m1 + inv_m2

            # Move each object by its inverse mass. More mass means it will move less
            correction = ((penetration - slop) / inv_mass_sum) * percent
            obj1.position -= norm * (correction * inv_m1)
            obj2.position += norm * (correction * inv_m2)
