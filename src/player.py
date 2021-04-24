import pygame
import math
import random
import asyncio
from time import sleep
from src.utilities.healthbar import Healthbar


class Player():

    def __init__(self):
        self.dims: tuple((int, int)) = (50, 50)
        self.sprite = pygame.Surface((50, 50))
        self.sprite.fill((69, 69, 69))
        self.x, self.y = 400, 400
        self.body = pygame.Rect((self.x, self.y), (self.w, self.h))

        #health
        self.hp = Healthbar(100)
        
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

        self.hp.update()
        

    def render(self, screen, dims):
        screen.blit(self.sprite, (self.x, self.y))
        self.hp.render(screen)
        #self.attack_ranged(screen)
    
    # "r" = ranged, "m" = melee
    def attack(self, screen, style: str):
        if style == "r":
            self.attack_ranged(screen)
        elif style == "m":
            self.attack_melee()

    # moving laser
    def attack_ranged(self, screen):
        for i in range(1, 361, 45):
            radians = math.radians(i)
            slope = math.tan(radians)
            dx = self.x + 20 * (-1 if i < 180 else 1)
            dy = self.y + slope * -20
            pygame.draw.line(screen, (80, 150, 50), (self.x, self.y), (dx, dy), 6)
            pygame.display.update()
