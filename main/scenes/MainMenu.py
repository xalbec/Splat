from main.scenes.SceneBase import SceneBase
from main.gameobjects.Text import Text
from main.scenes.GameScene import GameScene
import pygame


class MainMenu(SceneBase):

    game_objects = []

    def __init__(self):
        super().__init__()

    # Set everything up
    def setup(self, screen):
        play_text = Text("Play Splat", "arial", 50, [255, 255, 255])
        play_text.pos = (screen.get_width()/2 - play_text.rend.get_width()/2, 100)
        self.game_objects.append(play_text)

    # Doodle Zone
    def render(self, screen):
        screen.fill([0, 0, 0])

        for obj in self.game_objects:
            obj.render(screen)

    # Key Processing
    def process_input(self, filtered_events, pressed_keys):

        for event in filtered_events:

            if event.type == pygame.MOUSEBUTTONUP:

                if self.game_objects[0].get_rect().collidepoint(pygame.mouse.get_pos()):
                    self.switch_scene(GameScene())

    # Logic
    def update(self):

        # Sets the color of play_text to change when hovered over
        # TODO make a better way of saying a specific component and not just game_object[0]
        if self.game_objects[0].get_rect().collidepoint(pygame.mouse.get_pos()):
            self.game_objects[0].set_color([0, 255, 0])
        else:
            self.game_objects[0].set_color([255, 255, 255])
