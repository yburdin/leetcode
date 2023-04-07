import pytest
from typing import List


# 74. Search a 2D Matrix
def search_matrix(matrix: List[List[int]], target: int) -> bool:
    row_left = 0
    row_right = len(matrix) - 1
    while row_left < row_right:
        row_mid = (row_left + row_right) // 2
        start_value = matrix[row_mid][0]
        end_value = matrix[row_mid][-1]
        if start_value == target or end_value == target:
            return True
        elif start_value > target or end_value > target:
            row_right = row_mid
        else:
            row_left = row_mid + 1

    row = matrix[row_left]
    col_left = 0
    col_right = len(row) - 1
    while col_left < col_right:
        col_mid = (col_left + col_right) // 2
        value = row[col_mid]
        if value == target:
            return True
        elif value < target:
            col_left = col_mid + 1
        else:
            col_right = col_mid

    if row[col_left] == target:
        return True

    return False


@pytest.mark.parametrize('matrix, target, expected', [
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
    ([[1]], 1, True),
    ([[1], [3]], 1, True),
])
def test_search_matrix(matrix, target, expected):
    assert search_matrix(matrix, target) == expected
