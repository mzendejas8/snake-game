
import pygame
from snakeplayer import *
from scene import *
from Apple import *
import time


def display_info():

    """ Print out information about the"""
    """display driver and video information."""
    print('The display is using the "{}" driver.'.format(pygame.display.get_driver()))
    print('Video Info:')
    print(pygame.display.Info())


def main():

    print('hello world!')
    pygame.init()
    display_info()
    window_size = (800, 800)

    screen = pygame.display.set_mode(window_size)
    title = 'Snake++'
    pygame.display.set_caption(title)
    snake = SnakePlayer(screen)
    apple = Apple(screen, snake)
    scene_list = [TitleScene(screen, title, rgbcolors.green, 72), InstructionScene(screen, title,rgbcolors.grey, 72), GameLevel(screen, snake, apple)
    , GameOverScreen(screen,'Game Over',rgbcolors.red, 72)]

    for scene in scene_list:
        scene.play_music()
        while scene.is_valid():
            for e in pygame.event.get():
                scene.process_event(e)
            scene.update()
            scene.draw()
            pygame.display.update()
        scene.stop_music()
    pygame.quit()
