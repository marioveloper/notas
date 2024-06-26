from dokusan import generators
import numpy as np
import pygame

sudoku = np.array(list(str(generators.random_sudoku(avg_rank=150)))).reshape(9,9)
blanco = (0,0,0)
pygame.init()
screen = pygame.display.set_mode([100,100])

running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    screen.fill(blanco)
    pygame.display.flip()
pygame.quit()