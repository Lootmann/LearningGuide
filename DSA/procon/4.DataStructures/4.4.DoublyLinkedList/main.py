import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.next = self
        self.prev = self


class DoublyLinkedList:
    def __init__(self):
        self._dummy = Node(-1)

    def insert(self, x):
        new_node = Node(x)
        new_node.next = self._dummy.next
        self._dummy.next.prev = new_node
        self._dummy.next = new_node
        new_node.prev = self._dummy

    def delete(self, x):
        cur = self._dummy.next
        while (cur is not self._dummy) and cur.val != x:
            cur = cur.next

        self._del(cur)

    def delete_first(self):
        self._del(self._dummy.next)

    def delete_last(self):
        self._del(self._dummy.prev)

    def _del(self, node):
        if node is self._dummy:
            return

        node.prev.next = node.next
        node.next.prev = node.prev

    def print(self):
        lists = []
        cur = self._dummy.next

        while cur is not self._dummy:
            lists.append(cur.val)
            cur = cur.next

        sys.stdout.write(" ".join(lists))
        sys.stdout.write("\n")


def main():
    dll = DoublyLinkedList()

    for command in sys.stdin.readlines():
        if "deleteFirst" in command:
            dll.delete_first()

        elif "deleteLast" in command:
            dll.delete_last()

        elif "insert" in command:
            _, num = command.split()
            dll.insert(num)

        elif "delete" in command:
            _, num = command.split()
            dll.delete(num)
        else:
            pass

    dll.print()


if __name__ == "__main__":
    main()
