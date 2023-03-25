from common import *


class MinReorder:
    def __init__(self):
        self.count = 0

    def dfs(self, node, parent, adj):
        for edge in adj[node]:
            child, sign = edge
            if child != parent:
                self.count += sign
                self.dfs(child, node, adj)

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for edge in connections:
            adj[edge[0]].append((edge[1], 1))
            adj[edge[1]].append((edge[0], 0))

        self.dfs(0, -1, adj)

        return self.count


class TestMinReorder(unittest.TestCase):
    def test_example_1(self):
        sol = MinReorder()
        res = sol.minReorder(n=6, connections=[[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]])

        self.assertEqual(res, 3)

    def test_example_2(self):
        sol = MinReorder()
        res = sol.minReorder(n=5, connections=[[1, 0], [1, 2], [3, 2], [3, 4]])

        self.assertEqual(res, 2)

    def test_example_3(self):
        sol = MinReorder()
        res = sol.minReorder(n=3, connections=[[1, 0], [2, 0]])

        self.assertEqual(res, 0)


if __name__ == '__main__':
    unittest.main()
