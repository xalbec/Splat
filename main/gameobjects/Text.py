import pygame
from main.gameobjects.GameObjectBase import GameObjectBase

pygame.font.init()


class Text(GameObjectBase):

    def __init__(self, string, font, size, color=(0, 0, 0), pos=(0, 0)):
        self.string = string
        self.font = pygame.font.SysFont(font, size)
        self.rend = self.font.render(string, False, color)
        self.pos = pos

    def render(self, screen):
        screen.blit(self.rend, [self.get_rect().x, self.get_rect().y])

    def update(self):
        return

    def set_color(self, color):
        self.rend = self.font.render(self.string, False, color)

    def get_rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.rend.get_width(), self.rend.get_height())
