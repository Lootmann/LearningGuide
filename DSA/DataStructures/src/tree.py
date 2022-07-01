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

    def delete(self, val) -> None:
        self._root = self._delete(self._root, val)
        if self._root:
            self._size -= 1

    def _delete(self, node: Optional["TreeNode"], val) -> Optional["TreeNode"]:
        if not node:
            return None

        if node.val == val:
            if not node.right:
                return node.left

            if not node.left:
                return node.right

            if node.left and node.right:
                node.val = Tree.get_successor(node)
                node.right = self._delete(node.right, node.val)

        elif val < node.val:
            node.left = self._delete(node.left, val)

        else:
            node.right = self._delete(node.right, val)

        return node

    @classmethod
    def get_successor(cls, node: Optional["TreeNode"]) -> Optional["TreeNode"]:
        node = node.right
        while node.left:
            node = node.left
        return node.val

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
