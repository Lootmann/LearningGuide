import sys
from typing import Optional

input = sys.stdin.readline


class Process:
    """
    self.next はおかしくない?
    """

    next: Optional["Process"]

    def __init__(self, name: str, time: int):
        self._name = name
        self._time = time
        self.next = None

    def name(self) -> str:
        return self._name

    def time(self) -> int:
        return self._time

    def process(self, elapsed: int) -> None:
        self._time -= elapsed

    def is_end(self) -> bool:
        # return whether this process is finished
        return self._time <= 0

    def __str__(self) -> str:
        return f"{self._name} {self._time}"


class Queue:
    _head: Optional[Process]
    _tail: Optional[Process]

    def __init__(self):
        self._head = None
        self._tail = None

    def enqueue(self, p: Process) -> None:

        if self._head is None or self._tail is None:
            self._head = self._tail = p
        else:
            self._tail.next = p
            self._tail = p

    def dequeue(self) -> Process:
        if self._head is None or self._tail is None:
            raise ValueError("Queue is Empty :^)")

        if self._head == self._tail:
            q = self._head
            self._head = self._tail = None
            return q

        q = self._head
        self._head = self._head.next
        return q

    def empty(self) -> bool:
        return self._head is None or self._tail is None


def main():
    n, elapsed = map(int, input().split())
    que = Queue()

    for _ in range(n):
        name, time = map(str, input().split())
        que.enqueue(Process(name, int(time)))

    # simulation
    current_time = 0
    while not que.empty():
        process = que.dequeue()
        process.process(elapsed)
        current_time += elapsed

        if process.is_end():
            rest = process.time()
            current_time += rest
            print(f"{process.name()} {current_time}")
        else:
            # process continues
            que.enqueue(process)


if __name__ == "__main__":
    main()
