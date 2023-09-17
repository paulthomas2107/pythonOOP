import pytest
import DoubleIt


def test_doubleIt(self):
    assert DoubleIt.doubleIt(10) == 20


def test_tripleIt(self):
    assert DoubleIt.tripleIt(30) == 90


def test_double_type(self):
    with pytest.raises(TypeError):
        DoubleIt.doubleIt('hello')