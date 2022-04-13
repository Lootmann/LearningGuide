def newline(func):
    def wrapper(*args, **kwargs):
        print("~~~~~" * 9)
        result = func(*args, **kwargs)
        print()
        return result

    return wrapper


@newline
def with_file():
    filepath = "/etc/hosts"

    with open(filepath, "r") as hosts:
        for line in hosts:
            if line.startswith("#"):
                continue
            print(line.strip())


class TestContextManager:
    def __enter__(self):
        print("enter")

    def __exit__(self, exc_type, exc_value, traceback):
        print("exit")

    def out(self):
        print("out of sense")


@newline
def context_managet_test():
    tcm = TestContextManager()
    with tcm as t:
        print("tcm")


def main():
    with_file()
    context_managet_test()


if __name__ == "__main__":
    main()
