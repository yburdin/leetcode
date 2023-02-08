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


# 12. Integer to Roman
def int_to_roman(num: int) -> str:
    int_roman_dict = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
                      100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    result = ''

    for val in list(int_roman_dict.keys())[::-1]:
        if val > num:
            continue

        if num == 0:
            return result

        n = num // val
        num %= val

        result += int_roman_dict[val] * n

    return result


# 6. Zigzag Conversion
def convert(s: str, num_rows: int) -> str:
    if num_rows == 1:
        return s

    rows = ['' for _ in range(num_rows)]
    step = 2 * num_rows - 2
    chunks = [s[i:i + step] for i in range(0, len(s), step)]

    for chunk in chunks:
        forward_string = chunk[0:num_rows]
        backward_string = chunk[-1:num_rows - 1:-1] + ' '
        backward_string = ' ' * (num_rows - len(backward_string)) + backward_string
        for n in range(num_rows):
            if n < len(forward_string) and n < len(backward_string):
                rows[n] += forward_string[n] + backward_string[n]
            elif n < len(forward_string):
                rows[n] += forward_string[n]
            elif n < len(backward_string):
                rows[n] += backward_string[n]

    result_string = ''.join(rows).replace(' ', '')
    return result_string


# 459. Repeated Substring Pattern
def repeated_substring_pattern(s: str) -> bool:
    max_substring_len = len(s) // 2 + 1

    for substring_len in range(1, max_substring_len):
        if len(s) % substring_len == 0:
            substring = s[:substring_len]
            substring_list = [substring == s[substring_len*i:substring_len*(i+1)]
                              for i in range(len(s) // substring_len)]
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


# 54. Spiral Matrix
def spiral_order(matrix: List[List[int]]) -> List[int]:
    result = []
    while len(matrix) > 0:
        result.extend(matrix.pop(0))
        if len(matrix) > 0 and len(matrix[0]) > 0:
            result.extend([row.pop(-1) for row in matrix])
        if len(matrix) > 0:
            last_row = matrix.pop(-1)
            last_row.reverse()
            result.extend(last_row)
        if len(matrix) > 0 and len(matrix[0]) > 0:
            first_column = [row.pop(0) for row in matrix]
            first_column.reverse()
            result.extend(first_column)
    return result


# 49. Group Anagrams
def group_anagrams_slow(strs: List[str]) -> List[List[str]]:
    result = [[strs.pop()]]

    while len(strs) > 0:
        current_word = strs.pop()

        is_anagram_ = False
        for anagram in result:
            if sorted(current_word) == sorted(anagram[0]):
                anagram.append(current_word)
                is_anagram_ = True
                break

        if not is_anagram_:
            result.append([current_word])

    return result


def group_anagrams_accepted(strs: List[str]) -> List[List[str]]:
    anagram_dict = {}

    while len(strs) > 0:
        word = strs.pop()
        word_ord = sum([ord(char) for char in word])
        if word_ord not in anagram_dict.keys():
            anagram_dict[word_ord] = {0: [word]}
        else:
            is_ord_anagram = False
            for key in anagram_dict[word_ord]:
                if sorted(anagram_dict[word_ord][key][0]) == sorted(word):
                    anagram_dict[word_ord][key].append(word)
                    is_ord_anagram = True
                    break
            if not is_ord_anagram:
                anagram_dict[word_ord][len(anagram_dict[word_ord])] = [word]

    result = []
    for ord_key in anagram_dict:
        for anagram_key in anagram_dict[ord_key]:
            result.append(anagram_dict[ord_key][anagram_key])

    return result


def group_anagrams(strs: List[str]) -> List[List[str]]:
    d = {}
    for w in strs:
        key = tuple(sorted(w))
        d[key] = d.get(key, []) + [w]
    return list(d.values())


# 438. Find All Anagrams in a String
def find_anagrams_slow(s: str, p: str) -> List[int]:
    result = []
    for start_index in range(len(s) - len(p) + 1):
        if sorted(s[start_index:start_index+len(p)]) == sorted(p):
            result.append(start_index)

    return result


def find_anagrams(s: str, p: str) -> List[int]:
    result = []
    hashmap = {}

    if len(p) > len(s):
        return []

    for ch in p:
        hashmap[ch] = hashmap.get(ch, 0) + 1

    for i in range(len(p) - 1):
        if s[i] in hashmap:
            hashmap[s[i]] -= 1

    # slide the window with stride 1
    for i in range(-1, len(s) - len(p) + 1):
        if i > -1 and s[i] in hashmap:
            hashmap[s[i]] += 1
        if i + len(p) < len(s) and s[i + len(p)] in hashmap:
            hashmap[s[i + len(p)]] -= 1

        # check whether we encountered an anagram
        if all(v == 0 for v in hashmap.values()):
            result.append(i + 1)

    return result


# 342. Power of Four
def is_power_of_four(n: int) -> bool:
    x = 0
    while 4 ** x <= n:
        if 4 ** x == n:
            return True
        x += 1
    return False


# 326. Power of Three
def is_power_of_three(n: int) -> bool:
    x = 0
    while 3 ** x <= n:
        if 3 ** x == n:
            return True
        x += 1
    return False


# 62. Unique Paths
def unique_paths(m: int, n: int) -> int:
    # Количество уникальных путей равно количествую сочетаний из n по k,
    # где n - общая длина пути, k - длина стороны прямоугольника

    path_len = m + n - 2
    side_len = max(m, n) - 1

    return factorial(path_len) // factorial(path_len - side_len) // factorial(side_len)


# 63. Unique Paths II
def unique_paths_with_obstacles(obstacle_grid: List[List[int]]) -> int:
    if obstacle_grid[0][0] == 1:
        return 0
    else:
        obstacle_grid[0][0] = 1

    for column in range(1, len(obstacle_grid[0])):
        obstacle_grid[0][column] = obstacle_grid[0][column - 1] if obstacle_grid[0][column] == 0 else 0

    for row in range(1, len(obstacle_grid)):
        obstacle_grid[row][0] = obstacle_grid[row - 1][0] if obstacle_grid[row][0] == 0 else 0

    for row in range(1, len(obstacle_grid)):
        for column in range(1, len(obstacle_grid[0])):
            obstacle_grid[row][column] = (
                obstacle_grid[row - 1][column] + obstacle_grid[row][column - 1]
                if obstacle_grid[row][column] == 0 else 0
            )

    return obstacle_grid[-1][-1]


# 38. Count and Say
def count_and_say(n: int) -> str:
    if n == 1:
        return '1'
    else:
        return say(count_and_say(n-1))


def say(s: str) -> str:
    result_str = ''
    digits = [s[0], ]

    for c in s[1:]:
        if c == digits[-1][0]:
            digits[-1] += c
        else:
            digits.append(c)

    for digit in digits:
        result_str += f'{len(digit)}{digit[0]}'

    return result_str


# 45. Jump Game II
def jump(nums: List[int]) -> int:
    cur_end = 0
    cur_far = 0
    answer = 0

    for i, num in enumerate(nums[:-1]):
        cur_far = max(cur_far, i + num)

        if i == cur_end:
            answer += 1
            cur_end = cur_far

    return answer
