def f(ham: str, eggs: str = "eggs") -> str:
    return "{} {}".format(ham, eggs)


def main():
    print(f.__annotations__)


if __name__ == "__main__":
    main()
