def main():
    s = input()

    chars = set()
    has_lower, has_upper, all_different = False, False, False
    for ch in s:
        chars.add(ch)
        if ch.islower():
            has_lower = True
        elif ch.isupper():
            has_upper = True

    if has_lower and has_upper and len(s) == len(chars):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
