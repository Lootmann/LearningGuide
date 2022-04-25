def dist(sec, meter, rest, x) -> int:
    rep, mod = divmod(x, sec + rest)

    # total has time
    total = sec * rep

    if mod <= sec:
        total += mod
    else:
        total += sec

    return total * meter


def main():
    a, b, c, d, e, f, x = map(int, input().split())

    takahashi = dist(a, b, c, x)
    aoki = dist(d, e, f, x)

    if takahashi > aoki:
        print("Takahashi")
    elif takahashi < aoki:
        print("Aoki")
    else:
        print("Draw")


if __name__ == "__main__":
    main()
