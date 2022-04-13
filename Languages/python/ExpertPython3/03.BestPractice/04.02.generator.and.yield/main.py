from typing import Generator


def fibonacci() -> Generator:
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


def main():
    fib = fibonacci()
    lst = [next(fib) for _ in range(10)]
    print(lst)


if __name__ == "__main__":
    main()
