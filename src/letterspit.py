import pygame
import math
import random
from src.letters import Letter

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

class Letterspit():
    
    def __init__(self):
        self.cur = 0
        self.ind = random.randint(0, len(sentences)-1)
        self.level = 0

        self.cap = 20
        if random.randint(1, 2) == 1:
            self.x, self.y = random.choice([0, 700]), random.randint(0, 700)
        else:
            self.x, self.y = random.randint(0, 700), random.choice([0, 700])
    
    def update(self, pos, self_pos):
        #update things
        tmp = self.cur
        self.cur+=1
        xx, yy = self.x, self.y
        if self_pos != None:
            xx = self_pos[0]
            yy = self_pos[1]
        if tmp < len(sentences[self.ind])*self.cap-self.cap:
            if tmp % self.cap == 0:
                relx, rely = pos[0]-xx, pos[1]-yy
                angle = math.atan2(rely+random.randint(-30, 30), relx+ random.randint(-30, 30))
                direction = {
                    "angle": angle,
                    "chx": math.cos(angle),
                    "chy": math.sin(angle)
                }
                if sentences[self.ind][tmp//self.cap] != " ":
                    return Letter(self.level, direction, (xx, yy), sentences[self.ind][tmp//self.cap], colours[col[self.ind][tmp//self.cap]])
        else:
            self.cur = 0
            self.ind = random.randint(0, len(sentences)-1)
            if random.randint(1, 2) == 1:
                self.x, self.y = random.choice([0, 700]), random.randint(0, 700)
            else:
                self.x, self.y = random.randint(0, 700), random.choice([0, 700])
            return None
