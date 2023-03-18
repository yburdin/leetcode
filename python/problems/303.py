from common import *


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sum_range(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])


class TestNumArray(unittest.TestCase):
    def test_303(self):
        num_array = NumArray([-2, 0, 3, -5, 2, -1])
        self.assertEqual(num_array.sum_range(0, 2), 1)
        self.assertEqual(num_array.sum_range(2, 5), -1)
        self.assertEqual(num_array.sum_range(0, 5), -3)


if __name__ == '__main__':
    unittest.main()
