import pygame
from mouse import cursor
from palette import col


class Button:

    def __init__(self, dimensions: tuple[int, int], position: tuple[int, int], function):
        #make a Button
    
        self.dims = dimensions
        self.pos = position

        self.rect = pygame.Rect(self.pos, self.dims)

        self.color = (30, 30, 35)

        self.function = function

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
        if cursor.rect.colliderect(self.rect):
            self.color = col["cyan"]

            if cursor.Lclick:
                self.color = col["blue"]

                self.function()
    

    def render(self, screen):

        pygame.draw.rect(screen, self.color, self.rect)
