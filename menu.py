import pygame


class menu:
    def __init__(self):
        self.current_text = None

    def draw_boxes(self, window):
        pygame.draw.rect(window, (186, 140, 99), (480, 70, 240, 150))
        pygame.draw.rect(window, (101, 78, 58), (475, 65, 250, 160), 5)
        pygame.draw.rect(window, (245, 245, 220), (480, 250, 240, 150))
        pygame.draw.rect(window, (101, 78, 58), (475, 245, 250, 160), 5)
