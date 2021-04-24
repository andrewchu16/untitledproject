import pygame
import math
import random

class Letter():

    def __init__(self, health, direction, start):
        self.dims: tuple((int, int)) = (20, 20)
        self.sprite = pygame.Surface((20, 20))
        self.sprite.fill((69, 69, 69))
        self.x, self.y = start[0], start[1]
        self.body = pygame.Rect((self.x, self.y), (self.w, self.h))

        #health
        self.hp = health
        
        #mobility
        self.speed = 2
        self.direction = direction

    
    @property
    def w(self):
        return self.dims[0]

    @property 
    def h(self):
        return self.dims[1]

    def update(self):

        moveVecx = self.direction["chx"] * self.speed
        moveVecy = self.direction["chy"] * self.speed
        
        self.body.move_ip(moveVecx, moveVecy)
        self.x = self.body.x
        self.y = self.body.y
        

    def render(self, screen, dims):
        screen.blit(self.sprite, (self.x, self.y))
