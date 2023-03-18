from common import *


class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        self.peek()
        return self.s2.pop()

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self):
        return not self.s1 and not self.s2


class TestMyQueue(unittest.TestCase):
    def test_232(self):
        my_queue = MyQueue()
        my_queue.push(1)
        my_queue.push(2)
        self.assertEqual(my_queue.peek(), 1)
        self.assertEqual(my_queue.pop(), 1)
        self.assertFalse(my_queue.empty())


if __name__ == '__main__':
    unittest.main()
