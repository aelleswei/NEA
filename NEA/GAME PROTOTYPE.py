import pygame,sys,math,time,random,os
import plain
from settings import *
pygame.init()

clock = pygame.time.Clock()
win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT), vsync=1)
#BACKGROUND = pygame.image.load("graphics/man.png")
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)


class Player(pygame.sprite.Sprite):
	def __init__(self,path):
		super().__init__()
		self.image = pygame.image.load(path)
		self.image = pygame.transform.rotozoom(self.image,0,1)
		self.base_image = self.image
		self.rect = self.image.get_rect()
		self.base_image_rect = self.base_image.get_rect()
		self.cooldown = 10
		self.cooldown_base = self.cooldown
		self.enemy_count = 0
		self.map_drawn = False



	def update(self):
	
		mouse = pygame.mouse.get_pos()
		dx = self.rect.center[0] - mouse[0]
		dy = self.rect.center[1] - mouse[1]

		self.angle = math.degrees(math.atan2(dx,dy)) + 90
		#print(self.angle)
		self.image = pygame.transform.rotate(self.base_image, self.angle)
		self.rect = self.image.get_rect(center = self.rect.center)
		pygame.draw.rect(win,'red',self.base_image_rect,1)
		
		

		xvel = 0
		yvel = 0
		keys = pygame.key.get_pressed()
		block_collide = pygame.sprite.spritecollideany(player,blocks)
		
		if keys[pygame.K_d]:
			xvel = 5
			

		if keys[pygame.K_a]:
			xvel = -5
			
		if keys[pygame.K_w]:
			yvel = -5
			

		if keys[pygame.K_s]:
			yvel = 5
			

		


		if xvel != 0 and yvel != 0:
			xvel /= math.sqrt(2)
			yvel /= math.sqrt(2)

		self.rect[0] += xvel
		self.rect[1] += yvel
		self.base_image_rect[0] += xvel
		self.base_image_rect[1] += yvel
		#print(self.rect[0],self.rect[1])
		#pygame.draw.rect(win,'red',self.rect,2)
		#pygame.draw.rect(win,'yellow',self.base_image_rect,2)
		#print(self.rect.center)
		#pygame.draw.circle(win,'red',self.base_image_rect.center,250,width=1)



		self.cooldown -= 1
		if self.cooldown < 0:
			self.cooldown = 0


		if pygame.mouse.get_pressed() == (1,0,0):
			if self.cooldown <= 0:
				self.bullet = self.Bullet(self.rect.center[0],self.rect.center[1],self.angle)
				bullet_group.add(self.bullet)
	
				self.cooldown = self.cooldown_base


		
		







	class Bullet(pygame.sprite.Sprite):
		def __init__(self,xpos,ypos,angle):
			super().__init__()
			self.image = pygame.image.load('graphics/bullet.png')
			self.image = pygame.transform.rotozoom(self.image,angle,0.75)
			self.rect = self.image.get_rect()
			self.rect.center = (xpos,ypos)
			self.x = xpos
			self.y = ypos
			self.speed = BULLET_SPEED
			self.angle = angle
			self.xv = (math.cos(self.angle * (math.pi/180)) * self.speed) 
			self.yv = (math.sin(self.angle * (math.pi/180)) * self.speed) * -1

		def movement(self):
			self.x += self.xv 
			self.y += self.yv
			self.rect.x = int(self.x)
			self.rect.y = int(self.y)

			if self.x > WIN_WIDTH or self.y > WIN_HEIGHT or self.x < -50 or self.y < -50:
				self.kill()

		def update(self):
			self.movement()
			



class Enemy(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = pygame.image.load('graphics/enemy.png')
		self.image = pygame.transform.rotozoom(self.image,0,0.5)
		self.base_image = self.image
		self.base_image_rect = self.base_image.get_rect()
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y


	def update(self):
	

		if self.rect.x > 0:
			self.rect.x += random.randint(0,25)
		elif self.rect.x <= 0:
			self.rect.x = 0
		if self.rect.x < WIN_WIDTH - self.rect.width:
			self.rect.x += random.randint(-25,0)
		elif self.rect.x > WIN_WIDTH - self.rect.width:
			self.rect.x = WIN_WIDTH - self.rect.width
		
		if self.rect.y > 0:
			self.rect.y += random.randint(0,25)
		elif self.rect.y < 0:
			self.rect.y = 0
		if self.rect.y < WIN_HEIGHT - self.rect.height:
			self.rect.y += random.randint(-25,0)
		elif self.rect.y > WIN_HEIGHT - self.rect.height:
			self.rect.y = WIN_HEIGHT - self.rect.height



		pygame.draw.rect(win,'black',self.rect,1)



class Block(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = pygame.image.load('graphics/block.png')
		self.image = pygame.transform.rotozoom(self.image,0,1)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def update(self):
		pygame.draw.rect(win,'yellow',self.rect,1)

class Crosshair(pygame.sprite.Sprite):
	def __init__(self,path):
		super().__init__()
		self.image = pygame.image.load(path).convert_alpha()
		self.image = pygame.transform.rotozoom(self.image,0,0.1)
		self.rect = self.image.get_rect()
		self.gunshot = pygame.mixer.Sound("sounds/boom.mp3")

	def update(self):
		self.rect.center = pygame.mouse.get_pos()



class Target(pygame.sprite.Sprite):
	def __init__(self,path):
		super().__init__()
		self.image = pygame.image.load(path).convert_alpha()
		self.image = pygame.transform.rotozoom(self.image,0,0.1)
		self.rect = self.image.get_rect()
		self.v = 5

	def update(self):
		self.rect.x += self.v
		if self.rect.x >= WIN_WIDTH - self.rect.width:
			self.v *= -1
		if self.rect.x <= 0:
			self.v *= -1


crosshair = Crosshair("graphics/cross.png")
player = Player("graphics/player.png")
target = Target("graphics/target.png")

blocks = pygame.sprite.Group()
other_sprites = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()

other_sprites.add(target)
player_sprite.add(player)
other_sprites.add(crosshair)


bullet_group = pygame.sprite.Group()

run = True

map_drawn = False

while run:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_g]:
		if map_drawn == False:
			map_drawn = True
			for i in range(0,len(plain.plain)):
				y = i * 64
				for j in range(0,len(plain.plain[i])):
					if plain.plain[i][j] == "B":
						x = j * 64
						block = Block(x,y)
						blocks.add(block)

	if keys[pygame.K_ESCAPE]:
		run = False

	win.fill((50,50,50))
	other_sprites.draw(win)
	other_sprites.update()
	bullet_group.draw(win)
	bullet_group.update()
	player_sprite.draw(win)
	player_sprite.update()
	blocks.draw(win)
	blocks.update()
	pygame.display.update()
	

	clock.tick(FPS)






pygame.quit()
sys.exit()
