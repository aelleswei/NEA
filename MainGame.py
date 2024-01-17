import pygame
from player_prototype import Player
from settings2 import *
from level2 import plain
from block_new import Block
from math import sqrt

class MainGame():
	def __init__(self):
		self.player = Player()
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
		self.enemy_dict = {'0':'Eb',
		'1':'Er',
		'2':'Es'}
		self.door_count = 0 


		


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


		def default_draw():
			for i in range(len(plain)):
				for j in range(len(plain[i])):
					if plain[i][j] == 'p':
						player_block = Block(j,i,'graphics/player.png')
						self.block_group.add(player_block)
					elif plain[i][j] == 'd':
						door_block = Block(j,i,'graphics/door.png')
						self.block_group.add(door_block)



			


		def change_mouse(type):
			pygame.mouse.set_visible(False)
			mouse_img = pygame.image.load(f'graphics/{type}.png')
			mouse_img = pygame.transform.rotozoom(mouse_img,0,0.8)
			mouse_rect = mouse_img.get_rect()
			mouse_rect.center = mouse
			win.blit(mouse_img,mouse_rect.center)



		# def default_draw():
		# 	for i in range(len(plain)):
		# 		for j in range(len(plain[i])):
		# 			if plain[i][j] in block_dict:
		# 				x = plain[i][j]
		# 				graphic = (f'graphics/{block_dict[x]}.png')
		# 				type_block = Block(j,i,graphic)
		# 				self.block_group.add(type_block)

		# 	self.block_group.draw(win)




		def check_tile(current,hor,ver):
			current = current
			tile_check = (current[0] + hor, current[1] + ver)
			return tile_check


		def valid_tile(tile):
			if tile[0] > 19 or tile[0] < 0 or tile[1] > 11 or tile[1] < 0:
				valid = False
			else:
				valid = True

			return valid


		def check_around(current):
			current = current
			array = []
			tile0 = check_tile(current,-1,0)
			if valid_tile(tile0):
				array.append(tile0)
			
			tile1 = check_tile(current,-1,1)
			if valid_tile(tile1) == True:
				array.append(tile1)
			
			tile2 = check_tile(current,-1,-1)
			if valid_tile(tile2) == True:
				array.append(tile2)
			
			tile3 = check_tile(current,0,1)
			if valid_tile(tile3) == True:
				array.append(tile3)
			
			tile4 = check_tile(current,0,-1)
			if valid_tile(tile4) == True:
				array.append(tile4)
			
			tile5 = check_tile(current,1,0)
			if valid_tile(tile5) == True:
				array.append(tile5)
			
			tile6 = check_tile(current,1,1)
			if valid_tile(tile6) == True:
				array.append(tile6)
			
			tile7 = check_tile(current,1,-1)
			if valid_tile(tile7) == True:
				array.append(tile7)

			return array


		def player_valid(current):
			current = current
			
			array = check_around(current)
			
			#print(array)
			
			for tile in array:
				#print(tile)
				
				if plain[tile[1]][tile[0]] != "":
					valid = False
					break
				else:
					valid = True

			if plain[current[1]][current[0]] != "":
					valid = False






			return valid

		def block_valid(current):
			current = current
			array = check_around(current)

			for tile in array:
				if plain[tile[1]][tile[0]] == 'p':
					valid = False
					break
				elif plain[current[1]][current[0]] == 'p':
					valid = False
					break

				else:
					valid = True


			if valid == True:
				if plain[current[1]][current[0]] == 'd':
					valid = False

			return valid

		def enemy_valid(current):
			current = current
			for i in range(len(plain)):
				for j in range(len(plain[i])):
					if plain[i][j] == 'p':
						player_tile = (j,i)
						break

			for i in range(len(plain)):
				for j in range(len(plain[i])):
					distance = sqrt((j-player_tile[0])**2 + (i - player_tile[1])**2)
					if distance < 3: 
						invalid_block = Block(j,i,'graphics/invalid_block.png')
						invalid_block.draw()


			distance = sqrt((current[0] - player_tile[0])**2 + (current[1] - player_tile[1])**2)

			if distance < 3:
				valid = False
			else:
				valid = True

			if valid == True:
				if plain[current[1]][current[0]] == 'd':
					valid = False


			return valid





		

			



		def screen_check(type):
			for i in range(len(plain)):
					tile_y = i
					for j in range(len(plain[i])):
						tile_x = j
						valid = type((j,i))
						if valid == False:
							invalid_block = Block(j,i,'graphics/invalid_block.png')
							invalid_block.draw()


		if keys[pygame.K_1]:
			# self.block_selected = self.block_dict[0]
			# change_mouse(self.block_selected)
			# screen_check(block_valid)

			# if pygame.mouse.get_pressed()[0] and block_valid(current_tiles):
			# 	plain[current_tiles[1]][current_tiles[0]] = "B"
			# 	block_block = Block(current_tiles[0],current_tiles[1],'graphics/block.png')
			# 	self.block_group.add(block_block)
			# 	plain_updated = True

			if pygame.mouse.get_pressed()[2]:
				self.block_selected = (self.block_selected + 1) % len(self.block_list) # solution to cycle through the list, from stackoverflow. is this allowed?
				pygame.time.wait(200)

			change_mouse(self.block_list[self.block_selected])
			screen_check(block_valid)

			if pygame.mouse.get_pressed()[0] and block_valid(current_tiles):
				plain[current_tiles[1]][current_tiles[0]] = self.block_dict[str(self.block_selected)]
				block_graphic = (f'graphics/{self.block_list[self.block_selected]}.png')
				block_block = Block(current_tiles[0],current_tiles[1],block_graphic)
				self.block_group.add(block_block)




		# if keys[pygame.K_2]:
		# 	self.block_selected = 'player'
		# 	change_mouse(self.block_selected)
		# 	screen_check(player_valid)

		# 	if pygame.mouse.get_pressed()[0] and player_valid(current_tiles) and self.player_count == 0:
		# 		plain[current_tiles[1]][current_tiles[0]] = "P"
		# 		player_block = Block(current_tiles[0],current_tiles[1],'graphics/player.png')
		# 		self.block_group.add(player_block)
		# 		self.player_count += 1
		# 		for tile in check_around(current_tiles):
		# 			plain[current_tiles[1]][current_tiles[0]] = 'p'


		# 	if self.player_count > 0:
		# 		self.bg = pygame.image.load('graphics/level-creator-bg1.png')



		if keys[pygame.K_3]:
			# x = 'enemy1'
			# change_mouse(x)
			# enemy_valid(current_tiles)

			# if pygame.mouse.get_pressed()[0] and enemy_valid(current_tiles):
			# 	plain[current_tiles[1]][current_tiles[0]] = 'e'
			# 	enemy_block = Block(current_tiles[0],current_tiles[1],'graphics/enemy1.png')
			# 	self.block_group.add(enemy_block)

			if pygame.mouse.get_pressed()[2]:
				self.enemy_selected = (self.enemy_selected + 1) % len(self.enemy_list)
				pygame.time.wait(200)
			
			change_mouse(self.enemy_list[self.enemy_selected])
			
			enemy_valid(current_tiles)

			if pygame.mouse.get_pressed()[0] and enemy_valid(current_tiles):
				enemy_graphic = (f'graphics/{self.enemy_list[self.enemy_selected]}.png')
				plain[current_tiles[1]][current_tiles[0]] = self.enemy_dict[str(self.enemy_selected)]
				enemy_block = Block(current_tiles[0],current_tiles[1],enemy_graphic)
				self.block_group.add(enemy_block)





		# valid = block_valid(current_tiles)
		# if valid == False:
		# 	invalid_block = Block(current_tiles[0],current_tiles[1],'graphics/invalid_block.png')
		# 	invalid_block.draw()
		# print(valid)
			#print(tile)

		# if self.initial_drawn == False:
		# 	default_draw()
		# 	self.initial_drawn = True
			# if len(self.block_group) != 240:
			# 	self.block_group.clear()
			# 	default_draw()


		#self.player.draw()
		#print(self.initial_drawn)
		# test = check_block(current_tiles,1,1)
		# test1 = check_block(current_tiles,-1,1)
		# test_block = Block(test[0],test[1],'graphics/test_block.png')
		# test_block1 = Block(test1[0],test1[1],'graphics/test_block.png')
		# test_block.draw()
		# test_block1.draw()

		if self.first_draw == False:
			default_draw()
			self.first_draw = True

		self.block_group.draw(win)


		pygame.display.update()