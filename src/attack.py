import pygame
import math
from src.utilities.mouse import cursor


class Attack:
    def __init__(self, duration: int, mRange=100, rRange=380):
        self.duration = duration  # how long it takes to complete attack
        self.counter = 0  # progress into attack
        self.mode = ""
        self.target: list[int, int] = [0, 0]
        self.start: list[int, int] = [0, 0]

        # ranges for the attacks
        self.mRange = mRange 
        self.rRange = rRange

        self.slope: float = 0.0
        self.distance = 0.0

        self.rect = pygame.Rect((0, 0), (20, 20))

    # ppos: player's position as a list/tuple
    def update(self, ppos):
        if cursor.Lclick and self.counter == 0:
            self.counter = 1
            self.mode = "m"
            self.target = [cursor.x, cursor.y]
            self.start = ppos[:]
            # self.distance = math.sqrt((ppos[0] - cursor.x)**2 + (ppos[1] - cursor.y)**2)
            self.slope = None if ppos[0] == cursor.x else (ppos[1] - cursor.y) / (ppos[0] - cursor.x)
        elif cursor.Rclick and self.counter == 0:
            self.counter = 1
            self.mode = "r"
            self.target = [cursor.x, cursor.y]
            self.start = ppos[:]
            # self.distance = math.sqrt((ppos[0] - cursor.x)**2 + (ppos[1] - cursor.y)**2)
            self.slope = None if ppos[0] == cursor.x else (ppos[1] - cursor.y) / (ppos[0] - cursor.x)

        if self.counter != 0 and self.mode == "r":
            self.shoot()
        elif self.counter != 0 and self.mode == "m":
            self.swing()


    def render(self, screen, ppos):
        if self.mode == "r":
            if self.slope != None:
                x2 = (self.rRange * self.counter / self.duration) / math.sqrt(self.slope**2 + 1) * (-1 if self.target[0] < self.start[0] else 1) + self.start[0]
                y2 = self.slope * (x2 - self.target[0]) + self.target[1]

                # if self.target[0] < self.start[0]: y2 = -y2
                self.rect.x, self.rect.y = x2, y2
                pygame.draw.rect(screen, (180, 50, 50), self.rect)
            else:
                print("rendering None slope range attack...", self.counter)
        elif self.mode == "m":
            print("rendering melee attack...", self.counter)

    # ranged attack
    def shoot(self):
        self.counter += 30

        if self.counter > self.duration:
            self.counter = 0
            self.mode = ""

    # melee attack
    def swing(self):

        self.counter += 80

        if self.counter > self.duration:
            self.counter = 0
            self.mode = ""