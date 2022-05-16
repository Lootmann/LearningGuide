#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    # O(N)
    def inorder(self, node: TreeNode, values: list):
        if not node:
            return

        self.inorder(node.left, values)
        values.append(node.val)
        self.inorder(node.right, values)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []
        self.inorder(root, values)

        result = True

        # O(N)
        for i in range(len(values) - 1):
            result &= values[i] < values[i + 1]

        return result


# @lc code=end
