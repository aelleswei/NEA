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
		self.block_selected = ""
		self.current_tiles = ""
		self.initial_drawn = False
		self.bg = pygame.image.load('graphics/level-creator-bg.png')
		self.player_count = 0

		


	def run(self):
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

		def change_mouse(type):
			pygame.mouse.set_visible(False)
			mouse_img = pygame.image.load(f'graphics/{type}.png')
			mouse_img = pygame.transform.rotozoom(mouse_img,0,0.8)
			mouse_rect = mouse_img.get_rect()
			mouse_rect.center = mouse
			win.blit(mouse_img,mouse_rect.center)



		def default_draw():
			for i in range(len(plain)):
				tile_y = i
				for j in range(len(plain[i])):
					tile_x = j
					block = Block(tile_x,tile_y,'graphics/valid_block.png')
					self.block_group.add(block)

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
				elif plain[current[1]][current[0]] != "":
					valid = False
					break
				else:
					valid = True


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

			return valid

		def enemy_valid(current):
			current = current
			for i in range(len(plain)):
				for j in range(len(plain[i])):
					if plain[i][j] == 'p':
						player_tile = (j,i)
						print(tile)
						d = sqrt((current[0] - j)**2 + (current[1] - i)**2)
						print(d)
						if d > 3:
							valid = True
							break
						else:
							valid = False
							tile_invalid = (j,i)




					

			





			for i in range(len(plain)):
					tile_y = i
					for j in range(len(plain[i])):
						tile_x = j
						if tile_invalid == (j,i):
							invalid_block = Block(j,i,'graphics/invalid_block.png')
							invalid_block.draw()

			



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
			self.block_selected = "block"
			change_mouse(self.block_selected)
			screen_check(block_valid)

			if pygame.mouse.get_pressed()[0] and block_valid(current_tiles):
				plain[current_tiles[1]][current_tiles[0]] = "B"
				block_block = Block(current_tiles[0],current_tiles[1],'graphics/block.png')
				self.block_group.add(block_block)


		if keys[pygame.K_2]:
			self.block_selected = 'player'
			change_mouse(self.block_selected)
			screen_check(player_valid)

			if pygame.mouse.get_pressed()[0] and player_valid(current_tiles) and self.player_count == 0:
				plain[current_tiles[1]][current_tiles[0]] = "P"
				player_block = Block(current_tiles[0],current_tiles[1],'graphics/player.png')
				self.block_group.add(player_block)
				self.player_count += 1
				for tile in check_around(current_tiles):
					plain[current_tiles[1]][current_tiles[0]] = 'p'


			if self.player_count > 0:
				self.bg = pygame.image.load('graphics/level-creator-bg1.png')



		if keys[pygame.K_3]:
			self.block_selected = 'enemy1'
			change_mouse(self.block_selected)
			enemy_valid(current_tiles)





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
		



		self.block_group.draw(win)



		pygame.display.update()