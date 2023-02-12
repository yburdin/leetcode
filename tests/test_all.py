import unittest
from python.problems_0001to0500 import *
from python.problems_0501to1000 import *
from python.problems_1001to1500 import *
from python.problems_1501to2000 import Solution as Solution4
from python.problems_2001to2500 import Solution as Solution5
from classes import *


class Test0001to0500(unittest.TestCase):
    def test_06(self):
        with self.subTest('Example 1'):
            self.assertEqual(convert(s="PAYPALISHIRING", num_rows=3), 'PAHNAPLSIIGYIR')

        with self.subTest('Example 2'):
            self.assertEqual(convert(s="PAYPALISHIRING", num_rows=4), 'PINALSIGYAHRPI')

        with self.subTest('Example 3'):
            self.assertEqual(convert(s="A", num_rows=1), 'A')

        with self.subTest('Example 4'):
            self.assertEqual(convert(s="ABCDE", num_rows=4), 'ABCED')

    def test_20(self):
        with self.subTest('Example 1'):
            self.assertEqual(is_valid(s="()"), True)

        with self.subTest('Example 2'):
            self.assertEqual(is_valid(s="()[]{}"), True)

        with self.subTest('Example 3'):
            self.assertEqual(is_valid(s="(]"), False)

        with self.subTest('Example 4'):
            self.assertEqual(is_valid(s="]"), False)

    def test_016(self):
        with self.subTest('Example 1'):
            self.assertEqual(int_to_roman(3), 'III')

        with self.subTest('Example 2'):
            self.assertEqual(int_to_roman(58), 'LVIII')

        with self.subTest('Example 3'):
            self.assertEqual(int_to_roman(1994), 'MCMXCIV')

    def test_028(self):
        self.assertEqual(str_str(haystack="hello", needle="ll"), 2)
        self.assertEqual(str_str(haystack="aaaaa", needle="bba"), -1)
        self.assertEqual(str_str(haystack="a", needle="a"), 0)

    def test_043(self):
        self.assertEqual(multiply('2', '3'), '6')
        self.assertEqual(multiply('123', '456'), '56088')

    def test_045(self):
        with self.subTest('Example 1'):
            self.assertEqual(jump(nums=[2, 3, 1, 1, 4]), 2)

        with self.subTest('Example 2'):
            self.assertEqual(jump(nums=[2, 3, 0, 1, 4]), 2)

    def test_048(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        rotate(matrix)
        self.assertEqual(matrix, [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

        matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        rotate(matrix)
        self.assertEqual(matrix, [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]])

    def test_049(self):
        input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        anagrams = [sorted(anagram) for anagram in group_anagrams(input_strs)]
        self.assertCountEqual(anagrams, output)

        self.assertCountEqual(group_anagrams([""]),
                              [[""]])
        self.assertCountEqual(group_anagrams(["a"]),
                              [["a"]])

        input_strs = ["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"]
        output = [["max"], ["buy"], ["doc"], ["may"], ["ill"], ["duh"], ["tin"], ["bar"], ["pew"], ["cab"]]
        anagrams = [sorted(anagram) for anagram in group_anagrams(input_strs)]
        self.assertCountEqual(sorted(anagrams), sorted(output))

    def test_054(self):
        self.assertEqual(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5])
        self.assertEqual(spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]),
                         [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
        self.assertEqual(spiral_order([[7], [9], [6]]), [7, 9, 6])

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

    def test_355(self):
        with self.subTest('Example 1'):
            twitter = Twitter()

            # User 1 posts a new tweet (id = 5).
            twitter.postTweet(1, 5)

            # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
            twitter.getNewsFeed(1)

            # User 1 follows user 2.
            twitter.follow(1, 2)

            # User 2 posts a new tweet (id = 6).
            twitter.postTweet(2, 6)

            # User 1's news feed should return a list with 2 tweet ids -> [6, 5].
            # Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
            self.assertEqual(twitter.getNewsFeed(1), [6, 5])

            # User 1 unfollows user 2.
            twitter.unfollow(1, 2)

            # User 1's news feed should return a list with 1 tweet id -> [5],
            # since user 1 is no longer following user 2.
            self.assertEqual(twitter.getNewsFeed(1), [5])

    def test_389(self):
        self.assertEqual(find_the_difference(s="abcd", t="abcde"), 'e')
        self.assertEqual(find_the_difference(s="", t="y"), 'y')
        self.assertEqual(find_the_difference(s="a", t="aa"), 'a')

    def test_405(self):
        self.assertEqual(to_hex(26), '1a')
        self.assertEqual(to_hex(-1), 'ffffffff')

    def test_438(self):
        self.assertEqual(find_anagrams(s="cbaebabacd", p="abc"), [0, 6])
        self.assertEqual(find_anagrams(s="abab", p="ab"), [0, 1, 2])

    def test_459(self):
        self.assertTrue(repeated_substring_pattern("abab"))
        self.assertFalse(repeated_substring_pattern("aba"))
        self.assertTrue(repeated_substring_pattern("abcabcabcabc"))
        self.assertFalse(repeated_substring_pattern("aabaaba"))

    def test_496(self):
        self.assertEqual(next_greater_element([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1])
        self.assertEqual(next_greater_element([2, 4], [1, 2, 3, 4]), [3, -1])

    def test_304(self):
        num_matrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
        param_1 = num_matrix.sumRegion(2, 1, 4, 3)
        param_2 = num_matrix.sumRegion(1, 1, 2, 2)
        param_3 = num_matrix.sumRegion(1, 2, 2, 4)

        self.assertEqual(param_1, 8)
        self.assertEqual(param_2, 11)
        self.assertEqual(param_3, 12)

        num_matrix = NumMatrix([[-4, -5]])
        param_1 = num_matrix.sumRegion(0, 0, 0, 0)
        param_2 = num_matrix.sumRegion(0, 0, 0, 1)
        param_3 = num_matrix.sumRegion(0, 1, 0, 1)

        self.assertEqual(param_1, -4)
        self.assertEqual(param_2, -9)
        self.assertEqual(param_3, -5)

    def test_342(self):
        self.assertTrue(is_power_of_four(16))
        self.assertTrue(is_power_of_four(1))
        self.assertFalse(is_power_of_four(5))

    def test_062(self):
        with self.subTest('Example 1'):
            self.assertEqual(unique_paths(m=3, n=7), 28)

        with self.subTest('Example 2'):
            self.assertEqual(unique_paths(m=3, n=2), 3)

        with self.subTest('Example 2'):
            self.assertEqual(unique_paths(m=57, n=2), 57)

    def test_063(self):
        with self.subTest('Example 1'):
            self.assertEqual(unique_paths_with_obstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 2)

        with self.subTest('Example 2'):
            self.assertEqual(unique_paths_with_obstacles([[0, 1], [0, 0]]), 1)

        with self.subTest('Example 3'):
            self.assertEqual(unique_paths_with_obstacles([[0]]), 1)

        with self.subTest('Example 4'):
            self.assertEqual(unique_paths_with_obstacles([[1, 0]]), 0)

        with self.subTest('Example 5'):
            self.assertEqual(unique_paths_with_obstacles([[0, 0], [1, 1], [0, 0]]), 0)

    def test_038(self):
        with self.subTest('Example 1'):
            self.assertEqual(count_and_say(1), '1')

        with self.subTest('Example 2'):
            self.assertEqual(count_and_say(4), '1211')


class Test0501to1000(unittest.TestCase):
    def test_503(self):
        self.assertEqual(next_greater_elements([1, 2, 1]), [2, -1, 2])
        self.assertEqual(next_greater_elements([1, 2, 3, 4, 3]), [2, 3, 4, -1, 4])
        self.assertEqual(next_greater_elements([5, 4, 3, 2, 1]), [-1, 5, 5, 5, 5])
        self.assertEqual(next_greater_elements([1, 5, 3, 6, 8]), [5, 6, 6, 8, -1])

    def test_556(self):
        self.assertEqual(next_greater_element_iii(234157641), 234161457)
        self.assertEqual(next_greater_element_iii(12), 21)
        self.assertEqual(next_greater_element_iii(21), -1)
        self.assertEqual(next_greater_element_iii(364), 436)
        self.assertEqual(next_greater_element_iii(346), 364)
        self.assertEqual(next_greater_element_iii(1488), 1848)
        self.assertEqual(next_greater_element_iii(1312), 1321)
        self.assertEqual(next_greater_element_iii(2147483486), -1)

    def test_567(self):
        with self.subTest('Example 1'):
            self.assertEqual(check_inclusion(s1="ab", s2="eidbaooo"), True)

        with self.subTest('Example 2'):
            self.assertEqual(check_inclusion(s1="ab", s2="eidboaoo"), False)

    def test_709(self):
        self.assertEqual(to_lower_case("Hello"), "hello")
        self.assertEqual(to_lower_case("here"), "here")
        self.assertEqual(to_lower_case("LOVELY"), "lovely")

    def test_713(self):
        self.assertEqual(num_subarray_product_less_than_k(nums=[10, 5, 2, 6], k=100), 8)
        self.assertEqual(num_subarray_product_less_than_k(nums=[1, 2, 3], k=0), 0)

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

    def test_973(self):
        self.assertCountEqual(k_closest(points=[[1, 3], [-2, 2]], k=1), [[-2, 2]])
        self.assertCountEqual(k_closest(points=[[3, 3], [5, -1], [-2, 4]], k=2), [[3, 3], [-2, 4]])
        self.assertCountEqual(k_closest([[0, 1], [1, 0]], 2), [[0, 1], [1, 0]])
        self.assertCountEqual(k_closest([[6, 10], [-3, 3], [-2, 5], [0, 2]], 3), [[0, 2], [-3, 3], [-2, 5]])

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

    def test_910(self):
        self.assertEqual(smallest_range_ii(nums=[1], k=0), 0)
        self.assertEqual(smallest_range_ii(nums=[0, 10], k=2), 6)
        self.assertEqual(smallest_range_ii(nums=[1, 3, 6], k=3), 3)

    def test_804(self):
        self.assertEqual(unique_morse_representations(["gin", "zen", "gig", "msg"]), 2)
        self.assertEqual(unique_morse_representations(["a"]), 1)

    def test_860(self):
        self.assertTrue(lemonade_change([5, 5, 5, 10, 20]))
        self.assertFalse(lemonade_change([5, 5, 10, 10, 20]))

    def test_707(self):
        with self.subTest(msg='Testcase 1'):
            my_linked_list = MyLinkedList()
            my_linked_list.addAtHead(1)
            my_linked_list.addAtTail(3)
            my_linked_list.addAtIndex(1, 2)                 # linked list becomes 1->2->3
            self.assertEqual(my_linked_list.get(1), 2)      # return 2

            my_linked_list.deleteAtIndex(1)                 # now the linked list is 1->3
            self.assertEqual(my_linked_list.get(1), 3)      # return 3

        with self.subTest(msg='Testcase 2'):
            my_linked_list = MyLinkedList()
            my_linked_list.addAtHead(7)
            my_linked_list.addAtHead(2)
            my_linked_list.addAtHead(1)
            my_linked_list.addAtIndex(3, 0)
            my_linked_list.deleteAtIndex(2)
            my_linked_list.addAtHead(6)
            my_linked_list.addAtTail(4)
            self.assertEqual(my_linked_list.get(4), 4)

            my_linked_list.addAtHead(4)
            my_linked_list.addAtIndex(5, 0)
            my_linked_list.addAtHead(6)

        with self.subTest(msg='Testcase 3'):
            my_linked_list = MyLinkedList()
            my_linked_list.addAtIndex(0, 10)
            my_linked_list.addAtIndex(0, 20)
            my_linked_list.addAtIndex(1, 30)
            self.assertEqual(my_linked_list.get(0), 20)

        with self.subTest(msg='Testcase 4'):
            my_linked_list = MyLinkedList()
            my_linked_list.addAtTail(1)
            self.assertEqual(my_linked_list.get(0), 1)

        with self.subTest(msg='Testcase 5'):
            my_linked_list = MyLinkedList()
            my_linked_list.addAtHead(4)
            self.assertEqual(my_linked_list.get(1), -1)
            my_linked_list.addAtHead(1)
            my_linked_list.addAtHead(5)
            my_linked_list.deleteAtIndex(3)
            my_linked_list.addAtHead(7)
            self.assertEqual(my_linked_list.get(3), 4)
            self.assertEqual(my_linked_list.get(3), 4)
            self.assertEqual(my_linked_list.get(3), 4)
            my_linked_list.addAtHead(1)
            my_linked_list.deleteAtIndex(4)

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

    def test_692(self):
        with self.subTest('Example 1'):
            self.assertCountEqual(top_k_frequent(words=["i", "love", "leetcode", "i", "love", "coding"], k=2),
                                  ["i", "love"])

        with self.subTest('Example 2'):
            self.assertCountEqual(
                top_k_frequent(words=["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k=4),
                ["the", "is", "sunny", "day"])

    def test_904(self):
        with self.subTest('Example 1'):
            self.assertEqual(total_fruit(fruits=[1, 2, 1]), 3)

        with self.subTest('Example 2'):
            self.assertEqual(total_fruit(fruits=[0, 1, 2, 2]), 3)

        with self.subTest('Example 3'):
            self.assertEqual(total_fruit(fruits=[1, 2, 3, 2, 2]), 4)

        with self.subTest('Example 4'):
            self.assertEqual(total_fruit(fruits=[3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]), 5)

        with self.subTest('Example 5'):
            self.assertEqual(total_fruit(fruits=[0, 1, 6, 6, 4, 4, 6]), 5)


class Test1001to1500(unittest.TestCase):
    def test_1071(self):
        with self.subTest('Example 1'):
            self.assertEqual(gcd_of_strings(str1="ABCABC", str2="ABC"), 'ABC')

        with self.subTest('Example 2'):
            self.assertEqual(gcd_of_strings(str1="ABABAB", str2="ABAB"), 'AB')

        with self.subTest('Example 3'):
            self.assertEqual(gcd_of_strings(str1="LEET", str2="CODE"), '')

        with self.subTest('Example 4'):
            self.assertEqual(gcd_of_strings(str1="TAUXXTAUXXTAUXXTAUXXTAUXX",
                                            str2="TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"), 'TAUXX')

    def test_1129(self):
        with self.subTest('Example 1'):
            self.assertEqual(shortest_alternating_paths(n=3, redEdges=[[0, 1], [1, 2]], blueEdges=[]), [0, 1, -1])

        with self.subTest('Example 2'):
            self.assertEqual(shortest_alternating_paths(n=3, redEdges=[[0, 1]], blueEdges=[[2, 1]]), [0, 1, -1])

    def test_1162(self):
        with self.subTest('Example 1'):
            self.assertEqual(max_distance(grid=[[1, 0, 1], [0, 0, 0], [1, 0, 1]]), 2)

        with self.subTest('Example 2'):
            self.assertEqual(max_distance(grid=[[1, 0, 0], [0, 0, 0], [0, 0, 0]]), 4)

        with self.subTest('Example 3'):
            self.assertEqual(max_distance(
                grid=[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]), -1)

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

    def test_1295(self):
        with self.subTest('Example 1'):
            self.assertEqual(find_numbers(nums=[12, 345, 2, 6, 7896]), 2)

        with self.subTest('Example 2'):
            self.assertEqual(find_numbers(nums=[555, 901, 482, 1771]), 1)

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

    def test_1470(self):
        with self.subTest('Example 1'):
            self.assertEqual(shuffle(nums=[2, 5, 1, 3, 4, 7], n=3), [2, 3, 5, 4, 1, 7])

        with self.subTest('Example 2'):
            self.assertEqual(shuffle(nums=[1, 2, 3, 4, 4, 3, 2, 1], n=4), [1, 4, 2, 3, 3, 2, 4, 1])

        with self.subTest('Example 3'):
            self.assertEqual(shuffle(nums=[1, 1, 2, 2], n=2), [1, 2, 1, 2])

    def test_1491(self):
        self.assertEqual(average([4000, 3000, 1000, 2000]), 2500.)
        self.assertEqual(average([1000, 2000, 3000]), 2000.)

    def test_1323(self):
        with self.subTest('Example 1'):
            self.assertEqual(maximum_69_number(9669), 9969)

        with self.subTest('Example 2'):
            self.assertEqual(maximum_69_number(9996), 9999)

        with self.subTest('Example 3'):
            self.assertEqual(maximum_69_number(9999), 9999)

    def test_1266(self):
        with self.subTest('Example 1'):
            self.assertEqual(min_time_to_visit_all_points([[1, 1], [3, 4], [-1, 0]]), 7)

        with self.subTest('Example 2'):
            self.assertEqual(min_time_to_visit_all_points([[3, 2], [-2, 2]]), 5)


class Test1501to2000(unittest.TestCase):
    def test_1502(self):
        solution = Solution4()
        self.assertEqual(solution.can_make_arithmetic_progression([3, 5, 1]), True)
        self.assertEqual(solution.can_make_arithmetic_progression([1, 2, 4]), False)

    def test_1523(self):
        solution = Solution4()
        self.assertEqual(solution.count_odds(3, 7), 3)
        self.assertEqual(solution.count_odds(8, 10), 1)

    def test_1572(self):
        solution = Solution4()
        self.assertEqual(solution.diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 25)
        self.assertEqual(solution.diagonal_sum(
            [[1, 1, 1, 1],
             [1, 1, 1, 1],
             [1, 1, 1, 1],
             [1, 1, 1, 1]]), 8)
        self.assertEqual(solution.diagonal_sum([[5]]), 5)

    def test_1588(self):
        solution = Solution4()
        self.assertEqual(solution.sum_odd_length_subarrays([1, 4, 2, 5, 3]), 58)
        self.assertEqual(solution.sum_odd_length_subarrays([1, 2]), 3)
        self.assertEqual(solution.sum_odd_length_subarrays([10, 11, 12]), 66)

    def test_1603(self):
        parking_system = ParkingSystem(1, 1, 0)
        self.assertTrue(parking_system.add_car(1))
        self.assertTrue(parking_system.add_car(2))
        self.assertFalse(parking_system.add_car(3))
        self.assertFalse(parking_system.add_car(1))

    def test_1630(self):
        solution = Solution4()
        self.assertEqual(
            solution.check_arithmetic_subarrays(nums=[4, 6, 5, 9, 3, 7], l=[0, 0, 2], r=[2, 3, 5]
                                                ), [True, False, True])
        self.assertEqual(
            solution.check_arithmetic_subarrays(nums=[-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10],
                                                l=[0, 1, 6, 4, 8, 7],
                                                r=[4, 4, 9, 7, 9, 10]
                                                ), [False, True, False, False, True, True])

    def test_1672(self):
        solution = Solution4()
        self.assertEqual(solution.maximum_wealth([[1, 2, 3], [3, 2, 1]]), 6)
        self.assertEqual(solution.maximum_wealth([[1, 5], [7, 3], [3, 5]]), 10)
        self.assertEqual(solution.maximum_wealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]), 17)

    def test_1678(self):
        solution = Solution4()
        self.assertEqual(solution.interpret("G()(al)"), "Goal")
        self.assertEqual(solution.interpret("G()()()()(al)"), "Gooooal")
        self.assertEqual(solution.interpret("(al)G(al)()()G"), "alGalooG")

    def test_1700(self):
        solution = Solution4()
        self.assertEqual(solution.count_students([1, 1, 0, 0], [0, 1, 0, 1]), 0)
        self.assertEqual(solution.count_students([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]), 3)

    def test_1732(self):
        solution = Solution4()
        self.assertEqual(solution.largest_altitude([-5, 1, 5, 0, -7]), 1)
        self.assertEqual(solution.largest_altitude([-4, -3, -2, -1, 4, 3, 2]), 0)

    def test_1768(self):
        solution = Solution4()
        self.assertEqual(solution.merge_alternately(word1="abc", word2="pqr"), "apbqcr")
        self.assertEqual(solution.merge_alternately(word1="ab", word2="pqrs"), "apbqrs")
        self.assertEqual(solution.merge_alternately(word1="abcd", word2="pq"), "apbqcd")

    def test_1779(self):
        solution = Solution4()
        self.assertEqual(solution.nearest_valid_point(3, 4, [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]), 2)
        self.assertEqual(solution.nearest_valid_point(3, 4, [[3, 4]]), 0)
        self.assertEqual(solution.nearest_valid_point(3, 4, [[2, 3]]), -1)

    def test_1790(self):
        solution = Solution4()
        self.assertEqual(solution.are_almost_equal("bank", "kanb"), True)
        self.assertEqual(solution.are_almost_equal("attack", "defend"), False)
        self.assertEqual(solution.are_almost_equal("kelb", "kelb"), True)

    def test_1816(self):
        solution = Solution4()
        with self.subTest('Example 1'):
            self.assertEqual(solution.truncate_sentence(s="Hello how are you Contestant", k=4), "Hello how are you")

        with self.subTest('Example 1'):
            self.assertEqual(solution.truncate_sentence(s="What is the solution to this problem", k=4),
                             "What is the solution")

    def test_1822(self):
        solution = Solution4()
        self.assertEqual(solution.array_sign([-1, -2, -3, -4, 3, 2, 1]), 1)
        self.assertEqual(solution.array_sign([1, 5, 0, 2, -3]), 0)
        self.assertEqual(solution.array_sign([-1, 1, -1, 1, -1]), -1)

    def test_1828(self):
        solution = Solution4()
        self.assertEqual(solution.count_points([[1, 3], [3, 3], [5, 3], [2, 2]], [[2, 3, 1], [4, 3, 1], [1, 1, 2]]),
                         [3, 2, 2])
        self.assertEqual(
            solution.count_points([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],
                                  [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]]),
            [2, 3, 2, 4])

    def test_1886(self):
        solution = Solution4()
        self.assertTrue(
            solution.find_rotation(mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]], target=[[1, 1, 1], [0, 1, 0], [0, 0, 0]]))
        self.assertTrue(solution.find_rotation(mat=[[0, 1], [1, 0]], target=[[1, 0], [0, 1]]))
        self.assertFalse(solution.find_rotation(mat=[[0, 1], [1, 1]], target=[[1, 0], [0, 1]]))
        self.assertTrue(
            solution.find_rotation(mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]], target=[[1, 0, 0], [1, 1, 0], [1, 0, 0]]))

    def test_1925(self):
        solution = Solution4()
        self.assertEqual(solution.count_triples(5), 2)
        self.assertEqual(solution.count_triples(10), 4)

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


