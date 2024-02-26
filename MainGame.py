import pygame
from LevelCreator import LevelCreator
from player_prototype import Player
from settings2 import *
from level2 import plain
from block_new import *
from Enemy import *
from math import sqrt

class MainGame():
	def __init__(self):
		self.state = "main"
		self.draw_dict = {"p":"player","d":"door","B":"block","Bm":"move","Bd":"des","Bi":"item","E":"basic","Er":"rush","Es":"sniper"}
		self.all_class_dict = {'B':Block,'Bd':DestructiveBlock,'Bi':ItemBlock,'Bm':MoveableBlock,'d':Door,'p':Player,'E':Enemy,"Er":Rush,"Es":Sniper}
		self.all_block_group = pygame.sprite.Group()
		self.all_enemy_group = pygame.sprite.Group()
		self.enemy_bullet_group = pygame.sprite.Group()
		self.all_bullet_group = pygame.sprite.Group()
		self.inital_drawn = False
		self.player = None
		self.bg = pygame.image.load('graphics/level-creator-bg.png')
		
	
		
	def change_mouse(self,type,mouse):
		pygame.mouse.set_visible(False)
		mouse_img = pygame.image.load(f'graphics/{type}.png')
		mouse_img = pygame.transform.rotozoom(mouse_img,0,0.4)
		mouse_rect = mouse_img.get_rect()
		mouse_rect.center = mouse
			
		win.blit(mouse_img,mouse_rect.center)
	
	def inital_draw(self):
		self.player = Player(0,5)
		for i in range(len(plain)):
			for j in range(len(plain[i])):
				if plain[i][j] in self.all_class_dict:
					img = plain[i][j]
					if self.player != None:
						graphic = (f"graphics/{self.draw_dict[img]}.png")
						if img[0] == 'B' or img == 'd':
							#print(f'BLOCK DRAWN AT {j,i}')
							type_of_block = self.all_class_dict[img]
							block_to_draw = type_of_block(j,i,graphic)
							self.all_block_group.add(block_to_draw)
							
						if img[0] == 'E':
							#print(f'ENEMY DRAWN AT{j,i}')
							type_of_enemy = self.all_class_dict[img]
							#print(type_of_enemy)
							enemy_to_draw = type_of_enemy(self.player,j,i,graphic)
							#print(enemy_to_draw)
							self.all_enemy_group.add(enemy_to_draw)
	
							
	def run(self,state):
		#if self.state == "main":
		keys = pygame.key.get_pressed()
		mouse = pygame.mouse.get_pos()
		clock.tick(FPS)
		win.blit(self.bg,(0,0))
		
		
		
	
		if self.inital_drawn == False:
			self.inital_draw()
			self.inital_drawn = True
			
		
		
		self.change_mouse('crosshair',mouse)
		
		self.player.draw()
		self.player.update(self.all_block_group,self.enemy_bullet_group)
		player_bullet_group = self.player.bullet_group
		
		player_bullet_group.draw(win)
		player_bullet_group.update()
		
		self.all_enemy_group.draw(win)
		self.all_enemy_group.update(self.all_block_group,player_bullet_group)
		
		for enemy in self.all_enemy_group:
			self.enemy_bullet_group.add(enemy.bullet_group)
		
		
		
		self.enemy_bullet_group.draw(win)
		self.enemy_bullet_group.update()
		
		self.all_bullet_group.add(player_bullet_group)
		self.all_bullet_group.add(self.enemy_bullet_group)
		self.all_block_group.draw(win)
		self.all_block_group.update(self.all_bullet_group)
		
		if self.player.health <= 0:
			self.state = state
			pygame.time.wait(100)
			
		#print("MAIN GAME CURRENTLY RUNNING")
		
		#print("FPS:", int(clock.get_fps()))
		#print(self.state)

		pygame.display.update()