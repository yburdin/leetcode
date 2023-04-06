from typing import List
from itertools import product
import pytest


# 36. Valid Sudoku
class ValidSudoku:
    def is_valid_sudoku(self, board: List[List[str]]) -> bool:
        return (self._is_valid_rows(board) and
                self._is_valid_columns(board) and
                self._is_valid_sub_boxes(board))

    @staticmethod
    def _is_valid_rows(board: List[List[str]]) -> bool:
        for row in board:
            row_digits = [int(char) for char in row if char.isdigit()]
            if len(set(row_digits)) != len(row_digits):
                return False
        return True

    @staticmethod
    def _is_valid_columns(board: List[List[str]]) -> bool:
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            column_digits = [int(char) for char in column if char.isdigit()]
            if len(set(column_digits)) != len(column_digits):
                return False
        return True

    @staticmethod
    def _is_valid_sub_boxes(board: List[List[str]]) -> bool:
        for start_row, start_col in product([0, 3, 6], [0, 3, 6]):
            sub_box_digits = [board[i][j] for i in range(start_row, start_row + 3) for j in range(start_col, start_col + 3)]
            sub_box_digits = [int(char) for char in sub_box_digits if char.isdigit()]
            if len(set(sub_box_digits)) != len(sub_box_digits):
                return False
        return True


@pytest.mark.parametrize('board, expected', [
    ([["5", "3", ".", ".", "7", ".", ".", ".", "."],
      ["6", ".", ".", "1", "9", "5", ".", ".", "."],
      [".", "9", "8", ".", ".", ".", ".", "6", "."],
      ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
      ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
      ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
      [".", "6", ".", ".", ".", ".", "2", "8", "."],
      [".", ".", ".", "4", "1", "9", ".", ".", "5"],
      [".", ".", ".", ".", "8", ".", ".", "7", "9"]], True),
    ([["8", "3", ".", ".", "7", ".", ".", ".", "."],
      ["6", ".", ".", "1", "9", "5", ".", ".", "."],
      [".", "9", "8", ".", ".", ".", ".", "6", "."],
      ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
      ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
      ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
      [".", "6", ".", ".", ".", ".", "2", "8", "."],
      [".", ".", ".", "4", "1", "9", ".", ".", "5"],
      [".", ".", ".", ".", "8", ".", ".", "7", "9"]], False)
])
def test_is_valid_sudoku(board, expected):
    assert ValidSudoku().is_valid_sudoku(board) == expected
