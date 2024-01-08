import pygame

from levels import *

pygame.init()

WIN_SIZE = (900, 900)
screen = pygame.display.set_mode(WIN_SIZE)

pygame.display.set_caption('Baller')

level_loops = (level_0_loop, level_1_loop, level_2_loop, level_3_loop)
current_level = 2

while True:
    current_level = level_loops[current_level](screen)
