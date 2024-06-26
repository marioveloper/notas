import pygame, sys
from pygame.locals import *

#variables
ancho, alto = 900,480

class naveEspacial(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenNave = pygame.image.load('1.png')

        self.rect = self.ImagenNave.get_rect()
        self.rect.centerx = ancho/2
        self.rect.centery = alto-30

        self.listaDisparo = []
        self.Vida = True
        self.velocidad = 20

    def disparar(self):
        pass

    def dibujar(self, superficie):
        superficie.blit(self.ImagenNave, self.rect)

    def movimiento(self):
        if self.Vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right >870:
                self.rect.right = 840

def SpaceInvader():
    pygame.init()
    ventana = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Space Invader")
    ImagenFondo = pygame.image.load("bg_cave.png")
    jugador = naveEspacial()
    enjuego = True

    while True:

        jugador.movimiento()
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()

            if enjuego == True:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == K_LEFT:
                        jugador.rect.left -=jugador.velocidad
                    elif evento.key == K_RIGHT:
                        jugador.rect.right += jugador.velocidad
        ventana.blit(ImagenFondo,(0,0))
        jugador.dibujar(ventana)
        pygame.display.update()

SpaceInvader()