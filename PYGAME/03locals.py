import pygame
from pygame.locals import *

#definir colores
BLACK = (0,0,0)
GRAY = (127,127,127)
WHITE = (255,255,255)

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)

#diccionario donde se asocia cada color con su letra
key_dict = {
    K_k: BLACK,
    K_r: RED,
    K_g: GREEN,
    K_b: BLUE,
    K_y: YELLOW,
    K_c: CYAN,
    K_m: MAGENTA,
    K_w: WHITE
}

background = key_dict[K_k]
pygame.init()

screen = pygame.display.set_mode([500,500])

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key in key_dict:
                background = key_dict[event.key]

        if event.type == pygame.QUIT:
            running = False

    screen.fill(background)
    pygame.display.update()
pygame.quit()