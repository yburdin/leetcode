import unittest
from python.problems_0001to0500 import *
from python.problems_0501to1000 import *
from python.problems_1001to1500 import *
from python.problems_1501to2000 import Solution as Solution1501to2000
from python.problems_2001to2500 import Solution as Solution2001to2500
from python.problems_2501to3000 import Solution as Solution2501to3000
from classes import *


class Test0001to0500(unittest.TestCase):
    def test_006(self):
        with self.subTest('Example 1'):
            self.assertEqual(convert(s="PAYPALISHIRING", num_rows=3), 'PAHNAPLSIIGYIR')

        with self.subTest('Example 2'):
            self.assertEqual(convert(s="PAYPALISHIRING", num_rows=4), 'PINALSIGYAHRPI')

        with self.subTest('Example 3'):
            self.assertEqual(convert(s="A", num_rows=1), 'A')

        with self.subTest('Example 4'):
            self.assertEqual(convert(s="ABCDE", num_rows=4), 'ABCED')

    def test_016(self):
        with self.subTest('Example 1'):
            self.assertEqual(int_to_roman(3), 'III')

        with self.subTest('Example 2'):
            self.assertEqual(int_to_roman(58), 'LVIII')

        with self.subTest('Example 3'):
            self.assertEqual(int_to_roman(1994), 'MCMXCIV')

    def test_020(self):
        with self.subTest('Example 1'):
            self.assertEqual(is_valid(s="()"), True)

        with self.subTest('Example 2'):
            self.assertEqual(is_valid(s="()[]{}"), True)

        with self.subTest('Example 3'):
            self.assertEqual(is_valid(s="(]"), False)

        with self.subTest('Example 4'):
            self.assertEqual(is_valid(s="]"), False)

    def test_028(self):
        self.assertEqual(str_str(haystack="hello", needle="ll"), 2)
        self.assertEqual(str_str(haystack="aaaaa", needle="bba"), -1)
        self.assertEqual(str_str(haystack="a", needle="a"), 0)

    def test_035(self):
        with self.subTest('Example 1'):
            self.assertEqual(search_insert(nums=[1, 3, 5, 6], target=5), 2)

        with self.subTest('Example 2'):
            self.assertEqual(search_insert(nums=[1, 3, 5, 6], target=2), 1)

        with self.subTest('Example 3'):
            self.assertEqual(search_insert(nums=[1, 3, 5, 6], target=7), 4)

    def test_038(self):
        with self.subTest('Example 1'):
            self.assertEqual(count_and_say(1), '1')

        with self.subTest('Example 2'):
            self.assertEqual(count_and_say(4), '1211')

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

    def test_072(self):
        with self.subTest('Example 1'):
            self.assertEqual(min_distance(word1="horse", word2="ros"), 3)

        with self.subTest('Example 2'):
            self.assertEqual(min_distance(word1="intention", word2="execution"), 5)

    def test_094(self):
        with self.subTest('Example 1'):
            self.assertEqual(inorder_traversal(
                root=TreeNode(1, None, TreeNode(2, TreeNode(3)))
            ), [1, 3, 2])

        with self.subTest('Example 2'):
            self.assertEqual(inorder_traversal(
                root=TreeNode(1, TreeNode(3), TreeNode(2))
            ), [3, 1, 2])

        with self.subTest('Example 3'):
            self.assertEqual(inorder_traversal(
                root=TreeNode(10, TreeNode(20, TreeNode(40), TreeNode(60)), TreeNode(30, TreeNode(50)))
            ), [40, 20, 60, 10, 50, 30])

    def test_100(self):
        with self.subTest('Example 1'):
            self.assertTrue(is_same_tree(p=TreeNode(1, 2, 3), q=TreeNode(1, 2, 3)))

        with self.subTest('Example 2'):
            self.assertFalse(is_same_tree(p=TreeNode(1, 2), q=TreeNode(1, None, 2)))

        with self.subTest('Example 2'):
            self.assertFalse(is_same_tree(p=TreeNode(1, 2, 1), q=TreeNode(1, 1, 2)))

    def test_101(self):
        with self.subTest('Example 1'):
            root = TreeNode(1,
                            TreeNode(2,
                                     TreeNode(3), TreeNode(4)),
                            TreeNode(2,
                                     TreeNode(4), TreeNode(3)))

            self.assertTrue(is_symmetric(root))

        with self.subTest('Example 2'):
            root = TreeNode(1,
                            TreeNode(2,
                                     None, TreeNode(3)),
                            TreeNode(2,
                                     None, TreeNode(3)))

            self.assertFalse(is_symmetric(root))

        with self.subTest('Example 3'):
            root = TreeNode(1)
            self.assertTrue(is_symmetric(root))

    def test_103(self):
        with self.subTest('Example 1'):
            self.assertEqual(zigzag_level_order(
                TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
            ), [[3], [20, 9], [15, 7]])

        with self.subTest('Example 2'):
            self.assertEqual(zigzag_level_order(TreeNode(1)), [[1]])

        with self.subTest('Example 3'):
            self.assertEqual(zigzag_level_order(None), [])

    def test_104(self):
        with self.subTest('Example 1'):
            self.assertEqual(max_depth_binary(
                root=TreeNode(3,
                              TreeNode(9),
                              TreeNode(20,
                                       TreeNode(15),
                                       TreeNode(7)
                                       )
                              )
            ), 3)

        with self.subTest('Example 2'):
            self.assertEqual(max_depth_binary(
                root=TreeNode(1,
                              None,
                              TreeNode(2)
                              )
            ), 2)

    def test_111(self):
        with self.subTest('Example 1'):
            self.assertEqual(min_depth(root=TreeNode(3, 9, TreeNode(20, 15, 7))), 2)

        with self.subTest('Example 2'):
            self.assertEqual(
                min_depth(root=TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, 6))))), 5)

    def test_112(self):
        with self.subTest('Example 1'):
            self.assertTrue(has_path_sum(
                root=TreeNode(5,
                              TreeNode(4,
                                       TreeNode(11,
                                                TreeNode(7),
                                                TreeNode(2))),
                              TreeNode(8,
                                       TreeNode(13),
                                       TreeNode(4,
                                                None,
                                                TreeNode(1)))),
                targetSum=22
            ))

        with self.subTest('Example 2'):
            self.assertFalse(has_path_sum(root=TreeNode(1, TreeNode(2), TreeNode(3)), targetSum=5))

        with self.subTest('Example 3'):
            self.assertFalse(has_path_sum(root=None, targetSum=0))

        with self.subTest('Example 4'):
            self.assertTrue(has_path_sum(root=TreeNode(1), targetSum=1))

        with self.subTest('Example 5'):
            self.assertFalse(has_path_sum(root=TreeNode(1, TreeNode(2)), targetSum=1))

    def test_119(self):
        self.assertEqual(get_row(3), [1, 3, 3, 1])
        self.assertEqual(get_row(0), [1])
        self.assertEqual(get_row(1), [1, 1])

    def test_121(self):
        with self.subTest('Example 1'):
            self.assertEqual(max_profit(prices=[7, 1, 5, 3, 6, 4]), 5)

        with self.subTest('Example 2'):
            self.assertEqual(max_profit(prices=[7, 6, 4, 3, 1]), 0)

    def test_125(self):
        with self.subTest('Example 1'):
            self.assertTrue(is_palindrome(s="A man, a plan, a canal: Panama"))

        with self.subTest('Example 2'):
            self.assertFalse(is_palindrome(s="race a car"))

        with self.subTest('Example 3'):
            self.assertTrue(is_palindrome(s=" "))

        with self.subTest('Example 4'):
            self.assertFalse(is_palindrome(s="0P"))

    def test_134(self):
        with self.subTest('Example 1'):
            self.assertEqual(can_complete_circuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]), 3)

        with self.subTest('Example 2'):
            self.assertEqual(can_complete_circuit(gas=[2, 3, 4], cost=[3, 4, 3]), -1)

    def test_136(self):
        with self.subTest('Example 1'):
            self.assertEqual(single_number(nums=[2, 2, 1]), 1)

        with self.subTest('Example 2'):
            self.assertEqual(single_number(nums=[4, 1, 2, 1, 2]), 4)

        with self.subTest('Example 3'):
            self.assertEqual(single_number(nums=[1]), 1)

    def test_144(self):
        with self.subTest('Example 1'):
            self.assertEqual(preorder_traversal(
                root=TreeNode(1, None, TreeNode(2, TreeNode(3)))
            ), [1, 2, 3])

        with self.subTest('Example 2'):
            self.assertEqual(preorder_traversal(None), [])

        with self.subTest('Example 3'):
            self.assertEqual(preorder_traversal(TreeNode(1)), [1])

        with self.subTest('Example 4'):
            self.assertEqual(preorder_traversal(
                root=TreeNode(1, TreeNode(4, TreeNode(4), TreeNode(2)), None)
            ), [1, 4, 4, 2])

        with self.subTest('Example 5'):
            self.assertEqual(preorder_traversal(
                root=TreeNode(6,
                              TreeNode(3,
                                       None, TreeNode(1)),
                              TreeNode(2,
                                       TreeNode(2), None))
            ), [6, 3, 1, 2, 2])

    def test_150(self):
        self.assertEqual(eval_rpn(["2", "1", "+", "3", "*"]), 9)
        self.assertEqual(eval_rpn(["4", "13", "5", "/", "+"]), 6)
        self.assertEqual(eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]), 22)

    def test_171(self):
        with self.subTest('Example 1'):
            self.assertEqual(title_to_number('A'), 1)

        with self.subTest('Example 2'):
            self.assertEqual(title_to_number('AB'), 28)

        with self.subTest('Example 3'):
            self.assertEqual(title_to_number('ZY'), 701)

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

    def test_219(self):
        with self.subTest('Example 1'):
            self.assertTrue(contains_nearby_duplicate(nums=[1, 2, 3, 1], k=3))

        with self.subTest('Example 2'):
            self.assertTrue(contains_nearby_duplicate(nums=[1, 0, 1, 1], k=1))

        with self.subTest('Example 3'):
            self.assertFalse(contains_nearby_duplicate(nums=[1, 2, 3, 1, 2, 3], k=2))

        with self.subTest('Example 4'):
            self.assertTrue(contains_nearby_duplicate(nums=[99, 99], k=2))

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

    def test_257(self):
        with self.subTest('Example 1'):
            self.assertCountEqual(binary_tree_paths(
                root=TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))),
                ["1->2->5", "1->3"]
            )

    def test_268(self):
        with self.subTest('Example 1'):
            self.assertEqual(missing_number(nums=[3, 0, 1]), 2)

        with self.subTest('Example 2'):
            self.assertEqual(missing_number(nums=[0, 1]), 2)

        with self.subTest('Example 3'):
            self.assertEqual(missing_number(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)

        with self.subTest('Example 3'):
            self.assertEqual(missing_number(nums=[1]), 0)

    def test_290(self):
        with self.subTest('Example 1'):
            self.assertTrue(word_pattern(pattern="abba", s="dog cat cat dog"))

        with self.subTest('Example 2'):
            self.assertFalse(word_pattern(pattern="abba", s="dog cat cat fish"))

        with self.subTest('Example 3'):
            self.assertFalse(word_pattern(pattern="aaaa", s="dog cat cat dog"))

        with self.subTest('Example 4'):
            self.assertFalse(word_pattern(pattern="abba", s="dog dog dog dog"))

        with self.subTest('Example 5'):
            self.assertFalse(word_pattern(pattern="aba", s="cat cat cat dog"))

    def test_303(self):
        num_array = NumArray([-2, 0, 3, -5, 2, -1])
        self.assertEqual(num_array.sum_range(0, 2), 1)
        self.assertEqual(num_array.sum_range(2, 5), -1)
        self.assertEqual(num_array.sum_range(0, 5), -3)

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

    def test_316(self):
        with self.subTest('Example 1'):
            self.assertEqual(remove_duplicate_letters(s="bcabc"), 'abc')

        with self.subTest('Example 2'):
            self.assertEqual(remove_duplicate_letters(s="cbacdcbc"), 'acdb')

    def test_342(self):
        self.assertTrue(is_power_of_four(16))
        self.assertTrue(is_power_of_four(1))
        self.assertFalse(is_power_of_four(5))

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

    def test_392(self):
        with self.subTest('Example 1'):
            self.assertTrue(is_subsequence(s="abc", t="ahbgdc"))

        with self.subTest('Example 2'):
            self.assertFalse(is_subsequence(s="axc", t="ahbgdc"))

        with self.subTest('Example 3'):
            self.assertTrue(is_subsequence(s="", t="ahbgdc"))

        with self.subTest('Example 4'):
            self.assertFalse(is_subsequence(s="axc", t=""))

    def test_405(self):
        self.assertEqual(to_hex(26), '1a')
        self.assertEqual(to_hex(-1), 'ffffffff')

    def test_413(self):
        with self.subTest('Example 1'):
            self.assertEqual(number_of_arithmetic_slices(nums=[1, 2, 3, 4]), 3)

        with self.subTest('Example 2'):
            self.assertEqual(number_of_arithmetic_slices(nums=[1]), 0)

    def test_438(self):
        self.assertEqual(find_anagrams(s="cbaebabacd", p="abc"), [0, 6])
        self.assertEqual(find_anagrams(s="abab", p="ab"), [0, 1, 2])

    def test_443(self):
        with self.subTest('Example 1'):
            self.assertEqual(compress(chars=["a", "a", "b", "b", "c", "c", "c"]), 6)

        with self.subTest('Example 2'):
            self.assertEqual(compress(chars=["a"]), 1)

        with self.subTest('Example 3'):
            self.assertEqual(compress(chars=["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]), 4)

    def test_459(self):
        self.assertTrue(repeated_substring_pattern("abab"))
        self.assertFalse(repeated_substring_pattern("aba"))
        self.assertTrue(repeated_substring_pattern("abcabcabcabc"))
        self.assertFalse(repeated_substring_pattern("aabaaba"))

    def test_463(self):
        with self.subTest('Example 1'):
            self.assertEqual(island_perimeter(grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]), 16)

        with self.subTest('Example 2'):
            self.assertEqual(island_perimeter(grid=[[1]]), 4)

        with self.subTest('Example 3'):
            self.assertEqual(island_perimeter(grid=[[1, 0]]), 4)

        with self.subTest('Example 4'):
            self.assertEqual(island_perimeter(grid=[[1, 1]]), 6)

    def test_496(self):
        self.assertEqual(next_greater_element([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1])
        self.assertEqual(next_greater_element([2, 4], [1, 2, 3, 4]), [3, -1])


class Test0501to1000(unittest.TestCase):
    def test_502(self):
        with self.subTest('Example 1'):
            self.assertEqual(find_maximized_capital(k=2, w=0, profits=[1, 2, 3], capital=[0, 1, 1]), 4)

        with self.subTest('Example 2'):
            self.assertEqual(find_maximized_capital(k=3, w=0, profits=[1, 2, 3], capital=[0, 1, 2]), 6)

    def test_503(self):
        self.assertEqual(next_greater_elements([1, 2, 1]), [2, -1, 2])
        self.assertEqual(next_greater_elements([1, 2, 3, 4, 3]), [2, 3, 4, -1, 4])
        self.assertEqual(next_greater_elements([5, 4, 3, 2, 1]), [-1, 5, 5, 5, 5])
        self.assertEqual(next_greater_elements([1, 5, 3, 6, 8]), [5, 6, 6, 8, -1])

    def test_506(self):
        with self.subTest('Example 1'):
            self.assertEqual(find_relative_ranks(score=[5, 4, 3, 2, 1]),
                             ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"])

        with self.subTest('Example 2'):
            self.assertEqual(find_relative_ranks(score=[10, 3, 8, 9, 4]),
                             ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"])

    def test_520(self):
        with self.subTest('Example 1'):
            self.assertTrue(detect_capital_use(word='USA'))

        with self.subTest('Example 2'):
            self.assertFalse(detect_capital_use(word='FlaG'))

        with self.subTest('Example 3'):
            self.assertTrue(detect_capital_use(word='leetcode'))

        with self.subTest('Example 4'):
            self.assertTrue(detect_capital_use(word='Google'))

        with self.subTest('Example 2'):
            self.assertFalse(detect_capital_use(word='gooGle'))

    def test_540(self):
        with self.subTest('Example 1'):
            self.assertEqual(single_non_duplicate(nums=[1, 1, 2, 3, 3, 4, 4, 8, 8]), 2)

        with self.subTest('Example 2'):
            self.assertEqual(single_non_duplicate(nums=[3, 3, 7, 7, 10, 11, 11]), 10)

    def test_556(self):
        self.assertEqual(next_greater_element_iii(234157641), 234161457)
        self.assertEqual(next_greater_element_iii(12), 21)
        self.assertEqual(next_greater_element_iii(21), -1)
        self.assertEqual(next_greater_element_iii(364), 436)
        self.assertEqual(next_greater_element_iii(346), 364)
        self.assertEqual(next_greater_element_iii(1488), 1848)
        self.assertEqual(next_greater_element_iii(1312), 1321)
        self.assertEqual(next_greater_element_iii(2147483486), -1)

    def test_559(self):
        with self.subTest('Example 1'):
            self.assertEqual(max_depth(
                Node(1, [
                    Node(3, [Node(5), Node(6)]),
                    Node(2),
                    Node(4)]
                     )
            ), 3)

        with self.subTest('Example 2'):
            self.assertEqual(max_depth(
                Node(1,
                     [
                         Node(2),
                         Node(3,
                              [
                                  Node(6),
                                  Node(7, [Node(11, [Node(14)])])
                              ]),
                         Node(4,
                              [
                                  Node(8, [Node(12)]),
                              ]),
                         Node(5,
                              [
                                  Node(9, [Node(13)]),
                                  Node(10)
                              ]),
                     ]
                     )
            ), 5)

    def test_567(self):
        with self.subTest('Example 1'):
            self.assertEqual(check_inclusion(s1="ab", s2="eidbaooo"), True)

        with self.subTest('Example 2'):
            self.assertEqual(check_inclusion(s1="ab", s2="eidboaoo"), False)

    def test_575(self):
        with self.subTest('Example 1'):
            self.assertEqual(distribute_candies(candyType=[1, 1, 2, 2, 3, 3]), 3)

        with self.subTest('Example 2'):
            self.assertEqual(distribute_candies(candyType=[1, 1, 2, 3]), 2)

        with self.subTest('Example 3'):
            self.assertEqual(distribute_candies(candyType=[6, 6, 6, 6]), 1)

    def test_590(self):
        with self.subTest('Example 1'):
            root_ = Node(val=1, children=[Node(val=3, children=[Node(5), Node(6)]), Node(val=2), Node(val=4)])
            self.assertEqual(postorder(root_), [5, 6, 3, 2, 4, 1])

    def test_637(self):
        with self.subTest('Example 1'):
            result = average_of_levels(
                root=TreeNode(3,
                              TreeNode(9),
                              TreeNode(20,
                                       TreeNode(15),
                                       TreeNode(7)))
            )
            expected_result = [3.0, 14.5, 11.0]
            for i, avr_val in enumerate(result):
                self.assertAlmostEqual(avr_val, expected_result[i])

        with self.subTest('Example 2'):
            result = average_of_levels(
                root=TreeNode(3,
                              TreeNode(9,
                                       TreeNode(15),
                                       TreeNode(7)),
                              TreeNode(20))
            )
            expected_result = [3.0, 14.5, 11.0]
            for i, avr_val in enumerate(result):
                self.assertAlmostEqual(avr_val, expected_result[i])

    def test_645(self):
        with self.subTest('Example 1'):
            self.assertEqual(find_error_nums(nums=[1, 2, 2, 4]), [2, 3])

        with self.subTest('Example 2'):
            self.assertEqual(find_error_nums(nums=[1, 1]), [1, 2])

        with self.subTest('Example 3'):
            self.assertEqual(find_error_nums(nums=[2, 2]), [2, 1])

        with self.subTest('Example 4'):
            self.assertEqual(find_error_nums(nums=[3, 2, 2]), [2, 1])

        with self.subTest('Example 5'):
            self.assertEqual(find_error_nums(nums=[1, 3, 3]), [3, 2])

        with self.subTest('Example 6'):
            self.assertEqual(find_error_nums(nums=[2, 3, 2]), [2, 1])

    def test_680(self):
        with self.subTest('Example 1'):
            self.assertTrue(valid_palindrome('aba'))

        with self.subTest('Example 2'):
            self.assertTrue(valid_palindrome('abca'))

        with self.subTest('Example 3'):
            self.assertFalse(valid_palindrome('abc'))

    def test_692(self):
        with self.subTest('Example 1'):
            self.assertCountEqual(top_k_frequent(words=["i", "love", "leetcode", "i", "love", "coding"], k=2),
                                  ["i", "love"])

        with self.subTest('Example 2'):
            self.assertCountEqual(
                top_k_frequent(words=["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k=4),
                ["the", "is", "sunny", "day"])

    def test_703(self):
        with self.subTest('Example 1'):
            kth_largest = KthLargest(3, [4, 5, 8, 2])
            self.assertEqual(kth_largest.add(3), 4)
            self.assertEqual(kth_largest.add(5), 5)
            self.assertEqual(kth_largest.add(10), 5)
            self.assertEqual(kth_largest.add(9), 8)
            self.assertEqual(kth_largest.add(4), 8)

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

    def test_709(self):
        self.assertEqual(to_lower_case("Hello"), "hello")
        self.assertEqual(to_lower_case("here"), "here")
        self.assertEqual(to_lower_case("LOVELY"), "lovely")

    def test_713(self):
        self.assertEqual(num_subarray_product_less_than_k(nums=[10, 5, 2, 6], k=100), 8)
        self.assertEqual(num_subarray_product_less_than_k(nums=[1, 2, 3], k=0), 0)

    def test_724(self):
        with self.subTest('Example 1'):
            self.assertEqual(pivot_index(nums=[1, 7, 3, 6, 5, 6]), 3)

        with self.subTest('Example 2'):
            self.assertEqual(pivot_index(nums=[1, 2, 3]), -1)

        with self.subTest('Example 3'):
            self.assertEqual(pivot_index(nums=[2, 1, -1]), 0)

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

    def test_733(self):
        with self.subTest('Example 1'):
            self.assertEqual(flood_fill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2),
                             [[2, 2, 2], [2, 2, 0], [2, 0, 1]])

        with self.subTest('Example 2'):
            self.assertEqual(flood_fill(image=[[0, 0, 0], [0, 0, 0]], sr=0, sc=0, color=0),
                             [[0, 0, 0], [0, 0, 0]])

    def test_739(self):
        self.assertEqual(daily_temperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0])
        self.assertEqual(daily_temperatures(temperatures=[30, 40, 50, 60]), [1, 1, 1, 0])
        self.assertEqual(daily_temperatures(temperatures=[30, 60, 90]), [1, 1, 0])
        self.assertEqual(daily_temperatures(temperatures=[89, 62, 70, 58, 47, 47, 46, 76, 100, 70]),
                         [8, 1, 5, 4, 3, 2, 1, 1, 0, 0])

    def test_771(self):
        with self.subTest('Example 1'):
            self.assertEqual(num_jewels_in_stones(jewels="aA", stones="aAAbbbb"), 3)

        with self.subTest('Example 2'):
            self.assertEqual(num_jewels_in_stones(jewels="z", stones="ZZ"), 0)

    def test_783(self):
        with self.subTest('Example 1'):
            self.assertEqual(min_diff_in_bst(root=TreeNode(4, TreeNode(2, 1, 3), TreeNode(6))), 1)

        with self.subTest('Example 2'):
            self.assertEqual(min_diff_in_bst(root=TreeNode(1, TreeNode(0), TreeNode(48, 12, 49))), 1)

        with self.subTest('Example 3'):
            self.assertEqual(min_diff_in_bst(root=TreeNode(90,
                                                           TreeNode(69,
                                                                    TreeNode(49, None, 52),
                                                                    TreeNode(89)
                                                                    ),
                                                           None)
                                             ), 1)

    def test_797(self):
        self.assertCountEqual(all_paths_source_target([[1, 2], [3], [3], []]),
                              [[0, 1, 3], [0, 2, 3]])
        self.assertCountEqual(all_paths_source_target([[4, 3, 1], [3, 2, 4], [3], [4], []]),
                              [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]])

    def test_804(self):
        self.assertEqual(unique_morse_representations(["gin", "zen", "gig", "msg"]), 2)
        self.assertEqual(unique_morse_representations(["a"]), 1)

    def test_860(self):
        self.assertTrue(lemonade_change([5, 5, 5, 10, 20]))
        self.assertFalse(lemonade_change([5, 5, 10, 10, 20]))

    def test_875(self):
        with self.subTest('Example 1'):
            self.assertEqual(min_eating_speed(piles=[3, 6, 7, 11], h=8), 4)

        with self.subTest('Example 2'):
            self.assertEqual(min_eating_speed(piles=[30, 11, 23, 4, 20], h=5), 30)

        with self.subTest('Example 3'):
            self.assertEqual(min_eating_speed(piles=[30, 11, 23, 4, 20], h=6), 23)

    def test_876(self):
        self.assertEqual(linked_list_to_list(middle_node(list_to_linked_list([1, 2, 3, 4, 5]))), [3, 4, 5])
        self.assertEqual(linked_list_to_list(middle_node(list_to_linked_list([1, 2, 3, 4, 5, 6]))), [4, 5, 6])

    def test_896(self):
        self.assertTrue(is_monotonic([1, 2, 2, 3]))
        self.assertTrue(is_monotonic([6, 5, 4, 4]))
        self.assertFalse(is_monotonic([1, 3, 2]))

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

    def test_910(self):
        self.assertEqual(smallest_range_ii(nums=[1], k=0), 0)
        self.assertEqual(smallest_range_ii(nums=[0, 10], k=2), 6)
        self.assertEqual(smallest_range_ii(nums=[1, 3, 6], k=3), 3)

    def test_912(self):
        with self.subTest('Example 1'):
            self.assertEqual(sort_array(nums=[5, 2, 3, 1]), [1, 2, 3, 5])

        with self.subTest('Example 2'):
            self.assertEqual(sort_array(nums=[5, 1, 1, 2, 0, 0]), [0, 0, 1, 1, 2, 5])

        with self.subTest('Example 3'):
            self.assertEqual(sort_array(nums=[3, -1]), [-1, 3])

        with self.subTest('Example 4'):
            self.assertEqual(sort_array(nums=[-2, 3, -5]), [-5, -2, 3])

    def test_933(self):
        with self.subTest('Example 1'):
            recent_counter = RecentCounter()
            self.assertEqual(recent_counter.ping(1), 1)     # requests = [1], range is [-2999,1], return 1
            self.assertEqual(recent_counter.ping(100), 2)   # requests = [1, 100], range is [-2900,100], return 2
            self.assertEqual(recent_counter.ping(3001), 3)  # requests = [1, 100, 3001], range is [1,3001], return 3
            self.assertEqual(recent_counter.ping(3002),
                             3)  # requests = [1, 100, 3001, 3002], range is [2,3002], return 3

    def test_944(self):
        with self.subTest('Example 1'):
            self.assertEqual(min_deletion_size(strs=["cba", "daf", "ghi"]), 1)

        with self.subTest('Example 2'):
            self.assertEqual(min_deletion_size(strs=["a", "b"]), 0)

        with self.subTest('Example 3'):
            self.assertEqual(min_deletion_size(strs=["zyx", "wvu", "tsr"]), 3)

        with self.subTest('Example 4'):
            self.assertEqual(min_deletion_size(strs=["abc", "bce", "cae"]), 1)

    def test_953(self):
        self.assertTrue(is_alien_sorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"))
        self.assertFalse(is_alien_sorted(words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz"))
        self.assertFalse(is_alien_sorted(words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz"))

    def test_958(self):
        with self.subTest('Example 1'):
            self.assertTrue(is_complete_tree(
                root=TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
            ))

        with self.subTest('Example 2'):
            self.assertFalse(is_complete_tree(
                root=TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(7)))
            ))

    def test_965(self):
        with self.subTest('Example 1'):
            self.assertTrue(is_unival_tree(
                root=TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(1, None, TreeNode(1)))
            ))

        with self.subTest('Example 2'):
            self.assertFalse(is_unival_tree(
                root=TreeNode(2, TreeNode(2, TreeNode(5), TreeNode(2)), TreeNode(2))
            ))

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


class Test1001to1500(unittest.TestCase):
    def test_1011(self):
        with self.subTest('Example 1'):
            self.assertEqual(ship_within_days(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days=5), 15)

        with self.subTest('Example 2'):
            self.assertEqual(ship_within_days(weights=[3, 2, 2, 4, 1, 4], days=3), 6)

        with self.subTest('Example 3'):
            self.assertEqual(ship_within_days(weights=[1, 2, 3, 1, 1], days=4), 3)

    def test_1022(self):
        with self.subTest('Example 1'):
            self.assertEqual(sum_root_to_leaf(
                root=TreeNode(1,
                              TreeNode(0,
                                       TreeNode(0), TreeNode(1)),
                              TreeNode(1,
                                       TreeNode(0), TreeNode(1))
                              )
            ), 22)

        with self.subTest('Example 2'):
            self.assertEqual(sum_root_to_leaf(root=TreeNode(0)), 0)

        with self.subTest('Example 3'):
            self.assertEqual(sum_root_to_leaf(root=TreeNode(1, TreeNode(1))), 3)

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

    def test_1160(self):
        with self.subTest('Example 1'):
            self.assertEqual(count_characters(words=["cat", "bt", "hat", "tree"], chars="atach"), 6)

        with self.subTest('Example 2'):
            self.assertEqual(count_characters(words=["hello", "world", "leetcode"], chars="welldonehoneyr"), 10)

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

    def test_1266(self):
        with self.subTest('Example 1'):
            self.assertEqual(min_time_to_visit_all_points([[1, 1], [3, 4], [-1, 0]]), 7)

        with self.subTest('Example 2'):
            self.assertEqual(min_time_to_visit_all_points([[3, 2], [-2, 2]]), 5)

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

    def test_1302(self):
        with self.subTest('Example 1'):
            self.assertEqual(deepest_leaves_sum(
                root=TreeNode(1,
                              TreeNode(2,
                                       TreeNode(4,
                                                TreeNode(7)),
                                       TreeNode(5)),
                              TreeNode(3,
                                       None,
                                       TreeNode(6,
                                                None,
                                                TreeNode(8))))
            ), 15)

    def test_1309(self):
        self.assertEqual(freq_alphabets("10#11#12"), "jkab")
        self.assertEqual(freq_alphabets("1326#"), "acz")

    def test_1323(self):
        with self.subTest('Example 1'):
            self.assertEqual(maximum_69_number(9669), 9969)

        with self.subTest('Example 2'):
            self.assertEqual(maximum_69_number(9996), 9999)

        with self.subTest('Example 3'):
            self.assertEqual(maximum_69_number(9999), 9999)

    def test_1337(self):
        with self.subTest('Example 1'):
            self.assertEqual(
                k_weakest_rows(
                    [[1, 1, 0, 0, 0],
                     [1, 1, 1, 1, 0],
                     [1, 0, 0, 0, 0],
                     [1, 1, 0, 0, 0],
                     [1, 1, 1, 1, 1]], k=3),
                [2, 0, 3]
            )

        with self.subTest('Example 2'):
            self.assertEqual(
                k_weakest_rows(
                    [[1, 0, 0, 0],
                     [1, 1, 1, 1],
                     [1, 0, 0, 0],
                     [1, 0, 0, 0]], k=2),
                [0, 2]
            )

    def test_1345(self):
        with self.subTest('Example 1'):
            self.assertEqual(min_jumps(arr=[100, -23, -23, 404, 100, 23, 23, 23, 3, 404]), 3)

        with self.subTest('Example 2'):
            self.assertEqual(min_jumps(arr=[7]), 0)

        with self.subTest('Example 3'):
            self.assertEqual(min_jumps(arr=[7, 6, 9, 6, 9, 6, 9, 7]), 1)

    def test_1356(self):
        self.assertEqual(sort_by_bits([0, 1, 2, 3, 4, 5, 6, 7, 8]), [0, 1, 2, 4, 8, 3, 5, 6, 7])
        self.assertEqual(sort_by_bits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]),
                         [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024])

    def test_1437(self):
        self.assertEqual(k_length_apart([1, 0, 0, 0, 1, 0, 0, 1], 2), True)
        self.assertEqual(k_length_apart([1, 0, 0, 1, 0, 1], 2), False)
        self.assertEqual(k_length_apart([1, 0, 0, 0], 1), True)

    def test_1464(self):
        with self.subTest('Example 1'):
            self.assertEqual(max_product(nums=[3, 4, 5, 2]), 12)

        with self.subTest('Example 2'):
            self.assertEqual(max_product(nums=[1, 5, 4, 5]), 16)

        with self.subTest('Example 3'):
            self.assertEqual(max_product(nums=[3, 7]), 12)

    def test_1470(self):
        with self.subTest('Example 1'):
            self.assertEqual(shuffle(nums=[2, 5, 1, 3, 4, 7], n=3), [2, 3, 5, 4, 1, 7])

        with self.subTest('Example 2'):
            self.assertEqual(shuffle(nums=[1, 2, 3, 4, 4, 3, 2, 1], n=4), [1, 4, 2, 3, 3, 2, 4, 1])

        with self.subTest('Example 3'):
            self.assertEqual(shuffle(nums=[1, 1, 2, 2], n=2), [1, 2, 1, 2])

    def test_1480(self):
        with self.subTest('Example 1'):
            self.assertEqual(running_sum(nums=[1, 2, 3, 4]), [1, 3, 6, 10])

        with self.subTest('Example 2'):
            self.assertEqual(running_sum(nums=[1, 1, 1, 1, 1]), [1, 2, 3, 4, 5])

        with self.subTest('Example 3'):
            self.assertEqual(running_sum(nums=[3, 1, 2, 10, 1]), [3, 4, 6, 16, 17])

    def test_1491(self):
        self.assertEqual(average([4000, 3000, 1000, 2000]), 2500.)
        self.assertEqual(average([1000, 2000, 3000]), 2000.)


class Test1501to2000(unittest.TestCase):
    def test_1502(self):
        solution = Solution1501to2000()
        self.assertEqual(solution.can_make_arithmetic_progression([3, 5, 1]), True)
        self.assertEqual(solution.can_make_arithmetic_progression([1, 2, 4]), False)

    def test_1523(self):
        solution = Solution1501to2000()
        self.assertEqual(solution.count_odds(3, 7), 3)
        self.assertEqual(solution.count_odds(8, 10), 1)

    def test_1539(self):
        solution = Solution1501to2000()
        with self.subTest('Example 1'):
            self.assertEqual(solution.find_kth_positive(arr=[2, 3, 4, 7, 11], k=5), 9)

        with self.subTest('Example 2'):
            self.assertEqual(solution.find_kth_positive(arr=[1, 2, 3, 4], k=2), 6)

        with self.subTest('Example 2'):
            self.assertEqual(solution.find_kth_positive(
                arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 32, 33, 35,
                     37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61,
                     62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 83, 84, 85, 86, 87,
                     88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109,
                     110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129,
                     130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 150,
                     152, 153, 154, 155, 156, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172,
                     173, 174, 175, 177, 180, 181, 182, 183, 184, 185, 186, 188, 189, 190, 191, 192, 193, 194, 195, 196,
                     197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 209, 210, 211, 212, 213, 214, 215, 216, 217,
                     218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237,
                     238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 256, 257, 258,
                     262, 263, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282,
                     283, 284, 285, 286, 288, 289, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304,
                     305, 306, 307, 308, 309, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325,
                     326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 343, 344, 345, 346,
                     347, 349, 350, 351, 352, 353, 354, 355, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368,
                     369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388,
                     389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408,
                     409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428,
                     429, 430, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449,
                     450, 451, 452, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470,
                     472, 473, 474, 475, 476, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492,
                     493, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 508, 509, 510, 511, 512, 513, 514,
                     515, 516, 517, 518, 520, 521, 522, 523, 524, 525, 526, 528, 529, 530, 531, 532, 533, 534, 535, 536,
                     537, 538, 539, 540, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557,
                     558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577,
                     578, 579, 580, 581, 582, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598,
                     599, 600, 602, 603, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620,
                     621, 622, 623, 624, 625, 626, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641,
                     642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 654, 655, 656, 657, 658, 659, 660, 661, 662,
                     663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 679, 680, 681, 682, 683,
                     685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704,
                     705, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 720, 721, 722, 723, 724, 725, 726,
                     728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 740, 741, 742, 743, 744, 745, 746, 747, 748,
                     749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 769,
                     770, 771, 772, 773, 775, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791,
                     792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 806, 807, 808, 809, 810, 811, 812,
                     813, 814, 815, 816, 817, 818, 819, 820, 822, 823, 824, 826, 827, 828, 829, 830, 832, 833, 835, 836,
                     837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856,
                     857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876,
                     877, 878, 879, 880, 881, 882, 883, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 898, 899,
                     900, 901, 902, 904, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921,
                     922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 936, 937, 938, 939, 940, 941, 942,
                     943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 961, 962, 964,
                     965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 985,
                     986, 987, 988, 989, 990, 992, 993, 994, 995, 996, 997, 998, 999], k=8), 34)

    def test_1572(self):
        solution = Solution1501to2000()
        self.assertEqual(solution.diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 25)
        self.assertEqual(solution.diagonal_sum(
            [[1, 1, 1, 1],
             [1, 1, 1, 1],
             [1, 1, 1, 1],
             [1, 1, 1, 1]]), 8)
        self.assertEqual(solution.diagonal_sum([[5]]), 5)

    def test_1588(self):
        solution = Solution1501to2000()
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
        solution = Solution1501to2000()
        self.assertEqual(
            solution.check_arithmetic_subarrays(nums=[4, 6, 5, 9, 3, 7], l=[0, 0, 2], r=[2, 3, 5]
                                                ), [True, False, True])
        self.assertEqual(
            solution.check_arithmetic_subarrays(nums=[-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10],
                                                l=[0, 1, 6, 4, 8, 7],
                                                r=[4, 4, 9, 7, 9, 10]
                                                ), [False, True, False, False, True, True])

    def test_1672(self):
        solution = Solution1501to2000()
        self.assertEqual(solution.maximum_wealth([[1, 2, 3], [3, 2, 1]]), 6)
        self.assertEqual(solution.maximum_wealth([[1, 5], [7, 3], [3, 5]]), 10)
        self.assertEqual(solution.maximum_wealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]), 17)

    def test_1675(self):
        solution = Solution1501to2000()
        with self.subTest('Example 1'):
            self.assertEqual(solution.minimum_deviation(nums=[1, 2, 3, 4]), 1)

        with self.subTest('Example 2'):
            self.assertEqual(solution.minimum_deviation(nums=[4, 1, 5, 20, 3]), 3)

        with self.subTest('Example 3'):
            self.assertEqual(solution.minimum_deviation(nums=[2, 10, 8]), 3)

        with self.subTest('Example 4'):
            self.assertEqual(solution.minimum_deviation(nums=[3, 5]), 1)

    def test_1678(self):
        solution = Solution1501to2000()
        self.assertEqual(solution.interpret("G()(al)"), "Goal")
        self.assertEqual(solution.interpret("G()()()()(al)"), "Gooooal")
        self.assertEqual(solution.interpret("(al)G(al)()()G"), "alGalooG")

    def test_1700(self):
        solution = Solution1501to2000()
        self.assertEqual(solution.count_students([1, 1, 0, 0], [0, 1, 0, 1]), 0)
        self.assertEqual(solution.count_students([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]), 3)

    def test_1732(self):
        solution = Solution1501to2000()
        self.assertEqual(solution.largest_altitude([-5, 1, 5, 0, -7]), 1)
        self.assertEqual(solution.largest_altitude([-4, -3, -2, -1, 4, 3, 2]), 0)

    def test_1768(self):
        solution = Solution1501to2000()
        self.assertEqual(solution.merge_alternately(word1="abc", word2="pqr"), "apbqcr")
        self.assertEqual(solution.merge_alternately(word1="ab", word2="pqrs"), "apbqrs")
        self.assertEqual(solution.merge_alternately(word1="abcd", word2="pq"), "apbqcd")

    def test_1779(self):
        solution = Solution1501to2000()
        self.assertEqual(solution.nearest_valid_point(3, 4, [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]), 2)
        self.assertEqual(solution.nearest_valid_point(3, 4, [[3, 4]]), 0)
        self.assertEqual(solution.nearest_valid_point(3, 4, [[2, 3]]), -1)

    def test_1790(self):
        solution = Solution1501to2000()
        self.assertEqual(solution.are_almost_equal("bank", "kanb"), True)
        self.assertEqual(solution.are_almost_equal("attack", "defend"), False)
        self.assertEqual(solution.are_almost_equal("kelb", "kelb"), True)

    def test_1816(self):
        solution = Solution1501to2000()
        with self.subTest('Example 1'):
            self.assertEqual(solution.truncate_sentence(s="Hello how are you Contestant", k=4), "Hello how are you")

        with self.subTest('Example 1'):
            self.assertEqual(solution.truncate_sentence(s="What is the solution to this problem", k=4),
                             "What is the solution")

    def test_1822(self):
        solution = Solution1501to2000()
        self.assertEqual(solution.array_sign([-1, -2, -3, -4, 3, 2, 1]), 1)
        self.assertEqual(solution.array_sign([1, 5, 0, 2, -3]), 0)
        self.assertEqual(solution.array_sign([-1, 1, -1, 1, -1]), -1)

    def test_1828(self):
        solution = Solution1501to2000()
        self.assertEqual(solution.count_points([[1, 3], [3, 3], [5, 3], [2, 2]], [[2, 3, 1], [4, 3, 1], [1, 1, 2]]),
                         [3, 2, 2])
        self.assertEqual(
            solution.count_points([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],
                                  [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]]),
            [2, 3, 2, 4])

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

    def test_1886(self):
        solution = Solution1501to2000()
        self.assertTrue(
            solution.find_rotation(mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]], target=[[1, 1, 1], [0, 1, 0], [0, 0, 0]]))
        self.assertTrue(solution.find_rotation(mat=[[0, 1], [1, 0]], target=[[1, 0], [0, 1]]))
        self.assertFalse(solution.find_rotation(mat=[[0, 1], [1, 1]], target=[[1, 0], [0, 1]]))
        self.assertTrue(
            solution.find_rotation(mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]], target=[[1, 0, 0], [1, 1, 0], [1, 0, 0]]))

    def test_1925(self):
        solution = Solution1501to2000()
        self.assertEqual(solution.count_triples(5), 2)
        self.assertEqual(solution.count_triples(10), 4)

    def test_1971(self):
        solution = Solution1501to2000()
        with self.subTest('Example 1'):
            self.assertTrue(solution.valid_path(n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2))

        with self.subTest('Example 2'):
            self.assertFalse(
                solution.valid_path(n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5))

        with self.subTest('Example 3'):
            self.assertTrue(
                solution.valid_path(n=1, edges=[], source=0, destination=0))


