import pygame

#Constante
DIMENSIONES = [500, 500]
COLOR_FONDO = (124,213,111)


pygame.init()

screen = pygame.display.set_mode(DIMENSIONES)

running = True

while running:
    for event in pygame.event.get():
        #logica

        if event.type == pygame.QUIT:
            running = False

    #logica
    screen.fill(COLOR_FONDO)

    pygame.display.flip()

pygame.quit()