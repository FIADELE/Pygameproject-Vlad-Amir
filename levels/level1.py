import pygame
from pygame import Surface
from ourdata import *


def level_1_loop(screen: Surface) -> LevelId:
    clock = pygame.time.Clock()

    while True:
        clock.tick(MAX_FPS)
        screen.fill(BLACK)

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    exit()
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            return LEVEL_0

        pygame.display.flip()
