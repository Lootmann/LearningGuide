import sys
from typing import Any


def get_line() -> str:
    return sys.stdin.readline().strip()


def get_lines() -> list:
    return sys.stdin.readlines()


def write(msg: Any) -> None:
    sys.stdout.write(str(msg) + "\n")


def binary_search(s: list, key: int) -> bool:
    left = 0
    right = len(s)

    while left < right:
        mid = (left + right) // 2

        if s[mid] == key:
            return True

        elif key < s[mid]:
            right = mid

        else:
            left = mid + 1

    return False


def main():
    lines = get_lines()
    s = list(map(int, lines[1].strip().split()))
    t = list(map(int, lines[3].strip().split()))

    cnt = 0
    for key in t:
        if binary_search(s, key):
            cnt += 1

    write(cnt)


if __name__ == "__main__":
    main()
