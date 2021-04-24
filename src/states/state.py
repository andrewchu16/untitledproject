import pygame
from src.player import Player
from src.letters import Letter

class State():

    def __init__(self):
        self.changeTo = None
        self.states = {"play", "intro", "pause", "setting"}
  
    def exit(self):
        self.changeTo = None
