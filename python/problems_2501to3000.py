from common import *


class Solution:
    # 2558. Take Gifts From the Richest Pile
    def pick_gifts(self, gifts: List[int], k: int) -> int:
        q = []
        for gift in gifts:
            heappush(q, -gift)

        for _ in range(k):
            max_gifts = heappop(q) * -1
            heappush(q, -int(max_gifts ** 0.5))

        return sum(q) * -1

    # 2586. Count the Number of Vowel Strings in Range
    def vowel_strings(self, words: List[str], left: int, right: int) -> int:
        def is_vowel(word_: str) -> bool:
            return word_[0] in 'aeiou' and word_[-1] in 'aeiou'

        return sum(map(is_vowel, words[left:right+1]))

    # 2574. Left and Right Sum Differences
    def left_rigth_difference(self, nums: List[int]) -> List[int]:
        result = []
        left_sum = 0
        right_sum = sum(nums)

        for i, num in enumerate(nums):
            right_sum -= num
            result.append(abs(left_sum - right_sum))
            left_sum += num

        return result

    # 2525. Categorize Box According to Criteria
    def categorize_box(self, length: int, width: int, height: int, mass: int) -> str:
        def is_heavy(mass_):
            return mass >= 100

        def is_bulky(*args):
            volume = 1
            for arg in args:
                if arg >= 1e4:
                    return True
                volume *= arg
            return volume >= 1e9

        if is_heavy(mass) and is_bulky(length, width, height):
            return 'Both'
        elif is_heavy(mass):
            return 'Heavy'
        elif is_bulky(length, width, height):
            return 'Bulky'
        else:
            return 'Neither'
