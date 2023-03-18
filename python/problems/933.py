from common import *


class RecentCounter:
    def __init__(self):
        """
        RecentCounter() Initializes the counter with zero recent requests.
        """
        self.requests = []
        self.index_min = 0

    def ping(self, t: int) -> int:
        """
        Adds a new request at time t, where t represents some time in milliseconds,
        and returns the number of requests that has happened in the past 3000 milliseconds (including the new request).
        Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
        """

        self.requests.append(t)
        self.requests = sorted(self.requests)

        t_min = t - 3000
        while self.requests[self.index_min] < t_min and self.index_min < len(self.requests) - 1:
            self.index_min += 1

        return len(self.requests[self.index_min:])


class TestRecentCounter(unittest.TestCase):
    def test_933(self):
        with self.subTest('Example 1'):
            recent_counter = RecentCounter()
            self.assertEqual(recent_counter.ping(1), 1)     # requests = [1], range is [-2999,1], return 1
            self.assertEqual(recent_counter.ping(100), 2)   # requests = [1, 100], range is [-2900,100], return 2
            self.assertEqual(recent_counter.ping(3001), 3)  # requests = [1, 100, 3001], range is [1,3001], return 3
            self.assertEqual(recent_counter.ping(3002),
                             3)  # requests = [1, 100, 3001, 3002], range is [2,3002], return 3


if __name__ == '__main__':
    unittest.main()
