import pygame as pg


class Door:

    def __init__(self, x, y):

        self.image = pg.image.load(
            "assets/imagens/door.png"
        ).convert_alpha()

        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        pass

    def draw(self, window):
        window.blit(self.image, self.rect)

    def check_exit(self, player):

        if player.has_key and self.rect.colliderect(player.rect):
            return True

        return False