import pygame
from player_prototype import Player
from settings2 import *

class MainGame():
	def __init__(self):
		self.player = Player()
		


	def run(self):
		clock.tick(FPS)
		win.fill((COLOUR))


		self.player.draw()

		pygame.display.update()