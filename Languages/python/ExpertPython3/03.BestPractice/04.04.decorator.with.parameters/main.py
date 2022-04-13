def repeat(number: int = 3):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(number):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return actual_decorator


@repeat(2)
def greeting(name: str):
    print("Hello {}".format(name))


def main():
    name = "Lyo"
    greeting(name)


if __name__ == "__main__":
    main()
