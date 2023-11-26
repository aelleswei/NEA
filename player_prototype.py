import pygame
from settings2 import *

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load('graphics/player.png')
		self.rect = self.image.get_rect()


	def update(self):
		SPEED = 10
		xvel = 0
		yvel = 0
		keys = pygame.key.get_pressed()
		
		if keys[pygame.K_a]:
			xvel = -SPEED

		if keys[pygame.K_d]:
			xvel = SPEED 

		if keys[pygame.K_w]:
			yvel = -SPEED


		if keys[pygame.K_s]:
			yvel = SPEED



		self.rect[0] += xvel
		self.rect[1] += yvel

		#print(self.rect.x)

		



	def draw(self):

		self.update()

		win.blit(self.image,self.rect)

	












