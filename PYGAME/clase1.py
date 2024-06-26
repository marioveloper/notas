import pygame, sys

#inicializar
pygame.init()

#variable
size = (800, 500)

#crear ventana
screen = pygame.display.set_mode(size)

#bucle principal
while True:
    for event in pygame.event.get():
        print(event)#mostrar todos los eventos
        if event.type == pygame.QUIT:
            sys.exit()
