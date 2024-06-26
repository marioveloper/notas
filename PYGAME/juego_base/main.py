import pygame

#variables
SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#clase enemigo
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y = 10
        self.rect.x = 10

#clase jugador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.y = mouse_pos[0]
        self.rect.x = mouse_pos[1]


#clase juego
class Game(object):
    def __init__(self):
        self.score = 0

        self.enemy_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        self.enemy = Enemy()
        #enemy.rect.x = 100
        #enemy.rect.y = 100

        self.enemy_list.add(self.enemy)
        self.all_sprites_list.add(self.enemy)

        self.player = Player()
        self.all_sprites_list.add(self.player)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

    def run_logic(self):
        self.all_sprites_list.update()

    def display_frame(self):
        self.fill(WHITE)
        self.all_sprites_list.draw(screen)
        pygame.display.flip()

#funcion principal
def main():
    pygame.init()

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGTH])
    done = False
    clock = pygame.time.Clock()
    game = Game()

    while not done:
        done = game.process_events()
        game.run_logic
        game.display_frame(screen)
        clock.tick(60)
    pygame.quit()

#principal
if __name__ == "__main__":
    main()