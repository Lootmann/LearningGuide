from pathlib import Path


def walk():
    current = Path(".")

    for path in current.glob("*"):
        print(path)


def main():
    print(">>> path")
    walk()


if __name__ == "__main__":
    main()
