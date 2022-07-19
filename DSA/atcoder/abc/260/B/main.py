from typing import List, Tuple


def ranked_scores(scores: List[int]) -> List[Tuple[int, int]]:
    res = []
    for i, score in enumerate(scores):
        res.append((score, i + 1))
    return sorted(res, key=lambda x: (x[0], -x[1]), reverse=True)


def counts(ans: set, num: int, r_scores: List[Tuple[int, int]]):
    for _, idx in r_scores:
        if num == 0:
            return

        if idx not in ans:
            ans.add(idx)
            num -= 1


def main():
    _, x, y, z = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = set()

    counts(ans, x, ranked_scores(A))
    counts(ans, y, ranked_scores(B))
    counts(ans, z, ranked_scores([x + y for x, y in zip(A, B)]))

    for num in sorted(ans):
        print(num)


if __name__ == "__main__":
    main()
