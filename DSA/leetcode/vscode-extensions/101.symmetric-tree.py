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
    def compare_LR(self, L: Optional[TreeNode], R: Optional[TreeNode]) -> bool:
        if not L and not R:
            return True

        if L and R and L.val == R.val:
            return self.compare_LR(L.left, R.right) and self.compare_LR(L.right, R.left)

        return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.compare_LR(root.left, root.right)


# @lc code=end
