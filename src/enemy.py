import pygame
import random
import math
from src.letters import Letter
from src.letterspit import Letterspit

class Spitter():

    def __init__(self, level, start):

        self.hp = 15 * level
        self.max_health = 15 * level
        self.spit_speed = max(math.ceil(65 - level * 5), 10)
        self.peon_lvl = level
        self.peons = []

        #sprite
        self.dims = (40, 40)
        self.sprite = pygame.Surface((40, 40))
        self.sprite.fill((0, 0, 255))
        self.body = pygame.Rect((start[0], start[1]), (40, 40))
        self.x, self.y = start[0], start[1]
        self.speed = 2

        #movement bias value
        self.bias_move = random.randint(-200, 200)
        self.lettergen = Letterspit()
        self.lettergen.level = level * 2
        print(self.spit_speed)
        self.lettergen.cap = self.spit_speed
    
    def update(self, coords):

        if int(math.sqrt((self.x-coords[0])**2+(self.y-coords[1])**2)) >= 50:
            angle = math.atan2(coords[1]-self.y+self.bias_move, coords[0]-self.x+self.bias_move)
            chx, chy = math.cos(angle), math.sin(angle)
            self.x += chx
            self.y += chy
            self.body.x, self.body.y = self.x, self.y

        res = self.lettergen.update((coords[0], coords[1]), (self.x, self.y))
        if res != None:
            self.peons.append(res)


    def render(self, screen):
        screen.blit(self.sprite, (self.x, self.y))
