from common import *


class NumIslands:
    def __init__(self):
        self.number_of_islands = 0
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visit = [[0 for _ in range(cols)] for _ in range(rows)]

        for i, j in product(range(rows), range(cols)):
            if not visit[i][j]:
                visit[i][j] = 1

                if grid[i][j] == '1':
                    self.number_of_islands += 1
                    self._dfs(i, j, grid, visit)

        return self.number_of_islands

    def _dfs(self, row, col, grid, visit):
        visit[row][col] = 1
        for direction in self.directions:
            i = row + direction[0]
            j = col + direction[1]

            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                if not visit[i][j] and grid[i][j] == '1':
                    self._dfs(i, j, grid, visit)


class TestNumIslands(unittest.TestCase):
    def test_example_1(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]

        sol = NumIslands()
        res = sol.numIslands(grid)

        self.assertEqual(res, 1)

    def test_example_2(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]

        sol = NumIslands()
        res = sol.numIslands(grid)

        self.assertEqual(res, 3)


if __name__ == '__main__':
    unittest.main()
