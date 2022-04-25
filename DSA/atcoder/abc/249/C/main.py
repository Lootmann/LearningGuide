from collections import Counter


def main():
    N, K = map(int, input().split())
    S = []
    for _ in range(N):
        S.append(input())

    ans = 0
    for i in range(2**N):
        counter = Counter()
        for j in range(N):
            if (i >> j) & 1:
                for ch in S[j]:
                    counter[ch] += 1

        cnt = 0
        for m in counter.most_common():
            if m[1] == K:
                cnt += 1

        ans = max(ans, cnt)

    print(ans)


if __name__ == "__main__":
    main()
