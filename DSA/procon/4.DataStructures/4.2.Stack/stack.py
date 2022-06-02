import sys
from typing import Union

input = sys.stdin.readline


class Node:
    next: Union["Node", None]

    def __init__(self, val: int = 0):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self._head = None
        self._size = 0

    def size(self) -> int:
        return self._size

    def push(self, val: int) -> None:
        self._size += 1

        if self._head is None:
            self._head = Node(val)
            return

        new_node = Node(val)
        new_node.next = self._head
        self._head = new_node

    def pop(self) -> "Node":
        self._size -= 1

        if self._head is None:
            raise ValueError("stack is empty :^)")

        poped = self._head
        self._head = self._head.next
        return poped

    def peek(self) -> "Node":
        if not self._head:
            raise ValueError("stack is empty :^)")
        return self._head

    def empty(self) -> bool:
        return self._head is None


def is_operand(ch: str) -> bool:
    return ch in ("+", "-", "*")


def main():
    stack = Stack()
    string = input().strip()

    for ch in string.split(" "):
        if is_operand(ch):
            right = stack.pop().val
            left = stack.pop().val
            stack.push(eval(f"{left} {ch} {right}"))
        else:
            stack.push(int(ch))

    print(stack.peek().val)


if __name__ == "__main__":
    main()
