from typing import List
from math import atan


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
