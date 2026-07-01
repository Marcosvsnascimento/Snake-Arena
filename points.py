from PPlay.sprite import Sprite
import random

class Points:

    def __init__(self, largura, altura, cell_size):

        self.cell_size = cell_size

        self.max_x = largura // cell_size
        self.max_y = altura // cell_size

        self.sprite = Sprite("images/point.png")

        self.respawn()


    def respawn(self, occupiedPositions=None):

        if occupiedPositions is None:
            occupiedPositions = []

        while True:

            x = random.randint(0, self.max_x - 1)
            y = random.randint(0, self.max_y - 1)

            if (x, y) not in occupiedPositions:
                break

        self.grid_x = x
        self.grid_y = y

        self.sprite.x = x * self.cell_size
        self.sprite.y = y * self.cell_size

    def draw(self):
        self.sprite.draw()