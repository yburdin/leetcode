from common import *


class CountPairs:
    def __init__(self):
        self.pairs = 0
        self.visited = set()

    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        remaining_nodes = n
        adj = self._collect_adj(n, edges)

        for node in range(n):
            if node not in self.visited:
                size_of_component = self._dfs(node, adj)
                self.pairs += size_of_component * (remaining_nodes - size_of_component)
                remaining_nodes -= size_of_component

        return self.pairs

    def _dfs(self, node: int, adj: List[List[int]]) -> int:
        count = 1
        self.visited.add(node)
        for neighbour in adj[node]:
            if neighbour not in self.visited:
                count += self._dfs(neighbour, adj)

        return count

    @staticmethod
    def _collect_adj(n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        return adj


class TestCountPairs(unittest.TestCase):
    def test_example_1(self):
        sol = CountPairs()
        res = sol.countPairs(n=3, edges=[[0, 1], [0, 2], [1, 2]])
        self.assertEqual(res, 0)

    def test_example_2(self):
        sol = CountPairs()
        res = sol.countPairs(n=7, edges=[[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]])
        self.assertEqual(res, 14)


if __name__ == '__main__':
    unittest.main()
