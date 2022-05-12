"""src/test_fixed_array.py
"""


import pytest
from src.custom_errors import RangeError
from src.fixed_array import FixedArray


class TestInitFixedArray:
    def test_init_default_size(self):
        array = FixedArray()
        assert array.size == 10

    def test_init_with_size(self):
        array = FixedArray(20)
        assert array.size == 20

    def test_init_with_wrong_type_args(self):
        with pytest.raises(TypeError):
            FixedArray(1.0)

    def test_init_args_negative_size(self):
        with pytest.raises(RangeError):
            FixedArray(-10)

    def test_init_incorrect_type(self):
        with pytest.raises(TypeError):
            FixedArray(_type=dict)

    def test_repr_int(self):
        array = FixedArray(size=3)
        assert "0, 0, 0" == str(array)

    def test_repr_float(self):
        array = FixedArray(size=3, _type=float)
        assert "0.0, 0.0, 0.0" == str(array)


class TestInitFixedArrayWithType:
    def test_init_type_int(self):
        array = FixedArray(_type=int)
        assert array[0] == 0

    def test_init_type_float(self):
        array = FixedArray(_type=float)
        assert array[0] == 0.0

    def test_init_type_str(self):
        array = FixedArray(_type=str)
        assert array[0] == ""

    def test_init_type_str(self):
        array = FixedArray(_type=bool)
        assert array[0] == None

    def test_init_type_wrong_type(self):
        with pytest.raises(TypeError):
            FixedArray(_type=list)


class TestFixedArrayLength:
    def test_size(self):
        array = FixedArray()
        assert len(array) == 10


class TestAccessFixedArray:
    def test_outbound_lower(self):
        array = FixedArray()
        with pytest.raises(IndexError):
            array[-1]

    def test_outbound_upper(self):
        array = FixedArray()
        with pytest.raises(IndexError):
            array[10]

    def test_not_outbound(self):
        array = FixedArray()
        assert array[0] == 0


class TestFixedArrayWithStr:
    def test_init(self):
        arr = FixedArray(size=10, _type=str)
        assert arr[0] == ""
