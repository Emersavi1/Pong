import pygame 
import random

pygame.init()
paused = False

gadget_pair = 1
ch = int(input("Ingresa tu elección para el dispositivo"))
if ch == 1:
    gadget_pair = 1
elif ch == 2:
    gadget_pair = 2 

# Inicio 
WIDTH, HEIGHT= 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong_by_Emerson_Salguedo")
run = True
player_1 = player_2 = 0
direction = [0, 1]
angle = [0, 1, 2]


# colors
PINK = (255, 105, 180)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# pelota
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
ball_vel_x, ball_vel_y = 0.7, 0.7
dummy_ball_x, dummy_ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
dummy_ball_vel_x, dummy_ball_vel_y = 0.7, 0.7

# dimension paletas
paddle_width, paddle_height = 20, 120
left_paddle_y = right_paddle_y = HEIGHT/2 - paddle_height/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, WIDTH -(100 - paddle_width/2)
second_left_paddle_y = second_right_paddle_y = HEIGHT/2 - paddle_height/2
second_left_paddle_x, second_right_paddle_x = 100 - paddle_width/2, WIDTH -(100 - paddle_width/2)
right_paddle_vel = left_paddle_vel = 0
second_right_paddle_vel = second_left_paddle_vel = 0

# gadgets
left_gadget = right_gadget = 0
left_gadget_remaining = right_gadget_remaining = 5

# Variable para indicar si ya se mostró la pantalla de fin de juego
game_over_shown = False

