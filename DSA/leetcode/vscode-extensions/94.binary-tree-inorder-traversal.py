#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()

        def dfs(node: TreeNode):
            if node is None:
                return

            if node.left is not None:
                dfs(node.left)

            result.append(node.val)

            if node.right is not None:
                dfs(node.right)

        dfs(root)

        return result


# @lc code=end
