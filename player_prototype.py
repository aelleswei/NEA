import pygame
from block_new import Block
from settings2 import *
from math import sqrt,atan2,degrees
from Bullet import Bullet

class Player(pygame.sprite.Sprite):
	def __init__(self,tile_x,tile_y):
		super().__init__()
		self.name = "PLAYER"
		self.image = pygame.image.load('graphics/player.png')
		self.image = pygame.transform.rotozoom(self.image,0,0.8)
		self.rect = self.image.get_rect()
		self.rect[0] = tile_x * 64
		self.rect[1] = tile_y * 64
		self.controls = {'right':pygame.K_d,
				   'left':pygame.K_a,
				   'up':pygame.K_w,
				   'down':pygame.K_s}
		
		self.base_image = self.image
		self.base_image_rect = self.base_image.get_rect()
		self.angle = None
		self.bullet_group = pygame.sprite.Group()
		
		self.shoot_cooldown_base = 10
		self.shoot_cooldown = self.shoot_cooldown_base
		self.old_x = None
		self.old_y = None
		self.health = 10
		self.collided_with_door = False
	
	def display_health_bar(self):
		#print(health_bar)
		pygame.draw.rect(win,'red',(self.rect.centerx - 50, self.rect[1] - 50,100,25))
		pygame.draw.rect(win,'green',(self.rect.centerx - 50,self.rect[1] - 50,self.health * 10,25))
		
	def direction(self):
		speed = 10
		xvel = 0
		yvel = 0
		keys = pygame.key.get_pressed()
		
		if keys[self.controls['left']]:
			xvel = -speed
			

		if keys[self.controls['right']]:
			xvel = speed 

		if keys[self.controls['up']]:
			yvel = -speed

		if keys[self.controls['down']]:
			yvel = speed




		if xvel != 0 and yvel != 0:
			xvel /= sqrt(2)
			yvel /= sqrt(2)
			
		#self.rect[0] += xvel
		#self.rect[1] += yvel
			

		
		if self.rect[0] > 1280:
			self.rect[0] = 1280

		if self.rect[0] < 0 :
			self.rect[0] = 0 

		if self.rect[1] > 768:
			self.rect[1] = 768

		if self.rect[1] < 0 :
			self.rect[1] = 0
	
		return xvel,yvel

	def turning(self):
			
		mouse = pygame.mouse.get_pos()
			
		dx = self.rect.center[0] - mouse[0]
		dy = (self.rect.center[1] - mouse[1]) *-1
			
		self.angle = (degrees(atan2(dy,dx)) + 180) 
		
			
	def shooting(self):
		if pygame.mouse.get_pressed()[0] and self.shoot_cooldown == 0:
			bullet = Bullet(self.rect.center[0],self.rect.center[1],self.angle,50)
			self.bullet_group.add(bullet)
			self.shoot_cooldown = self.shoot_cooldown_base
		if self.shoot_cooldown > 0:
			self.shoot_cooldown -= 1
			
				
	def item_collide(self,block_group):
		collision = pygame.sprite.spritecollide(self,block_group,False)
		if collision != []:
			block = collision[0]
			if block.name == 'ITEM' and block.broken == True:
				block.kill()
				if block.item == 'fr+':
					self.shoot_cooldown_base -= 2
					if self.shoot_cooldown_base < 3:
						self.shoot_cooldown_base = 3
			else:
				pass
	
	# def block_collide(self,block_group,xv,yv):
	# 	collision = pygame.sprite.spritecollideany(self,block_group)
	# 	if collision != None:
	# 		rect = collision.rect
	# 		if xv > 0:
	# 			self.rect.right = rect.left
	# 		if xv < 0:
	# 			self.rect.left = rect.right
	# 		if yv > 0:
	# 			self.rect.bottom = rect.top
	# 		if yv < 0:
	# 			self.rect.top = rect.bottom
	def block_collide(self, block_group, xv, yv):
		# THIS FUNCTION IS (PARTIALLY) AI-GENERATED. THE ATTEMPT AT THE FUNCTION IS ABOVE. USING THE HELP OF CHATGPT IS THE ONLY WAY I COULD GET IT TO WORK.
		self.rect[0] += xv
		x_collision = pygame.sprite.spritecollideany(self, block_group)
		if x_collision != None:
			x_rect = x_collision.rect
			name = x_collision.name
			if name == "ITEM":
				self.item_collide(block_group)
			if name == "DOOR":
				pass
				#print("FINISHED")
			if xv > 0:
				self.rect.right = x_rect.left
			elif xv < 0:
				self.rect.left = x_rect.right

		self.rect[1] += yv
		y_collision = pygame.sprite.spritecollideany(self, block_group)
		if y_collision != None:
			y_rect = y_collision.rect
			name = y_collision.name
			if name == "ITEM":
				self.item_collide(block_group)
			if name == "DOOR":
				#print("FINISHED")
				self.collided_with_door = True
			if yv > 0:
				self.rect.bottom = y_rect.top
			elif yv < 0:
				self.rect.top = y_rect.bottom
			
				
		


				


	def detect_bullets(self,bullet_group):
		bullet_hit_list = pygame.sprite.spritecollide(self,bullet_group,True)
		if bullet_hit_list != []:
			hit = True
		else:
			hit = False
       
		return hit   
   
	def update_health(self,bullet_group):
		hit = self.detect_bullets(bullet_group)
		if hit:
			self.health -= 1
	
		
		

	def update(self,block_group,bullet_group):
			
		xv,yv = self.direction()
		self.turning()
		self.shooting()
		#self.item_collide(block_group)
		self.block_collide(block_group,xv,yv)
		self.display_health_bar()
		self.update_health(bullet_group)
		

		



	def draw(self):
		
		win.blit(self.image,self.rect)
		
		

	












