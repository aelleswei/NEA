from multiprocessing.context import assert_spawning
import random
import pygame
from block_new import Block
from settings2 import *
from math import sqrt,atan2,degrees
from Bullet import Bullet
from player_prototype import Player


class Enemy(Player,pygame.sprite.Sprite):
    def __init__(self,player,tile_x,tile_y,graphic):
        super().__init__(tile_x,tile_y)
        self.name = "ENEMY"
        self.image = pygame.image.load(graphic)
        self.image = pygame.transform.rotozoom(self.image,0,0.8)
        self.player = player
        self.test = pygame.time.get_ticks()
        self.speed = 5
        self.health = 10
        self.hit = False
       
    
    #def locate_player(self):
        #print(self.player.rect[0],self.player.rect[1])d


    def move_to_player(self,block_group):
        test2 = 0
        test1 = self.test
        test2 = pygame.time.get_ticks()
        
       
        xvel = 0
        yvel = 0
        
        if self.player.rect[0] > self.rect[0]:
            xvel = self.speed
        if self.player.rect[0] < self.rect[0]:
            xvel = -self.speed
        if self.player.rect[1] > self.rect[1]:
            yvel = self.speed
        if self.player.rect[1] < self.rect[1]:
            yvel = -self.speed
         
        if xvel != 0 and yvel != 0:
            xvel /= sqrt(2)
            yvel /= sqrt(2)
        
        self.block_collide(block_group,xvel,yvel)
    
    def turning(self):
        
        dx = self.rect.center[0] - self.player.rect.center[0]
        dy = (self.rect.center[1] - self.player.rect.center[1]) *-1
			
        self.angle = (degrees(atan2(dy,dx)) + 180) 

    def shooting(self):
        shoot = random.randint(1,1000)
       #print(shoot,self.shoot_cooldown)
        if shoot <= 100 and self.shoot_cooldown == 0:
            bullet = Bullet(self.rect.center[0],self.rect.center[1],self.angle,25)
            self.bullet_group.add(bullet)
            self.shoot_cooldown = self.shoot_cooldown_base
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        else:
            pass
        
    def update_health(self,bullet_group):
        hit = self.detect_bullets(bullet_group)
        if hit:
            self.health -= 1
    #     if self.health < 1:
    #         self.kill()
     
    # def detect_bullets(self,bullet_group):
    #     bullet_hit_list = pygame.sprite.spritecollide(self,bullet_group,True)
    #     if bullet_hit_list != []:
    #         hit = True
    #     else:
    #         hit = False
       
    #     return hit   
   
    def update(self,block_group,bullet_group):
        self.update_health(self.player.bullet_group)
        #self.locate_player()
        self.move_to_player(block_group)
        #self.dodge(bullet_group,block_group)
        self.turning()
        self.shooting()
        self.display_health_bar()
        if self.health < 1:
            self.kill()
class Rush(Enemy):
    pass

class Sniper(Enemy):
    pass