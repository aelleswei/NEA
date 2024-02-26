from re import S
import pygame
import random
from player_prototype import Player
from settings2 import *
from level2 import plain
from block_new import Block
from math import sqrt
from LevelCreator import *

class AutoLevelCreator(LevelCreator):
    def __init__(self):
        super().__init__()
        self.place_list = ["B","Bm","Bd","Bi","E","Er","Es"]
        self.special_place_list = ["Bm","Bd","Bi","Er","Es"]
        
    def run(self):
        self.plain_adjacency_dict = self.create_adjacency_dict(plain,self.plain_adjacency_dict)
        print("GENERATING LEVEL...")
        
        for i in range(1,(len(plain) -1)):
            for j in range(1,(len(plain[i]) -1)):
                n = random.randint(1,100)
                #print(n)
                if n <= 60:
                    if n <= 30:
                        item = "B"
                    else:
                        item = "E"
                else:
                    n = ((n // 10) - 6)
                    item = self.special_place_list[n]
                    
                
                #item = random.choice(self.place_list)
                current = (j,i)
                if item[0] == "B" and item != "B":
                    valid = self.block_valid(current,item)
                    valid = self.check_if_surrounded(current)
                    if valid == True:
                        plain[i][j] = item
                if item == "B":
                    valid = self.block_valid(current,item)
                   
                    if valid == True:
                        plain[i][j] = item
                if item[0] == "E":
                    #print("ENEMY AT",current)
                    valid = self.enemy_valid(current,item)
                    if valid == True:
                        plain[i][j] = item
                        self.enemy_count += 1
                    #print(self.enemy_count)
        
      
        self.state = 'main'
       
                
                    
                
                
