import pygame
from src.utilities.mouse import cursor
from src.utilities.palette import col


class Button:
    def __init__(self, dimensions: tuple((int, int)), position: tuple((int, int)), function):
        #make a Button
    
        self.dims = dimensions
        self.pos = position

        self.rect = pygame.Rect(self.pos, self.dims)

        self.color = (30, 30, 35)
        self.offHover = col["blue"]
        self.onHover = col["cyan"]

        self.function = function
    
    def setColor(self, offHover=None, onHover=None):
        self.offHover = offHover if offHover else self.offHover 
        self.onHover = onHover if onHover else self.onHover        

    @property
    def x(self):
        return pos[0]

    @property
    def y(self):
        return pos[1]

    @property
    def w(self):
        return dims[0]
    
    @property
    def h(self):
        return dims[1]

    def update(self):
        self.color = self.offHover
        if cursor.rect.colliderect(self.rect):
            self.color = self.onHover

            if cursor.Lclick:

                self.function()
    

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    
    def __str__(self):
        return f"Button({self.dims}, {self.pos}, self.function)"
