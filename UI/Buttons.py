import pygame
import pygame_gui as gui


def get_panel(manager: gui.UIManager, rect: pygame.Rect) -> gui.elements.UIPanel:
    panel = gui.elements.UIPanel(relative_rect=rect, starting_height=1, manager=manager)
    return panel


def get_button(
    manager: gui.UIManager,
    rect: pygame.Rect,
    container: gui.elements.UIPanel,
    text: str,
) -> gui.elements.UIButton:
    button = gui.elements.UIButton(
        relative_rect=rect, manager=manager, container=container, text=text
    )
    return button
