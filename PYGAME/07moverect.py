import pygame
from pygame.rect import *


running = True

pygame.init()

screen = pygame.display.set_mode([600,600])
rect = Rect(50, 60, 200, 80)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                rect.left = 0
            if event.key == K_c:
                rect.centerx = width//2
            if event.key == K_r:
                rect.right = width
            if event.key == K_t:
                rect.top = 0
            if event.key == K_m:
                rect.centery = height//2
            if event.key == K_b:
                rect.bottom = height

    screen.fill((127,127,127))
    pygame.draw.rect(screen, (0,0,255), rect)
    pygame.display.flip()
pygame.quit()