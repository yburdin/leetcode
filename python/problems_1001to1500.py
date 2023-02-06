from typing import List
from math import atan


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


# 1491. Average Salary Excluding the Minimum and Maximum Salary
def average(salary: List[int]) -> float:
    salary.sort()
    salary = salary[1:-1]
    return sum(salary) / len(salary)


# 1281. Subtract the Product and Sum of Digits of an Integer
def subtract_product_and_sum(n: int) -> int:
    product_of_digits = 1
    sum_of_digits = 0

    for digit in str(n):
        product_of_digits *= int(digit)
        sum_of_digits += int(digit)

    return product_of_digits - sum_of_digits


# 1437. Check If All 1's Are at Least Length K Places Away
def k_length_apart(nums: List[int], k: int) -> bool:
    i_loc = 0
    while i_loc < len(nums) - 1:
        if nums[i_loc] == 1:
            j_loc = i_loc
            while j_loc < len(nums) - 1:
                j_loc += 1
                if nums[j_loc] == 1:
                    if j_loc - i_loc - 1 < k:
                        return False
                    else:
                        i_loc = j_loc

                if j_loc == len(nums) - 1:
                    return True
        else:
            i_loc += 1
    return True


# 1232. Check If It Is a Straight Line
def check_straight_line(coordinates: List[List[int]]) -> bool:
    dx = coordinates[-1][0] - coordinates[0][0]
    dy = coordinates[-1][1] - coordinates[0][1]
    dy = 1e-9 if dy == 0 else dy
    k = abs(atan(dx / dy))

    for i in range(1, len(coordinates)):
        point_dx = coordinates[i][0] - coordinates[i - 1][0]
        point_dy = coordinates[i][1] - coordinates[i - 1][1]
        point_dy = 1e-9 if point_dy == 0 else point_dy
        point_k = abs(atan(point_dx / point_dy))

        # print(f'{k=}, {point_k=}, {k - point_k}')

        if abs(k - point_k) > 1e-5:
            return False

    return True


# 1309. Decrypt String from Alphabet to Integer Mapping
def freq_alphabets(s: str) -> str:
    result = []
    s_list = list(s)
    s_list.reverse()

    i = 0
    while i < len(s_list):
        if s_list[i] != '#':
            result.append(chr(int(s_list[i]) + 96))
            i += 1
        else:
            chars = s_list[i+1:i+3]
            chars.reverse()
            result.append(chr(int(''.join(chars)) + 96))
            i += 3

    result.reverse()
    return ''.join(result)


# 1290. Convert Binary Number in a Linked List to Integer
def get_decimal_value(head: ListNode) -> int:
    num = head.val
    while head.next:
        num = num * 2 + head.next.val
        head = head.next
    return num


# 1356. Sort Integers by The Number of 1 Bits
def sort_by_bits(arr: List[int]) -> List[int]:
    bit_dict = {}
    for item in arr:
        bits = bin(item).count('1')
        if bits in bit_dict:
            bit_dict[bits].append(item)
        else:
            bit_dict[bits] = [item]

    result = []
    for key in sorted(bit_dict.keys()):
        result += sorted(bit_dict[key])

    return result


# 1323. Maximum 69 Number
def maximum_69_number(num: int) -> int:
    num_str_list = list(f'{num}')
    if '6' in num_str_list:
        first_6 = num_str_list.index('6')
        num_str_list[first_6] = '9'
        return int(''.join(num_str_list))
    else:
        return num


# 1266. Minimum Time Visiting All Points
def min_time_to_visit_all_points_slow(points: List[List[int]]) -> int:
    current_point = points[0]
    steps = [current_point]

    for point in points[1:]:
        while current_point != point:
            dx = point[0] - current_point[0]
            dy = point[1] - current_point[1]
            step = find_next_step(dx, dy)
            current_point = [current_point[i] + step[i] for i in [0, 1]]

            steps.append(current_point)

    return len(steps) - 1


def find_next_step(dx: int, dy: int, tol=1e-3) -> List[int]:
    result = [0, 0]
    for i, direction in enumerate([dx, dy]):
        if direction > tol:
            result[i] = 1
        elif direction < -tol:
            result[i] = -1

    return result


def min_time_to_visit_all_points(points: List[List[int]]) -> int:
    result = 0

    for i in range(1, len(points)):
        p1 = points[i-1]
        p2 = points[i]

        dist = complex(*p2) - complex(*p1)
        result += max(map(abs, (dist.real, dist.imag)))

    return int(result)


# 1071. Greatest Common Divisor of Strings
def gcd_of_strings(str1: str, str2: str) -> str:
    substring_len = min(len(str1), len(str2))
    while substring_len > 0:
        if len(str1) % substring_len == 0 and len(str2) % substring_len == 0:
            substring = str1[0:substring_len]

            substring_1 = [str1[i:i+substring_len] == substring for i in range(0, len(str1), substring_len)]
            substring_2 = [str2[i:i+substring_len] == substring for i in range(0, len(str2), substring_len)]

            if all(substring_1 + substring_2):
                return substring
            else:
                substring_len -= 1
        else:
            substring_len -= 1

    return ''


# 1470. Shuffle the Array
def shuffle(nums: List[int], n: int) -> List[int]:
    xs = nums[0:n]
    ys = nums[n:]
    result = []

    for i in range(n):
        result.append(xs[i])
        result.append(ys[i])

    return result
