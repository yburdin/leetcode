from common import *


# 1491. Average Salary Excluding the Minimum and Maximum Salary
def average(salary: List[int]) -> float:
    salary.sort()
    salary = salary[1:-1]
    return sum(salary) / len(salary)


# 1281. Subtract the Product and Sum of Digits of an Integer
def subtract_product_and_sum(n: int) -> int:
    product_of_digits = 1
    sum_of_digits = 0

    for digit in str(n):
        product_of_digits *= int(digit)
        sum_of_digits += int(digit)

    return product_of_digits - sum_of_digits


# 1437. Check If All 1's Are at Least Length K Places Away
def k_length_apart(nums: List[int], k: int) -> bool:
    i_loc = 0
    while i_loc < len(nums) - 1:
        if nums[i_loc] == 1:
            j_loc = i_loc
            while j_loc < len(nums) - 1:
                j_loc += 1
                if nums[j_loc] == 1:
                    if j_loc - i_loc - 1 < k:
                        return False
                    else:
                        i_loc = j_loc

                if j_loc == len(nums) - 1:
                    return True
        else:
            i_loc += 1
    return True


# 1232. Check If It Is a Straight Line
def check_straight_line(coordinates: List[List[int]]) -> bool:
    dx = coordinates[-1][0] - coordinates[0][0]
    dy = coordinates[-1][1] - coordinates[0][1]
    dy = 1e-9 if dy == 0 else dy
    k = abs(atan(dx / dy))

    for i in range(1, len(coordinates)):
        point_dx = coordinates[i][0] - coordinates[i - 1][0]
        point_dy = coordinates[i][1] - coordinates[i - 1][1]
        point_dy = 1e-9 if point_dy == 0 else point_dy
        point_k = abs(atan(point_dx / point_dy))

        # print(f'{k=}, {point_k=}, {k - point_k}')

        if abs(k - point_k) > 1e-5:
            return False

    return True


# 1309. Decrypt String from Alphabet to Integer Mapping
def freq_alphabets(s: str) -> str:
    result = []
    s_list = list(s)
    s_list.reverse()

    i = 0
    while i < len(s_list):
        if s_list[i] != '#':
            result.append(chr(int(s_list[i]) + 96))
            i += 1
        else:
            chars = s_list[i+1:i+3]
            chars.reverse()
            result.append(chr(int(''.join(chars)) + 96))
            i += 3

    result.reverse()
    return ''.join(result)


# 1290. Convert Binary Number in a Linked List to Integer
def get_decimal_value(head: ListNode) -> int:
    num = head.val
    while head.next:
        num = num * 2 + head.next.val
        head = head.next
    return num


# 1356. Sort Integers by The Number of 1 Bits
def sort_by_bits(arr: List[int]) -> List[int]:
    bit_dict = {}
    for item in arr:
        bits = bin(item).count('1')
        if bits in bit_dict:
            bit_dict[bits].append(item)
        else:
            bit_dict[bits] = [item]

    result = []
    for key in sorted(bit_dict.keys()):
        result += sorted(bit_dict[key])

    return result


# 1323. Maximum 69 Number
def maximum_69_number(num: int) -> int:
    num_str_list = list(f'{num}')
    if '6' in num_str_list:
        first_6 = num_str_list.index('6')
        num_str_list[first_6] = '9'
        return int(''.join(num_str_list))
    else:
        return num


# 1266. Minimum Time Visiting All Points
def min_time_to_visit_all_points_slow(points: List[List[int]]) -> int:
    current_point = points[0]
    steps = [current_point]

    for point in points[1:]:
        while current_point != point:
            dx = point[0] - current_point[0]
            dy = point[1] - current_point[1]
            step = find_next_step(dx, dy)
            current_point = [current_point[i] + step[i] for i in [0, 1]]

            steps.append(current_point)

    return len(steps) - 1


def find_next_step(dx: int, dy: int, tol=1e-3) -> List[int]:
    result = [0, 0]
    for i, direction in enumerate([dx, dy]):
        if direction > tol:
            result[i] = 1
        elif direction < -tol:
            result[i] = -1

    return result


