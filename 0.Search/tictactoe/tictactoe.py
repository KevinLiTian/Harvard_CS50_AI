"""
Tic Tac Toe Player
"""

import copy
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
    num_x = 0
    num_o = 0
    for row in board:
        for col in row:
            if col == X:
                num_x += 1
            if  col == O:
                num_o += 1

    if num_o == num_x:
        return X

    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                possible_actions.add((row, col))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row = action[0]
    col = action[1]

    if board[row][col] != EMPTY:
        raise Exception("The move is invalid, please check your move")

    board_copy = copy.deepcopy(board)

    turn = player(board_copy)

    board_copy[row][col] = turn

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #Row check
    for row in range(3):
        candidate = board[row][0]
        if candidate is not None and candidate == board[row][1] and candidate == board[row][2]:
            return candidate

    #Column check
    for col in range(3):
        candidate = board[0][col]
        if candidate is not None and candidate == board[1][col] and candidate == board[2][col]:
            return candidate

    #Diagonals check
    candidate = board[1][1]
    if candidate is not None and (candidate == board[0][0] and candidate == board[2][2]) or \
    (candidate == board[0][2] and candidate == board[2][0]):
        return candidate

    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is None:
        for row in board:
            for col in row:
                if col == EMPTY:
                    return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    potential_winner = winner(board)
    if potential_winner == X:
        return 1
    elif potential_winner == O:
        return -1
    else:
        return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        cur_result = (None, -math.inf)
        for action in actions(board):
            score = minimax_algorithm(result(board, action), False)
            if score == 1:
                return action
            if score > cur_result[1]:
                cur_result = (action, score)

        return cur_result[0]


    cur_result = (None, math.inf)
    for action in actions(board):
        score = minimax_algorithm(result(board, action), True)
        if score == -1:
            return action
        if score < cur_result[1]:
            cur_result = (action, score)

    return cur_result[0]


def minimax_algorithm(board, max_min_player):
    """ The AI player logic recursive algorithm to get the optimal move """
    if terminal(board):
        return utility(board)

    if max_min_player:
        cur_score = -math.inf
        for action in actions(board):
            new_board = result(board, action)
            cur_score = max(cur_score, minimax_algorithm(new_board, False))

        return cur_score

    elif not max_min_player:
        cur_score = math.inf
        for action in actions(board):
            new_board = result(board, action)
            cur_score = min(cur_score, minimax_algorithm(new_board, True))

        return cur_score
