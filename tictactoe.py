"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


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
    if terminal(board):
        return None
    
    sumX = 0
    sumO = 0
    for i in range(3):
        for j in range(3):
            cell = board[i][j]
            if cell == EMPTY:
                continue
            if cell == X:
                sumX += 1
            else:
                sumO -= 1
    
    if sumX + sumO == 0:
        return 1  # x-player
    else:
        return -1 # o-player



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.append((i, j))
    
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if terminal(board) == True:
        return utility(board)


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for row in range (3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            return True
    
    for col in range (3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            return True

    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return True

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return True 

    return False    




def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    sumX = 0
    SumO = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                continue
            if board[i][j] == X:
                sumX += 1
            else:
                sumO -= 1

    if sumX + sumO == 0:
        return -1
    elif sumX + sumO == 1:
        return 1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
