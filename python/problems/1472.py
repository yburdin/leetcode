import unittest


class HistoryNode:
    def __init__(self, url='', following=None, previous=None):
        self.url = url
        self.following = following
        self.previous = previous

    def __repr__(self):
        return f'{self.url}'

    def __str__(self):
        return f'{self.url}'


class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = HistoryNode(url=homepage)

    def visit(self, url: str) -> None:
        prev = self.head
        cur = HistoryNode(url, previous=prev)
        prev.following = cur
        self.head = cur

    def back(self, steps: int) -> str:
        cur = self.head
        for _ in range(steps):
            if cur.previous:
                cur = cur.previous
            else:
                break
        self.head = cur
        return cur.url

    def forward(self, steps: int) -> str:
        cur = self.head
        for _ in range(steps):
            if cur.following:
                cur = cur.following
            else:
                break
        self.head = cur
        return cur.url


class TestBrowserHistory(unittest.TestCase):
    def test_example_1(self):
        browser_history = BrowserHistory("leetcode.com")
        browser_history.visit("google.com")
        browser_history.visit("facebook.com")
        browser_history.visit("youtube.com")

        with self.subTest('Back 1'):
            self.assertEqual(browser_history.back(1), 'facebook.com')

        with self.subTest('Back 2'):
            self.assertEqual(browser_history.back(1), 'google.com')

        with self.subTest('Forward 1'):
            self.assertEqual(browser_history.forward(1), 'facebook.com')

        browser_history.visit("linkedin.com")

        with self.subTest('Forward 2'):
            self.assertEqual(browser_history.forward(2), 'linkedin.com')

        with self.subTest('Back 3'):
            self.assertEqual(browser_history.back(2), 'google.com')

        with self.subTest('Back 4'):
            self.assertEqual(browser_history.back(7), 'leetcode.com')


if __name__ == '__main__':
    unittest.main()
