class Node:
    next: "Node"
    prev: "Node"

    def __init__(self, value):
        self.next = self
        self.prev = self
        self.value = value


class LinkedList:
    dummy: Node

    def __init__(self):
        self.length = 0

        self.dummy = Node(-1)

    def __len__(self) -> int:
        return self.length

    def __iter__(self):
        cur = self.dummy.next
        while not self.empty():
            yield cur.value
            cur = cur.next

    def __next__(self):
        if self.empty():
            raise StopIteration()
        return self.shift()

    def push(self, val: int) -> None:
        """push
        stack add
        """
        self.length += 1
        new_node = Node(val)

        new_node.next = self.dummy
        self.dummy.prev.next = new_node
        new_node.prev = self.dummy.prev
        self.dummy.prev = new_node

    def pop(self) -> int:
        if self.empty():
            raise ValueError("stack is emtpy")

        self.length -= 1

        p = self.dummy.prev.value
        self._del(self.dummy.prev)
        return p

    def unshift(self, val: int) -> None:
        self.length += 1

        new_node = Node(val)
        new_node.next = self.dummy.next
        self.dummy.next.prev = new_node
        self.dummy.next = new_node
        new_node.prev = self.dummy

    def shift(self) -> int:
        if self.empty():
            raise ValueError("stack is emtpy")

        self.length -= 1

        p = self.dummy.next.value
        self._del(self.dummy.next)
        return p

    def _del(self, node: Node) -> None:
        if node is self.dummy:
            return

        node.prev.next = node.next
        node.next.prev = node.prev

    def empty(self) -> bool:
        """empty
        When self.dummy.next points self.dummy,
        self has no Nodes.
        """
        return self.dummy == self.dummy.next or self.length == 0

    def __str__(self) -> str:
        res = []
        cur = self.dummy.next
        while cur != self.dummy:
            res.append(f"({cur.prev.value}) {cur.value} ({cur.next.value})")
            cur = cur.next

        return ", ".join(res)
