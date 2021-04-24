import pygame
from src.utilities.palette import col


# class for handling mouse events
class Mouse:
    def __init__(self):
        self.x, self.y = 0, 0
        self.hitbox = (10, 10)
        self.rect = pygame.Rect((self.x, self.y), self.hitbox)
        self.Lclick, self.Rclick = False, False
        self.scroll = 0

    @property
    def pos(self) -> tuple((int, int)):
        return (self.x, self.y)

    def update(self, scroll):
        self.scroll = scroll
        self.x, self.y = pygame.mouse.get_pos()

        mclick: tuple[bool, bool, bool] = pygame.mouse.get_pressed()
        self.Lclick: bool = mclick[0]
        self.Rclick: bool = mclick[2]
        self.rect.x, self.rect.y = self.x, self.y

    def render(self, screen):
        pygame.draw.rect(screen, col["white"], self.rect) #pyagem lies here

cursor = Mouse()