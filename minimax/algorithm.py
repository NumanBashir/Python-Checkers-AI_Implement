from copy import deepcopy
import time
from logging import root

import pygame
import math

RED = (255, 0, 0)
WHITE = (255, 255, 255)

counter = 0

def minimax(position, depth, is_max, game):
    global counter

    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    
    if is_max:
        maxEval = -math.inf
        bestMove = None
        for move in get_all_moves(position, WHITE, game):
            counter += 1
            evaluation = minimax(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                bestMove = move

        print(counter)
        return maxEval, bestMove
    else:
        minEval = math.inf
        bestMove = None
        for move in get_all_moves(position, RED, game):
            counter += 1
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                bestMove = move

        print(counter)
        return minEval, bestMove



def minimax_alpha_beta(position, depth, is_max, game, alpha, beta):
    global counter

    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    
    if is_max:
        maxEval = -math.inf
        bestMove = None
        for move in get_all_moves(position, WHITE, game):
            counter += 1
            evaluation = minimax_alpha_beta(move, depth-1, False, game, alpha, beta)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                bestMove = move
            if alpha <= beta:
                counter -= 1
                break

        print(counter)
        return maxEval, bestMove

    else:
        minEval = float("inf")
        bestMove = None
        for move in get_all_moves(position, RED, game):
            counter += 1
            evaluation = minimax_alpha_beta(move, depth-1, True, game, alpha, beta)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                bestMove = move
            if alpha <= beta:
                counter -= 1
                break

        print(counter)
        return minEval, bestMove

def get_moves(position, color, game):
    global counter
    counter = 0
    for move in get_all_moves(position, color, game):
        counter += 1

    return counter


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board

def get_all_moves(board, color, game):
    moves = []
    leaves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece) #Get all the valid moves for the given piece
        for move, skip in valid_moves.items():
            #draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves


def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0,255,0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    pygame.time.delay(250)


