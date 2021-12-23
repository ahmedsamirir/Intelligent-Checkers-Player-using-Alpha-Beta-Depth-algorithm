import pygame


#Start minimax_to_alphabeta algorithm
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
            evaluation = minimax_to_alphabeta(move, depth-1, alpha, beta, False, game)[0]
            #To check if the new state evaluation is better than maxEval that we have now
            maxEval = max(maxEval, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move
    else:
        pass


    
#End minimax_to_alphabeta algorithm

#Start simulate method
def simulate_move():
    pass
#End simulate method

#Start get_all_moves method
def get_all_moves():
    pass
#End get_all_moves method

