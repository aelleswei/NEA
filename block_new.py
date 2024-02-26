from ast import Try
import random
import pygame
from pygame.sprite import collide_circle_ratio
from settings2 import *
from level2 import plain
class Block(pygame.sprite.Sprite):
	def __init__(self,tile_x,tile_y,image):
		super().__init__()
		self.name = 'N/A'
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
		self.rect[0] = tile_x * 64
		self.rect[1] = tile_y * 64
		self.hit = False
		self.bullet_hit_list = None
		

	def draw(self):
		win.blit(self.image,(self.rect[0],self.rect[1]))
		
	def detect_bullets(self,bullet_group):
		self.bullet_hit_list = pygame.sprite.spritecollide(self,bullet_group,True)
		if self.bullet_hit_list != []:
			self.hit = True
			

		else:
			self.hit = False
			
			
	def update(self,bullet_group):
		self.detect_bullets(bullet_group)
		

class DestructiveBlock(Block):
	def __init__(self,tile_x,tile_y,image):
		super().__init__(tile_x,tile_y,image)
		self.health = 5
		self.sprite_dict = {1:'graphics/1hp.png',
					 2:'graphics/2hp.png',
					 3:'graphics/3hp.png',
					 4:'graphics/4hp.png'}
		self.broken = False
		
	def remove_health(self):
		if self.hit == True:
			self.health -= 1
		
		if self.health < 1:
			self.broken = True
			self.kill()
			x_tile = int(self.rect[0] / 64)
			y_tile = int(self.rect[1] / 64)
			plain[y_tile][x_tile] = ""
			

	def change_sprite(self):
		if self.health in self.sprite_dict:
			self.image = pygame.image.load(self.sprite_dict[self.health])
			

	def update(self,bullet_group):
		self.detect_bullets(bullet_group)
		self.remove_health()
		self.change_sprite()
		

class MoveableBlock(Block):
	def __init__(self,tile_x,tile_y,image):
		super().__init__(tile_x,tile_y,image)
		
		

	def move_tile(self,dx,dy,valid,current_x,current_y,new_x,new_y):
		x_tiles = (dx * 64)
		y_tiles = (dy * 64)
		
		if valid == True:
			
			plain[current_y][current_x] = ""
			plain[new_y][new_x] = "Bm"
			
			self.rect[0] += x_tiles
			self.rect[1] += y_tiles
		
		else:
			pass
		
		

	def check_for_move(self):
		
		x = 0
		y = 0
		
		bullet = self.bullet_hit_list[0]
		
		if bullet.xv > 0 and abs(bullet.xv) > abs(bullet.yv):
			x = 1
		elif bullet.xv < 0 and abs(bullet.xv) > abs(bullet.yv):
			x = -1
		elif bullet.yv > 0 and abs(bullet.yv) > abs(bullet.xv):
			y = 1
		elif bullet.yv < 0 and abs(bullet.yv) > abs(bullet.xv):
			y = -1
		elif bullet.xv == 0 and bullet.yv == 0:
			x = 0
			y = 0
		elif bullet.xv == bullet.yv:
			x = 1
			y = 1
			
		current_x_tile = int(self.rect[0] / 64)
		current_y_tile = int(self.rect[1] / 64)
		new_x_tile = int((self.rect[0] + x*64) / 64)
		new_y_tile = int((self.rect[1] + y*64) / 64)
	

		try:
			if plain[new_y_tile][new_x_tile] == "":
				valid = True
		
	
			
				plain[current_y_tile][current_x_tile] = ""
				plain[new_y_tile][new_x_tile] = "Bm"
			else:
				valid = False
		except:
			valid = False
	
		

		
		return x,y,valid,current_x_tile,current_y_tile,new_x_tile,new_y_tile
		
	def correct_position(self):
		if self.rect[0] < 0:
			self.rect[0] = 0
		if self.rect[1] < 0:
			self.rect[1] = 0
			
		
		
	def update(self,bullet_group):
		self.detect_bullets(bullet_group)
		if self.hit == True:
			x,y,valid,current_x,current_y,new_x,new_y = self.check_for_move()
			if x != 0 or y != 0:
				self.move_tile(x,y,valid,current_x,current_y,new_x,new_y)	
			self.correct_position()

class ItemBlock(DestructiveBlock):
	def __init__(self,tile_x,tile_y,image):
		super().__init__(tile_x,tile_y,image)
		self.name = 'ITEM'
		self.item_list = ['fr+']
		self.x_tile = int(self.rect[0] / 64)
		self.y_tile = int(self.rect[1] / 64)
		self.item = random.choice(self.item_list)
		
	def drop_item(self):
		if self.broken == True:
			plain[self.y_tile][self.x_tile] = random.choice(self.item_list)
			self.image = pygame.image.load(f'graphics/{self.item}.png')
	
	def remove_health(self):
		if self.hit == True:
			self.health -= 1
		
		if self.health < 1:
			self.broken = True
			x_tile = int(self.rect[0] / 64)
			y_tile = int(self.rect[1] / 64)
			plain[y_tile][x_tile] = ""
		
	def update(self, bullet_group):
		if self.broken == False: 
			self.detect_bullets(bullet_group)
			self.remove_health()
			self.change_sprite()
		self.drop_item()
	

class Door(Block):
	def __init__(self,tile_x,tile_y,image):
		super().__init__(tile_x,tile_y,image)
		self.name = 'DOOR'
		
		
		
		

