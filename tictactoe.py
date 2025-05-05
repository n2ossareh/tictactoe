"""
Tic Tac Toe Player
"""

import math
# import pygame
import sys
# import numpy as np
import copy
import os


X = "X"
O = "O"
EMPTY = None

optimalAction = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if isBoard3x3(board) == False:
        return None

    if terminal(board) == True:
        return None

    occupiedCells = 9 - cellsCount(EMPTY, board)

    if occupiedCells < 9:
        if occupiedCells % 2 == 0:
            return X
        else:
            return O
    else:
        return None



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    
    if isBoard3x3(board) == False:
        return actions

    for i in range(3):
        for j in range(3):
            if board[i][j] is not None:
                continue
            else:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if terminal (board):
        return utility(board)

    new_board = copy.deepcopy(board)

    if action is not None:
      row = action[0]
      col = action[1]
    else:
      return None

    if row != None and col != None:
      if row not in range(3) or col not in range(3):
          raise Exception("out-of-bound index.")
      if new_board[row][col] in {X, O}:
          raise Exception("Cell is occupied")

      new_board[row][col] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if isBoard3x3(board) == False:
        return None

    if isInitialState(board) == True:
        return None

    # Hotizontal
    for i in range(3):
        if (board[i][0] is not None and
            board[i][0] == board[i][1] and
            board[i][1] == board[i][2]):
            return board[i][0]

    # Vertical
    for i in range(3):
        if (board[0][i] is not None and
            board[0][i] == board[1][i] and
            board[1][i] == board[2][i]):
            return board[0][i]

    # Diagnal
    if ((board[1][1] is not None and
        board[0][0] == board[1][1] and
        board[1][1] == board[2][2]) or
        (board[0][2] == board[1][1] and
         board[1][1] == board[2][0])):
        return board[1][1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if isinstance(board, int):
        return False

    # winning combinations
    for row in range (3):
        if (isCellOccupied(board, row, 0) and
            board[row][0] == board[row][1] and
            board[row][1] == board[row][2]):
            return True

    for col in range (3):
        if (isCellOccupied(board, 0, col) and
            board[0][col] == board[1][col] and
            board[1][col] == board[2][col]):
            return True

    if ((isCellOccupied(board, 1, 1) and
        ((board[0][0] == board[1][1] and
        board[1][1] == board[2][2]) or
        (board[0][2] is not None and
         board[0][2] == board[1][1] and
         board[1][1] == board[2][0])))):
        return True


    # possibly drawn
    if cellsCount(EMPTY, board) == 0:
        return True

    return False




def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if board is None:
      sys.exit()

    if isBoard3x3(board) == False:
      if len(board) > 0:
          str_value = board[0]
          if str_value.isdigit():
              return int(str_value)

    if terminal(board):
        _winner = winner(board)
        if _winner == X:
            return 1
        elif _winner == O:
            return -1
        else:
            return 0
    else:
        return None

def minimax(board):
  if terminal(board):
      return None
  
  _player = player(board)
  if _player is None or terminal(board) == True:
        return utility(board)

  if _player == X:
    score = Max_Val(board)[0]
    return score

  if _player == O:
    score = Min_Val(board)[0]
    return score

def Max_Val(board):
    if terminal(board) == True:
        return None, utility(board)

    maxEval = float("-inf")
    best_move = None


    for action in actions(board):
      _, eval = Min_Val(result(board, action))
      if eval > maxEval:
        maxEval = eval
        best_move = action
    return best_move, maxEval

def Min_Val(board):
    if terminal(board) == True:
        return None, utility(board)

    minEval = float("inf")
    best_move = None

    for action in actions(board):
      _, eval = Max_Val(result(board, action))
      if eval < minEval:
        minEval = eval
        best_move = action

    return best_move, minEval


def isCellOccupied(board, row, col):
    if board is not None:
        if row in range(3) and col in range(3):
            if board[row][col] is None:
                return False
            else:
                return True

# returns the count of cells containg piece (X, O or EMPTY) on the given board
def cellsCount(piece, board):
    count = 0
    if board is None or isBoard3x3(board) == False:
        return count

    for i in range(3):
        for j in range(3):
            if board[i][j] == piece:
                count += 1
    return count

def isInitialState(board):
    if cellsCount(EMPTY, board) == 9:
        return True

    return False

def isBoard3x3(board):
    # Check if the board is a list
    if isinstance(board, list):
        # Check if it contains exactly 3 sublists
        if len(board) == 3 and all(isinstance(sublist, list) and len(sublist) == 3 for sublist in list(board)):
            return True
    return False

