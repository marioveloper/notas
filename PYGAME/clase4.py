from turtle import circle
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

#coordenadas
cord_x = 100
cord_y = 100

#velocidades
speed_x = 3
speed_y = 3



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
    ###logica--------------
    if(cord_x>size[0]-80 or cord_x<0):
        speed_x *= -1

    if(cord_y>size[1]-80 or cord_y<0):
        speed_y *= -1

    cord_x +=speed_x
    cord_y +=speed_y
    ###logica---------------

    ###pintar pantalla
    screen.fill(WHITE)#pintar la pantalla de un color
    #pintar pantalla

    ### ------ ZONA DE DIBUJO-------

    pygame.draw.rect(screen, GREEN, (cord_x, cord_y, 80, 80))
    ### ------ ZONA DE DIBUJO-------

    pygame.display.flip()#actualizar pantalla
    clock.tick(60)#60 frames por segudno