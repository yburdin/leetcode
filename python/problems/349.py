from typing import List
import pytest


# 349. Intersection of Two Arrays
def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1) & set(nums2))


@pytest.mark.parametrize('nums1, nums2, expected', [
    ([1, 2, 2, 1], [2, 2], [2]),
    ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9]),
])
def test_intersect(nums1, nums2, expected):
    assert sorted(intersection(nums1, nums2)) == sorted(expected)
