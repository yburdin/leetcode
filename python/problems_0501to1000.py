from typing import List, Optional
from classes import ListNode
import string


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


# 973. K Closest Points to Origin
def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    result = []
    distances = [abs(complex(*point)) for point in points]
    max_dist = sorted(distances)[k-1]
    for point in points:
        if abs(complex(*point)) <= max_dist:
            result.append(point)

    return result


# 503. Next Greater Element II
def next_greater_elements_slow(nums: List[int]) -> List[int]:
    result = [-1] * len(nums)

    p2 = len(nums) - 1
    while p2 >= 0:
        p1 = (p2 + 1) % len(nums)
        p2_num = nums[p2]

        while p1 != p2:
            p1_num = nums[p1]
            if p1_num > p2_num:
                result[p2] = p1_num
                break
            else:
                p1 = (p1 + 1) % len(nums)
        p2 -= 1

    return result


def next_greater_elements(nums: List[int]) -> List[int]:
    result = [-1] * len(nums)
    stack = []

    for _ in range(2):
        for n, num in enumerate(nums):
            while stack and num > nums[stack[-1]]:
                result[stack.pop()] = num
            stack.append(n)

    return result


# 556. Next Greater Element III
def next_greater_element_iii(n: int) -> int:
    n_str = str(n)

    p1 = len(n_str) - 2

    while p1 > -1 and int(n_str[p1]) >= int(n_str[p1 + 1]):
        p1 -= 1

    if p1 != -1:
        tail = [int(digit) for digit in n_str[p1+1:]]
        for n in range(len(tail) - 1, -1, -1):
            digit = tail[n]
            if digit > int(n_str[p1]):
                tail[n] = int(n_str[p1])
                result = n_str[:p1] + str(digit) + ''.join([str(k) for k in sorted(tail)])

                if int(result) < 2 ** 31:
                    return int(result)

    return -1


# 713. Subarray Product Less Than K
def num_subarray_product_less_than_k(nums: List[int], k: int) -> int:
    if k <= 1:
        return 0

    prod = 1
    ans = left = 0
    for right, val in enumerate(nums):
        prod *= val
        while prod >= k:
            prod /= nums[left]
            left += 1
        ans += right - left + 1
    return ans


# 910. Smallest Range II
def smallest_range_ii(nums: List[int], k: int) -> int:
    nums.sort()
    first_num, last_num = nums[0], nums[-1]
    result = last_num - first_num
    for i in range(len(nums) - 1):
        a, b = nums[i], nums[i+1]
        possible_result = max(last_num - k, a + k) - min(first_num + k, b - k)
        result = min(result, possible_result)

    return result


# 804. Unique Morse Code Words
def unique_morse_representations(words: List[str]) -> int:
    morse_map = dict(zip(string.ascii_lowercase,
                         [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                          "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--",
                          "--.."]))

    words_in_morse = [''.join([morse_map[char] for char in word]) for word in words]

    return len(set(words_in_morse))


# 860. Lemonade Change
def lemonade_change(bills: List[int]) -> bool:
    current_cash = {5: 0,
                    10: 0,
                    20: 0}

    for bill in bills:
        current_cash[bill] += 1

        if bill == 10:
            current_cash[5] -= 1
        if bill == 20:
            if current_cash[10] > 0:
                current_cash[10] -= 1
                current_cash[5] -= 1
            else:
                current_cash[5] -= 3

        if any([value < 0 for value in current_cash.values()]):
            return False

    return True
