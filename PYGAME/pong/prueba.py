import pygame

pygame.init()

#variables
BLACK = (0, 0, 0)
ORANGE = (240, 100, 0)
size = (800, 600)

#pelota
pelota_x = size[0]/2
pelota_y = size[1]/2
pelota_speed_x = 4
pelota_speed_y = 4
pelota_radio = 10
#jugador
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over=True

    pelota_x+=pelota_speed_x
    pelota_y+=pelota_speed_y


    #cuando la pelota toca la ventana
    if(pelota_y < 0 or pelota_y > size[1]):
        pelota_speed_y *= -1
    if(pelota_x < 0 or pelota_x > size[0]):
        pelota_speed_x *= -1

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

    screen.fill(ORANGE)

    pelota = pygame.draw.circle(screen, BLACK, (pelota_x, pelota_y), pelota_radio)#pelota
    #colisiones


    ###_______________________

    pygame.display.flip()
    clock.tick(80)

pygame.quit()