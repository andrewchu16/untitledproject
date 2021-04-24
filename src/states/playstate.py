import pygame
from src.player import Player
from src.letters import Letter
from src.letterspit import Letterspit
from src.enemy import Spitter
import math
import random

class PlayState():

    def __init__(self):
        self.changeTo = None
        self.states = {"play", "intro", "pause", "setting"}
        self.player = None
        self.letter = []

        self.player = Player()

        self.lettergen = Letterspit()
        self.lettergen.cap = 20
        self.enemylist = [Spitter(1, (50, 50))]

    def enter(self):
        #do nothing
        pass
  
    def exit(self):

        self.changeTo = None
  

    def update(self, keyspressed, keysdown):
        #update things
        res = self.lettergen.update((self.player.x, self.player.y), None)
        if res != None:
            self.letter.append(res)
        self.player.update(keysdown)
        removelist = []

        for nxt in self.letter:
            if self.player.body.colliderect(nxt.body):
                if self.player.hp.hp - 5 >= 0:
                    self.player.hp.hp -= 5
                removelist.append(nxt)
            if self.player.attack.body.colliderect(nxt.body):
                removelist.append(nxt)
        
        for nxt in self.letter:
            nxt.update()
            if nxt.x > 600 or nxt.x < 0 or nxt.y > 600 or nxt.x < 0:
                removelist.append(nxt)
        for nxt in removelist:
            if nxt in self.letter:
                self.letter.remove(nxt)

        for go in self.enemylist:
            for nxt in go.peons:
                nxt.update()
                if self.player.body.colliderect(nxt.body):
                    if self.player.hp.hp - 5 >= 0:
                        self.player.hp.hp -= 5
                    removelist.append(nxt)
            if nxt.x > 600 or nxt.x < 0 or nxt.y > 600 or nxt.x < 0:
                removelist.append(nxt)
            for nxt in removelist:
                if nxt in go.peons:
                    go.peons.remove(nxt)
            go.update((self.player.x, self.player.y))

    def render(self, screen, h: float, w: float):
        self.player.render(screen, (h, w))
        for nxt in self.letter:
            nxt.render(screen, (h, w))
        for nxt in self.enemylist:
            for go in nxt.peons:
                go.render(screen, (h, w))
            nxt.render(screen)

