from common import *


# 976. Largest Perimeter Triangle
def largest_perimeter(nums: List[int]) -> int:
    nums.sort()
    for i in range(len(nums)-3, -1, -1):
        if nums[i] + nums[i+1] > nums[i+2]:
            return nums[i] + nums[i+1] + nums[i+2]
    return 0


# 709. To Lower Case
def to_lower_case(s: str) -> str:
    return s.lower()


# 953. Verifying an Alien Dictionary
def is_alien_sorted(words: List[str], order: str) -> bool:
    for i in range(len(words) - 1):
        if not compare_two_words(words[i], words[i+1], order=order):
            return False
    return True


def compare_two_words(word1: str, word2: str, order: str) -> bool:
    for i, c in enumerate(word1):
        if i >= len(word2):
            return False
        if c != word2[i]:
            return order.index(c) < order.index(word2[i])
    return True


# 797. All Paths From Source to Target
def all_paths_source_target(graph: List[List[int]]) -> List[List[int]]:
    target = len(graph) - 1
    paths = []

    points_to_visit = graph[0]
    stack = []
    for point in points_to_visit:
        if point == target:
            paths.append([0, point])
        else:
            stack.append([[0, point], graph[point]])

    while len(stack) > 0:
        possible_path = stack.pop(0)
        previous_points, next_points = possible_path

        for point in next_points:
            if point == target:
                paths.append(previous_points + [point])
            else:
                stack.append([previous_points + [point], graph[point]])

    return paths


