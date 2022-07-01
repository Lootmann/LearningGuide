# tests/test_stack.py
import pytest
from src.stack import Stack


class TestStack:
    def setup_method(self):
        self.st = Stack()

    def test_init(self):
        assert self.st.size == 0
        assert self.st._head is None

    def test_empty(self):
        assert self.st.empty() is True

    def test_peek(self):
        self.st.push(9)
        assert self.st.peek == 9

        self.st.push(4)
        assert self.st.peek == 4

    def test_push(self):
        size = 10
        for num in range(1, size + 1):
            self.st.push(num)
            assert self.st.peek == num

        assert self.st.size == size

    def test_pop(self):
        nums = [1, 2, 3, 4]
        for num in nums:
            self.st.push(num)

        for num in reversed(nums):
            assert self.st.size == num
            assert self.st.pop().val == num

        assert self.st.size == 0

    def test_pop_many(self):
        assert self.st.size == 0

        for num in range(1, 10000):
            self.st.push(num)

        while not self.st.empty():
            self.st.pop()

        assert self.st.size == 0


class TestStackRaises:
    def setup_method(self):
        self.st = Stack()

    def test_top(self):
        assert self.st.size == 0

        with pytest.raises(ValueError):
            self.st.peek()

    def test_pop_raise_ValueError_when_stack_is_empty(self):
        self.st.push(1)
        assert self.st.pop().val == 1
        assert self.st.size == 0

        with pytest.raises(ValueError):
            self.st.pop()
