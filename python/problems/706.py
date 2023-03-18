from common import *


class MyHashMap:
    def __init__(self):
        """
        Initializes the object with an empty map.
        """
        self.storage = [None] * 1000001

    def put(self, key: int, value: int) -> None:
        """
        Inserts a (key, value) pair into the HashMap.
        If the key already exists in the map, update the corresponding value
        """
        self.storage[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
        """
        value = self.storage[key]
        return value if value is not None else -1

    def remove(self, key: int) -> None:
        """
        Removes the key and its corresponding value if the map contains the mapping for the key.
        """
        self.storage[key] = None


class TestMyHashMap(unittest.TestCase):
    def test_706(self):
        with self.subTest('Example 1'):
            my_hash_map = MyHashMap()
            my_hash_map.put(1, 1)  # The map is now [[1,1]]
            my_hash_map.put(2, 2)  # The map is now [[1,1], [2,2]]
            self.assertEqual(my_hash_map.get(1), 1)  # return 1, The map is now [[1,1], [2,2]]
            self.assertEqual(my_hash_map.get(3), -1)  # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
            my_hash_map.put(2, 1)  # The map is now [[1,1], [2,1]] (i.e., update the existing value)
            self.assertEqual(my_hash_map.get(2), 1)  # return 1, The map is now [[1,1], [2,1]]
            my_hash_map.remove(2)  # remove the mapping for 2, The map is now [[1,1]]
            self.assertEqual(my_hash_map.get(2), -1)  # return -1 (i.e., not found), The map is now [[1,1]]

        with self.subTest('Example 2'):
            my_hash_map = MyHashMap()
            my_hash_map.remove(2)
            my_hash_map.put(3, 11)
            my_hash_map.put(4, 13)
            my_hash_map.put(15, 6)
            my_hash_map.put(6, 15)
            my_hash_map.put(8, 8)
            my_hash_map.put(11, 0)
            self.assertEqual(my_hash_map.get(11), 0)
            my_hash_map.put(1, 10)
            my_hash_map.put(12, 4)


if __name__ == '__main__':
    unittest.main()
