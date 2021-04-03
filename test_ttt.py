import unittest

from ttt import (
    has_won,
    print_board,
)

board1 = [
    ['X', 'X', 'X'],
    ['O', ' ', 'O'],
    [' ', 'O', ' '],
]


board2 = [
    ['X', ' ', ' '],
    ['O', 'X', 'O'],
    [' ', 'O', 'X'],
]



class TestTicTacToe(unittest.TestCase):

    def test_wins_board_1(self):
        print_board(board1)
        winner = has_won(board1)
        print("winner", winner)

    def test_wins_board_2(self):
        print_board(board2)
        winner = has_won(board2)
        print("winner", winner)
        self.assertEqual(winner, 'X')
