import pygame as pg

from const import WIN_WIDTH, WIN_HEIGHT
from Menu import Menu

class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        

    def run(self):
        
        while True:
            menu = Menu(self.window)
            pass
            menu.run()
            
            #for event in pg.event.get():
            #   if event.type == pg.QUIT: #fechar janela
            #        quit() #encerra o programa
            
