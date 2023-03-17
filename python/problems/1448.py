from common import TreeNode


# 1448. Count Good Nodes in Binary Tree
class GoodNode:
    def __init__(self):
        self.result = 0

    def good_nodes(self, root: TreeNode) -> int:
        self.traverse(root)
        return self.result

    def traverse(self, node: TreeNode, cur_max=-10 ** 5):
        if node.val >= cur_max:
            self.result += 1
        if node.left:
            self.traverse(node.left, max(cur_max, node.val))
        if node.right:
            self.traverse(node.right, max(cur_max, node.val))
