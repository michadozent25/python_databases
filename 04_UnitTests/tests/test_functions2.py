import pytest
from functions import max1, max2, sum, div


@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 2),
    (5, -1, 5),
    (-3, -7, -3),
    (0, 0, 0)
])
def test_max1(a, b, expected):
    assert max1(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
    (2.5, 3.5, 6.0)
])
def test_sum(a, b, expected):
    assert sum(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 0.5),
    (10, 5, 2),
    (-4, 2, -2),
    (9, 3, 3)
])
def test_div(a, b, expected):
    assert div(a, b) == expected


def test_div_exception():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)


@pytest.mark.parametrize("values,expected", [
    ([1, 3, 2], 3),
    ([-1, -5, -2], -1),
    ([10], 10),
    ([0, 0, 0], 0)
])
def test_max2(values, expected):
    assert max2(values) == expected


def test_max2_empty_list():
    with pytest.raises(ValueError, match="List must not be empty!"):
        max2([])



