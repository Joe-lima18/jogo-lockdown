import pygame as pg


class Enemy:
    def __init__(self, x, y):
        # Imagem
        self.image = pg.image.load(
            "assets/imagens/enemy.png"
        ).convert_alpha()

        self.rect = self.image.get_rect(center=(x, y))

        self.speed = 2

        # Direção inicial
        self.dx = self.speed
        self.dy = 0

    def update(self, mask):
        self.move(mask)

    def move(self, mask):

        next_rect = self.rect.move(self.dx, self.dy)

        if self.collide(mask, next_rect):
            # bateu na parede → inverte direção
            self.dx *= -1
        else:
            self.rect = next_rect

    def collide(self, mask, rect):

        points = [
            rect.topleft,
            rect.topright,
            rect.bottomleft,
            rect.bottomright,
        ]

        for x, y in points:

            if x < 0 or y < 0:
                return True

            if x >= mask.get_width() or y >= mask.get_height():
                return True

            color = mask.get_at((x, y))

            if color.r < 20 and color.g < 20 and color.b < 20:
                return True

        return False

    def draw(self, window):
        window.blit(self.image, self.rect)