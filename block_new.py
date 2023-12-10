import pygame
from settings2 import *
class Block(pygame.sprite.Sprite):
	def __init__(self,tile_x,tile_y,image):
		super().__init__()
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
		self.rect[0] = tile_x * 64
		self.rect[1] = tile_y * 64

	def draw(self):
		win.blit(self.image,(self.rect[0],self.rect[1]))