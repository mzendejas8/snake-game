import pygame
import rgbcolors
import random as ran


class Apple:

    def __init__(self, screen, snake):
        self._screen = screen
        (w, h) = screen.get_size()
        self._dimension = (w/16, h/16)
        self._xpos = ran.randint(0, 14)*50
        self._ypos = ran.randint(0, 14)*50
        self._snake = snake
        self._avatar = pygame.Rect((self._xpos, self._ypos), self._dimension)

    def apple_reset(self):
        for i in self._snake._snake_body:
            if i['x'] == self._xpos and i['y'] == self._ypos:
                self._xpos = ran.randint(1, 14)*50
                self._ypos = ran.randint(1, 14)*50
        self._avatar = pygame.Rect((self._xpos, self._ypos), self._dimension)
    
    def draw(self):
        pygame.draw.rect(self._screen, rgbcolors.red, self._avatar)
