# Assets: https://techwithtim.net/wp-contenzt/uploads/2020/09/assets.zip
import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minimax.algorithm import minimax, minimax_alpha_beta, get_moves
import math

FPS = 60
MAX_VALUE = -math.inf
MIN_VALUE = math.inf

counter = 0

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    global counter

    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            number_of_moves = 0
            value, new_board = minimax(game.get_board(), 3, WHITE, game) # The higher the depth the longer it will take to calculate
            #value, new_board = minimax_alpha_beta(game.get_board(), 1, WHITE, game, MAX_VALUE, MIN_VALUE)

            number_of_moves += get_moves(game.get_board(), WHITE, game)
            # print(number_of_moves)
            # number_of_moves -= number_of_moves
            # print(number_of_moves)
            game.ai_move(new_board)

        if game.winner() is not None:
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


main()
