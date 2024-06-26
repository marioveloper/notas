import pygame, sys

#inicializar
pygame.init()

#variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

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

    pygame.draw.line(screen, GREEN, [0,100], [200,300], 6) #dibujar linea

    pygame.draw.rect(screen, BLACK, (100,400, 80, 80))#dibujar rectangulo

    pygame.draw.circle(screen, BLUE, (400, 250), 30)#dibujar circulo
    ### ------ ZONA DE DIBUJO-------

    pygame.display.flip()#actualizar pantalla