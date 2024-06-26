import random
import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super.__init__()
        self.color = (255, 0, 0)
        self.pos_x = random.randint(0,475)-self.pos_x%25
        self.pos_y = random.randint(0,475)-self.pos_y%25
