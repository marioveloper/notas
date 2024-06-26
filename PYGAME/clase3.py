from turtle import circle
import pygame, sys

#inicializar
pygame.init()

#variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (240, 100, 0)
size = (800, 500)

#crear ventana
screen = pygame.display.set_mode(size)

#bucle principal
while True:
    #capturar evento salir
    for event in pygame.event.get():
        #print(event)#mostrar todos los eventos
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(WHITE)#pintar la pantalla de un color

    ### ------ ZONA DE DIBUJO-------

    pygame.draw.circle(screen, GREEN, (size[0]/2, 100), 40)#cabeza
    pygame.draw.circle(screen, GREEN, (size[0]/2, 200), 70)#tronco
    pygame.draw.circle(screen, GREEN, (size[0]/2, 300), 100)#base

    #ojo izquierdo
    pygame.draw.circle(screen, WHITE, (size[0]/2-10, 90), 5)
    pygame.draw.circle(screen, BLACK, (size[0]/2-10, 90), 3)
    pygame.draw.circle(screen, WHITE, (size[0]/2-10, 90), 1)
    #ojo derecho
    pygame.draw.circle(screen, WHITE, (size[0]/2+10, 90), 5)
    pygame.draw.circle(screen, BLACK, (size[0]/2+10, 90), 3)
    pygame.draw.circle(screen, WHITE, (size[0]/2+10, 90), 1)

    #nariz
    pygame.draw.circle(screen, ORANGE, (size[0]/2, 105), 7)
    pygame.draw.line(screen, ORANGE, [size[0]/2-3,100], [size[0]/2-20, 110], 1)
    pygame.draw.line(screen, ORANGE, [size[0]/2-3,110], [size[0]/2-20, 110], 1)

    for y in range(150, 400, 50):
        pygame.draw.circle(screen, BLACK, (size[0]/2, y), 8)
        pygame.draw.circle(screen, WHITE, (size[0]/2, y), 4)
    ### ------ ZONA DE DIBUJO-------

    pygame.display.flip()#actualizar pantalla