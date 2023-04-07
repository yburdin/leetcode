import pytest
from typing import List, Tuple
from itertools import product


# 1020. Number of Enclaves
class NumberOfEnclaves:
    def __init__(self):
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def num_enclaves(self, grid: List[List[int]]) -> int:
        land = self.get_land_coordinates(grid)
        visited_land = set()
        enclave = 0

        while land:
            cur_land = land.pop(0)
            if cur_land not in visited_land:
                is_enclave = True
                enclaved_land = 1
                visited_land.add(cur_land)
                island_queue = [cur_land]
                while island_queue:
                    cur_island = island_queue.pop(0)
                    if self._is_boundary_coordinates(cur_island[0], cur_island[1], grid):
                        is_enclave = False

                    for direction in self.directions:
                        i = cur_island[0] + direction[0]
                        j = cur_island[1] + direction[1]
                        if (self._is_viable_land_coordinates(i, j, grid) and
                                (i, j) not in visited_land):
                            visited_land.add((i, j))
                            island_queue.append((i, j))
                            enclaved_land += 1

                if is_enclave:
                    enclave += enclaved_land

        return enclave

    @staticmethod
    def _is_viable_land_coordinates(i: int, j: int, grid: List[List[int]]):
        return (0 <= i < len(grid) and 0 <= j < len(grid[0])) and (grid[i][j] == 1)

    @staticmethod
    def _is_boundary_coordinates(i: int, j: int, grid: List[List[int]]):
        return i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1

    @staticmethod
    def get_land_coordinates(grid: List[List[int]]) -> List[Tuple[int, int]]:
        result = []
        for i, j in product(range(len(grid)), range(len(grid[0]))):
            if grid[i][j] == 1:
                result.append((i, j))

        return result


@pytest.mark.parametrize('grid, expected', [
    ([[0, 0, 0, 0],
      [1, 0, 1, 0],
      [0, 1, 1, 0],
      [0, 0, 0, 0]], 3),
    ([[0, 1, 1, 0],
      [0, 0, 1, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 0]], 0),
])
def test_closed_islands(grid, expected):
    assert NumberOfEnclaves().num_enclaves(grid) == expected
