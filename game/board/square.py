import pygame 

class Square(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 100)) #size of square
        self.color = color #color for the square
        self.image.fill(color) #set color for the square
        self.rect = self.image.get_rect() #rectangle object 
        self.rect.x = x*100 #square x position
        self.rect.y = y*100 #square y position
        self.has_piece = False # does this square have a piece on it?
        self.piece = None # if so, what piece is it?
