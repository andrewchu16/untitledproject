import pygame
from src.player import Player
from src.letters import Letter
import math
import random

sentences = [
    'Traceback (most recent call last):',
    'ModuleNotFoundError: No module named src',
    'ValueError: math domain error'
]

class PlayState():

    def __init__(self):
        self.changeTo = None
        self.states = {"play", "intro", "pause", "setting"}
        self.player = None
        self.letter = []
        self.cur = 0

        self.player = Player()

        if random.randint(1, 2) == 1:
            self.startx, self.starty = random.choice([0, 600]), random.randint(0, 600)
        else:
            self.startx, self.starty = random.randint(0, 600), random.choice([0, 600])
  
    def enter(self):
        #do nothing
        pass
  
    def exit(self):

        self.changeTo = None
  

    def update(self, keyspressed, keysdown):
        #update things
        if self.cur < len(sentences[0])*15:
            if self.cur % 15 == 0:
                relx, rely = self.player.x-self.startx, self.player.y-self.starty
                angle = math.atan2(rely+random.randint(-30, 30), relx+ random.randint(-30, 30))
                direction = {
                    "angle": angle,
                    "chx": math.cos(angle),
                    "chy": math.sin(angle)
                }
                self.letter.append(Letter(1, direction, (self.startx, self.starty), sentences[0][self.cur//15]))
            self.cur+=1
        self.player.update(keysdown)
        removelist = []

        for nxt in self.letter:
            if self.player.body.colliderect(nxt.body):
                if self.player.hp.hp - 5 >= 0:
                    self.player.hp.hp -= 5
                removelist.append(nxt)
        
        for nxt in self.letter:
            nxt.update()
            if nxt.x > 600 or nxt.x < 0 or nxt.y > 600 or nxt.x < 0:
                removelist.append(nxt)
        for nxt in removelist:
            self.letter.remove(nxt)

    

    def render(self, screen, h: float, w: float):
        self.player.render(screen, (h, w))
        for nxt in self.letter:
            nxt.render(screen, (h, w))

