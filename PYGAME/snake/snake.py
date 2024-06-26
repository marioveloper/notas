import random
import pygame, sys
from enemy import *
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
size = (500, 500)

#crear ventana
screen = pygame.display.set_mode(size)

#controlar fps
clock = pygame.time.Clock()
#bucle principal

game_over = False
while not game_over:
    #capturar evento salir
    for event in pygame.event.get():
        #print(event)#mostrar todos los eventos
        if event.type == pygame.QUIT:
            sys.exit()

        #eventos teclado
#        if event.type == pygame.KEYDOWN:
#            if event.key == pygame.K_LEFT:
#                speed_x = -25
#                speed_y = 0
#            if event.key == pygame.K_RIGHT:
#                speed_x = 25
#                speed_y = 0
#            if event.key == pygame.K_UP:
#                speed_y = -25
#                speed_x = 0
#            if event.key == pygame.K_DOWN:
#                speed_y = 25
#                speed_x = 0

    ###logica--------------

    ###logica---------------

    ###pintar pantalla
    screen.fill(WHITE)#pintar la pantalla de un color
    enemigo = Enemy()
    enemigo.dibujar(screen)
    #dibujar cuadricula
    for p in range(0, size[0], 25):
        pygame.draw.line(screen, ORANGE, (p, 0), (p, size[1]), 1)
        pygame.draw.line(screen, ORANGE, (0, p), (size[0], p), 1)
    #pintar pantalla

    ### ------ ZONA DE DIBUJO-------
    ### ------ ZONA DE DIBUJO-------

    pygame.display.flip()#actualizar pantalla
    clock.tick(2)#60 frames por segudno