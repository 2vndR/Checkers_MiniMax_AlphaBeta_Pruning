# Author: https://github.com/techwithtim/Python-Checkers

import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, WHITE
from checkers.game import Game
from minimax.algorithm import minimax_alpha_beta
import tkinter as tk

FPS = 60
depth = 3 # Cambiar a un valor entre 1 y 3 para aumentar o disminuir la dificultad, 

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    
    while run:
        clock.tick(FPS)
        
        # Sección para otorgar control a la IA, para jugar contra un oponente humano, comentar 
        if game.turn == WHITE:
            alpha = float('-inf')
            beta = float('inf')
            value, new_board = minimax_alpha_beta(game.get_board(), depth, alpha, beta, WHITE, game)
            game.ai_move(new_board)
        
        if game.winner() != None:
            print(game.winner())
            run = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
        
        game.update()
        
    pygame.quit()
    
if __name__ == '__main__':
    main()
