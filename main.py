import pygame
from game.board import board

class Main:
    def __init__(self):
        # pygame setup
        pygame.init() # init pygame
        pygame.display.set_caption("ChessAI") #set window title
        self.screen = pygame.display.set_mode((800, 800)) #set dimensions
        chess_matrix = board.Board.create_board() #create a game board
        clock = pygame.time.Clock() #frame rate object
        running = True
        
        # game loop
        while running:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: running = False # quit game
            board.Board.show_board(chess_matrix, self.screen) #display board game onto screen
            clock.tick(30) # 30 fps cap
            pygame.display.update() # update screen
Main()
