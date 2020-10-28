import sum_of_digits
import pytest

@pytest.mark.three_digits
def test_add_digits_three_digits_1():
    assert sum_of_digits.add_digits(568) == 18

@pytest.mark.three_digits
def test_add_digits_three_digits_2():
    assert sum_of_digits.add_digits(235) == 10

@pytest.mark.two_digits
def test_add_digits_two_digits_1():
    assert sum_of_digits.add_digits(23) == 5

@pytest.mark.two_digits
def test_add_digits_two_digits_2():
    assert sum_of_digits.add_digits(12) == 3
