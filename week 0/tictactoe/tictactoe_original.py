"""
Tic Tac Toe Player
"""

import math
import copy

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
    # x starts first
    x = 0 
    o = 0
    for i in range(3):
        for j in range(3):
            if (board[i][j]=="X"):
                x += 1
            if (board[i][j]=="O"):
                o += 1
    if (x>o):
        return O
    elif (not terminal(board) and x==o):
        return X
    else:
        return None
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return None
    actions  = []
    for i in range(3):
        for j in range(3):
            if (board[i][j]==EMPTY):
                actions.append((i,j))
    actions_ = set(actions)
    
    return actions_


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if actions(board) is not None:
        if action not in actions(board):
            raise ValueError('Not permitted action')
    else:
        return board
    
    p = player(board)
    i = action[0]
    j = action[1]
    new_board = copy.deepcopy(board)
    new_board[i][j] = p
    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check the rows
    sumx = 0
    sumo = 0
    for i in range(3):
        sumx = 0
        sumo = 0
        for j in range(3):
            if board[i][j]==X:
                sumx += 1
            if board[i][j]==O:
                sumo += 1
        if sumx==3:
            return X
        if sumo==3:
            return O
            
    
    # check the columns
    sumx = 0
    sumo = 0
    for j in range(3):
        sumx = 0
        sumo = 0
        for i in range(3):
            if board[i][j]==X:
                sumx += 1
            if board[i][j]==O:
                sumo += 1
        if sumx==3:
            return X
        if sumo==3:
            return O
            
    # check the diagonals
    sumx = 0
    sumo = 0
    for i in range(3):
        if board[i][i]==X:
            sumx += 1
        if board[i][i]==O:
            sumo += 1
    if sumx==3:
        return X
    if sumo==3:
        return O
        
    sumx = 0
    sumo = 0
    for i in range(2,-1,-1):
        if board[i][2-i]==X:
            sumx += 1
        if board[i][2-i]==O:
            sumo += 1
    if sumx==3:
        return X
    if sumo==3:
        return O
    
    return None
    
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    over = True
    win = winner(board)
    if win != None:
        return True
    
    # if no-one has won yet, we check if there is
    # an empty tile. If yes, we are not in a terminal state
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                over = False
    
    return over
    
   
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win==X:
        return 1
    elif win==O:
        return -1
    else:
        return 0
    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    p = player(board)
    best_action = (0,0)
    
    if terminal(board):
        return None
    # calculate the value for the current state
    # with respect to all possible actions
    if p == X:
        value = float('-inf')
        for action in actions(board):
            next_state = result(board,action)
            v = min_value(next_state)
            if v >= value:
                value = v
                best_action = action
    elif p == O:
        value = float('inf')
        for action in actions(board):
            next_state = result(board,action)
            v = max_value(next_state)
            if v <= value:
                value = v
                best_action = action
    
    return best_action
       
        
def max_value(board):
    
    if terminal(board):
        return utility(board)
    v = float('-inf')
    # for any action that starts from this state
    # recursively check the value of the state
    for action in actions(board):
        v = max(v,min_value(result(board,action)))
    return v   


def min_value(board):
    
    if terminal(board):
        return utility(board)
        
    v = float('inf')
    for action in actions(board):
        v = min(v,max_value(result(board,action)))
    return v