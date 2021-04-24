import pygame
import math
# from src.utilities.mouse import cursor


class Attack:
    def __init__(self, duration=1000, mRange=100, rRange=380):
        self.duration = duration  # how long it takes to complete attack
        self.counter = 0  # progress into attack
        self.mode = ""
        self.target: list[int, int] = [0, 0]
        self.start: list[int, int] = [0, 0]

        # ranges for the attacks
        self.mRange = mRange 
        self.rRange = rRange

        self.slope: float = 0.0

        self.body = pygame.Rect((0, 0), (20, 20))

    @property 
    def pos(self) -> tuple((int, int)): 
        return (self.body.x, self.body.y)

    # ppos: player's position as a list/tuple
    def update(self, start: tuple((int, int)), target: tuple((int, int)), mode: str):
        """
        [args]
        start: where the attack originates from
        end: the direction the attack is aimed
        mode: melee or ranged
        """
        if self.counter == 0 and mode:
            self.counter = 1
            self.mode =  mode
            self.target = target[:]
            self.start = start[:]
            self.slope = None if start[0] == target[0] else (start[1] - target[1]) / (start[0] - target[0])


        if self.counter != 0 and self.mode == "r":
            self.shoot()
        elif self.counter != 0 and self.mode == "m":
            self.swing()


    def render(self, screen):
        if self.mode == "r":
            pygame.draw.rect(screen, (180, 50, 50), self.body)

        elif self.mode == "m":
            print("rendering melee attack...", self.counter)

    # ranged attack
    def shoot(self):
        distance = self.rRange * self.counter / self.duration
        if self.slope != None:
            # calculate y using x
            if abs(self.slope) < 10:
                self.body.x = distance / math.sqrt(self.slope**2 + 1) * (-1 if self.target[0] < self.start[0] else 1) + self.start[0]
                self.body.y = self.slope * (self.body.x - self.target[0]) + self.target[1]
            # calculate x using y
            else:
                self.body.y = distance * (-1 if self.target[1] < self.start[1] else 1) + self.start[1]
                self.body.x = (self.body.y - self.start[1]) / self.slope + self.start[0]
        else:
            self.body.x = self.start[0]
            self.body.y = self.start[1] + distance * (-1 if self.target[1] < self.start[1] else 1)
        
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