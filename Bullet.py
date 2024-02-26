import pygame
import math
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,angle,speed):
        super().__init__()
        self.image = pygame.image.load('graphics/bullet.png')
        self.image = pygame.transform.rotate(self.image,angle)
        self.rect = self.image.get_rect(center = (x,y))
        self.speed = speed
        self.xv = (math.cos(angle * (math.pi/180)) * self.speed) 
        self.yv = (math.sin(angle * (math.pi/180)) * self.speed) * -1
        


    def movement(self):
        self.rect.x += self.xv
        self.rect.y += self.yv
            

    def check_in_boundary(self):
        if self.rect.x < 0:
            self.kill()
        if self.rect.x > 1280 + 100:
            self.kill()
                
        if self.rect.y < 0:
            self.kill()
        if self.rect.y > 720 + 100:
            self.kill()
           
                


    def update(self):
       self.movement()
       self.check_in_boundary()
