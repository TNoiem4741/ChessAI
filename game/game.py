import pygame 
from game.board import board

class game:
    def start_game(screen):
        chess_matrix = board.Board.create_board() #create a game board
        board.Board.show_board(chess_matrix, screen) #display board game onto screen
        clock = pygame.time.Clock() #frame rate object
        running = True
        # game loop
        while running:
            clock.tick(60) # 60 fps cap
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: running = False # quit game
            pygame.display.update() # update screen
