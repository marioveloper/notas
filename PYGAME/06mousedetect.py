import pygame, math
#Constante
DIMENSIONES = [500, 500]
COLOR_FONDO = (124,213,111)

pygame.init()
screen = pygame.display.set_mode(DIMENSIONES)
running = True

#dibujar rectangulo
start = (0,0)
size = (0,0)
drawing = False

while running:
    for event in pygame.event.get():
        #logica
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event)
            start = event.pos
            size= 0,0
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            print(event)
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]
            drawing = False
        elif event.type == pygame.MOUSEMOTION and drawing:
            #end - event.pos
            #size = end[0] - start[0], end[1] - start[1]
            print(event)

        if event.type == pygame.QUIT:
            running = False

    #logica
    screen.fill(COLOR_FONDO)
    pygame.draw.rect(screen, (255,0,0), (start, size), 2)
    pygame.display.update()

pygame.quit()