class Test2001to2500(unittest.TestCase):
    def test_2053(self):
        solution = Solution2001to2500()
        self.assertEqual(solution.kth_distinct(["d", "b", "c", "b", "c", "a"], 2), "a")
        self.assertEqual(solution.kth_distinct(["aaa", "aa", "a"], 1), "aaa")
        self.assertEqual(solution.kth_distinct(["a", "b", "a"], 3), "")

    def test_2073(self):
        solution = Solution2001to2500()
        self.assertEqual(solution.time_required_to_buy([2, 3, 2], 2), 6)
        self.assertEqual(solution.time_required_to_buy([5, 1, 1, 1], 0), 8)
        self.assertEqual(solution.time_required_to_buy([84, 49, 5, 24, 70, 77, 87, 8], 3), 154)

    def test_2187(self):
        solution = Solution2001to2500()
        with self.subTest('Example 1'):
            self.assertEqual(solution.minimum_time(time=[1, 2, 3], totalTrips=5), 3)

        with self.subTest('Example 2'):
            self.assertEqual(solution.minimum_time(time=[2], totalTrips=1), 2)

    def test_2221(self):
        solution = Solution2001to2500()
        self.assertEqual(solution.triangular_sum([1, 2, 3, 4, 5]), 8)
        self.assertEqual(solution.triangular_sum([5]), 5)

    def test_2244(self):
        solution = Solution2001to2500()
        with self.subTest('Example 1'):
            self.assertEqual(solution.minimum_rounds(tasks=[2, 2, 3, 3, 2, 4, 4, 4, 4, 4]), 4)

        with self.subTest('Example 2'):
            self.assertEqual(solution.minimum_rounds(tasks=[2, 3, 3]), -1)

    def test_2306(self):
        solution = Solution2001to2500()
        with self.subTest('Example 1'):
            self.assertEqual(solution.distinct_names(ideas=["coffee", "donuts", "time", "toffee"]), 6)

        with self.subTest('Example 2'):
            self.assertEqual(solution.distinct_names(ideas=["lack", "back"]), 0)

        with self.subTest('Example 3'):
            self.assertEqual(solution.distinct_names(ideas=["bzklqtbdr", "kaqvdlp", "r", "dk"]), 12)

    def test_2325(self):
        sol = Solution2001to2500()
        with self.subTest('Example 1'):
            self.assertEqual(sol.decode_message(key = "the quick brown fox jumps over the lazy dog",
                                                message = "vkbs bs t suepuv"),
                             "this is a secret")

        with self.subTest('Example 2'):
            self.assertEqual(sol.decode_message(key = "eljuxhpwnyrdgtqkviszcfmabo",
                                                message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"),
                             "the five boxing wizards jump quickly")

    def test_2444(self):
        solution = Solution2001to2500()

        with self.subTest('Example 1'):
            self.assertEqual(solution.count_subarrays(nums=[1, 3, 5, 2, 7, 5], minK=1, maxK=5), 2)

        with self.subTest('Example 2'):
            self.assertEqual(solution.count_subarrays(nums=[1, 1, 1, 1], minK=1, maxK=1), 10)

    def test_2469(self):
        solution = Solution2001to2500()
        with self.subTest('Example 1'):
            self.assertAlmostEqual(solution.convert_temperature(36.50)[0], 309.65000, delta=10e-5)
            self.assertAlmostEqual(solution.convert_temperature(36.50)[1], 97.70000, delta=10e-5)

        with self.subTest('Example 2'):
            self.assertAlmostEqual(solution.convert_temperature(122.11)[0], 395.26000, delta=10e-5)
            self.assertAlmostEqual(solution.convert_temperature(122.11)[1], 251.79800, delta=10e-5)

    def test_2477(self):
        with self.subTest('Example 1'):
            solution = Solution2001to2500()
            self.assertEqual(solution.minimum_fuel_cost(roads=[[0, 1], [0, 2], [0, 3]], seats=5), 3)

        with self.subTest('Example 2'):
            solution = Solution2001to2500()
            self.assertEqual(
                solution.minimum_fuel_cost(roads=[[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], seats=2), 7)

        with self.subTest('Example 3'):
            solution = Solution2001to2500()
            self.assertEqual(solution.minimum_fuel_cost(roads=[], seats=1), 0)


class Test2501to3000(unittest.TestCase):
    def test_2558(self):
        solution = Solution2501to3000()

        with self.subTest('Example 1'):
            self.assertEqual(solution.pick_gifts(gifts=[25, 64, 9, 4, 100], k=4), 29)

        with self.subTest('Example 2'):
            self.assertEqual(solution.pick_gifts(gifts=[1, 1, 1, 1], k=4), 4)

    def test_2574(self):
        sol = Solution2501to3000()
        with self.subTest('Example 1'):
            self.assertEqual(sol.left_rigth_difference(nums=[10, 4, 8, 3]), [15, 1, 11, 22])

        with self.subTest('Example 2'):
            self.assertEqual(sol.left_rigth_difference(nums=[1]), [0])

    def test_2586(self):
        sol = Solution2501to3000()
        with self.subTest('Example 1'):
            self.assertEqual(sol.vowel_strings(words=["are", "amy", "u"], left=0, right=2), 2)

        with self.subTest('Example 2'):
            self.assertEqual(sol.vowel_strings(words=["hey", "aeo", "mu", "ooo", "artro"], left=1, right=4), 3)


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
