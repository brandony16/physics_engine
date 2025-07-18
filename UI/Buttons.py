import pygame
import pygame_gui as gui


def get_panel(
    manager: gui.UIManager, rect: pygame.Rect, id: str = ""
) -> gui.elements.UIPanel:
    panel = gui.elements.UIPanel(
        relative_rect=rect, starting_height=1, manager=manager, object_id=id
    )
    return panel


def get_button(
    manager: gui.UIManager,
    rect: pygame.Rect,
    container: gui.elements.UIPanel,
    text: str,
) -> gui.elements.UIButton:
    button = gui.elements.UIButton(
        relative_rect=rect,
        manager=manager,
        container=container,
        text=text,
        object_id="#button",
    )
    return button
