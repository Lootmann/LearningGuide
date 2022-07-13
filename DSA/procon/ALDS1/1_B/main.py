def mygcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return mygcd(b, a % b)


def main():
    x, y = map(int, input().split())
    print(mygcd(x, y))


if __name__ == "__main__":
    main()
