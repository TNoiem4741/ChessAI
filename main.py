import pygame
from game import game

class Main:
    def __init__(self):
        pygame.init() # init pygame
        self.screen = pygame.display.set_mode((800, 800)) #set screen dimensions
        pygame.display.set_caption("ChessAI") #set screen title
        game.game.start_game(self.screen) #begin the game
        
Main()
