
class SceneBase:

    def __init__(self):
        self.next = self

    # Doodle Zone
    def render(self, screen):
        print("Scene needs a render function")

    # Key Processing
    def process_input(self, filtered_events, pressed_keys):
        print("Scene needs a process_input function")

    # Logic
    def update(self):
        print("Scene needs an update function")

    # One Time Run to setup the scene
    def setup(self, screen):
        print("Scene needs a Setup function")

    # Changes the current scene to next_scene
    def switch_scene(self, next_scene):
        self.next = next_scene

    # Sets current scene to display as Nothing. This will result in closing the game window
    def terminate(self):
        self.switch_scene(None)
