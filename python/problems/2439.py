from typing import List
from math import ceil
import pytest


# 2439. Minimize Maximum of Array
def minimize_array_value(nums: List[int]) -> int:
    result = 0
    prefix_sum = 0

    for i, num in enumerate(nums):
        prefix_sum += num
        average = ceil(prefix_sum / (i + 1))
        result = max(result, average)

    return result


@pytest.mark.parametrize('nums, expected', [
    ([3, 7, 1, 6], 5),
    ([10, 1], 10),
    ([13, 13, 20, 0, 8, 9, 9], 16),
])
def test_minimize_array_value(nums, expected):
    assert minimize_array_value(nums) == expected
