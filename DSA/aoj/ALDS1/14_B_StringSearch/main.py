def main():
    t = input()
    p = input()

    for i in range(len(t) - len(p) + 1):
        if t[i : i + len(p)] == p:
            print(i)


if __name__ == "__main__":
    main()
