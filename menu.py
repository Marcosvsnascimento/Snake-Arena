from PPlay.sprite import *
from utils import *

class Menu:
    def __init__(self, window):

        self.bJogar = Sprite("images/bJogar.png")
        self.bSair = Sprite("images/bSair.png")

        self.bJogar.set_position((window.width - self.bJogar.width)/2, 320)
        self.bSair.set_position((window.width - self.bSair.width)/2, 420)

    def draw(self):
        self.bJogar.draw()
        self.bSair.draw()

    def update(self, mouse, contagemClique, tempoClique):            
        if mouse.is_button_pressed(1) and  contagemClique >= tempoClique:

            if clicked(self.bJogar, mouse):
                return 1

            if clicked(self.bSair, mouse):
                return -1

        return 0   