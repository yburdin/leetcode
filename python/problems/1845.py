from common import *


class SeatManager:
    def __init__(self, n: int):
        self.heap = list(range(1, n + 1))

    def reserve(self) -> int:
        return heappop(self.heap)

    def unreserve(self, seat_number: int) -> None:
        heappush(self.heap, seat_number)


class TestSeatManager(unittest.TestCase):
    def test_1845(self):
        seat_manager = SeatManager(5)  # Initializes a SeatManager with 5 seats.

        # All seats are available, so return the lowest numbered seat, which is 1.
        self.assertEqual(seat_manager.reserve(), 1)

        # The available seats are [2,3,4,5], so return the lowest of them, which is 2.
        self.assertEqual(seat_manager.reserve(), 2)

        # Unreserve seat 2, so now the available seats are [2,3,4,5].
        seat_manager.unreserve(2)

        # The available seats are [2,3,4,5], so return the lowest of them, which is 2.
        self.assertEqual(seat_manager.reserve(), 2)

        # The available seats are [3,4,5], so return the lowest of them, which is 3.
        self.assertEqual(seat_manager.reserve(), 3)

        # The available seats are [4,5], so return the lowest of them, which is 4.
        self.assertEqual(seat_manager.reserve(), 4)

        # The only available seat is seat 5, so return 5.
        self.assertEqual(seat_manager.reserve(), 5)

        # Unreserve seat 5, so now the available seats are [5].
        seat_manager.unreserve(5)


if __name__ == '__main__':
    unittest.main()
