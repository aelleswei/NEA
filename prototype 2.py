import pygame, sys
from settings2 import *
from StartScreen import StartScreen
from OptionsMenu import OptionsMenu
from MainGame import MainGame
pygame.init()




class State():
	def __init__(self):
		self.state = 'start'



	
game_running = True

state = State()

start_screen = StartScreen()
opt_menu = OptionsMenu()
main_game = MainGame()


while game_running:

	if state.state == 'start':
		start_screen.state = 'start'
		start_screen.run()
		state.state = start_screen.state



	elif state.state == 'opt':
		#opt_menu = OptionsMenu()
		opt_menu.run()
		state.state = opt_menu.state


	elif state.state == 'main':
		#main_game = MainGame()
		main_game.run() 

	clock.tick(60)
	
	

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_running = False


EXIT()