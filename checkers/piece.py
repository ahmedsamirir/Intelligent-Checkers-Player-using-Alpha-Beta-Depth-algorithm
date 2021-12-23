import pygame
from .constants import *

class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    #To draw the pieces in the middle of the squares
    def calc_pos(self):
        self.x = (SQUARE_SIZE*self.col) + (SQUARE_SIZE//2)
        self.y = (SQUARE_SIZE*self.row) + (SQUARE_SIZE//2)

    #To make a king
    def make_king(self):
        self.king = True

    #To draw the pieces (circles)
    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        #Drawing the outline of the circle
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        #Drawing the main circle
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            #(blit) is means put anything like image on the screen 
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    #To Update the piece position after moveing it
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    #To fix any error while drawing pieces by show what we write here
    def __repr__(self):
        return str(self.color)
            


