# tests/test_min_stack.py
import pytest
from src.stack import MinStack


class TestMinStack:
    def setup_method(self):
        self.st = MinStack()

    def test_init(self):
        assert self.st.size == 0
        assert self.st._head is None

    def test_push(self):
        """
        [1][2][3]
        """
        self.st.push(1)
        assert self.st.peek == 1
        assert self.st.min_peek == 1

        self.st.push(2)
        assert self.st.peek == 2
        assert self.st.min_peek == 1

        self.st.push(3)
        assert self.st.peek == 3
        assert self.st.min_peek == 1

    def test_pop(self):
        """
        [10] [-1] [5] [15]
        """
        self.st.push(10)
        assert self.st.peek == 10
        assert self.st.min_peek == 10

        self.st.push(-1)
        assert self.st.peek == -1
        assert self.st.min_peek == -1

        self.st.push(5)
        assert self.st.peek == 5
        assert self.st.min_peek == -1

        self.st.push(15)
        assert self.st.peek == 15
        assert self.st.min_peek == -1

        assert self.st.size == 4

        p = self.st.pop()
        assert p.val == 15
        assert p.min_val == -1
        assert self.st.size == 3

        p = self.st.pop()
        assert p.val == 5
        assert p.min_val == -1
        assert self.st.size == 2

        p = self.st.pop()
        assert p.val == -1
        assert p.min_val == -1
        assert self.st.size == 1


class TestMinStackRaises:
    def setup_method(self):
        self.st = MinStack()

    def test_pop(self):
        assert self.st.size == 0

        with pytest.raises(ValueError):
            self.st.peek()

    def test_pop_raise_ValueError_when_stack_is_empty(self):
        self.st.push(1)
        assert self.st.pop().val == 1
        assert self.st.size == 0

        with pytest.raises(ValueError):
            self.st.pop()
