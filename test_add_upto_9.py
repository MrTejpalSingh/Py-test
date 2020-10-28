import add_upto_9
import pytest

@pytest.mark.Add9
def test_check_registration_number_1():
    assert add_upto_9.check_registration_number(9999) == True

@pytest.mark.Add9    
def test_check_registration_number_2():
    assert add_upto_9.check_registration_number(9099) == True

@pytest.mark.NotAdd9
def test_check_registration_number_3():
    assert add_upto_9.check_registration_number(1009) == False

@pytest.mark.NotAdd9
def test_check_registration_number_4():
    assert add_upto_9.check_registration_number(3256) == False

@pytest.mark.InavlidInput
def test_check_registration_number_5():
    assert add_upto_9.check_registration_number(125) == False

@pytest.mark.InavlidInput
def test_check_registration_number_6():
    assert add_upto_9.check_registration_number(12345) == False
