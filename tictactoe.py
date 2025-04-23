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
    if cellsCount(EMPTY, board) == 9:
        return X

    # if terminal(board):
    #     return None 

    countX = cellsCount(X, board)
    countO = cellsCount(O, board)

    takenCells = countX + countO
    if takenCells < 9 and takenCells % 2 == 0:
        return X
    else:
        return O
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                continue
            else:
                actions.add((i, j))
    
    
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    countX = cellsCount(X, board)
    countO = cellsCount(O, board)
    row = action[0]
    col = action[1]
    if (countX == countO):
        board[row][col] = X
    else:
        board[row][col] = O

    return board


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
    # winning combinations
    for row in range (3):
        if board[row][0] != EMPTY and board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            return True
    
    for col in range (3):
        if board[0][col] != EMPTY and board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            return True

    if board[0][0] != EMPTY and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return True

    if board[0][2] != EMPTY and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return True 

    # possibly drawn
    if cellsCount(EMPTY, board) == 0:
        return True
    
    return False    




def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if isInitialState(board) == True:
        return 0
    

    countX = cellsCount(X, board)

    countO = cellsCount(O, board)

    if countX + countO %2 == 0:
        return X
    else:
        return O


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    moves = actions(board)
    return moves[0]

# returns the count of cells containg piece (X, O or EMPTY) on the given board    
def cellsCount(piece, board):
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == piece:
                count += 1
    return count

def isInitialState(board):
    if cellsCount(EMPTY, board) == 9:
        return True

    return False 
        
