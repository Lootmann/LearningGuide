from enum import Enum


class Color(Enum):
    BOLD = "\033[01m"
    UNDERLINE = "\033[04m"

    ENDC = "\033[0m"


def close_string(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + Color.ENDC.value

    return wrapper


class Print:
    @classmethod
    @close_string
    def bold(cls, msg: str) -> str:
        return "{}{}".format(Color.BOLD.value, msg)

    @classmethod
    @close_string
    def underline(cls, msg: str) -> str:
        return "{}{}".format(Color.UNDERLINE.value, msg)


def main():
    print(Print.bold("hello world :^)"))
    print(Print.underline("umm ... it's cool ..."))


if __name__ == "__main__":
    main()
