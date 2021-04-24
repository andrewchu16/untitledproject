import pygame
import math
import random
from src.utilities.mouse import cursor
from src.utilities.healthbar import Healthbar
from src.attack import Attack
from src.bullet import Bullet

class Player():

    def __init__(self):
        self.w, self.h = 50, 50
        self.sprite = pygame.Surface((50, 50))
        self.sprite.fill((255, 100, 180))
        self.x, self.y = 400, 400
        self.body = pygame.Rect((self.x, self.y), self.dims)

        self.bulletList = []

        # attack cooldown
        self.cooldown = 100
        self.cooldownMax = 100

        # bullet damage and health 
        self.bulletHealth = 0

        #health
        self.hp = Healthbar(250)
        
        #mobility
        self.speed = 4

        self.attack = Attack(1000)
    
    @property
    def dims(self) -> tuple((int, int)):
        return (self.w, self.h)

    @property 
    def pos(self):
        return (self.x, self.y)

    def updateStats(self, nCooldown=0, nDamage=0):
        # changes stats by amount 
        self.cooldownMax += nCooldown 
        self.damage += nDamage

    def update(self, keysdown: list):

        moveVecx = 0
        moveVecy = 0
        if keysdown[pygame.K_s]:
            moveVecy += self.speed
        if keysdown[pygame.K_w]:
            moveVecy += -self.speed
        if keysdown[pygame.K_a]:
            moveVecx += -self.speed
        if keysdown[pygame.K_d]:
            moveVecx += self.speed
        
        if abs(moveVecx) == abs(moveVecy) and moveVecx != 0:
            diag = math.sqrt(2)
            moveVecx = round(moveVecx/diag, 2)
            moveVecy = round(moveVecy/diag, 2)
        
        self.x += moveVecx
        self.y += moveVecy
        self.body.x, self.body.y = self.x, self.y

        self.cooldown -= 1

        if self.cooldown <= 0 and cursor.Lclick:
            self.cooldown = self.cooldownMax
            relx, rely = cursor.x-self.x, cursor.y-self.y
            angle = math.atan2(rely+random.randint(-30, 30), relx+ random.randint(-30, 30))
            direction = {
                "angle": angle,
                "chx": math.cos(angle),
                "chy": math.sin(angle)
            }
            self.bulletList.append(Bullet(self.bulletHealth, direction, self.pos, (150, 2, 180), 300))

            
        self.hp.update()


    def render(self, screen, dims):
        screen.blit(self.sprite, (self.x, self.y))

        self.attack.render(screen)
        self.hp.render(screen)
