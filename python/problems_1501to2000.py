from common import *


class Solution:
    # 1523. Count Odd Numbers in an Interval Range
    @staticmethod
    def count_odds(low: int, high: int) -> int:
        n_odds = (high - low) // 2
        if not (low % 2 == 0 and high % 2 == 0):
            n_odds += 1
        return n_odds

    # 1732. Find the Highest Altitude
    @staticmethod
    def largest_altitude(gain: List[int]) -> int:
        highest_alt = 0
        current_alt = 0

        for i, g in enumerate(gain):
            current_alt += g
            highest_alt = max(current_alt, highest_alt)

            if max(gain[i:]) < 1:
                return highest_alt

        return highest_alt

    # 1700. Number of Students Unable to Eat Lunch
    @staticmethod
    def count_students(students: List[int], sandwiches: List[int]) -> int:
        while len(sandwiches) > 0:
            top_sandwich = sandwiches[0]
            if top_sandwich not in students:
                return len(students)

            current_student = students.pop(0)
            if current_student == top_sandwich:
                sandwiches.remove(top_sandwich)
            else:
                students.append(current_student)

        return len(students)

    # 1925. Count Square Sum Triples
    @staticmethod
    def count_triples(n: int) -> int:
        triples_count = 0
        for a in range(1, n):
            for b in range(a + 1, int((n ** 2 - a ** 2) ** 0.5) + 1):
                c = (a ** 2 + b ** 2) ** 0.5
                if c == int(c):
                    triples_count += 2

        return triples_count

    # 1779. Find Nearest Point That Has the Same X or Y Coordinate
    @staticmethod
    def nearest_valid_point(x: int, y: int, points: List[List[int]]) -> int:
        result = (2**32, -1)

        for point in points[::-1]:
            is_valid_point = point[0] == x or point[1] == y

            if is_valid_point:
                distance = abs(x - point[0]) + abs(y - point[1])
                if distance < result[0] or distance == result[0] and points.index(point) < result[1]:
                    result = (distance, points.index(point))

        return result[-1]

    # 1822. Sign of the Product of an Array
    @staticmethod
    def array_sign(nums: List[int]) -> int:
        if 0 in nums:
            return 0
        else:
            negatives = sum([1 for x in nums if x < 0])

            if negatives % 2 == 0:
                return 1
            else:
                return -1

    # 1502. Can Make Arithmetic Progression From Sequence
    @staticmethod
    def can_make_arithmetic_progression(arr: List[int]) -> bool:
        arr.sort()
        step = arr[1] - arr[0]

        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] != step:
                return False

        return True

    # 1790. Check if One String Swap Can Make Strings Equal
    @staticmethod
    def are_almost_equal(s1: str, s2: str) -> bool:
        equals_list = [0 if s1[i] == s2[i] else 1 for i in range(len(s1))]

        if sum(equals_list) == 0:
            return True
        elif sum(equals_list) == 2:
            i1 = equals_list.index(1)
            i2 = equals_list.index(1, i1 + 1)

            s1_swapped = s1[:i1] + s1[i2] + s1[i1+1:i2] + s1[i1] + s1[i2+1:]
            if s1_swapped == s2:
                return True

        return False

    # 1588. Sum of All Odd Length Subarrays
    @staticmethod
    def sum_odd_length_subarrays(arr: List[int]) -> int:
        result = 0

        for array_length in range(1, len(arr) + 1, 2):
            sub_arrays_sums = [sum(arr[i:array_length+i]) for i in range(len(arr) - array_length + 1)]
            result += sum(sub_arrays_sums)

        return result

    # 1672. Richest Customer Wealth
    @staticmethod
    def maximum_wealth(accounts: List[List[int]]) -> int:
        return max([sum(account) for account in accounts])

    # 1572. Matrix Diagonal Sum
    @staticmethod
    def diagonal_sum(mat: List[List[int]]) -> int:
        size = len(mat)
        primary_diagonal = list(zip(range(size), range(size)))
        secondary_diagonal = list(zip(range(size-1, -1, -1), range(size)))
        if size % 2 == 1:
            primary_diagonal.remove((size//2, size//2))

        diagonals = primary_diagonal + secondary_diagonal

        return sum([mat[row][column] for row, column in diagonals])

    # 1828. Queries on Number of Points Inside a Circle
    @staticmethod
    def is_point_in_circle(point: List[int], circle: List[int]) -> bool:
        distance = ((circle[0]-point[0]) ** 2 + (circle[1]-point[1]) ** 2) ** 0.5
        return distance <= circle[2]

    @staticmethod
    def is_point_in_circle_complex(point: List[int], circle: List[int]) -> bool:
        distance = abs(complex(*point) - complex(circle[0], circle[1]))
        return distance <= circle[2]

    def count_points(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []
        for circle in queries:
            result.append(sum([self.is_point_in_circle_complex(point, circle) for point in points]))

        return result

    # 1768. Merge Strings Alternately
    @staticmethod
    def merge_alternately(word1: str, word2: str) -> str:
        result = ''
        min_len = min(len(word1), len(word2))
        result += ''.join([f'{a}{b}' for a, b in list(zip(word1, word2))])
        result += word1[min_len:] + word2[min_len:]

        return result

    # 1678. Goal Parser Interpretation
    @staticmethod
    def interpret(command: str) -> str:
        return command.replace('()', 'o').replace('(al)', 'al')

    # 1886. Determine Whether Matrix Can Be Obtained By Rotation
    @staticmethod
    def find_rotation(mat: List[List[int]], target: List[List[int]]) -> bool:
        size = len(mat)
        eye_matrix = [[0 if column_n != size - row_n - 1 else 1 for column_n in range(size)]
                      for row_n in range(size)]

        for _ in range(4):
            transpose_mat = [[mat[i][j] for i in range(size)] for j in range(size)]
            result_mat = [[sum([transpose_mat[i][r] * eye_matrix[r][j] for r in range(size)])
                           for j in range(size)]
                          for i in range(size)]

            if result_mat == target:
                return True
            else:
                mat = result_mat

        return False

    # 1630. Arithmetic Subarrays
    def check_arithmetic_subarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        for query in range(len(r)):
            l_i = l[query]
            r_i = r[query]+1

            sub_array = nums[l_i:r_i]
            answer.append(self.is_arithmetic(sorted(sub_array)))
        return answer

    @staticmethod
    def is_arithmetic(array: List[int]) -> bool:
        for i in range(len(array) - 1):
            if array[i + 1] - array[i] != array[1] - array[0]:
                return False
        return True

    # 1816. Truncate Sentence
    @staticmethod
    def truncate_sentence(s: str, k: int) -> str:
        words = s.split(' ')
        new_sentence = ' '.join(words[:k])
        return new_sentence

    # 1675. Minimize Deviation in Array
    def minimum_deviation(self, nums: List[int]) -> int:
        min_val = float('inf')
        pq = []
        for num in nums:
            if num % 2 == 1:
                num = num * 2
            pq.append(-num)
            min_val = min(min_val, num)
        heapify(pq)

        min_deviation = float('inf')
        while True:
            max_val = -heappop(pq)
            min_deviation = min(min_deviation, max_val - min_val)
            if max_val % 2 == 1:
                break
            max_val //= 2
            min_val = min(min_val, max_val)
            heappush(pq, -max_val)
        return min_deviation

    # 1971. Find if Path Exists in Graph
    def valid_path(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n < 2:
            return True

        graph = {node: set() for node in range(n)}

        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        queue = [source]
        visited = {source}

        while queue:
            current_node = queue.pop()

            for next_node in graph[current_node]:
                if next_node == destination:
                    return True
                if next_node not in visited:
                    queue.append(next_node)
                    visited.add(next_node)

        return False

    # 1539. Kth Missing Positive Number
    def find_kth_positive(self, arr: List[int], k: int) -> int:
        left = 0
        right = len(arr)

        while left < right:
            mid = (left + right) // 2
            if arr[mid] - 1 - mid < k:
                left = mid + 1
            else:
                right = mid

        return left + k

    # 1512. Number of Good Pairs
    def num_identical_pairs(self, nums: List[int]) -> int:
        result = 0
        counter = Counter(nums)

        for num in counter:
            n = counter[num]
            result += n * (n - 1) // 2

        return result

    # 1528. Shuffle String
    def restore_string(self, s: str, indices: List[int]) -> str:
        result_list = ['' for _ in range(len(s))]
        for source_index, target_index in enumerate(indices):
            result_list[target_index] = s[source_index]

        return ''.join(result_list)

    # 1646. Get Maximum in Generated Array
    def get_maximum_generated(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]

        for i in range(1, n + 1):
            if i == 1:
                dp[i] = 1
            elif i % 2 == 0:
                dp[i] = dp[i // 2]
            else:
                dp[i] = dp[i // 2] + dp[i // 2 + 1]

        return max(dp)
