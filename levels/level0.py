import os
import sys

import pygame
from pygame import Surface
from ourdata import *


def get_cell(mouse_pos):
    if 630 <= mouse_pos[0] <= 630 + 200 and 318 < mouse_pos[1] < 318 + 125:
        print('Level1')
        return LEVEL_1
    if 850 <= mouse_pos[0] <= 850 + 200 and 318 < mouse_pos[1] < 318 + 125:
        print('Level2')
        return LEVEL_2
    elif width - 216 <= mouse_pos[0] <= width - 40 and height - 150 < mouse_pos[1] < height - 50:
        exit()


def level_0_loop(screen: Surface) -> LevelId:
    def start() -> None:
        print('Start pressed')

    clock = pygame.time.Clock()
    win_size = screen.get_size()

    while True:
        clock.tick(MAX_FPS)
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_focused():
            pygame.mouse.set_visible(False)
            x, y = pygame.mouse.get_pos()
            screen.blit(mouse, (x, y))
            pygame.display.flip()
        else:
            pygame.display.flip()
        image1 = pygame.transform.scale(image, size)
        screen.blit(image1, (0, 0))
        screen.blit(level11, (
            width // 2 - level11.get_rect().size[0] // 2 - 110, height // 2 - level11.get_rect().size[1] // 2 - 100))
        screen.blit(level21,
                    (width // 2 - level21.get_rect().size[0] // 2 + 110,
                     height // 2 - level21.get_rect().size[1] // 2 - 100))
        screen.blit(exit2, (width - 216, height - 150))
        for event in pygame.event.get():
            match event.type:
                case pygame.MOUSEBUTTONDOWN:
                    return get_cell(event.pos)
                case pygame.QUIT:
                    pygame.quit()
                    exit()
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            return LEVEL_0
                        case pygame.K_1:
                            return LEVEL_1
                        case pygame.K_2:
                            return LEVEL_2


pygame.init()
all_sprites = pygame.sprite.Group()
size = width, height = 1680, 960
screen = pygame.display.set_mode(size)
