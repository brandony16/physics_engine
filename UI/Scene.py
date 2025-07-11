import pygame
from physics.objects import Object


class Scene:
    def __init__(self, h: int, w: int, objects: list[Object] = None):
        self.h = h
        self.w = w

        self.objects = objects

        # Add objects to scene if any are given
        if objects is not None:
            for obj in objects :
                self.add_object(obj)

    def add_object(obj: Object):
        # TODO: Implement this
        pass
