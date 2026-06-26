import pygame as pg

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pg.image.load("assets/menu.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        
        pg.mixer_music.load("./assets/sommenu.wav")  # Carrega a música
        pg.mixer_music.play(-1)  # Reproduz em loop

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            pg.display.flip()
