import pieces.piece as piece
import pygame

class pawn(pieces.piece):
    def __init__(self, color, x, y):
        self.name = "pawn"
        self.color = color
        self.position = [x,y]
        self.alive = True
        self.legal_moves = []
    def get_legal_moves:
        