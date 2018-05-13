import pygame
import math
from main.gameobjects.GameObjectBase import GameObjectBase


class Splat(GameObjectBase):

    def __init__(self, pos=(0, 0)):
        self.radius = 30
        self.pos = pos
        self.vel = (0, 0)
        self.color = [255, 255, 255]

    def render(self, screen):
        pygame.draw.arc(screen, self.color, self.get_rect(), 0, math.pi*2)

    def update(self):
        self.pos += self.vel

    def get_rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.radius*2, self.radius*2)
