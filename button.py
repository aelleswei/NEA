import pygame,sys
from settings2 import *



class Button(pygame.sprite.Sprite):
	def __init__(self,image,image2,x,y,sound):
		super().__init__()
		self.x = x 
		self.y = y
		self.photo1 = image
		self.photo2 = image2
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
		self.rect.topleft = (x,y)
		self.click_sound = pygame.mixer.Sound(sound)

	def draw(self):

		clicked = False

		win.blit(self.image,self.rect.topleft)

		mouse = pygame.mouse.get_pos()
		hovering = self.rect.collidepoint(mouse)
		if hovering:
			#print("HOVERING")
			self.image = pygame.image.load(self.photo2)
			if pygame.mouse.get_pressed()[0]:
				#print("CLICKED")
				clicked = True
				# n = self.click_sound.get_num_channels()
				# if n == 0:
				# 	self.click_sound.play()

		else:
			#print("NOT HOVERING")
			self.image = pygame.image.load(self.photo1)

		return clicked

	def change_size(self,scale):

		self.image = pygame.transform.rotozoom(self.image,0,scale)
		self.rect = self.image.get_rect()
		self.rect.topleft = (self.x,self.y)