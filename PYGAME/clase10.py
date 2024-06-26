import pygame

screen = pygame.display.set_mode([752, 520])

clock = pygame.time.Clock()

done = False

background = pygame.image.load("background.jpg").convert()

player = pygame.image.load("player.png").convert()
player.set_colorkey([0,0,0])
player.set_colorkey([255,255,255])

pygame.mouse.set_visible(0)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    mouse_pos = pygame.mouse.get_pos()

    screen.blit(background, [0,0])
    screen.blit(player, mouse_pos)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()