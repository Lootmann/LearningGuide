# src/deque.py
from typing import Optional, Any
from src.node import DoublyLinkedList


class Deque:
    """
    Deque a.k.a. Double-Ended Queue

    is an abstract data type that generalizes a queue,
    for which elements can be added to removed from either the front or back
    """

    dummy: Optional["DoublyLinkedList"]

    def __init__(self):
        """
        length: int
        dummy: DoublyLinkedList with random number
        """
        self._length = 0
        self.dummy = DoublyLinkedList(-1)
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

    def __len__(self) -> int:
        return self._length

    def front(self) -> Any:
        if self.empty():
            raise ValueError("Node doesn't have any Nodes D:")

        return self.dummy.next.val

    def back(self) -> Any:
        if self.empty():
            raise ValueError("Node doesn't have any Nodes D:")

        return self.dummy.prev.val

    def push(self, val: Any) -> DoublyLinkedList:
        """push
        insert val at back
        this method simulates stack.push()

        :param val:
        :return: a pushed Node
        """
        self._length += 1
        new_node = DoublyLinkedList(val)

        new_node.next = self.dummy
        self.dummy.prev.next = new_node
        new_node.prev = self.dummy.prev
        self.dummy.prev = new_node

        return new_node

    def pop(self) -> DoublyLinkedList:
        """pop
        remove node at back
        this method simulates stack.pop()

        :return: a popped Node
        """
        if self.empty():
            raise ValueError("Stack is Empty :^)")

        self._length -= 1
        p = self.dummy.prev
        self._del(self.dummy.prev)
        return p

    def push_front(self, val: Any) -> DoublyLinkedList:
        """
        insert val at front
        this method simulates queue.enqueue()

        :return: a enqueued Node
        """
        self._length += 1

        new_node = DoublyLinkedList(val)
        new_node.next = self.dummy.next
        self.dummy.next.prev = new_node
        self.dummy.next = new_node
        new_node.prev = self.dummy
        return new_node

    def pop_front(self) -> DoublyLinkedList:
        """
        remove node at front
        this method simulates queue.Dequeue

        :return: a popped Node
        """

        if self.empty():
            raise ValueError("Queue is Empty :^)")

        self._length -= 1
        p = self.dummy.next
        self._del(self.dummy.next)
        return p

    def _del(self, node: DoublyLinkedList) -> None:
        if node is self.dummy:
            return

        node.prev.next = node.next
        node.next.prev = node.prev

    def empty(self):
        return self._length == 0 or (
            self.dummy.next == self.dummy and self.dummy.prev == self.dummy
        )
