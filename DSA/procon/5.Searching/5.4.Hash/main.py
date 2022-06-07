"""
Hash with Chaining

https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/4/ALDS1_4_C
"""
import sys
from typing import List, Optional


class Node:
    key: int
    next: Optional["Node"]

    def __init__(self, key: int = 0):
        self.key = key
        self.next = None


class Hash:
    """
    hash size lists

    Accepted:
        50021
        100003
        450001
        800011
        1100009
        1200007
        1300007
        2000003
        6000011
        7500013
        9999991

    TLE:
        10007
    """

    MAX = 110009
    _hash: List[Optional[Node]]

    def __init__(self):
        self._hash = [None] * self.MAX

    def _char_to_int(self, ch: str) -> int:
        if ch == "A":
            return 1
        if ch == "C":
            return 2
        if ch == "G":
            return 3
        if ch == "T":
            return 4
        raise ValueError("wrong ch")

    def _key_to_num(self, key: str) -> int:
        weight = 1
        total = 0
        for ch in key:
            total += self._char_to_int(ch) * weight
            weight *= 4
        return total

    def _get_key(self, key: str) -> int:
        return self._key_to_num(key)

    def insert(self, key: str) -> None:
        num = self._get_key(key)
        hash_key = num % self.MAX

        node = self._hash[hash_key]

        if node is None:
            self._hash[hash_key] = Node(num)
            return

        # Chaining
        while node.next is not None:
            # exists
            if node.key == num:
                return
            node = node.next

        node.next = Node(num)

    def find(self, key: str) -> bool:
        num = self._get_key(key)
        hash_key = num % self.MAX
        node = self._hash[hash_key]

        # Chaining
        while node is not None:
            if node.key == num:
                return True
            node = node.next

        return False


def main():
    hash = Hash()
    s = sys.stdin.readlines()

    for line in s[1:]:
        operation, key = line.strip().split()

        if "insert" in operation:
            hash.insert(key)
        else:
            if hash.find(key):
                print("yes")
            else:
                print("no")


if __name__ == "__main__":
    main()
