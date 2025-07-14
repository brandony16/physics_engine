import pygame
from UI.Scene import Scene
from UI.UI import UI

from physics.objects import Circle


class App:
    def __init__(self, width: int = 800, height: int = 800):
        # Set up window
        pygame.init()
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Physics Engine")

        self.clock = pygame.time.Clock()
        self.running = True


        circle = Circle(1, [400, 400], [0, 0], 100)  # Temp circle

        # Init Scene and UI
        self.scene = Scene(
            width, height, [circle]
        )  # Scene uses w and h as bounding box
        self.ui = UI(self.window, self.scene)

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000  # 60 FPS.

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    # TODO: implement UI buttons
                    continue

            self.scene.step(dt)  # physics step
            self.window.fill((0, 0, 0))  # Clear screen
            self.ui.render()  # Render scene
            pygame.display.flip()  # Show frame

        pygame.quit()


if __name__ == "__main__":
    app = App()
    app.run()
