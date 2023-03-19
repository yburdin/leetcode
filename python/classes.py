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


class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}