def min_time_to_visit_all_points(points: List[List[int]]) -> int:
    result = 0

    for i in range(1, len(points)):
        p1 = points[i-1]
        p2 = points[i]

        dist = complex(*p2) - complex(*p1)
        result += max(map(abs, (dist.real, dist.imag)))

    return int(result)


# 1071. Greatest Common Divisor of Strings
def gcd_of_strings(str1: str, str2: str) -> str:
    substring_len = min(len(str1), len(str2))
    while substring_len > 0:
        if len(str1) % substring_len == 0 and len(str2) % substring_len == 0:
            substring = str1[0:substring_len]

            substring_1 = [str1[i:i+substring_len] == substring for i in range(0, len(str1), substring_len)]
            substring_2 = [str2[i:i+substring_len] == substring for i in range(0, len(str2), substring_len)]

            if all(substring_1 + substring_2):
                return substring
            else:
                substring_len -= 1
        else:
            substring_len -= 1

    return ''


# 1470. Shuffle the Array
def shuffle(nums: List[int], n: int) -> List[int]:
    xs = nums[0:n]
    ys = nums[n:]
    result = []

    for i in range(n):
        result.append(xs[i])
        result.append(ys[i])

    return result


# 1295. Find Numbers with Even Number of Digits
def find_numbers(nums: List[int]) -> int:
    is_even_digits = [len(f'{n}') % 2 == 0 for n in nums]
    return sum(is_even_digits)


# 1162. As Far from Land as Possible
def max_distance(grid: List[List[int]]) -> int:
    from itertools import product

    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

    distance = -1
    land_coordinates = []
    visited_matrix = grid.copy()

    for i, j in product(range(len(grid)), range(len(grid))):
        if grid[i][j] == 1:
            land_coordinates.append([i, j])

    if len(land_coordinates) == len(grid) ** 2:
        return -1

    while land_coordinates:
        queue_size = len(land_coordinates)
        for _ in range(queue_size):
            cur_i, cur_j = land_coordinates.pop(0)

            for direction in directions:
                i = cur_i + direction[0]
                j = cur_j + direction[1]

                if 0 <= i < len(grid) and 0 <= j < len(grid) and visited_matrix[i][j] == 0:
                    visited_matrix[i][j] = 1
                    land_coordinates.append([i, j])

        distance += 1

    return distance


