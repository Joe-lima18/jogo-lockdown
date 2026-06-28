import pygame as pg

from const import BRANCO, VERMELHO, WIN_WIDTH


class Credits:

    def __init__(self, window):

        self.window = window

        self.font_title = pg.font.Font(
            "assets/fontes/Orbitron-VariableFont_wght.ttf",
            42
        )

        self.font = pg.font.Font(
            "assets/fontes/Orbitron-VariableFont_wght.ttf",
            24
        )

    def run(self):

        while True:

            self.window.fill((10, 10, 10))

            titulo = self.font_title.render(
                "CRÉDITOS",
                True,
                VERMELHO
            )

            self.window.blit(
                titulo,
                titulo.get_rect(center=(400, 80))
            )

            creditos = [

                "Desenvolvedor",

                "José Lima Assunção Filho",

                "RU: 5273170",
                
                "",

                "Projeto desenvolvido em Python",

                "Utilizando Pygame",

                "",

                "2026"

            ]

            y = 180

            for texto in creditos:

                surface = self.font.render(texto, True, BRANCO)

                self.window.blit(
                    surface,
                    surface.get_rect(center=(400, y))
                )

                y += 40

            pg.display.flip()

            for event in pg.event.get():

                if event.type == pg.QUIT:
                    pg.quit()
                    raise SystemExit

                if event.type == pg.KEYDOWN:

                    if event.key in (pg.K_ESCAPE, pg.K_RETURN):
                        return