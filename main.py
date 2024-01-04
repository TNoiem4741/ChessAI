import pygame
import sys

class Main:
    def __init__(self):
        # pygame setup
        pygame.init() # init pygame
        pygame.display.set_caption("ChessAI") #set window title
        self.screen = pygame.display.set_mode((800, 800)) #set dimensions
        clock = pygame.time.Clock() #frame rate object
        running = True
        # game loop
        while running:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: running = False # quit game
            clock.tick(60) # 60 fps cap

Main()
