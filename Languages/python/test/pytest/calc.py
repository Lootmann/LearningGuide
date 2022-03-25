# calc.py
from typing import Any


def convert(x: Any, var_type: Any) -> int:
    if not isinstance(x, var_type):
        raise ValueError("arg is not int")
    return x


def add(x: int, y: int) -> int:
    x = convert(x, int)
    y = convert(y, int)
    return x + y
