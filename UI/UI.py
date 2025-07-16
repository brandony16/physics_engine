import pygame
from UI.Scene import Scene
from physics.objects.Object import Object
from physics.objects.Circle import Circle

METRIC_TO_PIXEL_RATIO = 100


class UI:
    def __init__(self, window: pygame.Surface, scene: Scene):
        self.window = window
        self.scene = scene

    def render(self):
        objects = self.scene.objects

        if objects is not None:
            for obj in objects:
                self._renderShape(obj)

    def _renderShape(self, shape: Object):
        # TODO: Write func to render a shape on screen

        # TEMP FOR RENDERING A SINGLE CIRCLE. CHANGE FOR ACTUAL SHAPES

        # Flip y-axis so y=0 is on the bottom
        pos = shape.position.copy() * METRIC_TO_PIXEL_RATIO
        pos[1] = self.window.get_height() - pos[1]

        if isinstance(shape, Circle):
            pygame.draw.circle(
                self.window,
                (0, 255, 0),
                pos,
                shape.radius * METRIC_TO_PIXEL_RATIO,
            )
        pass
