import pygame
from checkers.constants import *
from checkers.game import Game
#from Ai_algorithm import alpha_beta_algo

#To render the game in a fixed frames number per second
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#Name of the game
pygame.display.set_caption('Checkers')


#Start get_row_col_from_mouse method to get the position of the piece that mouse clicked
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col
#End get_row_col_from_mouse method to get the position of the piece that mouse clicked

def main():
    run = True 

    #To make the game run in fixed speed
    clock = pygame.time.Clock()

    #To create a board and start the game
    game = Game(WIN)
    
    #Event Loop
    while run:
        #To run the game in a fixed speed -> (f/s)
        clock.tick(FPS)

        #Start To make the ai play
        pass
        #End To make the ai play

        if game.winner() != None:
            print(game.winner)
            run = False #To quit the game if someone is win
        
        #Start check if any event happen in the current time
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos() #return tuple
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
        #End check if any event happen in the current time

        game.update() #To update any change that happens in the game board
    #Quit from the game
    pygame.quit() 

#To call the main function and run the code inside it
main()