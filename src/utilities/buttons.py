import pygame
from src.utilities.mouse.py import cursor

class Button:


    def __init__(self, dimensions: tuple, position: tuple, function):

        #make a Button
    
    self.dims = dimensions
    self.pos = position

    self.rect = pygame.Rect(self.pos, self.dims)

    self.color = (30, 30, 35)

    self.function = function


    def update(self):

        if cursor.rect.colliderect(self.rect):
            self.color = (50, 50, 70)

            if cursor.Lclick:
                self.color = (90, 90, 120)

                self.function()
    

    def render(self, screen):

        pygame.draw.rect(screen, self.color, self.rect)

        screen.blit