from copy import deepcopy

import pygame
WHITE = (255,255,255)
BLUE = (0, 0, 255)

#start alpha beta depth first algo method
def alpha_beta_algo(board, depth, alpha, beta, max_player, game):
    #check if we reach the end depth of the decision tree
    if depth == 0 or board.winner() != None:
        #if true start to evaluate the states up
        return board.evaluate(), board

    #check if the ai try to maximize the score or minimize it and play based on that
    if max_player == BLUE: #maximize the score
        #if the ai don't checked anything in a specific position then it will be -inf
        maxEval = float('-inf') 
        best_move = None
        for move in get_all_moves(board, BLUE, game):
            #recursive call to go to the last depth in the decision tree
            evaluation = alpha_beta_algo(move, depth-1, alpha, beta, False, game)[0]
            #To check if the new state evaluation is better than maxEval that we have now
            maxEval = max(maxEval, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move
    else:
        #if the ai don't checked anything in a specific position then it will be -inf
        minEval = float('inf') 
        best_move = None
        for move in get_all_moves(board, WHITE, game):
            #recursive call to go to the last depth in the decision tree
            evaluation = alpha_beta_algo(move, depth-1, alpha, beta, True, game)[0]
            #To check if the new state evaluation is better than minEval that we have now
            minEval = min(minEval, evaluation)
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
            if minEval == evaluation:
                best_move = move
        return minEval, best_move
#End alpha beta depth first algo method

#Start simulate method
def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove_piece(skip)
    return board


#End simulate method

#Start get_all_moves method
def get_all_moves():
    pass
#End get_all_moves method

