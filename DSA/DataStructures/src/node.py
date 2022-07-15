# src/node.py
from typing import Optional


class SinglyLinkedNode:
    _next: Optional["SinglyLinkedNode"]

    def __init__(self, val):
        self._val = val
        self._next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, _next):
        self._next = _next

    @property
    def val(self):
        return self._val


class MinNode:
    _next: Optional["SinglyLinkedNode"]

    def __init__(self, val):
        self._val = val
        self._min_val = val
        self._next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, _next):
        self._next = _next

    @property
    def val(self):
        return self._val

    @property
    def min_val(self):
        return self._min_val

    @min_val.setter
    def min_val(self, _min):
        self._min_val = min(_min, self._min_val)

    def __str__(self) -> str:
        return "(val, min_val) = ({}, {})".format(self.val, self.min_val)


class DoublyLinkedList:
    _next: Optional["DoublyLinkedList"]
    _prev: Optional["DoublyLinkedList"]

    def __init__(self, val):
        self._val = val
        self._next = None
        self._prev = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, _next: Optional["DoublyLinkedList"]):
        self._next = _next

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, _prev: Optional["DoublyLinkedList"]):
        self._prev = _prev

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, _val):
        self._val = _val


class TreeNode:
    """
    TreeNode
        _val: val
        _left: TreeNode
        _right: TreeNode
    """

    _left = Optional["TreeNode"]
    _right = Optional["TreeNode"]

    def __init__(self, val):
        self._val = val
        self._left = self._right = None

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, _val):
        self._val = _val

    @property
    def left(self) -> Optional["TreeNode"]:
        return self._left

    @left.setter
    def left(self, node: "TreeNode"):
        self._left = node

    @property
    def right(self) -> Optional["TreeNode"]:
        return self._right

    @right.setter
    def right(self, node: "TreeNode"):
        self._right = node

    def __str__(self) -> str:
        left = right = None
        if self._left:
            left = self._left.val

        if self._right:
            right = self._right.val

        return f"(left, val, right) = ({left}, {self._val}, {right})"
