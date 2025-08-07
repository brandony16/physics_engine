import pygame
import pygame_gui as gui
from UI.Scene import Scene
from physics.objects.Object import Object
from physics.objects.Circle import Circle
from UI.Buttons import get_panel, get_button

METRIC_TO_PIXEL_RATIO = 50


class UI:
    def __init__(self, window: pygame.Surface, scene: Scene):
        self.window = window
        self.scene = scene

        self.manager = gui.UIManager(window.get_size(), "./UI/theme.json")

        # UI Constants
        self.padding = 20
        self.bg_color = (50, 50, 50)
        self.scene_bg = (200, 225, 255)
        self.border_color = (255, 200, 0)

        self.sidebar_width = 250
        self.sidebar_bg = (0, 0, 40)
        self.sidebar_padding = 10

        self.button_height = 50
        self.button_gap = 10

        # Create scene and sidebar rects
        w, h = self.window.get_size()
        self.scene_rect = pygame.Rect(
            self.padding,
            self.padding,
            w - self.sidebar_width - 2 * self.padding,
            h - 2 * self.padding,
        )
        self.sidebar_rect = pygame.Rect(
            w - self.sidebar_width - self.padding // 2,
            self.padding,
            self.sidebar_width - self.padding,
            h - 2 * self.padding,
        )

        # Create GUI buttons
        self.panel = get_panel(self.manager, self.sidebar_rect, id="#sidebar")
        self.start_button = get_button(
            manager=self.manager,
            rect=self._button_rect(),
            container=self.panel,
            text="Start Simulation",
        )
        self.pause_button = get_button(
            manager=self.manager,
            rect=self._button_rect(),
            container=self.panel,
            text="Pause Simulation",
        )
        self.clear_button = get_button(
            manager=self.manager,
            rect=self._button_rect(),
            container=self.panel,
            text="Clear Scene",
        )
        self.reset_button = get_button(
            manager=self.manager,
            rect=self._button_rect(),
            container=self.panel,
            text="Reset Simulation",
        )

        # Just doing circles for now, implement other shapes
        self.add_circle = get_button(
            manager=self.manager,
            rect=self._button_rect(),
            container=self.panel,
            text="Add Circle",
        )

        # Correct scene width and height
        self.scene.w = self.scene_rect.width / METRIC_TO_PIXEL_RATIO
        self.scene.h = self.scene_rect.height / METRIC_TO_PIXEL_RATIO

        # TEMP CIRCLES
        circle = Circle(1, 0.5, [1, 3], [5, 0])
        circle2 = Circle(1, 0.5, [self.scene.w - 1, 3], [-5, 0])
        self.scene.add_object(circle)
        self.scene.add_object(circle2)

    def render(self):
        self.window.fill(self.bg_color)

        # Draw scene and border
        pygame.draw.rect(self.window, self.scene_bg, self.scene_rect)
        pygame.draw.rect(self.window, self.border_color, self.scene_rect, width=2)

        objects = self.scene.objects

        if objects is not None:
            for obj in objects:
                self._renderShape(obj)

    def process_event(self, event: pygame.event.Event):
        self.manager.process_events(event)

    def update(self, dt: float):
        self.manager.update(dt)

    def draw(self):
        self.manager.draw_ui(self.window)

    def _renderShape(self, shape: Object):
        if isinstance(shape, Circle):
            pygame.draw.circle(
                self.window,
                (0, 255, 0),
                self._world_to_screen(shape.position),
                shape.radius * METRIC_TO_PIXEL_RATIO,
            )
        pass

    def _world_to_screen(self, world_pos: pygame.math.Vector2) -> tuple[int, int]:
        """
        Converts real world coordinates (like in Scene) into pixel values inside of scene_rect
        """
        x, y = world_pos * METRIC_TO_PIXEL_RATIO

        screen_x = self.scene_rect.left + x
        screen_y = self.scene_rect.bottom - y

        return int(screen_x), int(screen_y)

    def _button_rect(self):
        """
        Gets a new pygame rect for a button.
        """
        self.num_buttons = getattr(self, "num_buttons", -1) + 1

        return pygame.Rect(
            self.sidebar_padding,
            self.sidebar_padding
            + self.num_buttons * (self.button_height + self.button_gap),
            self.sidebar_rect.width - 2 * self.sidebar_padding,
            self.button_height,
        )
