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

cord_x = 10
cord_y = 10

speed_x = 0
speed_y = 0
#crear ventana
screen = pygame.display.set_mode(size)

#controlar fps
clock = pygame.time.Clock()
#bucle principal
while True:
    #capturar evento salir
    for event in pygame.event.get():
        #print(event)#mostrar todos los eventos
        if event.type == pygame.QUIT:
            sys.exit()

        #eventos teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x = -3
            if event.key == pygame.K_RIGHT:
                speed_x = 3
            if event.key == pygame.K_UP:
                speed_y = -3
            if event.key == pygame.K_DOWN:
                speed_y = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speed_x = 0
            if event.key == pygame.K_RIGHT:
                speed_x = 0
            if event.key == pygame.K_UP:
                speed_y = 0
            if event.key == pygame.K_DOWN:
                speed_y = 0

    ###logica--------------

    ###logica---------------

    ###pintar pantalla
    screen.fill(WHITE)#pintar la pantalla de un color
    #pintar pantalla

    ### ------ ZONA DE DIBUJO-------
    cord_x +=speed_x
    cord_y +=speed_y
    pygame.draw.rect(screen, RED, (cord_x, cord_y, 100, 100))

    ### ------ ZONA DE DIBUJO-------

    pygame.display.flip()#actualizar pantalla
    clock.tick(60)#60 frames por segudno