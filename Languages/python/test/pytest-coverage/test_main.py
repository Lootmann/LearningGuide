# test_main.py
# import pytest

from main import *


def test_add():
    assert add(1, 2) == 3


def test_add1():
    assert add(6, 5) == 0


def test_sub():
    assert sub(3, 2) == 1


def test_mul():
    assert mul(2, 3) == 6


def test_div1():
    assert div(1, 0) == 0


def test_div2():
    assert div(10, 0) == 0


def test_div3():
    assert div(10, 2) == 5
