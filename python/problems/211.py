from common import *


class WordDictionary:
    """
    Design a data structure that supports adding new words and finding if a string matches any previously added string.
    """

    def __init__(self):
        """Initializes the object"""
        self.root = TrieNode()
        self.search_result = False

    def addWord(self, word: str) -> None:
        """Adds word to the data structure, it can be matched later"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True

    def search(self, word: str) -> bool:
        """
        Returns true if there is any string in the data structure that matches word or false otherwise.
        word may contain dots '.' where dots can be matched with any letter
        """
        node = self.root
        self.search_result = False
        self.search_dfs(node, word)
        return self.search_result

    def search_dfs(self, node, word):
        if not word:
            if node.word:
                self.search_result = True
            return

        if word[0] == '.':
            for node in node.children.values():
                self.search_dfs(node, word[1:])

        else:
            node = node.children.get(word[0])
            if not node:
                return
            self.search_dfs(node, word[1:])


class TestWordDictionary(unittest.TestCase):
    def test_example_1(self):
        word_dictionary = WordDictionary()
        word_dictionary.addWord("bad")
        word_dictionary.addWord("dad")
        word_dictionary.addWord("mad")

        with self.subTest('Search 1'):
            self.assertFalse(word_dictionary.search("pad"))

        with self.subTest('Search 2'):
            self.assertTrue(word_dictionary.search("bad"))

        with self.subTest('Search 3'):
            self.assertTrue(word_dictionary.search(".ad"))

        with self.subTest('Search 4'):
            self.assertTrue(word_dictionary.search("b.."))

    def test_example_2(self):
        word_dictionary = WordDictionary()
        word_dictionary.addWord("a")
        word_dictionary.addWord("a")

        with self.subTest('Search 1'):
            self.assertTrue(word_dictionary.search("."))

        with self.subTest('Search 2'):
            self.assertTrue(word_dictionary.search("a"))

        with self.subTest('Search 3'):
            self.assertFalse(word_dictionary.search("aa"))

        with self.subTest('Search 4'):
            self.assertTrue(word_dictionary.search("a"))

        with self.subTest('Search 5'):
            self.assertFalse(word_dictionary.search(".a"))

        with self.subTest('Search 6'):
            self.assertFalse(word_dictionary.search("a."))


if __name__ == '__main__':
    unittest.main()
