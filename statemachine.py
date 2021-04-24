import pygame
from src.states import *


class StateMachine:
  
  def __init__(self):
        self.states = {
            "start": 0,
            "intro": 0,
            "pause": 0,
            "setting": 0,
        }
    self.currentstates["start"]

    self.currentstate.enter()
  
    def change(self, nxt):
        self.currentstate.exit()
        self.currentstate = self.states[nxt]
        self.currentstate.enter()
  
    def update(self, keyspressed, keysdown):
        self.currentstate.update(keyspressed, keysdown)
        if self.currentstate.changeTo != None:
            self.change(self.currentstate.changeTo)
            
            
    def render(self, screen, h, w):
        self.currentstate.render(screen, h, w)
        cursor.render(screen)