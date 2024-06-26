import pygame

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

#dimensiones pantall
dimensiones = [500,500]

# background
background = MAGENTA
#iniciar
pygame.init()

screen = pygame.display.set_mode(dimensiones)

running = True

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                background = RED
            elif event.key == pygame.K_b:
                background = BLACK
            elif event.key == pygame.K_w:
                background == WHITE
            elif event.key == pygame.K_y:
                background = YELLOW
        if event.type == pygame.QUIT:
            running = False
    screen.fill(background)
    pygame.display.update()

pygame.quit()

