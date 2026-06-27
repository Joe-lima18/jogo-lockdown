import pygame as pg


class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.surf = pg.image.load("assets/imagens/labirinto-level-1.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pg.mixer.music.load("./assets/sons/sommenu.wav")
        pg.mixer.music.play(-1)

        clock = pg.time.Clock()

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    raise SystemExit

            self.window.blit(self.surf, self.rect)

            pg.display.flip()
            clock.tick(60)