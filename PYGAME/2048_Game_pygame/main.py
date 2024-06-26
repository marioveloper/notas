import pygame
from constantes import *

pygame.init()
screen = pygame.display.set_mode(DIMENSIONES)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND)
    #horizontales
    pygame.draw.line(screen, BLACK, (100,200), (300,200))
    pygame.draw.line(screen, BLACK, (100,250), (300,250))
    pygame.draw.line(screen, BLACK, (100,300), (300,300))
    pygame.draw.line(screen, BLACK, (100,350), (300,350))
    pygame.draw.line(screen, BLACK, (100,400), (300,400))
    #verticales
    pygame.draw.line(screen, BLACK, (100,200), (100,400))
    pygame.draw.line(screen, BLACK, (150,200), (150,400))
    pygame.draw.line(screen, BLACK, (200,200), (200,400))
    pygame.draw.line(screen, BLACK, (250,200), (250,400))
    pygame.draw.line(screen, BLACK, (300,200), (300,400))

    pygame.draw.rect(screen, S_2, uno)
    pygame.draw.rect(screen, S_4, dos)
    pygame.draw.rect(screen, S_8, tres)
    pygame.draw.rect(screen, S_16, cuatro)
    pygame.draw.rect(screen, S_32, cinco)
    pygame.draw.rect(screen, S_64, seis)
    pygame.draw.rect(screen, S_128, siete)
    pygame.draw.rect(screen, S_256, ocho)
    pygame.draw.rect(screen, S_512, nueve)
    pygame.draw.rect(screen, S_1024, diez)
    pygame.draw.rect(screen, S_2048, once)
    pygame.draw.rect(screen, S_2, doce)
    pygame.draw.rect(screen, S_4, trece)
    pygame.draw.rect(screen, S_8, catorce)
    pygame.draw.rect(screen, S_16, quince)
    pygame.draw.rect(screen, S_32, dieciseis)
    pygame.display.flip()

pygame.quit()