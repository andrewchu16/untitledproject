import pygame
import math
import random


<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
class Player():

    def __init__(self):
        self.dims: tuple((int, int)) = (50, 50)
        self.sprite = pygame.Surface((50, 50))
        self.sprite.fill((69, 69, 69))
        self.x, self.y = 50, 50
        self.body = pygame.Rect((self.x, self.y), (self.w, self.h))

        #health
        self.hp = 1000
        
        #mobility
        self.speed = 2

    
    @property
    def w(self):
        return self.dims[0]

    @property 
    def h(self):
        return self.dims[1]

    def update(self, keysdown: list):

        moveVecx = 0
        moveVecy = 0
        if keysdown[pygame.K_s]:
            moveVecy += self.speed
        if keysdown[pygame.K_w]:
            moveVecy += -self.speed
        if keysdown[pygame.K_a]:
            moveVecx += -self.speed
        if keysdown[pygame.K_d]:
            moveVecx += self.speed
        
        if abs(moveVecx) == abs(moveVecy) and moveVecx != 0:
            diag = math.sqrt(2)
            moveVecx = round(moveVecx/diag, 2)
            moveVecy = round(moveVecy/diag, 2)
        
        self.body.move_ip(moveVecx, moveVecy)
        self.x = self.body.x
        self.y = self.body.y
        

    def render(self, screen, dims):
        screen.blit(self.sprite, (self.x, self.y))
