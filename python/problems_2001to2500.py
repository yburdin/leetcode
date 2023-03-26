from common import *


class Solution:
    def __init__(self):
        self.longest_cycle_answer = -1

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

    # 2187. Minimum Time to Complete Trips
    def minimum_time(self, time: List[int], totalTrips: int) -> int:
        left = min(time)
        right = totalTrips * max(time)

        while left < right:
            mid = (left + right) // 2

            sum_trips = 0
            for t in time:
                sum_trips += mid // t

            if sum_trips >= totalTrips:
                right = mid
            else:
                left = mid + 1

        return left

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

    # 2469. Convert the Temperature
    def convert_temperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]

    # 2444. Count Subarrays With Fixed Bounds
    def count_subarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        min_position = -1
        max_position = -1
        left_bound = -1
        result = 0

        for i, num in enumerate(nums):
            if num > maxK or num < minK:
                left_bound = i

            if num == minK:
                min_position = i
            if num == maxK:
                max_position = i
            result += max(0, min(min_position, max_position) - left_bound)

        return result

    # 2244. Minimum Rounds to Complete All Tasks
    def minimum_rounds(self, tasks: List[int]) -> int:
        result = 0
        counter = Counter(tasks)
        for task in counter:
            n_task = counter[task]
            if n_task < 2:
                return -1

            result += n_task // 3
            if n_task % 3 != 0:
                result += 1

        return result

    # 2236. Root Equals Sum of Children
    def check_tree(self, root: Optional[TreeNode]) -> bool:
        return root.val == root.left.val + root.right.val

    # 2325. Decode the Message
    def decode_message(self, key: str, message: str) -> str:
        key_dict = {}

        for letter in key:
            if letter == ' ' or letter in key_dict:
                continue
            key_dict[letter] = string.ascii_lowercase[len(key_dict)]
            if len(key_dict) == len(string.ascii_lowercase):
                break

        result_string = ''
        for char in message:
            result_string += key_dict.get(char, ' ')

        return result_string

    # 2348. Number of Zero-Filled Subarrays
    def zero_filled_subarray(self, nums: List[int]) -> int:
        cur_subarray_len = 0
        result = 0

        for num in nums:
            if num == 0:
                cur_subarray_len += 1
                result += cur_subarray_len
            else:
                cur_subarray_len = 0

        return result

    # 2347. Best Poker Hand
    def best_hand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return 'Flush'

        counter = Counter(ranks)
        result = 'High Card'
        for key in counter:
            if counter[key] >= 3:
                return 'Three of a Kind'
            elif counter[key] == 2:
                result = 'Pair'

        return result

    # 2492. Minimum Score of a Path Between Two Cities
    def min_score(self, n: int, roads: List[List[int]]) -> int:
        nearby_cities = [[] for _ in range(n + 1)]
        for road in roads:
            first_city, second_city, score = road
            nearby_cities[first_city].append([second_city, score])
            nearby_cities[second_city].append([first_city, score])

        queue = []
        visited = set()

        queue.extend(nearby_cities[1])

        result = 1e5
        while queue:
            next_city, score = queue.pop(0)
            if next_city not in visited:
                queue.extend(nearby_cities[next_city])
                visited.add(next_city)
            result = min(result, score)

        return result

    # 2360. Longest Cycle in a Graph
    def longest_cycle(self, edges: List[int]) -> int:
        def dfs(node_: int, edges_: List[int], dist_: dict, visited_nodes_: set):
            visited_nodes_.add(node_)
            next_node = edges_[node_]
            if next_node >= 0 and next_node not in visited_nodes_:
                dist_[next_node] = dist_.get(node_, 0) + 1
                dfs(next_node, edges_, dist_, visited_nodes_)
            elif next_node >= 0 and next_node in dist_:
                self.longest_cycle_answer = max(self.longest_cycle_answer, dist_[node_] - dist_[next_node] + 1)

        n_nodes = len(edges)
        visited_nodes = set()
        for node in range(n_nodes):
            if node not in visited_nodes:
                dist = {node: 0}
                dfs(node, edges, dist, visited_nodes)

        return self.longest_cycle_answer
