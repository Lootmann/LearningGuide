#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
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
    def inorder(self, node: TreeNode, lst: list) -> None:
        if not node:
            return

        if node:
            lst.append(node.val)

        if node.left:
            self.inorder(node.left, lst)

        if node.right:
            self.inorder(node.right, lst)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # stupid
        lst = []

        self.inorder(root, lst)

        lst.sort()

        return lst[k - 1]


# @lc code=end
