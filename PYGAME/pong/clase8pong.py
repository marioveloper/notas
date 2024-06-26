import pygame

pygame.init()

#variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (240, 100, 0)
size = (800, 600)

#pelota
pelota_x = size[0]/2
pelota_y = size[1]/2

pelota_speed_x = 4
pelota_speed_y = 4
pelota_radio = 10
#jugador
jugador_ancho=10
jugador_alto=100

#jugador1
jugador1_x = 10
jugador1_y = size[1]/2

jugador1_speed=0

#jugador2
jugador2_x = size[0]-20
jugador2_y = size[1]/2

jugador2_speed=0



screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

game_over = False

###_______APP

###_____________



while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over=True

        if event.type == pygame.KEYDOWN:
            #jugador 1
            if event.key == pygame.K_w:
                jugador1_speed -=3
            if event.key == pygame.K_s:
                jugador1_speed +=3

            #jugador 2
            if event.key == pygame.K_UP:
                jugador2_speed -=3
            if event.key == pygame.K_DOWN:
                jugador2_speed +=3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                jugador1_speed =0
            if event.key == pygame.K_s:
                jugador1_speed = 0
            if event.key == pygame.K_UP:
                jugador2_speed =0
            if event.key == pygame.K_DOWN:
                jugador2_speed = 0
    ### logica_________________
    pelota_x+=pelota_speed_x
    pelota_y+=pelota_speed_y

    jugador1_y += jugador1_speed
    jugador2_y += jugador2_speed

    #cuando la pelota toca la ventana
    if (pelota_y < 0 or pelota_y > size[1]):
        pelota_speed_y *= -1

    if pelota_x < 0:
        print('gana jugador 2')
        pelota_x = size[0]/2
        pelota_y = size[1]/2
        jugador1_x = 10
        jugador1_y = size[1]/2
        jugador2_x = size[0]-20
        jugador2_y = size[1]/2

    if pelota_x > size[0]:
        print('gana jugador 1')
        pelota_x = size[0]/2
        pelota_y = size[1]/2
        jugador1_x = 10
        jugador1_y = size[1]/2
        jugador2_x = size[0]-20
        jugador2_y = size[1]/2

    #para que jugadores no salgan de la pantalla
    if jugador1_y <= 0:
        jugador1_speed = 0
    if jugador1_y >= size[1]-100:
        jugador1_speed = 0
    if jugador2_y <= 0:
        jugador2_speed = 0
    if jugador2_y >= size[1]-100:
        jugador2_speed = 0

    ###logica__________________
    screen.fill(ORANGE)

    ###______dibujo
    jugador1 = pygame.draw.rect(screen, BLACK, (jugador1_x, jugador1_y, jugador_ancho, jugador_alto))#jugador 1
    jugador2 = pygame.draw.rect(screen, BLACK, (jugador2_x, jugador2_y, jugador_ancho, jugador_alto))#jugador 2
    pelota = pygame.draw.circle(screen, GREEN, (pelota_x, pelota_y), pelota_radio)#pelota

    #colisiones
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pelota_speed_x *=-1

    ###_______________________

    pygame.display.flip()
    clock.tick(80)

pygame.quit()