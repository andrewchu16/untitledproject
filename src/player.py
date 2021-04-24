import pygame
import math
import random


class Player(pygame.sprite.sprite):

    def __init__(self):
        self.dims: tuple((int, int)) = (50, 50)
        self.sprite = pygame.Surface((50, 50))
        self.x, self.y = 50, 50
        self.body = pygame.Rect((self.x, self.y), (self.dims[0], self.dims[1]))
    
    @property
    def w(self):
        return self.dims[0]

    @property 
    def h(self):
        return self.dims[1]
    