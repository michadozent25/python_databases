import pytest

from functions import max1, max2, sum, div

def test_max1():
     assert max1(1,2) == 2 


def test_sum():
     assert sum(1,2) == 3

def test_div():
     assert div(1,2) == 0.5
def test_div_exception():
    with pytest.raises(ZeroDivisionError):
        div(1,0)

def test_max2():
     assert max2([1,3,2])  == 3

def test_max2_empty_list():
     with pytest.raises(ValueError, match="List must not be empty!"):
          max2([])






