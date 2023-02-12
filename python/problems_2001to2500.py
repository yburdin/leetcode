from typing import List


class Solution:
    # 2053. Kth Distinct String in an Array
    @staticmethod
    def kth_distinct(arr: List[str], k: int) -> str:
        n_distinct = 0

        while len(arr) > 0:
            item = arr.pop(0)
            if arr.count(item) == 0:
                n_distinct += 1
                if n_distinct == k:
                    return item

            while arr.count(item) > 0:
                arr.remove(item)

        return ''

    # 2073. Time Needed to Buy Tickets
    @staticmethod
    def time_required_to_buy(tickets: List[int], k: int) -> int:
        time = 0
        while tickets[k] != 1:
            time += sum([1 if item > 0 else 0 for item in tickets])
            tickets = [item - 1 if item > 0 else 0 for item in tickets]

        time += sum([1 if item > 0 else 0 for item in tickets[:k+1]])

        return time

    # 2221. Find Triangular Sum of an Array
    @staticmethod
    def triangular_sum(nums: List[int]) -> int:
        while len(nums) > 1:
            new_nums = [(nums[i] + nums[i + 1]) % 10 for i in range(len(nums) - 1)]
            nums = new_nums

        return nums[0]

    # 2306. Naming a Company
    @staticmethod
    def distinct_names(ideas: List[str]) -> int:
        result = 0
        groups = [set() for _ in range(26)]

        for idea in ideas:
            groups[ord(idea[0]) - ord('a')].add(idea[1:])

        for i, group_i in enumerate(groups):
            for j, group_j in enumerate(groups):
                if i == j:
                    continue

                num_of_mutual = len(group_i & group_j)
                result += (len(group_i) - num_of_mutual) * (len(group_j) - num_of_mutual)

        return result

    # 2477. Minimum Fuel Cost to Report to the Capital
    from math import ceil
    fuel = 0

    def minimum_fuel_cost(self, roads: List[List[int]], seats: int) -> int:
        adj = [[] for _ in range(len(roads) + 1)]
        for node_i, node_j in roads:
            adj[node_i].append(node_j)
            adj[node_j].append(node_i)

        self.dfs_2477(0, -1, adj, seats)
        return self.fuel

    def dfs_2477(self, node: int, parent: int, adj: List[List[int]], seats: int) -> int:
        representatives = 1

        for child in adj[node]:
            if child != parent:
                representatives += self.dfs_2477(child, node, adj, seats)

        if node != 0:
            self.fuel += self.ceil(representatives / seats)

        return representatives
