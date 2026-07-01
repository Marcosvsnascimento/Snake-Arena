from PPlay.sprite import *
from snake import *
from points import *
from obstacles import *
from iaController import *
from playerController import *
import pygame

class JogoDuelo:

    def __init__(self, keyboard):

        self.keyboard = keyboard
        self.reset()
        

    def reset(self):
        self.iaController = IAController()
        self.player = Snake(200, 300, PlayerController(self.keyboard),"images/snake.png")
        self.ia = Snake(700, 300, self.iaController, "images/snake1.png")
        self.points = Points(900, 600, self.player.cell_size)
        self.iaController.set_game(self.player, self.points)

        self.playerScore = 0
        self.iaScore = 0

        self.matchTime = 120    
        self.finished = False

        self.bateuP1 = False
        self.bateuP2 = False

        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 30)
        self.vencedor = ""

    def update(self, delta):
        self.matchTime -= delta

        
        if self.matchTime <= 0:

            if self.playerScore > self.iaScore:
                vencedor = "Vitória"

            elif self.playerScore < self.iaScore:
                vencedor = "Derrota"

            else:
                vencedor = "EMPATE"

            self.resultado = vencedor
            
            return 5
    
        self.player.update(delta)
        self.ia.update(delta)
        occupied = []
        occupied.extend(self.player.positions)
        occupied.extend(self.ia.positions)


        if self.player.sprite.collided(self.points.sprite):
            self.player.grow()
            self.playerScore += 1
            self.points.respawn(occupied)


        if self.ia.sprite.collided(self.points.sprite):
            self.ia.grow()
            self.iaScore += 1
            self.points.respawn(occupied)
        
        head = (self.player.grid_x, self.player.grid_y)
        if head in self.player.positions[1:]:
            self.bateuP1 = True
        
        if self.player.grid_x < 0 or self.player.grid_x >= 40 or self.player.grid_y < 0 or self.player.grid_y >= 27:
            self.bateuP1 = True
        
        
        if self.bateuP1:
            self.player.reset(200,300)
            self.playerScore = 0
            self.bateuP1 = False

        headIa = (self.ia.grid_x, self.ia.grid_y)
        if headIa in self.ia.positions[1:]:
            self.bateuP2 = True
        
        if headIa in self.player.positions[1:]:
            self.bateuP2 = True
        
        if self.ia.grid_x < 0 or self.ia.grid_x >= 40 or self.ia.grid_y < 0 or self.ia.grid_y >= 27:
            self.bateuP2 = True

        if head in self.ia.positions[1:]:
            self.bateuP1 = True
    
        if self.bateuP2:
            self.ia.reset(700,300)
            self.iaScore = 0
            self.bateuP2 = False

    def drawHUD(self, window):

        tempo = f"{int(self.matchTime)}"

        textoPlayer = self.font.render(f"Player: {self.playerScore}", True, (255,255,255))
        textoIA = self.font.render(f"IA: {self.iaScore}", True, (255,255,255))
        textoTempo = self.font.render(f"Tempo: {tempo}", True, (255,255,0))

        window.screen.blit(textoPlayer, (20,20))
        window.screen.blit(textoTempo, (380,20))
        window.screen.blit(textoIA, (720,20))
    
    
    def draw(self, window):
        self.points.draw()
        self.player.draw()
        self.ia.draw()
        self.drawHUD(window)
