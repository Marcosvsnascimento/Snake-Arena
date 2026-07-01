import pygame

class Resultado:

    def __init__(self):
        self.titulo = ""
        self.texto = ""
        pygame.font.init()
        self.fontTitulo = pygame.font.SysFont("Arial", 48, bold=True)
        self.fontTexto = pygame.font.SysFont("Arial", 30)

    def setResultado(self, titulo, texto):
        self.titulo = titulo
        self.texto = texto

    def update(self, keyboard):

        if keyboard.key_pressed("ENTER"):
            return 0  

        return 5   

    def drawHUD(self, window):

        textoTitulo = self.fontTexto.render(f"{self.titulo}", True, (255,255,255))
        textoTexto = self.fontTitulo.render(f"{self.texto}", True, (255,255,255))
        textoContinuar = self.fontTexto.render("Pressione ENTER para voltar ao menu", True, (180, 180, 180))

        tituloX = (window.width - textoTitulo.get_width()) // 2
        textoX = (window.width - textoTexto.get_width()) // 2
        continuarX = (window.width - textoContinuar.get_width()) // 2

        window.screen.blit(textoTitulo, (tituloX, 160))
        window.screen.blit(textoTexto, (textoX, 260))
        window.screen.blit(textoContinuar, (continuarX, 500))

    def draw(self, window):
        self.drawHUD(window)
        pass