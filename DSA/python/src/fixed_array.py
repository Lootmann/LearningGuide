"""src/fixed_array.py

fixed length array
"""


from typing import Any

from src.custom_errors import RangeError


class FixedArray:
    def __init__(self, size: int = 10, _type: Any = int):
        if not isinstance(size, int):
            raise TypeError("size should be int")

        if size < 0:
            raise RangeError("size should be positive")

        self._size = int(size)
        self._type = _type

        if _type == str:
            self.fill("")
        elif _type == int:
            self.fill(0)
        elif _type == float:
            self.fill(0.0)
        elif _type == bool:
            self.fill(None)
        else:
            raise TypeError("The following 4 types are allowed, int, float, str, bool")

    def fill(self, value: Any):
        self._arr = [value] * self._size

    def __getitem__(self, key: int) -> int | float | str | bool:
        if key < 0 or self._size <= key:
            raise IndexError("Outbound Index")

        return self._arr[key]

    @property
    def size(self) -> int:
        return self._size

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return ", ".join(map(str, [num for num in self._arr]))
