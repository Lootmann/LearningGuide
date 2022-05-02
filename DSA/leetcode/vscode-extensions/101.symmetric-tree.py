#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def left_inorder(self, root: Optional[TreeNode], node: List[int]) -> None:
        if root:
            node.append(root.val)

        if root.left:
            self.left_inorder(root.left, node)
        else:
            node.append(None)

        if root.right:
            self.left_inorder(root.right, node)
        else:
            node.append(None)

    def right_inorder(self, root: Optional[TreeNode], node: List[int]) -> None:
        if root:
            node.append(root.val)

        if root.right:
            self.right_inorder(root.right, node)
        else:
            node.append(None)

        if root.left:
            self.right_inorder(root.left, node)
        else:
            node.append(None)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if root.left is None and root.right is None:
            return True

        if root.left and not root.right:
            return False

        if not root.left and root.right:
            return False

        left_node, right_node = [], []

        self.left_inorder(root.left, left_node)
        self.right_inorder(root.right, right_node)

        return left_node == right_node


# @lc code=end
