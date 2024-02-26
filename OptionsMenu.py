import pygame, sys
from settings2 import *
from button import Button

class OptionsMenu():

	def __init__(self):
		self.image = pygame.image.load('graphics/gabi.png')
		self.back_button = Button('graphics/exit_button.png','graphics/exit_button2.png',400,0,'sounds/boom.mp3')
		self.state = 'opt'

	def run(self):

		clock.tick(FPS)

		win.fill((COLOUR))

		b_clicked = self.back_button.draw()
		if b_clicked:
			self.state = 'start'
			
		

		

		pygame.display.update()
