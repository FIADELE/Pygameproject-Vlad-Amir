import pygame
from pygame import Surface, Vector2
from ourdata import *


def level_0_loop(screen: Surface) -> LevelId:
    def start() -> None:
        print('Start pressed')

    clock = pygame.time.Clock()

    win_size = screen.get_size()

    while True:
        clock.tick(MAX_FPS)
        screen.fill(WHITE)
        mouse_pos = pygame.mouse.get_pos()

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
