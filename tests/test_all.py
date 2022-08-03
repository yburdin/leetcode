import unittest
from python.problems_0001to0500 import *
from python.problems_0501to1000 import *
from python.problems_1001to1500 import *
from python.problems_1501to2000 import *
from python.problems_2001to2500 import *


class Test0001to0500(unittest.TestCase):
    def test_028(self):
        self.assertEqual(str_str(haystack="hello", needle="ll"), 2)
        self.assertEqual(str_str(haystack="aaaaa", needle="bba"), -1)
        self.assertEqual(str_str(haystack="a", needle="a"), 0)

    def test_043(self):
        self.assertEqual(multiply('2', '3'), '6')
        self.assertEqual(multiply('123', '456'), '56088')

    def test_058(self):
        self.assertEqual(length_of_last_word("Hello World"), 5)
        self.assertEqual(length_of_last_word("   fly me   to   the moon  "), 4)
        self.assertEqual(length_of_last_word("luffy is still joyboy"), 6)

    def test_066(self):
        self.assertEqual(plus_one([1, 2, 3]), [1, 2, 4])
        self.assertEqual(plus_one([4, 3, 2, 1]), [4, 3, 2, 2])
        self.assertEqual(plus_one([9]), [1, 0])

    def test_067(self):
        self.assertEqual(add_binary(a="11", b="1"), "100")
        self.assertEqual(add_binary(a="1010", b="1011"), "10101")

    def test_070(self):
        self.assertEqual(climb_stairs(2), 2)
        self.assertEqual(climb_stairs(3), 3)
        self.assertEqual(climb_stairs(4), 5)
        self.assertEqual(climb_stairs(5), 8)

    def test_119(self):
        self.assertEqual(get_row(3), [1, 3, 3, 1])
        self.assertEqual(get_row(0), [1])
        self.assertEqual(get_row(1), [1, 1])

    def test_150(self):
        self.assertEqual(eval_rpn(["2", "1", "+", "3", "*"]), 9)
        self.assertEqual(eval_rpn(["4", "13", "5", "/", "+"]), 6)
        self.assertEqual(eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]), 22)

    def test_191(self):
        self.assertEqual(hamming_weight(0b00000000000000000000000000001011), 3)
        self.assertEqual(hamming_weight(0b00000000000000000000000010000000), 1)
        self.assertEqual(hamming_weight(0b11111111111111111111111111111101), 31)

    def test_202(self):
        self.assertEqual(is_happy(19), True)
        self.assertEqual(is_happy(2), False)

    def test_217(self):
        self.assertTrue(contains_duplicate([1, 2, 3, 1]))
        self.assertFalse(contains_duplicate([1, 2, 3, 4]))
        self.assertTrue(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

    def test_232(self):
        my_queue = MyQueue()
        my_queue.push(1)
        my_queue.push(2)
        self.assertEqual(my_queue.peek(), 1)
        self.assertEqual(my_queue.pop(), 1)
        self.assertFalse(my_queue.empty())

    def test_242(self):
        self.assertTrue(is_anagram(s="anagram", t="nagaram"))
        self.assertFalse(is_anagram(s="rat", t="car"))
        self.assertFalse(is_anagram(s="ac", t="bb"))

    def test_303(self):
        num_array = NumArray([-2, 0, 3, -5, 2, -1])
        self.assertEqual(num_array.sum_range(0, 2), 1)
        self.assertEqual(num_array.sum_range(2, 5), -1)
        self.assertEqual(num_array.sum_range(0, 5), -3)

    def test_389(self):
        self.assertEqual(find_the_difference(s="abcd", t="abcde"), 'e')
        self.assertEqual(find_the_difference(s="", t="y"), 'y')
        self.assertEqual(find_the_difference(s="a", t="aa"), 'a')

    def test_405(self):
        self.assertEqual(to_hex(26), '1a')
        self.assertEqual(to_hex(-1), 'ffffffff')

    def test_459(self):
        self.assertTrue(repeated_substring_pattern("abab"))
        self.assertFalse(repeated_substring_pattern("aba"))
        self.assertTrue(repeated_substring_pattern("abcabcabcabc"))
        self.assertFalse(repeated_substring_pattern("aabaaba"))

    def test_496(self):
        self.assertEqual(next_greater_element([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1])
        self.assertEqual(next_greater_element([2, 4], [1, 2, 3, 4]), [3, -1])

    def test_048(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        rotate(matrix)
        self.assertEqual(matrix, [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

        matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        rotate(matrix)
        self.assertEqual(matrix, [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]])


class Test0501to1000(unittest.TestCase):
    def test_709(self):
        self.assertEqual(to_lower_case("Hello"), "hello")
        self.assertEqual(to_lower_case("here"), "here")
        self.assertEqual(to_lower_case("LOVELY"), "lovely")

    def test_739(self):
        self.assertEqual(daily_temperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0])
        self.assertEqual(daily_temperatures(temperatures=[30, 40, 50, 60]), [1, 1, 1, 0])
        self.assertEqual(daily_temperatures(temperatures=[30, 60, 90]), [1, 1, 0])
        self.assertEqual(daily_temperatures(temperatures=[89, 62, 70, 58, 47, 47, 46, 76, 100, 70]),
                         [8, 1, 5, 4, 3, 2, 1, 1, 0, 0])

    def test_797(self):
        self.assertCountEqual(all_paths_source_target([[1, 2], [3], [3], []]),
                              [[0, 1, 3], [0, 2, 3]])
        self.assertCountEqual(all_paths_source_target([[4, 3, 1], [3, 2, 4], [3], [4], []]),
                              [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]])

    def test_876(self):
        self.assertEqual(linked_list_to_list(middle_node(list_to_linked_list([1, 2, 3, 4, 5]))), [3, 4, 5])
        self.assertEqual(linked_list_to_list(middle_node(list_to_linked_list([1, 2, 3, 4, 5, 6]))), [4, 5, 6])

    def test_896(self):
        self.assertTrue(is_monotonic([1, 2, 2, 3]))
        self.assertTrue(is_monotonic([6, 5, 4, 4]))
        self.assertFalse(is_monotonic([1, 3, 2]))

    def test_953(self):
        self.assertTrue(is_alien_sorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"))
        self.assertFalse(is_alien_sorted(words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz"))
        self.assertFalse(is_alien_sorted(words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz"))

    def test_976(self):
        self.assertEqual(largest_perimeter([2, 1, 2]), 5)
        self.assertEqual(largest_perimeter([1, 2, 1]), 0)
        self.assertEqual(largest_perimeter([2, 6, 2, 5, 4, 15, 1]), 15)

    def test_989(self):
        self.assertEqual(add_to_array_form(num=[1, 2, 0, 0], k=34), [1, 2, 3, 4])
        self.assertEqual(add_to_array_form(num=[2, 7, 4], k=181), [4, 5, 5])
        self.assertEqual(add_to_array_form(num=[2, 1, 5], k=806), [1, 0, 2, 1])
        self.assertEqual(add_to_array_form(num=[0], k=23), [2, 3])
        self.assertEqual(add_to_array_form(num=[0], k=10000), [1, 0, 0, 0, 0])


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

    def test_1290(self):
        self.assertEqual(get_decimal_value(list_to_linked_list([1, 0, 1])), 5)
        self.assertEqual(get_decimal_value(list_to_linked_list([0])), 0)
        self.assertEqual(get_decimal_value(list_to_linked_list([1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0])), 18880)

    def test_1309(self):
        self.assertEqual(freq_alphabets("10#11#12"), "jkab")
        self.assertEqual(freq_alphabets("1326#"), "acz")

    def test_1356(self):
        self.assertEqual(sort_by_bits([0, 1, 2, 3, 4, 5, 6, 7, 8]), [0, 1, 2, 4, 8, 3, 5, 6, 7])
        self.assertEqual(sort_by_bits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]),
                         [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024])

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

    def test_1603(self):
        parking_system = ParkingSystem(1, 1, 0)
        self.assertTrue(parking_system.add_car(1))
        self.assertTrue(parking_system.add_car(2))
        self.assertFalse(parking_system.add_car(3))
        self.assertFalse(parking_system.add_car(1))

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

    def test_1886(self):
        self.assertTrue(find_rotation(mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]], target=[[1, 1, 1], [0, 1, 0], [0, 0, 0]]))
        self.assertTrue(find_rotation(mat=[[0, 1], [1, 0]], target=[[1, 0], [0, 1]]))
        self.assertFalse(find_rotation(mat=[[0, 1], [1, 1]], target=[[1, 0], [0, 1]]))
        self.assertTrue(find_rotation(mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]], target=[[1, 0, 0], [1, 1, 0], [1, 0, 0]]))


class Test2001to2500(unittest.TestCase):
    def test_2053(self):
        self.assertEqual(kth_distinct(["d", "b", "c", "b", "c", "a"], 2), "a")
        self.assertEqual(kth_distinct(["aaa", "aa", "a"], 1), "aaa")
        self.assertEqual(kth_distinct(["a", "b", "a"], 3), "")

    def test_2073(self):
        self.assertEqual(time_required_to_buy([2, 3, 2], 2), 6)
        self.assertEqual(time_required_to_buy([5, 1, 1, 1], 0), 8)
        self.assertEqual(time_required_to_buy([84, 49, 5, 24, 70, 77, 87, 8], 3), 154)

    def test_2221(self):
        self.assertEqual(triangular_sum([1, 2, 3, 4, 5]), 8)
        self.assertEqual(triangular_sum([5]), 5)


def list_to_linked_list(nodes: List[int]) -> ListNode:
    result = ListNode(val=nodes.pop(-1), next_=None)
    while len(nodes) > 0:
        result = ListNode(val=nodes.pop(-1), next_=result)

    return result


def linked_list_to_list(head: ListNode) -> List:
    result = [head.val]
    while head.next:
        result.append(head.next.val)
        head = head.next

    return result


if __name__ == '__main__':
    unittest.main()
