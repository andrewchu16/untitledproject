import pygame

class IntroState():

    def __init__(self):
        self.changeTo = None
        self.states = {"start", "intro", "pause", "setting"}
  
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
        if keyspressed != []:
            pass

        for key in 
