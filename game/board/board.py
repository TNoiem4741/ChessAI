import pygame 
from game.board import square

class Board:
    #create game board
    def create_board():
        chess_matrix = [] #game board matrix
        color = 0
        #stores a square object in each index of the matrix
        for y in range(8): 
            chess_row = []
            for x in range(8):
                if color % 2 == 0:
                    chess_row.append(square.Square(x, y, (240,235,210)))
                else:
                    chess_row.append(square.Square(x, y, (81, 4, 0)))
                color += 1
            chess_matrix.append(chess_row)
            color -=1 #decrements counter in order to start at the last color of the previous row
        return chess_matrix
    
    #displays board to the game screen
    def show_board(chess_matrix, screen):
        for x in range(8):
            for y in range(8):
                screen.blit(chess_matrix[x][y].image, chess_matrix[x][y].rect)