# 1129. Shortest Path with Alternating Colors
def shortest_alternating_paths(n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    answer = [0] + [-1] * (n - 1)
    adj = [[] for _ in range(n)]

    for node_i, node_j in redEdges:
        adj[node_i].append([node_j, 0])

    for node_i, node_j in blueEdges:
        adj[node_i].append([node_j, 1])

    visit = [[False] * 2 for _ in range(n)]

    queue = [(0, 0, -1)]
    visit[0][0] = True
    visit[0][1] = True

    while queue:
        node, steps, prev_color = queue.pop(0)

        for neighbor, color in adj[node]:
            if not visit[neighbor][color] and color != prev_color:
                visit[neighbor][color] = True
                queue.append((neighbor, steps + 1, color))

                if answer[neighbor] == -1:
                    answer[neighbor] = steps + 1

    return answer


# 1011. Capacity To Ship Packages Within D Days
def ship_within_days(weights: List[int], days: int) -> int:
    total_load = sum(weights)
    max_load = max(weights)

    left = max_load
    right = total_load

    while left < right:
        mid = (left + right) // 2
        if feasible(weights, mid, days):
            right = mid
        else:
            left = mid + 1

    return left


def feasible(weights: List[int], capacity: int, days: int) -> bool:
    current_load = 0
    days_needed = 1
    for weight in weights:
        if current_load + weight <= capacity:
            current_load += weight
        else:
            days_needed += 1
            current_load = weight

    return days_needed <= days


# 1464. Maximum Product of Two Elements in an Array
def max_product(nums: List[int]) -> int:
    result = 1
    q = []
    for num in nums:
        heappush(q, -num)

    for _ in range(2):
        result *= -heappop(q) - 1

    return result


# 1337. The K Weakest Rows in a Matrix
def k_weakest_rows(mat: List[List[int]], k: int) -> List[int]:
    q = []
    for n, row in enumerate(mat):
        num_soldiers = sum(row)
        heappush(q, (num_soldiers, n))

    res = []
    for _ in range(k):
        res.append(heappop(q)[1])

    return res


# 1345. Jump Game IV
def min_jumps(arr: List[int]) -> int:
    len_arr = len(arr)
    if len_arr < 2:
        return 0

    graph = {}
    for i, value in enumerate(arr):
        if value in graph:
            graph[value].append(i)
        else:
            graph[value] = [i]

    curs = [0]
    visited = {0}
    step = 0

    # when current layer exists
    while curs:
        next_ = []

        # iterate the layer
        for node in curs:
            # check if reached end
            if node == len_arr - 1:
                return step

            # check same value
            for child in graph[arr[node]]:
                if child not in visited:
                    visited.add(child)
                    next_.append(child)

            # clear the list to prevent redundant search
            graph[arr[node]].clear()

            # check neighbors
            for child in [node - 1, node + 1]:
                if 0 <= child < len_arr and child not in visited:
                    visited.add(child)
                    next_.append(child)

        curs = next_
        step += 1

    return 0


# 1160. Find Words That Can Be Formed by Characters
def count_characters(words: List[str], chars: str) -> int:
    chars_counter = Counter(chars)
    good_chars = 0

    for word in words:
        word_counter = Counter(word)
        char_in_chars = [chars_counter.get(key, 0) >= word_counter[key] for key in word_counter]

        if all(char_in_chars):
            good_chars += sum(word_counter.values())

    return good_chars


# 1022. Sum of Root To Leaf Binary Numbers
def sum_root_to_leaf(root: Optional[TreeNode]) -> int:
    def is_leaf(node_: TreeNode) -> bool:
        return not node_.left and not node_.right

    queue = []
    result = []

    if is_leaf(root):
        return root.val

    if root.left:
        queue.append((str(root.val), root.left))
    if root.right:
        queue.append((str(root.val), root.right))

    while queue:
        prev_val, node = queue.pop()
        prev_val += str(node.val)
        if is_leaf(node):
            result.append(int(prev_val, base=2))
        else:
            if node.left:
                queue.append((prev_val, node.left))
            if node.right:
                queue.append((prev_val, node.right))

    return sum(result)


# 1302. Deepest Leaves Sum
def deepest_leaves_sum(root: Optional[TreeNode]) -> int:
    depth_dict = {}

    queue = [(0, root)]
    while queue:
        depth, node = queue.pop()

        if not node.left and not node.right:
            depth_dict[depth] = depth_dict.get(depth, 0) + node.val
        else:
            if node.left:
                queue.append((depth + 1, node.left))
            if node.right:
                queue.append((depth + 1, node.right))

    max_depth = max(depth_dict.keys())
    return depth_dict[max_depth]


# 1325. Delete Leaves With a Given Value
def remove_leaf_nodes(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    def is_leaf(node_: TreeNode) -> bool:
        return not node_.left and not node_.right

    if root.left:
        root.left = remove_leaf_nodes(root.left, target)
    if root.right:
        root.right = remove_leaf_nodes(root.right, target)

    if is_leaf(root) and root.val == target:
        return
    else:
        return root


# 1008. Construct Binary Search Tree from Preorder Traversal
def bst_from_preorder(preorder: List[int]) -> Optional[TreeNode]:
    def build_tree(vals: List[int], max_val) -> Optional[TreeNode]:
        if not vals or vals[0] > max_val:
            return None

        node = TreeNode(vals.pop(0))
        node.left = build_tree(vals, node.val)
        node.right = build_tree(vals, max_val)

        return node

    bst = build_tree(preorder, 2e3)
    return bst
