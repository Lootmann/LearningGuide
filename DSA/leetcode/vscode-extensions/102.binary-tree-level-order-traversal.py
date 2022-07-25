#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.preorder(root, res, 0)
        return res

    def preorder(self, root: Optional[TreeNode], res: List[List[int]], height: int):
        if root:
            if len(res) == height:
                res.append([])

            res[height].append(root.val)
            self.preorder(root.left, res, height + 1)
            self.preorder(root.right, res, height + 1)


# @lc code=end
