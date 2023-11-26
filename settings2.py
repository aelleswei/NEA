import pygame,sys
W_WIDTH = 1280
W_HEIGHT = 768
COLOUR = (50,50,50)
win = pygame.display.set_mode((W_WIDTH,W_HEIGHT), vsync=1)
clock = pygame.time.Clock()
FPS = 60

def EXIT():
	pygame.quit()
	sys.exit()