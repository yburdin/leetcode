from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


# 976. Largest Perimeter Triangle
def largest_perimeter(nums: List[int]) -> int:
    nums.sort()
    for i in range(len(nums)-3, -1, -1):
        if nums[i] + nums[i+1] > nums[i+2]:
            return nums[i] + nums[i+1] + nums[i+2]
    return 0


# 709. To Lower Case
def to_lower_case(s: str) -> str:
    return s.lower()


# 953. Verifying an Alien Dictionary
def is_alien_sorted(words: List[str], order: str) -> bool:
    for i in range(len(words) - 1):
        if not compare_two_words(words[i], words[i+1], order=order):
            return False
    return True


def compare_two_words(word1: str, word2: str, order: str) -> bool:
    for i, c in enumerate(word1):
        if i >= len(word2):
            return False
        if c != word2[i]:
            return order.index(c) < order.index(word2[i])
    return True


# 797. All Paths From Source to Target
def all_paths_source_target(graph: List[List[int]]) -> List[List[int]]:
    target = len(graph) - 1
    paths = []

    points_to_visit = graph[0]
    stack = []
    for point in points_to_visit:
        if point == target:
            paths.append([0, point])
        else:
            stack.append([[0, point], graph[point]])

    while len(stack) > 0:
        possible_path = stack.pop(0)
        previous_points, next_points = possible_path

        for point in next_points:
            if point == target:
                paths.append(previous_points + [point])
            else:
                stack.append([previous_points + [point], graph[point]])

    return paths


# 876. Middle of the Linked List
def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    arr = [head]
    while arr[-1].next:
        arr.append(arr[-1].next)
    return arr[len(arr) // 2]


# 896. Monotonic Array
def is_monotonic(nums: List[int]) -> bool:
    sign = (nums[-1] - nums[0]) > 0
    for i, num in enumerate(nums):
        if i < len(nums) - 1 and num != nums[i+1] and ((nums[i+1] - num > 0) is not sign):
            return False
    return True


# 989. Add to Array-Form of Integer
def add_to_array_form(num: List[int], k: int) -> List[int]:
    stack, digit = divmod(num[-1] + k, 10)
    result = [digit]
    order = 1

    while stack > 0 or order < len(num):
        if order < len(num):
            stack, digit = divmod(num[-1-order] + stack, 10)
            result.append(digit)
            order += 1
        else:
            stack, digit = divmod(stack, 10)
            result.append(digit)
            order += 1

    result.reverse()

    return result


# 739. Daily Temperatures
def daily_temperatures_slow(temperatures: List[int]) -> List[int]:
    result = []

    for day, temperature in enumerate(temperatures):
        if day < len(temperatures):
            temp_set = set(temperatures[day+1:])
            min_days = 1000
            day_found = False

            if len(temp_set) > 0:
                for temp in range(temperature + 1, max(temp_set)+1):
                    if temp in temp_set:
                        day_found = True
                        temp_index = temperatures[day+1:].index(temp) + 1
                        if temp_index == 1:
                            min_days = 1
                            break
                        else:
                            min_days = min(min_days, temp_index)

                if day_found:
                    result.append(min_days)
                else:
                    result.append(0)
            else:
                result.append(0)

    return result


def daily_temperatures(temperatures: List[int]) -> List[int]:
    ans = [0] * len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            cur = stack.pop()
            ans[cur] = i - cur
        stack.append(i)

    return ans
