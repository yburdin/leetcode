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
