import pygame as pg

from const import BRANCO, VERMELHO, WIN_WIDTH, WIN_HEIGHT


class Controls:

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

            self.window.fill((15, 15, 15))

            titulo = self.font_title.render(
                "CONTROLES",
                True,
                VERMELHO
            )

            self.window.blit(
                titulo,
                titulo.get_rect(center=(WIN_WIDTH//2, 80))
            )

            textos = [

                "W A S D  - Movimentar",

                "ENTER - Confirmar",

                "ESC - Voltar",

                "Pegue a chave",

                "Abra a porta",

                "Evite os inimigos"

            ]

            y = 180

            for texto in textos:

                surface = self.font.render(texto, True, BRANCO)

                self.window.blit(
                    surface,
                    surface.get_rect(center=(WIN_WIDTH//2, y))
                )

                y += 45

            pg.display.flip()

            for event in pg.event.get():

                if event.type == pg.QUIT:
                    pg.quit()
                    raise SystemExit

                if event.type == pg.KEYDOWN:

                    if event.key in (pg.K_ESCAPE, pg.K_RETURN):
                        return