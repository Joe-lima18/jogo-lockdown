import sys
import pygame as pg

from Door import Door
from const import BRANCO, WIN_HEIGHT
from Player import Player
from Enemy import Enemy
from Key import Key


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
        
        # Máscara de colisão
        self.mask = pg.image.load(
            "assets/imagens/labirinto-mascara-de-colisao.png").convert()

        # Tempo da fase (60 segundos)
        self.timeout = 60000

        # Relógio
        self.clock = pg.time.Clock()

        # Fonte
        self.font = pg.font.Font(
            "assets/fontes/Orbitron-VariableFont_wght.ttf",
            18
        )

        self.entities = []

        # Jogador
        self.player = Player(200, 150)
        self.entities.append(self.player)
        
        # Chaves
        self.keys = []

        positions = [(400, 300), (600, 400), (200, 500)]

        for pos in positions:
            key = Key(pos[0], pos[1])
            self.keys.append(key)
            self.entities.append(key)

        # Inimigos
        self.enemies = []
        positions = [(250, 180), (500, 150), (600, 480), (325, 320)]

        for pos in positions:
            enemy = Enemy(pos[0], pos[1])
            self.entities.append(enemy)
            self.enemies.append(enemy)
            
        # Porta
        self.door = Door(730, 100)
        self.entities.append(self.door)
            
            
    def run(self):
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
            
            #jogador
            self.player.update(self.mask)
            
            #inimigos
            for enemy in self.enemies:
                enemy.update(self.mask)
                
            for enemy in self.enemies:
                enemy.update(self.mask)

                # Colisão com o jogador
                if enemy.rect.colliderect(self.player.rect):
                    pg.mixer.music.stop()
                    return "GAME_OVER"
                
            #chaves
            for key in self.keys:
                key.update()

                if key.collect(self.player):
                    self.player.has_key = True
                    print("Chave coletada!")
                    
            
            #porta
            if self.door.check_exit(self.player):

                print("FASE CONCLUÍDA!")

                pg.mixer.music.stop()

                return "WIN"
            
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
            if self.player.has_key:
                self.level_text(
                    "CHAVE: ABRA A PORTA",
                    (500, 10)
                )
            else:
                self.level_text(
                    "CHAVE: FALTA CHAVES",
                    (500, 10)
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