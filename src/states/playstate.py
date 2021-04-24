import pygame
from src.player import Player


class PlayState():

    def __init__(self):
        self.changeTo = None
        self.states = {"play", "intro", "pause", "setting"}
        self.player = None
  
    def enter(self):

        self.player = Player()
        angle = math.atan2(player.y, player.x)
        direction = {
            "chx": math.cos(angle)
            "chy": math.sin(angle)
        }
        self.letter = Letter(1, direction)
  
    def exit(self):

        self.changeTo = None
  

    def update(self, keyspressed, keysdown):
        #update things
        self.player.update(keysdown)
        self.letter.update()
    

    def render(self, screen, h: float, w: float):
        self.player.render(screen, (h, w))
        self.letter.render(screen, (h, w))

