from common import TreeNode
from problems_0001to0500 import inorder_traversal, sorted_array_to_bst


# 1382. Balance a Binary Search Tree
class BalanceBST:
    def balance_bst(self, root: TreeNode) -> TreeNode:
        traversal = inorder_traversal(root)
        bst = sorted_array_to_bst(traversal)
        return bst
