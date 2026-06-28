import pygame as pg
from pygame import mask


class Player:

    def __init__(self, x, y):
        # Imagem do jogador
        self.image = pg.image.load(
            "assets/imagens/player.png"
        ).convert_alpha()

        # Retângulo de colisão
        self.rect = self.image.get_rect(center=(x, y))

        # Velocidade
        self.speed = 5
        self.has_key = False

        # Direção
        self.dx = 0
        self.dy = 0

    def input(self):
        """Lê o teclado."""

        keys = pg.key.get_pressed()

        self.dx = 0
        self.dy = 0

        if keys[pg.K_a]:
            self.dx = -self.speed

        if keys[pg.K_d]:
            self.dx = self.speed

        if keys[pg.K_w]:
            self.dy = -self.speed

        if keys[pg.K_s]:
            self.dy = self.speed

    def move(self, mask):

    # Movimento no eixo X
        next_rect = self.rect.move(self.dx, 0)

        if not self.collide(mask, next_rect):
             self.rect = next_rect

    # Movimento no eixo Y
        next_rect = self.rect.move(0, self.dy)

        if not self.collide(mask, next_rect):
            self.rect = next_rect

    def update(self, mask):
        self.input()
        self.move(mask)

    def draw(self, window):
        window.blit(self.image, self.rect)
        
    def collide(self, mapa, rect):

        pontos = [
            rect.topleft,
            rect.topright,
            rect.bottomleft,
            rect.bottomright
        ]   

        for x, y in pontos:

        # Fora do mapa
            if (
                x < 0 or
                y < 0 or
                x >= mapa.get_width() or
                y >= mapa.get_height()
            ):
                return True

            cor = mapa.get_at((x, y))

        # Preto = parede
            if cor[:3] == (0, 0, 0):
                return True

        return False
        
    