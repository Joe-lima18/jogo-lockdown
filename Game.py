import pygame as pg

from Level import Level
from const import MENU_OPTIONS, WIN_WIDTH, WIN_HEIGHT
from Menu import Menu
from Controls import Controls
from Credits import Credits

class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        

    def run(self):
        
        while True:
            menu = Menu(self.window)
            pass
            menu_return = menu.run()
            
            # JOGAR
            if menu_return == MENU_OPTIONS[0]:

                level = Level(self.window, "Nível 1")

                result = level.run()

                if result == "WIN":
                    self.win_screen()

                elif result == "GAME_OVER":
                    self.game_over_screen()
               
            # CONTROLES     
            if menu_return == MENU_OPTIONS[1]:

                controls = Controls(self.window)

                controls.run()

            # CRÉDITOS
            elif menu_return == MENU_OPTIONS[2]:

                credits = Credits(self.window)

                credits.run()
                    
            #SAIR
            elif menu_return == MENU_OPTIONS[3]: 
                pg.quit()
                quit()  # Sai do jogo
                
                
    def win_screen(self):
        # Tela de vitória
        self.window.fill((0, 0, 0))
        font_title = pg.font.Font(
        "assets/fontes/Orbitron-VariableFont_wght.ttf",
        60)
        text = font_title.render("Você venceu!", True, (255, 255, 255))
        self.window.blit(text, (WIN_WIDTH // 2 - text.get_width() // 2, WIN_HEIGHT // 2 - text.get_height() // 2))
        pg.display.flip()
        pg.time.wait(3000)  # Espera 3 segundos antes de voltar ao menu 
        
    def game_over_screen(self):
        # Tela de derrota
        self.window.fill((0, 0, 0))
        font_title = pg.font.Font(
        "assets/fontes/Orbitron-VariableFont_wght.ttf",
        60)
        text = font_title.render("Game Over", True, (255, 0, 0))
        self.window.blit(text, (WIN_WIDTH // 2 - text.get_width() // 2, WIN_HEIGHT // 2 - text.get_height() // 2))
        pg.display.flip()
        pg.time.wait(3000)  # Espera 3 segundos antes de voltar ao menu
        
       
        
           