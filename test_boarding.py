import boarding
import pytest

def test_boarding_check_1():
    result=boarding.boarding_check(3)
    assert result==1

def test_boarding_check_2():
    result=boarding.boarding_check(-1)
    assert result==-1
