import pygame
from main.gameobjects.GameObjectBase import GameObjectBase


class Block(GameObjectBase):

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.image = "NoImageFound.jpg"
