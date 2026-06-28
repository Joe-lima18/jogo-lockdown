import pygame as pg

from Level import Level
from const import MENU_OPTIONS, WIN_WIDTH, WIN_HEIGHT
from Menu import Menu

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
                level = Level(self.window, name="Nível 1")
                result = level.run()

                if result == "WIN":
                    print("Parabéns!")
                    
            #SAIR
            elif menu_return == MENU_OPTIONS[3]: 
                pg.quit()
                quit()  # Sai do jogo