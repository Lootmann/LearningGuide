from collections import UserDict


def title(msg: str):
    def inner(func):
        def wrapper(*args, **kwgs):
            l = len(msg) + 8
            print(">" * l)
            print(f">>> {msg}")
            print(">" * l)
            result = func(*args, **kwgs)
            print()
            return result

        return wrapper

    return inner


class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, other) -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other) -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __repr__(self) -> str:
        return f"<Vector: x={self.x}, y={self.y}>"

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y


@title("vector")
def vector():
    v = Vector(2, 3)
    print(v)

    v += Vector(3, 4)
    print(v)

    v -= Vector(5, 7)
    print(v)

    print(v == Vector(0, 0))


class DistinctError(ValueError):
    """"""


class distinctdict(UserDict):
    def __setitem__(self, key, value) -> None:
        if value in self.values():
            if (key in self and self[key] != value) or key not in self:
                raise DistinctError("value should be unique :^)")
        super().__setitem__(key, value)


@title("distinct dict")
def distinctdict_sample():
    d = distinctdict()
    d["key"] = "v"
    d["kagi"] = "atai"
    d["key"] = "another"
    d["wow"] = "hey"
    d["new"] = "v"
    print(d)


class Mama:
    def says(self):
        print("Do your assignment")


class Sister(Mama):
    def says(self):
        # or super().says()
        super(Sister, self).says()
        print("and clean your bedroom")


@title("Mama")
def mama():
    mama = Mama()
    mama.says()

    sis = Sister()
    sis.says()


def main():
    vector()
    distinctdict_sample()
    mama()


if __name__ == "__main__":
    main()
