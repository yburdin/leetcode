import pytest
from typing import List, Tuple
from itertools import product


# 1254. Number of Closed Islands
class NumberOfClosedIslands:
    def __init__(self):
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def closed_island(self, grid: List[List[int]]) -> int:
        land = self.get_land_coordinates(grid)
        visited_land = set()
        islands = 0
        closed_islands = 0

        while land:
            cur_land = land.pop(0)
            if cur_land not in visited_land:
                islands += 1
                closed_island = True
                visited_land.add(cur_land)
                island_queue = [cur_land]
                while island_queue:
                    cur_island = island_queue.pop(0)
                    if self._is_boundary_coordinates(cur_island[0], cur_island[1], grid):
                        closed_island = False

                    for direction in self.directions:
                        i = cur_island[0] + direction[0]
                        j = cur_island[1] + direction[1]
                        if (self._is_viable_land_coordinates(i, j, grid) and
                                (i, j) not in visited_land):
                            visited_land.add((i, j))
                            island_queue.append((i, j))

                if closed_island:
                    closed_islands += 1

        return closed_islands

    @staticmethod
    def _is_viable_land_coordinates(i: int, j: int, grid: List[List[int]]):
        return (0 <= i < len(grid) and 0 <= j < len(grid[0])) and (grid[i][j] == 0)

    @staticmethod
    def _is_boundary_coordinates(i: int, j: int, grid: List[List[int]]):
        return i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1

    @staticmethod
    def get_land_coordinates(grid: List[List[int]]) -> List[Tuple[int, int]]:
        result = []
        for i, j in product(range(len(grid)), range(len(grid[0]))):
            if grid[i][j] == 0:
                result.append((i, j))

        return result


@pytest.mark.parametrize('grid, expected', [
    ([[1, 1, 1, 1, 1, 1, 1, 0],
      [1, 0, 0, 0, 0, 1, 1, 0],
      [1, 0, 1, 0, 1, 1, 1, 0],
      [1, 0, 0, 0, 0, 1, 0, 1],
      [1, 1, 1, 1, 1, 1, 1, 0]], 2),
    ([[0, 0, 1, 0, 0],
      [0, 1, 0, 1, 0],
      [0, 1, 1, 1, 0]], 1),
    ([[1, 1, 1, 1, 1, 1, 1],
      [1, 0, 0, 0, 0, 0, 1],
      [1, 0, 1, 1, 1, 0, 1],
      [1, 0, 1, 0, 1, 0, 1],
      [1, 0, 1, 1, 1, 0, 1],
      [1, 0, 0, 0, 0, 0, 1],
      [1, 1, 1, 1, 1, 1, 1]], 2),
])
def test_closed_islands(grid, expected):
    assert NumberOfClosedIslands().closed_island(grid) == expected


@pytest.mark.parametrize('grid, expected', [
    ([[0, 1],
      [1, 1]], [(0, 0)]),
    ([[0, 1],
      [1, 0]], [(0, 0), (1, 1)]),
])
def test_get_land_coordinates(grid, expected):
    assert NumberOfClosedIslands().get_land_coordinates(grid) == expected
