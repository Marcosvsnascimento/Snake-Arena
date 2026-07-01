from PPlay.sprite import *
from snake import *
from points import *
from obstacles import *
from playerController import *
from rock import *

class JogoSolo:

    def __init__(self, keyboard):

        self.keyboard = keyboard
        self.reset()
        

    def reset(self):
        
        controller = PlayerController(self.keyboard)
        self.snake = Snake(600, 500, controller,"images/snake.png")
        self.obstacles = Obstacles(0, 900, 600, self.snake.cell_size)
        self.points = Points(900, 600, self.snake.cell_size)
        self.timerPedra = 0
        self.score = 0
        self.intervaloPedra = 2
        self.perdeu = False

    def update(self, delta):
        self.snake.update(delta)
        occupied = []
        occupied.extend(self.snake.positions)

        for pedra in self.obstacles.pedras:
            occupied.append((pedra.grid_x, pedra.grid_y))

        if self.snake.sprite.collided(self.points.sprite):
            self.snake.grow()
            self.score += 100
            self.points.respawn(occupied)

        self.timerPedra += delta

        if self.timerPedra >= self.intervaloPedra:

            self.timerPedra = 0

            self.obstacles.criarPedra(self.snake.positions, (self.points.grid_x, self.points.grid_y))
        
        head = (self.snake.grid_x, self.snake.grid_y)

        for pedra in self.obstacles.pedras:

            if self.snake.sprite.collided(pedra.sprite):
                self.perdeu = True

        if head in self.snake.positions[1:]:
            self.perdeu = True
        
        if self.snake.grid_x < 0 or self.snake.grid_x >= 40 or self.snake.grid_y < 0 or self.snake.grid_y >= 27:
            self.perdeu = True
        
        if self.perdeu:
            self.resultado = self.score
            self.reset()
            return 5

    def draw(self):
        self.points.draw()
        self.snake.draw()
        self.obstacles.draw()
