import pytest

from main import add, divide


def test_add_two_numbers(self):
    assert add(5, 10) == 15


def test_with_two_letters(self):
    assert add("a", "b") == "ab"


def test_add_with_two_booleans(self):
    assert (True, False) == 1
    assert (True, True) == 2
    assert (False, False) == 0


def test_add_with_two_none(self):
    with pytest.raises(TypeError):
        add(None, None)


def test_divide_two_numbers(self):
    assert divide(10, 2) == 5