import pygame
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

class LetterSpit():
    
    def __init__(self):
        self.cur = 0
        self.ind = random.randint(0, len(sentences)-1)

        self.cap = 20;
    
    def update(self, pos, self_pos):
        #update things
        if self.cur < len(sentences[self.ind])*20-20:
            if self.cur % 20 == 0:
                relx, rely = pos[0]-self_pos[0], pos[1]-self_pos[1]
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
