from main.gameobjects.blocks.Block import Block


class Grass(Block):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.image_name = "grass.png"
        self.load_image()
