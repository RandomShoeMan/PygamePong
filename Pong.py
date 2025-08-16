import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

lpaddle = pygame.Surface((20, 100))
lpaddle.fill((255, 0, 0))

rpaddle = pygame.Surface((20, 100))
rpaddle.fill((0, 0, 255))

lpaddle_ypos = 150
lpaddle_speed = 0

rpaddle_ypos = 150
rpaddle_speed = 0

ball = pygame.Surface((20,20))
ball.fill((0, 255, 0))

ball_xpos = 190
ball_ypos = 190

ball_xspeed = 0
ball_yspeed = 0

lscore = 0
rscore = 0

rally_count = 1

while True:
    screen.fill("skyblue")

    text_surface = font.render(f"{lscore} - {rscore}", True, (0, 0, 0))

    if lpaddle_speed == 0:
        lpaddle_ypos = lpaddle_ypos
    else:
        lpaddle_ypos = lpaddle_ypos + lpaddle_speed
    
    if lpaddle_ypos <= 0:
        lpaddle_speed = 0
        lpaddle_ypos = 0

    if lpaddle_ypos >= 300:
        lpaddle_speed = 0
        lpaddle_ypos = 300

    if rpaddle_speed == 0:
        rpaddle_ypos = rpaddle_ypos
    else:
        rpaddle_ypos = rpaddle_ypos + rpaddle_speed
    
    if rpaddle_ypos <= 0:
        rpaddle_speed = 0
        rpaddle_ypos = 0

    if rpaddle_ypos >= 300:
        rpaddle_speed = 0
        rpaddle_ypos = 300

    if ball_xspeed != 0:
        ball_xpos = ball_xpos + ball_xspeed

    if ball_yspeed !=0:
        ball_ypos = ball_ypos + ball_yspeed

    if ball_xpos <= 50 and ball_xpos > 30: 
        if lpaddle_ypos <= ball_ypos <= lpaddle_ypos + 100:
            rally_count = rally_count + 0.1
            ball_xspeed = rally_count

            if ball_ypos - lpaddle_ypos >= 50:
                ball_yspeed = (ball_ypos - lpaddle_ypos) / 100

            if ball_ypos - lpaddle_ypos <= 50:
                ball_yspeed = ((ball_ypos - lpaddle_ypos) * -1) / 100

    if ball_xpos >= 330 and ball_xpos < 350:
        if rpaddle_ypos <= ball_ypos <= rpaddle_ypos + 100:
            rally_count = rally_count + 0.1
            ball_xspeed = rally_count * -1

            if ball_ypos - rpaddle_ypos >= 50:
                ball_yspeed = (ball_ypos - rpaddle_ypos) / 100

            if ball_ypos - rpaddle_ypos <= 50:
                ball_yspeed = ((ball_ypos - rpaddle_ypos) * -1) / 100

    if ball_ypos <= 0:
        ball_yspeed = ball_yspeed * -1

    if ball_ypos >= 380:
        ball_yspeed = ball_yspeed * -1

    if ball_xpos <= 0:
        rscore = rscore + 1

        ball_xspeed = 0
        ball_yspeed = 0
        ball_xpos = 190
        ball_ypos = 190
        rally_count = 1

    if ball_xpos >= 400:
        lscore = lscore + 1

        ball_xspeed = 0
        ball_yspeed = 0
        ball_xpos = 190
        ball_ypos = 190
        rally_count = 1

    screen.blit(text_surface, (200, 20))
    screen.blit(lpaddle, (30,lpaddle_ypos))
    screen.blit(rpaddle, (350,rpaddle_ypos))
    screen.blit(ball, (ball_xpos,ball_ypos))

    if pygame.event.get(pygame.QUIT):
        break

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                lpaddle_speed = -2

            if event.key == pygame.K_s:
                lpaddle_speed = 2

            if event.key == pygame.K_UP:
                rpaddle_speed = -2

            if event.key == pygame.K_DOWN:
                rpaddle_speed = 2

            if ball_xspeed == 0:
                ball_xspeed = 1

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_s):
                lpaddle_speed = 0

            if event.key in (pygame.K_UP, pygame.K_DOWN):
                rpaddle_speed = 0


    clock.tick(144)

    pygame.display.update()

pygame.quit()