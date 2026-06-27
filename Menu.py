import pygame as pg
from pygame.font import Font

from const import BRANCO, MENU_OPTIONS, VERMELHO



class Menu:
    def __init__(self, window):
        self.window = window
        #imagem de fundo do menu
        self.surf = pg.image.load("assets/imagens/menu.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0  # Opção de menu selecionada
        pg.mixer_music.load("./assets/sons/sommenu.wav")  # Carrega a música
        pg.mixer_music.play(-1)  # Reproduz em loop

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            
            for i in range(len(MENU_OPTIONS)):
                if i == menu_option:
                    self.menu_text(
                    text=MENU_OPTIONS[i],
                    text_size=36,
                    text_color=VERMELHO,
                    text_center_pos=(400, 250 + i * 70)
                )
                else:
                    self.menu_text(
                    text=MENU_OPTIONS[i],
                    text_size=36,
                    text_color=BRANCO,
                    text_center_pos=(400, 250 + i * 70)
                )

            #encerrar o jogo            
            for event in pg.event.get():
                if event.type == pg.QUIT: #fechar janela
                   quit() #encerra o programa
                
                if event.type == pg.KEYDOWN:
                        if event.key == pg.K_UP:
                            menu_option = (menu_option - 1) % len(MENU_OPTIONS)
                        elif event.key == pg.K_DOWN:
                            menu_option = (menu_option + 1) % len(MENU_OPTIONS)
                        if event.key == pg.K_RETURN:
                            return MENU_OPTIONS[menu_option] #ENTER     
                   
            pg.display.flip()
    
    def menu_text(self, text: str, text_size: int, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pg.font.Font("assets/fontes/Orbitron-VariableFont_wght.ttf", text_size)
        text_surf: pg.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pg.Rect = text_surf.get_rect(center = text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)               
            

    