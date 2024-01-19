import pygame

from levels import *
from ourdata import *

pygame.init()

WIN_SIZE = WIDTH, HEIGHT

screen = pygame.display.set_mode(WIN_SIZE)
icon = pygame.image.load('pics/Car1_desert.png')
pygame.display.set_icon(icon)

pygame.display.set_caption('Racing game for 2 players')

level_loops = (level_0_loop, level_1_loop, level_2_loop, level_3_loop)
current_level = 0

while True:
    current_level = level_loops[current_level](screen)
