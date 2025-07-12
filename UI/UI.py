import pygame
from UI.Scene import Scene
from physics.objects import Object


class UI:
    def __init__(self, window: pygame.Surface, scene: Scene):
        self.window = window
        self.scene = scene

    def render(self):
        objects = self.scene.get_objects()

        if objects is not None:
            for obj in objects:
                self._renderShape(obj)

    def _renderShape(self, shape: Object):
        # TODO: Write func to render a shape on screen

        # TEMP FOR RENDERING A SINGLE CIRCLE. CHANGE FOR ACTUAL SHAPES
        pygame.draw.circle(self.window, (0, 255, 0), shape.position, shape.radius)
        pass
