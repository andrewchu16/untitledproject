import pygame
from src.player import Player
from src.letters import Letter
import math
import random

sentences = [
    'Traceback(mostrecentcalllast):',
    'ModuleNotFoundError:Nomodulenamedsrc',
    'ValueError:mathdomainerror',
    'java.lang.instrumentASSERTIONFAILED',
    'TeeLllEee',
    'WaaWaa',
    'MmmmLllEee',
    'RrrTeeEee',
    'NameError:nameYrHacksisnotdefined',
    'RecursionError:maximumrecursiondepthexceeded',
    'ZeroDivisionError:divisionbyzero',
    'TypeError:Cantconvertintobjecttostrimplicitly',
    '#defineintlonglong',
    'SegmentationFault',
    'errorC2440:static_cast:cannotconvertfromDerived*toBase*'
]

col = [
    '444444444444444444444444444444', '444444444444444444444444444444444444', '44444444444444444444444444', 
    '44444444444444444444444444444444444', '000000000', '111111', '2222222222', '222222222', '444444444444444444444444444444444',
    '44444444444444444444444444444444444444444444','44444444444444444444444444444444', '444444444444444444444555444444445554444444444',
     '00000000000000000','11111111111111111', '3333333333333333333333333333333333333333333333333333333'
]
colours = {
    '0': (200,200,200), # light grey
    '1': (255,0,0), # red
    '2': (255,100,10), #orange
    '3': (180,255,100), #lime green
    '4': (255,255,255), #white
    '5': (240,0,255) #purple
}
class PlayState():

    def __init__(self):
        self.changeTo = None
        self.states = {"play", "intro", "pause", "setting"}
        self.player = None
        self.letter = []
        self.cur = 0
        self.ind = random.randint(0, len(sentences)-1)

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
        if self.cur < len(sentences[self.ind])*20-20:
            if self.cur % 20 == 0:
                relx, rely = self.player.x-self.startx, self.player.y-self.starty
                angle = math.atan2(rely+random.randint(-30, 30), relx+ random.randint(-30, 30))
                direction = {
                    "angle": angle,
                    "chx": math.cos(angle),
                    "chy": math.sin(angle)
                }
                if sentences[self.ind][self.cur//20] != " ":
                    self.letter.append(Letter(1, direction, (self.startx, self.starty), sentences[self.ind][self.cur//20], colours[col[self.ind][self.cur//20]]))
            self.cur+=1
        else:
            self.cur = 0
            self.ind = random.randint(0, len(sentences)-1)
            if random.randint(1, 2) == 1:
                self.startx, self.starty = random.choice([0, 600]), random.randint(0, 600)
            else:
                self.startx, self.starty = random.randint(0, 600), random.choice([0, 600])
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

