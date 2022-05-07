import pytest

from validate import validate


class TestValidate:
    @pytest.mark.parametrize("text", ["a", "a" * 50, "a" * 100])
    def test_validate(self, text: str):
        assert validate(text)

    @pytest.mark.parametrize("invalid_text", ["", "a" * 101])
    def test_invalid(self, invalid_text: str):
        assert not validate(invalid_text)
