# src/stack.py
from typing import Optional
from src.node import SinglyLinkedNode


class Stack:
    _head: Optional["SinglyLinkedNode"]

    def __init__(self):
        self._size = 0
        self._head = None

    def push(self, val):
        """push
        push val

        :param val:
        :return: None
        """
        self._size += 1
        new_node = SinglyLinkedNode(val)

        if self.empty():
            self._head = new_node
        else:
            new_node.next = self._head
            self._head = new_node

    def pop(self) -> SinglyLinkedNode:
        """
        NOTE: this 'pop' method pops an Node
            but pop Node.val(int, str or something) is also good.

        :return: SinglyLinkedNode, never return None
        """
        if self.empty():
            raise ValueError("stack is empty")

        self._size -= 1
        popped = self._head
        self._head = self._head.next
        return popped

    def empty(self) -> bool:
        return self._head is None

    @property
    def size(self) -> int:
        return self._size

    @property
    def peek(self):
        if self.empty():
            raise ValueError("stack is empty")
        return self._head.val
