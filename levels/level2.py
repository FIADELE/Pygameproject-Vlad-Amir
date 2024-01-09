import pygame
from pygame import Surface
from ourdata import *
import sys
import math


def level_2_loop(screen: Surface) -> LevelId:
    clock = pygame.time.Clock()
    shuttle_size = 100
    shuttle_x = 680
    shuttle_y = 335
    shuttle_speed = 0
    shuttle_angle = 0

    while True:
        clock.tick(MAX_FPS)
        screen.blit(bg2, (0, 0))

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    exit()
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            return LEVEL_0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and shuttle_x > 0:
            shuttle_angle += 5
        if keys[pygame.K_RIGHT] and shuttle_x < WIDTH - shuttle_size:
            shuttle_angle -= 5

        angle_radians = math.radians(shuttle_angle)

        shuttle_x += shuttle_speed * math.cos(angle_radians)
        shuttle_y -= shuttle_speed * math.sin(angle_radians)

        if keys[pygame.K_UP] and shuttle_speed < 16:
            shuttle_speed += 0.8
        if keys[pygame.K_DOWN] and 16 > shuttle_speed > -6:
            shuttle_speed -= 0.6
        if shuttle_speed > 0:
            shuttle_speed -= 0.2
        if 0.4 > shuttle_speed > -0.4:
            shuttle_speed = 0

        rotated_image = pygame.transform.rotate(carDesert, shuttle_angle)
        new_rect = rotated_image.get_rect(center=carDesert.get_rect(topleft=(shuttle_x, shuttle_y)).center)
        screen.blit(rotated_image, new_rect)

        pygame.display.flip()
