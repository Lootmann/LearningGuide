from typing import List


class Node:
    def __init__(self, ch: str, cnt: int):
        self.ch = ch
        self.cnt = cnt

    def __str__(self) -> str:
        return "({}, {})".format(self.ch, self.cnt)


def converted(s: str) -> List[Node]:
    res = []

    cnt = 1

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            cnt += 1
        else:
            if cnt == 1:
                res.append(Node(s[i], 1))
            else:
                res.append(Node(s[i], cnt))

            cnt = 1

    if cnt == 1:
        res.append(Node(s[-1], 1))
    else:
        res.append(Node(s[-1], cnt))

    return res


def solve():
    s = input()
    t = input()

    s_convs = converted(s)
    t_convs = converted(t)

    if len(s_convs) != len(t_convs):
        return "No"

    for (ss, tt) in zip(s_convs, t_convs):
        if ss.ch != tt.ch:
            return "No"
        if ss.cnt > tt.cnt:
            return "No"
        if ss.cnt == 1 and 1 < tt.cnt:
            return "No"

    return "Yes"


def main():
    print(solve())


if __name__ == "__main__":
    main()
