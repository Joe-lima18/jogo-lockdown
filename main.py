import pygame as pg

print('Setup start')
pg.init()
window = pg.display.set_mode(size=(800, 600))
print('Setup End')

print('Loop start')
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT: #fechar janela
            quit() #encerra o programa