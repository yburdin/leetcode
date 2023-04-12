from collections import Counter
from typing import List
import pytest


# 350. Intersection of Two Arrays II
def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    counter1 = Counter(nums1)
    counter2 = Counter(nums2)

    result = []
    for num in counter1:
        result.extend([num] * min(counter1[num], counter2[num]))
    return result


@pytest.mark.parametrize('nums1, nums2, expected', [
    ([1, 2, 2, 1], [2, 2], [2, 2]),
    ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9]),
])
def test_intersect(nums1, nums2, expected):
    assert intersect(nums1, nums2) == expected
