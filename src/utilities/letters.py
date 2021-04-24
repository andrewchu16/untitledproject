import pygame
import math
import random

pygame.font.init()

class Letter():

    def __init__(self, health, speed):

        self.hp = health
        self.speed = speed
