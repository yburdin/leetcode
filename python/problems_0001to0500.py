from typing import List
from math import factorial, sqrt


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
    
  
# 70. Climbing Stairs
def climb_stairs(n: int) -> int:
    n += 1
    phi = (1 + sqrt(5)) / 2
    return int((phi ** n - (-phi) ** (-n)) / (2 * phi - 1))


# 28. Implement strStr()
def str_str(haystack: str, needle: str) -> int:
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1


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


# 303. Range Sum Query - Immutable
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sum_range(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])


# 459. Repeated Substring Pattern
def repeated_substring_pattern(s: str) -> bool:
    max_substring_len = len(s) // 2 + 1

    for substring_len in range(1, max_substring_len):
        if len(s) % substring_len == 0:
            substring = s[:substring_len]
            substring_list = [substring == s[substring_len*i:substring_len*(i+1)] for i in range(len(s) // substring_len)]
            if all(substring_list):
                return True
    return False


# 66. Plus One
def plus_one(digits: List[int]) -> List[int]:
    i = -1
    digit = digits[i] + 1
    digits[i] = digit % 10
    residual = digit // 10

    while residual > 0:
        i -= 1
        try:
            digit = digits[i] + 1
            digits[i] = digit % 10
            residual = digit // 10
        except IndexError:
            return [1] + digits

    return digits


# 150. Evaluate Reverse Polish Notation
def eval_rpn(tokens: List[str]) -> int:
    operations = '+-*/'
    stack = []

    for token in tokens:
        if token not in operations:
            stack.append(token)
        else:
            operand1 = stack.pop(-2)
            operand2 = stack.pop(-1)
            stack.append(int(eval(f'{operand1}{token}{operand2}')))

    return int(stack[0])


# 43. Multiply Strings
def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    n = len(num1) + len(num2)
    answer = [0] * n

    first_number = num1[::-1]
    second_number = num2[::-1]

    for place2, digit2 in enumerate(second_number):
        for place1, digit1 in enumerate(first_number):
            num_zeros = place1 + place2
            carry = answer[num_zeros]
            multiplication = int(digit1) * int(digit2) + carry

            answer[num_zeros] = multiplication % 10
            answer[num_zeros + 1] += multiplication // 10

    if answer[-1] == 0:
        answer.pop()

    return ''.join(str(digit) for digit in reversed(answer))


# 67. Add Binary
def add_binary(a: str, b: str) -> str:
    len_dif = abs(len(b) - len(a))
    if len(a) < len(b):
        a = '0' * len_dif + a
    else:
        b = '0' * len_dif + b

    result = ''
    stack = 0

    for order, digit in enumerate(a[::-1]):
        stack, result_digit = divmod(int(digit) + int(b[::-1][order]) + stack, 2)
        result += f'{result_digit}'

    if stack > 0:
        result += f'{stack}'

    return result[::-1]


# 58. Length of Last Word
def length_of_last_word(s: str) -> int:
    words = s.split(' ')
    for word in words[::-1]:
        if len(word) > 0:
            return len(word)
    return 0


# 48. Rotate Image
def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix[0])
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
            matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = matrix[i][j]
            matrix[i][j] = tmp
