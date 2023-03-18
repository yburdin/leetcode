from common import *


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.sums = [[0 for _ in range(len(self.matrix[0]) + 1)] for _ in range(len(self.matrix) + 1)]
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[0])):
                self.sums[row+1][col+1] = sum([sum(row_[:col+1]) for row_ in self.matrix[:row+1]])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.sums[row2+1][col2+1] - self.sums[row1][col2+1] - self.sums[row2+1][col1] + self.sums[row1][col1]
        return result


class TestNumMatrix(unittest.TestCase):
    def test_304(self):
        num_matrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
        param_1 = num_matrix.sumRegion(2, 1, 4, 3)
        param_2 = num_matrix.sumRegion(1, 1, 2, 2)
        param_3 = num_matrix.sumRegion(1, 2, 2, 4)

        self.assertEqual(param_1, 8)
        self.assertEqual(param_2, 11)
        self.assertEqual(param_3, 12)

        num_matrix = NumMatrix([[-4, -5]])
        param_1 = num_matrix.sumRegion(0, 0, 0, 0)
        param_2 = num_matrix.sumRegion(0, 0, 0, 1)
        param_3 = num_matrix.sumRegion(0, 1, 0, 1)

        self.assertEqual(param_1, -4)
        self.assertEqual(param_2, -9)
        self.assertEqual(param_3, -5)


if __name__ == '__main__':
    unittest.main()
