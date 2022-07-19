from collections import Counter


def main():
    ans = "-1"

    c = Counter(input())

    for (k, v) in c.items():
        if v == 1:
            ans = k

    print(ans)


if __name__ == "__main__":
    main()
