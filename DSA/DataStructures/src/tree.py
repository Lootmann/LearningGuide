# src/tree.py
from typing import Optional
from src.node import TreeNode


class Tree:
    """
    non-balanced Binary Search tree
    """

    _root: Optional["TreeNode"]

    def __init__(self):
        self._root = None
        self._size = 0

    @property
    def size(self) -> int:
        return self._size

    @property
    def root(self) -> Optional["TreeNode"]:
        return self._root

    def insert(self, val):
        """
        insert val to TreeNode

        :param val:
        :return: None
        """
        self._size += 1
        node = TreeNode(val)

        if not self._root:
            self._root = node
        else:
            self._insert(self._root, val)

    def _insert(self, node, val):
        """
        insert val to Binary Search Tree

        A TreeNode should obey this following pattern:
            left.val < node.val < right.val

        :param node: TreeNode
        :param val: val
        :return: None
        """
        if val < node.val:
            if not node.left:
                node.left = TreeNode(val)
            else:
                self._insert(node.left, val)
        elif node.val < val:
            if not node.right:
                node.right = TreeNode(val)
            else:
                self._insert(node.right, val)
        else:
            # ignored node.val == val
            return

    def find(self, val) -> bool:
        """
        find val in TreeNode using DFS

        :param val:
        :return: boolean
        """
        stack, order = [], []
        cur = self._root

        while cur or len(stack) > 0:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if cur.val == val:
                    return True
                cur = cur.right

        return False

    def inorder(self) -> list:
        res = []
        self._inorder(self._root, res)
        return res

    def _inorder(self, node: Optional["TreeNode"], res: list):
        """
        inorder traversal with recursion
        :param node: TreeNode
        :param res: list
        """
        if node:
            self._inorder(node.left, res)
            res.append(node.val)
            self._inorder(node.right, res)

    def preorder(self) -> list:
        res = []
        self._preorder(self._root, res)
        return res

    def _preorder(self, node: Optional["TreeNode"], res: list):
        if node:
            res.append(node.val)
            self._preorder(node.left, res)
            self._preorder(node.right, res)

    def postorder(self) -> list:
        res = []
        self._postorder(self._root, res)
        return res

    def _postorder(self, node: Optional["TreeNode"], res: list):
        if node:
            self._postorder(node.left, res)
            self._postorder(node.right, res)
            res.append(node.val)
