# tests/test_deque.py
import pytest
from random import randint
from src.node import DoublyLinkedList
from src.deque import Deque


class TestDoublyLinkedList:
    def setup_method(self):
        self.node = DoublyLinkedList(10)

    def test_init(self):
        assert self.node.val == 10
        assert self.node.next is None
        assert self.node.prev is None


class TestDequeUtil:
    def setup_method(self):
        self.deq = Deque()
        self.nums = range(0, 1000)
        self.head = self.nums[0]

    def test_deque_stack(self):
        for num in self.nums:
            self.deq.push(num)
            assert self.deq.front() == self.head
            assert self.deq.back() == num

        assert len(self.deq) == len(self.nums)

    def test_deque_queue(self):
        for num in self.nums:
            self.deq.push_front(num)
            assert self.deq.front() == num
            assert self.deq.back() == self.head

        assert len(self.deq) == len(self.nums)


class TestDequeStack:
    def setup_method(self):
        self.deq = Deque()

    def test_push(self):
        assert len(self.deq) == 0

        for num in [1, 2, 3, 4, 5]:
            self.deq.push(num)
            assert self.deq.back() == num

        assert len(self.deq) == 5

    def test_pop(self):
        for num in [5, 4, 3, 2, 1]:
            self.deq.push(num)

        assert self.deq.pop().val == 1
        assert self.deq.pop().val == 2
        assert self.deq.pop().val == 3
        assert self.deq.pop().val == 4
        assert self.deq.pop().val == 5
        assert len(self.deq) == 0


class TestDequeQueue:
    def setup_method(self):
        self.deq = Deque()

    def test_queue(self):

        for num in [1, 2, 3, 4, 5]:
            self.deq.push_front(num)

        assert len(self.deq) == 5
        assert self.deq.pop_front().val == 5
        assert self.deq.pop_front().val == 4
        assert self.deq.pop_front().val == 3
        assert self.deq.pop_front().val == 2
        assert self.deq.pop_front().val == 1
        assert len(self.deq) == 0


class TestDequeMix:
    def setup_method(self):
        self.deq = Deque()
        self.nums = [randint(1, 1000) for _ in range(100)]

    def test_push_and_pop_front(self):
        for num in self.nums:
            self.deq.push(num)

        assert self.deq.front() == self.nums[0]
        assert self.deq.back() == self.nums[-1]
        assert len(self.deq) == len(self.nums)

        for num in self.nums:
            assert self.deq.pop_front().val == num

        assert len(self.deq) == 0

    def test_push_front_and_pop(self):
        for num in self.nums:
            self.deq.push_front(num)

        assert self.deq.front() == self.nums[-1]
        assert self.deq.back() == self.nums[0]
        assert len(self.deq) == len(self.nums)

        for num in self.nums:
            assert self.deq.pop().val == num

        assert len(self.deq) == 0


class TestDequeRaises:
    def setup_method(self):
        self.deq = Deque()

    def test_front_raises(self):
        with pytest.raises(ValueError):
            self.deq.front()

    def test_back_raises(self):
        with pytest.raises(ValueError):
            self.deq.back()

    def test_pop_raises(self):
        with pytest.raises(ValueError):
            self.deq.pop()

    def test_pop_front_raises(self):
        with pytest.raises(ValueError):
            self.deq.pop_front()
