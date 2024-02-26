import pygame, sys
from settings2 import *
from StartScreen import StartScreen
from OptionsMenu import OptionsMenu
from LevelCreator import LevelCreator
from MainGame import MainGame
from AutoLevelCreator import AutoLevelCreator
from CreatorSelect import CreatorSelect
pygame.init()




class State():
	def __init__(self):
		self.state = 'start'
		self.previous_state = None



	
game_running = True

state = State()

start_screen = StartScreen()
opt_menu = OptionsMenu()
level_creator = LevelCreator()
auto_creator = AutoLevelCreator()
main_game = MainGame()
creator_select = CreatorSelect()


while game_running:

	if state.state == 'start':
		start_screen.state = 'start'
		start_screen.run()
		state.state = start_screen.state



	elif state.state == 'opt':
		opt_menu.state = "opt"
		opt_menu.run()
		state.state = opt_menu.state

	elif state.state == 'select':
		creator_select.state = 'select'
		creator_select.run()
		state.state = creator_select.state
		
	elif state.state == 'main':
		main_game.run(state.previous_state)
		state.state = main_game.state
		




		
	elif state.state == 'manual':
		level_creator.state = "manual"
		#level_creator = LevelCreator()
		state.previous_state = 'manual'
		#level_creator = LevelCreator()
		level_creator.run()
		state.state = level_creator.state
	
	elif state.state == 'auto':
		auto_creator.state = "auto"
		state.previous_state = 'auto'
		#auto_creator = AutoLevelCreator()
		auto_creator.run()
		#state.state = auto_creator.state
		state.state = auto_creator.state
		if auto_creator.state == "main":
			main_game.state = "main"
	clock.tick(FPS)
	print(f"CURRENT STATE IS {state.state}, {main_game.state}")


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_running = False


EXIT()