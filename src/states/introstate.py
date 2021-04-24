import pygame
from src.utilities.buttons.py import buttons

start = Button((500, 50), (1, 1), None)
turn = Button((500, 50), (1, 1), None)

class IntroState():

    def __init__(self):
        self.changeTo = None
        self.states = {"play", "intro", "pause", "setting"}
  
    def enter(self):

        def escape1():
            self.changeTo = "play"

        def escape2():
            self.changeTo = "turn"
            
        start.function = escape1
        turn.function = escape2
  
    def exit(self):
        self.changeTo = None
  

    def update(self, keyspressed, keysdown):
        #update things
        start.update()
        turn.update()
    

    def render(self, screen, h: float, w: float):
        start.pos = (w // 2, h // 2 + 50)
        turn.pos = (w // 2, h // 2 - 50)
        start.render(screen)
        turn.render(screen)
