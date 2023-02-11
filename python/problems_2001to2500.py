from typing import List


# 2053. Kth Distinct String in an Array
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
def time_required_to_buy(tickets: List[int], k: int) -> int:
    time = 0
    while tickets[k] != 1:
        time += sum([1 if item > 0 else 0 for item in tickets])
        tickets = [item - 1 if item > 0 else 0 for item in tickets]

    time += sum([1 if item > 0 else 0 for item in tickets[:k+1]])

    return time


# 2221. Find Triangular Sum of an Array
def triangular_sum(nums: List[int]) -> int:
    while len(nums) > 1:
        new_nums = [(nums[i] + nums[i + 1]) % 10 for i in range(len(nums) - 1)]
        nums = new_nums

    return nums[0]


# 2306. Naming a Company
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
