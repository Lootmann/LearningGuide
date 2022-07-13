import pytest

from stack import Stack


@pytest.fixture
def stack():
    return Stack()


class TestStackPush:
    def setup_method(self):
        self.stack = Stack()

    def test_push_1(self):
        self.stack.push(1)
        assert self.stack.size() == 1
        assert self.stack.peek().val == 1

    def test_push_many(self):
        for i in range(100):
            self.stack.push(i)

        assert self.stack.size() == 100
        assert self.stack.peek().val == 99


class TestStack:
    def setup_method(self):
        self.stack = Stack()

    def test_init(self):
        assert self.stack.size() == 0
        assert self.stack.empty() is True


class TestStackPeek:
    def setup_method(self):
        self.stack = Stack()

    def test_peek_empty_stack(self):
        with pytest.raises(ValueError):
            self.stack.peek()

    def test_peek(self):
        self.stack.push(10)
        assert self.stack.peek().val == 10


class TestStackEmpty:
    def setup_method(self):
        self.stack = Stack()

    def test_empty(self):
        assert self.stack.empty() is True

    def test_not_empty(self):
        self.stack.push(1)
        assert self.stack.empty() is False


class TestStackSize:
    def setup_method(self):
        self.stack = Stack()

    def test_size_when_stack_is_empty(self):
        assert self.stack.size() == 0


class TestStackPop:
    def setup_method(self):
        self.stack = Stack()

    def test_pop_with_empty(self):
        with pytest.raises(ValueError):
            self.stack.pop()

    def test_pop(self):
        for i in range(5):
            self.stack.push(i)

        assert self.stack.pop().val == 4
        assert self.stack.size() == 4
