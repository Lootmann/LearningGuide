def main():
    n, m, x, t, d = map(int, input().split())
    print(t - d * max(0, x - m))


if __name__ == "__main__":
    main()
