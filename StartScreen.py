import pygame, sys
from settings2 import *
from button import Button

class StartScreen():

		def __init__(self):
			self.start_button = Button('graphics/start_button.png','graphics/start_button2.png',0,250,'sounds/boom.mp3')
			self.exit_button = Button('graphics/exit_button.png','graphics/exit_button2.png',779,250,'sounds/boom.mp3')
			self.opt_button = Button('graphics/opt_button.png','graphics/opt_button2.png',500,300,'sounds/boom.mp3')
			self.state = "start"

		def run(self):

			pygame.mouse.set_visible(True)

			clock.tick(FPS)
			
			win.fill((COLOUR))

			s_clicked = self.start_button.draw()
			if s_clicked:
				self.state = 'select'

			e_clicked = self.exit_button.draw()
			if e_clicked:
				EXIT()

			self.opt_button.change_size(0.57)
			o_clicked = self.opt_button.draw()
			if o_clicked:
				self.state = 'opt'



			pygame.display.update()
			
		