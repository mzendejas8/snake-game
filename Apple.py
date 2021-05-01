import pygame
import rgbcolors
import random as ran


class Apple:

    def __init__(self,screen):
        self._screen = screen
        (w, h) = screen.get_size()
        self._dimension = (w/16, h/16)
        self._xpos =ran.randint(0,15)*50
        self._ypos = ran.randint(0,15)*50
        
        
        self._avatar = pygame.Rect((self._xpos,self._ypos), self._dimension)

    

    def apple_reset(self):
        self._xpos =ran.randint(0,13)*50
        self._ypos = ran.randint(0,13)*50

        self._avatar = pygame.Rect((self._xpos,self._ypos), self._dimension)
        print(f'apple is at {self._xpos} and {self._ypos} ')


    def draw(self):
        pygame.draw.rect(self._screen, rgbcolors.red, self._avatar)
    
    