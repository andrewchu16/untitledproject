from src.attack import Attack
import pygame
import random
import math


class Turret():

    def __init__(self, start):

        self.shoot_speed = 0
        self.bullet_pen = 0

        #sprite
        self.dims = (40, 40)
        self.sprite = pygame.Surface((40, 40))
        self.sprite.fill((0, 0, 69))
        self.body = pygame.Rect((start[0], start[1]), (40, 40))
        self.x, self.y = start[0], start[1]

        # duration, mRange, rRange
        self.attack = Attack(400, 0, 280)
    
    def update(self, enlist):

        best = 999999999
        coords = (-1, -1)

        # attack closest to turret
        for nxt in enlist:
            best = min(best, math.sqrt((self.x-nxt.x)**2+(self.y-nxt.y)**2))
            coords = (nxt.x, nxt.y)
        
        if best <= 300:
            self.attack.update()


    def render(self, screen):
        screen.blit(self.sprite, (self.x, self.y))
