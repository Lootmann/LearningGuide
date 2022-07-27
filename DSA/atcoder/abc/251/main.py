from typing import OrderedDict


def vinput() -> tuple:
    s, t = input().split(" ")
    return s, int(t)


def main():
    d = OrderedDict()
    n = int(input())

    max_score = 0

    for i in range(1, n + 1):
        s, t = vinput()

        if s not in d:
            # d[key] = index, score
            d[s] = (i, t)
            max_score = max(max_score, t)

    for idx, score in d.values():
        if score == max_score:
            print(idx)
            return


if __name__ == "__main__":
    main()
