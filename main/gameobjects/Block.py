import pygame
from main.gameobjects.GameObjectBase import GameObjectBase


class Block(GameObjectBase):

    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.image = None
