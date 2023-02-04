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
