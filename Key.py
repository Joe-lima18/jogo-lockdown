import pygame as pg


class Key:
    def __init__(self, x, y):
        # Imagem da chave
        self.image = pg.image.load(
            "assets/imagens/chave.png"
        ).convert_alpha()

        self.rect = self.image.get_rect(center=(x, y))

        # Indica se a chave já foi coletada
        self.collected = False

    def update(self):
        pass

    def draw(self, window):
        if not self.collected:
            window.blit(self.image, self.rect)

    def collect(self, player):
        """
        Retorna True quando o jogador pega a chave.
        """
        if not self.collected and self.rect.colliderect(player.rect):
            self.collected = True
            return True

        return False