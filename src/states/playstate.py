import pygame
from src.utilities.buttons import Button
from src.player import Player

class PlayState():

    def __init__(self):
        self.changeTo = None
        self.states = {"play", "intro", "pause", "setting"}
        self.player = None
  
    def enter(self):

        self.player = Player()
  
    def exit(self):

        self.changeTo = None
  

    def update(self, keyspressed, keysdown):
        #update things
        self.player.update(keysdown)
    

    def render(self, screen, h: float, w: float):
        self.player.render(screen, (h, w))

