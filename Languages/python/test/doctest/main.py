def add(x: int = 0, y: int = 0) -> int:
    """Return the sum of x and y
    >>> add()
    0

    >>> add(1, 2)
    3

    >>> add(10, -10)
    0
    """

    return x + y


if __name__ == "__main__":
    import doctest

    doctest.testmod()
