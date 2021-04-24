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

        self.armageddon_status = False
        self.armageddon_cur = 0
        self.arma_counter = 0


    def enter(self):
        #do nothing
        self.armageddon_status = True
        f = open('src/utilities/segmenttree.txt', 'r')
        self.arma = f.readlines()
        f.close()
        pass
  
    def exit(self):

        self.changeTo = None


    def armageddon(self):
        if self.armageddon_cur == 0:
            #start armageddon
            self.arma_counter = 0
        change = False
        y = 0
        if self.arma_counter % 5 == 0:
            for nxt in self.arma:
                y += 15
                relx, rely = 700, 0
                #angle = math.atan2(rely+random.randint(-30, 30), relx+ random.randint(-30, 30))
                angle = math.atan2(rely, relx)
                direction = {
                    "angle": angle,
                    "chx": math.cos(angle),
                    "chy": math.sin(angle)
                }
                if self.armageddon_cur < len(nxt):
                    change = True
                    if nxt[self.armageddon_cur] != " ":
                        self.letter.append(Letter(1, direction, (0, y), nxt[self.armageddon_cur], (255, 245, 255)))
            self.armageddon_cur += 1
            if not change:
                self.armageddon_status = False
        self.arma_counter += 1

    def update(self, keyspressed, keysdown):
        #update things
        if self.armageddon_status:
            self.armageddon()

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
            if nxt.x > 700 or nxt.x < 0 or nxt.y > 700 or nxt.x < 0:
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
            if nxt.x > 700 or nxt.x < 0 or nxt.y > 700 or nxt.x < 0:
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

