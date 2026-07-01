from PPlay.sprite import *
from utils import *

class MenuMode:
    def __init__(self, window):

        self.bSolo = Sprite("images/bSolo.png")
        self.bDuelo = Sprite("images/bDuelo.png")
        self.bVoltar = Sprite("images/bVoltar.png")

        self.bSolo.set_position((window.width - self.bSolo.width)/2, 120)
        self.bDuelo.set_position((window.width - self.bDuelo.width)/2, 220)
        self.bVoltar.set_position((window.width - self.bVoltar.width)/2, 420)

    def draw(self):
        self.bSolo.draw()
        self.bDuelo.draw()
        self.bVoltar.draw()

    def update(self, mouse, contagemClique, tempoClique):            
        if mouse.is_button_pressed(1) and  contagemClique >= tempoClique:

            if clicked(self.bSolo, mouse):
                return 2, 1

            if clicked(self.bDuelo, mouse):
                return 3, 2
            
            if clicked(self.bVoltar, mouse):
                return 0, 0
            
        return 1, 0 