# 876. Middle of the Linked List
def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    arr = [head]
    while arr[-1].next:
        arr.append(arr[-1].next)
    return arr[len(arr) // 2]


# 896. Monotonic Array
def is_monotonic(nums: List[int]) -> bool:
    sign = (nums[-1] - nums[0]) > 0
    for i, num in enumerate(nums):
        if i < len(nums) - 1 and num != nums[i+1] and ((nums[i+1] - num > 0) is not sign):
            return False
    return True


# 989. Add to Array-Form of Integer
def add_to_array_form(num: List[int], k: int) -> List[int]:
    stack, digit = divmod(num[-1] + k, 10)
    result = [digit]
    order = 1

    while stack > 0 or order < len(num):
        if order < len(num):
            stack, digit = divmod(num[-1-order] + stack, 10)
            result.append(digit)
            order += 1
        else:
            stack, digit = divmod(stack, 10)
            result.append(digit)
            order += 1

    result.reverse()

    return result


# 739. Daily Temperatures
def daily_temperatures_slow(temperatures: List[int]) -> List[int]:
    result = []

    for day, temperature in enumerate(temperatures):
        if day < len(temperatures):
            temp_set = set(temperatures[day+1:])
            min_days = 1000
            day_found = False

            if len(temp_set) > 0:
                for temp in range(temperature + 1, max(temp_set)+1):
                    if temp in temp_set:
                        day_found = True
                        temp_index = temperatures[day+1:].index(temp) + 1
                        if temp_index == 1:
                            min_days = 1
                            break
                        else:
                            min_days = min(min_days, temp_index)

                if day_found:
                    result.append(min_days)
                else:
                    result.append(0)
            else:
                result.append(0)

    return result


def daily_temperatures(temperatures: List[int]) -> List[int]:
    ans = [0] * len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            cur = stack.pop()
            ans[cur] = i - cur
        stack.append(i)

    return ans


# 973. K Closest Points to Origin
def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    result = []
    distances = [abs(complex(*point)) for point in points]
    max_dist = sorted(distances)[k-1]
    for point in points:
        if abs(complex(*point)) <= max_dist:
            result.append(point)

    return result


# 503. Next Greater Element II
def next_greater_elements_slow(nums: List[int]) -> List[int]:
    result = [-1] * len(nums)

    p2 = len(nums) - 1
    while p2 >= 0:
        p1 = (p2 + 1) % len(nums)
        p2_num = nums[p2]

        while p1 != p2:
            p1_num = nums[p1]
            if p1_num > p2_num:
                result[p2] = p1_num
                break
            else:
                p1 = (p1 + 1) % len(nums)
        p2 -= 1

    return result


def next_greater_elements(nums: List[int]) -> List[int]:
    result = [-1] * len(nums)
    stack = []

    for _ in range(2):
        for n, num in enumerate(nums):
            while stack and num > nums[stack[-1]]:
                result[stack.pop()] = num
            stack.append(n)

    return result


# 556. Next Greater Element III
def next_greater_element_iii(n: int) -> int:
    n_str = str(n)

    p1 = len(n_str) - 2

    while p1 > -1 and int(n_str[p1]) >= int(n_str[p1 + 1]):
        p1 -= 1

    if p1 != -1:
        tail = [int(digit) for digit in n_str[p1+1:]]
        for n in range(len(tail) - 1, -1, -1):
            digit = tail[n]
            if digit > int(n_str[p1]):
                tail[n] = int(n_str[p1])
                result = n_str[:p1] + str(digit) + ''.join([str(k) for k in sorted(tail)])

                if int(result) < 2 ** 31:
                    return int(result)

    return -1


# 713. Subarray Product Less Than K
def num_subarray_product_less_than_k(nums: List[int], k: int) -> int:
    if k <= 1:
        return 0

    prod = 1
    ans = left = 0
    for right, val in enumerate(nums):
        prod *= val
        while prod >= k:
            prod /= nums[left]
            left += 1
        ans += right - left + 1
    return ans


# 910. Smallest Range II
def smallest_range_ii(nums: List[int], k: int) -> int:
    nums.sort()
    first_num, last_num = nums[0], nums[-1]
    result = last_num - first_num
    for i in range(len(nums) - 1):
        a, b = nums[i], nums[i+1]
        possible_result = max(last_num - k, a + k) - min(first_num + k, b - k)
        result = min(result, possible_result)

    return result


# 804. Unique Morse Code Words
def unique_morse_representations(words: List[str]) -> int:
    morse_map = dict(zip(string.ascii_lowercase,
                         [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                          "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--",
                          "--.."]))

    words_in_morse = [''.join([morse_map[char] for char in word]) for word in words]

    return len(set(words_in_morse))


# 860. Lemonade Change
def lemonade_change(bills: List[int]) -> bool:
    current_cash = {5: 0,
                    10: 0,
                    20: 0}

    for bill in bills:
        current_cash[bill] += 1

        if bill == 10:
            current_cash[5] -= 1
        if bill == 20:
            if current_cash[10] > 0:
                current_cash[10] -= 1
                current_cash[5] -= 1
            else:
                current_cash[5] -= 3

        if any([value < 0 for value in current_cash.values()]):
            return False

    return True


# 692. Top K Frequent Words
def top_k_frequent(words: List[str], k: int) -> List[str]:
    words_set = set(words)
    count_dict_by_count = {}

    for word in words_set:
        if words.count(word) in count_dict_by_count:
            count_dict_by_count[words.count(word)].append(word)
        else:
            count_dict_by_count[words.count(word)] = [word]

    result = []
    frequencies = sorted(count_dict_by_count.keys())
    while len(result) < k:
        top_frequency = frequencies.pop()
        result += sorted(count_dict_by_count.pop(top_frequency))

    return result[:k]


# 567. Permutation in String
def check_inclusion(s1: str, s2: str) -> bool:
    s2_substring = [s2[i:i+len(s1)] for i in range(len(s2) - len(s1) + 1)]
    for substring in s2_substring:
        s1_set = set(s1)
        substring_set = set(substring)

        if all([item in substring_set for item in s1_set]):
            s1_dict = {key: s1.count(key) for key in s1_set}
            substring_dict = {key: substring.count(key) for key in substring_set}

            if all([s1_dict[key] == substring_dict[key] for key in s1_dict]):
                return True

    return False


# 904. Fruit Into Baskets
def total_fruit(fruits: List[int]) -> int:
    basket = {}
    start_index = 0
    end_index = 0

    if len(set(fruits)) < 3:
        return len(fruits)

    for end_index, fruit in enumerate(fruits):
        basket[fruit] = basket.get(fruit, 0) + 1

        if len(basket) > 2:
            basket[fruits[start_index]] -= 1

            if basket[fruits[start_index]] == 0:
                del basket[fruits[start_index]]
            start_index += 1

    return end_index - start_index + 1


# 559. Maximum Depth of N-ary Tree
def max_depth(root: Optional[Node]) -> int:
    depth = 0
    if not root:
        return depth

    if root.children and len(root.children) > 0:
        for child in root.children:
            depth = max(max_depth(child), depth)

    return depth + 1


# 783. Minimum Distance Between BST Nodes
def min_diff_in_bst(root: Optional[TreeNode]) -> int:
    min_diff = 10000
    values = []

    children = [root]
    while children:
        root = children.pop(0)
        if root:
            values.append(root.val)
        if root.left:
            children.append(root.left)
        if root.right:
            children.append(root.right)

    values = sorted(values)
    for n, value in enumerate(values[:-1]):
        diff = abs(value - values[n + 1])
        min_diff = min(min_diff, diff)

        if min_diff == 1:
            return min_diff

    return min_diff


# 771. Jewels and Stones
def num_jewels_in_stones(jewels: str, stones: str) -> int:
    from collections import Counter
    counter = Counter(stones)

    result = 0
    for jewel in jewels:
        result += counter[jewel]

    return result


# 540. Single Element in a Sorted Array
def single_non_duplicate(nums: List[int]) -> int:
    counter = Counter(nums)
    for num, amount in counter.items():
        if amount == 1:
            return num


# 502. IPO
def find_maximized_capital(k: int, w: int, profits: List[int], capital: List[int]) -> int:
    n = len(profits)
    projects = list(zip(capital, profits))
    projects.sort()

    queue = []
    ptr = 0

    for _ in range(k):
        while ptr < n and projects[ptr][0] <= w:
            heappush(queue, -projects[ptr][1])
            ptr += 1
        if not queue:
            break
        w += -heappop(queue)
    return w


# 506. Relative Ranks
def find_relative_ranks(score: List[int]) -> List[str]:
    medals = {1: 'Gold Medal',
              2: 'Silver Medal',
              3: 'Bronze Medal'}

    result = [''] * len(score)
    q = []
    for i, score in enumerate(score):
        heappush(q, (-score, i))

    place = 1
    while q:
        item = heappop(q)
        if place in medals:
            result[item[1]] += str(medals[place])
        else:
            result[item[1]] += str(place)
        place += 1

    return result


# 652. Find Duplicate Subtrees
def find_duplicate_subtrees(root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    def traverse(node: TreeNode) -> int:
        if not node:
            return 0

        triplet = (traverse(node.left), node.val, traverse(node.right))

        if triplet not in triplet_to_id:
            triplet_to_id[triplet] = len(triplet_to_id) + 1
        id_ = triplet_to_id[triplet]

        count_dict[id_] += 1
        if count_dict[id_] == 2:
            duplicate_nodes.append(node)

        return id_

    triplet_to_id = {}
    count_dict = defaultdict(int)
    duplicate_nodes = []
    traverse(root)

    return duplicate_nodes


# 912. Sort an Array
def sort_array(nums: List[int]) -> List[int]:
    cnt_plus = [0] * (max(nums) + 1)
    cnt_minus = []
    if min(nums) < 0:
        cnt_minus = [0] * abs(min(nums))

    for item in nums:
        if item >= 0:
            cnt_plus[item] += 1
        else:
            cnt_minus[abs(item) - 1] += 1

    result = ([num - len(cnt_minus) for num, count in enumerate(cnt_minus[::-1]) for i in range(count)] +
              [num for num, count in enumerate(cnt_plus) for i in range(count)])

    return result


# 575. Distribute Candies
def distribute_candies(candyType: List[int]) -> int:
    types = set(candyType)
    return min(len(types), len(candyType) // 2)


# 645. Set Mismatch
def find_error_nums(nums: List[int]) -> List[int]:
    counter = Counter(nums)
    lost_number = set(range(1, len(nums) + 1)) - set(nums)

    for num in counter:
        if counter[num] == 2:
            return [num, lost_number.pop()]

    return []


# 637. Average of Levels in Binary Tree
def average_of_levels(root: Optional[TreeNode]) -> List[float]:
    result = []
    queue = [root]

    while queue:
        level_sum = 0
        level_nodes = len(queue)
        for _ in range(level_nodes):
            node = queue.pop(0)
            if node:
                level_sum += node.val
                queue.append(node.left)
                queue.append(node.right)
            else:
                level_nodes -= 1

        if level_nodes:
            result.append(level_sum / level_nodes)

    return result


# 733. Flood Fill
def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
    prev_color = image[sr][sc]

    image[sr][sc] = color
    queue = [(sr, sc)]
    visited = {(sr, sc)}

    while queue:
        current_position = queue.pop()
        for direction in directions:
            next_position = (current_position[0] + direction[0], current_position[1] + direction[1])

            if (0 <= next_position[0] < len(image) and
                    0 <= next_position[1] < len(image[0]) and
                    next_position not in visited):
                visited.add(next_position)
                if image[next_position[0]][next_position[1]] == prev_color:
                    image[next_position[0]][next_position[1]] = color
                    queue.append(next_position)

    return image


# 520. Detect Capital
def detect_capital_use(word: str) -> bool:
    n_capitals = 0
    not_first_capital = False
    for i, char in enumerate(word):
        is_capital = ord(char) < 97
        n_capitals += is_capital
        if i > 0 and is_capital:
            not_first_capital = True

    all_capitals = len(word) == n_capitals
    no_capitals = n_capitals == 0

    return no_capitals or all_capitals or not not_first_capital


# 944. Delete Columns to Make Sorted
def min_deletion_size(strs: List[str]) -> int:
    result = 0
    for i, _ in enumerate(strs[0]):
        column = [str_[i] for str_ in strs]
        if column != sorted(column):
            result += 1

    return result


# 501. Find Mode in Binary Search Tree
def find_mode(root: Optional[TreeNode]) -> List[int]:
    def get_vals(node: TreeNode) -> None:
        if node:
            counter[node.val] = counter.get(node.val, 0) + 1
            get_vals(node.left)
            get_vals(node.right)

    counter = {}
    get_vals(root)
    result = []
    max_val = max(counter.values())
    for key in counter:
        if counter[key] == max_val:
            result.append(key)

    return result


# 938. Range Sum of BST
def range_sum_bst(root: Optional[TreeNode], low: int, high: int) -> int:
    def dfs(node: Optional[TreeNode]):
        if node:
            if low <= node.val <= high:
                result.add(node.val)

            dfs(node.left)
            dfs(node.right)

    result = set()
    dfs(root)
    return sum(result)


# 700. Search in a Binary Search Tree
def search_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return

    cur = root
    while cur:
        if val < cur.val:
            cur = cur.left
        elif val > cur.val:
            cur = cur.right
        else:
            return cur


# 965. Univalued Binary Tree
def is_unival_tree(root: Optional[TreeNode]) -> bool:
    def dfs(node: TreeNode):
        if node:
            values.add(node.val)
            dfs(node.left)
            dfs(node.right)

    values = set()
    dfs(root)
    return len(values) == 1


# 701. Insert into a Binary Search Tree
def insert_into_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return TreeNode(val)

    cur = root
    parent = root
    while cur:
        parent = cur
        if val < cur.val:
            cur = cur.left
        else:
            cur = cur.right

    if val < parent.val:
        parent.left = TreeNode(val)
    else:
        parent.right = TreeNode(val)

    return root


# 958. Check Completeness of a Binary Tree
def is_complete_tree(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    none_node_found = False
    bfs_queue = [root]

    while bfs_queue:
        node = bfs_queue.pop(0)
        if not node:
            none_node_found = True
        else:
            if none_node_found:
                return False
            else:
                bfs_queue.append(node.left)
                bfs_queue.append(node.right)

    return True


# 617. Merge Two Binary Trees
def merge_trees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    def merge_node(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node1 and not node2:
            return

        result_node = TreeNode()
        if node1:
            result_node.val += node1.val
        if node2:
            result_node.val += node2.val

        if node1 and node2:
            result_node.left = merge_node(node1.left, node2.left)
            result_node.right = merge_node(node1.right, node2.right)

        elif node1:
            result_node.left = node1.left
            result_node.right = node1.right
        else:
            result_node.left = node2.left
            result_node.right = node2.right

        return result_node

    root = merge_node(root1, root2)
    return root


# 680. Valid Palindrome II
def valid_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            option_1 = s[:left] + s[left+1:]
            option_2 = s[:right] + s[right+1:]
            return option_1 == option_1[::-1] or option_2 == option_2[::-1]
        left += 1
        right -= 1

    return True


# 590. N-ary Tree Postorder Traversal
def postorder(root: Node) -> List[int]:
    def traverse(node: Node):
        if not node:
            return

        if node.children:
            for child in node.children:
                traverse(child)
        result.append(node.val)

    result = []
    traverse(root)

    return result


# 589. N-ary Tree Preorder Traversal
def preorder(root: Node) -> List[int]:
    def traverse(node: Node):
        if not node:
            return

        result.append(node.val)
        if node.children:
            for child in node.children:
                traverse(child)

    result = []
    traverse(root)

    return result
