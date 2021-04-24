import pygame

class Healthbar():

    def __init__(self, hp):
        
        self.hp = hp
        self.maxhp = hp

        self.health_bar = pygame.Surface((200, 30))
        self.health_bar_show = pygame.Surface((200, 30))
        
        self.health_bar.fill((0,255,0))
        self.health_bar_show.fill((255, 0 ,0))
    
    def update(self):
        
        self.health_bar = pygame.Surface((int(200*(self.hp/self.maxhp)),30))
        self.health_bar.fill((0,255,0))

    def render(self, screen):

        screen.blit(self.health_bar_show, (250, 640))
        screen.blit(self.health_bar, (250, 640))