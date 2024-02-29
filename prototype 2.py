import pygame, sys
from settings2 import *
from StartScreen import StartScreen
from OptionsMenu import OptionsMenu
from LevelCreator import LevelCreator
from MainGame import MainGame
from AutoLevelCreator import AutoLevelCreator
from CreatorSelect import CreatorSelect
from level2 import plain
pygame.init()




class State():
	def __init__(self):
		self.state = 'start'
		self.previous_state = None
		self.changed = False
		self.base_plain = [


["B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B"],
["B","","","","","","","","","","","","","","","","","","","B"],
["B","","","","","","","","","","","","","","","","","","","B"],
["B","","","","","","","","","","","","","","","","","","","B"],
["B","","","","","","","","","","","","","","","","","","","B"],
["p","","","","","","","","","","","","","","","","","","","d"],
["B","","","","","","","","","","","","","","","","","","","B"],
["B","","","","","","","","","","","","","","","","","","","B"],
["B","","","","","","","","","","","","","","","","","","","B"],
["B","","","","","","","","","","","","","","","","","","","B"],
["B","","","","","","","","","","","","","","","","","","","B"],
["B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B"],

]


	
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
		if state.changed:
			main_game = MainGame()
		state.changed = False
		main_game.run(state.previous_state)
		state.state = main_game.state
		




		
	elif state.state == 'manual':
		if state.changed:
			level_creator = LevelCreator()
			
		level_creator.state = "manual"
		#level_creator = LevelCreator()
		state.previous_state = 'manual'
		#level_creator = LevelCreator()
		level_creator.run()
		state.state = level_creator.state
		if level_creator.state == "main":
			state.changed = True
	
	elif state.state == 'auto':
		if state.changed:
			auto_creator = AutoLevelCreator()
			auto_creator.plain = state.base_plain
		auto_creator.state = "auto"
		state.changed = True
		state.previous_state = 'auto'
		#auto_creator = AutoLevelCreator()
		auto_creator.run()
		#state.state = auto_creator.state
		state.state = auto_creator.state
		

	
		
	clock.tick(FPS)
	#print(f"CURRENT STATE IS {state.state}, MAIN GAME STATE IS {main_game.state}")
	#print(state.base_plain)
	#print(state.changed)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_running = False


	
EXIT()