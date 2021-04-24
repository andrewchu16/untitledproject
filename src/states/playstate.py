import pygame
from src.player import Player
from src.letters import Letter
from src.letterspit import Letterspit
from src.enemy import Spitter
from src.turret import Turret
from src.bullet import Bullet 
import math
import random
import sys

pygame.font.init()


'''
State that is called during the main game
'''
class PlayState():

    def __init__(self):
        self.changeTo = None
        self.states = {"play", "intro", "pause", "setting"}
        self.player = None
        self.letter = []

        # Creates src.player.Player object
        self.player = Player()

        # Summons a letterspit and creates enemy list
        self.lettergen = Letterspit()
        self.lettergen.cap = 20
        self.lettergen.level = 1
        self.enemylist = []

        self.armageddon_status = False
        self.armageddon_cur = 0
        self.arma_counter = 0

        self.money = 0
        self.turrets = []
        self.money_font = pygame.font.SysFont("Arial", 50)

        self.timer = 0
        self.cnter = 0

        #self.turretup = pygame.Surface((60, 60))
        #self.healthup = pygame.Surface((60, 60))
        #self.attackup = pygame.Surface((60, 60))
        #self.turretup.fill((122,122,122))
        #self.healthup.fill((210, 69, 210))
        #self.attackup.fill((96,69,96))

    def enter(self):
        # Armageddon happens at the start for testing purposes FOR NOW
        #self.armageddon_status = True
        f = open('src/utilities/segmenttree.txt', 'r')
        self.arma = f.readlines()
        f.close()
        pass
  
    def exit(self):

        self.changeTo = None


    def armageddon(self):
        if self.armageddon_cur == 0:
            #start armageddon
            self.arma_counter = 0
        change = False
        y = 0
        if self.arma_counter % 5 == 0:
            for nxt in self.arma:
                y += 15
                relx, rely = 700, 0
                #angle = math.atan2(rely+random.randint(-30, 30), relx+ random.randint(-30, 30))
                angle = math.atan2(rely, relx)
                direction = {
                    "angle": angle,
                    "chx": math.cos(angle),
                    "chy": math.sin(angle)
                }
                if self.armageddon_cur < len(nxt):
                    change = True
                    if nxt[self.armageddon_cur] != " ":
                        self.letter.append(Letter(1, direction, (0, y), nxt[self.armageddon_cur], (255, 245, 255)))
            self.armageddon_cur += 1
            if not change:
                self.armageddon_status = False
        self.arma_counter += 1

    def update(self, keyspressed, keysdown):

        self.cnter += 1
        if self.cnter % 60 == 0 and self.cnter != 0:
            self.timer += 1
        
        if self.cnter % 1000 == 0 and self.cnter != 0:
            self.armageddon_status = True
        
        if self.cnter % 00 == 0 and self.timer != 0:
            self.lettergen.level += 1
        
        if self.cnter % 200 == 0 and self.timer != 0:
            if random.randint(1, 2) == 1:
                x, y = random.choice([0, 700]), random.randint(0, 700)
            else:
                x, y = random.randint(0, 700), random.choice([0, 700])
            self.enemylist.append(Spitter(self.timer // 5, (x,y)))

        # Calls armageddon 
        if self.armageddon_status:
            self.armageddon()

        # Summons letters
        res = self.lettergen.update((self.player.x, self.player.y), None)
        if res != None:
            self.letter.append(res)
        self.player.update(keysdown)
        removelist = []

        
        # TODO: calculate bullet and letter collisions, update letter/bullet hp here
        for bullet in self.player.bulletList:
            bullet.update() 
            for nxt in self.letter: 
                if bullet.body.colliderect(nxt.body):
                    tmp = bullet.hp
                    bullet.hp -= min(nxt.hp, tmp)
                    nxt.hp -= min(nxt.hp, tmp)
            for nxt in self.enemylist:
                for go in nxt.peons:
                    if bullet.body.colliderect(go.body):
                        removelist.append(go)
                        tmp = bullet.hp
                        bullet.hp -= min(go.hp, tmp)
            
            
            if bullet.hp <= 0 or bullet.distance > bullet.rRange:
                # print("bullet collision:", bullet.hp)
                removelist.append(bullet)
                
        # When letters hit the player, health and letter removal is executed here
        for nxt in self.letter:
            if self.player.body.colliderect(nxt.body):
                if self.player.hp.hp - nxt.hp >= 0:
                    self.player.hp.hp -= nxt.hp
                else:
                    #bye bye
                    print("you died lol")
                    sys.exit(0)
                removelist.append(nxt)
        
        # Deletes old letters and awards money for killing letters 
        for nxt in self.letter:
            nxt.update()
            if nxt.hp <= 0:
                removelist.append(nxt)
                self.money += nxt.max_health
            elif nxt.x > 700 or nxt.x < 0 or nxt.y > 700 or nxt.x < 0:
                removelist.append(nxt)

        # Letter cleanup
        for nxt in removelist:
            if nxt in self.letter:
                self.letter.remove(nxt)
            elif nxt in self.player.bulletList:
                self.player.bulletList.remove(nxt)
        removelist = []
        for go in self.enemylist:
            for nxt in go.peons:
                nxt.update()
                if self.player.body.colliderect(nxt.body):
                    if self.player.hp.hp - 5 >= 0:
                        self.player.hp.hp -= 5
                    removelist.append(nxt)
                
                if self.player.attack.body and self.player.attack.body.colliderect(nxt.body):
                #two cases, letter has more or attack has more hp
                    tmp = self.player.attack.hp
                    self.player.attack.hp -= min(tmp, nxt.hp)
                    nxt.hp -= min(tmp, nxt.hp)

                if nxt.hp <= 0:
                    removelist.append(nxt)
                    self.money += nxt.max_health
                elif nxt.x > 700 or nxt.x < 0 or nxt.y > 700 or nxt.x < 0:
                    removelist.append(nxt)

            for nxt in removelist:
                if nxt in go.peons:
                    go.peons.remove(nxt)
            
            if self.player.attack.body and self.player.attack.body.colliderect(go.body):
                #two cases, letter has more or attack has more hp
                    tmp = self.player.attack.hp
                    self.player.attack.hp -= min(tmp, go.hp)
                    go.hp -= min(tmp, go.hp)

            if go.hp <= 0:
                self.money += go.max_health
                removelist.append(go)

            go.update((self.player.x, self.player.y))
        
        for nxt in removelist:
            if nxt in self.enemylist:
                self.enemylist.remove(nxt)

    def render(self, screen, h: float, w: float):
        for nxt in self.letter:
            nxt.render(screen, (h, w))
        for nxt in self.enemylist:
            for go in nxt.peons:
                go.render(screen, (h, w))
            nxt.render(screen)
        self.player.render(screen, (h, w))
        # screen.blit(self.turretup, (260, 640))
        #screen.blit(self.healthup, (320, 640))
        #screen.blit(self.attackup, (380, 640))

        for nxt in self.player.bulletList:
            nxt.render(screen, (w, h))

        money_text = self.money_font.render("$"+str(self.money), False, (38,54,139))
        screen.blit(money_text, ((700-money_text.get_width())//2, 40))

