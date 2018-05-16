import pygame
import os
from main.gameobjects.GameObjectBase import GameObjectBase


class Block(GameObjectBase):

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.image_name = "NoImageFound.jpg"
        self.image = None

    def load_image(self):
        img_path = os.path.join("res\\blocks", self.image_name)
        self.image = pygame.image.load(img_path)

    def render(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
