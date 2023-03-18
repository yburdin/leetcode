from common import *


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapify(self.nums)

        while len(self.nums) > self.k:
            heappop(self.nums)

    def add(self, val: int) -> int:
        heappush(self.nums, val)
        if len(self.nums) > self.k:
            heappop(self.nums)
        return self.nums[0]


class TestKthLargest(unittest.TestCase):
    def test_703(self):
        with self.subTest('Example 1'):
            kth_largest = KthLargest(3, [4, 5, 8, 2])
            self.assertEqual(kth_largest.add(3), 4)
            self.assertEqual(kth_largest.add(5), 5)
            self.assertEqual(kth_largest.add(10), 5)
            self.assertEqual(kth_largest.add(9), 8)
            self.assertEqual(kth_largest.add(4), 8)


if __name__ == '__main__':
    unittest.main()
