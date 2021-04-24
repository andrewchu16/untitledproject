import pygame
import random
import math
from src.letters import Letter

class Spitter():

    def __init__(self, level, start):

        self.hp = 15 * level
        self.spit_speed = min(math.ceil(65 - level * 5, 10))
        self.peon_lvl = level
        self.peons = []

        #sprite
        self.dims = (40, 40)
        self.sprite = pygame.Surface((40, 40))
        self.sprite.fill((0, 0, 255))
        self.x, self.y = start[0], start[1]
        self.speed = 2

        #movement bias value
        self.bias_move = random.randint(-100, 100)
    
    def update(self, coords):

        relx, rely = coord[0]-self.x, coords[1]-self.y
        angle = math.atan2(rely+self.bias_move, relx+self.bias_move)
        direction = {
            "angle": angle,
            "chx": math.cos(angle),
            "chy": math.sin(angle)
        }
        moveVecx = direction["chx"] * self.speed
        moveVecy = direction["chy"] * self.speed
        self.x += moveVecx
        self.y += moveVecy
        self.body.x = self.x
        self.body.y = self.y

    def render(self):
        screen.blit(self.sprite, (self.x, self.y))
