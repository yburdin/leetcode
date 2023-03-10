from typing import List, Optional
from heapq import heappop, heapify, heappush
import random


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

    def __str__(self):
        return_str = f'val={self.val}'
        if self.next:
            return_str += f' next={self.next.val}'

        return return_str

    def __repr__(self):
        return f'ListNode({self.val})'


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

        if isinstance(left, int):
            self.left = TreeNode(left)
        elif isinstance(left, TreeNode):
            self.left = left

        if isinstance(right, int):
            self.right = TreeNode(right)
        elif isinstance(right, TreeNode):
            self.right = right

    def __str__(self):
        return_str = f'val={self.val}'
        if self.left:
            return_str += f' left={self.left.val}'
        if self.right:
            return_str += f' right={self.right.val}'

        return return_str

    def __repr__(self):
        return f'TreeNode({self.val})'


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class QuadNode:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


# 707. Design Linked List
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """

        if self.size <= index or index < 0:
            return -1

        current_node = self.head
        for i in range(index):
            current_node = current_node.next

        return current_node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        self.head = ListNode(val, self.head)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val as the last element of the linked list.
        """
        if self.size == 0:
            self.addAtHead(val)

        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next

            current_node.next = ListNode(val)
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the indexth node in the linked list.
        If index equals the length of the linked list, the node will be appended to the end of the linked list.
        If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)

        elif index == self.size:
            self.addAtTail(val)

        elif index < self.size:
            current_node = self.head
            for i in range(index - 1):
                current_node = current_node.next

            next_node = current_node.next
            current_node.next = ListNode(val, next_node)
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.size > index >= 0:
            current_node = self.head
            if index == 0:
                self.head = current_node.next
            else:
                for i in range(index - 1):
                    current_node = current_node.next

                current_node.next = current_node.next.next

            self.size -= 1


# 303. Range Sum Query - Immutable
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sum_range(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])


# 304. Range Sum Query 2D - Immutable
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.sums = [[0 for _ in range(len(self.matrix[0]) + 1)] for _ in range(len(self.matrix) + 1)]
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[0])):
                self.sums[row+1][col+1] = sum([sum(row_[:col+1]) for row_ in self.matrix[:row+1]])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.sums[row2+1][col2+1] - self.sums[row1][col2+1] - self.sums[row2+1][col1] + self.sums[row1][col1]
        return result


# 232. Implement Queue using Stacks
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        self.peek()
        return self.s2.pop()

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self):
        return not self.s1 and not self.s2


# 1603. Design Parking System
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.parking_dict = {1: big, 2: medium, 3: small}

    def add_car(self, car_type: int) -> bool:
        if self.parking_dict[car_type] > 0:
            self.parking_dict[car_type] -= 1
            return True
        else:
            return False


# 1845. Seat Reservation Manager
class SeatManager:

    def __init__(self, n: int):
        self.heap = list(range(1, n + 1))

    def reserve(self) -> int:
        return heappop(self.heap)

    def unreserve(self, seat_number: int) -> None:
        heappush(self.heap, seat_number)


# 729. My Calendar I
class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        for event_start, event_end in self.events:
            if event_start <= start < event_end:
                return False
            if event_start < end <= event_end:
                return False
            if start < event_start and end > event_end:
                return False

        self.events.append((start, end))
        return True


# 355. Design Twitter
class Twitter:
    # Implement the Twitter class
    def __init__(self):
        # Initializes your twitter object.
        self.users = {}
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Composes a new tweet with ID tweetId by the user userId.
        # Each call to this function will be made with a unique tweetId.
        self.tweets.append({'user_id': userId, 'tweet_id': tweetId})

        if userId not in self.users:
            self.users[userId] = {'follow': []}

    def getNewsFeed(self, userId: int) -> List[int]:
        # Retrieves the 10 most recent tweet IDs in the user's news feed.
        # Each item in the news feed must be posted by users who the user followed or by the user themself.
        # Tweets must be ordered from most recent to least recent.

        news_feed = []
        if userId in self.users:
            user_ids = self.users[userId]['follow'] + [userId]

            for tweet in self.tweets[::-1]:
                if tweet['user_id'] in user_ids:
                    news_feed.append(tweet['tweet_id'])

                    if len(news_feed) == 10:
                        return news_feed

        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        # The user with ID followerId started following the user with ID followeeId.
        if followeeId not in self.users:
            self.users[followeeId] = {'follow': []}

        if followerId not in self.users:
            self.users[followerId] = {'follow': []}

        if followerId in self.users and followeeId in self.users:
            self.users[followerId]['follow'].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # The user with ID followerId started unfollowing the user with ID followeeId.
        if followerId in self.users and followeeId in self.users[followerId]['follow']:
            self.users[followerId]['follow'].remove(followeeId)


# 933. Number of Recent Calls
class RecentCounter:
    def __init__(self):
        """
        RecentCounter() Initializes the counter with zero recent requests.
        """
        self.requests = []
        self.index_min = 0

    def ping(self, t: int) -> int:
        """
        Adds a new request at time t, where t represents some time in milliseconds,
        and returns the number of requests that has happened in the past 3000 milliseconds (including the new request).
        Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
        """

        self.requests.append(t)
        self.requests = sorted(self.requests)

        t_min = t - 3000
        while self.requests[self.index_min] < t_min and self.index_min < len(self.requests) - 1:
            self.index_min += 1

        return len(self.requests[self.index_min:])


# 706. Design HashMap
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


# 703. Kth Largest Element in a Stream
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapify(self.nums)

        while len(self.nums) > self.k:
            heappop(self.nums)

    def add(self, val: int) -> int:
        heappush(self.nums, val)
        if len(self.nums) > self.k:
            heappop(self.nums)
        return self.nums[0]


# 382. Linked List Random Node
class LinkedListRandom:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        cur_value = None
        element_number = 1

        cur = self.head
        if cur:
            cur_value = cur.val

        while cur:
            cur = cur.next
            element_number += 1
            if cur and random.random() < 1 / element_number:
                cur_value = cur.val

        return cur_value

