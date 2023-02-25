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
