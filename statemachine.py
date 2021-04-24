import pygame
from src.states import *


class StateMachine:
  
    def __init__(self):
        self.states = {
            "play": playstate.PlayState(),
            "intro": introstate.Introstate(),
            "pause": pausestate.PauseState(),
            "setting": settingstate.SettingState()
        }
        self.currentstates = ["start"]
        
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