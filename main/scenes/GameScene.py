import pygame
from main.scenes.SceneBase import SceneBase
from main.gameobjects.Splat import Splat


class GameScene(SceneBase):

    game_objects = []

    # splat is created here because he is super important to the scene
    splat = Splat()
    game_objects.append(splat)

    # Just tells it to do what the SceneBase does
    def __init__(self):
        super().__init__()

    def setup(self, screen):
        self.splat.pos = (0, screen.get_height() - self.splat.get_rect().h)

    # Doodle Zone
    def render(self, screen):
        screen.fill([0, 0, 0])

        for obj in self.game_objects:
            obj.render(screen)

    # Key Processing
    def process_input(self, filtered_events, pressed_keys):
        return

    # Logic
    def update(self):
        return
