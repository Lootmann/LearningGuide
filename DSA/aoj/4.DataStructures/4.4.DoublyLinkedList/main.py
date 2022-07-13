import sys


class Node:
    next: "Node"
    prev: "Node"

    def __init__(self, key: str):
        self.key = key
        self.next = self
        self.prev = self


class DoublyLinkedList:
    # sentinel, dummy, nil, and so forth.
    _dummy: Node

    def __init__(self):
        self._dummy = Node("")

    def insert(self, x: str):
        new_node = Node(x)
        new_node.next = self._dummy.next
        self._dummy.next.prev = new_node
        self._dummy.next = new_node
        new_node.prev = self._dummy

    def delete(self, x: str) -> None:
        # find all elements O(n)
        cur = self._dummy.next
        while (cur is not self._dummy) and cur.key != x:
            cur = cur.next

        if cur is self._dummy:
            return

        self._del(cur)

    def delete_first(self) -> None:
        first = self._dummy.next

        if self._dummy is first:
            return

        self._del(first)

    def delete_last(self) -> None:
        last = self._dummy.prev

        if self._dummy is last:
            return

        self._del(last)

    def _del(self, node: Node) -> None:
        if node is self._dummy:
            return

        node.prev.next = node.next
        node.next.prev = node.prev

    def __str__(self) -> str:
        lists = []
        cur = self._dummy.next

        while cur is not self._dummy:
            lists.append(cur.key)
            cur = cur.next

        return " ".join(lists)


def main():
    dll = DoublyLinkedList()

    # get all inputs
    _ = sys.stdin.readline()

    for line in sys.stdin.readlines():
        if "deleteFirst" in line:
            dll.delete_first()

        elif "deleteLast" in line:
            dll.delete_last()

        elif "insert" in line:
            _, key = line.split()
            dll.insert(key)

        elif "delete" in line:
            _, key = line.split()
            dll.delete(key)

        else:
            pass

    print(dll)


if __name__ == "__main__":
    main()
