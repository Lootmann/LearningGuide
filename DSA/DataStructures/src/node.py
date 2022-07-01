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

    @val.setter
    def val(self, _val):
        self._val = _val
