import unittest
from core import *
from random import randint, shuffle

BOARD = [
    [1, 0, 1, 0, 1, 1, -1, 1, 4, 4],
    [1, 0, 1, 0, 1, 1, -1, 1, 4, 4],
    [1, 0, 1, 0, 4, 1, -1, 1, 4, 4],
    [1, 0, 1, 0, 1, 1, 1, 1, 4, 4],
    [1, 0, 1, 0, 1, 1, 1, 1, 4, 4],
    [1, 0, 1, 0, 1, 1, 1, 1, 4, 4],
    [1, 0, 1, 0, 4, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 4, 4],
    [1, 0, 1, 0, 1, 1, 1, 1, 4, 1],
    [1, 0, 1, 0, 1, 1, 4, 4, 4, 4]
]


class CheckTests(unittest.TestCase):

    def test_check_col_for_win_beginning(self):
        c = Core()
        c.board_array = BOARD
        self.assertTrue(c.check_row_and_column_for_a_win(0, 0))

    def test_check_col_for_win_end(self):
        c = Core()
        c.board_array = BOARD
        self.assertTrue(c.check_row_and_column_for_a_win(9, 9))

    def test_check_col_for_win_random(self):
        c = Core()
        c.board_array = BOARD
        self.assertTrue(c.check_row_and_column_for_a_win(3, 4))

    def test_check_diagonals_win_beginning(self):
        c = Core()
        c.board_array = BOARD
        self.assertTrue(c.check_diagonals_for_a_win(0, 0))

    def test_check_diagonals_win_end(self):
        c = Core()
        c.board_array = BOARD
        self.assertFalse(c.check_diagonals_for_a_win(9, 9))

    def test_check_diagonals_win_random(self):
        c = Core()
        c.board_array = BOARD
        self.assertTrue(c.check_diagonals_for_a_win(1, 5))


class GetEmptySpaceTests(unittest.TestCase):

    def test_get_empty_space_in_column(self):
        c = Core()
        c.board_array = BOARD
        self.assertEqual(2, c.get_empty_space_in_column(6))

    def test_get_empty_space_in_column_where_none(self):
        c = Core()
        c.board_array = BOARD
        self.assertEqual(-1, c.get_empty_space_in_column(1))


def main():
    unittest.main()

if __name__ == '__main__':
    main()
