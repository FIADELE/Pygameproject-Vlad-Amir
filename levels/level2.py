import pygame
from pygame import Surface
from ourdata import *
import sys
import math


def level_2_loop(screen: Surface) -> LevelId:
    clock = pygame.time.Clock()
    shuttle_size = 100
    shuttle_x = 530
    shuttle_y = 220
    shuttle_speed = 0
    shuttle_angle = 0

    shuttle_x_blue = 530
    shuttle_y_blue = 300
    shuttle_speed_blue = 0
    shuttle_angle_blue = 0

    clock = pygame.time.Clock()

    red_wins = False
    run = True
    counter, text = float(0), '0'
    pygame.time.set_timer(pygame.K_z, 100)
    font = pygame.font.SysFont('Consolas', 60)
    win_font = pygame.font.SysFont('Consolas', 120)

    f = open('record.txt', 'r')
    lines = f.read().split()
    record2 = float(lines[1])
    f.close()
    while True:
        clock.tick(MAX_FPS)
        screen.blit(bg2, ((WIDTH - 2560) / 2, (HEIGHT - 1280) / 2))
        # Level engine
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    exit()
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            return LEVEL_0
                case pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                case pygame.K_z:
                    if run:
                        counter += 0.1
                        text = str(counter)

        # Car engine
        if run:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and shuttle_x > 0:
                shuttle_angle += 5
            if keys[pygame.K_RIGHT] and shuttle_x < WIDTH - shuttle_size:
                shuttle_angle -= 5

            if keys[pygame.K_UP]:  # Car control
                shuttle_speed += 0.8
            if keys[pygame.K_DOWN] and shuttle_speed > -6:
                shuttle_speed -= 0.6

        shuttle_speed = shuttle_speed * 0.95

        angle_radians = math.radians(shuttle_angle)  # Car coordinates

        shuttle_x += shuttle_speed * math.cos(angle_radians)
        shuttle_y -= shuttle_speed * math.sin(angle_radians)

        # Car rendering

        rotated_image = pygame.transform.rotate(car_Desert_red, shuttle_angle)
        new_rect = rotated_image.get_rect(center=car_Desert_red.get_rect(topleft=(shuttle_x, shuttle_y)).center)
        screen.blit(rotated_image, new_rect)

        if 500 < shuttle_x < 540 and 180 < shuttle_y < 330 and counter > 7:  # Finish coordinates
            run = False
            red_wins = True
            if record2 > counter:
                f = open('record.txt', 'wt')
                f.write(lines[0] + '\n' + str(counter))
                f.close()

        # Blue car

        # Car engine
        if run:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and shuttle_x > 0:
                shuttle_angle_blue += 5
            if keys[pygame.K_d] and shuttle_x < WIDTH - shuttle_size:
                shuttle_angle_blue -= 5

            if keys[pygame.K_w]:  # Car control
                shuttle_speed_blue += 0.8
            if keys[pygame.K_s] and shuttle_speed > -6:
                shuttle_speed_blue -= 0.6

        shuttle_speed_blue = shuttle_speed_blue * 0.95

        angle_radians_blue = math.radians(shuttle_angle_blue)  # Car coordinates

        shuttle_x_blue += shuttle_speed_blue * math.cos(angle_radians_blue)
        shuttle_y_blue -= shuttle_speed_blue * math.sin(angle_radians_blue)

        # Car rendering

        rotated_image = pygame.transform.rotate(car_Desert_blue, shuttle_angle_blue)
        new_rect = rotated_image.get_rect(
            center=car_Desert_blue.get_rect(topleft=(shuttle_x_blue, shuttle_y_blue)).center)
        screen.blit(rotated_image, new_rect)

        if 500 < shuttle_x_blue < 540 and 180 < shuttle_y_blue < 330 and counter > 7:  # Finish coordinates
            run = False
            red_wins = False
            if record2 > counter:
                f = open('record.txt', 'wt')
                f.write(lines[0] + '\n' + str(counter))
                f.close()

        # Timer

        if float(record2) > 10:
            screen.blit(font.render('Record: ' + str(record2), True, (0, 0, 0)), (WIDTH - 397, 0))
        else:
            screen.blit(font.render('Record: ' + str(record2), True, (255, 255, 0)), (WIDTH - 363, 0))
        if float(text) > 10:
            screen.blit(font.render(text, True, (0, 0, 0)), (WIDTH - 130, 70))
        else:
            screen.blit(font.render(text, True, (0, 0, 0)), (WIDTH - 100, 70))

        # Win window

        if not run:
            if red_wins:
                screen.blit(win_font.render('The RED wins!', True, (0, 0, 0)), (WIDTH / 3.9, HEIGHT - 100))
            else:
                screen.blit(win_font.render('The BLUE wins!', True, (0, 0, 0)), (WIDTH / 4.3, HEIGHT - 100))

        pygame.display.flip()
