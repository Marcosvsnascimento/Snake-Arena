from PPlay.sprite import Sprite
import random

class Rock:

    def __init__(self, x, y, cell_size):

        self.grid_x = x
        self.grid_y = y
        self.cell_size = cell_size

        self.sprite = Sprite("images/rock.png")

        self.sprite.x = x * cell_size
        self.sprite.y = y * cell_size

    def draw(self):
        self.sprite.draw()