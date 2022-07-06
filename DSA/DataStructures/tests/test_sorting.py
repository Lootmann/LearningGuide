# tests/test_sorting.py
# import pytest
from random import randint
from src.sorting import merge


class TestMergeSort:
    def setup_method(self):
        self.small = [randint(1, 100000) for _ in range(1000)]
        self.middle = [randint(1, 1000000) for _ in range(10000)]
        self.huge = [randint(1, 10000000) for _ in range(10000)]

    def test_sorting_small_size(self):
        want = sorted(self.small)
        got = merge(self.small)
        assert want == got

    def test_sorting_middle(self):
        want = sorted(self.middle)
        got = merge(self.middle)
        assert want == got

    # @pytest.mark.skip("huge takes too much time")
    def test_sorting_huge(self):
        want = sorted(self.huge)
        got = merge(self.huge)
        assert want == got
