from typing import List
from math import factorial


# 119. Pascal's Triangle II
def get_row(row_index: int) -> List[int]:
    row = [factorial(row_index) // (factorial(m) * (factorial(row_index - m))) for m in range(row_index + 1)]
    return row


# 191. Number of 1 Bits
def hamming_weight(n: int) -> int:
    return str(bin(n)).count('1')


# 202. Happy Number
def is_happy(n: int) -> bool:
    while True:
        n = sum([int(s) ** 2 for s in str(n)])

        if n == 1:
            return True
        elif n == 89:
            return False


# 405. Convert a Number to Hexadecimal
def to_hex(num: int) -> str:
    hex_dict = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'a',
        11: 'b',
        12: 'c',
        13: 'd',
        14: 'e',
        15: 'f',
    }

    hex_num = ''

    if num == 0:
        return '0'

    elif num < 0:
        num = num + 2 ** 32

    while num > 0:
        hex_num += f'{hex_dict[num % 16]}'
        num //= 16

    return hex_num[::-1]


# 496. Next Greater Element I
def next_greater_element(nums1: List[int], nums2: List[int]) -> List[int]:
    result = []

    for i, num in enumerate(nums1):
        j = nums2.index(num)
        for num2 in nums2[j:]:
            if num2 > num:
                result.append(num2)
                break

        if i > len(result) - 1:
            result.append(-1)

    return result


# 389. Find the Difference
def find_the_difference(s: str, t: str) -> str:
    return chr(sum([ord(x) for x in t]) - sum([ord(x) for x in s]))


# 232. Implement Queue using Stacks
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        self.peek()
        return self.s2.pop()

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self):
        return not self.s1 and not self.s2


# 242. Valid Anagram
def is_anagram(s: str, t: str) -> bool:
    s_dict = {char: s.count(char) for char in set(s)}
    t_dict = {char: t.count(char) for char in set(t)}
    return s_dict == t_dict


# 217. Contains Duplicate
def contains_duplicate(nums: List[int]) -> bool:
    unique = set()
    for num in nums:
        if num in unique:
            return True
        else:
            unique.add(num)
    return False
