import pygame
from pygame import Surface, Vector2
from constants import *
from my_utilities import Object, Button, objects


def level_0_loop(screen: Surface) -> LevelId:
    def start() -> None:
        print('Start pressed')

    clock = pygame.time.Clock()

    win_size = screen.get_size()

    start_button = Button('Start_Button',
                          './textures/Start_Button_01.png',
                          './textures/Start_Button_02.png',
                          './textures/Start_Button_03.png')
    start_button.set_function(LEFT_BUTTON, start)
    start_button.set_alignment(MIDDLE_CENTER)
    start_button.move(win_size[0] / 2, win_size[1] / 2 - start_button.h() / 2 - 4)

    exit_button = Button('Exit_Button',
                         './textures/Exit_Button_01.png',
                         './textures/Exit_Button_02.png',
                         './textures/Exit_Button_03.png')
    exit_button.set_function(LEFT_BUTTON, exit)
    exit_button.set_alignment(MIDDLE_CENTER)
    exit_button.move(win_size[0] / 2, win_size[1] / 2 + exit_button.h() / 2 + 4)

    objects.start_objects()

    while True:
        clock.tick(MAX_FPS)
        screen.fill(BLACK)
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
                case pygame.MOUSEMOTION:
                    objects.check_mouse_move(mouse_pos)
                case pygame.MOUSEBUTTONDOWN:
                    objects.check_mouse_down(event.button)
                case pygame.MOUSEBUTTONUP:
                    objects.check_mouse_up(event.button)

        objects.update_objects()

        objects.draw_objects(screen)

        pygame.display.flip()