class Test2001to2500(unittest.TestCase):
    def test_2053(self):
        solution = Solution5()
        self.assertEqual(solution.kth_distinct(["d", "b", "c", "b", "c", "a"], 2), "a")
        self.assertEqual(solution.kth_distinct(["aaa", "aa", "a"], 1), "aaa")
        self.assertEqual(solution.kth_distinct(["a", "b", "a"], 3), "")

    def test_2073(self):
        solution = Solution5()
        self.assertEqual(solution.time_required_to_buy([2, 3, 2], 2), 6)
        self.assertEqual(solution.time_required_to_buy([5, 1, 1, 1], 0), 8)
        self.assertEqual(solution.time_required_to_buy([84, 49, 5, 24, 70, 77, 87, 8], 3), 154)

    def test_2221(self):
        solution = Solution5()
        self.assertEqual(solution.triangular_sum([1, 2, 3, 4, 5]), 8)
        self.assertEqual(solution.triangular_sum([5]), 5)

    def test_2306(self):
        solution = Solution5()
        with self.subTest('Example 1'):
            self.assertEqual(solution.distinct_names(ideas=["coffee", "donuts", "time", "toffee"]), 6)

        with self.subTest('Example 2'):
            self.assertEqual(solution.distinct_names(ideas=["lack", "back"]), 0)

        with self.subTest('Example 3'):
            self.assertEqual(solution.distinct_names(ideas=["bzklqtbdr", "kaqvdlp", "r", "dk"]), 12)

    def test_2477(self):
        with self.subTest('Example 1'):
            solution = Solution5()
            self.assertEqual(solution.minimum_fuel_cost(roads=[[0, 1], [0, 2], [0, 3]], seats=5), 3)

        with self.subTest('Example 2'):
            solution = Solution5()
            self.assertEqual(
                solution.minimum_fuel_cost(roads=[[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], seats=2), 7)

        with self.subTest('Example 3'):
            solution = Solution5()
            self.assertEqual(solution.minimum_fuel_cost(roads=[], seats=1), 0)


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
