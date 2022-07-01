# src/queue.py
from typing import Optional
from src.node import SinglyLinkedNode


class Queue:
    _head: Optional["SinglyLinkedNode"]
    _tail: Optional["SinglyLinkedNode"]

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, val):
        new_node = SinglyLinkedNode(val)
        self._size += 1

        if self.empty():
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

    def dequeue(self) -> "SinglyLinkedNode":
        self._size -= 1

        if self.empty():
            raise ValueError("Queue is empty")
        elif self._head == self._tail:
            que = self._head
            self._head = self._tail = None
            return que
        else:
            que = self._head
            self._head = self._head.next
            return que

    def empty(self) -> bool:
        """empty

        :return: return True when Queue is empty
        """
        return self._head is None or self._tail is None

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, _size: int):
        self._size = _size

    @property
    def peek(self):
        if self.empty():
            raise ValueError("stack is empty")
        return self._head.val
