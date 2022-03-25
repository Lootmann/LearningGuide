# test.py
import pytest

from calc import add


def test_add():
    assert add(1, 2) == 3


class TestClass:
    def test_add(self):
        assert add(2, 3) == 5

    def test_raised(self):
        with pytest.raises(ValueError):
            assert add(1, "3") == 4  # type: ignore
