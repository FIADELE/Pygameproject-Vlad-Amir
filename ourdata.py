import pygame.cursors
from pygame import Color
from math import pi as PI
import sys
import os

# Settings

MAX_FPS = 120
MIN_DT = 1.0 / MAX_FPS
SIZE = WIDTH, HEIGHT = 1680, 960

# Level IDs

LevelId = int
LEVEL_0 = 0
LEVEL_1 = 1
LEVEL_2 = 2
LEVEL_3 = 3

# Pictures

bg1 = pygame.image.load('./pics/Track.png')
bg1 = pygame.transform.scale(bg1, SIZE)

bg2 = pygame.image.load('./pics/Desert.png')
car_Track_re = pygame.image.load('pics/Car1_track.png')
car_Track_red = pygame.transform.scale(car_Track_re, (40, 23))
car_Desert_re = pygame.image.load('pics/Car1_desert.png')
car_Desert_red = pygame.transform.scale(car_Desert_re, (40, 23))
car_Track_blu = pygame.image.load('pics/Car2_track.png')
car_Track_blue = pygame.transform.scale(car_Track_red, (40, 23))
car_Desert_blu = pygame.image.load('pics/Car2_desert.png')
car_Desert_blue = pygame.transform.scale(car_Desert_blu, (40, 23))
icon = pygame.image.load('pics/Car1_desert.png')
pygame.display.set_icon(icon)


def load_image(name, colorkey=None):
    fullname = os.path.join('pics', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    return pygame.image.load(fullname)


mouse = load_image('mouse_car.png')
image = load_image('Background.png')
level1 = load_image('Level-1.png')
level11 = pygame.transform.scale(level1, (200, 125))
level2 = load_image('Level-2.png')
level21 = pygame.transform.scale(level2, (200, 125))
exit1 = load_image('Exit1.png')
exit2 = pygame.transform.scale(exit1, (175, 100))

# Colors

BLACK = Color(0, 0, 0)
DARK_GREY = Color(63, 63, 63)
GREY = Color(127, 127, 127)
LIGHT_GREY = Color(191, 191, 191)
WHITE = Color(255, 255, 255)

RED = Color(255, 0, 0)
ORANGE = Color(255, 127, 63)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
LIGHT_BLUE = Color(127, 191, 255)
BLUE = Color(0, 0, 255)
PURPLE = Color(127, 63, 255)
PINK = Color(255, 127, 191)
BROWN = Color(127, 63, 0)

# Constants

PI = PI
DEG2RAD = PI / 180.0
SQRT_TWO = 2 ** 0.5
SQRT_THREE = 3 ** 0.5

# Alignments

Alignment = tuple[float, float]
LEFT_TOP, MIDDLE_TOP, RIGHT_TOP = (0.0, 0.0), (0.5, 0.0), (1.0, 0.0)
LEFT_CENTER, MIDDLE_CENTER, RIGHT_CENTER = (0.0, 0.5), (0.5, 0.5), (1.0, 0.5)
LEFT_BOTTOM, MIDDLE_BOTTOM, RIGHT_BOTTOM = (0.0, 1.0), (0.5, 1.0), (1.0, 1.0)

# Cursors

DEFAULT_CURSOR = pygame.cursors.tri_left
POINTED_CURSOR = pygame.cursors.broken_x

# Mouse buttons

LEFT_BUTTON = pygame.BUTTON_LEFT
RIGHT_BUTTON = pygame.BUTTON_RIGHT
MIDDLE_BUTTON = pygame.BUTTON_MIDDLE
WHEEL_UP_BUTTON = pygame.BUTTON_WHEELUP
WHEEL_DOWN_BUTTON = pygame.BUTTON_WHEELDOWN
MouseButton = LEFT_BUTTON | RIGHT_BUTTON | MIDDLE_BUTTON | WHEEL_UP_BUTTON | WHEEL_DOWN_BUTTON
