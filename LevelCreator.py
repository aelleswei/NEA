from calendar import c
import pygame
from player_prototype import Player
from settings2 import *
from level2 import plain
from block_new import Block
from math import sqrt

# how to check path:
# for every tile:
# 	put 'B' there
# 	run the bfs
# 	output result
# 	reset plain to what it was before

class LevelCreator():
	def __init__(self):
		self.block_group = pygame.sprite.Group()
		self.block_selected = 0
		self.current_tiles = ""
		self.initial_drawn = False
		self.bg = pygame.image.load('graphics/level-creator-bg.png')
		self.player_count = 0
		self.first_draw = False
		self.old_plain = plain
		self.block_list = ['block','move','des','item']
		self.block_dict = {'0':'B',
		'1':'Bm',
		'2':'Bd',
		'3':'Bi'
		}
		self.enemy_selected = 0
		self.enemy_list = ['basic','rush','sniper']
		self.enemy_dict = {'0':'E',
		'1':'Er',
		'2':'Es'}
		self.door_count = 0 
		self.plain_adjacency_dict = {}
		self.state = 'manual'
		self.enemy_count = 0
		self.draw_dict = {"p":"player","d":"door","B":"block","Bm":"move","Bd":"des","Bi":"item","E":"basic","Er":"rush","Es":"sniper"}
		self.dict_made = False
		self.special_place_list = ["E","Er","Es","Bm","Bi","Bd"]
		self.special_place_list_locations = []
		


	def create_adjacency_dict(self,plain,dict):
		for i in range(len(plain)):
			for j in range(len(plain[i])):
				dict[(j,i)] = self.check_around_small((j,i))
				
		return dict

	def check_around(self,current):
		current = current
		array = []
		tile0 = self.check_tile(current,-1,0)
		if self.valid_tile(tile0):
			array.append(tile0)
			
		tile1 = self.check_tile(current,-1,1)
		if self.valid_tile(tile1) == True:
			array.append(tile1)
			
		tile2 = self.check_tile(current,-1,-1)
		if self.valid_tile(tile2) == True:
			array.append(tile2)
			
		tile3 = self.check_tile(current,0,1)
		if self.valid_tile(tile3) == True:
			array.append(tile3)
			
		tile4 = self.check_tile(current,0,-1)
		if self.valid_tile(tile4) == True:
			array.append(tile4)
			
		tile5 = self.check_tile(current,1,0)
		if self.valid_tile(tile5) == True:
			array.append(tile5)
			
		tile6 = self.check_tile(current,1,1)
		if self.valid_tile(tile6) == True:
			array.append(tile6)
			
		tile7 = self.check_tile(current,1,-1)
		if self.valid_tile(tile7) == True:
			array.append(tile7)

		return array
	
	def check_tile(self,current,hor,ver):
		current = current
		tile_check = (current[0] + hor, current[1] + ver)
		return tile_check


	def valid_tile(self,tile):
		if tile[0] > 19 or tile[0] < 0 or tile[1] > 11 or tile[1] < 0:
			valid = False
		else:
			valid = True

		return valid
	
	def default_draw(self):
		for i in range(len(plain)):
			for j in range(len(plain[i])):
				# if plain[i][j] == 'p':
				# 	player_block = Block(j,i,'graphics/player.png')
				# 	self.block_group.add(player_block)
				# elif plain[i][j] == 'd':
				# 	door_block = Block(j,i,'graphics/door.png')
				# 	self.block_group.add(door_block)
				string = plain[i][j]
				if string != "":
					img = self.draw_dict[string]
					graphic = (f'graphics/{img}.png')
					block = Block(j,i,graphic)
					self.block_group.add(block)
	
	def change_mouse(self,type,mouse):
		pygame.mouse.set_visible(False)
		mouse_img = pygame.image.load(f'graphics/{type}.png')
		mouse_img = pygame.transform.rotozoom(mouse_img,0,0.8)
		mouse_rect = mouse_img.get_rect()
		mouse_rect.center = mouse
		win.blit(mouse_img,mouse_rect.center)
		
	def player_valid(self,current):
		current = current
			
		array = self.check_around(current)
			
			
		for tile in array:
				
			if plain[tile[1]][tile[0]] != "":
				valid = False
				break
			else:
				valid = True

		if plain[current[1]][current[0]] != "":
				valid = False
					
		return valid

	def block_valid(self,current,selected):
		current = current
		array = self.check_around(current)
			

		for tile in array:
			valid = None
			if plain[tile[1]][tile[0]] != "":
				if plain[tile[1]][tile[0]] == 'p' or plain[tile[1]][tile[0]][0] == 'E':
					valid = False
					break
		if plain[current[1]][current[0]] != "":	
			if plain[current[1]][current[0]] == 'p' or plain[current[1]][current[0]][0] == 'E':
				valid = False
				

		else:
			valid = True


		if valid == True:
			if plain[current[1]][current[0]] == 'd':
				valid = False
				
		if valid == True and selected == "B":
			plain[current[1]][current[0]] = "B"
			visited = self.check_for_path((0,5),self.plain_adjacency_dict,None)
			if (19,5) in visited and (18,5) in visited:
				valid = True
				plain[current[1]][current[0]] = ""
			else:
				valid = False
				plain[current[1]][current[0]] = ""
						
			
			
		
		if valid == True and selected != "B":
			valid = self.check_if_surrounded(current)
		
		elif valid == True:
			for i in range(len(plain)):
				for j in range(len(plain[i])):
					if plain[i][j] in self.special_place_list:
						special_position = (j,i)
						plain[current[1]][current[0]] = "B"
						valid = self.check_if_surrounded(special_position)
						plain[current[1]][current[0]] = ""

		

		return valid
	 
	def enemy_valid(self,current,selected):
		if self.enemy_count < 7:
			current = current
			for i in range(len(plain)):
				for j in range(len(plain[i])):
					if plain[i][j] == 'p':
						player_tile = (j,i)
						break

			# for i in range(len(plain)):
			# 	for j in range(len(plain[i])):
			# 		distance = sqrt((j-player_tile[0])**2 + (i - player_tile[1])**2)
			# 		if distance < 3: 
			# 			# invalid_block = Block(j,i,'graphics/invalid_block.png')
			# 			# invalid_block.draw()
			# 			valid = False


			distance = sqrt((current[0] - player_tile[0])**2 + (current[1] - player_tile[1])**2)

			if distance < 3:
				valid = False
			else:
				valid = True

			# if valid == True:
			# 	if plain[current[1]][current[0]] == 'd':
			# 		valid = False
			# 	array = self.check_around(current)
			# 	for tile in array:
			# 		if plain[tile[1]][tile[0]] != "":
			# 			if plain[tile[1]][tile[0]][0] == "B" or plain[tile[1]][tile[0]] == "d":
			# 				valid = False
			# 		if plain[current[1]][current[0]] != "":		
			# 			if plain[current[1]][current[0]] != "":
			# 				valid = False
				
			if plain[current[1]][current[0]] != "":
				#if plain[current[1]][current[0]][0] == "B" or plain[current[1]][current[0]][0] == "E":
				valid = False
			if valid == True:		
				valid = self.check_if_surrounded(current)
							
		else:
			valid = False
		return valid
							
	def screen_check(self,type,selected):
		for i in range(len(plain)):
				tile_y = i
				for j in range(len(plain[i])):
					tile_x = j
					valid = type((j,i),selected)
					if valid == False:
						invalid_block = Block(j,i,'graphics/invalid_block.png')
						invalid_block.draw()
	

	def select_item(self,keys,mouse,current_tiles):
		if keys[pygame.K_1]:
			if pygame.mouse.get_pressed()[2]:
				self.block_selected = (self.block_selected + 1) % len(self.block_list) # solution to cycle through the list, from stackoverflow. 
				pygame.time.wait(200)

			self.change_mouse(self.block_list[self.block_selected],mouse)
			self.screen_check(self.block_valid,self.block_dict[str(self.block_selected)])

			if pygame.mouse.get_pressed()[0] and self.block_valid(current_tiles,self.block_dict[str(self.block_selected)]):
				plain[current_tiles[1]][current_tiles[0]] = self.block_dict[str(self.block_selected)]
				block_graphic = (f'graphics/{self.block_list[self.block_selected]}.png')
				block_block = Block(current_tiles[0],current_tiles[1],block_graphic)
				self.block_group.add(block_block)

		if keys[pygame.K_2]:
		
			if pygame.mouse.get_pressed()[2]:
				self.enemy_selected = (self.enemy_selected + 1) % len(self.enemy_list)
				pygame.time.wait(200)
			
			self.change_mouse(self.enemy_list[self.enemy_selected],mouse)
			
			self.screen_check(self.enemy_valid,self.enemy_dict[str(self.enemy_selected)]) 

			if pygame.mouse.get_pressed()[0] and self.enemy_valid(current_tiles,self.enemy_dict[str(self.enemy_selected)]):
				enemy_graphic = (f'graphics/{self.enemy_list[self.enemy_selected]}.png')
				plain[current_tiles[1]][current_tiles[0]] = self.enemy_dict[str(self.enemy_selected)]
				enemy_block = Block(current_tiles[0],current_tiles[1],enemy_graphic)
				self.enemy_count += 1
				self.block_group.add(enemy_block)
			elif self.enemy_count >= 7:
				self.bg = pygame.image.load('graphics/level-creator-bg1.png')
				

		if keys[pygame.K_3]:
			
			self.change_mouse('eraser',mouse)
			if pygame.mouse.get_pressed()[0]:
				for block in self.block_group:
					block_x = int(block.rect[0] / 64)
					block_y = int(block.rect[1] / 64)
					if block_x <= 0 or block_x >= 19 or block_y <= 0 or block_y >= 11:
						pass
					else:
						if plain[current_tiles[1]][current_tiles[0]] != "":
							if block_x == current_tiles[0] and block_y == current_tiles[1]:
								if plain[current_tiles[1]][current_tiles[0]][0] == "E":
									self.enemy_count -= 1
									plain[current_tiles[1]][current_tiles[0]] = ""
									self.block_group.remove(block)
								else:
									plain[current_tiles[1]][current_tiles[0]] = ""
									self.block_group.remove(block)

		if keys[pygame.K_SPACE]:
			self.state = 'main'
			

					
	def check_for_path(self,start,dict,visited):
		
		if visited == None:
			visited = set()
		if start not in visited:
			item = plain[start[1]][start[0]]
			if item != "B":
				visited.add(start)
				for adj in dict[start]:
					self.check_for_path(adj,dict,visited)
					
		return visited

	def check_around_small(self,current):
		array = []
		current = current
		
		tile0 = self.check_tile(current,-1,0)
		if self.valid_tile(tile0):
			array.append(tile0)
		
		tile1 = self.check_tile(current,1,0)
		if self.valid_tile(tile1):
			array.append(tile1)
			
		tile2 = self.check_tile(current,0,1)
		if self.valid_tile(tile2):
			array.append(tile2)
			
		tile3 = self.check_tile(current,0,-1)
		if self.valid_tile(tile3):
			array.append(tile3)
			
		return array
		

	def check_if_surrounded(self,tile):
		array = self.check_around_small(tile)
		valid = False
		for tile in array:
			if plain[tile[1]][tile[0]] != "":
				#if plain[tile[1]][tile[0]][0] == "B":  
					pass
			else:
				valid = True
				break
		return valid

	def run(self):
		plain_updated = False
		clock.tick(FPS)
		win.blit(self.bg,(0,0))
		self.bg = pygame.image.load('graphics/level-creator-bg.png')
		mouse = pygame.mouse.get_pos()
		tile_x = mouse[0] // 64
		tile_y = mouse[1] // 64
		#print(tile_x,tile_y)
		current_tiles = (tile_x,tile_y)
		#print(current_tiles)
		keys = pygame.key.get_pressed()
		#print(self.enemy_count)









				

		if self.first_draw == False:
			self.default_draw()
			self.first_draw = True
		
		if self.dict_made == False:
			self.plain_adjacency_dict = self.create_adjacency_dict(plain,self.plain_adjacency_dict)
			self.dict_made = True
		
		self.select_item(keys,mouse,current_tiles)

		

		self.block_group.draw(win)
		#print(self.state)
		
		#print(plain[current_tiles[1]][current_tiles[0]])
	
		#print(self.enemy_count)
		pygame.display.update()