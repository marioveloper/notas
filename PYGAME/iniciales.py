import pygame, sys
from pygame.locals import *
pygame.init()

ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption('hola mundo')

mifuente = pygame.font.SysFont("Courier", 30)
texto = mifuente.render('hola mundo',0,(234,23,45))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    ventana.blit(texto, (100,100))
    pygame.display.update()