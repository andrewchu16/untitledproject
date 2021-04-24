import pygame
from src.utilities.buttons import Button


start = Button((500, 150), (1, 1), None)
setting = Button((500, 50), (100, 100), None)


class IntroState():

    def __init__(self):
        self.changeTo = None
        self.states = {"play", "intro", "pause", "setting"}
  
    def enter(self):

        def escape1():
            self.changeTo = "play"

        def escape2():
            self.changeTo = "setting"
            
        start.function = escape1
        setting.function = escape2
  
    def exit(self):
        self.changeTo = None
  

    def update(self, keyspressed, keysdown):
        #update things
        start.update()
        setting.update()
    

    def render(self, screen, h: float, w: float):
        start.pos = (w // 2, h // 2 + 50)
        setting.pos = (w // 2, h // 2 - 50)
        start.render(screen)
        setting.render(screen)
