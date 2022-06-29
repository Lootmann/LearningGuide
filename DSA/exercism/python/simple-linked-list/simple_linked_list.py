from typing import Optional


class Node:
    _next: Optional["Node"]

    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self) -> int:
        return self._value

    def next(self) -> Optional["Node"]:
        return self._next


class LinkedList:
    def __init__(self, values=[]):
        self._head = None
        self._cnt = 0

        for val in values:
            self.push(val)

    def __len__(self):
        return self._cnt

    def __iter__(self):
        self.iter_next = self._head
        return self

    def __next__(self):
        if self.iter_next:
            value = self.iter_next.value()
            self.iter_next = self.iter_next._next
            return value
        else:
            raise StopIteration

    def head(self):
        if self.empty():
            raise EmptyListException("The list is empty.")

        return self._head

    def push(self, value):
        new_node = Node(value)

        if self.empty():
            self._head = new_node
        else:
            new_node._next = self._head
            self._head = new_node

        self._cnt += 1

    def pop(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")

        cur = self._head
        self._head = self._head.next()
        self._cnt -= 1
        return cur.value()

    def empty(self) -> bool:
        return self._head is None

    def reversed(self) -> list:
        return list(self)[::-1]


class EmptyListException(Exception):
    pass
