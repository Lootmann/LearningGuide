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


def main():
    v = Vector(2, 3)
    print(v)

    v += Vector(3, 4)
    print(v)

    v -= Vector(5, 7)
    print(v)

    print(v == Vector(0, 0))


if __name__ == "__main__":
    main()
