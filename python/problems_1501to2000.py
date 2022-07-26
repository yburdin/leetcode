from typing import List


# 1523. Count Odd Numbers in an Interval Range
def count_odds(low: int, high: int) -> int:
    n_odds = (high - low) // 2
    if not (low % 2 == 0 and high % 2 == 0):
        n_odds += 1
    return n_odds


# 1732. Find the Highest Altitude
def largest_altitude(gain: List[int]) -> int:
    highest_alt = 0
    current_alt = 0

    for i, g in enumerate(gain):
        current_alt += g
        highest_alt = max(current_alt, highest_alt)

        if max(gain[i:]) < 1:
            return highest_alt

    return highest_alt


# 1700. Number of Students Unable to Eat Lunch
def count_students(students: List[int], sandwiches: List[int]) -> int:
    while len(sandwiches) > 0:
        top_sandwich = sandwiches[0]
        if top_sandwich not in students:
            return len(students)

        current_student = students.pop(0)
        if current_student == top_sandwich:
            sandwiches.remove(top_sandwich)
        else:
            students.append(current_student)

    return len(students)


# 1925. Count Square Sum Triples
def count_triples(n: int) -> int:
    triples_count = 0
    for a in range(1, n):
        for b in range(a + 1, int((n ** 2 - a ** 2) ** 0.5) + 1):
            c = (a ** 2 + b ** 2) ** 0.5
            if c == int(c):
                triples_count += 2

    return triples_count


# 1779. Find Nearest Point That Has the Same X or Y Coordinate
def nearest_valid_point(x: int, y: int, points: List[List[int]]) -> int:
    result = (2**32, -1)

    for point in points[::-1]:
        is_valid_point = point[0] == x or point[1] == y

        if is_valid_point:
            distance = abs(x - point[0]) + abs(y - point[1])
            if distance < result[0] or distance == result[0] and points.index(point) < result[1]:
                result = (distance, points.index(point))

    return result[-1]


# 1822. Sign of the Product of an Array
def array_sign(nums: List[int]) -> int:
    if 0 in nums:
        return 0
    else:
        negatives = sum([1 for x in nums if x < 0])

        if negatives % 2 == 0:
            return 1
        else:
            return -1


# 1502. Can Make Arithmetic Progression From Sequence
def can_make_arithmetic_progression(arr: List[int]) -> bool:
    arr.sort()
    step = arr[1] - arr[0]

    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] != step:
            return False

    return True


# 1790. Check if One String Swap Can Make Strings Equal
def are_almost_equal(s1: str, s2: str) -> bool:
    equals_list = [0 if s1[i] == s2[i] else 1 for i in range(len(s1))]

    if sum(equals_list) == 0:
        return True
    elif sum(equals_list) == 2:
        i1 = equals_list.index(1)
        i2 = equals_list.index(1, i1 + 1)

        s1_swapped = s1[:i1] + s1[i2] + s1[i1+1:i2] + s1[i1] + s1[i2+1:]
        if s1_swapped == s2:
            return True

    return False


# 1588. Sum of All Odd Length Subarrays
def sum_odd_length_subarrays(arr: List[int]) -> int:
    result = 0

    for array_length in range(1, len(arr) + 1, 2):
        sub_arrays_sums = [sum(arr[i:array_length+i]) for i in range(len(arr) - array_length + 1)]
        result += sum(sub_arrays_sums)

    return result


# 1672. Richest Customer Wealth
def maximum_wealth(accounts: List[List[int]]) -> int:
    return max([sum(account) for account in accounts])


# 1572. Matrix Diagonal Sum
def diagonal_sum(mat: List[List[int]]) -> int:
    size = len(mat)
    primary_diagonal = list(zip(range(size), range(size)))
    secondary_diagonal = list(zip(range(size-1, -1, -1), range(size)))
    if size % 2 == 1:
        primary_diagonal.remove((size//2, size//2))

    diagonals = primary_diagonal + secondary_diagonal

    return sum([mat[row][column] for row, column in diagonals])


# 1828. Queries on Number of Points Inside a Circle
def is_point_in_circle(point: List[int], circle: List[int]) -> bool:
    distance = ((circle[0]-point[0]) ** 2 + (circle[1]-point[1]) ** 2) ** 0.5
    return distance <= circle[2]


def is_point_in_circle_complex(point: List[int], circle: List[int]) -> bool:
    distance = abs(complex(*point) - complex(circle[0], circle[1]))
    return distance <= circle[2]


def count_points(points: List[List[int]], queries: List[List[int]]) -> List[int]:
    result = []
    for circle in queries:
        result.append(sum([is_point_in_circle_complex(point, circle) for point in points]))

    return result


# 1768. Merge Strings Alternately
def merge_alternately(word1: str, word2: str) -> str:
    result = ''
    min_len = min(len(word1), len(word2))
    result += ''.join([f'{a}{b}' for a, b in list(zip(word1, word2))])
    result += word1[min_len:] + word2[min_len:]

    return result


# 1678. Goal Parser Interpretation
def interpret(command: str) -> str:
    return command.replace('()', 'o').replace('(al)', 'al')


# 1603. Design Parking System
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.parking_dict = {1: big, 2: medium, 3: small}

    def add_car(self, car_type: int) -> bool:
        if self.parking_dict[car_type] > 0:
            self.parking_dict[car_type] -= 1
            return True
        else:
            return False
