import pygame
import math
import random
from src.utilities.mouse import cursor
from src.utilities.healthbar import Healthbar
from src.attack import Attack

class Player():

    def __init__(self):
        self.dims: tuple((int, int)) = (50, 50)
        self.sprite = pygame.Surface((50, 50))
        self.sprite.fill((255,100,180))
        self.x, self.y = 400, 400
        self.body = pygame.Rect((self.x, self.y), (self.w, self.h))

        #health
        self.hp = Healthbar(1000)
        
        #mobility
        self.speed = 4

        self.attack = Attack(1000)

    
    @property
    def w(self):
        return self.dims[0]

    @property 
    def h(self):
        return self.dims[1]

    @property 
    def pos(self):
        return (self.x, self.y)

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
        
        self.x += moveVecx
        self.y += moveVecy
        self.body.x, self.body.y = self.x, self.y

        self.attack.update(self.pos)

        self.hp.update()


    def render(self, screen, dims):
        screen.blit(self.sprite, (self.x, self.y))
        self.hp.render(screen)

        self.attack.render(screen, self.pos)
