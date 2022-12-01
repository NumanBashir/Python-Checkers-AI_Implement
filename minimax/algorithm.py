from copy import deepcopy
import time
from logging import root

import pygame
import math

RED = (255, 0, 0)
WHITE = (255, 255, 255)

counter = 0
leaf = 0


def minimax(position, depth, is_max, game):
    start = time.time()
    global counter
    global leaf

    if depth == 0 or position.winner() is not None:
        leaf += 1
        return position.evaluate(), position

    if is_max:
        maxEval = -math.inf
        bestMove = None
        for move in get_all_moves(position, WHITE, game):
            counter += 1
            eval = minimax(move, depth-1, False, game)[0]
            if eval > maxEval:
                bestMove = move
                maxEval = eval


        end = time.time()
        print('Evaluation time: {}s'.format(round(end - start, 7)))
        print(f"Number of moves: {counter}")
        print(f"Number of leaves: {leaf}")
        return maxEval, bestMove
    else:
        minEval = math.inf
        bestMove = None
        for move in get_all_moves(position, RED, game):
            counter += 1
            eval = minimax(move, depth-1, True, game)[0]
            if eval < minEval:
                bestMove = move
                minEval = eval

        end = time.time()
        print('Evaluation time: {}s'.format(round(end - start, 7)))
        print(f"Number of moves: {counter}")
        print(f"Number of leaves: {leaf}")
        return minEval, bestMove


def minimax_alpha_beta(position, depth, is_max, game, alpha, beta):
    start = time.time()
    global counter
    global leaf

    if depth == 0 or position.winner() is not None:
        leaf += 1
        return position.evaluate(), position

    if is_max:
        maxEval = -math.inf
        bestMove = None
        for move in get_all_moves(position, WHITE, game):
            counter += 1
            evaluation = minimax_alpha_beta(move, depth-1, False, game, alpha, beta)[0]
            if evaluation > maxEval:
                bestMove = move
                maxEval = evaluation
            alpha = max(alpha, maxEval)
            if (beta <= alpha):
                counter -= 1
                break


        end = time.time()
        print('Evaluation time: {}s'.format(round(end - start, 7)))
        print(f"Number of moves: {counter}")
        print(f"Number of leaves: {leaf}")
        #print(f"max val = {maxEval}")
        return maxEval, bestMove

    else:
        minEval = math.inf
        bestMove = None
        for move in get_all_moves(position, RED, game):
            counter += 1
            evaluation = minimax_alpha_beta(move, depth-1, True, game, alpha, beta)[0]
            if evaluation < minEval:
                bestMove = move
                minEval = evaluation
            beta = min(beta, minEval)
            if (beta <= alpha):
                counter -= 1
                break


        end = time.time()
        print('Evaluation time: {}s'.format(round(end - start, 7)))
        print(f"Number of moves: {counter}")
        print(f"Number of leaves: {leaf}")
        #print(f"min val = {minEval}")
        return minEval, bestMove


def get_moves(position, color, game):
    global counter
    global leaf
    counter = 0
    leaf = 0
    for move in get_all_moves(position, color, game):
        counter += 1
        leaf += 1

    return counter


def simulation_of_move(piece, move, board, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color, game):
    moves = []
    leaves = []

    for piece in board.get_all_pieces(color):
        applicable_move = board.get_valid_moves(piece)  # Get all the valid moves for the given piece
        for move, skip in applicable_move.items():
            temporary_board = deepcopy(board)
            temporary_piece = temporary_board.get_piece(piece.row, piece.col)
            new_board = simulation_of_move(temporary_piece, move, temporary_board, skip)
            moves.append(new_board)

    return moves
