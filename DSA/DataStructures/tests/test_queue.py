# tests/test_queue.py
import pytest
from src.queue import Queue


class TestQueue:
    def setup_method(self):
        self.q = Queue()

    def test_init(self):
        assert self.q.size == 0
        assert self.q.empty() is True

    def test_enqueue(self):
        self.q.enqueue(10)
        assert self.q.size == 1
        assert self.q.peek == 10

        self.q.enqueue(8)
        assert self.q.size == 2
        assert self.q.peek == 10

    def test_dequeue(self):
        for num in [1, 2, 3]:
            self.q.enqueue(num)
            assert self.q.size == num
            assert self.q.peek == 1

        for num in [1, 2, 3]:
            assert self.q.dequeue().val == num
            assert self.q.size == 3 - num

        assert self.q.size == 0

    def test_queue_many(self):
        for num in range(1, 10000 + 1):
            self.q.enqueue(num)
            assert self.q.size == num

        assert self.q.peek == 1
        assert self.q.size == 10000


class TestQueueRaises:
    def setup_method(self):
        self.q = Queue()

    def test_peek_with_empty(self):
        with pytest.raises(ValueError):
            _ = self.q.peek

    def test_dequeue_with_empty(self):
        for num in range(10):
            self.q.enqueue(num)

        for num in range(10):
            self.q.dequeue()

        assert self.q.size == 0

        with pytest.raises(ValueError):
            self.q.dequeue()
