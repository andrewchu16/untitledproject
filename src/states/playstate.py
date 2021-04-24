import pygame
from src.player import Player
from src.letters import Letter
import math
import random

class PlayState():

    def __init__(self):
        self.changeTo = None
        self.states = {"play", "intro", "pause", "setting"}
        self.player = None
  
    def enter(self):

        self.player = Player()
        angle = math.atan2(self.player.y, self.player.x)
        direction = {
            "chx": math.cos(angle),
            "chy": math.sin(angle)
        }
        if random.randint(1, 2) == 1:
            startx, starty = random.choice([0, 600]), random.randint(0, 600)
        else:
            startx, starty = random.randint(0, 600), random.choice([0, 600])
        self.letter = Letter(1, direction, (startx, starty))
  
    def exit(self):

        self.changeTo = None
  

    def update(self, keyspressed, keysdown):
        #update things
        self.player.update(keysdown)
        if self.letter != None:
            self.letter.update()
        if self.letter != None:
            if self.letter.x > 600 or self.letter.x < 0 or self.letter.y > 600 or self.letter.x < 0:
                self.letter = None
    

    def render(self, screen, h: float, w: float):
        self.player.render(screen, (h, w))
        if self.letter != None:
            self.letter.render(screen, (h, w))

