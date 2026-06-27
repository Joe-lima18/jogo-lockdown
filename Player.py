import pygame as pg


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

    def move(self):
        """Move o jogador."""

        self.rect.x += self.dx
        self.rect.y += self.dy

    def update(self):
        self.input()
        self.move()

    def draw(self, window):
        window.blit(self.image, self.rect)