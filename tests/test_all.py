import unittest
from python.problems_0001to0500 import *
from python.problems_0501to1000 import *
from python.problems_1001to1500 import *
from python.problems_1501to2000 import *
from python.problems_2001to2500 import *


class Test0001to0500(unittest.TestCase):
    def test_119(self):
        self.assertEqual(get_row(3), [1, 3, 3, 1])
        self.assertEqual(get_row(0), [1])
        self.assertEqual(get_row(1), [1, 1])

    def test_191(self):
        self.assertEqual(hamming_weight(0b00000000000000000000000000001011), 3)
        self.assertEqual(hamming_weight(0b00000000000000000000000010000000), 1)
        self.assertEqual(hamming_weight(0b11111111111111111111111111111101), 31)

    def test_202(self):
        self.assertEqual(is_happy(19), True)
        self.assertEqual(is_happy(2), False)

    def test_389(self):
        self.assertEqual(find_the_difference(s="abcd", t="abcde"), 'e')
        self.assertEqual(find_the_difference(s="", t="y"), 'y')
        self.assertEqual(find_the_difference(s="a", t="aa"), 'a')

    def test_405(self):
        self.assertEqual(to_hex(26), '1a')
        self.assertEqual(to_hex(-1), 'ffffffff')

    def test_496(self):
        self.assertEqual(next_greater_element([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1])
        self.assertEqual(next_greater_element([2, 4], [1, 2, 3, 4]), [3, -1])


class Test0501to1000(unittest.TestCase):
    def test_976(self):
        self.assertEqual(largest_perimeter([2, 1, 2]), 5)
        self.assertEqual(largest_perimeter([1, 2, 1]), 0)
        self.assertEqual(largest_perimeter([2, 6, 2, 5, 4, 15, 1]), 15)


class Test1001to1500(unittest.TestCase):
    def test_1232(self):
        self.assertEqual(check_straight_line([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]), True)
        self.assertEqual(check_straight_line([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]), False)
        self.assertEqual(check_straight_line([[0, 0], [0, 5], [5, 5], [5, 0]]), False)
        self.assertEqual(check_straight_line([[-3, -2], [-1, -2], [2, -2], [-2, -2], [0, -2]]), True)
        self.assertEqual(check_straight_line([[1, 2], [2, 3], [3, 5]]), False)
        self.assertEqual(check_straight_line([[1, 1], [2, 2], [2, 0]]), False)

    def test_1281(self):
        self.assertEqual(subtract_product_and_sum(234), 15)
        self.assertEqual(subtract_product_and_sum(4421), 21)

    def test_1437(self):
        self.assertEqual(k_length_apart([1, 0, 0, 0, 1, 0, 0, 1], 2), True)
        self.assertEqual(k_length_apart([1, 0, 0, 1, 0, 1], 2), False)
        self.assertEqual(k_length_apart([1, 0, 0, 0], 1), True)

    def test_1491(self):
        self.assertEqual(average([4000, 3000, 1000, 2000]), 2500.)
        self.assertEqual(average([1000, 2000, 3000]), 2000.)


class Test1501to2000(unittest.TestCase):
    def test_1502(self):
        self.assertEqual(can_make_arithmetic_progression([3, 5, 1]), True)
        self.assertEqual(can_make_arithmetic_progression([1, 2, 4]), False)

    def test_1523(self):
        self.assertEqual(count_odds(3, 7), 3)
        self.assertEqual(count_odds(8, 10), 1)

    def test_1572(self):
        self.assertEqual(diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 25)
        self.assertEqual(diagonal_sum(
            [[1, 1, 1, 1],
             [1, 1, 1, 1],
             [1, 1, 1, 1],
             [1, 1, 1, 1]]), 8)
        self.assertEqual(diagonal_sum([[5]]), 5)

    def test_1588(self):
        self.assertEqual(sum_odd_length_subarrays([1, 4, 2, 5, 3]), 58)
        self.assertEqual(sum_odd_length_subarrays([1, 2]), 3)
        self.assertEqual(sum_odd_length_subarrays([10, 11, 12]), 66)

    def test_1672(self):
        self.assertEqual(maximum_wealth([[1, 2, 3], [3, 2, 1]]), 6)
        self.assertEqual(maximum_wealth([[1, 5], [7, 3], [3, 5]]), 10)
        self.assertEqual(maximum_wealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]), 17)

    def test_1678(self):
        self.assertEqual(interpret("G()(al)"), "Goal")
        self.assertEqual(interpret("G()()()()(al)"), "Gooooal")
        self.assertEqual(interpret("(al)G(al)()()G"), "alGalooG")

    def test_1700(self):
        self.assertEqual(count_students([1, 1, 0, 0], [0, 1, 0, 1]), 0)
        self.assertEqual(count_students([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]), 3)

    def test_1732(self):
        self.assertEqual(largest_altitude([-5, 1, 5, 0, -7]), 1)
        self.assertEqual(largest_altitude([-4, -3, -2, -1, 4, 3, 2]), 0)

    def test_1768(self):
        self.assertEqual(merge_alternately(word1="abc", word2="pqr"), "apbqcr")
        self.assertEqual(merge_alternately(word1="ab", word2="pqrs"), "apbqrs")
        self.assertEqual(merge_alternately(word1="abcd", word2="pq"), "apbqcd")

    def test_1779(self):
        self.assertEqual(nearest_valid_point(3, 4, [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]), 2)
        self.assertEqual(nearest_valid_point(3, 4, [[3, 4]]), 0)
        self.assertEqual(nearest_valid_point(3, 4, [[2, 3]]), -1)

    def test_1790(self):
        self.assertEqual(are_almost_equal("bank", "kanb"), True)
        self.assertEqual(are_almost_equal("attack", "defend"), False)
        self.assertEqual(are_almost_equal("kelb", "kelb"), True)

    def test_1822(self):
        self.assertEqual(array_sign([-1, -2, -3, -4, 3, 2, 1]), 1)
        self.assertEqual(array_sign([1, 5, 0, 2, -3]), 0)
        self.assertEqual(array_sign([-1, 1, -1, 1, -1]), -1)

    def test_1828(self):
        self.assertEqual(count_points([[1, 3], [3, 3], [5, 3], [2, 2]], [[2, 3, 1], [4, 3, 1], [1, 1, 2]]), [3, 2, 2])
        self.assertEqual(
            count_points([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]]),
            [2, 3, 2, 4])

    def test_1925(self):
        self.assertEqual(count_triples(5), 2)
        self.assertEqual(count_triples(10), 4)


class Test2001to2500(unittest.TestCase):
    def test_2053(self):
        self.assertEqual(kth_distinct(["d", "b", "c", "b", "c", "a"], 2), "a")
        self.assertEqual(kth_distinct(["aaa", "aa", "a"], 1), "aaa")
        self.assertEqual(kth_distinct(["a", "b", "a"], 3), "")

    def test_2073(self):
        self.assertEqual(time_required_to_buy([2, 3, 2], 2), 6)
        self.assertEqual(time_required_to_buy([5, 1, 1, 1], 0), 8)
        self.assertEqual(time_required_to_buy([84, 49, 5, 24, 70, 77, 87, 8], 3), 154)


if __name__ == '__main__':
    unittest.main()
