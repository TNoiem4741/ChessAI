import pygame
import sys
from game.board import square

class Main:
    def __init__(self):
        # pygame setup
        pygame.init() # init pygame
        pygame.display.set_caption("ChessAI") #set window title
        self.screen = pygame.display.set_mode((800, 800)) #set dimensions
        clock = pygame.time.Clock() #frame rate object
        running = True
        one = square.Square(0, 0, (255, 50, 100))
        # game loop
        while running:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: running = False # quit game
            #display the red square on screen
            self.screen.blit(one.image, one.rect)
            clock.tick(60) # 60 fps cap
            pygame.display.update() # update screen
Main()
