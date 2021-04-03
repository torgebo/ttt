"""We represent a Tic Tac Toe board as a two dimensional
3x3 list, each cell containing one of ' ', 'X', 'O'.
"""

def print_board(board):
    print(*board, sep='\n')

    
def has_won(board):
    """Given board, return 
    - ' ' if no player has yet won
    - 'X' if player 'X' has won
    - 'O' if player 'O' has won.

    Note
    ----

    We assume board has at most one winning player.
    """
    win_X = has_won_player(board, player='X')
    if win_X:
        return 'X'

    win_O = has_won_player(board, player='O')
    if win_O:
        return 'O'

    return ' '


def has_won_player(board, player):
    """`player` is given as 'X' or 'O'

    Returns True if there is a winning position
    for `player`, otherwise False.
    """
    diag1 = True
    diag2 = True
    for i in range(len(board)):
        if board[i][i] != player:
            diag1 = False
        if board[i][2-i] != player:
            diag2 = False
    if diag1 or diag2:
        return True
            
    return False
