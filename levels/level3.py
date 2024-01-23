import pygame
from pygame import Surface
from ourdata import *
import sqlite3


def get_cell(mouse_pos):
    if 630 <= mouse_pos[0] <= 630 + 200 and 318 < mouse_pos[1] < 318 + 125:
        return LEVEL_1
    if 850 <= mouse_pos[0] <= 850 + 200 and 318 < mouse_pos[1] < 318 + 125:
        return LEVEL_2
    elif width - 216 <= mouse_pos[0] <= width - 40 and height - 150 < mouse_pos[1] < height - 50:
        exit()


def level_3_loop(screen: Surface) -> LevelId:
    clock = pygame.time.Clock()

    def start() -> None:
        print('Start pressed')

    clock = pygame.time.Clock()
    win_size = screen.get_size()

    while True:
        clock.tick(MAX_FPS)
        if pygame.mouse.get_focused():
            pygame.mouse.set_visible(False)
            x, y = pygame.mouse.get_pos()
            screen.blit(mouse, (x, y))
            pygame.display.flip()
        else:
            pygame.display.flip()
        image1 = pygame.transform.scale(image, size)
        screen.blit(image1, (0, 0))
        screen.blit(exit2, (width - 216, height - 150))
        font = pygame.font.SysFont('Consolas', 60)
        win_font = pygame.font.SysFont('Consolas', 120)
        screen.blit(win_font.render('RECORDS', True, (255, 255, 255)), (600, 100))
        screen.blit(font.render('Level 1:', True, (200, 200, 200)), (200, 200))
        screen.blit(font.render('Level 2:', True, (200, 200, 200)), (WIDTH - 500, 200))
        screen.blit(font.render(f'{round(result2, 2)} Sec', True, (255, 255, 255)), (WIDTH - 450, 250))
        screen.blit(font.render(f'{round(result1, 2)} Sec', True, (255, 255, 255)), (250, 250))
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


pygame.init()
all_sprites = pygame.sprite.Group()
size = width, height = 1680, 960
screen = pygame.display.set_mode(size)
