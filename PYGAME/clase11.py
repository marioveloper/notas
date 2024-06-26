import pygame, random

pygame.init()
screen = pygame.display.set_mode([752, 520])
clock = pygame.time.Clock()
done = False
score = 0
background = pygame.image.load("background.jpg").convert()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('enemy.png').convert()
        self.image.set_colorkey([0, 0, 0])
        self.image.set_colorkey([255, 255, 255])
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('player.png').convert()
        self.image.set_colorkey([0, 0, 0])
        self.image.set_colorkey([255, 255, 255])
        self.rect = self.image.get_rect()


enemy_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()


for i in range(50):
    enemy = Enemy()
    enemy.rect.x = random.randrange(752-30)
    enemy.rect.y = random.randrange(520-30)

    enemy_list.add(enemy)
    all_sprite_list.add(enemy)

player = Player()
all_sprite_list.add(player)
pygame.mouse.set_visible(0)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    mouse_pos = pygame.mouse.get_pos()
    player.rect.x = mouse_pos[0]
    player.rect.y = mouse_pos[1]

    enemy_hit_list = pygame.sprite.spritecollide(player, enemy_list, True)

    for enemy in enemy_hit_list:
        score +=1
        print(score)

    screen.blit(background, [0,0])

    all_sprite_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
