from PPlay.window import *
from PPlay.gameimage import *
from PPlay.mouse import *
from PPlay.keyboard import *

from menu import *
from menuMode import *
from jogoSolo import *
from jogoDuelo import *
from result import *

window = Window(900,600)
mouse = Mouse()
keyboard = Keyboard()

menu = Menu(window)
menuMode = MenuMode(window)
jogoSolo = JogoSolo(keyboard)
jogoDuelo = JogoDuelo(keyboard)
result = Resultado()


background = GameImage("images/background.png")

estado = 0
novoEstado = 0
mode = 0

contagemClique = 0
tempoClique = 0.2

while True:
    background.draw()
    delta = window.delta_time()
    contagemClique += delta

    # MENU
    if estado == 0:
        menu.draw()
        novoEstado = menu.update(mouse, contagemClique, tempoClique)
        if novoEstado != 0:
            estado = novoEstado
            contagemClique = 0

    elif estado == 1:
        menuMode.draw()
        novoEstado, mode = menuMode.update(mouse, contagemClique, tempoClique)
        
        if novoEstado != 1:
            estado = novoEstado
            contagemClique = 0

    elif estado == 2:
        novoEstado = jogoSolo.update(delta)
        jogoSolo.draw()

        if keyboard.key_pressed("ESC") or novoEstado == 0:
            estado = 0

        if novoEstado == 5:
            result.setResultado("GAME OVER", f"Pontuação: {jogoSolo.resultado}")
            estado = 5

    elif estado == 3:
        novoEstado = jogoDuelo.update(delta)
        jogoDuelo.draw(window)

        if keyboard.key_pressed('ESC') or novoEstado == 0:
            estado = 0

        if novoEstado == 5:
            result.setResultado(jogoDuelo.resultado,f"Player {jogoDuelo.playerScore} x {jogoDuelo.iaScore} IA")
            jogoDuelo.reset()
            estado = 5

    elif estado == 5:

        result.draw(window)

        novoEstado = result.update(keyboard)

        if novoEstado != 5:
            estado = novoEstado

    
    elif estado == -1:
        window.close()

    
    window.update()
