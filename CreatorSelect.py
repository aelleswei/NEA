import pygame,sys
from settings2 import *
from button import Button

class CreatorSelect():
    
    def __init__(self):
        self.state = "select"
        self.manual = Button('graphics/block.png','graphics/des.png',0,384,'sounds/boom.mp3')
        self.auto = Button('graphics/item.png','graphics/des.png',800,384,'sounds/boom.mp3')
        self.back_button = Button('graphics/exit_button.png','graphics/exit_button2.png',400,0,'sounds/boom.mp3')
        
    def run(self):


        clock.tick(FPS)

        win.fill((COLOUR))

        b_clicked = self.back_button.draw()
        a_clicked = self.auto.draw()
        m_clicked = self.manual.draw()
        if b_clicked:
            self.state = 'start'
        if a_clicked:
            self.state = 'auto'
        if m_clicked:
            self.state = 'manual'
		

		

        pygame.display.update()