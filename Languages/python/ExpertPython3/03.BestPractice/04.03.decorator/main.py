def mydecorator(func):
    def wrapper(*args, **kwargs):
        print("*** before")
        result = func(*args, **kwargs)
        print("*** after")
        return result

    return wrapper


@mydecorator
def greeting(name: str) -> None:
    print("Hello {} :^)".format(name))


def main():
    greeting("lyota")


if __name__ == "__main__":
    main()
