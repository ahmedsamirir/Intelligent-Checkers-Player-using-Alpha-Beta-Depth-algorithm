import pygame
from .constants import *
from .piece import Piece

####################
## Methods need edit ##
# 
# 
####################

class Board:
    def __init__(self):
        self.board = [] #[[]
                        # [1, 0, 1]]
        #The number of pieces still on the board
        self.blue_left = self.white_left = 12
        self.blue_kings = self.white_kings = 0
        self.create_pieces()


    #Start creation of squares
    def create_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            #To start with different color in every row
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, BLUE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)) #StartX, StartY, EndX, EndY 
    #End creation of squares

    #Start evaluate method 
    def evaluate(self):
        # Function (1)
        return self.blue_left - self.white_left
        # Function (2)
        # return self.blue_left - self.white_left + (self.blue_kings * 0.5 - self.white_kings * 0.5)
    #End evaluate method

    #Start get_all_pieces method
    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces
    #End get_all_pieces method

    #Start creation of move method that makes the moving of the piece to the position that we select
    def move(self, piece, row, col):
        #Swapping the position of the piece and the position that we need to move to
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        #To Update the piece position after moveing it
        piece.move(row, col)

        #if the piece reach the last square in the board it will be king by this coming code
        if row == ROWS-1 or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings +=1
            else:
                self.blue_kings +=1
    #End creation of move method that makes the moving of the piece to the position that we select

    #To give us the piece in a specific row and col from tha list of pieces
    def get_piece(self, row, col):
        return self.board[row][col]

    #Start creation of pieces in the list
    def create_pieces(self):
        for row in range(ROWS):
            #To represent the list of row inside the board
            self.board.append([])
            for col in range(COLS):
                #To draw pieces in the first and last 4 rows
                if col % 2 == ((row + 1) % 2):
                    #To added pieces to the first 4 rows
                    if row < 3:
                        #append the white pieces for the board array
                        self.board[row].append(Piece(row, col, BLUE))
                    #To added pieces to the last 4 rows
                    elif row > 4:
                        #append the blue pieces for the board array
                        self.board[row].append(Piece(row, col, WHITE))
                    else:
                        #append the empty squares
                        self.board[row].append(0)
                else:
                    #append the empty squares
                    self.board[row].append(0)
    #End creation of pieces in the list

    #Start drawing the board (pieces and squares)
    def draw(self, win):
        self.create_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:  #To check that the piece that we take is not 0
                    piece.draw(win)
    #End drawing the board (pieces and squares)

    #Start remove method to remove the piece that crashed
    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece !=0: #check if the piece is already deleted or not
                if piece.color == WHITE:
                    self.white_left -= 1
                else:
                    self.blue_left -= 1
    #End remove method to remove the piece that crashed

    #Start winner method (need Edit)
    def winner(self):
        if self.white_left <= 0:
            return BLUE
        elif self.blue_left <= 0:
            return WHITE
        return None
    #End winner method

    #Start get_valid_moves method to give us all valid moves for the specific piece
    def get_valid_moves(self, piece):
        moves = {} #key = move and value = the pieces jumped over
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        #if the piece is king it can move up and down
        if piece.color == WHITE or piece.king: 
            #To update the moves dic with the valid moves for White pieces
            moves.update(self._traverse_left(row-1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row-1, max(row-3, -1), -1, piece.color, right))

        #if the piece is king it can move up and down
        if piece.color == BLUE or piece.king: 
            #To update the moves dic with the valid moves for Blue pieces
            moves.update(self._traverse_left(row+1, min(row+3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row+1, min(row+3, ROWS), 1, piece.color, right))

        return moves
    #End get_valid_moves method to give us all valid moves for the specific piece

    #Start _traverse_left method to determine the valid moves for the piece from left side
    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped: #double jumping
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._traverse_left(r+step, row, step, color, left-1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, left+1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            left -= 1
        return moves
    #End _traverse_left method to determine the valid moves for the piece from left side

    #Start _traverse_right method to determine the valid moves for the piece from right side
    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._traverse_left(r+step, row, step, color, right-1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, right+1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            right += 1
        return moves
    #End _traverse_left method to determine the valid moves for the piece from right side

