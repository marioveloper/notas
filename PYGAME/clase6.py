import random
import pygame, sys

#inicializar
pygame.init()

#variables
#colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (240, 100, 0)
#tamano pantalla
size = (800, 500)

#crear ventana
screen = pygame.display.set_mode(size)

#controlar fps
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)
#bucle principal
while True:
    #capturar evento salir
    for event in pygame.event.get():
        #print(event)#mostrar todos los eventos
        if event.type == pygame.QUIT:
            sys.exit()
    ###logica--------------
    mouse_pos = pygame.mouse.get_pos()
    x=mouse_pos[0]
    y=mouse_pos[1]
    ###logica---------------

    ###pintar pantalla
    screen.fill(WHITE)#pintar la pantalla de un color
    #pintar pantalla

    ### ------ ZONA DE DIBUJO-------
    pygame.draw.rect(screen, RED, (x, y, 100, 100))

    ### ------ ZONA DE DIBUJO-------

    pygame.display.flip()#actualizar pantalla
    clock.tick(60)#60 frames por segudno