from PPlay.sprite import Sprite
import random
from rock import*

class Obstacles:

    def __init__(self, quantidade, largura, altura, cell_size):

        self.pedras = []

        self.max_x = largura // cell_size
        self.max_y = altura // cell_size
        self.cell_size = cell_size

        for _ in range(quantidade):

            x = random.randint(0, self.max_x - 1)
            y = random.randint(0, self.max_y - 1)

            self.pedras.append(Rock(x, y, cell_size))

    def draw(self):

        for pedra in self.pedras:
            pedra.draw()

    def criarPedra(self, snake_positions, food_pos):

        while True:

            x = random.randint(0, self.max_x - 1)
            y = random.randint(0, self.max_y - 1)

            if (x, y) in snake_positions:
                continue

            if (x, y) == food_pos:
                continue

            ocupado = False

            for pedra in self.pedras:
                if (x, y) == (pedra.grid_x, pedra.grid_y):
                    ocupado = True
                    break

            if not ocupado:
                break

        self.pedras.append(
            Rock(x, y, self.cell_size)
        )