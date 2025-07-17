import pygame
import pygame_gui as gui
from UI.Scene import Scene
from UI.UI import UI


class App:
    def __init__(self, width: int = 1200, height: int = 800):
        # Set up window
        pygame.init()
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Physics Engine")

        self.clock = pygame.time.Clock()
        self.running = True
        self.sim_running = False

        # Init Scene and UI
        self.scene = Scene(12, 8)  # Scene uses w and h as bounding box
        self.ui = UI(self.window, self.scene)

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000  # 60 FPS.

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                self.ui.process_event(event)

                if event.type == gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.ui.start_button:
                        self.sim_running = True
                        self.scene.save_objects()
                    elif event.ui_element == self.ui.reset_button:
                        self.sim_running = False
                        self.scene.load_objects()
                    elif event.ui_element == self.ui.clear_button:
                        self.sim_running = False
                        self.scene.reset()
                
            if self.sim_running:
                self.scene.step(dt)  # physics step

            self.window.fill((0, 0, 0))  # Clear screen
            self.ui.render()  # Render scene

            self.ui.update(dt)
            self.ui.draw()
            pygame.display.update()  # Show frame

        pygame.quit()


if __name__ == "__main__":
    app = App()
    app.run()
