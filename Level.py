import sys
import pygame as pg

from const import BRANCO, WIN_HEIGHT
from Player import Player


class Level:
    def __init__(self, window, name):
        print("Entrou no __init__")
        self.window = window
        self.name = name

        # Fundo da fase
        self.surf = pg.image.load(
            "assets/imagens/labirinto-level-1.png"
        ).convert()
        self.rect = self.surf.get_rect(topleft=(0, 0))

        # Tempo da fase (60 segundos)
        self.timeout = 60000

        # Relógio
        self.clock = pg.time.Clock()

        # Fonte
        self.font = pg.font.Font(
            "assets/fontes/Orbitron-VariableFont_wght.ttf",
            18
        )

        # Entidades do jogo
        self.entities = []

        # Jogador
        self.player = Player(100, 100)
        self.entities.append(self.player)

    def run(self):
        # Música da fase
        pg.mixer.music.load("assets/sons/sommenu.wav")
        pg.mixer.music.play(-1)

        running = True

        while running:

            # FPS
            dt = self.clock.tick(60)

            # Eventos
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            # Atualiza tempo
            if self.timeout > 0:
                self.timeout -= dt
            else:
                self.timeout = 0

            # Atualiza entidades
            for entity in self.entities:
                entity.update()

            # ---------- DESENHO ----------

            # Fundo
            self.window.blit(self.surf, self.rect)

            # Desenha entidades
            for entity in self.entities:
                entity.draw(self.window)

            # Interface
            self.level_text(
                f"{self.name}",
                (10, 10)
            )

            self.level_text(
                f"Tempo: {self.timeout/1000:.1f}s",
                (10, 35)
            )

            self.level_text(
                f"FPS: {self.clock.get_fps():.0f}",
                (10, WIN_HEIGHT - 40)
            )

            self.level_text(
                f"Entidades: {len(self.entities)}",
                (10, WIN_HEIGHT - 20)
            )

            pg.display.flip()

        pg.mixer.music.stop()
        pg.quit()
        sys.exit()

    def level_text(self, text, pos, color=BRANCO):
        surface = self.font.render(text, True, color)
        self.window.blit(surface, pos)