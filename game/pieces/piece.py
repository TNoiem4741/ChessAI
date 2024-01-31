class piece(pygame.sprite.Sprite):
    def __init__(self, name, color, x, y):
        self.name = name
        self.color = color
        self.position = [x,y]
        self.alive = True
        self.legal_moves = []
    def move(self, x, y):
        self.position = [x,y]
    def kill(self):
        self.alive = False
    def get_legal_moves(self):
        pass;