# bucle principal 
while run:
    wn.fill(BLACK)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                paused = not paused
            if i.key == pygame.K_UP:
                right_paddle_vel = -0.9
                second_right_paddle_vel = -0.9
            if i.key == pygame.K_DOWN:
                right_paddle_vel = 0.9
                second_right_paddle_vel = 0.9
            if i.key == pygame.K_RIGHT and right_gadget_remaining > 0:
                right_gadget = 1 
            if i.key == pygame.K_LEFT and right_gadget_remaining > 0:
                right_gadget = 2
            if i.key == pygame.K_w:
                left_paddle_vel = -0.9
                second_left_paddle_vel = -0.9
            if i.key == pygame.K_s:
                left_paddle_vel = 0.9
                second_left_paddle_vel = 0.9
            if i.key == pygame.K_d and left_gadget_remaining > 0:
                left_gadget = 1
            if i.key == pygame.K_a and left_gadget_remaining > 0:
                left_gadget = 2
            
    if not paused:
        if i.type == pygame.KEYUP:
            second_right_paddle_vel = 0
            right_paddle_vel = 0
            second_left_paddle_vel = 0
            left_paddle_vel = 0
             

    # control movimientos pelotas
    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
        ball_vel_y *= -1
    if dummy_ball_y <= 0 + radius or dummy_ball_y >= HEIGHT - radius:
        dummy_ball_vel_y *= -1
    if ball_x >= WIDTH - radius:
        player_1 += 1
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        dummy_ball_x, dummy_ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        second_left_paddle_y = left_paddle_y
        second_right_paddle_y = right_paddle_y
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -1.4, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = -1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.7, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = -0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.7, 1.4
                dummy_ball_vel_y, dummy_ball_vel_x = -0.7, 1.4

        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 1.4, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = 1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = 0.7, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = 0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.7, 1.4
                dummy_ball_vel_y, dummy_ball_vel_x = 0.7, 1.4
        ball_vel_x *= -1 
        dummy_ball_vel_x *= -1

    if ball_x <= 0 + radius:
        player_2 += 1
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        dummy_ball_x, dummy_ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        second_right_paddle_y = right_paddle_y
        second_left_paddle_y = left_paddle_y
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -1.4, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = -1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.7, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = -0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.7, 1.4
                dummy_ball_vel_y, dummy_ball_vel_x = -0.7, 1.4


        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 1.4, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = 1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = 0.7, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = 0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.7, 1.4
                dummy_ball_vel_y, dummy_ball_vel_x = 0.7, 1.4
        
    # control movimientos paletas
    if left_paddle_y >= HEIGHT - paddle_height:
        left_paddle_y = HEIGHT - paddle_height
    if left_paddle_y <= 0:
        left_paddle_y = 0
    if right_paddle_y >= HEIGHT - paddle_height:
        right_paddle_y = HEIGHT - paddle_height
    if right_paddle_y <= 0:
        right_paddle_y = 0
    
    if second_left_paddle_y >= HEIGHT - paddle_height:
        second_left_paddle_y = HEIGHT - paddle_height
    if second_left_paddle_y <= 0:
        second_left_paddle_y = 0
    if second_right_paddle_y >= HEIGHT - paddle_height:
        second_right_paddle_y = HEIGHT - paddle_height
    if second_right_paddle_y <= 0:
        second_right_paddle_y = 0

    # colision de paletas
    # paleta izquierda
    if second_left_paddle_y == left_paddle_y:
        if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
            if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
                ball_x = left_paddle_x + paddle_width
                dummy_ball_x = left_paddle_x + paddle_width
                ball_vel_x *= -1
                dummy_ball_vel_x *= -1

    if second_left_paddle_y != left_paddle_y:
        if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
            if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
                ball_x = left_paddle_x + paddle_width
                dummy_ball_x = left_paddle_x + paddle_width
                ball_vel_x *= -1
                dummy_ball_vel_x *= -1

        if second_left_paddle_x <= ball_x <= second_left_paddle_x + paddle_width:
            if second_left_paddle_y <= ball_y <= second_left_paddle_y + paddle_height:
                ball_x = left_paddle_x + paddle_width
                dummy_ball_x = left_paddle_x + paddle_width
                ball_vel_x *= -1
                dummy_ball_vel_x *= -1
    
    # paleta derecha
    if second_right_paddle_y == right_paddle_y:
        if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
            if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
                ball_x = right_paddle_x
                dummy_ball_x = right_paddle_x
                ball_vel_x *= -1
                dummy_ball_vel_x *= -1

    if second_right_paddle_y != right_paddle_y:
        if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
                if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
                    ball_x = right_paddle_x
                    dummy_ball_x = right_paddle_x
                    ball_vel_x *= -1
                    dummy_ball_vel_x *= -1
        
        if second_right_paddle_x <= ball_x <= second_right_paddle_x + paddle_width:
            if second_right_paddle_y <= ball_y <= second_right_paddle_y + paddle_height:
                ball_x = right_paddle_x
                dummy_ball_x = right_paddle_x
                ball_vel_x *= -1
                dummy_ball_vel_x *= -1

    # gadgets en accion
    if gadget_pair == 1:
        if left_gadget == 1:
            if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
                if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
                    ball_x = left_paddle_x + paddle_width
                    ball_vel_x *= -3.5
                    dummy_ball_vel_x *= -3.5
                    left_gadget = 0
                    left_gadget_remaining -= 1
        elif left_gadget == 2:
            left_paddle_y = ball_y
            left_gadget = 0
            left_gadget_remaining -= 1

        if right_gadget == 1:
            if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
                if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
                    ball_x = right_paddle_x
                    ball_vel_x *= -3.5
                    dummy_ball_vel_x *= -3.5
                    right_gadget = 0
                    right_gadget_remaining -= 1
        
        elif right_gadget == 2:
            right_paddle_y = ball_y
            right_gadget = 0
            right_gadget_remaining -= 1
    
    # segundo par
    elif gadget_pair == 2:
        if left_gadget == 1:
            if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
                if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
                    ball_x = left_paddle_x + paddle_width
                    dummy_ball_x = left_paddle_x + paddle_width
                    ball_vel_x *= -1
                    dummy_ball_vel_x *= -1
                    dummy_ball_vel_y *= -1
                    left_gadget = 0
                    left_gadget_remaining -= 1
        
        elif left_gadget == 2:
            second_left_paddle_y = left_paddle_y + 200
            left_gadget = 0
            left_gadget_remaining -= 1

        if right_gadget == 1:
            if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
                if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
                    ball_x = right_paddle_x
                    dummy_ball_x = right_paddle_x
                    ball_vel_x *= -1
                    dummy_ball_vel_x *= -1
                    dummy_ball_vel_y *= -1 
                    right_gadget = 0
                    right_gadget_remaining -= 1 
        
        elif right_gadget == 2:
            second_right_paddle_y = right_paddle_y + 200
            right_gadget = 0
            right_gadget_remaining -= 1

    # movimientos
    ball_x += ball_vel_x
    ball_y += ball_vel_y
    dummy_ball_x += dummy_ball_vel_x
    dummy_ball_y += dummy_ball_vel_y
    right_paddle_y += right_paddle_vel
    left_paddle_y += left_paddle_vel
    second_left_paddle_y += second_left_paddle_vel
    second_right_paddle_y += second_right_paddle_vel

    # puntuacion
    font = pygame.font.SysFont('callibri', 32)
    score_1 = font.render("Player_1:" + str(player_1), True, WHITE)
    wn.blit(score_1, (25, 25))
    score_2 = font.render("Player_2:" + str(player_2), True, WHITE)
    wn.blit(score_2, (825, 25))
    gad_left_1 = font.render("Gad Left:" + str(left_gadget_remaining), True, WHITE)
    wn.blit(gad_left_1, (25, 65))
    gad_left_2 = font.render("Gad Left:" + str(right_gadget_remaining), True, WHITE)
    wn.blit(gad_left_1, (825, 65))


    # objetos     
    pygame.draw.circle(wn, PINK, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, RED, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height) )
    pygame.draw.rect(wn, RED, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height) )

    
    pygame.draw.circle(wn, PINK, (dummy_ball_x, dummy_ball_y), radius)

    # segundas paletas
    pygame.draw.rect(wn, RED, pygame.Rect(second_left_paddle_x, second_left_paddle_y, paddle_width, paddle_height) )
    pygame.draw.rect(wn, RED, pygame.Rect(second_right_paddle_x, second_right_paddle_y, paddle_width, paddle_height) )

    # gadget indicacion
    if left_gadget == 1:
        pygame.draw.circle(wn, WHITE, (left_paddle_x + 10, left_paddle_y + 10), 4)
    if right_gadget == 1:
        pygame.draw.circle(wn, WHITE, (right_paddle_x + 10, right_paddle_y + 10), 4)

     # Verificar el ganador y mostrar la pantalla de fin de juego
    winning_font = pygame.font.SysFont('callibri', 100)
    if player_1 >= 3 and not game_over_shown:
        wn.fill(BLACK)
        endscreen = winning_font.render("Ganador PLAYER 1!!!!", True, WHITE)
        wn.blit(endscreen, (200, 250))
        pygame.display.update()
        pygame.time.wait(2000)
        game_over_shown = True
        # Reiniciar el juego
        player_1 = player_2 = 0
        game_over_shown = False
    
    if player_2 >= 3 and not game_over_shown:
        wn.fill(BLACK)
        endscreen = winning_font.render("Ganador PLAYER 2!!!!", True, WHITE)
        wn.blit(endscreen, (200, 250))
        pygame.display.update()
        pygame.time.wait(2000)
        game_over_shown = True
        # Reiniciar el juego
        player_1 = player_2 = 0
        game_over_shown = False
        
    pygame.display.update()
