import pygame
from main.scenes.SceneBase import SceneBase
from main.gameobjects.Splat import Splat
from main.gameobjects.GameObjectBase import GameObjectBase
from main.util.Quadtree import Quadtree
from main.gameobjects.blocks.Grass import Grass


class GameScene(SceneBase):

    game_objects = []
    obj_tree = None

    # splat is created here because he is super important to the scene
    splat = Splat()
    game_objects.append(splat)

    # Just tells it to do what the SceneBase does
    def __init__(self):
        super().__init__()

    def setup(self, screen):

        self.obj_tree = Quadtree(0, 0, screen.get_width(), screen.get_height())
        self.splat.pos = (0, screen.get_height() - self.splat.get_rect().h)
        self.game_objects.append(Grass(0, 0))

    # Doodle Zone
    def render(self, screen):
        screen.fill([0, 0, 0])

        self.obj_tree.render(screen)

        for obj in self.game_objects:
            obj.render(screen)

    # Key Processing
    def process_input(self, filtered_events, pressed_keys):
        return

    # Logic
    def update(self):

        for obj in self.game_objects:
            self.obj_tree.insert(obj)
