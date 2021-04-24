import pygame
from src.utilities.buttons import Button
from src.states.state import State

start = Button((500, 50), (1, 1), None)
setting = Button((500, 50), (1, 1), None)

'''
Triggered when the player pauses their game, the pausestate will allow the player to quit the program or resume their gameplay
'''
class PauseState(State):

    def __init__(self):
        super().__init__()

    def enter(self):

        def escape1():
            self.changeTo = "play"

        def escape2():
            self.changeTo = "sett"
            
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
