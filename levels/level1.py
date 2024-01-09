import pygame
from pygame import Surface
from ourdata import *
import sys
import math


def level_1_loop(screen: Surface) -> LevelId:
    clock = pygame.time.Clock()
    shuttle_size = 100
    shuttle_x = 870
    shuttle_y = 225
    shuttle_speed = 10
    shuttle_angle = 0
    while True:
        clock.tick(MAX_FPS)
        screen.blit(bg1, (0, 0))

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

        if keys[pygame.K_UP]:
            shuttle_x += shuttle_speed * math.cos(angle_radians)
            shuttle_y -= shuttle_speed * math.sin(angle_radians)

        rotated_image = pygame.transform.rotate(carTrack, shuttle_angle)
        new_rect = rotated_image.get_rect(center=carDesert.get_rect(topleft=(shuttle_x, shuttle_y)).center)
        screen.blit(rotated_image, new_rect)

        pygame.display.flip()
