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
