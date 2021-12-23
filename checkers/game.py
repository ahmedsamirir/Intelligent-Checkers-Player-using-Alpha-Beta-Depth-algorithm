import pygame
from checkers.board import Board
from checkers.constants import *

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    #Start _init private method that initialize all properties for the game to start
    def _init(self):
        self.selected = None
        self.board = Board() #Board object creation
        self.turn = WHITE
        self.valid_moves = {}
    #End _init private method that initialize all properties for the game to start

    #Start winner method
    def winner(self):
        return self.board.winner()

    #End winner method

    #Start update method that draw the board and update it
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()
    #End update method that draw the board and update it

    #Start reset method that reset the game
    def reset(self):
        self._init()
    #End reset method that reset the game

    #Start select method to try move the selected piece
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            #if the position that we try to move to is invalid
            if not result:
                self.selected = None
                self.select(row, col) #recursively calling the select method

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True #if the selected piece is valid
        return False #if the selected piece is invalid
    #End select method to try move the selected piece

    #Start move method to handle the moving of the selected piece to the pos we choose
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        #check if there is a selected piece and if the pos that we need to move to is = 0
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False #if the selection method is invalid
        return True #if the selection method is valid
    #End move method to handle the moving of the selected piece to the pos we choos e

    #Start draw_valid_moves method
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, RED, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)
    #End draw_valid_moves method

    #Start change_turn method
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == WHITE:
            self.turn = BLUE
        else:
            self.turn = WHITE
    #End change_turn method

    #Start get_board method
    def get_board(self): #Ahmed samir
        pass
    #End get_board method 

    #Start ai_move method 
    def ai_move(self, board): #adham
        pass
    #End ai_move method 


