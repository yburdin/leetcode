from common import *


class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        for event_start, event_end in self.events:
            if event_start <= start < event_end:
                return False
            if event_start < end <= event_end:
                return False
            if start < event_start and end > event_end:
                return False

        self.events.append((start, end))
        return True


class TestMyCalendar(unittest.TestCase):
    def test_729(self):
        with self.subTest(msg='Testcase 1'):
            my_calendar = MyCalendar()
            self.assertTrue(my_calendar.book(10, 20))
            self.assertFalse(my_calendar.book(15, 25))
            self.assertTrue(my_calendar.book(20, 30))

        with self.subTest(msg='Testcase 2'):
            my_calendar = MyCalendar()
            self.assertTrue(my_calendar.book(47, 50))
            self.assertTrue(my_calendar.book(33, 41))
            self.assertFalse(my_calendar.book(39, 45))
            self.assertFalse(my_calendar.book(33, 42))
            self.assertTrue(my_calendar.book(25, 32))
            self.assertFalse(my_calendar.book(26, 35))
            self.assertTrue(my_calendar.book(19, 25))
            self.assertTrue(my_calendar.book(3, 8))
            self.assertTrue(my_calendar.book(8, 13))
            self.assertFalse(my_calendar.book(18, 27))

        with self.subTest(msg='Testcase 3'):
            my_calendar = MyCalendar()
            self.assertTrue(my_calendar.book(97, 100))
            self.assertTrue(my_calendar.book(33, 51))
            self.assertFalse(my_calendar.book(89, 100))
            self.assertFalse(my_calendar.book(83, 100))
            self.assertTrue(my_calendar.book(75, 92))
            self.assertFalse(my_calendar.book(76, 95))
            self.assertTrue(my_calendar.book(19, 30))
            self.assertTrue(my_calendar.book(53, 63))
            self.assertFalse(my_calendar.book(8, 23))
            self.assertFalse(my_calendar.book(18, 37))
            self.assertFalse(my_calendar.book(87, 100))
            self.assertFalse(my_calendar.book(83, 100))
            self.assertFalse(my_calendar.book(54, 67))
            self.assertFalse(my_calendar.book(35, 48))
            self.assertFalse(my_calendar.book(58, 75))
            self.assertFalse(my_calendar.book(70, 89))
            self.assertFalse(my_calendar.book(13, 32))
            self.assertFalse(my_calendar.book(44, 63))
            self.assertFalse(my_calendar.book(51, 62))
            self.assertTrue(my_calendar.book(2, 15))


if __name__ == '__main__':
    unittest.main()
